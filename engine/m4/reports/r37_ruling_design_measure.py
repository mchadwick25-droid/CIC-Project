"""R37 ruling design brief (Decision-Log.md Entry 69, Rulings-Pending.md
R37), report-only, no engine change. Mark's own ruling on
R37 (relayed 2026-09-23): a Representative may use outside knowledge of
a named-but-uncovered tradition to choose WHICH PART of its own record
to answer from only under two conditions - (a) it would have known of
that tradition in its own time (a world-level fact about which
neighbouring traditions fall inside the world's window and horizon), or
(b) the Facilitator's introduction or the participant revealed it in
THIS conversation, and then only what was actually said in the
transcript, nothing beyond it. Outside both, the pivot must come from
the question's own words alone. In every case, content about the other
tradition still never enters the answer from outside the record - that
stays the net's own job (R38, PR #436).

This script computes the real, code-derivable numbers the design brief
cites - it does not itself decide anything, propose a rule choice, or
touch engine code. Two parts:

PART 1 (design brief item 1) - a candidate world-level "known in its own
time" list, for the 11 admitted formation worlds, from data already in
records/worlds/*.yaml (time_window - zero invention) plus a scan of
each world's own already-vendored, already-built records for a genuine
textual reference to another tradition's own name (real, code-derivable
evidence, not asserted from outside general knowledge). See this
script's own docstring note below on why plain "prose fields only" is
used, not engine.prose.all_text: a first attempt against the full
recursive all_text() produced a false positive (desert's own record
mentioning a historical "Theophilus" - a different, 4th-century
Alexandrian bishop entirely - matched rzg's OWN 16th-century
representative's chosen name; rzg's own window, 1519-1650, does not
even overlap desert's, 320-430, so the two "Theophilus"es are two
worlds' own independent naming choices colliding, not evidence of
anything). Restricting the scan to real prose fields (the same
TEXT_LIKE_KEYS grounding_fooling_measure.py's own Corpus C already
uses, plus positions/tensions/modern_lens_note) removed that false
positive and left only genuine hits - shown below, still spot-check
this data before trusting it as this brief's own text says.

Window overlap is computed TWO ways, since Mark's own wording ("window
and horizon") is genuinely ambiguous and materially changes the count -
presented as a real, unresolved option, not resolved here:
  symmetric  - the two worlds' own time_window ranges literally overlap
               (a strict contemporary-only reading)
  asymmetric - the OTHER tradition's own window starts at or before
               THIS world's own window ends (a "no knowledge of the
               unknowable future, but ordinary retrospective historical
               awareness of an earlier or contemporary tradition is
               fine" reading - the only reading under which a 1519-1650
               world could ever discuss 150-400 Alexandria, exactly the
               shape 8 of today's 11 real battery probes need, see
               PART 2)

PART 2 (design brief item 4) - the real battery's own B-other-tradition
probe target (engine.m4.live_uncited_claims_battery._other_tradition_turn,
reproduced here read-only, not re-implemented differently) is
deterministic and registry-derived, so this needs no live call: for each
of the 11 worlds' own real probe target, whether it is defensible under
symmetric-(a), asymmetric-(a), and whether the bare NAME is present in
that probe's own text (trivially, by construction, since every probe
names its target directly - the real test (a) is meant to answer is
CONTENT-specific pivot defensibility, not bare-name presence; (b) is
what actually licenses using the bare name in an answer, not (a)).

Run: python3 -m engine.m4.reports.r37_ruling_design_measure
"""
import json
import pathlib
import sys
from datetime import date, datetime, timezone

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from engine.m1.registry import formation_world_keys, load_registry
from engine.m4 import evidence as ev
from engine.m4.uncited_claims import _demonym_forms

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
REPORTS_DIR = pathlib.Path(__file__).resolve().parent

# Same field allowlist grounding_fooling_measure.py's own Corpus C already
# uses, plus three more genuine-prose keys (positions/tensions/
# modern_lens_note) that carry real interpretive text in several record
# types this scan needs - deliberately NOT engine.prose.all_text, whose
# broader reach (locus/source filename strings included) produced the
# Theophilus/Theophilus false positive this docstring names above.
PROSE_KEYS = {
    "text", "statement", "claim", "absent_detail", "plain_meaning", "quick_meaning",
    "bridge_line", "why_sources_cannot_answer", "positions", "tensions", "modern_lens_note",
}


def _prose_text(rec: dict) -> str:
    parts: list[str] = []

    def walk(value, key=None):
        if isinstance(value, str):
            if key in PROSE_KEYS:
                parts.append(value)
        elif isinstance(value, dict):
            for k, v in value.items():
                walk(v, k)
        elif isinstance(value, list):
            for item in value:
                walk(item, key)

    walk(rec)
    return " ".join(parts)


def latest_complete_package(world_key: str) -> pathlib.Path:
    pkgs = sorted((REPO_ROOT / "packages" / world_key).iterdir())
    for p in reversed(pkgs):
        if (p / "compiled" / "repository.json").exists():
            return p
    raise RuntimeError(f"no complete compiled package found for {world_key}")


