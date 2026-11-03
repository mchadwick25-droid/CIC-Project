"""engine.m3.v7_read on a synthetic world: no real probe text, no model call."""
import json
import re
from pathlib import Path

import pytest

import engine.m3.v7_passages as ps
import engine.m3.v7_read as rd
from engine.m1.loader import load_world_records

WORLD = "tst"
PROBES = [(f"p{n:02d}", cell) for n, cell in enumerate(
    ["C-I", "C-E", "F1-T", "F1-P", "F2-E", "F2-I", "F3-T", "F3-P", "F4-E", "F4-I", "F5-T", "F5-P", "F6-E", "F6-I"])]
QUESTION = "Synthetic question for {}?"


def _records():
    return {
        "tst.source.x": {"id": "tst.source.x", "record_type": "source", "kind": "vendored", "edition": "vendored as cic/texts/tst1_x.xml",
                         "external_ids": {"ccel_volume": "tst1", "thml_div": "w"}},
        "tst.source.u": {"id": "tst.source.u", "record_type": "source", "kind": "unvendored", "edition": "consultation only"},
        "tst.quote.one": {"id": "tst.quote.one", "record_type": "quote", "text": "Synthetic quoted words.", "modern_rendering": "Plain words.",
                          "modern_lens_note": "A lens note.", "speaker_or_author": "Author",
                          "sources": [{"source_id": "tst.source.x", "locus": "tst1 lines 40-41"}],
                          "reading_card": {"setting": "A synthetic setting."}, "_path": "records/tst/quote/tst.quote.one.md", "_body": "process note",
                          "canon_cells": ["C-I"]},
        "tst.term.risky": {"id": "tst.term.risky", "record_type": "term", "world_word": "risky", "distortion_risk": "high",
                           "false_friend": ["a modern sense"], "plain_meaning": "Synthetic meaning.", "senses": {"informational": "A sense."},
                           "sources": [{"source_id": "tst.source.x", "locus": "ch. 9"}]},
        "tst.term.calm": {"id": "tst.term.calm", "record_type": "term", "world_word": "calm", "distortion_risk": "low"},
        "tst.dw.plain": {"id": "tst.dw.plain", "record_type": "doctrinal_witness", "text": "chapter two line 50 of the synthetic source",
                         "positions": ["one"], "sources": [{"source_id": "tst.source.x", "locus": "ch. 2"}]},
        "tst.gravity.g": {"id": "tst.gravity.g", "record_type": "gravity", "name": "G", "description": "A synthetic gravity.",
                          "sources": [{"source_id": "tst.source.u", "locus": "whole"}]},
        "tst.limit.l": {"id": "tst.limit.l", "record_type": "honest_limit", "statement": "A synthetic limit."},
    }


def _xml_lines():
    lines = ['<div1 id="w" title="Work One">', '<div2 id="w.1" title="Chapter I">']
    lines += [f"chapter one line {n} of the synthetic source" for n in range(3, 31)]
    lines += ["</div2>", '<div2 id="w.2" title="Chapter II">']
    lines += [f"chapter two line {n} of the synthetic source" for n in range(33, 71)]
    lines += ["</div2>", "</div1>"]
    return lines


