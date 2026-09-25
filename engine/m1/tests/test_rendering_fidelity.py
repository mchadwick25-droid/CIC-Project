"""Mocked-grader tests (no live AWS/Bedrock call) for
engine.m1.rendering_fidelity: the forced-tool-use call shape (structured
verdict, no salvage parsing), rate-limit retry with backoff (the real
first fleet sweep hit this - 21/100 calls 429'd with no retry, an
incomplete sweep silently reported as the whole fleet), and sweep_world's
aggregation - skipping records with no modern_rendering, counting each
verdict, and landing a timeout/parse-failure/exhausted-retry in errors
rather than crashing the sweep."""
from pathlib import Path
from types import SimpleNamespace

import httpx2
from anthropic import APITimeoutError, RateLimitError

from engine.m1.rendering_fidelity import (
    cross_language_report,
    grade_rendering,
    non_english_sourced_quotes,
    sweep_world,
)
import engine.m1.rendering_fidelity as rendering_fidelity


def _rate_limit_error():
    request = httpx2.Request("POST", "https://example.com")
    response = httpx2.Response(429, request=request)
    return RateLimitError("rate limited", response=response, body=None)


class _FakeToolUse:
    def __init__(self, name, input_):
        self.type = "tool_use"
        self.name = name
        self.input = input_


_FAKE_USAGE = SimpleNamespace(input_tokens=10, output_tokens=5, cache_creation_input_tokens=0, cache_read_input_tokens=0)


class FakeGraderClient:
    """Returns the scripted responses in order, one per .create() call - a
    sweep grades several records in sequence and different records need
    different verdicts. A response that is an Exception instance is raised
    instead of returned; None simulates a parse failure (no tool_use block
    in the reply)."""

    def __init__(self, responses):
        self._responses = list(responses)
        self.captured_calls = []

    @property
    def messages(self):
        return self

    def create(self, *, model, max_tokens, system, tools, tool_choice, messages, timeout):
        self.captured_calls.append({"model": model, "tool_name": tool_choice["name"], "timeout": timeout})
        response = self._responses.pop(0)
        if isinstance(response, Exception):
            raise response
        if response is None:
            return SimpleNamespace(content=[], usage=_FAKE_USAGE)
        return SimpleNamespace(content=[_FakeToolUse(tool_choice["name"], response)], usage=_FAKE_USAGE)


# --- grade_rendering: the single-call contract --------------------------


def test_translation_verdict_returns_ok_outcome():
    client = FakeGraderClient([{"verdict": "translation", "reasoning": "Every clause carried across."}])
    outcome = grade_rendering(client, "fake-model", original="A and B.", modern_rendering="A and B, in modern words.")
    assert outcome.status == "ok"
    assert outcome.failed is False
    assert outcome.value["verdict"] == "translation"


def test_summary_verdict_names_the_dropped_clause():
    client = FakeGraderClient([{"verdict": "summary", "reasoning": "Drops the second clause, 'and B.'"}])
    outcome = grade_rendering(client, "fake-model", original="A and B.", modern_rendering="A.")
    assert outcome.value["verdict"] == "summary"
    assert "B" in outcome.value["reasoning"]


def test_expansion_verdict_names_the_added_clause():
    client = FakeGraderClient([{"verdict": "expansion", "reasoning": "Adds an explanation not in the original."}])
    outcome = grade_rendering(client, "fake-model", original="A.", modern_rendering="A, which meant everything to them.")
    assert outcome.value["verdict"] == "expansion"


def test_call_is_forced_tool_use():
    client = FakeGraderClient([{"verdict": "translation", "reasoning": "ok"}])
    grade_rendering(client, "fake-model", original="X.", modern_rendering="X.")
    call = client.captured_calls[0]
    assert call["tool_name"] == "submit_rendering_fidelity_verdict"


def test_api_timeout_returns_failed_timeout_outcome():
    client = FakeGraderClient([APITimeoutError(request=None)])
    outcome = grade_rendering(client, "fake-model", original="X.", modern_rendering="X.")
    assert outcome.status == "timeout"
    assert outcome.failed is True


