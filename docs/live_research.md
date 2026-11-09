# (A) 4GINE LIVE RESEARCH PASS 01: SPINALTAP ENGINE CONSTRAINTS [DOC]

Historical scope notice (2026-11-07): this is the original 2026-05-26 research
pass. Keep its source dates, formulations and dispositions as provenance.
Current delivery work follows the [global plan](global_plan.md).
The [new technical review](../research_notes/4GINE%20development%20realignment/technical_research.md)
records refreshed sources and the unresolved FR05 minimum-versus-runtime-mean
decision; it does not silently replace this historical formulation.

2026-11-09 supersession note: the
[governor policy decision](decisions/governor_policy.md) retains FR05's minimum
and supplies the authoritative outcome partition, input validation, risk flags
and exact threshold behavior for ST-008. It supersedes the incomplete
operational policy here and the current runtime mean, while preserving this
research snapshot and its original source dates.

This document records the first live research pass authorized on 2026-05-26
[DOC]. It follows the approved research plan's rule that research is evidence
pressure, not a copy source [WL02], [GR], [TR].

The result is not a proposal yet. It is a decision ledger that states what
source material supports, what it does not prove, and which SPINALTAP
formulations can move forward [RD], [OUT].

## (1) Method and guardrails [WL02]

> Goal: [GL01] - LIVE_RESEARCH_PASS
> Dependency: [DP01] - APPROVED_RESEARCH_PLAN
> Requirement: [RQ01] - TRUTHFUL_ORIGINAL_SYNTHESIS

The pass used one claim per lane, authoritative sources first, and no forum
material as proof [SQ]. Forum material was not needed for this pass because the
selected claims had stronger official documentation, standards, papers, and
technical articles available [SQ01], [SQ02].

Each lane was reduced to four outputs [RD]:

1. A tested claim.
2. Source pressure and source limits.
3. SPINALTAP-local translation.
4. A decision: accept, revise, reject, or defer.

## (2) Source intake [RS]

> Goal: [GL02] - SOURCE_INTAKE
> Dependency: [DP02] - AUTHORITATIVE_SOURCE_SET
> Requirement: [RQ02] - NO_BOILERPLATE_SUMMARIES

The source set is intentionally mixed [RS]. Engine architecture lanes use
official engine documentation. Solver and timing lanes use engine documentation,
a primary simulation paper record, and a technical article by the original
author. Originality uses ACM policy because it directly defines plagiarism risk
for technical ideas, code, equations, and creative work [RS06]. Rendering style
uses Khronos and Microsoft material because the style question needs pipeline
capability constraints rather than aesthetic labels [RS08], [RS09].

| Source | Lanes | Decision value | Limit |
| --- | --- | --- | --- |
| [RS01] | [RL01], [RL07] | ECS supports decoupled data and logic. | Do not clone Bevy's architecture. |
| [RS02] | [RL01], [RL07] | Scene trees support compositional ownership. | Godot node order is not a universal engine rule. |
| [RS03] | [RL02], [RL03] | Solver substeps and fixed steps bound simulation. | Box2D is 2D rigid-body specific. |
| [RS04] | [RL02] | Position projection supports local correction. | PBD is not a general engine architecture. |
| [RS05] | [RL03] | Accumulator timing separates render and physics. | Article guidance still needs local tests. |
| [RS06] | [RL04] | Attribution alone does not permit copied structure. | Publication policy is ethics guidance, not an engine method. |
| [RS07] | [RL05] | OpenGL registry anchors historical specs. | Registry is mostly an index. |
| [RS08] | [RL05] | Fixed function becomes measurable state. | Wiki page is weaker than a spec. |
| [RS09] | [RL05] | Direct3D 9 exposes pipeline capability axes. | Direct3D does not define all sixth-generation hardware. |
| [RS10] | [RL06] | Engine tests should live beside engine code. | Godot C++ testing is not the target engine's exact stack. |
| [RS11] | [RL06], [RL07] | Examples and testbeds need clear goals and behavior. | Bevy contribution style is not binding here. |

## (3) Lane decisions [RD]

### (3.1) Engine-state routing [RL01]

