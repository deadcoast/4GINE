# 4GINE planning and catalogue review [DOC]

Review date: 2026-11-07. Baseline: commit `9afd1cf`. This note reviews the
repository's document bodies, context registries, historical drafts, and task
relationships. It proposes planning structure; it does not implement runtime
features or assert that a design promise is satisfied by code [DOC].

The companion [catalogue inventory](catalogue_inventory.json) records tracked
Markdown paths, definition locations, reference locations, and bounded local
path checks. Live runtime verification belongs to the coordinator's evidence
and the separate source review.

## Which catalogue and project intent must survive? [GL01]

> Goal: [GL01] - PRESERVE_PROJECT_INTENT_AND_PROVENANCE
> Dependency: [DP01] - EXISTING_DOCUMENT_CHAIN
> Requirement: [RQ01] - DO_NOT_REPLACE_HISTORY_WITH_CURRENT_STATUS

### Takeaway 1

The repository already has a substantial research-to-contract chain. The
missing layer is a current, global delivery plan that joins that chain to
individual source tasks and clearly identifies historical snapshots. Preserve
the catalogue; change its navigation and authority rules.

### Cited findings 1

The current project document set consists of README, root TODO, seven core
documents under `docs`, and a historical changelog. Their roles follow from the
files themselves:

- **[README](../../README.md)**. Established content and role: Current scalar
  prototype, commands, six contracts, source behavior, destination and gaps;
  Recommended treatment: Keep as entry point; retain the three exact opening
  labels.
- **[Root TODO](../../TODO.md)**. Established content and role: IDE intake,
  eight source modules, twelve tasks and seven verification records;
  Recommended treatment: Preserve history; add global-plan and canonical-task
  navigation.
- **[Research plan](../../docs/research_plan.md)**. Established content and
  role: Method, guardrails, workflow, theories, research lanes, styles and
  evidence ladder; Recommended treatment: Keep methodological authority and
  full catalogue.
- **[Live research](../../docs/live_research.md)**. Established content and
  role: First research pass, eleven sources, lane decisions, six formulations;
  Recommended treatment: Keep dated research snapshot; add current-context
  navigation.
- **[Proposal](../../docs/proposal.md)**. Established content and role:
  Selected bounded prototype scope, six design modules, six contracts and
  gates; Recommended treatment: Keep scope rationale; identify original
  proposal phase.
- **[Requirements](../../docs/requirements.md)**. Established content and
  role: Fifteen numbered prototype requirements and acceptance conditions;
  Recommended treatment: Keep requirement authority; clarify current phase and
  evidence semantics.
- **[Design](../../docs/design.md)**. Established content and role: Conceptual
  flow plus detailed current ingress, timing, constraint and reconciliation
  boundaries; Recommended treatment: Keep technical contract authority.
- **[Docspec tasklist](../../docs/tasklist.md)**. Established content and
  role: Eighteen completed planning tasks; Recommended treatment: Keep
  completed planning history, never reinterpret as product completion.
- **[Source plan](../../docs/sourcecode_plan.md)**. Established content and
  role: Eight initial slices, continued runtime boundaries and traceability
  audit; Recommended treatment: Keep bounded implementation history and
  architectural sequence.
- **[Changelog](../../docs/logs/CHANGELOG.md)**. Established content and role:
  Four historical documentation-edit reports; Recommended treatment: Preserve
  ordinary historical Markdown; repair navigation and append realignment
  entry.

Two draft files under `.user_notes` are tracked despite that directory being
ignored for new files:
[4GINE_v01](../../.user_notes/depreciated_files/4GINE_v01.md)
and [4GINEv02](../../.user_notes/depreciated_files/4GINEv02.md). They preserve
the
original theory and older citation grammar. Their invalid draft syntax is
historical evidence, not current workflow. The other local files there,
`ONBOARDING_v02.md` and `STYLES.md`, were inventoried as local ignored material;
do not make private local notes required dependencies of the public workflow.

