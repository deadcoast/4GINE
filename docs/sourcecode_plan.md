# (A) 4GINE SOURCECODE IMPLEMENTATION PLAN [DOC]

This document records the gated implementation order and current source slices
for the SPINALTAP Constraint Engine [WL05]. It exists because the docspec
package reached the validation gate required before source planning [D04],
[D05], [D06], [REQ03], [TK16].

The plan keeps the first implementation target small: a contract-first
research prototype, not a complete renderer, complete physics engine, ECS
clone, scene-tree clone, or fixed-function renderer clone [REQ01], [REQ02].

## (1) Source gate [KN]

> Goal: [GL01] - ENTER_SOURCE_PLANNING_ONLY_AFTER_DOCSPEC
> Dependency: [DP01] - VALIDATED_DOCSPEC_PACKAGE
> Requirement: [RQ01] - NO_RUNTIME_SOURCECODE_IN_THIS_DOCUMENT

This file began as the sourcecode work order [TK17]. The eight initial source
slices below are present, and the user's 2026-11-05 instruction to continue
development authorizes continuation of the bounded prototype [WL05]. The
remaining source backlog is [TODO.md](../TODO.md); the initial docspec tasklist
[D06] remains a completed planning record.

Entry evidence:

- [D04] defines the accepted requirements and acceptance criteria.
- [D05] defines module ownership, data records, and validation behavior.
- [D06] verifies the work order through the final docspec gate [TK16].
- [REQ15] requires runnable specimen plans and failure paths before any claim
  becomes implementation-ready.

## (2) Prototype shape [PL]

> Goal: [GL02] - BUILD_CONTRACT_KERNEL_FIRST
> Dependency: [DP02] - EXPLICIT_DATA_CONTRACTS
> Requirement: [RQ02] - REFUSAL_BEHAVIOR_BEFORE_FEATURE_BEHAVIOR

The first source slice should implement a contract kernel before visible
engine behavior [DC01], [DC02], [DC03], [DC04], [DC05], [DC06]. The kernel
should expose records, refusal states, promotion states, and specimen hooks.

The first source slice must not create:

- renderer completion claims;
- physics completion claims;
- hidden global mutation;
- raw elapsed-time solver entry;
- unscored source influence;
- style decisions that remain mood labels;
- proof advancement without failure paths.

## (3) Implementation order [PL]

> Goal: [GL03] - IMPLEMENT_MODULES_IN_DEPENDENCY_ORDER
> Dependency: [DP03] - MODULE_CONTRACT_SEQUENCE
> Requirement: [RQ03] - SMALL_REVIEWABLE_SOURCE_SLICES

| Step | Source slice | Required owner | Contract | Gate |
| --- | --- | --- | --- | --- |
| 1 | Contract kernel records and refusal states | all modules | [DC01]-[DC06] | [VG06] |
| 2 | Context-Weight Governor specimen | [MG01] | [DC01] | [VG01] |
| 3 | Time Packet Pump specimen | [MG02] | [DC02] | [VG02] |
| 4 | Vertebra Delta Worker specimen | [MG04] | [DC04] | [VG04] |
| 5 | Signal-Constraint Spine specimen | [MG03] | [DC03] | [VG03] |
| 6 | Style Constraint Surface specimen | [MG05] | [DC05] | [VG05] |
| 7 | Soft-Proof Lab specimen | [MG06] | [DC06] | [VG06] |
| 8 | Minimal spinal reconciliation harness | [MG03], [MG04] | [DC03], [DC04] | [VG03], [VG04] |

Step 1 status: `spinaltap/contract_kernel.py` owns the contract references,
record fields, refusal states, promotion states, and initial proof specimen
hook. `tests/test_contract_kernel.py` verifies the [DC01] through [DC06]
fields and the [VG06] refusal path.

Step 2 status: `spinaltap/context_weight.py` owns the [MG01] source-influence
specimen. `tests/test_context_weight_governor.py` verifies that low-originality
or hidden-influence [DC01] claims are blocked before model influence [VG01].

Step 3 status: `spinaltap/time_packet.py` owns the [MG02] fixed-packet
specimen. `tests/test_time_packet_pump.py` verifies that raw elapsed time is
converted to [DC02] packets before solver access and oversized elapsed time
emits overflow risk [VG02].

