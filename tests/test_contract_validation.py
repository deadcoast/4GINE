import unittest
from collections.abc import MutableMapping
from dataclasses import replace
from typing import cast

from spinaltap.context_weight import ContextWeightGovernor, GovernorDecision
from spinaltap.contract_kernel import (
    ContractRef,
    DeltaPacket,
    GateRef,
    PromotionState,
    ProofRecord,
    RefusalCode,
    RefusalState,
    SignalBundle,
    SourceClaim,
    SpecimenHook,
    StyleLimits,
    TimePacket,
    contract_gate,
)
from spinaltap.contract_validation import ContractValidationError, parse_contract
from spinaltap.reconciliation import SpinalReconciliationHarness
from spinaltap.soft_proof import SoftProofLab
from spinaltap.style_surface import StyleConstraintSurface
from spinaltap.time_packet import TimePacketPump
from spinaltap.vertebra_delta import VertebraDeltaWorker


def time_payload() -> dict[str, object]:
    return {
        "elapsed_time": 0.040,
        "fixed_packet_size": 0.016,
        "packet_count": 2,
        "accumulator_remainder": 0.008,
        "interpolation_state": 0.5,
        "overflow_risk": None,
    }


def delta_payload() -> dict[str, object]:
    return {
        "local_state_slice": {"x": 4},
        "constraint_set": {"max_delta": 2},
        "time_packet": time_payload(),
        "bounded_delta": {"x": 1},
        "residual_risk": None,
    }


def proof_payload() -> dict[str, object]:
    return {
        "claim_ref": "claim:signal-spine-orders-deltas",
        "contract_ref": "DC03",
        "specimen_plan": "run signal spine ordering specimen",
        "failure_path": "fails if direct global mutation is accepted",
        "promotion_state": "candidate",
        "evidence_tier": "unit-specimen",
    }


def payloads() -> dict[ContractRef, dict[str, object]]:
    return {
        ContractRef.DC01: {
            "source_ref": "source:engine-pattern",
            "claim_text": "bounded source influence",
            "source_authority": 0.9,
            "claim_fit": 0.8,
            "originality_distance": 0.7,
            "validation_reach": 0.6,
            "influence_weight": None,
            "risk_flag": None,
            "governor_decision": None,
        },
        ContractRef.DC02: time_payload(),
        ContractRef.DC03: {
            "owner": "vertebra:motion",
            "channel": "motion.delta",
            "ordered_signal_bundle": [delta_payload()],
            "constraint_envelope": {"max_delta": 2},
            "validation_hook": "VG03",
            "residual_risk": None,
        },
        ContractRef.DC04: delta_payload(),
        ContractRef.DC05: {name: "specified_limit" for name in StyleLimits.fields()},
        ContractRef.DC06: proof_payload(),
    }


