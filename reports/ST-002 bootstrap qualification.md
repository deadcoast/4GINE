# ST-002 bootstrap qualification [DOC]

Date: 2026-11-08. Phase P1; requirements REQ02, REQ03 and REQ09.
The selected Windows x64 environment was installed locally and qualified from
empty caches in a fresh checkout. The [tooling card](../docs/todos/tooling.md)
owns task status; the [decision](../docs/decisions/prototype_toolchain.md)
owns policy and the [setup guide](../docs/getting_started.md) owns instructions.

> Goal: [GL01] - QUALIFY_REPRODUCIBLE_PROTOTYPE_SETUP
> Dependency: [DP01] - IMPLEMENTED_BOOTSTRAP_AND_PINNED_INPUTS
> Requirement: [RQ01] - RECORD_EXECUTION_AND_ITS_LIMITS

## Source and environment identity

Base commit: 8519d3c13aa6e6e574cd241aed0a79187a704905. Qualification cloned
that commit and overlaid the current uncommitted implementation and planning
inputs. It did not claim that those changes had already been committed.
[Raw evidence](evidence/st-002/qualification.json) records every overlaid path
and SHA-256, working-tree status, commands, exit codes, complete output and
the cold/repeat verification reports. No runtime contract revision changed.

The final run began at 2026-11-08T10:10:50Z. Its checkout was beneath
.qualification/ST-002 cold checkout 3429b3c96d/path with spaces. The harness
confirmed .tools, .venv and node_modules were absent before setup; uv, npm and
download caches were then created inside that fresh checkout. Global checker
executables and personal package caches did not supply the required tools.

| Component | Observed identity |
| --- | --- |
| OS | Windows 11, 10.0.26300, x64 |
| Python | CPython 3.13.18, GIL enabled, MSC v.1944 64 bit |
| Distribution | python-build-standalone, BUILD 20261026 |
| Python build string | main, Oct 26 2026, 14:10:48 |
| uv | 0.13.7 |
| Node / npm | 24.22.2 / 11.19.1 |
| Pyright | 1.1.414 |
| markdownlint-cli2 / core | 0.23.1 / 0.41.1 |

The pinned uv download catalogue identifies managed Python as
cpython-3.13.18+20261026-x86_64-pc-windows-msvc-install_only_stripped.tar.gz.
uv owns that managed distribution; it is not a python.org Windows installer.
The installed BUILD file and sys.version were inspected. Official uv and Node
archives passed the hashes in
[toolchain-artifacts.json](../scripts/toolchain-artifacts.json). Preserve the
retrieved [uv checksum](evidence/st-002/uv-SHA256.txt) and
[Node checksums](evidence/st-002/node-SHASUMS256.txt) with this record.

## Implemented boundary