> Goal: [GL03] - ENGINE_STATE_ROUTING
> Dependency: [DP03] - DATA_OWNERSHIP_MODELS
> Requirement: [RQ03] - TRACEABLE_SIGNAL_FLOW

Claim tested: SPINALTAP can route module output as typed state signals before
final aggregation [TH01], [TH08], [SA03].

Source pressure: Bevy separates app logic into entities, components, and
systems, with schedules and explicit ordering when needed [RS01]. Godot's
stable documentation treats scenes as node trees, activates nodes through the
scene tree, and gives tree order operational meaning [RS02]. Together they
support the claim that state routing needs ownership and order, but they do not
prove that one universal ownership model is best [EV03], [EV04].

SPINALTAP translation: [SA01] owns broad domains, [SA02] emits typed deltas,
and [SA03] is the only layer allowed to reconcile competing deltas into the
next visible engine state [TR03].

Decision: [RD02] revise [TH01] and [TH08]. Keep signal routing, but define
each signal by owner, channel, input boundary, emitted delta, ordering need,
and validation hook [FR01], [FR02].

### (3.2) Local solver behavior [RL02]

> Goal: [GL04] - LOCAL_SOLVER_BOUNDARIES
> Dependency: [DP04] - CONSTRAINT_SOLVER_EVIDENCE
> Requirement: [RQ04] - NO_IMPORTED_SOLVER_ARCHITECTURE

Claim tested: vertebrae can be bounded local solvers that transform state,
resolve constraints, and emit corrections [TH02], [SA02].

Source pressure: Box2D's simulation docs support fixed world steps,
sub-stepping for accuracy, contact impulses, and solver detail control [RS03].
The PBD paper record supports a position-focused correction method where
constraints can be resolved by projecting points to valid locations [RS04].
The useful extraction is not the Box2D or PBD method; it is the shared boundary
principle: a solver must own a small target, run under a time or iteration
budget, and emit a bounded correction [TR01], [TR02].

SPINALTAP translation: a vertebra is a constraint worker, not a physics engine.
It receives a local state slice, a constraint set, and a time slice; it emits a
delta plus residual risk instead of silently mutating global state [FR02].

Decision: [RD02] revise [TH02]. Keep local solvers, but require each vertebra
to declare state ownership, constraint type, time budget, correction output,
and failure residue.

### (3.3) Temporal coherence [RL03]

> Goal: [GL05] - TEMPORAL_COHERENCE
> Dependency: [DP05] - FIXED_STEP_AND_ACCUMULATOR
> Requirement: [RQ03] - TRACEABLE_SIGNAL_FLOW

Claim tested: engine time should be consumed as discrete simulation packets,
while rendering reads interpolated or otherwise presentation-safe state [TH06].

Source pressure: Box2D recommends fixed time steps and uses sub-steps for
solver accuracy [RS03]. Fiedler's article shows why variable delta time can
change simulation behavior, then uses an accumulator to consume fixed time
steps and interpolation to reduce visible stutter [RS05]. The article is not a
formal proof, but it directly pressures the architecture toward a time-owner
boundary [EV03].

SPINALTAP translation: [SA03] should own a time packet pump. [SA02] solvers do
not read raw frame time. They receive fixed dt slices or declared sub-slices and
return deltas that can be reconciled before presentation [FR03].

Decision: [RD01] accept [TH06] as a core proposal candidate. The future design
should separate simulation time, render time, and presentation interpolation
before any sourcecode begins.

### (3.4) Context weight and originality [RL04]

> Goal: [GL06] - ORIGINALITY_CONTROL
> Dependency: [DP06] - SOURCE_INFLUENCE_LIMIT
> Requirement: [RQ01] - TRUTHFUL_ORIGINAL_SYNTHESIS

Claim tested: context weight can prevent research from becoming method theft or
near-verbatim theory reuse [TH03], [CW], [TR].

Source pressure: ACM defines plagiarism broadly enough to include writings,
ideas, code, equations, charts, and other creative work when misrepresented as
one's own [RS06]. It also treats near-verbatim copying and intentional
paraphrase as risks, so attribution is necessary but not enough when the output
still preserves source structure [TR02], [TR05].

