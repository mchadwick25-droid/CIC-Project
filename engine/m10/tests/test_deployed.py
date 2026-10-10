"""Hermetic tests for engine.m10.deployed: fixtures live under tmp_path."""
import hashlib
import json

import pytest

from engine.m10 import deployed
from engine.m10.common import REPO_ROOT
from engine.m10.deployed import (
    ProbeTargetRefused,
    assert_compiled_target,
    check_citations,
    check_deployed,
    check_probe_pins,
    check_prompt_content,
    repin_command,
    runner_dry_run,
)

HARDENING = (
    "No invented memory. No explaining what kind of thing is speaking. No narrating our own refusal to answer. "
    "No 'I' smuggled in through a list of named roles."
)


def _record(code, rtype, slug, **fields):
    return {"id": f"{code}.{rtype}.{slug}", "record_type": rtype, **fields}


ENTRIES = ["the Demonstrations", "the Didascalia", "the Acts of Thomas", "the Odes", "the Book of Steps", "the Liber Graduum"]
ANCHOR = (
    "Our images come from " + ", ".join(ENTRIES) + ". "
    "When a fitting image does not come from what formed us, we fall back to the plain shape of our own life."
)


def _records(quotes=3, living=None, anchor=ANCHOR, entries=tuple(ENTRIES)):
    records = {}
    craft = _record("w", "voice_craft", "craft", **({"source_anchor": anchor, "source_anchor_entries": list(entries)} if anchor else {}))
    records[craft["id"]] = craft
    for i in range(quotes):
        r = _record("w", "quote", f"q{i}")
        records[r["id"]] = r
    g = _record("w", "gravity", "g1", classification="primary", confidence={"formation_confidence": "Documented"})
    core = _record("w", "world_core", "w", **({"living_traditions": living} if living else {}))
    records[g["id"]] = g
    records[core["id"]] = core
    return records


def _prompt(gravities=1, living=None, self_reference=HARDENING, quotation="Every quote record offered in this turn's ground qualifies.", anchor=ANCHOR):
    parts = ([f"## Where our images come from\n\n{anchor}\n"] if anchor else []) + ["## How we word things", f"- [self-reference] Strict we-voice. {self_reference}", f"- [quotation] {quotation}", "",
             "## Gravities (cite as [[w.core.w]])"] + [f"- [[w.gravity.g{i}]] Name" for i in range(1, gravities + 1)] + [""]
    if living:
        parts += ["## Living traditions (cite as [[w.core.w]])", "", living, ""]
    return "\n".join(parts) + "\n"


def _ids(findings):
    return sorted({f.check for f in findings})


def test_guard_refuses_legacy_prompt_and_capsule_files(tmp_path):
    for name in ("gallic_Representative_Permanent_Prompt_Renatus.txt", "Gallic_Capsule_Core.md"):
        with pytest.raises(ProbeTargetRefused):
            assert_compiled_target(tmp_path / name)
    with pytest.raises(ProbeTargetRefused):
        assert_compiled_target(REPO_ROOT / "Build" / "worlds" / "gallic" / "compiled" / "prompt.txt")


def test_guard_refuses_other_shapes_and_accepts_only_the_package_prompt():
    with pytest.raises(ProbeTargetRefused):
        assert_compiled_target(REPO_ROOT / "packages" / "gallic" / "compiled" / "prompt.txt")
    with pytest.raises(ProbeTargetRefused):
        assert_compiled_target(REPO_ROOT / "packages" / "gallic" / "2026-01-01T00-00-00Z" / "compiled" / "capsule.md")
    ok = REPO_ROOT / "packages" / "gallic" / "2026-01-01T00-00-00Z" / "compiled" / "prompt.txt"
    assert assert_compiled_target(ok) == ok.resolve()


def test_guard_accepts_the_default_local_package_cache_layout():
    fetched = REPO_ROOT / "packages" / "packages" / "gallic" / "2026-01-01T00-00-00Z" / "compiled" / "prompt.txt"
    assert assert_compiled_target(fetched) == fetched.resolve()


