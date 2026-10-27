"""The 14 October retest, replayed offline: each case is a real turn from that
retest's live-turn reports, its draft rebuilt (engine.m4.tests.live11_replay)
and run back through the reply shaping a turn applies, with the world's own
records. No model call."""
from functools import lru_cache

import pytest

from engine.m1 import gates
from engine.m1.horizon import post_window_mentions
from engine.m1.loader import load_fleet_records, load_world_records
from engine.m1.registry import load_registry
from engine.m4 import evidence, grounding_net, turn_prep
from engine.m4.person_claims import find_person_claim_flags
from engine.m4.tests import live11_replay
from engine.shape import shape_text

RUN = "retest"


@lru_cache(maxsize=None)
def _turns():
    return {(t["world"], t["q"]): t for t in live11_replay.turns(RUN)}


@lru_cache(maxsize=None)
def _replayed(world, q):
    return live11_replay.replay(_turns()[(world, q)])


def _removed(world, q):
    return [(r["why"], r["sentence"]) for r in _replayed(world, q)["first_net"]["reply_shape"]["removed"]]


def _shown(world, q, sentence):
    return live11_replay._shown(sentence, _replayed(world, q)["text"])


# ---- 1. the world's own wording is not a quotation ------------------------


@pytest.mark.parametrize("world, q, sentence", [
    # indirect speech the cited witness itself tells ("Ignatius answered that
    # he was truly raised")
    ("pahc", 1, "And Ignatius said he was truly raised, the same way we ourselves will be raised, by the same Father."),
    # 'very God of very God' is ijc.dw.jesus's own wording
    ("ijc", 4, "The creed at Nicaea bound the Son to the Father as one being - homoousios - because 'very God of very "
               "God' was what the inheritance carried."),
    # word for word ijc.dw.room-for-hesitation
    ("ijc", 5, "He explained, carefully, why he had hesitated over its defining word and what he understood it to mean."),
    # a list after "taught," is not someone's words
    ("hal", 2, "The gospels we spent our lives translating and correcting told what he did: he taught, healed, "
               "called disciples, and went to the cross."),
    # its own records' telling, no one's words
    ("syr", 5, "What the record shows from his own years is that covenant daughters performed the madrashe he wrote, "
               "carrying theological argument in verse to the whole congregation."),
])
def test_wording_the_sentences_own_records_hold_is_shown(world, q, sentence):
    assert sentence not in [s for _why, s in _removed(world, q)]
    assert _shown(world, q, sentence)


@pytest.mark.parametrize("world, q, sentence", [
    # Moses' saying reworded: "the errors of another man", where
    # desert.story.moses-leaking-jug says "faults that are not mine"
    ("desert", 5, "He said: these are my sins, running out behind me, and I do not see them - yet I come today to "
                  "judge the errors of another man."),
    # the homoios phrases stand in ijc.term.homoios only inside its own
    # quotation marks, as the formulas' words
    ("ijc", 3, "The imperial church itself, under Constantius II and Valens, held that the Son is like the Father - "
               "homoios - as the scriptures say, and refused both \"of one substance\" and \"of a different "
               "substance\" as words scripture does not use."),
])
def test_wording_the_cited_record_does_not_hold_as_its_own_is_still_cut(world, q, sentence):
    assert sentence in [s for _why, s in _removed(world, q)]


MOSES = ["desert.story.moses-leaking-jug"]


@pytest.mark.parametrize("sentence", [
    # the independent review's cases: a lead-in from the story, then words it does not hold
    "Abba Moses got up and came, carrying a basket with a hole in it, filled with sand, and he said: brothers, "
    "forgive him seven times and give him bread.",
    "When they asked what it meant, Abba Moses said: these are my sins, running out behind me, and God will burn "
    "every judge who sits in this church.",
    # an address after "said," is his words, not a list
    "Abba Moses said, brothers, do not judge anyone, for God alone sees the heart.",
    "Abba Moses said, my children, and my brothers, never judge another monk.",
    # the review's recheck: one invented word turns the saying round
    "Abba Moses said: these are my sins, running out behind me, and I cannot see them, so hang him.",
    # a list of deeds does not hide a later "said:" from its subject
    "Abba Moses taught, judged, and said: these are my sins, so hang him.",
    "Abba Moses taught, judged, and said: forgive him seven times.",
])
def test_words_the_story_does_not_hold_are_cut_after_he_said(sentence):
    records = live11_replay.records("desert")
    entry = grounding_net.check_turn(sentence[:-1] + " [[desert.story.moses-leaking-jug]].", records)["sentences"][0]
    assert entry["verdict"] == "withhold" and entry["why"] in grounding_net.QUOTATION_DROP_REASONS


def test_the_saying_in_the_storys_own_words_stands():
    records = live11_replay.records("desert")
    entry = grounding_net.check_turn("When the others asked what it meant, he said: these are my sins, running out "
                                     "behind me, and I cannot see them [[desert.story.moses-leaking-jug]].", records)
    assert entry["sentences"][0]["verdict"] == "ok"


