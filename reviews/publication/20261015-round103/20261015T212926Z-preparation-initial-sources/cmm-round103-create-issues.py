from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,subprocess
T=Path('/private/tmp');W=T/'CMMMech-expansion-round103-20261015';repo='CultureBotAI/CMMMech'
drafts=json.loads((T/'cmm-round103-issue-drafts.json').read_text())
existing=json.loads((T/'cmm-round103-issues-precreate.json').read_text())
assert len(existing)<1000
# All 270 all-state title/body rows inspected; matches #125, #130 and #293 concern distinct work. Comments not searched.
assert len(existing)==270
receipt=[]
for item in drafts:
 p=Path(item['body_file']);body=p.read_text()
 assert item['title'] not in [x['title'] for x in existing]
 command=['gh','issue','create','--repo',repo,'--title',item['title'],'--body-file',str(p)]
 r=subprocess.run(command,cwd=W,capture_output=True,text=True);assert r.returncode==0,r.stderr
 url=r.stdout.strip();number=int(url.rsplit('/',1)[1])
 q=subprocess.run(['gh','issue','view',str(number),'--repo',repo,'--json','number,title,body,state,url'],cwd=W,capture_output=True,text=True);assert q.returncode==0,q.stderr
 data=json.loads(q.stdout);assert data['body']==body and data['title']==item['title'] and data['state']=='OPEN'
 data.update(created_at_observed=datetime.now(timezone.utc).isoformat(),body_file=str(p),body_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),dedup_scope='270 all-state title/body rows; comments not searched. Related hidden/ignored local/source searches are retained in the paired source dossiers.')
 receipt.append(data)
 with (T/f'cmm-round103-created-issue-{number}.json').open('x') as f:json.dump(data,f,indent=2);f.write('\n')
 print(f'Created #{number}: {data["title"]}',flush=True)
with (T/'cmm-round103-source-issues.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
