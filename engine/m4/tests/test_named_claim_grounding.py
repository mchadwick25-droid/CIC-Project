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


# Possessive normalization: engine.prose._WORD keeps the apostrophe as
# part of a word, so "ignatius's" and "ignatius" never compared equal
# before this fix. Both directions are hermetic, synthetic fixtures
# (not the OG-9 record) so each isolates exactly one side of the
# comparison - "Ignatius" sits mid-sentence in every case below, never
# at position 0, since engine.prose._proper_nouns excludes a sentence's
# own first word from proper-noun detection.
_POSSESSIVE_IN_SENTENCE_REPOSITORY = {
    "pahc.dw.test-ignatius-plain": {
        "id": "pahc.dw.test-ignatius-plain",
        "record_type": "doctrinal_witness",
        "text": "Ignatius taught that the bishop must be obeyed by every member.",
    },
}


def test_possessive_in_sentence_bare_name_in_ground_grounds():
    # Reproduces the reported false positive: the sentence uses the
    # possessive ("Ignatius's"), the record's own ground names the bare
    # form ("Ignatius") - must ground, not flag.
    sentence = "This is why Ignatius's own teaching on obedience mattered so much."
    assert ungrounded_markers(
        sentence, ["pahc.dw.test-ignatius-plain"], repository_records=_POSSESSIVE_IN_SENTENCE_REPOSITORY
    ) == []


_POSSESSIVE_IN_GROUND_REPOSITORY = {
    "pahc.dw.test-ignatius-possessive": {
        "id": "pahc.dw.test-ignatius-possessive",
        "record_type": "doctrinal_witness",
        "text": "Ignatius's own letters describe this practice directly, across several churches.",
    },
}


def test_bare_name_in_sentence_possessive_in_ground_grounds():
    # The reverse direction: the sentence names the bare form, the
    # record's own ground only ever uses the possessive.
    sentence = "The letters, Ignatius wrote, describe one eucharist under the bishop."
    assert ungrounded_markers(
        sentence, ["pahc.dw.test-ignatius-possessive"], repository_records=_POSSESSIVE_IN_GROUND_REPOSITORY
    ) == []


_DERIVATIONAL_FORM_REPOSITORY = {
    "pahc.dw.test-smyrnaeans-only": {
        "id": "pahc.dw.test-smyrnaeans-only",
        "record_type": "doctrinal_witness",
        "text": "Ignatius also wrote a letter addressed to the Smyrnaeans.",
    },
}


def test_derivational_form_stays_an_accepted_known_limit():
    # "Smyrna" (the place) and "Smyrnaeans" (its people, the letter's
    # own addressees) are different derivational forms of the same
    # name - the possessive fix above does not attempt this, and this
    # test documents that it still doesn't: report-only noise, not a
    # regression.
    sentence = "Ignatius also wrote a letter to Smyrna."
    assert ungrounded_markers(
        sentence, ["pahc.dw.test-smyrnaeans-only"], repository_records=_DERIVATIONAL_FORM_REPOSITORY
    ) == ["smyrna"]


_ALEXANDRIA_NOUN_REPOSITORY = {
    "pahc.dw.test-alexandria-noun": {
        "id": "pahc.dw.test-alexandria-noun",
        "record_type": "doctrinal_witness",
        "text": "Athanasius returned to Alexandria after the council closed.",
    },
}

_ALEXANDRIA_ADJECTIVE_REPOSITORY = {
    "pahc.dw.test-alexandria-adjective": {
        "id": "pahc.dw.test-alexandria-adjective",
        "record_type": "doctrinal_witness",
        "text": "An Alexandrian delegation carried the letter home.",
    },
}


def test_alexandria_alexandrian_stays_an_accepted_known_limit():
    # A derivational bridge for exactly this pair (a place name ending
    # in "a" against its own bare-"n" adjective) was tried and removed:
    # the same surface shape also covers real, unrelated people
    # (Julian/Julia and the other pairs the tests below pin), and no
    # world's own compiled repository carries place records to gate a
    # bridge on safely. Alexandria/Alexandrian must flag each way, the
    # same accepted, unfixed status Smyrna/Smyrnaeans already has - this
    # test is the regression guard against the bridge quietly coming
    # back without a real place-based design.
    assert ungrounded_markers(
        "An Alexandrian bishop signed the letter.",
        ["pahc.dw.test-alexandria-noun"],
        repository_records=_ALEXANDRIA_NOUN_REPOSITORY,
    ) == ["alexandrian"]
    assert ungrounded_markers(
        "Athanasius returned home to Alexandria.",
        ["pahc.dw.test-alexandria-adjective"],
        repository_records=_ALEXANDRIA_ADJECTIVE_REPOSITORY,
    ) == ["alexandria"]