The original vision is a research-guided three-dimensional game engine using
bounded nervous-system domains, local vertebra solvers, and spinal-column
aggregation. Algorithmic stems pass bounded results to their parents. The
first accepted build scope is a research prototype, explicitly excluding full
renderer and physics completion. These are compatible horizons, not competing
requirements: [research plan](../../docs/research_plan.md), sections B and E-G;
[proposal](../../docs/proposal.md), sections 2-3; and
[requirements](../../docs/requirements.md), REQ01-REQ03.

The original guardrails exclude direct ECS, scene-tree, solver, or renderer
clones and traditional pixel art as an engine-level direction. They do not
specify a production language, hardware target, graphics backend, release
platform, or comprehensive application feature set. Those choices remain
explicit discovery work, not implied commitments:
[proposal](../../docs/proposal.md), sections 2-3;
[live research](../../docs/live_research.md), section 6.

The theory catalogue is eight candidates, all retained with decisions:

- **TH01 Signal-Routing Spine**. Live-research disposition: Revise;
  Formulation / design destination: FR01; MG03; DC03; VG03.
- **TH02 Vertebrae Local Solvers**. Live-research disposition: Revise;
  Formulation / design destination: FR02; MG04; DC04; VG04.
- **TH03 Context-Weight Governor**. Live-research disposition: Accept as core
  candidate; Formulation / design destination: FR05; MG01; DC01; VG01.
- **TH04 Style-Constraint Layer**. Live-research disposition: Revise;
  Formulation / design destination: FR04; MG05; DC05; VG05.
- **TH05 Soft-Proof Pipeline**. Live-research disposition: Revise; Formulation
  / design destination: FR06; MG06; DC06; VG06.
- **TH06 Temporal Coherence Controller**. Live-research disposition: Accept as
  core candidate; Formulation / design destination: FR03; MG02; DC02; VG02.
- **TH07 Visual Metric Translator**. Live-research disposition: Revise;
  Formulation / design destination: FR04; MG05; DC05; VG05.
- **TH08 Scope Boundary Allocator**. Live-research disposition: Revise;
  Formulation / design destination: FR01 and explicit ownership boundaries.

Sources: [research plan](../../docs/research_plan.md), section C, and
[live research](../../docs/live_research.md), sections 3-6. Acceptance here
means
research selection, not source completion or empirical originality proof.

Seven research lanes remain available for further investigations: engine-state
routing, local solver behavior, temporal coherence, context weight and
originality, style constraint mathematics, soft-proof and validation, and
module boundary mapping. Their stable local IDs are RL01-RL07:
[research plan](../../docs/research_plan.md), section D.4.

Fifteen style categories remain a vocabulary and research catalogue, not fifteen
committed rendering modes: low-poly 3D; texture-mapped low-poly;
affine-textured;
dithered; vertex-lit; Gouraud-shaded; flat-shaded; billboarded; pre-rendered;
fixed-function; cel/toon-shaded; arcade; early real-time CGI; sixth-generation;
and retro 3D. Preserve SY01-SY15 and their explanations in the
[research plan](../../docs/research_plan.md), section D.9.

The original eleven source records must remain accessible: Bevy ECS; Godot
nodes/scenes and SceneTree; Box2D simulation/samples; Position Based Dynamics;
Fix Your Timestep; ACM plagiarism policy; Khronos OpenGL Registry; Khronos
Fixed Function Pipeline; Microsoft Direct3D 9 Architecture; Godot Unit Testing;
and Bevy Creating Examples. Their recorded access dates belong to the original
2026-05-26 pass. This review does not silently renew those dates or assert that
those sources prove the prototype: [live research](../../docs/live_research.md),
source intake and RS01-RS11 registry.

### Inferences 1

A global roadmap should carry two horizons: finish and qualify the bounded
prototype, then discover and prove a minimal 3D application path. Rendering,
assets, richer simulation, and distribution are future capability decisions,
not permission to claim a complete engine after the existing eight slices.

