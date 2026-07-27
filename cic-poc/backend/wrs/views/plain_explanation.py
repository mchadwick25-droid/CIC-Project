"""S5.4 - Level 2: the on-request plain explanation (Pass 1 SS5.6).

Per-record render of:
  - period_sense stated plainly (STRUCTURE-ONLY simplification - the
    constitutional line, RCF V3.2 Part Five: sentence structure only,
    never vocabulary, never claims),
  - a plain-language confidence statement (the constitutional five-level
    formation-confidence vocabulary rendered in ordinary words - the
    level NAME is kept verbatim so the constitutional vocabulary is
    stated, then said plainly),
  - conceptual_distance_note wherever a then-vs-now gap exists,
machine-checked at render time against the reading floor that lives in
wrs/parameters.yaml (reading_floor: FK band 8-10, FRE >= 60 - both
governing documents point at that file, SS5.6).

Structure-only transformations, enumerated (nothing else is legal here):
  1. citation-apparatus parentheticals stripped: any "(...)" whose content
     is build-document apparatus (Doc_NN, SS-references, CO/FLAG ids) -
     apparatus belongs to Level 3, not Level 2;
  2. sentence splits at "; " and " -- " (em-dash) boundaries: each clause
     becomes its own sentence, capitalized, period-terminated.
Vocabulary and claims pass through verbatim. No word is ever replaced,
added, or dropped except the apparatus class in (1); the confidence
statement is the one deliberately NEW text (its five-level term is
quoted verbatim, then said plainly - it renders the record's confidence
field, it does not restate the meaning).

Same content for every participant; registers never gate access
(Article 30, per SS5.6).

Deterministic: same records -> byte-identical renders.

Usage (from cic-poc/backend):
  python wrs/views/plain_explanation.py            # render + floor-check all terms
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
for p in (str(HERE), str(BACKEND)):
    if p not in sys.path:
        sys.path.insert(0, p)

from chunk_views import load_records  # noqa: E402

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
    """The reading floor, read from wrs/parameters.yaml (SS5.6: the number
    lives in the operational-parameters file; this view is a consumer,
    never a second home for the value). Fail-open to the RCF values the
    file itself cites."""
    import yaml
    try:
        params = yaml.safe_load(
            (BACKEND / "wrs" / "parameters.yaml").read_text(encoding="utf-8"))
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

    # -- the meaning, stated plainly (period_sense, structure-simplified).
    # FLAG-012: a record with no period_sense says so honestly - never a
    # silent substitution of quick_meaning (different field, different job;
    # silent swapping is the drift class SS3.9 abolishes).
    period_sense = term.get("period_sense", "") or ""
    if period_sense.strip():
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

    # -- then-vs-now, wherever a gap exists --
    note = term.get("conceptual_distance_note", "").strip()
    if note:
        gap = " ".join(_sentences(note))
        sections.append(("Then vs. now", gap))

    body = "\n\n".join(f"{text}" for _t, text in sections)
    fk_max, fre_min = _load_floor()

    from wrs.gates.core import readability_check  # S1.3's instrument, reused
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
    terms = records if records is not None else load_records("term")
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
