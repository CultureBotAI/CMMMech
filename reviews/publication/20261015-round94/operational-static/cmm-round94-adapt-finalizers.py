from pathlib import Path
p=Path('/private/tmp')
s=(p/'cmm-round93-commit.py').read_text().replace('round93','round94')
a=s.index("rawlogs=");b=s.index("for label in ['baseline','final-gates']:")
s=s[:a]+'''rawlogs=['research/ingests/round94-checks-20261015/final-gates.log','research/ingests/round94-checks-20261015/baseline.log']
subprocess.run(['git','-C',str(r),'diff','--cached','--check','--','.',*[':(exclude)'+x for x in rawlogs]],check=True)
for logfile in rawlogs:subprocess.run(['git','-C',str(r),'-c','core.whitespace=-blank-at-eof','diff','--cached','--check','--',logfile],check=True)
'''+s[b:]
s=s.replace("Verbatim check logs and the independently retained hosted-five diff preserve original bytes and hashes; only blank-at-eof is disabled for the three raw logs and blank-at-eol for the exact byte-verified diff. Maintained content uses normal whitespace checks.","Verbatim baseline/final check logs preserve original bytes and hashes; only blank-at-eof is disabled for those exact two logs. All maintained content uses normal whitespace checks.")
q=p/'cmm-round94-commit.py';assert not q.exists();compile(s,str(q),'exec');q.write_text(s)
s=(p/'cmm-round93-finalize.py').read_text().replace('round93','round94').replace('==7333','==7381').replace('7,333','7,381').replace("'initial-gates','initial-gates-original',",'').replace("'baseline','initial-gates','final-gates'","'baseline','final-gates'").replace('thallium, beudantite, corkite, triphylite, lithiophilite and pig manure','amblygonite, ammoniojarosite, argentojarosite, hydroniumjarosite, montebrasite and petroleum coke').replace('Initial corkite/lithiophilite findings remain immutable with explicit resolved successors.','The initial argentojarosite locator finding remains immutable with an explicit resolved successor.')
q=p/'cmm-round94-finalize.py';assert not q.exists();compile(s,str(q),'exec');q.write_text(s)
print('Narrow finalizer and commit adapters compiled; not executed.')