def test_guard_still_refuses_what_is_not_a_package_prompt_even_under_a_packages_directory():
    stray = REPO_ROOT / "packages" / "gallic" / "compiled" / "prompt.txt"
    with pytest.raises(ProbeTargetRefused):
        assert_compiled_target(stray)
    with pytest.raises(ProbeTargetRefused):
        assert_compiled_target(REPO_ROOT / "Build" / "packages" / "gallic" / "2026-01-01T00-00-00Z" / "compiled" / "prompt.txt")
    with pytest.raises(ProbeTargetRefused):
        assert_compiled_target(REPO_ROOT / "Archive" / "packages" / "gallic" / "2026-01-01T00-00-00Z" / "compiled" / "prompt.txt")
    with pytest.raises(ProbeTargetRefused):
        assert_compiled_target(REPO_ROOT / "packages" / "gallic" / "2026-01-01T00-00-00Z" / "compiled" / "Permanent_Prompt.txt")


def test_guard_refuses_a_symlink_from_a_package_path_to_a_legacy_file(tmp_path):
    legacy = tmp_path / "x_Representative_Permanent_Prompt_Y.txt"
    legacy.write_text("legacy")
    link = tmp_path / "packages" / "zz" / "p1" / "compiled" / "prompt.txt"
    link.parent.mkdir(parents=True)
    link.symlink_to(legacy)
    with pytest.raises(ProbeTargetRefused):
        assert_compiled_target(link)


def test_guard_refuses_a_relative_path_that_climbs_out_of_packages(tmp_path):
    with pytest.raises(ProbeTargetRefused):
        assert_compiled_target(REPO_ROOT / "packages" / ".." / "Build" / "worlds" / "gallic" / "compiled" / "prompt.txt")


def test_guard_refuses_an_arbitrary_out_of_repo_path_named_compiled_prompt(tmp_path):
    target = tmp_path / "pin" / "compiled" / "prompt.txt"
    with pytest.raises(ProbeTargetRefused):
        assert_compiled_target(target)
    stray = tmp_path / "anything" / "packages" / "zz" / "compiled" / "prompt.txt"
    with pytest.raises(ProbeTargetRefused):
        assert_compiled_target(stray)


def test_guard_accepts_an_out_of_repo_package_only_with_its_manifest_beside_compiled(tmp_path):
    target = tmp_path / "cache" / "packages" / "zz" / "2026-09-26T20-12-08Z" / "compiled" / "prompt.txt"
    target.parent.mkdir(parents=True)
    with pytest.raises(ProbeTargetRefused, match="manifest.json"):
        assert_compiled_target(target)
    (target.parent.parent / "manifest.json").write_text("{}")
    assert assert_compiled_target(target) == target.resolve()


def test_guard_takes_the_repository_root_it_is_asked_about(tmp_path):
    inside = tmp_path / "packages" / "zz" / "2026-09-26T20-12-08Z" / "compiled" / "prompt.txt"
    assert assert_compiled_target(inside, tmp_path) == inside.resolve()
    with pytest.raises(ProbeTargetRefused):
        assert_compiled_target(tmp_path / "Build" / "packages" / "zz" / "2026-09-26T20-12-08Z" / "compiled" / "prompt.txt", tmp_path)


def test_the_loader_every_battery_uses_refuses_a_legacy_directory():
    from engine.m4.world_loader import LazyWorldLoader

    with pytest.raises(ProbeTargetRefused):
        LazyWorldLoader().load("gallic", package_dir=REPO_ROOT / "Build" / "worlds" / "gallic", expected_manifest_hash="sha256:0")


def test_a_complete_prompt_passes():
    living = "We do not adjudicate among the living communions."
    findings, notes = check_prompt_content("w", _prompt(living=living), _records(living=living), {}, "p")
    assert findings == []
    assert any(n.startswith("telos") for n in notes)


