"""Executable ST-005 compatibility corpus and ST-006 migration specimens."""

import copy
import json
import unittest
from collections.abc import MutableMapping
from dataclasses import FrozenInstanceError, replace
from pathlib import Path
from typing import cast
from unittest.mock import patch

from spinaltap.contract_kernel import (
    ContractRef,
    DeltaPacket,
    GateRef,
    PromotionState,
    ProofRecord,
    RefusalCode,
    RefusalState,
    SignalBundle,
    TimePacket,
    contract_gate,
)
from spinaltap.contract_validation import (
    CONTRACT_SCHEMAS,
    LEGACY_ADAPTER_ID,
    LEGACY_BASELINE_REVISION,
    ContractIdentity,
    ContractValidationError,
    DecodedContract,
    migrate_legacy_contract,
    parse_contract,
    parse_contract_envelope,
)
from spinaltap.time_packet import TimePacketPump, require_solver_step
from spinaltap.vertebra_delta import VertebraDeltaWorker


ROOT = Path(__file__).resolve().parents[1]
SPEC = json.loads((ROOT / "docs/examples/contract_identity.json").read_text())
MIGRATIONS = json.loads(
    (ROOT / "tests/fixtures/legacy_contract_migrations.json").read_text()
)


def envelope(contract: ContractRef):
    return copy.deepcopy(SPEC["accepted_envelopes"][contract.value])


def legacy(contract: ContractRef):
    return copy.deepcopy(next(
        case["legacy_payload"] for case in MIGRATIONS["cases"]
        if case["id"] == contract.value
    ))


