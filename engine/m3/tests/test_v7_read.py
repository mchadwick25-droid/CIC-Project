"""engine.m3.v7_read on a synthetic world: no real probe text, no model call."""
import json
import re
from pathlib import Path

import pytest

import engine.m3.v7_read as rd

WORLD = "tst"
PROBES = [(f"p{n:02d}", cell) for n, cell in enumerate(
    ["C-I", "C-E", "F1-T", "F1-P", "F2-E", "F2-I", "F3-T", "F3-P", "F4-E", "F4-I", "F5-T", "F5-P", "F6-E", "F6-I"])]
QUESTION = "Synthetic question for {}?"


def _records():
    return {
        "tst.quote.one": {"id": "tst.quote.one", "record_type": "quote", "text": "Synthetic quoted words.", "speaker_or_author": "Author",
                          "sources": [{"source_id": "tst.source.x", "locus": "cic/texts/tst/x.txt, lines 40-41"}],
                          "reading_card": {"setting": "A synthetic setting."}, "_path": "records/tst/quote/tst.quote.one.md", "_body": "process note"},
        "tst.term.risky": {"id": "tst.term.risky", "record_type": "term", "world_word": "risky", "distortion_risk": "high",
                           "false_friend": ["a modern sense"], "plain_meaning": "Synthetic meaning."},
        "tst.term.calm": {"id": "tst.term.calm", "record_type": "term", "world_word": "calm", "distortion_risk": "low"},
        "tst.dw.plain": {"id": "tst.dw.plain", "record_type": "doctrinal_witness", "text": "Synthetic witness."},
    }


@pytest.fixture
def env(tmp_path, monkeypatch):
    texts = tmp_path / "texts_root"
    (texts / "cic" / "texts" / "tst").mkdir(parents=True)
    (texts / "cic" / "texts" / "tst" / "x.txt").write_text("\n".join(f"line {n} of the synthetic source" for n in range(1, 120)), encoding="utf-8")
    monkeypatch.setattr(rd, "TEXTS_ROOT", texts)
    monkeypatch.setattr(rd, "_load_records", lambda world: _records())
    monkeypatch.setattr(rd, "read_question", lambda probe_id: QUESTION.format(probe_id))
    set_dir = tmp_path / "Set"
    set_dir.mkdir()
    a_lines, b_lines = [], []
    for n, (probe, cell) in enumerate(PROBES):
        cites = ["tst.quote.one", "tst.dw.plain"] if n % 2 == 0 else ["tst.dw.plain"]
        a_lines.append({"world": WORLD, "probe_id": probe, "cell": cell, "answer_text": f"Answer alpha for {probe} about gamma.", "citations": cites})
        b_lines.append({"world": WORLD, "probe_id": probe, "cell": cell, "arm": "b", "error": None, "answer_text": f"Answer beta for {probe} about delta.",
                        "citations": cites, "repo_commit": "deadbeef", "voice_model_id": "model-x"})
    (set_dir / f"A_{WORLD}.jsonl").write_text("\n".join(json.dumps(x) for x in a_lines), encoding="utf-8")
    run1, run2 = tmp_path / "b1.jsonl", tmp_path / "b2.jsonl"
    run1.write_text("\n".join(json.dumps(x) for x in b_lines), encoding="utf-8")
    run2.write_text("\n".join(json.dumps(x) for x in b_lines[:4]), encoding="utf-8")
    reviews = {
        "second_pass": {"by_probe": {"p00": {"cell": "C-I", "rigor": "NOT ACCEPTABLE", "rigor_note": "Answer alpha for p00 about gamma is wrong.",
                                             "overall": "BLOCK"}}},
        "outside_referees": {"by_probe": {"p01": {"verdict": "REJECT", "doubted_claims": [
            {"claim": "Answer beta for p01 about delta", "problem": "Overstated."}, {"claim": "fine words", "problem": "This is correct."}]}}},
    }
    (set_dir / f"A_reviews_{WORLD}.json").write_text(json.dumps(reviews), encoding="utf-8")
    return {"tmp": tmp_path, "set": set_dir, "run1": run1, "run2": run2}


def _export(env, name="exp", seed=7):
    out = env["tmp"] / name
    code = rd.main(["export", "--set-dir", str(env["set"]), "--b", str(env["run1"]), "--b", str(env["run2"]), "--worlds", WORLD,
                    "--out", str(out), "--seed", str(seed)])
    assert code == 0
    return out