def test_confirmed_living_traditions_missing_from_prompt_fails():
    findings, _ = check_prompt_content("w", _prompt(), _records(living="We do not adjudicate among the living communions."), {}, "p")
    assert _ids(findings) == ["k:living-traditions"]


def test_registry_living_flag_without_text_is_a_note_for_a_grandfathered_world():
    findings, notes = check_prompt_content("syr", _prompt(), _records(), {"living_tradition_flag": True}, "p")
    assert findings == []
    assert any(n.startswith("living_traditions") for n in notes)


def test_registry_living_flag_without_text_fails_a_world_that_is_not_grandfathered():
    findings, notes = check_prompt_content("w", _prompt(), _records(), {"living_tradition_flag": True}, "p")
    assert _ids(findings) == ["k:living-traditions"]
    assert not any(n.startswith("living_traditions") for n in notes)


def test_registry_without_the_living_flag_needs_no_living_traditions_text():
    assert check_prompt_content("w", _prompt(), _records(), {"living_tradition_flag": False}, "p")[0] == []


def test_missing_self_reference_hardening_in_the_shape_segment_names_each_absent_rule(monkeypatch):
    monkeypatch.setattr("engine.m10.deployed.shape_text", lambda: "## Pronoun rule\n\nStrict we-voice, always.\n")
    findings, _ = check_prompt_content("w", _prompt(), _records(), {}, "p")
    assert len(findings) == 4 and _ids(findings) == ["k:self-reference"]


def test_stale_quotation_count_fails():
    prompt = _prompt(quotation="Three exist. Martin's answer. The elder. Vincent's line.")
    findings, _ = check_prompt_content("w", prompt, _records(quotes=5), {}, "p")
    assert "k:quote-count" in _ids(findings)


def test_correct_stated_quotation_count_passes():
    prompt = _prompt(quotation="Three exist and all are quoted with marks.")
    findings, _ = check_prompt_content("w", prompt, _records(quotes=3), {}, "p")
    assert findings == []


def test_stated_record_count_anywhere_in_the_prompt_must_match():
    prompt = _prompt() + "\nThis store holds 7 quote records.\n"
    findings, _ = check_prompt_content("w", prompt, _records(quotes=3), {}, "p")
    assert "k:quote-count" in _ids(findings)


def test_gravity_index_must_list_exactly_the_records():
    findings, _ = check_prompt_content("w", _prompt(gravities=0), _records(), {}, "p")
    assert _ids(findings) == ["k:gravity-index"]


def _world_root(tmp_path, prompt, records, *, tamper=False):
    code = "w"
    pin = "2026-09-29T00-00-00Z"
    package = tmp_path / "packages" / code / pin
    (package / "compiled").mkdir(parents=True)
    payload = prompt.encode()
    (package / "compiled" / "prompt.txt").write_bytes(payload)
    digest = "sha256:" + hashlib.sha256(b"other" if tamper else payload).hexdigest()
    (package / "manifest.json").write_text(json.dumps({"files": {"compiled/prompt.txt": digest}}))
    (tmp_path / "records" / "worlds").mkdir(parents=True)
    (tmp_path / "records" / "worlds" / f"{code}.yaml").write_text(
        f"state: built\npackage:\n  location: packages/{code}/{pin}\n"
    )
    for rid, rec in records.items():
        directory = tmp_path / "records" / code / rec["record_type"]
        directory.mkdir(parents=True, exist_ok=True)
        body = {k: v for k, v in rec.items()}
        import yaml

        (directory / f"{rid}.md").write_text("---\n" + yaml.safe_dump(body) + "---\nbody\n")
    return tmp_path


def test_check_deployed_reads_the_pinned_prompt_and_passes(tmp_path):
    root = _world_root(tmp_path, _prompt(), _records())
    report = check_deployed("w", root, check_stale=False)
    assert report.findings == []
    assert any("pin 2026-09-29T00-00-00Z" in n for n in report.notes)