Step 4 status: `spinaltap/vertebra_delta.py` owns the [MG04] local-slice
delta specimen. `tests/test_vertebra_delta_worker.py` verifies that bounded
[DC04] deltas stay inside the declared local slice and outside-slice deltas
emit explicit refusal risk [VG04].

Step 5 status: `spinaltap/signal_spine.py` owns the [MG03] ordered signal
bundle specimen. `tests/test_signal_constraint_spine.py` verifies that bounded
deltas route through [DC03] bundles and direct or incomplete mutation attempts
emit explicit refusal risk before aggregation [VG03].

Step 6 status: `spinaltap/style_surface.py` owns the [MG05] measurable style
limit specimen. `tests/test_style_constraint_surface.py` verifies that style
profiles become [DC05] limits and mood-label profiles emit explicit refusal
risk [VG05].

Step 7 status: `spinaltap/soft_proof.py` owns the [MG06] proof-record
specimen. `tests/test_soft_proof_lab.py` verifies that complete claims become
implementation-ready [DC06] records and prose-only claims without specimen
plans remain blocked [VG06].

Step 8 status: `spinaltap/reconciliation.py` owns the minimal [MG03]/[MG04]
reconciliation harness. `tests/test_spinal_reconciliation.py` verifies that
worker deltas route into ordered [DC03] bundles and [DC04] worker refusals stop
before signal aggregation [VG03], [VG04].

Step 8 is only a harness. It may prove ordered signal reconciliation, but it
must not claim a complete engine loop.

Continuation status: root TODO task `TK04` adds
`spinaltap/contract_validation.py` for [DC01] through [DC06] mapping ingress.
The decoder checks required and unknown fields, finite numbers, declared
ranges, enum values, nested records, and refusal metadata. It reports a
blocked refusal with the failing field path. Style and specimen mapping inputs
use the decoder; direct dataclass constructors remain trusted internal APIs.
`tests/test_contract_validation.py` covers malformed inputs and preserves the
distinction between structural validity and module gate acceptance [VG01],
[VG02], [VG03], [VG04], [VG05], [VG06].

Root TODO tasks `TK06`, `TK07`, and `TK08` now add fixed-step worker entry,
per-component scalar budgets, and executed signal validation hooks. The
single-worker reconciliation harness converts invalid inputs into refused
bundles, and `spinaltap/demo.py` connects the time pump to that harness. Tests
cover accumulator conservation, refusal propagation, hook failure, and state
updates only after acceptance [VG02], [VG03], [VG04].

Root TODO task `TK11` now adds `WorkerUpdate`, `StepResult`, and
`SpinalReconciliationHarness.reconcile_step`. Workers share an initial scalar
snapshot and route in explicit order. Conflicting writes are refused before
hooks run; later worker or hook failures discard the entire candidate and
bundle set. `tests/test_multi_worker_reconciliation.py` verifies order,
ownership, snapshot isolation, conflict refusals, and all-or-nothing results
[VG02], [VG03], [VG04].

### (3.1) Run the prototype [PL]

> Goal: [GL03] - IMPLEMENT_MODULES_IN_DEPENDENCY_ORDER
> Dependency: [DP03] - MODULE_CONTRACT_SEQUENCE
> Requirement: [RQ03] - SMALL_REVIEWABLE_SOURCE_SLICES

From the repository root, using the verified Python 3.13 interpreter:

```powershell
py -3.13 -m spinaltap
py -3.13 -m spinaltap --json
py -3.13 -m unittest discover -s tests
```

The runtime uses only the standard library. The default demonstration converts
six elapsed-time samples into fourteen complete two-worker steps, drains an
oversized frame's backlog, and finishes at `x = 0.672`, `y = -0.336`, with
`0.008` time remaining. The y-worker runs before the x-worker. Separate
oversized-delta and conflicting-write specimens must be refused, and ordinary
demo steps must all succeed; otherwise the command exits with a failure status.
JSON output carries the frame evidence, worker order, final state, and guard
refusals. Its existing `final_position` field continues to report x.

The demo's custom signal hook restricts each coordinate to `-1..1`. Worker or
hook refusals leave both coordinates unchanged, while the elapsed simulation
step is consumed. This is a synchronous scalar prototype; rendering, general
state publication, worker/channel authority, concurrent scheduling, and
additive conflict merging remain future work [REQ02], [MG02], [MG03], [MG04].

