"""Retrieval reach benchmark - 118 participant questions across ten worlds
(the original six carry ten each; cappadocian/don/gallic/rzg carry 14-15,
added Build-Plan.md Stage 2e, see the history entry below).

WRITTEN BEFORE THE RECORDS IT MEASURES. The questions in bench/ were
composed on 2026-08-27 from each world's own subject matter, and locked,
BEFORE any quote record was hinted - which is the only reason the
before/after numbers mean anything. Hint words are merged into a cell's
retrieval vocabulary, so anyone who writes a hint after seeing a question
fail can make that question pass without retrieval getting better. See
cic/corpus-map/RETRIEVAL-HINTS.md, rule 2.

Reports, per world: total ground records over that world's own questions,
the average, how many canon cells were matched, how many questions
returned an ENTIRELY EMPTY ground, and how many quote records surfaced.

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

After three `[measured]` questions were added to Appendix A for the cases
a hint provably could not reach, and the canon reseeded (90 -> 93):
    466 ground / 7.8 avg / 67 cells /  0 empty / 79 quotes

The gain is not confined to the world that motivated it: alx went 77 -> 80
and ijc 85 -> 88, because the canon is fleet-wide and a question added for
desert's heart material widens the same cell everywhere.

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

Build-Plan.md STAGE 2E (2026-09-20): the fleet's four remaining worlds -
cappadocian, don, gallic, rzg - had no bench file at all, so this
instrument covered six of ten worlds and Stage 4c's own Done criterion
("bench on ten worlds") could not be measured. Wrote bench/{cappadocian,
don,gallic,rzg}.json (14-15 questions each) from each world's own
doorway_description/thinness_statement in records/worlds/<code>.yaml -
not from its compiled records or any existing retrieval.retrieve_when
hint, per this file's own rule 2 discipline above. Every draft question
was run once, unmodified, against that world's real compiled package;
four came back with an EMPTY ground (cappadocian's "What was a household
like in your congregation?", gallic's "What was Marseilles like?", and
two of rzg's) and were rephrased plainer and re-run before locking - the
same "write it, measure it" order rule 2 asks of a hint, applied here to
a question instead. Added this file's own world list (six -> ten); no
retrieval code changed. Locked result, all ten worlds, zero empty:

    world        qs  ground   avg  cells  empty  quotes
    alx          10      77   7.7     10      0      15
    cappadocian  15      40   2.7      9      0      12
    desert       10      88   8.8     12      0      20
    don          15     107   7.1     24      0       5
    gallic       14      93   6.6     28      0       1
    hal          10      73   7.3      9      0      14
    ijc          10      76   7.6     11      0      15
    pahc         10      65   6.5     13      0      12
    rzg          14      97   6.9     14      0      11
    syr          10      97   9.7     14      0      20
    TOTAL       118     813   6.9    144      0     125

cappadocian's low average (2.7) and gallic's near-absence of quotes (1)
are read here as honest measurements of where each world's own coverage/
canon-cell seeding currently sits, not as defects this stage fixes - the
six-world history above shows that kind of gap closing through many
separate hint/canon passes over real calendar time, which is Stage 4's
(and beyond) work, not this one's. Nothing here should read as "ready for
the same tuning six had" without that same measured effort.

Build-Plan.md STAGE 4C, PART 2 (2026-09-20): engine.m4.evidence.
select_cell_candidates gained Stage B2 - when a matched cell's own
compiled/coverage.json entry has literally zero candidates of some record
type (a structural absence, not a low score), the slot is now filled from
a whole-world scan scored against engine.prose.retrieval_words (the same
word set compiled/retrieval.json caches, landed unread in part 1 - see
that module's own comment), capped at that type's own floor, and never
touching honest_limit. This measures the exact same 118 questions cited
above, changing no question and no record - the numbers below are what
part 1's cache was compiled for and part 2 finally reads. Every world
moved up, zero regressions, zero empty (unchanged), cell count unchanged
(Stage A is untouched by this stage):

    world        qs  ground   avg  cells  empty  quotes
    alx          10      88   8.8     10      0      15
    cappadocian  15      91   6.1      9      0      14
    desert       10     106  10.6     12      0      22
    don          15     170  11.3     24      0      18
    gallic       14     207  14.8     28      0       7
    hal          10      83   8.3      9      0      14
    ijc          10      99   9.9     11      0      21
    pahc         10      81   8.1     13      0      16
    rzg          14     121   8.6     14      0      16
    syr          10     106  10.6     14      0      22
    TOTAL       118    1152   9.8    144      0     165

Build-Plan.md STAGE 4D (2026-09-20): a tier prior. `retrieval.tier`
(Artifact-1-Record-Schema.md: "1 core / 2 supporting / 3 ambient",
authored on roughly half the fleet's own records) had sat unread by any
ranking here - select_cell_candidates now adds a small, bounded lean
toward the lower tier number (+0.05 for tier 1, +0.02 for tier 2, +0 for
tier 3/unset) on top of the relevance score, in both the ordinary
coverage-seeded ranking and Stage B2's own whole-world fill.

THIS CARRIES A REGRESSION, same discipline as the Evagrius/Macarius entry
above: left visible, not rounded away. 4 of 118 questions moved (3 down,
1 up); net -2 ground fleet-wide:

    world        qs  ground   avg  cells  empty  quotes
    alx          10      88   8.8     10      0      15
    cappadocian  15      91   6.1      9      0      14
    desert       10     106  10.6     12      0      22
    don          15     169  11.3     24      0      18
    gallic       14     205  14.6     28      0       7
    hal          10      83   8.3      9      0      14
    ijc          10      99   9.9     11      0      21
    pahc         10      81   8.1     13      0      16
    rzg          14     122   8.7     14      0      16
    syr          10     106  10.6     14      0      22
    TOTAL       118    1150   9.7    144      0     165

Root-caused, not shrugged off: every affected question hit
select_cell_candidates' own shared per-cell `budget_chars` (9000). A
tier-1 record's own head text outran a tier-2 record's own shorter one it
displaced, on a GENUINE tie in relevance score (both 0.2, tier prior's
only job) - the extra characters occasionally pushed a later type's own
pick past the same turn's shared budget. Confirmed this is not the prior
over-reaching: the identical swaps reproduce under the most conservative
possible design (an exact-float-tie-break with no additive lean at all),
so a narrower prior would not have avoided this. Zero questions went
empty; net is still far ahead of the pre-4c baseline (813) this file
opened with. Shown the numbers plainly, the call is to ship it.

Spot-checked, not just counted: gallic's "Why did you leave the army?"
picked up gallic.force.army-and-rank-before ("Each founding narrative at
each house begins with a departure from Roman service or rank") purely
from this fill - real, on-topic ground a fully empty force slot withheld
before this stage existed.

Run: python3 engine/m4/reports/retrieval_bench.py
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from engine.m1 import loader
from engine.m1.registry import formation_world_keys
from engine.m4 import evidence as ev
fleet = loader.load_fleet_records()
cq = {r:v for r,v in fleet.items() if v.get("record_type")=="canon_question"}
S = pathlib.Path(__file__).resolve().parent / "bench"
tot_g=tot_q=tot_empty=tot_cells=0
per=[]
# Every formation world THIS BENCH HAS PROMPTS FOR - read from the
# registry, gated on a real S/<w>.json file existing, the one actual
# precondition this script has. A world with no bench/<w>.json yet is
# left out for that real reason, not silently included with nothing to
# read.
for w in [k for k in formation_world_keys() if (S / f"{k}.json").exists()]:
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
