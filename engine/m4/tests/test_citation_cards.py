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


def test_resolves_the_real_fleet_modern_term_carrying_its_own_modern_sense():
    """A modern_term card carries modern_sense and distinguishing_claim as
    real, sourced content, the same way a quote's own modern_rendering
    does. _fleet.modern.trinity is the one real modern_term record in the
    fleet."""
    from engine.m1.loader import load_fleet_records

    fleet = load_fleet_records()
    term_id = "_fleet.modern.trinity"
    assert term_id in fleet, "fixture assumes the fleet's own modern_term record"
    card = resolve_source_card(term_id, fleet)
    assert card["record_type"] == "modern_term"
    assert card["label"] == ", ".join(fleet[term_id]["display_terms"])
    assert card["modern_sense"] == fleet[term_id]["modern_sense"]
    assert card["distinguishing_claim"] == fleet[term_id]["distinguishing_claim"]
    source_ids = {s["source_id"] for s in card["sources"]}
    assert source_ids == {"_fleet.source.theophilus-to-autolycus", "_fleet.source.tertullian-against-praxeas"}


def test_a_modern_term_with_no_display_terms_resolves_to_no_card_not_a_bare_id():
    """_label's own generic fallback to the raw record id exists because a
    raw id is still a real, if unlabeled, reference for every other
    record_type - but a modern_term's own id is internal build vocabulary
    (e.g. "_fleet.modern.trinity") no participant should ever see. No
    display_terms means no card at all, not one carrying the id."""
    repo = {"_fleet.modern.x": {"id": "_fleet.modern.x", "record_type": "modern_term", "modern_sense": "a plain sense"}}
    assert resolve_source_card("_fleet.modern.x", repo) is None


def test_resolves_a_real_term_to_its_real_underlying_source():
    """alx.term.allegoria cites Origen's Philocalia, Clement's
    Stromateis, and Eusebius's Historia Ecclesiastica - real,
    public-domain, vendored primary texts, not placeholders."""
    repo = _real_repository("alx")
    card = resolve_source_card("alx.term.allegoria", repo)
    assert card["record_type"] == "term"
    assert card["label"] == "allegoria (the spiritual sense)"
    source_ids = {s["source_id"] for s in card["sources"]}
    assert source_ids == {
        "alx.source.origen-philocalia",
        "alx.source.clement-stromateis",
        "alx.source.eusebius-historia-ecclesiastica",
    }
    philocalia = next(s for s in card["sources"] if s["source_id"] == "alx.source.origen-philocalia")
    assert philocalia["citation"].startswith("Origen, Philocalia")
    assert philocalia["author"] is None
    assert philocalia["work"] is None
    assert philocalia["locus"] == "I"
    assert philocalia["rights_status"] is None


def test_a_record_with_no_sources_resolves_to_an_empty_list_not_a_guess():
    repo = {"w.figure.unattested": {"id": "w.figure.unattested", "record_type": "figure", "names": []}}
    card = resolve_source_card("w.figure.unattested", repo)
    assert card["sources"] == []


def test_a_sources_entry_with_no_source_id_and_no_locus_is_dropped_not_shipped_blank():
    """The renderer's own primary field is `work ?? source_id` - as long
    as an entry carries a real source_id, that id is the fallback text,
    never blank. The only shape that leaves nothing to print is an entry
    with no source_id at all (missing or blanked, upstream of this
    function, in the citing record's own sources[] list) and no locus of
    its own either - author/work/locus/rights_status all None. Dropped
    here rather than shipped as a blank bullet."""
    repo = {
        "w.term.x": {
            "id": "w.term.x",
            "record_type": "term",
            "term": "x",
            "sources": [{"source_id": None}],
        }
    }
    card = resolve_source_card("w.term.x", repo)
    assert card["sources"] == []


def test_a_sources_entry_with_a_dangling_source_id_still_shows_the_id_and_is_kept():
    """A source_id that doesn't resolve in this repository (retired,
    renamed, or a build-time typo the grounding net's own checks don't
    cover, since they verify the CITING record's id, not the CITED
    source's) still leaves the renderer something real to print - the raw
    id itself, via `work ?? source_id`. That is not an empty bullet, just
    an incompletely-resolved one, so it is kept rather than dropped."""
    repo = {
        "w.term.x": {
            "id": "w.term.x",
            "record_type": "term",
            "term": "x",
            "sources": [{"source_id": "w.source.gone"}],
        }
    }
    card = resolve_source_card("w.term.x", repo)
    assert len(card["sources"]) == 1
    assert card["sources"][0]["source_id"] == "w.source.gone"


