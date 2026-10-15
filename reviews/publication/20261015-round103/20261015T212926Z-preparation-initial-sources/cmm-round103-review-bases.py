from pathlib import Path
from datetime import datetime, timezone
import subprocess, json, os, yaml
root = Path('/private/tmp/CMMMech-expansion-round103-20261015')
base = '44d5b468519eb862b32ef54bf7c066bc0f79ba62'
revisions = set(); seen = set()
for directory, dirs, files in os.walk(root/'reviews/structured', followlinks=True):
    resolved = Path(directory).resolve()
    if resolved in seen: dirs[:] = []; continue
    seen.add(resolved)
    if 'review.yaml' in files:
        revisions.add(yaml.safe_load((Path(directory)/'review.yaml').read_text())['source']['git_revision'])
def git(*args): return subprocess.check_output(['git','-C',str(root),*args],text=True).strip()
rows = []
for revision in sorted(revisions):
    assert git('cat-file','-t',revision) == 'commit'
    p = subprocess.run(['git','-C',str(root),'merge-base','--is-ancestor',revision,base])
    assert p.returncode in (0,1)
    tags = []
    if p.returncode:
        for name in git('tag','--points-at',revision).splitlines():
            if name.startswith('review-base/'):
                assert git('cat-file','-t','refs/tags/'+name) == 'tag'
                assert git('rev-parse','refs/tags/'+name+'^{}') == revision
                tags.append(name)
        assert tags, revision
    rows.append({'revision':revision,'ancestor_of_main_base':p.returncode==0,'retained_tags':tags})
tag = 'refs/tags/review-base/cmm-source-survey-20261009'
remote = git('ls-remote','origin',tag,tag+'^{}')
assert dict(line.split()[::-1] for line in remote.splitlines()) == {tag:'fc4040c3abcd28f0a9cc52467e308100144ad1fd',tag+'^{}':'c0adc2c0763e1515ed07dc712b024974d98fb342'}
data = {'recorded_at':datetime.now(timezone.utc).isoformat(),'base':base,'bases':rows,'count':len(rows),'remote_retained_tag':remote,'passed':True,'scope':'All native review bundles enumerated with hidden/ignored inclusion and relevant symlink traversal; every exact review base is available and survives via main ancestry or the unchanged annotated remote evidence tag.'}
out = Path('/private/tmp/cmm-round103-review-bases-local.json')
with out.open('x') as f:json.dump(data,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in data.items() if k!='bases'},indent=2))
