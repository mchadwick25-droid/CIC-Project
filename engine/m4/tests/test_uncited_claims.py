"""Pins R27's own two motivating sentences (Decision-Log.md Entry 50/51,
2026-09-22) as real, real-world-shaped regression cases, plus the
verified finding that claim_markers alone would miss one of them."""
from engine.m4.grounding_net import check_turn, check_turn_with_paragraph_coverage
from engine.m4.uncited_claims import (
    build_uncited_claims_event,
    classify_neighbour_named,
    classify_other_tradition_turn,
    find_uncited_claims,
    find_uncited_paragraphs,
    known_tradition_names,
    match_named_tradition,
    world_records_mention_tradition,
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


# R27-A item 1 (Entry 55/PR #421): the upgrade now also requires the
# sentence to be a real paragraph-level failure (failing_paragraph_
# sentences) - not just "the turn was routed via other_tradition" alone,
# per PR #420's own live finding that the unconditional upgrade fired
# 24/24 and would fail nearly every other_tradition turn.
def test_classify_other_tradition_turn_upgrades_when_the_turn_was_routed_there_and_the_sentence_is_a_paragraph_failure():
    offense = {"sentence": "Even a broken priest could not block his grace.", "class": "uncited_claim"}
    upgraded = classify_other_tradition_turn(
        offense,
        is_other_tradition_turn=True,
        failing_paragraph_sentences={"Even a broken priest could not block his grace."},
    )
    assert upgraded["class"] == "own_doctrine_in_other_tradition_turn"


def test_classify_other_tradition_turn_leaves_ordinary_turns_alone():
    offense = {"sentence": "Even a broken priest could not block his grace.", "class": "uncited_claim"}
    upgraded = classify_other_tradition_turn(
        offense,
        is_other_tradition_turn=False,
        failing_paragraph_sentences={"Even a broken priest could not block his grace."},
    )
    assert upgraded["class"] == "uncited_claim"


def test_classify_other_tradition_turn_leaves_a_paragraph_grounded_frame_sentence_alone():
    # Routed via other_tradition, but this exact sentence is NOT in
    # failing_paragraph_sentences (its own paragraph is grounded) - the
    # narrowing this test pins.
    offense = {"sentence": "Even a broken priest could not block his grace.", "class": "uncited_claim"}
    upgraded = classify_other_tradition_turn(offense, is_other_tradition_turn=True, failing_paragraph_sentences=set())
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
        "alx": {
            "kind": "formation", "card_name": "Alexandrian Christianity", "display_name": "Alexandrian Christianity",
            "world_id": "alexandria-catechetical", "representative": {"name": "Theon"},
        },
        "don": {
            "kind": "formation", "card_name": "The Church of the Martyrs", "display_name": "Donatism",
            "world_id": "donatism", "representative": {"name": "Nundinarius"},
        },
        "fix": {"kind": "fixture", "card_name": "Fixture World", "representative": {"name": "Nobody"}},
    }


def test_known_tradition_names_excludes_the_speaking_world_and_fixtures():
    names = known_tradition_names(_registry(), exclude_world_key="alx")
    assert "Alexandrian Christianity" not in names
    assert "Theon" not in names
    assert "The Church of the Martyrs" in names
    assert "Nundinarius" in names
    assert "Fixture World" not in names  # kind != "formation"


# F5 (reviewer thread fix list, 2026-09-22, after PR #419's own re-run):
# a real gap the run itself surfaced - the battery's own probe named "the
# Donatists" (a demonym, what a voice's own prose actually says), never
# don's own card_name "The Church of the Martyrs", so
# classify_neighbour_named had nothing to match. Pinned to the fix list's
# own two named examples.
def test_known_tradition_names_includes_display_name_and_world_id():
    names = known_tradition_names(_registry(), exclude_world_key="alx")
    assert "Donatism" in names
    assert "donatism" in [n.lower() for n in names]  # world_id, hyphens read as spaces (single word here, unchanged)


