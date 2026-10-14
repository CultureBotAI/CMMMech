from pathlib import Path
from datetime import datetime, timezone
import runpy,json
lib=runpy.run_path('/private/tmp/cmm-round57-recover-original.py',run_name='snapshot_library')
p=Path('/private/tmp');initial=json.loads((p/'cmm-round73-preservation-before.json').read_text())
actual={'main':lib['snapshot'](lib['MAIN'],False),'skill':lib['snapshot'](lib['SKILL'],True)}
assert actual==initial['snapshots'] and lib['retained_tag']()==initial['retained_tag']
result={'recorded_at':datetime.now(timezone.utc).isoformat(),'passed':True,'preserved_entry_counts':{k:len(x['files']) for k,x in actual.items()},'initial_sha256':lib['sha'](p/'cmm-round73-preservation-before.json'),'scope':'Hidden/ignored-inclusive bytes, modes, symlink targets and Git state; original main nontracked files, unrelated skill tracked/nontracked files. Git administrative files and external symlink contents excluded.'}
lib['save'](p/'cmm-round73-preservation-prepublication.json',result)
print(json.dumps(result,indent=2))
