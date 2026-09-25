from engine.m4.named_claim_grounding import (
    find_named_claim_flags,
    ungrounded_markers,
    verdict_for_sentence,
)

# The real pahc records OG-9's own regression traces
# (worlds/pahc/Open_Gaps_Tracking.md, entry OG-9), copied verbatim from
# records/pahc/story/pahc.story.one-eucharist-under-bishop.md and
# records/pahc/source/pahc.source.ignatius-letters.md - not a synthetic
# paraphrase, so this pins the actual fleet record this defect was found
# on, same discipline engine.m4.tests.test_uncited_claims's own
# _REAL_CHURCH_FAILURE_TEXT/_REAL_REPOSITORY already use. Hermetic: no
# compiled package on disk, this dict is the whole "repository" a call
# needs.
_STORY_TEXT = (
    "This is how it would have been, in a community formed under Ignatius's own "
    "instruction. 'Take ye heed, then, to have but one Eucharist,' he writes. "
    "'For there is one flesh of our Lord Jesus Christ, and one cup to [show "
    "forth] the unity of His blood; one altar; as there is one bishop, along with "
    "the presbytery and deacons.' Whatever the bishop approves, he insists "
    "elsewhere, is pleasing to God. No one should do anything pertaining to the "
    "church without the bishop. 'Let that be deemed a proper Eucharist, which is "
    "administered either by the bishop, or by one to whom he has entrusted it.' "
    "Wherever the bishop appears, he writes, let the people be there also - 'even "
    "as, wherever Jesus Christ is, there is the Catholic Church.' It is not "
    "lawful, apart from the bishop, either to baptize or to hold a love-feast. A "
    "member formed this way would refuse, on Ignatius's own instruction, to "
    "attend any gathering that broke bread apart from this single, "
    "bishop-anchored table. The eucharist itself was inseparable from the "
    "question of who legitimately gathers the community at all."
)

# The real source row's own `work` field: an OMNIBUS covering all seven
# letters, the enumeration sitting in its own parenthetical apparatus -
# exactly the shape short_head() exists to drop, and exactly why this
# module resolves sources[] through short_head() rather than the raw
# field (see engine.m4.named_claim_grounding's own module docstring,
# GROUND SCOPE). Matching this string unTRUNCATED would let "Ephesians"
# ground itself off the very sentence OG-9 traced, since it is one of
# the seven letters this one omnibus row covers even though this
# story's own locus never cites it.
_SOURCE_WORK = (
    "The seven letters, middle recension (Ephesians, Magnesians, Trallians, "
    "Romans, Philadelphians, Smyrnaeans, To Polycarp); traditional dating c. "
    "107-117 CE, redated 130s-140s by Barnes and Foster, held pseudepigraphic "
    "c. 160-180 by Huebner and Lechner - a genuine three-way scholarly split"
)

_REAL_REPOSITORY = {
    "pahc.story.one-eucharist-under-bishop": {
        "id": "pahc.story.one-eucharist-under-bishop",
        "record_type": "story",
        "sources": [
            {
                "source_id": "pahc.source.ignatius-letters",
                "locus": "Philadelphians 4; Smyrnaeans 8",
                "license": "public-domain",
            }
        ],
        "text": _STORY_TEXT,
    },
    "pahc.source.ignatius-letters": {
        "id": "pahc.source.ignatius-letters",
        "record_type": "source",
        "work": _SOURCE_WORK,
    },
}

_STORY_TAG = "pahc.story.one-eucharist-under-bishop"


def test_og9_regression_ignatius_to_the_ephesians_is_flagged():
    # The exact traced fabrication (OG-9): the record's own locus is
    # "Philadelphians 4; Smyrnaeans 8" and its text never names a
    # letter - "Ephesians" appears nowhere in this record's own ground.
    # grounding_net's own ratio test passes this sentence (2 of 3
    # content words - "ignatius", "writes" - are grounded, clearing the
    # 40% floor); this is the check that must catch what that one can't.
    sentence = "Ignatius writes it to the Ephesians."
    missing = ungrounded_markers(sentence, [_STORY_TAG], repository_records=_REAL_REPOSITORY)
    assert missing == ["ephesians"]

    verdict = verdict_for_sentence(sentence, [_STORY_TAG], repository_records=_REAL_REPOSITORY)
    assert verdict["verdict"] == "flag"
    assert "ephesians" in verdict["missing"]


def test_og9_regression_caught_through_find_named_claim_flags_entry_point():
    # The same case through the real calling shape
    # (engine.m4.turn._run_ordinary_voice_turn's own net_result["sentences"]
    # entries) - verdict "ok" from grounding_net's own ratio test, WITH a
    # tag, exactly the shape that reached a participant live.
    sentences = [
        {"sentence": "Ignatius writes it to the Ephesians.", "tags": [_STORY_TAG], "verdict": "ok", "why": "grounded 67% in own tagged records"}
    ]
    flags = find_named_claim_flags(sentences, repository_records=_REAL_REPOSITORY)
    assert len(flags) == 1
    assert flags[0]["class"] == "named_claim_not_grounded"
    assert flags[0]["missing"] == ["ephesians"]


