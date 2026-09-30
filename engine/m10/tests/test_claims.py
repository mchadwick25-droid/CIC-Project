"""Hermetic tests for engine.m10.claims: fixtures live under tmp_path."""
import pytest

from engine.m10 import cli
from engine.m10.claims import (
    bootstrap_rows,
    check_claims,
    claim_id,
    derive_claims,
    markdown_units,
    matching_patterns,
    normalise,
)

CODE = "w"
CLAIM = "No source in this world's own corpus records what became of the daughter."
OTHER = "Only one letter survives from the bishop's own hand."
HEADER = "| id | status | confidence | source | check | file | claim |\n|---|---|---|---|---|---|---|\n"


def _write(root, rel, text):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def _row(text, *, status="UNVERIFIED", confidence="-", source="-", check="-", file="Doc_01_Identity.md"):
    return f"| `{claim_id(text)}` | {status} | {confidence} | {source} | {check} | {file} | {normalise(text)} |\n"


def _world(tmp_path, *sentences, rows=None):
    _write(tmp_path, f"Build/worlds/{CODE}/Doc_01_Identity.md", "# Doc 1\n\n" + " ".join(sentences) + "\n")
    if rows is not None:
        _write(tmp_path, f"Build/worlds/{CODE}/{CODE}_Claims_Register.md", "# Register\n\n" + HEADER + "".join(rows))
    return tmp_path


def _checks(report):
    return sorted({f.check for f in report.findings})


def test_a_registered_claim_passes_and_unverified_is_reported_not_failed(tmp_path):
    root = _world(tmp_path, CLAIM, "The city stood on a river.", rows=[_row(CLAIM)])
    report = check_claims(CODE, root)
    assert report.findings == [] and "1 claim(s) derived, 1 registered, 1 registered but UNVERIFIED" in report.notes[0]


def test_a_claim_with_no_register_entry_halts(tmp_path):
    root = _world(tmp_path, CLAIM, OTHER, rows=[_row(CLAIM)])
    report = check_claims(CODE, root)
    assert _checks(report) == ["c:unregistered"] and OTHER[:30] in report.findings[0].reason


def test_a_world_with_claims_and_no_register_file_fails(tmp_path):
    root = _world(tmp_path, CLAIM)
    assert _checks(check_claims(CODE, root)) == ["c:no-register"]


def test_a_world_with_no_claims_and_no_register_passes(tmp_path):
    root = _world(tmp_path, "The city stood on a river.")
    report = check_claims(CODE, root)
    assert report.findings == [] and report.ok


def test_a_reworded_claim_is_new_and_leaves_a_stale_entry(tmp_path):
    root = _world(tmp_path, CLAIM.replace("No source", "No text"), rows=[_row(CLAIM)])
    assert _checks(check_claims(CODE, root)) == ["c:stale", "c:unregistered"]


def test_a_register_entry_whose_claim_was_removed_is_stale(tmp_path):
    root = _world(tmp_path, "The city stood on a river.", rows=[_row(CLAIM)])
    assert _checks(check_claims(CODE, root)) == ["c:stale"]


def test_a_verified_entry_resolves_when_its_evidence_exists(tmp_path):
    _write(tmp_path, "cic/texts/vol01_letters.txt", "text")
    row = _row(CLAIM, status="VERIFIED", confidence="Documented", source="cic/texts/vol01_letters.txt", check="read the whole file")
    assert check_claims(CODE, _world(tmp_path, CLAIM, rows=[row])).findings == []


def test_a_cited_path_that_no_longer_exists_is_unresolved_evidence(tmp_path):
    row = _row(CLAIM, status="VERIFIED", confidence="Documented", source="cic/texts/gone.txt", check="read it")
    report = check_claims(CODE, _world(tmp_path, CLAIM, rows=[row]))
    assert _checks(report) == ["c:evidence-unresolved"] and "cic/texts/gone.txt" in report.findings[0].reason


def test_a_cited_record_that_does_not_exist_is_unresolved_evidence(tmp_path):
    row = _row(CLAIM, status="VERIFIED", confidence="Documented", source="w.source.letter", check="read it")
    assert _checks(check_claims(CODE, _world(tmp_path, CLAIM, rows=[row]))) == ["c:evidence-unresolved"]
    _write(tmp_path, "records/w/source/w.source.letter.md", "---\nid: w.source.letter\nrecord_type: source\n---\nbody\n")
    assert check_claims(CODE, tmp_path).findings == []


def test_a_full_record_path_as_evidence_resolves_to_its_record_id(tmp_path):
    record = "records/w/source/w.source.letter.md"
    row = _row(CLAIM, status="VERIFIED", confidence="Documented", source=record, check="read it")
    root = _world(tmp_path, CLAIM, rows=[row])
    _write(root, record, "---\nid: w.source.letter\nrecord_type: source\n---\nbody\n")
    assert check_claims(CODE, root).findings == []


def test_a_full_record_path_to_a_file_that_does_not_exist_is_still_rejected(tmp_path):
    row = _row(CLAIM, status="VERIFIED", confidence="Documented", source="records/w/source/w.source.gone.md", check="read it")
    report = check_claims(CODE, _world(tmp_path, CLAIM, rows=[row]))
    assert _checks(report) == ["c:evidence-unresolved"]
    assert any("w.source.gone is not a record" in f.reason for f in report.findings)


def test_a_row_naming_a_file_that_is_not_a_deliverable_fails(tmp_path):
    root = _world(tmp_path, CLAIM, rows=[_row(CLAIM, file="Doc_09_Gone.md")])
    assert _checks(check_claims(CODE, root)) == ["c:file-unresolved"]


