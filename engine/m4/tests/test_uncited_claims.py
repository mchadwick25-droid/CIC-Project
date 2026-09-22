"""Pins R27's own two motivating sentences (Decision-Log.md Entry 50/51,
2026-09-22) as real, real-world-shaped regression cases, plus the
verified finding that claim_markers alone would miss one of them."""
from engine.m4.grounding_net import check_turn
from engine.m4.uncited_claims import (
    build_uncited_claims_event,
    classify_neighbour_named,
    classify_other_tradition_turn,
    find_uncited_claims,
    known_tradition_names,
)


def sent(text: str, tags: list[str] | None = None, verdict: str = "ok") -> dict:
    return {"sentence": text, "tags": tags or [], "verdict": verdict, "why": None}


def test_catches_the_uncited_donatist_history_sentence():
    sentences = [sent("The Donatists split from the wider church over the treatment of traditores after the persecution.")]
    offenses = find_uncited_claims(sentences)
    assert len(offenses) == 1
    assert offenses[0]["class"] == "uncited_claim"


def test_catches_both_r26_augustinian_sacramental_sentences():
    # engine.prose.claim_markers on its own MISSES the second of these
    # two sentences outright (Decision-Log.md Entry 51's own verified
    # finding) - this test pins that find_uncited_claims still catches
    # it, confirming the module does not silently rely on claim_markers
    # as its gate.
    sentences = [
        sent("What the sacrament does, it does by Christ's power, not the minister's purity."),
        sent("Even a broken priest could not block his grace."),
    ]
    offenses = find_uncited_claims(sentences)
    assert len(offenses) == 2
    assert all(o["class"] == "uncited_claim" for o in offenses)


def test_a_cited_sentence_never_flags():
    sentences = [sent("We watched them turn back toward God.", tags=["alx.story.baptism-watch"])]
    assert find_uncited_claims(sentences) == []


def test_a_withheld_sentence_is_never_checked():
    # It never reaches the participant (apply_net drops it) - nothing to
    # check in a sentence that was never shown.
    sentences = [sent("An unsupported invented claim.", verdict="withhold")]
    assert find_uncited_claims(sentences) == []


def test_a_question_back_to_the_participant_is_allowed_uncited():
    sentences = [sent("What draws you to ask about the Donatists?")]
    assert find_uncited_claims(sentences) == []


def test_r26_own_honest_limit_sentence_is_allowed_uncited():
    sentences = [sent("Our record doesn't mention that Christian tradition.")]
    assert find_uncited_claims(sentences) == []


def test_existing_fleet_honest_limit_scaffolding_is_allowed_uncited():
    # engine.prose.SCAFFOLD_MARKERS, already fleet-calibrated -
    # reused directly, not a new keyword guess.
    sentences = [
        sent("We do not have anything more to tell you about that."),
        sent("We will not draw one for you where the record leaves none."),
        sent("We find none of these in what survives to us."),
    ]
    assert find_uncited_claims(sentences) == []


def test_first_person_framing_with_no_claim_is_allowed_uncited():
    sentences = [sent("I feel the weight of what you're asking.")]
    assert find_uncited_claims(sentences) == []


def test_first_person_framing_that_still_makes_a_claim_is_not_exempt():
    # Starts with "I", but names a real figure - still a checkable claim.
    sentences = [sent("I studied under Origen himself.")]
    offenses = find_uncited_claims(sentences)
    assert len(offenses) == 1


# F1 (reviewer thread fix list, 2026-09-22): the fleet's own real honest-
# limit forms, taken verbatim from the item-4 live battery's own offense
# list (live-uncited-claims-battery-report.json) - the exact sentences the
# raw check wrongly caught before this fix.
def test_fix_list_f1_record_absence_forms_are_allowed_uncited():
    sentences = [
        sent("How it ended among us is not in our record."),
        sent("Here is the honest limit."),
        sent("No rule of ours survives that explains the difference."),
    ]
    assert find_uncited_claims(sentences) == []


