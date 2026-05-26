# (A) 4GINE: SPINALTAP MULTI-MODULAR ALGORITHMIC ENGINE

A novel, research-guided three-dimensional game-engine design organized
through SPINALTAP_ALGORITHM [SA] and the multi-modular ALGORITHMIC_STEM model
[AS].

The upper document is a contextual knowledge map. It references compact
pseudo-citation markers that resolve to the bottom [Z] registry. The registry
is the source of truth, and the upper document should not redefine those
markers.

## (1.A) DOCUMENT FORMAT ONBOARDING: [FM]

> Goal: [GL01] — FORMAT_ONBOARDING
> Dependency: [DP01] — CONTEXT_CITATION_REGISTRY
> Requirement: [RQ01] — FORMAT_INTEGRITY

The document keeps only one active definition per marker. The complete
definition lives in [Z]. All body text, headings, blockquote metadata, lists,
and examples above [Z] should reference markers without recreating reference
definitions.

```md
[ID]: CATEGORY
  "Full contextual source-of-truth definition."

Body text uses [ID], [ID][], or [text][ID].
```

For this format, bracket-colon syntax is reserved for the registry. Local
metadata keeps the same semantic order, but it does not use bracket-colon
syntax.

```md
> Goal: [GL01] — FORMAT_ONBOARDING
> Dependency: [DP01] — CONTEXT_CITATION_REGISTRY
> Requirement: [RQ01] — FORMAT_INTEGRITY
```

### (1.A.1) Namespace and entry design: [NS], [CE]

The namespace model [NS] keeps families stable. Goals use [GL], dependencies
use [DP], requirements use [RQ], workflow stages use [WL], theory candidates
use [TH], style markers use [SY], evidence markers use [EV], design objects
use [DS], and source modules use [MO].

A citation entry [CE] must be readable as a complete object: marker label,
category destination, and quoted definition. The destination acts like a
compact title. The quoted definition carries the contextual weight.

### (1.A.2) Final-pass placeholder rule

Open work can be described in plain language, but completed passes must not
leave bracketed zero-number placeholder IDs. This keeps the file link-complete
and avoids confusing the Markdown reference-definition parser [RQ13].

## (2.A) GUARDRAILS: [GR]

> Goal: [GL02] — GUARDRAIL_ALIGNMENT
> Dependency: [DP02] — NOVELTY_CONTROL
> Requirement: [RQ02] — NON_REPLICATION_REQUIREMENT
> Requirement: [RQ03] — EVIDENCE_STANDARD

Research is used as pressure, not as a copy source. It can strengthen, reject,
or constrain theory, but it must not overwrite the internal
SPINALTAP_ALGORITHM structure [SA].

- Use CONTEXT_WEIGHT [CW] before importing outside theory into an internal
  claim.
- Apply DATA_REPLICATION [DN01] whenever a source begins to dominate the shape
  of the output.
- Promote claims from TECHNICALLY_PLAUSIBLE [TP] toward SOFT_PROVEN [SP] only
  after comparison, adjustment, and documented reasoning.
- Keep the ignore rule [IG01] active so the engine target does not drift into
  traditional pixel_art framing.

## (B) MULTI-MODULATED ALGORITHMIC MATHEMATICAL 3D ENGINE MODEL

### (1.B) CORE_THEORY: [CT]

> Goal: [GL03] — CORE_THEORY_LARGE_BATCH
> Dependency: [DP03] — SPINALTAP_FRAMEWORK
> Requirement: [RQ04] — MODULAR_ALGORITHM_CHAIN

4GINE is organized as a capable three-dimensional engine whose architecture is
mapped through SPINALTAP_ALGORITHM [SA]. The biological metaphor is not
decorative; it defines algorithm ownership, scoped responsibility, and data
movement.

```txt
[SA] = [SA01] -> [SA02] -> [SA03]
```

- nervous_system [SA01] represents large but bounded algorithm families.
- vertebrae [SA02] represents local solvers, transform units, and scoped
  formulas.
- spinal_column [SA03] represents the aggregation, routing, and reconciliation
  layer.

The ALGORITHMIC_STEM model [AS] keeps formulas scoped. Child stems solve or
transform bounded data. Parent stems ingest child outputs and produce
higher-order state.

```txt
engine_state_next = spinal_column
    nervous_system_batch
        vertebrae_formulas(input_state, constraints, context_weight)
    end
end
```