@pytest.fixture
def env(tmp_path, monkeypatch):
    texts = tmp_path / "texts_root"
    (texts / "cic" / "texts").mkdir(parents=True)
    (texts / "cic" / "texts" / "tst1_x.xml").write_text("\n".join(_xml_lines()), encoding="utf-8")
    monkeypatch.setattr(rd, "TEXTS_ROOT", texts)
    monkeypatch.setattr(rd, "_load_records", lambda world: _records())
    monkeypatch.setattr(rd, "read_question", lambda probe_id: QUESTION.format(probe_id))
    set_dir = tmp_path / "Set"
    set_dir.mkdir()
    a_lines, b_lines = [], []
    for n, (probe, cell) in enumerate(PROBES):
        cites = ["tst.quote.one", "tst.dw.plain"] if n % 2 == 0 else ["tst.dw.plain", "tst.gravity.g"]
        a_lines.append({"world": WORLD, "probe_id": probe, "cell": cell, "answer_text": f"Answer alpha for {probe} about gamma.", "citations": cites})
        b_lines.append({"world": WORLD, "probe_id": probe, "cell": cell, "arm": "b", "error": None, "answer_text": f"Answer beta for {probe} about delta.",
                        "citations": cites, "repo_commit": "deadbeef", "voice_model_id": "model-x"})
    (set_dir / f"A_{WORLD}.jsonl").write_text("\n".join(json.dumps(x) for x in a_lines), encoding="utf-8")
    run1, run2 = tmp_path / "b1.jsonl", tmp_path / "b2.jsonl"
    run1.write_text("\n".join(json.dumps(x) for x in b_lines), encoding="utf-8")
    run2.write_text("\n".join(json.dumps(x) for x in b_lines[:4]), encoding="utf-8")
    reviews = {
        "second_pass": {"by_probe": {
            "p00": {"cell": "C-I", "rigor": "NOT ACCEPTABLE", "rigor_note": "The answer says 'Answer alpha for p00 about gamma' with no source.",
                    "readable": "GOOD", "understandable": "POOR", "overall": "BLOCK", "craft_note": ""},
            "p02": {"cell": "F1-T", "rigor": "ACCEPTABLE", "rigor_note": "A slip with no quoted words.", "readable": "FAIR",
                    "understandable": "GOOD", "overall": "FIX", "craft_note": "Padding."},
            "p04": {"cell": "F2-E", "rigor": "SOUND", "rigor_note": "Fine.", "readable": "GOOD", "understandable": "GOOD", "overall": "SHIP", "craft_note": "x"}}},
        "outside_referees": {"by_probe": {"p01": {"verdict": "REJECT", "doubted_claims": [
            {"claim": "Answer beta for p01 about delta", "problem": "Broadly fine, but overstated."}, {"claim": "fine words here", "problem": "This is correct."}]}}},
    }
    (set_dir / f"A_reviews_{WORLD}.json").write_text(json.dumps(reviews), encoding="utf-8")
    band = tmp_path / "band"
    band.mkdir()
    for run, words in (("r1", "one two three"), ("r2", "one two three four five"), ("r3", "one")):
        probes = [{"probe_id": p, "passed": True, "transcript": {"answer_text": words + ".", "citations": ["tst.quote.one"]}} for p, _ in PROBES]
        (band / f"live-admission-report-baseline-{run}-{WORLD}-2026-10-02.json").write_text(
            json.dumps({"worlds": {WORLD: {"per_probe": probes}}}), encoding="utf-8")
    return {"tmp": tmp_path, "set": set_dir, "run1": run1, "run2": run2, "band": band}


def _export(env, name="exp", seed=7):
    out, keys = env["tmp"] / name, env["tmp"] / f"keys_{name}"
    code = rd.main(["export", "--set-dir", str(env["set"]), "--b", str(env["run1"]), "--b", str(env["run2"]), "--worlds", WORLD,
                    "--out", str(out), "--key-dir", str(keys), "--seed", str(seed)])
    assert code == 0
    return out, keys


def _reply(iid, reader, score=2, errors=None, depth="rich"):
    return {"item_id": iid, "reader": reader, "depth": depth, "errors": errors or [],
            "scores": {d: {"score": score, "reason": "Because."} for d in rd.DIMENSIONS}}


def _error(words="gamma", tier=3, typ="other: craft"):
    return {"answer_words": words, "source_words": "src", "type": typ, "tier": tier, "confidence": "sure", "evidence": "x lines 1-2"}


def _file(out, label, iid, reply):
    path = out / "replies" / label / f"{iid}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(reply), encoding="utf-8")


def _key(keys):
    return json.loads((keys / "key.json").read_text())["items"]


def _id_of(keys, name):
    return next(i for i, m in _key(keys).items() if m["key"] == name)


def test_no_request_carries_an_arm_name_an_october_grade_or_a_run_id(env):
    out, keys = _export(env)
    requests = sorted((out / "requests").rglob("*.json"))
    assert len(requests) == 2 * len(_key(keys)) == 2 * (14 + 14 + 4)
    for path in requests:
        text = path.read_text(encoding="utf-8")
        for pattern in (r"\barm\b", "october", "second_pass", "referee", "deadbeef", "model-x", r'"run"', "reading_context"):
            assert not re.search(pattern, text, re.IGNORECASE), (path.name, pattern)
        assert set(json.loads(text)) <= {"item_id", "kind", "reader", "world", "instructions", "rubric", "reply_format", "question", "answer",
                                         "cited_records", "source_passages", "source_passages_note", "source_passages_unresolved",
                                         "lexicon_risk_flags", "cited_records_not_found"}
    manifest = json.loads((out / "manifest.json").read_text())
    assert "seed" not in manifest and manifest["run_one_item_per_fresh_context"] is True
    assert not any(p.name in ("key.json", "seed.json") for p in out.rglob("*.json"))