class ContractValidationTests(unittest.TestCase):
    def assert_invalid(self, contract, payload, field):
        with self.assertRaises(ContractValidationError) as caught:
            parse_contract(contract, payload)
        error = caught.exception
        self.assertEqual(error.field, field)
        self.assertEqual(error.refusal.code, RefusalCode.INVALID_PAYLOAD)
        self.assertEqual(error.refusal.promotion_state, PromotionState.BLOCKED)
        self.assertEqual(error.refusal.gate, contract_gate(error.refusal.contract))
        return error

    def test_all_six_contracts_decode_complete_payloads(self):
        record_types = (
            SourceClaim,
            TimePacket,
            SignalBundle,
            DeltaPacket,
            StyleLimits,
            ProofRecord,
        )
        for (contract, payload), record_type in zip(payloads().items(), record_types):
            with self.subTest(contract=contract):
                record = parse_contract(contract, payload)
                self.assertIsInstance(record, record_type)
                self.assertEqual(parse_contract(contract, record), record)

    def test_nonmapping_inputs_are_refused_for_every_contract(self):
        for contract in ContractRef:
            for payload in (None, [], "record", 3, True):
                with self.subTest(contract=contract, payload=payload):
                    self.assert_invalid(contract, payload, contract.value)

    def test_every_declared_field_is_required_including_nullable_fields(self):
        for contract, payload in payloads().items():
            for field in payload:
                incomplete = dict(payload)
                del incomplete[field]
                with self.subTest(contract=contract, field=field):
                    self.assert_invalid(contract, incomplete, f"{contract}.{field}")

    def test_unknown_fields_are_never_silently_discarded(self):
        for contract, payload in payloads().items():
            with self.subTest(contract=contract):
                self.assert_invalid(
                    contract, {**payload, "typo": 1}, f"{contract}.typo"
                )

    def test_nonstring_or_blank_mapping_keys_are_refused(self):
        for key in (3, None, "", "  "):
            with self.subTest(key=key):
                self.assert_invalid(ContractRef.DC02, {key: "value"}, "DC02")
                payload = {**delta_payload(), "bounded_delta": {key: 1}}
                self.assert_invalid(ContractRef.DC04, payload, "DC04.bounded_delta")

    def test_source_scores_reject_bad_types_nonfinite_and_out_of_range_values(self):
        payload = payloads()[ContractRef.DC01]
        fields = (
            "source_authority",
            "claim_fit",
            "originality_distance",
            "validation_reach",
            "influence_weight",
        )
        for field in fields:
            for value in (True, "0.5", float("nan"), float("inf"), -0.1, 1.1, 10**1000):
                with self.subTest(field=field, value=repr(value)[:40]):
                    self.assert_invalid(
                        ContractRef.DC01, {**payload, field: value}, f"DC01.{field}"
                    )

    def test_source_score_boundaries_and_unscored_claims_remain_supported(self):
        payload = payloads()[ContractRef.DC01]
        for value in (0, 1, 0.5):
            claim = parse_contract(
                ContractRef.DC01, {**payload, "source_authority": value}
            )
            assert isinstance(claim, SourceClaim)
            self.assertEqual(claim.source_authority, value)
            self.assertIsNone(claim.influence_weight)

    def test_time_fields_reject_invalid_values_before_solver_use(self):
        cases = {
            "elapsed_time": (-1, "1", True, float("inf"), float("nan")),
            "fixed_packet_size": (0, -1, False, float("inf"), float("nan")),
            "packet_count": (-1, 1.5, "2", True),
            "accumulator_remainder": (-0.1, "0", False, float("nan")),
            "interpolation_state": (-0.1, 1.1, "0", True, float("nan")),
            "overflow_risk": (False, 1, " "),
        }
        for field, values in cases.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    self.assert_invalid(
                        ContractRef.DC02,
                        {**time_payload(), field: value},
                        f"DC02.{field}",
                    )

    def test_zero_packet_and_backlog_states_remain_supported(self):
        packet = parse_contract(
            ContractRef.DC02,
            {
                **time_payload(),
                "elapsed_time": 0,
                "packet_count": 0,
                "accumulator_remainder": 0,
                "interpolation_state": 0,
            },
        )
        assert isinstance(packet, TimePacket)
        self.assertEqual(packet.packet_count, 0)
        backlog = parse_contract(
            ContractRef.DC02,
            {
                **time_payload(),
                "accumulator_remainder": 0.1,
                "interpolation_state": 1,
                "overflow_risk": "elapsed_time_exceeded_packet_budget",
            },
        )
        assert isinstance(backlog, TimePacket)
        self.assertGreater(backlog.accumulator_remainder, backlog.fixed_packet_size)

    def test_nested_failure_identifies_the_exact_signal_and_owning_contract(self):
        payload = payloads()[ContractRef.DC03]
        bad_delta = {
            **delta_payload(),
            "time_packet": {**time_payload(), "packet_count": True},
        }
        error = self.assert_invalid(
            ContractRef.DC03,
            {
                **payload,
                "ordered_signal_bundle": [delta_payload(), bad_delta],
            },
            "DC03.ordered_signal_bundle[1].time_packet.packet_count",
        )
        self.assertEqual(error.refusal.contract, ContractRef.DC02)

    def test_existing_nested_dataclasses_are_revalidated(self):
        packet = parse_contract(ContractRef.DC02, time_payload())
        assert isinstance(packet, TimePacket)
        malformed = replace(packet, fixed_packet_size=float("nan"))
        self.assert_invalid(
            ContractRef.DC04,
            {
                **delta_payload(),
                "time_packet": malformed,
            },
            "DC04.time_packet.fixed_packet_size",
        )

    def test_signal_order_is_preserved_and_unordered_containers_are_refused(self):
        payload = payloads()[ContractRef.DC03]
        for value in ({"x": 1}, {1, 2}, "delta", None):
            with self.subTest(value=value):
                self.assert_invalid(
                    ContractRef.DC03,
                    {
                        **payload,
                        "ordered_signal_bundle": value,
                    },
                    "DC03.ordered_signal_bundle",
                )
        bundle = parse_contract(
            ContractRef.DC03,
            {
                **payload,
                "ordered_signal_bundle": [
                    delta_payload(),
                    {
                        **delta_payload(),
                        "bounded_delta": {"x": 2},
                    },
                ],
            },
        )
        assert isinstance(bundle, SignalBundle)
        self.assertEqual(
            [delta.bounded_delta["x"] for delta in bundle.ordered_signal_bundle], [1, 2]
        )

    def test_mapping_snapshots_do_not_share_top_level_mutations_with_input(self):
        state = {"x": 4}
        delta = parse_contract(
            ContractRef.DC04, {**delta_payload(), "local_state_slice": state}
        )
        assert isinstance(delta, DeltaPacket)
        state["world.x"] = 9
        self.assertEqual(dict(delta.local_state_slice), {"x": 4})
        with self.assertRaises(TypeError):
            cast(MutableMapping[str, object], delta.local_state_slice)["x"] = 9

    def test_malformed_refusal_cannot_claim_ready_or_mismatched_gate(self):
        risk = {
            "contract": "DC04",
            "gate": "VG04",
            "code": "outside_local_slice",
            "reason": "z outside local slice",
            "promotion_state": "blocked",
        }
        for field, value in (
            ("promotion_state", "implementation_ready"),
            ("gate", "VG03"),
            ("code", "invented"),
        ):
            with self.subTest(field=field):
                self.assert_invalid(
                    ContractRef.DC04,
                    {
                        **delta_payload(),
                        "residual_risk": {**risk, field: value},
                    },
                    f"DC04.residual_risk.{field}",
                )
        delta = parse_contract(
            ContractRef.DC04, {**delta_payload(), "residual_risk": risk}
        )
        assert isinstance(delta, DeltaPacket)
        self.assertIsInstance(delta.residual_risk, RefusalState)

    def test_unknown_enum_and_decision_values_are_refused(self):
        cases = (
            (ContractRef.DC01, "governor_decision", "trust_me"),
            (ContractRef.DC06, "contract_ref", "DC99"),
            (ContractRef.DC06, "promotion_state", "ready_enough"),
        )
        for contract, field, value in cases:
            with self.subTest(field=field):
                self.assert_invalid(
                    contract,
                    {**payloads()[contract], field: value},
                    f"{contract}.{field}",
                )


