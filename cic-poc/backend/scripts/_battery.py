"""Shared plumbing for the fleet's representative-freeze batteries.

Extracted from the six per-world freeze-battery scripts this module
replaced (Engineering P1-6, CiC_FullSystem_Review_2026-08-05):
s56_freeze_battery.py and s62_{alx,hal,ijc,pahc,syr}_freeze_battery.py.
See scripts/freeze_battery.py for the --world entry point that drives
this module, and scripts/_freeze_battery_parity_check.py (run once,
before the six originals were deleted) for the proof that this
extraction changed nothing the six originals' own STANDARDS dicts and
TRIAL_* probes asserted.

ONE NORMALIZED BEHAVIOR, documented here rather than smuggled: this
module's `_stream_turn` always sends the `X-Session-Token` header.
Four of the six originals (s56/desert, alx, hal, syr) never did -
they predate app/session_auth.py. That was not a legitimate per-world
difference; app/session_auth.py's `require_session_access` is applied
identically to every world's /message/stream route (app/main.py), and
every session, from every world, has minted a `session_token` since
that module shipped (only sessions started before it are grandfathered
open). Run today, those four scripts' own `_stream_turn` would 403 on
their very first call - a latent break the "byte-identical `_stream_turn`
across six scripts" claim in the P1-6 finding did not catch, because it
in fact is NOT byte-identical: two of the six (ijc, pahc, the two
batteries run after HAL) already carry the token. This module adopts
the current, working form for all six worlds. See freeze_battery.py's
module docstring for the same note.

TWO NORMALIZED, PURELY COSMETIC BEHAVIORS that do not touch any output
file's bytes: `run_case`'s progress print always passes flush=True
(three of six originals already did; the others just buffered stdout
slightly longer), and the REP speaker key is always taken from
per-world config rather than hardcoded inline (s56/desert alone
hardcoded "papnoute" instead of using a REP constant - same value,
different source shape).

TWO REAL, PRESERVED PER-WORLD DIVERGENCES, not normalized:
  - include_repair_evidence: s62_ijc's evidence dict has no "repair"
    key at all (the other five do). Preserved via the
    include_repair_evidence flag - IJC's sealed key file will not
    carry that field, exactly as its original script produced.
  - track_native_measure: s62_ijc and s62_pahc log per-turn
    Representative word counts (the native_measure feeding their
    ceiling-ceiling ceiling decision, per their own docstrings); the
    other four never did. Preserved via the track_native_measure flag.
"""
from __future__ import annotations

import json
import random
import statistics
from pathlib import Path


def _stream_turn(client, sid: str, message: str, token: str):
    resp = client.post(f"/api/session/{sid}/message/stream",
                       json={"message": message},
                       headers={"X-Session-Token": token})
    resp.raise_for_status()
    speakers, texts = [], {}
    for block in resp.text.split("\n\n"):
        for line in block.splitlines():
            if line.startswith("data: "):
                try:
                    ev = json.loads(line[6:])
                except Exception:
                    continue
                if ev.get("type") == "speaker_start":
                    speakers.append(ev["speaker"])
                elif ev.get("type") == "token":
                    texts[ev.get("speaker")] = (
                        texts.get(ev.get("speaker"), "") + ev.get("text", ""))
    return speakers, texts


