"""Pins R27's own two motivating sentences (Decision-Log.md Entry 50/51,
2026-09-22) as real, real-world-shaped regression cases, plus the
verified finding that claim_markers alone would miss one of them."""
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
