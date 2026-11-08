"""Verify the pinned, local Windows prototype without repairing its inputs."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import sysconfig
import tomllib
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


class VerificationError(RuntimeError):
    pass


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def local_environment(root: Path, node_dir: Path, uv_dir: Path) -> dict[str, str]:
    temp = root / ".tools/tmp"
    temp.mkdir(parents=True, exist_ok=True)
    env = {k: v for k, v in os.environ.items()
           if not k.upper().startswith(("UV_", "PYTHON", "NPM_CONFIG_"))
           and k.upper() not in {"VIRTUAL_ENV", "NODE_OPTIONS", "NODE_PATH"}}
    env.update({
        "PATH": os.pathsep.join((str(node_dir), str(uv_dir), env.get("PATH", ""))),
        "PYTHONNOUSERSITE": "1", "PYTHONDONTWRITEBYTECODE": "1",
        "TEMP": str(temp), "TMP": str(temp),
        "UV_CACHE_DIR": str(root / ".tools/cache/uv"),
        "UV_PYTHON_INSTALL_DIR": str(root / ".tools/python"),
        "UV_PROJECT_ENVIRONMENT": str(root / ".venv"),
        "UV_PYTHON_DOWNLOADS": "never", "UV_OFFLINE": "1",
        "npm_config_cache": str(root / ".tools/cache/npm"),
        "npm_config_userconfig": str(root / ".tools/empty-user.npmrc"),
        "npm_config_globalconfig": str(root / ".tools/empty-global.npmrc"),
    })
    return env


def require_version(actual: str, expected: str, label: str) -> None:
    if actual != expected:
        raise VerificationError(f"{label}: expected {expected}, got {actual}; run Bootstrap.cmd.")


def require_npm_lock(package: dict[str, Any], lock: dict[str, Any]) -> None:
    """Reject manifest drift before npm tries to resolve uncached metadata."""
    if lock.get("lockfileVersion") != 3:
        raise VerificationError("package-lock.json must use lockfileVersion 3.")
    locked = lock.get("packages", {}).get("", {})
    for field in ("name", "version", "dependencies", "devDependencies",
                  "optionalDependencies", "engines"):
        if package.get(field) != locked.get(field):
            raise VerificationError(f"Stale package-lock.json: root {field} differs from package.json; "
                                    "review and regenerate the lock during an intentional tool update.")


def require_runtime(root: Path, version: str) -> None:
    require_version(platform.python_version(), version, "Python")
    if sys.implementation.name != "cpython" or sysconfig.get_config_var("Py_GIL_DISABLED"):
        raise VerificationError("Reference runtime requires GIL-enabled CPython.")
    if sys.platform != "win32" or platform.machine().lower() not in {"amd64", "x86_64"}:
        raise VerificationError("Reference qualification covers Windows x64 only.")
    if Path(sys.prefix).resolve() != (root / ".venv").resolve():
        raise VerificationError("Use Verify.cmd or the repository .venv Python.")
    if not Path(sys.base_prefix).resolve().is_relative_to((root / ".tools/python").resolve()):
        raise VerificationError("Python must come from this repository's managed installation.")


def require_test_count(output: str) -> int:
    counts = re.findall(r"Ran (\d+) tests? in", output)
    if not counts or int(counts[-1]) == 0:
        raise VerificationError("Test discovery produced no tests or no unittest summary.")
    return int(counts[-1])


def validate_demo(report: Any) -> None:
    try:
        if not (report["oversized_delta_refused"] is True
                and report["conflicting_writes_refused"] is True
                and report["guard_refusal_code"] == "constraint_violation"
                and report["conflict_refusal_code"] == "write_conflict"
                and sum(f["accepted_steps"] for f in report["frames"]) == 14
                and sum(f["refused_steps"] for f in report["frames"]) == 0):
            raise ValueError("guard or step accounting mismatch")
        for actual, expected in ((report["final_state"]["x"], .672),
                                 (report["final_state"]["y"], -.336),
                                 (report["frames"][-1]["remainder"], .008)):
            if isinstance(actual, bool) or not math.isclose(actual, expected, abs_tol=1e-12):
                raise ValueError("unexpected numeric result")
    except (AssertionError, KeyError, IndexError, TypeError, ValueError) as error:
        raise VerificationError(f"Demo output does not satisfy the reference scenario: {error}") from error


def source_snapshot(root: Path) -> dict[str, str]:
    result = subprocess.run(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
                            cwd=root, capture_output=True, check=True)
    paths = result.stdout.decode("utf-8").split("\0")
    return {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
            for name in sorted(set(paths)) if name and (root / name).is_file()}


class Runner:
    def __init__(self, root: Path, env: dict[str, str]):
        self.root = root
        self.env = env
        self.stages: list[dict[str, Any]] = []

    def run(self, label: str, args: list[str]) -> str:
        print(f"Checking {label}...", flush=True)
        try:
            result = subprocess.run(args, cwd=self.root, env=self.env, capture_output=True,
                                    text=True, encoding="utf-8", errors="replace", timeout=180)
        except (OSError, subprocess.TimeoutExpired) as error:
            raise VerificationError(f"{label}: cannot run command: {error}") from error
        output = result.stdout + result.stderr
        self.stages.append({"name": label, "command": args, "exit_code": result.returncode,
                            "stdout": result.stdout, "stderr": result.stderr})
        if result.returncode:
            excerpt = output if len(output) < 5000 else output[:2000] + "\n[Full output in JSON evidence]\n" + output[-2000:]
            raise VerificationError(f"{label} failed (exit {result.returncode}):\n{excerpt}")
        return result.stdout if label == "demo" else output.strip()


def verify(root: Path, evidence: dict[str, Any]) -> None:
    before = source_snapshot(root)
    evidence["source_hashes_before"] = before
    runner = Runner(root, os.environ.copy())
    evidence["stages"] = runner.stages
    try:
        project_text = (root / "pyproject.toml").read_text(encoding="utf-8")
        project = tomllib.loads(project_text)
        package = read_json(root / "package.json")
        python_version = (root / ".python-version").read_text().strip()
        node_version = (root / ".node-version").read_text().strip()
        uv_pin = project["tool"]["uv"]["required-version"]
        if not re.fullmatch(r"==\d+\.\d+\.\d+", uv_pin):
            raise VerificationError("uv must have an exact required-version pin.")
        uv_version = uv_pin[2:]
        uv_dir = root / f".tools/uv-{uv_version}"
        node_dir = root / f".tools/node-v{node_version}-win-x64"
        uv, node = str(uv_dir / "uv.exe"), str(node_dir / "node.exe")
        npm = str(node_dir / "node_modules/npm/bin/npm-cli.js")
        runner.env = local_environment(root, node_dir, uv_dir)
        require_runtime(root, python_version)
        require_version(package["engines"]["node"], node_version, "Node manifest")
        require_version(package["packageManager"], "npm@" + package["engines"]["npm"], "npm manifest")
        for name in ("uv.lock", "package-lock.json"):
            if not (root / name).is_file():
                raise VerificationError(f"Missing {name}; verification never generates locks.")
        require_npm_lock(package, read_json(root / "package-lock.json"))
        if (root / ".tools/uv.toml").read_text().strip() != f'required-version = "{uv_pin}"':
            raise VerificationError("Derived uv configuration is stale; run Bootstrap.cmd.")
        require_version(runner.run("uv version", [uv, "--version"]).split()[1], uv_version, "uv")
        require_version(runner.run("Node version", [node, "--version"]), "v" + node_version, "Node")
        require_version(runner.run("npm version", [node, npm, "--version"]), package["engines"]["npm"], "npm")
        evidence["environment"] = {"python": sys.version, "executable": sys.executable,
            "base_prefix": sys.base_prefix, "platform": platform.platform(),
            "uv": uv_version, "node": node_version, "npm": package["engines"]["npm"]}
        for name, version in package["devDependencies"].items():
            manifest = root / "node_modules" / name / "package.json"
            if not manifest.is_file():
                raise VerificationError(f"Missing local checker {name}; run Bootstrap.cmd.")
            require_version(read_json(manifest)["version"], version, name)
        runner.run("Python lock freshness", [uv, "lock", "--check", "--managed-python",
                                             "--config-file", ".tools/uv.toml"])
        runner.run("npm lock freshness", [node, npm, "ci", "--dry-run", "--ignore-scripts",
                                          "--offline", "--no-audit", "--no-fund"])
        runner.run("installed npm tree", [node, npm, "ls", "--all", "--json"])
        evidence["test_counts"] = {}
        for label, directory in (("runtime tests", "tests"), ("tooling tests", "scripts/tests")):
            output = runner.run(label, [sys.executable, "-m", "unittest", "discover", "-s", directory])
            evidence["test_counts"][label] = require_test_count(output)
        demo = json.loads(runner.run("demo", [sys.executable, "-m", "spinaltap", "--json"]))
        validate_demo(demo)
        evidence["demo"] = demo
        runner.run("Pyright", [node, "node_modules/pyright/index.js", "--warnings"])
        runner.run("planning", [sys.executable, "scripts/check_planning.py"])
        runner.run("Markdown", [node, "node_modules/markdownlint-cli2/markdownlint-cli2-bin.mjs",
                                "README.md", "TODO.md", "docs/**/*.md", "reports/**/*.md",
                                "research_notes/**/*.md"])
        runner.run("whitespace", ["git", "diff", "--check"])
    finally:
        after = source_snapshot(root)
        evidence["source_hashes_after"] = after
        if before != after:
            raise VerificationError("Verification changed project inputs; inspect the recorded hashes.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="JSON evidence path (default .tools/verification/latest.json)")
    args = parser.parse_args(argv)
    report_path = args.report or ROOT / ".tools/verification/latest.json"
    if not report_path.resolve().is_relative_to((ROOT / ".tools").resolve()):
        parser.error("Evidence reports must be stored under this repository's .tools directory.")
    evidence: dict[str, Any] = {"timestamp_utc": datetime.now(timezone.utc).isoformat(), "root": str(ROOT)}
    try:
        evidence["revision"] = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        evidence["working_tree"] = subprocess.check_output(["git", "status", "--short"], cwd=ROOT, text=True)
        verify(ROOT, evidence)
        evidence["status"] = "passed"
        code = 0
        print("PASS: all required checks passed; project inputs unchanged.")
    except (VerificationError, OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        evidence.update(status="failed", error=str(error))
        print(f"VERIFICATION FAILED: {error}", file=sys.stderr)
        code = 1
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(f"Evidence: {report_path}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
