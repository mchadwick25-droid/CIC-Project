"""S1.1 B-COST runner (blueprint S1.1) - cache-aware cost baseline.

Two modes:

  --run [--limit-conversations N] [--limit-turns N] [--out raw.jsonl]
      Drives the FIXED conversation set (cost_baseline_conversations.json)
      through the real app in-process (fastapi TestClient, real API calls,
      mock_llm must be off) and writes one JSONL record per LLM call plus
      one per turn. Per-turn attribution is exact: every LLM call a turn
      triggers - including the invisible post-'done' governance calls -
      happens inside event_stream() before the SSE stream closes, so
      consuming the stream to EOF bounds the turn (verified against
      app/main.py's event_stream, 2026-07-26).

  --report raw.jsonl
      Deterministic aggregation of a raw log into the markdown baseline
      report (stdout). Same input -> byte-identical output.

Usage lines are captured by attaching a handler to the "cic.llm_usage"
logger (S1.1a made instrumentation complete: 30/30 call sites). Observation
only - nothing in the app is modified.

Pricing (per MTok, from the claude-api reference, cached 2026-06-24; cache
write = 1.25x input for the 5-minute TTL the app uses via its "ephemeral"
cache_control; cache read = 0.1x input). claude-sonnet-5 carries intro
pricing ($2/$10) through 2026-08-31; the report states standard-rate
dollars as the primary (stable) figure with intro-billed actuals beside it.
"""
import argparse
import json
import logging
import re
import sys
import threading
import time
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

SPEC_PATH = Path(__file__).with_name("cost_baseline_conversations.json")

# per-MTok: (input, output, cache_write_5m, cache_read)
PRICING_STANDARD = {
    "claude-sonnet-5": (3.00, 15.00, 3.75, 0.30),
    "claude-sonnet-4-6": (3.00, 15.00, 3.75, 0.30),
    "claude-sonnet-4-5": (3.00, 15.00, 3.75, 0.30),
    "claude-haiku-4-5": (1.00, 5.00, 1.25, 0.10),
}
# intro pricing in effect through 2026-08-31 (sonnet-5 only)
PRICING_INTRO = {
    "claude-sonnet-5": (2.00, 10.00, 2.50, 0.20),
}

USAGE_RE = re.compile(
    r"\[llm_usage\] label=(?P<label>\S+) model=(?P<model>\S+) "
    r"request_id=(?P<request_id>\S+) session_id=(?P<session_id>\S+) "
    r"input_tokens=(?P<input>\d+) output_tokens=(?P<output>\d+) "
    r"cache_creation_input_tokens=(?P<cache_creation>\d+) "
    r"cache_read_input_tokens=(?P<cache_read>\d+)"
)


class UsageCapture(logging.Handler):
    def __init__(self):
        super().__init__()
        self.records = []
        # NOT self.lock - logging.Handler owns that name (an RLock that
        # handle() acquires around emit()); overwriting it with a plain Lock
        # self-deadlocks the first time emit() tries to take it again.
        self._records_lock = threading.Lock()

    def emit(self, record):
        m = USAGE_RE.search(record.getMessage())
        if not m:
            return
        d = m.groupdict()
        entry = {
            "ts": time.time(),
            "label": d["label"],
            "model": d["model"],
            "request_id": d["request_id"],
            "session_id": d["session_id"],
            "input_tokens": int(d["input"]),
            "output_tokens": int(d["output"]),
            "cache_creation_input_tokens": int(d["cache_creation"]),
            "cache_read_input_tokens": int(d["cache_read"]),
        }
        with self._records_lock:
            self.records.append(entry)

    def drain(self):
        with self._records_lock:
            out, self.records = self.records, []
        return out