def test_a_source_with_a_citation_line_shows_only_that_line_and_its_place_in_the_work():
    repo = {
        "w.term.x": {
            "id": "w.term.x", "record_type": "term", "term": "x",
            "sources": [{"source_id": "w.source.s", "locus": "Hymn I.1 (npnf213_some-volume.xml)"}],
        },
        "w.source.s": {
            "id": "w.source.s", "record_type": "source", "citation": "An Author, A Work, trans. A Translator (1898)",
            "author": "An Author (fl. 350; per the legacy Doc_02)", "work": "A Work - registered for one passage",
            "rights_status": "public-domain (accepted on the transcriber's declaration)",
        },
    }
    [source] = resolve_source_card("w.term.x", repo)["sources"]
    assert source == {
        "source_id": "w.source.s", "citation": "An Author, A Work, trans. A Translator (1898)", "author": None,
        "work": None, "locus": "Hymn I.1", "rights_status": None, "edition": None,
    }


def test_a_sources_entry_with_no_source_id_but_a_real_locus_still_prints_something_and_is_kept():
    """The same missing source_id, but the citing record's own entry
    still names a locus - real, printable content (the frontend shows it
    after the work/source_id span) - so the entry is genuinely a source,
    just an incompletely-resolved one, not an empty bullet."""
    repo = {
        "w.term.x": {
            "id": "w.term.x",
            "record_type": "term",
            "term": "x",
            "sources": [{"source_id": None, "locus": "III.4"}],
        }
    }
    card = resolve_source_card("w.term.x", repo)
    assert len(card["sources"]) == 1
    assert card["sources"][0]["locus"] == "III.4"


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


def test_a_quote_attributed_to_a_bare_figure_id_resolves_to_the_figures_real_name():
    """alx.quote.clement-new-song's own speaker_or_author is the literal
    string "alx.figure.clement" - the corpus's own "sometimes an id,
    sometimes prose" convention for this field. Before this fix every
    such quote's label was that raw id, verbatim, to the participant.
    Since the source-first relabel, the
    resolved figure name is the attribution half, after the work."""
    repo = _real_repository("alx")
    card = resolve_source_card("alx.quote.clement-new-song", repo)
    assert card["label"] == "Protrepticus, I — Clement"


def test_a_quote_with_sources_labels_source_first_speaker_as_attribution():
    """A pilot read found the links pointed to the person, not
    the source. The quote card's headline was the speaker; now it is
    the work and passage, with the speaker after the dash - the same
    correction the figure bridge already carries. The headline takes the
    title half of work/locus (before the scholarly apparatus); the full
    strings still ride untouched in the card's sources[]."""
    repo = _real_repository("pahc")
    card = resolve_source_card("pahc.quote.ignatius-truly-born", repo)
    assert card["label"].startswith("The seven letters, middle recension, Trallians 9")
    assert card["label"].endswith("— Ignatius, bishop of Antioch")
    assert card["sources"][0]["citation"].startswith("Ignatius of Antioch, the seven letters")  # the source line below the headline


def test_a_quote_card_carries_three_labelled_layers_and_the_one_line_meaning():
    """A quote card carries the spoken rendering, the edition's words with their citation, and the
    original-language locus where held, plus the record's one-line meaning for the hover."""
    repo = _real_repository("pahc")
    record = repo["pahc.quote.ignatius-truly-born"]
    card = resolve_source_card("pahc.quote.ignatius-truly-born", repo)
    assert card["spoken_rendering"] == record["modern_rendering"]
    assert card["edition_words"] == record["text"]
    assert card["means"] == record["use_note"]["means"]
    assert card["speaker"] == "Ignatius, bishop of Antioch"
    source = card["sources"][0]
    assert source["citation"] and source["locus"]
    assert "edition" in source
    assert isinstance(card["original"], list)


def test_a_story_card_carries_no_source_wording():
    repo = _real_repository("fix")
    record = repo["fix.story.the-long-road"]
    card = resolve_source_card("fix.story.the-long-road", repo)
    assert "original_wording" not in card
    assert card["label"] == record["tellable_as"]
    assert record["text"] not in json.dumps(card)


