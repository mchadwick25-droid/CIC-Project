import json
import os
import subprocess
import sys
from dataclasses import replace
from pathlib import Path

import pytest

from index import bench, benchreport, catalog, contract, estimate, generate, retrieve, sample, store, windows
from index.check import check_context_line
from index.pricing import MODEL_ID, price_table
from index.prompting import allowed_text, build_request, window_block
from ixfixture import FILE_NAME, FakeClient, write_fixture, write_passage_jsonl

CLI = Path(__file__).resolve().parents[1] / "cli.py"
from engine.provider import guard  # noqa: E402


@pytest.fixture
def world(tmp_path):
    passages, entry = write_fixture(tmp_path / "texts")
    out_dir = tmp_path / "out"
    write_passage_jsonl(contract.passages_dir(out_dir) / f"{contract.file_stem(FILE_NAME)}.jsonl", passages)
    return passages, entry, out_dir, tmp_path / "texts"


@pytest.fixture
def approved(tmp_path, monkeypatch):
    monkeypatch.setenv(guard.LEDGER_ENV, str(tmp_path / "ledger.jsonl"))
    guard.reset_for_tests()
    yield
    guard.reset_for_tests()


def guarded(client, cap):
    return guard.wrap(client, guard.LiveTest("fixture run", cap), provider="anthropic")


def test_contract_roundtrip_and_missing_field(world, tmp_path):
    passages, _, out_dir, _ = world
    loaded = contract.read_file_passages(out_dir, FILE_NAME)
    assert [p.passage_id for p in loaded] == [p.passage_id for p in passages]
    assert loaded[0].speaker_state == "known" and loaded[0].row_ids == ("lpc.row.one",)
    bad = tmp_path / "bad.jsonl"
    bad.write_text(json.dumps({"passage_id": "x"}) + "\n", encoding="utf-8")
    with pytest.raises(contract.ContractError):
        contract.read_passages(bad)


