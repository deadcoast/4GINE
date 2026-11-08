# Realign 4GINE around evidence and delivery [DOC]

4GINE has a useful executable prototype and a substantial research catalogue,
but it lacked one current delivery plan connecting them. This realignment
establishes **five delivery phases and 34 canonical tasks across nine
workstreams**, with explicit scope, dependencies, acceptance and evidence.
The original theory, styles, sources, contracts and completed planning records
remain reachable. The runtime baseline is unchanged: it is a synchronous
scalar-state contract/reconciliation harness, not an interactive 3D engine.
Three reproduced behaviors identify the most urgent semantic gaps: text-only
proof promotion, string-only style acceptance and undocumented governor
formula drift. The new workflow makes those gaps actionable without claiming
that documentation itself has completed the application
([global plan](../docs/global_plan.md), [catalogue](../docs/README.md)) [GL01].

Review date: 2026-11-07. Runtime baseline: 9afd1cf. This report is dated
evidence;
the global plan and individual cards own ongoing scope and task status.

## The catalogue survives with explicit authority

> Goal: [GL01] - RESTORE_GLOBAL_DELIVERY_TRACEABILITY
> Dependency: [DP01] - COMPLETE_REPOSITORY_AND_SOURCE_REVIEWS
> Requirement: [RQ01] - PRESERVE_CONTEXT_WITHOUT_DUPLICATE_STATUS

The previous documents describe different time horizons. The research plan
preserves eight theory candidates, seven lanes and fifteen style categories;
the original live pass records eleven sources. The proposal and fifteen
requirements bound the first implementation as a prototype. Eighteen checked
docspec tasks and eight initial source slices demonstrate completed planning
and bounded implementation work, respectively. Neither record establishes a
finished game engine. The new catalogue keeps all these records visible and
labels their authority and historical scope
([planning review][S01], [original requirements](../docs/requirements.md)).

The naming problem was significant because identical markers had different
meanings across files. Research-plan MO01 means spinal column; root-TODO MO01
means the contract kernel. The TK families in docs/tasklist.md and root
TODO.md likewise refer to
different tasks.
The realignment retains those local meanings and uses globally unique ST
identifiers for current cards. Every card names a global phase and requirement
set; the root queue points to one ready task rather than copying status.
The preserved historical source ledger includes a successor crosswalk for
TK01-TK12, while the old docspec checklist retains its original completion
([catalogue](../docs/README.md), [root TODO](../TODO.md)).

P1 establishes reproducible development. P2 aligns policy, evidence and scalar
state authority. P3 specifies one useful 3D scenario and its data/style/backend
needs. P4 requires actual interactive, rendered and measured evidence. P5
qualifies the distributed application and controls later capability discovery.
Each phase has admission and exit conditions. Deferred concurrency, durability,
conflict merging, audio, editor, networking and broader simulation remain
use-case decisions, not hidden commitments imposed on the first demonstrator.
No target platform, production language, graphics backend or calendar deadline
was invented to make the roadmap appear complete
([phase gates](../docs/global_plan.md)).

## Passing specimens do not close the semantic gaps

> Goal: [GL02] - MATCH_READINESS_TO_OBSERVED_BEHAVIOR
> Dependency: [DP02] - SOURCE_PROBES_AND_RUNTIME_BASELINE
> Requirement: [RQ02] - DISTINGUISH_STRUCTURAL_AND_EXECUTED_EVIDENCE

The source review covers all **12 package files and 12 runtime test files**.
The strongest implemented boundary is synchronous scalar candidate validation:
strict mapping ingress, finite fixed-step inputs, bounded local proposals,
ordered hooks, conflict preflight and complete-candidate return. Every worker
sees the initial snapshot, and late refusal exposes neither partial state nor
partial bundles. The code does not own durable world state or roll back trusted
callback side effects. Caller-declared owner/channel labels do not establish
persistent authorization
([source review][S02], [reconciler](../spinaltap/reconciliation.py)).

