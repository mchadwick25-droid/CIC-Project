"""Hermetic tests for demonstration citation tagging (M4 step 4 follow-up,
engine/m2/builders.py: _demonstration_candidates/_candidate_head_text/
_tag_representative_text) - LIVE-GENERATION-DESIGN.md §5.3's own recommended
direct-scoring alternative to a `sources`-field-driven approach that real
records don't support. Synthetic fixture records, same discipline as
engine/m4/tests/test_evidence.py's own fixtures.
"""
from engine.m2.builders import (
    _candidate_head_text,
    _demonstration_candidates,
    _tag_representative_text,
    build_prompt,
)

WITNESS = {
    "id": "fix.witness.who-is-jesus",
    "record_type": "doctrinal_witness",
    "canon_cells": ["C-I"],
    "text": "We did not claim to have seen him ourselves.",
}
# A record whose HEAD (compiled-facing) text is short and unrelated to
# "death" or "cost", but whose trailing body (never compiled) happens to
# discuss torture and cost at length - the exact real-data shape that
# produced a false tag before this module scored against head text only.
TERM_WITH_MISLEADING_BODY = {
    "id": "fix.term.ministrae",
    "record_type": "term",
    "canon_cells": ["C-I"],
    "plain_meaning": "A word for two women in a recognized service role.",
    "quick_meaning": "Two women, a recognized role.",
    "_body": "A Roman magistrate's letter records the cost of an interrogation naming these women; the name for their office is otherwise unattested in this world's own record, and its own history is unrecorded.",
}
DEMO = {
    "id": "fix.demo.center-who-is-jesus",
    "record_type": "demonstration",
    "canon_cells": ["C-I"],
    "exchange": [
        {"speaker": "participant", "text": "Who was Jesus to your people?"},
        {
            "speaker": "representative",
            "text": (
                "We did not claim to have seen him ourselves. "
                "Vera met the travellers at the well outside Testland. "
                "What we can tell you is what a death for the name cost some of us."
            ),
        },
    ],
}
# A CLAIM-BEARING sentence and the record that grounds it. Needed because
# the compiler now asks the live net's own question first - does this
# sentence even make a checkable claim? - and only then what grounds it.
# "We did not claim to have seen him ourselves" names no person, place,
# text or number, so the net never demands a citation for it and the
# compiler correctly leaves it bare. Every test in this file used to assert
# tagging against exactly that sentence.
STORY = {
    "id": "fix.story.vera-at-the-well",
    "record_type": "story",
    "canon_cells": ["C-I"],
    "tellable_as": "how Vera met the travellers at the well outside Testland",
    "text": "Vera met the travellers at the well outside Testland and told them plainly what she had heard.",
}
# Deliberately OUTSIDE the demonstration's own canon cell, and the only
# record that grounds the Vera sentence - the miniature of what cell scoping
# used to hide (alx.story.potamiaena, sitting in the same package, unused,
# while the Potamiaena sentence was withheld for having no tag).
OUT_OF_CELL_STORY = {
    "id": "fix.story.marcella-on-the-road",
    "record_type": "story",
    "canon_cells": ["F6-P"],
    "tellable_as": "how Marcella walked the coast road to Testland",
    "text": "Marcella walked the coast road to Testland every spring and was remembered for it by name.",
}
REPOSITORY = {r["id"]: r for r in (WITNESS, TERM_WITH_MISLEADING_BODY, STORY, OUT_OF_CELL_STORY, DEMO)}


def test_demonstration_candidates_scoped_to_the_demos_own_cell():
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    assert {c["id"] for c in candidates} == {
        "fix.witness.who-is-jesus",
        "fix.term.ministrae",
        "fix.story.vera-at-the-well",
    }  # fix.story.marcella-on-the-road is in F6-P, not this demo's cell


def test_demonstration_candidates_empty_when_demo_has_no_canon_cells():
    assert _demonstration_candidates(REPOSITORY, {"canon_cells": []}) == []


def test_candidate_head_text_uses_compiler_facing_fields_only():
    head = _candidate_head_text(TERM_WITH_MISLEADING_BODY)
    assert "cost" not in head.lower()
    assert "interrogation" not in head.lower()
    assert "recognized service role" in head or "recognized role" in head


def test_tag_representative_text_tags_a_grounded_sentence():
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    tagged = _tag_representative_text(
        "Vera met the travellers at the well outside Testland.", candidates, REPOSITORY
    )
    assert "[[fix.story.vera-at-the-well]]" in tagged


def test_tag_representative_text_never_tags_from_a_records_trailing_body():
    """The regression case found against real data: a short sentence that
    shares 2 common words with a candidate's TRAILING BODY (never
    compiled, never seen by a model) must not get tagged to that
    candidate - only the record's own compiled-facing head text counts."""
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    tagged = _tag_representative_text(
        "What we can tell you is what a death for the name cost some of us.", candidates, REPOSITORY
    )
    assert "[[fix.term.ministrae]]" not in tagged
    assert "[[" not in tagged  # nothing else clears the floor either - correctly left untagged


