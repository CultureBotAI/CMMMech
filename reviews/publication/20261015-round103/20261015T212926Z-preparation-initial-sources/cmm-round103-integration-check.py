from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import json,subprocess,hashlib
W=Path('/private/tmp/CMMMech-expansion-round103-20261015');T=Path('/private/tmp');old=json.loads((W/'reviews/publication/20261015-round102/integration-status.json').read_text());new={}
def collect(item):
 k,v=item;p=subprocess.run(v['command'],cwd=W,capture_output=True,text=True);assert p.returncode==0,(k,p.stderr);return k,{'command':v['command'],'exit_code':p.returncode,'data':json.loads(p.stdout),'stderr':p.stderr}
with ThreadPoolExecutor(max_workers=4) as pool:
 for k,v in pool.map(collect,[(k,v) for k,v in old.items() if isinstance(v,dict) and 'command' in v and k!='governed_check']):new[k]=v
p=subprocess.run(['bash','scripts/check_vendored_sync.sh'],cwd=W,capture_output=True,text=True);log=T/'cmm-round103-governed-check.log'
with log.open('x') as f:f.write(p.stdout+p.stderr)
g={'recorded_at':datetime.now(timezone.utc).isoformat(),'command':['bash','scripts/check_vendored_sync.sh'],'exit_code':p.returncode,'log':str(log),'log_sha256':hashlib.sha256(log.read_bytes()).hexdigest()}
with (T/'cmm-round103-governed-check.json').open('x') as f:json.dump(g,f,indent=2);f.write('\n')
assert p.returncode==0,p.stderr
new.update(recorded_at=datetime.now(timezone.utc).isoformat(),governed_check=g,limits=old['limits']);pub=W/'reviews/publication/20261015-round103';pub.mkdir(exist_ok=True)
with (pub/'integration-status.json').open('x') as f:json.dump(new,f,indent=2);f.write('\n')
print(json.dumps({'main':new['main']['data']['object']['sha'],'admission':new['claw_admission581']['data'],'issue3':new['cmm_issue3']['data']['state'],'shepherd_runs':len(new['shepherd_runs']['data']),'governed_exit':p.returncode},indent=2))
