# Technical evidence for 4GINE development realignment [DOC]

Research date: 2026-11-07. Repository baseline: `9afd1cf`.
This review supplements the
[first research pass](../../docs/live_research.md); it does not replace its
historical source records. Source IDs in this file are local to this file.
Recommendations below are project-specific inferences, not findings that an
external source has validated SPINALTAP [RQ01].

## (1) What does the existing research actually support?

> Goal: [GL01] - RECHECK_RESEARCH_SUPPORT
> Dependency: [DP01] - ORIGINAL_SOURCES_AND_PROJECT_RECORDS
> Requirement: [RQ01] - SEPARATE_SUPPORT_FROM_INFERENCE

### Takeaway: section 1

The earlier sources support useful constraints and testing practices. They do
not establish that the SPINALTAP synthesis, its scalar prototype, or its
governor scoring is a complete or novel engine. Preserve the earlier research
as provenance; narrow the claims used for future promotion [RQ01].

### Cited findings: section 1

- Fiedler explains fixed-step accumulation, presentation interpolation, and
  overload that makes simulation fall behind. A step cap can trade catch-up
  work for slower simulation. The article supports time ownership and a
  stated overload policy, not a universal timestep or a performance guarantee.
  [Fix Your Timestep!](https://gafferongames.com/post/fix_your_timestep/)
  [RS01].
- Box2D documents fixed timesteps and solver substeps. Its determinism section
  additionally names ordered processing, compiler/math controls and recurring
  tests, and warns that library determinism does not establish application
  determinism.
  [Box2D simulation](https://box2d.org/documentation/md_simulation.html)
  [RS02].
- The original PBD paper works directly with positions and discusses
  constraint projection, illustrated through cloth simulation. This supports
  a bounded correction example; it does not validate all proposed vertebrae.
  The publisher page returned HTTP 403, but the author's PDF was readable.
  [Author's 2006 paper](https://matthias-research.github.io/pages/publications/posBasedDyn.pdf)
  [RS11].
- Bevy documents data/logic separation and notes that independent systems may
  execute in different orders. Godot documents scene activation, tree order
  and explicit exceptions. These are distinct precedents for making order
  explicit, not evidence for choosing either architecture for 4GINE.
  [Bevy ECS](https://bevy.org/learn/quick-start/getting-started/ecs/),
  [Godot SceneTree](https://docs.godotengine.org/en/stable/tutorials/scripting/scene_tree.html)
  [RS12], [RS13].
- Microsoft documents geometry, sampling, pixel processing, alpha, depth,
  stencil and fog as pipeline concerns. The Khronos registry links historical
  API specifications. Neither source provides a universal retro aesthetic
  budget or a hardware profile covering every sixth-generation console.
  [Direct3D 9 architecture](https://learn.microsoft.com/en-us/windows/win32/direct3d9/direct3d-architecture),
  [OpenGL registry](https://registry.khronos.org/OpenGL/index_gl.php)
  [RS08], [RS15].

### Earlier-source verification ledger

IDs below identify records in `docs/live_research.md`, not this note's registry.

- **RS01, Bevy ECS:** Result of this pass: Page opened; separation and order
  caveat supported. Qualification: Rolling page, not a pinned release.
- **RS02, Godot scenes/tree:** Result of this pass: Both pages opened;
  composition and activation supported. Qualification: Stable URL can move; do
  not relabel it as fixed 4.6 evidence.
- **RS03, Box2D simulation/samples:** Result of this pass: Both pages opened;
  timing and testbed supported. Qualification: Simulation header now 3.2.0;
  samples header still 3.1.0.
- **RS04, PBD:** Result of this pass: Publisher URL returned 403; author PDF
  verified. Qualification: Preserve 2006 citation and add accessible author
  link.
- **RS05, Fiedler:** Result of this pass: Page opened; original date 2004-06-10
  confirmed. Qualification: Practical explanation, not a formal correctness
  proof.
- **RS06, ACM plagiarism policy:** Result of this pass: Direct page and
  publisher mirror returned 403. Qualification: Full policy not reverified; do
  not strengthen its old interpretation.
- **RS07, Khronos registry:** Result of this pass: Index opened, including
  OpenGL 1.x entries. Qualification: Index locates specifications; does not
  establish a style budget.
- **RS08, Khronos fixed-function wiki:** Result of this pass: Page returned
  403. Qualification: Historical record preserved; not fresh verified evidence.
- **RS09, Microsoft Direct3D 9:** Result of this pass: Relevant page text
  opened. Qualification: API vocabulary does not select a renderer.
- **RS10, Godot unit testing:** Result of this pass: Page opened; assertions
  and test organization supported. Qualification: C++/doctest precedent, not a
  required Python stack.
- **RS11, Bevy examples:** Result of this pass: Page opened;
  examples/testbeds/stress tests distinguished. Qualification: Practice
  guidance, not a 4GINE acceptance result.

The Box2D samples page describes interactive inspection and performance data,
and explicitly separates its sample application from the renderer-agnostic
library. [Box2D samples](https://box2d.org/documentation/samples.html) [RS16].
Godot documents dedicated tests and assertion/filter mechanisms.
[Godot unit testing](https://docs.godotengine.org/en/stable/engine_details/architecture/unit_testing.html)
[RS14]. These facts corroborate narrow earlier claims; they are not reasons to
adopt those engines' entire implementation or build systems.

### Inferences

1. Treat the earlier requirement to avoid an architecture clone as a
   project-owned design constraint. Do not present it as a conclusion that all
   attributed reuse is prohibited by ACM policy.
2. Keep context weights as declared influence limits. A numerical score is
   not an external originality measurement. The current mean-of-four scoring
   and `0.20` threshold are project heuristics requiring their own rationale
   and tests. The earlier FR05 formulation uses the minimum of the four
   factors; the runtime uses their mean. Factors (1, 0, 1, 1) therefore
   produce 0 under the written formula and 0.75 under the current runtime.
   This is a concrete policy decision to resolve; neither formula was
   externally calibrated:
   [earlier formulation](../../docs/live_research.md),
   [governor source](../../spinaltap/context_weight.py).
3. Preserve historical access dates, add this verification date separately,
   and record moving versions. A source record's existence and a source's
   current availability are different facts.
4. Research only the next unresolved decision. An expanding bibliography is
   not progress unless a claim changes, a risk becomes testable, or a scoped
   development gate is resolved.

### Gaps: section 1

The ACM policy's full text and the Khronos wiki page could not be refreshed.
No source examined validates SPINALTAP's biological decomposition, the
governor's numerical calibration, a particular production language/backend,
or 4GINE's performance. Those remain internal hypotheses or pending decisions.

## (2) Which claims need stronger development gates?

> Goal: [GL02] - DEFINE_MEASURABLE_GATES
> Dependency: [DP02] - VERIFIED_LANGUAGE_AND_ENGINE_BEHAVIOR
> Requirement: [RQ02] - PROMOTION_MATCHES_ACTUAL_EVIDENCE

### Takeaway: section 2

Prioritize proof promotion and reproducibility before extending engine claims.
Then validate runtime semantics and typed style limits with explicit failure
cases. Existing structural checks are useful but cannot carry those broader
claims [RQ02].

### Cited findings: section 2

- Python dataclasses generally do not check annotated field types. Frozen
  records emulate assignment restrictions rather than guaranteeing deep
  immutability. This supports explicit ingress validation and precise
  documentation of trusted constructors.
  [Python dataclasses](https://docs.python.org/3.13/library/dataclasses.html)
  [RS03].
- A mapping proxy is a read-only view that reflects changes to its underlying
  mapping. A proxy alone is not a snapshot.
  [Python MappingProxyType](https://docs.python.org/3.13/library/types.html#types.MappingProxyType)
  [RS04]. Snapshot and nested-value claims must therefore be verified against
  the actual copies and admissible value types in the implementation.
- Binary floating-point arithmetic approximates many decimal fractions and
  operations may accumulate rounding error. Assertions need an explicit
  numerical comparison policy.
  [Python floating-point guide](https://docs.python.org/3.13/tutorial/floatingpoint.html)
  [RS05].
- ICFP's artifact guidance asks reviewers to build/run artifacts and compare
  them with their stated claims. It distinguishes demonstrated function from
  ease of later reuse.
  [ICFP 2026 artifact evaluation](https://icfp26.sigplan.org/track/icfp-2026-artifact-evaluation)
  [RS09]. Use that narrow evidence principle; this project is not seeking or
  claiming an ACM badge.
- Bevy separates focused working examples, performance stress cases and
  graphical/interactive testbeds. Different claims need different artifacts.
  [Bevy example guidance](https://bevy.org/learn/contribute/helping-out/creating-examples/)
  [RS10].

### Inferences: actionable gates for the global plan

These are recommended acceptance conditions, not completed work or externally
mandated standards. They should be assigned stable task IDs by the global plan.

- **Proof promotion:** Proposed gate: Distinguish plan completeness from
  executed evidence. Evidence required: Claim/contract/gate IDs, source
  revision, environment, command, expected result, actual result, artifact path
  and reviewer verdict. Claim that remains excluded: Prose-only record proving
  a runtime claim.
- **Proof failure handling:** Proposed gate: Missing, stale, failed or
  mismatched evidence cannot promote. Evidence required: Positive specimen plus
  negative cases for absent artifact, wrong contract, failed command and stale
  revision. Claim that remains excluded: User-supplied evidence-tier string as
  verification.
- **Timing policy:** Proposed gate: Specify backlog, pause/resume, refused-step
  and interpolation behavior. Evidence required: Fixed-step/refusal sequences,
  backlog drain and sustained-overload cases, explicit preserved/dropped-time
  accounting. Claim that remains excluded: Packet count cap bounding wall-clock
  execution time.
- **Replay:** Proposed gate: Define the supported determinism scope before
  promising it. Evidence required: Recorded inputs and order, initial state,
  step/config identity, repeated result comparison and declared float policy.
  Claim that remains excluded: Cross-platform deterministic replay from fixed
  dt alone.
- **Ownership:** Proposed gate: Distinguish validated local keys from authority
  to publish. Evidence required: Owner/channel registration policy and refusal
  cases; if needed, versioned commit acceptance tests. Claim that remains
  excluded: Concurrency, persistence or side-effect rollback from scalar
  candidate staging.
- **Style schema:** Proposed gate: Replace descriptive strings with units,
  ranges and allowed enums. Evidence required: One fully specified profile and
  legal/illegal fixtures for every field. Claim that remains excluded:
  Historical hardware accuracy without corresponding evidence.
- **Visual validation:** Proposed gate: Make profile behavior inspectable.
  Evidence required: Repeatable scene, camera, assets, render settings, metrics
  and captured output. Claim that remains excluded: Passing schema tests
  proving the intended visual result.
- **Governor policy:** Proposed gate: Define down-weight semantics and scoring
  provenance. Evidence required: Recorded rubric, source existence policy,
  boundary tests and decision examples. Claim that remains excluded: Automatic
  proof of novelty or ownership of ideas.

Current code makes the first and sixth rows especially urgent:

- `_evaluate_proof_record` promotes after nonblank specimen-plan and
  failure-path checks; `SoftProofLab.review` adds contract/gate consistency
  but does not execute a specimen or inspect a result artifact.
  [Contract kernel](../../spinaltap/contract_kernel.py),
  [Soft-Proof Lab](../../spinaltap/soft_proof.py).
- `_style_limits` decodes each style field as nonblank text. The translator
  therefore validates presence and shape, not numeric budget semantics.
  [Contract validation](../../spinaltap/contract_validation.py),
  [Style surface](../../spinaltap/style_surface.py).
- The time pump retains unsimulated backlog and caps its interpolation scalar
  at one. It needs an explicit presentation policy while backlog exceeds a
  fixed step; the scalar alone does not render interpolation.
  [Time pump](../../spinaltap/time_packet.py).

A useful initial style task should define units and measurable scope, for
example: triangle count per visible frame, texture dimensions and bytes,
permitted sampling mode, active-light count, color representation, fog
distance in world units, alpha mode, depth behavior, camera clipping distances,
animation updates per second, and individually named permitted artifacts.
These are schema design suggestions derived from the existing DC05 fields and
pipeline axes [RS08], not fabricated historical console limits. Select actual
numbers only after choosing a target profile and a validation fixture.

### Gaps: section 2

There is no externally established universal boundary between
`candidate` and `implementation_ready` for this project. Its evidence policy
must define that boundary. ICFP's page contains inconsistent availability-badge
wording between its overview and later section, so availability-badge details
are deliberately not used as support here. No primary source can decide the
user's desired latency budget, scene scale or visual identity.

## (3) What should be decided before a usable application milestone?

> Goal: [GL03] - MAKE_FUTURE_WORK_REPRODUCIBLE_AND_BOUNDED
> Dependency: [DP03] - PROJECT_SCOPE_AND_TOOLCHAIN_RECORD
> Requirement: [RQ03] - DISTINGUISH_PROTOTYPE_FROM_PRODUCT

### Takeaway: section 3

The current Python prototype can remain the executable reference for contract
behavior while a later decision selects how to deliver the first interactive
3D demonstration. Tooling decisions should make the current work repeatable;
they should not silently choose the final engine stack [RQ03].

### Cited findings: section 3

- The Python packaging guide provides separate mechanisms for package
  metadata, build requirements, development dependencies and tool settings.
  These let the repository declare its current environment rather than depend
  on whatever tools happen to be installed.
  [Writing pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
  [RS06].
- Python virtual environments isolate installed dependencies. They are meant
  to be recreated, not committed or copied as portable installations; invoking
  the environment interpreter directly does not require activation.
  [Python venv](https://docs.python.org/3.13/library/venv.html) [RS07].

### Inferences: decision order and recommended outputs

1. **Define the immediate user outcome.** Write one small scenario the
   developer can run, inspect and modify. A suggested future demonstration is
   moving bounded 3D state through input, fixed-step updates, reconciliation
   and a visible scene, with refusal inspection and reset/pause controls.
   This is a proposal for a milestone, not established approved product scope.
2. **Make the current prototype reproducible.** Declare the supported Python
   version, development tool versions and bootstrap commands. Prefer one
   repository-local environment and one verification entry point. Record
   interpreter/tool versions in evidence. Validate from a clean environment
   before claiming onboarding is reproducible. A pyproject alone does not
   lock all transitive tools or prove installation.
3. **Close correctness and claim gaps.** Implement the proof policy, governor
   decisions, timing policy and typed style profile in bounded source tasks.
   Every task links one global phase, its requirement/contract/gate, a
   specimen and its refusal case.
4. **Write the runtime/backend decision.** Compare a small set only after
   defining target OS, renderer capability needs, input/window requirements,
   distribution format and performance budget. Evaluate measured prototype
   constraints, integration cost, maintainability and licensing/provenance.
   Do not migrate language or adopt a host engine merely because a source used
   it.
5. **Specify the first interactive slice.** Define transforms/camera/state
   shape, input sampling boundary, presentation adapter, minimal asset intake,
   one style profile, diagnostics and a runnable launcher. Decide what is
   simulated versus displayed. Preserve the spinal column's publication
   boundary through the adapter.
6. **Qualify the actual artifact.** Require rendered inspection, interaction,
   clean launch, missing-resource/refusal paths, and measured timing on named
   hardware. Keep these results separate from unit/type/doc checks.
7. **Expand through evidence.** Collision/physics, asset pipelines, scene
   authoring, audio, persistence, packaging and wider platform support each
   need their own discovery/specification tasks. Do not label them
   implemented or commit a full-engine schedule before their scope is known.

The global plan should own phase outcomes and exit gates. Individual task
records should own current task status, dependencies and acceptance evidence.
Research records should own source provenance and limitations. A completed
planning document does not close an implementation task; an implementation
task closes only when its specific acceptance evidence exists [RQ02], [RQ03].

### Gaps: section 3

Target hardware, production language, graphics backend, first demonstrator
scene, numeric style budgets, and a release/distribution target were not
settled by the sources reviewed. Record them as bounded decisions with an
owner and required comparison evidence. They do not block documentation
realignment or continued correctness work on the current prototype.

## (Y) Link-complete usage index

This index only references the definitions below.

- Context: [DOC], [GL01], [GL02], [GL03], [DP01], [DP02], [DP03].
- Requirements: [RQ01], [RQ02], [RQ03].
- Sources: [RS01], [RS02], [RS03], [RS04], [RS05], [RS06], [RS07],
  [RS08], [RS09], [RS10], [RS11], [RS12], [RS13], [RS14], [RS15], [RS16].

## (Z) Context-Citations

[DOC]: TECHNICAL_RESEARCH_REALIGNMENT
  "Primary-source review for 4GINE development planning at repository baseline
  9afd1cf on 2026-11-07; recommendations are separate from verified support."

[GL01]: RECHECK_RESEARCH_SUPPORT
  "Verify the earlier research's limited claims and preserve its provenance."

[GL02]: DEFINE_MEASURABLE_GATES
  "Convert actual evidence limits into explicit development acceptance gates."

[GL03]: MAKE_FUTURE_WORK_REPRODUCIBLE_AND_BOUNDED
  "Sequence prototype reliability and later interactive application decisions."

[DP01]: ORIGINAL_SOURCES_AND_PROJECT_RECORDS
  "Existing live research, proposal, design and directly consulted sources."

[DP02]: VERIFIED_LANGUAGE_AND_ENGINE_BEHAVIOR
  "Official Python behavior and primary engine/evaluation documentation."

[DP03]: PROJECT_SCOPE_AND_TOOLCHAIN_RECORD
  "Explicit intended user outcome, supported environment and current contracts."

[RQ01]: SEPARATE_SUPPORT_FROM_INFERENCE
  "External evidence may constrain project hypotheses but cannot establish
  SPINALTAP correctness or originality without project-specific evaluation."

[RQ02]: PROMOTION_MATCHES_ACTUAL_EVIDENCE
  "A planning record, a schema check, a behavioral specimen, a performance
  measurement and a rendered acceptance result establish different claims."

[RQ03]: DISTINGUISH_PROTOTYPE_FROM_PRODUCT
  "Do not imply that prototype tooling chooses the production stack or that
  a finished planning phase proves a usable game engine."

[RS01]: RESEARCH_SOURCE
  "TITLE: Fix Your Timestep! AUTHOR: Glenn Fiedler. DATE: 2004-06-10.
  LINK: https://gafferongames.com/post/fix_your_timestep/.
  ACCESSED: 2026-11-07. USED_FOR: time ownership and overload tradeoffs.
  CONTEXT_WEIGHT: MEDIUM. LIMIT: practical timing guidance, not engine proof."

[RS02]: RESEARCH_SOURCE
  "TITLE: Simulation. SOURCE: Box2D official documentation, page header 3.2.0.
  LINK: https://box2d.org/documentation/md_simulation.html.
  ACCESSED: 2026-11-07. USED_FOR: stepping and scoped determinism.
  CONTEXT_WEIGHT: MEDIUM. LIMIT: 2D rigid-body implementation precedent."

[RS03]: RESEARCH_SOURCE
  "TITLE: dataclasses. SOURCE: Python 3.13 documentation.
  LINK: https://docs.python.org/3.13/library/dataclasses.html.
  ACCESSED: 2026-11-07. USED_FOR: type and frozen-record semantics.
  CONTEXT_WEIGHT: HIGH for Python behavior, LOW for engine architecture."

[RS04]: RESEARCH_SOURCE
  "TITLE: types.MappingProxyType. SOURCE: Python 3.13 documentation.
  LINK: https://docs.python.org/3.13/library/types.html#types.MappingProxyType.
  ACCESSED: 2026-11-07. USED_FOR: dynamic read-only view semantics.
  CONTEXT_WEIGHT: HIGH for Python behavior, LOW for engine architecture."

[RS05]: RESEARCH_SOURCE
  "TITLE: Floating-Point Arithmetic: Issues and Limitations.
  SOURCE: Python 3.13 tutorial.
  LINK: https://docs.python.org/3.13/tutorial/floatingpoint.html.
  ACCESSED: 2026-11-07. USED_FOR: numerical tolerance and precision limits.
  CONTEXT_WEIGHT: HIGH for number behavior, LOW for architecture."

[RS06]: RESEARCH_SOURCE
  "TITLE: Writing your pyproject.toml. SOURCE: Python Packaging User Guide.
  LINK: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/.
  ACCESSED: 2026-11-07. USED_FOR: explicit prototype tooling metadata.
  CONTEXT_WEIGHT: MEDIUM. LIMIT: metadata is not environment reproducibility."

[RS07]: RESEARCH_SOURCE
  "TITLE: venv. SOURCE: Python 3.13 documentation.
  LINK: https://docs.python.org/3.13/library/venv.html.
  ACCESSED: 2026-11-07. USED_FOR: isolated and recreatable local environment.
  CONTEXT_WEIGHT: HIGH for interpreter mechanics, LOW for production stack."

[RS08]: RESEARCH_SOURCE
  "TITLE: Direct3D Architecture (Direct3D 9). SOURCE: Microsoft Learn.
  UPDATED: 2021-01-06.
  LINK: https://learn.microsoft.com/en-us/windows/win32/direct3d9/direct3d-architecture.
  ACCESSED: 2026-11-07. USED_FOR: explicit rendering constraint axes.
  CONTEXT_WEIGHT: MEDIUM. LIMIT: no universal retro style or backend choice."

[RS09]: RESEARCH_SOURCE
  "TITLE: ICFP Artifacts, Evaluation Guidelines. SOURCE: ICFP 2026 committee.
  LINK: https://icfp26.sigplan.org/track/icfp-2026-artifact-evaluation.
  ACCESSED: 2026-11-07. USED_FOR: executable evidence tied to stated claims.
  CONTEXT_WEIGHT: MEDIUM. LIMIT: conference practice, not 4GINE certification;
  inconsistent availability-badge sections are not relied upon."

[RS10]: RESEARCH_SOURCE
  "TITLE: Creating Examples. SOURCE: Bevy contribution documentation.
  LINK: https://bevy.org/learn/contribute/helping-out/creating-examples/.
  ACCESSED: 2026-11-07. USED_FOR: focused examples versus visual testbeds.
  CONTEXT_WEIGHT: LOW. LIMIT: no obligation to copy Bevy workflows."

[RS11]: RESEARCH_SOURCE
  "TITLE: Position Based Dynamics. AUTHORS: Matthias Mueller, Bruno
  Heidelberger, Marcus Hennix, John Ratcliff. YEAR: 2006.
  LINK: https://matthias-research.github.io/pages/publications/posBasedDyn.pdf.
  ACCESSED: 2026-11-07. USED_FOR: position-space correction precedent.
  CONTEXT_WEIGHT: LOW. LIMIT: no general vertebra or engine correctness proof."

[RS12]: RESEARCH_SOURCE
  "TITLE: ECS. SOURCE: Bevy Quick Start.
  LINK: https://bevy.org/learn/quick-start/getting-started/ecs/.
  ACCESSED: 2026-11-07. USED_FOR: data/logic separation and order caveat.
  CONTEXT_WEIGHT: LOW. LIMIT: architecture is not selected for 4GINE."

[RS13]: RESEARCH_SOURCE
  "TITLE: Using SceneTree; Nodes and Scenes. SOURCE: Godot stable docs.
  LINKS: https://docs.godotengine.org/en/stable/tutorials/scripting/scene_tree.html
  and https://docs.godotengine.org/en/stable/getting_started/step_by_step/nodes_and_scenes.html.
  ACCESSED: 2026-11-07. USED_FOR: composition, activation and order precedent.
  CONTEXT_WEIGHT: LOW. LIMIT: stable URL is moving; no scene-tree adoption."

[RS14]: RESEARCH_SOURCE
  "TITLE: Unit testing. SOURCE: Godot stable documentation.
  LINK: https://docs.godotengine.org/en/stable/engine_details/architecture/unit_testing.html.
  ACCESSED: 2026-11-07. USED_FOR: dedicated assertions and failure checks.
  CONTEXT_WEIGHT: LOW. LIMIT: C++ testing precedent, not selected tooling."

[RS15]: RESEARCH_SOURCE
  "TITLE: OpenGL Registry. SOURCE: Khronos Group.
  LINK: https://registry.khronos.org/OpenGL/index_gl.php.
  ACCESSED: 2026-11-07. USED_FOR: locating historical specifications.
  CONTEXT_WEIGHT: LOW. LIMIT: index does not define visual budgets."

[RS16]: RESEARCH_SOURCE
  "TITLE: Samples. SOURCE: Box2D documentation, page header 3.1.0.
  LINK: https://box2d.org/documentation/samples.html.
  ACCESSED: 2026-11-07. USED_FOR: inspectable testbed and library separation.
  CONTEXT_WEIGHT: LOW. LIMIT: demo features do not prove 4GINE behavior."
