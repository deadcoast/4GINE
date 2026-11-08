# (A) 4GINE REQUIREMENTS: SPINALTAP CONSTRAINT ENGINE [DOC]

Current scope (2026-11-07): REQ01-REQ15 remain the prototype requirement
authority. Their initial docspec-before-source entry gate was satisfied for
the existing slices; it does not re-block authorized continuation. Changes
still need aligned requirements, design and task evidence through the
[development workflow](development_workflow.md). Application requirements must
be extended explicitly under the [global plan](global_plan.md).

Readiness interpretation: current implementation_ready proof records validate
planning structure, not executed results; style records currently validate
nonblank strings, not measurable budgets. REQ08/REQ14 and proof-evidence
semantics remain open under the [style](todos/style.md) and
[proof](todos/proof.md) cards. Requirement coverage is not satisfaction.

This requirements document is the first [WL04] docspec artifact. It converts
the proposal into testable conditions while preserving the context chain from
the research plan, live research pass, and proposal [D01], [D02], [D03].

Original entry condition: source began only after requirements, design and
tasklist alignment/validation [WL05]. The current scope notice above records
that this gate has been satisfied for existing authorized slices.

## (1) Context ledger [KN]

> Goal: [GL01] - REQUIREMENT_TRACEABILITY
> Dependency: [DP01] - DOCUMENT_CHAIN
> Requirement: [RQ01] - PRESERVE_CONTEXT_CHAIN

The current document chain is:

| Document | Owns | Must be preserved by this file |
| --- | --- | --- |
| [D01] | Research method and guardrails | truth, source handling, no copied methods |
| [D02] | Evidence and decision ledger | selected and revised theory candidates |
| [D03] | Proposal scope and contracts | modules, data contracts, validation gates |
| [D04] | Requirements | build conditions and acceptance criteria |

The requirements below must remain traceable to [D03]. Any requirement that
cannot point to a module, contract, or validation gate must be revised or
removed [KN].

## (2) Scope requirements [SC]

> Goal: [GL02] - BOUND_ENGINE_SCOPE
> Dependency: [DP02] - PROPOSAL_SCOPE
> Requirement: [RQ02] - SCOPE_IS_EXPLICIT

- [REQ01] The engine direction must remain a SPINALTAP Constraint Engine, not
  an ECS clone, scene-tree clone, physics-engine clone, or fixed-function
  renderer clone [DN01].
- [REQ02] The first implementation target must be a research prototype
  architecture, not a complete renderer or complete physics engine [SC].
- [REQ03] Runtime sourcecode must wait until [D04], [D05], and [D06] are
  complete and validated [WL05].

## (3) Module requirements [MG]

> Goal: [GL03] - DEFINE_REQUIRED_MODULES
> Dependency: [DP03] - PROPOSAL_MODULES
> Requirement: [RQ03] - MODULES_HAVE_CONTRACTS

- [REQ04] The Context-Weight Governor [MG01] must receive source-pressured
  claims and emit influence weight plus replication risk [DC01].
- [REQ05] The Time Packet Pump [MG02] must convert elapsed time into fixed
  simulation packets before any solver consumes time [DC02].
- [REQ06] The Signal-Constraint Spine [MG03] must route state changes through
  ordered signal bundles instead of hidden writes [DC03].
- [REQ07] Vertebra Delta Workers [MG04] must operate only on local state slices
  and emit bounded deltas plus residual risk [DC04].
- [REQ08] The Style Constraint Surface [MG05] must convert style profiles into
  measurable rendering and asset limits [DC05].
- [REQ09] The Soft-Proof Lab [MG06] must require a specimen plan, failure path,
  and promotion state before any claim becomes implementation-ready [DC06].

## (4) Data contract requirements [DC]

> Goal: [GL04] - REQUIRE_EXPLICIT_DATA_BOUNDARIES
> Dependency: [DP04] - CONTRACT_SET
> Requirement: [RQ04] - INPUT_OUTPUT_REFUSAL_DEFINED

Every contract must define input, output, and refusal behavior [DS03].