def test_a_request_holds_the_content_of_each_cited_record_and_its_division(env):
    out, keys = _export(env)
    iid = _id_of(keys, f"{WORLD}|a|1|p00")
    req = json.loads((out / "requests" / "reader-1" / f"{iid}.json").read_text())
    assert req["question"] == QUESTION.format("p00")
    assert "Source accuracy" in req["rubric"] and "How the readers work" not in req["rubric"]
    quote = next(r for r in req["cited_records"] if r["id"] == "tst.quote.one")
    assert quote["modern_rendering"] == "Plain words." and quote["modern_lens_note"] == "A lens note." and quote["text"]
    assert "project-authored" in quote["reading_card"]["label"].lower()
    assert not {"_body", "_path", "canon_cells"} & set(quote)
    passage = next(p for p in req["source_passages"] if p["record_id"] == "tst.quote.one")
    assert passage["division_path"] == ["Work One", "Chapter II"]
    assert "chapter two line 40 of" in passage["text"] and "chapter one" not in passage["text"]
    assert [t["id"] for t in req["lexicon_risk_flags"]["terms"]] == ["tst.term.risky"]


def test_each_type_keeps_its_main_text(env):
    out, keys = _export(env)
    iid = _id_of(keys, f"{WORLD}|a|1|p01")
    req = json.loads((out / "requests" / "reader-1" / f"{iid}.json").read_text())
    gravity = next(r for r in req["cited_records"] if r["id"] == "tst.gravity.g")
    assert gravity["description"] == "A synthetic gravity."
    assert req["source_passages_unresolved"][0]["reason"] == "passage not located: the source is not vendored"
    assert rd._record_view(_records()["tst.limit.l"])["statement"] == "A synthetic limit."
    assert rd._record_view(_records()["tst.term.risky"])["senses"] == {"informational": "A sense."}


def test_passages_come_from_lines_or_quoted_words_and_an_unlocated_one_has_no_text(env):
    records, root = _records(), env["tmp"] / "texts_root"
    lines = ps.resolve_record(records["tst.quote.one"], records, root)["passages"][0]
    assert lines["lines"] == "40-41" and lines["division_path"] == ["Work One", "Chapter II"]
    found = ps.resolve_record(records["tst.dw.plain"], records, root)["passages"][0]
    assert found["division_path"][-1] == "Chapter II" and "chapter two line 50" in found["text"]
    missing = ps.resolve_record(records["tst.term.risky"], records, root)
    assert missing["passages"] == [] and missing["unresolved"][0]["reason"].startswith("passage not located")
    none = ps.resolve_record(records["tst.gravity.g"], records, root)
    assert none["passages"] == [] and none["unresolved"][0]["reason"] == "passage not located: the source is not vendored"


def test_a_division_over_the_cap_keeps_the_cited_lines_whole(env):
    records, root = _records(), env["tmp"] / "texts_root"
    small = ps.resolve_record(records["tst.quote.one"], records, root, cap=40)["passages"][0]
    assert small["trimmed"] is True and "chapter two line 40 of" in small["text"] and "chapter two line 41 of" in small["text"]
    assert len(small["text"].split()) <= 60


def test_a_file_with_no_division_gives_lines_either_side(env):
    texts = env["tmp"] / "texts_root" / "cic" / "texts"
    (texts / "tst2_plain.txt").write_text("\n".join(f"plain line {n} here" for n in range(1, 120)), encoding="utf-8")
    records = {"s": {"id": "s", "kind": "vendored", "edition": "vendored as cic/texts/tst2_plain.txt"},
               "r": {"id": "r", "record_type": "quote", "sources": [{"source_id": "s", "locus": "tst2 line 60"}], "text": "x"}}
    got = ps.resolve_record(records["r"], records, env["tmp"] / "texts_root")["passages"][0]
    assert got["lines"] == "60-60" and got["division_path"] == [] and "plain line 60 here" in got["text"]


