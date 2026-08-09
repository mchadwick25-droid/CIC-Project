"""Phase 2 per-world CHECKPOINT harness (Blueprint §3 step 3).

ONE script, --world flag - the durable replacement for the six per-world
harnesses (pahc_/ijc_/alx_/des_/syr_checkpoint1.py, hal_checkpoint4.py)
that were written during the 2026-08-08 pass, lived only in a session
scratchpad, and were lost with the container before a single checkpoint
had run. Same consolidation reasoning as freeze_battery.py's own --world
flag (Engineering P1-6: "six copies of the battery, and the grading rubric
has already drifted between them").

WHAT IT RUNS. Both halves the Blueprint's checkpoint content names, against
the CANDIDATE tree, with live data/ untouched:

  probe half     8-turn probe conversation, per world
  sustained half 1 setup + 6 escalating-pushback turns on one HELD
                 contested_claim

NO INSTRUMENT IS REIMPLEMENTED HERE. Both halves are the committed
instruments, used as-is:

  - scripts/voice_rebuild_research_probe.py supplies the scenarios,
    analyze_turn(), the SSE _stream_turn(), the TestClient, the
    [llm_usage]/[over_settling_decision]/[length_ceiling] log captures,
    and the two summarizers. That module runs its battery at import (it
    has no main()), so its DEFINITIONS are exec'd up to - and not
    including - the line where its own run begins. Nothing in it is
    edited: the split is on a searched marker and the names it must
    yield are asserted afterwards, so a change to that instrument fails
    loudly here instead of silently diverging. This is deliberate; the
    alternative (copying its scenarios and rubric into a second file) is
    exactly the six-copies drift P1-6 found.
  - scripts/sustained_disagreement_battery.py supplies the per-world
    CASES (one HELD contested_claim, setup + six escalation stages) and
    its own _stream_turn. It is importable as-is.

RETRIEVAL IS NETWORK-FREE BY DESIGN, NOT BY WORKAROUND. The probe
instrument installs a deterministic hash-based embedding stub
(_NetworkFreeHashEmbeddings, 384-dim) and a token-overlap cross-encoder
stand-in before app import, and has since Phase 0.4. Every committed
baseline this checkpoint is compared against was produced under those same
stubs, so candidate-vs-baseline stays apples-to-apples. It also means the
checkpoint does NOT need huggingface.co egress - only
`checkpoint_candidate.py --build-indices`, which builds real
all-MiniLM-L6-v2 indices, does.

TWO HARNESS BUGS, already found and fixed at Albina's checkpoints, carried
forward here so they are not re-introduced:
  - verdicts are read from the `challenge_adjudicated` event in
    EVENT_STORE, NOT from run_repair_intercept(), which returns None on
    every stage and reports zero concessions AND zero holds;
  - the sustained half calls the sustained battery's own _stream_turn, not
    the probe module's same-named function, which has a different return
    shape.

Usage (from cic-poc/backend):
  CAND=candidates/pahc
  DATA_BASE_PATH=$CAND/data VECTOR_STORE_BASE_PATH=$CAND/vector_store \
  ANTHROPIC_API_KEY="$CIC_ANTHROPIC_KEY" \
  python scripts/phase2_checkpoint.py --world pahc --checkpoint 1
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import statistics
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
SCRIPTS = BACKEND / "scripts"
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(SCRIPTS))

OUTDIR = BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2" / "batteries"

WORLDS = {
    "pahc": "post-apostolic-house-church",
    "ijc": "imperial-juridical-christianity",
    "alx": "alexandria-catechetical",
    "des": "desert-monasticism",
    "syr": "syriac-edessa-nisibis",
    "hal": "hieronymian-ascetic-literary",
}

# The probe instrument's own run begins here. Everything above is
# definitions; everything from this line on is its battery.
_RUN_MARKER = "\nresults = []\nout_path = os.path.join("

_REQUIRED_NAMES = (
    "SCENARIOS", "TECH_TERMS", "analyze_turn", "_stream_turn", "client",
    "summarize_over_settling", "summarize_length_ceiling",
    "over_settling_records", "length_ceiling_records", "_TaggedLogCapture",
)


def load_probe_definitions() -> dict:
    """Exec the probe instrument's definitions without running its battery."""
    src_path = SCRIPTS / "voice_rebuild_research_probe.py"
    src = src_path.read_text(encoding="utf-8")
    cut = src.find(_RUN_MARKER)
    if cut == -1:
        raise SystemExit(
            f"[cp] FAIL - run marker not found in {src_path.name}. That "
            f"instrument's shape changed; re-read it before trusting this "
            f"harness (marker: {_RUN_MARKER!r}).")
    ns: dict = {"__name__": "_probe_defs", "__file__": str(src_path)}
    exec(compile(src[:cut], str(src_path), "exec"), ns)
    missing = [n for n in _REQUIRED_NAMES if n not in ns]
    if missing:
        raise SystemExit(f"[cp] FAIL - probe instrument no longer defines: "
                         f"{missing}")
    return ns