SPINALTAP translation: context weight must measure influence, not authority
alone. A high-authority source can still receive LOW design influence when it
would overwrite the SPINALTAP structure [CW], [DN01].

Decision: [RD01] accept [TH03]. Use the context-weight governor as a required
gate before any high-influence source changes theory [FR05].

## (4) Style, validation, and boundary lanes [RD]

### (4.1) Style constraint mathematics [RL05]

Claim tested: retro 3D style can become a measurable constraint surface rather
than a visual mood board [TH04], [TH07], [SY].

Source pressure: Khronos hosts OpenGL specifications and older 1.x material
[RS07]. Khronos wiki material describes fixed-function rendering as
configuration-state-driven legacy OpenGL with hard-coded transform, lighting,
texture environment, and fog behavior [RS08]. Microsoft Direct3D 9
documentation exposes a pipeline vocabulary around vertex data, primitive data,
vertex processing, texture sampling, pixel processing, depth, stencil, alpha,
and fog [RS09]. These sources support constraint axes, not a copied renderer
[EV03].

SPINALTAP translation: style becomes a vector of limits: geometry density,
vertex lighting, texture behavior, color and fog, alpha/depth behavior, camera
distance, animation cadence, and artifact allowance [FR04].

Decision: [RD02] revise [TH04] and [TH07]. Keep the style layer, but require
measurable style vectors before design claims enter [WL03].

### (4.2) Soft-proof and validation [RL06]

Claim tested: soft proof must include runnable checks, samples, or test cases,
not only argument quality [TH05], [SP].

Source pressure: Godot's engine documentation describes C++ tests in a
dedicated tests directory, test filtering, assertions, and failure-path checks
[RS10]. Box2D's samples application includes demos, tuning, pause/single-step,
debug drawing, performance data, and test cases [RS03], [RS10]. Bevy's
contribution guidance says examples need goals, working behavior, clarity,
relevance, and minimal scope, while stress tests and testbeds can validate
special behavior [RS11].

SPINALTAP translation: soft proof is a ladder. A claim can advance from prose
to acceptance only after it has a small runnable specimen, a failure path, and a
validation artifact tied to one theory marker [FR06].

Decision: [RD02] revise [TH05]. The proof pipeline must require runnable
specimens or tests before any claim is treated as implementation-ready [EV04],
[EV05].

### (4.3) Module boundary mapping [RL07]

Claim tested: module boundaries should follow state ownership and validation
responsibility, not only the nervous-system metaphor [DS02], [DS03], [MO].

Source pressure: Bevy's ECS source suggests a data/logic split and explicit
ordering when order matters [RS01]. Godot's scene model suggests composition
and activation through a tree [RS02]. Bevy's example guidance pressures
implementation artifacts toward one clear goal, minimal scope, and appropriate
organization [RS11].

SPINALTAP translation: a module boundary is valid only when it names owned
state, input channels, output deltas, ordering constraints, and tests. A
module that only has a metaphor name is not ready for [WL04] or [WL05] [FR06].

Decision: [RD02] revise [DS02], [DS03], and [MO]. Keep the module families, but
require explicit contracts before docspec work starts.

## (5) Innovative SPINALTAP formulations [FR]

> Goal: [GL07] - SYNTHESIZED_FORMULATIONS
> Dependency: [DP06] - SOURCE_INFLUENCE_LIMIT
> Requirement: [RQ05] - PROPOSAL_READY_LANGUAGE

The following formulations are original project translations from source
pressure. They are not copied methods or theories [TR02].

### (5.1) Signal-Constraint Spine [FR01]

SPINALTAP should treat every engine subsystem output as a typed signal with a
constraint envelope. The signal is not final state. It is an argument submitted
to the spinal column for reconciliation [SA03].

```txt
signal = {
  owner_domain,
  source_vertebra,
  channel,
  input_slice,
  proposed_delta,
  constraint_envelope,
  validation_hook,
  residual_risk
}
```

### (5.2) Stem Delta Packet [FR02]

