"""The phase-1 instrument suite (Artifact-8 §3): deterministic, report-only
(principle 10 - "report-only instruments stay report-only until data earns
them a bar"). Every instrument takes an AuditSession and returns findings
and/or metrics; none calls a model, none writes anywhere.

Severity vocabulary (Artifact-8 §3): defect (the build must fix), review
(Mark or a build thread should read), info (a tracked tendency). Findings
name record ids wherever the evidence does, so routing to a fix is a
lookup (Artifact-8 §6).
"""
import re
from collections import Counter
from dataclasses import dataclass, field

from engine.m7.readability import MIN_SCORABLE_WORDS, measure
from engine.m7.session_reader import AuditSession
from engine.prose import content_words

_WORDS = re.compile(r"[A-Za-z']+")


@dataclass
class Finding:
    instrument: str
    severity: str  # defect | review | info
    session_id: str
    detail: str
    record_ids: list = field(default_factory=list)
    # Voice text and ids only - participant text NEVER rides on a finding
    # (Artifact-8 §4: the fleet layer carries no participant text).
    excerpt: str | None = None


def _record_ids(citations: list) -> list[str]:
    """citations is per-sentence entries ({sentence, record_ids}) in the
    current shape, or bare id strings in older logs - accept both."""
    ids: list[str] = []
    for c in citations:
        if isinstance(c, dict):
            ids.extend(c.get("record_ids") or [])
        elif isinstance(c, str):
            ids.append(c)
    return ids


def unread_outputs(s: AuditSession) -> list[Finding]:
    """§3.1 - the four formerly-unread outputs, surfaced."""
    findings = []
    for t in s.voice_turns:
        if t.do_not_voice_violation:
            findings.append(Finding("do_not_voice", "defect", s.session_id,
                                    f"content-licensing violation on {t.speaker}'s turn (seq {t.seq}): {t.do_not_voice_violation}",
                                    excerpt=t.text[:200]))
        for d in t.output_defects:
            findings.append(Finding("output_defects", "review", s.session_id,
                                    f"output defect on {t.speaker}'s turn (seq {t.seq}): {d}"))
        if t.grounding:
            withheld = [x for x in t.grounding.get("sentences", []) if x.get("verdict") != "ok"]
            if withheld:
                tags = sorted({rid for x in withheld for rid in (x.get("tags") or [])})
                findings.append(Finding("net_withheld", "info", s.session_id,
                                        f"{len(withheld)} sentence(s) on {t.speaker}'s turn (seq {t.seq}) failed net verification "
                                        f"(decoration withheld, text untouched)", record_ids=tags))
        if t.degraded_by_net:
            findings.append(Finding("degraded_by_net", "info", s.session_id,
                                    f"{t.speaker}'s turn (seq {t.seq}) had no substantive survivor"))
    return findings


def isolation(s: AuditSession) -> list[Finding]:
    """§3.2 - the battery's isolation sweep over a real session: a citation
    whose world prefix is not its speaker's is a defect, always."""
    findings = []
    for t in s.voice_turns:
        foreign = [rid for rid in _record_ids(t.citations) if "." in rid and rid.split(".", 1)[0] != t.speaker]
        if foreign:
            findings.append(Finding("isolation", "defect", s.session_id,
                                    f"{t.speaker}'s turn (seq {t.seq}) cites outside its own world",
                                    record_ids=sorted(set(foreign)), excerpt=t.text[:200]))
    return findings


def register_mechanical(s: AuditSession) -> tuple[list[Finding], list[dict]]:
    """§3.3 - FK/FRE per voice turn (whole-turn, phase 1) and the
    first-sentence-answers-first-ask overlap ratio. All info; short turns
    report unscored, never clean."""
    metrics = []
    gate_by_seq = sorted(s.gate_decisions, key=lambda g: g["seq"])
    for t in s.voice_turns:
        m = measure(t.text)
        entry = {"seq": t.seq, "speaker": t.speaker, **m}
        gates_before = [g for g in gate_by_seq if g["seq"] < t.seq]
        asks = (gates_before[-1].get("asks") or []) if gates_before else []
        if asks:
            first_ask = asks[0].get("text", "") if isinstance(asks[0], dict) else str(asks[0])
            first_sentence = re.split(r"(?<=[.!?])\s+", t.text.strip(), maxsplit=1)[0]
            ask_words = content_words(first_ask)
            if ask_words:
                entry["first_sentence_first_ask_overlap"] = round(
                    len(content_words(first_sentence) & ask_words) / len(ask_words), 2
                )
        metrics.append(entry)
    return [], metrics


def ask_coverage(s: AuditSession) -> list[Finding]:
    """§3.4 - a reader ask that drew zero content-word coverage from any
    later voice turn in its exchange is a review finding."""
    findings = []
    for g in s.gate_decisions:
        answering = [t for t in s.voice_turns if t.seq > g["seq"]]
        answering = answering[:4]  # this exchange's turns (a table round is <=4)
        answered_words = set().union(*(content_words(t.text) for t in answering)) if answering else set()
        for ask in g.get("asks") or []:
            ask_text = ask.get("text", "") if isinstance(ask, dict) else str(ask)
            ask_words = content_words(ask_text)
            if ask_words and answering and not (ask_words & answered_words):
                findings.append(Finding("ask_coverage", "review", s.session_id,
                                        f"an ask at seq {g['seq']} drew no content-word coverage from the responding turn(s)"))
    return findings


