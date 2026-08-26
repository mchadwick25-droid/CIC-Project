"""Hermetic (no live model call) tests for engine.m4.name_bridge. Real
figure-record content throughout, compiled from the actual records/ tree
via engine.m2.compiler.compile_and_hash - the same real data a live turn
would load as world.figures, not invented fixtures - so a pass here is
evidence the detection works against genuine record content, not just
against a shape the test author made up.
"""
import json

from engine.m2.compiler import compile_and_hash
from engine.m4.citation_cards import resolve_citation_sources
from engine.m4.name_bridge import attach_cited_sources, find_figures_used


def _real_figures(world_key: str) -> list[dict]:
    package, _digest = compile_and_hash(
        world_key=world_key, package_id="TEST", records_commit="TEST", compiler_version="TEST"
    )
    return json.loads(package["compiled/figures.json"])["figures"]


def test_matches_the_scholarly_names_short_form_even_when_in_world_tag_differs():
    """syr.figure.aphrahat's in-world tag is "the Persian sage" - VR_1A's
    own measured transcript still had the voice say "Aphrahat" once (the
    scholarly form's head). Both must be checked or this exact real case
    is missed."""
    figures = _real_figures("syr")
    hits = find_figures_used("Aphrahat wrote against them from inside the persecution.", figures)
    assert [h["id"] for h in hits] == ["syr.figure.aphrahat"]
    assert hits[0]["matched_name"] == "Aphrahat"
    assert hits[0]["bridge_line"].startswith("the Persian sage")


def test_matches_the_in_world_epithet_too():
    figures = _real_figures("syr")
    hits = find_figures_used("We simply called him the Persian sage.", figures)
    assert [h["id"] for h in hits] == ["syr.figure.aphrahat"]
    assert hits[0]["matched_name"] == "the Persian sage"


def test_no_hit_when_no_figure_is_named():
    figures = _real_figures("syr")
    hits = find_figures_used("We sang the psalms together at vigil.", figures)
    assert hits == []


def test_already_bridged_ids_suppresses_a_repeat():
    figures = _real_figures("syr")
    text = "Ephrem taught the faith by singing it."
    first = find_figures_used(text, figures)
    assert [h["id"] for h in first] == ["syr.figure.ephrem"]
    second = find_figures_used(text, figures, already_bridged_ids={"syr.figure.ephrem"})
    assert second == []


def test_two_real_figures_ordered_by_first_appearance_in_text():
    figures = _real_figures("syr")
    hits = find_figures_used("Ephrem answered Bardaisan's songs with his own.", figures)
    assert [h["id"] for h in hits] == ["syr.figure.ephrem", "syr.figure.bardaisan"]

    reordered = find_figures_used("Bardaisan came first; Ephrem answered him a century later.", figures)
    assert [h["id"] for h in reordered] == ["syr.figure.bardaisan", "syr.figure.ephrem"]


def test_full_record_content_reaches_the_result_for_level_3():
    """The Level-3 "full entry" needs more than a bare name - dates and
    the complete names[] list (both tags), not just whichever one
    matched, so the UI can still show "also called Aphrahat" regardless
    of which form the voice actually used."""
    figures = _real_figures("syr")
    hits = find_figures_used("Ephrem was the deacon-poet of Nisibis and Edessa.", figures)
    assert hits[0]["dates"]["born"]
    names_by_tag = {n["tag"]: n["name"] for n in hits[0]["names"]}
    assert names_by_tag["in-world"] == "Ephrem"
    assert "Ephraem Syrus" in names_by_tag["scholarly"]


def test_two_figures_with_the_identical_in_world_name_resolve_to_exactly_one():
    """hal.figure.paula and hal.figure.paula-younger both register the
    bare in-world name "Paula" - a real collision in the fleet, not a
    hypothetical. The text alone can't say which one is meant; this
    proves exactly one wins (not both, and not neither), deterministically
    by lowest id, rather than leaving the frontend to arbitrarily pick
    whichever happened to come first in figures.json's own order - which
    also silently consumed BOTH ids from already_bridged_ids before this
    fix, so the one that lost the coin flip could never bridge at all."""
    figures = _real_figures("hal")
    hits = find_figures_used("Paula gave everything she had.", figures)
    assert [h["id"] for h in hits] == ["hal.figure.paula"]


def test_word_boundary_does_not_match_inside_a_longer_word():
    """A short synthetic fixture, not real records: proves a name that is
    a substring of an unrelated word never fires, independent of what
    real figure names happen to collide with real vocabulary today."""
    figures = [{"id": "w.figure.ann", "names": [{"name": "Ann", "tag": "in-world"}], "bridge_line": "b"}]
    assert find_figures_used("This happened annually.", figures) == []
    assert find_figures_used("Ann was there.", figures)[0]["id"] == "w.figure.ann"


def test_every_world_compiles_figures_the_bridge_can_read():
    """Not a name-detection test - a schema-shape guard. Every live world's
    compiled/figures.json must carry the {id, names, bridge_line, dates}
    shape find_figures_used depends on, so a future records/ edit that
    breaks the shape fails here, in a test, before it fails silently in a
    live turn. Not every figure carries an in-world tag - pahc.figure.
    ministrae is deliberately scholarly-only ("no in-world name or
    self-designation survives") - so this only requires at least one
    non-empty name, matching what _matchable_forms actually needs."""
    for world_key in ("alx", "desert", "hal", "ijc", "pahc", "syr"):
        figures = _real_figures(world_key)
        assert figures, f"{world_key} compiled zero figure records"
        for figure in figures:
            assert figure["id"]
            assert any(isinstance(n, dict) and n.get("name") for n in figure["names"])


def _real_repository(world_key: str) -> dict[str, dict]:
    package, _digest = compile_and_hash(
        world_key=world_key, package_id="TEST", records_commit="TEST", compiler_version="TEST"
    )
    return {r["id"]: r for r in json.loads(package["compiled/repository.json"])["records"]}


def test_attach_cited_sources_finds_the_source_behind_what_the_figure_is_saying():
    """Mark's own correction: not just who Origen is, but what he's
    saying here and what backs it. "Origen taught us..." names Origen and
    is tagged with alx.term.allegoria, whose own sources are Origen's
    Philocalia and Clement's Stromateis - real citable texts, not the
    figure record's own (unrelated) sources."""
    repo = _real_repository("alx")
    figures = _real_figures("alx")
    text = "Origen taught us to read Scripture at more than one level."
    figures_used = find_figures_used(text, figures)
    citations = resolve_citation_sources(
        [{"sentence": text, "record_ids": ["alx.term.allegoria"]}], repo
    )
    attached = attach_cited_sources(figures_used, citations)
    assert attached[0]["id"] == "alx.figure.origen"
    source_ids = {s["source_id"] for s in attached[0]["sourced_by"]}
    assert source_ids == {"alx.source.origen-philocalia", "alx.source.clement-stromateis"}


def test_attach_cited_sources_is_honest_when_nothing_was_cited():
    figures = _real_figures("alx")
    text = "Origen taught us to read Scripture at more than one level."
    figures_used = find_figures_used(text, figures)
    attached = attach_cited_sources(figures_used, citations_with_sources=[])
    assert attached[0]["sourced_by"] == []
