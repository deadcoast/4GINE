import unittest

from spinaltap.contract_kernel import (
    ContractRef,
    GateRef,
    PromotionState,
    ProofRecord,
    RefusalCode,
    RefusalState,
)
from spinaltap.soft_proof import SoftProofLab


class SoftProofLabTests(unittest.TestCase):
    def test_complete_claim_produces_implementation_ready_proof_record(self):
        lab = SoftProofLab()

        review = lab.review(
            claim_ref="claim:signal-spine-orders-deltas",
            contract_ref=ContractRef.DC03,
            validation_gate=GateRef.VG03,
            specimen_plan="run signal spine ordering specimen",
            failure_path="fails if direct global mutation is accepted",
            evidence_tier="unit-specimen",
        )

        self.assertIsInstance(review.record, ProofRecord)
        self.assertEqual(review.record.claim_ref, "claim:signal-spine-orders-deltas")
        self.assertEqual(review.record.contract_ref, ContractRef.DC03)
        self.assertEqual(
            review.record.promotion_state,
            PromotionState.IMPLEMENTATION_READY,
        )
        self.assertEqual(review.record.evidence_tier, "unit-specimen")
        self.assertIsNone(review.refusal)

    def test_missing_specimen_plan_blocks_claim_promotion(self):
        lab = SoftProofLab()

        review = lab.review(
            claim_ref="claim:prose-confidence-only",
            contract_ref=ContractRef.DC06,
            validation_gate=GateRef.VG06,
            specimen_plan="",
            failure_path="fails if claim advances by prose alone",
            evidence_tier="docs-only",
        )

        self.assertEqual(review.record.promotion_state, PromotionState.BLOCKED)
        refusal = review.refusal
        assert isinstance(refusal, RefusalState)
        self.assertEqual(refusal.code, RefusalCode.MISSING_SPECIMEN)
        self.assertIn("specimen plan", refusal.reason)


if __name__ == "__main__":
    unittest.main()