class MappingIngressTests(unittest.TestCase):
    def test_decoded_time_enters_reconciliation_and_preserves_domain_refusals(self):
        frame = parse_contract(ContractRef.DC02, time_payload())
        assert isinstance(frame, TimePacket)
        packet = TimePacketPump(0.016, 4).solver_steps(frame)[0]
        cases = (
            ("vertebra:motion", {"x": 1}, None),
            ("vertebra:motion", {"z": 1}, RefusalCode.OUTSIDE_LOCAL_SLICE),
            ("", {"x": 1}, RefusalCode.DIRECT_GLOBAL_MUTATION),
        )
        for owner, proposed_delta, expected_code in cases:
            with self.subTest(owner=owner, delta=proposed_delta):
                routed = SpinalReconciliationHarness().reconcile(
                    worker=VertebraDeltaWorker(local_keys={"x"}),
                    owner=owner,
                    channel="motion.delta",
                    local_state_slice={"x": 4},
                    constraint_set={"max_delta": 2},
                    time_packet=packet,
                    proposed_delta=proposed_delta,
                    validation_hook="VG03",
                )
                decoded = parse_contract(ContractRef.DC03, routed)
                assert isinstance(decoded, SignalBundle)
                self.assertEqual(decoded, routed)
                if expected_code is None:
                    self.assertIsNone(decoded.residual_risk)
                    self.assertEqual(
                        decoded.ordered_signal_bundle[0].bounded_delta, {"x": 1}
                    )
                else:
                    self.assertEqual(decoded.ordered_signal_bundle, ())
                    assert decoded.residual_risk is not None
                    self.assertEqual(decoded.residual_risk.code, expected_code)
                    self.assertEqual(
                        decoded.residual_risk.promotion_state, PromotionState.BLOCKED
                    )

    def test_style_mapping_rejects_wrong_types_and_unknown_keys(self):
        payload = payloads()[ContractRef.DC05]
        for profile in (
            None,
            {**payload, "camera_limit": 17},
            {**payload, "extra": "ignored?"},
        ):
            with self.subTest(profile=profile):
                result = StyleConstraintSurface().translate(profile)
                self.assertIsNone(result.limits)
                assert result.refusal is not None
                self.assertEqual(result.refusal.code, RefusalCode.INVALID_PAYLOAD)

    def test_blank_style_limits_keep_the_existing_vague_style_refusal(self):
        result = StyleConstraintSurface().translate(
            {**payloads()[ContractRef.DC05], "camera_limit": "  "}
        )
        assert result.refusal is not None
        self.assertEqual(result.refusal.code, RefusalCode.VAGUE_STYLE)

    def test_proof_hook_rejects_truthy_nontext_and_unknown_fields(self):
        hook = SpecimenHook.for_contract(ContractRef.DC06, GateRef.VG06)
        for payload in (
            None,
            {**proof_payload(), "specimen_plan": 1},
            {**proof_payload(), "failure_path": ["fail"]},
            {**proof_payload(), "extra": True},
        ):
            with self.subTest(payload=payload):
                result = hook.evaluate(payload)
                self.assertEqual(result.promotion_state, PromotionState.BLOCKED)
                assert result.refusal is not None
                self.assertEqual(result.refusal.code, RefusalCode.INVALID_PAYLOAD)

    def test_whitespace_proof_text_cannot_advance(self):
        hook = SpecimenHook.for_contract(ContractRef.DC06, GateRef.VG06)
        for field, code in (
            ("specimen_plan", RefusalCode.MISSING_SPECIMEN),
            ("failure_path", RefusalCode.MISSING_FAILURE_PATH),
        ):
            with self.subTest(field=field):
                result = hook.evaluate({**proof_payload(), field: " \n "})
                self.assertEqual(result.promotion_state, PromotionState.BLOCKED)
                assert result.refusal is not None
                self.assertEqual(result.refusal.code, code)

    def test_other_specimen_hooks_validate_shape_without_promoting(self):
        for contract, payload in payloads().items():
            if contract == ContractRef.DC06:
                continue
            with self.subTest(contract=contract):
                hook = SpecimenHook.for_contract(contract, contract_gate(contract))
                self.assertEqual(
                    hook.evaluate(payload).promotion_state, PromotionState.CANDIDATE
                )
                self.assertEqual(
                    hook.evaluate({}).promotion_state, PromotionState.BLOCKED
                )

    def test_proof_review_rejects_a_gate_for_another_contract(self):
        review = SoftProofLab().review(
            claim_ref="claim:motion",
            contract_ref=ContractRef.DC04,
            validation_gate=GateRef.VG03,
            specimen_plan="run local slice specimen",
            failure_path="fails on world mutation",
            evidence_tier="unit-specimen",
        )
        self.assertEqual(review.record.promotion_state, PromotionState.BLOCKED)
        assert review.refusal is not None
        self.assertEqual(review.refusal.code, RefusalCode.INVALID_PAYLOAD)

    def test_blank_source_remains_a_governor_refusal_after_shape_validation(self):
        for source in (None, "", "  "):
            with self.subTest(source=source):
                claim = parse_contract(
                    ContractRef.DC01,
                    {**payloads()[ContractRef.DC01], "source_ref": source},
                )
                assert isinstance(claim, SourceClaim)
                result = ContextWeightGovernor().evaluate(claim)
                self.assertEqual(result.governor_decision, GovernorDecision.BLOCK)
                self.assertEqual(result.influence_weight, 0)


if __name__ == "__main__":
    unittest.main()