def test_known_tradition_names_derives_the_ism_demonym():
    names = [n.lower() for n in known_tradition_names(_registry(), exclude_world_key="alx")]
    assert "donatist" in names
    assert "donatists" in names


def test_known_tradition_names_derives_the_ian_demonym():
    names = [n.lower() for n in known_tradition_names(_registry(), exclude_world_key="don")]
    assert "alexandria" in names


def test_classify_neighbour_named_upgrades_on_a_demonym_not_a_card_name():
    offense = {"sentence": "What did the Donatists believe about that?", "class": "uncited_claim"}
    names = known_tradition_names(_registry(), exclude_world_key="alx")
    upgraded = classify_neighbour_named(offense, names)
    assert upgraded["class"] == "neighbour_named"


def test_build_uncited_claims_event_returns_none_when_clean():
    voice_event = {"speaker": "alx", "uncited_claims": []}
    assert build_uncited_claims_event(voice_event, registry=_registry(), is_other_tradition_turn=False) is None


def test_build_uncited_claims_event_refines_both_classes():
    # own_doctrine_in_other_tradition_turn now requires the sentence to
    # also be a real paragraph-level failure (R27-A item 1) - the fixture
    # below puts "Even a broken priest..." in paragraph_offenses so the
    # upgrade still fires.
    voice_event = {
        "speaker": "alx",
        "uncited_claims": [
            {"sentence": "The Church of the Martyrs split over the treatment of traditores.", "class": "uncited_claim"},
            {"sentence": "Even a broken priest could not block his grace.", "class": "uncited_claim"},
        ],
        "paragraph_offenses": [
            {"sentence": "Even a broken priest could not block his grace.", "class": "wholly_uncited_paragraph"},
        ],
    }
    event = build_uncited_claims_event(voice_event, registry=_registry(), is_other_tradition_turn=True)
    assert event["speaker"] == "alx"
    classes = {o["class"] for o in event["offenses"]}
    assert "neighbour_named" in classes
    assert "own_doctrine_in_other_tradition_turn" in classes
    assert event["paragraph_offenses"] == voice_event["paragraph_offenses"]


def test_build_uncited_claims_event_returns_none_when_both_lists_are_empty():
    voice_event = {"speaker": "alx", "uncited_claims": [], "paragraph_offenses": []}
    assert build_uncited_claims_event(voice_event, registry=_registry(), is_other_tradition_turn=False) is None


def test_build_uncited_claims_event_fires_on_paragraph_offenses_alone():
    # A turn with no sentence-level offenses at all, but a real paragraph-
    # level one, still needs an event - build_uncited_claims_event's own
    # docstring: "None only when BOTH are empty."
    voice_event = {
        "speaker": "alx",
        "uncited_claims": [],
        "paragraph_offenses": [{"sentence": "A whole narrative paragraph with no citation anywhere in it.", "class": "wholly_uncited_paragraph"}],
    }
    event = build_uncited_claims_event(voice_event, registry=_registry(), is_other_tradition_turn=False)
    assert event is not None
    assert event["offenses"] == []
    assert len(event["paragraph_offenses"]) == 1


# R27-A item 2 (Entry 55): find_uncited_paragraphs's own baseline cases -
# built from check_turn_with_paragraph_coverage's real output, not a
# hand-built paragraph_check dict, so these exercise the real join
# between grounding_net's paragraph_coverage and this module's own
# reduction, the same end-to-end discipline the real-Dionysius tests
# above already use for the sentence-level check.
def test_find_uncited_paragraphs_a_wholly_uncited_narrative_paragraph_fails():
    # "Even a broken priest could not block his grace." carries no proper
    # noun/number (claim_markers finds nothing), so real check_turn gives
    # it verdict "ok" with no tag - exactly the gap R27's own module
    # docstring names (claim_markers alone misses it). No citation
    # anywhere in its own (single-sentence) paragraph, so it's a real
    # wholly_uncited_paragraph failure.
    tagged = "Even a broken priest could not block his grace."
    result = check_turn_with_paragraph_coverage(tagged, _REAL_REPOSITORY)
    offenses = find_uncited_paragraphs(result)
    assert len(offenses) == 1
    assert offenses[0]["class"] == "wholly_uncited_paragraph"