The schema is a design scaffold, not a proof claim. It defines the shape that
candidate theories should take before entering research and validation [TH],
[EV].

### (2.B) WORKFLOW: [WL]

> Goal: [GL04] — WORKFLOW_ROADMAP
> Dependency: [DP04] — WORKFLOW_SEQUENCE
> Requirement: [RQ05] — ORDERED_WORKFLOW

- [WL01] THEORIZE_BRAINSTORM — generate the largest useful batch of theory
  candidates.
- [WL02] RESEARCH — compare, pressure-test, adjust, and reject weak
  candidates.
- [WL03] PROPOSAL — convert selected theory into scoped engine direction.
- [WL04] DEVELOPMENT_DOCSPEC — create requirements.md, design.md, and
  tasklist.md.
- [WL05] DEVELOPMENT_SOURCECODE — build from traceable design and docspec
  output.

The older [PW01] tag is preserved only as a deprecated alias. The active
workflow marker for brainstorm work is [WL01].

## (C) THEORIZE_BRAINSTORM: [WL01]

> Goal: [GL05] — THEORY_GENERATION_BATCH
> Dependency: [DP05] — CREATIVE_MATHEMATICAL_SPACE
> Requirement: [RQ06] — TECHNICAL_PLAUSIBILITY_FILTER

The brainstorm stage starts wide. Its job is to create enough theory surface
that useful structures can be discovered, compared, cut, and refined.

1. Signal-Routing Spine [TH01] — convert independent module outputs into typed
   state signals before aggregation.
2. Vertebrae Local Solvers [TH02] — let scoped solver units perform bounded
   transforms, corrections, collisions, and transitions.
3. Context-Weight Governor [TH03] — measure how much outside research can
   influence internal theory before replication risk rises.
4. Style-Constraint Layer [TH04] — treat visual style as a bounded constraint
   surface rather than a loose aesthetic note.
5. Soft-Proof Pipeline [TH05] — move ideas from brainstorm to technical
   plausibility and then toward soft proof.
6. Temporal Coherence Controller [TH06] — keep evolving engine state coherent
   across frames and solver updates.
7. Visual Metric Translator [TH07] — translate style language into measurable
   rendering and asset constraints.
8. Scope Boundary Allocator [TH08] — decide which formulas belong to
   nervous_system, vertebrae, or spinal_column layers.

A brainstormed theory remains active only if it can be expressed through [SA],
decomposed into bounded [AS] units, converted into requirements or
dependencies, and researched without becoming a direct replica of prior work
[DN01].

## (D) RESEARCH: [WL02]

> Goal: [GL06] — RESEARCH_SUPPORT
> Dependency: [DP06] — RESEARCH_COLLECTION
> Requirement: [RQ07] — SOFT_PROVEN_STANDARD

Research challenges the theory. It identifies what existing work proves, where
it fails, and which constraints should be inherited or avoided. It does not
become the engine theory by itself.

1. State the exact claim being tested, such as routing, aggregation, solver
   stability, visual constraint, or engine-state composition.
2. Collect sources and create complete research-source records [RS].
3. Extract strengths, shortcomings, assumptions, and failure modes.
4. Assign CONTEXT_WEIGHT [CW] before using the source in a theory rewrite.
5. Rewrite the surviving claim in SPINALTAP_ALGORITHM terms [SA] instead of
   reproducing source structure.
6. Promote only the portion that survives the evidence ladder [EV] and
   soft-proof standard [SP].

### (D.1) Research-source record shape: [RS]

```md
[RSnn]: RESEARCH_SOURCE
  "TITLE: ...
  SOURCE: ...
  YEAR: ...
  LINK_OR_DOI: ...
  USED_FOR: ...
  CONTEXT_WEIGHT: LOW | MEDIUM | HIGH
  LINKED_CONTEXT: [SA], [THnn], [RQnn], [DPnn]"
```

Do not create a numbered research-source ID until the source exists. Until
then, describe the need in prose or a task note rather than creating a
bracketed placeholder marker [RQ13].

### (D.2) Evidence ladder: [EV]

- [EV01] OBSERVED_PATTERN — weakest support; useful for brainstorming but not
  proof.
- [EV02] MATHEMATICAL_ANALOGY — moderate support; useful only after
  translation into SPINALTAP terms.
