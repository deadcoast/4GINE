# (A) 4GINE DESIGN: SPINALTAP CONSTRAINT ENGINE [DOC]

This design document is the second [WL04] docspec artifact. It explains how
the requirements become architecture, module boundaries, data flow, and
validation behavior [D04].

The design defines the architecture for the bounded source prototype now in
[WL05]. Implementation status lives in [sourcecode_plan.md](sourcecode_plan.md)
and the remaining source tasks live in [TODO.md](../TODO.md).

## (1) Context and architecture stance [KN]

> Goal: [GL01] - ARCHITECTURE_CONTEXT
> Dependency: [DP01] - REQUIREMENT_SOURCE
> Requirement: [RQ01] - DESIGN_TRACEABILITY

The design consumes the document chain [D01] through [D04] and produces [D05].
It preserves three rules:

1. Research is pressure, not a copy source [DN01].
2. Modules need explicit contracts before sourcecode [DC].
3. Claims need validation gates before implementation readiness [VG].

Architecture stance: 4GINE is a modular state engine. Broad domains own
families of behavior [SA01]. Local workers transform bounded state [SA02]. The
spinal column orders, reconciles, and publishes higher-order state [SA03].

## (2) Architecture overview [AR]

> Goal: [GL02] - DEFINE_ARCHITECTURE
> Dependency: [DP02] - PROPOSAL_MODULES
> Requirement: [RQ02] - ARCHITECTURE_HAS_BOUNDARIES

The engine has six first-class design modules [MG]:

1. [MG01] Context-Weight Governor.
2. [MG02] Time Packet Pump.
3. [MG03] Signal-Constraint Spine.
4. [MG04] Vertebra Delta Workers.
5. [MG05] Style Constraint Surface.
6. [MG06] Soft-Proof Lab.

The primary flow is:

```txt
source pressure -> MG01 -> accepted claim influence
elapsed time -> MG02 -> fixed time packets
local state + constraints + time packet -> MG04 -> delta packet
delta packets -> MG03 -> ordered signal bundle
style profile -> MG05 -> measurable limits
claim + contract -> MG06 -> specimen plan + failure path
```

No module owns global state directly. Global state is an output of
spinal-column reconciliation after signal bundles are ordered and checked
[SA03], [VG03].

## (3) Module designs [MG]

> Goal: [GL03] - DESIGN_MODULES
> Dependency: [DP03] - MODULE_REQUIREMENTS
> Requirement: [RQ03] - MODULES_ARE_SEPARABLE

### (3.1) Context-Weight Governor [MG01]

Purpose: prevent source material or prior theory from controlling the final
model [REQ04].

Inputs: source-pressured claim, source authority, claim fit, originality
distance, validation reach [DC01].

Outputs: influence weight, replication risk, and allowed downstream use.

Failure behavior: if originality distance is low, the governor must output
LOW influence or block model influence [VG01].

### (3.2) Time Packet Pump [MG02]

Purpose: isolate elapsed render-frame time from solver execution [REQ05].

Inputs: elapsed time and accumulated remainder [DC02].

Outputs: fixed simulation packets, interpolation state, and overflow risk.

Failure behavior: if elapsed time exceeds the safe packet budget, the pump
must emit overflow risk instead of passing raw dt to solvers [VG02].

### (3.3) Signal-Constraint Spine [MG03]

Purpose: route proposed state changes as typed, ordered signals [REQ06].

Inputs: bounded delta packets from [MG04] and optional style limits from
[MG05] [DC03].

Outputs: ordered signal bundle with owner, channel, constraint envelope,
validation hook, and residual risk.

Failure behavior: if a packet lacks owner, channel, or validation hook, the
spine refuses it before aggregation [VG03].

### (3.4) Vertebra Delta Workers [MG04]

Purpose: perform local transformations without hidden global mutation [REQ07].

Inputs: local state slice, constraint set, and time packet [DC04].

Outputs: bounded delta and residual risk.

Failure behavior: if a worker needs state outside its declared slice, it must
emit refusal or risk rather than expanding ownership silently [VG04].

### (3.5) Style Constraint Surface [MG05]

Purpose: make retro 3D style decisions measurable [REQ08].

Inputs: style profile and target constraints [DC05].

Outputs: geometry, lighting, texture, color, fog, alpha, depth, camera,
animation, and artifact limits [FR04].

