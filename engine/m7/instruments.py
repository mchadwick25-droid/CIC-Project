"""The phase-1 instrument suite (Artifact-8 §3): deterministic, report-only
(principle 10 - "report-only instruments stay report-only until data earns
them a bar"). Every instrument takes an AuditSession and returns findings
and/or metrics; none calls a model, none writes anywhere.

Severity vocabulary (Artifact-8 §3): defect (the build must fix), review
(a human or a build thread should read), info (a tracked tendency). Findings
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


def _defect_family(d) -> str | None:
    return d.get("family") if isinstance(d, dict) else None


def unread_outputs(s: AuditSession) -> list[Finding]:
    """§3.1 - the four formerly-unread outputs, surfaced.

    guard_proximity entries are excluded from this generic bucket - they
    get their own dedicated instrument (guard_proximity, below) at defect
    severity, since a barred-claim proximity hit is the one output_check
    family that is a live fabrication risk, not a cosmetic/register issue
    like the other three; reporting the identical finding twice at two
    different severities in the same audit would be noise, not signal.
    """
    findings = []
    for t in s.voice_turns:
        if t.do_not_voice_violation:
            findings.append(Finding("do_not_voice", "defect", s.session_id,
                                    f"content-licensing violation on {t.speaker}'s turn (seq {t.seq}): {t.do_not_voice_violation}",
                                    excerpt=t.text[:200]))
        for d in t.output_defects:
            if _defect_family(d) == "guard_proximity":
                continue
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


def guard_proximity(s: AuditSession) -> list[Finding]:
    """Build-Plan.md Stage 4b: the guard_proximity family
    (engine.m4.output_check), read at defect severity - the one
    output_check family that is a live fabrication risk (a sentence
    sharing a cited record's own barred claim), not a cosmetic/register
    issue like the other three. Feeds R14 (Rulings-Pending.md): reports
    only, same as every instrument in this module, never a block."""
    findings = []
    for t in s.voice_turns:
        for d in t.output_defects:
            if _defect_family(d) != "guard_proximity":
                continue
            findings.append(Finding("guard_proximity", "defect", s.session_id,
                                    f"{t.speaker}'s turn (seq {t.seq}): {d.get('finding')}",
                                    excerpt=(d.get("sentence") or "")[:200]))
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


_QUOTED_SPAN = re.compile(r"[\"“][^\"”]{3,}[\"”]|(?<!\w)'[^']{15,}'(?!\w)")


def _strip_quoted(text: str) -> str:
    """The tradition's own words are exempt from the plain band: quotes
    are never screened by readability - the
    band governs OUR words, never theirs. Straight-single-quote spans
    only count at length, so contractions survive."""
    return _QUOTED_SPAN.sub(" ", text)


def register_mechanical(s: AuditSession) -> tuple[list[Finding], list[dict]]:
    """§3.3 - FK/FRE per voice turn and the first-sentence-answers-first-ask
    overlap ratio. All info; short turns report unscored, never clean.
    Primary numbers are measured with quoted spans stripped (the plain band
    has no jurisdiction over quoted material);
    whole-turn numbers ride alongside as fk_grade_whole/fre_whole."""
    metrics = []
    gate_by_seq = sorted(s.gate_decisions, key=lambda g: g["seq"])
    for t in s.voice_turns:
        stripped = _strip_quoted(t.text)
        m = measure(stripped)
        entry = {"seq": t.seq, "speaker": t.speaker, **m}
        # Cadence, measured never gated (the register-translation pass,
        # 2026-08-29: the fragment-poetic register lived in record prose and
        # was invisible to grade-level numbers - FK sat in-band while the
        # prose chanted). Spaced em-dashes per 100 words and the share of
        # sentences of five words or fewer make that drift visible per turn.
        words = stripped.split()
        if words:
            entry["dash_per_100w"] = round(100 * stripped.count(" - ") / len(words), 2)
        sentences = [x.strip() for x in re.split(r"(?<=[.!?])\s+", stripped) if x.strip()]
        if sentences:
            entry["fragment_ratio"] = round(
                sum(1 for x in sentences if len(x.split()) <= 5) / len(sentences), 2
            )
        whole = measure(t.text)
        if whole.get("scored"):
            entry["fk_grade_whole"] = whole["fk_grade"]
            entry["fre_whole"] = whole["fre"]
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


_STORY_RECORD_TYPES = frozenset({"story", "quote"})
_WITNESS_RECORD_TYPES = frozenset({"doctrinal_witness"})


def _legacy_anchor_marks(anchors: list[dict]) -> int:
    """A plan recorded before per-element placement (Decision-Log.md Entry
    69) carries sentence-run `anchors` and no `elements`; counted the way
    the anchor-era renderer drew it - one mark per (placement, family),
    witness runs placed at their start, story/quote runs at their end.
    The frontend now shows such a stored turn through its legacy renderer,
    which places the same families at run ends; this count is the
    historical record of what those turns carried, not a live render."""
    placements: set[tuple[int, str]] = set()
    for a in anchors:
        record_type = a.get("record_type")
        if record_type in _WITNESS_RECORD_TYPES:
            placements.add((a.get("run_start_sentence"), "witness"))
        elif record_type in _STORY_RECORD_TYPES:
            placements.add((a.get("run_end_sentence"), "story"))
    return len(placements)


def level1_element_density(s: AuditSession) -> list[dict]:
    """Stage 6d / R17 (Rulings-Pending.md, Decision-Log.md Entry 29): "an M7
    instrument counting Level-1 elements per turn" (Adjusted-Design.md's
    N2). Report-only, no findings (principle 10: report-only instruments
    stay report-only until data earns them a bar) - this measures, it
    does not enforce. Metrics only, same shape as register_mechanical's
    own metrics half.

    A "Level-1 element" is an inline mark visible directly in the running
    text, never a Level-2/3 tap-through. Read from transparency.elements
    (engine.m4.transparency_plan; R31, R31-A, R31-B), which is exactly
    what VoiceTurnBody.tsx's renderFromTransparencyPlan draws - one mark
    per element, placed at the element:
    - a citation mark per `quote` or `story` element;
    - a figure mark per `figure` element;
    - a gloss mark per `term` element.
    General references (end_references) are not inline and are not
    counted. A plan with no `elements` predates per-element placement and
    is counted from its anchors (_legacy_anchor_marks, with figures_used/
    glosses for word marks).

    Before the R17 cap: this counts every candidate, not what survives
    the renderer's own cap.
    """
    metrics = []
    for t in s.voice_turns:
        transparency = t.transparency or {}
        elements = transparency.get("elements")
        if elements is not None:
            kinds = [e.get("kind") for e in elements]
            citation_marks = sum(k in ("quote", "story") for k in kinds)
            figure_marks = kinds.count("figure")
            gloss_marks = kinds.count("term")
        else:
            citation_marks = _legacy_anchor_marks(transparency.get("anchors") or [])
            figure_marks = len(t.figures_used)
            gloss_marks = len(t.glosses)
        sentence_count = len([x for x in re.split(r"(?<=[.!?])\s+", t.text.strip()) if x.strip()])
        metrics.append({
            "seq": t.seq,
            "speaker": t.speaker,
            "citation_marks": citation_marks,
            "figure_marks": figure_marks,
            "gloss_marks": gloss_marks,
            "level1_total": citation_marks + figure_marks + gloss_marks,
            "sentence_count": sentence_count,
        })
    return metrics


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


def cited_ids(s: AuditSession) -> list[str]:
    """§3.7's utilization half: every distinct record id this session's
    voices actually cited. Record ids carry no participant text, so the
    list rides the fleet layer; the rollup unions these per world against
    each world's citable shelf to answer "what share of what we built do
    conversations actually draw on?"."""
    ids: set[str] = set()
    for t in s.voice_turns:
        ids.update(_record_ids(t.citations))
    return sorted(ids)


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


