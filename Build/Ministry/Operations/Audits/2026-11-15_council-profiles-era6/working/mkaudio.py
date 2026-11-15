import sys,os
d='/home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6'
for i in ['council-of-constance-1414','council-of-basel-ferrara-florence-1431']:
    t=open(f'{d}/{i}.brief.txt').read().rstrip('\n')
    p=t.split('\n\n'); p[0]='[calmly] '+p[0]; p[-1]='[warmly] '+p[-1]
    open(f'{d}/audio/{i}.audio.txt','w').write('\n\n'.join(p)+'\n')
    # check
    a=open(f'{d}/audio/{i}.audio.txt').read()
    assert a.replace('[calmly] ','',1).replace('[warmly] ','',1).rstrip('\n')==t
print('ok')