def test_a_sources_words_a_story_quotes_stay_the_sources():
    # lpc.story.the-plague-and-the-enemies quotes Pontius in its own marks
    records = load_world_records("lpc")
    entry = grounding_net.check_turn(
        "'All were shuddering, fleeing, shunning the contagion, impiously exposing their own friends' "
        "[[lpc.story.the-plague-and-the-enemies]].", records)["sentences"][0]
    assert (entry["verdict"], entry["why"]) == ("withhold", grounding_net.REASON_TYPED_QUOTATION)


def test_creed_clauses_no_ijc_record_holds_are_still_cut():
    # "under Pontius Pilate, was crucified, died" stand in no ijc record (the
    # 325 creed and ijc.dw.jesus do not have them), and "heaven" and "again"
    # only in the creed quote: words only a quote holds (decision 61, option A)
    assert (grounding_net.REASON_QUOTE_WORDS,
            "He came down from heaven, was made man, suffered under Pontius Pilate, was crucified, died, and rose "
            "again on the third day.") in _removed("ijc", 2)


def test_a_record_quoting_someone_does_not_explain_those_words():
    # A record's own wording leaves out what it sets in quotation marks:
    # those are someone else's words, not the world's telling.
    records = {
        "fix.force.f": {"id": "fix.force.f", "record_type": "force",
                        "description": "He wrote of 'the manifold and deplorable tempests of secular warfare' once."},
        "fix.quote.q": {"id": "fix.quote.q", "record_type": "quote", "speaker_or_author": "Vincent",
                        "modern_rendering": "I came from the manifold and deplorable tempests of secular warfare."},
    }
    index = grounding_net.QuotationIndex(records)
    sentence = "He came from the manifold and deplorable tempests of secular warfare."
    assert index.quote_words_of(sentence, ["fix.force.f"]) == "fix.quote.q"
    assert not index.own_telling(sentence, ["fix.force.f"])


# ---- 2. a typed quotation in a lead-in ------------------------------------


def test_a_lead_in_that_types_its_own_quotation_places_nothing():
    # syr Q4: the voice's rewording of the hymn in an unclosed mark, ahead of
    # the real quote
    removed = _removed("syr", 4)
    assert [why for why, s in removed if s.startswith('Ephrem sang: "This is the day')] == [
        grounding_net.REASON_LEAD_TYPES_QUOTATION]
    assert _replayed("syr", 4)["first_net"]["reply_shape"]["placed"] == []
    assert '"' not in _replayed("syr", 4)["text"]


def test_the_voice_is_told_not_to_say_the_quote_before_it_is_placed():
    assert "do not say first, in other words, what it is about to say" in turn_prep.QUOTE_SPEAKER_LINE


# ---- 3. the lead-in names the quote's speaker -----------------------------


@pytest.mark.parametrize("world, q, lead", [
    ("desert", 4, "It is Christ who works them, by means of those who believe in him."),  # Antony unnamed
    ("ijc", 3, "Eusebius of Caesarea, who was at the council, hesitated before he signed"),  # Socrates' words
])
def test_a_quote_whose_lead_in_does_not_name_its_speaker_is_not_placed(world, q, lead):
    assert (grounding_net.REASON_SPEAKER_UNNAMED, lead) in _removed(world, q)
    assert _replayed(world, q)["first_net"]["reply_shape"]["placed"] == []


@pytest.mark.parametrize("run", list(live11_replay.RUNS))
def test_every_quote_placed_in_the_replays_names_its_speaker(run):
    counts = live11_replay.summary(live11_replay.run_all(run), run)
    assert counts["placed_without_speaker_named"] == 0


# ---- 4. claims about a named person: a logged flag ------------------------


@pytest.mark.parametrize("world, q, flagged", [
    ("pahc", 2, "credited"),  # 1 Clement's chain credited to Justin
    ("ijc", 5, "reason"),     # an invented reason for Eusebius's signature
])
def test_the_person_claim_flag_finds_both_retest_faults(world, q, flagged):
    flags = find_person_claim_flags(_replayed(world, q)["net_result"]["sentences"],
                                    repository_records=live11_replay.records(world))
    assert flagged in {f["class"] for entry in flags for f in entry["flags"]}


def test_the_person_claim_flag_cuts_nothing():
    # Over every 13 and 14 October draft it also flags true claims, so it is
    # logged for review (engine.m7.offline_checks): pahc Q2's sentence is
    # still shown
    assert _shown("pahc", 2, "Justin said the apostles preached what they had received from the Lord, and appointed "
                             "others to carry it forward once they themselves were gone.")


def test_the_person_claim_flags_over_both_runs():
    flagged = live11_replay.person_claim_flags_over_runs()
    assert len(flagged) == 12
    assert {(f["run"], f["world"], f["q"]) for f in flagged} >= {("retest", "pahc", 2), ("retest", "ijc", 5)}


# ---- 5. the horizon gate reads the meaning the voice is offered -----------


