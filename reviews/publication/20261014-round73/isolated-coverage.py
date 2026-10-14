"""Verify exact scientific coverage and base availability in a supplied fresh clone."""
import argparse, datetime, hashlib, json, os, subprocess
from pathlib import Path
import yaml

parser=argparse.ArgumentParser()
parser.add_argument('--clone',required=True)
parser.add_argument('--output',required=True)
args=parser.parse_args()
root=Path(args.clone).resolve()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def yaml_files(directory,name=None):
 result=[];seen=set()
 for d,dirs,files in os.walk(directory,followlinks=True):
  resolved=Path(d).resolve()
  if resolved in seen:dirs[:]=[];continue
  seen.add(resolved)
  for f in files:
   if (name and f==name) or (not name and f.endswith(('.yaml','.yml'))):result.append(Path(d)/f)
 return sorted(result)
records=yaml_files(root/'data/records')
histories=yaml_files(root/'history/records')
reviews=[(p,yaml.safe_load(p.read_text())) for p in yaml_files(root/'reviews/structured','review.yaml')]
coverage=[]
for p in records:
 path=str(p.relative_to(root));content=yaml.safe_load(p.read_text());digest=sha(p);matching=[]
 for rp,r in reviews:
  if r.get('scientific_review') is not True or r.get('completion')!='completed' or r.get('verdict') not in ('pass','pass_with_limitations'):continue
  if content['id'] not in r.get('scope',{}).get('reviewed_target_ids',[]):continue
  if not any(t.get('path')==path and t.get('target_id')==content['id'] for t in r.get('targets',[])):continue
  if not any(i.get('path')==path and i.get('sha256')==digest for i in r.get('source',{}).get('inputs',[])):continue
  matching.append({'path':str(rp.relative_to(root)),'review_id':r['review_id'],'review_sha256':sha(rp),'verdict':r['verdict']})
 coverage.append({'path':path,'id':content['id'],'sha256':digest,'matching_scientific_reviews':matching})
bases=sorted({r['source']['git_revision'] for p,r in reviews})
base_checks=[]
for rev in bases:
 p=subprocess.run(['git','-C',str(root),'cat-file','-t',rev],capture_output=True,text=True)
 base_checks.append({'revision':rev,'available_commit':p.returncode==0 and p.stdout.strip()=='commit'})
result={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root':str(root),'record_count':len(records),'history_count':len(histories),'structured_review_count':len(reviews),'review_base_count':len(bases),'bases':base_checks,'covered_records':sum(bool(x['matching_scientific_reviews']) for x in coverage),'records':coverage,'scope':'Hidden/ignored-inclusive filesystem enumeration follows relevant symlinks with cycle prevention. Current record ID, target path, reviewed target scope and exact SHA256 must match completed positive scientific reviews; context-only successors cannot substitute. This supplements the canonical review checker.'}
expected=json.loads(Path('/private/tmp/cmm-round73-helper-config.json').read_text())['counts']
result['passed']=all(result[k]==v for k,v in expected.items()) and all(b['available_commit'] for b in base_checks) and all(x['matching_scientific_reviews'] for x in coverage)
output=Path(args.output)
if output.exists():raise SystemExit('Refusing to overwrite coverage receipt: '+str(output))
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['records','bases']},indent=2))
raise SystemExit(0 if result['passed'] else 1)
