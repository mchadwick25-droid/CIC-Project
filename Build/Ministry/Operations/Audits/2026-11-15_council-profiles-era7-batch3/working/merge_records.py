import json,os
d='/home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/records.json'
w=os.path.dirname(os.path.abspath(__file__))
r=json.load(open(d))
for i in ['union-of-brest-1596','synod-of-diamper-1599','synod-of-dort','westminster-assembly']:
    p=f'{w}/records_{i}.json'
    if os.path.exists(p): r[i]=json.load(open(p)); print('merged',i)
json.dump(r,open(d,'w'),ensure_ascii=False,indent=2); open(d,'a').write('\n')