def run_battery(*, client, world_id, rep, trial, single, twoturn, sustained,
                 EVENT_STORE, parroting_score, parrot_source,
                 include_repair_evidence, track_native_measure):
    """Runs every probe case fresh-session against the REAL system and
    returns (items, rep_word_counts) exactly as each original script's
    main() built its own `items` list in place, turn by turn."""
    items = []
    rep_word_counts = []

    def run_case(pid, cat, turns):
        print(f"[{trial}] {pid} ({cat}) ...", flush=True)
        r = client.post("/api/session/start", json={"world_id": world_id})
        r.raise_for_status()
        sid = r.json()["session_id"]
        token = r.json()["session_token"]
        exchange, evidence, prior_rep_turns = [], [], []
        for msg in turns:
            pre = len(EVENT_STORE.events(sid))
            speakers, texts = _stream_turn(client, sid, msg, token)
            rep_text = texts.get(rep, "")
            fac_text = texts.get("facilitator", "")
            exchange.append({"participant": msg,
                             "responses": [
                                 {"speaker": s, "text": texts.get(s, "")}
                                 for s in dict.fromkeys(speakers)]})
            ev = [e.to_json() for e in EVENT_STORE.events(sid)][pre:]
            evidence_entry = {
                "speakers": speakers,
                "event_types": [e["type"] for e in ev],
                "safety": [e["payload"] for e in ev
                           if "relational" in e["type"] or "rs_" in e["type"]],
            }
            if include_repair_evidence:
                evidence_entry["repair"] = [e["payload"] for e in ev
                                            if e["type"] == "challenge_adjudicated"]
            evidence.append(evidence_entry)
            if track_native_measure and rep_text:
                rep_word_counts.append(len(rep_text.split()))
            if cat == "parroting" and (rep_text or fac_text):
                spoken = rep_text or fac_text
                src = (prior_rep_turns[-1] if pid.endswith("parrot-6")
                       and prior_rep_turns else parrot_source)
                evidence[-1]["parroting"] = parroting_score(src, spoken)
            if rep_text:
                prior_rep_turns.append(rep_text)
        items.append({"id": pid, "category": cat,
                      "exchange": exchange, "evidence": evidence})

    for pid, cat, probe in single:
        run_case(pid, cat, [probe])
    for pid, cat, t1, t2 in twoturn:
        run_case(pid, cat, [t1, t2])
    sid_, cat_, turns_ = sustained
    run_case(sid_, cat_, turns_)

    return items, rep_word_counts


def write_masked_and_key(*, items, standards, trial, shuffle_seed,
                          file_tag, outdir: Path):
    """The blind-grading mask/key writer (V7.4 [533]): seeded shuffle,
    ids hidden, expected withheld, standard shown; evidence sealed into
    the key. Byte-identical to all six originals' own copy of this
    block, parameterized by this world's shuffle_seed and file_tag."""
    rng = random.Random(shuffle_seed + (0 if trial == "A" else 1))
    order = list(range(len(items)))
    rng.shuffle(order)
    masked, key = [], []
    for mask_i, real_i in enumerate(order):
        it = items[real_i]
        masked.append({"item": mask_i, "category": it["category"],
                       "standard": standards[it["category"]],
                       "exchange": it["exchange"]})
        key.append({"item": mask_i, "id": it["id"],
                    "category": it["category"], "evidence": it["evidence"]})

    outdir.mkdir(parents=True, exist_ok=True)
    mpath = outdir / f"{file_tag}_{trial}_masked.jsonl"
    kpath = outdir / f"{file_tag}_{trial}_key.jsonl"
    with mpath.open("w", encoding="utf-8") as f:
        for row in masked:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    with kpath.open("w", encoding="utf-8") as f:
        for row in key:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return mpath, kpath, masked, key


def print_summary(*, items, mpath, kpath, masked, rep, rep_word_counts):
    parrot_scores = [e["parroting"]["score"] for it in items
                     for e in it["evidence"] if "parroting" in e]
    print(f"\nwritten: {mpath.name} ({len(masked)} items), {kpath.name}")
    if parrot_scores:
        print(f"parroting mechanical: n={len(parrot_scores)} "
              f"mean={statistics.mean(parrot_scores):.4f} "
              f"max={max(parrot_scores):.4f}")
    if rep_word_counts:
        print(f"native_measure ({rep}, this trial): "
              f"n={len(rep_word_counts)} "
              f"mean={statistics.mean(rep_word_counts):.1f} "
              f"median={statistics.median(rep_word_counts):.0f} "
              f"min={min(rep_word_counts)} max={max(rep_word_counts)}")