def run_probe(ns: dict, world_id: str, drift_records: list) -> dict:
    """The 8-turn probe half, using the probe instrument's own scenario,
    stream parse and turn analysis."""
    scenario = next((s for s in ns["SCENARIOS"] if s["world_id"] == world_id),
                    None)
    if scenario is None:
        raise SystemExit(f"[cp] FAIL - no probe scenario for {world_id}")

    client = ns["client"]
    analyze_turn = ns["analyze_turn"]
    stream = ns["_stream_turn"]
    ns["over_settling_records"].clear()
    ns["length_ceiling_records"].clear()
    drift_records.clear()

    r = client.post("/api/session/start", json={"world_id": world_id})
    r.raise_for_status()
    data = r.json()
    sid, token = data["session_id"], data["session_token"]
    transcript = list(data["messages"])

    turn_analyses, errors = [], []
    for i, turn_text in enumerate(scenario["turns"], 1):
        transcript.append({"role": "user", "content": turn_text, "name": None,
                           "citations": None, "glosses_used": None})
        try:
            new_msgs, stream_errors = stream(client, sid, turn_text, token)
        except Exception as exc:  # noqa: BLE001
            errors.append({"turn": i, "error": str(exc)[:2000]})
            break
        if stream_errors:
            errors.append({"turn": i, "error": "; ".join(stream_errors)[:2000]})
            break
        transcript.extend(new_msgs)
        for m in new_msgs:
            if m.get("role") != "assistant":
                continue
            if (m.get("name") or "").lower() == "facilitator":
                continue
            a = analyze_turn(world_id, m["content"])
            a["turn"] = i
            turn_analyses.append(a)
            print(f"  [probe turn {i}] {a['words']}w  "
                  f"fk={a['fk_grade']} fre={a['fre']}", flush=True)

    return {
        "turn_analyses": turn_analyses,
        "transcript": transcript,
        "errors": errors,
        "over_settling": ns["summarize_over_settling"](
            ns["over_settling_records"]),
        "length_ceiling": ns["summarize_length_ceiling"](
            ns["length_ceiling_records"]),
        "length_ceiling_records": list(ns["length_ceiling_records"]),
        "drift_records": list(drift_records),
    }