def run(limit_conversations, limit_turns, out_path):
    from app.config import settings
    assert not settings.mock_llm, "B-COST must run against the real system, not mock_llm"

    capture = UsageCapture()
    logging.getLogger("cic.llm_usage").addHandler(capture)

    from fastapi.testclient import TestClient
    from app.main import app

    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    conversations = spec["conversations"][:limit_conversations or None]

    out = open(out_path, "a", encoding="utf-8")

    def write(rec):
        out.write(json.dumps(rec) + "\n")
        out.flush()

    with TestClient(app) as client:
        for conv in conversations:
            resp = client.post("/api/session/start",
                               json={"world_ids": conv["world_ids"]})
            resp.raise_for_status()
            session_id = resp.json()["session_id"]
            # session-start LLM calls (facilitator reception/handoff via graph)
            for r in capture.drain():
                write({"kind": "llm_call", "conversation": conv["id"],
                       "turn": 0, "turn_label": "session_start", **r})
            write({"kind": "turn", "conversation": conv["id"], "turn": 0,
                   "turn_label": "session_start", "session_id": session_id,
                   "ts": time.time()})

            turns = conv["turns"][:limit_turns or None]
            for i, turn in enumerate(turns, start=1):
                pause = turn.get("pause_before_s", 0)
                if pause:
                    print(f"[{conv['id']}] pausing {pause}s before turn {i} "
                          f"(cache-TTL observation)", flush=True)
                    time.sleep(pause)
                t0 = time.time()
                text_len = 0
                events = 0
                phase = None
                with client.stream(
                    "POST", f"/api/session/{session_id}/message/stream",
                    json={"message": turn["message"]},
                ) as r:
                    for line in r.iter_lines():
                        if not line.startswith("data: "):
                            continue
                        events += 1
                        try:
                            ev = json.loads(line[6:])
                        except json.JSONDecodeError:
                            continue
                        if ev.get("type") == "token":
                            text_len += len(ev.get("text", ""))
                        elif ev.get("type") == "done":
                            phase = ev.get("phase")
                        elif ev.get("type") == "error":
                            print(f"[{conv['id']}] turn {i} ERROR: "
                                  f"{ev.get('message')}", flush=True)
                # stream closed -> all governance calls for this turn are done
                elapsed = time.time() - t0
                calls = capture.drain()
                for r2 in calls:
                    write({"kind": "llm_call", "conversation": conv["id"],
                           "turn": i, "paused_before_s": pause, **r2})
                write({"kind": "turn", "conversation": conv["id"], "turn": i,
                       "message": turn["message"], "elapsed_s": round(elapsed, 2),
                       "streamed_chars": text_len, "phase": phase,
                       "llm_calls": len(calls), "paused_before_s": pause,
                       "session_id": session_id, "ts": time.time()})
                print(f"[{conv['id']}] turn {i}/{len(turns)} done "
                      f"({elapsed:.1f}s, {len(calls)} llm calls)", flush=True)
                time.sleep(3)
    out.close()
    print(f"raw log written: {out_path}", flush=True)


def price_for(model, table):
    for prefix, rates in table.items():
        if model.startswith(prefix):
            return rates
    return None


def dollars(rec, table):
    rates = price_for(rec["model"], table)
    if rates is None:
        return None
    i, o, w, r = rates
    return (rec["input_tokens"] * i + rec["output_tokens"] * o
            + rec["cache_creation_input_tokens"] * w
            + rec["cache_read_input_tokens"] * r) / 1_000_000


def billed(rec):
    """Dollars at the rates actually billed today (intro where in effect)."""
    merged = {**PRICING_STANDARD, **PRICING_INTRO}
    return dollars(rec, merged)


