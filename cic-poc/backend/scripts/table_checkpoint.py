#!/usr/bin/env python3
"""T2.2 - the TABLE checkpoint instrument (2026-08-10).

The 1A bar is per EMITTED turn, and until this instrument existed no
emitted table turn had ever been measured against it: phase2_checkpoint.py
drives solo conversations only; s44a tests orchestration (who spoke, in
what order); s47 tests governance detectors on constructed rounds;
cross_world_probe.py proves convergence/divergence across six SOLO
conversations. This instrument applies those same measures WITHIN one
multi-world conversation - where the table lives or dies.

WHAT IT RUNS. The fixed conversational probe set
(table_checkpoint_probes.json - fixed for comparability, like
cost_baseline_conversations.json) through the REAL streaming endpoint at a
2-world and a 3-world table, and measures every participant-visible turn.

WHAT IS HARD AND WHAT IS REPORTED - exactly the 1A design's own split:

  HARD (listed per turn)   the B2 edge: FK <= 10 / FRE >= 60 per emitted
                           turn, every voice, Facilitator included. The
                           band floor of 8 is reported, never failed
                           ("too-simple is not the risk the floor guards").
  REPORT ONLY (Goodhart)   everything else: within-conversation
                           convergence/divergence, vocabulary ownership,
                           round shapes, question endings, rep-to-rep
                           naming, length variance, transparency payload
                           rates. Per the Voice Design's standing rule
                           these are watchlist reports and read aids,
                           never targets, never scored bars. The score of
                           record is the human read.

NO INSTRUMENT IS REIMPLEMENTED HERE, with one declared exception:
  - readability is wrs.gates.core.readability_check - the fleet's one
    implementation, so table numbers are comparable to every committed
    checkpoint number;
  - the TestClient, network-free retrieval stubs and TECH_TERMS come from
    phase2_checkpoint.load_probe_definitions(), same as variance_probe and
    cross_world_probe;
  - phrase overlap is the probes' own mean pairwise Jaccard over 5-grams,
    replicated verbatim (they each carry their own copy already);
  - THE EXCEPTION: the SSE parser. The probe module's _stream_turn keys
    text by speaker name, which at a table would silently CONCATENATE two
    turns by the same speaker in one round (the selector legitimately
    lets a voice return). _stream_round below is segment-aware: every
    speaker_start opens a new segment. Deliberate, stated here, asserted
    against the same event vocabulary (speaker_start/token/speaker_end/
    error/done) the shipped frontend consumes.

COST. Roughly $0.20 per 3-world round at the measured baseline (see
Ministry/Technology/Table/T1): a full run (8+8 rounds) is on the order of
$2.50-3.50 of API spend. Printed before starting; --dry-run to see the
resolved probes without spending.

Usage (from cic-poc/backend, on the Voice Rebuild lineage - the rebuilt
voices are what Phase 2 measures):
  ANTHROPIC_API_KEY="$CIC_ANTHROPIC_KEY" \
  python scripts/table_checkpoint.py --arm pre1A-table
  # options: --seating T2|T3|all (default all), --dry-run
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import statistics
import sys
from datetime import date as _date
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
SCRIPTS = BACKEND / "scripts"
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(SCRIPTS))

PROBES_PATH = SCRIPTS / "table_checkpoint_probes.json"
OUTDIR = BACKEND.parents[1] / "Ministry" / "Technology" / "Table" / "runs"

FK_EDGE, FRE_EDGE, FK_BAND_FLOOR = 10.0, 60.0, 8.0
MIN_WORDS_FOR_READABILITY = 30   # cross_world_probe's own guard: FK/FRE
                                 # are unstable on very short texts; turns
                                 # under this are reported unmeasured, and
                                 # a short turn is often the guidance
                                 # working ("a sentence of real agreement
                                 # ... is a complete turn")
LONG_SENTENCE_WORDS = 25         # the Writing Standard's sentence guard


# ---------------------------------------------------------------- metrics
def _grams(text: str, n: int = 5) -> set:
    """Verbatim from variance_probe/cross_world_probe - same measure."""
    w = re.findall(r"[a-z']+", text.lower())
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}


def _jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if (a or b) else 0.0


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]


# ---------------------------------------------------------------- harness
def _stream_round(client, session_id: str, message: str, token: str) -> dict:
    """One participant turn over the streaming endpoint, SEGMENT-AWARE.

    Returns {"segments": [{speaker, text, citations, glosses_used}...],
             "errors": [...]} in spoken order. Every speaker_start opens a
    new segment (see module docstring for why this differs from the probe
    module's _stream_turn); speaker_end attaches its payload to that
    speaker's most recent segment still awaiting one.
    """
    resp = client.post(f"/api/session/{session_id}/message/stream",
                       json={"message": message},
                       headers={"X-Session-Token": token})
    resp.raise_for_status()
    segments: list[dict] = []
    errors: list[str] = []
    for block in resp.text.split("\n\n"):
        for line in block.splitlines():
            if not line.startswith("data: "):
                continue
            try:
                ev = json.loads(line[6:])
            except Exception:
                continue
            kind = ev.get("type")
            if kind == "speaker_start":
                segments.append({"speaker": ev.get("speaker"), "text": "",
                                 "citations": None, "glosses_used": None,
                                 "_ended": False})
            elif kind == "token":
                sp = ev.get("speaker")
                seg = next((s for s in reversed(segments)
                            if s["speaker"] == sp and not s["_ended"]), None)
                if seg is None:   # token before any start - tolerate, log
                    seg = {"speaker": sp, "text": "", "citations": None,
                           "glosses_used": None, "_ended": False}
                    segments.append(seg)
                seg["text"] += ev.get("text", "")
            elif kind == "speaker_end":
                sp = ev.get("speaker")
                seg = next((s for s in reversed(segments)
                            if s["speaker"] == sp and not s["_ended"]), None)
                if seg is not None:
                    seg["citations"] = ev.get("citations")
                    seg["glosses_used"] = ev.get("glosses_used")
                    seg["_ended"] = True
            elif kind == "error":
                errors.append(ev.get("message", "unknown stream error"))
    for s in segments:
        s.pop("_ended", None)
    return {"segments": [s for s in segments if s["text"].strip()],
            "errors": errors}


def _resolve_probes(turns: list[str], display: dict[str, str]) -> list[str]:
    """Fill {rep:<world_id>} placeholders from the seating's display names."""
    out = []
    for t in turns:
        for wid, name in display.items():
            t = t.replace("{rep:%s}" % wid, name)
        if "{rep:" in t:
            raise SystemExit(f"[tc] FAIL - unresolved placeholder in probe: {t}")
        out.append(t)
    return out


# ---------------------------------------------------------------- scoring
def _turn_measures(text: str, readability_check) -> dict:
    words = re.findall(r"[A-Za-z']+", text)
    sents = _sentences(text)
    m = {"words": len(words), "sentences": len(sents),
         "long_sentences": [s for s in sents
                            if len(re.findall(r"[A-Za-z']+", s)) > LONG_SENTENCE_WORDS],
         "ends_on_question": text.rstrip().endswith("?"),
         "fk": None, "fre": None, "measured": False, "breach": None}
    if len(words) >= MIN_WORDS_FOR_READABILITY:
        rr = readability_check(text)
        m["fk"], m["fre"], m["measured"] = rr["fk_grade"], rr["fre"], True
        breaches = []
        if m["fk"] is not None and m["fk"] > FK_EDGE:
            breaches.append(f"FK {m['fk']} > {FK_EDGE}")
        if m["fre"] is not None and m["fre"] < FRE_EDGE:
            breaches.append(f"FRE {m['fre']} < {FRE_EDGE}")
        m["breach"] = "; ".join(breaches) if breaches else None
        m["below_band"] = bool(m["fk"] is not None and m["fk"] < FK_BAND_FLOOR)
    return m


def _score_conversation(seating_key: str, world_ids: list[str], rounds: list[dict],
                        name_by_msgname: dict, display_by_wid: dict,
                        tech_terms: dict, readability_check) -> dict:
    """All measures for one table conversation. rounds[i] = {probe, segments}."""
    msgname_by_wid = {wid: mn for mn, wid in
                      ((mn, wid) for wid, mn in name_by_msgname.items())}

    turns = []            # flat participant-visible turns with measures
    per_voice_text: dict[str, list[str]] = {}
    breaches = []
    facilitator_only_rounds = []
    round_reports = []

    for ri, rnd in enumerate(rounds):
        rep_segs = [s for s in rnd["segments"] if s["speaker"] != "facilitator"]
        if not rep_segs:
            facilitator_only_rounds.append(ri)
        q_endings = 0
        rep_names_mentioned = 0
        lengths = []
        for s in rnd["segments"]:
            m = _turn_measures(s["text"], readability_check)
            voice = name_by_msgname.get(s["speaker"], s["speaker"])
            turn = {"round": ri, "probe": rnd["probe"], "speaker": voice,
                    "speaker_msgname": s["speaker"], "text": s["text"],
                    "citations_n": len(s["citations"] or []),
                    "glosses_n": len(s["glosses_used"] or []), **m}
            turns.append(turn)
            per_voice_text.setdefault(voice, []).append(s["text"])
            if m["breach"]:
                breaches.append({"round": ri, "speaker": voice,
                                 "fk": m["fk"], "fre": m["fre"],
                                 "breach": m["breach"],
                                 "text_head": s["text"][:140]})
            if s["speaker"] != "facilitator":
                lengths.append(m["words"])
                q_endings += int(m["ends_on_question"])
                others = [display_by_wid[w] for w in world_ids
                          if name_by_msgname.get(s["speaker"]) != display_by_wid[w]]
                if any(o.split()[0] in s["text"] for o in others if o):
                    rep_names_mentioned += 1
        round_reports.append({
            "round": ri, "rep_turns": len(rep_segs),
            "question_ending_turns": q_endings,
            "rep_turns_naming_another_rep": rep_names_mentioned,
            "rep_turn_words": lengths,
            "length_spread": (max(lengths) - min(lengths)) if len(lengths) > 1 else None,
        })

    # ---- within-conversation convergence / divergence (per VOICE aggregate)
    voice_agg = {v: " ".join(ts) for v, ts in per_voice_text.items()
                 if v != "facilitator" and len(" ".join(ts).split()) > 30}
    reads = {v: readability_check(t) for v, t in voice_agg.items()}
    fks = [r["fk_grade"] for r in reads.values() if r["fk_grade"] is not None]
    overlaps = {f"{a}|{b}": round(_jaccard(_grams(voice_agg[a]), _grams(voice_agg[b])), 4)
                for a, b in itertools.combinations(sorted(voice_agg), 2)}

    # ---- vocabulary ownership (observational; attribution-quoting is legal)
    borrowed = []
    for wid in world_ids:
        terms = tech_terms.get(wid, [])
        owner = display_by_wid[wid]
        for t in turns:
            if t["speaker"] in ("facilitator", owner):
                continue
            low = t["text"].lower()
            for term in terms:
                for hit in re.finditer(r"\b%s\b" % re.escape(term.lower()), low):
                    a = max(0, hit.start() - 40)
                    borrowed.append({"term": term, "owner_world": wid,
                                     "spoken_by": t["speaker"], "round": t["round"],
                                     "context": t["text"][a:hit.end() + 40]})

    rep_turn_counts = [r["rep_turns"] for r in round_reports]
    return {
        "seating": seating_key, "world_ids": world_ids,
        "turns": turns, "rounds": round_reports,
        "hard_readability": {
            "edge": {"fk_max": FK_EDGE, "fre_min": FRE_EDGE},
            "measured_turns": sum(1 for t in turns if t["measured"]),
            "unmeasured_short_turns": sum(1 for t in turns if not t["measured"]),
            "breaches": breaches,
            "below_band_reported": sum(1 for t in turns if t.get("below_band")),
        },
        "convergence": {
            "per_voice": {v: {"fk": r["fk_grade"], "fre": r["fre"],
                              "words": len(voice_agg[v].split())}
                          for v, r in reads.items()},
            "fk_spread": round(max(fks) - min(fks), 2) if len(fks) > 1 else None,
        },
        "divergence": {
            "pairwise_phrase_overlap": overlaps,
            "overlap_mean": round(statistics.mean(overlaps.values()), 4) if overlaps else None,
            "overlap_max": max(overlaps.values()) if overlaps else None,
            "borrowed_vocabulary": borrowed,
        },
        "shape": {
            "rep_turns_per_round": rep_turn_counts,
            "mean_rep_turns_per_round": round(statistics.mean(rep_turn_counts), 2)
                if rep_turn_counts else None,
            "facilitator_only_rounds": facilitator_only_rounds,
            "question_ending_turns_total": sum(r["question_ending_turns"]
                                               for r in round_reports),
            "rounds_with_2plus_open_questions": [
                r["round"] for r in round_reports
                if r["question_ending_turns"] >= 2],
        },
        "transparency": {
            v: {"turns": sum(1 for t in turns if t["speaker"] == v),
                "turns_with_citations": sum(1 for t in turns
                                            if t["speaker"] == v and t["citations_n"]),
                "citations_total": sum(t["citations_n"] for t in turns
                                       if t["speaker"] == v),
                "glosses_total": sum(t["glosses_n"] for t in turns
                                     if t["speaker"] == v)}
            for v in sorted({t["speaker"] for t in turns} - {"facilitator"})
        },
    }


# ------------------------------------------------------------------ main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", required=True,
                    help="run label, e.g. pre1A-table / post1A-table")
    ap.add_argument("--seating", default="all", choices=["T2", "T3", "all"])
    ap.add_argument("--date", default=str(_date.today()))
    ap.add_argument("--dry-run", action="store_true",
                    help="resolve probes and print the plan; no API spend")
    args = ap.parse_args()

    spec = json.loads(PROBES_PATH.read_text(encoding="utf-8"))
    seatings = {k: v for k, v in spec["seatings"].items()
                if args.seating in ("all", k)}

    import phase2_checkpoint as cp
    ns = cp.load_probe_definitions()
    client, tech_terms = ns["client"], ns["TECH_TERMS"]
    from wrs.gates.core import readability_check
    from app.world_manifest import WORLD_MANIFEST

    name_by_msgname = {e.representative_message_name: e.representative_name
                       for e in WORLD_MANIFEST}
    display_by_wid = {e.world_id: e.representative_name for e in WORLD_MANIFEST}

    total_rounds = sum(len(s["turns"]) for s in seatings.values())
    est = sum(len(s["turns"]) * (0.20 if len(s["world_ids"]) >= 3 else 0.15)
              for s in seatings.values())
    print(f"[tc] arm={args.arm} seatings={sorted(seatings)} rounds={total_rounds} "
          f"estimated spend ~${est:.2f} (T1 baseline rates)")

    if args.dry_run:
        for key, s in seatings.items():
            probes = _resolve_probes(
                s["turns"], {w: display_by_wid[w] for w in s["world_ids"]})
            print(f"[tc] {key}: {', '.join(display_by_wid[w] for w in s['world_ids'])}")
            for i, p in enumerate(probes):
                print(f"      {i}: {p}")
        return 0

    results = {}
    for key, s in sorted(seatings.items()):
        world_ids = s["world_ids"]
        probes = _resolve_probes(
            s["turns"], {w: display_by_wid[w] for w in world_ids})
        r = client.post("/api/session/start", json={"world_ids": world_ids})
        r.raise_for_status()
        sid, tok = r.json()["session_id"], r.json()["session_token"]
        print(f"[tc] {key} session {sid[:8]} "
              f"({', '.join(display_by_wid[w] for w in world_ids)})")
        rounds = []
        for i, probe in enumerate(probes):
            out = _stream_round(client, sid, probe, tok)
            rounds.append({"probe": probe, **out})
            spoken = ", ".join(
                f"{name_by_msgname.get(sg['speaker'], sg['speaker'])}"
                f"({len(sg['text'].split())}w)" for sg in out["segments"])
            print(f"[tc]   r{i}: {spoken}" + (
                f"  ERRORS: {out['errors']}" if out["errors"] else ""))
        results[key] = _score_conversation(
            key, world_ids, rounds, name_by_msgname, display_by_wid,
            tech_terms, readability_check)

    artifact = {"instrument": "table_checkpoint", "version": 1,
                "arm": args.arm, "date": args.date,
                "probes_file": PROBES_PATH.name,
                "goodhart_note": ("Everything except hard_readability is "
                                  "REPORT ONLY - watchlist and read aids, "
                                  "never targets (Voice Design 2026-08-09)."),
                "seatings": results}
    OUTDIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTDIR / f"table_checkpoint_{args.arm}_{args.date}.json"
    out_path.write_text(json.dumps(artifact, indent=2, ensure_ascii=False),
                        encoding="utf-8")

    print(f"\n[tc] ===== {args.arm} =====")
    any_breach = False
    for key, res in sorted(results.items()):
        hr = res["hard_readability"]
        print(f"[tc] {key}: {hr['measured_turns']} measured turns, "
              f"{hr['unmeasured_short_turns']} short/unmeasured, "
              f"below-band reported {hr['below_band_reported']}")
        if hr["breaches"]:
            any_breach = True
            for b in hr["breaches"]:
                print(f"[tc]   HARD BREACH r{b['round']} {b['speaker']}: "
                      f"{b['breach']}  \"{b['text_head']}...\"")
        else:
            print(f"[tc]   B2 edge: no breaches")
        print(f"[tc]   convergence: FK spread {res['convergence']['fk_spread']}  "
              f"divergence: overlap mean {res['divergence']['overlap_mean']} "
              f"max {res['divergence']['overlap_max']}  "
              f"borrowed-vocab occurrences {len(res['divergence']['borrowed_vocabulary'])}")
        print(f"[tc]   shape: rep turns/round {res['shape']['rep_turns_per_round']} "
              f"(mean {res['shape']['mean_rep_turns_per_round']})  "
              f"question-ending turns {res['shape']['question_ending_turns_total']}  "
              f"2+-open-question rounds {res['shape']['rounds_with_2plus_open_questions']}")
        for v, t in res["transparency"].items():
            print(f"[tc]   transparency {v}: {t['turns_with_citations']}/{t['turns']} "
                  f"turns cited, {t['citations_total']} citations, "
                  f"{t['glosses_total']} glosses")
    print(f"[tc] artifact: {out_path}")
    print(f"[tc] verdict on the one hard bar (B2 edge per emitted turn): "
          f"{'BREACHES LISTED ABOVE' if any_breach else 'CLEAN'}")
    print("[tc] everything else is report-only; the score of record is the "
          "human read.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
