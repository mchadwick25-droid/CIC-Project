"""Every case here is one the live probe actually produced, or the exact
false positive that would make the check useless."""
import pytest

from engine.m4 import events
from engine.m4.output_check import check_output, find_shipped_defects


def _families(findings):
    return sorted(f["family"] for f in findings)


def test_clean_text_produces_nothing():
    assert check_output("We rose before dawn and wove baskets.", history=[]) == []


def test_catches_the_malformed_tag_strip_tags_cannot():
    """grounding_net.strip_tags matches [a-z0-9_.-]+ only, so a tag with
    uppercase, a colon and spaces survives it. Eight reached a participant
    across three turns of the desert probe."""
    text = "We kept the teaching [[THIN: no material on dying practices]]."
    assert _families(check_output(text, history=[])) == ["display"]


def test_a_claim_of_prior_discourse_on_the_opening_turn_is_false():
    findings = check_output("We already told you how we ate.", history=[])
    assert [f["finding"].startswith("false:") for f in findings] == [True]


def test_names_a_person_no_prior_turn_named():
    """The bug, verbatim: 'the one woman I have named to you so far in this
    conversation' - two turns into a conversation about food."""
    history = [
        {"role": "user", "content": "How did you get food?"},
        {"role": "assistant", "content": "We wove baskets and sold them in the village."},
    ]
    findings = [f for f in check_output("We already named Sarah among us.", history=history) if f["family"] == "conversational"]
    assert len(findings) == 1
    assert findings[0]["finding"].startswith("false:")
    assert "Sarah" in findings[0]["finding"]


def test_a_name_that_was_said_is_not_flagged():
    history = [
        {"role": "user", "content": "Who taught you?"},
        {"role": "assistant", "content": "Sarah was an amma among us."},
    ]
    assert [f for f in check_output("We already named Sarah among us.", history=history) if f["family"] == "conversational"] == []


def test_a_nameless_claim_is_unverified_not_ruled_on():
    """'We told you it is not effort alone' - no name, so whether the topic
    was discussed is a judgment no pattern here can make."""
    history = [
        {"role": "user", "content": "How did you get food?"},
        {"role": "assistant", "content": "We wove baskets."},
    ]
    findings = [f for f in check_output("We told you it is not effort alone.", history=history) if f["family"] == "conversational"]
    assert len(findings) == 1
    assert findings[0]["finding"].startswith("unverified:")


def test_first_person_singular_is_flagged():
    assert "pronoun" in _families(check_output("You are asking me to identify her.", history=[]))


def test_a_quoted_figure_keeps_their_own_first_person():
    """The pronoun rule's own carve-out: a named figure's quoted words keep
    their original wording - that is a citation, not the voice speaking."""
    text = 'She answered them: "It is I who am a man among you, and ye who are women".'
    assert "pronoun" not in _families(check_output(text, history=[]))


def test_the_sanctioned_self_naming_line_is_not_flagged():
    text = "I am a representative of Desert Monasticism, not one of its elders."
    assert "pronoun" not in _families(check_output(text, history=[]))


def test_voice_turn_cannot_be_emitted_without_the_check_having_run():
    payload = {
        "speaker": "desert", "text": "We wove baskets.", "citations": [],
        "glosses": [], "figures_used": [], "quote_offers": [],
        "attempts_meta": {"empty_stream_retries": 0},
    }
    with pytest.raises(events.EventValidationError):
        events.validate("voice_turn", payload)
    events.validate("voice_turn", {**payload, "output_defects": []})


# ---- the participant-message half ------------------------------------------
# The false premise lives in the participant's turn; acceptance is the ABSENCE
# of a correction in the reply. Every case below is one the live probe produced.

_FOOD_HISTORY = [
    {"role": "user", "content": "How did you get food?"},
    {"role": "assistant", "content": "We wove baskets and sold them in the village."},
]


def test_accepting_a_false_premise_by_deixis_is_caught():
    """'That was Sarah' carries no back-reference phrase at all - the
    acceptance is the word 'that', pointing at a mention the participant
    asserted and the transcript refutes. No pattern over the reply reaches
    it."""
    findings = check_output(
        "That was Sarah - Amma Sarah, by the honored address we gave to proven elders.",
        history=_FOOD_HISTORY,
        participant_message="Earlier you mentioned a woman among you by name. Who was she?",
    )
    conversational = [f for f in findings if f["family"] == "conversational"]
    assert len(conversational) == 1
    assert conversational[0]["finding"].startswith("false:")
    assert "Sarah" in conversational[0]["finding"]