def test_find_uncited_paragraphs_a_properly_cited_paragraph_passes():
    tagged = "The tradition that won here brought the repentant back in, even at the deathbed, and Dionysius defended doing so [[alx.dw.church-failure]]."
    result = check_turn_with_paragraph_coverage(tagged, _REAL_REPOSITORY)
    assert find_uncited_paragraphs(result) == []


def test_find_uncited_paragraphs_an_honest_limit_only_paragraph_passes():
    tagged = "Our record doesn't mention that Christian tradition."
    result = check_turn_with_paragraph_coverage(tagged, _REAL_REPOSITORY)
    assert find_uncited_paragraphs(result) == []


def test_find_uncited_paragraphs_a_one_sentence_paragraph_inherits_the_preceding_cited_paragraph():
    tagged = (
        "The tradition that won here brought the repentant back in, even at the deathbed, and "
        "Dionysius defended doing so [[alx.dw.church-failure]].\n\n"
        "That, too, is in our record."
    )
    result = check_turn_with_paragraph_coverage(tagged, _REAL_REPOSITORY)
    coverage = result["paragraph_coverage"]
    assert len(coverage) == 2
    assert coverage[1]["inherited_from_preceding"] is True
    # Whatever the net's own verdict on the inherited check, it must never
    # be reported as wholly_uncited_paragraph - it has a cited_record_ids
    # set (inherited), so the wholly_uncited branch never applies to it.
    assert all(o["sentence"] != "That, too, is in our record." or o["class"] != "wholly_uncited_paragraph" for o in find_uncited_paragraphs(result))


# R27-A item 3 (Decision-Log.md Entry 55's own "Pinned for item 3's own
# tests" section, 2026-09-23) - the two cases the reviewer named directly,
# real sentences, not invented ones.
def test_r27a_narrowed_rule_still_catches_both_augustinian_sentences_as_real_paragraph_failures():
    # R26's own motivating pair (Entry 50/51): "What the sacrament does,
    # it does by Christ's power, not the minister's purity." and "Even a
    # broken priest could not block his grace." - genuinely unsupported
    # by anything in alx's own records, real doctrine belonging to a
    # different world. Entry 55: "the narrowed rule must still fail
    # both." This is classify_other_tradition_turn's own narrowing logic
    # in isolation (hand-built offenses, the same discipline the other
    # classify_other_tradition_turn tests above already use) - both
    # sentences marked as real paragraph-level failures
    # (failing_paragraph_sentences), both upgraded. (The two sentences
    # together do not both survive as verdict "ok" through the real
    # check_turn pipeline in one turn - "Christ's" alone trips
    # claim_markers and withholds the first sentence upstream, the same
    # fallback-ladder split test_real_dionysius_deathbed_sentence_
    # uncited_is_withheld_upstream_not_reported_by_this_module already
    # documents - so this pins the classification rule itself, which is
    # what Entry 55 is actually specifying.)
    sentence_a = "What the sacrament does, it does by Christ's power, not the minister's purity."
    sentence_b = "Even a broken priest could not block his grace."
    failing_paragraph_sentences = {sentence_a, sentence_b}
    offenses = [{"sentence": sentence_a, "class": "uncited_claim"}, {"sentence": sentence_b, "class": "uncited_claim"}]
    refined = [
        classify_other_tradition_turn(o, is_other_tradition_turn=True, failing_paragraph_sentences=failing_paragraph_sentences)
        for o in offenses
    ]
    assert all(o["class"] == "own_doctrine_in_other_tradition_turn" for o in refined)