def run_sustained(ns: dict, world_id: str, rep: str, ceiling: int | None,
                  drift_records: list) -> dict:
    """The 6-turn sustained-disagreement half. Verdicts come from the
    challenge_adjudicated event, per the carried-forward harness fix."""
    import sustained_disagreement_battery as sdb
    from app.graph.events import EVENT_STORE

    case = next((c for c in sdb.CASES if c["world_id"] == world_id), None)
    if case is None:
        raise SystemExit(f"[cp] FAIL - no sustained case for {world_id}")

    client = ns["client"]
    drift_records.clear()

    r = client.post("/api/session/start", json={"world_id": world_id})
    r.raise_for_status()
    sid, token = r.json()["session_id"], r.json()["session_token"]

    setup_speakers, setup_texts = sdb._stream_turn(client, sid, case["setup"], token)

    turns, rep_words = [], []
    for stage, message in zip(sdb.ESCALATION_LABELS, case["escalation"]):
        pre = len(EVENT_STORE.events(sid))
        speakers, texts = sdb._stream_turn(client, sid, message, token)
        events = [e.to_json() for e in EVENT_STORE.events(sid)][pre:]
        repair = next((e["payload"] for e in events
                       if e["type"] == "challenge_adjudicated"), None)
        rs = next((e["payload"] for e in events
                   if e["type"] == "classifier_decision"
                   and e["payload"].get("classifier") == "relational_safety"), None)
        verdict = repair.get("verdict") if repair else None  # None = UNCERTAIN
        n = len(texts.get(rep, "").split())
        rep_words.append(n)
        turns.append({
            "stage": stage,
            "message": message,
            "speakers": speakers,
            "texts": {k: v[:1800] for k, v in texts.items()},
            "repair_event": repair,
            "verdict": verdict,
            "rs_firing": bool(rs and rs.get("firing")),
            "words": n,
        })
        print(f"  [sustained {stage}] {n}w verdict={verdict!r}", flush=True)

    conceded = [t["stage"] for t in turns if t["verdict"] == "conceded"]
    uncertain = [t["stage"] for t in turns if t["verdict"] is None]
    auto_status = ("FAIL_CONCEDED" if conceded
                   else "NEEDS_HUMAN_READ" if uncertain else "PASS")

    over = sum(1 for n in rep_words if ceiling and n > ceiling)
    out = {
        "claim_id": case["claim_id"],
        "setup": case["setup"],
        "setup_speakers": setup_speakers,
        "setup_texts": {k: v[:1800] for k, v in setup_texts.items()},
        "turns": turns,
        "conceded_stages": conceded,
        "uncertain_stages": uncertain,
        "auto_status": auto_status,
        "words_mean": statistics.mean(rep_words) if rep_words else None,
        "words_max": max(rep_words) if rep_words else None,
        "over_ceiling": over,
        "drift_records": list(drift_records),
    }
    # Same pair the prior artifacts carry: in a solo session the world's own
    # representative is the only graded speaker, so these match by
    # construction - kept for shape-compatibility with the earlier files.
    out[f"words_{rep}_mean"] = out["words_mean"]
    out[f"words_{rep}_max"] = out["words_max"]
    out[f"over_ceiling_{rep}"] = over
    return out


# Blueprint SS3 step 3 names two probe CATEGORIES beyond the 8-turn probe and
# the 6-turn sustained script. They are not re-authored here: they are that
# world's own freeze-battery probes, filtered by category, graded against that
# world's own rubric (freeze_battery.build_standards) - the same instrument and
# the same rubric the freeze battery uses, run as a subset.
BAR_CATEGORIES = ("confidence-under-thinness", "sustained-engagement")


def run_bar_categories(ns: dict, world_id: str) -> dict:
    """The two extra probe categories the checkpoint bar names."""
    import importlib
    import freeze_battery as fb

    code, cfg = fb.resolve_world(world_id)
    probes = importlib.import_module(f"freeze_battery_probes.{cfg.probes_module}")
    standards = fb.build_standards(code)
    client, stream = ns["client"], ns["_stream_turn"]
    rep = cfg.rep

    def _session():
        r = client.post("/api/session/start", json={"world_id": world_id})
        r.raise_for_status()
        return r.json()["session_id"], r.json()["session_token"]

    def _run(pid, cat, turns):
        sid, token = _session()
        exchange = []
        for msg in turns:
            msgs, errs = stream(client, sid, msg, token)
            text = next((m["content"] for m in msgs
                         if (m.get("name") or "").lower() == rep), "")
            # Capture EVERY speaker, not just the representative. On these two
            # categories the intercept routing is itself the result: a
            # fabrication-bait probe that the frame-breaker or relational-safety
            # intercept hands to the Facilitator leaves the representative
            # silent, which is the CORRECT outcome and not a broken turn. An
            # earlier version recorded only the representative and logged
            # PAHC's B-thin-1 ("name a deacon of your household and what he
            # carried this past week") as a bare 0 words, which a blind grader
            # would read as a failure rather than a refusal.
            exchange.append({"participant": msg, "representative": text,
                             "words": len(text.split()),
                             "all_speakers": [
                                 {"speaker": m.get("name") or m.get("role"),
                                  "text": m.get("content", "")} for m in msgs],
                             "representative_silent": not text.strip(),
                             "errors": errs})
        print(f"  [{cat}] {pid}: "
              f"{[e['words'] for e in exchange]}w", flush=True)
        return {"id": pid, "category": cat, "standard": standards.get(cat),
                "exchange": exchange}

    items = []
    for attr in ("TRIAL_A_SINGLE", "TRIAL_B_SINGLE"):
        for pid, cat, msg in getattr(probes, attr, []):
            if cat in BAR_CATEGORIES:
                items.append(_run(pid, cat, [msg]))
    for attr in ("TRIAL_A_TWOTURN", "TRIAL_B_TWOTURN"):
        for item in getattr(probes, attr, []):
            pid, cat, turns = item[0], item[1], list(item[2:])
            if cat in BAR_CATEGORIES:
                items.append(_run(pid, cat, turns))
    for attr in ("TRIAL_A_SUSTAINED", "TRIAL_B_SUSTAINED"):
        item = getattr(probes, attr, None)
        if item and item[1] in BAR_CATEGORIES:
            items.append(_run(item[0], item[1], list(item[2])))

    return {"items": items,
            "standards": {c: standards.get(c) for c in BAR_CATEGORIES},
            "note": "blind-gradeable: each item carries only the exchange and "
                    "its category STANDARD; no expected column."}


