from engine.m4.sentence_fact_check import find_unsupported_named_claims

# Hermetic, synthetic fixtures: a specific named claim with zero support
# anywhere in the world's own compiled ground.
_REPOSITORY = {
    "cap.story.council": {
        "id": "cap.story.council",
        "record_type": "story",
        "text": "Our teachers defended the same homoousios that the council at Nicaea had written into the creed.",
    },
    "cap.figure.eustathius": {
        "id": "cap.figure.eustathius",
        "record_type": "figure",
        "text": "Eustathius of Sebaste, our own ascetic reformer, became our adversary over the Spirit's own standing.",
    },
    "rzg.witness.schism": {
        "id": "rzg.witness.schism",
        "record_type": "doctrinal_witness",
        "text": "Felix Manz broke from our founder over infant baptism in 1525, one of three men who did.",
    },
}


def test_whole_repository_ground_not_a_single_tags_own_ground():
    # "Manz" is grounded by rzg.witness.schism even though this sentence
    # carries no tag at all (or a different one) - a whole-repository
    # check, not a per-tag one.
    sentence = "Felix Manz argued that a true church gathers only by a believer's own profession."
    flags = find_unsupported_named_claims(
        [{"sentence": sentence, "tags": []}], repository_records=_REPOSITORY
    )
    assert flags == []


def test_sentence_initial_proper_noun_is_caught():
    # A sentence's own first word is included in proper-noun detection
    # here, unlike engine.prose.claim_markers' own default.
    sentence = "Athanasius himself was named among the bishops who signed the creed."
    flags = find_unsupported_named_claims(
        [{"sentence": sentence, "tags": ["cap.story.council"], "verdict": "ok"}], repository_records=_REPOSITORY
    )
    assert len(flags) == 1
    assert flags[0]["class"] == "unsupported_named_claim"
    assert "athanasius" in flags[0]["missing"]
    assert flags[0]["tags"] == ["cap.story.council"]


def test_unsupported_number_is_caught():
    sentence = "Felix Manz was drowned in the Limmat River in January 1527."
    flags = find_unsupported_named_claims(
        [{"sentence": sentence, "tags": []}], repository_records=_REPOSITORY
    )
    missing = flags[0]["missing"]
    assert "limmat" in missing
    assert "river" in missing


def test_grounded_number_is_not_flagged():
    # 1525 is real ground (rzg.witness.schism); a sentence naming only the
    # real, grounded year must not flag on the number check.
    sentence = "Felix Manz broke from the founder in 1525."
    assert find_unsupported_named_claims([{"sentence": sentence, "tags": []}], repository_records=_REPOSITORY) == []


def test_interpretive_sentence_with_no_claim_marker_passes():
    assert find_unsupported_named_claims(
        [{"sentence": "It did not end cleanly.", "tags": []}], repository_records=_REPOSITORY
    ) == []


def test_question_is_exempt():
    sentence = "Was Athanasius really among the bishops who signed it?"
    assert find_unsupported_named_claims([{"sentence": sentence, "tags": []}], repository_records=_REPOSITORY) == []


def test_honest_limit_absence_claim_is_exempt():
    # Reused unchanged from engine.m4.uncited_claims - a sentence
    # explicitly denying knowledge of something makes no claim this
    # module has any business grounding.
    sentence = "Whether Athanasius ever wrote to us, our record does not say."
    assert find_unsupported_named_claims([{"sentence": sentence, "tags": []}], repository_records=_REPOSITORY) == []


def test_first_person_no_claim_is_exempt():
    sentence = "We will not pretend to know what Athanasius himself believed."
    # SCAFFOLD_MARKERS' own "we will not pretend" already exempts this via
    # _is_honest_limit before _is_first_person_no_claim is even reached -
    # this fixture is deliberately built to also carry no OTHER checkable
    # claim, so either exemption path clears it.
    assert find_unsupported_named_claims([{"sentence": sentence, "tags": []}], repository_records=_REPOSITORY) == []


def test_hypothetical_conditional_naming_an_absent_entity_is_exempt():
    # A subjunctive "if X, we would Y" names X while asserting nothing
    # about it - the grammatical mirror of the honest-limit case above,
    # and not covered by _is_honest_limit's own fixed phrases (which look
    # for an explicit absence claim, not a subjunctive mood).
    sentence = "If Athanasius had written to us, we would have kept the letter."
    assert find_unsupported_named_claims([{"sentence": sentence, "tags": []}], repository_records=_REPOSITORY) == []