def _reply(iid, reader, score=2, errors=None, depth="rich"):
    return {"item_id": iid, "reader": reader, "depth": depth, "errors": errors or [],
            "scores": {d: {"score": score, "reason": "Because."} for d in rd.DIMENSIONS}}


def _error(words="gamma", tier=3, typ="other: craft"):
    return {"answer_words": words, "source_words": "src", "type": typ, "tier": tier, "confidence": "sure", "evidence": "x lines 1-2"}


def _file(out, label, iid, reply):
    path = out / "replies" / label / f"{iid}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(reply), encoding="utf-8")


def test_no_request_carries_an_arm_name_an_october_grade_or_a_run_id(env):
    out = _export(env)
    key = json.loads((out / "key" / "key.json").read_text())
    requests = sorted((out / "requests").rglob("*.json"))
    assert len(requests) == 2 * len(key["items"]) == 2 * (14 + 14 + 4)
    for path in requests:
        text = path.read_text(encoding="utf-8")
        for pattern in (r"\barm\b", "october", "second_pass", "referee", "deadbeef", "model-x", r'"run"', "reading_context"):
            assert not re.search(pattern, text, re.IGNORECASE), (path.name, pattern)
        body = json.loads(text)
        assert set(body) <= {"item_id", "kind", "reader", "world", "instructions", "rubric", "reply_format", "question", "answer",
                             "cited_records", "source_passages", "lexicon_risk_flags", "cited_records_not_found", "source_passages_note"}
    assert not any(env["run1"].name in p.name for p in requests)


def test_a_request_holds_the_context_the_readers_need(env):
    out = _export(env)
    key = json.loads((out / "key" / "key.json").read_text())
    iid = next(i for i, m in key["items"].items() if m["key"] == f"{WORLD}|a|1|p00")
    req = json.loads((out / "requests" / "reader-1" / f"{iid}.json").read_text())
    assert req["question"] == QUESTION.format("p00")
    assert "Source accuracy" in req["rubric"] and "How the readers work" not in req["rubric"]
    quote = next(r for r in req["cited_records"] if r["id"] == "tst.quote.one")
    assert "project-authored" in quote["reading_card"]["label"].lower() and "_body" not in quote and "_path" not in quote
    assert any("line 40 of the synthetic source" in p["text"] and "line 10 of" in p["text"] for p in req["source_passages"])
    assert [t["id"] for t in req["lexicon_risk_flags"]["terms"]] == ["tst.term.risky"]


def test_a_world_with_no_risk_flags_says_so(env, monkeypatch):
    monkeypatch.setattr(rd, "_load_records", lambda world: {"tst.dw.plain": _records()["tst.dw.plain"]})
    out = _export(env)
    req = next((out / "requests" / "reader-1").glob("*.json"))
    assert json.loads(req.read_text())["lexicon_risk_flags"]["terms"] == []
    assert "No term record" in json.loads(req.read_text())["lexicon_risk_flags"]["note"]


def test_ids_and_order_reproduce_from_the_seed(env):
    first, again, other = _export(env, "e1"), _export(env, "e2"), _export(env, "e3", seed=8)
    m1, m2, m3 = (json.loads((d / "manifest.json").read_text()) for d in (first, again, other))
    assert [m1["order"][r] for r in rd.READERS] == [m2["order"][r] for r in rd.READERS]
    assert sorted(m1["items"]) == sorted(m2["items"]) != sorted(m3["items"])
    assert (first / "key" / "key.json").read_bytes() == (again / "key" / "key.json").read_bytes()
    assert m1["order"]["reader-1"] != m1["order"]["reader-2"]
    assert rd.item_id(7, "k") == rd.item_id(7, "k") != rd.item_id(8, "k")


def test_agreement_on_a_fixed_example():
    pairs = [(2, 2), (2, 1), (0, 2), (1, 1), (0, 1)]
    assert rd.agreement(pairs) == {"n": 5, "exact": 0.4, "within_one": 0.8}
    assert rd.agreement([]) == {"n": 0, "exact": None, "within_one": None}