| Contract | Required input | Required output | Must refuse |
| --- | --- | --- | --- |
| [DC01] | source-pressured claim | influence weight, risk flag | hidden influence |
| [DC02] | elapsed time | fixed packets, interpolation state | raw dt in solvers |
| [DC03] | delta packets | ordered signal bundle | direct global mutation |
| [DC04] | local state, constraints, time packet | bounded delta, residual risk | ownership outside local slice |
| [DC05] | style profile | measurable limits | vague style labels |
| [DC06] | claim and contract | specimen plan, failure path, promotion state | proof by prose alone |

Exact required fields:

- [DC01] fields: `source_ref`, `claim_text`, `source_authority`,
  `claim_fit`, `originality_distance`, `validation_reach`,
  `influence_weight`, `risk_flag`, `governor_decision`.
- [DC02] fields: `elapsed_time`, `fixed_packet_size`, `packet_count`,
  `accumulator_remainder`, `interpolation_state`, `overflow_risk`.
- [DC03] fields: `owner`, `channel`, `ordered_signal_bundle`,
  `constraint_envelope`, `validation_hook`, `residual_risk`.
- [DC04] fields: `local_state_slice`, `constraint_set`, `time_packet`,
  `bounded_delta`, `residual_risk`.
- [DC05] fields: `geometry_limit`, `lighting_limit`, `texture_limit`,
  `color_limit`, `fog_limit`, `alpha_limit`, `depth_limit`,
  `camera_limit`, `animation_cadence`, `artifact_limits`.
- [DC06] fields: `claim_ref`, `contract_ref`, `specimen_plan`,
  `failure_path`, `promotion_state`, `evidence_tier`.

## (5) Validation requirements [VG]

> Goal: [GL05] - REQUIRE_VALIDATION_GATES
> Dependency: [DP05] - PROOF_LADDER
> Requirement: [RQ05] - EVIDENCE_BEFORE_ADVANCEMENT

- [REQ10] Every high-influence source or borrowed idea must pass [VG01] before
  it can affect the model [TR02].
- [REQ11] Every solver-facing time value must pass [VG02] by arriving as a
  fixed packet from [DC02].
- [REQ12] Every proposed state mutation must pass [VG03] by routing through a
  signal bundle from [DC03].
- [REQ13] Every local solver must pass [VG04] by proving ownership of only its
  local state slice [DC04].
- [REQ14] Every visual style claim must pass [VG05] by becoming a measurable
  limit through [DC05].
- [REQ15] Every implementation-ready claim must pass [VG06] with a runnable
  specimen plan and explicit failure path [EV05].

Validation specimens must be planned before sourcecode. Each specimen names the
input, the permitted output, the refusal condition, and the promotion rule:

- [VG01] originality specimen: one source-pressured claim from [DC01] is scored
  for source authority, claim fit, originality distance, and validation reach.
  The only permitted outcomes are allow, down-weight, or block [REQ10].
- [VG02] time specimen: one raw elapsed-time value is converted into fixed
  packets, accumulator remainder, interpolation state, and overflow risk before
  solver access [REQ11], [DC02].
- [VG03] signal specimen: one proposed bounded delta is wrapped in an ordered
  signal bundle with owner, channel, constraint envelope, validation hook, and
  residual risk before state publication [REQ12], [DC03].
- [VG04] solver specimen: one vertebra receives only its local state slice,
  constraint set, and time packet, then refuses any delta outside that slice
  [REQ13], [DC04].
- [VG05] style specimen: one style profile becomes measurable geometry,
  lighting, texture, color, fog, alpha, depth, camera, cadence, and artifact
  limits before visual acceptance [REQ14], [DC05].
- [VG06] proof specimen: one implementation-ready claim must produce a
  specimen plan, failure path, promotion state, and evidence tier before it can
  leave docspec status [REQ15], [DC06].

## (6) Risk requirements [RK]

> Goal: [GL06] - REQUIRE_RISK_CONTROLS
> Dependency: [DP06] - PROPOSAL_RISKS
> Requirement: [RQ06] - RISKS_HAVE_CONTROLS