- [EV03] RESEARCH_SUPPORT — stronger support from external literature or
  technical documentation.
- [EV04] TRACEABLE_IMPLEMENTATION_PRECEDENT — strong support from documented
  implementation behavior.
- [EV05] DIRECT_INTERNAL_TEST — strongest support, reserved for future
  prototype or engine testing.

### (D.3) Style examples: [SY]

> Goal: [GL07] — STYLE_TAXONOMY
> Dependency: [DP07] — FORMAL_STYLE_LANGUAGE
> Requirement: [RQ08] — STYLE_EXCLUSION_REQUIREMENT

1. Low-poly 3D [SY01] — broad reduced-polygon modeling style.
2. Texture-mapped low-poly 3D [SY02] — simplified geometry with image texture
   detail.
3. Affine-textured 3D [SY03] — perspective-imperfect warped texture behavior.
4. Dithered 3D [SY04] — limited-color or noise-pattern visual treatment.
5. Vertex-lit 3D [SY05] — lighting calculated at vertices and interpolated
   across faces.
6. Gouraud-shaded 3D [SY06] — smooth polygonal lighting from interpolated
   vertex values.
7. Flat-shaded 3D [SY07] — hard polygon facets, often with minimal texture
   detail.
8. Billboarded 3D [SY08] — two-dimensional planes or sprites inside a
   three-dimensional scene.
9. Pre-rendered 3D [SY09] — offline-rendered backgrounds, sprites, or assets
   in an interactive context.
10. Fixed-function 3D [SY10] — limited pre-modern-shader rendering behavior.
11. Cel-shaded or toon-shaded 3D [SY11] — stylized cartoon-like lighting or
   outlines.
12. Arcade 3D [SY12] — clean, bright, readable arcade-style presentation.
13. Early real-time CGI [SY13] — glossy toy-like presentation imitating
   offline CGI.
14. Sixth-generation 3D [SY14] — Dreamcast, PlayStation 2, GameCube, and
   original Xbox-era style language.
15. Retro 3D [SY15] — modern umbrella term for older real-time
   three-dimensional aesthetics.

Traditional pixel_art remains excluded as an engine-level target through
[IG01].

## (E) PROPOSAL: [WL03]

> Goal: [GL08] — PROPOSAL_FORMATION
> Dependency: [DP08] — PROPOSAL_INPUTS
> Requirement: [RQ09] — PROPOSAL_READINESS

The proposal is the first stage where the document stops expanding theory and
begins selecting a buildable direction.

- Define engine scope through [DS01].
- Define module boundaries through [DS02].
- Define data contracts through [DS03].
- Define validation gates through [DS04].
- Track unresolved risk through [DS05].

A proposal is ready only when it can connect selected theory [TH], source
influence [RS], context weighting [CW], dependencies [DP], requirements [RQ],
style constraints [SY], and implementation boundaries [MO].

## (F) DEVELOPMENT_DOCSPEC: [WL04]

> Goal: [GL09] — DEVELOPMENT_DOCSPEC
> Dependency: [DP09] — DOCUMENTATION_PACKAGE
> Requirement: [RQ10] — DOCSPEC_TRACEABILITY

The docspec turns the proposal into development artifacts. requirements.md
records the build conditions. design.md explains architecture. tasklist.md
turns the design into ordered implementation work.

- requirements.md must connect each requirement to at least one goal and
  dependency.
- design.md must explain how [SA01], [SA02], [SA03], and [AS] cooperate.
- tasklist.md must not create tasks without a parent requirement [RQ].

## (G) DEVELOPMENT_SOURCECODE: [WL05]

> Goal: [GL10] — DEVELOPMENT_SOURCECODE
> Dependency: [DP10] — CODE_ARCHITECTURE_SCAFFOLD
> Requirement: [RQ11] — SOURCE_TRACEABILITY

Sourcecode should begin as a traceable scaffold, not as a detached generic
engine. The first structure should preserve the conceptual chain [SA01] to
[SA02] to [SA03].

```txt
/engine
  /spinal_column      # [MO01]
  /nervous_system     # [MO02]
  /vertebrae          # [MO03]
  /docs               # [MO04]
  /tests              # [MO05]
```

Implementation can rename files later, but the first scaffold should keep
architecture legible against the pseudo-citation map [MO].

## (H) PSEUDO-CITATION LINT RULES: [LN]

