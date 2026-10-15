from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,sys
p=Path('/private/tmp');repo='CultureBotAI/CMMMech';number=json.loads((p/'cmm-round93-publish-receipt.json').read_text())['pr']['number'];c=json.loads((p/'cmm-round93-commit-receipt.json').read_text());peerpath=Path(sys.argv[1]);a=json.loads(peerpath.read_text());bodypath=p/'cmm-round93-hosted-review-comment.md';body=bodypath.read_text();out=p/'cmm-round93-posted-review.json';assert not out.exists()
def gh(*args):return subprocess.check_output(['gh',*args],text=True).strip()
assert a['passed'] and a['pr']==number and not a['findings'] and not a['pending']
assert all(a[k]==c[k] for k in ['head','tree','base']) and a['workflow_run']['head_sha']==c['head'] and a['workflow_run']['conclusion']=='success'
pr=json.loads(gh('api',f'repos/{repo}/pulls/{number}'));assert pr['state']=='open' and pr['head']['sha']==c['head'] and pr['base']['sha']==c['base']
conversation={}
for field,endpoint in [('reviews',f'pulls/{number}/reviews'),('issue_comments',f'issues/{number}/comments'),('inline_comments',f'pulls/{number}/comments')]:
 conversation[field]=[x for page in json.loads(gh('api',f'repos/{repo}/{endpoint}?per_page=100','--paginate','--slurp')) for x in page]
query='query($n:Int!){repository(owner:"CultureBotAI",name:"CMMMech"){pullRequest(number:$n){reviewThreads(first:100){nodes{id isResolved} pageInfo{hasNextPage}}}}}'
threads=json.loads(gh('api','graphql','-f','query='+query,'-F','n='+str(number)))['data']['repository']['pullRequest']['reviewThreads'];assert not threads['pageInfo']['hasNextPage'];conversation['review_threads']=threads['nodes']
assert conversation==a['conversation'],'Conversation changed since independent audit; reassess before posting.'
request=p/'cmm-round93-review-request.json';assert not request.exists();request.write_text(json.dumps({'commit_id':c['head'],'event':'COMMENT','body':body})+'\n')
r=json.loads(gh('api','--method','POST',f'repos/{repo}/pulls/{number}/reviews','--input',str(request)));assert r['commit_id']==c['head'] and r['state']=='COMMENTED' and r['body']==body
receipt={'recorded_at':datetime.now(timezone.utc).isoformat(),'head':c['head'],'review':r,'peer_receipt':str(peerpath),'peer_sha256':hashlib.sha256(peerpath.read_bytes()).hexdigest(),'body_sha256':hashlib.sha256(bodypath.read_bytes()).hexdigest()};out.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'review_id':r['id'],'url':r['html_url'],'head':c['head']},indent=2))