Failure behavior: if a style claim cannot become a limit, it stays out of
implementation-ready design [VG05].

### (3.6) Soft-Proof Lab [MG06]

Purpose: stop claims from advancing by prose alone [REQ09].

Inputs: claim, data contract, validation gate, and expected failure path
[DC06].

Outputs: specimen plan, failure condition, promotion state, and evidence tier.

Failure behavior: if a claim lacks a specimen plan or failure path, it remains
below implementation-ready status [VG06], [EV05].

## (4) Data model [DM]

> Goal: [GL04] - DEFINE_DATA_MODEL
> Dependency: [DP04] - CONTRACT_SET
> Requirement: [RQ04] - DATA_IS_EXPLICIT

The design uses these conceptual records:

```txt
SourceClaim =
  { source_ref, claim_text, source_authority, claim_fit,
    originality_distance, validation_reach, influence_weight,
    risk_flag, governor_decision }

TimePacket =
  { elapsed_time, fixed_packet_size, packet_count, accumulator_remainder,
    interpolation_state, overflow_risk }

SignalBundle =
  { owner, channel, ordered_signal_bundle, constraint_envelope,
    validation_hook, residual_risk }

DeltaPacket =
  { local_state_slice, constraint_set, time_packet, bounded_delta,
    residual_risk }

StyleLimits =
  { geometry_limit, lighting_limit, texture_limit, color_limit, fog_limit,
    alpha_limit, depth_limit, camera_limit, animation_cadence,
    artifact_limits }

ProofRecord =
  { claim_ref, contract_ref, specimen_plan, failure_path, promotion_state,
    evidence_tier }
```

Field ownership:

- [DC01] owns `source_authority`, `claim_fit`, `originality_distance`,
  `validation_reach`, `influence_weight`, and `risk_flag`.
- [DC02] owns `elapsed_time`, `fixed_packet_size`, `packet_count`,
  `accumulator_remainder`, `interpolation_state`, and `overflow_risk`.
- [DC03] owns `owner`, `channel`, `ordered_signal_bundle`,
  `constraint_envelope`, `validation_hook`, and `residual_risk`.
- [DC04] owns `local_state_slice`, `constraint_set`, `time_packet`,
  `bounded_delta`, and `residual_risk`.
- [DC05] owns `geometry_limit`, `lighting_limit`, `texture_limit`,
  `color_limit`, `fog_limit`, `alpha_limit`, `depth_limit`, `camera_limit`,
  `animation_cadence`, and `artifact_limits`.
- [DC06] owns `claim_ref`, `contract_ref`, `specimen_plan`, `failure_path`,
  `promotion_state`, and `evidence_tier`.

These are design records, not final code types. Their purpose is to force
ownership, input, output, and refusal behavior before sourcecode [DS03].

### (4.1) Runtime mapping ingress [DC]

> Goal: [GL04] - DEFINE_DATA_MODEL
> Dependency: [DP04] - CONTRACT_SET
> Requirement: [RQ04] - DATA_IS_EXPLICIT

`spinaltap/contract_validation.py` implements the root source TODO task `TK04`
for [DC01] through [DC06]. `parse_contract(contract, payload)` accepts a
complete mapping or a matching record, returning a validated record or raising
`ContractValidationError`. The error carries a field path and a blocked
`invalid_payload` refusal attributed to the failing contract and gate [DS03].

The ingress rules are:

- Every declared field is required, including nullable fields. Unknown fields
  and nonstring or blank mapping keys are refused.
- [DC01] scores and non-null influence weight must be finite numbers in
  `0..1`. Boolean values and numeric strings are refused. Missing source
  attribution remains representable so [MG01] can issue its influence refusal.
- [DC02] elapsed time and remainder must be finite and nonnegative; fixed
  packet size must also be positive. Packet count must be a nonnegative
  integer excluding booleans, and interpolation must be in `0..1`. Overflow
  backlog may exceed one packet. These checks do not certify pump provenance
  or the consistency of independently supplied timing fields.
- [DC03] signals must be a list or tuple. Every nested [DC04] delta and its
  [DC02] time packet is validated, including existing dataclass instances.
  Errors identify the failing signal index and field. A residual refusal must
  have a known code, matching contract and gate, and blocked promotion state.