def cross_voice_echo(s: AuditSession) -> list[Finding]:
    """§3.5's cross-voice half, added 2026-08-28 after the F1 register-reach
    battery: two DIFFERENT voices in one round sharing long word runs is a
    distinctiveness defect the within-voice repetition instrument cannot
    see (the battery's L4 turns opened near-verbatim alike across all
    three seats; the Gemini outside read named it 'template echo').
    Deterministic: shared 6-grams across distinct speakers in the same
    round -> review. Interview sessions have one voice and are skipped."""
    findings = []
    by_round: dict[int, list] = {}
    for t in s.voice_turns:
        if t.round_no is not None:
            by_round.setdefault(t.round_no, []).append(t)
    for round_no, turns in by_round.items():
        grams: dict[tuple, str] = {}
        for t in turns:
            words = _WORDS.findall(t.text.lower())
            for j in range(len(words) - 5):
                g = tuple(words[j:j + 6])
                if g in grams and grams[g] != t.speaker:
                    findings.append(Finding("cross_voice_echo", "review", s.session_id,
                                            f"round {round_no}: {t.speaker} echoes {grams[g]}'s wording "
                                            f"(shared run: \"{' '.join(g)}\")"))
                    break  # one finding per turn, not per gram
                grams.setdefault(g, t.speaker)
    return findings