def test_two_different_names_never_ground_each_other():
    # No derivational bridge exists at all - an unrelated name flags
    # exactly as any other absent name would, even one that happens to
    # end in "a" the same way a real bridged pair once did.
    sentence = "Our own bishop wrote to Antioch and to Persia about the dispute."
    assert ungrounded_markers(
        sentence, ["pahc.dw.test-smyrnaeans-only"], repository_records=_DERIVATIONAL_FORM_REPOSITORY
    ) == ["antioch", "persia"]


_NUMBER_DIGIT_REPOSITORY = {
    "ijc.dw.test-number-digit": {
        "id": "ijc.dw.test-number-digit",
        "record_type": "doctrinal_witness",
        "text": "Ammianus counted 137 dead in the square that day.",
    },
}

_NUMBER_SPELLED_REPOSITORY = {
    "ijc.dw.test-number-spelled": {
        "id": "ijc.dw.test-number-spelled",
        "record_type": "doctrinal_witness",
        "text": "Ammianus counted one hundred thirty-seven dead in the square that day.",
    },
}


def test_number_grounds_each_way_across_digit_and_spelled_form():
    assert ungrounded_markers(
        "Ammianus says one hundred thirty-seven people died there.",
        ["ijc.dw.test-number-digit"],
        repository_records=_NUMBER_DIGIT_REPOSITORY,
    ) == []
    assert ungrounded_markers(
        "Ammianus says 137 people died there.",
        ["ijc.dw.test-number-spelled"],
        repository_records=_NUMBER_SPELLED_REPOSITORY,
    ) == []


def test_number_cross_form_check_does_not_manufacture_ground():
    # A genuinely different, unsupported number still flags after the
    # cross-form check - it does not start matching every number.
    assert ungrounded_markers(
        "Ammianus says 200 people died there.",
        ["ijc.dw.test-number-digit"],
        repository_records=_NUMBER_DIGIT_REPOSITORY,
    ) == ["200"]


# A real bug an earlier version of the cross-form check had: comparing a
# BAG of a number's own component words against ground, rather than its
# composed value, let an unrelated number ground a completely different
# one whenever their spelled-out forms happened to share a word - "100"
# matched a ground stating "three hundred eighteen" (shared "hundred"),
# "137" matched "seven hundred thirty" (shared "hundred" and "seven"),
# and "seven" matched a bare digit "27" (spelled "twenty-seven", sharing
# "seven"). `_numbers_in_text` parses each side to its own exact integer
# value and compares those, so none of these three should ever ground
# each other again.

_UNRELATED_SPELLED_NUMBER_REPOSITORY = {
    "wit.dw.test-three-eighteen": {
        "id": "wit.dw.test-three-eighteen",
        "record_type": "doctrinal_witness",
        "text": "The council seated three hundred eighteen bishops that year.",
    },
}


def test_digit_100_does_not_ground_against_an_unrelated_three_hundred_eighteen():
    assert ungrounded_markers(
        "Our own record counts 100 bishops present.",
        ["wit.dw.test-three-eighteen"],
        repository_records=_UNRELATED_SPELLED_NUMBER_REPOSITORY,
    ) == ["100"]


_UNRELATED_SPELLED_NUMBER_REPOSITORY_2 = {
    "wit.dw.test-seven-thirty": {
        "id": "wit.dw.test-seven-thirty",
        "record_type": "doctrinal_witness",
        "text": "The garrison held seven hundred thirty men at the wall.",
    },
}


def test_digit_137_does_not_ground_against_an_unrelated_seven_hundred_thirty():
    assert ungrounded_markers(
        "Ammianus says 137 people died there.",
        ["wit.dw.test-seven-thirty"],
        repository_records=_UNRELATED_SPELLED_NUMBER_REPOSITORY_2,
    ) == ["137"]


_UNRELATED_DIGIT_27_REPOSITORY = {
    "wit.dw.test-digit-27": {
        "id": "wit.dw.test-digit-27",
        "record_type": "doctrinal_witness",
        "text": "The council met for 27 days before it closed.",
    },
}


def test_spelled_seven_does_not_ground_against_an_unrelated_digit_27():
    assert ungrounded_markers(
        "Our record names seven bishops present at the council.",
        ["wit.dw.test-digit-27"],
        repository_records=_UNRELATED_DIGIT_27_REPOSITORY,
    ) == ["seven"]


# _parse_cardinal's own grammar: "and" joins a hundred/thousand block to
# its own remainder, and two complete numbers sitting next to each other
# with nothing joining them are never summed into one.

_HUNDRED_AND_37_REPOSITORY = {
    "wit.dw.test-hundred-and-37": {
        "id": "wit.dw.test-hundred-and-37",
        "record_type": "doctrinal_witness",
        "text": "Ammianus counted one hundred and thirty-seven dead in the square that day.",
    },
}


