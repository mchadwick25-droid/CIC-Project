from engine.m9.confinement import CHECKS, run_all
from engine.m9.shelf import Shelf


def _shelf() -> Shelf:
    rows = {
        "trad-row": {"source_file": "trad.txt", "role": "tradition", "confidence": "assigned", "voice_of": None, "documented_exchange": None},
        "ctx-row": {"source_file": "ctx.txt", "role": "context", "confidence": "assigned", "voice_of": "neighbour", "documented_exchange": "confirmed"},
        "ctx-row-nopair": {"source_file": "ctx2.txt", "role": "context", "confidence": "assigned", "voice_of": "stranger", "documented_exchange": "confirmed"},
        "ctx-row-notconfirmed": {"source_file": "ctx3.txt", "role": "context", "confidence": "assigned", "voice_of": "neighbour", "documented_exchange": "not-confirmed"},
        "ctx-row-novoiceof": {"source_file": "ctx4.txt", "role": "context", "confidence": "assigned", "voice_of": None, "documented_exchange": None},
        "needs-ruling-row": {"source_file": "unsure.txt", "role": "tradition", "confidence": "needs-ruling", "voice_of": None, "documented_exchange": None},
    }
    return Shelf(
        world_key="w",
        census_id="w",
        rows=rows,
        files={row["source_file"]: [rid] for rid, row in rows.items()},
        units={
            "trad.txt": "the exact words of the verbatim quote appear here",
            "ctx.txt": "context text", "ctx2.txt": "context text", "ctx3.txt": "context text", "ctx4.txt": "context text",
            "unsure.txt": "unsure text",
        },
        pairs={frozenset({"w", "neighbour"}): {"relation": "mutual-awareness", "direction": None, "confidence": "assigned"}},
        parties={},
        vendored_files=frozenset({"trad.txt", "ctx.txt", "ctx2.txt", "ctx3.txt", "ctx4.txt", "unsure.txt", "elsewhere-in-library.txt"}),
    )


def _base_records() -> dict:
    def source(rid, **kw):
        base = {"id": rid, "record_type": "source", "register": "etic", "sources": []}
        base.update(kw)
        return base

    return {
        "src.trad": source("src.trad", kind="vendored", edition="cic/texts/trad.txt", shelf_row="trad-row"),
        "src.ctx": source("src.ctx", kind="vendored", edition="cic/texts/ctx.txt", shelf_row="ctx-row"),
        "src.ctx-nopair": source("src.ctx-nopair", kind="vendored", edition="cic/texts/ctx2.txt", shelf_row="ctx-row-nopair"),
        "src.ctx-notconfirmed": source("src.ctx-notconfirmed", kind="vendored", edition="cic/texts/ctx3.txt", shelf_row="ctx-row-notconfirmed"),
        "src.ctx-novoiceof": source("src.ctx-novoiceof", kind="vendored", edition="cic/texts/ctx4.txt", shelf_row="ctx-row-novoiceof"),
        "src.unsure": source("src.unsure", kind="vendored", edition="cic/texts/unsure.txt", shelf_row="needs-ruling-row"),
        "src.unvendored": source("src.unvendored", kind="unvendored", edition="a consult-only book, never vendored"),
        "src.absence": source(
            "src.absence", kind="absence", edition="cic/texts/trad.txt",
            absence_probes=["a phrase never written anywhere in that file"],
        ),
    }


def test_clean_shelf_and_records_produce_no_findings():
    records = _base_records()
    findings = run_all(records, _shelf())
    assert findings == {name: [] for name in CHECKS}


def test_source_kind_missing_kind():
    records = _base_records()
    del records["src.trad"]["kind"]
    findings = run_all(records, _shelf())
    assert any("no kind set" in f for f in findings["source-kind"])


def test_source_kind_vendored_claim_against_nonexistent_file():
    records = _base_records()
    records["src.trad"]["edition"] = "cic/texts/does-not-exist.txt"
    findings = run_all(records, _shelf())
    assert any("does not name a real cic/texts/ file" in f for f in findings["source-kind"])