def test_real_records_resolve_for_the_cited_records_of_a(env):
    repo = rd.REPO_ROOT
    resolved, unresolved, quote_lines = 0, [], {}
    for world in ("alx", "pahc", "syr"):
        records = load_world_records(world)
        ids = set()
        for line in (rd.SET_DIR / f"A_{world}.jsonl").read_text(encoding="utf-8").splitlines():
            ids |= set(json.loads(line)["citations"])
        for rid in sorted(ids):
            got = ps.resolve_record(records[rid], records, repo)
            if got["passages"]:
                resolved += 1
                if records[rid]["record_type"] == "quote":
                    quote_lines[rid] = got["passages"][0]
            else:
                unresolved.append((rid, got["unresolved"][0]["reason"]))
    assert resolved + len(unresolved) == 153 and resolved >= 100, unresolved
    assert all(r.startswith("passage not located") for _, r in unresolved)
    assert len(quote_lines) == 8
    assert all(reason for _, reason in unresolved)
    bee = quote_lines["alx.quote.clement-bee"]
    assert bee["division_path"][-1].startswith("Chapter I.")
    assert "bee" in bee["text"].lower()


def test_ids_and_order_reproduce_from_the_seed(env):
    (first, k1), (again, k2), (other, k3) = _export(env, "e1"), _export(env, "e2"), _export(env, "e3", seed=8)
    m1, m2, m3 = (json.loads((d / "manifest.json").read_text()) for d in (first, again, other))
    assert m1["order"] == m2["order"] and sorted(m1["items"]) == sorted(m2["items"]) != sorted(m3["items"])
    assert (k1 / "key.json").read_bytes() == (k2 / "key.json").read_bytes()
    assert json.loads((k1 / "seed.json").read_text()) == {"seed": 7}
    assert m1["order"]["reader-1"] != m1["order"]["reader-2"]
    assert rd.item_id(7, "k") == rd.item_id(7, "k") != rd.item_id(8, "k")


def test_the_seed_is_written_before_the_draw(env, monkeypatch):
    order = []
    original = rd.write_seed
    monkeypatch.setattr(rd, "write_seed", lambda key_dir, seed: (order.append("seed"), original(key_dir, seed)))
    monkeypatch.setattr(rd, "shuffled", lambda *a, **k: (order.append("draw"), sorted(a[0]))[1])
    _export(env)
    assert order[0] == "seed" and "draw" in order


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
    assert rd.needs_adjudication(_reply("i", "a", errors=[_error(tier=1)]), _reply("i", "b", errors=[_error(tier=1)]))
    assert not rd.needs_adjudication(_reply("i", "a", errors=[_error(tier=3)]), _reply("i", "b", errors=[_error(tier=3)]))
    one = _reply("i", "a", errors=[_error("alpha beta gamma", tier=3), _error("delta epsilon zeta", tier=3)])
    two = _reply("i", "b", errors=[_error("alpha beta gamma", tier=3)])
    assert rd.needs_adjudication(one, two) and rd.needs_adjudication(two, one)


def test_adjudicate_writes_requests_only_for_triggered_items(env):
    out, _ = _export(env)
    ids = sorted(json.loads((out / "manifest.json").read_text())["items"])
    for n, iid in enumerate(ids):
        _file(out, "reader-1", iid, _reply(iid, "reader-1", 2))
        _file(out, "reader-2", iid, _reply(iid, "reader-2", 1 if n == 0 else 2, errors=[_error(tier=3)] if n == 1 else None))
    assert rd.main(["adjudicate", "--export-dir", str(out)]) == 0
    listing = json.loads((out / "adjudication_manifest.json").read_text())
    assert sorted(listing["items"]) == [ids[0], ids[1]]
    req = json.loads(Path(listing["items"][ids[1]]["request"]).read_text())
    assert req["kind"] == "adjudication" and len(req["reader_findings"]) == 2 and req["source_passages"]
    assert not re.search(r"\barm\b", json.dumps(req))


def _fill(out, keys, readers=rd.READERS, skip=()):
    for iid in json.loads((out / "manifest.json").read_text())["items"]:
        for r in readers:
            if (r, iid) not in skip:
                _file(out, r, iid, _reply(iid, r))