> Goal: [GL11] — LINT_VALIDATION
> Dependency: [DP11] — CITATION_LINTER
> Requirement: [RQ12] — LINT_COMPLIANCE

- [LN01] Keep exactly one source-of-truth definition for each active marker.
- [LN02] Reference markers above the registry; do not redefine them above it.
- [LN03] Remove zero-number placeholders from completed passes.
- [LN04] Preserve renamed draft artifacts only as explicit aliases.
- [LN05] Avoid unsafe nested double quotes inside definition titles.
- [LN06] Route external factual claims through research-source records.
- [LN07] Keep category labels stable and mostly uppercase snake case.
- [LN08] Require goal, dependency, and requirement metadata for workflow
  stages.
- [LN09] Use a usage index when the registry needs every definition to count
  as referenced.
- [LN10] Treat marker labels as case-normalized and therefore
  case-insensitive.
- [LN11] Do not use bracket-colon definitions inside blockquote metadata.
- [LN12] Reserve bracket-colon reference-definition lines for the registry.

## (I) LINK-COMPLETE USAGE INDEX: [LI]

> Goal: [GL12] — LINK_COMPLETENESS
> Dependency: [DP12] — USAGE_ANCHOR_INDEX
> Requirement: [RQ13] — NO_PLACEHOLDER_IDS

This section is intentionally non-authoritative. It exists to reference every
active registry marker at least once without redefining any of them. It is the
MD053-safe bridge between the body map and the bottom source-of-truth
registry.

- Core registry classes:
  [Z], [FM], [GR], [LN], [LI], [NS], [CE], [CT], [TP], [SP], [WL], [TH]
- Control markers:
  [SA], [SA01], [SA02], [SA03], [AS], [CW], [DN], [DN01], [SY], [IG], [IG01],
  [RS], [EV], [DS], [MO]
- Goal markers:
  [GL], [GL01], [GL02], [GL03], [GL04], [GL05], [GL06], [GL07], [GL08],
  [GL09], [GL10], [GL11], [GL12]
- Dependency markers:
  [DP], [DP01], [DP02], [DP03], [DP04], [DP05], [DP06], [DP07], [DP08],
  [DP09], [DP10], [DP11], [DP12]
- Requirement markers:
  [RQ], [RQ01], [RQ02], [RQ03], [RQ04], [RQ05], [RQ06], [RQ07], [RQ08],
  [RQ09], [RQ10], [RQ11], [RQ12], [RQ13]
- Workflow markers:
  [WL01], [WL02], [WL03], [WL04], [WL05], [PW01]
- Theory markers:
  [TH], [TH01], [TH02], [TH03], [TH04], [TH05], [TH06], [TH07], [TH08]
- Style markers:
  [SY], [SY01], [SY02], [SY03], [SY04], [SY05], [SY06], [SY07], [SY08],
  [SY09], [SY10], [SY11], [SY12], [SY13], [SY14], [SY15]
- Evidence markers:
  [EV], [EV01], [EV02], [EV03], [EV04], [EV05]
- Design markers:
  [DS], [DS01], [DS02], [DS03], [DS04], [DS05]
- Module markers:
  [MO], [MO01], [MO02], [MO03], [MO04], [MO05]
- Lint markers:
  [LN], [LN01], [LN02], [LN03], [LN04], [LN05], [LN06], [LN07], [LN08],
  [LN09], [LN10], [LN11], [LN12]

## (Z) Context-Citations

[Z]: CONTEXT_CITATIONS
  "Bottom registry that holds the complete source-of-truth definition for
  every active pseudo-citation marker used by the document."

[FM]: FORMAT_MODEL
  "Document-format model that joins compact inline markers, local metadata,
  and registry entries into one traceable syntax."

[GR]: GUARDRAILS
  "Safety, novelty, research, and formatting constraints that keep the
  document from drifting away from its intended design."

[LN]: LINT_RULES
  "Validation rules that keep the pseudo-citation system consistent,
  traceable, and readable under markdownlint-style parsing."

[LI]: LINK_INDEX
  "A deliberate marker-use index that makes every active registry definition
  visible as a reference before the registry appears."

[NS]: NAMESPACE_MODEL
  "The rule set for assigning stable marker families such as goals,
  dependencies, requirements, theories, styles, and modules."

[CE]: CITATION_ENTRY
  "A single pseudo-citation object consisting of a marker label, category
  destination, and complete quoted context definition."

