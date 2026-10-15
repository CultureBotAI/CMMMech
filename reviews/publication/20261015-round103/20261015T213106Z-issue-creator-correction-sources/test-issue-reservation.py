from pathlib import Path as RealPath
from unittest.mock import patch
from types import SimpleNamespace
from contextlib import ExitStack,redirect_stdout
from datetime import datetime,timezone
import tempfile,json,hashlib,io
helper=RealPath('/private/tmp/cmm-round103-create-issues.py');source=helper.read_text();real_receipt=RealPath('/private/tmp/cmm-round103-source-issues.json');real_before=real_receipt.read_bytes();original_open=RealPath.open
results=[]
for case in ['normal','occupied_regular','existing_symlink','dangling_symlink','racing_creator','rerun','partial_create_failure','post_create_verification_failure']:
 with tempfile.TemporaryDirectory(prefix='cmm-round103-issue-guard-',dir='/private/tmp') as temp:
  root=RealPath(temp);drafts=[]
  for i in range(6):
   p=root/f'body-{i}.md';p.write_text(f'Source follow-up {i}\n');drafts.append({'slug':str(i),'title':f'New issue {i}','body_file':str(p)})
  (root/'cmm-round103-issue-drafts.json').write_text(json.dumps(drafts));(root/'cmm-round103-issues-precreate.json').write_text(json.dumps([{'title':f'Old issue {i}'} for i in range(270)]));aggregate=root/'cmm-round103-source-issues.json';target=root/'target.json';calls=[];created={};raced=[False]
  if case=='occupied_regular':aggregate.write_text('original\n')
  if case=='existing_symlink':target.write_text('target original\n');aggregate.symlink_to(target)
  if case=='dangling_symlink':aggregate.symlink_to(root/'missing.json')
  def path(arg):return root if str(arg)=='/private/tmp' else RealPath(arg)
  def run(cmd,**kwargs):
   calls.append(cmd)
   if cmd[:3]==['gh','issue','create']:
    if case=='partial_create_failure' and len(created)==1:return SimpleNamespace(returncode=1,stdout='',stderr='mocked failure after one creation')
    n=1000+len(created);title=cmd[cmd.index('--title')+1];body=RealPath(cmd[cmd.index('--body-file')+1]).read_text();url=f'https://github.com/CultureBotAI/CMMMech/issues/{n}';created[n]={'number':n,'title':title,'body':body,'state':'OPEN','url':url};return SimpleNamespace(returncode=0,stdout=url+'\n',stderr='')
   if cmd[:3]==['gh','issue','view']:
    if case=='post_create_verification_failure':return SimpleNamespace(returncode=1,stdout='',stderr='mocked view failure')
    return SimpleNamespace(returncode=0,stdout=json.dumps(created[int(cmd[3])]),stderr='')
   raise AssertionError('Unexpected subprocess: '+repr(cmd))
  def racing_open(self,mode='r',*args,**kwargs):
   if self==aggregate and mode=='x' and not raced[0]:
    raced[0]=True
    with original_open(self,'x') as f:f.write('racing creator\n')
   return original_open(self,mode,*args,**kwargs)
  def invoke():
   err=None
   with ExitStack() as stack:
    stack.enter_context(patch('pathlib.Path',path));stack.enter_context(patch('subprocess.run',run));stack.enter_context(redirect_stdout(io.StringIO()))
    if case=='racing_creator':stack.enter_context(patch.object(RealPath,'open',racing_open))
    try:exec(compile(source,str(helper),'exec'),{'__name__':'__main__'})
    except BaseException as e:err=type(e).__name__
   return err
  err=invoke()
  if case in ['normal','rerun']:
   assert err is None and len(created)==6 and len(json.loads(aggregate.read_text()))==6
   if case=='rerun':
    before=aggregate.read_bytes();calls.clear();err=invoke();assert err=='FileExistsError' and not calls and aggregate.read_bytes()==before
  elif case in ['occupied_regular','existing_symlink','dangling_symlink','racing_creator']:
   assert err=='FileExistsError' and not calls
   if case=='occupied_regular':assert aggregate.read_text()=='original\n'
   elif case=='existing_symlink':assert aggregate.is_symlink() and target.read_text()=='target original\n'
   elif case=='dangling_symlink':assert aggregate.is_symlink() and not target.exists()
   else:assert aggregate.read_text()=='racing creator\n'
  elif case=='partial_create_failure':
   d=json.loads(aggregate.read_text());assert err=='AssertionError' and d['status']=='failed' and len(d['created_issues'])==1 and d['active']['create_response']['exit_code']==1
  elif case=='post_create_verification_failure':
   d=json.loads(aggregate.read_text());assert err=='AssertionError' and d['status']=='failed' and d['active']['stage']=='created_unverified' and d['active']['number']==1000 and d['active']['verification_response']['exit_code']==1
  results.append({'case':case,'passed':True,'subprocess_calls':len(calls),'exception':err})
assert real_receipt.read_bytes()==real_before
print(json.dumps({'saved_at_utc':datetime.now(timezone.utc).isoformat(),'helper_sha256':hashlib.sha256(helper.read_bytes()).hexdigest(),'passed':True,'cases':results,'real_successful_receipt_unchanged_sha256':hashlib.sha256(real_before).hexdigest(),'scope':'Exact helper bytes executed only with temporary path mapping and all subprocess calls mocked. No network/GitHub mutations; original real #385–390 receipt unchanged.'},indent=2))