A vertebra emits bounded deltas, not hidden mutations [SA02]. The packet makes
solver behavior inspectable and lets [SA03] reject or re-order outputs.

```txt
delta_packet = vertebra(local_state, constraints, dt_slice)
```

### (5.3) Time Packet Pump [FR03]

The renderer produces elapsed time; the temporal spine converts it into fixed
simulation packets. Solvers consume packets. Presentation receives reconciled
state plus interpolation data [TH06].

### (5.4) Style Constraint Vector [FR04]

Style should become a vector of measurable constraints instead of a prose label:
geometry budget, lighting model, texture behavior, color limit, fog, alpha,
depth, camera, animation cadence, and allowed artifacts [TH04], [TH07].

### (5.5) Context-Weight Governor [FR05]

Context weight is a gate:

```txt
context_weight =
  min(authority, claim_fit, originality_distance, validation_reach)
```

A source cannot receive HIGH influence unless it improves the local model
without controlling its final structure [CW], [DN01], [TR02].

### (5.6) Soft-Proof Ladder [FR06]

The proof ladder for proposal work is:

```txt
prose claim
  -> source-pressured constraint
  -> SPINALTAP translation
  -> runnable specimen or test
  -> failure-path check
  -> proposal-ready requirement
```

## (6) Readiness gate [OUT]

> Goal: [GL08] - RESEARCH_GATE
> Dependency: [DP06] - SOURCE_INFLUENCE_LIMIT
> Requirement: [RQ06] - PROPOSAL_GATE

Selected candidates: [TH03] and [TH06] can move forward as core proposal
constraints [RD01].

Revised candidates: [TH01], [TH02], [TH04], [TH05], [TH07], and [TH08] remain
active but require the formulations in [FR01], [FR02], [FR04], and [FR06]
before proposal work [RD02].

Rejected directions: direct ECS cloning, direct Godot scene-tree cloning,
direct Box2D/PBD solver copying, fixed-function renderer cloning, and
boilerplate source summaries are outside the project guardrails [RD03],
[TR02].

Deferred work: exact hardware targets, benchmark thresholds, prototype tests,
and final module names require proposal and docspec work after this research
pass [RD04], [EV05].

The next safe step is [WL03]: write a proposal that turns [FR01] through [FR06]
into engine scope, module boundaries, data contracts, and validation gates
[OUT].

## (Y) Link-complete usage index [LC]

This section is non-authoritative. It invokes every active marker so the
registry below remains link-complete [LC], [LN].

- Document markers: [DOC], [FM], [WL02], [WL03], [WL04], [WL05], [GR], [LC],
  [LN], [OUT]
- Source and method markers: [RS], [RS01], [RS02], [RS03], [RS04], [RS05],
  [RS06], [RS07], [RS08], [RS09], [RS10], [RS11], [SQ], [SQ01], [SQ02],
  [TR], [TR01], [TR02], [TR03], [TR05], [RD], [RD01], [RD02], [RD03],
  [RD04], [EV], [EV03], [EV04], [EV05], [CW], [DN01], [SP]
- Research lanes: [RL01], [RL02], [RL03], [RL04], [RL05], [RL06], [RL07]
- Theory and design markers: [TH01], [TH02], [TH03], [TH04], [TH05], [TH06],
  [TH07], [TH08], [SY], [SA01], [SA02], [SA03], [DS02], [DS03], [MO]
- Formulation markers: [FR], [FR01], [FR02], [FR03], [FR04], [FR05], [FR06]
- Goal markers: [GL01], [GL02], [GL03], [GL04], [GL05], [GL06], [GL07],
  [GL08]
- Dependency markers: [DP01], [DP02], [DP03], [DP04], [DP05], [DP06]
- Requirement markers: [RQ01], [RQ02], [RQ03], [RQ04], [RQ05], [RQ06]

## (Z) Context-Citations

[DOC]: LIVE_RESEARCH_DOCUMENT
  "The first live research log for converting the approved 4GINE research plan
  into source-grounded decisions and SPINALTAP-local formulations."

[FM]: FORMAT_MODEL
  "The pseudo-citation document format where body markers reference a bottom
  registry and active definitions appear only in Context-Citations."

