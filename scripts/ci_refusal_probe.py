"""Exercise actual planning and Markdown failures in an isolated source fixture."""
from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tomllib
from typing import Any
from uuid import uuid4

from verify import ROOT, local_environment, source_snapshot


def require_refusal(exit_code: int, output: str, diagnostic: str) -> None:
    if exit_code == 0 or diagnostic not in output:
        raise RuntimeError(f"Expected nonzero refusal containing {diagnostic!r}; got exit {exit_code}.\n{output}")


def main() -> int:
    evidence_dir = ROOT / '.tools/ci'
    evidence_dir.mkdir(parents=True, exist_ok=True)
    fixture = evidence_dir / ('invalid planning fixture ' + uuid4().hex[:10])
    before = source_snapshot(ROOT)
    record: dict[str, Any] = {'timestamp_utc': datetime.now(timezone.utc).isoformat(),
                              'fixture': str(fixture), 'stages': [], 'source_hashes_before': before}
    node_dir = ROOT / ('.tools/node-v' + (ROOT/'.node-version').read_text().strip() + '-win-x64')
    uv_version = tomllib.loads((ROOT/'pyproject.toml').read_text())['tool']['uv']['required-version'][2:]
    env = local_environment(ROOT, node_dir, ROOT/f'.tools/uv-{uv_version}')

    def run(name: str, command: list[str], diagnostic: str = '') -> None:
        result = subprocess.run(command, cwd=ROOT, env=env, capture_output=True,
                                text=True, encoding='utf-8', errors='replace', timeout=180)
        output = result.stdout + result.stderr
        record['stages'].append({'name': name, 'command': command, 'exit_code': result.returncode,
                                  'stdout': result.stdout, 'stderr': result.stderr,
                                  'expected_diagnostic': diagnostic})
        if diagnostic:
            require_refusal(result.returncode, output, diagnostic)
        elif result.returncode:
            raise RuntimeError(f'{name} failed before fixture mutation:\n{output}')
        print(f'PASS: {name} (child exit {result.returncode})', flush=True)

    try:
        for name in before:
            target = fixture/name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT/name, target)
        checker = [sys.executable, str(ROOT/'scripts/check_planning.py'), '--root', str(fixture)]
        run('valid planning fixture', checker)
        todo = fixture/'TODO.md'
        broken, replacements = re.subn(r'(?m)^Next task: ST-\d+\s*$', 'Next task: ST-999999', todo.read_text(), count=1)
        if replacements != 1:
            raise RuntimeError('Cannot locate the next-task pointer for the planning refusal.')
        todo.write_text(broken, encoding='utf-8')
        run('invalid planning fixture', checker, 'ST-999999')
        markdown = fixture/'invalid-markdown.md'
        markdown.write_text('# First heading\n\n# Second heading\n', encoding='utf-8')
        run('invalid Markdown fixture', [str(node_dir/'node.exe'),
            str(ROOT/'node_modules/markdownlint-cli2/markdownlint-cli2-bin.mjs'), str(markdown)], 'MD025')
        record['status'] = 'passed'
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        record.update(status='failed', error=str(error))
        print(f'CI REFUSAL PROBE FAILED: {error}', file=sys.stderr)
    finally:
        record['source_hashes_after'] = source_snapshot(ROOT)
        if before != record['source_hashes_after']:
            record.update(status='failed', error='Refusal probes changed project inputs.')
        (evidence_dir/'refusal-probes.json').write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
    return 0 if record.get('status') == 'passed' else 1


if __name__ == '__main__':
    raise SystemExit(main())
