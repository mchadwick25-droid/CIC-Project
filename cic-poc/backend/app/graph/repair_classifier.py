"""The repair classifier - the SIXTH intercept (S4.6, Pass 1 §6.3).

Mirrors epistemology_bridge.py's classify-then-route shape (the closest
existing template), with one structural difference: a repair hit never
produces a Facilitator turn. The direction - hold or concede - is decided
by EVIDENCE, and the selected strategy rides INSIDE the challenged
Representative's own answering turn as a private directive (the S4.4a
mechanism), so the near-silent room is preserved.

Why this exists (§6.3): the model this system runs has a measured
tendency to reverse previously-correct answers under bare pushback
("are you sure?" - roughly a quarter of correct answers reversed in the
cited benchmark). The mirror failure - resisting all correction - would
be worse: a fabrication that survives every challenge is the cardinal
sin. So the design never instructs "resist pushback"; it distinguishes:

- claim SUPPORTED by the world's own record -> HOLD, from inside the
  world, with the matching contested_claim record supplying how this
  world CHARACTERISTICALLY holds it under challenge (pressure_response);
- claim UNSUPPORTED -> CONCEDE plainly - the fabrication guard working
  as designed;
- genuinely UNCERTAIN -> no directive at all: the turn proceeds exactly
  as today (fail-open to substantive, the discipline every intercept in
  this chain shares). A false "hold" hardens a possible fabrication; a
  false "concede" talks a world out of its own conviction; silence
  costs only what today's behavior already costs.

The guidance is SELECTED from the closed set below, never composed
free-form - the recorded incident of a reroot model inventing sources to
fix an over-confidence flag is the standing argument (same rule as the
S4.3 fabrication strategies and the over-settling pass-through).

Chain placement: LAST. governance.classify_pre_turn runs this only when
no safety intercept fired, no epistemology bridge, no closing sequence,
and no modern-term match - a pushback phrasing that is actually distress
routes to relational safety FIRST (the battery's crisis-overlap case).

Compatibility classification: requires contested_claim/world_core
records, so it runs ONLY for migrated worlds (currently Desert);
unmigrated worlds keep current behavior exactly.
"""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import yaml
from langchain_core.messages import HumanMessage, SystemMessage

_RECORDS_ROOT = Path(__file__).resolve().parents[2] / "wrs" / "records"


REPAIR_INITIATION_CLASSIFIER_PROMPT = """You are classifying a single incoming participant message. This classifier has no generation role - it only decides routing, and it runs after the safety classifiers have already declined the message.

Your only question: is this message a REPAIR INITIATION on the Representative's prior claim - is the participant challenging, doubting, or asking the Representative to fix/justify something specific the Representative said in the turn quoted below?

The Representative's prior turn ({rep_name}):
\"\"\"{last_rep_text}\"\"\"

Kinds of repair initiation:
- OPEN_REQUEST - trouble signaled, source unspecified: "wait, what?", "I don't follow that."
- RESTRICTED_REQUEST - asks about a specific part: "what do you mean by X?", "which elders?"
- RESTRICTED_OFFER - offers a candidate correction/understanding for confirmation: "so you're saying X?", "surely you mean Y?", "that can't be right - wasn't it actually Z?"
- BARE_PUSHBACK - doubt with no content: "are you sure?", "really?", "I don't buy that."

NOT repair (output NOT_REPAIR):
- A new question on a new or adjacent topic, however abrupt.
- Emotional response to the content ("that unsettles me") without challenging its truth.
- A request for MORE ("tell me more about that") rather than doubt about what was said.
- Personal distress of any kind - that is never yours; it was already screened before you ran, and if you can read distress in the message, output NOT_REPAIR.

If it IS a repair initiation, respond in exactly this format:
REPAIR: <OPEN_REQUEST|RESTRICTED_REQUEST|RESTRICTED_OFFER|BARE_PUSHBACK>
CHALLENGED_CLAIM: <one sentence restating the SPECIFIC claim from the Representative's turn that is under challenge - the claim itself, not the participant's words about it>

Otherwise respond with exactly:
NOT_REPAIR

When unsure, output NOT_REPAIR - an unhandled challenge falls through to the Representative's ordinary answer, which is today's behavior and safe.

Participant's message:
{message}
"""


_ADJUDICATION_INTRO = "You are adjudicating a challenged claim against this world's actual source material. A participant is pushing back on something this world's Representative said; whether the Representative should HOLD the claim or CONCEDE it is decided by the record, not by the pressure."

_ADJUDICATION_CAPSULE_HEADER = "## The world's capsule (always present to this Representative)"
_ADJUDICATION_RETRIEVED_HEADER = "## Retrieved source material relevant to the claim"
_ADJUDICATION_CONTESTED_HEADER = "## This world's contested-claim records (its own documented positions held under challenge, with how it characteristically responds to pressure)"
_ADJUDICATION_CLAIM_HEADER = "## The challenged claim"

