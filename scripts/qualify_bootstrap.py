"""Cold-checkout qualification and disposable refusal probes for ST-002."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Any, Iterator
from uuid import uuid4

from verify import ROOT, local_environment, source_snapshot


def python_registry() -> dict[str, Any]:
    """Capture uv's per-user registration area without creating any keys."""
    import winreg
    result: dict[str, Any] = {}

    def visit(path: str) -> None:
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)
        except FileNotFoundError:
            return
        with key:
            children, values, _ = winreg.QueryInfoKey(key)
            result[path] = [repr(winreg.EnumValue(key, i)) for i in range(values)]
            for i in range(children):
                visit(path + '\\' + winreg.EnumKey(key, i))

    visit(r'Software\Python\Astral')
    return result


@contextmanager
def changed(path: Path, content: str) -> Iterator[None]:
    original = path.read_bytes()
    try:
        path.write_text(content, encoding="utf-8")
        yield
    finally:
        path.write_bytes(original)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--unsupported-python', type=Path,
                        help='Optional actual unsupported interpreter for an additional refusal probe')
    args = parser.parse_args()
    run = ROOT / '.qualification' / ('ST-002 cold checkout ' + uuid4().hex[:10])
    run.mkdir(parents=True)
    checkout = run / 'path with spaces'
    evidence: dict[str, Any] = {'started_utc': datetime.now(timezone.utc).isoformat(),
                               'source_root': str(ROOT), 'checkout': str(checkout), 'cases': []}
    evidence['python_registry_before'] = python_registry()
    def execute(name: str, command: list[str], *, expected: int = 0,
                contains: str = '', cwd: Path = checkout, env=None) -> str:
        print(f'Qualifying {name}...', flush=True)
        result = subprocess.run(command, cwd=cwd, env=env, capture_output=True,
                                text=True, encoding='utf-8', errors='replace', timeout=600)
        output = result.stdout + result.stderr
        log = run / f'{len(evidence["cases"]):02d}-{name}.txt'
        log.write_text(output, encoding='utf-8')
        accepted = ((result.returncode == 0) if expected == 0 else (result.returncode != 0))
        accepted = accepted and contains in output
        evidence['cases'].append({'name': name, 'command': command, 'exit_code': result.returncode,
                                  'expected_success': expected == 0, 'passed': accepted,
                                  'log': log.name, 'output': output})
        if not accepted:
            raise RuntimeError(f'{name}: unexpected result {result.returncode}; see {log}\n{output[-4000:]}')
        return output
    try:
        execute('clone', ['git', 'clone', '--quiet', '--no-hardlinks', str(ROOT), str(checkout)], cwd=ROOT)
        snapshot = source_snapshot(ROOT)
        evidence['implementation_hashes'] = snapshot
        # Overlay uncommitted implementation on a fresh clone; never copy environments/caches.
        for name in snapshot:
            target = checkout / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / name, target)
        evidence['base_revision'] = subprocess.check_output(['git','rev-parse','HEAD'], cwd=checkout, text=True).strip()
        evidence['cold_paths_absent'] = {name: not (checkout / name).exists()
                                        for name in ('.tools', '.venv', 'node_modules')}
        if not all(evidence['cold_paths_absent'].values()):
            raise RuntimeError('Cold checkout inherited an environment or cache.')
        bootstrap = ['powershell.exe','-NoProfile','-ExecutionPolicy','Bypass','-File', str(checkout/'scripts/bootstrap.ps1')]
        execute('cold-bootstrap', bootstrap)
        cold_report = json.loads((checkout/'.tools/verification/latest.json').read_text())
        evidence['cold_verification'] = cold_report
        if cold_report['source_hashes_after'] != snapshot:
            raise RuntimeError('Cold bootstrap changed project inputs.')
        evidence['python_build'] = (Path(cold_report['environment']['base_prefix'])/'BUILD').read_text().strip()
        locked_files = ['.python-version','.node-version','pyproject.toml','uv.lock','package.json','package-lock.json']
        def hashes():
            return {name: hashlib.sha256((checkout/name).read_bytes()).hexdigest() for name in locked_files}
        evidence['lock_hashes_before_repeat'] = hashes()
        execute('repeat-bootstrap', bootstrap)
        evidence['lock_hashes_after_repeat'] = hashes()
        if evidence['lock_hashes_before_repeat'] != evidence['lock_hashes_after_repeat']:
            raise RuntimeError('Repeat bootstrap changed locked inputs.')
        evidence['repeat_verification'] = json.loads((checkout/'.tools/verification/latest.json').read_text())
        python = str(checkout/'.venv/Scripts/python.exe')
        node_dir = checkout / ('.tools/node-v' + (checkout/'.node-version').read_text().strip() + '-win-x64')
        import tomllib
        uv_version = tomllib.loads((checkout/'pyproject.toml').read_text())['tool']['uv']['required-version'][2:]
        uv_dir = checkout / f'.tools/uv-{uv_version}'
        uv = str(uv_dir/'uv.exe')
        env = local_environment(checkout, node_dir, uv_dir)
        verify = [python, str(checkout/'scripts/verify.py')]
        project = checkout/'pyproject.toml'
        with changed(project, project.read_text().replace('>=3.13.18,<3.14', '>=3.13.18,<3.13.19')):
            execute('stale-python-lock', [uv,'sync','--locked','--managed-python','--config-file','.tools/uv.toml'],
                    expected=1, contains='lockfile', env=env)
        package = checkout/'package.json'
        data = json.loads(package.read_text())
        data['devDependencies']['pyright'] = '1.1.413'
        with changed(package, json.dumps(data)):
            execute('stale-npm-lock', verify, expected=1, contains='Stale package-lock.json', env=env)
        manifest = checkout/'node_modules/pyright/package.json'
        held = manifest.with_suffix('.held')
        manifest.rename(held)
        try:
            execute('missing-checker', verify, expected=1, contains='Missing local checker pyright', env=env)
        finally:
            held.rename(manifest)
        data = json.loads(manifest.read_text())
        data['version'] = '0.0.0'
        with changed(manifest, json.dumps(data)):
            execute('wrong-checker-version', verify, expected=1, contains='got 0.0.0', env=env)
        entry = checkout/'node_modules/pyright/index.js'
        with changed(entry, "console.log('PASS'); process.exit(23);\n"):
            execute('failed-child-command', verify, expected=1, contains='Pyright failed (exit 23)', env=env)
        if args.unsupported_python:
            execute('unsupported-python', [str(args.unsupported_python.resolve()), str(checkout/'scripts/verify.py')],
                    expected=1, contains='Python: expected', env=env)
        # Real process: simulate a GIL-disabled build flag before entering verification.
        execute('free-threaded-refusal', [python,'-c',
                "import sys; sys.path.insert(0,'scripts'); import verify; "
                "verify.sysconfig.get_config_var=lambda key: 1 if key=='Py_GIL_DISABLED' else None; "
                "raise SystemExit(verify.main([]))"], expected=1, contains='GIL-enabled CPython', env=env)
        # Empty tool location, no real network needed: injected downloader failure.
        outage = run / 'network outage fixture'
        (outage/'scripts').mkdir(parents=True)
        for name in ('.python-version','.node-version','pyproject.toml','package.json',
                     'scripts/bootstrap.ps1','scripts/toolchain-artifacts.json'):
            shutil.copy2(checkout/name, outage/name)
        harness = outage/'outage.ps1'
        harness.write_text("function Invoke-WebRequest { throw 'simulated network outage' }\n"
                           "& (Join-Path $PSScriptRoot 'scripts/bootstrap.ps1') -ToolsOnly\n"
                           "exit $LASTEXITCODE\n", encoding='utf-8')
        execute('network-failure', ['powershell.exe','-NoProfile','-ExecutionPolicy','Bypass','-File',str(harness)],
                expected=1, contains='simulated network outage', cwd=outage)
        execute('after-refusals', verify, env=env)
        evidence['python_registry_after'] = python_registry()
        if evidence['python_registry_before'] != evidence['python_registry_after']:
            raise RuntimeError('Qualification changed the per-user Astral Python registrations.')
        evidence['status'] = 'passed'
        print(f'PASS: qualification evidence at {run / "qualification.json"}')
        return 0
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        evidence.update(status='failed', error=str(error))
        print(f'QUALIFICATION FAILED: {error}', file=sys.stderr)
        return 1
    finally:
        (run/'qualification.json').write_text(json.dumps(evidence, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    raise SystemExit(main())
