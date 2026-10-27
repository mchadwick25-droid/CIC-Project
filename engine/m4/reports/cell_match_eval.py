"""Cell-matching instruments, offline, no model call.

Three measures per world, run against the matcher as the checkout has it, so
a change is shown by running this on the base and on the branch and comparing
the two JSON files:

  hint recall   each record's own `retrieve_when` entry, with its leading
                "participant asks" taken off, asked as a question; a hit when
                one of the record's `canon_cells` is among the cells returned.
  canon         each canon question asked with the world's records; a hit when
                its own cell is among the cells returned.
  bench         the questions in bench/<world>.json run through
                engine.m4.evidence.assemble_evidence on the world's newest
                package: ground records, empty grounds, quote records, and the
                cells each question reached.

The hint-recall questions are the hints themselves, so that measure shows
whether the cell that names a question comes back when competitors exist, not
how well unseen questions do; the bench is the independent set.

Needs the compiled packages (`python -m engine.m2.cli restore`).

Usage: python engine/m4/reports/cell_match_eval.py out.json
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from engine.m1 import loader
from engine.m1.registry import formation_world_keys
from engine.m4 import evidence as ev

BENCH = pathlib.Path(__file__).resolve().parent / "bench"
FRAME = re.compile(
    r"^\s*(?:a\s+)?(?:participant|visitor|user|someone)\s+(?:asks?|says?|mentions?|wants?|raises?|names?|brings? up|is asking)"
    r"\s*(?:about|for|what|whether|if|how|why)?\s*", re.I,
)


def _worlds() -> list[str]:
    keys = {*formation_world_keys(), *(p.stem for p in BENCH.glob("*.json"))}
    return sorted(w for w in keys if pathlib.Path(f"records/{w}").is_dir() and any(pathlib.Path(f"packages/{w}").glob("*")))


def _cells(question, canon, records):
    matches = ev.match_asks_to_cells(
        message=question, asks=[{"order": 1, "text": question}], canon_questions=canon, repository_records=records,
    )
    return {m["cell"].split("|")[0] for m in matches}


def hint_recall(records, canon):
    total = hits = 0
    misses = []
    for rid, record in records.items():
        cells = set(record.get("canon_cells") or [])
        for hint in (record.get("retrieval") or {}).get("retrieve_when") or []:
            question = FRAME.sub("", hint).strip()
            if not cells or len(ev._query_words(question, None)) < 2:
                continue
            got = _cells(question, canon, records)
            total += 1
            if got & cells:
                hits += 1
            else:
                misses.append([rid, question[:70], sorted(got)])
    return {"total": total, "hit": hits, "misses": misses}


def canon_self(records, canon):
    asked = [r for r in canon.values() if r.get("cell")]
    return {"total": len(asked), "hit": sum(r["cell"] in _cells(r["text"], canon, records) for r in asked)}


def bench(world, canon):
    package = sorted(pathlib.Path(f"packages/{world}").iterdir())[-1] / "compiled"
    records = ev.repository_records_by_id(json.loads((package / "repository.json").read_text()))
    coverage = json.loads((package / "coverage.json").read_text())
    thin = ev.thin_topics_for(records)
    out = {"qs": 0, "ground": 0, "empty": 0, "quotes": 0, "cells": []}
    for question in json.loads((BENCH / f"{world}.json").read_text()):
        found = ev.assemble_evidence(
            message=question, asks=[{"order": 1, "text": question}], canon_questions=canon,
            coverage=coverage, repository_records=records, thin_topics=thin,
        )
        out["qs"] += 1
        out["ground"] += len(found["candidates"])
        out["empty"] += not found["candidates"]
        out["quotes"] += sum(c["record_type"] == "quote" for c in found["candidates"])
        out["cells"].append([c["cell"] for c in found["cells"]])
    return out


def main(path: str) -> None:
    fleet = loader.load_fleet_records()
    canon = {rid: r for rid, r in fleet.items() if r.get("record_type") == "canon_question"}
    result = {"hint_recall": {}, "canon": {}, "bench": {}}
    for world in _worlds():
        records = loader.load_world_records(world)
        result["hint_recall"][world] = hint_recall(records, canon)
        result["canon"][world] = canon_self(records, canon)
        if (BENCH / f"{world}.json").exists():
            result["bench"][world] = bench(world, canon)
    pathlib.Path(path).write_text(json.dumps(result, indent=1))
    for world in result["hint_recall"]:
        h, c, b = result["hint_recall"][world], result["canon"][world], result["bench"].get(world, {})
        print(f"{world:12s} hints {h['hit']}/{h['total']}  canon {c['hit']}/{c['total']}  ground {b.get('ground')}  empty {b.get('empty')}  quotes {b.get('quotes')}")


if __name__ == "__main__":
    main(sys.argv[1])
