"""Read-only operational closeout. Execute only after coordinator's complete handoff."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, os, runpy, subprocess

P=Path('/private/tmp')
W=P/'CMMMech-expansion-round87-20261015'
BASE='9deef8843b7efcf2dd2586c2a13f47b72231e336'
BRANCH='curate/cmm-expansion-round87-20261015'
REPO='CultureBotAI/CMMMech'
COUNT_KEYS={'record_count','history_count','structured_review_count','review_base_count','covered_records'}
SLUGS={'alabandite','simonkolleite','secondary-aluminium-dross'}
EXPECTED_ISSUES={298:'closed',299:'open',300:'open'}
ENV=dict(os.environ,GIT_OPTIONAL_LOCKS='0',PYTHONDONTWRITEBYTECODE='1')
now=lambda:datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def need(test,message):
 if not test:raise AssertionError(message)
def run(args,allowed=(0,)):
 r=subprocess.run(args,capture_output=True,text=True,env=ENV,timeout=55)
 need(r.returncode in allowed,(args,r.returncode,r.stderr));return r
def git(root,*args):return run(['git','-c','core.fsmonitor=false','-c','gc.auto=0','-c','maintenance.auto=false','-c','core.hooksPath=/dev/null','-C',str(root),*args]).stdout.strip()
def api(path):return json.loads(run(['gh','api',path]).stdout)

def main():
 started=now();bindings=[]
 def bind(p):
  p=Path(p);need(p.is_file() and not p.is_symlink(),'Missing or unsafe receipt '+str(p));bindings.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size});return p
 def load(name):return json.loads(bind(P/f'cmm-round87-{name}.json').read_text())
 prep=load('independent-closeout-preparation')
 for f in prep['helpers']:
  need(sha(f['path'])==f['sha256'],'Prepared helper changed '+f['path']);bind(f['path'])
 c,cl,post,hosted,after,opened,cfg=[load(n) for n in ['commit-receipt','pr-cleanup','postmerge-merged-terminal','hosted-audit-final','main-preservation-after','pr-open','helper-config']]
 head,tree,merge,pr=c['head'],c['tree'],cl['merge'],cl['pr']
 COUNTS=dict(cfg['counts'])
 need(set(COUNTS)==COUNT_KEYS and all(type(v) is int and v>0 for v in COUNTS.values()) and COUNTS['covered_records']==COUNTS['record_count'],'Final measured count configuration incomplete')
 need(set(cfg['slugs'])==SLUGS and len(cfg['slugs'])==3,'Wrong finalized three-owner cohort')
 need(c['base']==BASE and c['branch']==BRANCH and c['worktree']==str(W),'Wrong committed cohort')
 need(cfg['base']==BASE and cfg['branch']==BRANCH and cfg['counts']==COUNTS and cfg['issues']=={'corrected_review_issues':[298],'closed_source_issues':[],'open_source_issues':[299,300]},'Configuration mismatch')
 need(opened['number']==pr and opened['headRefOid']==head and opened['headRefName']==BRANCH and opened['baseRefName']=='main','Open receipt mismatch')
 need(cl['head']==head and cl['tree']==tree and cl['branch']==BRANCH and cl['worktree']==str(W) and all(cl[k] is True for k in ['local_branch_absent','remote_branch_absent','clean_detached_worktree']),'Cleanup receipt mismatch')
 for f in c['files']:need(sha(W/f['path'])==f['sha256'],'Committed file changed '+f['path'])
 finalaudit=bind(W/c['publication_audit']);need(sha(finalaudit)==c['publication_audit_sha256'] and json.loads(finalaudit.read_text())['passed'] is True,'Publication audit binding mismatch')
 need(git(W,'rev-parse','HEAD')==merge and git(W,'rev-parse','HEAD^{tree}')==tree and git(W,'rev-list','--parents','-n','1','HEAD').split()==[merge,BASE],'Retained merge identity or sole parent mismatch')
 need(not git(W,'branch','--show-current') and not git(W,'status','--porcelain=v1','--untracked-files=all'),'Retained worktree not clean detached')
 need(run(['git','-C',str(W),'show-ref','--verify','--quiet','refs/heads/'+BRANCH],(0,1)).returncode==1,'Local topic ref remains')
 need(run(['git','-C',str(W),'ls-remote','--exit-code','origin','refs/heads/'+BRANCH],(0,2)).returncode==2,'Remote topic ref remains')
 need(post['exit_code']==0 and post['mode']=='postmerge' and post['trusted_base']==BASE and post['topic_head']==head and post['expected_tree']==tree and post['merge_commit']==merge and post['counts']==COUNTS,'Fresh postmerge receipt mismatch')
 need(all(x['exit_code'] in x['allowed_exit_codes'] for x in post['commands']),'Postmerge command failed')
 need(len(post['topic_object_checks'])==3 and all(x['absent'] is True and x['exit_code']!=0 for x in post['topic_object_checks']),'Topic absence checks incomplete')
 log=bind(post['log']);need(sha(log)==post['log_sha256'],'Postmerge log hash mismatch');text=log.read_text()
 for expected in ['317 passed, 3 skipped',f"Checked {COUNTS['record_count']} record(s); 0 failed.",f"Checked {COUNTS['history_count']} history record(s); 0 error(s).",f'"valid_reviews": {COUNTS["structured_review_count"]}']:need(expected in text,'Postmerge census absent '+expected)
 required=[['just','check'],['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',BASE],['just','review-check','--base',BASE,'--require-reviews']]
 succeeded=[x['command'] for x in post['commands'] if x['exit_code']==0]
 for command in required:need(command in succeeded,'Missing actual required command '+repr(command))
 covp=bind(post['coverage_receipt']);cov=json.loads(covp.read_text());need(cov['passed'] is True and {k:cov[k] for k in COUNTS}==COUNTS,'Postmerge exact coverage mismatch')
 clone=Path(post['clone']);need(git(clone,'rev-parse','HEAD')==merge and git(clone,'rev-parse','HEAD^{tree}')==tree and git(clone,'rev-list','--parents','-n','1','HEAD').split()==[merge,BASE] and not git(clone,'status','--porcelain=v1','--untracked-files=all'),'Fresh clone state changed')
 need(run(['git','-C',str(clone),'cat-file','-e',head+'^{commit}'],(0,1,128)).returncode!=0,'Deleted topic object present in isolated clone')
 need(hosted['passed'] is True and hosted['findings']==[] and hosted['all_five_hosted_runs_and_jobs_succeeded'] is True and hosted['pr']==pr and hosted['topic']==head and hosted['tree']==tree and hosted['base']==BASE and hosted['merge']==merge,'Hosted audit mismatch')
 roles={'required_pr':('Validate strictly',head,'pull_request',BRANCH,'validate-strict'),'merge_group':('Validate strictly',merge,'merge_group',None,'validate-strict'),'main_validation':('Validate strictly',merge,'push','main','validate-strict'),'main_integrity':('Verify merge integrity',merge,'push','main','merge-integrity'),'pages_deployment':('Deploy GitHub Pages',merge,'push','main','deploy')}
 need(set(hosted['runs'])==set(roles) and len({r['databaseId'] for r in hosted['runs'].values()})==5,'Wrong hosted run set')
 for role,r in hosted['runs'].items():
  name,h,event,branch,job=roles[role]
  need(r['workflowName']==name and r['headSha']==h and r['event']==event and (r['headBranch']==branch if branch else r['headBranch'].startswith('gh-readonly-queue/main/')) and r['status']=='completed' and r['conclusion']=='success' and r['jobs'] and all(j['status']=='completed' and j['conclusion']=='success' for j in r['jobs']) and any(j['name']==job for j in r['jobs']),'Hosted receipt run or jobs mismatch '+role)
 need(all(after[k] is True for k in ['passed','main_clean','main_nontracked_preserved','unrelated_skill_preserved','retained_tag_preserved']) and after['head']==merge and after['tree']==tree and after['topic_head']==head and after['base']==BASE and after['preserved_entry_counts']=={'main':7187,'skill':7389},'Original main synchronization mismatch')
 beforep=bind(after['before_receipt']);need(sha(beforep)==after['before_sha256'],'Preservation-before changed');before=json.loads(beforep.read_text());initial=load('preservation-before')
 need(sha(P/'cmm-round87-preservation-before.json')==before['initial_snapshot_sha256'] and initial['snapshots']==before['snapshots'] and initial['retained_tag']==before['retained_tag'],'Preservation does not match initialization')
 need(sha(P/'cmm-round87-sync-main.py')==before['helper_sha256'],'Sync helper changed')
 lib=runpy.run_path(str(P/'cmm-round57-recover-original.py'),run_name='snapshot_library')
 mainstate=lib['snapshot'](Path(after['main']),False);skillstate=lib['snapshot'](Path(after['skill']),True)
 need(mainstate['head']==merge and mainstate['tree']==tree and mainstate['branch']=='main' and not mainstate['status'] and mainstate['files']==before['snapshots']['main']['files'] and skillstate==before['snapshots']['skill'] and lib['retained_tag']()==before['retained_tag'],'Fresh hidden/ignored preservation failed')
 need(len(mainstate['files'])==7187 and len(skillstate['files'])==7389,'Preservation count differs')
 remote={s.split()[1]:s.split()[0] for s in git(W,'ls-remote','origin','refs/heads/main',lib['TAG'],lib['TAG']+'^{}').splitlines()}
 need(remote=={'refs/heads/main':merge,lib['TAG']:lib['TAG_OBJECT'],lib['TAG']+'^{}':lib['TAG_COMMIT']},'Remote main or retained tag differs')
 queries={'pr':f'repos/{REPO}/pulls/{pr}','merge':f'repos/{REPO}/git/commits/{merge}','main':f'repos/{REPO}/git/ref/heads/main'}
 queries.update({str(n):f'repos/{REPO}/issues/{n}' for n in EXPECTED_ISSUES})
 queries.update({role:f'repos/{REPO}/actions/runs/{r["databaseId"]}' for role,r in hosted['runs'].items()})
 with ThreadPoolExecutor(max_workers=4) as ex:live=dict(zip(queries,ex.map(api,queries.values())))
 need(live['pr']['state']=='closed' and live['pr']['merged'] is True and live['pr']['head']['sha']==head and live['pr']['merge_commit_sha']==merge and live['pr']['base']['ref']=='main' and live['pr']['title']==opened['title'] and live['pr']['body'].rstrip()==opened['body'].rstrip(),'Live merged PR differs')
 need(live['merge']['tree']['sha']==tree and [p['sha'] for p in live['merge']['parents']]==[BASE] and live['main']['object']['sha']==merge,'Live squash identity mismatch')
 for n,state in EXPECTED_ISSUES.items():need(live[str(n)]['number']==n and live[str(n)]['state']==state and 'pull_request' not in live[str(n)],'Live issue state differs '+str(n))
 def jobs(role):
  r=hosted['runs'][role];pages=json.loads(run(['gh','api',f'repos/{REPO}/actions/runs/{r["databaseId"]}/jobs?per_page=100&filter=latest','--paginate','--slurp']).stdout);rows=[j for p in pages for j in p['jobs']];need(rows and len(rows)==len({j['id'] for j in rows}) and all(p['total_count']==len(rows) for p in pages),'Incomplete job pagination '+role);return rows
 with ThreadPoolExecutor(max_workers=4) as ex:livejobs=dict(zip(roles,ex.map(jobs,roles)))
 for role,r in hosted['runs'].items():
  name,h,event,branch,job=roles[role];v=live[role];js=livejobs[role]
  need(v['id']==r['databaseId'] and v['repository']['full_name']==REPO and v['name']==name and v['head_sha']==h and v['event']==event and v['head_branch']==r['headBranch'] and v['status']=='completed' and v['conclusion']=='success','Live run differs '+role)
  need(all(j['status']=='completed' and j['conclusion']=='success' for j in js) and any(j['name']==job for j in js) and {j['id'] for j in js}=={j['databaseId'] for j in r['jobs']},'Live job set differs '+role)
 need(all(sha(x['path'])==x['sha256'] for x in bindings),'Bound inputs changed during audit')
 finished=now();out={'started_at':started,'finished_at':finished,'reviewer':'codex /root/round68_iron_sulfides','authorship':'Authored alabandite, independently reviewed by phosphates; independently reviewed secondary aluminium dross and the HP1 operational status-guard correction. This is a read-only operational closeout, not self-acceptance of scientific authorship.','helper_sha256':sha(__file__),'passed':True,'verdict':'pass_with_limitations','findings':[],'pr':pr,'head':head,'tree':tree,'base':BASE,'merge':merge,'counts':COUNTS,'inputs':bindings,'live':live,'live_jobs':livejobs,'preserved_entry_counts':after['preserved_entry_counts'],'retained_tag':before['retained_tag'],'branch_absent_local_and_remote':True,'retained_worktree_clean_detached':True,'topic_absent_in_postmerge_clone':True,'all_five_hosted_runs_and_jobs_succeeded':True,'issue_states':EXPECTED_ISSUES,'limitations':['Observations are not atomic against subsequent external changes.','Fresh original-main/skill preservation includes hidden/ignored bytes, modes and symlink targets; Git administration and external symlink target contents are excluded.','No test rerun or Git/GitHub mutation was performed; actual completed fresh-clone receipts/logs and live hosted jobs were independently checked.','Source issues299–300 remain open; publication does not resolve those documented evidence gaps. No byte-preservation claim is made for every other historical worktree.']}
 stem=P/('cmm-round87-independent-closeout-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
 with stem.with_suffix('.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
 with stem.with_suffix('.md').open('x') as f:f.write(f'# Round87 independent closeout\n\nPass with limitations. Actual audit {started} to {finished}.\n\n[PR #{pr}](https://github.com/{REPO}/pull/{pr}) is merged as `{merge}`, with exact reviewed tree `{tree}` and sole parent `{BASE}`. Both topic branch refs are absent; the retained worktree is clean and detached. Fresh remote-main validation verifies{COUNTS["record_count"]} records, {COUNTS["history_count"]} histories, {COUNTS["structured_review_count"]} reviews, {COUNTS["review_base_count"]} review bases and {COUNTS["covered_records"]} covered records, with the deleted topic absent. All five exact hosted runs and their complete paginated job lists succeeded.\n\nOperational issue #298 is closed; source issues #299–300 remain open. Original main is clean at the merge. Independent hidden/ignored-inclusive recomputation preserves7187 main nontracked entries,7389 unrelated skill entries and the retained provenance tag.\n\nReviewer authored alabandite, whose scientific acceptance was independently supplied by phosphates, and independently reviewed secondary aluminium dross plus the HP1 operational correction. This operational audit makes no new scientific claim. No Git/GitHub mutation or full test rerun occurred. Observations are time-bounded; preservation excludes Git administration and external symlink targets.\n')
 print(json.dumps({'passed':True,'json':str(stem.with_suffix('.json')),'markdown':str(stem.with_suffix('.md')),'sha256':sha(stem.with_suffix('.json'))}))

if __name__=='__main__':main()