[WL02]: RESEARCH_WORKFLOW
  "The approved workflow phase that compares theory candidates against external
  research without letting sources overwrite the internal model."

[WL03]: PROPOSAL_WORKFLOW
  "The next workflow phase that turns selected research decisions into engine
  scope, module boundaries, risks, and acceptance criteria."

[WL04]: DEVELOPMENT_DOCSPEC
  "The later phase for requirements, design, and tasklist documents."

[WL05]: DEVELOPMENT_SOURCECODE
  "The later phase for sourcecode work after research, proposal, and docspec."

[GR]: GUARDRAILS
  "Novelty, truth, anti-replication, and evidence rules controlling source use."

[LC]: LINK_COMPLETE_STATE
  "A state where all active body markers have one registry definition and every
  registry definition is referenced at least once."

[LN]: LINT_RULE
  "The rule that pseudo-citation documents should be structurally valid without
  suppressing markdownlint."

[OUT]: OUTPUT_GATE
  "The handoff state that names selected, revised, rejected, and deferred
  research outcomes before proposal work starts."

[RS]: RESEARCH_SOURCE
  "A real external source used in the live research pass with date or version,
  source type, link, context weight, and linked markers."

[RS01]: RESEARCH_SOURCE
  "TITLE: ECS. SOURCE: Bevy official Quick Start. DATE: accessed 2026-05-26.
  LINK: https://bevy.org/learn/quick-start/getting-started/ecs/. USED_FOR:
  ECS data and logic separation, schedules, explicit order, and parallelism.
  CONTEXT_WEIGHT: MEDIUM. LINKED_CONTEXT: RL01, RL07, TH01, TH08, DS02."

[RS02]: RESEARCH_SOURCE
  "TITLE: Nodes and Scenes plus Using SceneTree. SOURCE: Godot Engine 4.6
  stable documentation. DATE: accessed 2026-05-26. LINKS:
  https://docs.godotengine.org/en/stable/getting_started/step_by_step/nodes_and_scenes.html
  and https://docs.godotengine.org/en/stable/tutorials/scripting/scene_tree.html.
  USED_FOR: composition, scene activation, and operational order.
  CONTEXT_WEIGHT: MEDIUM. LINKED_CONTEXT: RL01, RL07, TH08, DS02."

[RS03]: RESEARCH_SOURCE
  "TITLE: Box2D Simulation and Samples. SOURCE: Box2D 3.1.0 official
  documentation. DATE: accessed 2026-05-26. LINKS:
  https://box2d.org/documentation/md_simulation.html and
  https://box2d.org/documentation/samples.html. USED_FOR: fixed time steps,
  sub-steps, contact impulses, sample testbed behavior. CONTEXT_WEIGHT:
  MEDIUM. LINKED_CONTEXT: RL02, RL03, RL06, TH02, TH05, TH06."

[RS04]: RESEARCH_SOURCE
  "TITLE: Position Based Dynamics. SOURCE: Eurographics record for Müller,
  Heidelberger, Hennix, and Ratcliff. YEAR: 2006. LINK:
  https://diglib.eg.org/items/deb0a7a1-2ddf-496f-889a-fe0df1feeb73. USED_FOR:
  position-space constraint projection as local solver pressure.
  CONTEXT_WEIGHT: LOW. LINKED_CONTEXT: RL02, TH02."

[RS05]: RESEARCH_SOURCE
  "TITLE: Fix Your Timestep. SOURCE: Glenn Fiedler, Gaffer On Games. DATE:
  2004-06-10. LINK: https://gafferongames.com/post/fix_your_timestep/.
  USED_FOR: fixed dt, accumulator timing, render-simulation separation, and
  interpolation pressure. CONTEXT_WEIGHT: MEDIUM. LINKED_CONTEXT: RL03, TH06."

[RS06]: RESEARCH_SOURCE
  "TITLE: ACM Policy on Plagiarism, Misrepresentation, and Falsification.
  SOURCE: Association for Computing Machinery. DATE: updated 2023-02-23.
  LINK: https://www.acm.org/publications/policies/plagiarism-overview.
  USED_FOR: originality, attribution, idea and method reuse boundaries.
  CONTEXT_WEIGHT: HIGH for ethics guardrails, LOW for engine design mechanics.
  LINKED_CONTEXT: RL04, TH03, TR, CW."

