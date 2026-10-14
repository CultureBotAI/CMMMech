from pathlib import Path
from datetime import datetime,timezone
import subprocess,os,json,hashlib,sys
root=Path('/private/tmp/CMMMech-expansion-round73-20261014');base='ea4b9370fdb3d1ab23e5f43f6f9fe5f8d46a31e3'
mode=sys.argv[1];assert mode in ('baseline','final-gates')
prefix=Path('/private/tmp')/('cmm-round73-'+mode)
log=prefix.with_suffix('.log');out=prefix.with_suffix('.json');assert not log.exists() and not out.exists()
env=dict(os.environ,UV_CACHE_DIR='/private/tmp/cmmmech-uv-cache',UV_OFFLINE='1',PYTHONDONTWRITEBYTECODE='1')
now=lambda:datetime.now(timezone.utc).isoformat()
r={'started_at':now(),'worktree':str(root),'base':base,'commands':[]}
cmds=[['just','check'],['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',base]]
if mode=='baseline':cmds.insert(0,['uv','sync','--quiet','--locked','--extra','dev','--offline'])
code=0
with log.open('x') as f:
 for cmd in cmds:
  start=now();f.write('$ '+repr(cmd)+'\n');f.flush()
  q=subprocess.run(cmd,cwd=root,env=env,stdout=f,stderr=subprocess.STDOUT)
  r['commands'].append({'command':cmd,'started_at':start,'finished_at':now(),'exit_code':q.returncode})
  if q.returncode:code=q.returncode;break
r.update(finished_at=now(),exit_code=code,log=str(log),log_sha256=hashlib.sha256(log.read_bytes()).hexdigest())
out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));raise SystemExit(code)
