"""The conversation's rhythm (decision 60): a quote about every third round,
a new figure at most every third round, the world's own words for what it
held, and a quote or story already used referred back to rather than repeated.
Everything here reads the transcript only; nothing is stored."""
import pytest

from engine.m4 import turn_prep
from engine.m4.evidence import QUESTION_KINDS, assemble_evidence, render_evidence_block
from engine.m4.rhythm import RhythmTally, asks_for_the_words, tally_from_transcript
from engine.m4.turn_prep import (
    LEXICON_LINE,
    NO_NEW_FIGURE_LINE,
    QUOTE_LINE,
    REFER_BACK_LINE,
    prepare_voice_turn_inputs,
)
from engine.m4.world_loader import LoadedWorld
from engine.m5.routing import Directive

CANON = {
    "fleet.canon.q1": {
        "id": "fleet.canon.q1", "record_type": "canon_question", "cell": "C-E",
        "text": "What did your community remember about Jesus at the meal?",
    },
}
MESSAGE = "What did your community remember about Jesus at the meal?"
FIGURES = [
    {"id": "fix.figure.ignatius", "names": [{"name": "Ignatius"}]},
    {"id": "fix.figure.polycarp", "names": [{"name": "Polycarp"}]},
]


def _record(rid, record_type, text, **extra):
    body = {"text": text, "modern_rendering": text} if record_type == "quote" else {"tellable_as": text} if record_type == "story" else {"text": text}
    return {"id": rid, "record_type": record_type, "canon_cells": ["C-E"], "sources": [{"source_id": f"fix.source.{rid}"}], **body, **extra}


def _records():
    records = [
        _record("fix.witness.w", "doctrinal_witness", "The community kept the memory of Jesus at the meal."),
        _record("fix.quote.a", "quote", "The community kept the memory of Jesus at the meal, whole.", speaker_or_author="Ignatius"),
        _record("fix.quote.b", "quote", "The meal held the memory of Jesus for the community.", speaker_or_author="Polycarp"),
        _record("fix.quote.c", "quote", "At the meal the community remembered Jesus together.", speaker_or_author="Anon"),
        _record("fix.story.s", "story", "The community told how Jesus broke bread at the meal."),
    ]
    return {r["id"]: r for r in records}


def _coverage():
    return {"C-E": {
        "doctrinal_witness": ["fix.witness.w"], "terms": [], "stories": ["fix.story.s"],
        "quotes": ["fix.quote.a", "fix.quote.b", "fix.quote.c"], "honest_limit": [],
        "gravities": [], "forces": [], "contested_claims": [],
    }}


def _world():
    records = list(_records().values())
    return LoadedWorld(
        world_key="fix", manifest_hash="sha256:test", prompt_text="## Identity\nVera.", capsule_text="capsule",
        repository={"records": records}, quotes={"quotes": []}, figures={"figures": FIGURES}, coverage=_coverage(),
        frame={"representative": {"name": "Vera", "role_label": "Witness"}},
    )


@pytest.fixture(autouse=True)
def _canon(monkeypatch):
    monkeypatch.setattr(turn_prep, "load_fleet_records", lambda: CANON)


def _participant():
    return {"speaker": "participant", "text": "A question."}


def _voice(*, quotes=(), stories=(), figures=()):
    elements = [{"record_id": r, "kind": "quote"} for r in quotes] + [{"record_id": r, "kind": "story"} for r in stories]
    return {
        "speaker": "fix", "text": "A reply.", "citations": [], "glosses": [],
        "figures_used": [{"id": f} for f in figures], "transparency": {"elements": elements},
    }


def _transcript(*rounds):
    """One (participant, voice) pair per round."""
    out = []
    for voice in rounds:
        out += [_participant(), voice]
    return out


def _prepare(transcript, *, kind="who", message=MESSAGE):
    return prepare_voice_turn_inputs(
        world=_world(), participant_message=message,
        directive=Directive(asks=[{"order": 1, "text": message}], kind=kind),
        rhythm=tally_from_transcript(transcript),
    )


def _quotes(prepared):
    return [c for c in prepared_candidates(prepared) if c["record_type"] == "quote"]


