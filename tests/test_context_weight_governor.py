import unittest

from spinaltap.context_weight import ContextWeightGovernor, GovernorDecision
from spinaltap.contract_kernel import SourceClaim


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


if __name__ == "__main__":
    unittest.main()