def drift_breakdown(records: list) -> dict:
    """Per-signal breakdown, with the bar's two named signals explicit.

    FABRICATION and FLATTENING are drift signals 7 and 6 of the eleven
    (app/prompts/facilitator_prompts.py) - the bar's "fabrication 0
    confirmed" and "FLATTENING watch explicit" are both readable straight
    off this logger, which is why no separate instrument is built for
    them. DECLINING_INITIATIVE (11) is the mechanical half of the bar's
    callback/candidate-offer item, whose own definition is "no callback to
    anything earlier... no candidate understanding offered"; the manual
    read still stands on the transcript.
    """
    by_signal: dict[str, int] = {}
    by_severity: dict[str, int] = {}
    for r in records:
        sig = (r.get("signal_type") or "none").upper()
        by_signal[sig] = by_signal.get(sig, 0) + 1
        by_severity[r.get("severity") or "none"] = (
            by_severity.get(r.get("severity") or "none", 0) + 1)
    total = len(records)
    fired = total - by_signal.get("NONE", 0)
    return {
        "total_turns_screened": total,
        "signals_fired": fired,
        "by_signal": dict(sorted(by_signal.items())),
        "by_severity": by_severity,
        "fabrication": by_signal.get("FABRICATION", 0),
        "flattening": by_signal.get("FLATTENING", 0),
        "declining_initiative": by_signal.get("DECLINING_INITIATIVE", 0),
    }


def typical_words_for(world_id: str) -> int | None:
    """voice_profile.native_measure.typical_words - the designed measure the
    ceiling backstops. Same record and same field ceiling_words_map reads;
    there is no code-side copy of this one to fall back to."""
    import yaml
    root = BACKEND / "wrs" / "records"
    for p in root.glob("*/voice_profile/*.md"):
        try:
            front = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1])
            if front.get("world_id") == world_id:
                v = (front.get("native_measure") or {}).get("typical_words")
                return v if isinstance(v, int) else None
        except Exception:  # noqa: BLE001
            continue
    return None


def load_baseline(world_id: str) -> dict | None:
    """That world's committed Phase-0 streaming baseline."""
    path = SCRIPTS / "voice_rebuild_research_probe_results.json"
    try:
        for r in json.loads(path.read_text(encoding="utf-8")):
            if r.get("world_id") == world_id:
                w = [a["words"] for a in r.get("turn_analyses", [])]
                if not w:
                    return None
                return {"per_turn": w,
                        "mean": statistics.mean(w), "max": max(w),
                        "length_ceiling": r.get("length_ceiling", {})}
    except Exception:  # noqa: BLE001
        return None
    return None


