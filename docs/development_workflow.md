# 4GINE development workflow [DOC]

Use this workflow with the [onboarding](../.agents/ONBOARDING.md),
[global plan](global_plan.md), [catalogue](README.md) and
[root queue](../TODO.md). The user has authorized this realignment and
continuation of the bounded prototype. Routine implementation and documentation
decisions do not require repeated permission [RQ01].

## Select a bounded task

> Goal: [GL01] - CONTINUE_WITH_GLOBAL_CONTEXT
> Dependency: [DP01] - PLAN_CARD_AND_CHECKOUT
> Requirement: [RQ01] - HONOR_AUTHORIZATION_AND_SCOPE

Read the next-task pointer and canonical card, then the owning phase,
requirements and design. Confirm the checkout, working tree and current
evidence. Use CodeGraph first if an index exists; otherwise inspect source
normally. Old machine/tool observations are not current facts.

Choose ready work with satisfied dependencies. Independent policy analysis can
proceed early; implementation still obeys phase and card gates. Mark the card
in_progress when work starts. Preserve unrelated changes and research history.

Resolve routine engineering details autonomously and record decisions. Ask the
owner only when missing product intent or a material scope tradeoff prevents a
defensible choice. Historical proposal/docspec handoff language does not revoke
authorization already given for bounded source work. A future capability
catalogue is not automatic approval of all its features.

## Specify before expanding behavior

> Goal: [GL02] - ALIGN_DESIGN_AND_IMPLEMENTATION
> Dependency: [DP02] - REQUIREMENTS_CONTRACTS_AND_FAILURES
> Requirement: [RQ02] - TRACE_CHANGES_BEFORE_SOURCE

For policy/schema changes, record alternatives, selected rule, rationale,
compatibility and refusals in the owning design section or linked decision.
Preserve superseded research as dated history. Silently choosing the governor
formula or proof-state meaning does not resolve its design record.

Every card has one phase, workstream owner, requirements, dependencies, scope,
acceptance and evidence. New application work requires actual requirements
and design extensions through ST-025; the original prototype requirements
alone do not specify a renderer. Update downstream task traces accordingly.

ST identifiers are globally unique and stable. Pseudo-citations are local to
their document; qualify historical TK/MO identifiers by file when crossing
records. Give unrelated new work a new card rather than reopening an old
completed task with a different meaning.

## Verify the exact claim and close its card

> Goal: [GL03] - CLOSE_WITH_APPROPRIATE_EVIDENCE
> Dependency: [DP03] - ACCEPTANCE_AND_REFUSAL_SPECIMENS
> Requirement: [RQ03] - KEEP_EVIDENCE_LIMITS_EXPLICIT

Implement one reviewable slice. Exercise meaningful positive and refused cases
at the changed boundary. Run the full runtime suite for core contract or
integration changes. Documentation-only changes need planning, link, citation
and Markdown checks. Run checker regression tests when its parser/rules change.

Evidence names date, source revision or working-tree delta, contract revision,
environment/tool versions, command/scenario, expected/actual result, artifact
and limits. A plan is not an execution log; a unit test is not rendered,
installed or human acceptance. Direct tests support their exact claim while
the wider engine remains unfinished.

Set done only after acceptance and evidence are met. Link the result in the
card. If a required check is unavailable, name the affected gap or an explicit
replacement decision; never report it as passed. Do not copy mutable task
status into the README, root queue or global plan.

## Maintain the complete planning path

> Goal: [GL04] - PREVENT_TRACEABILITY_DRIFT
> Dependency: [DP04] - SINGLE_AUTHORITY_AND_CHECKS
> Requirement: [RQ04] - UPDATE_AFFECTED_RECORDS_TOGETHER

Update the owning card and affected requirement/design claims. Update the README
when behavior or entry commands change. Link new workstreams and artifacts from
the catalogue. Append dated evidence without rewriting old command results as
today's verification.

When required cards finish, review the phase's aggregate exit evidence before
closing it. Deferred optional work stays visible with its reason. Replace the
root Next task pointer when its old target closes, choosing a ready or
in_progress card. Run consistency checks before handoff.

### Canonical card example

```md
### ST-035: A concrete bounded outcome

- Status: planned
- Phase: P2
- Requirements: REQ03, REQ09
- Depends on: ST-005
- Owner: contracts
- Scope: Name the exact behavior and exclusions.
- Acceptance: State observable success and refusal conditions.
- Evidence: pending
```

This fenced example is not active task data. Select the next unused ID.
Required field values use plain IDs and comma-separated dependencies or none;
indented continuations are allowed. Cards live under docs/todos.

| Status | Meaning | Condition |
| --- | --- | --- |
| planned | Accepted work not ready | Resolve scope/prerequisites |
| ready | Acceptance concrete; dependencies done | Selectable |
| in_progress | Active work | Dependencies satisfied |
| blocked | Named blocker prevents progress | State how to unblock |
| done | Acceptance and evidence complete | Link reviewed results |
| deferred | Outside required delivery | State rationale and re-entry |

## Commands and tooling limits

> Goal: [GL05] - MAKE_CHECKS_REPEATABLE
> Dependency: [DP05] - INTERPRETER_AND_SELECTED_TOOLS
> Requirement: [RQ05] - DISTINGUISH_LOCAL_AND_CLEAN_SETUP

