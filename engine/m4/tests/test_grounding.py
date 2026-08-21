from engine.m4.grounding import find_do_not_voice_violation, ground_citations

WITNESS_RECORD = {
    "id": "fix.witness.who-is-jesus",
    "record_type": "doctrinal_witness",
    "text": "We did not claim to have seen him ourselves. We claimed only that the ones who told us could not be talked out of what they had seen, and that this was worth our lives changing because of it.",
}
TERM_RECORD = {
    "id": "fix.term.the-three",
    "record_type": "term",
    "plain_meaning": "How this world named Father, Son, and Spirit together. This was said before any later word for it existed.",
}
REPOSITORY = {WITNESS_RECORD["id"]: WITNESS_RECORD, TERM_RECORD["id"]: TERM_RECORD}

DO_NOT_VOICE_QUOTE = {
    "id": "fix.quote.private-teaching",
    "license": "do-not-voice",
    "text": "What is written for the initiate alone is not for the crowd, and not for the voice to speak.",
}
VERBATIM_QUOTE = {
    "id": "fix.quote.witness-saying",
    "license": "verbatim",
    "text": "I did not see him. I only saw what his witnesses could not stop telling.",
}
QUOTES = [DO_NOT_VOICE_QUOTE, VERBATIM_QUOTE]


def test_grounded_claim_with_excerpt_present_stays_drawn_on():
    answer = "We did not claim to have seen him ourselves - only that the witnesses could not be talked out of it."
    result = ground_citations(answer_text=answer, claimed_drawn_on=["fix.witness.who-is-jesus"], repository_records=REPOSITORY)
    assert result["drawn_on"] == ["fix.witness.who-is-jesus"]
    assert result["consulted"] == []
    assert result["unknown_ids"] == []


def test_claim_without_excerpt_present_demotes_to_consulted():
    answer = "I can tell you a little about the Three, though it's a deep subject."
    result = ground_citations(answer_text=answer, claimed_drawn_on=["fix.witness.who-is-jesus"], repository_records=REPOSITORY)
    assert result["drawn_on"] == []
    assert result["consulted"] == ["fix.witness.who-is-jesus"]


def test_invented_record_id_is_unknown_not_drawn_on_or_consulted():
    answer = "Anything at all."
    result = ground_citations(answer_text=answer, claimed_drawn_on=["fix.invented.not-a-real-record"], repository_records=REPOSITORY)
    assert result["drawn_on"] == []
    assert result["consulted"] == []
    assert result["unknown_ids"] == ["fix.invented.not-a-real-record"]


def test_multiple_claims_split_correctly():
    answer = (
        "We did not claim to have seen him ourselves. We named them Father, Son, and Spirit together, "
        "before any later word for it existed."
    )
    result = ground_citations(
        answer_text=answer,
        claimed_drawn_on=["fix.witness.who-is-jesus", "fix.term.the-three", "fix.invented.nope"],
        repository_records=REPOSITORY,
    )
    assert set(result["drawn_on"]) == {"fix.witness.who-is-jesus", "fix.term.the-three"}
    assert result["unknown_ids"] == ["fix.invented.nope"]


def test_do_not_voice_quote_verbatim_is_flagged():
    answer = "As my people said: what is written for the initiate alone is not for the crowd, and not for the voice to speak."
    violation = find_do_not_voice_violation(answer_text=answer, quotes=QUOTES)
    assert violation == "fix.quote.private-teaching"


def test_verbatim_licensed_quote_is_never_flagged():
    answer = "I did not see him. I only saw what his witnesses could not stop telling."
    violation = find_do_not_voice_violation(answer_text=answer, quotes=QUOTES)
    assert violation is None


def test_no_violation_when_do_not_voice_text_absent():
    answer = "I cannot speak to that particular teaching."
    violation = find_do_not_voice_violation(answer_text=answer, quotes=QUOTES)
    assert violation is None
