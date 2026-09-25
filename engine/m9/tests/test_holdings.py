"""Stage 2d's own tests (Build-Plan.md): the holdings report is a real,
computed read of the fleet, never a hand-maintained table, so what it is
actually worth testing is that it stays report-only and that its
disposition vocabulary stays closed."""
from engine.m9.holdings import DISPOSITIONS, holdings_for, report


def test_gallic_shows_twenty_not_yet_assessed():
    """Build-Plan.md Stage 2d's own Done bar pinned this at 19 - a real,
    checkable number, not an illustrative one - reflecting the fleet's
    own state at that stage's completion; the fleet has since grown.
    gallic's own records name Palladius via his Lausiac History and
    Paradise material, so every vendored-but-unopened Palladius work
    (now including palladius_dialogue-life-chrysostom_moore1921.txt)
    counts here - the mechanism working as designed on corpus growth,
    not a defect."""
    rows = holdings_for("gallic")
    assert sum(1 for r in rows if r["disposition"] == "not yet assessed") == 20


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
    """webbe/anf10 exist precisely so nothing cites them, per
    gen_corpus_table.py's own DISPOSITION map - if one shows drawn_on
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
