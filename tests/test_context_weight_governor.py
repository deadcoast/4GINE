import copy
import json
import math
import unittest
from dataclasses import asdict
from itertools import product
from pathlib import Path

from spinaltap.context_weight import (
    GOVERNOR_POLICY_ID,
    ContextWeightGovernor,
    GovernorDecision,
)
from spinaltap.contract_kernel import (
    ContractRef,
    GateRef,
    PromotionState,
    RefusalCode,
    SourceClaim,
)
from spinaltap.contract_validation import (
    LEGACY_BASELINE_REVISION,
    ContractIdentity,
    ContractValidationError,
    migrate_legacy_contract,
    parse_contract,
    parse_contract_envelope,
)


SPEC = json.loads(
    (Path(__file__).resolve().parents[1] / "docs/examples/governor_policy.json").read_text()
)


class ContextWeightGovernorTests(unittest.TestCase):
    def test_low_originality_claim_is_blocked_from_model_influence(self):
        governor = ContextWeightGovernor()

        result = governor.evaluate(
            SourceClaim(
                source_ref="source:engine-pattern",
                claim_text="replicate the source structure directly",
                source_authority=0.90,
                claim_fit=0.90,
                originality_distance=0.05,
                validation_reach=0.70,
                influence_weight=None,
                risk_flag=None,
                governor_decision=None,
            )
        )

        self.assertEqual(result.governor_decision, GovernorDecision.BLOCK)
        self.assertEqual(result.influence_weight, 0.0)
        self.assertEqual(result.risk_flag, "low_originality")

    def test_hidden_influence_claim_is_blocked_without_source_ref(self):
        governor = ContextWeightGovernor()

        result = governor.evaluate(
            SourceClaim(
                source_ref="",
                claim_text="import an unattributed design pattern",
                source_authority=0.80,
                claim_fit=0.80,
                originality_distance=0.80,
                validation_reach=0.80,
                influence_weight=None,
                risk_flag=None,
                governor_decision=None,
            )
        )

        self.assertEqual(result.governor_decision, GovernorDecision.BLOCK)
        self.assertEqual(result.influence_weight, 0.0)
        self.assertEqual(result.risk_flag, "hidden_influence")


