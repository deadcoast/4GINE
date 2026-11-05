"""Context-Weight Governor specimen for source influence scoring."""

from __future__ import annotations

from dataclasses import replace
from enum import StrEnum

from spinaltap.contract_kernel import SourceClaim


class GovernorDecision(StrEnum):
    ALLOW = "allow"
    DOWN_WEIGHT = "down_weight"
    BLOCK = "block"


class ContextWeightGovernor:
    def evaluate(self, claim: SourceClaim) -> SourceClaim:
        if not claim.source_ref or not claim.source_ref.strip():
            return replace(
                claim,
                influence_weight=0.0,
                risk_flag="hidden_influence",
                governor_decision=GovernorDecision.BLOCK,
            )

        if float(claim.originality_distance) < 0.20:
            return replace(
                claim,
                influence_weight=0.0,
                risk_flag="low_originality",
                governor_decision=GovernorDecision.BLOCK,
            )

        return replace(
            claim,
            influence_weight=_bounded_weight(claim),
            risk_flag="none",
            governor_decision=GovernorDecision.ALLOW,
        )


def _bounded_weight(claim: SourceClaim) -> float:
    factors = (
        float(claim.source_authority),
        float(claim.claim_fit),
        float(claim.originality_distance),
        float(claim.validation_reach),
    )
    return max(0.0, min(1.0, sum(factors) / len(factors)))