## (4) Specimen-first tests [VG]

> Goal: [GL04] - TEST_REFUSAL_PATHS_FIRST
> Dependency: [DP04] - VALIDATION_SPECIMENS
> Requirement: [RQ04] - RUNNABLE_FAILURE_BEFORE_PROMOTION

The first source tests should target the refusal paths before happy paths:

- [VG01]: a copied or hidden-influence claim is blocked or down-weighted.
- [VG02]: a solver cannot receive raw elapsed time.
- [VG03]: a direct global mutation is refused before aggregation.
- [VG04]: a vertebra cannot read or write outside its local state slice.
- [VG05]: a style profile that cannot become limits is refused.
- [VG06]: an implementation claim without specimen plan and failure path stays
  below implementation-ready status.

Passing these tests does not prove the engine complete. It only proves the
first source slice preserves the docspec constraints.

## (5) Requirement traceability audit [AC]

> Goal: [GL05] - DECIDE_SOURCE_BLOCK_STATUS_FROM_TRACEABILITY
> Dependency: [DP05] - REQUIREMENT_TO_OWNER_MATRIX
> Requirement: [RQ05] - NO_UNOWNED_REQUIREMENT_ENTERS_SOURCE

The audit below checks the [TK18] condition. A requirement may enter source
planning only when it has a design owner, contract, validation gate, and
task coverage.

| Requirement | Design owner | Contract | Gate | Task coverage |
| --- | --- | --- | --- | --- |
| [REQ01] | all modules | [DC01]-[DC06] | [VG01]-[VG06] | `TK02` |
| [REQ02] | all modules | [DC01]-[DC06] | [VG01]-[VG06] | `TK02` |
| [REQ03] | [MG06] | [DC06] | [VG06] | `TK16`, `TK17` |
| [REQ04] | [MG01] | [DC01] | [VG01] | `TK04`, `TK10` |
| [REQ05] | [MG02] | [DC02] | [VG02] | `TK05`, `TK11` |
| [REQ06] | [MG03] | [DC03] | [VG03] | `TK06`, `TK12` |
| [REQ07] | [MG04] | [DC04] | [VG04] | `TK07`, `TK13` |
| [REQ08] | [MG05] | [DC05] | [VG05] | `TK08`, `TK14` |
| [REQ09] | [MG06] | [DC06] | [VG06] | `TK09`, `TK15` |
| [REQ10] | [MG01] | [DC01] | [VG01] | `TK10` |
| [REQ11] | [MG02] | [DC02] | [VG02] | `TK11` |
| [REQ12] | [MG03] | [DC03] | [VG03] | `TK12` |
| [REQ13] | [MG04] | [DC04] | [VG04] | `TK13` |
| [REQ14] | [MG05] | [DC05] | [VG05] | `TK14` |
| [REQ15] | [MG06] | [DC06] | [VG06] | `TK15`, `TK17` |

Audit result: no requirement in this plan lacks a design owner, contract,
validation gate, or task coverage. The [TK18] traceability block is therefore
not triggered. [WL05] is active within the bounded prototype scope.

## (6) Handoff rule [OUT]

> Goal: [GL06] - HAND_SOURCE_WORK_TO_A_FUTURE_AGENT
> Dependency: [DP06] - USER_APPROVAL_TO_START_WL05
> Requirement: [RQ06] - SOURCE_WORK_BEGINS_WITH_TESTABLE_CONTRACTS

A continuing source agent should use [TODO.md](../TODO.md) to select the next
unfinished source task and preserve the completed slices above. Write refusal
tests for the applicable gates before expanding behavior [VG01], [VG02],
[VG03], [VG04], [VG05], [VG06]. Any claim that needs a broader engine loop must
pass through [MG06] before it is promoted.

## (Y) Link-complete usage index [LC]

This section is non-authoritative. It invokes active markers so the registry
below remains link-complete [LC], [LN].

- Documents and workflow: [DOC], [D04], [D05], [D06], [WL05], [KN], [PL],
  [AC], [OUT]
- Requirements: [REQ01], [REQ02], [REQ03], [REQ04], [REQ05], [REQ06],
  [REQ07], [REQ08], [REQ09], [REQ10], [REQ11], [REQ12], [REQ13], [REQ14],
  [REQ15]
