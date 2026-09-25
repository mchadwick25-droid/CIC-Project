"""Which canon cells are served WITHOUT a quote or a story, and what can be
done about each.

WHY THIS EXISTS. Program-Spec SS4.2: "A cell is covered when the records
serving it include, wherever the sources hold them, the stories that carry
the answer and the licensed quotes that voice it - never only propositional
records." Nothing measured that. On 2026-08-27 this report found 69 cells
across the fleet served by propositional records alone; nine quotes were
opened that day and it stands at 60.

THE RULING, and its discriminator is empirical rather than a guess. Across
those nine quotes, a record citing a NAMED LOCUS in a VENDORED file had a
quotable sentence sitting at that locus every single time - Justin 1 Apol.
67, 1 Clement 42, Origen Contra Celsum II.56, Jerome Ep. XXII.30, Aphrahat
Demonstration I, Ephrem's Pearl I, and the rest. A record citing "passim",
or a work with no vendored edition, or a modern scholarly study, did not.
So each bare cell is ruled:

  OPENABLE       a serving record names a specific locus in a vendored
                 file. Go and read it; on the evidence so far the quote is
                 there. This is the work-list.
  NEEDS READING  vendored, but the locus is vague ("passim", "the whole
                 collection"). Someone has to read before anyone can say
                 whether a voice exists.
  UNQUOTABLE     nothing vendored stands behind the cell at all - it rests
                 on scholarship or on consult-only editions. The
                 propositional record IS the honest answer here, and no
                 amount of work changes that until a text is acquired.
  LIMIT-ONLY     the cell is served by an honest_limit and nothing else. A
                 limit's job is to name what is missing; it owes no quote.

A cell moving OPENABLE -> served is corpus work. A cell sitting at
UNQUOTABLE is a SOURCING question for a human, not a defect to fix.

VERIFIED BY SAMPLE, not asserted: three OPENABLE rulings were checked by
reading the cited locus (pahc F6-P at Pliny 10.96, hal F3-P at Jerome Ep.
XXII.28, ijc F4-T at Vita Constantini IV.61). All three had quotable text
where the ruling said it would be.

Run: python3 engine/m1/reports/cell_voice.py [--verbose]
"""
import collections
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from engine.m1 import canon, loader
from engine.m1.registry import formation_world_keys

# Originally the six worlds this report first ran against - stale once the
# fleet grew past them (all five later worlds carry canon_cells too, per
# direct measurement; this report had simply never been pointed at them).
# Read off the registry instead (item 2, 2026-09-25 CI/tooling audit) so a
# newly admitted world is covered automatically.
WORLDS = formation_world_keys()

# A locus is VAGUE when it points at a body of text rather than a place in
# one. These are the phrasings the corpus actually uses for that.
# HOW A LOCUS IS JUDGED, and the shape of the rule matters more than the
# pattern in it.
#
# REWRITTEN 2026-08-27 after the enumeration approach under-reported TWICE.
# The first version wanted a keyword before the number ("ch. 4", "Book II")
# and missed the bare ones this corpus mostly uses. It was widened with the
# forms that had been missed - and promptly missed a fresh set: bare Roman
# numerals ("XXII", "I-VII"), letter citations ("Ep. XXVIII", "Epp.
# 135-139"), section marks, pages ("p. 682"), lemmas ("s.v. Papa bar
# Aggai"), structural positions ("praef.", "salutation"). Three more cells
# were openable all along, one of them carrying a locus - "Ep. XXVIII
# (npnf212 line 5099)" - as precise as any in the corpus.
#
# The second failure is the informative one: ENUMERATING SPECIFICITY CANNOT
# WORK. Citation grammar is open-ended, because every edition brings its
# own divisions, so the list is never finished and each widening only moves
# the boundary. What can be tested instead is whether the locus points at a
# PLACE at all, and a place is named with a locator token: a number, a
# Roman numeral, a section mark, a page, a lemma, a named structural
# position. Which grammar those tokens sit in is the edition's business,
# not this pattern's.
#
# So there is one rule. A locus is specific when it carries a locator
# token, and vague when it carries none. The old vocabulary falls out of it
# rather than being listed: "passim", "the whole collection", "the
# exile-years letters", "the polemic's own harshness" all name bodies of
# text, and none of them contains a locator.
#
# Two attempts that were tried and rejected, recorded so they are not tried
# again. Listing vague head-nouns ("the ... corpus/letters/tradition")
# fires on the descriptive glosses this corpus attaches to precise
# citations - "Canon XXVIII (the claim contested in the conciliar record)"
# is not vague. Stripping those glosses first fixes that and breaks
# something worse, because parentheses here also carry REAL loci:
# "the withdrawal narrative (SS3-14)", "the Ephraim chapter (file line
# 471)". One test over the whole string misrules one locus in 1242; each
# of the cleverer versions misruled thirty or more.
_SPECIFIC = re.compile(
    r"\d"                                   # any number: 42, 10.96, line 5099
    r"|\b[IVXLC]+\b"                        # a Roman numeral standing alone
    r"|SS|\u00a7"                            # section marks
    r"|\bs\.\s?v\.|\bpp?\."                # a lemma; a page
    r"|\bpraef|\bpreface|\bsalutation|\bfront matter|\btitle page"
    r"|\bopening\b|\bclosing\b")


