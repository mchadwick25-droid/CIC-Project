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
After the short-query single-word tier:
    394 ground / 6.6 avg / 54 cells /  5 empty / 65 quotes
After adding the participant's own words to the records holding that
material (baptise/baptize/babies/infants, appointed/ordained, pagan
temples, neighbours):
    450 ground / 7.5 avg / 63 cells /  1 empty / 74 quotes

After four questions were added to Appendix A of the Program Spec and
the canon reseeded (86 -> 90):
    459 ground / 7.7 avg / 64 cells /  0 empty / 76 quotes

After the Evagrius and Macarius reading passes, and after those eleven
records' hints were rewritten in participant idiom:
    461 ground / 7.7 avg / 64 cells /  0 empty / 79 quotes

That last line carries a REGRESSION and it is left visible: the reading
pass alone measured 462/80, and rewriting the hints cost one ground record
and one quote in desert (88->87, 18->17). Hint words are merged into a
cell's vocabulary, so a wider hint can displace a candidate that used to
rank; vocabulary bloat is a real cost and this is what it looks like at
small scale. Net across the day is still positive (459/76 -> 461/79) and
no question went empty.

WHAT THE SIXTY CANNOT TELL YOU, and why a second instrument was used. The
sixty were written to measure whether a world's records are REACHABLE AT
ALL. They cannot measure whether a newly opened source informs ordinary
questions ALONGSIDE the existing ones, because none of them was written
about the new material. That question was probed separately (twelve
questions on the interior life, 2026-08-27), and the honest result was
mixed: the new records reached questions using their own vocabulary but
missed three that should plainly have found them. Two of those three are
NOT hint-fixable and are recorded in cic/corpus-map/RETRIEVAL-HINTS.md
under the structural limit - they route to cells the records do not claim,
and rule 4 forbids papering over that with a hint.

NO QUESTION IN THE SIXTY NOW REACHES AN EMPTY GROUND. The last holdout
was pahc's "What did the neighbours think of you?", and it is worth
recording why the canon closed what a hint could not: its words are
`neighbours` and `think`, and a two-word query may be decided by a lone
CANON word but not a lone HINT word. Putting `neighbours` in a hint left
it stranded; putting it in a canon question - F3-E, "What did your
neighbours say about you - what were you accused of?" - made it a word
the router trusts on its own.

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
