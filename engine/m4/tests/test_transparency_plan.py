"""engine.m4.transparency_plan's own tests: per-element mark placement.

Real compiled repository content for the record lookups (same discipline
as test_citation_cards.py). The turns themselves are constructed by hand
- (sentence, tags, verdict) triples joined into the reply text - since
the placement patterns under test need to be pinned down exactly, not
hoped for out of whatever a live turn happens to produce.
"""
import json

from engine.m2.compiler import compile_and_hash
from engine.m4.grounding_net import check_turn_with_paragraph_coverage, strip_tags
from engine.m4.term_glosses import find_glosses_used
from engine.m4.transparency_plan import ElementBuilder, build_transparency_plan


def _real_repository(world_key: str) -> dict[str, dict]:
    package, _digest = compile_and_hash(
        world_key=world_key, package_id="TEST", records_commit="TEST", compiler_version="TEST"
    )
    records = json.loads(package["compiled/repository.json"])["records"]
    return {r["id"]: r for r in records}


REPO = _real_repository("alx")

TERM_ID = "alx.term.allegoria"
STORY_ID = next(rid for rid, r in REPO.items() if r.get("record_type") == "story")
QUOTE_ID = "alx.quote.a-doctrine-they-would-not-have-taught"
WITNESS_ID = next(rid for rid, r in REPO.items() if r.get("record_type") == "doctrinal_witness")
GRAVITY_ID = next(rid for rid, r in REPO.items() if r.get("record_type") == "gravity")
QUOTED_WORDS = "his disciples committed themselves to teaching a doctrine"
# A quotation the voice actually speaks is checked against modern_rendering,
# never text (item 3, the modern_rendering-required gate: text is never
# voiced). This phrase is drawn from the record's own modern_rendering
# rather than its archaic text for exactly that reason.
assert QUOTED_WORDS in REPO[QUOTE_ID]["modern_rendering"]


def _turn(rows: list[tuple[str, list[str], str]], *, separator: str = " ") -> tuple[str, list[dict], dict]:
    """rows: (sentence, tags, verdict). Returns (text, citations,
    net_result) in apply_net's own shapes."""
    text = separator.join(sentence for sentence, _tags, _verdict in rows)
    net_result = {"sentences": [{"sentence": s, "tags": tags, "verdict": v} for s, tags, v in rows]}
    citations = [{"sentence": s, "record_ids": tags} for s, tags, v in rows if v == "ok" and tags]
    return text, citations, net_result


def _plan(rows, **kwargs):
    text, citations, net_result = _turn(rows)
    return text, build_transparency_plan(
        citations=citations, net_result=net_result, repository_records=REPO, world_key="alx", text=text, **kwargs,
    )


def _of(plan, record_id):
    return [e for e in plan["elements"] if e["record_id"] == record_id]


# ---- offsets and index space --------------------------------------------


def test_every_sentence_span_and_every_element_surface_is_exact():
    rows = [
        (f'He wrote that it was "{QUOTED_WORDS}" and kept to it.', [QUOTE_ID], "ok"),
        ("That was told across one sentence.", [STORY_ID], "ok"),
        ("Nothing cited here.", [], "ok"),
    ]
    text, plan = _plan(rows)
    for span in plan["sentences"]:
        assert text[span["text_start"]:span["text_end"]] == rows[span["index"]][0]
    for element in plan["elements"]:
        sentence = rows[element["sentence_index"]][0]
        assert sentence[element["char_start"]:element["char_end"]] == element["surface"]


def test_sentence_index_counts_withheld_sentences_the_same_list_unverified_claims_uses():
    rows = [
        ("Withheld first.", [STORY_ID], "withhold"),
        ("Told here.", [STORY_ID], "ok"),
    ]
    _text, plan = _plan(rows)
    assert [e["sentence_index"] for e in _of(plan, STORY_ID)] == [1]
    assert plan["unverified_claims"] == {"count": 1, "sentence_indexes": [0]}


# ---- quote: the mark follows the quoted words ---------------------------


def test_quote_element_sits_on_the_verified_quotation_including_its_marks():
    sentence = f'He wrote that it was "{QUOTED_WORDS}" and kept to it.'
    _text, plan = _plan([(sentence, [QUOTE_ID], "ok")])
    [element] = _of(plan, QUOTE_ID)
    assert element["kind"] == "quote"
    assert element["surface"] == f'"{QUOTED_WORDS}"'
    assert sentence[element["char_end"]:].startswith(" and kept")


def test_single_quotation_marks_place_the_same_way():
    sentence = f"He wrote that it was '{QUOTED_WORDS}', and kept to it."
    _text, plan = _plan([(sentence, [QUOTE_ID], "ok")])
    [element] = _of(plan, QUOTE_ID)
    assert element["surface"] == f"'{QUOTED_WORDS}'"


