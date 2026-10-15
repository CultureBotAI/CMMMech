"""Retain completed publication evidence after actual merge, deletion and fresh-main checks."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,shutil,stat,subprocess,sys
T=Path('/private/tmp');W=T/'CMMMech-expansion-round93-20261015';MAIN=Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CMMMech')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(n):return json.loads((T/f'cmm-round93-{n}.json').read_text())
def git(root,*a):return subprocess.check_output(['git','-C',str(root),*a],text=True).strip()
def boundgate(d):
 assert d['exit_code']==0 and sha(d['log'])==d['log_sha256']
 if 'commands' in d:assert d['commands'] and all(x['exit_code'] in x.get('allowed_exit_codes',[0]) for x in d['commands'])
c=load('commit-receipt');cfg=load('helper-config');pr=load('publish-receipt');clean=load('pr-cleanup');track=load('tracking-cleanup');sync=load('main-sync');post=load('postmerge-published-terminal');pre=load('preflight-committed-terminal');hosted=load('hosted-audit-final');posted=load('posted-review');peerpath=Path(posted['peer_receipt']);peer=json.loads(peerpath.read_text());before=load('preservation-before')
for x in ['baseline','final-gates','review-check-final']:boundgate(load(x))
for d,mode in [(pre,'preflight'),(post,'postmerge')]:
 boundgate(d);assert d['mode']==mode and d['trusted_base']==c['base'] and d['topic_head']==c['head'] and d['expected_tree']==c['tree'] and d['counts']==cfg['counts']
 for cmd in [['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',c['base']],['just','review-check','--base',c['base'],'--require-reviews']]:assert any(x['command']==cmd and x['exit_code']==0 for x in d['commands'])
 assert d['topic_object_checks'] and all(x['absent'] for x in d['topic_object_checks']) and d['verified_retained_tag']['remote_verified']
 cv=json.loads(Path(d['coverage_receipt']).read_text());assert cv['passed'] and all(cv[k]==v for k,v in cfg['counts'].items())
merge=clean['merge'];n=pr['pr']['number'];assert clean['local_branch_absent'] and clean['remote_branch_absent'] and track['absent'] and sync['passed'] and sync['main_clean']
assert all(clean[k]==c[k] for k in ['base','head','tree']) and sync['merge']==post['merge_commit']==merge and sync['tree']==c['tree']
assert hosted['passed'] and hosted['all_five_hosted_runs_and_jobs_succeeded'] and hosted['pr']==n and hosted['merge']==merge and all(hosted[k]==c[k] for k in ['base','head','tree']) and len(hosted['runs'])==5 and not hosted['findings'] and not hosted['pending']
for r in hosted['runs'].values():assert r['status']=='completed' and r['conclusion']=='success' and r['jobs'] and all(j['status']=='completed' and j['conclusion']=='success' for j in r['jobs'])
assert peer['passed'] and sha(peerpath)==posted['peer_sha256'] and all(peer[k]==c[k] for k in ['base','head','tree'])
draft=peer['comment_draft'];assert sha(draft['path'])==draft['sha256']==posted['body_sha256'] and posted['review']['body']==Path(draft['path']).read_text() and posted['review']['commit_id']==c['head'] and posted['review']['state']=='COMMENTED'
issues=load('issue-ledger');corrected=load('corrective-issue-ledger');assert hosted['issue_states']=={str(x['number']):x['state'].lower() for x in issues+corrected}
assert git(MAIN,'rev-parse','HEAD')==merge and git(MAIN,'rev-parse','HEAD^{tree}')==c['tree'] and git(MAIN,'branch','--show-current')=='main' and not git(MAIN,'status','--porcelain=v1','--untracked-files=all')
assert git(MAIN,'ls-remote','origin','refs/heads/main').split()==[merge,'refs/heads/main'] and not git(MAIN,'ls-remote','origin','refs/heads/'+c['branch'])
assert subprocess.run(['git','-C',str(MAIN),'show-ref','--verify','--quiet','refs/heads/'+c['branch']]).returncode==1
for name,b in before['main']['files'].items():
 q=MAIN/name
 if b['kind']=='symlink':assert q.is_symlink() and os.readlink(q)==b['target'] and stat.S_IMODE(q.lstat().st_mode)==b['mode'],name
 else:assert q.is_file() and not q.is_symlink() and q.stat().st_size==b['bytes'] and sha(q)==b['sha256'] and stat.S_IMODE(q.stat().st_mode)==b['mode'],name
assert len(before['main']['files'])==sync['baseline_nontracked_entries_preserved']==7333
assert sha(before['durable_backup_manifest'])==before['durable_backup_manifest_sha256']
assert git(MAIN,'rev-parse','refs/tags/review-base/cmm-source-survey-20261009')==before['retained_tag']['object'] and git(MAIN,'rev-parse','refs/tags/review-base/cmm-source-survey-20261009^{commit}')==before['retained_tag']['peeled_commit']
# Prevalidate every source and destination before creating the additive report directory.
labels=['helper-config','baseline','initial-gates','initial-gates-original','final-gates','review-check-final','local-coverage','preservation-before','preservation-precommit','commit-receipt','publish-receipt','preflight-committed-terminal','posted-review','queue-receipt','pr-cleanup','tracking-cleanup','postmerge-published-terminal','main-sync','hosted-audit-final','issue-ledger','corrective-issue-ledger','integration-status']
files=[T/f'cmm-round93-{x}.json' for x in labels]+[peerpath,Path(draft['path']),Path(pre['log']),Path(post['log']),Path(pre['coverage_receipt']),Path(post['coverage_receipt'])]
files += [Path(load(x)['log']) for x in ['baseline','initial-gates','final-gates','review-check-final']]
files += [T/f'cmm-round93-{x}.py' for x in ['commit','publish','post-review','enqueue','cleanup','tracking-cleanup','isolated-verification','isolated-coverage','sync-main','hosted-peer','hosted-five','finalize']]
files += [T/'cmm-round93-pr-body.md',T/'cmm-round93-build-report.py']
files=list(dict.fromkeys(files));assert len({p.name for p in files})==len(files)
plan=[]
for p in files:assert p.is_file() and not p.is_symlink();plan.append({'source':str(p),'name':p.name,'bytes':p.stat().st_size,'sha256':sha(p)})
dest=MAIN/'reports/publication/round93-20261015';assert not dest.exists() and not dest.is_symlink();dest.mkdir(parents=True);ev=dest/'evidence';ev.mkdir()
for item in plan:
 q=ev/item['name'];shutil.copy2(item['source'],q);assert sha(q)==item['sha256'];item['path']=str(q.relative_to(dest))
counts=cfg['counts'];body=f"[PR #{n}](https://github.com/CultureBotAI/CMMMech/pull/{n}) merged through the native queue as `{merge}`. Reviewed tree `{c['tree']}`.\n\nSix records added: thallium, beudantite, corkite, triphylite, lithiophilite and pig manure. Corpus: {counts['record_count']} records, {counts['history_count']} histories and {counts['structured_review_count']} structured reviews, with exact {counts['covered_records']}/{counts['record_count']} current scientific coverage.\n\nBaseline and corrected final checks passed: 317 tests, 3 skipped; strict records/history, pages and native reviews passed. Initial corkite/lithiophilite findings remain immutable with explicit resolved successors. Posting-consumer COMMENT binding was independently verified and its actual posted bytes match the accepted peer receipt.\n\nIsolated squash preflight and fresh remote-main checks after branch deletion passed with all {counts['review_base_count']} review bases available and the topic commit absent. All five hosted workflows and their selected-attempt jobs passed.\n\n"
body+='\n'.join(f"- [{role}]({r['url']}): success" for role,r in hosted['runs'].items())+'\n\n'
body+='Corrective issues '+', '.join('#'+str(x['number']) for x in corrected)+' are closed. Source questions '+', '.join('#'+str(x['number']) for x in issues)+' remain open; qualified records preserve their limits. No frontier exhaustion is asserted.\n\n'
body+=f"Only the owned branch refs were deleted. Clean detached worktree: `{W}`. Original main is clean at the merge; all 7,333 baseline nontracked entries including hidden/ignored files, retained review tag and earlier durable preservation manifest were verified unchanged. Unrelated worktrees were not reset, removed or pruned.\n\nRecord, source and native-review links: `research/ingests/round93-frontier-20261015.md`. CLAW admission and native queue are installed; future integration uses supported CLAW admission/sync. PR-shepherd credentials and controlled dry-run readiness remain unverified.\n"
(dest/'summary.md').write_text(body)
m={'recorded_at':datetime.now(timezone.utc).isoformat(),'passed':True,'pr':n,'base':c['base'],'head':c['head'],'merge':merge,'tree':c['tree'],'counts':counts,'issue_states':hosted['issue_states'],'files':plan,'summary_sha256':sha(dest/'summary.md'),'scope':'Completed actual publication, queue, branch cleanup and preservation evidence; additive ignored report only.'}
(dest/'manifest.json').write_text(json.dumps(m,indent=2)+'\n');assert all(sha(dest/x['path'])==x['sha256'] for x in plan);assert not git(MAIN,'status','--porcelain=v1','--untracked-files=all');print(dest/'summary.md')
