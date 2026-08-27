"""Retrieval reach benchmark - 60 participant questions, ten per world.

WRITTEN BEFORE THE RECORDS IT MEASURES. The questions in bench/ were
composed on 2026-08-27 from each world's own subject matter, and locked,
BEFORE any quote record was hinted - which is the only reason the
before/after numbers mean anything. Hint words are merged into a cell's
retrieval vocabulary, so anyone who writes a hint after seeing a question
fail can make that question pass without retrieval getting better. See
cic/corpus-map/RETRIEVAL-HINTS.md, rule 2.

Reports, per world: total ground records over the ten questions, the
average, how many canon cells were matched, how many questions returned
an ENTIRELY EMPTY ground, and how many quote records surfaced.

Baseline on the day it was written (entity routing in, no quote hints):
    214 ground / 3.6 avg / 19 cells / 11 empty / 25 quotes
After hinting all 125 quotes and fixing six records that carried no
canon_cells at all:
    290 ground / 4.8 avg / 30 cells /  9 empty / 48 quotes

Run: python3 engine/m4/reports/retrieval_bench.py
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from engine.m1 import loader
from engine.m4 import evidence as ev
fleet = loader.load_fleet_records()
cq = {r:v for r,v in fleet.items() if v.get("record_type")=="canon_question"}
S = pathlib.Path(__file__).resolve().parent / "bench"
tot_g=tot_q=tot_empty=tot_cells=0
per=[]
for w in ["alx","desert","hal","ijc","pahc","syr"]:
    pkgs=sorted(pathlib.Path(f"packages/{w}").iterdir())
    C=pkgs[-1]/"compiled"
    recs=ev.repository_records_by_id(json.loads((C/"repository.json").read_text()))
    cov=json.loads((C/"coverage.json").read_text())
    thin=ev.thin_topics_for(recs)
    g=q=empty=cells=quotes=0
    for m in json.loads((S/f"{w}.json").read_text()):
        e=ev.assemble_evidence(message=m, asks=[{"order":1,"text":m}], canon_questions=cq,
                               coverage=cov, repository_records=recs, thin_topics=thin)
        n=len(e["candidates"]); q+=1; g+=n; cells+=len(e["cells"])
        quotes+=sum(1 for c in e["candidates"] if c["record_type"]=="quote")
        if n==0: empty+=1
    per.append((w,q,g,round(g/q,1),cells,empty,quotes))
    tot_q+=q; tot_g+=g; tot_empty+=empty; tot_cells+=cells
print(f"{'world':7s} {'qs':>3s} {'ground':>7s} {'avg':>5s} {'cells':>6s} {'empty':>6s} {'quotes':>7s}")
for r in per: print(f"{r[0]:7s} {r[1]:3d} {r[2]:7d} {r[3]:5.1f} {r[4]:6d} {r[5]:6d} {r[6]:7d}")
print(f"{'TOTAL':7s} {tot_q:3d} {tot_g:7d} {tot_g/tot_q:5.1f} {tot_cells:6d} {tot_empty:6d} {sum(r[6] for r in per):7d}")
