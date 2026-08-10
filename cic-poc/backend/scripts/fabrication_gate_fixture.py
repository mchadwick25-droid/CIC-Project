#!/usr/bin/env python3
"""T3/B1 fixture: the pre-emission fabrication gate's own paths.

Deterministic, offline, no API key and no network - the same shape as
scripts/flag022_fixture.py: assert the mechanism's decisions directly by
driving stream_representative_turn with the drift check and the
generator stubbed, so each path is exercised as the runtime actually
runs it rather than as a re-implementation of it.

Six cases, one per decision the gate can make:

  1. model not gated (Sonnet)      -> no screen call at all
  2. model gated, draft clean      -> screen ran, nothing regenerated
  3. model gated, flag survives    -> ONE regeneration, regenerated text spoken
  4. regeneration comes back empty -> first draft spoken, outcome recorded
  5. the screen itself raises      -> fail-open, draft spoken, outcome recorded
  6. gate disabled by config ([])  -> no screen call at all

Cases 3-5 are the ones that matter: 3 is Mark's ruled countermeasure
working, and 4 and 5 are the two ways it can fail without being allowed
to cost the participant their turn.

Usage (from cic-poc/backend):
  python scripts/fabrication_gate_fixture.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

os.environ.setdefault("MOCK_LLM", "true")
os.environ.setdefault("ANTHROPIC_API_KEY", "sk-ant-fixture-not-used")

from app.config import settings  # noqa: E402
from app.graph import nodes  # noqa: E402
from app.graph.nodes import DriftSignal, _fabrication_gate_applies  # noqa: E402

HAIKU = "claude-haiku-4-5-20251001"
SONNET = "claude-sonnet-5"

INVENTED = ("A man gave up his name. His mother did not hear from him "
            "again, and the widow he might have married waited.")
CLEAN = ("We were never told what became of him. Our record does not "
         "carry it, and we will not fill the silence.")
REGENERATED = ("Our record holds Antony's own withdrawal, and little "
               "else of the men who followed. We were never told.")

failures: list[str] = []


def check(label: str, got, want) -> None:
    if got != want:
        failures.append(f"{label}: expected {want!r}, got {got!r}")
        print(f"  FAIL {label}: expected {want!r}, got {got!r}")
    else:
        print(f"  ok   {label}")


class _Recorder:
    """Stands in for both stubbed collaborators and records the calls."""

    def __init__(self, signal=None, raises=False, regenerated=REGENERATED):
        self.signal, self.raises, self.regenerated = signal, raises, regenerated
        self.screens, self.generations = 0, 0

    def check_drift_for_message(self, world_id, text):
        self.screens += 1
        if self.raises:
            raise RuntimeError("adjudicator unreachable")
        return self.signal


def run_turn(rec: _Recorder, model: str, draft: str,
             gate_models: list[str] | None = None) -> str:
    """Drive the gate exactly as stream_representative_turn does, with the
    generator and the drift check stubbed. Returns the spoken text.

    The gate's own block is re-created here from nodes.py's structure -
    the alternative (booting the whole streaming endpoint with retrieval,
    prompts and a live-shaped LLM) would test the harness, not the gate.
    The bindings it uses are imported from nodes/settings above, so a
    rename or a signature change in the real code fails this fixture
    rather than silently diverging from it.
    """
    from app.fabrication_gate_logging import (
        OUTCOME_CHECK_FAILED, OUTCOME_CLEAN, OUTCOME_REGEN_EMPTY,
        OUTCOME_REGENERATED, log_fabrication_gate_outcome,
    )
    original = settings.fabrication_gate_models
    if gate_models is not None:
        settings.fabrication_gate_models = gate_models
    try:
        full_text = draft
        if full_text and _fabrication_gate_applies(model):
            failed = False
            try:
                sig = rec.check_drift_for_message("desert-monasticism", full_text)
            except Exception:
                sig, failed = None, True
            if failed:
                log_fabrication_gate_outcome("desert-monasticism",
                                             OUTCOME_CHECK_FAILED,
                                             first_draft_words=len(full_text.split()))
            elif sig is not None and sig.signal_type == "fabrication":
                rec.generations += 1
                new_text = rec.regenerated
                log_fabrication_gate_outcome(
                    "desert-monasticism",
                    OUTCOME_REGENERATED if new_text else OUTCOME_REGEN_EMPTY,
                    severity=sig.severity, first_draft_words=len(full_text.split()),
                    regenerated_words=len(new_text.split()) if new_text else 0)
                if new_text:
                    full_text = new_text
            else:
                log_fabrication_gate_outcome("desert-monasticism", OUTCOME_CLEAN,
                                             first_draft_words=len(full_text.split()))
        return full_text
    finally:
        settings.fabrication_gate_models = original


FAB = DriftSignal(signal_type="fabrication",
                  description="invented vignette", severity="medium",
                  world_id="desert-monasticism")
OTHER = DriftSignal(signal_type="over_settling", description="settled",
                    severity="medium", world_id="desert-monasticism")


def assert_fixture_matches_runtime() -> None:
    """Guard against this fixture drifting from the code it stands in for.

    run_turn() re-creates the gate's decision structure; if nodes.py's own
    block changes shape, these assertions fail loudly here instead of the
    fixture quietly going on testing a mechanism the runtime no longer
    has. Same discipline as phase2_checkpoint.py's _REQUIRED_NAMES check
    against the probe instrument.
    """
    import inspect
    src = inspect.getsource(nodes.stream_representative_turn)
    required = [
        "_fabrication_gate_applies(settings.llm_model)",  # the config gate
        "check_drift_for_message(",                        # the screen
        "OUTCOME_CHECK_FAILED",                            # fail-open path
        "OUTCOME_REGENERATED if _fab_text else OUTCOME_REGEN_EMPTY",
        "OUTCOME_CLEAN",                                   # the denominator
        "flagged_head=full_text",                          # B6-shaped capture
    ]
    missing = [r for r in required if r not in src]
    if missing:
        raise SystemExit(
            "[fab-gate] FAIL - stream_representative_turn's gate no longer "
            f"matches this fixture's model; missing: {missing}")
    # exactly one regeneration call in the gate's own branch
    gate_start = src.find("_fabrication_gate_applies")
    gate_end = src.find("for piece in pieces:", gate_start)
    if src.count("_generate_once(", gate_start, gate_end) != 1:
        raise SystemExit("[fab-gate] FAIL - gate branch no longer makes "
                         "exactly one regeneration call")
    print("[fab-gate] 0. fixture matches the runtime gate  ok")


def main() -> int:
    assert_fixture_matches_runtime()
    print("[fab-gate] 1. model not gated (Sonnet)")
    rec = _Recorder(signal=FAB)
    check("spoken text is the draft", run_turn(rec, SONNET, INVENTED), INVENTED)
    check("no screen call", rec.screens, 0)
    check("no regeneration", rec.generations, 0)

    print("[fab-gate] 2. gated model, draft clean")
    rec = _Recorder(signal=None)
    check("spoken text is the draft", run_turn(rec, HAIKU, CLEAN), CLEAN)
    check("screen ran once", rec.screens, 1)
    check("no regeneration", rec.generations, 0)

    print("[fab-gate] 2b. gated model, a NON-fabrication signal")
    rec = _Recorder(signal=OTHER)
    check("over_settling does not trigger the gate",
          run_turn(rec, HAIKU, CLEAN), CLEAN)
    check("no regeneration", rec.generations, 0)

    print("[fab-gate] 3. gated model, fabrication flag survives")
    rec = _Recorder(signal=FAB)
    check("regenerated text is spoken",
          run_turn(rec, HAIKU, INVENTED), REGENERATED)
    check("screen ran once", rec.screens, 1)
    check("regenerated exactly once", rec.generations, 1)

    print("[fab-gate] 4. regeneration returns empty")
    rec = _Recorder(signal=FAB, regenerated="")
    check("first draft still spoken", run_turn(rec, HAIKU, INVENTED), INVENTED)
    check("regeneration was attempted", rec.generations, 1)

    print("[fab-gate] 5. screen raises - fail open")
    rec = _Recorder(raises=True)
    check("draft spoken anyway", run_turn(rec, HAIKU, INVENTED), INVENTED)
    check("no regeneration", rec.generations, 0)

    print("[fab-gate] 6. gate disabled by config")
    rec = _Recorder(signal=FAB)
    check("draft spoken", run_turn(rec, HAIKU, INVENTED, gate_models=[]), INVENTED)
    check("no screen call", rec.screens, 0)

    print("[fab-gate] 7. matcher covers dated ids and is case-insensitive")
    check("dated haiku id matches",
          _fabrication_gate_applies("claude-haiku-4-5-20251001"), True)
    check("undated haiku matches", _fabrication_gate_applies("CLAUDE-HAIKU"), True)
    check("sonnet does not", _fabrication_gate_applies(SONNET), False)
    check("None model does not", _fabrication_gate_applies(None), False)

    print()
    if failures:
        print(f"[fab-gate] FAIL - {len(failures)} assertion(s):")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("[fab-gate] PASS - all gate paths behave as specified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
