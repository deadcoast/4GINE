# Application discovery and qualification [DOC]

The long-term direction is a usable SPINALTAP 3D engine. The first interactive
application, hardware, backend, language boundary and release target are not
yet selected.

> Goal: [GL01] - DELIVER_BOUNDED_TRACEABLE_SLICES
> Dependency: [DP01] - GLOBAL_PLAN_AND_TECHNICAL_CONTRACTS
> Requirement: [RQ01] - ACCEPTANCE_AND_EVIDENCE_BEFORE_COMPLETION

Follow the [global plan](../global_plan.md) and
[development workflow](../development_workflow.md). Requirements below refer
only to [requirements.md](../requirements.md); DC/VG meanings come from
[design.md](../design.md). ST identifiers are global task keys, while bracketed
context markers are local to this document.

## Scope and source map

- [Demo](../../spinaltap/demo.py)
- [CLI](../../spinaltap/__main__.py)
- [Demo tests](../../tests/test_demo.py)
- [Original scope](../proposal.md)

## Individual TODOs

### ST-025: Define the first useful interactive 3D scenario

- Status: planned
- Phase: P3
- Requirements: REQ01, REQ02, REQ03, REQ15
- Depends on: ST-033
- Owner: application
- Legacy: New application admission decision
- Scope: Select intended user, target OS/hardware, minimal scene, input,
  reset/pause, inspectable refusals, asset needs and measurable success.
- Acceptance: Record one small use case and explicit exclusions with an owner
  decision. Define visual/latency/frame budgets to be measured and required
  user acceptance. Publish accepted application requirements and design
  extensions, then update downstream task requirement mappings before new
  application source work. This brief admits a demonstrator; it does not
  promise a complete renderer, physics engine, editor, network stack or every
  style category.
- Evidence: pending

### ST-026: Compare and select the presentation and language boundary

- Status: planned
- Phase: P3
- Requirements: REQ01, REQ02, REQ03
- Depends on: ST-015, ST-020, ST-025
- Owner: application
- Legacy: New architecture decision
- Scope: Compare a small set of viable presentation approaches against the
  accepted use case while preserving SPINALTAP scope ownership.
- Acceptance: Run bounded experiments that measure integration cost and
  required capabilities. Record chosen backend, runtime/language boundary,
  dependencies, provenance/licensing constraints, hardware support and
  rejected alternatives. No production stack is selected merely because an
  external research source uses it. Define the runnable build path before P4.
- Evidence: pending

### ST-027: Build the integrated interactive demonstrator

- Status: planned
- Phase: P4
- Requirements: REQ01, REQ02, REQ05, REQ06, REQ07, REQ08, REQ12, REQ13
- Depends on: ST-011, ST-016, ST-018, ST-021, ST-024, ST-026
- Owner: application
- Legacy: Extends demo.py and __main__.py beyond the current CLI
- Scope: Connect input, fixed updates, the bounded solver, reconciliation and
  presentation under the selected application lifecycle.
- Acceptance: Provide an obvious direct launcher and controlled sample scene.
  Presentation reads only accepted state; refusal inspection, reset/pause and
  overload behavior follow the brief. Smoke tests exercise lifecycle/failure
  paths and a rendered run demonstrates interaction. A running window alone
  does not close visual or performance acceptance.
- Evidence: pending

### ST-028: Qualify the scene's performance and visual behavior

- Status: planned
- Phase: P4
- Requirements: REQ02, REQ08, REQ11, REQ14, REQ15
- Depends on: ST-012, ST-022, ST-027
- Owner: application
- Legacy: New target-specific qualification
- Scope: Evaluate the accepted budgets on the named hardware and distinguish
  measurement from perception.
- Acceptance: Record repeatable inputs, scene/asset versions, warm-up/sample
  method, frame/step measurements and captures. Exercise overload, refusal,
  pause/reset and representative worst cases. Compare results with the brief
  and list failures or limits explicitly. Do not infer other hardware/platform
  performance from this run.
- Evidence: pending

### ST-029: Record human acceptance of the intended workflow

- Status: planned
- Phase: P4
- Requirements: REQ02, REQ09, REQ15
- Depends on: ST-028
- Owner: application
- Legacy: New interactive acceptance
- Scope: Have the project owner or designated user exercise the agreed
  scenario using the runnable artifact.
- Acceptance: Record who reviewed which revision, the scenario and observed
  usability/visual outcomes. Capture defects as new linked cards and
  distinguish acceptance from automated checks. Close only when the agreed
  success criteria are met or an explicit scope decision changes them.
- Evidence: pending

### ST-030: Specify and implement the first distribution workflow

- Status: planned
- Phase: P5
- Requirements: REQ02, REQ03, REQ15
- Depends on: ST-029
- Owner: application
- Legacy: New application packaging
- Scope: Choose a supported installation/run/update path and required
  asset/dependency packaging for the accepted application.
- Acceptance: Document artifact format, target environment, version identity,
  provenance, licenses and reproducible build instructions. Test install,
  launch, missing-resource behavior and removal in an isolated target
  environment. Do not add cross-platform release promises without acceptance
  scope.
- Evidence: pending

### ST-031: Qualify a reproducible application release

- Status: planned
- Phase: P5
- Requirements: REQ02, REQ09, REQ15
- Depends on: ST-003, ST-030
- Owner: application
- Legacy: New release gate
- Scope: Connect repeatable build/verification to the actual distributed
  artifact.
- Acceptance: Identify the exact source and artifact digest, dependency/tool
  versions, install environment and successful user workflow. Retain
  build/runtime/visual evidence and known limitations. A source checkout or
  unit-test pass does not replace installed-artifact verification; release
  only the accepted scope.
- Evidence: pending

### ST-032: Admit further engine capabilities through scoped decisions

- Status: deferred
- Phase: P5
- Requirements: REQ01, REQ02, REQ03
- Depends on: ST-025
- Owner: application
- Legacy: Long-term engine horizon
- Scope: Preserve discovery for assets, collision/physics, audio,
  authoring/editor tools, scripting, networking and additional
  platforms/styles.
- Acceptance: For each requested capability, document the user outcome,
  SPINALTAP owner, contracts, dependencies, non-goals and acceptance evidence
  before creating implementation cards. Keep rejected or deferred directions
  visible. These examples are a future capability catalogue, not an approved
  feature checklist.
- Evidence: pending

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: CANONICAL_WORKSTREAM_TODO
  "Application discovery and qualification; authoritative individual task status and acceptance live here."

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