def test_the_adjudication_trigger():
    same = _reply("i", "reader-1", 2)
    assert not rd.needs_adjudication(same, _reply("i", "reader-2", 2))
    differ = _reply("i", "reader-2", 2)
    differ["scores"]["source_accuracy"]["score"] = 1
    assert rd.needs_adjudication(same, differ)
    assert rd.needs_adjudication(_reply("i", "a", errors=[_error()]), _reply("i", "b"))
    assert rd.needs_adjudication(_reply("i", "a", errors=[_error(tier=2)]), _reply("i", "b", errors=[_error(tier=3)]))
    assert rd.needs_adjudication(_reply("i", "a", errors=[_error(tier=1)]), _reply("i", "b", errors=[_error(tier=1)]))
    assert not rd.needs_adjudication(_reply("i", "a", errors=[_error(tier=3)]), _reply("i", "b", errors=[_error(tier=3)]))


def test_adjudicate_writes_requests_only_for_triggered_items(env):
    out = _export(env)
    ids = sorted(json.loads((out / "manifest.json").read_text())["items"])
    for n, iid in enumerate(ids):
        _file(out, "reader-1", iid, _reply(iid, "reader-1", 2))
        _file(out, "reader-2", iid, _reply(iid, "reader-2", 1 if n == 0 else 2, errors=[_error(tier=1)] if n == 1 else None))
    assert rd.main(["adjudicate", "--export-dir", str(out)]) == 0
    listing = json.loads((out / "adjudication_manifest.json").read_text())
    assert sorted(listing["items"]) == [ids[0], ids[1]]
    req = json.loads(Path(listing["items"][ids[1]]["request"]).read_text())
    assert req["kind"] == "adjudication" and len(req["reader_findings"]) == 2 and req["source_passages"] is not None
    assert not re.search(r"\barm\b", json.dumps(req))


def test_after_october_shows_the_findings_for_a_items_only(env):
    out = _export(env)
    key = json.loads((out / "key" / "key.json").read_text())["items"]
    a0 = next(i for i, m in key.items() if m["key"] == f"{WORLD}|a|1|p00")
    b0 = next(i for i, m in key.items() if m["key"] == f"{WORLD}|b|1|p00")
    for iid in (a0, b0):
        _file(out, "reader-1", iid, _reply(iid, "reader-1"))
    assert rd.main(["after-october", "--export-dir", str(out), "--set-dir", str(env["set"])]) == 0
    listing = json.loads((out / "after_october_manifest.json").read_text())["items"]
    assert list(listing) == [f"reader-1/{a0}"]
    req = json.loads(Path(listing[f"reader-1/{a0}"]["request"]).read_text())
    assert req["october_review"]["second_pass"]["rigor"] == "NOT ACCEPTABLE" and req["your_filed_reply"]["depth"] == "rich"


def _seed_file(env, out, count):
    key = json.loads((out / "key" / "key.json").read_text())["items"]
    bases = [m["key"] for m in key.values() if m["arm"] == "a"][:count]
    copies = [{"base": b, "answer_text": f"Planted answer {n} about gamma and a planted claim.", "defect_type": "modern_projection",
               "expected_location": "planted claim"} for n, b in enumerate(bases)]
    path = env["tmp"] / "copies.json"
    path.write_text(json.dumps(copies), encoding="utf-8")
    return path


def test_seed_copies_are_indistinguishable_in_form_and_the_key_is_sealed(env, capsys):
    out = _export(env)
    capsys.readouterr()
    path = _seed_file(env, out, 10)
    assert rd.main(["seed-copies", "--export-dir", str(out), "--copies", str(path)]) == 0
    sealed = json.loads((out / "key" / "seed_key.json").read_text())
    assert len(sealed["items"]) == 10
    assert json.loads(capsys.readouterr().out)["seed_key_sha256"] == rd._sha256(out / "key" / "seed_key.json")
    manifest = json.loads((out / "manifest.json").read_text())
    assert len(manifest["items"]) == 32 + 10
    fake = next(iter(sealed["items"]))
    base = next(i for i, m in json.loads((out / "key" / "key.json").read_text())["items"].items() if m["key"] == sealed["items"][fake]["base"])
    r_req, f_req = (json.loads((out / "requests" / "reader-1" / f"{i}.json").read_text()) for i in (base, fake))
    assert set(r_req) == set(f_req) and f_req["answer"].startswith("Planted answer")
    assert rd.main(["seed-copies", "--export-dir", str(out), "--copies", str(path)]) == 2
    assert rd.main(["seed-copies", "--export-dir", str(out), "--copies", str(_seed_file(env, out, 9))]) == 2