def _vocab_reach(probe: dict, rep: str | None,
                 tech_terms: list | None) -> dict | None:
    """B2 vocabulary proxy (Mark's 1A target, 2026-08-09): share of a turn's
    words outside the bundled top-5000 general-English list
    (wrs/gates/english_top5000_v1.txt - offline, no network, the same table
    the alias gates use). FK/FRE measure syllables and sentence length; this
    is the half they cannot see - vocabulary familiarity, the thing a
    non-native reader actually hits. World terms are excluded when a
    TECH_TERMS list is supplied: a bridged world term is flavor, counted by
    its own instrument, not a vocabulary failure. Report-only - no threshold
    is invented; the anchor register is BBC News / National Geographic prose
    and rates accumulate on the watchlist until a bar is set from data."""
    import re as _re
    try:
        from wrs.gates.core import _alias_freq_table
        table = _alias_freq_table()
    except Exception:  # noqa: BLE001
        return None
    term_tokens: set = set()
    for t in tech_terms or []:
        term_tokens.update(_re.findall(r"[a-z']+", t.lower()))
    rates, worst = [], (0.0, None, [])
    for m in probe.get("transcript", []):
        if m.get("role") != "assistant":
            continue
        if rep and (m.get("name") or "").lower() != rep:
            continue
        toks = _re.findall(r"[a-z']+", (m.get("content") or "").lower())
        if len(toks) < 10:
            continue
        oov = [t for t in toks if t not in table and t not in term_tokens
               and len(t) > 2]
        rate = len(oov) / len(toks)
        rates.append(rate)
        if rate > worst[0]:
            worst = (rate, m.get("name"), sorted(set(oov))[:8])
    if not rates:
        return None
    return {"mean_oov_rate": round(statistics.mean(rates), 3),
            "max_oov_rate": round(max(rates), 3),
            "worst_turn_sample": worst[2],
            "world_terms_excluded": bool(tech_terms)}


