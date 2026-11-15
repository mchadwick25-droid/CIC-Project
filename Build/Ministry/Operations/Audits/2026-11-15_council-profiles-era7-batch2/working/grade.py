import sys,re;sys.path.insert(0,'/home/user/CIC-Project')
from engine.m7.turn_readability import grade_text
for f in sys.argv[1:]:
    t=open(f).read(); w=len(t.split())
    s=[x for x in re.split(r'(?<=[.!?])["”]?\s+',t.replace('\n',' ')) if x.strip()]
    g=grade_text(t)
    print(f.split('/')[-1], w,'words', f"{w/160:.2f}min", 'FK %.2f FRE %.2f'%(g['fk'],g['fre']),'max sent',max(len(x.split()) for x in s))
    for x in s:
        if len(x.split())>25: print('  LONG:',x)