def test_and_joins_a_hundred_block_to_its_remainder():
    assert ungrounded_markers(
        "Ammianus says 137 people died there.",
        ["wit.dw.test-hundred-and-37"],
        repository_records=_HUNDRED_AND_37_REPOSITORY,
    ) == []
    assert ungrounded_markers(
        "The garrison held three hundred and eighteen men at the wall.",
        ["wit.dw.test-hundred-and-37"],
        repository_records=_HUNDRED_AND_37_REPOSITORY,
    ) == ["three hundred and eighteen"]


_GROUND_HOLDS_37_REPOSITORY = {
    "wit.dw.test-ground-holds-37": {
        "id": "wit.dw.test-ground-holds-37",
        "record_type": "doctrinal_witness",
        "text": "Thirty-seven bishops signed the letter that year.",
    },
}


def test_ground_containing_37_does_not_ground_one_hundred_and_thirty_seven():
    # 37 and 137 are different values - "and" must not let a hundred
    # block's own remainder alone stand in for the whole number.
    assert ungrounded_markers(
        "Ammianus says one hundred and thirty-seven people died there.",
        ["wit.dw.test-ground-holds-37"],
        repository_records=_GROUND_HOLDS_37_REPOSITORY,
    ) == ["one hundred and thirty seven"]


_FIFTEEN_AND_TWENTYSEVEN_REPOSITORY = {
    "wit.dw.test-fifteen-27": {
        "id": "wit.dw.test-fifteen-27",
        "record_type": "doctrinal_witness",
        "text": "Fifteen bishops signed first; twenty-seven more signed later.",
    },
}


def test_adjacent_number_words_are_not_summed_into_one_value():
    # "fifteen twenty-seven" must not parse as 15+20+7=42 (a value
    # neither number in the text) - each complete number is its own
    # value, and a ground holding 15 and 27 separately grounds both.
    assert ungrounded_markers(
        "Our own record lists fifteen twenty-seven as the counts that year.",
        ["wit.dw.test-fifteen-27"],
        repository_records=_FIFTEEN_AND_TWENTYSEVEN_REPOSITORY,
    ) == []
    # A ground that does NOT hold 42 must not ground a sentence naming 42
    # outright - the summed value is still absent.
    assert ungrounded_markers(
        "Our own record says 42 bishops signed that year.",
        ["wit.dw.test-fifteen-27"],
        repository_records=_FIFTEEN_AND_TWENTYSEVEN_REPOSITORY,
    ) == ["42"]


_EMPTY_NUMBER_GROUND_REPOSITORY = {
    "wit.dw.test-empty-numbers": {
        "id": "wit.dw.test-empty-numbers",
        "record_type": "doctrinal_witness",
        "text": "Our own record names no bishops and counts nothing here.",
    },
}


def test_two_three_is_two_separate_values_not_five():
    assert ungrounded_markers(
        "Our own record says two three separately, not one combined count.",
        ["wit.dw.test-empty-numbers"],
        repository_records=_EMPTY_NUMBER_GROUND_REPOSITORY,
    ) == ["three", "two"]


# No derivational bridge exists (removed, not narrowed further - see
# module docstring): every one of these pairs shares the same "-a"/
# bare-"n" surface shape a bridge once covered, and every one is a real
# person, not a place - "Julian" is properly derived from "Julius," not
# "Julia," and the two only collide on spelling. A figure-lexicon gate
# was tried first and still let every one of these through (none of
# these names happened to be a figure record in the worlds actually
# measured) - the regression guard here is the plain absence of any
# bridge at all, not a gate that depends on what a given world's own
# figure records happen to contain.

_JULIA_REPOSITORY = {
    "wit.dw.test-julia": {
        "id": "wit.dw.test-julia",
        "record_type": "doctrinal_witness",
        "text": "Julia herself never wrote to the council on this question.",
    },
}


def test_julian_does_not_ground_against_julia():
    assert ungrounded_markers(
        "The Julian reform of the calendar is not our own record's concern.",
        ["wit.dw.test-julia"],
        repository_records=_JULIA_REPOSITORY,
    ) == ["julian"]


_HADRIA_REPOSITORY = {
    "wit.dw.test-hadria": {
        "id": "wit.dw.test-hadria",
        "record_type": "doctrinal_witness",
        "text": "Hadria taught the household in secret for a generation.",
    },
}


def test_hadrian_does_not_ground_against_hadria():
    assert ungrounded_markers(
        "The Hadrianic peace changed little for our own community.",
        ["wit.dw.test-hadria"],
        repository_records=_HADRIA_REPOSITORY,
    ) == ["hadrianic"]