def test_check_deployed_flags_a_prompt_that_does_not_match_its_manifest(tmp_path):
    root = _world_root(tmp_path, _prompt(), _records(), tamper=True)
    assert _ids(check_deployed("w", root, check_stale=False).findings) == ["k:prompt-hash"]


def test_check_deployed_flags_a_world_with_no_pin(tmp_path):
    (tmp_path / "records" / "worlds").mkdir(parents=True)
    (tmp_path / "records" / "worlds" / "w.yaml").write_text("state: draft\n")
    assert _ids(check_deployed("w", tmp_path).findings) == ["k:no-pin"]


def test_staleness_is_reported_from_the_m2_sweep(tmp_path, monkeypatch):
    root = _world_root(tmp_path, _prompt(), _records())
    monkeypatch.setattr("engine.m2.checks.staleness_sweep", lambda registry, repo_root: {"w": {"stale": True, "diff": ["compiled/prompt.txt"]}})
    assert _ids(check_deployed("w", root).findings) == ["k:stale"]


def test_failure_messages_say_where_to_author_the_fix(monkeypatch):
    records = _records()
    craft_id = next(r["id"] for r in records.values() if r["record_type"] == "voice_craft")
    records[craft_id]["_path"] = "records/w/voice_craft/w.voice_craft.craft.md"
    monkeypatch.setattr("engine.m10.deployed.shape_text", lambda: "No invented memory.")
    findings, _ = check_prompt_content("w", _prompt(), records, {}, "pin")
    reason = next(f.reason for f in findings if f.check == "k:self-reference")
    assert "engine shape segment" in reason and "fleet_voice record's pronoun_rule" in reason
    monkeypatch.undo()
    findings, _ = check_prompt_content("w", "## Gravities\n", _records(anchor=None, quotes=0), {}, "pin")
    by_check = {f.check: f.reason for f in findings}
    assert "source_anchor and source_anchor_entries fields" in by_check["k:source-anchor"]
    thin = _records(entries=tuple(ENTRIES[:2]))
    findings, _ = check_prompt_content("w", _prompt(), thin, {}, "pin")
    assert "edit source_anchor_entries in the voice_craft record" in findings[0].reason
    no_section = _prompt(anchor=None)
    findings, _ = check_prompt_content("w", no_section, records, {}, "pin")
    assert repin_command("w") in next(f.reason for f in findings if f.check == "k:source-anchor")


def test_the_stale_message_carries_the_exact_repin_command(tmp_path, monkeypatch):
    root = _world_root(tmp_path, _prompt(), _records())
    monkeypatch.setattr("engine.m2.checks.staleness_sweep", lambda registry, repo_root: {"w": {"stale": True, "diff": ["compiled/prompt.txt"]}})
    reason = check_deployed("w", root).findings[0].reason
    assert "python -m engine.m2.cli build w" in reason and "records/worlds/w.yaml" in reason and "package: block" in reason


def _citation_root(tmp_path):
    for rtype, slug in (("quote", "alpha"), ("gravity", "beta"), ("term", "gamma")):
        directory = tmp_path / "records" / "w" / rtype
        directory.mkdir(parents=True, exist_ok=True)
        (directory / f"w.{rtype}.{slug}.md").write_text(f"---\nid: w.{rtype}.{slug}\nrecord_type: {rtype}\n---\n")
    (tmp_path / "cic" / "texts").mkdir(parents=True)
    (tmp_path / "cic" / "texts" / "real.txt").write_text("x")
    return tmp_path


def test_citations_resolve_and_report_fabricated_wrong_namespace_and_wrong_type(tmp_path):
    root = _citation_root(tmp_path)
    doc = root / "doc.md"
    doc.write_text(
        "Good: [[w.quote.alpha]] and the gravity w.gravity.beta.\n"
        "Fabricated: w.quote.invented.\n"
        "Wrong namespace: w.term.alpha.\n"
        "Wrong type: see the quote w.gravity.beta here.\n"
        "Edition cic/texts/real.txt and cic/texts/missing.txt.\n"
    )
    report = check_citations("w", [doc], root)
    by_check = {f.check: f.reason for f in report.findings}
    assert set(by_check) == {"d:unknown-id", "d:wrong-namespace", "d:wrong-type", "d:unknown-text"}
    assert "w.quote.invented" in by_check["d:unknown-id"]
    assert "w.quote.alpha" in by_check["d:wrong-namespace"]
    assert "cic/texts/missing.txt" in by_check["d:unknown-text"]


