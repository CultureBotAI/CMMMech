from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlencode
import argparse,hashlib,json,re,subprocess

parser=argparse.ArgumentParser()
parser.add_argument('--merge-sha',required=True)
parser.add_argument('--queue-sha',required=True)
parser.add_argument('--output',required=True)
args=parser.parse_args()
assert re.fullmatch('[0-9a-f]{40}',args.merge_sha)
assert re.fullmatch('[0-9a-f]{40}',args.queue_sha)
out=Path(args.output);out.mkdir(parents=True,exist_ok=False)
repo='repos/CultureBotAI/CMMMech'
topic='ROUND102_TOPIC_HEAD'
now=lambda:datetime.now(timezone.utc).isoformat()
rows=[]
def api(name,endpoint=None,command=None,paginate=False):
    cmd=command or ['gh','api',endpoint]+(['--paginate','--slurp'] if paginate else [])
    start=now();p=subprocess.run(cmd,capture_output=True,text=True)
    f=out/(name+'.json');assert not f.exists();f.write_text(p.stdout)
    (out/(name+'.stderr')).write_text(p.stderr)
    row=dict(name=name,command=cmd,started_at=start,finished_at=now(),exit_code=p.returncode,output=str(f),sha256=hashlib.sha256(p.stdout.encode()).hexdigest(),stderr=p.stderr)
    rows.append(row)
    if p.returncode:raise RuntimeError(row)
    return json.loads(p.stdout)
started=now()
pr=api('pr',repo+'/pulls/ROUND102_PR_NUMBER')
assert pr['merged'] and pr['merge_commit_sha']==args.merge_sha and pr['head']['sha']==topic
merge=api('merge-commit',repo+'/git/commits/'+args.merge_sha)
queue=api('queue-commit',repo+'/git/commits/'+args.queue_sha)
assert merge['tree']['sha']=='ROUND102_TOPIC_TREE'
assert queue['tree']['sha']==merge['tree']['sha']
assert [p['sha'] for p in merge['parents']]==['1c2a3bb043c4bd267a3d911d0e77b029c742689e']
ancestry=api('queue-base-ancestry',repo+'/compare/1c2a3bb043c4bd267a3d911d0e77b029c742689e...'+args.queue_sha)
assert ancestry['merge_base_commit']['sha']=='1c2a3bb043c4bd267a3d911d0e77b029c742689e' and ancestry['status']=='ahead'
specs=[('pr-strict','validate-strict.yaml','pull_request',topic),('queue-strict','validate-strict.yaml','merge_group',args.queue_sha),('main-strict','validate-strict.yaml','push',args.merge_sha),('merge-integrity','verify-merge-integrity.yaml','push',args.merge_sha),('pages','pages.yaml','push',args.merge_sha)]
evaluated=[]
def workflow(spec):
    label,path,event,sha=spec
    pages=api(label+'-runs',repo+'/actions/workflows/'+path+'/runs?'+urlencode(dict(head_sha=sha,event=event,per_page=100)),paginate=True)
    runs=[r for p in pages for r in p['workflow_runs']]
    assert runs and all(r['head_sha']==sha and r['event']==event for r in runs),(label,runs)
    selected=max(runs,key=lambda r:(r['created_at'],r['run_number'],r['id']))
    run=api(label+'-latest-run',repo+'/actions/runs/'+str(selected['id']))
    attempt=run['run_attempt'];rid=run['id']
    assert run['head_sha']==sha and run['event']==event and run['path']=='.github/workflows/'+path
    attempt_meta=api(label+'-attempt',repo+f'/actions/runs/{rid}/attempts/{attempt}')
    assert attempt_meta['run_attempt']==attempt and attempt_meta['head_sha']==sha
    jobpages=api(label+'-attempt-jobs',repo+f'/actions/runs/{rid}/attempts/{attempt}/jobs?per_page=100',paginate=True)
    jobs=[j for p in jobpages for j in p['jobs']]
    assert jobs and len(jobs)==jobpages[0]['total_count']
    annotations=[];checkrows=[]
    for job in jobs:
        assert job['run_id']==rid and job['head_sha']==sha
        cid=job['check_run_url'].rsplit('/',1)[1]
        check=api(label+'-check-'+cid,repo+'/check-runs/'+cid)
        assert check['head_sha']==sha
        apages=api(label+'-check-'+cid+'-annotations',repo+'/check-runs/'+cid+'/annotations?per_page=100',paginate=True)
        ar=[a for p in apages for a in p]
        assert len(ar)==check['output']['annotations_count']
        annotations.extend(ar)
        checkrows.append(dict(id=check['id'],name=check['name'],status=check['status'],conclusion=check['conclusion'],annotations_count=len(ar),html_url=check['html_url']))
    final=api(label+'-latest-run-recheck',repo+'/actions/runs/'+str(rid))
    fresh_pages=api(label+'-runs-final',repo+'/actions/workflows/'+path+'/runs?'+urlencode(dict(head_sha=sha,event=event,per_page=100)),paginate=True)
    fresh_runs=[r for p in fresh_pages for r in p['workflow_runs']]
    assert fresh_runs and all(r['head_sha']==sha and r['event']==event for r in fresh_runs)
    newest=max(fresh_runs,key=lambda r:(r['created_at'],r['run_number'],r['id']))
    stable=final['run_attempt']==attempt and newest['id']==rid and newest['run_attempt']==attempt
    passed=stable and run['status']=='completed' and run['conclusion']=='success' and attempt_meta['status']=='completed' and attempt_meta['conclusion']=='success' and all(j['status']=='completed' and j['conclusion']=='success' for j in jobs)
    return dict(label=label,workflow=path,event=event,head_sha=sha,run_id=rid,run_number=run['run_number'],run_attempt=attempt,latest_attempt_stable=stable,html_url=run['html_url'],status=run['status'],conclusion=run['conclusion'],completed_at=run.get('updated_at'),attempt_status=attempt_meta['status'],attempt_conclusion=attempt_meta['conclusion'],jobs=[{k:j[k] for k in ['id','name','status','conclusion','started_at','completed_at','head_sha','run_id','html_url']} for j in jobs],checks=checkrows,annotations=annotations,passed=passed)