- Mapping fields receive shallow, read-only snapshots with string keys.
  Their values remain opaque to this decoder. The worker and spine apply the
  scalar ownership and magnitude rules below; conflicts and nested value
  schemas remain future module work.
- [DC05] fields must be nonblank strings in this slice. Numeric style budgets
  remain pending. [DC06] uses known contract and promotion enum values;
  specimen and failure text may be blank so [VG06] can record the specific
  missing-plan or missing-failure refusal. Truthy non-text values are invalid.

The style surface, specimen hooks, workers, and spine use this boundary.
Direct dataclass constructors remain trusted internal APIs; workers and the
spine revalidate records before acceptance. Other external callers must use
`parse_contract` before invoking typed modules. Shape validation does not
execute a specimen, establish source authority, or grant publication rights.
The proof lab also refuses a validation gate that belongs to another reviewed
contract [VG01], [VG03], [VG06].

### (4.2) Fixed-step solver boundary [DC02]

> Goal: [GL04] - DEFINE_DATA_MODEL
> Dependency: [DP04] - CONTRACT_SET
> Requirement: [RQ04] - DATA_IS_EXPLICIT

Root TODO task `TK06` makes [MG02] the conversion boundary for [REQ05] and
[VG02]. `TimePacketPump.step` accepts finite, nonnegative elapsed time and
remainder, with a positive fixed size and integer execution budget in
`1..4096`. It retains excess time as backlog and marks packet-budget overflow.
Accumulated-time overflow is refused. Division boundaries snap within four
floating-point ULPs, capped at one billionth of the fixed size, to avoid losing
a step to representational rounding while preserving smaller fractions.

`pump.solver_steps(frame_packet)` verifies the configured size and budget,
then emits zero or more [DC02] records. Each has count one, elapsed time equal
to fixed size, zero remainder and interpolation, and no overflow flag. Frame
diagnostics remain in the original packet. `solver_packets` remains a checked
compatibility projection of fixed durations; new worker callers use records.

[MG04] requires a single expanded step. Raw numbers or mappings raise a
`ContractValidationError` carrying `raw_dt`; malformed records, frame batches,
zero-step packets, and unconsumed frame metadata carry `invalid_payload`.
The reconciliation harness converts these failures to empty refused bundles
before signal acceptance. These checks validate the supplied values, without
claiming authenticated packet provenance [VG02], [VG03].

### (4.3) Scalar delta constraints [DC04]

> Goal: [GL04] - DEFINE_DATA_MODEL
> Dependency: [DP04] - CONTRACT_SET
> Requirement: [RQ04] - DATA_IS_EXPLICIT

Root TODO task `TK07` implements [REQ07] and [VG04]. A worker refuses an input
state slice containing keys outside its registered local keys, as well as any
proposed key absent from the local slice. The current constraint schema is
exactly `max_delta`: a finite nonnegative number. Unsupported rules, missing
limits, numeric strings, booleans, and nonfinite numbers are refused.

Every proposed value must be a finite scalar and satisfy
`abs(delta[key]) <= max_delta`. The limit applies separately to each component
for one fixed step. A zero budget permits zero updates. If any component fails,
the whole proposal returns an empty bounded delta and a refusal; components
are neither clamped nor partially accepted. Vector norms, per-key limits,
cross-worker conflicts, and general state schemas remain pending [VG04].

### (4.4) Executed signal validation hooks [DC03]

> Goal: [GL05] - DESIGN_VALIDATION
> Dependency: [DP05] - VALIDATION_REQUIREMENTS
> Requirement: [RQ05] - FAILURE_PATHS_VISIBLE

Root TODO task `TK08` implements the hook boundary for [REQ06] and [VG03].
`SignalConstraintSpine` registers named synchronous callables; `VG03` is the
built-in acceptance hook after mandatory checks. Blank, duplicate, and
noncallable registrations are rejected.

Before any hook runs, the spine validates record shape, the constraint envelope
(including empty bundles), worker residual refusals, fixed-step time, local
delta ownership, and both worker and envelope scalar budgets. It preserves
worker refusals and rejects the entire bundle if any member fails. Custom
hooks cannot skip these checks [VG02], [VG03], [VG04].