def test_citations_missing_document_is_a_finding(tmp_path):
    root = _citation_root(tmp_path)
    assert _ids(check_citations("w", [root / "absent.md"], root).findings) == ["d:file-missing"]


def test_citation_with_md_suffix_and_trailing_punctuation_resolves(tmp_path):
    root = _citation_root(tmp_path)
    doc = root / "doc.md"
    doc.write_text("See w.quote.alpha. Also `w.term.gamma.md`, and (w.gravity.beta).\n")
    assert check_citations("w", [doc], root).findings == []


def _probe_root(tmp_path, body, pins=("2026-09-29T00-00-00Z",)):
    (tmp_path / "records" / "worlds").mkdir(parents=True)
    (tmp_path / "records" / "worlds" / "w.yaml").write_text("package:\n  location: packages/w/2026-09-29T00-00-00Z\n")
    for pin in pins:
        (tmp_path / "packages" / "w" / pin).mkdir(parents=True)
    world = tmp_path / "Build" / "worlds" / "w"
    world.mkdir(parents=True)
    (world / "w_Phase5_Validation.md").write_text(body)
    (world / "w_Representative_Permanent_Prompt_X.txt").write_text("legacy")
    return tmp_path


def test_probe_results_must_name_the_pin_they_tested(tmp_path):
    root = _probe_root(tmp_path, "Results with no pin.\n")
    assert _ids(check_probe_pins("w", root).findings) == ["l:pin-missing"]


def test_probe_results_naming_an_existing_pin_pass(tmp_path):
    root = _probe_root(tmp_path, "Tested packages/w/2026-09-29T00-00-00Z/compiled/prompt.txt\n")
    assert check_probe_pins("w", root).findings == []


def test_probe_results_naming_an_unknown_pin_fail(tmp_path):
    root = _probe_root(tmp_path, "Tested pin 2026-01-01T00-00-00Z\n")
    assert _ids(check_probe_pins("w", root).findings) == ["l:pin-unknown"]


def test_an_older_pin_fails(tmp_path):
    root = _probe_root(tmp_path, "Tested pin 2026-09-01T00-00-00Z\n", pins=("2026-09-29T00-00-00Z", "2026-09-01T00-00-00Z"))
    report = check_probe_pins("w", root)
    assert _ids(report.findings) == ["l:pin-not-current"]
    assert "2026-09-29T00-00-00Z" in report.findings[0].reason


def test_a_tested_artifact_line_must_name_only_the_current_pin(tmp_path):
    pins = ("2026-09-29T00-00-00Z", "2026-09-01T00-00-00Z")
    root = _probe_root(tmp_path, "Tested artifact: packages/w/2026-09-29T00-00-00Z/compiled/prompt.txt\nEarlier run on 2026-09-01T00-00-00Z.\n", pins=pins)
    assert check_probe_pins("w", root).findings == []
    root = _probe_root(tmp_path / "b", "Tested artifact: packages/w/2026-09-01T00-00-00Z/compiled/prompt.txt\n", pins=pins)
    assert _ids(check_probe_pins("w", root).findings) == ["l:pin-not-current"]


def test_probes_run_the_guard_on_every_tested_artifact_path_without_the_dry_run_flag(tmp_path):
    good = "Tested artifact: packages/w/2026-09-29T00-00-00Z/compiled/prompt.txt\n"
    assert check_probe_pins("w", _probe_root(tmp_path, good)).findings == []
    legacy = "Tested artifact: Build/worlds/w/w_Representative_Permanent_Prompt_X.txt 2026-09-29T00-00-00Z\n"
    report = check_probe_pins("w", _probe_root(tmp_path / "b", legacy))
    assert "l:guard-refuses" in _ids(report.findings) and "legacy prompt" in report.findings[0].reason
    other = "Tested artifact: Build/packages/w/2026-09-29T00-00-00Z/compiled/prompt.txt\n"
    assert "l:guard-refuses" in _ids(check_probe_pins("w", _probe_root(tmp_path / "c", other)).findings)


