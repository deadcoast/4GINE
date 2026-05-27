# (A) 4GINE PROPOSAL: SPINALTAP CONSTRAINT ENGINE [DOC]

This proposal is the next research step after the approved research plan
[D01] and first live research pass [D02]. It converts source-pressured theory
into a scoped engine direction without starting sourcecode [WL03], [WL04],
[WL05].

The proposal target is a research-first, three-dimensional engine architecture
where modules emit bounded signals, the spinal column reconciles them, and
validation decides whether a claim can advance [SA01], [SA02], [SA03], [SP].

## (1) Document and knowledge ledger [KN]

> Goal: [GL01] - PRESERVE_DOCUMENT_CONTEXT
> Dependency: [DP01] - DOCUMENT_CHAIN
> Requirement: [RQ01] - TRACEABLE_KNOWLEDGE

The active document chain is:

| Document | Role | Knowledge preserved | Current output |
| --- | --- | --- | --- |
| [D01] | Method source | Research rules, guardrails, pseudo-citation rules | Controls how future agents research |
| [D02] | Evidence source | Source records, lane decisions, SPINALTAP formulations | Supplies selected and revised theory |
| [D03] | Proposal source | Scope, modules, data contracts, validation gates | Guides docspec work |

The durable knowledge chain is:

- [KN01] method: no boilerplate, no copied methods, no weak-source laundering.
- [KN02] evidence: accepted and revised claims only, with source limits.
- [KN03] synthesis: [FR01] through [FR06] as original SPINALTAP formulations.
- [KN04] decisions: selected, revised, rejected, and deferred outcomes.
- [KN05] handoff: proposal decisions must map cleanly into [WL04].

## (2) Proposal thesis [DS01]

> Goal: [GL02] - SELECT_ENGINE_DIRECTION
> Dependency: [DP02] - RESEARCH_DECISIONS
> Requirement: [RQ02] - PROPOSAL_READINESS

4GINE should move forward as a SPINALTAP Constraint Engine [DS01]. The engine
is not an ECS clone, a scene-tree clone, a physics-engine clone, or a
fixed-function renderer clone [DN01], [RD03]. It is a modular state engine
whose smallest useful unit is a bounded delta packet, whose coordination layer
is a typed signal spine, and whose style target is a measurable constraint
surface [FR01], [FR02], [FR04].

The accepted core is:

- [TH03] Context-Weight Governor becomes a mandatory influence gate [MG01].
- [TH06] Temporal Coherence Controller becomes the first runtime architecture
  invariant [MG02].

The revised theory set becomes proposal material only through explicit
contracts: [TH01] and [TH08] through [FR01], [TH02] through [FR02], [TH04] and
[TH07] through [FR04], and [TH05] through [FR06] [RD02].

## (3) Engine scope [DS01]

> Goal: [GL03] - DEFINE_ENGINE_SCOPE
> Dependency: [DP03] - SELECTED_THEORY
> Requirement: [RQ03] - SCOPE_CONTROL

In scope:

- A research prototype architecture for a three-dimensional engine [SY].
- Explicit module ownership through [SA01], [SA02], and [SA03].
- Time packet handling before solver execution [FR03].
- Signal and delta packet contracts before global state mutation [FR01],
  [FR02].
- Style constraints as measurable limits, not mood labels [FR04].
- Proof gates that require runnable specimens before implementation-ready
  claims [FR06].

Out of scope:

- Full renderer implementation.
- Full physics engine implementation.
- Runtime sourcecode before [WL04] produces requirements, design, and tasks.
- Pixel-art framing or any direct clone of a researched source [DN01],
  [RD03].

## (4) Module proposal [MO]

> Goal: [GL04] - DEFINE_MODULE_BOUNDARIES
> Dependency: [DP04] - FORMULATION_SET
> Requirement: [RQ04] - MODULE_CONTRACTS

### (4.1) Context-Weight Governor [MG01]

The governor controls source and design influence before a claim changes the
model [TH03], [CW]. It scores authority, claim fit, originality distance, and
validation reach [FR05].

Contract: receive a source-pressured claim, output allowed influence and
replication risk [DC01].

### (4.2) Time Packet Pump [MG02]

The pump owns elapsed time conversion [TH06]. It turns render-frame elapsed
time into fixed simulation packets before any vertebra consumes time [FR03].

Contract: receive elapsed time, output ordered simulation packets and
presentation interpolation state [DC02].

### (4.3) Signal-Constraint Spine [MG03]