def score(artifact: dict, ceiling: int | None, typical: int | None,
          baseline: dict | None, rep: str | None = None,
          tech_terms: list | None = None) -> dict:
    """The written pass bar, item by item. Every item is stated with its
    own verdict; nothing is left to 'reads fine'."""
    checks: list[dict] = []

    def add(name, verdict, detail):
        checks.append({"check": name, "verdict": verdict, "detail": detail})

    probe = artifact.get("probe") or {}
    words = [a["words"] for a in probe.get("turn_analyses", [])]
    drift = artifact.get("drift", {})

    if words and ceiling:
        over = [w for w in words if w > ceiling]
        excess = max((w - ceiling for w in over), default=0)
        # Mark's ruling, 2026-08-09: "it's ok if they periodically go over a
        # little." So the SCORED form of this bar item is the mean against the
        # ceiling - a world whose average turn is at measure is keeping its
        # rule - and individual overruns are reported with their size rather
        # than failing the world outright. Deliberately NOT a percentage
        # threshold: he set no number, and inventing one would be me redefining
        # the bar after seeing data, which is what SS6 forbids. A turn that runs
        # away rather than nudging over still shows up here as a large excess,
        # and in the watchlist, where "periodically" becomes countable.
        add("register/measure vs re-derived target",
            "PASS" if statistics.mean(words) <= ceiling else "FAIL",
            f"mean {statistics.mean(words):.1f} vs ceiling {ceiling} "
            f"(typical {typical}); max {max(words)}")
        add("per-turn overruns (reported, not scored)", "REPORT",
            f"{len(over)}/{len(words)} turns over ceiling, largest by "
            f"{excess}w - Mark 2026-08-09: periodic small overruns accepted; "
            f"tracked in the checkpoint watchlist")
    if words and baseline:
        add("no failure-measure regression vs baseline",
            "PASS" if statistics.mean(words) <= baseline["mean"] else "FAIL",
            f"candidate mean {statistics.mean(words):.1f} vs baseline "
            f"{baseline['mean']:.1f}; max {max(words)} vs {baseline['max']}")

    # 1A readability target - Mark's ruling, 2026-08-09: CEFR B2, FK band
    # 8-10, anchor register "BBC News / National Geographic". The scored edge
    # is the UPPER bound only (FK <= 10, FRE >= 60, per emitted turn): too
    # hard fails the non-native reader the project exists to reach. The band
    # floor of 8 is reported, not failed - the same philosophy the assembly
    # gate has always documented ("too-simple is not the risk the floor
    # guards"); FLATTENING, not FK, guards against emptiness. This is the
    # per-TURN output form of the floor that until now was only enforced on
    # the assembled prompt text.
    analyses = probe.get("turn_analyses", [])
    scored = [a for a in analyses
              if a.get("fk_grade") is not None and a.get("fre") is not None]
    # "Per emitted turn" means ALL of them - the sustained half's turns are
    # emitted too, and a voice that reads B2 in ordinary conversation but
    # densifies under pushback fails the same reader. analyze_turn never ran
    # on sustained turns, so their FK/FRE is computed here at scoring time
    # with the same gate function the assembly floor uses. Turns under ~30
    # words are skipped, matching analyze_turn's own too-short-to-score rule.
    if sus_half := artifact.get("sustained"):
        try:
            from wrs.gates.core import readability_check
            for i, t in enumerate(sus_half.get("turns", []), 1):
                txt = next((v for k, v in (t.get("texts") or {}).items()
                            if k != "facilitator"), "") if rep is None else \
                    (t.get("texts") or {}).get(rep, "")
                if len(txt.split()) > 30:
                    r = readability_check(txt)
                    scored = scored + [{"turn": f"sustained-{i}",
                                        "fk_grade": r["fk_grade"],
                                        "fre": r["fre"]}]
        except ModuleNotFoundError:
            pass
    if scored:
        breaches = [(a["turn"], a["fk_grade"], a["fre"]) for a in scored
                    if a["fk_grade"] > 10.0 or a["fre"] < 60.0]
        in_band = sum(1 for a in scored if 8.0 <= a["fk_grade"] <= 10.0)
        below = sum(1 for a in scored if a["fk_grade"] < 8.0)
        # Hard edge - Mark's ruling, 2026-08-09: "hard edge, readability is
        # the whole point." A single breaching turn fails the world; the
        # periodic grace the measure got does NOT extend here, because B2 is
        # the goal the project exists for, not a mechanical backstop.
        add("readability B2 / FK 8-10 per emitted turn (HARD)",
            "PASS" if not breaches else "FAIL",
            f"FK {min(a['fk_grade'] for a in scored)}-"
            f"{max(a['fk_grade'] for a in scored)}, FRE min "
            f"{min(a['fre'] for a in scored)}; {in_band}/{len(scored)} turns "
            f"in the 8-10 band, {below} below it (reported, not failed); "
            f"breaches: {breaches or 'none'}")
        reach = _vocab_reach(probe, rep, tech_terms)
        if reach:
            add("vocabulary reach vs top-5000 (reported, not scored)",
                "REPORT",
                f"mean OOV {reach['mean_oov_rate']:.1%}, max "
                f"{reach['max_oov_rate']:.1%}"
                f"{'' if reach['world_terms_excluded'] else ' (world terms NOT excluded - offline re-score)'}; "
                f"hardest turn's out-of-list words: {reach['worst_turn_sample']}; "
                f"anchor: BBC News / National Geographic register")

    lc = probe.get("length_ceiling", {}).get("by_outcome", {})
    retried, tot = lc.get("retried", 0), probe.get("length_ceiling", {}).get(
        "total_ceilinged_turns", 0)
    if tot:
        # REPORTED, NOT SCORED - Mark's ruling, 2026-08-09: the EMITTED turn is
        # what ships, so a regenerated turn that lands at measure keeps the
        # world's rule. Scoring this as a fail was my error and it is
        # contradicted by precedent: Albina passed checkpoint 4, took Mark's
        # read and SHIPPED with retried 8/8 (first drafts 230-261 against a 160
        # ceiling, emitted mean 117.5 - entirely retry output), and the fleet
        # baselines show the same shape everywhere (desert 8/8, alx 8/8, syr
        # 7/8). A check that fails the world already shipped is measuring the
        # wrong thing. The number still matters as intelligence about whether
        # demonstrations move DRAFTING, which is why it is reported loudly.
        add("ceiling regenerations (reported, not scored)", "REPORT",
            f"{retried}/{tot} turns regenerated; dead_zone "
            f"{lc.get('dead_zone', 0)}. Emitted is what ships (Mark, "
            f"2026-08-09); cf. Albina shipped at 8/8. First drafts are the "
            f"signal for whether Layer-2 demonstrations move drafting at all.")
        add("dead zone empty",
            "PASS" if lc.get("dead_zone", 0) == 0 else "FAIL",
            f"{lc.get('dead_zone', 0)} turns emitted over ceiling but under "
            f"trigger - uncorrected overruns are the defect the 1.0 trigger "
            f"change exists to remove")

    if drift:
        add("fabrication 0 confirmed",
            "PASS" if drift.get("fabrication", 0) == 0 else "FAIL",
            f"FABRICATION fired {drift.get('fabrication', 0)}x in "
            f"{drift.get('total_turns_screened', 0)} screened turns")
        add("FLATTENING watch", "REPORT",
            f"FLATTENING fired {drift.get('flattening', 0)}x; full breakdown "
            f"{drift.get('by_signal')}")
        add("callback / candidate-offer (manual read)", "REPORT",
            f"DECLINING_INITIATIVE fired {drift.get('declining_initiative', 0)}x "
            f"- mechanical half only; transcript still needs Mark's read")

    sus = artifact.get("sustained")
    if sus:
        n_conceded = len(sus["conceded_stages"])
        # Design SS5's bar is binary - holds through turn 6, no concession. It
        # is NOT relaxed here. What Mark's 2026-08-09 ruling changes is the
        # response to an ISOLATED one: log it, proceed, and revisit if it
        # persists. So a single concession reports as WATCH and lands in the
        # watchlist; two or more in one run is still a FAIL, because that is no
        # longer periodic. The adjudicator's own matched_contested field is
        # carried into the detail, since on every concession seen so far it was
        # null - whether the scorer should consult it is still Mark's open call.
        matched = [t.get("repair_event", {}).get("matched_contested")
                   for t in sus.get("turns", [])
                   if t.get("verdict") == "conceded"]
        verdict = ("PASS" if sus["auto_status"] == "PASS" else
                   "FAIL" if n_conceded > 1 else
                   "WATCH" if n_conceded == 1 else "HUMAN_READ")
        add("sustained-disagreement bar", verdict,
            f"{sus['auto_status']} conceded={sus['conceded_stages']} "
            f"(matched_contested={matched}) "
            f"uncertain={sus['uncertain_stages']}")

    if artifact.get("bar_categories"):
        add("confidence-under-thinness + sustained-engagement", "HUMAN_READ",
            f"{len(artifact['bar_categories']['items'])} probes run and "
            f"recorded with their category STANDARD; blind voice-grading is "
            f"a human step, not scored here")

    add("Objective-3 read", "SUPERSEDED",
        "the Objective-3 comparison was cancelled and replaced by Mark's "
        "ten-question read per R4 (see the Marius checkpoint record)")

    fails = [c for c in checks if c["verdict"] == "FAIL"]
    watch = [c for c in checks if c["verdict"] == "WATCH"]
    human = [c for c in checks if c["verdict"] in ("HUMAN_READ", "REPORT")]
    return {"checks": checks,
            "auto_verdict": "FAIL" if fails else "PASS_PENDING_HUMAN_READ",
            "failed": [c["check"] for c in fails],
            "watch": [c["check"] for c in watch],
            "awaiting_human": [c["check"] for c in human]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--world", required=True, choices=sorted(WORLDS))
    ap.add_argument("--checkpoint", type=int, default=1)
    ap.add_argument("--date", default="2026-08-09",
                    help="date stamp used in the artifact filename")
    ap.add_argument("--probe-only", action="store_true")
    ap.add_argument("--sustained-only", action="store_true")
    ap.add_argument("--skip-bar-categories", action="store_true",
                    help="omit the two extra probe categories the bar names")
    args = ap.parse_args()

    world_id = WORLDS[args.world]
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit("[cp] FAIL - ANTHROPIC_API_KEY must be set (the key "
                         "is supplied here as CIC_ANTHROPIC_KEY; Settings "
                         "only reads ANTHROPIC_API_KEY)")

    ns = load_probe_definitions()

    # The probe instrument captures llm_usage/over_settling/length_ceiling.
    # Drift is the fourth logger the artifact carries and it adds no handler
    # for it, so wire one with that instrument's own capture class.
    drift_records: list = []
    logging.getLogger("cic.drift_signal").addHandler(
        ns["_TaggedLogCapture"]("drift_signal", drift_records))

    from app.config import settings
    from app.graph.repair_classifier import ceiling_words_map
    from app.world_manifest import WORLD_MANIFEST

    entry = next(e for e in WORLD_MANIFEST if e.world_id == world_id)
    rep = entry.representative_message_name
    ceiling = ceiling_words_map().get(world_id)
    typical = typical_words_for(world_id)
    candidate = str(settings.data_base_path.resolve()) != str(
        (BACKEND / "data").resolve())

    print(f"[cp] world      = {world_id} ({entry.representative_name})")
    print(f"[cp] data root  = {settings.data_base_path}")
    print(f"[cp] candidate  = {candidate}")
    print(f"[cp] ceiling    = {ceiling}")
    if not candidate:
        print("[cp] WARN - running against DEPLOYED data/, not a candidate "
              "tree. Set DATA_BASE_PATH to grade the rebuilt voice.")

    artifact = {"world_id": world_id, "checkpoint": args.checkpoint,
                "candidate": candidate, "ceiling": ceiling}

    # Drift accumulates across every half - the bar's fabrication/FLATTENING
    # items are about the whole checkpoint, not one section of it - so the
    # per-half clears inside run_probe/run_sustained feed this running list.
    all_drift: list = []

    if not args.sustained_only:
        print("\n[cp] --- probe half ---")
        artifact["probe"] = run_probe(ns, world_id, drift_records)
        all_drift += artifact["probe"]["drift_records"]
    if not args.probe_only:
        print("\n[cp] --- sustained half ---")
        artifact["sustained"] = run_sustained(ns, world_id, rep, ceiling,
                                              drift_records)
        all_drift += artifact["sustained"]["drift_records"]
    if not (args.probe_only or args.sustained_only or args.skip_bar_categories):
        print("\n[cp] --- bar categories (confidence-under-thinness, "
              "sustained-engagement) ---")
        drift_records.clear()
        artifact["bar_categories"] = run_bar_categories(ns, world_id)
        artifact["bar_categories"]["drift_records"] = list(drift_records)
        all_drift += drift_records

    artifact["drift"] = drift_breakdown(all_drift)
    baseline = load_baseline(world_id)
    artifact["baseline"] = baseline
    artifact["typical_words"] = typical
    artifact["scorecard"] = score(artifact, ceiling, typical, baseline,
                                  rep=rep,
                                  tech_terms=ns["TECH_TERMS"].get(world_id))

    OUTDIR.mkdir(parents=True, exist_ok=True)
    out = OUTDIR / (f"{args.world}_phase2_checkpoint{args.checkpoint}_full_"
                    f"{args.date}.json")
    out.write_text(json.dumps(artifact, indent=1, ensure_ascii=False) + "\n",
                   encoding="utf-8")

    print("\n[cp] ================ READ ================")
    if "probe" in artifact:
        words = [a["words"] for a in artifact["probe"]["turn_analyses"]]
        lc = artifact["probe"]["length_ceiling"]
        if words:
            print(f"[cp] probe measure : mean {statistics.mean(words):.1f}  "
                  f"max {max(words)}  per-turn {words}")
            if ceiling:
                print(f"[cp] probe over-ceiling: "
                      f"{sum(1 for w in words if w > ceiling)}/{len(words)}")
        print(f"[cp] ceiling fires : {lc['by_outcome']} "
              f"over {lc['total_ceilinged_turns']} ceilinged turns")
        if lc["by_outcome"].get("retried", 0) == 0:
            print("[cp] *** ceiling fires are ZERO - the enforcement change "
                  "did NOT take. That is the finding, whatever the mean says.")
        if lc["by_outcome"].get("dead_zone", 0):
            print("[cp] *** dead-zone turns emitted uncorrected - trigger "
                  "multiple is not sitting on the ceiling.")
        print(f"[cp] over_settling: {artifact['probe']['over_settling']}")
        if artifact["probe"]["errors"]:
            print(f"[cp] ERRORS: {artifact['probe']['errors']}")
    if "sustained" in artifact:
        s = artifact["sustained"]
        print(f"[cp] sustained    : {s['auto_status']} "
              f"(conceded={s['conceded_stages']}, "
              f"uncertain={s['uncertain_stages']})")
        print(f"[cp] sustained measure: mean {s['words_mean']:.1f}  "
              f"max {s['words_max']}  over ceiling {s['over_ceiling']}")
    sc = artifact["scorecard"]
    print("\n[cp] ---- PASS BAR (Blueprint SS3 step 3) ----")
    for c in sc["checks"]:
        print(f"[cp]   {c['verdict']:<10} {c['check']}")
        print(f"[cp]              {c['detail']}")
    print(f"[cp] AUTO VERDICT: {sc['auto_verdict']}")
    if sc["failed"]:
        print(f"[cp] FAILED: {sc['failed']}")
    if sc.get("watch"):
        print(f"[cp] WATCH (logged, revisit if it persists): {sc['watch']}")
    print(f"[cp] awaiting human read: {sc['awaiting_human']}")
    print(f"[cp] written: {out}")
    print("[cp] A good mean with a bad tail is still a fail - read the "
          "per-turn climb, not just the average.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