A hook receives the validated bundle and returns `None` to accept or a
`RefusalState` to refuse. Unknown names, exceptions, unexpected return values,
or malformed refusal metadata produce `validation_failed` and an empty bundle.
Hooks see shallow read-only mappings; nested state objects remain opaque.
Hooks are trusted synchronous code, with no timeout or external side-effect
isolation in this slice. Registration is a local lookup, not a channel or
worker authorization registry [VG03].

Accepted bundles are eligible for the caller's publication policy. The scalar
demo applies them to demo-owned state, but the engine still lacks a general
state publisher, multi-worker conflict merge, and transaction model [MG03].

## (5) Validation design [VG]

> Goal: [GL05] - DESIGN_VALIDATION
> Dependency: [DP05] - VALIDATION_REQUIREMENTS
> Requirement: [RQ05] - FAILURE_PATHS_VISIBLE

Validation is module-local first and spinal-column-wide second:

- [VG01] checks source influence before model change.
- [VG02] checks fixed packet use before solver execution.
- [VG03] checks signal completeness before aggregation.
- [VG04] checks local ownership before delta acceptance.
- [VG05] checks measurable style limits before visual design acceptance.
- [VG06] checks specimen and failure path before implementation readiness.

The validation design intentionally delays [EV05] until a later prototype or
engine test exists.

Specimen definitions:

- [VG01] runs a [DC01] claim through [MG01]. It records `source_authority`,
  `claim_fit`, `originality_distance`, and `validation_reach`, then emits
  `influence_weight`, `risk_flag`, and a decision of allow, down-weight, or
  block. A claim fails if it has hidden influence, no `source_ref`, or a copied
  structure presented as original.
- [VG02] runs one elapsed-time sample through [MG02]. It emits a [DC02] packet
  with packet count, accumulator remainder, interpolation state, and overflow
  risk. It fails if any solver receives raw elapsed time.
- [VG03] runs one bounded delta through [MG03]. It emits a [DC03] signal bundle
  with owner, channel, `ordered_signal_bundle`, constraint envelope,
  validation hook, and residual risk. It fails on direct state mutation or
  missing order data.
- [VG04] runs one vertebra update through [MG04]. It emits a [DC04] bounded
  delta only for the declared local state slice. It fails if the update reads
  or writes outside the slice without an explicit refusal.
- [VG05] runs one style profile through [MG05]. It emits [DC05] limits for
  geometry, lighting, texture, color, fog, alpha, depth, camera, animation
  cadence, and `artifact_limits`. It fails if the profile remains a mood label.
- [VG06] runs one claim through [MG06]. It emits a [DC06] proof record with a
  specimen plan, failure path, promotion state, and evidence tier. It fails if
  the claim depends on prose confidence instead of runnable proof.

## (6) Risk handling [RK]

> Goal: [GL06] - DESIGN_RISK_CONTROLS
> Dependency: [DP06] - REQUIREMENT_RISKS
> Requirement: [RQ06] - RISKS_ARE_DESIGNED_AGAINST

- [RK01] is controlled by [MG01] and [VG01].
- [RK02] is controlled by [MG02] and [VG02].
- [RK03] is controlled by [MG04] and [VG04].
- [RK04] is controlled by [MG05] and [VG05].
- [RK05] is controlled by [MG06] and [VG06].
- [RK06] is controlled by all [DC] records.

## (7) Handoff to tasklist [OUT]

> Goal: [GL07] - TASK_HANDOFF
> Dependency: [DP07] - DESIGN_OUTPUT
> Requirement: [RQ07] - TASKS_CAN_BE_DERIVED

The tasklist must create work items in this order:

1. Preserve document context.
2. Lock requirements.
3. Detail architecture records.
4. Define validation specimens.
5. Build sourcecode plan only after docspec review.

## (Y) Link-complete usage index [LC]

This section is non-authoritative. It invokes active markers so the registry
below remains link-complete [LC], [LN].

- Documents: [DOC], [D01], [D02], [D03], [D04], [D05], [D06], [WL04], [WL05]
- Context and architecture: [KN], [AR], [SA01], [SA02], [SA03], [DN01],
  [DS03], [LC], [LN], [OUT]
- Requirements and formulations: [REQ04], [REQ05], [REQ06], [REQ07], [REQ08],
  [REQ09], [FR04], [EV05]
