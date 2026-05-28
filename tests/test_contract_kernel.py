import unittest

from spinaltap.contract_kernel import (
    ContractRef,
    DeltaPacket,
    GateRef,
    PromotionState,
    ProofRecord,
    RefusalCode,
    SpecimenHook,
    SignalBundle,
    SourceClaim,
    StyleLimits,
    TimePacket,
    contract_fields,
    refuse,
)


class ContractKernelTests(unittest.TestCase):
    def test_contract_record_types_match_the_docspec_fields(self):
        records = (
            (ContractRef.DC01, SourceClaim),
            (ContractRef.DC02, TimePacket),
            (ContractRef.DC03, SignalBundle),
            (ContractRef.DC04, DeltaPacket),
            (ContractRef.DC05, StyleLimits),
            (ContractRef.DC06, ProofRecord),
        )

        for contract, record_type in records:
            with self.subTest(contract=contract):
                self.assertEqual(record_type.fields(), contract_fields(contract))

    def test_contract_records_expose_exact_docspec_fields(self):
        self.assertEqual(
            contract_fields(ContractRef.DC01),
            (
                "source_ref",
                "claim_text",
                "source_authority",
                "claim_fit",
                "originality_distance",
                "validation_reach",
                "influence_weight",
                "risk_flag",
                "governor_decision",
            ),
        )
        self.assertEqual(
            contract_fields(ContractRef.DC02),
            (
                "elapsed_time",
                "fixed_packet_size",
                "packet_count",
                "accumulator_remainder",
                "interpolation_state",
                "overflow_risk",
            ),
        )
        self.assertEqual(
            contract_fields(ContractRef.DC03),
            (
                "owner",
                "channel",
                "ordered_signal_bundle",
                "constraint_envelope",
                "validation_hook",
                "residual_risk",
            ),
        )
        self.assertEqual(
            contract_fields(ContractRef.DC04),
            (
                "local_state_slice",
                "constraint_set",
                "time_packet",
                "bounded_delta",
                "residual_risk",
            ),
        )
        self.assertEqual(
            contract_fields(ContractRef.DC05),
            (
                "geometry_limit",
                "lighting_limit",
                "texture_limit",
                "color_limit",
                "fog_limit",
                "alpha_limit",
                "depth_limit",
                "camera_limit",
                "animation_cadence",
                "artifact_limits",
            ),
        )
        self.assertEqual(
            contract_fields(ContractRef.DC06),
            (
                "claim_ref",
                "contract_ref",
                "specimen_plan",
                "failure_path",
                "promotion_state",
                "evidence_tier",
            ),
        )

    def test_refusal_state_keeps_claim_below_implementation_ready(self):
        state = refuse(
            ContractRef.DC06,
            GateRef.VG06,
            RefusalCode.MISSING_FAILURE_PATH,
            "claim lacks an explicit failure path",
        )

        self.assertEqual(state.contract, ContractRef.DC06)
        self.assertEqual(state.gate, GateRef.VG06)
        self.assertEqual(state.code, RefusalCode.MISSING_FAILURE_PATH)
        self.assertEqual(state.promotion_state, PromotionState.BLOCKED)
        self.assertIn("failure path", state.reason)

    def test_specimen_hook_blocks_proof_without_plan_or_failure_path(self):
        hook = SpecimenHook.for_contract(ContractRef.DC06, GateRef.VG06)

        result = hook.evaluate(
            {
                "claim_ref": "claim:demo",
                "contract_ref": "DC06",
                "specimen_plan": "",
                "failure_path": "",
                "promotion_state": "candidate",
                "evidence_tier": "docs-only",
            }
        )

        self.assertEqual(result.promotion_state, PromotionState.BLOCKED)
        refusal = result.refusal
        assert refusal is not None
        self.assertEqual(refusal.code, RefusalCode.MISSING_SPECIMEN)


if __name__ == "__main__":
    unittest.main()