def prepared_candidates(prepared):
    block = prepared.user_message
    return [
        {"id": line.split("[[")[1].split("]]")[0], "record_type": line.split("]] ")[1].split(",")[0].split(" ")[0], "line": line}
        for line in block.splitlines() if line.startswith("- [[")
    ]


def _tag(how, round_no):
    return f"{how} in round {round_no}"


def _fresh_quotes(prepared):
    return [c for c in _quotes(prepared) if " in round " not in c["line"]]


# ---- the tally ----------------------------------------------------------


def test_the_tally_counts_rounds_and_reads_marked_quotes_stories_and_figures():
    transcript = _transcript(_voice(quotes=["q1"], figures=["f1"]), _voice(stories=["s1"]), _voice())
    tally = tally_from_transcript(transcript)
    assert tally.round_no == 4
    assert tally.quotes_voiced == {"q1": 1}
    assert tally.stories_told == {"s1": 2}
    assert tally.figures_introduced == {"f1": 1}


def test_a_record_cited_without_a_mark_is_not_voiced():
    entry = _voice()
    entry["citations"] = [{"record_ids": ["fix.quote.a"]}]
    assert tally_from_transcript(_transcript(entry)).quotes_voiced == {}


def test_the_table_tally_counts_its_own_seat_and_a_round_already_holding_its_question():
    other = {**_voice(quotes=["x"]), "speaker": "other"}
    transcript = [_participant(), _voice(quotes=["q1"]), other, _participant()]
    tally = tally_from_transcript(transcript, speaker="fix", question_recorded=True)
    assert tally.round_no == 2
    assert tally.quotes_voiced == {"q1": 1}


def test_an_old_transcript_without_a_transparency_plan_tallies_nothing():
    entry = {**_voice(), "transparency": None}
    assert tally_from_transcript(_transcript(entry)).quotes_voiced == {}


# ---- quote cadence ------------------------------------------------------


def test_a_quote_voiced_one_round_ago_drops_the_quote_line_and_the_floor_to_one():
    prepared = _prepare(_transcript(_voice(quotes=["fix.quote.a"])))
    assert QUOTE_LINE not in prepared.turn_directive
    assert len(_fresh_quotes(prepared)) == 1


def test_a_quote_voiced_three_rounds_ago_brings_the_line_and_the_normal_floor_back():
    prepared = _prepare(_transcript(_voice(quotes=["fix.quote.a"]), _voice(), _voice()))
    assert QUOTE_LINE in prepared.turn_directive
    assert len(_fresh_quotes(prepared)) == 2


def test_two_rounds_ago_is_still_too_soon():
    prepared = _prepare(_transcript(_voice(quotes=["fix.quote.a"]), _voice()))
    assert QUOTE_LINE not in prepared.turn_directive


def test_a_first_turn_asks_for_a_quote():
    prepared = _prepare([])
    assert QUOTE_LINE in prepared.turn_directive
    assert len(_fresh_quotes(prepared)) == 2


@pytest.mark.parametrize("message", ["What did your community say about Jesus at the meal?", "How did your community put it, the memory of Jesus at the meal?", "In their own words, what did your community remember about Jesus at the meal?"])
def test_a_question_that_asks_for_the_words_turns_the_line_on_whatever_the_count(message):
    prepared = _prepare(_transcript(_voice(quotes=["fix.quote.a"])), kind="what_did", message=message)
    assert QUOTE_LINE in prepared.turn_directive
    assert len(_fresh_quotes(prepared)) == 2


def test_asking_for_the_words_depends_on_the_kind():
    assert asks_for_the_words("what_did", "What did he say?")
    assert asks_for_the_words("what_happened", "Tell me, word for word, what happened.")
    assert asks_for_the_words("what_means", "How was the word used?")
    assert not asks_for_the_words("what_means", "What does the word mean?")
    assert not asks_for_the_words("who", "What did he say?")
    assert not asks_for_the_words("what_did", "What did he do?")


def test_a_voiced_quote_never_fills_the_floor_of_a_later_turn():
    prepared = _prepare(_transcript(_voice(quotes=["fix.quote.a"]), _voice(), _voice()))
    assert "fix.quote.a" not in [c["id"] for c in _fresh_quotes(prepared)]
    assert len(_fresh_quotes(prepared)) == 2