def report(raw_path):
    calls, turns = [], []
    for line in Path(raw_path).read_text(encoding="utf-8").splitlines():
        rec = json.loads(line)
        (calls if rec["kind"] == "llm_call" else turns).append(rec)

    def agg(rows):
        a = {"n": 0, "input": 0, "output": 0, "cache_w": 0, "cache_r": 0,
             "usd_std": 0.0, "usd_billed": 0.0}
        for r in rows:
            a["n"] += 1
            a["input"] += r["input_tokens"]
            a["output"] += r["output_tokens"]
            a["cache_w"] += r["cache_creation_input_tokens"]
            a["cache_r"] += r["cache_read_input_tokens"]
            a["usd_std"] += dollars(r, PRICING_STANDARD) or 0.0
            a["usd_billed"] += billed(r) or 0.0
        return a

    print("# B-COST — cache-aware cost baseline, current system (2026-07)\n")
    print("Generated deterministically from the committed raw log by "
          "`scripts/cost_baseline_runner.py --report`. Fixed conversation set: "
          "`scripts/cost_baseline_conversations.json` (40 turns; sources cited there).")
    print("Pricing: standard rates as the primary figure; `billed` applies "
          "claude-sonnet-5's intro pricing ($2/$10 per MTok) in effect through "
          "2026-08-31. Cache write = 1.25x input (5-min TTL); cache read = 0.1x.\n")

    total = agg(calls)
    n_turns = len([t for t in turns if t["turn"] > 0])
    print(f"**Totals: {total['n']} LLM calls across {n_turns} participant turns "
          f"+ {len([t for t in turns if t['turn'] == 0])} session starts.** "
          f"input={total['input']:,} output={total['output']:,} "
          f"cache_write={total['cache_w']:,} cache_read={total['cache_r']:,} "
          f"tokens. **${total['usd_std']:.4f} standard** "
          f"(${total['usd_billed']:.4f} billed at current intro rates). "
          f"Per participant turn: ${total['usd_std']/max(n_turns,1):.4f} standard.\n")

    print("## Per call site (label x model)\n")
    print("| label | model | calls | input | output | cache_write | cache_read | $ std | $ billed |")
    print("|---|---|---|---|---|---|---|---|---|")
    keys = sorted({(c["label"], c["model"]) for c in calls})
    for label, model in keys:
        a = agg([c for c in calls if c["label"] == label and c["model"] == model])
        print(f"| {label} | {model} | {a['n']} | {a['input']:,} | {a['output']:,} "
              f"| {a['cache_w']:,} | {a['cache_r']:,} | {a['usd_std']:.4f} "
              f"| {a['usd_billed']:.4f} |")

    print("\n## Per conversation\n")
    print("| conversation | turns | calls | input | output | cache_write | cache_read | $ std | $/turn std |")
    print("|---|---|---|---|---|---|---|---|---|")
    for conv in sorted({c["conversation"] for c in calls}):
        a = agg([c for c in calls if c["conversation"] == conv])
        nt = len([t for t in turns if t["conversation"] == conv and t["turn"] > 0])
        print(f"| {conv} | {nt} | {a['n']} | {a['input']:,} | {a['output']:,} "
              f"| {a['cache_w']:,} | {a['cache_r']:,} | {a['usd_std']:.4f} "
              f"| {a['usd_std']/max(nt,1):.4f} |")

    print("\n## Per turn\n")
    print("| conversation | turn | calls | input | output | cache_write | cache_read | $ std | elapsed_s | paused_before_s |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for t in turns:
        rows = [c for c in calls
                if c["conversation"] == t["conversation"] and c["turn"] == t["turn"]]
        a = agg(rows)
        print(f"| {t['conversation']} | {t['turn']} | {a['n']} | {a['input']:,} "
              f"| {a['output']:,} | {a['cache_w']:,} | {a['cache_r']:,} "
              f"| {a['usd_std']:.4f} | {t.get('elapsed_s', '')} "
              f"| {t.get('paused_before_s', 0)} |")

    # Cache-TTL observation: the deliberately paused turn vs its neighbors
    paused = [t for t in turns if t.get("paused_before_s", 0) > 0]
    if paused:
        print("\n## Cache-TTL observation (deliberate >5-min pause)\n")
        for t in paused:
            conv = t["conversation"]

            def main_calls(turn_no):
                return [c for c in calls if c["conversation"] == conv
                        and c["turn"] == turn_no and c["label"] == "main_response"]

            print(f"Conversation `{conv}`, pause of {t['paused_before_s']}s "
                  f"before turn {t['turn']} (cache TTL is 5 min):\n")
            print("| turn | main_response cache_read | cache_write | input |")
            print("|---|---|---|---|")
            for n in (t["turn"] - 1, t["turn"], t["turn"] + 1):
                rows = main_calls(n)
                if rows:
                    a = agg(rows)
                    print(f"| {n} | {a['cache_r']:,} | {a['cache_w']:,} | {a['input']:,} |")
        print("\nExpected shape: the post-pause turn shows cache_read collapsing "
              "toward 0 and cache_write re-paying the prefix; neighbors show "
              "warm reads. The table above is the measurement, not the claim.")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--run", action="store_true")
    p.add_argument("--report")
    p.add_argument("--limit-conversations", type=int, default=0)
    p.add_argument("--limit-turns", type=int, default=0)
    p.add_argument("--out", default="cost_baseline_raw.jsonl")
    args = p.parse_args()
    if args.run:
        run(args.limit_conversations, args.limit_turns, args.out)
    elif args.report:
        report(args.report)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