| Risk | Requirement control |
| --- | --- |
| [RK01] architecture copy risk | [REQ04], [REQ10] |
| [RK02] temporal theory risk | [REQ05], [REQ11] |
| [RK03] solver import risk | [REQ07], [REQ13] |
| [RK04] style vagueness risk | [REQ08], [REQ14] |
| [RK05] proof by prose risk | [REQ09], [REQ15] |
| [RK06] metaphor-only module risk | [REQ04], [REQ05], [REQ06], [REQ07], [REQ08], [REQ09] |

## (7) Acceptance criteria [AC]

> Goal: [GL07] - DEFINE_ACCEPTANCE
> Dependency: [DP07] - REQUIREMENT_SET
> Requirement: [RQ07] - ACCEPTANCE_IS_AUDITABLE

The docspec package is acceptable when:

1. [D04] defines every in-scope requirement without placeholders.
2. [D05] maps each requirement to architecture, module ownership, data flow,
   and validation behavior.
3. [D06] maps every task to at least one requirement.
4. No document creates live pseudo-citation definitions above its registry.
5. Markdownlint and link-completeness checks pass for [D04], [D05], and [D06].

## (Y) Link-complete usage index [LC]

This section is non-authoritative. It invokes active markers so the registry
below remains link-complete [LC], [LN].

- Documents: [DOC], [D01], [D02], [D03], [D04], [D05], [D06], [WL04], [WL05]
- Knowledge and scope: [KN], [SC], [DN01], [DS03], [EV05], [TR02], [LC], [LN]
- Modules: [MG], [MG01], [MG02], [MG03], [MG04], [MG05], [MG06]
- Contracts: [DC], [DC01], [DC02], [DC03], [DC04], [DC05], [DC06]
- Validation and risks: [VG], [VG01], [VG02], [VG03], [VG04], [VG05], [VG06],
  [RK], [RK01], [RK02], [RK03], [RK04], [RK05], [RK06], [AC]
- Requirements: [REQ01], [REQ02], [REQ03], [REQ04], [REQ05], [REQ06],
  [REQ07], [REQ08], [REQ09], [REQ10], [REQ11], [REQ12], [REQ13], [REQ14],
  [REQ15]
- Goals: [GL01], [GL02], [GL03], [GL04], [GL05], [GL06], [GL07]
- Dependencies: [DP01], [DP02], [DP03], [DP04], [DP05], [DP06], [DP07]
- Requirement metadata: [RQ01], [RQ02], [RQ03], [RQ04], [RQ05], [RQ06], [RQ07]

## (Z) Context-Citations

[DOC]: REQUIREMENTS_DOCUMENT
  "The WL04 requirements artifact for the SPINALTAP Constraint Engine."

[D01]: RESEARCH_PLAN_DOCUMENT
  "docs/research_plan.md, the approved method and guardrail source."

[D02]: LIVE_RESEARCH_DOCUMENT
  "docs/live_research.md, the evidence and decision ledger."

[D03]: PROPOSAL_DOCUMENT
  "docs/proposal.md, the proposal source for scope, modules, contracts, gates,
  and risks."

[D04]: REQUIREMENTS_DOCUMENT_INSTANCE
  "docs/requirements.md, the current requirements document."

[D05]: DESIGN_DOCUMENT
  "docs/design.md, the companion architecture design document."

[D06]: TASKLIST_DOCUMENT
  "docs/tasklist.md, the companion ordered task document."

[WL04]: DEVELOPMENT_DOCSPEC
  "The workflow phase for requirements, design, and tasklist artifacts."

[WL05]: DEVELOPMENT_SOURCECODE
  "The sourcecode phase, blocked until the docspec package is validated."

[KN]: KNOWLEDGE_LEDGER
  "The document-context tracking layer that preserves method, evidence,
  proposal, requirements, design, and task knowledge."

[SC]: SCOPE_CONTROL
  "The requirement family that states what is in scope, out of scope, and
  blocked."

[DN01]: DATA_REPLICATION
  "The guardrail against lightly renamed copies of researched sources."