# ---- figure cadence -----------------------------------------------------


def test_a_figure_introduced_last_round_closes_the_gate_and_the_floor_is_zero():
    tally = tally_from_transcript(_transcript(_voice(figures=["fix.figure.ignatius"])))
    assert tally.figure_gate_closed
    prepared = _prepare(_transcript(_voice(figures=["fix.figure.ignatius"])))
    assert NO_NEW_FIGURE_LINE in prepared.turn_directive


def test_three_rounds_on_the_gate_opens_again():
    tally = tally_from_transcript(_transcript(_voice(figures=["fix.figure.ignatius"]), _voice(), _voice()))
    assert not tally.figure_gate_closed
    assert NO_NEW_FIGURE_LINE not in _prepare(_transcript(_voice(figures=["fix.figure.ignatius"]), _voice(), _voice())).turn_directive


def test_a_figure_already_introduced_is_met_freely_and_never_triggers_the_gate():
    tally = tally_from_transcript(_transcript(_voice(figures=["fix.figure.ignatius"]), _voice(), _voice(), _voice()))
    assert not tally.figure_gate_closed


def test_the_figure_gate_changes_no_evidence():
    gated = tally_from_transcript(_transcript(_voice(figures=["fix.figure.polycarp"])))
    open_ = tally_from_transcript([])
    assert gated.figure_gate_closed and not open_.figure_gate_closed
    args = dict(message=MESSAGE, asks=None, canon_questions=CANON, coverage=_coverage(), repository_records=_records(), kind="who")
    assert assemble_evidence(**args, rhythm=gated)["candidates"] == assemble_evidence(**args, rhythm=RhythmTally(round_no=gated.round_no))["candidates"]


def test_the_figure_the_question_asks_about_is_not_held_back_by_the_gate():
    transcript = _transcript(_voice(figures=["fix.figure.polycarp"]))
    prepared = _prepare(transcript, message="What did Ignatius say about the meal and the memory of Jesus?", kind="what_did")
    assert NO_NEW_FIGURE_LINE not in prepared.turn_directive


# ---- the lexicon line ---------------------------------------------------


@pytest.mark.parametrize("kind", QUESTION_KINDS)
def test_the_lexicon_line_is_present_for_every_kind(kind):
    assert LEXICON_LINE == "Use the world's own words for what it held."
    assert LEXICON_LINE in _prepare([], kind=kind).turn_directive
    assert LEXICON_LINE in _prepare(_transcript(_voice(quotes=["fix.quote.a"])), kind=kind).turn_directive


# ---- referring back -----------------------------------------------------


def test_a_quote_voiced_in_round_one_and_a_story_told_in_round_two_are_still_listed_at_round_four():
    transcript = _transcript(_voice(quotes=["fix.quote.a"]), _voice(stories=["fix.story.s"]), _voice())
    prepared = _prepare(transcript, kind="what_did")
    lines = {c["id"]: c["line"] for c in prepared_candidates(prepared)}
    assert _tag("voiced", 1) in lines["fix.quote.a"]
    assert _tag("told", 2) in lines["fix.story.s"]
    assert REFER_BACK_LINE in prepared.turn_directive
    assert QUOTE_LINE in prepared.turn_directive
    assert "fix.quote.a" not in [c["id"] for c in _fresh_quotes(prepared)]
    assert len(_fresh_quotes(prepared)) == 2


def test_the_refer_back_line_is_absent_when_nothing_used_is_in_the_block():
    assert REFER_BACK_LINE not in _prepare([]).turn_directive


def test_a_used_quote_is_tagged_in_the_rendered_block():
    tally = RhythmTally(round_no=3, quotes_voiced={"fix.quote.a": 1})
    result = assemble_evidence(
        message=MESSAGE, asks=None, canon_questions=CANON, coverage=_coverage(), repository_records=_records(),
        kind="who", rhythm=tally,
    )
    assert _tag("voiced", 1) in render_evidence_block(result)


# ---- nothing stored -----------------------------------------------------


def test_the_tally_adds_no_field_to_the_session_state():
    from engine.m4.projection import SessionState

    assert not [name for name in SessionState.__dataclass_fields__ if any(w in name for w in ("rhythm", "voiced", "tally", "figures_introduced"))]
