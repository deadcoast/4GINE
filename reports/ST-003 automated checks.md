# ST-003 automated checks and P1 exit review [DOC]

Date: 2026-11-08. Phase P1; requirements REQ03, REQ09 and REQ15.
A real GitHub-hosted Windows checkout ran the accepted bootstrap, all required
checks and deliberate planning/Markdown refusal fixtures. The successful job
and an earlier failed job both retained their diagnostic artifacts.

> Goal: [GL01] - QUALIFY_AUTOMATION_AND_REVIEW_P1_EXIT
> Dependency: [DP01] - PINNED_TOOLING_AND_HOSTED_EXECUTION
> Requirement: [RQ01] - KEEP_STATUS_TIED_TO_OBSERVED_EVIDENCE

## Source and hosted run identity

The starting checkout was 8519d3c13aa6e6e574cd241aed0a79187a704905 with the
authorized planning realignment and ST-001/ST-002 work still uncommitted.
An isolated clone carried those prerequisites and the new automation to
[codex/st-003-accepted-checks](https://github.com/deadcoast/4GINE/tree/codex/st-003-accepted-checks)
in the existing private repository. The original working checkout was preserved.
No merge or branch-protection change was performed.

The [successful run](https://github.com/deadcoast/4GINE/actions/runs/42481713173)
tested ae935751776b282b7e70a5062ca674717ca78197. Its job began at
2026-11-08T12:45:52Z. The committed workflow and executable scripts were the
same ones used for local checks. Dated report/task closure follows that run;
the source hashes in each artifact identify exactly what it tested.

| Item | Observed value |
| --- | --- |
| Workflow / job | Accepted checks / Windows reference checks |
| Runner label | windows-2025, x64 |
| Actual OS | Windows Server 2025, 10.0.26100 |
| Image identity | win25-vs2026, 20261103.298.1 |
| CPython | 3.13.18, MSC v.1944, GIL enabled |
| Python build | Oct 26 2026, 14:10:48; managed by pinned uv |
| uv / Node / npm | 0.13.7 / 24.22.2 / 11.19.1 |
| Pyright | 1.1.414 |
| Markdown CLI / core | 0.23.1 / 0.41.1 |

The job record confirms .tools, .venv and node_modules were all absent before
setup. No cache action or runner-preinstalled language tool supplied the
selected environment. Python runtime dependencies remain empty.

## Implemented job and acceptance results

The [workflow](../.github/workflows/accepted-checks.yml) covers push,
pull_request and workflow_dispatch events with read-only repository permission,
full-SHA action pins, a bounded timeout and artifact retention. It invokes
[ci.ps1](../scripts/ci.ps1), which runs the existing bootstrap and its verifier,
then the isolated negative fixtures and submitted-diff whitespace gate.
The [CI guide](../docs/continuous_integration.md) explains the event/base rules,
commands, artifact allowlist and recovery workflow.

The successful hosted run observed:

- 87 runtime tests and 31 tooling tests passed. The tooling count comprises
  19 planning-checker tests, nine verifier tests and three new refusal-probe
  tests that reject successful or unrelated commands as negative evidence.
- The JSON demo passed both refusal guards and expected codes, 14 accepted
  steps, zero refused steps, x approximately 0.672, y approximately -0.336
  and remainder approximately 0.008.
- Exact versions, uv/npm lock freshness and the installed dependency tree
  passed. Pyright reported zero errors and zero warnings.
- Planning passed for 30 then-current Markdown files, 34 cards, five phases
  and 15 requirements. All 30 scoped Markdown files linted cleanly.
- Working-tree and submitted-diff whitespace passed. Verification and the
  negative probes preserved their source hashes.
- A valid planning fixture exited 0. Changing only its next-task pointer to
  unknown ST-999999 exited 1 with that diagnostic. A separate Markdown fixture
  with two top-level headings exited 1 with MD025. The real checkout was not
  modified by either invalid fixture.

The [job record](evidence/st-003/passed/job.json),
[verification record](evidence/st-003/passed/verification.json),
[refusal record](evidence/st-003/passed/refusal-probes.json) and
[transcript](evidence/st-003/passed/job-log.json) preserve the downloaded
artifact contents. Transcript text is stored inside JSON to preserve its
output whitespace without introducing source whitespace errors.

The successful artifact is accepted-checks-42481713173-1, ID 13617767859;
its archive SHA-256 is
32621017020b9bd70ab646db4de77a0818ba898aa8dca5da7a4f7ced1856e433.
GitHub recorded expiry on 2026-11-22; the repository evidence copies above
preserve the record after hosted retention ends.

## Real failure propagation and retained diagnostics

The [first hosted run](https://github.com/deadcoast/4GINE/actions/runs/42481417652)
tested bc3ada529f2e77fac5d5ab43b25bd1f478b86a36. Bootstrap, required verification
and both negative fixtures passed. The submitted-commit whitespace check then
found an extra blank line at the end of the previously untracked ST-002 Node
checksum record. Git exited 2, the job wrapper exited 1, and GitHub marked the
job failed. The artifact upload step still succeeded.

The [failed job record](evidence/st-003/failed/job.json),
[failed-job transcript](evidence/st-003/failed/job-log.json),
[successful prerequisite gates](evidence/st-003/failed/verification.json) and
[negative fixtures](evidence/st-003/failed/refusal-probes.json) distinguish the
actual failure from preceding success. Artifact ID 13616993672 has SHA-256
b9c6b378a702f15de3b12df2eed49929472710e78d06680ad867e1958d919dec.
The correction removed only that final blank line; all checksum values remain
unchanged. The following fresh hosted run passed. This was a real whitespace
defect, not an intentionally broken runtime test.

A separate [local wrapper refusal](evidence/st-003/local/warm-environment-refusal.json)
confirmed that a warm checkout is refused before installation and still writes
job.json/job.log with a failing exit. Deliberate fixture failures are accepted
only when both a nonzero status and the intended diagnostic are observed.

## P1 aggregate exit review

The accepted P1 outcome is reproducible, traceable prototype development.
Review against [global_plan.md](../docs/global_plan.md) found:

| Exit criterion | Evidence |
| --- | --- |
| Declared versions and required/optional checks | ST-001 accepted policy |
| Fresh local setup and unchanged locked inputs | ST-002 cold/repeat evidence |
| Fresh automated checkout and version capture | This hosted Windows run |
| Runtime, demo, static and documentation gates | Downloaded verification JSON |
| Planning drift refusal | Hosted unknown-task fixture and checker tests |
| Failure output retained | Failed and successful hosted artifacts |
| Maintained planning catalogue | ST-034 and current planning validation |

P1's exit is satisfied for the declared Windows prototype environment. ST-004
remains an explicitly deferred IDE intake; Mypy and a fresh IDE export are not
required CLI gates. This closes the development-baseline phase, not the
prototype's outstanding behavioral requirements. ST-005 specifies contract
identity and schema evolution before related source changes in P2.

## Limits and delivery state

Observed execution covers Windows desktop tooling through ST-002 and the
Windows Server hosted image above. Linux, macOS, ARM, GPU/rendered behavior,
performance and installed application acceptance remain unqualified.
The runner image can change; each job captures its actual identity.

Hosted qualification exercised push events. Pull-request and manual triggers
are configured but were not separately executed. Manual dispatch follows
GitHub's default-branch workflow registration rules. Cancellation or a runner
failure can prevent artifact upload; normal check failure was exercised and
retained successfully. Main-branch adoption requires merging the reviewed
branch; this task did not change default-branch content or protection rules.

Runtime source, runtime tests, agent controls, historical drafts and the
unrelated root VERIFICATION.md have no changes from the starting commit.
The report and final task updates receive local required checks and a follow-up
branch run. Task status and the next pointer remain in their canonical files.

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: ST003_HOSTED_QUALIFICATION_RECORD
  "Dated local and hosted automation evidence, failure artifacts and P1 review."

[GL01]: QUALIFY_AUTOMATION_AND_REVIEW_P1_EXIT
  "Exercise the accepted checks in a real hosted job and review phase criteria."

[DP01]: PINNED_TOOLING_AND_HOSTED_EXECUTION
  "ST-001/ST-002 tools, ST-034 planning and the recorded GitHub Actions runs."

[RQ01]: KEEP_STATUS_TIED_TO_OBSERVED_EVIDENCE
  "Separate configured triggers, actual execution, retained failures and
  platform limits before closing the task and its owning phase."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative invocation list for every local context marker."