The [accepted tooling decision](decisions/prototype_toolchain.md) owns target
versions, dependency locks and required checks. Pyright is the required type
gate; Mypy is optional. The [setup guide](getting_started.md) describes the
repository-local bootstrap, verification entry point and failure recovery.
The [automated-checks guide](continuous_integration.md) describes the fresh
Windows CI job, negative fixtures and retained failure artifacts.

From the repository root:

```powershell
.\Bootstrap.cmd
.\Verify.cmd
.\.venv\Scripts\python.exe -m spinaltap --json
```

Bootstrap downloads and installs the pinned environment, then verifies it.
Verify.cmd uses that environment offline without repairing it. It records
versions, source hashes, commands, exit codes and complete output under
.tools/verification/latest.json. Runtime and tooling test counts remain
separate. The verifier rejects zero discovery and validates the actual demo
JSON. Pyright covers spinaltap, tests and scripts with warnings fatal.

The 2026-11-07 audit used Python 3.13.12 and cached Pyright 1.1.414 and
markdownlint-cli2 0.23.1 / markdownlint 0.41.1. Mypy was unavailable. The
[dated report][S01] preserves that earlier evidence; current qualification
belongs to the linked ST-002 card. The planning checker resolves the repository
from its script location; see --help for explicit fixture roots.

The checker covers fields, phases/requirements, dependency relationships,
requirement coverage, next-task selection, local links and document-local
citations. It cannot certify external URL availability, factual truth, evidence
quality, semantic acceptance, phase completion or rendered output. Fixture
tests cover representative failures, not full CommonMark conformance.

Current repair scope is root README/TODO plus Markdown under docs, reports and
research_notes. Historical CHANGELOG remains ordinary Markdown and is exempt
from pseudo-citation registries, but receives lint/link checks. Read-only
.agents controls and tracked historical .user_notes drafts are preserved and
excluded from format repair. Known control-link issues are recorded in the
[catalogue](README.md); no claim is made that those old paths pass.

## Handoff

> Goal: [GL04] - PREVENT_TRACEABILITY_DRIFT
> Dependency: [DP04] - SINGLE_AUTHORITY_AND_CHECKS
> Requirement: [RQ04] - UPDATE_AFFECTED_RECORDS_TOGETHER

Name the changed behavior/documents, owning card, exact checks passed or
unavailable, remaining acceptance gaps and next runnable task. Link artifacts
so a fresh agent can continue without chat memory. Use the working
[template](../.agents/template/TEMPLATE_ONBOARDING.md) rather than stale paths
inside older control documents.

Extend the workflow only when it improves traceability or verification.
Preserve historical snapshots and avoid parallel mutable status ledgers.

## (Y) Link-complete usage index [LI]

- Context: [DOC], [LI], [S01]
- Goals: [GL01], [GL02], [GL03], [GL04], [GL05]
- Dependencies: [DP01], [DP02], [DP03], [DP04], [DP05]
- Requirements: [RQ01], [RQ02], [RQ03], [RQ04], [RQ05]

## (Z) Context-Citations

[DOC]: DEVELOPMENT_WORKFLOW
  "Repeatable work selection, specification, implementation and evidence
  updates."

[GL01]: CONTINUE_WITH_GLOBAL_CONTEXT
  "Select authorized bounded work using the current phase, card and checkout."

[GL02]: ALIGN_DESIGN_AND_IMPLEMENTATION
  "Resolve policy and contract meaning before expanding behavior."

[GL03]: CLOSE_WITH_APPROPRIATE_EVIDENCE
  "Attach acceptance and refusal evidence for the exact changed claim."

[GL04]: PREVENT_TRACEABILITY_DRIFT
  "Maintain the affected plan, task, contract, claim and evidence path."

[GL05]: MAKE_CHECKS_REPEATABLE
  "Expose check targets and distinguish local success from clean setup."

[DP01]: PLAN_CARD_AND_CHECKOUT
  "Current delivery intent, owning card and actual repository state."

[DP02]: REQUIREMENTS_CONTRACTS_AND_FAILURES
  "Technical meaning, compatibility and observable refusal conditions."

[DP03]: ACCEPTANCE_AND_REFUSAL_SPECIMENS
  "Appropriate successful and failing scenarios for the claimed behavior."

[DP04]: SINGLE_AUTHORITY_AND_CHECKS
  "One task status owner and mechanical relationship validation."

[DP05]: INTERPRETER_AND_SELECTED_TOOLS
  "Pinned repository-local tools and the recorded qualification environment."

[RQ01]: HONOR_AUTHORIZATION_AND_SCOPE
  "Do not add permission gates to routine authorized development."

[RQ02]: TRACE_CHANGES_BEFORE_SOURCE
  "Every expansion identifies its phase and accepted technical requirements."

[RQ03]: KEEP_EVIDENCE_LIMITS_EXPLICIT
  "Planning, execution, rendering, measurement and user acceptance differ."

[RQ04]: UPDATE_AFFECTED_RECORDS_TOGETHER
  "Keep each changed task, technical contract and current claim consistent."

[RQ05]: DISTINGUISH_LOCAL_AND_CLEAN_SETUP
  "Personal cached tools passing does not prove reproducible onboarding."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative invocation list for each local context marker."

[S01]: ../reports/4GINE%20development%20realignment.md
  "Dated baseline and final realignment verification record."
