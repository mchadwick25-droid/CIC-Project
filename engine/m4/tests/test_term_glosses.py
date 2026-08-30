"""Hermetic (no live model call) tests for engine.m4.term_glosses. Real
compiled repository content throughout, same discipline as
test_name_bridge.py and test_citation_cards.py.

The firing rule under test is the 2026-08-30 design (Mark: "the lexicon
... is the heart of the depth"): a text scan of the finished turn against
the world's own term records - the same contract as the name bridge -
replacing the citation-anchored lock that measured zero fires on the
live pilot. See the module docstring for the full history.
"""
import json

from engine.m2.compiler import compile_and_hash
from engine.m4.citation_cards import resolve_citation_sources
from engine.m4.term_glosses import _matchable_forms, find_glosses_used


def _real_repository(world_key: str) -> dict[str, dict]:
    package, _digest = compile_and_hash(
        world_key=world_key, package_id="TEST", records_commit="TEST", compiler_version="TEST"
    )
    return {r["id"]: r for r in json.loads(package["compiled/repository.json"])["records"]}


def test_a_lexicon_word_said_uncited_still_glosses():
    """The pilot's own failure case: the voice says "Logos" grounded in
    the witness record, never citing the lexicon entry - the word must
    light anyway, glossed from the compiled lexicon, with an honest
    empty sourced_by."""
    repo = _real_repository("alx")
    text = "To us, Jesus is the Logos - God's own Word, come in flesh."
    glosses = find_glosses_used(text, [], repo)
    ids = [g["id"] for g in glosses]
    assert "alx.term.logos" in ids
    logos = next(g for g in glosses if g["id"] == "alx.term.logos")
    assert logos["matched_name"] == "Logos"
    assert logos["quick_meaning"]
    assert logos["sourced_by"] == []


def test_sourced_by_attaches_when_the_words_sentence_carries_a_citation():
    repo = _real_repository("alx")
    text = "We read Scripture through allegoria, the spirit beneath the letter."
    citations = resolve_citation_sources(
        [{"sentence": text, "record_ids": ["alx.term.allegoria"]}], repo
    )
    glosses = find_glosses_used(text, citations, repo)
    allegoria = next(g for g in glosses if g["id"] == "alx.term.allegoria")
    assert allegoria["plain_meaning"].startswith("Reading Scripture")
    assert allegoria["translational_sense"]
    assert allegoria["false_friend"]
    source_ids = {s["source_id"] for s in allegoria["sourced_by"]}
    assert "alx.source.origen-philocalia" in source_ids


def test_already_bridged_ids_suppresses_a_repeat():
    repo = _real_repository("alx")
    text = "The Logos was with God from the beginning."
    assert not any(
        g["id"] == "alx.term.logos"
        for g in find_glosses_used(text, [], repo, already_bridged_ids={"alx.term.logos"})
    )


def test_fires_once_per_turn_even_when_said_twice():
    repo = _real_repository("alx")
    text = "The Logos speaks in Scripture, and the Logos speaks now."
    glosses = [g for g in find_glosses_used(text, [], repo) if g["id"] == "alx.term.logos"]
    assert len(glosses) == 1


def test_comma_and_slash_forms_each_match():
    """Fleet-measured compound world_words: "baptism, photismos
    (illumination)" and "geron / abba / amma" - every piece a voice would
    say is a matchable form; the identical-span tie (alx.term.baptism's
    own "photismos" piece against alx.term.photismos itself) resolves to
    the lowest id, deterministically, same as the name bridge."""
    assert _matchable_forms({"world_word": "baptism, photismos (illumination)"}) == ["baptism, photismos", "baptism", "photismos"]
    assert _matchable_forms({"world_word": "geron / abba / amma"}) == ["geron / abba / amma", "geron", "abba", "amma"]

    desert = _real_repository("desert")
    hits = find_glosses_used("An amma gave the word that day.", [], desert)
    assert [g["id"] for g in hits] == ["desert.term.geron-abba-amma"]

    alx = _real_repository("alx")
    tie = find_glosses_used("They called it photismos.", [], alx)
    assert [g["id"] for g in tie] == ["alx.term.baptism"]


def test_reading_order_and_word_boundaries():
    repo = _real_repository("alx")
    text = "Metanoia comes first, then gnosis grows. Catalogos is not a word of ours."
    ids = [g["id"] for g in find_glosses_used(text, [], repo)]
    assert ids[:2] == ["alx.term.metanoia", "alx.term.gnosis"]
    assert "alx.term.logos" not in ids  # "Catalogos" must not match inside a longer word


def test_every_world_has_at_least_one_term_a_real_sentence_can_gloss():
    """Schema-shape/reachability guard, same spirit as test_name_bridge's
    own: every world's first term record must self-match in a plausible
    sentence."""
    for world_key in ("alx", "desert", "hal", "ijc", "pahc", "syr"):
        repo = _real_repository(world_key)
        terms = [r for r in repo.values() if r.get("record_type") == "term" and r.get("world_word")]
        assert terms, f"{world_key} has no term records with a world_word"
        term = sorted(terms, key=lambda r: r["id"])[0]
        head = _matchable_forms(term)[0]
        glosses = find_glosses_used(f"We spoke of {head} often.", [], repo)
        assert term["id"] in [g["id"] for g in glosses], world_key
