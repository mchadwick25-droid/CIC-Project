"""setfield.py REPO WORLD JSONFILE : JSON {short_id: {field: value}} ; replaces top-level scalar fields in quote records, verifying YAML round-trip."""
import sys,re,json,yaml
from pathlib import Path
repo,world,jf=sys.argv[1:4]
for sid,fields in json.load(open(jf)).items():
    p=Path(repo)/'records'/world/'quote'/f'{world}.quote.{sid}.md'; t=p.read_text()
    end=t.index('\n---\n',4); fm=t[4:end]; d0=yaml.safe_load(fm)
    for field,v in fields.items():
        m=re.search(rf'(?m)^{field}:.*(?:\n(?:[ ]+.*|))*?(?=\n[A-Za-z_]+:|\Z)',fm); assert m,(sid,field)
        new=f'{field}: '+json.dumps(v,ensure_ascii=False)
        fm=fm[:m.start()]+new+fm[m.end():]
    d=yaml.safe_load(fm)
    for k in d0:
        assert d[k]==(fields[k] if k in fields else d0[k]),(sid,k)
    p.write_text(t[:4]+fm+t[end:]); print('set',sid,list(fields))
