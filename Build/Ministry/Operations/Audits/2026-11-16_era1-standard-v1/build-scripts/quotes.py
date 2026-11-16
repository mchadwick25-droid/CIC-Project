import re,glob,os,sys,json,subprocess
B='Build/Ministry/Features/Church-Family-Tree/'
fs=sorted(glob.glob(B+'Who-Profiles/era1/batch*/*.brief.txt'))+[B+'Council-Profiles/era1/councils-of-rome-and-carthage-251.brief.txt']
rev=sys.argv[1] if len(sys.argv)>1 else None
out={}
for f in fs:
    t=subprocess.check_output(['git','show',f'{rev}:{f}']).decode() if rev else open(f).read()
    out[os.path.basename(f)[:-10]]=len(re.findall(r'"[^"]+"',t))
print(sum(out.values()),out)
if len(sys.argv)>2: json.dump(out,open(sys.argv[2],'w'))
