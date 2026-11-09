"""Minimum-based source influence rubric; scores do not verify provenance."""

from __future__ import annotations

from dataclasses import replace
from enum import StrEnum

from spinaltap.contract_kernel import ContractRef, SourceClaim
from spinaltap.contract_validation import parse_contract


GOVERNOR_POLICY_ID = "governor-minimum-v1"


class GovernorDecision(StrEnum):
    ALLOW = "allow"
    DOWN_WEIGHT = "down_weight"
    BLOCK = "block"


class ContextWeightGovernor:
    def evaluate(self, claim: SourceClaim) -> SourceClaim:
        """Revalidate and rescore a claim without trusting its previous outputs.

        Policy identity belongs in caller evidence alongside source identity;
        decoding or migrating a DC01 record alone does not execute this policy.
        """
        checked = parse_contract(ContractRef.DC01, claim)
        assert isinstance(checked, SourceClaim)
        claim = checked
        if not claim.source_ref or not claim.source_ref.strip():
            return replace(
                claim,
                influence_weight=0.0,
                risk_flag="hidden_influence",
                governor_decision=GovernorDecision.BLOCK,
            )

        if claim.originality_distance < 0.20:
            return replace(
                claim,
                influence_weight=0.0,
                risk_flag="low_originality",
                governor_decision=GovernorDecision.BLOCK,
            )

        weight = min(
            claim.source_authority,
            claim.claim_fit,
            claim.originality_distance,
            claim.validation_reach,
        )
        if weight == 0:
            decision, risk = GovernorDecision.BLOCK, "zero_support"
            weight = 0.0
        elif weight < 1:
            decision, risk = GovernorDecision.DOWN_WEIGHT, "limited_support"
        else:
            decision, risk = GovernorDecision.ALLOW, "none"

        return replace(
            claim,
            influence_weight=weight,
            risk_flag=risk,
            governor_decision=decision,
        )