class GovernorPolicyTests(unittest.TestCase):
    def setUp(self):
        self.governor = ContextWeightGovernor()

    def claim(self, **changes):
        # Deliberately use the trusted constructor so validation cannot be
        # accidentally delegated to the caller in these boundary specimens.
        return SourceClaim(**{**SPEC["invalid_input_base"], **changes})

    def assert_outcome(self, result, expected):
        self.assertEqual(result.governor_decision, expected["governor_decision"])
        self.assertEqual(result.influence_weight, expected["influence_weight"])
        self.assertEqual(result.risk_flag, expected["risk_flag"])

    def assert_invalid(self, claim, field):
        with self.assertRaises(ContractValidationError) as caught:
            self.governor.evaluate(claim)
        error = caught.exception
        self.assertEqual(error.field, field)
        self.assertEqual(error.refusal.contract, ContractRef.DC01)
        self.assertEqual(error.refusal.gate, GateRef.VG01)
        self.assertEqual(error.refusal.code, RefusalCode.INVALID_PAYLOAD)
        self.assertEqual(error.refusal.promotion_state, PromotionState.BLOCKED)
        return error

    def test_policy_identity_matches_the_accepted_corpus(self):
        self.assertEqual(GOVERNOR_POLICY_ID, "governor-minimum-v1")
        self.assertEqual(GOVERNOR_POLICY_ID, SPEC["policy_id"])
        self.assertEqual(SPEC["record_identity"], {"contract": "DC01", "schema_revision": 1})

    def test_all_twenty_outcome_cases_reach_the_exact_selected_results(self):
        self.assertEqual(len(SPEC["cases"]), 20)
        decisions = set()
        for case in SPEC["cases"]:
            with self.subTest(case=case["id"]):
                result = self.governor.evaluate(SourceClaim(**case["payload"]))
                self.assert_outcome(result, case["selected_policy_outcome"])
                decisions.add(result.governor_decision)
        self.assertEqual(decisions, set(GovernorDecision))

    def test_all_thirty_two_invalid_scores_receive_structured_refusals(self):
        self.assertEqual(len(SPEC["invalid_inputs"]), 32)
        for case in SPEC["invalid_inputs"]:
            value = case["value"]
            if isinstance(value, dict):
                value = float(value["special_float"])
            with self.subTest(case=case["id"]):
                error = self.assert_invalid(
                    self.claim(**{case["field"]: value}),
                    case["selected_policy_outcome"]["field"],
                )
                expected = case["selected_policy_outcome"]
                self.assertEqual(expected["status"], "refused")
                for key in ("contract", "gate", "code", "promotion_state"):
                    self.assertEqual(getattr(error.refusal, key), expected[key])

    def test_text_and_derived_fields_are_revalidated_even_if_overwritten(self):
        invalids = {
            "source_ref": (True, 1, []),
            "claim_text": (None, "", "  ", 1),
            "influence_weight": (True, "0.5", -0.1, 1.1, float("nan"), float("inf")),
            "risk_flag": ("", "  ", 1),
            "governor_decision": ("unknown", "", True),
        }
        for field, values in invalids.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    self.assert_invalid(self.claim(**{field: value}), f"DC01.{field}")

    def test_invalid_scores_take_precedence_over_both_business_blocks(self):
        for source_ref in (None, "", "  ", "source:valid"):
            for originality in (0.1, 1):
                with self.subTest(source=source_ref, originality=originality):
                    self.assert_invalid(
                        self.claim(
                            source_ref=source_ref, originality_distance=originality,
                            validation_reach=float("nan"),
                        ),
                        "DC01.validation_reach",
                    )

    def test_invalid_derived_fields_cannot_be_repaired_by_an_early_block(self):
        for field, value in (
            ("influence_weight", False), ("risk_flag", ""),
            ("governor_decision", "trust_me"),
        ):
            for source_ref in (None, "source:valid"):
                with self.subTest(field=field, source=source_ref):
                    self.assert_invalid(
                        self.claim(
                            source_ref=source_ref, originality_distance=0.1,
                            **{field: value},
                        ),
                        f"DC01.{field}",
                    )

    def test_each_factor_bounds_influence_without_compensation(self):
        for scores in product((0, 0.2, 0.6, 1), repeat=4):
            with self.subTest(scores=scores):
                result = self.governor.evaluate(
                    self.claim(**dict(zip(SPEC["score_order"], scores)))
                )
                assert result.influence_weight is not None
                self.assertGreaterEqual(result.influence_weight, 0)
                for score in scores:
                    self.assertLessEqual(result.influence_weight, score)

    def test_all_corpus_inputs_are_preserved_and_rescoring_is_idempotent(self):
        for case in SPEC["cases"]:
            with self.subTest(case=case["id"]):
                before = copy.deepcopy(case["payload"])
                claim = SourceClaim(**case["payload"])
                result = self.governor.evaluate(claim)
                self.assertEqual(asdict(claim), before)
                self.assertEqual(case["payload"], before)
                for field in ("source_ref", "claim_text", *SPEC["score_order"]):
                    self.assertEqual(getattr(result, field), getattr(claim, field))
                self.assertEqual(self.governor.evaluate(result), result)

    def test_previous_decisions_and_weights_never_override_fresh_scores(self):
        for decision, weight in product(GovernorDecision, (0, 0.25, 1)):
            with self.subTest(decision=decision, weight=weight):
                result = self.governor.evaluate(self.claim(
                    claim_fit=0.5, influence_weight=weight,
                    governor_decision=decision, risk_flag="old_risk",
                ))
                self.assert_outcome(result, {
                    "governor_decision": "down_weight", "influence_weight": 0.5,
                    "risk_flag": "limited_support",
                })

    def test_signed_zero_yields_zero_influence_with_a_positive_zero_result(self):
        for field in SPEC["score_order"]:
            with self.subTest(field=field):
                result = self.governor.evaluate(self.claim(**{field: -0.0}))
                self.assertEqual(result.governor_decision, GovernorDecision.BLOCK)
                self.assertEqual(result.influence_weight, 0.0)
                assert result.influence_weight is not None
                self.assertEqual(math.copysign(1.0, result.influence_weight), 1.0)
                self.assertEqual(
                    result.risk_flag,
                    "low_originality" if field == "originality_distance" else "zero_support",
                )

    def test_adjacent_float_fixtures_keep_their_exact_boundaries(self):
        cases = {case["id"]: case for case in SPEC["cases"]}
        for name, field, exact in (
            ("below_originality_floor", "originality_distance", math.nextafter(0.2, 0)),
            ("at_originality_floor", "originality_distance", 0.2),
            ("above_originality_floor", "originality_distance", math.nextafter(0.2, 1)),
            ("below_full_support", "claim_fit", math.nextafter(1, 0)),
            ("smallest_positive_fit", "claim_fit", math.nextafter(0, 1)),
        ):
            with self.subTest(case=name):
                case = cases[name]
                self.assertEqual(case["payload"][field], exact)
                self.assert_outcome(
                    self.governor.evaluate(SourceClaim(**case["payload"])),
                    case["selected_policy_outcome"],
                )

    def test_versioned_ingress_and_governor_evaluation_are_separate_operations(self):
        value = {
            "contract": "DC01", "schema_revision": 1,
            "payload": {**SPEC["invalid_input_base"], "claim_fit": 0},
        }
        decoded = parse_contract_envelope(ContractRef.DC01, value)
        self.assertEqual(decoded.identity, ContractIdentity(ContractRef.DC01, 1))
        assert isinstance(decoded.record, SourceClaim)
        self.assertIsNone(decoded.record.governor_decision)
        result = self.governor.evaluate(decoded.record)
        self.assert_outcome(result, {
            "governor_decision": "block", "influence_weight": 0,
            "risk_flag": "zero_support",
        })
        self.assertIsNone(decoded.record.governor_decision)
        self.assertEqual(parse_contract(ContractRef.DC01, result), result)

    def test_migration_preserves_legacy_outputs_until_explicit_reevaluation(self):
        case = next(case for case in SPEC["cases"] if case["id"] == "reevaluate_existing_outputs")
        original = copy.deepcopy(case["payload"])
        migrated = migrate_legacy_contract(
            ContractRef.DC01, original, LEGACY_BASELINE_REVISION, "fixture:legacy-governor"
        )
        assert isinstance(migrated.decoded.record, SourceClaim)
        self.assertEqual(migrated.decoded.record.governor_decision, "allow")
        self.assertEqual(migrated.decoded.record.influence_weight, 0.75)
        self.assertEqual(migrated.receipt.target_identity, ContractIdentity(ContractRef.DC01, 1))
        self.assert_outcome(
            self.governor.evaluate(migrated.decoded.record), case["selected_policy_outcome"]
        )
        self.assertEqual(migrated.decoded.record.influence_weight, 0.75)
        self.assertEqual(original, case["payload"])


if __name__ == "__main__":
    unittest.main()