def test_windows_partition_keep_divisions_and_meet_cache_minimum(world):
    passages, *_ = world
    many = [replace(passages[i % len(passages)], passage_id=f"p{i}", division_locus=str(i // 4)) for i in range(120)]
    built = windows.build_windows("f", many, lambda p: 300, 400)
    covered = [i for w in built for i in w.indices()]
    assert covered == list(range(120))
    assert all(w.prefix_tokens <= windows.MAX_PREFIX_TOKENS + windows.MIN_PREFIX_TOKENS for w in built)
    assert all(w.cacheable for w in built[:-1])
    for w in built:
        divisions = {many[i].division_locus for i in w.indices()}
        for division in divisions:
            members = [i for i, p in enumerate(many) if p.division_locus == division]
            if sum(300 + windows.MARKER_TOKENS for _ in members) <= windows.MAX_PREFIX_TOKENS - 400:
                assert set(members) <= set(w.indices())


def test_oversize_division_is_split_and_edges_get_neighbours(world):
    passages, entry, *_ = world
    one_division = [replace(passages[0], passage_id=f"p{i}", division_locus="1") for i in range(60)]
    built = windows.build_windows("f", one_division, lambda p: 500, 400)
    assert len(built) > 1
    assert windows.oversize_divisions(one_division, lambda p: 500, 400) == 1
    previous, following = windows.neighbor_outside(built[1], one_division, built[1].start)
    assert previous is one_division[built[1].start - 1] and following is None


def test_context_check_flags_invented_entities_and_passes_supplied_ones(world):
    passages, entry, *_ = world
    window = windows.Window(FILE_NAME, 0, 3, 100, 100)
    supplied = allowed_text(entry, window, passages, 0)
    assert check_context_line("This passage from Cyprian on the lapsed opens the first division.", supplied).ok
    flagged = check_context_line("This passage from Cyprian recalls the Council of Nicaea in 325.", supplied)
    assert not flagged.ok and any(r.startswith("entity_not_supplied:Nicaea") for r in flagged.reasons)
    assert not check_context_line("", supplied).ok


def test_request_marks_the_prefix_for_caching_and_keeps_the_target_out_of_it(world):
    passages, entry, *_ = world
    big = windows.Window(FILE_NAME, 0, 3, 5000, 100)
    request = build_request(MODEL_ID, entry, big, passages, 1)
    prefix, fresh = request["messages"][0]["content"]
    assert prefix["cache_control"] == {"type": "ephemeral"}
    assert prefix["text"] == window_block(entry, big, passages)
    assert passages[1].passage_id in fresh["text"] and "cache_control" not in fresh
    small = windows.Window(FILE_NAME, 0, 3, 50, 100)
    assert "cache_control" not in build_request(MODEL_ID, entry, small, passages, 1)["messages"][0]["content"][0]


def test_estimate_prices_one_window_from_the_repo_table(world):
    passages, entry, out_dir, _ = world
    plan = estimate.plan_file(entry, out_dir)
    assert plan.source == "segmented" and plan.passages == len(passages)
    table = price_table()
    assert table.cache_read_per_token == pytest.approx(0.10e-6)
    low, high = plan.dollars("low", table), plan.dollars("high", table)
    assert 0 < low < high
    expected_output = len(passages) * estimate.BANDS["high"].output_tokens * table.output_per_token
    assert plan.usage["high"].breakdown(table)["output"] == pytest.approx(expected_output)
    assert sum(plan.usage["high"].breakdown(table).values()) == pytest.approx(high)


def test_modeled_plan_when_no_segmenter_output(world, tmp_path, monkeypatch):
    _, entry, _, texts = world
    monkeypatch.setattr(catalog, "TEXTS_DIR", texts)
    plan = estimate.plan_file(entry, tmp_path / "empty-out")
    assert plan.source == "modeled" and plan.passages >= 1


def test_run_resumes_and_logs_without_repeating_calls(world, approved):
    passages, entry, out_dir, _ = world
    client = FakeClient()
    jobs = [generate.Job(entry, passages)]
    first = generate.run_jobs(guarded(client, 5.0), jobs, out_dir, MODEL_ID, "fixture run", (guard.LiveTestCapReached,))
    assert first.generated == len(passages) and first.stopped is None and first.remaining == 0
    assert len(client.messages.requests) == len(passages)
    again = generate.run_jobs(guarded(client, 5.0), jobs, out_dir, MODEL_ID, "fixture run", (guard.LiveTestCapReached,))
    assert again.generated == 0 and again.skipped == len(passages)
    assert len(client.messages.requests) == len(passages)
    lines = generate.read_context_lines(out_dir, FILE_NAME)
    assert set(lines) == {p.passage_id for p in passages} and all(r["live_test"] == "fixture run" for r in lines.values())
    ledger = [json.loads(l) for l in open(os.environ[guard.LEDGER_ENV])]
    assert {l["live_test"] for l in ledger} == {"fixture run"}


def test_run_stops_before_the_cap_and_resumes_later(world, approved):
    passages, entry, out_dir, _ = world
    client = FakeClient()
    jobs = [generate.Job(entry, passages)]
    stopped = generate.run_jobs(guarded(client, 0.0035), jobs, out_dir, MODEL_ID, "fixture run", (guard.LiveTestCapReached,))
    assert stopped.stopped.startswith("cap") and 0 < stopped.generated < len(passages)
    assert stopped.remaining == len(passages) - stopped.generated
    guard.reset_for_tests()
    rest = generate.run_jobs(guarded(client, 5.0), jobs, out_dir, MODEL_ID, "fixture run", (guard.LiveTestCapReached,))
    assert rest.generated == stopped.remaining and rest.remaining == 0


def test_flagged_lines_are_recorded_but_not_indexed(world, approved, tmp_path):
    passages, entry, out_dir, texts = world
    client = FakeClient("This is the Council of Nicaea in 325 held under Constantine.")
    generate.run_jobs(guarded(client, 5.0), [generate.Job(entry, passages)], out_dir, MODEL_ID, "fixture run", (guard.LiveTestCapReached,))
    records = generate.read_context_lines(out_dir, FILE_NAME)
    assert all(r["status"] == "flagged" for r in records.values())
    assert store.usable_contexts(records, passages) == {}


def test_index_search_filters_version_and_source_links(world, tmp_path):
    passages, entry, out_dir, texts = world
    contexts = {passages[0].passage_id: "Opening of the letter on the lapsed, by Cyprian."}
    db = tmp_path / "index.sqlite"
    version = store.build_index(db, passages, contexts, {FILE_NAME: entry}, MODEL_ID)
    assert store.read_meta(db)["version"] == version
    assert store.build_index(db, passages, contexts, {FILE_NAME: entry}, MODEL_ID) == version
    changed = store.build_index(tmp_path / "other.sqlite", passages, {passages[0].passage_id: "Another line."}, {FILE_NAME: entry}, MODEL_ID)
    assert changed != version

    hits = retrieve.search(db, "lapsed letter", world="lpc", roles=["tradition"])
    assert hits and hits[0].passage_id == passages[0].passage_id
    assert hits[0].text == passages[0].text and hits[0].context not in hits[0].text
    source = hits[0].source
    assert source["path"] == f"cic/texts/{FILE_NAME}" and source["byte_start"] == passages[0].byte_start
    assert source["row_ids"] == ["lpc.row.one"] and source["speaker"]["state"] == "known" and source["ocr_score"] == 0.95
    assert retrieve.search(db, "church", world="other") == []
    assert retrieve.search(db, "church", roles=["none"]) == []
    assert all(h.source["speaker"]["state"] == "known" for h in retrieve.search(db, "church", speakers=["known"]))
    assert all(h.source["ocr_score"] >= 0.9 for h in retrieve.search(db, "church", min_ocr=0.9))
    assert retrieve.by_work_locus(db, f"{FILE_NAME}#2") == [passages[3].passage_id, passages[4].passage_id]
    assert retrieve.search(db, "Opening Cyprian", world="lpc")[0].passage_id == passages[0].passage_id


def test_every_indexed_passage_resolves_to_its_vendored_span(world, tmp_path):
    passages, entry, out_dir, texts = world
    db = tmp_path / "index.sqlite"
    store.build_index(db, passages, {}, {FILE_NAME: entry}, MODEL_ID)
    assert retrieve.verify_sources(db, texts) == []
    path = texts / FILE_NAME
    path.write_text(path.read_text(encoding="utf-8").replace("Cyprian writes", "Cyprian wrote "), encoding="utf-8")
    assert [p["passage_id"] for p in retrieve.verify_sources(db, texts)] == [passages[0].passage_id]


def test_sample_takes_whole_divisions_and_skips_front_matter(world):
    passages, *_ = world
    taken = sample.take_divisions(passages, 4)
    assert {p.division_locus for p in taken} == {"1", "2"}
    assert [p.ordinal for p in taken] == [1, 2, 3, 4, 5]


def test_unapproved_run_exits_with_the_rule_before_any_work(tmp_path):
    done = subprocess.run([sys.executable, str(CLI), "--out-dir", str(tmp_path), "run", "--union"], capture_output=True, text=True)
    assert done.returncode == guard.EXIT_REFUSED
    assert guard.RULE in done.stderr and "RUN SETTINGS" not in done.stdout
    cap_only = subprocess.run([sys.executable, str(CLI), "--out-dir", str(tmp_path), "run", "--union", "--cap-usd", "3"], capture_output=True, text=True)
    assert cap_only.returncode == guard.EXIT_REFUSED


def test_dry_run_refuses_to_guess_passages_without_segmenter_output(tmp_path):
    done = subprocess.run([sys.executable, str(CLI), "--out-dir", str(tmp_path), "run", "--world", "lpc", "--dry-run"], capture_output=True, text=True)
    assert done.returncode != 0 and "no segmenter output" in done.stderr


def test_cli_run_prints_settings_before_the_first_call_and_logs(world, approved, monkeypatch, capsys, tmp_path):
    import importlib.util
    from engine.provider import anthropic_direct

    spec = importlib.util.spec_from_file_location("ix_cli", CLI)
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)

    passages, entry, out_dir, _ = world
    client = FakeClient()
    seen = {}

    def make_client():
        seen["printed_before_client"] = "RUN SETTINGS" in capsys.readouterr().out
        return guarded(client, 5.0)

    monkeypatch.setattr(cli.catalog, "load_shelves", lambda: {FILE_NAME: entry})
    monkeypatch.setattr(anthropic_direct, "make_client", make_client)
    argv = ["cli.py", "--out-dir", str(out_dir), "run", "--world", "lpc", "--live-test", "fixture run", "--cap-usd", "5"]
    monkeypatch.setattr(sys, "argv", argv)
    assert cli.main(argv[1:]) == 0
    assert seen["printed_before_client"] and len(client.messages.requests) == len(passages)
    log = json.loads((generate.context_dir(out_dir) / "_runs.jsonl").read_text().splitlines()[0])
    assert log["generated"] == len(passages) and log["run"]["name"] == "fixture run" and log["run"]["cap_usd"] == 5.0
    monkeypatch.setattr(sys, "argv", argv[:6] + ["--dry-run"])
    assert cli.main(argv[1:6] + ["--dry-run"]) == 0
    assert "Passages still to do (resume skips the rest): 0" in capsys.readouterr().out


def test_selector_picks_xml_weakest_ocr_and_latin_files(world, tmp_path):
    passages, entry, _, _ = world
    out_dir = tmp_path / "selector-out"

    def lay_out(name, language, ocr):
        copies = [replace(p, passage_id=f"{name}:{i}", file=name, language=language, ocr_score=ocr, apparatus=False,
                          division_locus=str(i // 5), ordinal=i) for i, p in enumerate(passages * 9)]
        write_passage_jsonl(contract.passages_dir(out_dir) / f"{contract.file_stem(name)}.jsonl", copies)
        return replace(entry, file=name)

    entries = [lay_out("a_edition.xml", "eng", 0.99), lay_out("b-lat_scan.txt", "lat", 0.97), lay_out("c-fra_scan.txt", "fra", 0.60)]
    chosen = {s.role: s for s in sample.select_sample(entries, out_dir, per_file=12)}
    assert chosen["xml"].file == "a_edition.xml" and chosen["weak_ocr"].file == "c-fra_scan.txt" and chosen["latin"].file == "b-lat_scan.txt"
    assert all(len(s.passage_ids) >= 12 for s in chosen.values())
    path = tmp_path / "selection.json"
    sample.write_selection(path, "lpc", list(chosen.values()))
    assert sample.read_selection(path)[1][0].passage_ids == list(chosen.values())[0].passage_ids


def _bench_world(world, tmp_path):
    passages, entry, out_dir, texts = world
    db = tmp_path / "bench.sqlite"
    store.build_index(db, passages, {}, {FILE_NAME: entry}, MODEL_ID)
    records = tmp_path / "records" / "lpc"
    (records / "quote").mkdir(parents=True)
    (records / "doctrinal_witness").mkdir()
    quote = passages[3].text
    (records / "quote" / "lpc.quote.unity.md").write_text(
        "---\nid: lpc.quote.unity\nrecord_type: quote\nsources:\n- source_id: x\n  locus: cic/texts/%s, line 99\ntext: %s\n---\nbody\n" % (FILE_NAME, quote),
        encoding="utf-8")
    (records / "doctrinal_witness" / "lpc.witness.lapsed.md").write_text(
        "---\nid: lpc.witness.lapsed\nrecord_type: doctrinal_witness\nsources:\n- source_id: y\n  locus: the letter, cic/texts/%s, lines 3-3\n---\nbody\n" % FILE_NAME,
        encoding="utf-8")
    coverage = tmp_path / "coverage"
    coverage.mkdir()
    (coverage / "C1-coverage.json").write_text(json.dumps({"worlds": {"lpc": {"S1": {"records": ["lpc.quote.unity", "lpc.witness.lapsed", "lpc.quote.absent"]}}}}))
    subs = {"C1.S1": {"id": "C1.S1", "label": "Unity", "ids": ["Q1", "Q2"]}}
    questions = {"Q1": "What did the bishop urge about the unity of the church?", "Q2": "Why wait for judgment of repentance?"}
    evidence = bench.load_record_evidence(records.parent / "lpc")
    return db, texts, evidence, bench.load_cells("lpc", coverage), subs, questions


def test_citations_parse_files_and_line_ranges():
    found = bench.parse_citations("x cic/texts/a.xml, lines 23591-23604; Latin at cic/texts/b.txt, lines 12467-12478 and 5, 9")
    assert [(c.file, c.start, c.end) for c in found] == [
        ("a.xml", 23591, 23604), ("b.txt", 12467, 12478), ("b.txt", 5, 5), ("b.txt", 9, 9)]


def test_bench_reaches_cited_passages_and_reports_unresolvable_records(world, tmp_path):
    db, texts, evidence, cells, subs, questions = _bench_world(world, tmp_path)
    cases, gold, ungrounded = bench.run_bench(db, "lpc", evidence, cells, subs, questions, texts)
    passages = world[0]
    assert set(gold["lpc.quote.unity"]) == {passages[3].passage_id}
    assert set(gold["lpc.witness.lapsed"]) == {passages[1].passage_id}
    by = {(c.wording_id, c.record_id): c.best_rank for c in cases}
    assert by[("Q1", "lpc.quote.unity")] == 1
    assert ungrounded["C1.S1"] == ["lpc.quote.absent"]
    assert bench.recall(cases, 5) > 0
    text = benchreport.render_report(db, "lpc", cases, gold, ungrounded, {"C1": "Jesus"}, subs, store.read_meta(db))
    assert "recall@10" in text and "lpc.quote.absent" in text and "C1 Jesus" in text