The spine routes subsystem arguments into the spinal column [FR01]. A signal
is a typed proposal, not final state [SA03].

Contract: receive delta packets, output ordered signal bundles with constraint
envelopes and validation hooks [DC03].

### (4.4) Vertebra Delta Workers [MG04]

Vertebrae are local constraint workers [SA02]. They do not mutate global state
directly. They emit bounded deltas plus residual risk [FR02].

Contract: receive a local state slice, constraint set, and time packet; output
a bounded delta packet [DC04].

### (4.5) Style Constraint Surface [MG05]

The style layer translates retro 3D language into measurable engine limits
[TH04], [TH07], [SY]. It constrains geometry, lighting, texture behavior,
color, fog, alpha, depth, camera, animation cadence, and allowed artifacts
[FR04].

Contract: receive a style profile, output numeric or categorical limits for
rendering and asset decisions [DC05].

### (4.6) Soft-Proof Lab [MG06]

The validation layer turns proposal claims into small runnable specimens,
failure-path checks, and acceptance records before implementation work [TH05],
[FR06].

Contract: receive a claim and its data contract, output a specimen plan,
failure condition, and promotion state [DC06].

## (5) Data contracts [DS03]

> Goal: [GL05] - DEFINE_DATA_CONTRACTS
> Dependency: [DP05] - MODULE_BOUNDARIES
> Requirement: [RQ05] - INPUT_OUTPUT_REFUSAL

| Contract | Input | Output | Refuses |
| --- | --- | --- | --- |
| [DC01] | Source-pressured claim | Influence weight, risk flag | Hidden source influence |
| [DC02] | Elapsed time | Fixed packets, interpolation state | Raw dt in solvers |
| [DC03] | Delta packets | Ordered signal bundle | Direct global mutation |
| [DC04] | Local state, constraints, dt packet | Bounded delta, residual risk | Ownership outside local slice |
| [DC05] | Style profile | Measurable limits | Vague aesthetic labels |
| [DC06] | Claim and contract | Specimen plan, failure path | Proof by prose alone |

## (6) Validation gates [DS04]

> Goal: [GL06] - DEFINE_VALIDATION_GATES
> Dependency: [DP06] - SOFT_PROOF_LADDER
> Requirement: [RQ06] - EVIDENCE_BEFORE_ADVANCEMENT

- [VG01] Originality gate: the claim passes [TR02] and records context weight.
- [VG02] Time gate: solvers consume [DC02] packets, not raw frame time.
- [VG03] Signal gate: state changes arrive through [DC03], not hidden writes.
- [VG04] Solver gate: each vertebra owns only its local state slice [DC04].
- [VG05] Style gate: style claims become measurable [DC05] limits.
- [VG06] Proof gate: implementation-ready claims need a specimen and failure
  path [DC06], [EV05].

## (7) Risk ledger [DS05]

> Goal: [GL07] - RECORD_RISKS
> Dependency: [DP07] - RESEARCH_LIMITS
> Requirement: [RQ07] - RISKS_VISIBLE

| Risk | Description | Control |
| --- | --- | --- |
| [RK01] | Architecture becomes a renamed ECS or scene tree | [MG01], [VG01] |
| [RK02] | Temporal model stays theoretical | [MG02], [VG02], [DC02] |
| [RK03] | Solver language imports physics-engine architecture | [MG04], [VG04] |
| [RK04] | Style remains descriptive instead of measurable | [MG05], [VG05] |
| [RK05] | Proof claims advance without tests | [MG06], [VG06] |
| [RK06] | Module names keep metaphor but lack contracts | [DC01], [DC06] |

## (8) Handoff to docspec [OUT]

> Goal: [GL08] - DOCSPEC_HANDOFF
> Dependency: [DP08] - PROPOSAL_OUTPUT
> Requirement: [RQ08] - READY_FOR_REQUIREMENTS

The next document package should be [WL04]. It should create:

1. `requirements.md`: requirements from [DC01] through [DC06] and [VG01]
   through [VG06].
2. `design.md`: architecture for [MG01] through [MG06].
3. `tasklist.md`: ordered work from context tracking to validation specimen.

The proposal does not authorize [WL05] sourcecode yet. It authorizes docspec
work that preserves the chain from [D01] to [D02] to [D03] [KN05].

## (Y) Link-complete usage index [LC]

This section is non-authoritative. It invokes active markers so the registry
below remains link-complete [LC], [LN].

- Document markers: [DOC], [D01], [D02], [D03], [FM], [GR], [LC], [LN],
  [WL02], [WL03], [WL04], [WL05], [OUT]
