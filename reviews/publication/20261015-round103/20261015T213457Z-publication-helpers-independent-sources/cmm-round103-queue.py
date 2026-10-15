from pathlib import Path
import datetime,hashlib,json,subprocess
T=Path('/private/tmp');W=T/'CMMMech-expansion-round103-20261015';REPO='CultureBotAI/CMMMech';BASE='44d5b468519eb862b32ef54bf7c066bc0f79ba62';HEAD='ROUND103_TOPIC_HEAD';TREE='ROUND103_TOPIC_TREE';BRANCH='curate/cmm-expansion-round103-20261015'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
out=T/'cmm-round103-queue-receipt.json';f=out.open('x');r={'started_at':now(),'base':BASE,'head':HEAD,'tree':TREE,'commands':[]};json.dump({'state':'in_progress'},f);f.flush()
def run(cmd):
 p=subprocess.run(cmd,cwd=W,capture_output=True,text=True);r['commands'].append({'at':now(),'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr});assert p.returncode==0,(cmd,p.stderr);return p.stdout.strip()
def api(path):return json.loads(run(['gh','api',path]))
def paged(path):return json.loads(run(['gh','api','--paginate','--slurp',path]))
def git(*a):return run(['git',*a])
try:
 c=json.loads((T/'cmm-round103-commit-receipt.json').read_text());pr0=json.loads((T/'cmm-round103-pr-created.json').read_text())['pr'];pre=T/'ROUND103_PREFLIGHT_RECEIPT.json';p=json.loads(pre.read_text());assert p['exit_code']==0 and p['mode']=='preflight' and p['trusted_base']==BASE and p['topic_head']==HEAD and p['expected_tree']==TREE
 assert sha(p['log'])==p['log_sha256'] and sha(p['coverage']['path'])==p['coverage']['sha256'];cv=json.loads(Path(p['coverage']['path']).read_text());assert cv['passed'];cfg=json.loads((T/'cmm-round103-helper-config.json').read_text());assert p['counts']==cfg['counts']
 assert all(x['exit_code'] in x['allowed_exit_codes'] for x in p['commands'])
 for required in [['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',BASE],['just','review-check','--base',BASE,'--require-reviews']]:assert any(x['command']==required and x['exit_code']==0 for x in p['commands'])
 assert any(x['command'][1:]==[str(T/'cmm-round103-isolated-coverage.py'),'--clone',p['clone'],'--output',p['coverage']['path']] and x['exit_code']==0 for x in p['commands'])
 for name,key in [('cmm-round103-helper-config.json','config_sha256'),('cmm-round103-isolated-verification.py','verification_helper_sha256'),('cmm-round103-isolated-coverage.py','coverage_helper_sha256')]:assert sha(T/name)==c[key]
 assert p['config_sha256']==c['config_sha256'] and p['helper_sha256']==c['verification_helper_sha256']
 assert git('rev-parse','HEAD')==HEAD and git('rev-parse','HEAD^{tree}')==TREE and git('branch','--show-current')==BRANCH and not git('status','--porcelain=v1','--untracked-files=all')
 for name,h in c['hashes'].items():assert sha(W/name)==h,name
 pr=api(f'repos/{REPO}/pulls/ROUND103_PR_NUMBER');assert pr['base']['ref']=='main' and pr['head']['ref']==BRANCH and pr['base']['repo']['full_name']==REPO and pr['head']['repo']['full_name']==REPO;assert pr['state']=='open' and not pr['draft'] and pr['head']['sha']==HEAD and pr['base']['sha']==BASE and pr['title']==pr0['title'] and pr['body']==pr0['body']
 files=[x for page in paged(f'repos/{REPO}/pulls/ROUND103_PR_NUMBER/files?per_page=100') for x in page];assert sorted(x['filename'] for x in files)==c['files']
 checks=json.loads(run(['gh','pr','checks','ROUND103_PR_NUMBER','--repo',REPO,'--required','--json','name,state,link']));assert checks and all(x['state']=='SUCCESS' for x in checks) and any(x['name']=='validate-strict' for x in checks)
 rules=api(f'repos/{REPO}/rules/branches/main');mq=[x for x in rules if x['type']=='merge_queue'];assert len(mq)==1 and mq[0]['parameters']['merge_method']=='SQUASH' and mq[0]['parameters']['grouping_strategy']=='ALLGREEN';assert any(x['type']=='required_status_checks' and any(z['context']=='validate-strict' for z in x['parameters']['required_status_checks']) for x in rules)
 posted=json.loads((T/'cmm-round103-posted-review.json').read_text());review=api(f'repos/{REPO}/pulls/ROUND103_PR_NUMBER/reviews/{posted["id"]}');assert review['commit_id']==HEAD and review['state']=='COMMENTED' and review['body']==posted['body']
 comments=[x for page in paged(f'repos/{REPO}/issues/ROUND103_PR_NUMBER/comments?per_page=100') for x in page];inline=[x for page in paged(f'repos/{REPO}/pulls/ROUND103_PR_NUMBER/comments?per_page=100') for x in page];reviews=[x for page in paged(f'repos/{REPO}/pulls/ROUND103_PR_NUMBER/reviews?per_page=100') for x in page];assert not comments and not inline and [x['id'] for x in reviews]==[posted['id']], 'New discussion requires assessment'
 r.update(preflight={'path':str(pre),'sha256':sha(pre),'log_sha256':p['log_sha256'],'coverage_sha256':p['coverage']['sha256']},required_checks=checks,review=review,rules=rules,files=files)
 # Last remote read before queue admission. This is not an atomic base lock.
 main=api(f'repos/{REPO}/git/ref/heads/main');assert main['object']['sha']==BASE;r['live_main_immediately_before_queue']={'observed_at':now(),'ref':main}
 r['queue_output']=run(['gh','pr','merge','ROUND103_PR_NUMBER','--repo',REPO,'--match-head-commit',HEAD]);r['exit_code']=0
except Exception as e:r.update(exit_code=1,error=str(e))
finally:
 r['finished_at']=now();f.seek(0);json.dump(r,f,indent=2);f.write('\n');f.truncate();f.close();print(json.dumps({k:v for k,v in r.items() if k not in ['commands','files','rules','review']},indent=2))
raise SystemExit(r['exit_code'])