- Modules: [MG], [MG01], [MG02], [MG03], [MG04], [MG05], [MG06]
- Contracts and data: [DC], [DC01], [DC02], [DC03], [DC04], [DC05], [DC06],
  [DM]
- Gates and risks: [VG], [VG01], [VG02], [VG03], [VG04], [VG05], [VG06],
  [RK], [RK01], [RK02], [RK03], [RK04], [RK05], [RK06]
- Goals: [GL01], [GL02], [GL03], [GL04], [GL05], [GL06], [GL07]
- Dependencies: [DP01], [DP02], [DP03], [DP04], [DP05], [DP06], [DP07]
- Requirement metadata: [RQ01], [RQ02], [RQ03], [RQ04], [RQ05], [RQ06], [RQ07]

## (Z) Context-Citations

[DOC]: DESIGN_DOCUMENT
  "The WL04 architecture design artifact for the SPINALTAP Constraint Engine."

[D01]: RESEARCH_PLAN_DOCUMENT
  "docs/research_plan.md, the approved method and guardrail source."

[D02]: LIVE_RESEARCH_DOCUMENT
  "docs/live_research.md, the evidence and decision ledger."

[D03]: PROPOSAL_DOCUMENT
  "docs/proposal.md, the proposal source."

[D04]: REQUIREMENTS_DOCUMENT
  "docs/requirements.md, the companion requirements document."

[D05]: DESIGN_DOCUMENT_INSTANCE
  "docs/design.md, the current design document."

[D06]: TASKLIST_DOCUMENT
  "docs/tasklist.md, the companion ordered task document."

[WL04]: DEVELOPMENT_DOCSPEC
  "The workflow phase for requirements, design, and tasklist artifacts."

[WL05]: DEVELOPMENT_SOURCECODE
  "The bounded prototype source phase entered after docspec validation."

[KN]: KNOWLEDGE_CONTEXT
  "The tracked method, evidence, proposal, requirements, design, and task
  context."

[AR]: ARCHITECTURE
  "The high-level engine design stance and module relationship model."

[SA01]: NERVOUS_SYSTEM
  "Broad domain owner for engine behavior families."

[SA02]: VERTEBRAE
  "Local solver, transform unit, or scoped formulation."

[SA03]: SPINAL_COLUMN
  "Aggregation and reconciliation layer for higher-order engine state."

[DN01]: DATA_REPLICATION
  "The guardrail against lightly renamed copies of researched sources."

[DS03]: DATA_CONTRACT
  "Input, output, ownership, and refusal boundary model."

[LC]: LINK_COMPLETE_STATE
  "A state where every active marker is defined once and referenced."

[LN]: LINT_RULE
  "The pseudo-citation rule that definitions live in the registry."

[OUT]: OUTPUT_HANDOFF
  "The handoff from design into tasklist and later planning."

[REQ04]: CONTEXT_WEIGHT_REQUIREMENT
  "Requirement for source influence and replication-risk output."

[REQ05]: TIME_PACKET_REQUIREMENT
  "Requirement for fixed packet output before solver use."

[REQ06]: SIGNAL_SPINE_REQUIREMENT
  "Requirement for signal-bundled state mutation."

[REQ07]: VERTEBRA_REQUIREMENT
  "Requirement for local state ownership and bounded deltas."

[REQ08]: STYLE_CONSTRAINT_REQUIREMENT
  "Requirement for measurable style limits."

[REQ09]: SOFT_PROOF_REQUIREMENT
  "Requirement for specimen plans and failure paths."

[FR04]: STYLE_CONSTRAINT_VECTOR
  "The formulation that converts style into measurable limits."

[EV05]: DIRECT_INTERNAL_TEST
  "The future evidence tier reserved for direct prototype or engine tests."

[MG]: MODULE_GROUP
  "The proposed SPINALTAP Constraint Engine modules."

[MG01]: CONTEXT_WEIGHT_GOVERNOR_MODULE
  "Module that scores source influence and replication risk."

[MG02]: TIME_PACKET_PUMP_MODULE
  "Module that converts elapsed time into fixed simulation packets."

[MG03]: SIGNAL_CONSTRAINT_SPINE_MODULE
  "Module that routes signal bundles for spinal aggregation."

[MG04]: VERTEBRA_DELTA_WORKER_MODULE
  "Module family for local solvers emitting bounded deltas."

