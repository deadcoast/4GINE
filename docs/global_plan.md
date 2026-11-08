# 4GINE global development plan [DOC]

This is the authority for delivery scope, phase order and completion gates.
Individual status belongs only to the [workstream TODOs](README.md).
[Requirements](requirements.md) and [design](design.md) own technical
contracts; the [research catalogue](research_plan.md) retains theory and source
context. This plan realigns development on 2026-11-07 against runtime baseline
9afd1cf; it does not claim new engine behavior [GL01].

## Direction and current boundary

> Goal: [GL01] - CONNECT_THE_PROTOTYPE_TO_A_USABLE_ENGINE
> Dependency: [DP01] - PRESERVED_RESEARCH_AND_VERIFIED_BASELINE
> Requirement: [RQ01] - SEPARATE_HORIZONS_AND_ACCEPTANCE

4GINE's long-term direction is a usable 3D game engine organized around
SPINALTAP: bounded nervous-system families contain local vertebra solvers,
while the spinal column routes and reconciles their outputs. Algorithmic
stems pass bounded results to their parents. Scope and ownership must carry
technical meaning; biological names alone do not establish an architecture.

The accepted first horizon is a research prototype. Today it is a Python
standard-library scalar contract and reconciliation harness, with a CLI and
87 passing internal tests at the reviewed revision. It has no renderer,
interactive application loop, asset pipeline, general physics, editor or
distributed application. Python is the current specimen language; the final
engine stack has not been selected. See the [source review][S01].

The second horizon is one explicitly defined interactive 3D demonstrator.
The third is a qualified application and a process for admitting further
engine capabilities. Those horizons need their own requirements and measured
acceptance. The existing fifteen prototype requirements are not a complete
product specification.

The original exclusions remain: no disguised ECS/scene-tree/solver/renderer
clone, no unbounded hidden state mutation, and no traditional pixel-art
direction presented as the engine solution. The eight theory candidates,
seven research lanes, fifteen style categories and eleven original sources
remain available for research. They are not a promise to deliver eight engines
or fifteen rendering modes.

## Authority and phase rules

> Goal: [GL02] - KEEP_ONE_AUTHORITY_FOR_EACH_PLANNING_FACT
> Dependency: [DP02] - GLOBAL_PHASES_AND_CANONICAL_TASK_CARDS
> Requirement: [RQ02] - TRACE_EVERY_SLICE_TO_ITS_PARENT