def test_after_october_goes_out_per_reader_only_when_every_blind_reply_is_filed(env):
    out, keys = _export(env)
    a0 = _id_of(keys, f"{WORLD}|a|1|p00")
    b0 = _id_of(keys, f"{WORLD}|b|1|p00")
    _fill(out, keys, skip={("reader-2", b0)})
    assert rd.main(["after-october", "--export-dir", str(out), "--key-dir", str(keys), "--set-dir", str(env["set"])]) == 0
    listing = json.loads((out / "after_october_manifest.json").read_text())
    assert sorted(listing["items"]) == sorted(f"reader-1/{i}" for i, m in _key(keys).items() if m["arm"] == "a")
    assert listing["readers_held_back_missing_blind_replies"] == {"reader-2": 1}
    req = json.loads(Path(listing["items"][f"reader-1/{a0}"]["request"]).read_text())
    assert req["october_review"]["second_pass"]["rigor"] == "NOT ACCEPTABLE" and req["your_filed_reply"]["depth"] == "rich"


def _seed_file(env, keys, count, defect="modern_projection"):
    bases = [m["key"] for m in _key(keys).values() if m["arm"] == "a"][:count]
    copies = [{"base": b, "answer_text": f"Planted answer {n} about gamma and a planted claim.", "defect_type": defect,
               "expected_location": "planted claim here today"} for n, b in enumerate(bases)]
    path = env["tmp"] / "copies.json"
    path.write_text(json.dumps(copies), encoding="utf-8")
    return path


def test_seed_copies_are_indistinguishable_in_form_and_the_key_is_sealed(env, capsys):
    out, keys = _export(env)
    capsys.readouterr()
    path = _seed_file(env, keys, 10)
    assert rd.main(["seed-copies", "--export-dir", str(out), "--key-dir", str(keys), "--copies", str(path)]) == 0
    sealed = json.loads((keys / "seed_key.json").read_text())
    assert len(sealed["items"]) == 10 and not (out / "key").exists()
    assert json.loads(capsys.readouterr().out)["seed_key_sha256"] == rd._sha256(keys / "seed_key.json")
    manifest = json.loads((out / "manifest.json").read_text())
    assert len(manifest["items"]) == 32 + 10 and "seed" not in manifest
    fake = next(iter(sealed["items"]))
    base = _id_of(keys, sealed["items"][fake]["base"])
    r_req, f_req = (json.loads((out / "requests" / "reader-1" / f"{i}.json").read_text()) for i in (base, fake))
    assert set(r_req) == set(f_req) and f_req["answer"].startswith("Planted answer")
    assert rd.main(["seed-copies", "--export-dir", str(out), "--key-dir", str(keys), "--copies", str(path)]) == 2
    assert rd.main(["seed-copies", "--export-dir", str(out), "--key-dir", str(keys), "--copies", str(_seed_file(env, keys, 9))]) == 2


def test_a_defect_type_the_catch_check_cannot_match_is_refused(env):
    out, keys = _export(env)
    assert rd.main(["seed-copies", "--export-dir", str(out), "--key-dir", str(keys), "--copies", str(_seed_file(env, keys, 10, "mystery"))]) == 2


def test_a_catch_needs_the_defect_type_and_half_the_planted_span():
    planted = {"defect_type": "modern_projection", "expected_location": "the planted claim here today"}
    right = _reply("i", "r", errors=[_error("a planted claim here", typ="modern projection")])
    assert rd.catches(right, planted)
    assert not rd.catches(_reply("i", "r", errors=[_error("a planted claim here", typ="invented")]), planted)
    assert not rd.catches(_reply("i", "r", errors=[_error("claim", typ="modern projection")]), planted)
    assert not rd.catches(_reply("i", "r", errors=[_error("an unrelated long sentence about other things", typ="modern projection")]), planted)
    assert rd.accepted_error_types("wrong frame") == {"out of context"}


def _score(env, out, keys, **kw):
    return rd.compute_tables(out, keys, env["set"], env["band"])