def test_the_horizon_gate_reads_use_note_means():
    records = {
        "fix.story.s": {"id": "fix.story.s", "world_id": "fixture-world", "record_type": "story",
                        "tellable_as": "A story from our own years.",
                        "use_note": {"means": "This story first appears in a writer around 500."}},
    }
    registry = {"fix": {"world_id": "fixture-world", "time_window": {"start": 300, "end": 410}}}
    assert gates.gate_horizon(records, {}, registry) == [
        "fix.story.s.use_note.means: names the year 500, after the window closes in 410; "
        "rewrite it from inside the window, or mark the record voice: analytic"
    ]


@pytest.mark.parametrize("text, year", [
    ("compiled from civic archives about 540", 540),
    ("writing in Constantinople in the 440s", 440),
    ("Rabbula of Edessa (411-435) personally", 411),
    ("Theodoret, writing about 444-450, tells", 444),
])
def test_the_horizon_check_reads_about_ranges_and_decades(text, year):
    assert f"the year {year}" in post_window_mentions(text, 410)


def test_syr_has_no_post_window_year_left_in_what_its_voice_is_offered():
    findings = gates.gate_horizon(load_world_records("syr"), load_fleet_records(), load_registry())
    assert findings == []


# ---- 6. 'we', not 'I' -----------------------------------------------------


def test_the_pronoun_rule_answers_a_question_put_to_you_as_we():
    shape = shape_text()
    assert "The exception is that one naming sentence, not a license for 'I'." in shape
    assert "'what we would want you to understand', 'we believed it because'" in shape


# ---- 7. Q1 and Q2 reach their world's own evidence ------------------------


def _canon():
    return {r: v for r, v in load_fleet_records().items() if v.get("record_type") == "canon_question"}


def test_who_is_jesus_reaches_the_cells_that_ask_who_jesus_is():
    cells = evidence.match_asks_to_cells(message="Who is Jesus?", asks=None, canon_questions=_canon(),
                                         repository_records=live11_replay.records("pahc"))
    assert [c["cell"] for c in cells] == ["C-I", "C-P"]


@pytest.mark.parametrize("message", ["Who are you?", "Who won the game?", "Do you like pizza?", "What is that?"])
def test_a_question_word_alone_still_reaches_no_cell(message):
    assert evidence.match_asks_to_cells(message=message, asks=None, canon_questions=_canon(),
                                        repository_records=live11_replay.records("pahc")) == []


def test_what_did_he_do_after_who_is_jesus_carries_the_same_cells():
    history = [{"role": "user", "content": "Who is Jesus?"}, {"role": "assistant", "content": "..."}]
    canon = _canon()
    records = live11_replay.records("ijc")
    assert evidence._looks_like_follow_up("What did he do?", None, canon, records)
    cells = evidence.inherited_cells(history, canon_questions=canon, repository_records=records, top_n=2)
    assert [c["cell"] for c in cells] == ["C-I", "C-P"]


# ---- 8. small records ------------------------------------------------------


@pytest.mark.parametrize("text", ["about 500 monks", "around 150 bishops", "Psalms (119-120)", "lines (1954-1958)"])
def test_a_counted_number_or_a_reference_is_not_a_year(text):
    assert post_window_mentions(text, 410) == []


def test_alx_offers_the_bee_teacher_as_unnamed_by_clement_and_named_by_eusebius():
    means = load_world_records("alx")["alx.quote.clement-bee"]["use_note"]["means"]
    assert "whom he does not name here and Eusebius names as Pantaenus" in means


def test_desert_apophthegma_guard_carries_no_modern_word_the_voice_can_echo():
    note = load_world_records("desert")["desert.term.apophthegma"]["use_note"]
    assert not [line for line in note["not_for"] if "soundbite" in line]


# ---- the regression replay over all 42 retest drafts ------------------------


def test_every_rebuilt_retest_draft_puts_every_recorded_sentence_back():
    for (world, q), turn in _turns().items():
        draft = live11_replay.rebuild_draft(turn["voice_event"], live11_replay.CUT_PLACED_AFTER.get((RUN, world, q)))
        for entry in turn["voice_event"]["grounding"]["sentences"] + turn["voice_event"]["reply_shape"]["removed"]:
            assert grounding_net.strip_tags(entry["draft"]).strip()[:40] in grounding_net.strip_tags(draft), (world, q)


def test_the_replay_over_all_42_retest_drafts():
    counts = live11_replay.summary(live11_replay.run_all(RUN), RUN)
    assert counts["turns"] == 42
    # recorded on 14 October: 20 cuts, 8 overcuts, 10 placed, 2 unnamed;
    # 18 by the net, 1 more that leaned on a cited sentence it removed
    assert counts["cuts"] == 19
    # still cut: ijc Q2's creed clauses, ijc Q3's homoios phrases and desert
    # Q5's reworded saying, which the records they cite do not hold as theirs
    assert counts["overcuts_still_cut"] == 3
    assert counts["placed_quotes"] == 7 and counts["placed_without_speaker_named"] == 0
    assert counts["degraded_sent"] == 0 and counts["stray_punctuation_sentences"] == 0