# alx's own conflict-turn shape (PR #420's own live report: a frame
# sentence, "For years they held together.", riding inside a paragraph
# the report already shows fully cited - uncited_in_cited_paragraph: 7).
# Hermetic fixture, same discipline _REAL_CHURCH_FAILURE_TEXT above
# already uses (real record content, no live package) - a record whose
# own text shares real ground with the frame sentence, so the inherited
# check has something genuine to find, not a rigged pass.
_HELD_TOGETHER_REPOSITORY = {
    "alx.dw.donatist-schism": {
        "id": "alx.dw.donatist-schism",
        "record_type": "doctrinal_witness",
        "text": (
            "The two communities argued for years before the final break came, "
            "but for years they held together despite the strain between them."
        ),
    }
}


def test_r27a_narrowed_rule_passes_a_grounded_frame_sentence_inside_a_cited_other_tradition_paragraph():
    # is_other_tradition_turn=True is forced on this - the whole point of
    # Entry 55's own pinned case is to prove the NARROWED rule, not
    # merely R27-A's own base paragraph coverage, is what passes this
    # sentence: a frame sentence the paragraph's own citation genuinely
    # grounds is not own_doctrine_in_other_tradition_turn even inside an
    # other_tradition turn.
    tagged = (
        "The two sides argued for years before the break finally came [[alx.dw.donatist-schism]]. "
        "For years they held together."
    )
    result = check_turn_with_paragraph_coverage(tagged, _HELD_TOGETHER_REPOSITORY)
    paragraph_offenses = find_uncited_paragraphs(result)
    assert paragraph_offenses == []  # the paragraph is cited and the inherited check grounds it

    base_offenses = find_uncited_claims(result["sentences"])
    failing_paragraph_sentences = {o["sentence"] for o in paragraph_offenses}
    refined = [
        classify_other_tradition_turn(o, is_other_tradition_turn=True, failing_paragraph_sentences=failing_paragraph_sentences)
        for o in base_offenses
    ]
    assert all(o["class"] != "own_doctrine_in_other_tradition_turn" for o in refined)


# R36's own hand-sort finding (Decision-Log.md Entry 56, 2026-09-23): the
# inherited_ungrounded branch of find_uncited_paragraphs never applied the
# question/honest-limit/first-person exemptions its own wholly_uncited_
# paragraph branch already applies - catching R26's own fixed sentence and
# a literal question among the withheld inherited sentences #427's own live
# run surfaced. Fixed as part of item 5's own PR (a correctness fix to
# report-only logic, not a change to what enforcement covers - Rulings-
# Pending.md R36).
_INHERITED_EXEMPTION_REPOSITORY = {
    "x.rec": {"id": "x.rec", "record_type": "doctrinal_witness", "text": "The synod met and decided the matter after long debate."}
}


def test_find_uncited_paragraphs_never_counts_r26s_own_fixed_sentence_as_inherited_ungrounded():
    tagged = (
        "The synod met and decided the matter after long debate [[x.rec]]. "
        "Our record doesn't mention that Christian tradition."
    )
    result = check_turn_with_paragraph_coverage(tagged, _INHERITED_EXEMPTION_REPOSITORY)
    offenses = find_uncited_paragraphs(result)
    assert all(o["class"] != "inherited_ungrounded" for o in offenses)


def test_find_uncited_paragraphs_never_counts_a_literal_question_as_inherited_ungrounded():
    tagged = "The synod met and decided the matter after long debate [[x.rec]]. How did it end?"
    result = check_turn_with_paragraph_coverage(tagged, _INHERITED_EXEMPTION_REPOSITORY)
    offenses = find_uncited_paragraphs(result)
    assert all(o["class"] != "inherited_ungrounded" for o in offenses)


def test_find_uncited_paragraphs_never_counts_first_person_no_claim_as_inherited_ungrounded():
    tagged = "The synod met and decided the matter after long debate [[x.rec]]. I feel the weight of what you're asking."
    result = check_turn_with_paragraph_coverage(tagged, _INHERITED_EXEMPTION_REPOSITORY)
    offenses = find_uncited_paragraphs(result)
    assert all(o["class"] != "inherited_ungrounded" for o in offenses)


