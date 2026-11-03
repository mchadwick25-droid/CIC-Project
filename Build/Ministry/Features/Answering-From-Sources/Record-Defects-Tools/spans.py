"""spans.py REPO WORLD... : print record short id -> (file, first, last) parsed from the batch review tables"""
import sys,re,glob,json,os
repo=sys.argv[1]; out={}
for w in sys.argv[2:]:
    for f in sorted(glob.glob(f'{repo}/Build/worlds/{w}/Review-Artifacts/Rendering_Review_*_Batch*_2026-11-03.md')):
        for line in open(f):
            c=[x.strip() for x in re.split(r'(?<!\\)\|',line.strip().strip('|'))]
            if len(c)==5 and c[0] and not c[0].startswith('Record') and not set(c[0])<=set('-: '):
                m=re.findall(r'(cic/texts/[\w.\-]+)[^|]*?lines? (\d+)(?:\s*[-–]\s*(\d+))?',c[1])
                out[f'{w}.quote.{c[0]}']=[(a,int(b),int(e or b)) for a,b,e in m] or c[1]
json.dump(out,sys.stdout,indent=0)
