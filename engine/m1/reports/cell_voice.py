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

WORLDS = ["alx", "pahc", "hal", "syr", "ijc", "desert"]

# A locus is VAGUE when it points at a body of text rather than a place in
# one. These are the phrasings the corpus actually uses for that.
_VAGUE = re.compile(
    r"passim|whole (file|work|collection|volume|letter)|scattered|throughout|"
    r"the collections? as a whole|entire|no vendored|consult-only", re.I)
# ...and SPECIFIC when it names a section, chapter, book, letter or line.
_SPECIFIC = re.compile(
    r"\bSS?\s?\d|\b[IVXLC]{1,6}\.\s?\d|\bch(?:ap)?\.?\s*[IVXLC\d]|\bBook\s+[IVXLC\d]|"
    r"\bsecs?\.\s*\d|\bletter\s+[IVXLC\d]|\b\d+[.:]\d+|file line \d|"
    r"Hymn\s+[IVXLC\d]|Demonstration\s+[IVXLC]", re.I)


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
            elif _VAGUE.search(locus) or True:
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