[RS07]: RESEARCH_SOURCE
  "TITLE: Khronos OpenGL Registry. SOURCE: Khronos Group. DATE: accessed
  2026-05-26. LINK: https://registry.khronos.org/OpenGL/index_gl.php.
  USED_FOR: official OpenGL specification index and historical API anchor.
  CONTEXT_WEIGHT: LOW. LINKED_CONTEXT: RL05, TH04, TH07."

[RS08]: RESEARCH_SOURCE
  "TITLE: Fixed Function Pipeline. SOURCE: Khronos OpenGL Wiki. DATE: page last
  edited 2015-04-10, accessed 2026-05-26. LINK:
  https://wikis.khronos.org/opengl/Fixed_Function_Pipeline. USED_FOR:
  fixed-function rendering constraints, transform and lighting state,
  texture environment, fog, and legacy limitations. CONTEXT_WEIGHT: MEDIUM.
  LINKED_CONTEXT: RL05, TH04, TH07, SY."

[RS09]: RESEARCH_SOURCE
  "TITLE: Direct3D Architecture (Direct3D 9). SOURCE: Microsoft Learn. DATE:
  page last updated 2021-01-06, accessed 2026-05-26. LINK:
  https://learn.microsoft.com/en-us/windows/win32/direct3d9/direct3d-architecture.
  USED_FOR: vertex data, primitive data, vertex processing, texture sampling,
  pixel processing, alpha, depth, stencil, and fog pipeline axes.
  CONTEXT_WEIGHT: MEDIUM. LINKED_CONTEXT: RL05, TH04, TH07."

[RS10]: RESEARCH_SOURCE
  "TITLE: Unit testing. SOURCE: Godot Engine 4.6 stable documentation. DATE:
  accessed 2026-05-26. LINK:
  https://docs.godotengine.org/en/stable/engine_details/architecture/unit_testing.html.
  USED_FOR: dedicated tests, filtered runs, assertions, and failure-path checks.
  CONTEXT_WEIGHT: MEDIUM. LINKED_CONTEXT: RL06, TH05."

[RS11]: RESEARCH_SOURCE
  "TITLE: Creating Examples. SOURCE: Bevy contribution documentation. DATE:
  accessed 2026-05-26. LINK:
  https://bevy.org/learn/contribute/helping-out/creating-examples/.
  USED_FOR: goal-driven examples, working behavior, minimal scope, stress tests,
  and testbeds. CONTEXT_WEIGHT: LOW. LINKED_CONTEXT: RL06, RL07, TH05, DS02."

[SQ]: SOURCE_QUALITY
  "The requirement that source use state tested claim, extracted constraint,
  source limit, and decision value instead of boilerplate summary."

[SQ01]: AUTHORITATIVE_SOURCE_PREFERENCE
  "The preference for official documentation, standards, primary papers, source
  repositories, and dated technical articles before secondary summaries."

[SQ02]: FORUM_SIGNAL_LIMIT
  "Forum material may be used for problem discovery or terminology, not as
  independent proof."

[TR]: TRANSFORMATION_PROTOCOL
  "The rule that source pressure must be converted into original SPINALTAP-local
  reasoning before it affects theory."

[TR01]: CONSTRAINT_EXTRACTION
  "The step that reduces source material to a constraint, behavior, failure
  mode, or validation condition before design use."

[TR02]: REPLICATION_RISK_CHECK
  "The check that rejects or down-weights output whose structure remains too
  visibly copied from a source."

[TR03]: SPINALTAP_TRANSLATION
  "The rewrite step that maps source pressure to nervous_system ownership,
  vertebra operation, spinal_column aggregation, and context weight."

[TR05]: ATTRIBUTED_ORIGINAL_PROSE
  "The rule that sources are attributed while final prose remains original."

[RD]: RESEARCH_DECISION
  "A traceable record stating whether a claim is accepted, revised, rejected, or
  deferred after source pressure and originality checks."

