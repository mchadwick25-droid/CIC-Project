"""Hermetic (no live model call) tests for engine.m4.term_glosses. Real
compiled repository content throughout, same discipline as
test_name_bridge.py and test_citation_cards.py.
"""
import json

from engine.m2.compiler import compile_and_hash
from engine.m4.citation_cards import resolve_citation_sources
from engine.m4.term_glosses import find_glosses_used


def _real_repository(world_key: str) -> dict[str, dict]:
    package, _digest = compile_and_hash(
        world_key=world_key, package_id="TEST", records_commit="TEST", compiler_version="TEST"
    )
    return {r["id"]: r for r in json.loads(package["compiled/repository.json"])["records"]}


def test_glosses_a_real_term_cited_in_its_own_sentence():
    repo = _real_repository("alx")
    citations = resolve_citation_sources(
        [{"sentence": "We read Scripture through allegoria, the spirit beneath the letter.", "record_ids": ["alx.term.allegoria"]}],
        repo,
    )
    glosses = find_glosses_used(citations, repo)
    assert [g["id"] for g in glosses] == ["alx.term.allegoria"]
    assert glosses[0]["matched_name"] == "allegoria"
    assert glosses[0]["plain_meaning"].startswith("Reading Scripture")
    assert glosses[0]["translational_sense"]
    assert glosses[0]["false_friend"]
    source_ids = {s["source_id"] for s in glosses[0]["sourced_by"]}
    assert "alx.source.origen-philocalia" in source_ids


def test_no_gloss_when_the_term_is_cited_but_not_actually_said():
    """Citation-anchored, not fleet-wide word matching: the record is
    grounding this sentence, but the sentence never SAYS the term itself,
    so nothing fires - the whole discipline the module docstring names."""
    repo = _real_repository("alx")
    citations = resolve_citation_sources(
        [{"sentence": "Scripture holds more than its surface tells.", "record_ids": ["alx.term.allegoria"]}], repo
    )
    assert find_glosses_used(citations, repo) == []


def test_non_term_citations_never_gloss():
    repo = _real_repository("alx")
    citations = resolve_citation_sources(
        [{"sentence": "Origen taught this from his own chair.", "record_ids": ["alx.figure.origen"]}], repo
    )
    assert find_glosses_used(citations, repo) == []


def test_already_bridged_ids_suppresses_a_repeat():
    repo = _real_repository("alx")
    citations = resolve_citation_sources(
        [{"sentence": "We read through allegoria.", "record_ids": ["alx.term.allegoria"]}], repo
    )
    assert find_glosses_used(citations, repo, already_bridged_ids={"alx.term.allegoria"}) == []


def test_fires_once_even_if_cited_in_two_sentences():
    repo = _real_repository("alx")
    citations = resolve_citation_sources(
        [
            {"sentence": "We read through allegoria first.", "record_ids": ["alx.term.allegoria"]},
            {"sentence": "And allegoria again, later.", "record_ids": ["alx.term.allegoria"]},
        ],
        repo,
    )
    glosses = find_glosses_used(citations, repo)
    assert len(glosses) == 1


def test_every_world_has_at_least_one_term_a_real_sentence_can_gloss():
    """Not a detection test - a schema-shape/reachability guard, same
    spirit as test_name_bridge's own. Every term record's world_word must
    at least self-match so a plausible sentence using it glosses."""
    for world_key in ("alx", "desert", "hal", "ijc", "pahc", "syr"):
        repo = _real_repository(world_key)
        terms = [r for r in repo.values() if r.get("record_type") == "term" and r.get("world_word")]
        assert terms, f"{world_key} has no term records with a world_word"
        term = terms[0]
        head = term["world_word"].split(" (", 1)[0].strip()
        citations = resolve_citation_sources([{"sentence": f"We spoke of {head} often.", "record_ids": [term["id"]]}], repo)
        glosses = find_glosses_used(citations, repo)
        assert [g["id"] for g in glosses] == [term["id"]]
