# Prototype setup and verification [DOC]

Use this guide to run the current scalar prototype on Windows x64. The
[toolchain decision](decisions/prototype_toolchain.md) owns version policy;
the [global plan](global_plan.md) and [task cards](todos/tooling.md) own scope.

> Goal: [GL01] - REPRODUCE_THE_SELECTED_ENVIRONMENT
> Dependency: [DP01] - PINNED_INPUTS_AND_LOCAL_TOOLS
> Requirement: [RQ01] - VERIFY_WITHOUT_REPAIRING_INPUTS

## First setup

Start from a Git checkout with 64-bit Windows PowerShell 5.1 or newer and Git
available on PATH. Allow network access to the official uv, managed Python,
Node and npm distribution services. No preinstalled Python, uv, Node or npm
is required. From the repository root:

```powershell
.\Bootstrap.cmd
```

The bootstrap downloads checksum-verified uv and Node archives, installs the
pinned GIL-enabled CPython through uv, creates .venv, installs locked npm
development tools and runs every required check. A path containing spaces is
supported. Tools and caches stay inside the checkout; global tool versions
and shell configuration are not changed. Repeating setup reuses the local
downloads and enforces the same locks.

| Component | Selected version | Repository authority |
| --- | --- | --- |
| CPython | 3.13.18, normal GIL | [.python-version](../.python-version) |
| uv | 0.13.7 | [pyproject.toml](../pyproject.toml) |
| Node | 24.22.2 | [.node-version](../.node-version) |
| npm | 11.19.1, bundled with Node | [package.json](../package.json) |
| Pyright | 1.1.414 | package.json and package-lock.json |
| markdownlint-cli2 | 0.23.1 | package.json and package-lock.json |

The [archive record](../scripts/toolchain-artifacts.json) fixes upstream URLs
and SHA-256 values. [uv.lock](../uv.lock) records an empty runtime dependency
set; [package-lock.json](../package-lock.json) fixes the development dependency
tree and package integrity values. This is a non-packaged Python project;
there is no wheel build or application installer.

## Everyday commands

```powershell
.\Verify.cmd
.\.venv\Scripts\python.exe -m spinaltap
.\.venv\Scripts\python.exe -m spinaltap --json
```

Verification uses the existing local environment without downloading or
installing tools. It checks exact versions and interpreter origin, lock
freshness, the installed npm tree, nonempty runtime and tooling test suites,
the demo's JSON results, Pyright with warnings treated as failures, planning
consistency, Markdown lint and Git whitespace. Source and lock hashes must
remain unchanged. The full command outputs and results are written to
.tools/verification/latest.json; a failing check returns a nonzero exit code.

Markdown scope is README.md, TODO.md and Markdown under docs, reports and
research_notes. Agent controls, historical .user_notes and the unrelated root
VERIFICATION.md are outside that gate. Mypy is optional and is not installed
by this bootstrap. See the [development workflow](development_workflow.md)
for task selection and evidence requirements.

## Failure recovery and intentional updates

Missing local tools or a damaged environment: run Bootstrap.cmd and inspect
the named failing stage. Verification itself never repairs or downloads them.
A stale manifest/lock pair fails; restore the intended pair or make an explicit
tool update. An archive integrity error identifies the exact cached archive
to remove before retrying. Network failures report the failed download or
child command and return failure; restore access and retry setup.

Pins and locks are reviewed together. For an intentional update, first revise
the accepted policy, version files, manifest pins and archive URL/hash record.
Bootstrap.cmd -ToolsOnly installs only uv and Node, allowing maintainers to
generate reviewed locks before a normal bootstrap. With the pinned executables:

```powershell
.\Bootstrap.cmd -ToolsOnly
.\.tools\uv-0.13.7\uv.exe lock --managed-python --config-file .tools/uv.toml
.\.tools\node-v24.22.2-win-x64\node.exe `
  .\.tools\node-v24.22.2-win-x64\node_modules\npm\bin\npm-cli.js `
  install --package-lock-only --ignore-scripts --no-audit --no-fund
.\Bootstrap.cmd
```

Those versioned paths must follow the new pins when upgrading. Lock generation
is a maintainer operation, never part of ordinary setup or verification. Review
the complete lock diff and repeat qualification before accepting an upgrade.

## Repeat the environment qualification

```powershell
.\.venv\Scripts\python.exe scripts/qualify_bootstrap.py
```

The harness makes a fresh local clone, overlays the current uncommitted inputs
and downloads into empty caches under .qualification in a path with spaces.
It runs setup twice, compares locked inputs, exercises refusal cases and runs
verification again after restoring fixtures. The JSON record retains the base
commit, every source hash, command, result and log. It preserves scratch
directories for inspection. An optional --unsupported-python argument names
an existing interpreter for a real wrong-version probe. GIL-disabled and
network-outage probes are simulations; they do not install a free-threaded
interpreter or depend on an actual service outage.

Qualification covers the selected Windows x64 environment. CI, other operating
systems, rendered behavior, performance and installed-application acceptance
require their own evidence. Dated results are linked from the tooling card.
The [automated-checks guide](continuous_integration.md) explains the CI job and
how to diagnose or reproduce it in a fresh checkout.

## (Y) Link-complete usage index [LI]

- Context: [DOC], [GL01], [DP01], [RQ01], [LI]

## (Z) Context-Citations

[DOC]: PROTOTYPE_SETUP_GUIDE
  "Contributor commands, version ownership, failure recovery and qualification."

[GL01]: REPRODUCE_THE_SELECTED_ENVIRONMENT
  "Bootstrap and verify the accepted Windows scalar prototype toolchain."

[DP01]: PINNED_INPUTS_AND_LOCAL_TOOLS
  "Version files, manifests, dependency locks and checksum-verified archives."

[RQ01]: VERIFY_WITHOUT_REPAIRING_INPUTS
  "Required checks fail on drift and preserve project source and locked inputs."

[LI]: LINK_COMPLETE_USAGE_INDEX
  "The non-authoritative invocation list for every local context marker."
