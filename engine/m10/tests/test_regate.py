import argparse
import subprocess

import pytest

from engine.m1 import cross_world, gates
from engine.m10 import regate
from engine.m10.common import REPO_ROOT

CLEAR = (
    "Ephrem taught the faith through hymns that families could learn by heart, so the songs carried "
    "his teaching into homes where few people could read. Men and women took a vow to stay single "
    "and serve the poor, and they lived inside the local church."
)
DENSE = (
    "This world serves participants processing an unsettled or fractured sense of who holds legitimate "
    "authority to teach or lead, and its own record neither pretends this was settled nor treats it as "
    "a crisis still needing resolution, which is a genuinely unresolved plurality of authority sources."
)


def _term(rid, text):
    return {"id": rid, "record_type": "term", "plain_meaning": text, "_path": f"records/zzz/term/{rid}.md"}


def _brief(rid, text, cautions=()):
    return {
        "id": rid, "record_type": "facilitator_brief", "audience": "facilitator",
        "world_identity": {"text": text, "grounded_in": ["zzz.term.a"]},
        "cautions": list(cautions), "_path": f"records/zzz/facilitator_brief/{rid}.md",
    }


def _world(*recs):
    return {r["id"]: r for r in recs}


def test_fixture_texts_sit_on_the_right_sides_of_the_gate():
    assert gates.grade_text(CLEAR)["fk"] <= gates.FK_CEILING and gates.grade_text(CLEAR)["fre"] >= gates.FRE_FLOOR
    assert gates.grade_text(DENSE)["fk"] > gates.FK_CEILING


def test_front_prose_takes_units_teasers_notes_hedges_and_cautions_and_skips_ids():
    rec = {
        "record_type": "world_front",
        "skim": {"tile": {"text": "tile text", "grounded_in": ["a.b.c"]}},
        "orientation": {
            "documented_stories": [{"story_id": "a.story.x", "title": "T", "when": "200", "teaser": "a teaser", "grounded_in": ["a.b.c"]}],
            "voices": [{"figure": "a.figure.y", "text": "voice text", "grounded_in": ["a.b.c"], "hedge": "we think so"}],
            "read_first": [{"source": "a.source.z", "note": "read this"}],
        },
        "narrative": {"quiet": "a.limit.q", "pull_quotes": ["a.quote.p"]},
    }
    labels = dict(regate.front_prose_checks(rec))
    assert labels == {
        "skim.tile.text": "tile text",
        "orientation.documented_stories[0].teaser": "a teaser",
        "orientation.voices[0].text": "voice text",
        "orientation.voices[0].hedge": "we think so",
        "orientation.read_first[0].note": "read this",
    }
    brief = _brief("zzz.brief.a", "identity", cautions=["one caution", "two caution"])
    assert dict(regate.front_prose_checks(brief)) == {
        "world_identity.text": "identity",
        "cautions[0]": "one caution",
        "cautions[1]": "two caution",
    }


def test_public_fields_cover_spoken_fields_and_the_brief_with_unique_labels():
    voice = {"id": "zzz.demo.a", "record_type": "demonstration", "exchange": [
        {"speaker": "participant", "text": "one"}, {"speaker": "participant", "text": "two"}]}
    fields = regate.public_fields(_world(_term("zzz.term.a", CLEAR), _brief("zzz.brief.a", CLEAR), voice))
    labels = [(f.rid, f.label) for f in fields]
    assert ("zzz.term.a", "plain_meaning") in labels
    assert ("zzz.brief.a", "world_identity.text") in labels
    assert len(labels) == len(set(labels))


def test_a_new_dense_field_fails_and_a_new_clear_one_passes():
    head = _world(_term("zzz.term.a", CLEAR), _brief("zzz.brief.a", DENSE))
    findings, _ = regate.compare_world(head, {}, {"x"})
    assert [f.check for f in findings] == ["readability", "readability"]
    assert all("zzz.brief.a" in f.reason for f in findings)
    assert any("FK grade" in f.reason for f in findings) and any("FRE" in f.reason for f in findings)


def test_an_unchanged_dense_field_is_reported_not_failed():
    base = _world(_brief("zzz.brief.a", DENSE))
    head = _world(_brief("zzz.brief.a", DENSE), _term("zzz.term.a", CLEAR))
    findings, notes = regate.compare_world(head, base, set())
    assert findings == []
    assert any("already failed at the base" in n for n in notes)


def test_an_edited_field_that_is_still_dense_fails_and_one_that_is_fixed_passes():
    base = _world(_brief("zzz.brief.a", DENSE))
    still = _world(_brief("zzz.brief.a", DENSE + " It also matters."))
    fixed = _world(_brief("zzz.brief.a", CLEAR))
    assert regate.compare_world(still, base, {"p"})[0] != []
    assert regate.compare_world(fixed, base, {"p"})[0] == []


def test_a_short_field_is_not_graded():
    findings, _ = regate.compare_world(_world(_term("zzz.term.a", "Ecclesiastical reconfigurations.")), {}, {"x"})
    assert findings == []


