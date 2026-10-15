from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,os,re,subprocess,yaml
p=argparse.ArgumentParser();p.add_argument('--pr',type=int);a=p.parse_args()
T=Path('/private/tmp');W=T/'CMMMech-expansion-round90-20261015';repo='CultureBotAI/CMMMech';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
def run(cmd):return subprocess.check_output(cmd,cwd=W,text=True).strip()
def git(*a):return run(['git',*a])
def api(path):return json.loads(run(['gh','api',path]))
def pages(path):return [x for page in json.loads(run(['gh','api',path+'?per_page=100','--paginate','--slurp'])) for x in page]
def has_reviewed_target(review, record_id, path):
 return record_id in review.get('scope',{}).get('reviewed_target_ids',[]) and any(t.get('target_id')==record_id and t.get('path')==path for t in review.get('targets',[]))
def has_reviewed_history(review, record_id, path, digest):
 if any(i.get('path')==path and i.get('sha256')==digest for i in review.get('source',{}).get('inputs',[])):
  return True
 evidence=review.get('evidence',[])
 ids=[e.get('evidence_id') for e in evidence]
 if len(ids)!=len(set(ids)):
  return False
 return any(e.get('kind')=='record_content' and e.get('reference')==path and e.get('snapshot_sha256')==digest and e.get('support')=='supports' and any(a.get('outcome')=='supported' and record_id in a.get('target_ids',[]) and e.get('evidence_id') in a.get('evidence_ids',[]) for a in review.get('assessments',[])) for e in evidence)
c=json.loads((T/'cmm-round90-commit-receipt.json').read_text());cfg=json.loads((T/'cmm-round90-helper-config.json').read_text());assert c['base']==cfg['base'] and c['branch']==cfg['branch']
assert git('rev-parse','HEAD')==c['head'] and git('rev-parse','HEAD^{tree}')==c['tree'] and git('rev-list','--parents','-n','1','HEAD').split()==[c['head'],c['base']]
assert not git('status','--porcelain=v1','--untracked-files=all')
names=git('diff',c['base'],c['head'],'--name-only').splitlines();assert sorted(names)==sorted(c['files'])
assert all(n=='README.md' or n.startswith(('pages/','research/ingests/round90-','research/sources/round90-','reviews/publication/20261015-round90/','reviews/structured/')) or n in ['data/records/'+s+'.yaml' for s in cfg['slugs']] or any(n.startswith('history/records/'+s+'/') for s in cfg['slugs']) for n in names)
assert {n for n in names if n.startswith('data/records/')}=={'data/records/'+s+'.yaml' for s in cfg['slugs']}
g=json.loads((T/'cmm-round90-final-gates.json').read_text());r=json.loads((T/'cmm-round90-review-check-final.json').read_text());cov=json.loads((T/'cmm-round90-local-coverage.json').read_text());report=json.loads((W/'research/ingests/round90-frontier-20261015.json').read_text())
assert g['base']==c['base'] and g['worktree']==str(W) and g['exit_code']==r['exit_code']==0 and g['inputs_unchanged'] and cov['passed']
for x in [g,r]:assert sha(x['log'])==x['log_sha256']
assert any(x['command']==['just','check'] and x['exit_code']==0 for x in g['commands'])
assert all(x['exit_code']==0 for x in g['commands']) and all(sha(W/n)==h for n,h in g['record_inputs'].items())
assert all(cov[k]==v for k,v in cfg['counts'].items()) and report['counts']==cfg['counts']
assert all(sha(W/x['path'])==x['sha256'] for x in cov['records'])
reviews=[]
for row in report['records']:
 record=yaml.safe_load((W/row['path']).read_text());v=yaml.safe_load((W/row['review']['path']).read_text());assert row['sha256']==sha(W/row['path']) and row['id']==record['id'] and row['history_refs']==record['history_refs']
 assert v['scientific_review'] and v['completion']=='completed' and v['verdict'] in ['pass','pass_with_limitations'] and v['reviewer']['independence']=='independent' and v['source']['git_revision']==c['base']
 assert has_reviewed_target(v,record['id'],row['path'])
 assert all(sha(W/i['path'])==i['sha256'] for i in v['source']['inputs'])
 assert any(i['path']==row['path'] and i['sha256']==row['sha256'] for i in v['source']['inputs'])
 assert all(has_reviewed_history(v,record['id'],h,sha(W/h)) for h in record['history_refs'])
 assert all(x['status']=='passed' for x in v['checks'] if x.get('required'))
 assert all(f['status'] in ['resolved','rejected','accepted_risk'] or f['severity']=='informational' for f in v['findings'])
 assert (W/row['review']['markdown']).is_file();reviews.append({'record':row['path'],'sha256':row['sha256'],'review':row['review']['path'],'reviewer':v['reviewer'],'verdict':v['verdict']})
