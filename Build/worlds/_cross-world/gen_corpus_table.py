"""Generates CORPUS-USE.md: the corpus Mark supplied, against what each world
actually draws on.

The chain this walks, and why it is three hops rather than one: a vendored
file under cic/texts/ is named by a `source` record's own `edition` field
(the same literal-path convention cic/engine/texts_registry.py already scans
for), and CONTENT records reach that file only indirectly, by naming the
source record in their own `sources[].source_id`. Counting citations of the
file path alone would report the source records - a handful per file - and
miss the thing worth knowing, which is how much of a world's actual claim
surface rests on text the pipeline can verify offline.

That distinction is the point of the report. A record backed by a vendored
file can have its wording checked by any session at any time with no network
(cic/texts/README.md's own stated reason for existing). A record backed by a
consult-only source - Rubenson on Antony's Letters, Bamberger on Evagrius,
Ward on the Sayings - cannot, because redistributing those editions would be
copyright infringement, so the build carries the bibliography without the
text. Both are legitimate. Only one is verifiable.

Non-use is NOT read as a defect here and the report says so on its face: no
world should draw on every volume in a shared corpus, and a Syriac world has
no business in Chrysostom on Corinthians. What the table is for is letting a
human see, per world, where the corpus already in hand is going unread -
which is a different question from whether the record is thin.

    python Build/worlds/_cross-world/gen_corpus_table.py
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from engine.m1.loader import RECORDS_ROOT, load_world_records  # noqa: E402

# The registry itself, never its generated README. An earlier draft parsed the
# markdown table and silently lost 9 of 46 rows to titles the split mangled,
# reporting "36 of 37 supplied by Mark" instead of 45 of 46.
sys.path.insert(0, str(ROOT / "cic" / "engine"))
import texts_registry  # noqa: E402

# The corpus-scope tables live with the standing check that also reads them
# (engine/m1/cross_world.py). A second copy here is exactly how this report
# would come to disagree with the check it exists to illustrate.
from engine.m1.cross_world import BY_DESIGN, COVERAGE, corpus_key as key_for, corpus_tier  # noqa: E402
from engine.m1.cross_world import observe_second_hand_sources  # noqa: E402
from engine.m1 import registry as world_registry  # noqa: E402

TEXTS_DIR = ROOT / "cic" / "texts"
# Every formation world with compiled records, not a hand-maintained list -
# the prior hardcoded six (alx/pahc/desert/hal/syr/ijc) silently stopped
# covering cappadocian, gallic, and don as each was admitted, so this report
# went stale for three of the fleet's nine live worlds without ever saying so.
W = [w for w in world_registry.formation_world_keys()
     if (RECORDS_ROOT / w).is_dir()]

# Short subject labels, so a reader can tell a meaningful gap from a correct
# one without opening the volume. Taken from each file's own README title.
SUBJECT = {
    "addai": "Syriac: Doctrine of Addai",
    "anf01": "Apostolic Fathers, Justin, Irenaeus",
    "anf02": "Hermas, Tatian, Clement of Alexandria",
    "anf03": "Tertullian",
    "anf04": "Tertullian, Minucius Felix, Origen",
    "anf05": "Hippolytus, Cyprian, Novatian",
    "anf06": "Gregory Thaumaturgus, Dionysius, Methodius",
    "anf07": "Lactantius, Didache, liturgies",
    "anf08": "Twelve Patriarchs, Clementina, Syriac Edessa",
    "anf09": "Gospel of Peter, Diatessaron, Origen",
    "anf10": "bibliographic index (reference only)",
    "aphrahat": "Syriac: Aphrahat, Demonstrations 2-7",
    "chronicle-of-edessa": "Syriac: Chronicle of Edessa",
    "ephraim": "Syriac: Ephrem, Prose Refutations",
    "npnf101": "Augustine: Confessions, Letters",
    "npnf102": "Augustine: City of God",
    "npnf103": "Augustine: Trinity, moral treatises",
    "npnf104": "Augustine: anti-Manichaean/Donatist",
    "npnf105": "Augustine: anti-Pelagian",
    "npnf106": "Augustine: Sermon on the Mount, homilies",
    "npnf107": "Augustine: homilies on John",
    "npnf108": "Augustine: Psalms",
    "npnf109": "Chrysostom: priesthood, ASCETIC homilies",
    "npnf110": "Chrysostom: Matthew",
    "npnf111": "Chrysostom: Acts, Romans",
    "npnf112": "Chrysostom: Corinthians",
    "npnf113": "Chrysostom: Galatians-Philemon",
    "npnf114": "Chrysostom: John, Hebrews",
    "npnf201": "Eusebius: Church History",
    "npnf202": "Socrates, Sozomen: histories",
    "npnf203": "Theodoret, Jerome, Gennadius, Rufinus",
    "npnf204": "Athanasius (incl. Vita Antonii)",
    "npnf205": "Gregory of Nyssa: dogmatic treatises",
    "npnf206": "Jerome (incl. desert Lives)",
    "npnf207": "Cyril of Jerusalem, Gregory Nazianzen",
    "npnf208": "Basil: letters and select works (ASCETIC)",
    "npnf209": "Hilary, John of Damascus",
    "npnf210": "Ambrose",
    "npnf211": "Sulpitius Severus, Cassian (incl. De Incarnatione)",
    "npnf212": "Leo the Great, Gregory the Great",
    "npnf213": "Gregory the Great, Ephrem, Aphrahat",
    "npnf214": "The Seven Ecumenical Councils",
    "optatus": "Optatus: Against the Donatists",
    "origen": "Origen: Philocalia",
    "palladius": "Palladius: Lausiac History (DESERT)",
    "webbe": "World English Bible",
}


# Why a file is unread, where there is a real basis for saying. Everything
# absent from this map is reported as NOT YET REVIEWED rather than assumed
# correct - guessing a volume's relevance is a scholarly judgment this script
# has no standing to make.
DISPOSITION = {
    "webbe": ("by design",
              "Mark's ruling, 2026-08-26: scripture is in the corpus only as the authors "
              "themselves used it. This project does not interpret the Bible directly, so "
              "nothing should ever cite this file as a source of its own."),
    "anf10": ("by design", "a bibliographic index, not a text - nothing to cite."),
    "npnf205": ("IN WINDOW, UNREAD",
                "Gregory of Nyssa (d. 395) is inside five of the six worlds' windows and is "
                "named in zero records anywhere in the fleet."),
    "npnf207": ("IN WINDOW, UNREAD",
                "Gregory Nazianzen (d. 390) is named in alx (2 records) and ijc (1) and cited "
                "from this volume by neither; Cyril of Jerusalem (d. 386) is named nowhere, "
                "though his Catechetical Lectures are the central 4th-century catechesis text "
                "and alx is the catechetical world."),
    "npnf208": ("IN WINDOW, UNREAD",
                "Basil (d. 379) is named in alx (2), syr (2), desert (1) and ijc (1) - every "
                "world whose window covers him except hal - and cited from his own works by "
                "none of them. desert reaches him only through Palladius."),
}


def subject_for(filename: str) -> str:
    key = re.split(r"[_.]", filename)[0]
    return SUBJECT.get(key, "—")


def main() -> None:
    files = sorted(p.name for p in TEXTS_DIR.iterdir() if p.suffix in (".xml", ".txt") and p.name != "README.md")

    # hop 1: vendored file -> the source records that name its literal path.
    # A dumb full-text scan, exactly as cic/engine/texts_registry.py does it -
    # schema-agnostic, and it cannot drift out of date the way a hand-kept
    # "covers" field would.
    file_to_sources: dict[str, set[str]] = defaultdict(set)
    for record_path in RECORDS_ROOT.rglob("*.md"):
        text = record_path.read_text(encoding="utf-8", errors="replace")
        for filename in files:
            if f"cic/texts/{filename}" in text:
                file_to_sources[filename].add(record_path.stem)

    records = {w: load_world_records(w) for w in W}

    # hop 2+3: source record -> the content records citing it, per world.
    counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    backed: dict[str, set[str]] = defaultdict(set)
    for w in W:
        by_source: dict[str, list[str]] = defaultdict(list)
        for rid, rec in records[w].items():
            for ref in rec.get("sources") or []:
                if ref.get("source_id"):
                    by_source[ref["source_id"]].append(rid)
        for filename, source_ids in file_to_sources.items():
            reached = {rid for sid in source_ids for rid in by_source.get(sid, [])}
            if reached:
                counts[filename][w] = len(reached)
                backed[w] |= reached

    by_mark = sum(1 for e in texts_registry.ENTRIES if e.supplied_by == "Mark")
    out = ["# The supplied corpus, against what each world draws on\n"]
    out.append(
        "Generated by `gen_corpus_table.py` from the live tree. `cic/texts/` holds "
        f"**{len(files)} vendored files, {by_mark} of them supplied by Mark** — the agents' sandbox "
        "blocks every patristic text host (ccel.org, archive.org, wikisource, gutenberg, "
        "newadvent, tertullian.org), so nothing here was ever fetched by a build thread.\n"
    )
    out.append(
        "**A blank cell is not a defect.** No world should draw on every volume in a shared "
        "corpus. The table is here so a human can see where text already in hand is going "
        "unread — a different question from whether a world's record is thin.\n"
    )

    # --- verifiability summary -------------------------------------------
    out.append("\n## How much of each world rests on text the pipeline can verify\n")
    out.append(
        "A record backed by a vendored file can have its wording re-checked by any session, "
        "offline. A record backed only by a consult-only edition (Rubenson, Bamberger, Ward) "
        "carries the bibliography without the text, because redistributing those editions "
        "would be infringement. Both are legitimate; only one is checkable.\n"
    )
    out.append("| world | records | with any source | backed by a vendored file | share of sourced records |")
    out.append("|---|---|---|---|---|")
    for w in W:
        total = len(records[w])
        sourced = sum(1 for r in records[w].values() if r.get("sources"))
        n = len(backed[w])
        pct = f"{round(100 * n / sourced)}%" if sourced else "—"
        out.append(f"| `{w}` | {total} | {sourced} | {n} | **{pct}** |")

    # --- the matrix -------------------------------------------------------
    out.append("\n## File by world\n")
    out.append("Cell = how many of that world's records reach that file through a source record.\n")
    out.append("| vendored file | subject | " + " | ".join(f"`{w}`" for w in W) + " |")
    out.append("|---|---|" + "---|" * len(W))
    for filename in files:
        row = counts.get(filename, {})
        cells = " | ".join(str(row.get(w, "·")) for w in W)
        name = filename if len(filename) <= 46 else filename[:43] + "…"
        out.append(f"| `{name}` | {subject_for(filename)} | {cells} |")

    # --- the unread shelf, sorted by whether that is a problem -------------
    unread = [f for f in files if not counts.get(f)]
    buckets: dict[str, list[str]] = defaultdict(list)
    for filename in unread:
        key = re.split(r"[_.]", filename)[0]
        verdict, why = DISPOSITION.get(key, ("not yet reviewed", ""))
        buckets[verdict].append((filename, why))

    out.append(f"\n## Reached by no world — {len(unread)} of {len(files)}\n")
    out.append(
        "Sorted by whether that is a problem. A flat list of unread volumes invites the "
        "wrong reading: most of these are correctly unread, and the few that are not "
        "should not have to be found by eye.\n"
    )
    for verdict in ("IN WINDOW, UNREAD", "by design", "not yet reviewed"):
        rows = buckets.get(verdict)
        if not rows:
            continue
        out.append(f"\n### {verdict} — {len(rows)}\n")
        if verdict == "not yet reviewed":
            out.append(
                "No basis recorded either way. Most are plainly out of every world's window "
                "or geography; this script does not assume so on their behalf.\n"
            )
        for filename, why in rows:
            out.append(f"- `{filename}` — {subject_for(filename)}" + (f"  \n  {why}" if why else ""))
    out.append("")

    # --- the worklist Mark's "ranked, never ignored" standard implies ------
    reg = world_registry.load_registry()
    out.append("\n## Worklist — in scope for a world, with no source record there\n")
    out.append(
        "Mark's standard, 2026-08-26: *every world should reach every available resource; "
        "they can be ranked, but not ignored.* A volume becomes in-scope for a world when "
        "its coverage range overlaps that world's `time_window`.\n"
    )
    out.append(
        "**The runtime cannot close this gap by ranking.** `engine/m4` never opens a file "
        "under `cic/texts/` — retrieval runs entirely over the world's own "
        "`compiled/repository.json`. A volume with no source record in a world is invisible "
        "at turn time whatever the ranking does, so 'not ignored' has to mean a source "
        "record exists (even a low-ranked one), not a retrieval change.\n"
    )
    out.append(
        "Coverage ranges below are a **first pass asserted for correction**, not derived — "
        "a volume's dates cannot be read off the file mechanically. Argue with them.\n"
    )
    # tier 1 comes from the standing check itself, so this report and
    # `python -m engine.m1.cross_world` can never disagree about it.
    second_hand_by_world = {
        f.scope: re.findall(r"[\w.-]+\.(?:xml|txt)", f.message)
        for f in observe_second_hand_sources(records=records, worlds=W)
    }
    out.append(
        "Geography was added on Mark's ruling and **ranks rather than excludes** — the "
        "standard is that a resource may be ranked low and never dropped. Tier 1 is the one "
        "derived signal here; tiers 2-4 rest on the asserted COVERAGE and REGIONS tables in "
        "`engine/m1/cross_world.py`, which are a first pass for correction.\n"
    )
    out.append("| tier | what it means |")
    out.append("|---|---|")
    out.append("| **1 — named, never opened** | this world's records already name the author and have never opened their works. Derived, not asserted. |")
    out.append("| **2 — same time and place** | coverage overlaps the window *and* the region (or the volume is ecumenical). |")
    out.append("| **3 — same time, different region** | in the window, outside the world's own geography. Rank low; do not drop. |")
    out.append("| **4 — outside this window** | coverage checked, no time overlap. Lowest rank. |")
    out.append("| **4 — unclassified** | no COVERAGE entry for the volume, so no date judgement has been made. "
               "NOT a finding of no overlap — these need dates entered in `engine/m1/cross_world.py`. |")
    out.append("")

    tiers = ("1 - named, never opened", "2 - same time and place",
             "3 - same time, different region", "4 - outside this window", "4 - unclassified")
    per_world = {}
    for w in W:
        win = reg[w]["time_window"]
        named = set(second_hand_by_world.get(w, []))
        buckets = defaultdict(list)
        for filename in files:
            if key_for(filename) in BY_DESIGN or counts.get(filename, {}).get(w):
                continue
            buckets[corpus_tier(filename, w, win, named=filename in named)].append(filename)
        per_world[w] = buckets

    out.append("| world | window | sourced | tier 1 | tier 2 | tier 3 | tier 4 | unclassified |")
    out.append("|---|---|---|---|---|---|---|---|")
    for w in W:
        b = per_world[w]
        sourced = sum(1 for f in files if counts.get(f, {}).get(w))
        t4 = len(b.get("4 - outside this window", []))
        t4u = len(b.get("4 - unclassified", []))
        out.append(f"| `{w}` | {reg[w]['time_window']['start']}–{reg[w]['time_window']['end']} | {sourced} | "
                   f"**{len(b.get(tiers[0], []))}** | {len(b.get(tiers[1], []))} | {len(b.get(tiers[2], []))} | {t4} | {t4u} |")

    for w in W:
        b = per_world[w]
        out.append(f"\n### `{w}`\n")
        for tier in tiers[:3]:
            rows = b.get(tier)
            if not rows:
                continue
            out.append(f"**Tier {tier}** — {len(rows)}\n")
            for filename in sorted(rows):
                lo, hi = COVERAGE.get(key_for(filename), (None, None))
                span = f"({lo}–{hi}) " if lo else ""
                out.append(f"- `{filename}` {span}— {subject_for(filename)}")
            out.append("")
        outside = sorted(b.get(tiers[3], []))
        if outside:
            out.append(f"Tier 4, outside this window — {len(outside)}: "
                       + ", ".join(f"`{key_for(f)}`" for f in outside) + "\n")
        uncl = sorted(b.get(tiers[4], []))
        if uncl:
            out.append(f"Tier 4, unclassified (no COVERAGE entry — no date judgement made) — {len(uncl)}: "
                       + ", ".join(f"`{key_for(f)}`" for f in uncl) + "\n")

    target = Path(__file__).resolve().parent / "CORPUS-USE.md"
    target.write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