def test_declining_a_false_premise_produces_nothing():
    findings = check_output(
        "We have not named anyone yet. Sarah was an amma among us, and here is what we kept of her.",
        history=_FOOD_HISTORY,
        participant_message="Earlier you mentioned a woman among you by name. Who was she?",
    )
    assert [f for f in findings if f["family"] == "conversational"] == []


def test_a_supported_follow_up_is_not_flagged():
    """The common case, and the one that would make this check unusable if it
    fired: the participant refers back to something really said."""
    history = [
        {"role": "user", "content": "What did you believe about the end of the world?"},
        {"role": "assistant", "content": "We held that judgment was coming and the dead would rise."},
    ]
    findings = check_output(
        "We did not keep an account of how we sat with the dying.",
        history=history,
        participant_message="You just answered about the end. Did that shape how you treated the dying?",
    )
    assert [f for f in findings if f["family"] == "conversational"] == []


def test_a_traditions_phrasing_is_not_a_claim_about_this_conversation():
    """'as we put it' attributes WORDING to the tradition. An earlier version
    flagged it, which is a false positive on ordinary voice."""
    findings = check_output(
        "We took that from experience - led, as we put it, not by chattering words but by experience.",
        history=_FOOD_HISTORY,
        participant_message="How were you saved?",
    )
    assert [f for f in findings if f["family"] == "conversational"] == []


# find_shipped_defects: a defect check_output() already caught reached engine.m4.live_turn_run's
# own report with `degraded: false` on the same turn - nothing read
# output_defects back before this. These cases are the report shapes
# themselves, not the text-level check already covered above.

def _defect(finding="false: claims something was already said, on a turn with no prior turns"):
    return {"family": "conversational", "finding": finding, "sentence": "We have named it plainly, more than once."}


def test_clean_turn_run_report_has_no_shipped_defects():
    report = {"results": [{"id": "message-1", "message": "hi", "result": {"voice_event": {"output_defects": []}}}]}
    assert find_shipped_defects(report) == []


def test_turn_run_report_surfaces_a_shipped_defect():
    report = {"results": [{"id": "message-3", "message": "What did your founder write?",
                            "result": {"voice_event": {"output_defects": [_defect()]}}}]}
    found = find_shipped_defects(report)
    assert len(found) == 1
    assert found[0]["id"] == "message-3"
    assert found[0]["family"] == "conversational"


def test_turn_run_report_with_no_voice_event_is_clean():
    """A facilitator-only turn (e.g. safety_turn) has voice_event: None."""
    report = {"results": [{"id": "message-1", "message": "hi", "result": {"voice_event": None}}]}
    assert find_shipped_defects(report) == []


def test_table_run_report_surfaces_a_shipped_defect():
    report = {"rounds": [{"message": "hi", "turns": [
        {"round_no": 2, "position": 1, "turn_selected": {"world_key": "witt"}, "voice": {"output_defects": [_defect()]}},
    ]}]}
    found = find_shipped_defects(report)
    assert len(found) == 1
    assert found[0]["round_no"] == 2
    assert found[0]["position"] == 1


def test_table_run_report_with_no_voice_this_position_is_clean():
    """A closed/facilitator-only table turn has no 'voice' key at all."""
    report = {"rounds": [{"message": "hi", "turns": [{"round_no": 1, "position": 0, "turn_selected": None}]}]}
    assert find_shipped_defects(report) == []


# ---- guard_proximity: the prefer_instead redirect rule's guard half (Build-Plan.md Stage 4b) -----------
# The real guard text and the real fabricated assertion the measurement
# used - gallic.story.brictio-in-the-
# courtyard, one of the 13 real guard clauses, caught only 2/13 times by
# grounding_net's own per-sentence check.

_BRICTIO_GUARD = (
    "participant is asking whether Brictio succeeded Martin as bishop - our "
    "vendored evidence does not say, and the Representative must not supply it"
)
_BRICTIO_RECORD = {"id": "gallic.story.brictio-in-the-courtyard", "record_type": "story", "claim_guards": [_BRICTIO_GUARD]}
_BRICTIO_RECORDS = {_BRICTIO_RECORD["id"]: _BRICTIO_RECORD}


def _cited(sentence):
    return [{"sentence": sentence, "record_ids": [_BRICTIO_RECORD["id"]]}]