A navigation catalogue can preserve all theories, sources, styles, modules,
requirements, and historical task meanings without copying every paragraph.
Use direct links and compact crosswalks; keep each original record authoritative
for its own content.

### Gaps 1

There is no accepted minimum end-user application or vertical-slice acceptance
specification in the inspected documents. Exact hardware targets and benchmark
thresholds were explicitly deferred in the original research and have no
resolved successor record in the inspected planning chain.

## Where has planning and evidence drifted? [GL02]

> Goal: [GL02] - SEPARATE_CURRENT_FACTS_FROM_OLD_GATES
> Dependency: [DP02] - DOCUMENT_AND_IDENTIFIER_AUDIT
> Requirement: [RQ02] - RECORD_DISAGREEMENTS_WITHOUT_ERASING_THEM

### Takeaway 2

The problem is mainly conflicting time horizons and disconnected status
ownership, with two substantive policy gaps: measurable style is still a
textual specimen, and proof promotion is structurally defined rather than
execution-backed. Numeric governor policy also diverges from the research
formulation without a decision trail.

### Cited findings 2

1. **Governor formula drift.** FR05 in
   [live research](../../docs/live_research.md), lines 265-275, uses the minimum
   of authority, fit, originality distance, and validation reach. The
   [README](../../README.md) instead describes a bounded arithmetic mean plus
   an originality threshold of 0.20. The proposal and design prescribe the
   factors without resolving this replacement. Root TODO TK05 only asks for
   down-weight behavior. Add an explicit policy-decision task that compares
   counterexamples, records the selected rule, and documents its limitations.
   No cited research establishes either formula as a calibrated detector.
2. **Proof by prose remains insufficiently distinguished.** The
   [requirements](../../docs/requirements.md), DC06, forbid proof by prose;
   [live research](../../docs/live_research.md), section 4.2, requires a
   runnable
   check and validation artifact. Yet
   [source plan](../../docs/sourcecode_plan.md), step 7, describes complete
   claim records becoming implementation-ready. The
   [design](../../docs/design.md), section 4.1, correctly says shape validation
   does not execute a specimen. Reconcile these meanings before using the
   promotion label to close implementation tasks; source review provides the
   actual code boundary.
3. **Style completion wording overreaches.** REQ08/REQ14 require measurable
   limits. [Source plan](../../docs/sourcecode_plan.md), step 6, calls its
   current artifact a measurable style specimen, while
   [design](../../docs/design.md), section 4.1, explicitly limits DC05 fields
   to nonblank strings and leaves numeric budgets pending. Root TODO MO06's
   status label likewise says `MEASURABLE_LIMIT_SPECIMEN_PRESENT`. Describe
   this as textual shape validation, with measurable enforcement still open.
4. **Initial docspec completion is not engine completion.** All eighteen
   [docspec tasks](../../docs/tasklist.md) are checked because they describe
   planning outputs and specimen definitions. Their source-plan traceability
   audit establishes coverage, not satisfaction of every runtime requirement.
   Keep the completion history and place current task status elsewhere.
5. **Old handoffs look like current blocks.** The
   [requirements](../../docs/requirements.md) introduction still says source
   starts after docspec alignment; the
   [proposal](../../docs/proposal.md) handoff says it does not authorize source;
   [live research](../../docs/live_research.md) says the next step is proposal.
   Meanwhile [source plan](../../docs/sourcecode_plan.md), section 1, explicitly
   records the user's continuation authorization and the active bounded
   prototype. Add dated scope/status notices and a current-plan link rather
   than reopening satisfied gates or rewriting history.
