from pathlib import Path as RealPath
from unittest.mock import patch
from types import SimpleNamespace
import tempfile,json,io,contextlib,hashlib
original=RealPath('/private/tmp/cmm-round103-create-issues.py');source=original.read_text()
with tempfile.TemporaryDirectory(prefix='cmm-round103-issue-replay-',dir='/private/tmp') as temp:
 root=RealPath(temp);drafts=[]
 for i in range(6):
  p=root/f'body-{i}.md';p.write_text('Bounded source follow-up '+str(i)+'\n');drafts.append({'slug':str(i),'title':'Fresh issue '+str(i),'body_file':str(p)})
 (root/'cmm-round103-issue-drafts.json').write_text(json.dumps(drafts));(root/'cmm-round103-issues-precreate.json').write_text(json.dumps([{'title':'Old issue '+str(i)} for i in range(270)]))
 existing=root/'cmm-round103-source-issues.json';existing.write_text('original completed receipt\n');before=existing.read_bytes();created={};calls=[]
 def path(arg):return root if str(arg)=='/private/tmp' else RealPath(arg)
 def run(cmd,**kwargs):
  calls.append(cmd)
  if cmd[:3]==['gh','issue','create']:
   num=1000+len(created);title=cmd[cmd.index('--title')+1];body=RealPath(cmd[cmd.index('--body-file')+1]).read_text();url=f'https://github.com/CultureBotAI/CMMMech/issues/{num}';created[num]={'number':num,'title':title,'body':body,'state':'OPEN','url':url};return SimpleNamespace(returncode=0,stdout=url+'\n',stderr='')
  if cmd[:3]==['gh','issue','view']:return SimpleNamespace(returncode=0,stdout=json.dumps(created[int(cmd[3])]),stderr='')
  raise AssertionError('Unexpected mocked subprocess '+repr(cmd))
 error=None
 with patch('pathlib.Path',path),patch('subprocess.run',run),contextlib.redirect_stdout(io.StringIO()):
  try:exec(compile(source,str(original),'exec'),{'__name__':'__main__'})
  except Exception as e:error=type(e).__name__+': '+str(e)
 result={'helper_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),'existing_receipt_preserved':existing.read_bytes()==before,'mocked_issue_creations_before_failure':len(created),'final_exception':error,'network_or_github_mutations':False,'scope':'Full exact helper executed only with pathlib base redirected to unique temporary directory and all subprocess.run calls mocked; occupied aggregate receipt represents a prior completed run.'}
 assert len(created)==6 and error.startswith('FileExistsError') and existing.read_bytes()==before
 print(json.dumps(result,indent=2))
