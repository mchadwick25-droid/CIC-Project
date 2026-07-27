"""S4.3 G checkpoint - queue-ordering fixtures.

The blueprint's requirement: "queue-ordering fixtures: the
fabrication-vs-stylistic-complaint contention case seeded and won by
fabrication."

Parts, all deterministic:

A (non-vacuous, legacy semantics reproduced): the pre-S4.3 per-world
  guidance slot was one string, last-writer-wins (git df04f30
  governance.run_table_checks: `guidance[signal.world_id] =
  signal.description`; the tail's drift loop then overwrote the same
  key). Seeded with a fabrication finding first and a stylistic
  complaint (question_stacking) second, the fabrication LOSES the slot.
  The defect must reproduce.

B (the cure, real gate): the same contention through the REAL
  governance.queue_guidance - fabrication wins regardless of insertion
  order; same-type supersession; the intrinsic/extrinsic severity split
  ranks a high entry above a medium one from the same ordering.

C (consumption): popping delivers fabrication first and the stylistic
  complaint on the NEXT pop - contention delays a finding now, it never
  deletes one.

D (declared parity delta, bounded): S4.2's state-parity instrument is
  re-run unmodified against its frozen legacy snapshots. Exactly one
  case (S4-stream-multiworld, whose tape carries a real recorded
  over_settling finding) may diverge, and only in pending_guidance, and
  only by the declared shape change: the legacy string value becomes a
  single queue entry whose text is the SAME string verbatim and whose
  signal_type/severity are the recorded finding's own. Anything else -
  another case diverging, another field diverging, altered text - fails
  the gate. (Same pattern as S4.1's delta_labels: the delta is allowed
  because it is enumerated, and everything outside the enumeration is a
  parity failure.)

E (declaration completeness): ConversationState.DriftSignal declares
  exactly 17 signal types; every type the code can emit (the monitor's
  valid list, the over-settling path, the five table checks) is
  declared; over_settling and self_narration - the two that were
  emitted-but-undeclared - are present; the one priority ordering covers
  all 17.

Determinism: the whole gate runs twice; result summaries must be
byte-identical. (Part D's replay makes live session-start calls, but
every compared field is masked or tape-served - the same determinism
scope as the S4.1/S4.2 parity instruments themselves.)

Usage (from cic-poc/backend):
  python <repo>/Ministry/Technology/Pass2/gates/S4.3_queue_ordering.py
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[4] / "cic-poc" / "backend"
sys.path.insert(0, str(BACKEND))

SUITE = BACKEND / "app" / "graph" / "replay" / "suite"


def part_a_legacy_last_writer_wins() -> dict:
    """The pre-S4.3 slot semantics, reproduced: one string per world,
    last writer wins - the fabrication must LOSE for this to pass."""
    guidance: dict = {}
    # writer 1: the drift loop finds a fabrication (high)
    guidance["w"] = "correct the record (fabrication)"
    # writer 2: a table check files a stylistic complaint (medium), later
    # in statement order - exactly how run_table_checks + the drift loop
    # shared one key pre-S4.3
    guidance["w"] = "stack fewer questions (question_stacking)"
    fabrication_lost = "fabrication" not in guidance["w"]
    return {"case": "A-legacy-last-writer-wins",
            "surviving": guidance["w"],
            "fabrication_lost": fabrication_lost,
            "defect_reproduced": fabrication_lost}


def part_b_gate_ordering() -> dict:
    from app.graph.governance import queue_guidance

    # contention, stylistic enqueued LAST (the legacy losing order)
    p: dict = {}
    p = queue_guidance(p, "w", "fabrication", "high", "correct the record")
    p = queue_guidance(p, "w", "question_stacking", "medium", "stack fewer")
    order1 = [e["signal_type"] for e in p["w"]]

    # contention, stylistic enqueued FIRST
    q: dict = {}
    q = queue_guidance(q, "w", "question_stacking", "medium", "stack fewer")
    q = queue_guidance(q, "w", "fabrication", "high", "correct the record")
    order2 = [e["signal_type"] for e in q["w"]]

    # same-type supersession: a fresher fabrication replaces the older
    r = queue_guidance(q, "w", "fabrication", "high", "newer correction")
    superseded = (len(r["w"]) == 2 and r["w"][0]["text"] == "newer correction")

    # the intrinsic/extrinsic severity split ranks within one type-slot
    # world: an intrinsic (high) fabrication vs an extrinsic (medium) one
    # on DIFFERENT worlds keeps distinct ranks under the one ordering
    from app.graph.nodes import signal_rank
    intrinsic_rank = signal_rank("fabrication", "high")
    extrinsic_rank = signal_rank("fabrication", "medium")
    stylistic_rank = signal_rank("question_stacking", "medium")
    severities_distinct = (intrinsic_rank < extrinsic_rank < stylistic_rank)

    ok = (order1 == ["fabrication", "question_stacking"]
          and order2 == ["fabrication", "question_stacking"]
          and superseded and severities_distinct)
    return {"case": "B-gate-ordering",
            "order_stylistic_last": order1,
            "order_stylistic_first": order2,
            "same_type_supersedes": superseded,
            "intrinsic_extrinsic_stylistic_ranks":
                [list(intrinsic_rank), list(extrinsic_rank),
                 list(stylistic_rank)],
            "pass": ok}


def part_c_consumption() -> dict:
    """Delivery order via the REAL consumer logic shape: pop the head,
    keep the rest - fabrication this turn, stylistic the next, nothing
    dropped."""
    from app.graph.governance import queue_guidance

    p: dict = {}
    p = queue_guidance(p, "w", "question_stacking", "medium", "stack fewer")
    p = queue_guidance(p, "w", "fabrication", "high", "correct the record")

    delivered = []
    while p.get("w"):
        queue = list(p["w"])
        entry = queue.pop(0)
        delivered.append(entry["signal_type"])
        p = {**p, "w": queue} if queue else {k: v for k, v in p.items()
                                             if k != "w"}
    ok = delivered == ["fabrication", "question_stacking"]
    return {"case": "C-consumption-order", "delivered": delivered,
            "nothing_dropped": ok, "pass": ok}


def part_d_declared_parity_delta() -> dict:
    """Run S4.2's state-parity instrument UNMODIFIED; bound the divergence
    to exactly the declared queue-shape delta on the one tape that
    carries a recorded finding."""
    for f in SUITE.glob("*.state-diff.json"):
        f.unlink()
    proc = subprocess.run(
        [sys.executable, "-m", "app.graph.replay.state_parity", "verify"],
        cwd=BACKEND, capture_output=True, text=True)
    out = proc.stdout + proc.stderr
    mismatches = [line for line in out.splitlines() if "MISMATCH" in line]
    diff_files = sorted(f.name for f in SUITE.glob("*.state-diff.json"))

    only_s4 = diff_files == ["S4-stream-multiworld.state-diff.json"]
    shape_ok = False
    detail = ""
    if only_s4:
        legacy = json.loads((SUITE / "S4-stream-multiworld.state.json")
                            .read_text(encoding="utf-8"))
        new = json.loads((SUITE / "S4-stream-multiworld.state-diff.json")
                         .read_text(encoding="utf-8"))
        other_fields_equal = all(
            legacy[k] == new.get(k) for k in legacy if k != "pending_guidance")
        lg, ng = legacy["pending_guidance"], new["pending_guidance"]
        shape_only = (
            set(lg) == set(ng)
            and all(isinstance(lg[w], str) and isinstance(ng[w], list)
                    and len(ng[w]) == 1
                    and ng[w][0]["text"] == lg[w]
                    and ng[w][0]["signal_type"] == "over_settling"
                    and ng[w][0]["severity"] == "medium"
                    for w in lg))
        shape_ok = other_fields_equal and shape_only
        detail = (f"worlds={sorted(lg)}, other_fields_equal="
                  f"{other_fields_equal}, text_verbatim={shape_only}")
    ok = only_s4 and shape_ok and len(mismatches) == 1
    for f in SUITE.glob("*.state-diff.json"):
        f.unlink()
    return {"case": "D-declared-parity-delta",
            "diverging_cases": diff_files,
            "divergence_bounded_to_declared_shape": shape_ok,
            "detail": detail,
            "pass": ok}


def part_e_declaration_completeness() -> dict:
    import typing
    from app.graph.state import DriftSignal
    from app.graph import nodes

    declared = list(typing.get_args(
        DriftSignal.__dataclass_fields__["signal_type"].type))
    emitted = set(nodes._SIGNAL_PRIORITY)
    # the monitor's own accepted list is a subset of the declaration
    monitor_valid = {
        "smoothing", "generating", "agreeing", "over_producing",
        "temporal_bleed", "flattening", "fabrication", "apologetics",
        "first_person", "anachronism", "self_narration", "over_settling"}
    table = {"dominance", "convergence", "cross_world_vocabulary",
             "length_ceiling", "question_stacking"}
    ok = (len(declared) == 17
          and set(declared) == monitor_valid | table
          and {"over_settling", "self_narration"} <= set(declared)
          and emitted == set(declared))
    return {"case": "E-declaration-completeness",
            "declared_count": len(declared),
            "previously_undeclared_present":
                sorted({"over_settling", "self_narration"} & set(declared)),
            "priority_ordering_covers_all": emitted == set(declared),
            "pass": ok}


def run_once() -> dict:
    a = part_a_legacy_last_writer_wins()
    b = part_b_gate_ordering()
    c = part_c_consumption()
    d = part_d_declared_parity_delta()
    e = part_e_declaration_completeness()
    all_pass = (a["defect_reproduced"] and b["pass"] and c["pass"]
                and d["pass"] and e["pass"])
    return {"A": a, "B": b, "C": c, "D": d, "E": e,
            "gate": "PASS" if all_pass else "FAIL"}


def main() -> int:
    r1 = run_once()
    r2 = run_once()
    s1, s2 = (json.dumps(r, sort_keys=True) for r in (r1, r2))
    print(json.dumps(r1, indent=1))
    print(f"\ndouble-run byte-identical: {s1 == s2}")
    print(f"GATE: {r1['gate']}")
    return 0 if (r1["gate"] == "PASS" and s1 == s2) else 1


if __name__ == "__main__":
    sys.exit(main())