@pytest.mark.parametrize(
    "row, expected",
    [
        (_row(CLAIM, status="SETTLED"), "c:status"),
        (_row(CLAIM, status="VERIFIED", confidence="Documented"), "c:check-missing"),
        (_row(CLAIM, status="JUDGEMENT", confidence="Probable", check="a reading"), "c:confidence"),
        (_row(CLAIM, status="UNVERIFIED", confidence="Probable"), "c:confidence"),
    ],
)
def test_malformed_rows_fail(tmp_path, row, expected):
    assert expected in _checks(check_claims(CODE, _world(tmp_path, CLAIM, rows=[row])))


def test_a_judgement_entry_with_a_named_reading_and_a_level_passes(tmp_path):
    row = _row(CLAIM, status="JUDGEMENT", confidence="Inferential-Thin", check="a reading of Doc_02 section 6")
    assert check_claims(CODE, _world(tmp_path, CLAIM, rows=[row])).findings == []


def test_a_duplicate_id_and_a_missing_column_fail(tmp_path):
    assert _checks(check_claims(CODE, _world(tmp_path, CLAIM, rows=[_row(CLAIM), _row(CLAIM)]))) == ["c:duplicate"]
    root = _world(tmp_path / "b", CLAIM)
    _write(root, f"Build/worlds/{CODE}/{CODE}_Claims_Register.md", f"| id | status | claim |\n|---|---|---|\n| `{claim_id(CLAIM)}` | UNVERIFIED | {CLAIM} |\n")
    assert "c:columns" in _checks(check_claims(CODE, root))


def test_claims_are_derived_from_record_bodies_and_prose_fields_but_not_guards(tmp_path):
    _write(tmp_path, f"Build/worlds/{CODE}/Doc_01_Identity.md", "# Doc\n\nThe city stood on a river.\n")
    _write(
        tmp_path,
        "records/w/gravity/w.gravity.a.md",
        f"---\nid: w.gravity.a\nrecord_type: gravity\ndescription: {CLAIM}\nclaim_guards:\n- No source says the daughter lived.\n---\n{OTHER}\n",
    )
    derived = derive_claims(CODE, tmp_path)
    assert {c["text"] for c in derived.values()} == {normalise(CLAIM), normalise(OTHER)}
    assert {c["file"] for c in derived.values()} == {"w.gravity.a.md"}


def test_review_files_the_register_and_fenced_blocks_are_not_deliverables(tmp_path):
    _write(tmp_path, f"Build/worlds/{CODE}/Doc_01_Identity.md", f"# Doc\n\n```yaml\nnote: {CLAIM}\n```\n\nFine.\n")
    _write(tmp_path, f"Build/worlds/{CODE}/Doc_01_Review_Round1.md", CLAIM + "\n")
    _write(tmp_path, f"Build/worlds/{CODE}/{CODE}_Claims_Register.md", CLAIM + "\n")
    assert derive_claims(CODE, tmp_path) == {}


def test_a_table_row_is_one_unit_and_a_sentence_ends_a_unit():
    units = markdown_units("| a | b |\n|---|---|\n| No source says this | x |\n\nOne. Two sentences here.\n")
    assert units == ["a b", "No source says this x", "One.", "Two sentences here."]


@pytest.mark.parametrize(
    "sentence, pattern",
    [
        ("No source in the corpus names her.", "no-source"),
        ("None of the surviving letters mention it.", "none-of"),
        ("Not one witness records the date.", "not-one"),
        ("Nothing in the sources explains the change.", "nothing-in"),
        ("It is the only surviving account of the trial.", "only"),
        ("Only one letter names the town.", "only"),
        ("He is the sole witness to the event.", "sole"),
        ("The bishop never mentions the schism.", "never"),
        ("There is no other text on the matter.", "no-other"),
        ("The rite is nowhere attested in the record.", "nowhere"),
        ("The event is not attested elsewhere.", "not-attested"),
        ("The chronicle is silent on the date.", "silent"),
        ("The custom is exclusively Eastern.", "exclusive"),
        ("The name is absent from the surviving sources.", "absent-from"),
        ("No one wrote it down.", "no-one-writes"),
    ],
)
def test_each_claim_shape_is_matched_by_the_pattern_that_names_it(sentence, pattern):
    assert pattern in matching_patterns(sentence)


@pytest.mark.parametrize("sentence", ["The city stood on a river.", "Sources disagree about the date.", "We hold two letters and a sermon.", "Nobody left early."])
def test_ordinary_sentences_are_not_claims(sentence):
    assert matching_patterns(sentence) == []


def test_the_id_follows_the_normalised_text():
    assert claim_id("**No source** says  this.") == claim_id("no source says this.")
    assert claim_id("No source says this.") != claim_id("No text says this.")


def test_bootstrap_prints_only_the_claims_not_yet_registered(tmp_path):
    root = _world(tmp_path, CLAIM, OTHER, rows=[_row(CLAIM)])
    rows = bootstrap_rows(CODE, root)
    assert len(rows) == 1 and claim_id(OTHER) in rows[0] and "UNVERIFIED" in rows[0]


def test_the_command_exits_one_on_a_finding_and_zero_when_clean(tmp_path, capsys):
    root = _world(tmp_path, CLAIM, OTHER, rows=[_row(CLAIM)])
    assert cli.main(["claims", CODE, "--root", str(root)]) == 1
    assert "c:unregistered" in capsys.readouterr().out
    _write(root, f"Build/worlds/{CODE}/{CODE}_Claims_Register.md", HEADER + _row(CLAIM) + _row(OTHER))
    assert cli.main(["claims", CODE, "--root", str(root)]) == 0
    assert cli.main(["claims", CODE, "--root", str(root), "--bootstrap"]) == 0


def test_a_world_with_no_deliverables_fails(tmp_path):
    assert _checks(check_claims("nowhere", tmp_path)) == ["c:no-deliverables"]
