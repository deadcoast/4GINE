# Tooling and development workflow [DOC]

The standard-library prototype needs a declared, repeatable development
environment. This work does not choose the production engine stack.

> Goal: [GL01] - DELIVER_BOUNDED_TRACEABLE_SLICES
> Dependency: [DP01] - GLOBAL_PLAN_AND_TECHNICAL_CONTRACTS
> Requirement: [RQ01] - ACCEPTANCE_AND_EVIDENCE_BEFORE_COMPLETION

Follow the [global plan](../global_plan.md) and
[development workflow](../development_workflow.md). Requirements below refer
only to [requirements.md](../requirements.md); DC/VG meanings come from
[design.md](../design.md). ST identifiers are global task keys, while bracketed
context markers are local to this document.

## Scope and source map

- [Current package](../../spinaltap/__init__.py)
- [Runtime specimens](../../tests)
- [Planning checker](../../scripts/check_planning.py)
- [Checker regression tests](../../scripts/tests/test_check_planning.py)

## Individual TODOs

### ST-001: Choose the prototype toolchain and required checks

- Status: done
- Phase: P1
- Requirements: REQ02, REQ03, REQ09
- Depends on: none
- Owner: tooling
- Legacy: TODO.md::TK01, TODO.md::TK02
- Scope: Decide supported Python, dependency management and required type/lint
  tools. Keep runtime dependencies justified independently from developer
  tools.
- Acceptance: Record one setup decision with versions, reproducibility
  strategy and required versus optional checks. Explain whether Mypy is
  required, replaced or deferred. Include a clean-environment verification
  plan; do not claim that a manifest alone proves reproducibility.
- Evidence: 2026-11-08 [accepted decision](../decisions/prototype_toolchain.md)
  specifies exact target versions, lock ownership, required checks, optional
  Mypy and fresh-environment success/failure cases. Planning and Markdown
  checks pass for 27 scoped documents. Local baseline: 87 runtime tests,
  19 checker tests, JSON demo and Pyright pass. Selected-version installation
  and clean-environment qualification are explicitly ST-002 work.

### ST-002: Provide a repeatable bootstrap and verification entry point

- Status: done
- Phase: P1
- Requirements: REQ02, REQ03, REQ09
- Depends on: ST-001
- Owner: tooling
- Legacy: TODO.md::TK01, TODO.md::TK02
- Scope: Implement the selected manifest/environment and one documented
  verification command without relying on personal npm-cache paths. Follow
  the [accepted decision](../decisions/prototype_toolchain.md), including exact
  pins, local tools, lock freshness and its clean-environment failure cases.
- Acceptance: From a fresh repository-local environment, run the demo, runtime
  suite, chosen static checks, Markdown lint and planning checker. Missing
  tools fail with actionable messages. Record commands, versions, source
  revision and results; preserve the standard-library runtime unless the
  decision explicitly changes it.
- Evidence: 2026-11-08 [qualification report](../../reports/ST-002%20bootstrap%20qualification.md)
  and raw command evidence. Pinned tools installed; cold and repeated setup in
  a path with spaces pass 87 runtime and 28 tooling tests, demo, Pyright,
  planning, Markdown and whitespace gates. Eight refusal probes pass, locks
  and project inputs remain unchanged, and Windows Python registrations match
  before/after. GIL-disabled and outage probes are explicitly simulated.

### ST-003: Automate the accepted repository checks

- Status: done
- Phase: P1
- Requirements: REQ03, REQ09, REQ15
- Depends on: ST-002
- Owner: tooling
- Legacy: New reproducibility work
- Scope: Run the selected checks in a repository-owned automated job and
  retain relevant failure output.
- Acceptance: A fresh automated checkout reproduces required checks, fails on
  a deliberately invalid fixture in a temporary test, and records tool
  versions. Include planning and documentation gates. Document environment
  limits rather than claiming every operating system or GPU has been
  qualified.
- Evidence: 2026-11-08 [hosted qualification and P1 review](../../reports/ST-003%20automated%20checks.md).
  Run 42481713173 on Windows Server 2025 passed the fresh bootstrap, 87 runtime
  tests, 31 tooling tests, demo, static/planning/Markdown gates and submitted
  diff whitespace. Invalid planning/Markdown fixtures exited 1 as expected.
  Run 42481417652 proves a real check failure fails the job and retains logs.
  Source/tool identities and both artifacts are preserved; PR/manual triggers
  are configured but not separately exercised. The qualification branch was
  unmerged at that review. On 2026-11-09 it was fast-forwarded into main at
  d7c789b and main run 42592497332 passed; the
  [merge record](../../reports/ST-005%20contract%20identity%20review.md) preserves
  the adoption and local checkout alignment evidence.

### ST-004: Refresh or retire the historical IDE diagnostic intake

- Status: deferred
- Phase: P1
- Requirements: REQ03
- Depends on: ST-002
- Owner: tooling
- Legacy: TODO.md::TK03
- Scope: The checked-in JSON is an old 37-diagnostic export. This optional IDE
  follow-up does not block independent command checks or P2 admission.
- Acceptance: Obtain a dated export from the selected IDE configuration and
  compare the original 8 Mypy and 29 Pylance diagnostics, or record a
  deliberate retirement decision and replacement checks. Do not overwrite the
  original evidence as if it were a fresh pass. Deferral ends when that IDE is
  used for acceptance.
- Evidence: pending

### ST-034: Establish the global plan and task consistency workflow

- Status: done
- Phase: P1
- Requirements: REQ01, REQ02, REQ03, REQ09, REQ15
- Depends on: none
- Owner: tooling
- Legacy: Continues TODO.md::TK12 as a repository workflow
- Scope: Deliver this realignment: preserve the catalogue, establish one
  global plan and canonical individual cards, and add repeatable consistency
  validation.
- Acceptance: All 15 requirements have task coverage; cards have valid phases,
  dependencies and evidence rules; root queue selects a ready card. Original
  catalogue and historical ledgers remain reachable. Current project Markdown,
  local links and citation checks pass with named exclusions, and checker
  regression tests reject representative drift. Record exact verification
  scope before closing.
- Evidence: 2026-11-07 [realignment report](../../reports/4GINE%20development%20realignment.md).
  Planning/link/citation check passed for 26 Markdown files, 34 cards,
  5 phases and 15 requirements. All 26 Markdown files lint clean; 19 checker
  regression tests and static checks pass. Diff whitespace passes, and runtime,
  runtime tests, historical drafts and agent controls are unchanged.

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: CANONICAL_WORKSTREAM_TODO
  "Tooling and development workflow; authoritative individual task status and acceptance live here."

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