def test_no_tool_use_block_returns_parse_failure():
    client = FakeGraderClient([None])
    outcome = grade_rendering(client, "fake-model", original="X.", modern_rendering="X.")
    assert outcome.status == "parse_failure"
    assert outcome.failed is True


# --- RateLimitError retry with backoff -----------------------------------


def test_rate_limit_retries_then_succeeds(monkeypatch):
    slept = []
    monkeypatch.setattr(rendering_fidelity.time, "sleep", lambda s: slept.append(s))
    client = FakeGraderClient([_rate_limit_error(), _rate_limit_error(), {"verdict": "translation", "reasoning": "ok"}])

    outcome = grade_rendering(client, "fake-model", original="X.", modern_rendering="X.")

    assert outcome.status == "ok"
    assert outcome.value["verdict"] == "translation"
    assert len(client.captured_calls) == 3  # two 429s, then the real call
    assert slept == [2.0, 4.0]  # real exponential backoff, not a fixed pause


def test_rate_limit_exhausted_retries_returns_error_outcome_not_a_crash(monkeypatch):
    monkeypatch.setattr(rendering_fidelity.time, "sleep", lambda s: None)
    client = FakeGraderClient([_rate_limit_error()] * (rendering_fidelity._RATE_LIMIT_MAX_RETRIES + 1))

    outcome = grade_rendering(client, "fake-model", original="X.", modern_rendering="X.")

    assert outcome.status == "error"
    assert outcome.failed is True
    assert "rate limited" in outcome.value["error"]
    assert len(client.captured_calls) == rendering_fidelity._RATE_LIMIT_MAX_RETRIES + 1


# --- sweep_world: aggregation over a world's quote records ---------------


def _record(rid, *, text, modern_rendering=None, verification_state="verified-direct"):
    rec = {
        "id": rid,
        "record_type": "quote",
        "text": text,
        "confidence": {"verification_state": verification_state},
    }
    if modern_rendering is not None:
        rec["modern_rendering"] = modern_rendering
    return rec


def test_sweep_world_skips_records_with_no_modern_rendering(monkeypatch):
    records = {
        "w.quote.a": _record("w.quote.a", text="A.", modern_rendering="A, in modern words."),
        "w.quote.b": _record("w.quote.b", text="B."),  # no modern_rendering at all
    }
    monkeypatch.setattr("engine.m1.rendering_fidelity.load_world_records", lambda world_key: records)
    client = FakeGraderClient([{"verdict": "translation", "reasoning": "ok"}])

    report = sweep_world("w", client, "fake-model")

    assert report["total_quotes"] == 2
    assert report["graded_count"] == 1
    assert report["no_modern_rendering_count"] == 1
    assert report["no_modern_rendering"] == ["w.quote.b"]


def test_sweep_world_counts_each_verdict_and_records_non_translation_findings(monkeypatch):
    records = {
        "w.quote.a": _record("w.quote.a", text="A and B.", modern_rendering="A and B, in modern words."),
        "w.quote.b": _record("w.quote.b", text="C and D.", modern_rendering="C."),
        "w.quote.c": _record("w.quote.c", text="E.", modern_rendering="E, which changed everything.", verification_state="verified-via-authority"),
    }
    monkeypatch.setattr("engine.m1.rendering_fidelity.load_world_records", lambda world_key: records)
    client = FakeGraderClient(
        [
            {"verdict": "translation", "reasoning": "ok"},
            {"verdict": "summary", "reasoning": "Drops 'and D.'"},
            {"verdict": "expansion", "reasoning": "Adds a claim not in the original."},
        ]
    )

    report = sweep_world("w", client, "fake-model")

    assert report["graded_count"] == 3
    assert report["verdict_counts"] == {"translation": 1, "summary": 1, "expansion": 1, "mixed": 0}
    finding_ids = {f["id"] for f in report["findings"]}
    assert finding_ids == {"w.quote.b", "w.quote.c"}
    # a translation verdict never produces a finding - only the two non-translation ones do
    by_id = {f["id"]: f for f in report["findings"]}
    assert by_id["w.quote.b"]["verdict"] == "summary"
    assert by_id["w.quote.c"]["verdict"] == "expansion"
    # verification_state rides along for context, never as a filter - one
    # general standard, no per-record scope carve-out - so both escalated
    # and verified-direct records get graded and can both produce findings.
    assert by_id["w.quote.c"]["verification_state"] == "verified-via-authority"


