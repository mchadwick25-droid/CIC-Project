"""mklog.py REPO WORLD Prefix  -> writes Rendering_Review_Log_<N>_2026-11-03.md from Rendering_Review_<Prefix>_Batch*.md and _Round2/_Round3"""
import sys,glob,re,os,json
repo,world,pre=sys.argv[1:4]
d=f'{repo}/Build/worlds/{world}/Review-Artifacts'
rows={}
for f in sorted(glob.glob(f'{d}/Rendering_Review_{pre}_Batch*_2026-11-03.md')):
    for line in open(f).read().splitlines():
        c=[x.strip().replace('\\|','/') for x in re.split(r'(?<!\\)\|',line.strip().strip('|'))]
        if len(c)==5 and c[0] and not c[0].startswith('Record') and not set(c[0])<=set('-: '):
            rows[c[0]]={'files':[os.path.basename(f)],'check':c[3],'verdict':c[4]}
for r in ('Round2','Brackets','Round3'):
    f=f'{d}/Rendering_Review_{pre}_{r}_2026-11-03.md'
    if not os.path.exists(f): continue
    for line in open(f).read().splitlines():
        c=[x.strip().replace('\\|','/') for x in re.split(r'(?<!\\)\|',line.strip().strip('|'))]
        if len(c)==4 and c[0] in rows: rows[c[0]].setdefault('later',[]).append((os.path.basename(f),r,c[3]))
sys.path.insert(0,repo)
from engine.m1.loader import load_world_records
R=load_world_records(world)
rendered={k.split('.',2)[2] for k,v in R.items() if isinstance(v.get('modern_rendering'),str) and v['modern_rendering'].strip()}
missing=rendered-set(rows); extra=set(rows)-rendered
assert not missing and not extra,(missing,extra)
n=len(rows); nb=len(glob.glob(f'{d}/Rendering_Review_{pre}_Batch*_2026-11-03.md'))
fails=[k for k,v in rows.items() if 'later' in v]
out=[f"# {world} quote renderings: per-rendering review log ({n} records)","",
f"Date: 2026-11-03. Records: the {n} `{world}.quote.*` records, each with a `modern_rendering` and a `text` taken from a vendored source.","",
f"What this log is for: it lets the claim \"reviewed\" be checked, one record at a time. Each row gives the record id (the `{world}.quote.` prefix is dropped), the review file or files that read the rendering, and the verdict. All review files are in `Build/worlds/{world}/Review-Artifacts/`.","",
f"How it was made. Independent Opus 5.5 reviewers read every rendering in {nb} batch file{'s' if nb>1 else ''} (`Rendering_Review_{pre}_Batch*_2026-11-03.md`). Each rendering was read against the record's `text` and against the edition text at its locus in `cic/texts/`. The bar: every clause rendered, nothing added, one thought per sentence, no sentence past about 25 words, no word whose modern sense misleads, and the source's own hedges kept."
+ (f" Round 1 failed {len(fails)}. Each was re-rendered by Opus at the source record and rechecked by a second, independent Opus reader in `Rendering_Review_{pre}_Round2_2026-11-03.md`." if fails else " Round 1 failed none."),"",
"| Record | Review file(s) | Verdict on the rendering |","|---|---|---|"]
for k in sorted(rows):
    v=rows[k]; files=list(dict.fromkeys(v['files']+[f for f,_,_ in v.get('later',[])]))
    if 'later' in v: lab={'Round2':'round 2','Brackets':'bracket recheck','Round3':'round 3'}; verdict='round 1 '+v['verdict']+'; '+'; '.join(f"{lab[r]} {x}" for _,r,x in v['later'])+(', after re-rendering' if any(x.startswith('PASS') for _,_,x in v['later'][1:]) or v['verdict'].startswith('FAIL') else '')
    else: verdict=v['verdict']+' ('+v['check']+')'
    out.append(f"| {k} | {', '.join(files)} | {verdict} |")
open(f'{d}/Rendering_Review_Log_{n}_2026-11-03.md','w').write('\n'.join(out)+'\n')
print(world,n,'fails',fails)
