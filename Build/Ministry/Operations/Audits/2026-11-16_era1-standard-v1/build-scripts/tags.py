import re,glob,os,sys,json
V=r"(?:says|said|say|writes|wrote|write|tells|told|tell|reports|reported|adds|added|records|recorded|notes|noted|claims|claimed|charges|charged)"
def count(t): return len(re.findall(r"\b"+V+r"\b",t))
B='Build/Ministry/Features/Church-Family-Tree/'
fs=sorted(glob.glob(B+'Who-Profiles/era1/batch*/*.brief.txt'))+[B+'Council-Profiles/era1/councils-of-rome-and-carthage-251.brief.txt']
out={os.path.basename(f)[:-10]:count(open(f).read()) for f in fs}
if len(sys.argv)>1: json.dump(out,open(sys.argv[1],'w'),indent=1)
print(sum(out.values()), out)