def register_frame(s: AuditSession, names: dict[str, list[str]] | None = None) -> list[Finding]:
    """§3.3's frame half: a voice standing OUTSIDE its own world's witness. A
    read of syr's first answer ("To this world Jesus is...") named it -
    "this should be first person plural" - and the pairing batteries had
    already shown the same family twice (P1-L4 Papnoute in the third
    person; F1-L4 a "Papnoute (Desert Monasticism):" label echo). Three
    deterministic detectors, all review:

    - "this world" / "to this world" in a voice's own turn - the communal
      witness ("we", "our") never calls itself "this world".
    - the voice's own representative or world name in its own running text
      (names supplied by the caller from the registry; keyed by the
      speaker's world_key).
    - a leading "Name (World):" label echo - transcript attribution
      format bleeding into the spoken text.
    """
    findings = []
    names = names or {}
    for t in s.voice_turns:
        lowered = t.text.lower()
        if "this world" in lowered:
            findings.append(Finding("register_frame", "review", s.session_id,
                                    f"{t.speaker}'s turn (seq {t.seq}) speaks of its own world in the third person "
                                    f"(\"this world\") - the witness register is first person plural",
                                    excerpt=t.text[:160]))
        for own_name in names.get(t.speaker, []):
            if own_name and own_name.lower() in lowered:
                findings.append(Finding("register_frame", "review", s.session_id,
                                        f"{t.speaker}'s turn (seq {t.seq}) says its own name ({own_name!r}) in its "
                                        f"running text - third-person self-reference",
                                        excerpt=t.text[:160]))
                break
        if re.match(r"^\s*\S[^:\n]{0,60}\([^)]{1,60}\)\s*:", t.text):
            findings.append(Finding("register_frame", "review", s.session_id,
                                    f"{t.speaker}'s turn (seq {t.seq}) opens with a \"Name (World):\" label echo",
                                    excerpt=t.text[:160]))
    return findings


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


def run_all(s: AuditSession, names: dict[str, list[str]] | None = None) -> dict:
    """Every phase-1 instrument over one session. The per-session audit
    document's content half (report.py owns the file shapes). `names` maps
    world_key -> that world's own names (representative, display, card)
    for the register_frame self-reference detector; the CLI builds it from
    the registry."""
    reg_findings, reg_metrics = register_mechanical(s)
    findings = (
        unread_outputs(s) + isolation(s) + reg_findings + ask_coverage(s)
        + repetition(s) + cross_voice_echo(s) + safety_review(s)
        + register_frame(s, names) + encounter_openings(s) + governance(s)
        + guard_proximity(s)
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
        "level1_element_density": level1_element_density(s),
        "offer_rates": offer_rates(s),
        "cited_record_ids": cited_ids(s),
        "canon_asks": canon_candidate_asks(s),
        "min_scorable_words": MIN_SCORABLE_WORDS,
    }
