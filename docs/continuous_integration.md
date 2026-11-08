# Automated accepted checks [DOC]

The [workflow](../.github/workflows/accepted-checks.yml) runs the accepted
Windows prototype checks on pushes, pull requests and manual dispatch.
The [tooling decision](decisions/prototype_toolchain.md) still owns tool pins
and required gates; [ST-003](todos/tooling.md) owns acceptance and dated evidence.

> Goal: [GL01] - AUTOMATE_THE_QUALIFIED_CHECKS
> Dependency: [DP01] - LOCKED_BOOTSTRAP_AND_REPOSITORY_WORKFLOW
> Requirement: [RQ01] - PRESERVE_FAILURE_AND_ENVIRONMENT_EVIDENCE

## Job contract

The Windows reference checks job uses windows-2025 x64. It checks out the event
revision with full history, runs [ci.ps1](../scripts/ci.ps1), and retains check
artifacts. Its GitHub token has contents: read permission. Checkout credential
persistence is disabled. Both reusable actions are pinned to full commit IDs;
the runner image itself is maintained by GitHub, so its actual image version
is captured with each run [RS01], [RS02].

The job has a 20-minute timeout and cancels older runs for the same ref. It has
no path filters or restored dependency caches. Each run must start without
.tools, .venv or node_modules, then obtain the selected tools through
Bootstrap.cmd. Runner-preinstalled Python, Node or checkers cannot substitute
for the pinned local environment. Bootstrap already runs the complete verifier.

The job then exercises the real planning and Markdown CLIs against disposable
fixtures through [ci_refusal_probe.py](../scripts/ci_refusal_probe.py). A valid
planning copy must pass first. An unknown next-task pointer must fail with
the fixture's identifier, and duplicate top-level Markdown headings must fail
with MD025. Unrelated crashes and successful commands containing error text
cannot satisfy these probes. The real checkout's input hashes must stay equal.

Finally, the job checks submitted-diff whitespace. Pull requests use the event
base SHA; ordinary pushes use their preceding SHA. New branches/manual runs
without a base check the HEAD commit, including the first-parent merge diff.
This complements Verify.cmd's working-tree whitespace check, which alone sees
no changes in a clean committed checkout. Referenced history must be available;
an invalid base fails rather than silently skipping the gate.

## Evidence and failure behavior

The job records each stage's exit code, revision, runner OS/architecture,
image version, run identity and fresh-environment observations. A nonzero child
exit fails the job. It does not use continue-on-error. The final artifact step
runs after success or failure and retains the following allowlisted outputs:

| Artifact file | Meaning |
| --- | --- |
| ci/job.json | Job identity, stages, final status and any failure |
| ci/job.log | PowerShell transcript, including bootstrap/download failures |
| ci/refusal-probes.json | Fixture commands, failures and source hashes |
| verification/latest.json | Versions, tests, demo and required gate output |

Files are generated beneath .tools and uploaded as
accepted-checks-RUN_ID-RUN_ATTEMPT with a 14-day retention request. Hidden-file
inclusion is enabled because .tools is hidden by name; only the listed JSON/log
patterns are included. Environments, caches, Git credentials and fixture trees
are not artifact inputs. If checkout fails before the job starts, use the
Actions step log; there is no invented bootstrap evidence [RS03].

The workflow serves the same check contract as local Verify.cmd. It does not
change branch protection or make a merge. A manual workflow_dispatch becomes
available through GitHub's normal default-branch registration rules; pushes
can exercise a newly introduced workflow branch directly [RS01].

## Local diagnosis and scope

Use Verify.cmd in an existing development environment. The refusal probes can
also be exercised independently:

```powershell
.\.venv\Scripts\python.exe scripts/ci_refusal_probe.py
```

To reproduce the entire job locally, use a fresh Git checkout containing the
implementation, with no generated environment directories, and run:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/ci.ps1
```

The script refuses a warm environment instead of deleting it. Keep source
changes outside the checkout being tested. A local run has no GitHub artifact
upload and no hosted-runner claim; inspect .tools/ci and .tools/verification.

Windows Server runner evidence complements the Windows desktop qualification
from ST-002. It does not qualify Linux, macOS, ARM, a renderer, GPU behavior,
performance budgets or an installed application. The
[hosted qualification and P1 review](../reports/ST-003%20automated%20checks.md)
records actual execution; a workflow file alone cannot close the phase.

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]
- Upstream contracts: [RS01], [RS02], [RS03]

## (Z) Context-Citations

[DOC]: AUTOMATED_CHECKS_GUIDE
  "Repository workflow, job behavior, artifacts and local diagnosis."

[GL01]: AUTOMATE_THE_QUALIFIED_CHECKS
  "Run the selected bootstrap and verification on fresh automated checkouts."

[DP01]: LOCKED_BOOTSTRAP_AND_REPOSITORY_WORKFLOW
  "ST-001 policy, ST-002 implementation and the GitHub Actions job definition."

[RQ01]: PRESERVE_FAILURE_AND_ENVIRONMENT_EVIDENCE
  "Record actual versions, job identity and failure output without widening
  platform or application acceptance claims."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative invocation list for every local context marker."

[RS01]: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
  "GitHub workflow syntax, events, runner labels, permissions and shell exits;
  consulted 2026-11-08."

[RS02]: https://github.com/actions/checkout/tree/d23441a48e516b6c34aea4fa41551a30e30af803
  "Pinned checkout action, fetch depth and credential persistence contract."

[RS03]: https://github.com/actions/upload-artifact/tree/cf430e030ddbb5b0abf93d22962f4752f3646cd9
  "Pinned artifact action, hidden-file inclusion and retention contract."
