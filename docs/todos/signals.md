# Signal routing and state adoption [DOC]

Current reconciliation returns a complete scalar candidate or no candidate. It
does not own durable state or roll back trusted callback side effects.

> Goal: [GL01] - DELIVER_BOUNDED_TRACEABLE_SLICES
> Dependency: [DP01] - GLOBAL_PLAN_AND_TECHNICAL_CONTRACTS
> Requirement: [RQ01] - ACCEPTANCE_AND_EVIDENCE_BEFORE_COMPLETION

Follow the [global plan](../global_plan.md) and
[development workflow](../development_workflow.md). Requirements below refer
only to [requirements.md](../requirements.md); DC/VG meanings come from
[design.md](../design.md). ST identifiers are global task keys, while bracketed
context markers are local to this document.

## Scope and source map

- [Spine](../../spinaltap/signal_spine.py)
- [Reconciler](../../spinaltap/reconciliation.py)
- [Spine tests](../../tests/test_signal_constraint_spine.py)
- [Single-worker tests](../../tests/test_spinal_reconciliation.py)
- [Batch tests](../../tests/test_multi_worker_reconciliation.py)

## Individual TODOs

### ST-017: Specify channel, hook and candidate-adoption policy

- Status: planned
- Phase: P2
- Requirements: REQ06, REQ12, REQ13
- Depends on: ST-005, ST-013
- Owner: signals
- Legacy: Extends TODO.md::TK08 and TODO.md::TK11
- Scope: Define authorized channels, whole-step invariants, candidate
  adoption/version checks and the trust boundary of synchronous hooks.
- Acceptance: Document allowed routes and refusal examples, including two
  individually valid deltas whose combined state violates an invariant. Define
  stale-version behavior and supported side effects. Keep concurrent
  publication, durability and process isolation out unless an accepted use
  case requires them.
- Evidence: pending

### ST-018: Validate and adopt authorized whole-step candidates

- Status: planned
- Phase: P2
- Requirements: REQ06, REQ07, REQ12, REQ13
- Depends on: ST-002, ST-014, ST-017
- Owner: signals
- Legacy: Extends TODO.md::TK08 and TODO.md::TK11
- Scope: Extend the synchronous scalar boundary with the approved authority
  and whole-candidate policy.
- Acceptance: Authorized disjoint jobs preserve declared order and
  original-snapshot reads. Unknown channels, aggregate invariant failures,
  stale state versions and late hook failures expose no partial candidate or
  publication. Keep equal/zero shared-write refusals. State explicitly that
  external callback side effects are outside rollback guarantees.
- Evidence: pending

### ST-019: Decide whether stronger publication guarantees are needed

- Status: deferred
- Phase: P5
- Requirements: REQ02, REQ06, REQ12
- Depends on: ST-025
- Owner: signals
- Legacy: Reclassifies broad historical MO05/MO08 future work
- Scope: Evaluate concurrency, durable commits, conflict merging and hook
  isolation only against an accepted application requirement.
- Acceptance: Record a concrete use case and measured limitation before
  admitting any stronger guarantee. Each selected feature gets its own
  contract, failure model, dependency and evidence task; rejected or deferred
  features retain rationale. Do not treat this discovery card as an
  implementation commitment.
- Evidence: pending

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: CANONICAL_WORKSTREAM_TODO
  "Signal routing and state adoption; authoritative individual task status and acceptance live here."

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
