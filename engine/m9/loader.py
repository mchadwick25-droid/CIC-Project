"""The ONLY place in engine/m9/ that touches cic/corpus-map/ and
cic/texts/ (Library Access Gate D3 SS1.3). Lifts the import pattern
engine/m1/cross_world.py:940 already uses (sys.path.insert(cic/engine);
from corpus_map import load) WITHOUT the try/except that lets that
observer swallow failure - a gate cannot (D2 SS1.3(b)). Reads bucket rows
with corpus_map.load(), pair rulings from cic/corpus-map/PAIRS.yaml,
and passage units with corpus_index.passage_units() - the same extractor
Q7-B and Q7-I5 both reused. Nothing else in engine/m9/ touches the
filesystem; everything downstream of this module is pure.

Exposed as small, separately-callable pieces (not just one load_shelf())
so engine/m9/selftest.py can mutate one raw piece - a bucket row, a
PAIRS.yaml entry - in memory before it ever becomes a Shelf, per
fixtures/seeded_defects.yaml's target_kind: bucket | pairs (this
increment's own extension to that catalog's mutation vocabulary).
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
CIC_ENGINE_DIR = REPO_ROOT / "cic" / "engine"
TEXTS_DIR = REPO_ROOT / "cic" / "texts"
PAIRS_PATH = REPO_ROOT / "cic" / "corpus-map" / "PAIRS.yaml"

sys.path.insert(0, str(CIC_ENGINE_DIR))
from corpus_index import passage_units  # noqa: E402
from corpus_map import load as load_corpus_map  # noqa: E402

from .confinement import _EDITION_PATH  # noqa: E402
from .shelf import Shelf, build_shelf  # noqa: E402


def read_bucket_rows(census_id: str) -> list[dict]:
    docs = load_corpus_map()
    return list(docs.get(census_id, {}).get("works") or [])


def read_pairs() -> tuple[list[dict], dict[str, dict]]:
    if not PAIRS_PATH.is_file():
        return [], {}
    doc = yaml.safe_load(PAIRS_PATH.read_text(encoding="utf-8")) or {}
    return list(doc.get("pairs") or []), dict(doc.get("parties") or {})


def read_vendored_files() -> frozenset[str]:
    if not TEXTS_DIR.is_dir():
        return frozenset()
    return frozenset(p.name for p in TEXTS_DIR.iterdir() if p.suffix in (".txt", ".xml"))


def read_units(bucket_rows: list[dict], records: dict) -> dict[str, str]:
    """Every on-shelf file's normalized text (verbatim-in-shelf needs it)
    plus every file a kind: absence source record in `records` names,
    however off-shelf it is (absence-probe's narrow, Q5-licensed
    exception - the compiler reads it to verify a claimed absence, the
    Representative never sees it)."""
    files = {row["source_file"] for row in bucket_rows if row.get("source_file")}
    for rec in records.values():
        if rec.get("record_type") == "source" and rec.get("kind") == "absence":
            m = _EDITION_PATH.search(str(rec.get("edition") or ""))
            if m:
                files.add(m.group(1))
    units: dict[str, str] = {}
    for filename in files:
        path = TEXTS_DIR / filename
        if not path.is_file():
            continue
        parts = passage_units(path)
        units[filename] = " ".join(u["text"] for u in parts)
    return units


def load_shelf(*, world_key: str, census_id: str, records: dict) -> Shelf:
    """The convenience composition of the pieces above - what cli.py's
    report/shelf commands use. selftest.py calls the pieces directly
    instead, so it can mutate one of them first."""
    bucket_rows = read_bucket_rows(census_id)
    pairs_list, parties = read_pairs()
    return build_shelf(
        world_key=world_key,
        census_id=census_id,
        bucket_rows=bucket_rows,
        pairs_list=pairs_list,
        parties=parties,
        units_by_file=read_units(bucket_rows, records),
        vendored_files=read_vendored_files(),
    )
