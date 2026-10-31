"""Routing by sub-question: the reader names one, the offer takes its records first."""
import yaml

from engine.m4 import subquestion_routing as sr
from engine.m4.evidence import assemble_evidence
from engine.m4.tests.test_evidence import CANON_QUESTIONS, COVERAGE, REPOSITORY
from engine.m5 import live_calls
from engine.m5.routing import assemble_directive

SIDECAR = {
    "world": "fix",
    "subquestions": {
        "C1.S1": {"cluster": "C1", "label": "Who Jesus was to them", "records": ["fix.term.baptisma", "fix.limit.jesus"]},
        "C1.S2": {"cluster": "C1", "label": "Was he God", "records": []},
    },
}


def test_catalogue_lists_every_sub_question_with_its_label():
    assert sr.reader_catalogue(SIDECAR) == "C1.S1 Who Jesus was to them\nC1.S2 Was he God"


def test_parse_sub_question_keeps_only_a_catalogue_id():
    assert sr.parse_sub_question({"sub_question": " C1.S1 "}, SIDECAR) == "C1.S1"
    assert sr.parse_sub_question({"sub_question": "C9.S9"}, SIDECAR) is None
    assert sr.parse_sub_question({"sub_question": "none"}, SIDECAR) is None
    assert sr.parse_sub_question({}, SIDECAR) is None
    assert sr.parse_sub_question(None, SIDECAR) is None


def test_coverage_entries_are_shaped_like_compiled_coverage_and_skip_empty_sub_questions():
    entries = sr.coverage_entries(SIDECAR, REPOSITORY)
    assert entries == {"C1.S1": {"terms": ["fix.term.baptisma"], "honest_limit": ["fix.limit.jesus"]}}


def _offer(sub_question):
    coverage = {**COVERAGE, **sr.coverage_entries(SIDECAR, REPOSITORY)}
    return assemble_evidence(
        message="What does your community remember of Jesus?", asks=None, canon_questions=CANON_QUESTIONS,
        coverage=coverage, repository_records=REPOSITORY, sub_question=sub_question,
    )


def test_the_sub_question_cell_comes_first_and_its_records_are_offered():
    result = _offer("C1.S1")
    assert result["cells"][0] == {"cell": "C1.S1", "score": 1.0, "from_sub_question": True}
    assert "fix.term.baptisma" in [c["id"] for c in result["candidates"]]
    assert {c["cell"] for c in result["candidates"] if c["id"] in ("fix.term.baptisma", "fix.limit.jesus")} == {"C1.S1"}


def test_the_word_matched_cells_stay_in_the_offer():
    assert {c["id"] for c in _offer(None)["candidates"]} <= {c["id"] for c in _offer("C1.S1")["candidates"]}


def test_no_sub_question_or_one_without_records_leaves_the_offer_unchanged():
    base = _offer(None)
    assert _offer("C1.S2") == base
    assert _offer("C7.S7") == base


def test_a_sub_question_alone_is_a_match_so_the_full_text_fallback_does_not_run():
    coverage = {**COVERAGE, **sr.coverage_entries(SIDECAR, REPOSITORY)}
    result = assemble_evidence(
        message="What is the weather like today?", asks=None, canon_questions=CANON_QUESTIONS,
        coverage=coverage, repository_records=REPOSITORY, sub_question="C1.S1",
    )
    assert not any(c.get("fulltext_fallback") for c in result["candidates"])
    assert "fix.term.baptisma" in [c["id"] for c in result["candidates"]]


def test_the_reader_prompt_and_tool_carry_the_catalogue_only_when_asked():
    system, tool = live_calls.reader_with_sub_questions(sr.reader_catalogue(SIDECAR))
    assert system.startswith(live_calls.READER_SYSTEM_PROMPT) and "C1.S1 Who Jesus was to them" in system
    assert "sub_question" in tool["input_schema"]["properties"] and "sub_question" not in tool["input_schema"]["required"]
    assert "sub_question" not in live_calls._READER_TOOL["input_schema"]["properties"]


def test_the_directive_carries_the_named_sub_question():
    reader = {"asks": [], "register": "informational", "kind": "other", "ambiguity_options": [], "sub_question": "C1.S1"}
    assert assemble_directive(reader).sub_question == "C1.S1"
    assert assemble_directive({**reader, "sub_question": " C1.S1 "}).sub_question == "C1.S1"
    assert assemble_directive({**reader, "sub_question": "C-E"}).sub_question is None
    assert assemble_directive({**reader, "sub_question": None}).sub_question is None
    assert assemble_directive({k: v for k, v in reader.items() if k != "sub_question"}).sub_question is None


def test_the_lpc_sidecar_only_names_records_the_world_holds():
    from pathlib import Path
    root = Path(__file__).resolve().parents[3]
    sidecar = yaml.safe_load((root / "Build/worlds/lpc/build/lpc_Answers_Sidecar.yaml").read_text(encoding="utf-8"))
    assert len(sidecar["subquestions"]) == 130
    assert all(set(e) == {"cluster", "label", "records"} for e in sidecar["subquestions"].values())
    assert sr.SUB_QUESTION_ID.fullmatch(next(iter(sidecar["subquestions"])))