def _scored_export(env, caught_by_second):
    out, keys = _export(env)
    rd.main(["seed-copies", "--export-dir", str(out), "--key-dir", str(keys), "--copies", str(_seed_file(env, keys, 10))])
    sealed = json.loads((keys / "seed_key.json").read_text())["items"]
    err = _error("a planted claim here today", tier=2, typ="modern projection")
    for n, iid in enumerate(sorted(sealed)):
        _file(out, "reader-1", iid, _reply(iid, "reader-1", errors=[err]))
        _file(out, "reader-2", iid, _reply(iid, "reader-2", errors=[err] if n < caught_by_second else []))
        _file(out, "adjudicator", iid, _reply(iid, "adjudicator", errors=[err]))
    for iid, m in _key(keys).items():
        for r in rd.READERS:
            _file(out, r, iid, _reply(iid, r, 2 if m["arm"] == "a" else 1))
    return out, keys


def test_the_catch_rate_gate(env):
    assert rd.catch_gate({"seeded": 10, "missing": [], "by_reader": {r: {"rate": 0.9, "caught": 9} for r in rd.READERS}})["scores_count"]
    low = rd.catch_gate({"seeded": 10, "missing": [], "by_reader": {"reader-1": {"rate": 1.0, "caught": 10}, "reader-2": {"rate": 0.8, "caught": 8}}})
    assert not low["scores_count"] and "reader-2 caught 8 of 10" in low["reasons"][0]
    assert not rd.catch_gate({"seeded": 9, "missing": [], "by_reader": {r: {"rate": 1.0, "caught": 9} for r in rd.READERS}})["scores_count"]
    tables = _score(env, *_scored_export(env, 8))
    assert not tables["gate"]["scores_count"] and "SCORES DO NOT COUNT" in rd.render_markdown(tables)
    ok = _score(env, *_scored_export_again(env))
    assert ok["gate"]["scores_count"] and "SCORES DO NOT COUNT" not in rd.render_markdown(ok)


def _scored_export_again(env):
    out, keys = _export(env, "exp_clean")
    rd.main(["seed-copies", "--export-dir", str(out), "--key-dir", str(keys), "--copies", str(_seed_file(env, keys, 10))])
    err = _error("a planted claim here today", tier=2, typ="modern projection")
    for iid in json.loads((keys / "seed_key.json").read_text())["items"]:
        for r in rd.READERS:
            _file(out, r, iid, _reply(iid, r, errors=[err]))
        _file(out, "adjudicator", iid, _reply(iid, "adjudicator", errors=[err]))
    return out, keys


def test_score_tables_use_rulings_and_report_agreement_noise_band_and_october(env):
    out, keys = _scored_export(env, 10)
    split = _id_of(keys, f"{WORLD}|b|1|p00")
    _file(out, "reader-2", split, _reply(split, "reader-2", 2))
    assert split in _score(env, out, keys)["awaiting_adjudication"]
    _file(out, "adjudicator", split, _reply(split, "adjudicator", 0, errors=[_error("delta", tier=1, typ="invented")]))
    t = _score(env, out, keys)
    assert t["awaiting_adjudication"] == []
    assert t["scores"]["source_accuracy"]["a"][WORLD]["mean"] == 2 and t["scores"]["source_accuracy"]["a"][WORLD]["n"] == 14
    assert t["scores"]["source_accuracy"]["b"][WORLD]["distribution"] == {"0": 1, "1": 13, "2": 0}
    assert t["reader_agreement"]["source_accuracy"]["exact"] == pytest.approx(1 - 1 / 32)
    assert t["noise_floor"]["repeat_probes"] == 4 and t["noise_floor"]["by_dimension"]["source_accuracy"]["exact"] == 0.75
    assert t["error_counts"][WORLD]["b"]["invented"] == {"1": 1} and t["error_counts"]["all"]["b"]["invented"] == {"1": 1}
    band = t["older_engine_band"]["by_world"][WORLD]
    assert band["spread"]["words"] == {"min": 1, "max": 5} and band["runs"]["r2"]["check_pass_rate"] == 1.0
    assert t["older_engine_band"]["current_arms_by_world"][WORLD]["a"]["n"] == 14
    grades = t["october_comparison"]["by_grade"]
    assert grades["rigor"]["NOT ACCEPTABLE"] == {"n": 1, "mean_fresh": 2} and grades["understandable"]["POOR"]["n"] == 1
    md = rd.render_markdown(t)
    assert "Older-engine band" in md and "Fresh scores against the October grades" in md and "| tst | b | invented | 1 | 0 | 0 |" in md