[DS03]: DATA_CONTRACT
  "The design object for input, output, ownership, and refusal boundaries."

[EV05]: DIRECT_INTERNAL_TEST
  "Direct internal test evidence for the exact tested claim. Current scalar
  specimens can occupy this tier without establishing rendering, performance
  or complete-engine acceptance."

[TR02]: REPLICATION_RISK_CHECK
  "The originality check that rejects copied source structure."

[LC]: LINK_COMPLETE_STATE
  "A state where every active marker has one definition and at least one
  reference."

[LN]: LINT_RULE
  "The pseudo-citation validation rule that keeps definitions in the registry."

[MG]: MODULE_GROUP
  "The set of proposed SPINALTAP Constraint Engine modules."

[MG01]: CONTEXT_WEIGHT_GOVERNOR_MODULE
  "Module that scores source influence and replication risk."

[MG02]: TIME_PACKET_PUMP_MODULE
  "Module that converts elapsed time into fixed simulation packets."

[MG03]: SIGNAL_CONSTRAINT_SPINE_MODULE
  "Module that routes ordered signal bundles for spinal-column aggregation."

[MG04]: VERTEBRA_DELTA_WORKER_MODULE
  "Module family for local solvers emitting bounded deltas."

[MG05]: STYLE_CONSTRAINT_SURFACE_MODULE
  "Module that converts style profiles into measurable limits."

[MG06]: SOFT_PROOF_LAB_MODULE
  "Module that creates specimen plans, failure paths, and promotion records."

[DC]: DATA_CONTRACT_SET
  "The contract family for module inputs, outputs, and refusal behavior."

[DC01]: CONTEXT_WEIGHT_CONTRACT
  "Receive a source-pressured claim; output influence weight and risk flag."

[DC02]: TIME_PACKET_CONTRACT
  "Receive elapsed time; output fixed packets and interpolation state."

[DC03]: SIGNAL_BUNDLE_CONTRACT
  "Receive delta packets; output ordered signal bundles."

[DC04]: VERTEBRA_DELTA_CONTRACT
  "Receive local state, constraints, and time packet; output bounded delta and
  residual risk."

[DC05]: STYLE_LIMIT_CONTRACT
  "Receive a style profile; output measurable rendering and asset limits."

[DC06]: PROOF_SPECIMEN_CONTRACT
  "Receive a claim and contract; output specimen plan, failure path, and
  promotion state."

[VG]: VALIDATION_GATE_SET
  "The gate family that blocks advancement until evidence conditions pass."

[VG01]: ORIGINALITY_GATE
  "Gate requiring context weight and replication-risk review."

[VG02]: TIME_GATE
  "Gate requiring solvers to consume fixed time packets."

[VG03]: SIGNAL_GATE
  "Gate requiring state changes to route through signal bundles."

[VG04]: SOLVER_GATE
  "Gate requiring local solver ownership and bounded delta output."

[VG05]: STYLE_GATE
  "Gate requiring style claims to become measurable limits."

[VG06]: PROOF_GATE
  "Gate requiring runnable specimens and failure paths."

[RK]: RISK_SET
  "The known proposal risk family."

[RK01]: ARCHITECTURE_COPY_RISK
  "Risk that the architecture becomes a renamed ECS or scene tree."

[RK02]: TEMPORAL_THEORY_RISK
  "Risk that timing remains theoretical."

[RK03]: SOLVER_IMPORT_RISK
  "Risk that solver language imports physics-engine architecture."

[RK04]: STYLE_VAGUENESS_RISK
  "Risk that style remains descriptive instead of measurable."

[RK05]: PROOF_BY_PROSE_RISK
  "Risk that claims advance without specimens or tests."

[RK06]: METAPHOR_ONLY_MODULE_RISK
  "Risk that module names keep metaphor but lack contracts."

[AC]: ACCEPTANCE_CRITERIA
  "The conditions that make the docspec package acceptable."

[REQ01]: ENGINE_IDENTITY_REQUIREMENT
  "The engine must remain a SPINALTAP Constraint Engine, not a researched-source
  clone."

