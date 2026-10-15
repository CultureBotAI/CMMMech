from pathlib import Path
import json
p=Path('/private/tmp');base='1d40007a3309d6c6f8c845363f96ef0e407306d0'
for label in ['final-gates','review-check-final','isolated-coverage','isolated-verification','publish','enqueue','cleanup','tracking-cleanup','sync-main']:
 q=p/f'cmm-round94-{label}.py';assert not q.exists();s=(p/f'cmm-round93-{label}.py').read_text().replace('round93','round94').replace('e0bffe8eb1c6e359f35d9c52c74a95a4efdc2b9d',base);compile(s,str(q),'exec');q.write_text(s)
cfg={'base':base,'branch':'curate/cmm-expansion-round94-20261015','title':'Curate five mineral species and petroleum coke with primary evidence','slugs':['amblygonite','ammoniojarosite','argentojarosite','hydroniumjarosite','montebrasite','petroleum-coke'],'counts':{'record_count':452,'history_count':517,'structured_review_count':534,'review_base_count':95,'covered_records':452}}
(p/'cmm-round94-helper-config.json').write_text(json.dumps(cfg,indent=2)+'\n');print('Core adapters compiled; counts provisional until exact enumeration.')