def test_october_findings_are_all_kept_and_matches_are_only_candidates(env):
    out, keys = _scored_export(env, 10)
    b1 = _id_of(keys, f"{WORLD}|b|1|p01")
    for r in rd.READERS:
        _file(out, r, b1, _reply(b1, r, 1, errors=[_error("Answer beta for p01 about delta", tier=3)]))
    table = _score(env, out, keys)["october_errors"]
    rows = {(e["probe_id"], e["source"]): e for e in table}
    referee = next(e for e in table if e["claim"] == "Answer beta for p01 about delta")
    assert referee["b_status"] == "candidate repeated" and referee["claim_wording_in_b_answer"] is True and referee["may_be_confirmation"]
    assert len([e for e in table if e["probe_id"] == "p01"]) == 2
    quoted = rows[("p00", "second pass rigor")]
    assert quoted["match_text"] == ["Answer alpha for p00 about gamma"] and quoted["b_status"] == "no candidate found"
    assert rows[("p02", "second pass rigor")]["b_status"] == "unmatched (for V10)"
    assert ("p02", "second pass craft") in rows and ("p04", "second pass rigor") not in rows
    assert not any(e["b_status"] == "not repeated" for e in rows.values())


def test_after_october_errors_are_counted_under_their_own_arm_and_unknown_ids_are_skipped(env):
    out, keys = _scored_export(env, 10)
    a0 = _id_of(keys, f"{WORLD}|a|1|p00")
    added = {"item_id": a0, "reader": "reader-1", "added_errors": [{**_error(tier=2, typ="invented"), "after_october_review": True}]}
    for iid, reply in ((a0, added), ("iunknown", {**added, "item_id": "iunknown"})):
        path = out / "replies" / "after-october" / "reader-1" / f"{iid}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(reply), encoding="utf-8")
    t = _score(env, out, keys)
    assert t["after_october_error_counts"] == {WORLD: {"a": {"invented": {"2": 1}}}, "all": {"a": {"invented": {"2": 1}}}}


def test_mark_pack_gives_twelve_per_world_with_the_same_probes_in_both_arms(env):
    out, keys = env["tmp"] / "pack", env["tmp"] / "pack_keys"
    argv = ["mark-pack", "--set-dir", str(env["set"]), "--b", str(env["run1"]), "--worlds", WORLD, "--out", str(out), "--key-dir", str(keys), "--seed", "3"]
    assert rd.main(argv) == 0
    pack = json.loads((out / "mark_pack.json").read_text())["items"]
    key = json.loads((keys / "mark_pack_key.json").read_text())["items"]
    assert json.loads((keys / "seed.json").read_text()) == {"seed": 3} and not (out / "mark_pack_key.json").exists()
    assert len(pack) == 24
    by_arm = {a: sorted(m["probe_id"] for m in key.values() if m["arm"] == a) for a in ("a", "b")}
    assert by_arm["a"] == by_arm["b"] and len(set(by_arm["a"])) == 12
    assert set(pack[0]) == {"item_id", "world", "question", "answer", "cited_records", "source_lines"}
    assert pack[0]["source_lines"] and pack[0]["source_lines"][0]["division_path"]
    assert not re.search(r"\barm\b", json.dumps(pack))
    again = env["tmp"] / "pack2"
    rd.main(argv[:-6] + ["--out", str(again), "--key-dir", str(env["tmp"] / "pack2_keys"), "--seed", "3"])
    assert (again / "mark_pack.json").read_bytes() == (out / "mark_pack.json").read_bytes()


def test_mark_pack_passages_are_trimmed_but_in_context(env):
    out, keys = env["tmp"] / "pack", env["tmp"] / "pack_keys"
    assert rd.main(["mark-pack", "--set-dir", str(env["set"]), "--b", str(env["run1"]), "--worlds", WORLD, "--out", str(out),
                    "--key-dir", str(keys), "--seed", "3", "--per-world", "12"]) == 0
    line = next(s for i in json.loads((out / "mark_pack.json").read_text())["items"] for s in i["source_lines"] if s["lines"] == "40-41")
    assert len(line["text"].split()) <= rd.MARK_PASSAGE_WORDS + 20 and "chapter two line 40 of" in line["text"]


