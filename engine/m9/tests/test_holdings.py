"""Stage 2d's own tests (Build-Plan.md): the holdings report is a real,
computed read of the fleet, never a hand-maintained table, so what it is
actually worth testing is that it stays report-only and that its
disposition vocabulary stays closed."""
import pytest

from engine.m9.holdings import DISPOSITIONS, holdings_for, report


_GALLIC_NINETEEN = {
    "anf04_tertullian4-minucius-felix-commodian-origen1-2.xml",
    "anf05_hippolytus-cyprian-caius-novatian.xml",
    "anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml",
    "anf09_gospel-of-peter-diatessaron-origen-commentaries.xml",
    "npnf102_augustine-city-of-god-christian-doctrine.xml",
    "npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml",
    "npnf104_augustine-anti-manichaean-anti-donatist.xml",
    "npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml",
    "npnf107_augustine-homilies-john-soliloquies.xml",
    "npnf108_augustine-exposition-psalms.xml",
    "npnf201_eusebius-church-history-life-of-constantine.xml",
    "npnf204_athanasius-select-works-letters.xml",
    "npnf206_jerome-principal-works.xml",
    "npnf208_basil-letters-select-works.xml",
    "npnf209_hilary-poitiers-john-damascus.xml",
    "origen_de-oratione-grc_koetschau1899.txt",
    "origen_philocalia_lewis1911.txt",
    "palladius_lausiac-history_clarke1918.txt",
    "palladius_paradise-v1-syriac_budge1907.txt",
}


def test_gallic_shows_nineteen_not_yet_assessed():
    """The literal Done bar in Build-Plan.md Stage 2d: "gallic's 19
    unopened volumes show not-yet-assessed" - the nineteen named above stay
    not-yet-assessed; a volume vendored later and in scope adds to the
    count, never subtracts."""
    rows = holdings_for("gallic")
    unassessed = {r["file"] for r in rows if r["disposition"] == "not yet assessed"}
    assert len(unassessed) >= 19 and _GALLIC_NINETEEN <= unassessed


def test_every_row_carries_a_closed_disposition():
    rows = holdings_for("gallic")
    assert rows
    assert all(r["disposition"] in DISPOSITIONS for r in rows)


def test_drawn_on_implies_in_scope():
    """A file this world's own records actually cite is definitionally in
    scope - drawn_on can never outrun in_scope."""
    rows = holdings_for("gallic")
    assert all(r["in_scope"] for r in rows if r["drawn_on"])


def test_by_design_files_are_never_drawn_on():
    """webbe/anf10 exist precisely so nothing cites them (per
    gen_corpus_table.py's own DISPOSITION map) - if one shows drawn_on
    here, that is a real citation this report should surface, not hide
    behind the "by design" label."""
    rows = holdings_for("gallic")
    by_design = [r for r in rows if r["disposition"] == "by design"]
    assert by_design
    assert all(not r["drawn_on"] for r in by_design)


def test_report_runs_on_every_built_world_without_blocking():
    """Report-only, per this stage's own bar - nothing here may raise or
    block a build for any world the fleet has."""
    from engine.m1.registry import formation_world_keys, load_registry

    registry = load_registry()
    for world in formation_world_keys(registry):
        text = report(world)
        assert f"holdings: {world}" in text


def _registry_root(tmp_path, code, body):
    path = tmp_path / "records" / "worlds" / f"{code}.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    return tmp_path


def test_a_registered_world_with_no_records_directory_reports_an_empty_holding(tmp_path):
    root = _registry_root(tmp_path, "nw", "kind: formation\ntime_window: {start: 9000, end: 9100}\n")
    assert not (root / "records" / "nw").exists()
    rows = holdings_for("nw", root)
    assert rows and all(r["disposition"] in DISPOSITIONS for r in rows)
    assert not any(r["named_in_records"] or r["drawn_on"] for r in rows)


def test_an_unregistered_world_names_the_missing_registry_file(tmp_path):
    from engine.m9.holdings import HoldingsError

    with pytest.raises(HoldingsError, match=r"records/worlds/zzz\.yaml does not exist"):
        holdings_for("zzz", _registry_root(tmp_path, "nw", "time_window: {start: 1, end: 2}\n"))


def test_a_registry_entry_without_a_time_window_names_the_file_and_field(tmp_path):
    from engine.m9.holdings import HoldingsError

    with pytest.raises(HoldingsError, match=r"records/worlds/nw\.yaml has no time_window"):
        holdings_for("nw", _registry_root(tmp_path, "nw", "kind: formation\n"))


def test_the_report_command_ends_with_the_message_not_a_traceback(tmp_path, monkeypatch):
    monkeypatch.setattr("engine.m9.holdings.load_registry", lambda path=None: {})
    with pytest.raises(SystemExit) as raised:
        report("zzz")
    assert "is not a registered world" in str(raised.value)