6. **Direct test evidence is described as future everywhere.** EV05 definitions
   in [requirements](../../docs/requirements.md),
   [design](../../docs/design.md), and [research
   plan](../../docs/research_plan.md)
   reserve direct tests for a future prototype. The
   [root TODO](../../TODO.md) already records unit specimens. Clarify that
   EV05 is available for the exact behavior tested, while integrated engine,
   rendering, performance, and human acceptance remain separate unproved
   claims. Do not turn a unit-test tier into a universal maturity score.
7. **Local marker IDs collide across files.** Research-plan MO01-MO05 mean
   spinal column, nervous system, vertebrae, docs, and tests. Root TODO
   MO01-MO08 mean concrete source modules. Docspec TK01-TK18 and root
   TK01-TK12 also mean different tasks. This is legal document-local context,
   but dangerous as an unqualified global key:
   [research plan](../../docs/research_plan.md), MO registry;
   [root TODO](../../TODO.md); [docspec tasklist](../../docs/tasklist.md).
8. **The active root queue is dominated by old IDE intake.** Root TODO preserves
   37 historical diagnostics, disposition buckets, module statuses, pending
   tooling decisions, feature gaps, and command results together. Its twelve
   tasks have no unified priority/dependency/acceptance schema. Useful history
   should remain accessible while new work gets explicit global-phase parents:
   [root TODO](../../TODO.md), sections 1-6.
9. **Tooling and validation evidence lack a durable repository workflow.**
   Root TODO records cached CLIs, absent Mypy, and no repository virtualenv.
   The coordinator is collecting fresh commands. Treat the old ledger as
   dated evidence, not the current machine state:
   [root TODO](../../TODO.md), section 5;
   [README](../../README.md), current-state tooling paragraph.
10. **The catalogue is not uniformly navigable or validated.** The bounded
    scan found 736 definitions and 736 unique body references across eight
    current pseudo-cited project documents, with no missing, unused,
    duplicate, misplaced, or zero-placeholder IDs. README has no registry.
    The changelog's three ordinary link definitions have no Z registry, which
    is ordinary historical Markdown rather than a false pseudo-cited document.
    It has a broken `4GINE_v01.md` path and obsolete sandbox download URI:
    [catalogue inventory](catalogue_inventory.json) and
    [changelog](../../docs/logs/CHANGELOG.md).
11. **Control-document links drifted.** Four onboarding paths resolve to
    nonexistent files: three template links and a wrongly relative refresher
    link. Actual template navigation is
[.agents/template/TEMPLATE_ONBOARDING.md](../../.agents/template/TEMPLATE_ONBOARDING.md).
    The refresher/template also depend on an ignored historical onboarding
    copy. Keep `.agents` read-only in this task and give correct navigation
    in the new catalogue: [inventory](catalogue_inventory.json),
    [onboarding](../../.agents/ONBOARDING.md),
    [refresher](../../.agents/REFRESHER.md).

The scan reads complete files, ignores fenced examples and inline code, honors
fence length, and excludes task checkboxes. It checks pseudo markers and inline
filesystem targets, not URL availability or heading anchors. Pseudo-citation
category destinations such as `SOURCE_TODO_LEDGER` are contextual labels, not
filesystem paths. Do not flag them as broken files.

The coordinator separately reports baseline markdownlint findings: 44 issues
across ten current project files, confined to README (28) and CHANGELOG (16).
These are reported baseline results, not a lint run by this researcher. Active
`.agents` files and preserved historical drafts need a separate audit scope;
invalid historical grammar must not be rewritten merely to make a new global
lint command pass.

### Inferences 2

Most stale prose can be repaired by a current-context notice and clear
ownership. Formula, proof, and style policy require explicit design decisions
and later implementation. Documentation must acknowledge those gaps now;
this realignment should not silently implement or bless an arbitrary policy.

### Gaps 2

No durable recorded decision was located for minimum-versus-mean aggregation,
proof execution evidence, final numeric style schema, production backend,
accepted performance budget, or target hardware. These are bounded decision
work items, not reasons to block all independent development.

## How should global planning and individual TODOs stay aligned? [GL03]