- Modules and contracts: [MG01], [MG02], [MG03], [MG04], [MG05], [MG06],
  [DC01], [DC02], [DC03], [DC04], [DC05], [DC06]
- Validation gates: [VG01], [VG02], [VG03], [VG04], [VG05], [VG06]
- Tasks and metadata: [TK16], [TK17], [TK18], [GL01], [GL02], [GL03],
  [GL04], [GL05], [GL06], [DP01], [DP02], [DP03], [DP04], [DP05], [DP06],
  [RQ01], [RQ02], [RQ03], [RQ04], [RQ05], [RQ06]

## (Z) Context-Citations

[DOC]: SOURCECODE_IMPLEMENTATION_PLAN
  "The source-facing implementation order and status for the bounded prototype."

[D04]: REQUIREMENTS_DOCUMENT
  "docs/requirements.md, the validated requirements document."

[D05]: DESIGN_DOCUMENT
  "docs/design.md, the validated design document."

[D06]: TASKLIST_DOCUMENT
  "docs/tasklist.md, the validated tasklist document."

[WL05]: DEVELOPMENT_SOURCECODE
  "The active bounded prototype source phase following docspec validation."

[KN]: KNOWLEDGE_GATE
  "The section that records the source-planning entry gate."

[PL]: IMPLEMENTATION_PLAN
  "The source-facing implementation order with completed slice status."

[VG]: VALIDATION_SPECIMEN_SET
  "The validation gates that must become runnable specimen tests."

[AC]: ACCEPTANCE_AUDIT
  "The traceability audit for source planning."

[OUT]: HANDOFF_RULE
  "The rule for a later source agent."

[LC]: LINK_COMPLETE_STATE
  "A state where every active marker is defined once and referenced."

[LN]: LINT_RULE
  "The rule that reference definitions belong only in the bottom registry."

[REQ01]: REQUIRE_SPINALTAP_NOT_CLONE
  "The engine must remain a SPINALTAP Constraint Engine, not a clone."

[REQ02]: REQUIRE_RESEARCH_PROTOTYPE
  "The first implementation target is a research prototype architecture."

[REQ03]: REQUIRE_VALIDATED_DOCSPEC_BEFORE_SOURCE
  "Runtime sourcecode must wait for validated requirements, design, and tasks."

[REQ04]: REQUIRE_CONTEXT_WEIGHT_GOVERNOR
  "The Context-Weight Governor must score source-pressured claims."

[REQ05]: REQUIRE_TIME_PACKET_PUMP
  "The Time Packet Pump must convert elapsed time into fixed packets."

[REQ06]: REQUIRE_SIGNAL_CONSTRAINT_SPINE
  "The Signal-Constraint Spine must route ordered signal bundles."

[REQ07]: REQUIRE_VERTEBRA_DELTA_WORKERS
  "Vertebra workers must operate only on local state slices."

[REQ08]: REQUIRE_STYLE_CONSTRAINT_SURFACE
  "The Style Constraint Surface must convert style claims into limits."

[REQ09]: REQUIRE_SOFT_PROOF_LAB
  "The Soft-Proof Lab must require specimen plans and failure paths."

[REQ10]: REQUIRE_ORIGINALITY_GATE
  "High-influence source or borrowed ideas must pass originality validation."

[REQ11]: REQUIRE_TIME_GATE
  "Solver-facing time must arrive as fixed packets."

[REQ12]: REQUIRE_SIGNAL_GATE
  "State mutation must route through a signal bundle."

[REQ13]: REQUIRE_SOLVER_GATE
  "Local solvers must prove ownership of their local state slice."

[REQ14]: REQUIRE_STYLE_GATE
  "Visual style claims must become measurable limits."

[REQ15]: REQUIRE_PROOF_GATE
  "Implementation-ready claims need runnable specimen plans and failure paths."

[MG01]: CONTEXT_WEIGHT_GOVERNOR_MODULE
  "Module for source influence and risk scoring."

[MG02]: TIME_PACKET_PUMP_MODULE
  "Module for converting elapsed time into fixed simulation packets."

[MG03]: SIGNAL_CONSTRAINT_SPINE_MODULE
  "Module for routing ordered signal bundles."

[MG04]: VERTEBRA_DELTA_WORKER_MODULE
  "Module family for local solvers and bounded deltas."