def test_tag_representative_text_leaves_ungrounded_sentences_untagged():
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    tagged = _tag_representative_text("We are glad you asked us that question today.", candidates, REPOSITORY)
    assert "[[" not in tagged


def test_tag_representative_text_empty_candidates_is_a_no_op():
    text = "Vera met the travellers at the well outside Testland."
    assert _tag_representative_text(text, [], {}) == text


def test_build_prompt_tags_only_representative_turns_not_participant_turns():
    prompt = build_prompt(REPOSITORY, {}, {"display_name": "Fixture World"}).decode("utf-8")
    idx = prompt.find("## Demonstration:")
    section = prompt[idx:]
    participant_line = next(line for line in section.splitlines() if line.startswith("participant:"))
    representative_line = next(line for line in section.splitlines() if line.startswith("representative:"))
    assert "[[" not in participant_line
    assert "[[fix.story.vera-at-the-well]]" in representative_line
    assert "[[fix.term.ministrae]]" not in representative_line


# ---------------------------------------------------------------------------
# Placement, and the round-trip that placement exists for.
#
# Every test above this line passed while the compiler emitted its tags on
# the WRONG SIDE of the terminal punctuation, because each one asserted only
# that the right record id appeared SOMEWHERE in the string. The live net
# does not read the string; it splits it first. These tests assert the thing
# the earlier ones assumed.
# ---------------------------------------------------------------------------
from engine.m4.grounding_net import check_turn, parse_tagged


def test_tag_lands_before_the_terminal_punctuation_not_after_it():
    """The citation contract's own requirement, in its own words: tags go
    "before the terminal punctuation... so a sentence-boundary split can
    never break inside one\"."""
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    tagged = _tag_representative_text(
        "Vera met the travellers at the well outside Testland.", candidates, REPOSITORY
    )
    assert tagged == "Vera met the travellers at the well outside Testland [[fix.story.vera-at-the-well]]."


def test_the_tag_grounds_its_own_sentence_after_the_live_splitter_runs():
    """The actual defect, stated as the invariant it violated: run the
    compiled text through the LIVE parser and the tag must still be on the
    sentence it was computed for - not carried onto the next one.

    With the tag emitted after the stop, parse_tagged returned
    [{sentence-1, tags: []}, {sentence-2, tags: [witness]}] - sentence 1
    untagged and therefore withheld, sentence 2 grounded in a record it
    never drew on. That is a one-sentence-late shift through the whole
    turn, and the first substantive claim always falls off the front."""
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    tagged = _tag_representative_text(
        "Vera met the travellers at the well outside Testland. We are glad you asked us that today.",
        candidates,
        REPOSITORY,
    )
    parsed = parse_tagged(tagged)
    assert parsed[0]["text"] == "Vera met the travellers at the well outside Testland."
    assert parsed[0]["tags"] == ["fix.story.vera-at-the-well"]
    assert parsed[1]["tags"] == []


def test_a_tagged_demo_sentence_survives_the_live_net_it_teaches():
    """The invariant this module's own note has always claimed - "a demo
    that would pass its own net if it were live output is exactly the demo
    that gets tagged here" - asserted for the first time."""
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    tagged = _tag_representative_text(
        "Vera met the travellers at the well outside Testland.", candidates, REPOSITORY
    )
    verdicts = check_turn(tagged, REPOSITORY)["sentences"]
    assert [v["verdict"] for v in verdicts] == ["ok"]


def test_a_sentence_with_no_terminal_punctuation_still_gets_its_tag():
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    tagged = _tag_representative_text(
        "Vera met the travellers at the well outside Testland", candidates, REPOSITORY
    )
    assert tagged == "Vera met the travellers at the well outside Testland [[fix.story.vera-at-the-well]]"


# ---------------------------------------------------------------------------
# Quote-holder preference.
# ---------------------------------------------------------------------------
QUOTE_RECORD = {
    "id": "fix.quote.seen-him",
    "record_type": "quote",
    "canon_cells": ["C-I"],
    "text": "we did not claim to have seen him ourselves",
}
PARAPHRASE_WITNESS = {
    "id": "fix.witness.paraphrase",
    "record_type": "doctrinal_witness",
    "canon_cells": ["C-I"],
    # Deliberately out-scores the quote record on plain lexical overlap
    # while containing none of the quoted words verbatim.
    "text": "Our own teachers reported that the community reported the report of the reporting witnesses.",
}
QUOTE_REPOSITORY = {r["id"]: r for r in (QUOTE_RECORD, PARAPHRASE_WITNESS, DEMO)}