class VersionedIngressTests(unittest.TestCase):
    def assert_invalid(self, contract, value, field, owner=None):
        with self.assertRaises(ContractValidationError) as caught:
            parse_contract_envelope(contract, value)
        error = caught.exception
        self.assertEqual(error.field, field)
        self.assertEqual(error.refusal.contract, owner or contract)
        self.assertEqual(error.refusal.gate, contract_gate(owner or contract))
        self.assertEqual(error.refusal.code, RefusalCode.INVALID_PAYLOAD)
        self.assertEqual(error.refusal.promotion_state, PromotionState.BLOCKED)

    def test_all_six_specified_envelopes_decode_with_explicit_identity(self):
        self.assertEqual(set(SPEC["accepted_envelopes"]), set(ContractRef))
        for contract in ContractRef:
            with self.subTest(contract=contract):
                decoded = parse_contract_envelope(contract, envelope(contract))
                self.assertEqual(decoded.identity, ContractIdentity(contract, 1))
                self.assertEqual(decoded.record, parse_contract(contract, legacy(contract)))

    def test_all_eighteen_specified_refusals_match_wire_path_and_owner(self):
        self.assertEqual(len(SPEC["refusal_examples"]), 18)
        for case in SPEC["refusal_examples"]:
            with self.subTest(case=case["id"]):
                expected = case["specified_outcome"]
                self.assertEqual(expected["status"], "refused")
                self.assertEqual(expected["code"], "invalid_payload")
                self.assertEqual(expected["promotion_state"], "blocked")
                self.assert_invalid(
                    ContractRef(case["expected_contract"]), case["envelope"],
                    expected["field"], ContractRef(expected["contract"]),
                )

    def test_invalid_expected_contract_is_a_programmer_error(self):
        for invalid in ("DC02", "DC99", None, True, 2):
            with self.subTest(value=invalid), self.assertRaises(TypeError):
                parse_contract_envelope(cast(ContractRef, invalid), envelope(ContractRef.DC02))

    def test_every_envelope_field_is_required_for_every_contract(self):
        for contract in ContractRef:
            for field in ("contract", "schema_revision", "payload"):
                value = envelope(contract)
                del value[field]
                with self.subTest(contract=contract, field=field):
                    self.assert_invalid(contract, value, f"{contract}.{field}")

    def test_every_body_field_is_required_including_nullable_fields(self):
        for contract in ContractRef:
            for field in SPEC["required_body_fields"][contract]:
                value = envelope(contract)
                del value["payload"][field]
                with self.subTest(contract=contract, field=field):
                    self.assert_invalid(contract, value, f"{contract}.payload.{field}")

    def test_closed_fields_and_nonblank_string_mapping_keys(self):
        for contract in ContractRef:
            for target, path in (("header", str(contract)), ("body", f"{contract}.payload")):
                for key in ("extra", "", "  ", 3, None):
                    value = envelope(contract)
                    mapping = value if target == "header" else value["payload"]
                    mapping[key] = 1
                    with self.subTest(contract=contract, target=target, key=key):
                        self.assert_invalid(
                            contract, value, path + (".extra" if key == "extra" else "")
                        )

    def test_nonmapping_headers_and_bodies_are_refused_including_domain_records(self):
        for contract in ContractRef:
            record = parse_contract(contract, legacy(contract))
            for invalid in (record, None, [], True, 1, "body"):
                with self.subTest(contract=contract, invalid=type(invalid).__name__):
                    self.assert_invalid(contract, invalid, str(contract))
                    value = envelope(contract)
                    value["payload"] = invalid
                    self.assert_invalid(contract, value, f"{contract}.payload")

    def test_header_validation_order_precedes_body_validation(self):
        self.assert_invalid(ContractRef.DC02, {"extra": 1}, "DC02.contract")
        value = {"contract": "DC99", "schema_revision": 999, "payload": None, "extra": 1}
        self.assert_invalid(ContractRef.DC02, value, "DC02.extra")
        del value["extra"]
        self.assert_invalid(ContractRef.DC02, value, "DC02.contract")
        value["contract"] = "DC02"
        self.assert_invalid(ContractRef.DC02, value, "DC02.schema_revision")

    def test_identity_is_exact_and_case_sensitive_for_all_contracts(self):
        for contract in ContractRef:
            for name in (contract.value.lower(), f" {contract}", "DC99", None, True):
                value = envelope(contract)
                value["contract"] = name
                self.assert_invalid(contract, value, f"{contract}.contract")
            for revision in (None, True, False, 1.0, "1", 0, -1, 2, 999):
                value = envelope(contract)
                value["schema_revision"] = revision
                self.assert_invalid(contract, value, f"{contract}.schema_revision")

    def test_all_numeric_fields_refuse_booleans_nonfinite_strings_and_overflow(self):
        numeric = {
            ContractRef.DC01: (
                "source_authority", "claim_fit", "originality_distance",
                "validation_reach", "influence_weight",
            ),
            ContractRef.DC02: (
                "elapsed_time", "fixed_packet_size", "accumulator_remainder",
                "interpolation_state",
            ),
        }
        for contract, names in numeric.items():
            for field in names:
                invalids = (
                    True, False, "0.5", float("nan"), float("inf"),
                    -float("inf"), -0.1, 10**1000,
                )
                for invalid in invalids:
                    value = envelope(contract)
                    value["payload"][field] = invalid
                    with self.subTest(contract=contract, field=field, value=repr(invalid)[:30]):
                        self.assert_invalid(contract, value, f"{contract}.payload.{field}")

    def test_numeric_boundaries_counts_and_valid_backlog_remain_supported(self):
        for count in (0, 1, 2):
            value = envelope(ContractRef.DC02)
            value["payload"].update(
                packet_count=count, accumulator_remainder=0.1, interpolation_state=1
            )
            decoded = parse_contract_envelope(ContractRef.DC02, value)
            self.assertIsInstance(decoded.record, TimePacket)
        invalids = (
            ("packet_count", True), ("packet_count", 1.0), ("packet_count", -1),
            ("fixed_packet_size", 0), ("interpolation_state", 1.1),
        )
        for field, invalid in invalids:
            value = envelope(ContractRef.DC02)
            value["payload"][field] = invalid
            self.assert_invalid(ContractRef.DC02, value, f"DC02.payload.{field}")
        for field in (
            "source_authority", "claim_fit", "originality_distance",
            "validation_reach", "influence_weight",
        ):
            value = envelope(ContractRef.DC01)
            for boundary in (0, 1):
                value["payload"][field] = boundary
                parse_contract_envelope(ContractRef.DC01, value)
            value["payload"][field] = 1.1
            self.assert_invalid(ContractRef.DC01, value, f"DC01.payload.{field}")

    def test_second_signal_nested_error_retains_full_wire_path_and_child_owner(self):
        value = envelope(ContractRef.DC03)
        signals = value["payload"]["ordered_signal_bundle"]
        signals.append(copy.deepcopy(signals[0]))
        signals[1]["payload"]["time_packet"]["payload"]["packet_count"] = True
        self.assert_invalid(
            ContractRef.DC03, value,
            "DC03.payload.ordered_signal_bundle[1].payload.time_packet.payload.packet_count",
            ContractRef.DC02,
        )

    def test_nested_identity_mismatch_and_bare_dataclass_are_never_unwrapped(self):
        for child, field in (
            ({"contract": "DC04", "schema_revision": 1, "payload": {}}, ".contract"),
            (parse_contract(ContractRef.DC02, legacy(ContractRef.DC02)), ""),
        ):
            value = envelope(ContractRef.DC04)
            value["payload"]["time_packet"] = child
            self.assert_invalid(
                ContractRef.DC04, value, "DC04.payload.time_packet" + field,
                ContractRef.DC02,
            )
        value = envelope(ContractRef.DC03)
        value["payload"]["ordered_signal_bundle"] = [legacy(ContractRef.DC04)]
        self.assert_invalid(
            ContractRef.DC03, value,
            "DC03.payload.ordered_signal_bundle[0].contract", ContractRef.DC04,
        )

    def test_parent_pin_refuses_a_child_even_when_that_revision_is_registered(self):
        # Synthetic future registry entry isolates pin enforcement from lookup.
        future = ContractIdentity(ContractRef.DC02, 2)
        schemas = dict(CONTRACT_SCHEMAS)
        schemas[future] = replace(schemas[ContractIdentity(ContractRef.DC02, 1)], identity=future)
        child = envelope(ContractRef.DC02)
        child["schema_revision"] = 2
        with patch("spinaltap.contract_validation.CONTRACT_SCHEMAS", schemas):
            self.assertEqual(parse_contract_envelope(ContractRef.DC02, child).identity, future)
            value = envelope(ContractRef.DC04)
            value["payload"]["time_packet"] = child
            self.assert_invalid(
                ContractRef.DC04, value, "DC04.payload.time_packet.schema_revision",
                ContractRef.DC02,
            )

    def test_registry_is_closed_immutable_and_records_transitive_pins(self):
        self.assertEqual(
            set(CONTRACT_SCHEMAS), {ContractIdentity(c, 1) for c in ContractRef}
        )
        for identity, schema in CONTRACT_SCHEMAS.items():
            self.assertEqual(identity, schema.identity)
            self.assertEqual(
                schema.body_fields, tuple(SPEC["required_body_fields"][identity.contract])
            )
            self.assertTrue((ROOT / schema.document_ref).is_file())
            with self.assertRaises(FrozenInstanceError):
                setattr(schema, "body_fields", ())
        dc03 = CONTRACT_SCHEMAS[ContractIdentity(ContractRef.DC03, 1)]
        self.assertEqual(dc03.nested_contracts, (ContractIdentity(ContractRef.DC04, 1),))
        dc04 = CONTRACT_SCHEMAS[dc03.nested_contracts[0]]
        self.assertEqual(dc04.nested_contracts, (ContractIdentity(ContractRef.DC02, 1),))
        self.assertEqual(
            CONTRACT_SCHEMAS[ContractIdentity(ContractRef.DC06, 1)].nested_contracts, ()
        )
        with self.assertRaises(TypeError):
            cast(MutableMapping, CONTRACT_SCHEMAS)[ContractIdentity(ContractRef.DC02, 2)] = dc04

    def test_helper_codes_and_enum_vocabularies_are_frozen(self):
        schema = CONTRACT_SCHEMAS[ContractIdentity(ContractRef.DC04, 1)]
        codes = {
            "invalid_payload", "constraint_violation", "validation_failed",
            "write_conflict", "hidden_influence", "raw_dt", "direct_global_mutation",
            "outside_local_slice", "vague_style", "missing_specimen", "missing_failure_path",
        }
        self.assertEqual(schema.enum_values[RefusalCode], codes)
        self.assertEqual(
            schema.enum_values[PromotionState], {"candidate", "blocked", "implementation_ready"}
        )
        self.assertEqual(
            schema.enum_values[ContractRef], {"DC01", "DC02", "DC03", "DC04", "DC05", "DC06"}
        )
        self.assertEqual(
            schema.enum_values[GateRef], {"VG01", "VG02", "VG03", "VG04", "VG05", "VG06"}
        )
        with self.assertRaises(TypeError):
            cast(MutableMapping, schema.enum_values)[RefusalCode] = frozenset()
        for code in codes:
            value = envelope(ContractRef.DC04)
            value["payload"]["residual_risk"] = RefusalState(
                ContractRef.DC04, GateRef.VG04, RefusalCode(code), "refused"
            )
            parse_contract_envelope(ContractRef.DC04, value)

    def test_refusal_helper_is_revalidated_and_all_fields_remain_required(self):
        risk = {
            "contract": "DC04", "gate": "VG04", "code": "outside_local_slice",
            "reason": "z outside slice", "promotion_state": "blocked",
        }
        for field in risk:
            value = envelope(ContractRef.DC04)
            value["payload"]["residual_risk"] = {
                key: item for key, item in risk.items() if key != field
            }
            self.assert_invalid(ContractRef.DC04, value, f"DC04.payload.residual_risk.{field}")
        for field, invalid in (
            ("gate", "VG03"), ("promotion_state", "candidate"), ("code", "invented"),
            ("reason", "  "), ("extra", 1),
        ):
            value = envelope(ContractRef.DC04)
            value["payload"]["residual_risk"] = {**risk, field: invalid}
            self.assert_invalid(ContractRef.DC04, value, f"DC04.payload.residual_risk.{field}")
        value = envelope(ContractRef.DC04)
        value["payload"]["residual_risk"] = RefusalState(
            ContractRef.DC04, GateRef.VG03, RefusalCode.OUTSIDE_LOCAL_SLICE, "invalid gate"
        )
        self.assert_invalid(ContractRef.DC04, value, "DC04.payload.residual_risk.gate")

    def test_ordered_tuple_and_empty_bundle_preserve_the_declared_item_type(self):
        value = envelope(ContractRef.DC03)
        first = value["payload"]["ordered_signal_bundle"][0]
        second = copy.deepcopy(first)
        second["payload"]["bounded_delta"]["x"] = 2
        for signals in ((), (first, second)):
            value["payload"]["ordered_signal_bundle"] = signals
            decoded = parse_contract_envelope(ContractRef.DC03, value)
            assert isinstance(decoded.record, SignalBundle)
            self.assertEqual(
                [delta.bounded_delta["x"] for delta in decoded.record.ordered_signal_bundle],
                [] if not signals else [1, 2],
            )
        for invalid in ({}, {1, 2}, None, "signal"):
            value["payload"]["ordered_signal_bundle"] = invalid
            self.assert_invalid(ContractRef.DC03, value, "DC03.payload.ordered_signal_bundle")

    def test_shallow_snapshots_preserve_opaque_aliases_without_copying(self):
        opaque = []
        value = envelope(ContractRef.DC04)
        state = {"x": opaque}
        value["payload"]["local_state_slice"] = state
        decoded = parse_contract_envelope(ContractRef.DC04, value)
        assert isinstance(decoded.record, DeltaPacket)
        state["new"] = []
        self.assertNotIn("new", decoded.record.local_state_slice)
        self.assertIs(decoded.record.local_state_slice["x"], opaque)
        opaque.append(1)
        self.assertEqual(decoded.record.local_state_slice["x"], [1])
        with self.assertRaises(TypeError):
            cast(MutableMapping, decoded.record.local_state_slice)["x"] = 3
        for wrapper, name in ((decoded, "record"), (decoded.identity, "schema_revision")):
            with self.assertRaises(FrozenInstanceError):
                setattr(wrapper, name, None)

    def test_trusted_constructors_are_not_validation_proofs(self):
        packet = TimePacket(float("nan"), 0, -1, 0, 2, None)
        decoded = DecodedContract(ContractIdentity(ContractRef.DC02, 0), packet)
        self.assertEqual(decoded.identity.schema_revision, 0)
        value = envelope(ContractRef.DC02)
        value["payload"] = packet
        self.assert_invalid(ContractRef.DC02, value, "DC02.payload")

    def test_no_implicit_fallback_between_versioned_and_legacy_apis(self):
        for contract in ContractRef:
            self.assert_invalid(contract, legacy(contract), f"{contract}.contract")
            with self.assertRaises(ContractValidationError):
                parse_contract(contract, envelope(contract))

    def test_domain_timing_and_delta_refusals_survive_successful_ingress(self):
        decoded = parse_contract_envelope(ContractRef.DC02, envelope(ContractRef.DC02))
        assert isinstance(decoded.record, TimePacket)
        with self.assertRaises(ContractValidationError):
            require_solver_step(decoded.record)
        step = TimePacketPump(0.016, 4).solver_steps(decoded.record)[0]
        for proposal, code in (
            ({"x": 1}, None), ({"x": 3}, RefusalCode.CONSTRAINT_VIOLATION),
            ({"z": 1}, RefusalCode.OUTSIDE_LOCAL_SLICE),
        ):
            delta = VertebraDeltaWorker({"x"}).propose(
                local_state_slice={"x": 4}, constraint_set={"max_delta": 2},
                time_packet=step, proposed_delta=proposal,
            )
            self.assertEqual(delta.residual_risk.code if delta.residual_risk else None, code)