The proof probe supplied an unexecuted plan, an unobserved failure path and a
docs-only tier, yet received implementation_ready without refusal. That matches
the current code and tests; it is a readiness-semantic gap against the wider
proof ambition, not a newly failing test. ST-023 defines an unambiguous
lifecycle and ST-024 implements evidence checks. The policy must distinguish
permission to implement from verified execution, identify the claim/contract
revision and reject missing, failed, stale or mismatched evidence. This follows
the narrow principle that artifacts must be run against their stated claims;
it does not assert a conference badge or external certification
([proof review][S02],
[ICFP artifact
guidance](https://icfp26.sigplan.org/track/icfp-2026-artifact-evaluation))
[RS01].

The style probe set all ten fields to vague and passed. DC05 currently checks
nonblank strings, so it does not enforce numeric units, ranges or profile
budgets. ST-020/ST-021 specify and implement one measurable profile; ST-022
then checks its behavior in rendered output. The historical rendering sources
supply useful axes such as geometry, textures, fog, alpha and depth, but no
universal retro aesthetic budget. Choosing one profile requires the actual
scenario and hardware, with deliberate visual artifacts distinguished from
hardware-emulation accuracy
([style review][S02],
[Direct3D
architecture](https://learn.microsoft.com/en-us/windows/win32/direct3d9/direct3d-architecture))
[RS02].

The governor's historical FR05 formula takes the minimum of four factors;
current code takes their clamped mean and blocks originality below 0.20.
Factors (1,0,1,1) therefore produce 0 in the formulation and 0.75 in the
runtime.
No superseding decision or empirical calibration was located. DOWN_WEIGHT is
declared but unreachable. ST-007 resolves the rule and its limits before
ST-008 changes behavior; ST-009 supplies inspectable provenance records.
This is an unresolved policy divergence, not evidence that one convenient
formula is scientifically correct
([historical formulation](../docs/live_research.md),
[governor](../spinaltap/context_weight.py), [technical review][S03]).

## Research constrains the next work without choosing the engine

> Goal: [GL03] - USE_RESEARCH_WITH_EXPLICIT_LIMITS
> Dependency: [DP03] - VERIFIED_PRIMARY_SOURCES_AND_PROJECT_HYPOTHESES
> Requirement: [RQ03] - DO_NOT_TURN_PRECEDENT_INTO_PROOF

The technical pass records sixteen primary-source entries and separately
rechecks the eleven older source families. It preserves original access dates
and marks rolling-document drift: Box2D's simulation page now labels 3.2.0,
while its samples page labels 3.1.0. The ACM policy and Khronos fixed-function
wiki could not be refreshed because their pages returned 403. Those gaps remain
visible; no stronger claims are drawn from the unavailable pages. The earlier
research remains provenance rather than being silently rewritten as current
verification ([technical verification ledger][S03]).

Fixed timesteps are a useful prerequisite, but they do not prove application
determinism or bounded wall-clock latency. Fiedler discusses accumulation and
overload tradeoffs; Box2D additionally names ordering, compiler/math controls
and recurring determinism tests. ST-010 therefore decides backlog,
refused-step, pause and replay semantics before ST-011/ST-012 implement and
measure them. The current choice to consume refused-step time remains explicit
until deliberately superseded
([Fix Your Timestep](https://gafferongames.com/post/fix_your_timestep/),
[Box2D simulation](https://box2d.org/documentation/md_simulation.html))
[RS03], [RS04].

Python's documentation also supports careful boundary wording. Dataclass
annotations generally do not validate fields, frozen records do not guarantee
deep immutability, and a mapping proxy is a read-only view rather than an
automatic snapshot. The prototype's explicit parser and actual copies are the
relevant evidence. Future schema work must specify nested values, versioning
and numeric semantics rather than assuming those properties follow from type
names
([dataclasses](https://docs.python.org/3.13/library/dataclasses.html),
[MappingProxyType](https://docs.python.org/3.13/library/types.html#types.MappingProxyType))
[RS05], [RS06].

These sources support bounded engineering decisions. They do not validate the
biological decomposition, measure originality, choose the final language, or
establish 4GINE's performance. ST-025 must publish the actual application
requirements and design extensions before new application source begins.
That gives later rendering, assets, input and lifecycle work a real acceptance
target while keeping the current prototype independently useful
([application tasks](../docs/todos/application.md)).

## The evidence baseline is explicit and reproducibility remains work

> Goal: [GL04] - REPORT_WHAT_WAS_ACTUALLY_CHECKED
> Dependency: [DP04] - EXECUTED_COMMANDS_AND_SCOPE_DECLARATIONS
> Requirement: [RQ04] - NO_UNAVAILABLE_OR_FUTURE_CHECK_AS_PASS

The coordinator executed the following baseline checks on 2026-11-07 against
runtime revision 9afd1cf. These are fresh local results, separate from older
root-TODO evidence and the checked-in 37-diagnostic IDE export.

| Check | Observed result | Limit |
| --- | --- | --- |
| Python | 3.13.12 via py -3.13 | Default python was 3.14 |
| Runtime suite | 87 passed in 0.127 seconds | Scalar/contract specimens |
| JSON demo | 14 accepted; 0 refused | Scripted elapsed inputs |
| Refusal guards | Both passed | Oversized delta and overlapping writes |
| Pyright 1.1.414 | 0 errors, 0 warnings | Cached local static checker |
| Mypy | Unavailable for Python 3.13 | Not run |
| Initial Markdown lint | 44 issues in README/CHANGELOG | Eight others clean |
| Initial citation audit | 736 defs and references | Eight original docs |

The default demo ended at x=0.672, y=-0.336, with about 0.008 seconds
remaining. The initial citation count means 736 definitions and 736 unique
body references; it belongs to the frozen pre-realignment snapshot.

Executed runtime commands were py -3.13 -m unittest discover -s tests and
py -3.13 -m spinaltap --json. The static command invoked the cached Pyright
index.js with spinaltap and tests targets. Node v25.8.1 hosted the cached
CLIs. Markdown validation used cached
markdownlint-cli2 0.23.1 with markdownlint 0.41.1. Those local passes do not
prove fresh-checkout reproducibility. ST-001 selects supported tooling and
ST-002 supplies the repeatable bootstrap; ST-003 automates the accepted checks.

Final integration checks passed on 2026-11-07 after the documentation and
planning-checker changes. This evidence closes ST-034 within its documentation
and workflow scope. The other P1 tooling/bootstrap tasks remain future work.

| Realignment check | Result |
| --- | --- |
| Planning, links and citations | PASS: 26 docs, 34 cards, 5 phases, 15 REQs |
| Checker regression tests | PASS: 19 tests |
| All scoped Markdown | PASS: 26 files, 0 issues |
| Static checks including checker/tests | PASS: 0 errors, 0 warnings |
| Diff whitespace | PASS: git diff --check |
| Runtime, tests, history and controls | Unchanged |

The final static check covered spinaltap, runtime tests, the planning checker
and its separate fixture tests. The preservation check compared spinaltap,
tests, .user_notes and .agents against the baseline and found no changes.
The checker test command was py -3.13 -m unittest discover -s scripts/tests;
planning validation used py -3.13 scripts/check_planning.py. The final Markdown
targets were README.md, TODO.md, docs/**/*.md, reports/**/*.md and
research_notes/**/*.md, with no rule suppression or configuration changes.

The repair scope includes root README/TODO and Markdown under docs, reports
and research_notes. Historical CHANGELOG remains ordinary Markdown. Read-only
.agents controls and the tracked historical .user_notes drafts are preserved
and excluded from format repair. The catalogue gives working onboarding and
template links while recording stale internal control links. The inventory JSON
is a frozen initial audit, not a live planning manifest.

No rendered/GPU session, installed application, production performance target,
external originality audit or human acceptance was performed. Those evidence
gates remain explicit future work, rather than implied by the passing baseline.

## The next slice has a concrete parent and completion test

> Goal: [GL01] - RESTORE_GLOBAL_DELIVERY_TRACEABILITY
> Dependency: [DP01] - COMPLETE_REPOSITORY_AND_SOURCE_REVIEWS
> Requirement: [RQ01] - PRESERVE_CONTEXT_WITHOUT_DUPLICATE_STATUS

The next development task is ST-001 in the
[tooling TODO](../docs/todos/tooling.md). It decides supported Python,
dependency management and required versus optional checks, with a
clean-environment verification plan. The independent governor, timing and
proof-policy decisions can be prepared while tooling is established. Runtime
changes then follow their dependency cards and evidence gates.

The lasting change is the relationship among records: global outcomes own
scope, cards own current status, technical documents own semantics, and dated
artifacts own evidence. The consistency checker catches broken relationships;
reviewers still decide whether the evidence proves the intended behavior.
That permits continued development without discarding the research catalogue
or mistaking its volume for completed application capability
([development workflow](../docs/development_workflow.md)).

## (Y) Link-complete usage index [LI]

- Context: [DOC], [LI], [S01], [S02], [S03]
- Goals: [GL01], [GL02], [GL03], [GL04]
- Dependencies: [DP01], [DP02], [DP03], [DP04]
- Requirements: [RQ01], [RQ02], [RQ03], [RQ04]
- Primary sources: [RS01], [RS02], [RS03], [RS04], [RS05], [RS06]

## (Z) Context-Citations

[DOC]: DEVELOPMENT_REALIGNMENT_REPORT
  "Dated synthesis of source, planning and primary-source research for 4GINE."

[GL01]: RESTORE_GLOBAL_DELIVERY_TRACEABILITY
  "Connect preserved research to explicit delivery phases and canonical tasks."

[GL02]: MATCH_READINESS_TO_OBSERVED_BEHAVIOR
  "Separate structural prototype checks from stronger semantic acceptance."

[GL03]: USE_RESEARCH_WITH_EXPLICIT_LIMITS
  "Use primary evidence to constrain decisions without treating it as engine
  proof."

[GL04]: REPORT_WHAT_WAS_ACTUALLY_CHECKED
  "Record exact observed baseline and integration checks with material limits."

[DP01]: COMPLETE_REPOSITORY_AND_SOURCE_REVIEWS
  "The planning catalogue, source/test audit and current delivery artifacts."

[DP02]: SOURCE_PROBES_AND_RUNTIME_BASELINE
  "Reviewed code, three reproduced semantic probes and fresh local checks."

[DP03]: VERIFIED_PRIMARY_SOURCES_AND_PROJECT_HYPOTHESES
  "Primary technical records with access results and declared influence bounds."

[DP04]: EXECUTED_COMMANDS_AND_SCOPE_DECLARATIONS
  "Dated command results and explicit included/excluded validation surfaces."

[RQ01]: PRESERVE_CONTEXT_WITHOUT_DUPLICATE_STATUS
  "Retain historical meaning while giving current scope and tasks one
  authority."

[RQ02]: DISTINGUISH_STRUCTURAL_AND_EXECUTED_EVIDENCE
  "Text completeness and runtime execution establish different claims."

[RQ03]: DO_NOT_TURN_PRECEDENT_INTO_PROOF
  "External engine or language examples cannot certify SPINALTAP."

[RQ04]: NO_UNAVAILABLE_OR_FUTURE_CHECK_AS_PASS
  "Unrun checks and later acceptance remain identified gaps."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative invocation list for every local report marker."

[S01]: ../research_notes/4GINE%20development%20realignment/planning_review.md
  "Preservation catalogue, authority drift and migration reasoning."

[S02]: ../research_notes/4GINE%20development%20realignment/source_review.md
  "Complete twelve-module source/test review and reproduced semantic probes."

[S03]: ../research_notes/4GINE%20development%20realignment/technical_research.md
  "Primary-source verification, original-source refresh and inference limits."

[RS01]: RESEARCH_SOURCE
  "TITLE: ICFP 2026 Artifact Evaluation. SOURCE: conference committee.
  LINK: https://icfp26.sigplan.org/track/icfp-2026-artifact-evaluation.
  ACCESSED: 2026-11-07. USED_FOR: executing artifacts against stated claims.
  CONTEXT_WEIGHT: MEDIUM. LIMIT: no badge or certification claim for 4GINE."

[RS02]: RESEARCH_SOURCE
  "TITLE: Direct3D Architecture. SOURCE: Microsoft Learn, Direct3D 9.
  LINK:
  https://learn.microsoft.com/en-us/windows/win32/direct3d9/direct3d-architecture.
  ACCESSED: 2026-11-07. USED_FOR: rendering-constraint vocabulary.
  CONTEXT_WEIGHT: MEDIUM. LIMIT: no universal aesthetic or hardware budget."

[RS03]: RESEARCH_SOURCE
  "TITLE: Fix Your Timestep! AUTHOR: Glenn Fiedler. DATE: 2004-06-10.
  LINK: https://gafferongames.com/post/fix_your_timestep/.
  ACCESSED: 2026-11-07. USED_FOR: accumulation and overload tradeoffs.
  CONTEXT_WEIGHT: MEDIUM. LIMIT: not a correctness or performance proof."

[RS04]: RESEARCH_SOURCE
  "TITLE: Simulation. SOURCE: Box2D official documentation, header 3.2.0.
  LINK: https://box2d.org/documentation/md_simulation.html.
  ACCESSED: 2026-11-07. USED_FOR: scoped determinism and order/math controls.
  CONTEXT_WEIGHT: MEDIUM. LIMIT: 2D precedent, not 4GINE certification."

[RS05]: RESEARCH_SOURCE
  "TITLE: dataclasses. SOURCE: Python 3.13 documentation.
  LINK: https://docs.python.org/3.13/library/dataclasses.html.
  ACCESSED: 2026-11-07. USED_FOR: annotations and frozen-record semantics.
  CONTEXT_WEIGHT: HIGH for Python behavior, LOW for engine architecture."

[RS06]: RESEARCH_SOURCE
  "TITLE: types.MappingProxyType. SOURCE: Python 3.13 documentation.
  LINK: https://docs.python.org/3.13/library/types.html#types.MappingProxyType.
  ACCESSED: 2026-11-07. USED_FOR: read-only view versus snapshot distinction.
  CONTEXT_WEIGHT: HIGH for Python behavior, LOW for engine architecture."
