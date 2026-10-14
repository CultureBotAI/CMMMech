from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess

root = Path('/private/tmp/CMMMech-expansion-round77-20261014')
base = 'e5e70cfc93a3aa68a166eba7bbbd3dc1053ce60d'
out = Path('/private/tmp/cmm-round77-final-gates.json')
logpath = out.with_suffix('.log')
assert not out.exists() and not logpath.exists()
now = lambda: datetime.now(timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
def inputs():
    result = {}
    seen = set()
    for directory, dirs, files in os.walk(root / 'data/records', followlinks=True):
        resolved = Path(directory).resolve()
        if resolved in seen:
            dirs[:] = []
            continue
        seen.add(resolved)
        for name in files:
            if name.endswith(('.yaml', '.yml')):
                p = Path(directory) / name
                result[str(p.relative_to(root))] = sha(p)
    return result
before = inputs()
assert len(before) == 368
env = dict(os.environ, UV_OFFLINE='1', UV_CACHE_DIR='/private/tmp/cmmmech-uv-cache', PYTHONDONTWRITEBYTECODE='1')
receipt = {'base': base, 'worktree': str(root), 'started_at': now(), 'record_inputs': before, 'commands': []}
commands = [
    ['just', 'check'],
    ['uv', 'run', '--locked', 'cmmmech', 'validate', '--require-records'],
    ['uv', 'run', '--locked', 'cmmmech', 'validate-history', '--base', base],
    ['uv', 'run', '--locked', 'python', 'scripts/render_pages.py', '--check'],
]
with logpath.open('x') as log:
    for command in commands:
        started = now()
        p = subprocess.run(command, cwd=root, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log.write('$ ' + repr(command) + '\n' + p.stdout + '\n')
        log.flush()
        receipt['commands'].append({'command': command, 'started_at': started, 'finished_at': now(), 'exit_code': p.returncode})
        if p.returncode:
            break
receipt['inputs_unchanged'] = before == inputs()
receipt['exit_code'] = 0 if receipt['inputs_unchanged'] and len(receipt['commands']) == len(commands) and all(c['exit_code'] == 0 for c in receipt['commands']) else 1
receipt.update(finished_at=now(), log=str(logpath), log_sha256=sha(logpath))
out.write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({k: v for k, v in receipt.items() if k != 'record_inputs'}, indent=2))
raise SystemExit(receipt['exit_code'])