def _vendored_sources(records):
    return {
        rid for rid, rec in records.items()
        if rec.get("record_type") == "source"
        and "cic/texts/" in " ".join(str(rec.get("edition") or "").split())
    }


def rule_cell(cell, records, vendored):
    """One cell's verdict, plus the loci that justify it."""
    classified = canon.classify_cell(cell, records)
    ids = (classified.get("substantive") or []) + (classified.get("honest_limit") or [])
    if not ids:
        return None
    kinds = {records[i]["record_type"] for i in ids if i in records}
    if kinds & {"quote", "story"}:
        return None

    openable, vague, unbacked = [], [], []
    for record_id in ids:
        for source in (records.get(record_id) or {}).get("sources") or []:
            if not isinstance(source, dict):
                continue
            sid = source.get("source_id", "")
            locus = " ".join(str(source.get("locus") or "").split())
            where = f"{record_id} <- {sid.split('.')[-1]}"
            if sid not in vendored:
                unbacked.append(where)
            elif _SPECIFIC.search(locus):
                openable.append((where, locus))
            else:
                # names a body of text, not a place in one: someone must read
                vague.append(where)

    if not (openable or vague):
        verdict = "UNQUOTABLE"
    elif not (classified.get("substantive") or []) and not openable:
        verdict = "LIMIT-ONLY"
    elif openable:
        verdict = "OPENABLE"
    else:
        verdict = "NEEDS READING"
    return verdict, openable, unbacked


def main(verbose=False):
    fleet = loader.load_fleet_records()
    tally = collections.Counter()
    per_world = collections.defaultdict(list)
    for world in WORLDS:
        records = loader.load_world_records(world)
        vendored = _vendored_sources(records)
        for cell in sorted(canon.valid_cells(fleet)):
            ruled = rule_cell(cell, records, vendored)
            if not ruled:
                continue
            verdict, openable, unbacked = ruled
            tally[verdict] += 1
            per_world[world].append((cell, verdict, openable, unbacked))

    total = sum(tally.values())
    print(f"{total} cells served without a quote or story\n")
    for verdict in ["OPENABLE", "NEEDS READING", "UNQUOTABLE", "LIMIT-ONLY"]:
        if tally[verdict]:
            print(f"  {tally[verdict]:3}  {verdict}")
    print()
    for world in WORLDS:
        rows = per_world[world]
        if not rows:
            continue
        counts = collections.Counter(r[1] for r in rows)
        print(f"{world:7} {len(rows):2}  " + ", ".join(f"{v} {k.lower()}" for k, v in counts.most_common()))
        if verbose:
            for cell, verdict, openable, unbacked in rows:
                print(f"    {cell:6} {verdict}")
                for where, locus in openable[:2]:
                    print(f"           -> {where}  [{locus[:64]}]")
                if not openable and unbacked:
                    print(f"           (unbacked: {', '.join(sorted(set(unbacked))[:2])})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(verbose="--verbose" in sys.argv))