def _other_names(entry: dict) -> list[str]:
    names = []
    card_name = entry.get("card_name")
    display_name = entry.get("display_name")
    if card_name:
        names.append(card_name.lower())
    if display_name:
        names.append(display_name.lower())
    rep_name = (entry.get("representative") or {}).get("name")
    if rep_name:
        names.append(rep_name.lower())
    for base in (card_name, display_name):
        if base:
            names.extend(_demonym_forms(base))
    return [n for n in names if n]


def _symmetric_overlap(a: dict, b: dict) -> bool:
    return a["start"] <= b["end"] and b["start"] <= a["end"]


def _asymmetric_no_future(self_win: dict, other_win: dict) -> bool:
    """other could have been known by self's own time: other started at or
    before self's own window closes - excludes only genuine foreknowledge
    of a tradition that has not arisen yet by self's own window's end."""
    return other_win["start"] <= self_win["end"]


def build_world_level_list(registry: dict, worlds: list[str]) -> dict:
    out = {}
    for w in worlds:
        C = latest_complete_package(w) / "compiled"
        recs = ev.repository_records_by_id(json.loads((C / "repository.json").read_text()))
        w_win = registry[w]["time_window"]
        rows = []
        for other in worlds:
            if other == w:
                continue
            o_entry = registry[other]
            o_win = o_entry["time_window"]
            sym = _symmetric_overlap(w_win, o_win)
            asym = _asymmetric_no_future(w_win, o_win)
            names = _other_names(o_entry)
            evidence_records = sorted({
                rid for rid, rec in recs.items()
                if any(n in _prose_text(rec).lower() for n in names)
            })
            if sym or asym or evidence_records:
                rows.append({
                    "other_world": other,
                    "other_card_name": o_entry.get("card_name"),
                    "other_window": o_win,
                    "symmetric_overlap": sym,
                    "asymmetric_no_future_violation": asym,
                    "text_evidence_records": evidence_records,
                    "proposed_confidence": (
                        "Documented" if evidence_records
                        else ("Inferential-Thin" if (sym or asym) else None)
                    ),
                })
        out[w] = {"window": w_win, "candidate_rows": rows}
    return out


# Reproduced read-only from engine.m4.live_uncited_claims_battery's own
# _other_tradition_turn (not imported, to avoid this report-only module
# taking a dependency on a live-battery script it does not otherwise
# need) - same alphabetical-first-other-card-name logic, same alx
# special case. If that function ever changes, this reproduction can
# drift; flagged here rather than silently assumed current.
def _battery_probe_target(world_key: str, registry: dict) -> str:
    if world_key == "alx":
        return "don"
    card_names = sorted(
        (key, entry["card_name"])
        for key, entry in registry.items()
        if key != world_key and entry.get("kind") == "formation" and entry.get("card_name")
    )
    return card_names[0][0]


def measure_battery_defensibility(registry: dict, worlds: list[str]) -> dict:
    rows = []
    for w in worlds:
        target = _battery_probe_target(w, registry)
        w_win = registry[w]["time_window"]
        t_win = registry[target]["time_window"]
        sym = _symmetric_overlap(w_win, t_win)
        asym = _asymmetric_no_future(w_win, t_win)
        rows.append({
            "asking_world": w,
            "probe_target_world": target,
            "probe_target_card_name": registry[target]["card_name"],
            "asking_window": w_win,
            "target_window": t_win,
            "defensible_under_symmetric_a": sym,
            "defensible_under_asymmetric_a": asym,
            "bare_name_present_under_b": True,  # every probe names its target directly, by construction
        })
    return {
        "rows": rows,
        "count_defensible_symmetric_a": sum(1 for r in rows if r["defensible_under_symmetric_a"]),
        "count_defensible_asymmetric_a": sum(1 for r in rows if r["defensible_under_asymmetric_a"]),
        "count_bare_name_under_b": len(rows),
        "total": len(rows),
    }


def main():
    registry = load_registry()
    worlds = formation_world_keys(registry)
    report = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "worlds_scanned": worlds,
        "world_level_known_tradition_candidates": build_world_level_list(registry, worlds),
        "battery_defensibility": measure_battery_defensibility(registry, worlds),
    }
    out_path = REPORTS_DIR / f"r37-ruling-design-measure-{date.today().isoformat()}.json"
    out_path.write_text(json.dumps(report, indent=2))

    bd = report["battery_defensibility"]
    print(f"Worlds scanned: {len(worlds)}")
    print(
        f"Battery item 4: defensible under symmetric (a): {bd['count_defensible_symmetric_a']}/{bd['total']}, "
        f"under asymmetric (a): {bd['count_defensible_asymmetric_a']}/{bd['total']}, "
        f"bare name present under (b): {bd['count_bare_name_under_b']}/{bd['total']}"
    )
    for r in bd["rows"]:
        print(
            f"  {r['asking_world']:12s} -> {r['probe_target_world']:12s} "
            f"sym={r['defensible_under_symmetric_a']!s:5s} asym={r['defensible_under_asymmetric_a']!s:5s}"
        )
    print(f"Report written: {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
