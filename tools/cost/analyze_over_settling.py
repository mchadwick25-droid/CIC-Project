#!/usr/bin/env python3
"""Decide the OVER_SETTLING screen's sensitivity from real traffic.

The two-stage design (_screen_over_settling -> _adjudicate_over_settling) is
deliberately tuned to over-flag, on the reasoning that only a miss is
unrecoverable. app/over_settling_logging.py exists to measure whether that
still makes sense on ordinary conversation, and states the rule this script
enforces: tightening the screen trades directly against Article 5 rigor and
is "not a decision to make on a guess".

This turns those log lines into the decision. It reports the fire rate and
the confirm rate, and prices the two-stage design against the alternatives
using the measured token shape.

    python3 tools/cost/analyze_over_settling.py <logfile> [--turns N]

THE ECONOMICS
-------------
The screen costs ~869 prompt tokens plus the response, on EVERY turn. The
adjudicator costs an 8,831-token cached head (measured, fleet mean, via
count_tokens) plus a ~2,600-token uncached tail, but only on turns the
screen flags. A gate is only worth paying for if it turns work away often
enough to cover its own cost - and this one does not, past a fire rate of
about 60%. Above that, running the adjudicator unconditionally is cheaper
AND has no screen false-negatives.

Makes no API calls.
"""
from __future__ import annotations
import argparse, re, sys
from collections import defaultdict

H_IN, H_OUT, READ, WRITE = 1.0, 5.0, 0.1, 2.0
HEAD, TAIL, SCREEN_IN, OUT = 8831, 2598, 1199, 60   # tokens; measured 2026-08-16
TURNS_PER_SESSION = 12
LINE = re.compile(r"\[over_settling_decision\]\s+world_id=(\S+)\s+screened=(\S+)\s+confirmed=(\S+)")


def adj_cost_per_turn(fire_rate: float) -> float:
    n = TURNS_PER_SESSION * fire_rate
    if n <= 0:
        return 0.0
    write = HEAD * H_IN * WRITE / 1e6
    read = max(n - 1, 0) * HEAD * H_IN * READ / 1e6
    body = n * TAIL * H_IN / 1e6 + n * OUT * H_OUT / 1e6
    return (write + read + body) / TURNS_PER_SESSION


SCREEN_COST = SCREEN_IN * H_IN / 1e6 + OUT * H_OUT / 1e6


def break_even() -> float:
    target = adj_cost_per_turn(1.0)
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if adj_cost_per_turn(mid) + SCREEN_COST < target:
            lo = mid
        else:
            hi = mid
    return lo


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """95% Wilson score interval for k successes in n trials.

    Wilson rather than the normal approximation because the whole question
    here is whether a rate near 0.6-0.8 is distinguishable from a threshold
    on a sample of a few dozen - exactly where the normal approximation is
    worst and can put the bound above 1.0.
    """
    if n <= 0:
        return 0.0, 1.0
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z / d * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)
    return max(0.0, c - h), min(1.0, c + h)


