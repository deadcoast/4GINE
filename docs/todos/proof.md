# Proof lifecycle and evidence records [DOC]

Current implementation_ready records establish structural planning readiness
only. The current API does not execute specimens or verify their artifacts.

> Goal: [GL01] - DELIVER_BOUNDED_TRACEABLE_SLICES
> Dependency: [DP01] - GLOBAL_PLAN_AND_TECHNICAL_CONTRACTS
> Requirement: [RQ01] - ACCEPTANCE_AND_EVIDENCE_BEFORE_COMPLETION

Follow the [global plan](../global_plan.md) and
[development workflow](../development_workflow.md). Requirements below refer
only to [requirements.md](../requirements.md); DC/VG meanings come from
[design.md](../design.md). ST identifiers are global task keys, while bracketed
context markers are local to this document.

## Scope and source map

- [Proof lab](../../spinaltap/soft_proof.py)
- [Proof hook](../../spinaltap/contract_kernel.py)
- [Proof tests](../../tests/test_soft_proof_lab.py)

## Individual TODOs

### ST-023: Define proof states and executed-evidence semantics

- Status: ready
- Phase: P2
- Requirements: REQ09, REQ15
- Depends on: none
- Owner: proof
- Legacy: TODO.md::TK10
- Scope: Resolve whether implementation_ready denotes permission to implement
  or verified implementation, and specify unambiguous successor states.
- Acceptance: Distinguish planned, executed, failed and accepted evidence.
  Define claim/contract/schema identity, specimen and failure result,
  revision, environment, command, artifact and review decision. Text-only
  plans cannot satisfy execution. State migration treatment for existing
  records and the evidence-tier vocabulary. Never infer command execution
  authority from arbitrary plan text.
- Evidence: pending

### ST-024: Implement evidence records and promotion checks

- Status: planned
- Phase: P2
- Requirements: REQ09, REQ15
- Depends on: ST-002, ST-005, ST-023
- Owner: proof
- Legacy: TODO.md::TK10
- Scope: Implement the approved structured evidence ledger, choosing in-memory
  or persisted storage only as justified by the decision.
- Acceptance: Positive and deliberately failing specimens have distinguishable
  recorded results. Missing artifacts, unknown tiers, mismatched
  claims/contracts, failed checks and stale revisions cannot silently promote.
  A plan saying not executed remains unverified. Verify record
  serialization/audit output where selected; no arbitrary execution of
  user-supplied plan strings.
- Evidence: pending

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: CANONICAL_WORKSTREAM_TODO
  "Proof lifecycle and evidence records; authoritative individual task status and acceptance live here."

[GL01]: DELIVER_BOUNDED_TRACEABLE_SLICES
  "Advance the owning global phase through individually scoped and verified
  development work."

[DP01]: GLOBAL_PLAN_AND_TECHNICAL_CONTRACTS
  "Global phase intent comes from global_plan.md; requirements and design own
  technical meaning; task dependencies name globally unique ST identifiers."

[RQ01]: ACCEPTANCE_AND_EVIDENCE_BEFORE_COMPLETION
  "Each task retains its phase, requirements, dependencies, acceptance and
  evidence. Planned or structural evidence cannot imply runtime completion."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative index invoking each active local context marker."
