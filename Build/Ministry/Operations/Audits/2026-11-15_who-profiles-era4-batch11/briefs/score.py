import sys,glob,os,json
sys.path.insert(0,'/home/user/CIC-Project')
from engine.m1.gates import grade_text
d=sys.argv[1]
for f in sorted(glob.glob(d+'/*.brief.txt')):
    t=open(f).read().strip()
    n=len(t.split()); s=n/162.5*60
    g=grade_text(t)
    print(f"{os.path.basename(f)[:-10]:45s} {n:4d}w {int(s//60)}:{int(s%60):02d} FK {g['fk']:.1f} FRE {g['fre']:.1f}")
    # audio
    paras=t.split('\n\n'); paras[0]='[calmly] '+paras[0]; paras[-1]='[warmly] '+paras[-1]
    os.makedirs(d+'/audio',exist_ok=True)
    open(d+'/audio/'+os.path.basename(f)[:-10]+'.audio.txt','w').write('\n\n'.join(paras)+'\n')
for f in glob.glob(d+'/*.json'): json.load(open(f))
