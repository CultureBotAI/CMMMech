from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,os,hashlib
p=Path('/private/tmp');root=p/'CMMMech-expansion-round77-20261014';out=p/'cmm-round77-review-check-final.json';log=out.with_suffix('.log');assert not out.exists() and not log.exists()
now=lambda:datetime.now(timezone.utc).isoformat()
command=['just','review-check','--base','e5e70cfc93a3aa68a166eba7bbbd3dc1053ce60d','--require-reviews']
r={'started_at':now(),'command':command,'worktree':str(root)}
x=subprocess.run(command,cwd=root,env=dict(os.environ,UV_OFFLINE='1',UV_CACHE_DIR='/private/tmp/cmmmech-uv-cache',PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True)
log.write_text(x.stdout+x.stderr);r.update(finished_at=now(),exit_code=x.returncode,log=str(log),log_sha256=hashlib.sha256(log.read_bytes()).hexdigest());out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));print(x.stdout[-1200:]);raise SystemExit(x.returncode)
