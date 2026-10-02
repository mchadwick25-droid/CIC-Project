"""Table governance, deterministic half (Artifact-7 SS2's round-level
governance; C5). Ported from the proven poc implementation
(cic-poc/backend/app/graph/nodes.py check_dominance) rather than invented:
the thresholds and minimums are the ones that ran live, and the poc's own
rationale for each is kept below. Convergence deliberately has NO
deterministic port: the poc implemented it as a conservative model
judgment ("echoed words with each world's own sense intact are NOT
drift"), and its prompt explicitly rejects what a vocabulary-overlap
heuristic would measure - so convergence lives in the live battery
(engine.m4.live_table_battery), not here.

Also home to direct-address detection (Facilitator Governance SS8, quoted
in the poc's S4.4a battery as the governing sentence: "When the
participant addresses a specific Representative, you route accordingly.
Immediately, completely, without editorial intervention"): a participant
who names exactly one seated Representative gets that voice, with no
selector call. Conservative by design, same as the poc's detector: two
names is ambiguous and falls through to the selector; "each of you"
blocks the short-circuit.

Everything here is pure - no model call, no store access - so the round
loop can run it on every close and the battery can re-run it over any
transcript.
"""
import re

# The poc's own threshold rationale, kept verbatim in spirit: 0.70, not
# lower, because legitimate cross-world length asymmetry is by design (a
# desert word is a sentence; a Syriac demonstration is staged paragraphs)
# - dominance means crowding out, not merely out-speaking a form that is
# short on purpose.
WORD_SHARE_THRESHOLD = 0.70
WORD_SHARE_MINIMUM_WORDS = 150
# The floor-allocation prong (poc S4.7): a world SELECTED every round can
# dominate at 40% of the words, invisible to the word-share backstop.
# Turn-count share is the cheap proxy; fires only at 3+ seated worlds
# with enough turns for a share to mean anything.
TURN_SHARE_THRESHOLD = 0.50
TURN_SHARE_MINIMUM_TURNS = 6


def voice_stats(transcript: list[dict], world_keys: list[str]) -> dict[str, dict]:
    """Words and turns per seated voice over a projected transcript."""
    stats = {k: {"words": 0, "turns": 0} for k in world_keys}
    for entry in transcript:
        speaker = entry.get("speaker")
        if speaker in stats:
            stats[speaker]["words"] += len((entry.get("text") or "").split())
            stats[speaker]["turns"] += 1
    return stats


def dominance_signals(transcript: list[dict], world_keys: list[str]) -> list[dict]:
    """Deterministic dominance findings over the whole conversation so far
    - cumulative, not per-round (dominance is a pattern across a
    conversation, per the poc's own docstring). Detected, never blocking:
    the caller attaches these to the round_closed event for the audit
    surface; acting on them is a separate, undecided policy."""
    if len(world_keys) <= 1:
        return []
    stats = voice_stats(transcript, world_keys)
    total_words = sum(s["words"] for s in stats.values())
    total_turns = sum(s["turns"] for s in stats.values())
    spoken = [k for k, s in stats.items() if s["words"] > 0]

    signals = []
    if len(world_keys) >= 3 and total_turns >= TURN_SHARE_MINIMUM_TURNS:
        for k, s in stats.items():
            share = s["turns"] / total_turns
            if share >= TURN_SHARE_THRESHOLD:
                signals.append({
                    "signal_type": "dominance",
                    "basis": "turn_share",
                    "world_key": k,
                    "share": round(share, 2),
                    "severity": "medium",
                })
    if len(spoken) >= 2 and total_words >= WORD_SHARE_MINIMUM_WORDS:
        for k, s in stats.items():
            if s["words"] == 0:
                continue
            share = s["words"] / total_words
            if share >= WORD_SHARE_THRESHOLD:
                signals.append({
                    "signal_type": "dominance",
                    "basis": "word_share",
                    "world_key": k,
                    "share": round(share, 2),
                    "severity": "medium" if share < 0.8 else "high",
                })
    return signals


def governance_summary(transcript: list[dict], world_keys: list[str]) -> dict:
    """What _close_round attaches to every round_closed payload: the
    per-voice word/turn stats and any dominance findings, so the M7 audit
    reads allocation health per round without recomputing it."""
    stats = voice_stats(transcript, world_keys)
    total_words = sum(s["words"] for s in stats.values()) or 1
    return {
        "word_share": {k: round(s["words"] / total_words, 2) for k, s in stats.items()},
        "turns": {k: s["turns"] for k, s in stats.items()},
        "dominance_signals": dominance_signals(transcript, world_keys),
    }


_EACH_OF_YOU = re.compile(r"\b(each|all|both|any)\s+of\s+you\b", re.IGNORECASE)


def detect_direct_address(message: str, name_to_world: dict[str, str]) -> str | None:
    """Facilitator Governance SS8's immediate routing, at the cheap-check
    layer the poc's S4.4a battery proved: exactly one seated
    Representative's name in the participant's message routes to that
    voice with no selector call. Conservative by the same design:

    - "each of you" / "all of you" / "both of you" blocks the
      short-circuit - the participant is addressing the Table;
    - two or more names is ambiguous and falls through to the selector
      (the poc's L3 case: "Papnoute, ask Mar Yausep..." names both);
    - title-only address ("presbyter", "the elder") is deliberately below
      this check's line and remains the selector's regime.

    Names match on word boundaries, case-insensitively, against the
    registry-authored representative names the door turn already spoke."""
    if _EACH_OF_YOU.search(message):
        return None
    hits = [
        world_key
        for name, world_key in name_to_world.items()
        if re.search(rf"\b{re.escape(name)}\b", message, re.IGNORECASE)
    ]
    return hits[0] if len(hits) == 1 else None