def test_a_quoted_sentence_is_tagged_to_the_record_that_holds_the_quote():
    """The net judges a quoted sentence on ONE rule - the quoted words are
    verbatim in a tagged record - and lexical overlap cannot satisfy it. A
    record that PARAPHRASES a quote routinely out-scores the record holding
    it, so the ranked-best tag named a record the net then rejected and the
    quote was withheld. Found in hal's shipped package: the Ciceronian-dream
    quote tagged to a paraphrasing witness while
    hal.quote.dream-follower-of-cicero sat unused in the same package."""
    sentence = "He answered them: 'we did not claim to have seen him ourselves'."
    candidates = _demonstration_candidates(QUOTE_REPOSITORY, DEMO)
    tagged = _tag_representative_text(sentence, candidates, QUOTE_REPOSITORY)
    assert "[[fix.quote.seen-him]]" in tagged
    assert "[[fix.witness.paraphrase]]" not in tagged
    assert [v["verdict"] for v in check_turn(tagged, QUOTE_REPOSITORY)["sentences"]] == ["ok"]


def test_a_demonstration_is_never_another_demonstrations_quote_ground():
    """A demo's own text lives in the repository, so it matches itself (and
    any demo quoting the same line) trivially. Citing one as ground would
    be circular."""
    sentence = "He answered them: 'we did not claim to have seen him ourselves'."
    tagged = _tag_representative_text(sentence, [], QUOTE_REPOSITORY)
    assert "fix.demo" not in tagged


# ---------------------------------------------------------------------------
# The citation contract's placeholder ids.
# ---------------------------------------------------------------------------
from engine.m2.builders import build_fleet_preamble

_FLEET_WITH_PLACEHOLDER = {
    "fleet.voice.fleet": {
        "id": "fleet.voice.fleet",
        "record_type": "fleet_voice",
        "citation_contract": (
            "Every claim is tagged before the terminal punctuation - for example: "
            "'...the same bread [[world.term.example]] [[world.gravity.example]].'"
        ),
    }
}


def test_the_contracts_placeholder_ids_are_never_shipped_to_a_model():
    """`world.term.example` is a PLACEHOLDER, and the fleet record says so:
    it exists "only so citation_contract is a complete, self-explanatory
    paragraph on its own - never the line a model is actually shown". The
    substitution was never implemented, so all seven packages shipped the
    literal token `world` into live model input - and a model reads it as
    the namespace, emitting world.story.pliny-interrogation,
    world.term.hesychia: right shape, no such record, sentence withheld.
    46% of all tags emitted in the 2026-08-23 live run were this."""
    segments = build_fleet_preamble(_FLEET_WITH_PLACEHOLDER, {"display_name": "Fixture World"}, REPOSITORY)
    contract = next(s for s in segments if s.startswith("## Citation contract"))
    assert "world.term.example" not in contract
    assert "world.gravity.example" not in contract
    # the term placeholder takes this world's own lowest-sorted term record;
    # the gravity one has no gravity record to take, so it is dropped rather
    # than filled with an off-type id
    assert "[[fix.term.ministrae]]" in contract


def test_a_placeholder_with_no_real_substitute_is_dropped_not_shipped():
    """An absent second tag still reads as a correct worked line. An
    unresolvable one teaches a fabrication."""
    only_one_record = {"fix.witness.who-is-jesus": WITNESS}
    segments = build_fleet_preamble(_FLEET_WITH_PLACEHOLDER, {"display_name": "Fixture World"}, only_one_record)
    contract = next(s for s in segments if s.startswith("## Citation contract"))
    assert "world." not in contract
    # one real id fills the first placeholder; the second has nothing left
    # to point at that isn't a duplicate, so it is dropped
    assert contract.count("[[fix.witness.who-is-jesus]]") == 1


def test_a_double_quoted_sentence_is_tagged_to_its_quote_record_too():
    """The compiler's quote-holder preference reads spans through the same
    splitter the net does. While that splitter saw only ' , a demo quoting
    with " got no quote-holder treatment at all and fell back to lexical
    ranking - which is exactly what hands a quote to a paraphrase."""
    sentence = 'He answered them: "we did not claim to have seen him ourselves".'
    candidates = _demonstration_candidates(QUOTE_REPOSITORY, DEMO)
    tagged = _tag_representative_text(sentence, candidates, QUOTE_REPOSITORY)
    assert "[[fix.quote.seen-him]]" in tagged
    assert "[[fix.witness.paraphrase]]" not in tagged
    assert [v["verdict"] for v in check_turn(tagged, QUOTE_REPOSITORY)["sentences"]] == ["ok"]


