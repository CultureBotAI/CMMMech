from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import json,subprocess,hashlib,os
p=Path('/private/tmp');r=p/'CMMMech-expansion-round73-20261014'
commands={'admission':['gh','pr','view','581','--repo','CultureBotAI/culturebotai-claw','--json','number,state,mergedAt,url'],'convergence':['gh','issue','view','580','--repo','CultureBotAI/culturebotai-claw','--json','number,state,title,url'],'cmm_integration':['gh','issue','view','3','--repo','CultureBotAI/CMMMech','--json','number,state,title,url'],'queue':['gh','api','repos/CultureBotAI/CMMMech/rulesets/24692449']}
def fetch(kv):k,c=kv;return k,json.loads(subprocess.check_output(c,cwd=r,text=True))
with ThreadPoolExecutor(max_workers=4) as e:d=dict(e.map(fetch,commands.items()))
v=subprocess.run(['bash','scripts/check_vendored_sync.sh'],cwd=r,capture_output=True,text=True);log=p/'cmm-round73-vendored.log';log.write_text(v.stdout+v.stderr);assert v.returncode==0
assert d['admission']['state']=='MERGED' and d['convergence']['state']=='CLOSED' and d['cmm_integration']['state']=='CLOSED' and d['queue']['enforcement']=='active'
d.update(recorded_at=datetime.now(timezone.utc).isoformat(),scope='Read-only current status; no governance changes.',vendored_result=v.stdout.strip(),vendored_log_sha256=hashlib.sha256(log.read_bytes()).hexdigest())
out=p/'cmm-round73-integration-status.json';assert not out.exists();out.write_text(json.dumps(d,indent=2)+'\n');print(d['vendored_result'])