[GL]: GOAL
  "The intended outcome of a correlated section, subsection, task, request,
  theory object, or validation pass."

[GL01]: FORMAT_ONBOARDING
  "Define how the note uses compact contextual pseudo-citations, local
  metadata, and the bottom registry without losing traceability."

[GL02]: GUARDRAIL_ALIGNMENT
  "Keep the project novel, mathematically creative, research-aware, and
  internally traceable without letting source material overwrite the
  SPINALTAP_ALGORITHM design."

[GL03]: CORE_THEORY_LARGE_BATCH
  "Generate a large batch of technically plausible mathematical theory
  candidates that can support or refine the engine model."

[GL04]: WORKFLOW_ROADMAP
  "Move from open theory generation to research-supported theory, then into
  proposal, docspec, and sourcecode development."

[GL05]: THEORY_GENERATION_BATCH
  "Create broad but usable mathematical theory candidates that may support
  the SPINALTAP_ALGORITHM model."

[GL06]: RESEARCH_SUPPORT
  "Use external research to challenge, strengthen, narrow, and correct the
  best brainstormed theory candidates."

[GL07]: STYLE_TAXONOMY
  "Use formal style language for three-dimensional game aesthetics from
  roughly 1995 to 2005 while excluding pixel-art framing."

[GL08]: PROPOSAL_FORMATION
  "Convert research-adjusted theory into a specific engine proposal that can
  become requirements, design, and tasks."

[GL09]: DEVELOPMENT_DOCSPEC
  "Create the document package that turns the proposal into
  implementation-ready development artifacts."

[GL10]: DEVELOPMENT_SOURCECODE
  "Begin sourcecode development only after theory, research, proposal, and
  docspec have created enough traceable structure."

[GL11]: LINT_VALIDATION
  "Keep the pseudo-citation system internally consistent as the document
  grows and as tags are renamed or retired."

[GL12]: LINK_COMPLETENESS
  "Ensure every active registry definition is referenced at least once so
  markdownlint does not treat it as unused."

[DP]: DEPENDENCY
  "A component, task, prerequisite, input, or contextual support object that
  must exist before a requirement can be satisfied."

[DP01]: CONTEXT_CITATION_REGISTRY
  "The registry must contain the full description for every active reusable
  marker used in the document."

[DP02]: NOVELTY_CONTROL
  "The document depends on CONTEXT_WEIGHT and DO_NOT rules to prevent
  research material from becoming accidental replication."

[DP03]: SPINALTAP_FRAMEWORK
  "The model depends on the three-layer chain nervous_system, vertebrae, and
  spinal_column."

[DP04]: WORKFLOW_SEQUENCE
  "Each workflow stage depends on the prior stage producing enough context to
  advance without destroying traceability."

[DP05]: CREATIVE_MATHEMATICAL_SPACE
  "The brainstorm depends on technical imagination, loose early constraints,
  and strong anti-replication control."

[DP06]: RESEARCH_COLLECTION
  "Research requires source gathering, comparison, extraction of useful
  constraints, and explicit context-weight assignment."

[DP07]: FORMAL_STYLE_LANGUAGE
  "The style section depends on named rendering and presentation categories
  that can become design constraints."

[DP08]: PROPOSAL_INPUTS
  "The proposal depends on active theory candidates, research-source records,
  context weighting, and guardrails."

[DP09]: DOCUMENTATION_PACKAGE
  "The docspec depends on proposal output, numbered requirements, numbered
  dependencies, and traceable design claims."

[DP10]: CODE_ARCHITECTURE_SCAFFOLD
  "Sourcecode depends on the docspec and should mirror SPINALTAP_ALGORITHM
  structure rather than a generic engine layout."

[DP11]: CITATION_LINTER
  "The document depends on repeatable lint rules that catch unresolved IDs,
  duplicate IDs, broken aliases, and unsafe syntax."

[DP12]: USAGE_ANCHOR_INDEX
  "The document depends on a non-authoritative index that references every
  active marker without redefining it."

[RQ]: REQUIREMENT
  "A necessary condition, object, rule, output, or acceptance criterion
  required to achieve or build the correlated goal."

[RQ01]: FORMAT_INTEGRITY
  "Every active inline marker must resolve to exactly one complete definition
  in the context-citation registry."

[RQ02]: NON_REPLICATION_REQUIREMENT
  "Research must inform the theory without recreating, lightly renaming, or
  over-weighting existing theories."