def test_a_quote_attributed_to_prose_passes_through_unchanged():
    repo = {"w.quote.x": {"id": "w.quote.x", "record_type": "quote", "speaker_or_author": "The Council of Chalcedon (451), Canon 28"}}
    assert resolve_source_card("w.quote.x", repo)["label"] == "The Council of Chalcedon (451), Canon 28"


def test_a_figure_with_no_in_world_name_falls_back_to_its_scholarly_name_not_a_raw_id():
    """pahc.figure.ministrae is the one figure in the fleet with no
    in-world tag at all ("no in-world name or self-designation
    survives") - a real content gap, not something to fabricate an
    in-world name for. The label should still be the real scholarly
    description, not the bare record id."""
    repo = _real_repository("pahc")
    card = resolve_source_card("pahc.figure.ministrae", repo)
    assert card["label"] != "pahc.figure.ministrae"
    assert "enslaved women" in card["label"]


def test_gravity_and_force_labels_strip_the_build_taxonomy_bracket_not_the_name():
    """alx.gravity.divine-pedagogy's own `name` field is "Divine Pedagogy
    [SUPPORTING - explanatory framework]" - real, useful during the build
    process, never meant for a participant."""
    repo = _real_repository("alx")
    card = resolve_source_card("alx.gravity.divine-pedagogy", repo)
    assert card["label"] == "Divine Pedagogy"


def test_a_leading_build_taxonomy_tag_is_stripped_and_the_names_own_parens_survive():
    """Two rzg gravity records carry the tag first, not last: the name
    reads better that way. Both also carry real, unrelated parentheses
    inside the name itself, which must not be touched."""
    repo = _real_repository("rzg")

    card = resolve_source_card("rzg.gravity.council-led-authority-vs-consistorial-independence", repo)
    assert card["label"] == (
        "Council-Led Civic Authority (Zurich) vs. Consistorial Independence from Civil Control (Geneva)"
    )
    assert "TENSIONAL" not in card["label"]

    card = resolve_source_card("rzg.gravity.zwinglis-remembrance-reading-vs-negotiated-consensus", repo)
    assert card["label"] == (
        "Zwingli's Own 'Remembrance' Reading of the Supper vs. the Negotiated Spiritual-Presence Consensus"
    )
    assert "TENSIONAL" not in card["label"]


def test_a_bracket_that_is_not_build_taxonomy_shaped_is_left_alone():
    """The strip only fires on the fleet's own closed taxonomy vocabulary
    (PRIMARY/SUPPORTING/TENSIONAL, or a force code like 1A/2B/3A). A name
    that happens to open or close with an unrelated bracket - invented
    here, since no real record has this shape - is not a build-taxonomy
    tag and must survive untouched."""
    repo = {
        "fix.gravity.synthetic": {
            "id": "fix.gravity.synthetic",
            "record_type": "gravity",
            "name": "[Cited from a 1611 pamphlet] A Real Name (with real parens) [not a tag]",
        }
    }
    card = resolve_source_card("fix.gravity.synthetic", repo)
    assert card["label"] == "[Cited from a 1611 pamphlet] A Real Name (with real parens) [not a tag]"


def test_contested_claim_doctrinal_witness_and_honest_limit_get_real_labels_not_raw_ids():
    """Before this fix these three record_types had no entry in
    _LABEL_FIELDS at all, so every General Reference of these types, in
    every world, was a bare record id."""
    repo = _real_repository("alx")
    contested = resolve_source_card("alx.contested.allegory-from-within", repo)
    assert contested["label"] and contested["label"] != "alx.contested.allegory-from-within"

    desert_repo = _real_repository("desert")
    dw = resolve_source_card("desert.dw.jesus", desert_repo)
    assert dw["label"] and dw["label"] != "desert.dw.jesus"

    limit = resolve_source_card("alx.limit.f5-women-own-words", repo)
    assert limit["label"] and limit["label"] != "alx.limit.f5-women-own-words"


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
        citable_types = ("term", "story", "quote", "figure", "doctrinal_witness", "gravity", "force", "contested_claim", "honest_limit")
        citable = [r["id"] for r in repo.values() if r.get("record_type") in citable_types]
        assert citable, f"{world_key} has no citable records to test against"
        citations = [{"sentence": "s", "record_ids": citable}]
        resolved = resolve_citation_sources(citations, repo)
        assert len(resolved[0]["sources"]) == len(citable)