> Goal: [GL03] - MAKE_DEVELOPMENT_TRACEABLE_AND_MAINTAINABLE
> Dependency: [DP03] - SINGLE_AUTHORITY_PER_FACT
> Requirement: [RQ03] - EVERY_TASK_HAS_PARENT_AND_ACCEPTANCE

### Takeaway 3

Use one global plan, Markdown task cards as the sole task-status authority,
a small catalogue manifest for path enumeration, and a validator that checks
relationships. Keep research, technical contracts, historical evidence, and
current work connected without repeating their status in parallel ledgers.

### Recommended authority and layout

This is a proposed implementation layout, not a claim that these files exist:

- `README.md`: preserve exact opening labels `CURRENT STATE:`,
  `PLANNED COMPLETED STATE:`, `STILL TODO:` in that order. Use Setext headings
  consistently if necessary to preserve the literal first line and lint clean.
  Summarize the actual code and point to planning; do not repeat task status.
- `docs/global_plan.md`: sole authority for global objectives, product horizons,
  milestone order, admission/exit criteria, non-goals and open product
  decisions.
- `docs/README.md`: navigable catalogue with document roles, full research
  taxonomy, module crosswalk and links to the current plan, tasks, and audit.
- `docs/todos/`: canonical workstream TODO files, each containing individual
  stable task cards. Cover tooling/workflow; contracts; source governance;
  time; workers; signals/reconciliation; style; proof; and future application
  discovery. Group related small modules rather than creating a file per
  incidental Python support file.
- Root `TODO.md`: concise route into the current task cards plus preserved
  intake/source history. Keep existing TK01-TK12 meanings and recorded results;
  explicitly label migrated entries and link their canonical successors.
  No second handwritten current-status table.
- `docs/WORKFLOW.md`: how to select ready work, maintain traceability, record
  design changes, verify the slice and update its evidence. It complements the
  existing onboarding rather than changing the citation grammar.
- `docs/planning_manifest.json`: paths and memberships only, such as active
  docs, task files, historical docs, and required source/test inventory.
  Never copy task statuses, requirements, or acceptance text into this file.
- `scripts/check_planning.py`: standard-library validation of task records,
  references and catalogue coverage. It should fail on drift with file/line
  messages and explain any intentionally historical scope exclusions.
- `reports/4GINE development realignment.md`: dated review and research
  synthesis, with linkable findings and verification limits. This is evidence
  for the realignment, not another live roadmap.

Avoid unnecessary separate decision/status databases. Open decisions can be
individual task cards whose outcomes update the owning requirement/design
section; the global plan lists only decisions that control its horizons.

### Suggested global milestones

These milestones are design recommendations. They avoid invented deadlines,
backends, platforms, or performance targets.

- **P1 Reproducible baseline**. Desired outcome: A fresh checkout can run and
  check the prototype; Exit evidence: Recorded setup, tests, type/lint
  commands and planning validation; Boundary: Does not select production
  engine stack.
- **P2 Trustworthy prototype claims**. Desired outcome: Source influence,
  proof promotion and state authority have explicit policies; Exit evidence:
  Decision records, adversarial specimens, attached results and traces;
  Boundary: Current scalar scope remains visible.
- **P3 Measurable style and richer local state**. Desired outcome: At least
  one bounded profile and required state schema are typed and enforced; Exit
  evidence: Units/ranges, refusal cases, profile fixture and applicable
  integration evidence; Boundary: Fifteen style labels are not fifteen
  delivered modes.
- **P4 Minimal 3D demonstrator**. Desired outcome: One approved use case
  presents reconciled state through a selected presentation path; Exit
  evidence: Runnable artifact, rendered inspection, input/timing behavior,
  target-specific budgets; Boundary: Scope/backend/hardware decisions precede
  implementation.
- **P5 Application qualification**. Desired outcome: The agreed application
  workflow is usable and distributable; Exit evidence: Repeatable install/run,
  representative integration/performance and human acceptance evidence;
  Boundary: Full-engine or release claims require their own acceptance scope.

