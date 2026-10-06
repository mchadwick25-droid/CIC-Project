"""The report-only turn checks, run after the conversation instead of on the
live turn (slice 8): uncited claims, wholly uncited paragraphs, named-claim
grounding, the sentence fact check, and the output families other than the
horizon backstop (display, conversational, pronoun, guard_proximity). Each
reads what the voice_turn event already carries - the net's per-sentence
result in `grounding`, the text and citations - plus the speaker world's
compiled records. A session logged before slice 8 already carries its
output families on the event; those are read by instruments.unread_outputs
and guard_proximity and are not recomputed here.
"""
from engine.m4.named_claim_grounding import find_named_claim_flags
from engine.m4.output_check import check_output
from engine.m4.sentence_fact_check import find_unsupported_named_claims
from engine.m4.uncited_claims import find_uncited_claims, find_uncited_paragraphs
from engine.m7.session_reader import AuditSession, VoiceTurnRecord

LIVE_FAMILIES = frozenset({"horizon"})


def _logged_before_slimming(turn: VoiceTurnRecord) -> bool:
    return any(isinstance(d, dict) and d.get("family") not in LIVE_FAMILIES for d in turn.output_defects)


def _context(s: AuditSession, turn: VoiceTurnRecord) -> tuple[str | None, list[dict]]:
    """The participant message the turn answered and the speaker's earlier
    turns as history, rebuilt from the event log."""
    asked = [m for m in s.participant_messages if m["seq"] < turn.seq]
    history = []
    for earlier in s.voice_turns:
        if earlier.seq >= turn.seq:
            break
        if earlier.speaker == turn.speaker:
            question = next((m["text"] for m in reversed(s.participant_messages) if m["seq"] < earlier.seq), "")
            history += [{"role": "user", "content": question}, {"role": "assistant", "content": earlier.text}]
    return (asked[-1]["text"] if asked else None), history


def offline_checks(s: AuditSession, repositories: dict[str, dict[str, dict]]):
    """Findings for every voice turn in the session. `repositories` maps
    world_key -> that world's compiled records by id."""
    from engine.m7.instruments import Finding

    findings = []
    for turn in s.voice_turns:
        sentences = (turn.grounding or {}).get("sentences") or []
        records = repositories.get(turn.speaker) or {}
        where = f"{turn.speaker}'s turn (seq {turn.seq})"
        uncited = find_uncited_claims(sentences)
        if uncited:
            findings.append(Finding("uncited_claims", "info", s.session_id,
                                    f"{len(uncited)} claim sentence(s) on {where} carry no citation",
                                    excerpt=uncited[0]["sentence"][:200]))
        if turn.grounding and turn.grounding.get("paragraph_coverage"):
            paragraphs = find_uncited_paragraphs(turn.grounding)
            if paragraphs:
                findings.append(Finding("uncited_paragraphs", "info", s.session_id,
                                        f"{len(paragraphs)} sentence(s) on {where} sit in a paragraph with no citation",
                                        excerpt=paragraphs[0]["sentence"][:200]))
        if records:
            for flag in find_named_claim_flags(sentences, repository_records=records):
                findings.append(Finding("named_claim_grounding", "review", s.session_id,
                                        f"{where}: a cited sentence names something its own records do not carry",
                                        record_ids=list(flag.get("tags") or []), excerpt=flag["sentence"][:200]))
            for flag in find_unsupported_named_claims(sentences, repository_records=records):
                findings.append(Finding("sentence_fact_check", "review", s.session_id,
                                        f"{where}: names {', '.join(flag.get('missing') or [])} the world's records do not carry",
                                        record_ids=list(flag.get("tags") or []), excerpt=flag["sentence"][:200]))
        if _logged_before_slimming(turn):
            continue
        participant_message, history = _context(s, turn)
        for defect in check_output(turn.text, history=history, participant_message=participant_message,
                                   citations=turn.citations, repository_records=records or None):
            severity = "defect" if defect["family"] == "guard_proximity" else "review"
            findings.append(Finding(defect["family"], severity, s.session_id, f"{where}: {defect['finding']}",
                                    excerpt=(defect.get("sentence") or "")[:200]))
    return findings