def test_a_real_story_card_carries_the_records_one_line_meaning_for_the_hover():
    records = _real_repository("lpc")
    record = records["lpc.story.celerinus-writes-to-lucian"]

    card = resolve_source_card(record["id"], records)

    assert card["means"] == record["use_note"]["means"]
    assert card["means"].startswith("Celerinus asked Lucian")
    assert card["narrative_tier"] == record["narrative_tier"] == 1


def test_a_story_or_quote_card_names_the_vendored_text_span_each_source_cites():
    from engine.m1.loader import load_world_records
    from engine.m4.citation_cards import resolve_source_card
    records = load_world_records("lpc")
    story = resolve_source_card("lpc.story.celerinus-writes-to-lucian", records)
    assert story["sources"][0]["vendored"] == [{"file": "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml", "lines": "30528-30720", "label": None}]
    assert story["heart"] and story["means"] and story["narrative_tier"] == 1 and "telling" not in story
    quote = resolve_source_card("lpc.quote.a-respite-from-their-torments", records)
    files = [ref["file"] for ref in quote["sources"][0]["vendored"]]
    assert files == ["cic/texts/npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml", "cic/texts/augustine_doctrina-christiana-enchiridion-lat_bruder1838.txt"]
    assert [ref["label"] for ref in quote["sources"][0]["vendored"]] == ["English", "Latin"]
    assert quote["original"] == [{"label": "Latin", "file": "cic/texts/augustine_doctrina-christiana-enchiridion-lat_bruder1838.txt", "lines": "12508-12516"}]
    assert quote["edition_words"] and quote["means"]
    term = resolve_source_card("lpc.term.catechesis", records)
    assert all("vendored" not in source for source in term["sources"])


def test_locus_refs_reads_single_lines_ranges_and_refuses_the_rest():
    from engine.prose import locus_refs
    assert locus_refs("Ep. 5; cic/texts/a_b.xml, line 42") == [{"file": "cic/texts/a_b.xml", "lines": "42-42", "label": None}]
    assert locus_refs("English at cic/texts/a_b.xml, lines 10–20; Latin at cic/texts/c.txt, lines 3-4") == [
        {"file": "cic/texts/a_b.xml", "lines": "10-20", "label": "English"}, {"file": "cic/texts/c.txt", "lines": "3-4", "label": "Latin"}]
    assert locus_refs("") == [] and locus_refs(None) == []
    assert locus_refs("cic/texts/../../etc/passwd, lines 1-2") == []


def _quote_repo(license_, locus):
    return {
        "w.quote.x": {"id": "w.quote.x", "record_type": "quote", "speaker_or_author": "A", "text": "The edition words.", "modern_rendering": "Plain words.",
                      "license": license_, "use_note": {"means": "It means this."}, "sources": [{"source_id": "w.source.s", "locus": locus}]},
        "w.source.s": {"id": "w.source.s", "record_type": "source", "citation": "A work, ed. B"},
    }


def test_a_paraphrase_only_quote_never_shows_its_edition_words():
    verbatim = resolve_source_card("w.quote.x", _quote_repo("verbatim", "ch. 1"))
    assert verbatim["edition_words"] == "The edition words."
    assert resolve_source_card("w.quote.x", _quote_repo("paraphrase-only", "ch. 1"))["edition_words"] is None


def test_a_latin_only_quote_marks_its_edition_as_latin_and_repeats_no_original():
    card = resolve_source_card("w.quote.x", _quote_repo("verbatim", "Latin at cic/texts/a.txt, lines 1-2"))
    assert card["edition_language"] == "Latin" and card["original"] == []
    both = resolve_source_card("w.quote.x", _quote_repo("verbatim", "English at cic/texts/e.xml, lines 5-6; Latin at cic/texts/a.txt, lines 1-2"))
    assert both["edition_language"] is None and [r["label"] for r in both["original"]] == ["Latin"]


def test_a_word_before_at_that_is_not_a_language_is_not_a_label():
    from engine.prose import locus_refs
    assert locus_refs("Augustine at cic/texts/a.txt, lines 1-2")[0]["label"] is None