def test_the_pick_favours_quote_placing_and_t_or_e_probes():
    cands = [{"probe_id": f"q{n}", "cell": "F1-T" if n < 20 else "F1-I", "places_quote": n < 20} for n in range(40)]
    wins = sum(sum(c["probe_id"] in {x["probe_id"] for x in rd.pick_probes(cands, 12, s, "w")} for c in cands[:20]) for s in range(30))
    assert wins / (30 * 12) > 0.7
    assert rd.register_of("C-E") == "E" and rd.register_of("F4-T") == "T"
    with pytest.raises(ValueError):
        rd.register_of("F4-X")


def test_writing_into_the_repository_is_refused(env, capsys):
    inside = rd.REPO_ROOT / "engine" / "m3" / "_v7_read_refused_probe_dir"
    outside = env["tmp"] / "fine"
    for argv in (["export", "--set-dir", str(env["set"]), "--b", str(env["run1"]), "--worlds", WORLD, "--out", str(inside),
                  "--key-dir", str(outside / "k1"), "--seed", "1"],
                 ["export", "--set-dir", str(env["set"]), "--b", str(env["run1"]), "--worlds", WORLD, "--out", str(outside / "o2"),
                  "--key-dir", str(inside), "--seed", "1"],
                 ["mark-pack", "--set-dir", str(env["set"]), "--b", str(env["run1"]), "--worlds", WORLD, "--out", str(inside),
                  "--key-dir", str(outside / "k3"), "--seed", "1"]):
        assert rd.main(argv) == 2
    assert not inside.exists()
    assert "inside the repository" in capsys.readouterr().err
    with pytest.raises(rd.Refused):
        rd.require_outside_repo(rd.REPO_ROOT / "Build")


def test_the_key_directory_may_not_sit_inside_the_export(env):
    out = env["tmp"] / "exp_nested"
    assert rd.main(["export", "--set-dir", str(env["set"]), "--b", str(env["run1"]), "--worlds", WORLD, "--out", str(out),
                    "--key-dir", str(out / "keys"), "--seed", "1"]) == 2


def test_a_reply_that_does_not_fit_is_reported_not_scored(env):
    out, keys = _export(env)
    iid = sorted(json.loads((out / "manifest.json").read_text())["items"])[0]
    bad = _reply(iid, "reader-1")
    bad["scores"]["source_accuracy"]["score"] = 3
    _file(out, "reader-1", iid, bad)
    t = _score(env, out, keys)
    assert t["invalid_replies"][0]["item_id"] == iid and t["items_scored"] == 0


def test_a_record_citing_one_source_twice_shows_each_passage(env):
    records, root = _records(), env["tmp"] / "texts_root"
    twice = {"id": "tst.dw.twice", "record_type": "doctrinal_witness",
             "sources": [{"source_id": "tst.source.x", "locus": "tst1 lines 40-41"}, {"source_id": "tst.source.x", "locus": "tst1 lines 60-61"}]}
    got = ps.resolve_record(twice, records, root)["passages"]
    assert [p["lines"] for p in got] == ["40-41", "60-61"] and [p["locus"] for p in got] == ["tst1 lines 40-41", "tst1 lines 60-61"]


def test_sources_cut_by_the_passage_cap_are_listed(env):
    records, root = _records(), env["tmp"] / "texts_root"
    many = {"id": "tst.dw.many", "record_type": "doctrinal_witness",
            "sources": [{"source_id": "tst.source.x", "locus": f"tst1 lines {n}-{n}"} for n in range(35, 35 + ps.MAX_PASSAGES_PER_RECORD + 2)]}
    got = ps.resolve_record(many, records, root)
    assert len(got["passages"]) == ps.MAX_PASSAGES_PER_RECORD
    cut = [u for u in got["unresolved"] if u["reason"] == f"cut by the {ps.MAX_PASSAGES_PER_RECORD}-passage cap"]
    assert len(cut) == 2 and ps.MAX_PASSAGES_PER_RECORD == 5


def test_same_words_with_different_types_go_to_adjudication_and_findings_are_not_counted_twice():
    a = _reply("i", "a", errors=[_error("alpha beta gamma", tier=3, typ="invented")])
    b = _reply("i", "b", errors=[_error("alpha beta gamma", tier=3, typ="misquoted")])
    assert rd.needs_adjudication(a, b)
    ruled = _reply("i", "adj", errors=[_error("alpha beta gamma", tier=2, typ="invented"), _error("alpha beta gamma delta", tier=2, typ="misquoted")])
    assert len(rd._final_errors(a, b, ruled)) == 1
