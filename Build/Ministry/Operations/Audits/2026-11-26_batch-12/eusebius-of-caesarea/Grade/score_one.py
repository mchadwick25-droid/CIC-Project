import json,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import grade_whole as gw
HERE=gw.HERE
mod=gw.load('grade28',os.path.join(HERE,'grade.py'))
rows=gw.score(mod,HERE,os.path.join(HERE,'Set.json'),os.path.join(HERE,'trust','Trust_Results.json'))
json.dump(rows,open(os.path.join(HERE,'Grade_Eusebius.json'),'w'),indent=1,ensure_ascii=False)
for r in rows:
    print(r['rigor'],r['rigor_load'],r['craft'],r['craft_load'],r['overall'],r['action'])
    for f in r['findings']: print(' ',f['dim'],f['kind'],f['band'],f['size'],'|',f['quote'][:90])