def _score_setup(env, caught_by_second):
    out = _export(env)
    rd.main(["seed-copies", "--export-dir", str(out), "--copies", str(_seed_file(env, out, 10))])
    sealed = json.loads((out / "key" / "seed_key.json").read_text())["items"]
    key = json.loads((out / "key" / "key.json").read_text())["items"]
    for n, iid in enumerate(sorted(sealed)):
        _file(out, "reader-1", iid, _reply(iid, "reader-1", errors=[_error("a planted claim", tier=2)]))
        _file(out, "reader-2", iid, _reply(iid, "reader-2", errors=[_error("a planted claim", tier=2)] if n < caught_by_second else []))
        _file(out, "adjudicator", iid, _reply(iid, "adjudicator", errors=[_error("a planted claim", tier=2)]))
    for iid in key:
        _file(out, "reader-1", iid, _reply(iid, "reader-1", 2 if key[iid]["arm"] == "a" else 1))
        _file(out, "reader-2", iid, _reply(iid, "reader-2", 2 if key[iid]["arm"] == "a" else 1))
    return out


def test_the_catch_rate_gate(env):
    assert rd.catch_gate({"seeded": 10, "missing": [], "by_reader": {r: {"rate": 0.9, "caught": 9} for r in rd.READERS}})["scores_count"]
    low = rd.catch_gate({"seeded": 10, "missing": [], "by_reader": {"reader-1": {"rate": 1.0, "caught": 10}, "reader-2": {"rate": 0.8, "caught": 8}}})
    assert not low["scores_count"] and "reader-2 caught 8 of 10" in low["reasons"][0]
    assert not rd.catch_gate({"seeded": 9, "missing": [], "by_reader": {r: {"rate": 1.0, "caught": 9} for r in rd.READERS}})["scores_count"]
    tables = rd.compute_tables(_score_setup(env, 8), env["set"])
    assert not tables["gate"]["scores_count"]
    assert "SCORES DO NOT COUNT" in rd.render_markdown(tables)
    ok = rd.compute_tables(_fresh_score(env), env["set"])
    assert ok["gate"]["scores_count"] and "SCORES DO NOT COUNT" not in rd.render_markdown(ok)


def _fresh_score(env):
    out = _export(env, "exp_clean")
    rd.main(["seed-copies", "--export-dir", str(out), "--copies", str(_seed_file(env, out, 10))])
    sealed = json.loads((out / "key" / "seed_key.json").read_text())["items"]
    for iid in sealed:
        for r in rd.READERS:
            _file(out, r, iid, _reply(iid, r, errors=[_error("a planted claim", tier=2)]))
        _file(out, "adjudicator", iid, _reply(iid, "adjudicator", errors=[_error("a planted claim", tier=2)]))
    return out


def test_score_tables_use_rulings_and_report_agreement_noise_and_october(env):
    out = _score_setup(env, 10)
    key = json.loads((out / "key" / "key.json").read_text())["items"]
    split = next(i for i, m in key.items() if m["key"] == f"{WORLD}|b|1|p00")
    _file(out, "reader-2", split, _reply(split, "reader-2", 2))
    awaiting = rd.compute_tables(out, env["set"])
    assert split in awaiting["awaiting_adjudication"]
    _file(out, "adjudicator", split, _reply(split, "adjudicator", 0, errors=[_error("delta", tier=1, typ="invented")]))
    t = rd.compute_tables(out, env["set"])
    assert t["awaiting_adjudication"] == []
    assert t["scores"]["source_accuracy"]["a"][WORLD]["mean"] == 2
    assert t["scores"]["source_accuracy"]["a"][WORLD]["n"] == 14
    assert t["scores"]["source_accuracy"]["b"][WORLD]["distribution"] == {"0": 1, "1": 13, "2": 0}
    assert t["reader_agreement"]["source_accuracy"]["exact"] == pytest.approx(1 - 1 / 32)
    assert t["noise_floor"]["repeat_probes"] == 4
    assert t["noise_floor"]["by_dimension"]["source_accuracy"]["exact"] == 0.75
    assert t["error_counts"]["b"]["invented"] == {"1": 1}
    repeated = {(e["probe_id"], e["source"]): e["b_status"] for e in t["october_errors"]}
    assert repeated[("p00", "second pass")] == "not repeated"
    assert repeated[("p01", "outside referee")] == "not repeated"
    assert len([e for e in t["october_errors"] if e["probe_id"] == "p01"]) == 1
    md = rd.render_markdown(t)
    assert "Known October errors" in md