class LegacyMigrationTests(unittest.TestCase):
    def migrate(
        self, contract, payload, revision: object = LEGACY_BASELINE_REVISION,
        source: object = "fixture:legacy",
    ):
        # Deliberately exercise untrusted runtime metadata despite annotations.
        return migrate_legacy_contract(
            contract, payload, cast(str, revision), cast(str, source)
        )

    def test_all_eight_fixtures_migrate_mappings_and_dataclasses_with_exact_receipts(self):
        self.assertEqual(len(MIGRATIONS["cases"]), 8)
        self.assertEqual(MIGRATIONS["source_revision"], LEGACY_BASELINE_REVISION)
        self.assertEqual(MIGRATIONS["adapter_id"], LEGACY_ADAPTER_ID)
        for case in MIGRATIONS["cases"]:
            contract = ContractRef(case["contract"])
            original = copy.deepcopy(case["legacy_payload"])
            expected = parse_contract_envelope(contract, case["expected_envelope"])
            payloads = (
                case["legacy_payload"], parse_contract(contract, case["legacy_payload"])
            )
            for payload in payloads:
                with self.subTest(case=case["id"], kind=type(payload).__name__):
                    migrated = self.migrate(
                        contract, payload, MIGRATIONS["source_revision"], case["source_ref"]
                    )
                    self.assertEqual(migrated.decoded, expected)
                    self.assertEqual(migrated.decoded.record, parse_contract(contract, payload))
                    receipt = migrated.receipt
                    self.assertEqual(receipt.source_ref, case["source_ref"])
                    self.assertEqual(receipt.source_revision, MIGRATIONS["source_revision"])
                    self.assertEqual(
                        receipt.source_identity.contract, case["source_identity"]["contract"]
                    )
                    self.assertEqual(receipt.source_identity.schema_revision, "legacy-0")
                    self.assertEqual(
                        receipt.target_identity,
                        ContractIdentity(contract, case["target_identity"]["schema_revision"]),
                    )
                    self.assertEqual(receipt.adapter_id, MIGRATIONS["adapter_id"])
                    self.assertEqual(case["legacy_payload"], original)

    def test_receipt_and_result_are_immutable_attribution_not_execution_evidence(self):
        result = self.migrate(ContractRef.DC02, legacy(ContractRef.DC02))
        self.assertEqual(set(vars(result.receipt)), {
            "source_ref", "source_revision", "source_identity", "target_identity", "adapter_id",
        })
        for obj, name in (
            (result, "decoded"), (result.receipt, "source_ref"),
            (result.receipt.source_identity, "schema_revision"),
        ):
            with self.assertRaises(FrozenInstanceError):
                setattr(obj, name, None)

    def test_unregistered_baselines_and_missing_attribution_fail_closed(self):
        for field, invalids in (
            ("source_revision", (None, "", "legacy-0", "d7c789b", "current", True)),
            ("source_ref", (None, "", "  ", 1)),
        ):
            for invalid in invalids:
                kwargs = {"revision" if field == "source_revision" else "source": invalid}
                with (
                    self.subTest(field=field, invalid=invalid),
                    self.assertRaises(ContractValidationError) as caught,
                ):
                    self.migrate(ContractRef.DC02, legacy(ContractRef.DC02), **kwargs)
                self.assertEqual(caught.exception.field, f"DC02.{field}")
                self.assertEqual(caught.exception.refusal.code, RefusalCode.INVALID_PAYLOAD)
                self.assertEqual(caught.exception.refusal.promotion_state, PromotionState.BLOCKED)
        with self.assertRaises(TypeError):
            self.migrate("DC02", legacy(ContractRef.DC02))

    def test_missing_nullable_fields_are_not_filled_by_migration(self):
        for contract in ContractRef:
            value = legacy(contract)
            for field in value:
                incomplete = {key: item for key, item in value.items() if key != field}
                with (
                    self.subTest(contract=contract, field=field),
                    self.assertRaises(ContractValidationError) as caught,
                ):
                    self.migrate(contract, incomplete)
                self.assertEqual(caught.exception.field, f"{contract}.{field}")

    def test_invalid_nested_dataclass_retains_legacy_error_path(self):
        value = legacy(ContractRef.DC03)
        packet = parse_contract(ContractRef.DC02, legacy(ContractRef.DC02))
        assert isinstance(packet, TimePacket)
        value["ordered_signal_bundle"][0]["time_packet"] = replace(
            packet, fixed_packet_size=float("nan")
        )
        with self.assertRaises(ContractValidationError) as caught:
            self.migrate(ContractRef.DC03, value)
        self.assertEqual(
            caught.exception.field,
            "DC03.ordered_signal_bundle[0].time_packet.fixed_packet_size",
        )
        self.assertEqual(caught.exception.refusal.contract, ContractRef.DC02)

    def test_versioned_inputs_do_not_trigger_a_second_implicit_migration(self):
        for contract in ContractRef:
            with self.subTest(contract=contract), self.assertRaises(ContractValidationError):
                self.migrate(contract, envelope(contract))

    def test_migration_preserves_opaque_identity_without_deepcopy_or_input_mutation(self):
        class Opaque:
            def __deepcopy__(self, memo):
                raise AssertionError("opaque values must not be copied")

        opaque = Opaque()
        value = legacy(ContractRef.DC04)
        value["local_state_slice"] = {"x": opaque}
        original_time = value["time_packet"]
        migrated = self.migrate(ContractRef.DC04, value)
        assert isinstance(migrated.decoded.record, DeltaPacket)
        self.assertIs(migrated.decoded.record.local_state_slice["x"], opaque)
        self.assertIs(value["time_packet"], original_time)
        self.assertNotIn("schema_revision", original_time)
        value["local_state_slice"]["new"] = 1
        self.assertNotIn("new", migrated.decoded.record.local_state_slice)

    def test_proof_promotion_and_free_evidence_tier_are_preserved_without_subject_identity(self):
        for state in PromotionState:
            value = legacy(ContractRef.DC06)
            value.update(
                promotion_state=state.value, evidence_tier="caller-declared",
                specimen_plan="", failure_path="",
            )
            migrated = self.migrate(ContractRef.DC06, value)
            assert isinstance(migrated.decoded.record, ProofRecord)
            self.assertEqual(migrated.decoded.record.promotion_state, state)
            self.assertEqual(migrated.decoded.record.evidence_tier, "caller-declared")
            self.assertEqual(migrated.decoded.record.contract_ref, ContractRef.DC03)
            self.assertEqual(migrated.receipt.target_identity.contract, ContractRef.DC06)
            self.assertFalse(hasattr(migrated.receipt, "subject_identity"))


if __name__ == "__main__":
    unittest.main()