| Concern | Authority | Update |
| --- | --- | --- |
| Delivery scope and gates | This plan | Change with scope or exit evidence |
| Technical meaning | requirements.md, design.md | Before behavior changes |
| Task status and acceptance | docs/todos/*.md | Change the owning card only |
| Current next task | Root TODO.md | Point to ready work |
| Research provenance | Dated source records | Preserve dates and supersession |
| Verification results | Linked evidence | Name revision, command and limits |
| Historical completion | Original ledgers | Preserve the original scope |

P1-P5 are delivery phases. WL01-WL05 remain the original research-to-source
method; they are not renamed milestones. ST identifiers are global task keys.
Pseudo-citation IDs remain document-local, so use qualified forms such as
TODO.md::TK05 and research_plan.md::MO01 when crossing files.

A phase closes only when its required cards are done **and** its exit evidence
is reviewed against the phase outcome. Task counts alone do not certify a
phase. Deferred optional cards are named below and cannot silently become
required implementation. Independent policy analysis can proceed early;
implementation observes dependencies and phase admission. No calendar dates or
production backend are promised before scope and measurements justify them.

The next development task is reached through the [root queue](../TODO.md).
The roadmap keeps no second mutable task-status table.

## P1: Reproduce and maintain the development baseline

> Goal: [GL03] - MAKE_A_FRESH_CHECKOUT_REPRODUCIBLE
> Dependency: [DP03] - EXISTING_RUNNABLE_SCALAR_PROTOTYPE
> Requirement: [RQ03] - RECORD_TOOLS_AND_VALIDATE_PLANNING

Outcome: a new contributor can bootstrap the prototype and run its accepted
checks without undocumented global installations or personal cache paths.

Admission: the current source baseline and this realignment's evidence.
Required work: tooling decision, bootstrap, automated checks, and the planning
consistency workflow. The historical IDE export is an optional diagnostic
follow-up; it cannot substitute for fresh command evidence.

Exit: a clean-environment run identifies interpreter/tool versions and source
revision, runs the demo and runtime suite, passes the selected static and
documentation checks, and demonstrates that planning drift fails validation.
The required checks and any deliberately optional tools have a recorded
decision. This chooses prototype tooling, not the production engine stack.

The [accepted tooling policy](decisions/prototype_toolchain.md) specifies
versions, required checks and the clean-environment qualification procedure.
The [bootstrap qualification](../reports/ST-002%20bootstrap%20qualification.md)
records cold and repeated Windows setup with refusal evidence. P1 also requires
automation through ST-003 and aggregate exit review; local qualification alone
does not close the phase.

Required cards:

-
  [ST-001](todos/tooling.md#st-001-choose-the-prototype-toolchain-and-required-checks)
-
  [ST-002](todos/tooling.md#st-002-provide-a-repeatable-bootstrap-and-verification-entry-point)
- [ST-003](todos/tooling.md#st-003-automate-the-accepted-repository-checks)
-
  [ST-034](todos/tooling.md#st-034-establish-the-global-plan-and-task-consistency-workflow)

Optional diagnostic card:

-
  [ST-004](todos/tooling.md#st-004-refresh-or-retire-the-historical-ide-diagnostic-intake)

## P2: Make prototype claims and state boundaries trustworthy

> Goal: [GL04] - ALIGN_POLICY_IMPLEMENTATION_AND_EVIDENCE
> Dependency: [DP04] - REPRODUCIBLE_CHECKS_AND_EXPLICIT_CONTRACTS
> Requirement: [RQ04] - NO_PROMOTION_FROM_PROSE_OR_LABELS

Outcome: source influence, proof promotion, timing identity and scalar state
authority have explicit policies with positive and refused specimens.

Admission: P1's reproducible development path before source expansion.
Independent proof, governor and timing decisions may be drafted while P1
tooling is prepared. Source work follows the cards' prerequisites.

Resolve the governor minimum-versus-mean divergence without pretending either
formula is empirically calibrated. Separate proof-plan readiness from executed
evidence. Distinguish caller-declared keys from authorization, and returned
candidate atomicity from storage durability or callback rollback.

Exit: version/compatibility rules, reachable governor decisions and provenance,
evidence-backed proof states, declared replay/overload scope, registered scalar
authority and whole-candidate checks have their own refusal evidence. The
requirement matrix records what is implemented and what remains deferred.
REQ08/REQ14 remain pending numeric/rendered style qualification in P3/P4;
acknowledging that gap is not satisfying those requirements.

Required cards:

-
  [ST-005](todos/contracts.md#st-005-specify-contract-identity-and-schema-evolution)
-
  [ST-006](todos/contracts.md#st-006-implement-version-aware-ingress-and-migration-fixtures)
-
  [ST-007](todos/governance.md#st-007-resolve-governor-aggregation-and-down-weight-policy)
-
  [ST-008](todos/governance.md#st-008-implement-and-test-the-selected-governor-outcomes)
-
  [ST-009](todos/governance.md#st-009-resolve-source-references-through-a-provenance-record)
- [ST-010](todos/time.md#st-010-specify-time-identity-and-overload-semantics)
-
  [ST-011](todos/time.md#st-011-implement-checkpoint-and-ordered-step-replay-specimens)
- [ST-012](todos/time.md#st-012-measure-overload-and-refused-step-accounting)
- [ST-013](todos/workers.md#st-013-define-worker-authority-and-state-ownership)
- [ST-014](todos/workers.md#st-014-enforce-registered-scalar-worker-authority)
-
  [ST-017](todos/signals.md#st-017-specify-channel-hook-and-candidate-adoption-policy)
-
  [ST-018](todos/signals.md#st-018-validate-and-adopt-authorized-whole-step-candidates)
-
  [ST-023](todos/proof.md#st-023-define-proof-states-and-executed-evidence-semantics)
-
  [ST-024](todos/proof.md#st-024-implement-evidence-records-and-promotion-checks)
-
  [ST-033](todos/contracts.md#st-033-reconcile-the-full-prototype-requirement-evidence-matrix)

## P3: Specify the first 3D use case and measurable data

> Goal: [GL05] - SELECT_ONE_BOUNDED_VISIBLE_OUTCOME
> Dependency: [DP05] - TRUSTWORTHY_PROTOTYPE_AND_PRODUCT_BRIEF
> Requirement: [RQ05] - SPECIFY_BEFORE_EXPANDING_ENGINE_SYSTEMS

Outcome: a small useful scenario determines the state types, one style
profile, one local solver and the presentation/language boundary.

Admission: the P2 requirement/evidence review. Product questions can be
researched earlier, but no renderer or production-stack choice is implied by
the current Python code or external engine examples.

The scenario decision names its intended user, OS/hardware, scene, inputs,
asset needs, failure inspection and measurable acceptance. It must publish
the accepted application requirements and corresponding design extensions,
then update downstream task mappings before new application source begins.
Richer state and style values must have units, bounds and valid categories.
Compare only presentation approaches that can satisfy that scenario; preserve
provenance and the SPINALTAP ownership model.

Exit: an accepted scenario brief and application requirements, typed local
state, a bounded solver fixture, typed DC05 validation, and a recorded
backend/language decision with measured experiments. Chosen numerical budgets
are justified by that profile and target, not invented as universal
historical-console limits.

Required cards:

- [ST-015](todos/workers.md#st-015-specify-the-demonstrators-richer-local-state)
- [ST-016](todos/workers.md#st-016-implement-one-bounded-local-solver-fixture)
- [ST-020](todos/style.md#st-020-define-one-typed-and-measurable-style-profile)
-
  [ST-021](todos/style.md#st-021-implement-typed-profile-decoding-and-budget-checks)
-
  [ST-025](todos/application.md#st-025-define-the-first-useful-interactive-3d-scenario)
-
  [ST-026](todos/application.md#st-026-compare-and-select-the-presentation-and-language-boundary)

## P4: Demonstrate and inspect an interactive 3D slice

> Goal: [GL06] - CONNECT_ACCEPTED_STATE_TO_OBSERVABLE_BEHAVIOR
> Dependency: [DP06] - SELECTED_SCENARIO_AND_PRESENTATION_PATH
> Requirement: [RQ06] - REQUIRE_RENDERED_AND_INTERACTIVE_EVIDENCE

Outcome: the selected user can launch, interact with and inspect one complete
SPINALTAP scenario, including refusals and time behavior.

Admission: P3's accepted brief, application specification and experiments.
Input, fixed updates, local behavior, reconciliation and presentation are
integrated in bounded slices. The renderer consumes accepted state. Asset and
lifecycle work is limited to what the brief requires.

Exit: a direct launcher, repeatable scene and input, measured profile
enforcement, target-specific performance records, captured rendered output,
and human acceptance of the agreed workflow. Automated checks, GPU output,
performance measurements and user review are separate evidence. A visible
window or passing scalar suite cannot replace them.

Required cards:

- [ST-022](todos/style.md#st-022-measure-profile-enforcement-in-rendered-output)
-
  [ST-027](todos/application.md#st-027-build-the-integrated-interactive-demonstrator)
-
  [ST-028](todos/application.md#st-028-qualify-the-scenes-performance-and-visual-behavior)
-
  [ST-029](todos/application.md#st-029-record-human-acceptance-of-the-intended-workflow)

## P5: Qualify the application and admit further capabilities

> Goal: [GL07] - DELIVER_THE_ACCEPTED_APPLICATION_SCOPE
> Dependency: [DP07] - INTERACTIVE_ACCEPTANCE_AND_DISTRIBUTION_DECISION
> Requirement: [RQ07] - VERIFY_THE_INSTALLED_ARTIFACT

Outcome: the agreed application can be built, distributed and used in its
supported environment, with a controlled path for future engine work.

Admission: P4's accepted scenario. Choose the supported install/run/update
workflow and artifact format explicitly.

Exit: an identified release artifact with source revision and digest,
repeatable build and install instructions, dependency/asset provenance,
installed-workflow verification, retained acceptance evidence and known
limitations. Broader platform or complete-engine claims need new scope and
acceptance records.

Required cards:

-
  [ST-030](todos/application.md#st-030-specify-and-implement-the-first-distribution-workflow)
-
  [ST-031](todos/application.md#st-031-qualify-a-reproducible-application-release)

Optional discovery remains separate. Concurrency, durable commits, conflict
merging, stronger hook isolation, audio, authoring, physics, networking and
additional platforms/styles require an accepted use case before implementation
cards are admitted. They are not hidden prerequisites of P4 or this release.

Deferred discovery cards:

-
  [ST-019](todos/signals.md#st-019-decide-whether-stronger-publication-guarantees-are-needed)
-
  [ST-032](todos/application.md#st-032-admit-further-engine-capabilities-through-scoped-decisions)

## Decisions that control later development

> Goal: [GL02] - KEEP_ONE_AUTHORITY_FOR_EACH_PLANNING_FACT
> Dependency: [DP02] - GLOBAL_PHASES_AND_CANONICAL_TASK_CARDS
> Requirement: [RQ02] - TRACE_EVERY_SLICE_TO_ITS_PARENT

| Decision | Current uncertainty | Owning task |
| --- | --- | --- |
| Prototype tooling | Python, environment and checkers | ST-001 |
| Proof lifecycle | Planning-ready versus executed/accepted evidence | ST-023 |
| Governor policy | Minimum versus mean, threshold and down-weight | ST-007 |
| Contract evolution | Version identity and compatibility | ST-005 |
| Time semantics | Backlog, refused steps and replay | ST-010 |
| State authority | Owner lifecycle and state | ST-013 |
| Publication boundary | Channels, invariants and hook trust | ST-017 |
| First application | User, hardware, scenario and budgets | ST-025 |
| Typed style | Units, categories and one selected profile | ST-020 |
| Presentation boundary | Backend and language integration | ST-026 |
| Distribution | Supported artifact and installation workflow | ST-030 |

Decisions are owned by the canonical task's workstream. Their final rationale
belongs in the relevant requirement/design section or a linked scoped decision
artifact. Do not create a parallel decision database carrying duplicate status.

## Evidence and scope discipline

> Goal: [GL08] - MATCH_EACH_CLAIM_TO_ITS_EVIDENCE
> Dependency: [DP08] - DATED_REVIEW_AND_EXECUTED_CHECKS
> Requirement: [RQ08] - NEVER_INFER_PRODUCT_READINESS_FROM_INTERNAL_SPECIMENS

Use the original EV01-EV05 meanings within their defining documents; a tier
does not make evidence universally applicable. Record a claim's actual scope:
source inspection, schema validation, unit/refusal specimen, integrated
runtime, rendered output, performance measurement, installed artifact or human
acceptance. Evidence records identify date, source and contract revision,
command/scenario, environment, expected/actual result, artifact and limits.

The 2026-11-07 baseline passed 87 runtime tests and Pyright; the default demo
accepted 14 updates and ended at x=0.672, y=-0.336. These results support the
current scalar implementation. They do not establish numeric style semantics,
executed proof promotion, cross-platform replay, 3D output or release quality.
The [realignment report][S02] records checks and the three reproduced semantic
gaps. The [technical research][S03] records primary sources and influence
limits.

Historical complete labels stay attached to their original slice. A new task
closes only with its own acceptance and evidence. If a source or check is
unavailable, record the gap and affected claim; never convert it to a pass.

## (Y) Link-complete usage index [LI]

- Identity and sources: [DOC], [LI], [S01], [S02], [S03]
- Goals: [GL01], [GL02], [GL03], [GL04], [GL05], [GL06], [GL07], [GL08]
- Dependencies: [DP01], [DP02], [DP03], [DP04], [DP05], [DP06], [DP07], [DP08]
- Requirements: [RQ01], [RQ02], [RQ03], [RQ04], [RQ05], [RQ06], [RQ07], [RQ08]

## (Z) Context-Citations

[DOC]: GLOBAL_DELIVERY_PLAN
  "The current authority for 4GINE delivery horizons, phase order and exit
  gates."

[GL01]: CONNECT_THE_PROTOTYPE_TO_A_USABLE_ENGINE
  "Retain SPINALTAP intent while separating the existing scalar prototype from
  a scoped interactive demonstrator and a qualified application."

[GL02]: KEEP_ONE_AUTHORITY_FOR_EACH_PLANNING_FACT
  "Global scope, technical semantics, task status and evidence each have a
  single owning document surface."

[GL03]: MAKE_A_FRESH_CHECKOUT_REPRODUCIBLE
  "A contributor can install declared tooling and reproduce accepted checks."

[GL04]: ALIGN_POLICY_IMPLEMENTATION_AND_EVIDENCE
  "Resolve prototype policy gaps and verify the claimed state boundaries."

[GL05]: SELECT_ONE_BOUNDED_VISIBLE_OUTCOME
  "Let an accepted application scenario determine state, style and
  presentation."

[GL06]: CONNECT_ACCEPTED_STATE_TO_OBSERVABLE_BEHAVIOR
  "Integrate a directly inspectable interactive 3D scenario with refusal paths."

[GL07]: DELIVER_THE_ACCEPTED_APPLICATION_SCOPE
  "Qualify the distributed application without expanding unapproved promises."

[GL08]: MATCH_EACH_CLAIM_TO_ITS_EVIDENCE
  "Require evidence appropriate to the exact behavior and environment claimed."

[DP01]: PRESERVED_RESEARCH_AND_VERIFIED_BASELINE
  "Existing theory, sources, requirements, contracts and dated scalar evidence."

[DP02]: GLOBAL_PHASES_AND_CANONICAL_TASK_CARDS
  "P identifiers belong to this plan; globally unique ST cards own task status."

[DP03]: EXISTING_RUNNABLE_SCALAR_PROTOTYPE
  "The reviewed package and CLI provide the baseline for reproducible setup."

[DP04]: REPRODUCIBLE_CHECKS_AND_EXPLICIT_CONTRACTS
  "Reliable prototype changes depend on the accepted tooling and schema policy."

[DP05]: TRUSTWORTHY_PROTOTYPE_AND_PRODUCT_BRIEF
  "Richer state and style require an accepted use case and its evidence needs."

[DP06]: SELECTED_SCENARIO_AND_PRESENTATION_PATH
  "Integration follows the chosen scope, typed data and presentation
  experiments."

[DP07]: INTERACTIVE_ACCEPTANCE_AND_DISTRIBUTION_DECISION
  "Distribution follows acceptance of the intended application workflow."

[DP08]: DATED_REVIEW_AND_EXECUTED_CHECKS
  "Source findings and recorded checks establish bounded evidence, not
  promises."

[RQ01]: SEPARATE_HORIZONS_AND_ACCEPTANCE
  "Prototype, interactive demonstration and release have separate exit
  evidence."

[RQ02]: TRACE_EVERY_SLICE_TO_ITS_PARENT
  "Each canonical task names a global phase, requirements and prerequisites."

[RQ03]: RECORD_TOOLS_AND_VALIDATE_PLANNING
  "Setup and checks must be reproducible; planning relationships must be
  checked."

[RQ04]: NO_PROMOTION_FROM_PROSE_OR_LABELS
  "Nonblank evidence text and ownership labels cannot prove execution or
  authority."

[RQ05]: SPECIFY_BEFORE_EXPANDING_ENGINE_SYSTEMS
  "Choose bounded use cases, types, budgets and failure rules before source
  work."

[RQ06]: REQUIRE_RENDERED_AND_INTERACTIVE_EVIDENCE
  "A 3D claim needs inspected output and actual workflow evidence."

[RQ07]: VERIFY_THE_INSTALLED_ARTIFACT
  "Release claims apply to the exact built artifact and supported environment."

[RQ08]: NEVER_INFER_PRODUCT_READINESS_FROM_INTERNAL_SPECIMENS
  "A passing scalar suite does not establish rendering, performance or
  acceptance."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative invocation list for every local context marker."

[S01]: ../research_notes/4GINE%20development%20realignment/source_review.md
  "Complete source/test review and current requirement evidence boundaries."

[S02]: ../reports/4GINE%20development%20realignment.md
  "Dated synthesis and realignment verification record."

[S03]: ../research_notes/4GINE%20development%20realignment/technical_research.md
  "Verified primary-source support, limitations and project-specific
  inferences."
