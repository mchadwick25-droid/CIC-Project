"""An approved live-turn run names itself in its report, and every call in it
carries the live-test name and the world. Fixture world, fake client: no model
call."""
import sys

import pytest

from engine.m4 import live_turn_run
from engine.m4.tests.test_turn import FakeBedrockClient, _reader, _safety
from engine.provider import guard

HAIKU = "us.anthropic.claude-haiku-4-5-20251001-v1:0"
SONNET = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"


@pytest.fixture(autouse=True)
def _clean_guard():
    guard.reset_for_tests()
    yield
    guard.reset_for_tests()


def test_the_report_carries_the_live_test_and_a_world_on_every_call(monkeypatch):
    lines = []
    monkeypatch.setattr(guard, "_emit", lines.append)
    monkeypatch.setattr(sys, "argv", ["prog", "--live-test", "report proof", "--cap-usd", "2.00"])
    fake = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"), reader_response=_reader(), stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."],
    )
    monkeypatch.setattr(
        live_turn_run, "resolve_model_id",
        lambda pattern, region: (guard.note_model(SONNET if "sonnet" in pattern else HAIKU), SONNET if "sonnet" in pattern else HAIKU)[1],
    )
    monkeypatch.setattr(live_turn_run, "make_client", lambda region: guard.wrap(fake, guard.admit(), provider="bedrock", region=region))

    report = live_turn_run.run("us-east-1", world_key="fix", messages=["Who was Jesus to your people?"])

    assert len(lines) == 1 and "report proof" in lines[0]
    summary = report["live_test"]
    assert (summary["name"], summary["cap_usd"]) == ("report proof", 2.0)
    assert summary["route"] == "Bedrock, regional inference profile, us-east-1"
    assert summary["model_ids"] == sorted([HAIKU, SONNET])
    assert 0 < summary["priced_total_usd"] <= 2.0
    assert {row["call_kind"] for row in report["usage"]} == {"safety_call", "reader_call", "voice_generation"}
    assert all(row["world_key"] == "fix" and row["live_test"] == "report proof" for row in report["usage"])


def test_a_report_made_outside_a_live_test_says_so(monkeypatch):
    fake = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(), stream_chunks=["Yes [[fix.witness.who-is-jesus]]."])
    monkeypatch.setattr(live_turn_run, "resolve_model_id", lambda pattern, region: HAIKU)
    monkeypatch.setattr(live_turn_run, "make_client", lambda region: fake)
    report = live_turn_run.run("us-east-1", world_key="fix", messages=["Who was Jesus to your people?"])
    assert report["live_test"] is None
    assert all(row["live_test"] is None and row["world_key"] == "fix" for row in report["usage"])