[RQ03]: EVIDENCE_STANDARD
  "Critical theory claims must move from technical plausibility toward soft
  proof through research and documented reasoning."

[RQ04]: MODULAR_ALGORITHM_CHAIN
  "The core theory must remain expressible as SPINALTAP_ALGORITHM equals
  nervous_system to vertebrae to spinal_column."

[RQ05]: ORDERED_WORKFLOW
  "The workflow must preserve the ordered progression from brainstorm to
  research, proposal, docspec, and sourcecode."

[RQ06]: TECHNICAL_PLAUSIBILITY_FILTER
  "Every candidate must remain plausible enough to research, formalize, or
  reject without becoming incoherent speculation."

[RQ07]: SOFT_PROVEN_STANDARD
  "A theory can be soft-proven only when it is coherent, research-adjusted,
  internally consistent, and proposal-ready."

[RQ08]: STYLE_EXCLUSION_REQUIREMENT
  "Traditional pixel_art must remain excluded as an engine or core-design
  solution unless the ignore rule is revised."

[RQ09]: PROPOSAL_READINESS
  "A proposal must identify selected theories, rejected theories,
  dependencies, requirements, risks, and source influence."

[RQ10]: DOCSPEC_TRACEABILITY
  "requirements.md, design.md, and tasklist.md must preserve traceability
  back to registry definitions and workflow IDs."

[RQ11]: SOURCE_TRACEABILITY
  "Every major source module should trace back to an active requirement,
  dependency, workflow stage, and context entry."

[RQ12]: LINT_COMPLIANCE
  "Before a section is treated as complete, it must satisfy the active
  pseudo-citation lint rules."

[RQ13]: NO_PLACEHOLDER_IDS
  "Completed passes must not leave bracketed placeholder IDs such as
  zero-numbered goal, dependency, requirement, or source tags."

[CT]: CORE_THEORY
  "The fundamental idea or framework describing how the theory operates, what
  problem it solves, and how the engine is organized."

[TP]: TECHNICALLY_PLAUSIBLE
  "A creative theory standard that permits novelty while rejecting
  incoherent, unbounded, or non-actionable speculation."

[SP]: SOFT_PROVEN
  "A research-supported plausibility standard based on coherent mathematics,
  explicit assumptions, comparison, and critical adjustment."

[WL]: WORKFLOW
  "Ordered roadmap from theory generation to research, proposal, docspec, and
  sourcecode development."

[WL01]: THEORIZE_BRAINSTORM
  "First and loosest guardrail stage; create the largest useful batch of
  theory candidates, then trim toward a selected framework."

[WL02]: RESEARCH
  "Second stage; compare candidates against external research, extract
  strengths and failures, and promote only what survives review."

[WL03]: PROPOSAL
  "Third stage; convert the strongest research-adjusted theory into a scoped
  engine proposal with risks and acceptance criteria."

[WL04]: DEVELOPMENT_DOCSPEC
  "Fourth stage; create requirements.md, design.md, and tasklist.md as
  implementation-ready development artifacts."

[WL05]: DEVELOPMENT_SOURCECODE
  "Fifth stage; begin sourcecode from the research, proposal, requirements,
  design, and tasklist."

[PW01]: DEPRECATED_ALIAS
  "Former artifact tag for THEORIZE_BRAINSTORM; preserve only as historical
  draft context and use WL01 as the active workflow ID."

[TH]: THEORY_CANDIDATE
  "A brainstormed or research-adjusted theoretical object that may become
  part of the SPINALTAP_ALGORITHM engine model."

[TH01]: SIGNAL_ROUTING_SPINE
  "Candidate theory where independent module outputs become typed state
  signals before spinal_column aggregation."

[TH02]: VERTEBRAE_LOCAL_SOLVERS
  "Candidate theory where small scoped solver units perform transformations,
  collisions, corrections, or state changes."

[TH03]: CONTEXT_WEIGHT_GOVERNOR
  "Candidate theory for measuring and limiting how strongly outside research
  can influence the internal theory."

[TH04]: STYLE_CONSTRAINT_LAYER
  "Candidate theory where visual style is treated as a formal constraint
  surface rather than a loose aesthetic note."

[TH05]: SOFT_PROOF_PIPELINE
  "Candidate theory for moving an idea from brainstorm to technical
  plausibility and then toward soft proof."