- Knowledge markers: [KN], [KN01], [KN02], [KN03], [KN04], [KN05]
- Theory and formulation markers: [TH01], [TH02], [TH03], [TH04], [TH05],
  [TH06], [TH07], [TH08], [FR], [FR01], [FR02], [FR03], [FR04], [FR05],
  [FR06]
- Engine markers: [SA01], [SA02], [SA03], [AS], [SY], [MO], [CW], [DN01],
  [SP], [EV05], [TR02]
- Design markers: [DS01], [DS03], [DS04], [DS05], [RD02], [RD03]
- Module markers: [MG01], [MG02], [MG03], [MG04], [MG05], [MG06]
- Contract markers: [DC01], [DC02], [DC03], [DC04], [DC05], [DC06]
- Validation markers: [VG01], [VG02], [VG03], [VG04], [VG05], [VG06]
- Risk markers: [RK01], [RK02], [RK03], [RK04], [RK05], [RK06]
- Goal markers: [GL01], [GL02], [GL03], [GL04], [GL05], [GL06], [GL07],
  [GL08]
- Dependency markers: [DP01], [DP02], [DP03], [DP04], [DP05], [DP06],
  [DP07], [DP08]
- Requirement markers: [RQ01], [RQ02], [RQ03], [RQ04], [RQ05], [RQ06],
  [RQ07], [RQ08]

## (Z) Context-Citations

[DOC]: PROPOSAL_DOCUMENT
  "The WL03 proposal artifact that converts research decisions into engine
  scope, module boundaries, data contracts, validation gates, and risks."

[D01]: RESEARCH_PLAN_DOCUMENT
  "docs/research_plan.md, the approved method source for live research,
  guardrails, source handling, and proposal readiness."

[D02]: LIVE_RESEARCH_DOCUMENT
  "docs/live_research.md, the first live research pass containing source
  records, lane decisions, and original SPINALTAP formulations."

[D03]: PROPOSAL_DOCUMENT_INSTANCE
  "docs/proposal.md, the current proposal document and next context source for
  docspec work."

[FM]: FORMAT_MODEL
  "The pseudo-citation document model where body markers reference a bottom
  registry."

[GR]: GUARDRAILS
  "Novelty, truth, source handling, and anti-replication constraints."

[LC]: LINK_COMPLETE_STATE
  "The state where every active marker is defined once and referenced at least
  once."

[LN]: LINT_RULE
  "The rule that pseudo-citation syntax should validate without lint
  suppression."

[WL02]: RESEARCH_WORKFLOW
  "The workflow phase that pressure-tests theory with source records and
  decisions."

[WL03]: PROPOSAL_WORKFLOW
  "The workflow phase that turns selected research into scope, contracts, and
  validation gates."

[WL04]: DEVELOPMENT_DOCSPEC
  "The workflow phase that creates requirements, design, and tasklist
  documents."

[WL05]: DEVELOPMENT_SOURCECODE
  "The sourcecode phase, blocked until docspec artifacts are ready."

[OUT]: OUTPUT_HANDOFF
  "The handoff state from proposal into docspec work."

[KN]: KNOWLEDGE_LEDGER
  "The document-context and knowledge-tracking layer for the research family."

[KN01]: METHOD_KNOWLEDGE
  "Rules for source handling, originality, citation format, and research
  discipline."

[KN02]: EVIDENCE_KNOWLEDGE
  "Source records, decisions, source limits, and evidence tiers."

[KN03]: SYNTHESIS_KNOWLEDGE
  "Original SPINALTAP formulations derived from source pressure."

[KN04]: DECISION_KNOWLEDGE
  "Selected, revised, rejected, and deferred outcomes."

[KN05]: HANDOFF_KNOWLEDGE
  "The mapping from proposal into requirements, design, tasklist, and later
  sourcecode."

[TH01]: SIGNAL_ROUTING_SPINE
  "Theory candidate for converting module outputs into typed signals before
  spinal-column aggregation."

[TH02]: VERTEBRAE_LOCAL_SOLVERS
  "Theory candidate for bounded local solver units that emit corrections or
  transitions."

[TH03]: CONTEXT_WEIGHT_GOVERNOR
  "Accepted theory candidate for limiting outside influence and replication
  risk."

[TH04]: STYLE_CONSTRAINT_LAYER
  "Revised theory candidate for treating style as measurable constraints."