[MG05]: STYLE_CONSTRAINT_SURFACE_MODULE
  "Module for measurable style limits."

[MG06]: SOFT_PROOF_LAB_MODULE
  "Module for specimen plans, failure paths, and promotion records."

[DC01]: CONTEXT_WEIGHT_CONTRACT
  "Contract for source influence, risk flags, and governor decisions."

[DC02]: TIME_PACKET_CONTRACT
  "Contract for elapsed time, fixed packets, and interpolation state."

[DC03]: SIGNAL_BUNDLE_CONTRACT
  "Contract for owner, channel, ordered signal bundle, and validation hook."

[DC04]: VERTEBRA_DELTA_CONTRACT
  "Contract for local state slices, constraints, and bounded deltas."

[DC05]: STYLE_LIMIT_CONTRACT
  "Contract for measurable geometry, lighting, texture, and artifact limits."

[DC06]: PROOF_SPECIMEN_CONTRACT
  "Contract for claim proof records and promotion state."

[VG01]: ORIGINALITY_GATE
  "Gate for source influence and originality distance."

[VG02]: TIME_GATE
  "Gate that prevents raw elapsed time from reaching solvers."

[VG03]: SIGNAL_GATE
  "Gate that prevents direct global mutation."

[VG04]: SOLVER_GATE
  "Gate for local state ownership."

[VG05]: STYLE_GATE
  "Gate that requires style claims to become measurable limits."

[VG06]: PROOF_GATE
  "Gate requiring specimen plans and failure paths."

[TK16]: VALIDATE_DOCSPEC_TASK
  "Task to rerun link-completeness and markdownlint."

[TK17]: WRITE_SOURCE_PLAN_TASK
  "Task to write the sourcecode implementation plan."

[TK18]: SOURCE_BLOCK_TRACEABILITY_TASK
  "Task to keep sourcecode blocked if traceability is incomplete."

[GL01]: ENTER_SOURCE_PLANNING_ONLY_AFTER_DOCSPEC
  "Plan source work only after docspec validation."

[GL02]: BUILD_CONTRACT_KERNEL_FIRST
  "Start future source work with explicit records and refusal states."

[GL03]: IMPLEMENT_MODULES_IN_DEPENDENCY_ORDER
  "Order future source slices by contract dependencies."

[GL04]: TEST_REFUSAL_PATHS_FIRST
  "Validate refusal paths before promotion paths."

[GL05]: DECIDE_SOURCE_BLOCK_STATUS_FROM_TRACEABILITY
  "Use the traceability audit to decide whether source remains blocked."

[GL06]: HAND_SOURCE_WORK_TO_A_FUTURE_AGENT
  "Give a future source agent a bounded start rule."

[DP01]: VALIDATED_DOCSPEC_PACKAGE
  "The source plan depends on validated requirements, design, and tasklist."

[DP02]: EXPLICIT_DATA_CONTRACTS
  "The source plan depends on concrete data contracts."

[DP03]: MODULE_CONTRACT_SEQUENCE
  "The source plan depends on module dependency order."

[DP04]: VALIDATION_SPECIMENS
  "The source plan depends on planned validation specimens."

[DP05]: REQUIREMENT_TO_OWNER_MATRIX
  "The source block decision depends on traceability."

[DP06]: USER_APPROVAL_TO_START_WL05
  "The user's continuation instruction authorizes bounded prototype source work."

[RQ01]: NO_RUNTIME_SOURCECODE_IN_THIS_DOCUMENT
  "This document may plan source work but not start runtime sourcecode."

[RQ02]: REFUSAL_BEHAVIOR_BEFORE_FEATURE_BEHAVIOR
  "Future source work must implement refusal behavior before feature behavior."

[RQ03]: SMALL_REVIEWABLE_SOURCE_SLICES
  "Future source work must proceed through small reviewable slices."

[RQ04]: RUNNABLE_FAILURE_BEFORE_PROMOTION
  "Future source work must prove failure behavior before promotion."

[RQ05]: NO_UNOWNED_REQUIREMENT_ENTERS_SOURCE
  "A requirement may not enter source work without traceability."

[RQ06]: SOURCE_WORK_BEGINS_WITH_TESTABLE_CONTRACTS
  "Future source work starts with testable contracts."