def test_sweep_world_lands_a_failed_call_in_errors_not_a_crash(monkeypatch):
    records = {
        "w.quote.a": _record("w.quote.a", text="A.", modern_rendering="A."),
        "w.quote.b": _record("w.quote.b", text="B.", modern_rendering="B, in modern words."),
    }
    monkeypatch.setattr("engine.m1.rendering_fidelity.load_world_records", lambda world_key: records)
    client = FakeGraderClient([APITimeoutError(request=None), {"verdict": "translation", "reasoning": "ok"}])

    report = sweep_world("w", client, "fake-model")

    assert report["error_count"] == 1
    assert report["errors"][0]["id"] == "w.quote.a"
    assert report["errors"][0]["status"] == "timeout"
    assert report["graded_count"] == 1  # the second record still gets graded


def test_sweep_world_ignores_non_quote_records(monkeypatch):
    records = {
        "w.quote.a": _record("w.quote.a", text="A.", modern_rendering="A."),
        "w.figure.someone": {"id": "w.figure.someone", "record_type": "figure"},
    }
    monkeypatch.setattr("engine.m1.rendering_fidelity.load_world_records", lambda world_key: records)
    client = FakeGraderClient([{"verdict": "translation", "reasoning": "ok"}])

    report = sweep_world("w", client, "fake-model")

    assert report["total_quotes"] == 1


# --- non_english_sourced_quotes: the cross-language scoping ---------------
# The grader itself (SYSTEM_PROMPT, grade_rendering) is already language-
# agnostic; what needs its own test is only the SCOPING - finding the real
# subset of quotes whose own source declares a non-English original,
# against real vendored-file headers (cic/engine/texts_registry.py's own
# `Language:` convention), not a mocked language lookup.


def _source_record(sid, *, edition):
    return {"id": sid, "record_type": "source", "edition": edition}


def test_non_english_sourced_quotes_finds_a_latin_source(monkeypatch, tmp_path):
    (tmp_path / "some-latin-work.txt").write_text(
        "Title: A Latin Work\nLanguage: lat\n\nBody text here.\n", encoding="utf-8")
    (tmp_path / "an-english-work.txt").write_text(
        "Title: An English Work\n\nBody text here.\n", encoding="utf-8")
    monkeypatch.setattr(rendering_fidelity, "_TEXTS_DIR", tmp_path)

    worlds = {
        "w": {
            "w.quote.lat": {
                "id": "w.quote.lat", "record_type": "quote", "text": "Verbum.",
                "modern_rendering": "The word.",
                "sources": [{"source_id": "w.source.lat"}],
            },
            "w.source.lat": _source_record("w.source.lat", edition="cic/texts/some-latin-work.txt"),
            "w.quote.eng": {
                "id": "w.quote.eng", "record_type": "quote", "text": "Word.",
                "modern_rendering": "The word.",
                "sources": [{"source_id": "w.source.eng"}],
            },
            "w.source.eng": _source_record("w.source.eng", edition="cic/texts/an-english-work.txt"),
        }
    }

    found = non_english_sourced_quotes(worlds)

    assert [f["id"] for f in found] == ["w.quote.lat"]
    assert found[0]["language"] == "lat"
    assert found[0]["filename"] == "some-latin-work.txt"