def test_hypothetical_exemption_is_scoped_to_the_conditional_clause_only():
    # A name or number OUTSIDE the if...would span, even in a sentence
    # that also contains one, must still be checked - only the
    # conditional clause's own claims are exempt, not the whole sentence.
    sentence = "Felix Manz was drowned in the Limmat in 1527, and if you ask why, the council would say heresy."
    flags = find_unsupported_named_claims([{"sentence": sentence, "tags": []}], repository_records=_REPOSITORY)
    assert flags and "limmat" in flags[0]["missing"]


def test_unsupported_characterization_of_a_real_figure_is_not_flagged():
    # Eustathius is a real, grounded name; "coward" is an ordinary
    # adjective, not a proper noun or number, so claim_markers finds
    # nothing to check in this sentence at all. An unsupported
    # characterization of an already-grounded name carries no marker of
    # its own for this module to compare against ground.
    sentence = "Some among us thought he was a coward."
    assert find_unsupported_named_claims(
        [{"sentence": sentence, "tags": ["cap.figure.eustathius"], "verdict": "ok"}], repository_records=_REPOSITORY
    ) == []


def test_examines_every_sentence_regardless_of_tag_or_verdict():
    # Unlike named_claim_grounding.find_named_claim_flags (verdict=="ok"
    # and tags only), this module's whole point is sentences a paragraph-
    # or tag-scoped check would never look at - an untagged sentence and a
    # withheld one are both examined here.
    sentences = [
        {"sentence": "Felix Manz argued for believer's baptism.", "tags": [], "verdict": "ok"},
        {"sentence": "Athanasius was named among the signers.", "tags": ["cap.story.council"], "verdict": "withhold"},
    ]
    flags = find_unsupported_named_claims(sentences, repository_records=_REPOSITORY)
    assert len(flags) == 1
    assert "athanasius" in flags[0]["missing"]


def test_clean_turn_returns_no_flags():
    sentences = [
        {"sentence": "Eustathius became our adversary over the Spirit's own standing.", "tags": ["cap.figure.eustathius"], "verdict": "ok"},
        {"sentence": "It did not end cleanly.", "tags": [], "verdict": "ok"},
    ]
    assert find_unsupported_named_claims(sentences, repository_records=_REPOSITORY) == []


# Two known, accepted false-positive classes this module inherits from
# missing_markers unchanged - pinned here the same way
# test_named_claim_grounding.py's own
# test_derivational_form_stays_an_accepted_known_limit pins the identical
# root cause for its own (tag-scoped) check.

_DERIVATIONAL_REPOSITORY = {
    "cap.core.cappadocian": {
        "id": "cap.core.cappadocian",
        "record_type": "core",
        "text": "Alexandria's own school shaped a generation of Cappadocian teachers.",
    },
}


def test_derivational_form_mismatch_is_a_known_limit():
    # "Alexandria" (noun) is real ground here, but "Alexandrian"
    # (adjective) is a different token content_words() does not equate
    # to it - engine.m4.named_claim_grounding's own module docstring
    # names this exact class of gap (Smyrna/Smyrnaeans) as an accepted
    # limit; this module inherits it unchanged via the shared function.
    sentence = "No Alexandrian bishop is named attending any synod our own people convened."
    flags = find_unsupported_named_claims(
        [{"sentence": sentence, "tags": []}], repository_records=_DERIVATIONAL_REPOSITORY
    )
    assert flags and flags[0]["missing"] == ["alexandrian"]


_ABSENCE_PHRASING_REPOSITORY = {
    "ijc.core.ijc": {
        "id": "ijc.core.ijc",
        "record_type": "core",
        "text": "Our authority contests reached us through Rome and its own bishops, not through any other see's whole life.",
    },
}


def test_honest_limit_phrase_not_in_the_reused_fixed_list_is_a_known_gap():
    # "Our record doesn't mention 'Alexandrian Christianity' as a
    # separate tradition from our own" genuinely denies knowledge of a
    # neighbour, but _is_honest_limit's fixed phrase list (engine.m4.
    # uncited_claims, reused unchanged here) requires an exact "our
    # record does not"/"not in our record" match, which "doesn't
    # mention" is close to but does not satisfy - a narrow gap in that
    # reused vocabulary's own coverage, not a judgment call this module
    # makes on its own.
    sentence = "Our record doesn't mention \"Alexandrian Christianity\" as a separate tradition from our own."
    flags = find_unsupported_named_claims(
        [{"sentence": sentence, "tags": []}], repository_records=_ABSENCE_PHRASING_REPOSITORY
    )
    assert flags and flags[0]["missing"] == ["alexandrian"]