def test_real_locus_names_philadelphians_and_smyrnaeans_never_flag():
    # The record's own real letters, correctly named - must never flag,
    # the false-positive case a too-broad check would cost a genuinely
    # correct citation. Both come from the record's own locus string
    # (engine.prose.all_text already walks sources[].locus).
    for sentence in (
        "Ignatius writes this to the Philadelphians.",
        "Ignatius writes this to the Smyrnaeans.",
    ):
        assert ungrounded_markers(sentence, [_STORY_TAG], repository_records=_REAL_REPOSITORY) == []


def test_source_work_omnibus_enumeration_does_not_leak_through_short_head():
    # Direct proof of the GROUND SCOPE decision: every OTHER letter this
    # one omnibus source row's own `work` field enumerates - the exact
    # words a naive, untruncated match against `work` would have wrongly
    # grounded - must still be caught. Magnesians/Trallians/Romans/"To
    # Polycarp" are all real words in that field, none of them cited by
    # this record's own locus.
    for wrong_letter in ("Magnesians", "Trallians", "Romans"):
        sentence = f"Ignatius writes this to the {wrong_letter}."
        assert ungrounded_markers(sentence, [_STORY_TAG], repository_records=_REAL_REPOSITORY) == [wrong_letter.lower()]


def test_locus_digit_grounds_a_correctly_numbered_chapter():
    # The locus "Philadelphians 4; Smyrnaeans 8" carries two real chapter
    # numbers - content_words() strips digits entirely (engine.prose._WORD
    # only matches letters), so this exercises the separate digit-ground
    # path (engine.m4.named_claim_grounding._source_ground/_number_tokens),
    # not the word-ground path the proper-noun tests above already cover.
    sentence = "Ignatius makes this argument in Philadelphians, chapter 4."
    assert ungrounded_markers(sentence, [_STORY_TAG], repository_records=_REAL_REPOSITORY) == []


def test_wrong_chapter_number_is_flagged():
    sentence = "Ignatius makes this argument in Philadelphians, chapter 9."
    assert ungrounded_markers(sentence, [_STORY_TAG], repository_records=_REAL_REPOSITORY) == ["9"]


def test_untagged_sentence_is_never_checked_here():
    # This module narrows an already-tagged, already-passing sentence's
    # own claim - it does not decide whether a sentence should have been
    # tagged at all (grounding_net/uncited_claims's own job).
    assert ungrounded_markers("Ignatius writes it to the Ephesians.", [], repository_records=_REAL_REPOSITORY) == []


def test_unresolvable_tag_contributes_no_ground_but_does_not_crash():
    # grounding_net.verdict_for_sentence already withholds a sentence
    # tagged to an unresolvable id before this check would ever see it
    # live - this only confirms the function itself is defensive, not
    # that this is a live-reachable path.
    assert ungrounded_markers("Ignatius writes it to the Ephesians.", ["pahc.story.does-not-exist"], repository_records=_REAL_REPOSITORY) == []


def test_sentence_with_no_checkable_marker_is_never_flagged():
    assert ungrounded_markers("The bishop led the community's own worship.", [_STORY_TAG], repository_records=_REAL_REPOSITORY) == []


def test_find_named_claim_flags_skips_withheld_sentences():
    # A sentence grounding_net already withheld never reaches a
    # participant - auditing it a second time here adds no
    # participant-facing signal, so find_named_claim_flags (unlike
    # ungrounded_markers itself) only examines verdict == "ok" sentences.
    sentences = [
        {"sentence": "Ignatius writes it to the Ephesians.", "tags": [_STORY_TAG], "verdict": "withhold", "why": "some other reason"}
    ]
    assert find_named_claim_flags(sentences, repository_records=_REAL_REPOSITORY) == []


def test_find_named_claim_flags_skips_untagged_sentences():
    sentences = [{"sentence": "Ignatius writes it to the Ephesians.", "tags": [], "verdict": "ok", "why": None}]
    assert find_named_claim_flags(sentences, repository_records=_REAL_REPOSITORY) == []


def test_find_named_claim_flags_empty_on_a_clean_turn():
    sentences = [
        {"sentence": "Ignatius writes this to the Philadelphians.", "tags": [_STORY_TAG], "verdict": "ok", "why": "grounded"},
        {"sentence": "The bishop led the community's own worship.", "tags": [_STORY_TAG], "verdict": "ok", "why": "grounded"},
    ]
    assert find_named_claim_flags(sentences, repository_records=_REAL_REPOSITORY) == []