def repetition(s: AuditSession) -> list[Finding]:
    """§3.5 - repeated 8-grams across one voice's turns within a session."""
    findings = []
    by_speaker: dict[str, list[str]] = {}
    for t in s.voice_turns:
        by_speaker.setdefault(t.speaker, []).append(t.text.lower())
    for speaker, texts in by_speaker.items():
        if len(texts) < 2:
            continue
        seen: dict[tuple, int] = {}
        repeats = 0
        for i, text in enumerate(texts):
            words = _WORDS.findall(text)
            grams = {tuple(words[j:j + 8]) for j in range(len(words) - 7)}
            for g in grams:
                if g in seen and seen[g] != i:
                    repeats += 1
                seen.setdefault(g, i)
        if repeats:
            findings.append(Finding("repetition", "info", s.session_id,
                                    f"{speaker} repeated {repeats} 8-gram(s) across turns"))
    return findings


def safety_review(s: AuditSession) -> list[Finding]:
    """§3.6 - every safety turn listed; intervention-followed-by-abandonment
    (the pattern the spec names) is review, always."""
    findings = []
    safety_turns = [f for f in s.facilitator_turns if f.get("kind") == "safety"]
    for st in safety_turns:
        later_participant = any(m["seq"] > st["seq"] for m in s.participant_messages)
        if not later_participant and s.close_reason != "cap":
            findings.append(Finding("safety_abandonment", "review", s.session_id,
                                    f"safety intervention at seq {st['seq']} was the participant's last exchange "
                                    f"(no later message; close_reason={s.close_reason!r}) - spec: "
                                    f"intervention-followed-by-abandonment"))
        else:
            findings.append(Finding("safety_turn", "info", s.session_id,
                                    f"safety turn at seq {st['seq']}; participant continued: {later_participant}"))
    return findings


def offer_rates(s: AuditSession) -> dict:
    """§3.7 - story/quote citation counts from the id's own type segment
    (per-cell attribution is phase 2)."""
    counts = Counter()
    for t in s.voice_turns:
        for rid in _record_ids(t.citations):
            parts = rid.split(".")
            if len(parts) >= 2:
                counts[parts[1]] += 1
    return dict(counts)


def encounter_openings(s: AuditSession) -> list[Finding]:
    """§3.8 - personal_wound-register messages, with what followed."""
    findings = []
    for g in s.gate_decisions:
        if g.get("register") == "personal_wound":
            after_voice = any(t.seq > g["seq"] for t in s.voice_turns)
            after_safety = any(f["seq"] > g["seq"] and f.get("kind") == "safety" for f in s.facilitator_turns)
            findings.append(Finding("encounter_opening", "info", s.session_id,
                                    f"personal_wound ask at seq {g['seq']}; voice answered: {after_voice}; "
                                    f"safety turn followed: {after_safety}"))
    return findings


def governance(s: AuditSession) -> list[Finding]:
    """§3.9 - dominance flags and close reasons from round_closed, selector
    degradation from turn_selected."""
    findings = []
    for r in s.rounds_closed:
        gov = r.get("governance") or {}
        for flag in gov.get("flags", []) if isinstance(gov, dict) else []:
            findings.append(Finding("governance", "review", s.session_id,
                                    f"round {r.get('round_no')}: {flag}"))
        if r.get("reason") == "floor_unmet_exhausted":
            findings.append(Finding("governance", "review", s.session_id,
                                    f"round {r.get('round_no')} closed floor-unmet"))
    degraded = [t for t in s.turn_selected if t.get("degraded")]
    if degraded:
        findings.append(Finding("selector_degraded", "review", s.session_id,
                                f"{len(degraded)} selector fallback(s): " +
                                "; ".join(str(d.get("reason", ""))[:80] for d in degraded[:3])))
    return findings


def canon_candidate_asks(s: AuditSession) -> list[str]:
    """§3.10 - the raw material for question-canon growth: reader asks,
    normalized. Participant-authored text - the caller keeps this in the
    operator-only output, never the fleet rollup (Artifact-8 §4)."""
    asks = []
    for g in s.gate_decisions:
        for ask in g.get("asks") or []:
            text = ask.get("text", "") if isinstance(ask, dict) else str(ask)
            norm = " ".join(_WORDS.findall(text.lower()))
            if norm:
                asks.append(norm)
    return asks


def run_all(s: AuditSession) -> dict:
    """Every phase-1 instrument over one session. The per-session audit
    document's content half (report.py owns the file shapes)."""
    reg_findings, reg_metrics = register_mechanical(s)
    findings = (
        unread_outputs(s) + isolation(s) + reg_findings + ask_coverage(s)
        + repetition(s) + safety_review(s) + encounter_openings(s) + governance(s)
    )
    return {
        "session_id": s.session_id,
        "mode": s.mode,
        "world_keys": s.world_keys,
        "closed": s.closed,
        "close_reason": s.close_reason,
        "counts": {
            "events": s.event_count,
            "participant_messages": len(s.participant_messages),
            "voice_turns": len(s.voice_turns),
            "safety_turns": sum(1 for f in s.facilitator_turns if f.get("kind") == "safety"),
            "rounds": len(s.rounds_closed),
        },
        "findings": findings,
        "register_metrics": reg_metrics,
        "offer_rates": offer_rates(s),
        "canon_asks": canon_candidate_asks(s),
        "min_scorable_words": MIN_SCORABLE_WORDS,
    }
