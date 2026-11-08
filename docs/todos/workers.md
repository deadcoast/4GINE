# Worker authority and bounded local solvers [DOC]

Current workers validate caller-proposed scalar deltas against locally
declared keys. Persistent authority and actual richer local solver behavior
require explicit contracts.

> Goal: [GL01] - DELIVER_BOUNDED_TRACEABLE_SLICES
> Dependency: [DP01] - GLOBAL_PLAN_AND_TECHNICAL_CONTRACTS
> Requirement: [RQ01] - ACCEPTANCE_AND_EVIDENCE_BEFORE_COMPLETION

Follow the [global plan](../global_plan.md) and
[development workflow](../development_workflow.md). Requirements below refer
only to [requirements.md](../requirements.md); DC/VG meanings come from
[design.md](../design.md). ST identifiers are global task keys, while bracketed
context markers are local to this document.

## Scope and source map

- [Worker](../../spinaltap/vertebra_delta.py)
- [Worker tests](../../tests/test_vertebra_delta_worker.py)
- [Runtime gate tests](../../tests/test_runtime_gates.py)

## Individual TODOs

### ST-013: Define worker authority and state ownership

- Status: planned
- Phase: P2
- Requirements: REQ01, REQ07, REQ13
- Depends on: ST-005
- Owner: workers
- Legacy: Extends TODO.md::TK07
- Scope: Separate a worker's declared local_keys from authority to read/write
  registered state and name state lifecycle boundaries.
- Acceptance: Specify owner identity, registration/revocation, key membership,
  state/schema version and failure rules. Give authorized, unknown, revoked
  and overlapping-owner examples. Preserve shared-write refusal unless a
  separately accepted requirement justifies merging. State which objects are
  trusted.
- Evidence: pending

### ST-014: Enforce registered scalar worker authority

- Status: planned
- Phase: P2
- Requirements: REQ07, REQ13
- Depends on: ST-002, ST-013
- Owner: workers
- Legacy: Extends TODO.md::TK07
- Scope: Implement the approved authority model for existing scalar worker
  behavior.
- Acceptance: Registered allowed writes succeed; unknown/revoked owners,
  out-of-scope reads/writes and malformed registrations fail before
  publication. Scalar max_delta limits still refuse the entire proposal. Tests
  distinguish authorization from caller-supplied labels and attach
  acceptance/refusal evidence.
- Evidence: pending

### ST-015: Specify the demonstrator's richer local state

- Status: planned
- Phase: P3
- Requirements: REQ02, REQ03, REQ07, REQ13
- Depends on: ST-025
- Owner: workers
- Legacy: New scoped state design
- Scope: Choose only the state types needed by the accepted 3D scenario,
  including units, component budgets and any vector norm semantics.
- Acceptance: Publish a schema with concrete use cases, ownership,
  finite/range rules and exact-integer requirements where relevant. Explain
  which scalar assumptions remain and which change. Reject unneeded
  nested/concurrent/durable generalization. Define fixture data and migration
  boundaries before source work.
- Evidence: pending

### ST-016: Implement one bounded local solver fixture

- Status: planned
- Phase: P3
- Requirements: REQ07, REQ13, REQ15
- Depends on: ST-014, ST-015, ST-024
- Owner: workers
- Legacy: New demonstrator solver slice
- Scope: Implement the chosen local behavior and distinguish calculated solver
  output from validation of caller-proposed changes.
- Acceptance: A runnable positive fixture produces expected bounded state.
  Outside-ownership, invalid-number, excessive-step and
  contradictory-constraint cases refuse the complete proposal. Record units,
  tolerances and expected results. Do not infer general physics correctness
  from this one solver.
- Evidence: pending

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: CANONICAL_WORKSTREAM_TODO
  "Worker authority and bounded local solvers; authoritative individual task status and acceptance live here."

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