The existing eight slices are baseline evidence leading into P1, not proof that
P2-P5 are complete. The frozen validator schema uses `## P1: Title` headings
in the global
plan, `### ST-001: Title` task headings under `docs/todos`, and required
`Status`, `Phase`, `Requirements`, `Depends on`, `Acceptance`, and `Evidence`
field bullets. Requirements are comma-separated REQ identifiers; dependencies
are comma-separated ST identifiers or `none`. Each milestone should list
owned tasks and dependencies;
its completion should be derived or checked against canonical task statuses and
its own exit evidence. The original WL01-WL05 are method phases; do not rename
them into product milestones. New milestone IDs need a distinct explicit role.

### Task-card schema

Use a fixed, parseable Markdown field block with individual prose acceptance
criteria. Illustrative syntax is fenced so it is not active task data:

```md
### ST-013: Define execution-backed proof promotion

- Status: ready
- Phase: P2
- Owner: proof
- Requirements: REQ09, REQ15
- Contracts: docs/design.md::DC06
- Gates: docs/design.md::VG06
- Depends on: none
- Legacy: TODO.md::TK10
- Evidence: none

Outcome: Promotion distinguishes a specimen plan from an executed result.
Scope: Define evidence schema, trust boundary, and allowed state transitions.
- Acceptance: Distinguish planned and executed evidence with the criteria below.

Criteria:
1. Planned, executed, failed, and accepted states have explicit meanings.
2. A nonblank plan alone cannot satisfy the executed-result condition.
3. Evidence identifies command, source revision, result and applicable claim.
4. The implementation task and its refusal specimens are linked.
```

Keep stable task IDs globally unique and independent of local pseudo markers.
Use `ST-nnn` IDs for task cards and `P1`, `P2` and later phase IDs in the
global plan. The example task number remains illustrative. Every task
must have one milestone, a workstream owner, requirement references, explicit
scope, dependencies, acceptance criteria, and an evidence field. Future
discovery tasks can link the global scope requirement rather than pretending
that old prototype requirements already specify a renderer.

Allowed states should have fixed meanings: `planned` (not yet ready), `ready`
(dependencies satisfied and acceptance concrete), `in_progress`, `blocked`
(specific
external or prerequisite blocker named), `done` (acceptance and evidence met),
and `deferred` (deliberately outside the current milestone). A dependency-free
record uses `none`, not an invented dependency ID. A completed design decision
needs a linked outcome; a completed source task needs evidence for its actual
behavior. Optional tools may be waived only with a recorded decision and
replacement gate, not a false pass.

### Legacy migration crosswalk

Keep the old task text and historical checks accessible. The mapping below
specifies work ownership rather than requiring a particular new numeric ID.

- **TODO.md::TK01**. Recorded state: Pending; Canonical successor
  responsibility: Tooling: choose and document reproducible managed tooling.
- **TODO.md::TK02**. Recorded state: Conditional pending; Canonical successor
  responsibility: Tooling: decide required type gates; configure Mypy only if
  selected.
- **TODO.md::TK03**. Recorded state: Pending; Canonical successor
  responsibility: Tooling: refresh IDE export; does not block independent
  command checks.
- **TODO.md::TK04**. Recorded state: Done for original slice; Canonical
  successor responsibility: Contracts: preserve ingress evidence; new schemas
  get new tasks.
- **TODO.md::TK05**. Recorded state: Pending; Canonical successor
  responsibility: Governance: resolve formula and down-weight policy, then
  implement/tests.
- **TODO.md::TK06**. Recorded state: Done for original slice; Canonical
  successor responsibility: Time: preserve fixed-step evidence;
  provenance/replay are new tasks.
- **TODO.md::TK07**. Recorded state: Done for original slice; Canonical
  successor responsibility: Workers: preserve scalar-budget evidence; richer
  schemas are new tasks.