[TH05]: SOFT_PROOF_PIPELINE
  "Revised theory candidate for advancing claims through evidence and runnable
  validation."

[TH06]: TEMPORAL_COHERENCE_CONTROLLER
  "Accepted theory candidate for fixed packets, solver order, and presentation
  coherence."

[TH07]: VISUAL_METRIC_TRANSLATOR
  "Revised theory candidate for translating style language into measurable
  rendering and asset limits."

[TH08]: SCOPE_BOUNDARY_ALLOCATOR
  "Revised theory candidate for assigning formulas to nervous_system,
  vertebrae, or spinal_column layers."

[FR]: FORMULATION
  "An original SPINALTAP-local synthesis produced by live research."

[FR01]: SIGNAL_CONSTRAINT_SPINE
  "Formulation where subsystem outputs become typed signals with constraint
  envelopes."

[FR02]: STEM_DELTA_PACKET
  "Formulation where vertebrae emit bounded deltas and residual risk."

[FR03]: TIME_PACKET_PUMP
  "Formulation where elapsed time becomes fixed simulation packets."

[FR04]: STYLE_CONSTRAINT_VECTOR
  "Formulation where style becomes measurable rendering and presentation
  limits."

[FR05]: CONTEXT_WEIGHT_GOVERNOR
  "Formulation that caps source influence by authority, claim fit, originality
  distance, and validation reach."

[FR06]: SOFT_PROOF_LADDER
  "Formulation that moves claims from prose to source pressure, translation,
  runnable specimen, failure check, and proposal-ready requirement."

[SA01]: NERVOUS_SYSTEM
  "Broad but bounded domain owner for engine behavior families."

[SA02]: VERTEBRAE
  "Local solver, transform unit, or scoped formulation."

[SA03]: SPINAL_COLUMN
  "Aggregation and reconciliation layer for higher-order engine state."

[AS]: ALGORITHMIC_STEM
  "A modular operation model where scoped stems solve assigned jobs and pass
  bounded results upward."

[SY]: STYLE
  "Formal rendering or presentation style represented as constraints."

[MO]: MODULE_OBJECT
  "Implementation-facing module marker that connects theory to future source
  and docs."

[CW]: CONTEXT_WEIGHT
  "The allowed influence weight of discovered source material or prior theory."

[DN01]: DATA_REPLICATION
  "The guardrail against lightly renamed replicas of source material."

[SP]: SOFT_PROVEN
  "A proposal-readiness standard based on coherent reasoning, evidence, and
  validation."

[EV05]: DIRECT_INTERNAL_TEST
  "The evidence tier reserved for future prototype or engine tests."

[TR02]: REPLICATION_RISK_CHECK
  "The check that rejects output whose structure remains too close to a source."

[DS01]: ENGINE_SCOPE
  "Design object defining what the proposal includes, excludes, and postpones."

[DS03]: DATA_CONTRACT
  "Design object defining inputs, outputs, ownership, and refusal boundaries."

[DS04]: VALIDATION_GATE
  "Design object defining advancement conditions for claims and modules."

[DS05]: RISK_LEDGER
  "Design object recording unresolved risks and controls."

[RD02]: REVISE_DECISION
  "Decision state where a theory remains useful only after scope or contract
  changes."

[RD03]: REJECT_DECISION
  "Decision state where a direction is outside evidence, originality, or
  proposal guardrails."

[MG01]: CONTEXT_WEIGHT_GOVERNOR_MODULE
  "Module proposal for source influence scoring and originality risk."

[MG02]: TIME_PACKET_PUMP_MODULE
  "Module proposal for converting elapsed time into fixed simulation packets."

[MG03]: SIGNAL_CONSTRAINT_SPINE_MODULE
  "Module proposal for routing typed signal bundles into spinal aggregation."

[MG04]: VERTEBRA_DELTA_WORKER_MODULE
  "Module proposal for local solvers that emit bounded deltas."

[MG05]: STYLE_CONSTRAINT_SURFACE_MODULE
  "Module proposal for measurable retro 3D style constraints."

[MG06]: SOFT_PROOF_LAB_MODULE
  "Module proposal for runnable specimens, failure paths, and promotion
  records."

[DC01]: CONTEXT_WEIGHT_CONTRACT
  "Contract for receiving source-pressured claims and outputting influence and
  risk."

[DC02]: TIME_PACKET_CONTRACT
  "Contract for receiving elapsed time and outputting fixed simulation packets."

[DC03]: SIGNAL_BUNDLE_CONTRACT
  "Contract for receiving delta packets and outputting ordered signal bundles."