def test_curly_quotation_marks_place_the_same_way():
    sentence = f"He wrote that it was “{QUOTED_WORDS}” and kept to it."
    _text, plan = _plan([(sentence, [QUOTE_ID], "ok")])
    [element] = _of(plan, QUOTE_ID)
    assert element["surface"] == f"“{QUOTED_WORDS}”"
    assert sentence[element["char_end"]:].startswith(" and kept")


def test_a_quotation_the_splitter_re_merged_across_a_stop_is_one_element():
    """A stop inside the quotation does not end the sentence, so the
    quote's mark follows the whole quotation, not its first half."""
    raw = f'Origen spoke. He wrote "{QUOTED_WORDS}. The disciples taught it." and kept to it [[{QUOTE_ID}]]. Then more.'
    net_result = check_turn_with_paragraph_coverage(raw, REPO)
    text = strip_tags(raw)
    citations = [{"sentence": s["sentence"], "record_ids": s["tags"]} for s in net_result["sentences"] if s["verdict"] == "ok" and s["tags"]]
    plan = build_transparency_plan(citations=citations, net_result=net_result, repository_records=REPO, world_key="alx", text=text)
    [element] = _of(plan, QUOTE_ID)
    assert element["surface"] == f'"{QUOTED_WORDS}. The disciples taught it."'
    span = plan["sentences"][element["sentence_index"]]
    sentence = text[span["text_start"]:span["text_end"]]
    assert sentence[element["char_end"]:] == " and kept to it."


def test_a_quote_record_whose_words_are_not_quoted_ends_its_sentence():
    sentence = "He held that the disciples' teaching was proof enough."
    _text, plan = _plan([(sentence, [QUOTE_ID], "ok")])
    [element] = _of(plan, QUOTE_ID)
    assert (element["char_start"], element["char_end"]) == (0, len(sentence))


def test_the_quote_mark_skips_a_quotation_its_record_does_not_hold():
    sentence = f'They called it "the new song" and wrote "{QUOTED_WORDS}" too.'
    _text, plan = _plan([(sentence, [QUOTE_ID], "ok")])
    [element] = _of(plan, QUOTE_ID)
    assert element["surface"] == f'"{QUOTED_WORDS}"'


# ---- story: the mark ends the telling -----------------------------------


def test_a_contiguous_story_run_is_one_element_at_the_end_of_its_last_sentence():
    rows = [("Part one.", [STORY_ID], "ok"), ("Part two.", [STORY_ID], "ok"), ("Part three.", [STORY_ID], "ok")]
    _text, plan = _plan(rows)
    [element] = _of(plan, STORY_ID)
    assert element["sentence_index"] == 2
    assert element["char_end"] == len("Part three.")
    assert element["repeat"] is False


def test_any_sentence_not_citing_the_story_ends_its_run_and_a_later_run_repeats():
    rows = [
        ("Told here.", [STORY_ID], "ok"),
        ("A connecting sentence.", [], "ok"),
        ("Told again, later.", [STORY_ID], "ok"),
    ]
    _text, plan = _plan(rows)
    elements = _of(plan, STORY_ID)
    assert [(e["sentence_index"], e["repeat"]) for e in elements] == [(0, False), (2, True)]
    assert sum(1 for r in plan["references"] if r["record_id"] == STORY_ID) == 1


# ---- one mark per element, never one per sentence ----------------------


def test_a_quote_and_a_term_in_one_sentence_are_two_elements_in_two_places():
    """Two grounded elements on one sentence give two marks at two
    positions, not a stacked pair at the sentence end."""
    sentence = f'By allegoria he read it, and wrote "{QUOTED_WORDS}" of the disciples.'
    text, citations, net_result = _turn([(sentence, [QUOTE_ID, TERM_ID], "ok")])
    glosses = [g for g in find_glosses_used(text, citations, REPO) if g["id"] == TERM_ID]
    assert glosses, "the lexicon scan must find the term for this fixture to mean anything"
    plan = build_transparency_plan(
        citations=citations, net_result=net_result, repository_records=REPO, world_key="alx", text=text, glosses=glosses,
    )
    [quote] = _of(plan, QUOTE_ID)
    [term] = _of(plan, TERM_ID)
    assert term["kind"] == "term" and term["surface"].lower() == "allegoria"
    assert term["char_end"] < quote["char_end"] < len(sentence)
    assert plan["end_references"] == []


def test_a_word_mark_offset_is_carried_from_the_detector_not_searched_again():
    sentence = "Allegoria was our way of reading."
    text, citations, net_result = _turn([("First.", [], "ok"), (sentence, [], "ok")])
    glosses = [g for g in find_glosses_used(text, citations, REPO) if g["id"] == TERM_ID]
    plan = build_transparency_plan(
        citations=citations, net_result=net_result, repository_records=REPO, world_key="alx", text=text, glosses=glosses,
    )
    [term] = _of(plan, TERM_ID)
    assert term["sentence_index"] == 1 and term["char_start"] == 0