with ThreadPoolExecutor(max_workers=3) as pool:evaluated=list(pool.map(workflow,specs))
thread_query='''query($endCursor: String) { repository(owner:"CultureBotAI",name:"CMMMech") { pullRequest(number:ROUND102_PR_NUMBER) { number headRefOid baseRefOid merged mergeCommit { oid } reviewThreads(first:100,after:$endCursor) { pageInfo { hasNextPage endCursor } nodes { id isResolved isOutdated path line comments(first:100) { pageInfo { hasNextPage endCursor } nodes { id databaseId body url createdAt updatedAt author { login } commit { oid } originalCommit { oid } } } } } } } }'''
surface_specs=[('issue-comments',repo+'/issues/ROUND102_PR_NUMBER/comments?per_page=100'),('reviews',repo+'/pulls/ROUND102_PR_NUMBER/reviews?per_page=100'),('inline-comments',repo+'/pulls/ROUND102_PR_NUMBER/comments?per_page=100'),('pr-events',repo+'/issues/ROUND102_PR_NUMBER/events?per_page=100')]
def surface(spec):return api(spec[0],spec[1],paginate=True)
with ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(surface,surface_specs))
threads=api('review-threads',command=['gh','api','graphql','-f','query='+thread_query,'--paginate','--slurp'])
assert not threads[-1]['data']['repository']['pullRequest']['reviewThreads']['pageInfo']['hasNextPage']
assert all(not t['comments']['pageInfo']['hasNextPage'] for p in threads for t in p['data']['repository']['pullRequest']['reviewThreads']['nodes'])
def issue(n):
    data=api(f'issue-{n}',repo+f'/issues/{n}')
    api(f'issue-{n}-comments',repo+f'/issues/{n}/comments?per_page=100',paginate=True)
    api(f'issue-{n}-events',repo+f'/issues/{n}/events?per_page=100',paginate=True)
    return dict(number=n,state=data['state'],closed_at=data['closed_at'],comments=data['comments'])
with ThreadPoolExecutor(max_workers=4) as pool:issues=list(pool.map(issue,[186,375,376,377,378,379,380,381,382,383]))
final_pr=api('pr-final',repo+'/pulls/ROUND102_PR_NUMBER')
assert final_pr['merged'] and final_pr['merge_commit_sha']==args.merge_sha and final_pr['head']['sha']==topic
receipt=dict(started_at=started,finished_at=now(),read_only=True,topic_head=topic,queue_head=args.queue_sha,merge_sha=args.merge_sha,tree=merge['tree']['sha'],all_five_latest_attempts_successful=all(r['passed'] for r in evaluated),runs=evaluated,issues=issues,queries=sorted(rows,key=lambda x:x['name']))
(out/'acquisition-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='queries'},indent=2))