[DC04]: VERTEBRA_DELTA_CONTRACT
  "Contract for local state, constraints, time packet, bounded delta, and
  residual risk."

[DC05]: STYLE_LIMIT_CONTRACT
  "Contract for translating style profile input into measurable rendering
  limits."

[DC06]: PROOF_SPECIMEN_CONTRACT
  "Contract for claim, specimen plan, failure path, and promotion state."

[VG01]: ORIGINALITY_GATE
  "Validation gate requiring context weight and replication-risk review."

[VG02]: TIME_GATE
  "Validation gate requiring solvers to consume time packets rather than raw
  frame time."

[VG03]: SIGNAL_GATE
  "Validation gate requiring state changes to route through typed signal
  bundles."

[VG04]: SOLVER_GATE
  "Validation gate requiring local solver ownership and bounded delta output."

[VG05]: STYLE_GATE
  "Validation gate requiring style claims to become measurable limits."

[VG06]: PROOF_GATE
  "Validation gate requiring runnable specimens and failure paths before
  implementation readiness."

[RK01]: ARCHITECTURE_COPY_RISK
  "Risk that the project becomes a renamed ECS or scene-tree architecture."

[RK02]: TEMPORAL_THEORY_RISK
  "Risk that timing remains theoretical without packet-level validation."

[RK03]: SOLVER_IMPORT_RISK
  "Risk that solver language imports a physics-engine architecture."

[RK04]: STYLE_VAGUENESS_RISK
  "Risk that style remains descriptive instead of measurable."

[RK05]: PROOF_BY_PROSE_RISK
  "Risk that proof claims advance without tests or specimens."

[RK06]: METAPHOR_ONLY_MODULE_RISK
  "Risk that module names preserve metaphor but lack input-output contracts."

[GL01]: PRESERVE_DOCUMENT_CONTEXT
  "Track which document owns method, evidence, proposal, and handoff knowledge."

[GL02]: SELECT_ENGINE_DIRECTION
  "Select a proposal direction from accepted and revised theory."

[GL03]: DEFINE_ENGINE_SCOPE
  "State what the proposal includes, excludes, and postpones."

[GL04]: DEFINE_MODULE_BOUNDARIES
  "Define the first module set and their responsibilities."

[GL05]: DEFINE_DATA_CONTRACTS
  "Define input, output, and refusal rules for proposed modules."

[GL06]: DEFINE_VALIDATION_GATES
  "Define evidence gates before a claim can advance."

[GL07]: RECORD_RISKS
  "Record risks and controls for proposal and docspec work."

[GL08]: DOCSPEC_HANDOFF
  "Prepare the next document package without starting sourcecode."

[DP01]: DOCUMENT_CHAIN
  "The dependency on research_plan, live_research, and proposal staying
  traceable."

[DP02]: RESEARCH_DECISIONS
  "The selected and revised decisions from live_research."

[DP03]: SELECTED_THEORY
  "The accepted core theories and revised candidates allowed into proposal."

[DP04]: FORMULATION_SET
  "The FR01 through FR06 formulations produced by live research."

[DP05]: MODULE_BOUNDARIES
  "The proposed module set and their explicit ownership boundaries."

[DP06]: SOFT_PROOF_LADDER
  "The validation ladder that blocks implementation-ready claims until
  specimens and failure paths exist."

[DP07]: RESEARCH_LIMITS
  "Source and validation limits recorded by the live research pass."

[DP08]: PROPOSAL_OUTPUT
  "The proposal's module, contract, validation, and risk outputs."

[RQ01]: TRACEABLE_KNOWLEDGE
  "Each document and knowledge object must have an explicit role."

[RQ02]: PROPOSAL_READINESS
  "The proposal must identify selected theory, revised theory, rejected
  directions, and contracts."

[RQ03]: SCOPE_CONTROL
  "The proposal must say what is in scope, out of scope, and blocked."

[RQ04]: MODULE_CONTRACTS
  "Each proposed module must define its role and contract."

[RQ05]: INPUT_OUTPUT_REFUSAL
  "Each data contract must include inputs, outputs, and refused behavior."

[RQ06]: EVIDENCE_BEFORE_ADVANCEMENT
  "Claims must pass validation gates before implementation readiness."

[RQ07]: RISKS_VISIBLE
  "Known proposal risks must be recorded with controls."

[RQ08]: READY_FOR_REQUIREMENTS
  "The proposal must hand cleanly to requirements, design, and tasklist docs."