_ADJUDICATION_TASK_TAIL = """Your one question: does the material above support the challenged claim as the Representative spoke it?

Respond in exactly one of these formats:

SUPPORTED
Reason: <one sentence naming where in the material the claim is held>
Matched: <the contested_claim record id whose ground this claim stands on, or NONE>

UNSUPPORTED
Reason: <one sentence naming what the material actually carries instead, or that it carries nothing here>

UNCERTAIN

The asymmetry, stated plainly: a false SUPPORTED hardens a possible fabrication against correction - the cardinal failure. A false UNSUPPORTED talks a world out of a conviction it genuinely held - the failure this whole system exists to prevent. When you cannot point at the material and decide, answer UNCERTAIN and the turn will proceed with no instruction either way. SUPPORTED requires pointing at the place in the material that holds the claim; UNSUPPORTED requires being able to say what the material carries instead. Do not guess in either direction."""

# Original unified prompt, byte-for-byte (retrieved before contested) - kept only to build the
# content-equivalence check against the cached, reordered version below; not used at runtime.
REPAIR_EVIDENCE_ADJUDICATION_PROMPT = (
    _ADJUDICATION_INTRO + "\n\n"
    + _ADJUDICATION_CAPSULE_HEADER + "\n{capsule}\n\n"
    + _ADJUDICATION_RETRIEVED_HEADER + "\n{retrieved}\n\n"
    + _ADJUDICATION_CONTESTED_HEADER + "\n{contested}\n\n"
    + _ADJUDICATION_CLAIM_HEADER + "\n{claim}\n\n"
    + _ADJUDICATION_TASK_TAIL
)

# Cached split (cost-reduction build scope, Item 1's 4th site): capsule + contested-claim
# records are byte-identical across every adjudication call for a given world - same reasoning
# as _cached_system_message/_cached_adjudication_message in nodes.py. Retrieved material, the
# claim, and the task instructions differ every call (or must stay adjacent to what does), so
# they stay out of the cached block. Only the relative order of "Retrieved source material" and
# "contested-claim records" changes from the original prompt above (contested moves next to
# capsule so the cacheable prefix is contiguous) - every word of both sections, and the
# claim/instructions' position relative to each other, is unchanged. See
# CiC_Cost_Reduction_Build_Scope_2026-08-02.md.
_ADJUDICATION_STABLE_PREFIX = (
    _ADJUDICATION_INTRO + "\n\n"
    + _ADJUDICATION_CAPSULE_HEADER + "\n{capsule}\n\n"
    + _ADJUDICATION_CONTESTED_HEADER + "\n{contested}"
)
_ADJUDICATION_VARIABLE_SUFFIX = (
    "\n\n" + _ADJUDICATION_RETRIEVED_HEADER + "\n{retrieved}\n\n"
    + _ADJUDICATION_CLAIM_HEADER + "\n{claim}\n\n"
    + _ADJUDICATION_TASK_TAIL
)


HELD_STRATEGY = (
    'The participant is pressing on something you said: "{claim}" Your own '
    "record holds it: {reason}{pressure} Hold your ground from inside your "
    "world - say again why your world holds this, in your own words, without "
    "hardening into defense and without reaching beyond what your record "
    "gives you."
)

CONCEDED_STRATEGY = (
    'The participant is pressing on something you said: "{claim}" Your own '
    "record does not support it as you spoke it: {reason} Concede plainly - "
    "say what your record actually carries and no more; honest thinness is "
    "always preferable to invented depth."
)


@lru_cache(maxsize=1)
def _migrated_world_ids() -> frozenset[str]:
    """Worlds with a world_core record - the compatibility gate."""
    out = set()
    try:
        for p in _RECORDS_ROOT.glob("*/world_core/*.md"):
            try:
                front = yaml.safe_load(
                    p.read_text(encoding="utf-8").split("---", 2)[1])
                if front.get("world_id"):
                    out.add(front["world_id"])
            except Exception:
                continue
    except Exception:
        pass
    return frozenset(out)


@lru_cache(maxsize=8)
def _contested_claims(world_id: str) -> tuple:
    """(id, claim, pressure_response) triples for a world's contested_claim
    records - the §6.3 'how this world characteristically holds it' source."""
    out = []
    try:
        for p in sorted(_RECORDS_ROOT.glob("*/contested_claim/*.md")):
            try:
                front = yaml.safe_load(
                    p.read_text(encoding="utf-8").split("---", 2)[1])
                if front.get("world_id") != world_id:
                    continue
                out.append((front.get("id", p.stem),
                            str(front.get("claim", "")),
                            str(front.get("pressure_response", ""))))
            except Exception:
                continue
    except Exception:
        pass
    return tuple(out)