def test_non_english_sourced_quotes_skips_a_source_that_does_not_resolve(monkeypatch, tmp_path):
    monkeypatch.setattr(rendering_fidelity, "_TEXTS_DIR", tmp_path)
    worlds = {
        "w": {
            "w.quote.a": {
                "id": "w.quote.a", "record_type": "quote", "text": "A.",
                "sources": [{"source_id": "w.source.missing"}],
            },
            "w.source.missing": _source_record("w.source.missing", edition="not a real edition path"),
        }
    }

    assert non_english_sourced_quotes(worlds) == []


def test_non_english_sourced_quotes_decided_by_the_first_resolving_source_not_any_source(monkeypatch, tmp_path):
    """The real bug this pins: a quote citing an English translation FIRST
    and a Latin critical edition SECOND (the NPNF-then-Petschenig shape a
    real fleet record actually has) must be judged by the first source -
    English - and skipped entirely, not picked up because a LATER source
    happens to be non-English. The record's own `text` field is whatever
    the first-cited edition gives it (English here), so grading it against
    the second source's language would silently compare English to
    English under a "cross-language" label."""
    (tmp_path / "english-translation.txt").write_text(
        "Title: An English Translation\n\nBody text here.\n", encoding="utf-8")
    (tmp_path / "latin-critical-edition.txt").write_text(
        "Title: A Latin Critical Edition\nLanguage: lat\n\nBody text here.\n", encoding="utf-8")
    monkeypatch.setattr(rendering_fidelity, "_TEXTS_DIR", tmp_path)

    worlds = {
        "w": {
            "w.quote.eng-then-lat": {
                "id": "w.quote.eng-then-lat", "record_type": "quote",
                "text": "The English translation's own words.",
                "modern_rendering": "The English translation's own words, modernized.",
                "sources": [
                    {"source_id": "w.source.eng"},
                    {"source_id": "w.source.lat"},
                ],
            },
            "w.source.eng": _source_record("w.source.eng", edition="cic/texts/english-translation.txt"),
            "w.source.lat": _source_record("w.source.lat", edition="cic/texts/latin-critical-edition.txt"),
        }
    }

    assert non_english_sourced_quotes(worlds) == []


# --- cross_language_report: aggregation over the scoped subset ------------


def test_cross_language_report_grades_only_the_non_english_subset(monkeypatch, tmp_path):
    (tmp_path / "latin-work.txt").write_text("Language: lat\n\nBody.\n", encoding="utf-8")
    monkeypatch.setattr(rendering_fidelity, "_TEXTS_DIR", tmp_path)
    worlds = {
        "w": {
            "w.quote.lat": {
                "id": "w.quote.lat", "record_type": "quote", "text": "Verbum.",
                "modern_rendering": "The word.",
                "sources": [{"source_id": "w.source.lat"}],
                "confidence": {"verification_state": "verified-direct"},
            },
            "w.source.lat": _source_record("w.source.lat", edition="cic/texts/latin-work.txt"),
            "w.quote.eng": {
                "id": "w.quote.eng", "record_type": "quote", "text": "An English quote, not in scope.",
                "modern_rendering": "An English quote, not in scope.",
            },
        }
    }
    monkeypatch.setattr("engine.m1.quote_verbatim.REPORT_WORLDS", ("w",))
    monkeypatch.setattr(rendering_fidelity, "load_world_records", lambda world_key: worlds[world_key])
    monkeypatch.setattr("engine.provider.bedrock.resolve_model_id", lambda pattern, region: "fake-model")
    monkeypatch.setattr("engine.provider.bedrock.make_client",
                        lambda region: FakeGraderClient([{"verdict": "translation", "reasoning": "ok"}]))

    report = cross_language_report("fake-region")

    assert report["total_non_english_sourced_quotes"] == 1
    assert report["graded_count"] == 1
    assert report["findings"][0]["id"] == "w.quote.lat"
    assert report["findings"][0]["language"] == "lat"
    assert report["findings"][0]["verdict"] == "translation"
    assert report["grader_scope"] == "single Haiku run; first-pass screen, not a V1.8 two-grader pass"
