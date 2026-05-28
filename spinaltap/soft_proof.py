"""Soft-Proof Lab specimen for claim promotion gates."""

from __future__ import annotations

from dataclasses import dataclass, replace

from spinaltap.contract_kernel import (
    ContractRef,
    GateRef,
    PromotionState,
    ProofRecord,
    RefusalState,
    SpecimenHook,
)


@dataclass(frozen=True)
class ProofReview:
    record: ProofRecord
    refusal: RefusalState | None


class SoftProofLab:
    def __init__(self) -> None:
        self._proof_hook = SpecimenHook.for_contract(ContractRef.DC06, GateRef.VG06)

    def review(
        self,
        *,
        claim_ref: str,
        contract_ref: ContractRef,
        validation_gate: GateRef,
        specimen_plan: str,
        failure_path: str,
        evidence_tier: str,
    ) -> ProofReview:
        record = ProofRecord(
            claim_ref=claim_ref,
            contract_ref=contract_ref,
            specimen_plan=specimen_plan,
            failure_path=failure_path,
            promotion_state=PromotionState.CANDIDATE,
            evidence_tier=evidence_tier,
        )
        result = self._proof_hook.evaluate(
            {
                "claim_ref": record.claim_ref,
                "contract_ref": record.contract_ref,
                "validation_gate": validation_gate,
                "specimen_plan": record.specimen_plan,
                "failure_path": record.failure_path,
                "promotion_state": record.promotion_state,
                "evidence_tier": record.evidence_tier,
            }
        )

        return ProofReview(
            record=replace(record, promotion_state=result.promotion_state),
            refusal=result.refusal,
        )