# ---- general references at the end ------------------------------------


def test_witness_gravity_and_an_unsaid_term_are_general_references_not_elements():
    rows = [("A claim with several grounds.", [WITNESS_ID, GRAVITY_ID, TERM_ID], "ok")]
    _text, plan = _plan(rows)
    assert plan["elements"] == []
    assert {c["record_id"] for c in plan["end_references"]} == {WITNESS_ID, GRAVITY_ID, TERM_ID}


def test_every_cited_record_is_inline_or_at_the_end_never_both_never_neither():
    rows = [
        (f'He wrote "{QUOTED_WORDS}" plainly.', [QUOTE_ID, WITNESS_ID], "ok"),
        ("Told here.", [STORY_ID], "ok"),
        ("Held here.", [GRAVITY_ID], "ok"),
    ]
    _text, plan = _plan(rows)
    cited = {rid for _s, tags, _v in rows for rid in tags}
    inline = {e["record_id"] for e in plan["elements"]}
    ending = {c["record_id"] for c in plan["end_references"]}
    assert {r["record_id"] for r in plan["references"]} == cited
    assert inline | ending == cited
    assert not inline & ending


def test_an_element_on_a_sentence_missing_from_the_text_falls_back_to_the_end():
    rows = [("Told here.", [STORY_ID], "ok")]
    _text, citations, net_result = _turn(rows)
    plan = build_transparency_plan(
        citations=citations, net_result=net_result, repository_records=REPO, world_key="alx", text="Something else.",
    )
    assert plan["elements"] == []
    assert [c["record_id"] for c in plan["end_references"]] == [STORY_ID]


# ---- streaming: add-only, same result as the whole turn ------------------


def test_streamed_sentence_by_sentence_equals_the_whole_turn_and_never_changes_an_emitted_element():
    rows = [
        ("Told here.", [STORY_ID], "ok"),
        (f'And he wrote "{QUOTED_WORDS}" then.', [STORY_ID, QUOTE_ID], "ok"),
        ("Unrelated.", [GRAVITY_ID], "ok"),
        ("Told once more.", [STORY_ID], "ok"),
    ]
    _text, plan = _plan(rows)
    whole = [e for e in plan["elements"] if e["kind"] in ("quote", "story")]

    builder = ElementBuilder(repository_records=REPO, world_key="alx")
    emitted = []
    for index, (sentence, tags, verdict) in enumerate(rows):
        new = builder.add_sentence(index=index, sentence=sentence, tags=tags, verdict=verdict)
        # add-only: a new element is never placed on a sentence after the
        # one that just cleared, and nothing already emitted is revisited.
        assert all(e["sentence_index"] <= index for e in new)
        snapshot = [dict(e) for e in emitted]
        emitted += new
        assert emitted[: len(snapshot)] == snapshot
    emitted += builder.finish()

    def order(e):
        return (e["sentence_index"], e["char_end"], e["char_start"])

    assert sorted(emitted, key=order) == whole
    # the quote mark lands with its own sentence; the story run's mark
    # lands one sentence late, when the next sentence clears without it.
    assert [(e["kind"], e["sentence_index"]) for e in whole] == [("quote", 1), ("story", 1), ("story", 3)]


# ---- carried over from the anchor-era plan -------------------------------


def test_world_key_and_confidence_are_the_records_own():
    rows = [("Told here.", [STORY_ID], "ok")]
    _text, plan = _plan(rows)
    assert plan["world_key"] == "alx"
    [element] = plan["elements"]
    assert element["world_key"] == "alx"
    assert element["confidence"] == REPO[STORY_ID].get("confidence")
    assert all(r["world_key"] == "alx" for r in plan["references"])
    assert plan["references"][0]["confidence"] == REPO[STORY_ID].get("confidence")


def test_a_record_id_absent_from_the_repository_is_skipped_not_crashed_on():
    rows = [("Cites something gone.", ["alx.term.does-not-exist"], "ok")]
    _text, plan = _plan(rows)
    assert plan["references"] == []
    assert plan["elements"] == []
    assert plan["end_references"] == []


def test_deterministic_for_identical_input():
    rows = [("A.", [TERM_ID], "ok"), ("B.", [STORY_ID, TERM_ID], "ok")]
    _text, first = _plan(rows)
    _text, second = _plan(rows)
    assert first == second


def test_empty_turn_produces_an_empty_plan_not_an_error():
    plan = build_transparency_plan(citations=[], net_result={"sentences": []}, repository_records=REPO, world_key="alx")
    assert plan == {
        "world_key": "alx",
        "sentences": [],
        "elements": [],
        "references": [],
        "end_references": [],
        "unverified_claims": {"count": 0, "sentence_indexes": []},
    }