def test_fix_list_f1_a_genuine_survives_claim_with_no_negation_is_not_exempt():
    # The negation-proximity guard's own negative control: "survives" alone,
    # with no negator, is a real citable claim, not a record-absence form.
    sentences = [sent("The letter survives in three copies.")]
    offenses = find_uncited_claims(sentences)
    assert len(offenses) == 1


# F2 (same fix list): a conditional offer whose MAIN clause is first-
# person, not its opener - the opener-only check missed this exact battery
# sentence.
def test_fix_list_f2_conditional_first_person_offer_is_allowed_uncited():
    sentences = [
        sent("If you name the conflict you mean, I will tell you plainly where our own record speaks to it and where it does not.")
    ]
    assert find_uncited_claims(sentences) == []


def test_fix_list_f2_a_first_person_clause_that_still_makes_a_claim_is_not_exempt():
    sentences = [sent("If you ask, we can tell you Origen taught this in the year 240.")]
    offenses = find_uncited_claims(sentences)
    assert len(offenses) == 1


def test_classify_neighbour_named_upgrades_when_a_known_tradition_is_named():
    offense = {"sentence": "The Donatists refused to accept bishops who had handed over Scriptures.", "class": "uncited_claim"}
    upgraded = classify_neighbour_named(offense, known_tradition_names=["The Church of the Martyrs", "Donatists"])
    assert upgraded["class"] == "neighbour_named"


def test_classify_neighbour_named_leaves_unrelated_offenses_alone():
    offense = {"sentence": "The sacrament works by Christ's own power.", "class": "uncited_claim"}
    upgraded = classify_neighbour_named(offense, known_tradition_names=["The Church of the Martyrs", "Donatists"])
    assert upgraded["class"] == "uncited_claim"


def test_classify_other_tradition_turn_upgrades_when_the_turn_was_routed_there():
    offense = {"sentence": "Even a broken priest could not block his grace.", "class": "uncited_claim"}
    upgraded = classify_other_tradition_turn(offense, is_other_tradition_turn=True)
    assert upgraded["class"] == "own_doctrine_in_other_tradition_turn"


def test_classify_other_tradition_turn_leaves_ordinary_turns_alone():
    offense = {"sentence": "Even a broken priest could not block his grace.", "class": "uncited_claim"}
    upgraded = classify_other_tradition_turn(offense, is_other_tradition_turn=False)
    assert upgraded["class"] == "uncited_claim"


# R27 build item 3's own must-pass case, named directly by the reviewer
# thread's build order: "Dionysius deathbed sentence (alx.dw.church-
# failure)" - real record text (records/alx/doctrinal_witness/alx.dw.
# church-failure.md), not a synthetic paraphrase, so this pins the actual
# fleet language rather than a stand-in for it. Same hermetic-fixture
# discipline as engine.m4.tests.test_grounding_net's own REPOSITORY -
# built from the real record's own text, not tied to a compiled package
# path, so this runs with no package on disk.
_REAL_CHURCH_FAILURE_TEXT = (
    "Your churches had failures too - what did you do with them? Our "
    "record leaves the wounds visible. Our greatest teacher was driven out, not "
    "by pagans, but by his own bishop. The church remembered both men rather than "
    "erasing either. Under persecution, many gave way. Some sacrificed to the "
    "gods. When peace came, the community fought "
    "bitterly over them. The strict party demanded they stay out. The tradition "
    "that won here brought the repentant back in, even at the deathbed, and "
    "Dionysius defended doing so. After Nicaea, the church itself learned to use "
    "exile and condemnation, and some of what was done with that power our own "
    "sources report without pride. At our best, we refused the two easy "
    "exits: we did not pretend the failure away, and we did not make the failed "
    "unforgivable. At our worst, we did what churches with power do. That, too, "
    "is in our record."
)
_REAL_REPOSITORY = {
    "alx.dw.church-failure": {
        "id": "alx.dw.church-failure",
        "record_type": "doctrinal_witness",
        "text": _REAL_CHURCH_FAILURE_TEXT,
    }
}


