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

    python world-build-docs/_cross-world/gen_corpus_table.py
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

TEXTS_DIR = ROOT / "cic" / "texts"
W = ["alx", "pahc", "desert", "hal", "syr", "ijc"]

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

    # --- the unread shelf --------------------------------------------------
    unread = [f for f in files if not counts.get(f)]
    out.append(f"\n## Reached by no world — {len(unread)} of {len(files)}\n")
    for filename in unread:
        out.append(f"- `{filename}` — {subject_for(filename)}")
    out.append("")

    target = Path(__file__).resolve().parent / "CORPUS-USE.md"
    target.write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