def test_find_uncited_paragraphs_still_catches_a_genuine_inherited_ungrounded_sentence():
    # The exemption fix must not swallow the real catch alongside the false
    # ones - a genuine unsupported claim inside a cited paragraph still
    # fails.
    tagged = "The synod met and decided the matter after long debate [[x.rec]]. Ursinus was exiled by imperial order."
    result = check_turn_with_paragraph_coverage(tagged, _INHERITED_EXEMPTION_REPOSITORY)
    offenses = find_uncited_paragraphs(result)
    assert any(o["class"] == "inherited_ungrounded" for o in offenses)


# R39's own reviewer-ordered fix (relayed 2026-09-23): the false fixed
# honest-limit sentence. match_named_tradition/world_records_mention_
# tradition are this fix's own detection half - engine.m4.turn's own
# _other_tradition_directive tests (test_turn.py) pin the participant-
# facing half.
def test_match_named_tradition_finds_the_demonym_not_just_the_card_name():
    # Same real gap F5 already found for classify_neighbour_named
    # (module docstring above): a probe names "the Donatists", never
    # don's own card_name "The Church of the Martyrs" - this function
    # must resolve the demonym back to don's own world_key regardless.
    assert match_named_tradition(
        "What was your relationship with the Donatists?", _registry(), exclude_world_key="alx"
    ) == "don"


def test_match_named_tradition_returns_none_for_a_non_fleet_name():
    # "The Arians" names no world in this fleet's own registry (Arianism
    # is not one of the 11 formation worlds) - the caller's own fallback
    # to the unconditional honest-limit sentence is correct here, since
    # there is no registry world to check a real mention against.
    assert match_named_tradition("What did the Arians believe?", _registry(), exclude_world_key="alx") is None


_DONATISM_MENTIONING_REPOSITORY = {
    "ijc.quote.compelled-to-come-in": {
        "id": "ijc.quote.compelled-to-come-in", "record_type": "quote",
        "text": (
            "Wherefore, if the power which the Church has received by divine appointment... it seemed to "
            "certain of the brethren, of whom I was one, that although the madness of the Donatists was..."
        ),
    },
    "ijc.dw.unrelated": {
        "id": "ijc.dw.unrelated", "record_type": "doctrinal_witness",
        "text": "The council met at Nicaea and confessed the faith the churches already worshipped.",
    },
}

_ALX_CHURCH_FAILURE_REPOSITORY = {
    "alx.dw.church-failure": {
        "id": "alx.dw.church-failure", "record_type": "doctrinal_witness",
        "text": "Under persecution, many gave way. Some sacrificed to the gods. When peace came, the community fought bitterly over them.",
    },
}


def test_world_records_mention_tradition_finds_a_real_reference():
    # Real-shaped, per the reviewer's own explicit ask: ijc's own records
    # genuinely name Donatism (ijc.quote.compelled-to-come-in) - the
    # excerpt is trimmed but the real record's own words, not invented.
    ids = world_records_mention_tradition(_DONATISM_MENTIONING_REPOSITORY, _registry()["don"])
    assert ids == ["ijc.quote.compelled-to-come-in"]


def test_world_records_mention_tradition_empty_when_the_world_never_mentions_it():
    # alx's own church-failure record - the R37/R38 worked example's own
    # ground - never names Donatism at all; the true "honest-limit stays
    # exactly as it is" case.
    ids = world_records_mention_tradition(_ALX_CHURCH_FAILURE_REPOSITORY, _registry()["don"])
    assert ids == []


def test_world_records_mention_tradition_ignores_a_locus_filename_coincidence():
    # The same false positive R37's own design brief already found and
    # fixed (Decision-Log.md Entry 57, PR #438): a vendored source
    # filename carrying an unrelated name as a substring is not real
    # prose. Only PROSE_KEYS fields are scanned, so a locus-only mention
    # must not count as evidence.
    repository = {
        "x.rec": {
            "id": "x.rec", "record_type": "doctrinal_witness",
            "text": "An ordinary sentence naming nobody in particular.",
            "sources": [{"source_id": "x.source.one", "locus": "anf-hermas-tatian-donatism-appendix.xml"}],
        }
    }
    assert world_records_mention_tradition(repository, _registry()["don"]) == []