[REQ02]: RESEARCH_PROTOTYPE_REQUIREMENT
  "The first implementation target must be a research prototype architecture."

[REQ03]: SOURCECODE_BLOCK_REQUIREMENT
  "Runtime sourcecode waits until the docspec package is validated."

[REQ04]: CONTEXT_WEIGHT_REQUIREMENT
  "The Context-Weight Governor must emit influence weight and replication risk."

[REQ05]: TIME_PACKET_REQUIREMENT
  "The Time Packet Pump must emit fixed simulation packets before solver use."

[REQ06]: SIGNAL_SPINE_REQUIREMENT
  "The Signal-Constraint Spine must prevent hidden global writes."

[REQ07]: VERTEBRA_REQUIREMENT
  "Vertebra workers must operate on local state and emit bounded deltas."

[REQ08]: STYLE_CONSTRAINT_REQUIREMENT
  "The Style Constraint Surface must emit measurable style limits."

[REQ09]: SOFT_PROOF_REQUIREMENT
  "The Soft-Proof Lab must require specimen plans and failure paths."

[REQ10]: ORIGINALITY_VALIDATION_REQUIREMENT
  "High-influence sources must pass originality review before model influence."

[REQ11]: TIME_VALIDATION_REQUIREMENT
  "Solver-facing time must arrive as fixed packets."

[REQ12]: SIGNAL_VALIDATION_REQUIREMENT
  "State mutation must route through signal bundles."

[REQ13]: SOLVER_VALIDATION_REQUIREMENT
  "Local solvers must prove ownership of their local state slice."

[REQ14]: STYLE_VALIDATION_REQUIREMENT
  "Style claims must become measurable limits."

[REQ15]: PROOF_VALIDATION_REQUIREMENT
  "Implementation-ready claims require a runnable specimen plan and failure
  path."

[GL01]: REQUIREMENT_TRACEABILITY
  "Preserve document-chain traceability."

[GL02]: BOUND_ENGINE_SCOPE
  "State explicit scope and sourcecode block."

[GL03]: DEFINE_REQUIRED_MODULES
  "Define required modules and their contract obligations."

[GL04]: REQUIRE_EXPLICIT_DATA_BOUNDARIES
  "Require input, output, and refusal behavior."

[GL05]: REQUIRE_VALIDATION_GATES
  "Require evidence gates before advancement."

[GL06]: REQUIRE_RISK_CONTROLS
  "Connect known risks to requirement controls."

[GL07]: DEFINE_ACCEPTANCE
  "Define acceptance criteria for the docspec package."

[DP01]: DOCUMENT_CHAIN
  "The dependency on research_plan, live_research, proposal, requirements,
  design, and tasklist staying traceable."

[DP02]: PROPOSAL_SCOPE
  "The proposal's selected scope and blocked directions."

[DP03]: PROPOSAL_MODULES
  "The module set defined by the proposal."

[DP04]: CONTRACT_SET
  "The data contract set defined by the proposal."

[DP05]: PROOF_LADDER
  "The soft-proof ladder and validation gate set."

[DP06]: PROPOSAL_RISKS
  "The risk set recorded by the proposal."

[DP07]: REQUIREMENT_SET
  "The complete requirements in this document."

[RQ01]: PRESERVE_CONTEXT_CHAIN
  "Requirements must preserve the document and knowledge chain."

[RQ02]: SCOPE_IS_EXPLICIT
  "Scope must state included, excluded, and blocked work."

[RQ03]: MODULES_HAVE_CONTRACTS
  "Each required module must have a contract."

[RQ04]: INPUT_OUTPUT_REFUSAL_DEFINED
  "Each contract must define input, output, and refused behavior."

[RQ05]: EVIDENCE_BEFORE_ADVANCEMENT
  "Claims must satisfy evidence gates before advancement."

[RQ06]: RISKS_HAVE_CONTROLS
  "Risks must have explicit controls."

[RQ07]: ACCEPTANCE_IS_AUDITABLE
  "Acceptance criteria must be checkable by a future agent."