def test_the_probes_command_reports_a_refused_artifact_without_runner_dry_run(tmp_path, capsys):
    root = _probe_root(tmp_path, "Tested artifact: Build/worlds/w/w_Representative_Permanent_Prompt_X.txt 2026-09-29T00-00-00Z\n")
    assert _run_command("probes", "w", "--root", str(root)) == 1
    assert "l:guard-refuses" in capsys.readouterr().out


def test_deployed_citations_and_probes_take_root(tmp_path, capsys):
    root = _world_root(tmp_path, _prompt(), _records())
    assert _run_command("deployed", "w", "--no-stale", "--root", str(root)) == 0
    assert _run_command("citations", "w", "--root", str(root)) == 1
    assert "d:no-documents" in capsys.readouterr().out
    assert _run_command("probes", "w", "--root", str(root)) == 0


def test_runner_dry_run_offers_legacy_files_to_the_guard(tmp_path):
    root = _probe_root(tmp_path, "x\n")
    report = runner_dry_run("w", root)
    assert report.findings == []
    assert "1 legacy file(s)" in report.notes[0]


def test_probe_result_discovery_skips_reviews_and_templates(tmp_path):
    root = _probe_root(tmp_path, "x\n")
    world = root / "Build" / "worlds" / "w"
    (world / "w_Phase5_Review_Round1.md").write_text("x")
    (world / "Probe_Result_Record_Template.md").write_text("x")
    assert [p.name for p in deployed.probe_result_files("w", root)] == ["w_Phase5_Validation.md"]


def test_citations_with_no_files_checks_the_worlds_build_documents_and_result_files(tmp_path):
    root = _probe_root(tmp_path, "Tested pin 2026-09-29T00-00-00Z\n")
    world = root / "Build" / "worlds" / "w"
    (world / "Doc_01_Identity.md").write_text("x")
    (world / "Doc_01_Review_Round1.md").write_text("x")
    names = [p.name for p in deployed.citation_files("w", root)]
    assert names == ["Doc_01_Identity.md", "w_Phase5_Validation.md"]


def test_the_citations_command_runs_with_only_a_world_code(capsys):
    import argparse

    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    deployed.add_parser(sub)
    args = parser.parse_args(["citations", "no-such-world"])
    assert args.files == []
    assert deployed.run(args) == 1
    assert "d:no-documents" in capsys.readouterr().out


def test_the_probes_command_also_runs_the_result_label_check(tmp_path, capsys):
    root = _probe_root(tmp_path, "Tested pin 2026-09-29T00-00-00Z\n\n| Probe ID | Result | Basis | Transcript |\n|---|---|---|---|\n| SA-1 | PASS | authored | - |\n")
    assert _run_command("probes", "w", "--root", str(root)) == 1
    assert "m:authored-scored" in capsys.readouterr().out


def _run_command(*argv):
    import argparse

    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    deployed.add_parser(sub)
    return deployed.run(parser.parse_args(list(argv)))


def test_the_loader_gets_past_the_guard_for_a_package_fetched_into_the_default_cache(tmp_path, monkeypatch):
    from engine.m2.loader_stub import PackageRefused
    from engine.m4.world_loader import LazyWorldLoader

    monkeypatch.setattr(deployed, "REPO_ROOT", tmp_path)
    package = tmp_path / "packages" / "packages" / "zz" / "2026-09-26T20-12-08Z"
    (package / "compiled").mkdir(parents=True)
    with pytest.raises(PackageRefused) as raised:
        LazyWorldLoader().load("zz", package_dir=package, expected_manifest_hash="sha256:0")
    assert not isinstance(raised.value, ProbeTargetRefused) and "no manifest.json" in str(raised.value)
    stray = tmp_path / "Build" / "packages" / "zz" / "2026-09-26T20-12-08Z"
    (stray / "compiled").mkdir(parents=True)
    with pytest.raises(ProbeTargetRefused):
        LazyWorldLoader().load("zz", package_dir=stray, expected_manifest_hash="sha256:0")