[MG05]: STYLE_CONSTRAINT_SURFACE_MODULE
  "Module that converts style profiles into measurable limits."

[MG06]: SOFT_PROOF_LAB_MODULE
  "Module that creates specimen plans and failure paths."

[DC]: DATA_CONTRACT_SET
  "The set of module input, output, and refusal contracts."

[DC01]: CONTEXT_WEIGHT_CONTRACT
  "Claim influence and replication-risk contract."

[DC02]: TIME_PACKET_CONTRACT
  "Elapsed-time to fixed-packet contract."

[DC03]: SIGNAL_BUNDLE_CONTRACT
  "Delta-packet to signal-bundle contract."

[DC04]: VERTEBRA_DELTA_CONTRACT
  "Local-state to bounded-delta contract."

[DC05]: STYLE_LIMIT_CONTRACT
  "Style-profile to measurable-limit contract."

[DC06]: PROOF_SPECIMEN_CONTRACT
  "Claim to specimen-plan and failure-path contract."

[DM]: DATA_MODEL
  "The conceptual record set used by the design."

[VG]: VALIDATION_GATE_SET
  "The evidence and advancement gate family."

[VG01]: ORIGINALITY_GATE
  "Gate requiring context weight and replication-risk review."

[VG02]: TIME_GATE
  "Gate requiring fixed packet use."

[VG03]: SIGNAL_GATE
  "Gate requiring signal bundle routing."

[VG04]: SOLVER_GATE
  "Gate requiring local solver ownership."

[VG05]: STYLE_GATE
  "Gate requiring measurable style limits."

[VG06]: PROOF_GATE
  "Gate requiring specimen and failure path."

[RK]: RISK_SET
  "The known proposal and design risks."

[RK01]: ARCHITECTURE_COPY_RISK
  "Risk that architecture becomes a renamed external pattern."

[RK02]: TEMPORAL_THEORY_RISK
  "Risk that timing remains theoretical."

[RK03]: SOLVER_IMPORT_RISK
  "Risk that solver language imports physics-engine architecture."

[RK04]: STYLE_VAGUENESS_RISK
  "Risk that style remains descriptive."

[RK05]: PROOF_BY_PROSE_RISK
  "Risk that claims advance without tests."

[RK06]: METAPHOR_ONLY_MODULE_RISK
  "Risk that module names lack contracts."

[GL01]: ARCHITECTURE_CONTEXT
  "Preserve context while defining architecture."

[GL02]: DEFINE_ARCHITECTURE
  "Define the high-level architecture and flow."

[GL03]: DESIGN_MODULES
  "Design separable modules with purpose, inputs, outputs, and failure behavior."

[GL04]: DEFINE_DATA_MODEL
  "Define conceptual records for future implementation planning."

[GL05]: DESIGN_VALIDATION
  "Design validation behavior and failure paths."

[GL06]: DESIGN_RISK_CONTROLS
  "Connect risks to design controls."

[GL07]: TASK_HANDOFF
  "Prepare the tasklist derivation."

[DP01]: REQUIREMENT_SOURCE
  "The requirements document and upstream documents."

[DP02]: PROPOSAL_MODULES
  "The proposal's module set."

[DP03]: MODULE_REQUIREMENTS
  "The requirements governing each module."

[DP04]: CONTRACT_SET
  "The contract set from requirements."

[DP05]: VALIDATION_REQUIREMENTS
  "The validation gates from requirements."

[DP06]: REQUIREMENT_RISKS
  "The risk controls from requirements."

[DP07]: DESIGN_OUTPUT
  "The completed design artifacts needed for task derivation."

[RQ01]: DESIGN_TRACEABILITY
  "Design must trace to upstream requirements and proposal decisions."

[RQ02]: ARCHITECTURE_HAS_BOUNDARIES
  "Architecture must define ownership and module boundaries."

[RQ03]: MODULES_ARE_SEPARABLE
  "Modules must be independently understandable."

[RQ04]: DATA_IS_EXPLICIT
  "Conceptual records must make data movement explicit."

[RQ05]: FAILURE_PATHS_VISIBLE
  "Validation must show failure behavior."

[RQ06]: RISKS_ARE_DESIGNED_AGAINST
  "Risks must have architecture controls."

[RQ07]: TASKS_CAN_BE_DERIVED
  "The design must support an ordered tasklist."
