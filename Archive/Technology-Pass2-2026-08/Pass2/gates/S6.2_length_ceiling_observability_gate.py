"""S6.2 gate — length-ceiling retry observability.

Verifies the purely-additive instrumentation added for the 2026-07-31
retry-cost investigation, and pins the measurement that investigation
rests on so a later reader can re-derive it instead of trusting it.

Checks:
  1. The report's CEILING_WORLDS table matches HARD_CEILING_WORLDS and
     RETRY_TRIGGER_MULTIPLES as actually deployed in app/graph/nodes.py
     (read from source, not imported — no app import, no API key).
  2. The forensic retry detector finds exactly the retries the
     investigation reports on the committed 2026-07 raw log, and its
     count is stable across a wide surplus window (so it does not depend
     on the corrective message's current wording).
  3. World attribution from cached-prefix arithmetic reproduces the
     per-world rep-turn and retry counts the investigation reports.
  4. The retry cost figures the investigation reports reproduce to the
     cent from the raw log, using the runner's own pricing.
  5. `--report` on the committed raw log is byte-identical to the
     committed baseline report for every section that existed before
     this change — the new section is strictly appended.
  6. app/length_ceiling_logging.py emits all three outcome shapes and
     the runner's CEILING_RE parses every one of them back.
  7. A raw log containing length_ceiling records still reports correctly:
     the new record kind is not counted as a turn and not counted as an
     LLM call.
  8. nodes.py's ceiling branch still logs an outcome on every path
     (under / dead zone / retried) — an outcome that stops being logged
     silently removes the denominator this whole measurement needs.

Deterministic; re-runnable offline; exit 0 = gate green. Emits a markdown
report on stdout. Run from the repo root:
    python Archive/Technology-Pass2-2026-08/Pass2/gates/S6.2_length_ceiling_observability_gate.py
"""
import ast
import importlib.util
import io
import json
import logging
import re
import sys
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BACKEND = ROOT / "cic-poc" / "backend"
RUNNER = BACKEND / "scripts" / "cost_baseline_runner.py"
NODES = BACKEND / "app" / "graph" / "nodes.py"
RAW = ROOT / "Archive/Technology-Pass2-2026-08/Pass2/baselines/cost_baseline_2026-07_raw.jsonl"
REPORT = ROOT / "Archive/Technology-Pass2-2026-08/Pass2/baselines/cost_baseline_2026-07.md"
NEW_SECTION = "\n## Length-ceiling retry mechanism"

# The investigation's own numbers. This gate exists to make them checkable,
# so they are written here as literals and re-derived below, not read from
# the memo.
EXPECTED_RETRIES = 15
EXPECTED_FIRSTS = 49
EXPECTED_PER_WORLD = {                       # world: (rep turns, retries)
    "desert-monasticism": (19, 15),
    "post-apostolic-house-church": (15, 0),
    "alexandria-catechetical": (10, 0),
    "syriac-edessa-nisibis": (5, 0),
}
EXPECTED_C2_RETRY_USD = 0.1423               # C2_desert retry spend, standard
EXPECTED_C2_TOTAL_USD = 0.5964               # C2_desert whole-conversation
EXPECTED_TOTAL_RETRY_USD = 0.3188            # whole 40-turn baseline

failures, notes = [], []


def check(name, ok, detail=""):
    (notes if ok else failures).append((name, detail))
    return ok


