import copy
import hashlib
import io
import json
import tempfile
from contextlib import redirect_stdout
from pathlib import Path
import yaml
from cmmmech.validation import validate_record
from cmmmech.cli import main

base = {'id':'cmmmech:boundary-fixture','name':'Synthetic boundary fixture','material_kind':'element','description':'Synthetic review fixture only.','sources':[{'id':'fixture','title':'Synthetic source','url':'https://example.invalid/fixture','accessed_on':'2026-10-11'}]}
results=[]
def check(name, record, valid):
    errors=validate_record(record)
    assert (not errors)==valid, (name,errors)
    results.append({'case':name,'expected_valid':valid,'errors':errors})
check('identity only without criticality or mechanisms',base,True)
x=copy.deepcopy(base);x['material_kind']='ion';check('ion rejected as a root schema kind',x,False)
x=copy.deepcopy(base);x['mechanisms']=[{'id':'inactive_biosorption','name':'Synthetic dead biomass biosorption','process':'biosorption','description':'Synthetic binding observation, no metabolism claim.','context':'Inactive dried microbial biomass; synthetic test only.','microbial':True,'organisms':[{'id':'NCBITaxon:1','label':'Synthetic root label'}],'evidence':[{'source_ref':'fixture','supports':'partial','explanation':'Synthetic weak-control observation.'}]}];check('inactive biomass can use microbial true',x,True)
y=copy.deepcopy(x);y['mechanisms'][0]['microbial']=False;check('organisms rejected without microbial true',y,False)
obs={'id':'cell','source_ref':'fixture','source_table':'Synthetic table 1','source_sample_id':'A','source_column':'U','raw_value':'-0.025','analyte':{'id':'CHEBI:27214','label':'Synthetic uranium label'},'material_form':'Synthetic aqueous aliquot','sampled_fraction':'Synthetic total element assay','study_arm':'abiotic','result_status':'below_detection','detection_limit':0.025,'unit':'mg/kg','analyzed_on':'2026-10-11','context':'Synthetic source explicitly encodes below detection with a negative limit.'}
x['mechanisms'][0]['observations']=[obs];check('negative source limit with abiotic arm under microbial mechanism',x,True)
y=copy.deepcopy(x);y['mechanisms'][0]['observations'][0]['value']=0;check('censored value cannot also be a zero measurement',y,False)
y=copy.deepcopy(x);y['mechanisms'][0]['observations'][0]['unit']='mg/L';check('mg/L needs another contract and is rejected',y,False)
y=copy.deepcopy(x);second=copy.deepcopy(obs);second['id']='different_id';y['mechanisms'][0]['observations'].append(second);check('duplicate source cell rejected despite distinct observation ID',y,False)
y=copy.deepcopy(x);y['mechanisms'][0]['observations'][0]['sampled_on']='2026-10-12';y['mechanisms'][0]['observations'][0]['sampling_source_locator']='Synthetic date column';check('sample date cannot follow analysis date',y,False)
with tempfile.TemporaryDirectory(prefix='cmmmech-boundary-') as tmp:
    root=Path(tmp)
    for name in ('a.yaml','b.yaml'):
        (root/name).write_text(yaml.safe_dump(base))
    out=io.StringIO()
    with redirect_stdout(out): code=main(['validate',str(root),'--require-records'])
    assert code==1 and 'duplicate record id' in out.getvalue()
    results.append({'case':'full corpus catches duplicate record IDs','exit_code':code,'output':out.getvalue()})
print(json.dumps(results,indent=2))