[TH06]: TEMPORAL_COHERENCE_CONTROLLER
  "Candidate theory for keeping evolving engine state coherent across frames,
  transitions, and solver updates."

[TH07]: VISUAL_METRIC_TRANSLATOR
  "Candidate theory for translating style language into measurable
  constraints for rendering, assets, and presentation."

[TH08]: SCOPE_BOUNDARY_ALLOCATOR
  "Candidate theory for deciding which formulas belong to nervous_system,
  vertebrae, or spinal_column layers."

[SA]: SPINALTAP_ALGORITHM
  "A modular algorithm family organized through a nervous-system-inspired
  framework for a mathematical three-dimensional game engine."

[SA01]: nervous_system
  "Broad but bounded algorithm family; each domain contains scoped
  formulations and contributes to the engine ecosystem."

[SA02]: vertebrae
  "Smaller modular algorithm, local solver, transform unit, or scoped
  formulation operating on a defined data target."

[SA03]: spinal_column
  "Aggregation, routing, and reconciliation layer that orders module
  relationships and produces higher-order engine state."

[AS]: ALGORITHMIC_STEM
  "Modular operation model where scoped algorithmic stems formulate assigned
  jobs and pass bounded results to parent stems."

[CW]: CONTEXT_WEIGHT
  "The allowed influence weight of discovered data, source material,
  research, or prior theory on the current output."

[DN]: DO_NOT
  "A negative constraint used to remove, ignore, limit, or release an item
  from contextual relevance."

[DN01]: DATA_REPLICATION
  "Do not over-weight established theories so heavily that the result becomes
  a lightly modified replica of the original."

[SY]: STYLE
  "Formal video-game design or rendering style marker framed around platform
  capability, rendering behavior, or presentation constraint."

[SY01]: LOW_POLY_3D
  "Reduced-polygon three-dimensional modeling style where simplified geometry
  is intentional."

[SY02]: TEXTURE_MAPPED_LOW_POLY_3D
  "Low-poly style where image textures provide most surface detail over
  simplified geometry."

[SY03]: AFFINE_TEXTURED_3D
  "Retro texture-mapping style associated with perspective-imperfect or
  visibly warped texture behavior."

[SY04]: DITHERED_3D
  "Visual style using dithering, color limits, or noise-pattern transitions
  for retro color behavior."

[SY05]: VERTEX_LIT_3D
  "Lighting style where illumination is calculated at vertices and
  interpolated across polygon faces."

[SY06]: GOURAUD_SHADED_3D
  "Smooth polygonal shading style based on interpolated vertex color or
  lighting values."

[SY07]: FLAT_SHADED_3D
  "Hard-faceted three-dimensional style where individual polygon planes
  remain visibly distinct."

[SY08]: BILLBOARDED_3D
  "Technique where two-dimensional planes or sprites are placed and oriented
  inside a three-dimensional scene."

[SY09]: PRE_RENDERED_3D
  "Presentation style using offline-rendered backgrounds, sprites, or assets
  inside an interactive context."

[SY10]: FIXED_FUNCTION_3D
  "Rendering style associated with pre-modern-shader hardware and limited
  programmable graphics behavior."

[SY11]: CEL_SHADED_TOON_SHADED_3D
  "Stylized rendering approach using simplified lighting, ramps, outlines, or
  cartoon-like presentation."

[SY12]: ARCADE_3D
  "Clean, bright, readable real-time three-dimensional aesthetic associated
  with arcade presentation."

[SY13]: EARLY_REAL_TIME_CGI
  "Glossy or toy-like three-dimensional presentation imitating early offline
  CGI within real-time limits."

[SY14]: SIXTH_GENERATION_3D
  "Style language associated with Dreamcast, PlayStation 2, GameCube, and
  original Xbox-era presentation."

[SY15]: RETRO_3D
  "Modern umbrella style for recreating, remixing, or constraining older
  real-time three-dimensional aesthetics."

[IG]: IGNORE
  "Contextual ignore marker used to remove a style, concept, source, or
  direction from active design relevance."

[IG01]: STYLE
  "Ignore traditional pixel_art as an engine-level or core-design solution
  for this document."

[RS]: RESEARCH_SOURCE
  "External source entry such as a paper, book, documentation page, talk, or
  implementation note with context-weight metadata."