[RD01]: ACCEPT_DECISION
  "A claim survives current source pressure and can move forward as a proposal
  candidate."

[RD02]: REVISE_DECISION
  "A claim remains useful but must change scope, wording, contract, or
  formulation before proposal work."

[RD03]: REJECT_DECISION
  "A claim or direction fails evidence review, originality control, or project
  guardrails."

[RD04]: DEFER_DECISION
  "A claim cannot be resolved truthfully in the current pass and must wait for
  later research, proposal, or prototype work."

[EV]: EVIDENCE_LEVEL
  "The strength tier assigned to a claim after source intake and validation."

[EV03]: RESEARCH_SUPPORT
  "Support from external research, documentation, policy, or technical articles."

[EV04]: TRACEABLE_IMPLEMENTATION_PRECEDENT
  "Support from documented implementation behavior, tests, examples, or engine
  workflows."

[EV05]: DIRECT_INTERNAL_TEST
  "Support reserved for future prototype or engine tests created by this
  project."

[CW]: CONTEXT_WEIGHT
  "The allowed influence a source can exert after authority, fit, originality
  distance, and validation reach are considered."

[DN01]: DATA_REPLICATION
  "The rule that research must not become a lightly renamed replica of source
  material."

[SP]: SOFT_PROVEN
  "A claim state requiring coherent reasoning, source pressure, translation,
  and validation steps before implementation readiness."

[RL01]: ENGINE_STATE_ROUTING
  "Research lane for state flow, data ownership, scene organization, module
  communication, and spinal_column aggregation."

[RL02]: LOCAL_SOLVER_BEHAVIOR
  "Research lane for scoped solvers, constraints, corrections, impulses, and
  bounded numerical updates."

[RL03]: TEMPORAL_COHERENCE
  "Research lane for fixed steps, accumulator timing, interpolation, and
  simulation-render separation."

[RL04]: CONTEXT_WEIGHT_AND_ORIGINALITY
  "Research lane for provenance, source influence, novelty distance, and
  anti-replication control."

[RL05]: STYLE_CONSTRAINT_MATHEMATICS
  "Research lane for turning retro 3D style language into measurable rendering
  constraints."

[RL06]: SOFT_PROOF_AND_VALIDATION
  "Research lane for tests, specimens, examples, benchmarks, failure paths, and
  acceptance gates."

[RL07]: MODULE_BOUNDARY_MAPPING
  "Research lane for mapping theory objects into traceable module and document
  boundaries."

[TH01]: SIGNAL_ROUTING_SPINE
  "Candidate theory where independent module outputs become typed state signals
  before spinal_column aggregation."

[TH02]: VERTEBRAE_LOCAL_SOLVERS
  "Candidate theory where scoped solver units perform bounded transforms,
  corrections, collisions, or transitions."

[TH03]: CONTEXT_WEIGHT_GOVERNOR
  "Candidate theory for measuring and limiting outside research influence."

[TH04]: STYLE_CONSTRAINT_LAYER
  "Candidate theory where visual style is treated as a formal constraint
  surface."

[TH05]: SOFT_PROOF_PIPELINE
  "Candidate theory for advancing ideas through evidence, validation, and
  proposal readiness."

[TH06]: TEMPORAL_COHERENCE_CONTROLLER
  "Candidate theory for coherent evolving state across frames and solver
  updates."

[TH07]: VISUAL_METRIC_TRANSLATOR
  "Candidate theory for translating style language into measurable rendering
  and asset constraints."

[TH08]: SCOPE_BOUNDARY_ALLOCATOR
  "Candidate theory for deciding whether formulas belong to nervous_system,
  vertebrae, or spinal_column layers."

[SY]: STYLE
  "Formal rendering or presentation style framed as measurable constraints."

[SA01]: NERVOUS_SYSTEM
  "Broad but bounded domain owner for families of engine behavior."

[SA02]: VERTEBRAE
  "Local solver, transform unit, or scoped formulation operating on a defined
  state target."

[SA03]: SPINAL_COLUMN
  "Aggregation and reconciliation layer that orders module relationships and
  produces higher-order engine state."

