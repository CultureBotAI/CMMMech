from pathlib import Path
from datetime import datetime,timezone
import subprocess,os,json,hashlib
root=Path('/private/tmp/CMMMech-expansion-round73-20261014');base='ea4b9370fdb3d1ab23e5f43f6f9fe5f8d46a31e3'
prefix=Path('/private/tmp/cmm-round73-review-check-final');log=prefix.with_suffix('.log');out=prefix.with_suffix('.json')
assert not log.exists() and not out.exists()
env=dict(os.environ,UV_CACHE_DIR='/private/tmp/cmmmech-uv-cache',UV_OFFLINE='1',PYTHONDONTWRITEBYTECODE='1')
now=lambda:datetime.now(timezone.utc).isoformat()
cmd=['just','review-check','--base',base,'--require-reviews'];started=now()
with log.open('x') as f:p=subprocess.run(cmd,cwd=root,env=env,stdout=f,stderr=subprocess.STDOUT)
r={'started_at':started,'finished_at':now(),'base':base,'worktree':str(root),'commands':[{'command':cmd,'exit_code':p.returncode}],'exit_code':p.returncode,'log':str(log),'log_sha256':hashlib.sha256(log.read_bytes()).hexdigest()}
out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));raise SystemExit(p.returncode)
