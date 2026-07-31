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

# app/length_ceiling_logging.py's line. One per representative turn in a
# HARD_CEILING_WORLDS world, covering all three outcomes - so a run's raw
# log carries the retry mechanism's fire rate, dead-zone rate, and
# first-draft word distribution directly, instead of leaving them to be
# reconstructed from token arithmetic afterwards.
CEILING_RE = re.compile(
    r"\[length_ceiling\] world_id=(?P<world_id>\S+) ceiling=(?P<ceiling>\d+) "
    r"trigger_multiple=(?P<trigger_multiple>[\d.]+) "
    r"first_draft_words=(?P<first_draft_words>\d+) outcome=(?P<outcome>\S+) "
    r"retry_words=(?P<retry_words>\S+) request_id=(?P<request_id>\S+) "
    r"session_id=(?P<session_id>\S+)"
)


class UsageCapture(logging.Handler):
    """Captures both instrumentation lines this baseline reads.

    One handler, two regexes, attached to both `cic.llm_usage` and
    `cic.length_ceiling`. Records carry a "kind" so run() can file them
    into the raw log under the right record type without re-parsing.
    """

    def __init__(self):
        super().__init__()
        self.records = []
        # NOT self.lock - logging.Handler owns that name (an RLock that
        # handle() acquires around emit()); overwriting it with a plain Lock
        # self-deadlocks the first time emit() tries to take it again.
        self._records_lock = threading.Lock()

    def emit(self, record):
        msg = record.getMessage()
        m = USAGE_RE.search(msg)
        if m:
            d = m.groupdict()
            entry = {
                "kind": "llm_call",
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
        else:
            m = CEILING_RE.search(msg)
            if not m:
                return
            d = m.groupdict()
            entry = {
                "kind": "length_ceiling",
                "ts": time.time(),
                "world_id": d["world_id"],
                "ceiling": int(d["ceiling"]),
                "trigger_multiple": float(d["trigger_multiple"]),
                "first_draft_words": int(d["first_draft_words"]),
                "outcome": d["outcome"],
                "retry_words": (None if d["retry_words"] == "None"
                                else int(d["retry_words"])),
                "request_id": d["request_id"],
                "session_id": d["session_id"],
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
    logging.getLogger("cic.length_ceiling").addHandler(capture)

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
            # Possession secret minted by /api/session/start (app/session_auth.py).
            # Every later call on this session requires it as X-Session-Token or
            # the endpoint returns 403 - without this header --run cannot reach
            # a single turn. Added 2026-07-31; the 2026-07-26 raw log predates
            # the ownership check, which is why that run needed no token.
            headers = {"X-Session-Token": resp.json()["session_token"]}
            # session-start LLM calls (facilitator reception/handoff via graph)
            for r in capture.drain():
                # "kind" named first so a new raw log's field order matches
                # the committed 2026-07 one; **r then supplies its value
                # (a repeated key keeps its first position in a dict literal).
                write({"kind": r["kind"], "conversation": conv["id"], "turn": 0,
                       "turn_label": "session_start", **r})
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
                    json={"message": turn["message"]}, headers=headers,
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
                drained = capture.drain()
                for r2 in drained:
                    write({"kind": r2["kind"], "conversation": conv["id"],
                           "turn": i, "paused_before_s": pause, **r2})
                # llm_calls stays a count of LLM calls only - the ceiling
                # records are observations of the same turn, not extra calls,
                # and folding them in would silently change what every
                # existing per-turn call count in the committed report means.
                calls = [r2 for r2 in drained if r2["kind"] == "llm_call"]
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
    # LangChain's usage_metadata["input_tokens"] - what usage_logging.py
    # records as this row's input_tokens - is already Anthropic's raw
    # input_tokens PLUS cache_read PLUS cache_creation added back in.
    # Verified against the installed langchain_anthropic source
    # (_create_usage_metadata: "Anthropic's input_tokens excludes cached
    # tokens, so we manually add cache_read and cache_creation tokens to get
    # the true total"). usage_logging.py takes the cache figures from
    # Anthropic's RAW usage block, so the two are directly comparable.
    #
    # Pricing that inflated figure at the full input rate and then adding
    # cache_read/cache_creation again at their own rates bills every cached
    # token twice. Subtract them back out to recover the genuinely uncached
    # span that Anthropic charges at the full input rate.
    uncached_input = (rec["input_tokens"] - rec["cache_read_input_tokens"]
                       - rec["cache_creation_input_tokens"])
    return (uncached_input * i + rec["output_tokens"] * o
            + rec["cache_creation_input_tokens"] * w
            + rec["cache_read_input_tokens"] * r) / 1_000_000


def billed(rec):
    """Dollars at the rates actually billed today (intro where in effect)."""
    merged = {**PRICING_STANDARD, **PRICING_INTRO}
    return dollars(rec, merged)


# --- length-ceiling retry mechanism -----------------------------------------
#
# HARD_CEILING_WORLDS / RETRY_TRIGGER_MULTIPLES as deployed in
# app/graph/nodes.py. Duplicated here rather than imported because --report
# must run with no app import and no API key, and because a report about a
# past run has to be able to state the values in force at report time even
# if the code has since moved on. Kept in sync by
# gates/S6.2_length_ceiling_observability_gate.py, which fails if it drifts.
CEILING_WORLDS = {
    "desert-monasticism": (60, 1.5),
    # Updated 180 -> 160 (S6.2/HAL freeze, 2026-07-31, Decision HAL-4): the
    # committed 2026-07 baseline log predates this change and was measured
    # against the old 180 ceiling - the values here are always nodes.py's
    # CURRENT state per this constant's own docstring above, not a
    # historical record of what was in force when any given raw log was
    # collected. A report run against the 2026-07 log will therefore
    # describe Hieronymian's ceiling as 160 even though it was 180 at
    # collection time - Hieronymian never seated in that fixed
    # conversation set anyway (see the retry-cost investigation memo), so
    # no committed report figure actually depends on this value being
    # historically accurate.
    "hieronymian-ascetic-literary": (160, 1.2),
    "alexandria-catechetical": (160, 1.2),
    "syriac-edessa-nisibis": (165, 1.2),
}

# Forensic detector for raw logs collected BEFORE app/length_ceiling_logging.py
# existed (the committed 2026-07 baseline is one). A length-ceiling retry is
# the same call made twice in a row inside one representative turn, with the
# discarded first draft and a fixed corrective message appended - so the
# second call's input_tokens exceed the first's by exactly the first call's
# output_tokens (the draft, re-tokenized) plus the corrective's own small,
# constant token cost, and the two calls read the identical cached prefix.
#
# Measured on the committed 2026-07 log the surplus is exactly 51 tokens on
# all 15 detected retries. The window below is deliberately much wider than
# 51 and the detected count is flat across it (verified 51..250 -> 15 every
# time), so the detector does not depend on the corrective's current wording.
RETRY_SURPLUS_MAX = 250


def _prefix(rec):
    """Total cached prompt prefix this call read or wrote."""
    return rec["cache_read_input_tokens"] + rec["cache_creation_input_tokens"]


def split_retry_calls(calls):
    """Split main_response calls into (first drafts, ceiling retries).

    Works on any raw log, with or without length_ceiling records - it reads
    only token counts, which every log has.
    """
    from collections import defaultdict
    by_turn = defaultdict(list)
    for c in calls:
        if c["label"] == "main_response":
            by_turn[(c["conversation"], c["turn"])].append(c)
    firsts, retries = [], []
    for key in sorted(by_turn):
        prev = None
        for c in sorted(by_turn[key], key=lambda r: r["ts"]):
            surplus = (None if prev is None else
                       c["input_tokens"] - prev["input_tokens"] - prev["output_tokens"])
            if (prev is not None and surplus is not None
                    and 0 < surplus <= RETRY_SURPLUS_MAX
                    and _prefix(prev) == _prefix(c)):
                retries.append((c, prev))
                prev = None          # a retry is never itself a first draft
            else:
                firsts.append(c)
                prev = c
    return firsts, retries


def attribute_worlds(calls, spec):
    """Map each main_response call to a world id from its cached prefix.

    Every representative's cached prefix is its own static system prompt,
    optionally plus one conditionally-present guidance block that gets its
    own cache breakpoint (see _cached_system_message in nodes.py). Each
    single-world conversation in the fixed set therefore pins exactly one
    world's static-prefix size, and a multi-world conversation's calls
    decode as (some pinned static size) + (0 | one block size), which
    identifies the speaker without the raw log carrying a world field.

    Returns {id(call): world_id}; calls that do not decode map to None
    rather than to a guess.
    """
    mains = [c for c in calls if c["label"] == "main_response"]
    conv_worlds = {c["id"]: c["world_ids"] for c in spec["conversations"]}
    prefixes = {_prefix(c) for c in mains}

    # 1. Pin one static size per single-world conversation. A single-world
    #    conversation carries no guidance block, so all its calls share one
    #    prefix; if they do not, that world is simply left unpinned rather
    #    than guessed at.
    statics = {}
    for conv, worlds in conv_worlds.items():
        if len(worlds) != 1:
            continue
        sizes = {_prefix(c) for c in mains if c["conversation"] == conv}
        if len(sizes) == 1:
            statics[sizes.pop()] = worlds[0]

    # 2. Recover the guidance-block sizes. A guidance block is the SAME text
    #    for every representative, so a real block size shows up added to at
    #    least two different worlds' statics. Requiring that is what keeps
    #    coincidental differences between two worlds' prefixes (e.g. one
    #    world's static minus another's) from being mistaken for a block and
    #    mis-attributing every call that follows.
    blocks = {0}
    for cand in {p - b for p in prefixes for b in statics if p - b > 0}:
        if sum(1 for b in statics if b + cand in prefixes) >= 2:
            blocks.add(cand)

    # 3. Any prefix still unexplained belongs to a world seen only at the
    #    multi-world table. Accept it only if every unexplained prefix
    #    reduces to ONE base and exactly one world is left unassigned -
    #    otherwise return None for those calls rather than guessing.
    unexplained = [p for p in prefixes
                   if not any(p - b in blocks for b in statics)]
    if unexplained:
        cands = {p - blk for p in unexplained for blk in blocks if p - blk > 0}
        bases = {c for c in cands
                 if all(any(p - c == blk for blk in blocks) or
                        any(p - b in blocks for b in statics)
                        for p in unexplained)}
        unseen = {w for ws in conv_worlds.values() for w in ws
                  if w not in statics.values()}
        if len(bases) == 1 and len(unseen) == 1:
            statics[bases.pop()] = unseen.pop()

    return {id(c): next((w for b, w in statics.items() if _prefix(c) - b in blocks),
                        None)
            for c in mains}


def report_length_ceiling(calls, ceiling_recs, spec):
    """The length-ceiling retry mechanism's frequency and cost."""
    firsts, retries = split_retry_calls(calls)
    if not firsts:
        return
    worlds = attribute_worlds(calls, spec) if spec else {}
    retry_calls = [r for r, _ in retries]

    print("\n## Length-ceiling retry mechanism\n")
    print("`stream_representative_turn` buffers the first draft for a "
          "HARD_CEILING_WORLDS world and regenerates once if it exceeds "
          "`ceiling x trigger_multiple`. Both calls log as `main_response`, so "
          "the split below is reconstructed from token arithmetic (see "
          "`split_retry_calls`) for logs collected before "
          "`app/length_ceiling_logging.py` existed, and read directly from "
          "`length_ceiling` records when the log has them.\n")

    print("| world | ceiling x trigger | rep turns | retries fired | fire rate | "
          "retry $ std | discarded draft output tok |")
    print("|---|---|---|---|---|---|---|")
    seen = sorted({w for w in worlds.values() if w}, key=str)
    for w in seen:
        wf = [c for c in firsts if worlds.get(id(c)) == w]
        wr = [(r, p) for r, p in retries if worlds.get(id(r)) == w]
        c, t = CEILING_WORLDS.get(w, (None, None))
        spec_s = f"{c} x {t} = {c * t:.0f}w" if c else "(no ceiling)"
        usd = sum(dollars(r, PRICING_STANDARD) or 0.0 for r, _ in wr)
        print(f"| {w} | {spec_s} | {len(wf)} | {len(wr)} | "
              f"{(len(wr)/len(wf) if wf else 0):.1%} | {usd:.4f} | "
              f"{sum(p['output_tokens'] for _, p in wr):,} |")

    absent = [w for w in CEILING_WORLDS if w not in seen]
    if absent:
        print(f"\nCeilinged worlds with no representative turn in this log at "
              f"all: {', '.join(sorted(absent))} — the fixed conversation set "
              f"does not seat them, so this log measures nothing about them.")
    if not ceiling_recs:
        print("\n**Read a 0% fire rate here carefully.** Without "
              "`length_ceiling` records, a zero means only that no second "
              "`main_response` call was made — it cannot distinguish \"the "
              "world's drafts stayed under its trigger\" from \"the world was "
              "not yet in HARD_CEILING_WORLDS when this log was collected.\" "
              "Check the ceiling's own commit date against the run date before "
              "citing a zero as a measurement of the mechanism.")

    tot = sum(dollars(c, PRICING_STANDARD) or 0.0 for c in calls)
    rtot = sum(dollars(r, PRICING_STANDARD) or 0.0 for r in retry_calls)
    mtot = sum(dollars(c, PRICING_STANDARD) or 0.0
               for c in calls if c["label"] == "main_response")
    print(f"\n**Retry spend: ${rtot:.4f} of ${tot:.4f} whole-baseline standard "
          f"({rtot/tot:.2%}), ${mtot:.4f} of main_response-labelled spend "
          f"({rtot/mtot:.2%}).** {len(retry_calls)} retries over {len(firsts)} "
          f"representative turns.\n")

    print("| conversation | rep turns | retries | fire rate | conv $ std | "
          "retry $ std | retry share of conversation |")
    print("|---|---|---|---|---|---|---|")
    for conv in sorted({c["conversation"] for c in calls}):
        cf = [c for c in firsts if c["conversation"] == conv]
        cr = [r for r in retry_calls if r["conversation"] == conv]
        cusd = sum(dollars(c, PRICING_STANDARD) or 0.0
                   for c in calls if c["conversation"] == conv)
        rusd = sum(dollars(r, PRICING_STANDARD) or 0.0 for r in cr)
        print(f"| {conv} | {len(cf)} | {len(cr)} | "
              f"{(len(cr)/len(cf) if cf else 0):.1%} | {cusd:.4f} | {rusd:.4f} "
              f"| {(rusd/cusd if cusd else 0):.1%} |")

    # Where a retry's dollars actually go - the number that decides which
    # cost options are worth anything.
    ui = sum((r["input_tokens"] - _prefix(r)) * 3.0 / 1e6 for r in retry_calls)
    cp = sum(r["cache_read_input_tokens"] * 0.30 / 1e6
             + r["cache_creation_input_tokens"] * 3.75 / 1e6 for r in retry_calls)
    ow = sum(r["output_tokens"] * 15.0 / 1e6 for r in retry_calls)
    if rtot:
        print(f"\nRetry cost decomposition (standard rates): uncached input "
              f"${ui:.4f} ({ui/rtot:.1%}), cached-prefix reads/writes "
              f"${cp:.4f} ({cp/rtot:.1%}), output ${ow:.4f} ({ow/rtot:.1%}).")

    if ceiling_recs:
        print("\n### Direct `length_ceiling` records (this run only)\n")
        print("| world | turns observed | under ceiling | dead zone | retried | "
              "fire rate | first-draft words min/median/max |")
        print("|---|---|---|---|---|---|---|")
        import statistics
        for w in sorted({r["world_id"] for r in ceiling_recs}):
            rs = [r for r in ceiling_recs if r["world_id"] == w]
            n = {k: sum(1 for r in rs if r["outcome"] == k)
                 for k in ("under_ceiling", "dead_zone", "retried")}
            words = sorted(r["first_draft_words"] for r in rs)
            print(f"| {w} | {len(rs)} | {n['under_ceiling']} | {n['dead_zone']} "
                  f"| {n['retried']} | {n['retried']/len(rs):.1%} | "
                  f"{words[0]}/{statistics.median(words):.0f}/{words[-1]} |")


def report(raw_path):
    calls, turns, ceiling_recs = [], [], []
    for line in Path(raw_path).read_text(encoding="utf-8").splitlines():
        rec = json.loads(line)
        if rec["kind"] == "llm_call":
            calls.append(rec)
        elif rec["kind"] == "length_ceiling":
            ceiling_recs.append(rec)
        else:
            turns.append(rec)

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

    # Appended after every pre-existing section, so a report regenerated from
    # an older raw log is byte-identical up to this point (asserted by
    # gates/S6.2_length_ceiling_observability_gate.py).
    try:
        spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    except OSError:
        spec = None
    report_length_ceiling(calls, ceiling_recs, spec)


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