def test_a_world_with_the_anchoring_paragraph_in_records_and_prompt_passes():
    assert check_prompt_content("w", _prompt(), _records(), {}, "p")[0] == []


def test_a_world_that_is_not_grandfathered_fails_without_the_anchoring_paragraph():
    findings, _ = check_prompt_content("w", _prompt(anchor=None), _records(anchor=None), {}, "p")
    assert _ids(findings) == ["k:source-anchor"]


def test_a_grandfathered_world_without_the_anchoring_paragraph_gets_a_note():
    findings, notes = check_prompt_content("syr", _prompt(anchor=None), _records(anchor=None), {}, "p")
    assert findings == [] and any(n.startswith("source_anchor") for n in notes)


def test_the_anchoring_paragraph_in_records_but_missing_from_the_prompt_fails():
    findings, _ = check_prompt_content("w", _prompt(anchor=None), _records(), {}, "p")
    assert _ids(findings) == ["k:source-anchor"]


def test_the_anchoring_paragraph_must_be_its_own_section_verbatim():
    changed = ANCHOR.replace("plain shape", "plain form")
    findings, _ = check_prompt_content("w", _prompt(anchor=changed), _records(), {}, "p")
    assert _ids(findings) == ["k:source-anchor"]


def test_the_anchoring_paragraph_needs_five_to_ten_entries():
    for entries in (ENTRIES[:4], ENTRIES + ["the Cave of Treasures", "the Doctrine of Addai", "the Chronicle of Edessa", "the Hymns", "the Letters"]):
        anchor = "Our images come from " + ", ".join(entries) + ". We fall back to the plain shape of our own life."
        findings, _ = check_prompt_content("w", _prompt(anchor=anchor), _records(anchor=anchor, entries=entries), {}, "p")
        assert _ids(findings) == ["k:source-anchor-entries"], entries
    edge = ENTRIES[:5]
    anchor = "Our images come from " + ", ".join(edge) + ". We fall back to the plain shape of our own life."
    assert check_prompt_content("w", _prompt(anchor=anchor), _records(anchor=anchor, entries=edge), {}, "p")[0] == []


def test_every_anchor_entry_must_be_named_in_the_paragraph():
    findings, _ = check_prompt_content("w", _prompt(), _records(entries=tuple(ENTRIES[:5]) + ("the Cave of Treasures",)), {}, "p")
    assert _ids(findings) == ["k:source-anchor-entries"]

def test_a_fixture_world_is_exempt_from_the_source_anchor_check():
    prompt = _prompt(self_reference="Strict we-voice, always.", anchor=None)
    findings, notes = check_prompt_content("w", prompt, _records(anchor=None), {"kind": "fixture"}, "p")
    assert findings == []
    assert any(n.startswith("source_anchor:") and "fixture" in n for n in notes)


def test_the_same_prompt_fails_a_world_that_is_not_a_fixture():
    prompt = _prompt(self_reference="Strict we-voice, always.", anchor=None)
    findings, _ = check_prompt_content("w", prompt, _records(anchor=None), {}, "p")
    assert set(_ids(findings)) == {"k:source-anchor"}


def test_a_fixture_world_still_gets_every_other_check():
    prompt = _prompt(quotation="Three exist. Martin's answer. The elder. Vincent's line.", self_reference="Strict we-voice, always.", anchor=None)
    findings, _ = check_prompt_content("w", prompt, _records(quotes=5, anchor=None), {"kind": "fixture"}, "p")
    assert _ids(findings) == ["k:quote-count"]
