"""Each record kind lives in its home: world material in records/<code>/,
world fronts and facilitator briefs in Build/worlds/<code>/surface/, search
records in Build/worlds/<code>/build/records/."""
from pathlib import Path

from engine.m1 import gates
from engine.m1.loader import load_world_records, package_records, world_record_homes


def _record(path: str, record_type: str) -> dict:
    return {"record_type": record_type, "_path": path}


def test_every_kind_in_its_home_passes():
    records = {
        "w.term.a": _record("records/w/term/w.term.a.md", "term"),
        "w.front.a": _record("Build/worlds/w/surface/world_front/w.front.a.md", "world_front"),
        "w.brief.a": _record("Build/worlds/w/surface/facilitator_brief/w.brief.a.md", "facilitator_brief"),
        "w.search.a": _record("Build/worlds/w/build/records/search_record/w.search.a.md", "search_record"),
    }
    assert gates.gate_record_home(records, {}, {}) == []


def test_a_search_record_written_to_the_old_place_fails():
    records = {"w.search.a": _record("records/w/search_record/w.search.a.md", "search_record")}
    [finding] = gates.gate_record_home(records, {}, {})
    assert "Build/worlds/<code>/build/records/" in finding


def test_a_world_record_in_the_surface_home_fails():
    records = {"w.term.a": _record("Build/worlds/w/surface/term/w.term.a.md", "term")}
    [finding] = gates.gate_record_home(records, {}, {})
    assert "records/<code>/" in finding


def test_the_loader_reads_every_home_and_the_package_keeps_records_only(tmp_path):
    records_root = tmp_path / "records"
    for home, kind, rid in (("world", "term", "w.term.a"), ("surface", "world_front", "w.front.a"), ("residue", "search_record", "w.search.a")):
        d = world_record_homes("w", records_root)[home] / kind
        d.mkdir(parents=True)
        (d / f"{rid}.md").write_text(f"---\nid: {rid}\nrecord_type: {kind}\n---\n", encoding="utf-8")
    import engine.m1.loader as loader
    original = loader.REPO_ROOT
    loader.REPO_ROOT = tmp_path
    try:
        records = load_world_records("w", records_root)
        assert set(records) == {"w.term.a", "w.front.a", "w.search.a"}
        assert set(package_records("w", records, records_root)) == {"w.term.a"}
    finally:
        loader.REPO_ROOT = original


def test_the_live_worlds_pass_the_gate():
    for code in ("alx", "fix", "gallic", "rzg"):
        assert gates.gate_record_home(load_world_records(code), {}, {}) == []