[Bootstrap.cmd](../Bootstrap.cmd) calls the repository PowerShell script to
install pinned local tools, managed Python, the locked uv environment and
locked npm development dependencies, then invoke
[Verify.cmd's verifier](../scripts/verify.py). Python remains a non-packaged
standard-library prototype with no third-party runtime dependencies.

Bootstrap uses uv sync --locked and npm ci --ignore-scripts. Verification
checks uv lock freshness, npm root-manifest parity and npm's offline dry-run,
then validates the installed dependency tree. Tool versions must match;
no global checker fallback or implicit lock repair is allowed. Pyright covers
spinaltap, tests and scripts with warnings fatal. All child failures propagate.
Source hashes before and after verification must match.

PowerShell saves/restores its process environment. Tool caches, Python,
temporary files and development packages stay under the checkout. Python
installation uses --no-bin and --no-registry. The final qualification captured
the per-user Astral Python registry before and after; they match exactly.

## Commands and observed results

From the main checkout:

```powershell
.\Bootstrap.cmd
.\Verify.cmd
.\.venv\Scripts\python.exe scripts/qualify_bootstrap.py `
  --unsupported-python C:\Python314\python.exe
```

The last path identifies an existing Python 3.14.3 used only for a refusal
probe. Contributors need not install it to run the prototype. The harness
invoked bootstrap.ps1 in new PowerShell processes inside the fresh checkout;
the local Bootstrap.cmd and Verify.cmd launchers also passed.

| Scenario | Expected and observed result |
| --- | --- |
| Cold clone/setup | Exit 0; pinned downloads, install and all gates passed |
| Repeat bootstrap | Exit 0; all six version/manifest/lock hashes unchanged |
| Stale uv lock | Locked sync exited 1 with lockfile failure |
| Stale npm lock | Verifier exited 1 naming package-lock.json manifest drift |
| Missing local Pyright manifest | Exit 1 with bootstrap recovery instruction |
| Wrong checker version | Exit 1; rejected 0.0.0 |
| Child prints PASS then exits 23 | Verifier exits 1; records child exit 23 |
| Actual Python 3.14.3 | Exit 1; expected 3.13.18 |
| Simulated GIL-disabled build flag | Exit 1; requires GIL-enabled CPython |
| Simulated downloader outage | Exit 1; reports simulated network outage |
| Restored fixtures | Full verification returned exit 0 |

The JSON contains 12 successful case evaluations: four successful operations
including clone, and eight expected nonzero refusals. Every fixture mutation
was restored before the final verification. Cold and repeat verification each
passed 87 runtime tests and 28 tooling tests, Pyright with zero diagnostics,
planning and Markdown checks for the then-current 28 documents, and whitespace.
The additional nine tooling tests cover verifier behavior; the existing
19 planning-checker specimens remain separate from the 87 runtime specimens.

The JSON demo was parsed and checked: both refusal guards true, expected
constraint_violation and write_conflict codes, 14 accepted steps, zero refused
steps, x approximately 0.672, y approximately -0.336 and remainder approximately
0.008. Nonempty test discovery and unchanged project inputs are enforced.

The qualified executable scripts, manifests and locks match the final source.
This report, evidence copies and documentation/task closure were added after
the cold snapshot. Final Verify.cmd closure passed 87 runtime and 28 tooling
tests, the demo, Pyright with zero diagnostics, planning and Markdown for
29 documents, and whitespace. Planning covered 34 cards, five phases and
15 requirements with zero issues. All 13 executable/configuration inputs
were also compared to their cold-qualified hashes and matched. The live
detailed verification output is .tools/verification/latest.json.

## Findings resolved during qualification

An initial stale-npm probe reached an uncached registry request before npm
explained lock drift. Explicit root-manifest parity now fails before resolution;
npm still validates the full locked tree afterward. A simulated-outage harness
initially failed to forward its child PowerShell exit status; it now does.
That was a harness defect, not successful bootstrap during an outage.

Inspection also found uv's default Windows interpreter registration. The final
bootstrap disables registration and executable shims. Only the trial-created
CPython3.13.18 registration was removed after checking its exact fixture path;
its absence was verified. Existing interpreter registrations were preserved,
and the final qualification proves the corrected setup leaves them unchanged.

## Evidence limits and next work

This qualifies version/dependency reproducibility on the observed Windows x64
machine, including cold network acquisition and subsequent offline checks.
It does not promise fully offline installation, byte-identical environments,
other operating systems, CI execution, performance, a renderer, an installed
application or human acceptance. The GIL-disabled and outage cases are
controlled simulations, not installations of another interpreter variant or
an observed upstream outage. Raw scratch checkouts are retained locally.

Runtime source, runtime tests, agent controls, historical drafts and the
unrelated root VERIFICATION.md remain unchanged. ST-003 owns automation of
these accepted gates; P1 still requires that work and aggregate exit review.

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: ST002_QUALIFICATION_RECORD
  "Dated execution evidence for the implemented prototype bootstrap."

[GL01]: QUALIFY_REPRODUCIBLE_PROTOTYPE_SETUP
  "Exercise cold setup, repeated setup and required refusal boundaries."

[DP01]: IMPLEMENTED_BOOTSTRAP_AND_PINNED_INPUTS
  "Repository scripts, version files, manifests, locks and archive identities."

[RQ01]: RECORD_EXECUTION_AND_ITS_LIMITS
  "Preserve source identity, environment, commands and outcomes without
  overstating simulation, platform or application evidence."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative invocation list for every local context marker."
