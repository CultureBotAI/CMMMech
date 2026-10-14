from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess

def require_preflight_identity(preflight, commit):
 expected={'exit_code':0,'mode':'preflight','trusted_base':commit['base'],'topic_head':commit['head'],'expected_tree':commit['tree']}
 if any(preflight.get(k)!=v for k,v in expected.items()):
  raise RuntimeError('Preflight identity differs from the reviewed commit')
 commands=preflight.get('commands',[])
 if not commands or any(x['exit_code'] not in x['allowed_exit_codes'] for x in commands):
  raise RuntimeError('Preflight command evidence is missing or failed')
 for command in [
  ['uv','run','--locked','cmmmech','validate','--require-records'],
  ['uv','run','--locked','cmmmech','validate-history','--base',commit['base']],
  ['just','review-check','--base',commit['base'],'--require-reviews']]:
  if not any(x['command']==command and x['exit_code']==0 for x in commands):
   raise RuntimeError('Required preflight gate is missing')
 if hashlib.sha256(Path(preflight['log']).read_bytes()).hexdigest()!=preflight['log_sha256']:
  raise RuntimeError('Preflight log differs from its receipt')

def require_live_base(live_ref, commit):
 if live_ref.get('ref')!='refs/heads/main' or live_ref.get('object',{}).get('sha')!=commit['base']:
  raise RuntimeError('Live main moved from the reviewed base; refresh preflight before queue admission')

p=Path('/private/tmp');repo='CultureBotAI/CMMMech';c=json.loads((p/'cmm-round75-commit-receipt.json').read_text());opened=json.loads((p/'cmm-round75-pr-open.json').read_text());number=opened['number'];out=p/'cmm-round75-queue-request.json';assert not out.exists()
assert c['base']=='4cb10d22d5542370cf5fac27288907ec0d42308c' and c['branch']=='curate/cmm-expansion-round75-20261014'
def run(a):return subprocess.check_output(a,text=True).strip()
pr=json.loads(run(['gh','pr','view',str(number),'--repo',repo,'--json','number,state,headRefOid,baseRefName,statusCheckRollup,url']))
assert pr['state']=='OPEN' and pr['headRefOid']==c['head'] and pr['baseRefName']=='main'
peers=[json.loads(f.read_text()) for f in p.glob('cmm-round75-hosted-peer-*.json') if not f.name.endswith('-responses.json')]
assert any(x.get('passed') and x.get('pr')==number and x.get('head')==c['head'] and x.get('tree')==c['tree'] for x in peers), 'Require completed exact-head hosted peer assurance before queue admission'
checks=json.loads(run(['gh','pr','checks',str(number),'--repo',repo,'--required','--json','name,state,bucket,link']))
assert checks and all(x['bucket']=='pass' for x in checks) and any(x['name']=='validate-strict' for x in checks)
rules=json.loads(run(['gh','api',f'repos/{repo}/rulesets/24692449']))
assert rules['enforcement']=='active' and not rules.get('bypass_actors')
queue=[r for r in rules['rules'] if r['type']=='merge_queue'];assert len(queue)==1
assert queue[0]['parameters']['merge_method']=='SQUASH' and queue[0]['parameters']['grouping_strategy']=='ALLGREEN'
effective=json.loads(run(['gh','api',f'repos/{repo}/rules/branches/main']))
assert any(r['type']=='merge_queue' and r['parameters']['merge_method']=='SQUASH' and r['parameters']['grouping_strategy']=='ALLGREEN' for r in effective)
review=json.loads((p/'cmm-round75-pr-review-posted.json').read_text());assert review['commit_id']==c['head'] and review['state']=='COMMENTED'
live_review=json.loads(run(['gh','api',f"repos/{repo}/pulls/{number}/reviews/{review['id']}"]))
assert live_review['commit_id']==c['head'] and live_review['state']=='COMMENTED' and live_review['body']==review['body']
preflight=json.loads((p/'cmm-round75-preflight-committed-terminal.json').read_text())
require_preflight_identity(preflight,c)
live_main=json.loads(run(['gh','api',f'repos/{repo}/git/ref/heads/main']))
live_main_observed_at=datetime.now(timezone.utc).isoformat()
require_live_base(live_main,c)
x=subprocess.run(['gh','pr','merge',str(number),'--repo',repo,'--match-head-commit',c['head']],capture_output=True,text=True)
receipt={'recorded_at':datetime.now(timezone.utc).isoformat(),'pr':number,'head':c['head'],'pr_before':pr,'required_checks':checks,'ruleset':rules,'effective_main_rules':effective,'live_review':live_review,'preflight_receipt_sha256':hashlib.sha256((p/'cmm-round75-preflight-committed-terminal.json').read_bytes()).hexdigest(),'live_main_before_enqueue':{'observed_at':live_main_observed_at,'response':live_main,'matches_reviewed_base':True},'concurrency_limit':'Read-before-enqueue is not atomic base locking; actual merged tree/parent and fresh-main checks remain required.','command':x.args,'exit_code':x.returncode,'stdout':x.stdout,'stderr':x.stderr}
out.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'pr':number,'exit_code':x.returncode,'stdout':x.stdout,'stderr':x.stderr},indent=2));raise SystemExit(x.returncode)