assert {x['record'] for x in reviews}=={'data/records/'+s+'.yaml' for s in cfg['slugs']}
d={'recorded_at':now(),'passed':True,'scientific_review':False,'scope':'Operational exact-commit audit; primary scientific acceptance is delegated to the separately identified independent reviewers. No new scientific self-acceptance.','audit_helper':{'path':str(Path(__file__)), 'sha256':sha(Path(__file__))},'head':c['head'],'tree':c['tree'],'base':c['base'],'files':[{'path':n,'sha256':sha(W/n)} for n in names],'counts':cfg['counts'],'selected_reviews':reviews,'findings':[],'limits':['Source uncertainties remain open. Branch deletion and actual merged-tree provenance require later checks.']}
if a.pr:
 pr=api(f'repos/{repo}/pulls/{a.pr}');assert pr['state']=='open' and not pr['draft'] and pr['head']['sha']==c['head'] and pr['head']['ref']==c['branch'] and pr['base']['sha']==c['base'] and pr['base']['ref']=='main'
 assert pr['title']==cfg['title'] and pr['body'].strip()==(T/'cmm-round90-pr-body.md').read_text().strip()
 files=pages(f'repos/{repo}/pulls/{a.pr}/files');assert len(files)==pr['changed_files']==len(names) and {x['filename'] for x in files}==set(names)
 assert all(x['status'] in ['added','modified'] and x['sha']==git('rev-parse',c['head']+':'+x['filename']) for x in files)
 conv={k:pages(f'repos/{repo}/'+path) for k,path in {'reviews':f'pulls/{a.pr}/reviews','comments':f'issues/{a.pr}/comments','inline':f'pulls/{a.pr}/comments'}.items()}
 assert not any(x['state']=='CHANGES_REQUESTED' for x in conv['reviews'])
 # Do not silently accept any unassessed hosted conversation.
 assert not any(conv.values()),conv
 query='query($n:Int!){repository(owner:"CultureBotAI",name:"CMMMech"){pullRequest(number:$n){reviewThreads(first:100){nodes{id isResolved} pageInfo{hasNextPage}}}}}'
 threads=json.loads(run(['gh','api','graphql','-f','query='+query,'-F','n='+str(a.pr)]))['data']['repository']['pullRequest']['reviewThreads'];assert not threads['pageInfo']['hasNextPage'] and not threads['nodes'],threads
 conv['threads']=threads['nodes']
 runs=api(f'repos/{repo}/commits/{c["head"]}/check-runs?per_page=100');assert runs['total_count']<=100
 required=[x for x in runs['check_runs'] if x['name']=='validate-strict' and x['app']['id']==15368 and x['head_sha']==c['head']];assert required
 strict=max(required,key=lambda x:x['id']);assert strict['status']=='completed' and strict['conclusion']=='success'
 run_match=re.search(r'/actions/runs/(\d+)',strict['details_url']);assert run_match
 workflow=api(f'repos/{repo}/actions/runs/{run_match.group(1)}');assert workflow['head_sha']==c['head'] and workflow['event']=='pull_request' and workflow['path']=='.github/workflows/validate-strict.yaml' and workflow['status']=='completed' and workflow['conclusion']=='success'
 job_pages=json.loads(run(['gh','api',f'repos/{repo}/actions/runs/{workflow["id"]}/jobs?per_page=100','--paginate','--slurp']));jobs=[j for page in job_pages for j in page['jobs']];assert len(jobs)==job_pages[0]['total_count'] and len({j['id'] for j in jobs})==len(jobs)
 assert any(j['name']=='validate-strict' for j in jobs) and all(j['run_id']==workflow['id'] and j['head_sha']==c['head'] and j['status']=='completed' and j['conclusion']=='success' for j in jobs)
 d.update(required_check_run=strict,workflow_run=workflow,workflow_jobs=jobs)

 checks=json.loads(run(['gh','pr','checks',str(a.pr),'--repo',repo,'--required','--json','name,state,bucket,link']));assert checks and all(x['bucket']=='pass' for x in checks) and any(x['name']=='validate-strict' for x in checks)
 pre=json.loads((T/'cmm-round90-preflight-committed-terminal.json').read_text());assert pre['mode']=='preflight' and pre['exit_code']==0 and pre['trusted_base']==c['base'] and pre['topic_head']==c['head'] and pre['expected_tree']==c['tree'] and pre['counts']==cfg['counts'] and sha(pre['log'])==pre['log_sha256']
 assert api(f'repos/{repo}/git/ref/heads/main')['object']['sha']==c['base']
 d.update(pr=a.pr,url=pr['html_url'],pr_snapshot=pr,hosted_files=files,conversation=conv,required_checks=checks,preflight={'receipt':str(T/'cmm-round90-preflight-committed-terminal.json'),'sha256':sha(T/'cmm-round90-preflight-committed-terminal.json')})
 body='Adversarial publication review of exact head `'+c['head']+'` (tree `'+c['tree']+'`).\n\nVerified every changed file against its hosted blob, exact base/title/body, all paginated reviews/comments, final owner hashes and the four independent scientific reviews. Full local checks and the committed squash-shaped preflight passed; required `validate-strict` passed for this head. Source issues #311 and #314 remain open.\n\nNo unresolved corrective finding remains in the accepted record scope. This COMMENT records the audit; it does not impersonate a separate GitHub approval. Native queue checks, actual merged tree/parent, owned-branch deletion and fresh-main provenance validation remain required.\n'
 (T/'cmm-round90-hosted-review-comment.md').write_text(body)
label='hosted' if a.pr else 'local';out=T/f'cmm-round90-publication-audit-{label}.json';assert not out.exists();out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({'passed':True,'receipt':str(out),'head':c['head'],'files':len(names),'counts':cfg['counts']},indent=2))