def test_a_known_october_error_is_repeated_when_a_b_finding_overlaps(env):
    out = _score_setup(env, 10)
    key = json.loads((out / "key" / "key.json").read_text())["items"]
    b1 = next(i for i, m in key.items() if m["key"] == f"{WORLD}|b|1|p01")
    for r in rd.READERS:
        _file(out, r, b1, _reply(b1, r, 1, errors=[_error("Answer beta for p01 about delta", tier=3)]))
    t = rd.compute_tables(out, env["set"])
    row = next(e for e in t["october_errors"] if e["probe_id"] == "p01")
    assert row["b_status"] == "repeated" and row["claim_wording_in_b_answer"] is True
    assert t["error_counts"]["b"]["other"]["3"] == 1


def test_mark_pack_gives_twelve_per_world_with_the_same_probes_in_both_arms(env):
    out = env["tmp"] / "pack"
    assert rd.main(["mark-pack", "--set-dir", str(env["set"]), "--b", str(env["run1"]), "--worlds", WORLD, "--out", str(out), "--seed", "3"]) == 0
    pack = json.loads((out / "mark_pack.json").read_text())["items"]
    key = json.loads((out / "mark_pack_key.json").read_text())["items"]
    assert len(pack) == 24 and {m["world"] for m in key.values()} == {WORLD}
    by_arm = {a: sorted(m["probe_id"] for i, m in key.items() if m["arm"] == a) for a in ("a", "b")}
    assert by_arm["a"] == by_arm["b"] and len(set(by_arm["a"])) == 12
    assert set(pack[0]) == {"item_id", "world", "question", "answer", "cited_records", "source_lines"}
    again = env["tmp"] / "pack2"
    rd.main(["mark-pack", "--set-dir", str(env["set"]), "--b", str(env["run1"]), "--worlds", WORLD, "--out", str(again), "--seed", "3"])
    assert (again / "mark_pack.json").read_bytes() == (out / "mark_pack.json").read_bytes()
    assert not re.search(r"\barm\b", json.dumps(pack))


def test_the_pick_favours_quote_placing_and_t_or_e_probes():
    cands = [{"probe_id": f"q{n}", "cell": "F1-T" if n < 20 else "F1-I", "places_quote": n < 20} for n in range(40)]
    wins = sum(sum(c["probe_id"] in {x["probe_id"] for x in rd.pick_probes(cands, 12, s, "w")} for c in cands[:20]) for s in range(30))
    assert wins / (30 * 12) > 0.7
    assert rd.register_of("C-E") == "E" and rd.register_of("F4-T") == "T"
    with pytest.raises(ValueError):
        rd.register_of("F4-X")


def test_writing_into_the_repository_is_refused(env, capsys):
    inside = rd.REPO_ROOT / "engine" / "m3" / "_v7_read_refused_probe_dir"
    for argv in (["export", "--set-dir", str(env["set"]), "--b", str(env["run1"]), "--worlds", WORLD, "--out", str(inside), "--seed", "1"],
                 ["mark-pack", "--set-dir", str(env["set"]), "--b", str(env["run1"]), "--worlds", WORLD, "--out", str(inside), "--seed", "1"]):
        assert rd.main(argv) == 2
    assert not inside.exists()
    assert "inside the repository" in capsys.readouterr().err
    with pytest.raises(rd.Refused):
        rd.require_outside_repo(rd.REPO_ROOT / "Build")


def test_a_reply_that_does_not_fit_is_reported_not_scored(env):
    out = _export(env)
    iid = sorted(json.loads((out / "manifest.json").read_text())["items"])[0]
    bad = _reply(iid, "reader-1")
    bad["scores"]["source_accuracy"]["score"] = 3
    _file(out, "reader-1", iid, bad)
    t = rd.compute_tables(out, env["set"])
    assert t["invalid_replies"][0]["item_id"] == iid and t["items_scored"] == 0
