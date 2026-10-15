from pathlib import Path
from datetime import datetime, timezone
import subprocess, json, hashlib, os
root = Path('/private/tmp/CMMMech-expansion-round103-20261015')
base = '44d5b468519eb862b32ef54bf7c066bc0f79ba62'
out = Path('/private/tmp/cmm-round103-review-check-final.json')
log = out.with_suffix('.log')
now = lambda: datetime.now(timezone.utc).isoformat()
command = ['just', 'review-check', '--base', base, '--require-reviews']
with out.open('x') as receipt, log.open('x') as stream:
    start = now()
    result = subprocess.run(command, cwd=root, env=dict(os.environ, UV_OFFLINE='1', UV_CACHE_DIR='/private/tmp/cmmmech-uv-cache', PYTHONDONTWRITEBYTECODE='1'), stdout=stream, stderr=subprocess.STDOUT, text=True)
    stream.flush()
    data = {'base': base, 'command': command, 'started_at': start, 'finished_at': now(), 'exit_code': result.returncode, 'log': str(log), 'log_sha256': hashlib.sha256(log.read_bytes()).hexdigest()}
    json.dump(data, receipt, indent=2); receipt.write('\n')
print(json.dumps(data, indent=2))
raise SystemExit(result.returncode)