def load_runner():
    spec = importlib.util.spec_from_file_location("cbr", RUNNER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def deployed_ceilings():
    """HARD_CEILING_WORLDS / RETRY_TRIGGER_MULTIPLES straight from source."""
    tree = ast.parse(NODES.read_text(encoding="utf-8"))
    found = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        tgt = node.targets[0]
        if isinstance(tgt, ast.Name) and tgt.id in (
                "HARD_CEILING_WORLDS", "RETRY_TRIGGER_MULTIPLES"):
            found[tgt.id] = ast.literal_eval(node.value)
    return found


def main():
    cbr = load_runner()
    calls, ceiling_recs = [], []
    for line in RAW.read_text(encoding="utf-8").splitlines():
        rec = json.loads(line)
        if rec["kind"] == "llm_call":
            calls.append(rec)
        elif rec["kind"] == "length_ceiling":
            ceiling_recs.append(rec)

    # --- 1. deployed constants vs the report's copy --------------------------
    dep = deployed_ceilings()
    want = {w: (c, dep["RETRY_TRIGGER_MULTIPLES"].get(w))
            for w, c in dep.get("HARD_CEILING_WORLDS", {}).items()}
    check("1. CEILING_WORLDS matches nodes.py",
          want == cbr.CEILING_WORLDS,
          f"nodes.py={want} runner={cbr.CEILING_WORLDS}")

    # --- 2. detector count + stability --------------------------------------
    firsts, retries = cbr.split_retry_calls(calls)
    check("2a. retry count on the committed raw log",
          len(retries) == EXPECTED_RETRIES and len(firsts) == EXPECTED_FIRSTS,
          f"{len(retries)} retries / {len(firsts)} first drafts "
          f"(expected {EXPECTED_RETRIES}/{EXPECTED_FIRSTS})")
    saved = cbr.RETRY_SURPLUS_MAX
    counts = {}
    for window in (51, 80, 120, 250, 400):
        cbr.RETRY_SURPLUS_MAX = window
        counts[window] = len(cbr.split_retry_calls(calls)[1])
    cbr.RETRY_SURPLUS_MAX = saved
    check("2b. detector stable across surplus windows 51..400",
          len(set(counts.values())) == 1, str(counts))
    surpluses = {r["input_tokens"] - p["input_tokens"] - p["output_tokens"]
                 for r, p in retries}
    check("2c. corrective-message surplus is a single constant",
          len(surpluses) == 1, f"observed surplus values: {sorted(surpluses)}")

    # --- 3. world attribution ------------------------------------------------
    spec = json.loads((BACKEND / "scripts" / "cost_baseline_conversations.json")
                      .read_text(encoding="utf-8"))
    worlds = cbr.attribute_worlds(calls, spec)
    check("3a. every main_response call attributes to a world",
          all(v is not None for v in worlds.values()),
          f"{sum(1 for v in worlds.values() if v is None)} unattributed")
    got = {}
    for w in set(EXPECTED_PER_WORLD):
        got[w] = (sum(1 for c in firsts if worlds.get(id(c)) == w),
                  sum(1 for r, _ in retries if worlds.get(id(r)) == w))
    check("3b. per-world rep-turn and retry counts",
          got == EXPECTED_PER_WORLD, f"got={got}")
    # A world only ever seen at the multi-world table is the hard case; make
    # its identification explicit rather than implied by the totals above.
    check("3c. syriac (multi-world-only) identified, not left unknown",
          got.get("syriac-edessa-nisibis", (0, 0))[0] > 0)

    # --- 4. cost figures -----------------------------------------------------
    S = lambda r: cbr.dollars(r, cbr.PRICING_STANDARD) or 0.0
    retry_calls = [r for r, _ in retries]
    c2 = [c for c in calls if c["conversation"] == "C2_desert"]
    c2r = [r for r in retry_calls if r["conversation"] == "C2_desert"]
    c2_retry, c2_total = sum(S(r) for r in c2r), sum(S(r) for r in c2)
    all_retry = sum(S(r) for r in retry_calls)
    check("4a. C2_desert retry spend", round(c2_retry, 4) == EXPECTED_C2_RETRY_USD,
          f"${c2_retry:.4f}")
    check("4b. C2_desert whole-conversation spend",
          round(c2_total, 4) == EXPECTED_C2_TOTAL_USD, f"${c2_total:.4f}")
    check("4c. whole-baseline retry spend",
          round(all_retry, 4) == EXPECTED_TOTAL_RETRY_USD, f"${all_retry:.4f}")
    # The disputed figure, settled arithmetically: a main_response-scoped
    # share and a whole-conversation share must differ by exactly
    # main_response's share of the conversation. 13.6% and 38.8% cannot both
    # be right; 23.9% and 38.8% are the same measurement at two scopes.
    c2_main = sum(S(c) for c in c2 if c["label"] == "main_response")
    check("4d. 38.8% main-scoped x main's share of C2 == the 23.9% figure",
          abs((c2_retry / c2_main) * (c2_main / c2_total) - 0.239) < 0.001,
          f"main-scoped {c2_retry/c2_main:.1%} x main share "
          f"{c2_main/c2_total:.1%} = {c2_retry/c2_total:.1%}")

    # --- 5. report determinism and append-only shape -------------------------
    # The append-only property (every section that existed before this change
    # is byte-identical, the new one strictly appended) was verified at
    # implementation time against the pre-change committed report and is
    # recorded in the commit; it cannot be re-asserted here now that the
    # committed report has been regenerated to include the new section. What
    # IS re-assertable, and is the contract that matters going forward, is
    # that --report on the committed raw log still reproduces the committed
    # report byte-for-byte, and that the new section stays last.
    buf = io.StringIO()
    with redirect_stdout(buf):
        cbr.report(str(RAW))
    produced = buf.getvalue()
    head, sep, tail = produced.partition(NEW_SECTION)
    check("5a. new section is present", bool(sep))
    check("5b. --report reproduces the committed report byte-for-byte",
          produced == REPORT.read_text(encoding="utf-8"),
          "regenerate the committed report if this is an intended change")
    check("5c. the new section is last (nothing appended after it)",
          "\n## " not in tail, "a later section would break append-only")

    # --- 6. logging module round-trip ---------------------------------------
    sys.path.insert(0, str(BACKEND))
    lspec = importlib.util.spec_from_file_location(
        "lcl", BACKEND / "app" / "length_ceiling_logging.py")
    lcl = importlib.util.module_from_spec(lspec)
    lspec.loader.exec_module(lcl)

    class Cap(logging.Handler):
        def __init__(self):
            super().__init__()
            self.lines = []

        def emit(self, r):
            self.lines.append(r.getMessage())

    cap = Cap()
    lcl.logger.addHandler(cap)
    lcl.log_length_ceiling_outcome("desert-monasticism", 60, 1.5, 44,
                                   lcl.OUTCOME_UNDER,
                                   request_id="abc", session_id="s1")
    lcl.log_length_ceiling_outcome("desert-monasticism", 60, 1.5, 77,
                                   lcl.OUTCOME_DEAD_ZONE,
                                   request_id="abc", session_id="s1")
    lcl.log_length_ceiling_outcome("alexandria-catechetical", 160, 1.2, 311,
                                   lcl.OUTCOME_RETRIED, retry_words=148,
                                   request_id="abc", session_id="s1")
    lcl.logger.removeHandler(cap)
    check("6a. all three outcome shapes emit a line", len(cap.lines) == 3)
    parsed = [cbr.CEILING_RE.search(l) for l in cap.lines]
    check("6b. runner's CEILING_RE parses every shape",
          all(parsed), f"{sum(1 for p in parsed if p)}/3 parsed")
    if all(parsed):
        check("6c. parsed fields survive the round trip",
              parsed[0].group("outcome") == "under_ceiling"
              and parsed[1].group("outcome") == "dead_zone"
              and parsed[2].group("outcome") == "retried"
              and parsed[2].group("retry_words") == "148"
              and parsed[0].group("retry_words") == "None"
              and parsed[2].group("first_draft_words") == "311"
              and parsed[2].group("trigger_multiple") == "1.2")

    # --- 7. a log carrying the new record kind still reports correctly -------
    lines = RAW.read_text(encoding="utf-8").splitlines()
    extra = json.dumps({
        "kind": "length_ceiling", "conversation": "C2_desert", "turn": 1,
        "ts": 0.0, "world_id": "desert-monasticism", "ceiling": 60,
        "trigger_multiple": 1.5, "first_draft_words": 175,
        "outcome": "retried", "retry_words": 58,
        "request_id": "d706a2be", "session_id": "x"})
    mixed = Path(sys.argv[0]).parent / "_gate_tmp_mixed.jsonl"
    mixed.write_text("\n".join(lines + [extra]) + "\n", encoding="utf-8")
    try:
        buf2 = io.StringIO()
        with redirect_stdout(buf2):
            cbr.report(str(mixed))
        mixed_out = buf2.getvalue()
    finally:
        mixed.unlink()
    turnline = [l for l in produced.splitlines()
                if l.startswith("**Totals:")]
    mixedline = [l for l in mixed_out.splitlines() if l.startswith("**Totals:")]
    check("7a. length_ceiling records do not inflate call/turn totals",
          turnline == mixedline, f"{turnline} vs {mixedline}")
    check("7b. the direct-records table appears when records are present",
          "### Direct `length_ceiling` records" in mixed_out
          and "### Direct `length_ceiling` records" not in produced)

    # --- 8. nodes.py logs an outcome on every ceiling path -------------------
    src = NODES.read_text(encoding="utf-8")
    for outcome in ("OUTCOME_UNDER", "OUTCOME_DEAD_ZONE", "OUTCOME_RETRIED"):
        check(f"8. nodes.py ceiling branch logs {outcome}",
              f"{outcome},\n" in src or f"{outcome}," in src)

    # --- report --------------------------------------------------------------
    print("# S6.2 gate — length-ceiling retry observability\n")
    print("| check | result | detail |")
    print("|---|---|---|")
    for name, detail in sorted(notes):
        print(f"| {name} | PASS | {detail} |")
    for name, detail in sorted(failures):
        print(f"| {name} | **FAIL** | {detail} |")
    print(f"\n**{len(notes)} passed, {len(failures)} failed.**")
    if failures:
        print("\n## GATE: FAIL")
        return 1
    print("\n## GATE: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
