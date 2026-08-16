#!/usr/bin/env python3
"""Price a CiC usage log correctly, and report whether prompt caching is
actually paying off.

Reads the `[llm_usage]` lines app/usage_logging.py emits and reports true
spend, cache effectiveness, and the pooling factor - the three things that
were invisible when a whole session concluded the system cost $1.09/hour
when it cost about half that.

THE ARITHMETIC THAT MATTERS
---------------------------
LangChain's usage_metadata["input_tokens"] is the TOTAL input, with
cache_read and cache_creation as SUBSETS of it. The raw Anthropic block
reports the same fields as ADDITIVE buckets, where input_tokens is the
uncached remainder only. Verified live 2026-08-16: one non-streamed call
reported input_tokens=115 raw and 17,680 via LangChain, for cache_read
17,565.

Pricing input_tokens at the full rate and then ADDING cache_read at the read
rate therefore charges the cached prefix twice, once at 1x and again at 0.1x.
On a realistic CiC turn that overstates main_response by ~2.6x.

    uncached = input_tokens - cache_read - cache_creation

CACHE WRITES ARE NOT ONE PRICE
------------------------------
A write is 2x the input rate at a 1h TTL and 1.25x at 5m. Same token count
either way, so cache_creation_input_tokens alone cannot be priced. This
reads cache_creation_1h/_5m where the API supplied them (non-streamed calls
only) and falls back to the logged cache_ttl otherwise.

Usage:
    python3 tools/cost/analyze_usage_log.py <logfile> [--hours-per-month 1000]
    ... | python3 tools/cost/analyze_usage_log.py -
"""
from __future__ import annotations
import argparse, re, sys
from collections import defaultdict

# $ per million tokens. Sonnet 5 verified flat $2/$10 on 2026-08-16.
PRICES = {
    "claude-sonnet-5":            (2.0, 10.0),
    "claude-opus-5":              (5.0, 25.0),
    "claude-haiku-4-5":           (1.0, 5.0),
    "claude-haiku-4-5-20251001":  (1.0, 5.0),
    "claude-sonnet-4-6":          (3.0, 15.0),
}
READ_MULT = 0.1
WRITE_MULT = {"1h": 2.0, "5m": 1.25}

LINE = re.compile(r"\[llm_usage\]\s+(.*)$")
FIELD = re.compile(r"(\w+)=(\S+)")


def parse(stream):
    for raw in stream:
        m = LINE.search(raw)
        if not m:
            continue
        f = dict(FIELD.findall(m.group(1)))
        if "input_tokens" not in f:
            continue
        def i(k):
            try:
                return int(f.get(k, 0))
            except ValueError:
                return 0
        yield {
            "label": f.get("label", "?"), "model": f.get("model", "?"),
            "session": f.get("session_id", "None"), "ttl": f.get("cache_ttl", "1h"),
            "in": i("input_tokens"), "out": i("output_tokens"),
            "cc": i("cache_creation_input_tokens"), "cr": i("cache_read_input_tokens"),
            "cc1h": i("cache_creation_1h"), "cc5m": i("cache_creation_5m"),
        }


def price(r):
    pin, pout = PRICES.get(r["model"], (None, None))
    if pin is None:
        return None, None
    uncached = max(r["in"] - r["cr"] - r["cc"], 0)
    if r["cc1h"] or r["cc5m"]:
        write = (r["cc1h"] * WRITE_MULT["1h"] + r["cc5m"] * WRITE_MULT["5m"])
    else:
        write = r["cc"] * WRITE_MULT.get(r["ttl"], 2.0)
    true = (uncached * pin + r["cr"] * pin * READ_MULT
            + write * pin + r["out"] * pout) / 1e6
    naive = (r["in"] * pin + r["cr"] * pin * READ_MULT
             + r["cc"] * pin * WRITE_MULT.get(r["ttl"], 2.0) + r["out"] * pout) / 1e6
    return true, naive


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("logfile")
    ap.add_argument("--hours-per-month", type=float, default=1000.0)
    ap.add_argument("--turns-per-hour", type=float, default=12.0)
    a = ap.parse_args()
    src = sys.stdin if a.logfile == "-" else open(a.logfile, encoding="utf-8")

    rows = list(parse(src))
    if not rows:
        sys.exit("no [llm_usage] lines found")

    by = defaultdict(lambda: {"n": 0, "true": 0.0, "naive": 0.0,
                              "cr": 0, "cc": 0, "unc": 0, "out": 0})
    unknown, sessions, turns = set(), set(), set()
    for r in rows:
        t, n = price(r)
        if t is None:
            unknown.add(r["model"]); continue
        d = by[r["label"]]
        d["n"] += 1; d["true"] += t; d["naive"] += n
        d["cr"] += r["cr"]; d["cc"] += r["cc"]
        d["unc"] += max(r["in"] - r["cr"] - r["cc"], 0); d["out"] += r["out"]
        sessions.add(r["session"])
        if r["label"] == "main_response":
            turns.add((r["session"], d["n"]))

    n_turns = by["main_response"]["n"] or 1
    tot_true = sum(d["true"] for d in by.values())
    tot_naive = sum(d["naive"] for d in by.values())

    print(f"{len(rows)} calls | {len(sessions)} session(s) | "
          f"{by['main_response']['n']} representative turns\n")
    print(f"{'label':34}{'calls':>6}{'true $':>10}{'as-if-summed':>14}{'/turn':>9}")
    for lab, d in sorted(by.items(), key=lambda x: -x[1]["true"]):
        print(f"{lab[:33]:34}{d['n']:6}{d['true']:10.4f}{d['naive']:14.4f}"
              f"{d['true']/n_turns:9.5f}")
    print(f"{'TOTAL':34}{len(rows):6}{tot_true:10.4f}{tot_naive:14.4f}"
          f"{tot_true/n_turns:9.5f}")

    if tot_true:
        print(f"\ndouble-count factor if the three token fields are summed: "
              f"{tot_naive/tot_true:.2f}x")

    cr = sum(d["cr"] for d in by.values())
    cc = sum(d["cc"] for d in by.values())
    unc = sum(d["unc"] for d in by.values())
    tot_in = cr + cc + unc
    if tot_in:
        print(f"\nCACHE")
        print(f"  read      {cr:>12,} tok   {100*cr/tot_in:5.1f}% of input")
        print(f"  written   {cc:>12,} tok   {100*cc/tot_in:5.1f}%")
        print(f"  uncached  {unc:>12,} tok   {100*unc/tot_in:5.1f}%")
        if cc:
            print(f"  pooling factor (read/write): {cr/cc:6.1f}x   "
                  f"-- 1x means every write served exactly one read;")
            print(f"  {'':29}higher is better, and rises with concurrency")
        elif cr:
            print("  pooling factor: no writes in this log - every call read a "
                  "cache written earlier")
        else:
            print("  *** NO CACHE ACTIVITY AT ALL - caching is not working ***")

    hourly = tot_true / n_turns * a.turns_per_hour
    print(f"\nPROJECTION  ${hourly:.3f}/hour  "
          f"${hourly*a.hours_per_month:,.0f}/month  "
          f"${hourly*a.hours_per_month*12:,.0f}/year  "
          f"@ {a.hours_per_month:,.0f} h/mo")
    if unknown:
        print(f"\nunpriced model(s), excluded: {', '.join(sorted(unknown))}")


if __name__ == "__main__":
    main()
