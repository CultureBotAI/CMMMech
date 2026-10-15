from pathlib import Path
from datetime import datetime,timezone
import copy,json,runpy,hashlib,ast
T=Path('/private/tmp');g=runpy.run_path(str(T/'cmm-round105-publication-guards.py'));rows=[]
cfg=dict(base='b'*40,branch='topic',status=g['FINAL_CONFIG_STATUS'],counts=dict(record_count=2,history_count=2,structured_review_count=2,review_base_count=1,covered_records=2))
commit=dict(base=cfg['base'],head='h'*40,tree='t'*40,exit_code=0,config_sha256='config',verification_helper_sha256='verification',coverage_helper_sha256='coveragehelper');helper='/tmp/coverage.py';clone='/tmp/clone'
commands=[['uv','run','--locked','cmmmech','validate','--require-records'],['uv','run','--locked','cmmmech','validate-history','--base',cfg['base']],['just','review-check','--base',cfg['base'],'--require-reviews'],[clone+'/.venv/bin/python',helper,'--clone',clone,'--output','coverage.json']]
p=dict(mode='postmerge',exit_code=0,trusted_base=cfg['base'],topic_head=commit['head'],expected_tree=commit['tree'],config_sha256='config',helper_sha256='verification',clone=clone,log='postmerge.log',log_sha256='loghash',coverage=dict(path='coverage.json',sha256='coveragehash'),counts=cfg['counts'],commands=[dict(command=c,exit_code=0,allowed_exit_codes=[0],cwd=clone) for c in commands]);cv=dict(passed=True,root=clone,**cfg['counts']);digests={helper:'coveragehelper','postmerge.log':'loghash','coverage.json':'coveragehash'}
def test(name,change=None,reject=False):
 a,b,c,d,e=copy.deepcopy([cfg,commit,p,cv,digests]);
 if change:change(a,b,c,d,e)
 try:g['check_postmerge_receipt'](a,b,c,d,e.__getitem__,helper)
 except (AssertionError,KeyError):assert reject,name;observed='rejected'
 else:assert not reject,name;observed='accepted'
 rows.append(dict(name=name,expected='rejected' if reject else 'accepted',observed=observed,passed=True))
test('valid complete matching postmerge evidence')
mut=[('empty command set',lambda a,b,c,d,e:c.update(commands=[])),('failed coverage',lambda a,b,c,d,e:d.update(passed=False)),('wrong coverage count',lambda a,b,c,d,e:d.update(record_count=3)),('wrong reported counts',lambda a,b,c,d,e:c.update(counts={})),('wrong clone coverage',lambda a,b,c,d,e:d.update(root='/tmp/other')),('wrong base',lambda a,b,c,d,e:c.update(trusted_base='x'*40)),('wrong topic',lambda a,b,c,d,e:c.update(topic_head='x'*40)),('wrong tree',lambda a,b,c,d,e:c.update(expected_tree='x'*40)),('preflight mode',lambda a,b,c,d,e:c.update(mode='preflight')),('failed verification',lambda a,b,c,d,e:c.update(exit_code=1)),('failed commit',lambda a,b,c,d,e:b.update(exit_code=1)),('provisional config',lambda a,b,c,d,e:a.update(status='Provisional')),('changed receipt config digest',lambda a,b,c,d,e:c.update(config_sha256='changed')),('changed verification helper digest',lambda a,b,c,d,e:c.update(helper_sha256='changed')),('changed current coverage helper',lambda a,b,c,d,e:e.update({helper:'changed'})),('changed log',lambda a,b,c,d,e:e.update({'postmerge.log':'changed'})),('changed coverage file',lambda a,b,c,d,e:e.update({'coverage.json':'changed'})),('wrong command cwd',lambda a,b,c,d,e:c['commands'][0].update(cwd='/tmp/other')),('duplicate required invocation',lambda a,b,c,d,e:c['commands'].append(copy.deepcopy(c['commands'][0])))]
for name,change in mut:test(name,change,True)
for i in range(4):
 test('missing required gate '+str(i),lambda a,b,c,d,e,i=i:c['commands'].pop(i),True)
 test('failed required gate even if allowed '+str(i),lambda a,b,c,d,e,i=i:c['commands'][i].update(exit_code=1,allowed_exit_codes=[0,1]),True)
for origin,ok in [(g['EXPECTED_ORIGIN'],True),('https://github.com/unrelated/repo.git',False)]:
 try:g['check_cleanup_origin'](origin)
 except AssertionError:assert not ok;result='rejected'
 else:assert ok;result='accepted'
 rows.append(dict(name='cleanup origin '+origin,expected='accepted' if ok else 'rejected',observed=result,passed=True))
for n in ['cleanup','finalize']:
 s=(T/f'cmm-round105-{n}.py').read_text();ast.parse(s)
 first=s.index("guards['check_cleanup_origin']")
 for mutation in (["git('push'","git('checkout'","git('update-ref'"] if n=='cleanup' else ["git('fetch'","git('merge'"]):assert first<s.index(mutation)
 rows.append(dict(name=n+' origin guard precedes first mutations',passed=True))
s=(T/'cmm-round105-finalize.py').read_text();assert s.index("guards['check_postmerge_receipt']")<s.index("git('fetch'")<s.index("git('merge'");assert s.index("sha(T/('cmm-round105-'+name))==commit[key]")<s.index("guards['check_postmerge_receipt']")
rows.append(dict(name='current helper/config bindings and postmerge gates precede main mutations',passed=True))
r=dict(recorded_at=datetime.now(timezone.utc).isoformat(),passed=True,case_count=len(rows),cases=rows,guard_sha256=hashlib.sha256((T/'cmm-round105-publication-guards.py').read_bytes()).hexdigest(),test_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Pure gate rejection/acceptance tests plus source ordering; no network/Git mutations. Independent reviewer also executes inert exact-helper probes.')
p=T/'cmm-round105-guard-regression.json';assert not p.exists();p.write_text(json.dumps(r,indent=2)+'\n');print(len(rows),'tests passed')