def test_real_dionysius_deathbed_sentence_properly_cited_never_flags():
    # End-to-end through the real check_turn pipeline, not a hand-built
    # sent() dict: confirms the real sentence both survives grounding_net
    # (verdict "ok", not withheld) AND is never flagged as uncited when
    # tagged to its own real record - the must-pass case a false positive
    # here would cost a genuinely well-cited answer.
    sentence = (
        "The tradition that won here brought the repentant back in, even at the deathbed, and "
        "Dionysius defended doing so"
    )
    tagged = f"{sentence} [[alx.dw.church-failure]]."
    result = check_turn(tagged, _REAL_REPOSITORY)
    assert result["sentences"][0]["verdict"] == "ok"
    assert find_uncited_claims(result["sentences"]) == []


def test_real_dionysius_deathbed_sentence_uncited_is_withheld_upstream_not_reported_by_this_module():
    # The same real sentence, uncited: grounding_net withholds it before
    # find_uncited_claims ever runs (a specific claim naming Dionysius,
    # no citation tag) - it never reaches the participant, so this module
    # correctly reports nothing on it. R27's own check is scoped to
    # verdict == "ok" sentences by design (module docstring); this test
    # pins that the two modules' fallback ladders don't double-report the
    # same real defect shape.
    sentence = (
        "The tradition that won here brought the repentant back in, even at the deathbed, and "
        "Dionysius defended doing so."
    )
    result = check_turn(sentence, _REAL_REPOSITORY)
    assert result["sentences"][0]["verdict"] == "withhold"
    assert find_uncited_claims(result["sentences"]) == []


def test_a_facilitator_turn_is_never_checked_by_this_module():
    # Facilitator turns are code-owned templates, never model-generated
    # (engine.m4.facilitator_turns's own module docstring) - the caller
    # never calls find_uncited_claims on one, so there is no dedicated
    # branch here; this test documents that fact rather than exercising
    # a code path, since the module takes grounding_net's own sentence
    # list, which a facilitator_turn never produces in the first place.
    assert find_uncited_claims([]) == []


def _registry():
    return {
        "alx": {"kind": "formation", "card_name": "Alexandrian Christianity", "representative": {"name": "Theon"}},
        "don": {"kind": "formation", "card_name": "The Church of the Martyrs", "representative": {"name": "Nundinarius"}},
        "fix": {"kind": "fixture", "card_name": "Fixture World", "representative": {"name": "Nobody"}},
    }


def test_known_tradition_names_excludes_the_speaking_world_and_fixtures():
    names = known_tradition_names(_registry(), exclude_world_key="alx")
    assert "Alexandrian Christianity" not in names
    assert "Theon" not in names
    assert "The Church of the Martyrs" in names
    assert "Nundinarius" in names
    assert "Fixture World" not in names  # kind != "formation"


def test_build_uncited_claims_event_returns_none_when_clean():
    voice_event = {"speaker": "alx", "uncited_claims": []}
    assert build_uncited_claims_event(voice_event, registry=_registry(), is_other_tradition_turn=False) is None


def test_build_uncited_claims_event_refines_both_classes():
    voice_event = {
        "speaker": "alx",
        "uncited_claims": [
            {"sentence": "The Church of the Martyrs split over the treatment of traditores.", "class": "uncited_claim"},
            {"sentence": "Even a broken priest could not block his grace.", "class": "uncited_claim"},
        ],
    }
    event = build_uncited_claims_event(voice_event, registry=_registry(), is_other_tradition_turn=True)
    assert event["speaker"] == "alx"
    classes = {o["class"] for o in event["offenses"]}
    assert "neighbour_named" in classes
    assert "own_doctrine_in_other_tradition_turn" in classes
