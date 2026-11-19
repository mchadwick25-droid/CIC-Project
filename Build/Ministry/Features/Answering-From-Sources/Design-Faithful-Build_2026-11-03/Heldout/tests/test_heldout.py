import functools
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

import pytest
import yaml

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import heldout as h  # noqa: E402

REPO = h.REPO


def questions(world):
    return yaml.safe_load((HERE / f"{world}_questions.yaml").read_text(encoding="utf-8"))


@functools.lru_cache(maxsize=None)
def shelf_tokens(world):
    from engine.m1.registry import load_registry
    from engine.m9.loader import read_bucket_rows

    rows = read_bucket_rows(load_registry()[world]["census_id"])
    files = {r["source_file"] for r in rows if r.get("source_file")}
    return sum((REPO / "cic/texts" / f).stat().st_size for f in files if (REPO / "cic/texts" / f).exists()) / 4


@pytest.mark.parametrize("world", h.WORLDS)
def test_count_matches_rule(world):
    assert len(questions(world)) == h.EXPECTED[world] == 20 + round(shelf_tokens(world) / 2_000_000)


def test_total_is_360():
    assert sum(len(questions(w)) for w in h.WORLDS) == 360


def test_ids_unique_and_shaped():
    for w in h.WORLDS:
        qs = questions(w)
        assert [sorted(q) for q in qs] == [["id", "text"]] * len(qs)
        assert len({q["id"] for q in qs}) == len(qs)
        assert all("?" in q["text"] or re.match(r"(Tell|Describe|Explain|Walk|Help|Give|Say)\b", q["text"]) for q in qs)


def test_no_near_duplicates():
    assert h.flags({w: questions(w) for w in h.WORLDS}) == []


def test_sha256sums_match():
    lines = (HERE / "SHA256SUMS").read_text().splitlines()
    assert [l.split("  ")[1] for l in lines] == [f"{w}_questions.yaml" for w in h.WORLDS]
    for l in lines:
        digest, name = l.split("  ")
        assert hashlib.sha256((HERE / name).read_bytes()).hexdigest() == digest


@functools.lru_cache(maxsize=None)
def _forbidden_ids():
    ids = set()
    for f in ("07-subquestions.yaml", "08-subquestion-splits.yaml"):
        for e in yaml.safe_load((h.SB / f).read_text(encoding="utf-8"))[f.startswith("07") and "subquestions" or "splits"]:
            ids.add(e["id"])
            ids.update(e.get("ids") or [])
    for p in (REPO / "records").glob("*/*/*.md"):
        ids.add(p.stem)
    return ids


def test_request_set_is_complete():
    names = {p.name for p in (HERE / "requests").glob("*.md")}
    assert {f"{w}_request.md" for w in h.WORLDS} <= names
    assert all(n.endswith("_request.md") for n in names)


@pytest.mark.parametrize("path", sorted((HERE / "requests").glob("*_request.md")), ids=lambda p: p.name)
def test_request_file_is_clean(path):
    text = path.read_text(encoding="utf-8")
    if "rewrite" not in path.name:
        assert text == h.request_text(path.name.split("_")[0])
    assert not re.search(r"\bC\d+\.S\d+[a-z]?\b|\bC\d+-\d+\b", text)
    assert not re.search(r"\b[a-z]+\.(?:term|story|quote|gravity|force|figure|contested_claim|honest_limit|ambient|demonstration|doctrinal_witness|source)\.[a-z0-9_-]+", text)
    hits = [i for i in _forbidden_ids() if len(i) > 5 and i in text]
    assert hits == []
    for banned in ("Question-Coverage", "sidecar", "Sidecar", "Passage_Seeds", "sealed", "records/"):
        assert banned not in text


@pytest.mark.parametrize("world", h.WORLDS)
def test_variety(world):
    rows = yaml.safe_load((HERE / "drafts" / f"{world}_draft.yaml").read_text(encoding="utf-8"))
    n = h.EXPECTED[world]
    assert len(rows) == n
    themes = Counter(r["theme"] for r in rows)
    assert set(themes) <= set(h.THEMES)
    assert max(themes.values()) <= int(n * h.THEME_CAP)
    assert themes["modern_concern"] >= 2 and themes["unanswerable"] >= 2
    lengths = [len(r["text"].split()) for r in rows]
    assert min(lengths) <= 10 and max(lengths) >= 20
    for r in rows:
        assert not re.search(r"\b[a-z]+\.[a-z_]+\.[a-z0-9-]+\b", r["text"])
        assert not re.search(r"\bC\d+\.S\d+\b", r["text"])