- **TODO.md::TK08**. Recorded state: Done for original slice; Canonical
  successor responsibility: Signals: preserve hook evidence;
  authority/isolation are new tasks.
- **TODO.md::TK09**. Recorded state: Pending; Canonical successor
  responsibility: Style: specify typed measurable profile, then implement and
  verify.
- **TODO.md::TK10**. Recorded state: Pending; Canonical successor
  responsibility: Proof: define evidence/promotion policy, then ledger and
  audits.
- **TODO.md::TK11**. Recorded state: Done for original slice; Canonical
  successor responsibility: Reconciliation: preserve scalar-candidate
  evidence; broader state tasks remain open.
- **TODO.md::TK12**. Recorded state: Done for recorded pass; Canonical
  successor responsibility: Workflow: retain old result and make alignment a
  per-change rule.

The separate `docs/tasklist.md::TK01` through `TK18` retain their completed
docspec meanings. Never merge these with same-numbered root tasks.

### Required mapping coverage

Every original requirement should remain visible in the new task coverage:

- **REQ01**. Current planning meaning: Preserve SPINALTAP identity and avoid
  clones; Workstream: All; scope/governance review.
- **REQ02**. Current planning meaning: First implementation is a bounded
  prototype; Workstream: Global plan and application admission.
- **REQ03**. Current planning meaning: Design and task traceability precede
  source; Workstream: Workflow and contract changes.
- **REQ04, REQ10**. Current planning meaning: Source influence and originality
  gate; Workstream: Governance.
- **REQ05, REQ11**. Current planning meaning: Fixed packet timing before
  solver entry; Workstream: Time.
- **REQ06, REQ12**. Current planning meaning: Ordered signal mutation path;
  Workstream: Signals and reconciliation.
- **REQ07, REQ13**. Current planning meaning: Local ownership and bounded
  deltas; Workstream: Workers and reconciliation.
- **REQ08, REQ14**. Current planning meaning: Measurable style limits;
  Workstream: Style.
- **REQ09, REQ15**. Current planning meaning: Specimen, failure and promotion
  evidence; Workstream: Proof.

Source: [requirements](../../docs/requirements.md). The technical source module
crosswalk uses root TODO meanings, not research-plan MO meanings:

- **MO01 kernel**. Design module: All; Contract / gate: DC01-DC06 / VG01-VG06;
  Files: contract_kernel.py, contract_validation.py.
- **MO02 governor**. Design module: MG01; Contract / gate: DC01 / VG01; Files:
  context_weight.py.
- **MO03 time**. Design module: MG02; Contract / gate: DC02 / VG02; Files:
  time_packet.py.
- **MO04 workers**. Design module: MG04; Contract / gate: DC04 / VG04; Files:
  vertebra_delta.py.
- **MO05 signal spine**. Design module: MG03; Contract / gate: DC03 / VG03;
  Files: signal_spine.py.
- **MO06 style**. Design module: MG05; Contract / gate: DC05 / VG05; Files:
  style_surface.py.
- **MO07 proof**. Design module: MG06; Contract / gate: DC06 / VG06; Files:
  soft_proof.py.
- **MO08 reconciliation**. Design module: MG03, MG04; Contract / gate: DC03,
  DC04 / VG03, VG04; Files: reconciliation.py.

`__init__.py`, `__main__.py`, and `demo.py` are supporting package/runtime
surfaces rather than additional independent design modules. Their source/test
inventory must still be included. The parallel source review supplies the
complete twelve-source and twelve-test map.

### Development loop and validation

1. Read onboarding, current plan, and the canonical task card; confirm the
   checkout and current evidence. Select ready work with satisfied dependencies.
2. For a new behavior or unresolved policy, update its scoped requirement and
   design before coding; record alternatives and why the selected option fits.
3. Implement one bounded slice, including meaningful refusal/failure evidence
   for the affected contract. Keep the current scalar/engine boundary explicit.