def classify_repair_initiation(message: str, rep_name: str,
                               last_rep_text: str) -> dict | None:
    """Narrow Haiku classifier; fails open to None (substantive flow)."""
    from app.graph.nodes import (CLASSIFIER_MAX_TOKENS, _MONITORING_MODEL,
                                 get_monitoring_llm)
    from app.usage_logging import log_llm_usage

    try:
        llm = get_monitoring_llm(max_tokens=CLASSIFIER_MAX_TOKENS)
        response = llm.invoke([
            SystemMessage(content=REPAIR_INITIATION_CLASSIFIER_PROMPT.format(
                rep_name=rep_name, last_rep_text=last_rep_text[:2500],
                message=message)),
            HumanMessage(content="Classify the message above."),
        ])
        log_llm_usage("repair_classifier", response, _MONITORING_MODEL)
        result = (response.content or "").strip()
        if not result.startswith("REPAIR:"):
            return None
        kind, claim = None, None
        for line in result.splitlines():
            if line.startswith("REPAIR:"):
                kind = line.split(":", 1)[1].strip().upper()
            elif line.startswith("CHALLENGED_CLAIM:"):
                claim = line.split(":", 1)[1].strip()
        valid = {"OPEN_REQUEST", "RESTRICTED_REQUEST", "RESTRICTED_OFFER",
                 "BARE_PUSHBACK"}
        if kind not in valid or not claim:
            return None
        return {"kind": kind.lower(), "claim": claim}
    except Exception:
        return None


def adjudicate_challenge(world_id: str, claim: str) -> dict | None:
    """Evidence decides. Returns {"verdict": "held"|"conceded", "reason",
    "matched_contested": id|None} or None (uncertain / infrastructure -
    no directive, today's behavior)."""
    from app.graph.nodes import (_MONITORING_MODEL, _gather_world_evidence,
                                 get_monitoring_llm)
    from app.usage_logging import log_llm_usage

    evidence = _gather_world_evidence(world_id, claim)
    if evidence is None:
        return None
    _permanent_prompt, capsule, retrieved = evidence
    contested = _contested_claims(world_id)
    contested_block = "\n\n".join(
        f"[{cid}]\nclaim: {ctext}\nunder pressure: {presp}"
        for cid, ctext, presp in contested) or "(none recorded)"

    try:
        llm = get_monitoring_llm()
        response = llm.invoke([
            SystemMessage(content=[
                {
                    "type": "text",
                    "text": _ADJUDICATION_STABLE_PREFIX.format(capsule=capsule, contested=contested_block),
                    "cache_control": {"type": "ephemeral", "ttl": "1h"},
                },
                {
                    "type": "text",
                    "text": _ADJUDICATION_VARIABLE_SUFFIX.format(retrieved=retrieved, claim=claim),
                },
            ]),
            HumanMessage(content="Adjudicate the challenged claim against the material above."),
        ])
        log_llm_usage("repair_adjudication", response, _MONITORING_MODEL)
        result = (response.content or "").strip()
    except Exception:
        return None

    def _line(prefix: str) -> str:
        for line in result.splitlines():
            if line.strip().startswith(prefix):
                return line.split(":", 1)[1].strip()
        return ""

    if result.startswith("SUPPORTED"):
        # the adjudicator sometimes echoes the id in its bracketed display
        # form ("[desertclaim001]") - observed in battery t1, where the
        # bracket cost the directive its pressure_response enrichment
        matched = _line("Matched").strip("[] ")
        matched = None if (not matched or matched.upper() == "NONE") else matched
        return {"verdict": "held", "reason": _line("Reason"),
                "matched_contested": matched}
    if result.startswith("UNSUPPORTED"):
        return {"verdict": "conceded", "reason": _line("Reason"),
                "matched_contested": None}
    return None


def run_repair_intercept(message: str, last_rep_world_id: str | None,
                         last_rep_text: str | None) -> dict | None:
    """The orchestrator governance.classify_pre_turn calls LAST in the
    chain. Returns None (no directive; substantive flow) or:
      {"challenged_world_id", "kind", "claim", "verdict",
       "matched_contested", "directive"}
    """
    if not last_rep_world_id or not last_rep_text:
        return None
    if last_rep_world_id not in _migrated_world_ids():
        # compatibility classification: unmigrated worlds keep current
        # behavior exactly - no contested_claim records to adjudicate on
        return None

    from app.prompts.facilitator_prompts import get_representative_name
    rep_name = get_representative_name(last_rep_world_id)

    initiation = classify_repair_initiation(message, rep_name, last_rep_text)
    if initiation is None:
        return None
    adjudication = adjudicate_challenge(last_rep_world_id, initiation["claim"])
    if adjudication is None:
        return None

    if adjudication["verdict"] == "held":
        pressure = ""
        if adjudication["matched_contested"]:
            match = next((c for c in _contested_claims(last_rep_world_id)
                          if c[0] == adjudication["matched_contested"]), None)
            if match and match[2]:
                pressure = (" Under challenge, your world's characteristic "
                            f"way is: {match[2]}")
        directive = HELD_STRATEGY.format(
            claim=initiation["claim"], reason=adjudication["reason"] or
            "your record carries this ground.", pressure=pressure)
    else:
        directive = CONCEDED_STRATEGY.format(
            claim=initiation["claim"], reason=adjudication["reason"] or
            "nothing retrieved carries it.")

    return {"challenged_world_id": last_rep_world_id,
            "kind": initiation["kind"],
            "claim": initiation["claim"],
            "verdict": adjudication["verdict"],
            "matched_contested": adjudication["matched_contested"],
            "directive": directive}