[DS02]: MODULE_BOUNDARY
  "A design object defining where one algorithmic stem ends and another begins."

[DS03]: DATA_CONTRACT
  "A design object defining input, transformation, output, ownership, and
  refusal boundaries."

[MO]: MODULE_OBJECT
  "Implementation-facing module marker connecting theory to sourcecode and
  documentation structure."

[FR]: FORMULATION
  "An original SPINALTAP-local synthesis derived from source pressure without
  copying source method or wording."

[FR01]: SIGNAL_CONSTRAINT_SPINE
  "A formulation where engine subsystem outputs become typed signals with
  constraint envelopes before aggregation."

[FR02]: STEM_DELTA_PACKET
  "A formulation where vertebrae emit bounded deltas and residual risk instead
  of hidden global mutations."

[FR03]: TIME_PACKET_PUMP
  "A formulation where elapsed time is converted into fixed simulation packets
  before solver consumption."

[FR04]: STYLE_CONSTRAINT_VECTOR
  "A formulation where style becomes measurable geometry, lighting, texture,
  color, fog, alpha, depth, camera, animation, and artifact constraints."

[FR05]: CONTEXT_WEIGHT_GOVERNOR
  "A formulation that caps source influence by authority, claim fit,
  originality distance, and validation reach."

[FR06]: SOFT_PROOF_LADDER
  "A formulation that moves claims from prose to source pressure, translation,
  runnable specimen, failure check, and proposal-ready requirement."

[GL01]: LIVE_RESEARCH_PASS
  "Run the approved live research process without reopening the plan."

[GL02]: SOURCE_INTAKE
  "Collect and summarize sources by tested claim, extraction, limit, and
  decision value."

[GL03]: ENGINE_STATE_ROUTING
  "Pressure-test signal routing and state aggregation."

[GL04]: LOCAL_SOLVER_BOUNDARIES
  "Pressure-test vertebrae as bounded local solvers."

[GL05]: TEMPORAL_COHERENCE
  "Pressure-test fixed-step, accumulator, and presentation boundaries."

[GL06]: ORIGINALITY_CONTROL
  "Pressure-test context weight and anti-replication guardrails."

[GL07]: SYNTHESIZED_FORMULATIONS
  "Produce original SPINALTAP-local formulations from source pressure."

[GL08]: RESEARCH_GATE
  "Name selected, revised, rejected, and deferred research outcomes."

[DP01]: APPROVED_RESEARCH_PLAN
  "The user-approved docs/research_plan.md controls this live research pass."

[DP02]: AUTHORITATIVE_SOURCE_SET
  "The curated set of official documentation, standards, papers, and technical
  articles used for source pressure."

[DP03]: DATA_OWNERSHIP_MODELS
  "Source material about ECS, scene trees, schedules, and execution order."

[DP04]: CONSTRAINT_SOLVER_EVIDENCE
  "Source material about substeps, contact impulses, projection, and bounded
  correction."

[DP05]: FIXED_STEP_AND_ACCUMULATOR
  "Source material about fixed dt, accumulators, interpolation, and temporal
  stability."

[DP06]: SOURCE_INFLUENCE_LIMIT
  "The anti-replication dependency that limits source influence before proposal
  work."

[RQ01]: TRUTHFUL_ORIGINAL_SYNTHESIS
  "The research result must state source support honestly and translate it into
  original project-owned language."

[RQ02]: NO_BOILERPLATE_SUMMARIES
  "Every source summary must state claim, extraction, limit, and decision value."

[RQ03]: TRACEABLE_SIGNAL_FLOW
  "Engine-state claims must name ownership, input, output, order, and
  validation boundaries."

[RQ04]: NO_IMPORTED_SOLVER_ARCHITECTURE
  "The project may extract constraints from solver sources but must not import
  their full architecture."

[RQ05]: PROPOSAL_READY_LANGUAGE
  "The output must phrase surviving ideas so proposal work can use them without
  copying source structure."

[RQ06]: PROPOSAL_GATE
  "The handoff must separate selected, revised, rejected, and deferred outcomes
  before proposal work begins."