4. Run applicable checks. Attach date, source revision, exact command/result,
   relevant environment/tool version, and limitations to the evidence record.
5. Update the task's canonical status and evidence, affected design/README
   claims, and milestone exit evidence. Append history without rewriting old
   command results as if they were rerun today.
6. Run planning, citation, local-link and Markdown validation before handoff.

The planning validator should check unique task IDs; required fields; known
milestones, owners, requirements, contracts and gates; valid dependency targets;
acyclic dependencies; readiness/completion rules; evidence targets for done
items; every requirement has task coverage; every task belongs to the global
plan; every declared current document and source/test file is catalogued; and
all canonical task files are enumerated. Scope exceptions need names and
reasons, not silent broad exclusions.

Citation checks should remain document-local, detect misplaced/duplicate/
missing/unused markers and active zero placeholders, and distinguish code
examples, checkboxes, ordinary Markdown links, and pseudo-category destinations.
Local-link checks should verify files and usable heading anchors. These checks
cannot prove semantic acceptance or correctness of an attached result; reviewer
judgment and actual execution remain necessary.

### Gaps and remaining decisions

A global plan can order the work now without deciding every future engine
choice. Concrete early decision cards are required for tool management and
type gates, governor aggregation/down-weight, proof promotion/evidence, worker
and channel authority, cross-worker candidate constraints, time provenance and
checkpoint policy, numeric style units, and the first demonstrator's scope.

Concurrent publication, durable commits, conflict merging, nested/vector state,
and hook isolation should be separately justified by an accepted use case.
Their appearance in the old TODO as remaining work does not automatically make
them mandatory features of the first 3D demonstrator.

## (Y) Link-complete usage index [LI]

- Review: [DOC], [LI]
- Goals: [GL01], [GL02], [GL03]
- Dependencies: [DP01], [DP02], [DP03]
- Requirements: [RQ01], [RQ02], [RQ03]

## (Z) Context-Citations

[DOC]: PLANNING_CATALOGUE_REVIEW
  "The dated repository planning and provenance review supporting development
  realignment without changing runtime behavior."

[GL01]: PRESERVE_PROJECT_INTENT_AND_PROVENANCE
  "Retain the research, theory, style, requirement, module and historical
  catalogue while clarifying the role of each document."

[DP01]: EXISTING_DOCUMENT_CHAIN
  "The tracked research plan, live research, proposal, requirements, design,
  tasklist, source plan, README, root TODO and historical material."

[RQ01]: DO_NOT_REPLACE_HISTORY_WITH_CURRENT_STATUS
  "Historical decisions and verification remain dated evidence rather than
  being silently rewritten as current delivery claims."

[GL02]: SEPARATE_CURRENT_FACTS_FROM_OLD_GATES
  "Identify conflicting horizons, scope claims, policy gaps and stale links
  before creating a new global development plan."

[DP02]: DOCUMENT_AND_IDENTIFIER_AUDIT
  "The review uses document bodies, context registries and a bounded catalogue
  scan; pseudo-citation identifiers are local to their defining file."

[RQ02]: RECORD_DISAGREEMENTS_WITHOUT_ERASING_THEM
  "Substantive disagreements receive explicit decision tasks and historical
  context rather than being hidden by a broad rewrite."

[GL03]: MAKE_DEVELOPMENT_TRACEABLE_AND_MAINTAINABLE
  "Connect global milestones to individually scoped work with acceptance,
  dependencies, evidence, and one authoritative task status."

[DP03]: SINGLE_AUTHORITY_PER_FACT
  "Global scope belongs to the plan, technical contracts to design and
  requirements, task statuses to canonical cards, and results to evidence."

[RQ03]: EVERY_TASK_HAS_PARENT_AND_ACCEPTANCE
  "Each development task has a global milestone, requirement trace,
  dependencies, bounded outcome and evidence-backed completion criteria."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative index that invokes every active context marker."