def _voice(words_each, world_id="zzz"):
    return {
        "id": "zzz.voice.craft", "record_type": "voice_craft", "world_id": world_id, "_path": "records/zzz/voice_craft/zzz.voice.craft.md",
        "identity": " ".join(["We keep the lamp lit."] * (words_each // 5)), "guard": "Hold the line.", "flavor_notes": [], "characteristic_concerns": [],
    }


def test_the_voice_budget_fails_a_new_record_over_900_words():
    assert regate.voice_budget_failures(_voice(880), None) == []
    reasons = regate.voice_budget_failures(_voice(950), None)
    assert len(reasons) == 1 and "above the ceiling of 900" in reasons[0]


def test_the_voice_budget_fails_when_an_edit_pushes_a_compliant_record_over_or_makes_an_over_record_longer():
    assert regate.voice_budget_failures(_voice(950), _voice(800)) != []
    assert regate.voice_budget_failures(_voice(960), _voice(950)) != []
    assert regate.voice_budget_failures(_voice(940), _voice(950)) == []


def test_the_voice_budget_fails_a_combined_read_above_fk_10():
    rec = _voice(1)
    rec["identity"] = DENSE
    reasons = regate.voice_budget_failures(rec, None)
    assert any("FK grade" in r for r in reasons)


def test_the_voice_budget_uses_the_gates_own_ceiling_for_a_ruled_world():
    rec = _voice(1400, world_id="gallic-monastic-ascetic-christianity")
    assert regate.voice_budget(rec)["ceiling"] == 1500
    assert not any("words" in r for r in regate.voice_budget_failures(rec, None))


def test_only_a_changed_voice_record_is_budget_checked():
    over = _voice(950)
    findings, _ = regate.compare_world(_world(over), _world(over), set())
    assert findings == []
    findings, _ = regate.compare_world(_world(over), {}, {over["_path"]})
    assert {f.check for f in findings} == {"voice-budget"}


def _git(root, *args):
    subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t", *args], cwd=root, check=True, capture_output=True)


def test_changed_paths_and_base_records_come_from_git(tmp_path):
    _git(tmp_path, "init", "-q", "-b", "main")
    term_dir = tmp_path / "records" / "zzz" / "term"
    term_dir.mkdir(parents=True)
    body = "---\nid: zzz.term.a\nrecord_type: term\nplain_meaning: {}\n---\nnotes\n"
    (term_dir / "zzz.term.a.md").write_text(body.format("one"), encoding="utf-8")
    (term_dir / "zzz.term.b.md").write_text(body.format("two").replace("term.a", "term.b"), encoding="utf-8")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "base")
    (term_dir / "zzz.term.a.md").write_text(body.format("edited"), encoding="utf-8")
    (term_dir / "zzz.term.c.md").write_text(body.format("new").replace("term.a", "term.c"), encoding="utf-8")
    mb = regate.resolve_merge_base(tmp_path, "main")
    assert regate.changed_record_paths(tmp_path, "zzz", mb) == {"records/zzz/term/zzz.term.a.md", "records/zzz/term/zzz.term.c.md"}
    before = regate.base_records(tmp_path, "zzz", mb)
    assert set(before) == {"zzz.term.a", "zzz.term.b"}
    assert before["zzz.term.a"]["plain_meaning"] == "one"


def test_an_unresolvable_base_is_a_finding_not_a_pass():
    report = regate.run_regate("syr", "no-such-ref-anywhere")
    assert not report.ok and report.findings[0].check == "base"


def test_a_world_with_no_registry_entry_fails_both_commands():
    assert not regate.run_regate("zzz-not-a-world").ok
    assert not regate.run_records("zzz-not-a-world").ok


def test_a_world_unchanged_against_its_own_base_passes_regate():
    assert regate.run_regate("syr", "HEAD").ok


def test_a_complete_world_passes_records():
    report = regate.run_records("syr")
    assert report.ok, [f.line() for f in report.findings]


def test_records_builds_the_capsule(monkeypatch):
    from engine.m2 import builders

    monkeypatch.setattr(builders, "build_capsule", lambda records, entry: (_ for _ in ()).throw(ValueError("broken")))
    report = regate.run_records("syr")
    assert any(f.check == "capsule" and "broken" in f.reason for f in report.findings)


def _stub_world(monkeypatch, code, types, census_id="zzz-census"):
    records = {f"{code}.{t}.a": {"id": f"{code}.{t}.a", "record_type": t} for t in types}
    monkeypatch.setattr(regate, "load_world_records", lambda c: records)
    monkeypatch.setattr(regate, "registry_entry", lambda c, root=REPO_ROOT: {"census_id": census_id})
    from engine.m2 import builders

    monkeypatch.setattr(builders, "build_capsule", lambda r, e: b"capsule")


def test_a_missing_required_type_fails_for_a_new_world(monkeypatch):
    _stub_world(monkeypatch, "zzz", ["world_front", "search_record"])
    report = regate.run_records("zzz")
    checks = {(f.check, f.reason) for f in report.findings}
    assert ("required-record-type", "no facilitator_brief record") in checks
    assert any(c == "required-site-json" for c, _ in checks)


def test_a_waiver_for_a_required_type_on_a_new_world_is_itself_a_failure(monkeypatch):
    _stub_world(monkeypatch, "zzz", ["world_front", "facilitator_brief", "search_record"])
    monkeypatch.setattr(cross_world, "ACCEPTED_OPEN", {**cross_world.ACCEPTED_OPEN, "required-record-type/zzz/facilitator_brief": "waived"})
    monkeypatch.setattr(regate, "SITE_DATA_DIR", REPO_ROOT / "cic-website" / "data" / "worlds")
    report = regate.run_records("zzz")
    assert any(f.check == "waiver-not-allowed" for f in report.findings)


def test_a_grandfathered_world_with_a_live_waiver_reports_the_missing_type_without_failing():
    report = regate.run_records("witt")
    assert report.ok
    assert sum("waived for a grandfathered world" in n for n in report.notes) == 3


def test_the_subcommands_register_and_dispatch():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    regate.add_parser(sub)
    assert set(sub.choices) == {"records", "regate"}
    assert regate.run(parser.parse_args(["regate", "syr", "--base", "HEAD"])) == 0
    assert regate.run(parser.parse_args(["records", "syr"])) == 0
    assert regate.run(parser.parse_args(["records", "zzz-not-a-world"])) == 1