def test_a_double_quote_spanning_a_sentence_boundary_gets_one_tag_not_two():
    """The compiler tags per quote-aware sentence. If the splitter breaks
    inside a double-quoted span, the compiler tags two half-sentences and
    the net then judges each half on its own - the compile-time twin of the
    orphaning seen live."""
    sentence = 'He told them: "we did not claim to have seen him ourselves. We claimed only what we were told".'
    tagged = _tag_representative_text(sentence, [], QUOTE_REPOSITORY)
    assert tagged.count("[[") == 1


# ---------------------------------------------------------------------------
# The net's bar (2026-08-23 ruling).
#
# The compiler used to score an overlap coefficient over _candidate_head_text,
# scoped to the demo's own canon cell. The net scored a ratio over the whole
# record text and did not scope by cell at all. Between the two, 20 true,
# sourced sentences were dropped from the fleet's own demonstrations - and
# the demos then taught a live model that such sentences go untagged.
# ---------------------------------------------------------------------------
def test_a_claim_is_grounded_by_a_record_outside_the_demonstrations_own_cell():
    """The miniature of what cell scoping hid. alx.story.potamiaena sat in
    the same package, unused, while "One young woman, Potamiaena, was
    remembered among us by name" was withheld for carrying no tag - because
    the story record was not in the demonstration's cell."""
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    assert "fix.story.marcella-on-the-road" not in {c["id"] for c in candidates}
    tagged = _tag_representative_text(
        "Marcella walked the coast road to Testland every spring.", candidates, REPOSITORY
    )
    assert "[[fix.story.marcella-on-the-road]]" in tagged
    assert [v["verdict"] for v in check_turn(tagged, REPOSITORY)["sentences"]] == ["ok"]


def test_an_interpretive_sentence_carries_no_tag_even_when_a_record_scores_well():
    """The citation contract's own rule - "a connective or interpretive
    sentence carries no tag; only a sentence naming a person, place, text,
    number, or attributed quote does" - which the demonstrations themselves
    used to violate. With the bar widened, suppressing these matters more,
    not less: without it a framing line picks up a tag on coincidence and
    teaches a model to cite its own framing."""
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    # shares most of its content words with the Vera story, and still must
    # not be tagged: it makes no checkable claim.
    tagged = _tag_representative_text("What she heard, she told plainly.", candidates, REPOSITORY)
    assert "[[" not in tagged


def test_honesty_scaffolding_is_exempt_here_exactly_as_the_net_exempts_it():
    candidates = _demonstration_candidates(REPOSITORY, DEMO)
    tagged = _tag_representative_text(
        "We will not invent a story about Vera at Testland that our record does not hold.",
        candidates,
        REPOSITORY,
    )
    assert "[[" not in tagged


def test_a_sentence_quoting_two_records_names_both():
    """The net's quoted-span rule is over the UNION of the cited records, so
    demanding that ONE record hold every span was the compiler being stricter
    than the net again, one level down. hal's monastery-burning turn quotes
    hal.quote.house-destroyed and hal.quote.innocent-ravages in one breath."""
    two = {
        "fix.quote.first": {"id": "fix.quote.first", "record_type": "quote", "canon_cells": ["C-I"],
                            "text": "the road was long and the well was dry"},
        "fix.quote.second": {"id": "fix.quote.second", "record_type": "quote", "canon_cells": ["C-I"],
                             "text": "she carried the water back before dawn"},
    }
    sentence = "She wrote: 'the road was long and the well was dry', and later: 'she carried the water back before dawn'."
    tagged = _tag_representative_text(sentence, [], two)
    assert "[[fix.quote.first]]" in tagged and "[[fix.quote.second]]" in tagged
    assert [v["verdict"] for v in check_turn(tagged, two)["sentences"]] == ["ok"]


def test_build_apparatus_is_never_named_as_a_sentences_ground():
    """The live net accepts any record id that resolves, voice_craft and
    source records included - so widening the compiler's search to every
    type produced a syr claim about persecution tagged to syr.voice.craft.
    The compiler stays stricter than the net on this one axis, which can
    only change WHICH record grounds a sentence, never whether one does."""
    with_apparatus = dict(REPOSITORY)
    with_apparatus["fix.voice.craft"] = {
        "id": "fix.voice.craft",
        "record_type": "voice_craft",
        "canon_cells": ["C-I"],
        "identity": "Vera met the travellers at the well outside Testland, and speaks for them.",
    }
    tagged = _tag_representative_text(
        "Vera met the travellers at the well outside Testland.",
        _demonstration_candidates(with_apparatus, DEMO),
        with_apparatus,
    )
    assert "[[fix.voice.craft]]" not in tagged
    assert "[[fix.story.vera-at-the-well]]" in tagged


def test_records_is_required_so_a_caller_can_never_silently_tag_nothing():
    """The search scope is package-wide now; a caller passing candidates
    alone would tag nothing at all rather than fail."""
    import pytest

    with pytest.raises(TypeError):
        _tag_representative_text("Vera met the travellers at the well.", [])