_LUCIA_REPOSITORY = {
    "wit.dw.test-lucia": {
        "id": "wit.dw.test-lucia",
        "record_type": "doctrinal_witness",
        "text": "Lucia kept the household faith alive after the edict.",
    },
}


def test_lucian_does_not_ground_against_lucia():
    assert ungrounded_markers(
        "Our own record never names Lucian at all.",
        ["wit.dw.test-lucia"],
        repository_records=_LUCIA_REPOSITORY,
    ) == ["lucian"]


_DOMITIA_REPOSITORY = {
    "wit.dw.test-domitia": {
        "id": "wit.dw.test-domitia",
        "record_type": "doctrinal_witness",
        "text": "Domitia's own household sheltered several believers.",
    },
}


def test_domitian_does_not_ground_against_domitia():
    assert ungrounded_markers(
        "The Domitianic persecution is not described in our own record.",
        ["wit.dw.test-domitia"],
        repository_records=_DOMITIA_REPOSITORY,
    ) == ["domitianic"]


_SEBASTIA_REPOSITORY = {
    "wit.dw.test-sebastia": {
        "id": "wit.dw.test-sebastia",
        "record_type": "doctrinal_witness",
        "text": "Sebastia is not named anywhere in our own account.",
    },
}


def test_sebastian_does_not_ground_against_sebastia():
    assert ungrounded_markers(
        "Our own record never mentions Sebastian's martyrdom at all.",
        ["wit.dw.test-sebastia"],
        repository_records=_SEBASTIA_REPOSITORY,
    ) == ["sebastian"]


_FLAVIA_REPOSITORY = {
    "wit.dw.test-flavia": {
        "id": "wit.dw.test-flavia",
        "record_type": "doctrinal_witness",
        "text": "Flavia gave the ground on which the community met.",
    },
}


def test_flavian_does_not_ground_against_flavia():
    assert ungrounded_markers(
        "The Flavian dynasty is not discussed in our own record.",
        ["wit.dw.test-flavia"],
        repository_records=_FLAVIA_REPOSITORY,
    ) == ["flavian"]


_CLAUDIA_REPOSITORY = {
    "wit.dw.test-claudia": {
        "id": "wit.dw.test-claudia",
        "record_type": "doctrinal_witness",
        "text": "Claudia is mentioned once, in passing, in our own greetings.",
    },
}


def test_claudian_does_not_ground_against_claudia():
    assert ungrounded_markers(
        "The Claudian aqueduct is not named anywhere in our own record.",
        ["wit.dw.test-claudia"],
        repository_records=_CLAUDIA_REPOSITORY,
    ) == ["claudian"]


# Regression coverage: these pairs never fit the narrow "-a"/"-an" shape
# the removed bridge covered, so removing it changes nothing for them.

_ROME_ROMANIA_REPOSITORY = {
    "wit.dw.test-rome": {
        "id": "wit.dw.test-rome",
        "record_type": "doctrinal_witness",
        "text": "Our own bishop wrote to Rome about the dispute.",
    },
}


def test_rome_does_not_ground_romania():
    assert ungrounded_markers(
        "Our own record says nothing at all about Romania.",
        ["wit.dw.test-rome"],
        repository_records=_ROME_ROMANIA_REPOSITORY,
    ) == ["romania"]


_ARIUS_REPOSITORY = {
    "wit.dw.test-arius": {
        "id": "wit.dw.test-arius",
        "record_type": "doctrinal_witness",
        "text": "Arius himself never recanted before the council closed.",
    },
}


def test_arius_does_not_ground_arian():
    assert ungrounded_markers(
        "The Arian controversy shaped a generation of bishops.",
        ["wit.dw.test-arius"],
        repository_records=_ARIUS_REPOSITORY,
    ) == ["arian"]


_GAUL_REPOSITORY = {
    "wit.dw.test-gaul": {
        "id": "wit.dw.test-gaul",
        "record_type": "doctrinal_witness",
        "text": "Bishops from Gaul attended the same council.",
    },
}


def test_gaul_does_not_ground_gaulish():
    assert ungrounded_markers(
        "Our own record never names any Gaulish custom at all.",
        ["wit.dw.test-gaul"],
        repository_records=_GAUL_REPOSITORY,
    ) == ["gaulish"]


_NICAEA_REPOSITORY = {
    "wit.dw.test-nicaea": {
        "id": "wit.dw.test-nicaea",
        "record_type": "doctrinal_witness",
        "text": "Nicaea settled the question for our own community.",
    },
}


def test_nicaea_does_not_ground_nicene():
    assert ungrounded_markers(
        "The Nicene formula is not quoted anywhere in our own record.",
        ["wit.dw.test-nicaea"],
        repository_records=_NICAEA_REPOSITORY,
    ) == ["nicene"]