def test_source_kind_unvendored_but_names_a_file():
    records = _base_records()
    records["src.unvendored"]["edition"] = "cic/texts/elsewhere-in-library.txt"
    findings = run_all(records, _shelf())
    assert any("kind is 'unvendored' but edition names" in f for f in findings["source-kind"])


def test_source_kind_absence_missing_probes():
    records = _base_records()
    records["src.absence"]["absence_probes"] = []
    findings = run_all(records, _shelf())
    assert any("absence_probes is empty" in f for f in findings["source-kind"])


def test_shelf_row_missing():
    records = _base_records()
    del records["src.trad"]["shelf_row"]
    findings = run_all(records, _shelf())
    assert any("shelf_row is not set" in f for f in findings["shelf-row"])


def test_shelf_row_dangling():
    records = _base_records()
    records["src.trad"]["shelf_row"] = "no-such-row"
    findings = run_all(records, _shelf())
    assert any("does not resolve to a row" in f for f in findings["shelf-row"])


def test_shelf_row_points_at_wrong_file():
    records = _base_records()
    records["src.trad"]["shelf_row"] = "ctx-row"  # a real row, wrong file
    findings = run_all(records, _shelf())
    assert any("but edition names" in f for f in findings["shelf-row"])


def test_emic_vendored_only_fires_on_unvendored_citation():
    records = _base_records()
    records["citable"] = {
        "id": "citable", "record_type": "ambient", "register": "emic",
        "sources": [{"source_id": "src.unvendored", "locus": "1"}],
    }
    findings = run_all(records, _shelf())
    assert any("kind is 'unvendored'" in f for f in findings["emic-vendored-only"])


def test_emic_vendored_only_fires_on_absence_citation():
    records = _base_records()
    records["citable"] = {
        "id": "citable", "record_type": "ambient", "register": "emic",
        "sources": [{"source_id": "src.absence", "locus": "1"}],
    }
    findings = run_all(records, _shelf())
    assert any("kind is 'absence'" in f for f in findings["emic-vendored-only"])


def test_emic_vendored_only_silent_on_vendored_citation():
    records = _base_records()
    records["citable"] = {
        "id": "citable", "record_type": "ambient", "register": "emic",
        "sources": [{"source_id": "src.trad", "locus": "1"}],
    }
    findings = run_all(records, _shelf())
    assert findings["emic-vendored-only"] == []


def test_absence_probe_fires_when_probe_actually_present():
    records = _base_records()
    records["src.absence"]["absence_probes"] = ["the exact words of the verbatim quote"]
    findings = run_all(records, _shelf())
    assert any("DOES window-match" in f for f in findings["absence-probe"])


def test_absence_probe_silent_when_probe_genuinely_absent():
    findings = run_all(_base_records(), _shelf())
    assert findings["absence-probe"] == []


def test_verbatim_in_shelf_fires_on_invented_text():
    records = _base_records()
    records["quote"] = {
        "id": "quote", "record_type": "quote", "register": "emic", "license": "verbatim",
        "text": "nothing like this sentence exists in any shelf file",
        "sources": [{"source_id": "src.trad", "locus": "1"}],
    }
    findings = run_all(records, _shelf())
    assert any("does not window-match" in f for f in findings["verbatim-in-shelf"])


def test_verbatim_in_shelf_silent_on_real_quote():
    records = _base_records()
    records["quote"] = {
        "id": "quote", "record_type": "quote", "register": "emic", "license": "verbatim",
        "text": "the exact words of the verbatim quote",
        "sources": [{"source_id": "src.trad", "locus": "1"}],
    }
    findings = run_all(records, _shelf())
    assert findings["verbatim-in-shelf"] == []


def test_verbatim_in_shelf_ignores_do_not_voice_quotes():
    records = _base_records()
    records["quote"] = {
        "id": "quote", "record_type": "quote", "register": "emic", "license": "do-not-voice",
        "text": "nothing like this sentence exists in any shelf file",
        "sources": [{"source_id": "src.trad", "locus": "1"}],
    }
    findings = run_all(records, _shelf())
    assert findings["verbatim-in-shelf"] == []


