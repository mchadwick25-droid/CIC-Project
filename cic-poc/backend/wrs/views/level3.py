"""S5.4 - Level 3: the full scholarly apparatus, scaffolded (Pass 1 SS5.6).

Level 3 is the complete record - attribution status, edition and
translation, evidentiary weight, Author Gravity notes, transmission
path, field state, the full source rows - presented as a scaffold, not
a field dump: an Observe -> Reflect -> Question layer sits on top (the
LC model; doc 12 claims a stated design intent for it, not a tested
shape - adopted here as A STARTING SHAPE TO TEST, said plainly, per
SS5.6), with the full record reachable beneath.

The scaffold is deterministic and generated from the record's own
structured data - Observe states what the record contains, Reflect
states what kind of claim it is (the confidence axes in the
constitutional vocabulary, plus the author-gravity notes), Question
asks what the record's own structure marks as live (tension edges,
contested-claim links, UNVERIFIED markers, thin confidence). Nothing
is invented: every scaffold line traces to a field.

Rights note: this module renders whatever record dict it is handed.
The rights gate (display_permitted, FLAG-013 fail-closed) is applied
UPSTREAM by repository.py, which withholds gated text fields before
any render sees them - so a leak would require bypassing the
composition, not a bug inside it.

The retrieval-audit backbone for live conversations is the /audit
endpoint (S4.2) - the repository's Level 3 face covers the record side;
the per-conversation side already exists and is linked, not duplicated.

Deterministic: same records -> byte-identical renders.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
for p in (str(HERE), str(BACKEND)):
    if p not in sys.path:
        sys.path.insert(0, p)

from plain_explanation import CONFIDENCE_PLAIN  # noqa: E402

SCAFFOLD_NOTE = (
    "This Observe-Reflect-Question shape is a starting scaffold being "
    "tested, not a settled method."
)


def _title(rec: dict) -> str:
    rt = rec.get("record_type")
    if rt == "term":
        return rec.get("term", rec.get("id", ""))
    if rt in ("story", "ambient"):
        return rec.get("title", rec.get("id", ""))
    if rt == "quote":
        return f"Saying - {rec.get('locus', rec.get('id', ''))}"
    if rt == "figure":
        names = rec.get("names") or []
        return names[0]["name"] if names else rec.get("id", "")
    if rt in ("gravity", "force"):
        return rec.get("name", rec.get("id", ""))
    if rt == "contested_claim":
        claim = rec.get("claim", "")
        return claim if len(claim) <= 90 else claim[:87] + "..."
    if rt == "source":
        return rec.get("work_title", rec.get("id", ""))
    if rt == "world_core":
        return "The world's own ground"
    return rec.get("id", "")


def _confidence_lines(conf: dict) -> list[str]:
    if not conf:
        return []
    lines = []
    level = conf.get("formation_confidence")
    if level:
        plain = CONFIDENCE_PLAIN.get(level, "")
        lines.append(f'Formation confidence: "{level}" - {plain}' if plain
                     else f'Formation confidence: "{level}".')
    weight = conf.get("evidentiary_weight")
    if weight:
        lines.append(f"Evidentiary weight: {weight}.")
    spec = conf.get("citation_specificity")
    state = conf.get("verification_state")
    if spec or state:
        lines.append(
            "Citation: "
            + " / ".join(x for x in (f"specificity {spec}" if spec else "",
                                     state or "") if x) + ".")
    return lines


def _source_lines(rec: dict, sources: dict[str, dict]) -> list[str]:
    """The full source rows behind this record, with Author Gravity notes -
    an existing CiC strength (doc 12's own baseline), carried whole."""
    lines = []
    for s in rec.get("sources", []) or []:
        sid = s.get("source_id")
        row = sources.get(sid, {})
        bits = [row.get("work_author", ""), row.get("work_title", "")]
        cite = ", ".join(b for b in bits if b) or sid or "?"
        lines.append(f"{sid}: {cite}")
        note = (s.get("author_gravity_note") or "").strip()
        if note:
            lines.append(f"  Author Gravity - {note}")
    return lines


def _observe(rec: dict, sources: dict[str, dict]) -> list[str]:
    """What is actually in front of you - stated from the record."""
    rt = rec.get("record_type")
    out: list[str] = []
    if rt == "term":
        if rec.get("period_sense"):
            out.append(f"Sense in this world: {rec['period_sense']}")
        if rec.get("prior_sense"):
            out.append(f"Sense before this world: {rec['prior_sense']}")
        if rec.get("modern_sense"):
            out.append(f"How it is heard today: {rec['modern_sense']}")
    elif rt == "story":
        out.append(f"Narrative tier: {rec.get('narrative_tier', '?')}.")
        if rec.get("attested_occasion"):
            out.append(f"Attested occasion: {rec['attested_occasion']}")
        text = rec.get("text")
        out.append(text if isinstance(text, str) and text else
                   "Story text: (withheld or absent - see rights note)")
    elif rt == "quote":
        out.append(f"Speaker/author record: {rec.get('speaker_or_author', '?')}.")
        out.append(f"Locus: {rec.get('locus', '?')}.")
        text = rec.get("text_translation")
        if isinstance(text, str) and text:
            out.append(f'Text: "{text}"')
        else:
            out.append("Text: withheld from public display "
                       "(rights not established - FLAG-013 fail-closed). "
                       "The locus above is the road to it.")
        if rec.get("translation_used"):
            out.append(f"Translation used: {rec['translation_used']}.")
        if rec.get("license"):
            out.append(f"License basis: {rec['license']}.")
    elif rt == "figure":
        for n in rec.get("names", []) or []:
            out.append(f"Name: {n.get('name')} ({n.get('name_kind', '?')}).")
        out.append("Narratable: "
                   + ("yes" if rec.get("narratable") else "no") + ".")
        if rec.get("accepted_refusal_note"):
            out.append(f"Accepted refusal: {rec['accepted_refusal_note']}")
    elif rt == "gravity":
        out.append(f"Classification: {rec.get('classification', '?')}.")
        six = rec.get("six_tests") or {}
        for name, cell in six.items():
            verdict = cell.get("verdict", "") if isinstance(cell, dict) else str(cell)
            out.append(f"Test - {name}: {verdict}")
    elif rt == "force":
        pos = rec.get("six_cell_position", {})
        if isinstance(pos, dict):
            out.append("Six-cell position: "
                       + " / ".join(str(v) for v in pos.values()) + ".")
        for key, label in (
                ("layer_historical_event", "Historical event"),
                ("layer_worlds_own_experience", "The world's own experience"),
                ("layer_formation_impact", "Formation impact")):
            if rec.get(key):
                out.append(f"{label}: {rec[key]}")
    elif rt == "contested_claim":
        out.append(f"The claim: {rec.get('claim', '')}")
        for h in rec.get("held_against", []) or []:
            if isinstance(h, dict):
                out.append(f"Held against: {h.get('challenge', h)}")
    elif rt == "source":
        for key, label in (
                ("work_author", "Author"), ("work_title", "Title"),
                ("work_locus", "Locus/date"), ("edition", "Edition"),
                ("translation", "Translation"), ("language", "Language"),
                ("attribution_status", "Attribution status"),
                ("transmission_path", "Transmission path"),
                ("field_state", "Field state")):
            if rec.get(key):
                out.append(f"{label}: {rec[key]}")
    elif rt == "world_core":
        for key, label in (("time_window", "Time window"),
                           ("horizon", "Horizon"),
                           ("formation_logic", "Formation logic"),
                           ("telos", "Telos")):
            if rec.get(key):
                out.append(f"{label}: {rec[key]}")
    return [x for x in out if x]


def _reflect(rec: dict, sources: dict[str, dict]) -> list[str]:
    """What kind of claim this is - the evidentiary situation."""
    out = _confidence_lines(rec.get("confidence") or {})
    if rec.get("record_type") == "term" and rec.get("conceptual_distance_note"):
        out.append(f"Then vs. now: {rec['conceptual_distance_note']}")
    src = _source_lines(rec, sources)
    if src:
        out.append("The source rows this record stands on:")
        out.extend(src)
    if rec.get("record_type") == "gravity" and rec.get("confidence_crosscheck"):
        out.append(f"Confidence cross-check: {rec['confidence_crosscheck']}")
    return out


def _question(rec: dict, records_by_id: dict[str, dict]) -> list[str]:
    """Questions the record's own structure marks as live. Every line
    traces to a field; nothing is editorial."""
    out: list[str] = []
    rt = rec.get("record_type")
    conf = rec.get("confidence") or {}
    if conf.get("formation_confidence") in ("Contested", "Inferential-Thin"):
        out.append(
            f"This record's confidence level is "
            f"\"{conf['formation_confidence']}\" - what would count as "
            "better evidence, and does it exist?")
    if rt == "term":
        for edge in rec.get("field_relations", []) or []:
            if edge.get("type") == "tension-with":
                partner = records_by_id.get(edge.get("target_id"), {})
                pname = partner.get("term", edge.get("target_id"))
                out.append(
                    f"This record stands in documented tension with "
                    f"{pname} - how did the world hold both?")
        if "UNVERIFIED" in (rec.get("prior_sense") or ""):
            out.append(
                "The pre-world sense above is marked UNVERIFIED against a "
                "registry source - what would verifying it change?")
        for cid in rec.get("contested_claim_ids", []) or []:
            claim = records_by_id.get(cid, {})
            if claim:
                out.append(
                    f"A contested claim rides on this term: "
                    f"\"{claim.get('claim', cid)}\" - who contests it, "
                    "and on what evidence?")
    if rt == "contested_claim":
        for d in rec.get("divergence_partners", []) or []:
            if isinstance(d, dict):
                pw = d.get("world_id") or d.get("partner_world") or "?"
                out.append(
                    f"Another world ({pw}) reads this differently - "
                    "what does each world's reading protect?")
    if rt == "story" and str(rec.get("narrative_tier", "")).startswith("4"):
        out.append(
            "This story is a marked composite reconstruction (Tier 4) - "
            "which elements are attested, and which are typical-of-the-"
            "world reconstruction? Its source rows answer per element.")
    if rt == "source" and rec.get("attribution_status") not in (None, "genuine"):
        out.append(
            f"Attribution status is \"{rec.get('attribution_status')}\" - "
            "how does that change what this source can carry?")
    return out


def render_level3(rec: dict, sources: dict[str, dict],
                  records_by_id: dict[str, dict]) -> dict:
    """The Level 3 face of one record: the scaffold on top, the full
    record beneath."""
    full = {k: v for k, v in rec.items() if not k.startswith("_")}
    return {
        "record_id": rec.get("id"),
        "record_type": rec.get("record_type"),
        "title": _title(rec),
        "scaffold_note": SCAFFOLD_NOTE,
        "observe": _observe(rec, sources),
        "reflect": _reflect(rec, sources),
        "question": _question(rec, records_by_id),
        "full_record": full,
        "conversation_audit_backbone": (
            "For claims made in a live conversation, the per-session "
            "retrieval audit is at /api/session/{session_id}/audit (S4.2)."
        ),
    }
