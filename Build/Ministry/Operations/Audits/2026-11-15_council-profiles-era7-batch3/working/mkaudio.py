import sys,os,glob
IDS=['union-of-brest-1596','synod-of-diamper-1599','synod-of-dort','westminster-assembly']
d='/home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7'
os.makedirs(f'{d}/audio',exist_ok=True)
for f in sorted(glob.glob(f'{d}/*.brief.txt')):
    if os.path.basename(f).split('.')[0] not in IDS: continue
    i=os.path.basename(f)[:-len('.brief.txt')]
    t=open(f).read().rstrip('\n')
    p=t.split('\n\n'); p[0]='[calmly] '+p[0]; p[-1]='[warmly] '+p[-1]
    open(f'{d}/audio/{i}.audio.txt','w').write('\n\n'.join(p)+'\n')
    a=open(f'{d}/audio/{i}.audio.txt').read()
    assert a.replace('[calmly] ','',1).replace('[warmly] ','',1).rstrip('\n')==t
    print('ok',i)
