#!/usr/bin/env python3
"""Read-only round86 exact-head PR audit; creates only unique /private/tmp receipts."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import json, hashlib, subprocess, os, re, sys, traceback, yaml
ROOT=Path('/private/tmp'); WT=ROOT/'CMMMech-expansion-round86-20261015'; REPO='CultureBotAI/CMMMech'
BASE='6a579d90978267cf5d145bca05b4c97e5ba4d629'; BRANCH='curate/cmm-expansion-round86-20261015'
ENV=dict(os.environ,GIT_OPTIONAL_LOCKS='0',PYTHONDONTWRITEBYTECODE='1'); responses=[]
def now():return datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def sha(p):return sha_bytes(Path(p).read_bytes())
class Pending(Exception):pass
class Failure(Exception):pass
def need(ok,message):
 if not ok:raise Failure(message)
def execute(command):
 start=now()
 try:
  p=subprocess.run(command,cwd=WT,env=ENV,capture_output=True,text=True,timeout=55)
  return dict(command=command,started_at=start,finished_at=now(),exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)
 except subprocess.TimeoutExpired as e:return dict(command=command,started_at=start,finished_at=now(),exit_code=None,stdout='',stderr='55-second timeout')
def get(command,allowed=(0,)):
 r=execute(command);responses.append(r);need(r['exit_code'] in allowed,'Command failed: '+str(command)+' '+r['stderr']);return r['stdout']
def api(path):return json.loads(get(['gh','api',path]))
def git(*args):return get(['git',*args]).strip()
def validate_file_pages(pages,expected,blob_for_path,changed_count):
 need(isinstance(pages,list) and bool(pages) and all(isinstance(p,list) for p in pages),'PR files response is not a nonempty page list')
 need(all(0 < len(p)<=100 for p in pages) and all(len(p)==100 for p in pages[:-1]),'Incomplete/invalid API file page size')
 files=[f for page in pages for f in page];names=[f.get('filename') for f in files]
 need(all(isinstance(n,str) and n for n in names),'Invalid API file path')
 need(len(names)==len(set(names)),'Duplicate file path across API pages')
 need(len(files)==changed_count==len(expected),'API/PR/receipt file counts disagree')
 need(set(names)==set(expected),'Complete API file path set differs from reviewed package')
 verified=[]
 for f in files:
  name=f['filename'];need(f.get('status') in ('added','modified'),'Unexpected deletion/rename/type in reviewed batch: '+name)
  blob=blob_for_path(name);need(f.get('sha')==blob,'Hosted blob differs from reviewed tree: '+name)
  verified.append(dict(path=name,status=f['status'],api_blob=f['sha'],reviewed_blob=blob))
 return verified

def main():
 stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');prefix=ROOT/('cmm-round86-hosted-peer-'+stamp)
 report=dict(started_at=now(),reviewer='codex /root/round68_new_frontier',scope='Independent operational hosted PR review. Reviewer authored municipal-sewage-sludge; its separate independent scientific review is required and this audit does not reassess their science. Native artifacts identify each scientific reviewer. This audit checks publication identity, complete committed package and hosted validation, and does not claim scientific self-review or human approval. No Git/GitHub mutations; COMMENT draft only.',passed=False,findings=[],helper_sha256=sha(__file__),worktree=str(WT),base=BASE)
 status='failed'
 try:
  paths={k:ROOT/('cmm-round86-'+n) for k,n in {'commit':'commit-receipt.json','opened':'pr-open.json','config':'helper-config.json','body':'pr-body.md'}.items()}
  for p in paths.values():need(p.is_file() and not p.is_symlink(),'Required regular input missing or symlink: '+str(p))
  commit=json.loads(paths['commit'].read_text());opened=json.loads(paths['opened'].read_text());cfg=json.loads(paths['config'].read_text());body=paths['body'].read_text();head=commit['head'];tree=commit['tree'];n=opened['number']
  need(commit['worktree']==str(WT) and commit['base']==BASE and commit['branch']==BRANCH,'Commit receipt scope mismatch')
  need(all(re.fullmatch('[0-9a-f]{40}',s) for s in (head,tree,BASE)) and isinstance(n,int) and n>0,'Invalid commit/tree/PR identifiers')
  need(opened['headRefOid']==head and opened['headRefName']==BRANCH and opened['baseRefName']=='main','Open receipt identity mismatch')
  need(opened['title']==cfg['title'] and opened['body']==body and opened['body_sha256']==sha(paths['body']),'Prepared title/body and open receipt differ byte-for-byte')
  report.update(pr=n,head=head,tree=tree,url=opened['url'],input_provenance={k:dict(path=str(p),sha256=sha(p)) for k,p in paths.items()})
  need(git('rev-parse','HEAD')==head and git('rev-parse','HEAD^{tree}')==tree and git('rev-parse','HEAD^')==BASE and git('rev-list','--parents','-n','1','HEAD').split()==[head,BASE],'Local commit/tree/sole parent differs')
  need(git('branch','--show-current')==BRANCH,'Local branch differs from owned branch')
  need(not git('status','--porcelain=v1','--untracked-files=all'),'Local tracked/nonignored working package is not clean')
  # Git-tracked package identity is independent of ignored caches; ignored files are not claimed absent.
  expected={x['path']:x for x in commit['files']};need(len(expected)==len(commit['files']) and expected,'Duplicate or empty commit receipt file list')
  changed=get(['git','diff','--name-only','-z','--no-renames',BASE,head]).split('\0');changed=[p for p in changed if p]
  need(len(changed)==len(set(changed)) and set(changed)==set(expected),'Independent committed diff differs from complete reviewed file list')
  checked=[]
  for name,item in expected.items():
   p=WT/name;need(p.is_file() and not p.is_symlink() and sha(p)==item['sha256'],'Working file differs from reviewed receipt: '+name)
   b=subprocess.run(['git','show',tree+':'+name],cwd=WT,env=ENV,capture_output=True,timeout=55);need(b.returncode==0 and sha_bytes(b.stdout)==item['sha256'],'Committed blob content differs from receipt: '+name)
   checked.append(dict(path=name,sha256=item['sha256'],blob=git('rev-parse',tree+':'+name)))
  audit=WT/commit['publication_audit'];need(sha(audit)==commit['publication_audit_sha256'],'Publication audit hash differs')
  a=json.loads(audit.read_text());need(a['passed'] is True and type(a.get('unresolved_corrective_findings')) is int and a['unresolved_corrective_findings']==0,'Publication audit is not a resolved pass')
  report['local_package']=dict(files=checked,publication_audit=str(audit),publication_audit_sha256=sha(audit),clean_scope='Tracked and nonignored untracked paths; ignored caches are not claimed absent.')
  globals()['body_for_review']=body
  review_package(globals(), report, commit, cfg, expected, audit, a)
  queries={
   'pr':['gh','api',f'repos/{REPO}/pulls/{n}'],
   'commit':['gh','api',f'repos/{REPO}/git/commits/{head}'],
   'files':['gh','api',f'repos/{REPO}/pulls/{n}/files?per_page=100','--paginate','--slurp'],
   'checks':['gh','pr','checks',str(n),'--repo',REPO,'--required','--json','name,state,bucket,link'],
   'workflow':['gh','api',f'repos/{REPO}/actions/workflows/validate-strict.yaml'],
   'main':['gh','api',f'repos/{REPO}/git/ref/heads/main']}
  with ThreadPoolExecutor(max_workers=4) as pool:rr=list(pool.map(execute,queries.values()))
  responses.extend(rr);data={}
  for key,r in zip(queries,rr):
   if key=='checks' and r['exit_code']==1 and 'no checks reported' in (r['stdout']+r['stderr']).lower():raise Pending('Required checks have not appeared')
   need(r['exit_code'] in ((0,8) if key=='checks' else (0,)),'Hosted read failed: '+key+' '+r['stderr']);data[key]=json.loads(r['stdout'])
  pr=data['pr'];obj=data['commit'];workflow=data['workflow'];checks=data['checks']
  def pr_identity(v):
   need(v['number']==n and v['state']=='open' and not v['draft'] and v['html_url']==opened['url'],'Live PR identity/state differs')
   need(v['head']['sha']==head and v['head']['ref']==BRANCH and v['head']['repo']['full_name']==REPO,'Live PR head differs')
   need(v['base']['sha']==BASE and v['base']['ref']=='main' and v['base']['repo']['full_name']==REPO,'Live PR base differs')
   need(v['title']==cfg['title'] and v['body']==body,'Live title/body differ from exact prepared text')
  pr_identity(pr)
  need(obj['sha']==head and obj['tree']['sha']==tree and [x['sha'] for x in obj['parents']]==[BASE],'Hosted commit/tree/parent differs')
  need(data['main']['object']['sha']==BASE,'Remote main moved from reviewed base')
  verified=validate_file_pages(data['files'],expected,lambda p:git('rev-parse',tree+':'+p),pr['changed_files'])
  report.update(file_count=len(verified),file_page_lengths=[len(p) for p in data['files']],verified_hosted_files=verified,publication_text=dict(title=pr['title'],body_sha256=sha_bytes(pr['body'].encode()),exact_match=True),required_checks=checks)
  need(isinstance(checks,list) and checks,'No required-check response')
  need(all(c['bucket'] in ('pass','pending') for c in checks),'A required check failed, skipped, or was cancelled')
  selected=[c for c in checks if c['name']=='validate-strict'];need(len(selected)==1,'Required validate-strict check is not unique')
  if any(c['bucket']=='pending' for c in checks):raise Pending('Required exact-head checks are still pending')
  link=selected[0]['link'];match=re.search(r'/actions/runs/(\d+)(?:/job/(\d+))?',link);need(match is not None,'Required check lacks identifiable Actions run')
  runid=int(match.group(1));run=api(f'repos/{REPO}/actions/runs/{runid}')
  need(workflow['path']=='.github/workflows/validate-strict.yaml' and workflow['name']=='Validate strictly' and workflow['state']=='active','Workflow identity differs')
  need(run['id']==runid and run['workflow_id']==workflow['id'] and run['path']==workflow['path'] and run['name']==workflow['name'],'Required check run workflow identity differs')
  need(run['head_sha']==head and run['head_branch']==BRANCH and run['event']=='pull_request' and run['repository']['full_name']==REPO,'Required CI head/branch/event/repository differs')
  if run['status']!='completed':raise Pending('Required workflow is not completed')
  need(run['conclusion']=='success','Required workflow completed without success')
  jobs_pages=json.loads(get(['gh','api',f'repos/{REPO}/actions/runs/{runid}/jobs?per_page=100','--paginate','--slurp']))
  jobs=[j for page in jobs_pages for j in page['jobs']];need(jobs and len({j['id'] for j in jobs})==len(jobs),'Missing or duplicated run jobs')
  need(all(j['status']=='completed' and j['conclusion']=='success' for j in jobs),'Required run contains a non-success job')
  strict=[j for j in jobs if j['name']=='validate-strict'];need(len(strict)==1,'Required run lacks unique validate-strict job')
  if match.group(2):need(strict[0]['id']==int(match.group(2)),'Required check link points to a different job')
  report['required_ci']=dict(run_id=runid,url=run['html_url'],workflow_id=workflow['id'],workflow_path=workflow['path'],head=head,event=run['event'],status=run['status'],conclusion=run['conclusion'],jobs=[{k:j[k] for k in ['id','name','status','conclusion','html_url']} for j in jobs])
  review_inventory(globals(), report, n)
  verify_preflight(globals(), report, head, tree, cfg)
  closing=api(f'repos/{REPO}/pulls/{n}');pr_identity(closing);need(api(f'repos/{REPO}/git/ref/heads/main')['object']['sha']==BASE,'Remote main moved during audit')
  need(git('rev-parse','HEAD')==head and git('rev-parse','HEAD^{tree}')==tree and not git('status','--porcelain=v1','--untracked-files=all'),'Local package changed during audit')
  report['closing_identity_check']=dict(at=now(),head=closing['head']['sha'],base=closing['base']['sha'],limitation='Read observations are not an atomic lock against later changes.')
  report.update(passed=True,verdict='pass_with_limitations');status='passed'
 except Pending as e:report.update(verdict='pending',pending_reason=str(e));status='pending'
 except Exception as e:report.update(verdict='failed');report['findings'].append(str(e));report['failure_type']=type(e).__name__;status='failed'
 report['finished_at']=now();response_path=Path(str(prefix)+'-responses.json');response_path.write_text(json.dumps(responses,indent=2)+'\n');report['responses']=dict(path=str(response_path),sha256=sha(response_path),count=len(responses));receipt=Path(str(prefix)+'.json')
 with receipt.open('x') as f:f.write(json.dumps(report,indent=2)+'\n')
 draft=Path(str(prefix)+'.md')
 with draft.open('x') as f:
  if report['passed']:
   f.write('Independent operational review of `'+report['head']+'` (tree `'+report['tree']+'`): qualified pass.\n\nChecked the clean committed package, exact PR head/base/title/body, and all '+str(report['file_count'])+' unique changed paths across API pages '+str(report['file_page_lengths'])+'. Every hosted file blob matches the reviewed tree. The final audit, batch manifest, native scientific review hashes, the exact current five independent native scientific acceptances and current issue dispositions, complete review/comment/thread inventory and actual squash-shaped preflight were also verified. Required `validate-strict` run ['+str(report['required_ci']['run_id'])+']('+report['required_ci']['url']+') completed successfully for this exact PR head and workflow.\n\nScientific review remains in the separately saved native artifacts, with qualified source and experimental limitations retained there. I authored municipal-sewage-sludge, whose independent assessment is retained in separate native scientific review artifacts; this operational check does not claim independent scientific review of my own record. No Git/GitHub changes were made by this reviewer. This is a COMMENT review, not an approval.\n\nNative queue/merge and fresh postmerge checks remain the coordinator’s next steps. This read-only observation cannot prevent later branch or metadata changes.\n')
  else:f.write('Operational audit '+status+': '+report.get('pending_reason','; '.join(report['findings']))+'\n\nDo not post this as acceptance.\n')
 if report['passed']:
  final_draft=ROOT/'cmm-round86-hosted-review.md'
  need(not final_draft.exists(),'Proposed hosted review already exists; preserve it and inspect rather than overwrite')
  with final_draft.open('x') as f:f.write(draft.read_text())
 print(json.dumps(dict(passed=report['passed'],verdict=report['verdict'],receipt=str(receipt),receipt_sha256=sha(receipt),draft=str(draft),draft_sha256=sha(draft),findings=report['findings'],pending_reason=report.get('pending_reason')),indent=2));return {'passed':0,'pending':3,'failed':1}[status]
from cmm_round86_peer_checks import review_package, verify_preflight, review_inventory
if __name__=='__main__':raise SystemExit(main())
