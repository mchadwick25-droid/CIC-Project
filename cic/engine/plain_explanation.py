"""S5.4 - Level 2: the on-request plain explanation (Pass 1 SS5.6).

CO-P2-12 (Mark, 2026-07-27, resolving FLAG-011): Level 2's content
source is the AUTHORED `plain_explanation` field - the record's meaning
and its then-vs-now gap written in plain language TO the reading floor,
rendered VERBATIM here (the machine check verifies the authoring, it
never manufactures plainness). The floor lives in old-tree:parameters.yaml
(reading_floor: FK band 8-10, FRE >= 60) and is computed at render time
on every render, always.

Render composition per term:
  - the authored plain_explanation, verbatim (meaning + then-vs-now gap
    - the gap content SS5.6 assigns to Level 2 is folded into the
    authored text; the scholarly conceptual_distance_note itself stays
    a Level 3 field);
  - a plain-language confidence statement (the constitutional five-level
    formation-confidence vocabulary: level NAME quoted verbatim, then
    said plainly).

Fallback (records not yet carrying the authored field - none in Desert
today; future mid-authoring worlds): the FLAG-011-era structure-only
simplification of period_sense, kept so the view never silently invents
content. Its transformations, still the only legal ones on that path:
  1. citation-apparatus parentheticals stripped (Doc_NN/SS/CO/FLAG
     patterns - apparatus belongs to Level 3);
  2. sentence splits at "; " and " -- " (em-dash) boundaries.
On the fallback path vocabulary and claims pass through verbatim; a
record with no period_sense either says so honestly (FLAG-012).

Same content for every participant; registers never gate access
(Article 30, per SS5.6).

Deterministic: same records -> byte-identical renders.

Usage (from the old tree/backend):
  python old-tree:views/plain_explanation.py            # render + floor-check all terms
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


# ---------------------------------------------------------------------------
# The constitutional five-level vocabulary, said plainly. The level name is
# kept verbatim (vocabulary is never replaced - it is stated, then explained).
# Article 17 vocabulary per the L4 templates; SS3.0's confidence row.
# ---------------------------------------------------------------------------
CONFIDENCE_PLAIN = {
    "Documented": (
        "the sources from that time state this directly."
    ),
    "Widely Accepted": (
        "nearly all scholars who study this world read the evidence this way."
    ),
    "Dominant Modern Reconstruction": (
        "this is the leading modern scholarly reading. It is built up from "
        "the evidence, not stated outright in any ancient source."
    ),
    "Contested": (
        "scholars genuinely disagree about this. More than one serious "
        "reading of the evidence exists."
    ),
    "Inferential-Thin": (
        "this rests on thin evidence and inference. Hold it loosely."
    ),
}

# Citation-apparatus parentheticals: Doc_NN, section signs, CO/FLAG ids,
# "cf." chains of the same. Semantic parentheticals (real words of the
# claim) are NOT matched and pass through untouched.
_APPARATUS_RE = re.compile(
    r"\s*\((?=[^)]*(?:Doc_\d|§|CO-|FLAG-))[^)]*\)"
)

_EMDASH_SPLIT_RE = re.compile(r"\s+—\s+")


def _load_floor() -> tuple[float, float]:
    """The reading floor, read from the engine parameters file (SS5.6: the number
    lives in the operational-parameters file; this view is a consumer,
    never a second home for the value). Fail-open to the RCF values the
    file itself cites."""
    import yaml
    try:
        params = yaml.safe_load(
            (HERE / "parameters.yaml").read_text(encoding="utf-8"))
        floor = params["parameters"]["reading_floor"]
        band = floor["flesch_kincaid_grade_band"]
        return float(band[1]), float(floor["flesch_reading_ease_min"])
    except Exception:
        return 10.0, 60.0


def _sentences(text: str) -> list[str]:
    """Structure-only simplification of one prose field (transformations
    1 and 2 of the module contract)."""
    text = _APPARATUS_RE.sub("", text).strip()
    # split at clause boundaries that read as full stops in plain register
    parts: list[str] = []
    for chunk in text.split("; "):
        parts.extend(_EMDASH_SPLIT_RE.split(chunk))
    out = []
    for part in parts:
        part = part.strip().strip(";").strip()
        if not part:
            continue
        # capitalize the (possibly mid-clause) fragment and close it
        part = part[0].upper() + part[1:]
        if part[-1] not in ".!?":
            part += "."
        out.append(part)
    return out


def _plain_name(term_name: str) -> str:
    """'Anachōrēsis (Withdrawal)' -> primary name as written."""
    return term_name.strip()


def render_plain_explanation(term: dict) -> dict:
    """The Level 2 face of one term record. Returns the render plus its
    at-render-time floor check (SS5.6: computed at render time, always)."""
    name = _plain_name(term.get("term", ""))
    sections: list[tuple[str, str]] = []

    # -- the meaning: the authored plain_explanation, verbatim (CO-P2-12).
    authored = (term.get("plain_explanation") or "").strip()
    period_sense = term.get("period_sense", "") or ""
    if authored:
        sections.append(("What it meant in this world", authored))
    elif period_sense.strip():
        # fallback: FLAG-011-era structure-only simplification
        meaning = " ".join(_sentences(period_sense))
        sections.append(("What it meant in this world", meaning))
    else:
        # participant-facing copy states the mechanism plainly; the flag
        # id stays builder-facing (here and in FLAGS.md), not in the render
        sections.append((
            "What it meant in this world",
            "This record does not yet carry a period-sense entry. "
            "The full record (Level 3) shows what it does carry.",
        ))

    # -- plain-language confidence statement (wherever the record carries
    #    one - the R checkpoint's own criterion) --
    conf = term.get("confidence") or {}
    level = conf.get("formation_confidence")
    if level:
        plain = CONFIDENCE_PLAIN.get(level)
        statement = f"How sure is this? The record's level is \"{level}\": {plain}" if plain \
            else f"How sure is this? The record's level is \"{level}\"."
        sections.append(("How sure is this", statement))

    # -- then-vs-now, wherever a gap exists (fallback path only: the
    # authored text carries the gap itself per CO-P2-12; the scholarly
    # note stays Level 3) --
    note = term.get("conceptual_distance_note", "").strip()
    if note and not authored:
        gap = " ".join(_sentences(note))
        sections.append(("Then vs. now", gap))

    body = "\n\n".join(f"{text}" for _t, text in sections)
    fk_max, fre_min = _load_floor()

    from gates import readability_check  # S1.3's instrument, reused
    check = readability_check(body, fk_max=fk_max, fre_min=fre_min)
    check["ok"] = not check["violations"]

    return {
        "record_id": term.get("id"),
        "term": name,
        "sections": [
            {"title": t, "text": text} for t, text in sections
        ],
        "readability": check,
    }


def render_all(records: dict[str, dict] | None = None) -> list[dict]:
    terms = records if records is not None else {}
    return [render_plain_explanation(t)
            for _id, t in sorted(terms.items())]


if __name__ == "__main__":
    renders = render_all()
    bad = 0
    for r in renders:
        chk = r["readability"]
        flag = "PASS" if chk["ok"] else "FAIL " + "; ".join(chk["violations"])
        if not chk["ok"]:
            bad += 1
        print(f"{r['record_id']}  FK {chk['fk_grade']:5.2f}  FRE {chk['fre']:6.2f}  {flag}")
    print(f"\n{len(renders) - bad}/{len(renders)} renders at the floor")