def test_the_real_stage_1_fabrication_is_caught():
    sentence = "Brictio succeeded Martin as bishop of Tours."
    findings = check_output(sentence, citations=_cited(sentence), repository_records=_BRICTIO_RECORDS)
    hits = [f for f in findings if f["family"] == "guard_proximity"]
    assert len(hits) == 1
    assert _BRICTIO_RECORD["id"] in hits[0]["finding"]


def test_a_reworded_sentence_sharing_the_claims_own_words_is_still_caught():
    """Different sentence structure, same barred claim - this is a
    keyword-overlap check, not real NLU, so it catches a reworded
    assertion that still uses the claim's own words ("succeeded",
    "bishop"), not every possible paraphrase. A rewording that avoids
    both words entirely (e.g. "took his place") is a known, accepted gap
    of this family - report-only, reviewed by a human, never the only
    net (grounding_net's own per-sentence check runs independently)."""
    sentence = "It was Brictio who succeeded as bishop, once Martin had died."
    findings = check_output(sentence, citations=_cited(sentence), repository_records=_BRICTIO_RECORDS)
    assert "guard_proximity" in _families(findings)


def test_merely_naming_both_figures_together_is_not_flagged():
    """THE FALSE POSITIVE THAT WOULD MAKE THIS FAMILY USELESS: Brictio and
    Martin are the two people the story is actually about, so their names
    alone co-occur in every truthful sentence about it - only a sentence
    sharing the claim's own non-name vocabulary (what it actually says
    about them, not just who they are) is asserting the barred claim."""
    sentence = "Brictio was in the courtyard when Martin confronted him about his conduct."
    findings = check_output(sentence, citations=_cited(sentence), repository_records=_BRICTIO_RECORDS)
    assert "guard_proximity" not in _families(findings)


def test_a_different_true_claim_about_the_same_names_is_not_flagged():
    sentence = "Martin never named a successor before he died."
    findings = check_output(sentence, citations=_cited(sentence), repository_records=_BRICTIO_RECORDS)
    assert "guard_proximity" not in _families(findings)


def test_a_sentence_declining_the_barred_claim_is_not_flagged():
    """The voice correctly saying it must not supply this is the opposite
    of the defect - GUARD_MARKERS' own phrases are what claim_guards
    notes are written in, so a sentence using the identical honesty
    register is framing a limit, not asserting one."""
    sentence = "Our own sources do not say who succeeded Martin as bishop, and we must not supply an answer."
    findings = check_output(sentence, citations=_cited(sentence), repository_records=_BRICTIO_RECORDS)
    assert "guard_proximity" not in _families(findings)


def test_a_sentence_citing_a_different_record_is_not_checked_against_this_guard():
    sentence = "Brictio succeeded Martin as bishop of Tours."
    citations = [{"sentence": sentence, "record_ids": ["gallic.story.unrelated"]}]
    findings = check_output(sentence, citations=citations, repository_records=_BRICTIO_RECORDS)
    assert "guard_proximity" not in _families(findings)


def test_no_citations_or_no_repository_records_is_a_quiet_no_op():
    """A caller that never learned about citations/records (a bare-text
    check) gets the other three families exactly as before this one
    existed - never an error."""
    sentence = "Brictio succeeded Martin as bishop of Tours."
    assert check_output(sentence, history=[]) == []
    assert check_output(sentence, history=[], citations=_cited(sentence)) == []
    assert check_output(sentence, history=[], repository_records=_BRICTIO_RECORDS) == []


def test_multiple_defects_across_both_report_shapes_all_surface():
    report = {
        "results": [{"id": "message-1", "message": "a", "result": {"voice_event": {"output_defects": [_defect(), _defect("false: second")]}}}],
        "rounds": [{"message": "b", "turns": [{"round_no": 1, "position": 0, "voice": {"output_defects": [_defect("false: third")]}}]}],
    }
    assert len(find_shipped_defects(report)) == 3


def test_the_horizon_family_reports_a_later_mention_and_needs_the_window():
    from engine.m4.output_check import check_output
    text = "We kept the feast. After the Council of Chalcedon we parted."
    found = [d for d in check_output(text, window_end=400) if d["family"] == "horizon"]
    assert found == [{"family": "horizon", "finding": "names the Council of Chalcedon (451), after the window closes in 400",
                      "sentence": "After the Council of Chalcedon we parted."}]
    assert not [d for d in check_output(text) if d["family"] == "horizon"]
