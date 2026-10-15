from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,hashlib,sys
p=Path('/private/tmp');r=p/'CMMMech-expansion-round92-20261015';repo='CultureBotAI/CMMMech';number=int(sys.argv[1]);review_body=p/'cmm-round92-hosted-review-comment.md';out=p/'cmm-round92-queue-receipt.json';assert not out.exists()
sha=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
def run(cmd):return subprocess.check_output(cmd,cwd=r,text=True).strip()
def gh(*args):return run(['gh',*args])
c=json.loads((p/'cmm-round92-commit-receipt.json').read_text());prepath=p/'cmm-round92-preflight-committed-terminal.json';pre=json.loads(prepath.read_text())
assert pre['mode']=='preflight' and pre['exit_code']==0 and pre['trusted_base']==c['base'] and pre['topic_head']==c['head'] and pre['expected_tree']==c['tree']
assert sha(Path(pre['log']))==pre['log_sha256'] and all(x['exit_code'] in x['allowed_exit_codes'] for x in pre['commands'])
for cmd in [['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',c['base']],['just','review-check','--base',c['base'],'--require-reviews']]:assert any(x['command']==cmd and x['exit_code']==0 for x in pre['commands'])
assert pre['counts']==json.loads((p/'cmm-round92-helper-config.json').read_text())['counts']
assert run(['git','rev-parse','HEAD'])==c['head'] and not run(['git','status','--porcelain=v1','--untracked-files=all'])
pr=json.loads(gh('pr','view',str(number),'--repo',repo,'--json','number,url,state,headRefName,headRefOid,baseRefName,baseRefOid,title,body,isDraft'))
assert pr['state']=='OPEN' and not pr['isDraft'] and pr['headRefOid']==c['head'] and pr['headRefName']==c['branch'] and pr['baseRefName']=='main' and pr['baseRefOid']==c['base']
assert pr['body'].strip()==(p/'cmm-round92-pr-body.md').read_text().strip()
assert pr['title']==json.loads((p/'cmm-round92-helper-config.json').read_text())['title']
files=json.loads(gh('api',f'repos/{repo}/pulls/{number}/files?per_page=100','--paginate','--slurp'));names=sorted(x['filename'] for page in files for x in page);assert names==sorted(c['files'])
required=gh('pr','checks',str(number),'--repo',repo,'--required','--json','name,state,bucket,link');checks=json.loads(required);assert checks and all(x['bucket']=='pass' for x in checks) and any(x['name']=='validate-strict' for x in checks)
reviews=json.loads(gh('api',f'repos/{repo}/pulls/{number}/reviews?per_page=100'));matches=[x for x in reviews if x['commit_id']==c['head'] and x['state']=='COMMENTED' and x['body'].strip()==review_body.read_text().strip()];assert matches
rules=json.loads(gh('api',f'repos/{repo}/rules/branches/main'));assert any(x['type']=='merge_queue' and x['parameters']['merge_method']=='SQUASH' and x['parameters']['grouping_strategy']=='ALLGREEN' for x in rules)
assert any(x['type']=='required_status_checks' and any(s['context']=='validate-strict' for s in x['parameters']['required_status_checks']) for x in rules)
# This last read is immediately before admission; the native queue and postmerge parent/tree checks remain required.
main=json.loads(gh('api',f'repos/{repo}/git/ref/heads/main'));observed=datetime.now(timezone.utc).isoformat();assert main['object']['sha']==c['base']
command=['gh','pr','merge',str(number),'--repo',repo,'--match-head-commit',c['head']];x=subprocess.run(command,cwd=r,capture_output=True,text=True)
d={'recorded_at':datetime.now(timezone.utc).isoformat(),'pr':pr,'topic':c,'preflight_receipt':str(prepath),'preflight_sha256':sha(prepath),'preflight_log_sha256':pre['log_sha256'],'live_main_observed_at':observed,'live_main':main['object']['sha'],'checks':checks,'hosted_review_ids':[x['id'] for x in matches],'review_body_sha256':sha(review_body),'files':names,'effective_rules':rules,'queue_command':command,'exit_code':x.returncode,'stdout':x.stdout,'stderr':x.stderr,'limitation':'Live base read is not atomic locking; native merge-group checks and actual merged tree/parent plus fresh-main validation remain required.'}
out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({k:d[k] for k in ['recorded_at','live_main','hosted_review_ids','exit_code','stdout','stderr']},indent=2));raise SystemExit(x.returncode)