def test_voicing_pair_tradition_role_always_passes():
    records = _base_records()
    records["citable"] = {"id": "citable", "record_type": "ambient", "register": "emic", "sources": [{"source_id": "src.trad"}]}
    findings = run_all(records, _shelf())
    assert findings["voicing-pair"] == []


def test_voicing_pair_confirmed_exchange_passes():
    records = _base_records()
    records["citable"] = {"id": "citable", "record_type": "ambient", "register": "emic", "sources": [{"source_id": "src.ctx"}]}
    findings = run_all(records, _shelf())
    assert findings["voicing-pair"] == []


def test_voicing_pair_missing_voice_of():
    records = _base_records()
    records["citable"] = {"id": "citable", "record_type": "ambient", "register": "emic", "sources": [{"source_id": "src.ctx-novoiceof"}]}
    findings = run_all(records, _shelf())
    assert any("carries no voice_of" in f for f in findings["voicing-pair"])


def test_voicing_pair_no_pair_ruling():
    records = _base_records()
    records["citable"] = {"id": "citable", "record_type": "ambient", "register": "emic", "sources": [{"source_id": "src.ctx-nopair"}]}
    findings = run_all(records, _shelf())
    assert any("has no PAIRS.yaml ruling" in f for f in findings["voicing-pair"])


def test_voicing_pair_relation_not_mutual_awareness():
    shelf = _shelf()
    shelf.pairs[frozenset({"w", "stranger"})] = {"relation": "one-way", "direction": None, "confidence": "assigned"}
    records = _base_records()
    records["citable"] = {"id": "citable", "record_type": "ambient", "register": "emic", "sources": [{"source_id": "src.ctx-nopair"}]}
    findings = run_all(records, shelf)
    assert any("ruled 'one-way', not mutual-awareness" in f for f in findings["voicing-pair"])


def test_voicing_pair_confidence_needs_ruling():
    shelf = _shelf()
    shelf.pairs[frozenset({"w", "neighbour"})]["confidence"] = "needs-ruling"
    records = _base_records()
    records["citable"] = {"id": "citable", "record_type": "ambient", "register": "emic", "sources": [{"source_id": "src.ctx"}]}
    findings = run_all(records, shelf)
    assert any("still needs-ruling" in f for f in findings["voicing-pair"])


def test_voicing_pair_documented_exchange_not_confirmed():
    records = _base_records()
    records["citable"] = {"id": "citable", "record_type": "ambient", "register": "emic", "sources": [{"source_id": "src.ctx-notconfirmed"}]}
    findings = run_all(records, _shelf())
    assert any("not confirmed" in f for f in findings["voicing-pair"])


def test_voicing_pair_skips_unresolved_source_no_double_report():
    records = _base_records()
    records["citable"] = {"id": "citable", "record_type": "ambient", "register": "emic", "sources": [{"source_id": "src.unvendored"}]}
    findings = run_all(records, _shelf())
    assert findings["voicing-pair"] == []  # emic-vendored-only's finding, not this check's


def test_shelf_confidence_fires_on_needs_ruling_row():
    records = _base_records()
    records["citable"] = {"id": "citable", "record_type": "ambient", "register": "emic", "sources": [{"source_id": "src.unsure"}]}
    findings = run_all(records, _shelf())
    assert any("needs-ruling" in f for f in findings["shelf-confidence"])


def test_shelf_confidence_silent_on_assigned_row():
    records = _base_records()
    records["citable"] = {"id": "citable", "record_type": "ambient", "register": "emic", "sources": [{"source_id": "src.trad"}]}
    findings = run_all(records, _shelf())
    assert findings["shelf-confidence"] == []


def test_etic_records_never_checked_for_voicing_or_vendored_only():
    records = _base_records()
    records["citable"] = {
        "id": "citable", "record_type": "ambient", "register": "etic",
        "sources": [{"source_id": "src.unvendored"}],
    }
    findings = run_all(records, _shelf())
    assert findings["emic-vendored-only"] == []
    assert findings["voicing-pair"] == []
