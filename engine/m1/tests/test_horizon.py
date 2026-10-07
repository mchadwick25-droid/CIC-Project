"""engine.m1.horizon and the three slice-5 gates: status-ready,
cells-required and horizon."""
from engine.m1 import gates
from engine.m1.horizon import post_window_mentions
from engine.m1.loader import voiced_records

REGISTRY = {"w": {"world_id": "test-world", "time_window": {"start": 150, "end": 400}}}


def _rec(rid, rtype, **fields):
    return {rid: {"id": rid, "world_id": "test-world", "record_type": rtype, "status": "ready", **fields}}


def test_a_gazetteer_event_after_the_window_is_named():
    assert post_window_mentions("After the Council of Chalcedon we parted.", 400) == ["the Council of Chalcedon (451)"]
    assert post_window_mentions("At the Council of Nicaea we were present.", 400) == []


def test_an_explicit_later_year_or_century_is_named():
    assert post_window_mentions("In 641 the city fell.", 400) == ["the year 641"]
    assert post_window_mentions("By the fifth century the school had gone.", 400) == ["the fifth century"]
    assert post_window_mentions("The 5th-century copies survive.", 400) == ["the 5th-century"]


def test_years_and_centuries_inside_the_window_and_bare_numbers_are_not():
    text = "In 250 our teachers wrote; the fourth century was ours; 500 people came; 600 years later."
    assert post_window_mentions(text, 400) == []


def test_a_modern_term_after_the_window_is_named():
    import re
    terms = [("the modern term 'Trinity'", 325, re.compile(r"\bTrinity\b"))]
    assert post_window_mentions("We did not speak of the Trinity.", 200, terms) == ["the modern term 'Trinity' (325)"]
    assert post_window_mentions("We did not speak of the Trinity.", 400, terms) == []


def test_analytic_records_are_not_voiced():
    records = {**_rec("w.force.a", "force", voice="analytic"), **_rec("w.force.b", "force")}
    assert list(voiced_records(records)) == ["w.force.b"]


def test_the_status_gate_fails_a_voiced_draft_and_spares_unshipped_and_analytic_records():
    records = {
        **_rec("w.story.a", "story", status="draft"),
        **_rec("w.story.b", "story", status="draft", voice="analytic"),
        **_rec("w.search.c", "search_record", status="draft"),
        **_rec("w.story.d", "story"),
    }
    findings = gates.gate_status_ready(records, {}, REGISTRY)
    assert len(findings) == 1 and findings[0].startswith("w.story.a:")


def test_the_cells_gate_fails_a_routed_type_with_no_cells_and_spares_figures():
    records = {
        **_rec("w.term.a", "term", canon_cells=[]),
        **_rec("w.term.b", "term", canon_cells=["C-I"]),
        **_rec("w.figure.c", "figure", canon_cells=[]),
        **_rec("w.term.d", "term", canon_cells=[], voice="analytic"),
    }
    findings = gates.gate_cells_required(records, {}, REGISTRY)
    assert len(findings) == 1 and findings[0].startswith("w.term.a:")


def test_the_horizon_gate_scans_voice_facing_fields_and_spares_edge_fields_and_analytic_records():
    records = {
        **_rec("w.force.a", "force", description="After the Council of Chalcedon the churches split."),
        **_rec("w.force.b", "force", description="After the Council of Chalcedon the churches split.", voice="analytic"),
        **_rec("w.core.w", "world_core", horizon="Our years end before the Council of Chalcedon."),
        **_rec("w.quote.c", "quote", text="In 641 it fell.", modern_rendering="It fell."),
    }
    findings = gates.gate_horizon(records, {}, REGISTRY)
    assert len(findings) == 1 and findings[0].startswith("w.force.a.description: names the Council of Chalcedon (451)")
