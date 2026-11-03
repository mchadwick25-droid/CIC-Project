"""brit.py REPO : list British spellings in modern-English fields of records changed vs merge-base"""
import sys,re,subprocess,yaml
repo=sys.argv[1]
base=subprocess.run(['git','-C',repo,'merge-base','HEAD','origin/main'],capture_output=True,text=True).stdout.strip()
files=subprocess.run(['git','-C',repo,'diff','--name-only',base,'--','records/'],capture_output=True,text=True).stdout.split()
pat=re.compile(r"\b\w*(?:our(?:s|ed|ing|able)?|ise[sd]?|ising|isation|yse[sd]?|tre|ence|elled|elling|eller|ogue|gramme)\b",re.I)
words={'colour','honour','favour','labour','behaviour','neighbour','harbour','humour','rumour','savour','vigour','valour','splendour','fervour','ardour','candour','centre','theatre','metre','fibre','sombre','defence','offence','pretence','travelled','travelling','traveller','travellers','counselled','cancelled','marvelled','marvellous','jewellery','judgement','grey','catalogue','programme','realise','recognise','organise','apologise','baptise','baptised','sympathise','criticise','emphasise','authorise','civilise','evangelise','memorise','agonise','scandalise','analyse','paralyse','towards'}
for f in files:
    try: d=yaml.safe_load(open(f'{repo}/{f}').read().split('\n---\n')[0][4:])
    except Exception: continue
    fields={'modern_rendering':d.get('modern_rendering'),'modern_lens_note':d.get('modern_lens_note'),'use_note.means':(d.get('use_note') or {}).get('means')}
    for k,v in fields.items():
        if not isinstance(v,str): continue
        hits=sorted({w for w in re.findall(r"[A-Za-z]+",v) if w.lower().rstrip('s') in words or w.lower() in words or re.fullmatch(r"\w+(our|ours|oured)",w.lower()) and w.lower() not in {'our','ours','four','hour','hours','pour','sour','your','yours','flour','tour','court','journey','favourite'}})
        if hits: print(f.split('/')[-1][:-3],k,hits)