[EV]: EVIDENCE_LEVEL
  "Evidence-strength label used to show how much support a claim has before
  it is promoted in the workflow."

[EV01]: OBSERVED_PATTERN
  "Weak support based on a recurring observed behavior, design pattern, or
  implementation tendency."

[EV02]: MATHEMATICAL_ANALOGY
  "Moderate support based on a mathematical analogy that still needs stricter
  translation into SPINALTAP terms."

[EV03]: RESEARCH_SUPPORT
  "Stronger support from external literature, technical documentation, or
  well-described implementation precedent."

[EV04]: TRACEABLE_IMPLEMENTATION_PRECEDENT
  "Strong support from a documented implementation pattern that can be mapped
  to requirements and dependencies."

[EV05]: DIRECT_INTERNAL_TEST
  "Highest support tier reserved for future direct testing inside a built
  prototype or engine module."

[DS]: DESIGN_OBJECT
  "Design-level object used by the proposal and docspec to turn theory into
  scoped architecture and acceptance criteria."

[DS01]: ENGINE_SCOPE
  "Defines what the engine proposal includes, excludes, and postpones so
  novelty does not expand without control."

[DS02]: MODULE_BOUNDARY
  "Defines where one algorithmic stem ends and another begins so
  responsibilities remain bounded."

[DS03]: DATA_CONTRACT
  "Defines what data a module receives, transforms, emits, and refuses to
  own."

[DS04]: VALIDATION_GATE
  "Defines the condition that must be satisfied before a theory, requirement,
  or module advances."

[DS05]: RISK_LEDGER
  "Defines known risks caused by novelty, weak evidence, scope,
  implementation difficulty, or research mismatch."

[MO]: MODULE_OBJECT
  "Implementation-facing module marker that maps the conceptual algorithm
  model onto sourcecode and documentation structure."

[MO01]: SPINAL_COLUMN_MODULE
  "Source module family for aggregation, routing, reconciliation, and
  higher-order engine-state production."

[MO02]: NERVOUS_SYSTEM_MODULE
  "Source module family for broad engine domains such as rendering,
  simulation, scene state, and style constraints."

[MO03]: VERTEBRAE_MODULE
  "Source module family for local solvers, transform units, signal units, and
  bounded corrective formulas."

[MO04]: DOCS_MODULE
  "Documentation module containing requirements.md, design.md, tasklist.md,
  and traceability maps."

[MO05]: TESTS_MODULE
  "Validation module for future unit tests, integration tests, prototype
  checks, and internal proof experiments."

[LN01]: UNIQUE_SOURCE_OF_TRUTH
  "Every active marker must have exactly one source-of-truth definition and
  that definition must live in the registry."

[LN02]: REFERENCE_NOT_REDEFINE
  "The upper document may reference markers, but it must not repeat
  reference-definition syntax for those markers."

[LN03]: NO_ZERO_NUMBER_PLACEHOLDERS
  "Completed passes must not leave zero-numbered placeholder IDs in active
  text, metadata, or registry entries."

[LN04]: EXPLICIT_ALIAS_RULE
  "Deprecated or renamed IDs must be declared as aliases instead of silently
  reusing the old meaning."

[LN05]: SAFE_QUOTATION_RULE
  "Definitions should avoid unescaped nested double quotes and should prefer
  apostrophes inside title text."

[LN06]: EXTERNAL_CLAIM_LINKAGE
  "External factual or research claims should connect to a research-source
  record before they become design support."

[LN07]: STABLE_CATEGORY_LABELS
  "Category destination labels should use stable uppercase snake-case names
  unless the marker intentionally names a concept."

[LN08]: WORKFLOW_METADATA_COMPLETENESS
  "No workflow stage should advance unless its goal, dependency, and
  requirement metadata are present."

[LN09]: USAGE_INDEX_RULE
  "A link-complete pass may include a usage index so every registry
  definition has at least one visible reference."

[LN10]: CASE_NORMALIZATION_RULE
  "Marker labels must be unique after case folding because Markdown reference
  labels are matched by normalized form."

[LN11]: NO_BLOCKQUOTE_DEFINITIONS
  "Blockquote section metadata must avoid bracket-colon definition syntax
  unless it is meant to create a real definition."

[LN12]: REGISTRY_ONLY_DEFINITION_RULE
  "Only the registry should use bracket-colon reference-definition lines for
  active pseudo-citation definitions."
