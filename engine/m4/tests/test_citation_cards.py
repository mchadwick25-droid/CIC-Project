"""Hermetic (no live model call) tests for engine.m4.citation_cards. Real
compiled repository content throughout, same discipline as
test_name_bridge.py: a pass here is evidence against genuine record
content, not an invented shape.
"""
import json

from engine.m2.compiler import compile_and_hash
from engine.m4.citation_cards import resolve_citation_sources, resolve_source_card


def _real_repository(world_key: str) -> dict[str, dict]:
    package, _digest = compile_and_hash(
        world_key=world_key, package_id="TEST", records_commit="TEST", compiler_version="TEST"
    )
    records = json.loads(package["compiled/repository.json"])["records"]
    return {r["id"]: r for r in records}


def test_resolves_a_real_term_to_its_real_underlying_source():
    """alx.term.allegoria cites Origen's Philocalia and Clement's
    Stromateis - real, public-domain, vendored primary texts, not
    placeholders."""
    repo = _real_repository("alx")
    card = resolve_source_card("alx.term.allegoria", repo)
    assert card["record_type"] == "term"
    assert card["label"] == "allegoria (the spiritual sense)"
    source_ids = {s["source_id"] for s in card["sources"]}
    assert source_ids == {"alx.source.origen-philocalia", "alx.source.clement-stromateis"}
    philocalia = next(s for s in card["sources"] if s["source_id"] == "alx.source.origen-philocalia")
    assert philocalia["author"].startswith("Origen")
    assert philocalia["work"]
    assert philocalia["locus"] == "I"
    assert philocalia["rights_status"] == "public-domain"


def test_a_record_with_no_sources_resolves_to_an_empty_list_not_a_guess():
    repo = {"w.figure.unattested": {"id": "w.figure.unattested", "record_type": "figure", "names": []}}
    card = resolve_source_card("w.figure.unattested", repo)
    assert card["sources"] == []


def test_an_id_outside_the_repository_resolves_to_none():
    assert resolve_source_card("does.not.exist", {}) is None


def test_label_falls_back_by_record_type():
    repo = {
        "w.story.x": {"id": "w.story.x", "record_type": "story", "tellable_as": "how it was told"},
        "w.quote.x": {"id": "w.quote.x", "record_type": "quote", "speaker_or_author": "someone"},
        "w.dw.x": {"id": "w.dw.x", "record_type": "doctrinal_witness"},
    }
    assert resolve_source_card("w.story.x", repo)["label"] == "how it was told"
    assert resolve_source_card("w.quote.x", repo)["label"] == "someone"
    assert resolve_source_card("w.dw.x", repo)["label"] == "w.dw.x"  # no dedicated field - id is the honest fallback


def test_resolve_citation_sources_is_additive_and_never_drops_a_citation():
    repo = _real_repository("alx")
    citations = [{"sentence": "Origen taught this.", "record_ids": ["alx.term.allegoria"]}]
    out = resolve_citation_sources(citations, repo)
    assert out[0]["sentence"] == citations[0]["sentence"]
    assert out[0]["record_ids"] == citations[0]["record_ids"]
    assert len(out[0]["sources"]) == 1
    assert out[0]["sources"][0]["record_id"] == "alx.term.allegoria"


def test_resolve_citation_sources_over_every_world_never_crashes():
    """A schema-shape guard, same spirit as test_name_bridge's own: every
    real cited record type this fleet actually uses resolves without a
    KeyError, across all six worlds' real citable records."""
    for world_key in ("alx", "desert", "hal", "ijc", "pahc", "syr"):
        repo = _real_repository(world_key)
        citable = [r["id"] for r in repo.values() if r.get("record_type") in ("term", "story", "quote", "figure", "doctrinal_witness")]
        assert citable, f"{world_key} has no citable records to test against"
        citations = [{"sentence": "s", "record_ids": citable}]
        resolved = resolve_citation_sources(citations, repo)
        assert len(resolved[0]["sources"]) == len(citable)
