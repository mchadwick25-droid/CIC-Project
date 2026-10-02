#!/usr/bin/env python3
"""Ask the vendored corpus what it holds for one world and one canon cell.

THE PROBLEM THIS EXISTS FOR. 61 of the fleet's 168 world-cells answer from a
single record, and every one passes the M1 coverage gate, because that gate
asks whether a cell has >=1 substantive record and stops. Presence, not depth.
That is why `desert` answered "who is Jesus" with one witness: cell C-I was
green with exactly one record in it, and nothing anywhere had ever asked what
the corpus actually held for that cell.

Nothing has ever asked. Build threads reached for the sources they already
knew; no tool could answer "what does this corpus contain for Alexandria on
cell F2-P?" This is that tool.

A BUILDER'S TOOL, NOT A RUNTIME PATH - and the distinction is deliberate.
engine/m4 retrieves only over a world's compiled records, every one of which
carries `register` (is this the world's own voice?), `confidence`, a rights-
checked source and a citable id. A raw passage has none of those. Wiring the
texts straight into a turn would produce fuller answers that are less
checkable, which trades away the exact thing that makes this project's answers
worth having. So this searches the texts to tell a HUMAN what records are
missing; the records still mediate everything a participant ever meets.

Scope comes from the corpus map, never from this file: a world's in-scope
files are those its Atlas entry (`cic/corpus-map/<census_id>.yaml`) has
assigned a work from, and the cell vocabulary is
the fleet's own canon_question keyword corpus
(engine.m1.canon.cell_keywords), the identical derivation Stage A scores a
live turn against.

STATUS: PROTOTYPE. The mechanism works - it reads the corpus, scopes by the
world's own review, scores against the fleet's cell vocabulary, and returns
real prose. The results are not yet usable, for three reasons:

  1. Scope is real and now populated for most worlds. The corpus map scopes
     by addition, so a world searches the files its Atlas entry assigned;
     65 of the 68 map files carry at least one work (desert-monasticism
     alone now holds 27). A world with no map file yet still falls back to
     the whole corpus and says so on stderr.

  2. The cell vocabulary is conversational, not theological. It derives from
     the canon_question texts - "Who was Jesus, to you and your people?" -
     which yields {believe, people, good, make, teach}. Those words find
     prose about anything. Finding Christology needs a theological index
     vocabulary per cell, which the fleet does not have and which is a real
     piece of work, not a tuning pass.

  2b. Scope is per FILE, the map is per WORK. `desert-monasticism.yaml`
     assigns Athanasius' Vita Antonii from `npnf204`, not his De Synodis -
     but the probe can only include or exclude whole files, so De Synodis
     comes back too (it does, on C-I, second). Honouring the per-work ruling
     needs the locus work in (3): once a chunk knows which `div1` it came
     from, the map's `locus` field becomes a filter. Until then file-level
     scope is an over-approximation, and knowing which way it errs matters
     more than the error.

  3. Passages carry no locus. The chunker splits on blank lines after
     stripping tags, so a promising hit cannot be cited without a human going
     back to find book and section. A real chunker would walk the ThML div
     structure and carry the reference down - the same structure
     corpus_authors.py already reads for attribution.

Until at least (2) is addressed this finds prose, not arguments.

    python cic/engine/corpus_probe.py desert C-I
    python cic/engine/corpus_probe.py alx F2-P --limit 5
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from engine.m1 import canon  # noqa: E402
from engine.m1.loader import load_fleet_records, load_world_records  # noqa: E402
from engine.m1.registry import load_registry  # noqa: E402
from engine.prose import content_words  # noqa: E402

sys.path.insert(0, str(REPO_ROOT / "cic" / "engine"))
from corpus_authors import build_index  # noqa: E402

TEXTS_DIR = REPO_ROOT / "cic" / "texts"

_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")
# A paragraph short enough to be noise (a heading, a page number, a stray
# footnote marker) carries no argument and would crowd out real passages.
_MIN_PASSAGE_WORDS = 40

# Editorial apparatus reads as keyword-dense because a table of contents names
# every subject in the volume at once. A first pass ranked Hilary's contents
# page top for desert's Christology cell. These are the shapes that produce it.
_APPARATUS_MARKERS = re.compile(
    r"(table of contents|index of|introductory note|translator|elucidation|"
    r"bibliograph|the life and writings of|chapter [ivxl]+\.—the (life|theology)|"
    r"english translation|pp\. \d+-\d+|\bpage \d+|gallandi|migne|bibl\. vet)", re.I)

# A contents listing is many short fragments joined by periods; real prose runs
# in sentences. Measured on the noise this filter was written against: the
# Hilary contents page averages under 6 words per period-delimited run, an
# actual argument averages well over 12.
def _is_prose(text: str) -> bool:
    runs = [r for r in re.split(r"[.;]", text) if r.strip()]
    if not runs:
        return False
    return sum(len(r.split()) for r in runs) / len(runs) >= 10


def passages(path: Path):
    """Yield (approximate_paragraph_index, text) for one vendored file.

    Deliberately crude: strip markup, split on blank lines, drop the short
    fragments. A real chunker would respect div structure and carry loci, and
    that is worth building - but the question this answers first is whether
    the corpus holds relevant material at all, and a crude splitter answers
    that honestly. It cannot invent a passage that is not there.
    """
    raw = path.read_text(encoding="utf-8", errors="replace")
    body = _TAG.sub(" ", raw)
    for i, chunk in enumerate(re.split(r"\n\s*\n", body)):
        text = _WS.sub(" ", chunk).strip()
        if len(text.split()) < _MIN_PASSAGE_WORDS:
            continue
        if _APPARATUS_MARKERS.search(text[:400]) or not _is_prose(text):
            continue
        yield i, text


def in_scope_files(world_key: str) -> dict[str, list[str]]:
    """file -> the authors in it, for every file this world's Atlas entry has
    assigned a work from.

    Reads `cic/corpus-map/<census_id>.yaml` and scopes by ADDITION: an entry
    with two works assigned searches two files, not forty-six - never by
    subtraction over every file not explicitly declined, which would search
    everything the moment nothing has been declined.

    A world whose map file does not exist yet falls back to the whole corpus
    and says so. That is the honest default - an unwritten map is not a claim
    that nothing is in scope - but it still means nothing is filtered, so the
    caller is told which of the two it got.
    """
    import yaml

    registry = load_registry()
    census_id = (registry.get(world_key) or {}).get("census_id")
    map_file = REPO_ROOT / "cic" / "corpus-map" / f"{census_id}.yaml"
    authors, per_file = build_index()
    corpus = {name for name in per_file if (TEXTS_DIR / name).suffix in (".xml", ".txt")}

    if census_id and map_file.is_file():
        doc = yaml.safe_load(map_file.read_text(encoding="utf-8")) or {}
        assigned = {w.get("source_file") for w in (doc.get("works") or []) if isinstance(w, dict)}
        scoped = corpus & assigned
        if scoped:
            print(f"scope: {len(scoped)} file(s) from {census_id}.yaml", file=sys.stderr)
            corpus = scoped
    else:
        print(f"scope: NO corpus map for {world_key!r} - searching all {len(corpus)} vendored "
              f"file(s), so hits from outside this world are expected", file=sys.stderr)

    return {
        name: sorted({a for a, v in authors.items() if name in v["files"]})
        for name in corpus
    }


def probe(world_key: str, cell: str, limit: int = 8) -> list[dict]:
    fleet = load_fleet_records()
    vocabulary = canon.cell_keywords(fleet).get(cell)
    if not vocabulary:
        raise SystemExit(f"cell {cell!r} is not in the canon")

    scored = []
    for name, authors in sorted(in_scope_files(world_key).items()):
        for index, text in passages(TEXTS_DIR / name):
            shared = vocabulary & content_words(text)
            if len(shared) < 3:
                continue
            # Overlap coefficient against the cell vocabulary, the same metric
            # engine.m4.evidence uses to rank a live turn's candidates - so a
            # passage that scores well here is one the retrieval layer would
            # also have favoured, had a record ever carried it.
            # Density against the PASSAGE, not the overlap coefficient. The
            # coefficient divides by whichever side is smaller, so a passage
            # naming many subjects briefly beat a passage arguing one at
            # length - exactly backwards for finding material worth a record.
            words = content_words(text)
            score = len(shared) / max(len(words), 1) * (len(shared) ** 0.5)
            scored.append({"file": name, "authors": authors, "index": index,
                           "score": round(score, 3), "shared": sorted(shared), "text": text})
    scored.sort(key=lambda entry: (-entry["score"], entry["file"], entry["index"]))
    return scored[:limit]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python cic/engine/corpus_probe.py")
    parser.add_argument("world_key")
    parser.add_argument("cell")
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args(argv)

    records = load_world_records(args.world_key)
    held = canon.classify_cell(args.cell, records)
    print(f"{args.world_key} · cell {args.cell}")
    print(f"  currently answered by {len(held['substantive'])} record(s): "
          f"{', '.join(held['substantive']) or '— none —'}\n")

    hits = probe(args.world_key, args.cell, args.limit)
    if not hits:
        print("  no passage in this world's in-scope corpus clears the floor for this cell.")
        return 0
    print(f"  {len(hits)} candidate passage(s) in the corpus, best first:\n")
    for hit in hits:
        who = ", ".join(hit["authors"]) or "unattributed"
        print(f"  [{hit['score']:.3f}] {hit['file'].split('_')[0]} ({who})")
        print(f"          on: {', '.join(hit['shared'][:8])}")
        print(f"          {hit['text'][:300]}…\n")
    print("  These are CANDIDATES for a human to turn into records, never ground for a turn.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
