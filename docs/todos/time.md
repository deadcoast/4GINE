# Time ownership and replay scope [DOC]

Fixed-step conversion and raw-time refusal already work for scalar specimens.
Identity, backlog policy and replay evidence are separate work.

> Goal: [GL01] - DELIVER_BOUNDED_TRACEABLE_SLICES
> Dependency: [DP01] - GLOBAL_PLAN_AND_TECHNICAL_CONTRACTS
> Requirement: [RQ01] - ACCEPTANCE_AND_EVIDENCE_BEFORE_COMPLETION

Follow the [global plan](../global_plan.md) and
[development workflow](../development_workflow.md). Requirements below refer
only to [requirements.md](../requirements.md); DC/VG meanings come from
[design.md](../design.md). ST identifiers are global task keys, while bracketed
context markers are local to this document.

## Scope and source map

- [Time pump](../../spinaltap/time_packet.py)
- [Pump tests](../../tests/test_time_packet_pump.py)
- [Runtime gate tests](../../tests/test_runtime_gates.py)
- [Demo](../../spinaltap/demo.py)

## Individual TODOs

### ST-010: Specify time identity and overload semantics

- Status: ready
- Phase: P2
- Requirements: REQ05, REQ11
- Depends on: none
- Owner: time
- Legacy: Extends TODO.md::TK06
- Scope: Decide backlog preservation/drop behavior, pause/resume, refused-step
  time consumption, interpolation under backlog and the supported replay
  scope.
- Acceptance: Document elapsed-time accounting for nominal, oversized,
  sustained-overload and refused-step sequences. Define step/config/input
  identity and numerical comparison policy. Preserve the current
  consume-refused-step behavior until deliberately superseded. A packet cap
  must not be described as a wall-clock deadline guarantee.
- Evidence: pending

### ST-011: Implement checkpoint and ordered-step replay specimens

- Status: planned
- Phase: P2
- Requirements: REQ05, REQ11, REQ15
- Depends on: ST-002, ST-005, ST-010
- Owner: time
- Legacy: New continuation of the time slice
- Scope: Add only the identity and checkpoint behavior required by the
  accepted bounded replay policy.
- Acceptance: Replay recorded initial state, configuration, input order and
  fixed steps to the declared comparison tolerance. Duplicate, stale,
  wrong-configuration or out-of-order steps follow explicit refusal rules.
  Checkpoint restore includes accumulator policy. Keep existing
  decimal/subnormal and fixed-step ingress specimens.
- Evidence: pending

### ST-012: Measure overload and refused-step accounting

- Status: planned
- Phase: P2
- Requirements: REQ05, REQ11, REQ15
- Depends on: ST-011
- Owner: time
- Legacy: New timing qualification
- Scope: Qualify the scalar harness under the declared backlog policy and
  report actual elapsed-work measurements separately from packet counts.
- Acceptance: Record nominal, backlog-drain, sustained-overload and refusal
  traces. Account for preserved or discarded elapsed time and bounded work
  according to policy. Identify environment and numeric tolerance. Distinguish
  observed scalar timings from future interactive frame budgets.
- Evidence: pending

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: CANONICAL_WORKSTREAM_TODO
  "Time ownership and replay scope; authoritative individual task status and acceptance live here."

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