def _n_to_resolve(p: float, threshold: float, cap: int = 2000) -> int | None:
    """Smallest n at which an observed rate of p would clear `threshold`.

    Answers "how many more turns" honestly instead of quoting a round
    number: it walks n upward until the Wilson interval around p stops
    straddling the break-even. Returns None if that never happens below
    `cap`, which is the real finding when p sits on the threshold.
    """
    for n in range(10, cap + 1, 2):
        lo, hi = wilson(round(p * n), n)
        if threshold < lo or threshold > hi:
            return n
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("logfile")
    ap.add_argument("--hours-per-month", type=float, default=1000.0)
    a = ap.parse_args()
    src = sys.stdin if a.logfile == "-" else open(a.logfile, encoding="utf-8")

    per = defaultdict(lambda: {"turns": 0, "screened": 0,
                               "confirmed": 0, "cleared": 0, "inconclusive": 0})
    for raw in src:
        m = LINE.search(raw)
        if not m:
            continue
        world, screened, confirmed = m.group(1), m.group(2) == "True", m.group(3)
        d = per[world]
        d["turns"] += 1
        if screened:
            d["screened"] += 1
            d["confirmed" if confirmed == "True" else
              "cleared" if confirmed == "False" else "inconclusive"] += 1

    if not per:
        sys.exit("no [over_settling_decision] lines found")

    tot = {k: sum(d[k] for d in per.values())
           for k in ("turns", "screened", "confirmed", "cleared", "inconclusive")}

    print(f"{'world':26}{'turns':>7}{'fired':>7}{'fire%':>7}{'confirm%':>10}{'incon.':>8}")
    for w, d in sorted(per.items()):
        fr = d["screened"] / d["turns"] if d["turns"] else 0
        cr = d["confirmed"] / d["screened"] if d["screened"] else 0
        print(f"{w[:25]:26}{d['turns']:7}{d['screened']:7}{fr:7.0%}{cr:10.0%}{d['inconclusive']:8}")
    fire = tot["screened"] / tot["turns"] if tot["turns"] else 0
    conf = tot["confirmed"] / tot["screened"] if tot["screened"] else 0
    print(f"{'ALL':26}{tot['turns']:7}{tot['screened']:7}{fire:7.0%}{conf:10.0%}"
          f"{tot['inconclusive']:8}")

    be = break_even()
    now = adj_cost_per_turn(fire) + SCREEN_COST
    nogate = adj_cost_per_turn(1.0)
    yr = lambda c: c * 12 * a.hours_per_month * 12
    print(f"\nCOST at the measured fire rate ({fire:.0%})")
    print(f"  two-stage as built     ${now:.5f}/turn   ${yr(now):,.0f}/yr")
    print(f"  no screen, adjudicate  ${nogate:.5f}/turn   ${yr(nogate):,.0f}/yr")
    print(f"  screen break-even fire rate: {be:.0%}")

    lo, hi = wilson(tot["screened"], tot["turns"])
    print(f"\n  fire rate {fire:.0%}, 95% CI {lo:.0%}-{hi:.0%} on {tot['turns']} turns")

    print("\nVERDICT")
    if lo <= be <= hi:
        # The sample size that matters is not a round number, it is whatever
        # separates the observed rate from the break-even. A rate far from
        # the threshold settles in a few dozen turns; one near it may never
        # settle at any affordable sample - and that itself is the answer
        # (the two designs cost the same, so pick on rigor, not on price).
        print(f"  INCONCLUSIVE. The break-even ({be:.0%}) lies inside the confidence")
        print(f"  interval ({lo:.0%}-{hi:.0%}), so this sample cannot say which side the")
        print("  true fire rate falls on. The screen's sensitivity trades directly")
        print("  against Article 5 rigor; do not retune on this.")
        need = _n_to_resolve(fire, be)
        if need:
            print(f"  At the observed rate, ~{need} turns would resolve it "
                  f"({tot['turns']} so far).")
        else:
            print("  At the observed rate no affordable sample resolves it - which")
            print("  means the two designs cost about the same. Decide on rigor.")
    elif fire > be:
        print(f"  The screen fires more often ({fire:.0%}) than it can pay for ({be:.0%}).")
        print(f"  It is costing ${yr(now - nogate):,.0f}/yr against adjudicating every turn,")
        print("  and every screen false-negative is a miss the adjudicator never sees.")
        print("  Either retune the screen below the break-even, or fold detection into")
        print("  the adjudicator and drop the stage. Both need this sample to justify.")
    else:
        print(f"  The screen pays for itself: fires {fire:.0%}, break-even {be:.0%}. Leave it.")
    if tot["screened"] and conf < 0.35:
        clo, chi = wilson(tot["confirmed"], tot["screened"])
        print(f"  Confirm rate is {conf:.0%} (95% CI {clo:.0%}-{chi:.0%}) - "
              f"{tot['cleared']} of {tot['screened']} flags cleared.")
        print("  That is the screen's designed-in false-positive rate. Judge it against")
        print("  what a miss costs, not against the flag count.")


if __name__ == "__main__":
    main()
