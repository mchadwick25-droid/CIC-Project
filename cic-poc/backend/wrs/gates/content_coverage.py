"""Content-coverage parity program (blueprint S2.2's checkpoint instrument,
built at S1.3 per F7 - a checkpoint program cannot be authored in the step
it must pass).

The anti-fan-out check in its purest form: every sentence of a source
chunk's body must land in exactly one migrated record field or an explicit,
logged drop - nothing silently lost, nothing silently duplicated.

Matching is normalized-sentence containment: a chunk sentence counts as
"landed" in a field if its normalized form appears within the field's
normalized text. Normalization strips markdown emphasis, collapses
whitespace, lowercases, and unifies quote/dash characters - so an
equivalent restructure still matches while a dropped or reworded-away
sentence does not.
"""
import re

_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")


def _normalize(text: str) -> str:
    t = text.lower()
    t = re.sub(r"[*_`#>]", " ", t)
    t = t.replace("—", "-").replace("–", "-")
    t = t.replace("‘", "'").replace("’", "'")
    t = t.replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", t).strip()


def sentences(text: str):
    out = []
    for para in text.split("\n"):
        para = para.strip()
        if not para or set(para) <= {"-", "="}:
            continue
        for s in _SENT_SPLIT.split(para):
            s = s.strip()
            if len(_normalize(s)) >= 12:  # skip headings/fragments
                out.append(s)
    return out


def check_coverage(chunk_body: str, record_fields: dict, logged_drops: list) -> dict:
    """chunk_body: the source chunk's body text. record_fields: {field_name:
    text} for the migrated record's prose fields. logged_drops: explicit
    drop entries (each a sentence or sentence-prefix, with its reason
    handled by the caller's log).

    Returns {missing: [...], duplicated: [...], covered: int, total: int}.
    missing = sentences in neither any field nor the drop log.
    duplicated = sentences appearing in MORE than one field.
    """
    norm_fields = {k: _normalize(v) for k, v in record_fields.items() if isinstance(v, str)}
    norm_drops = [_normalize(d) for d in logged_drops]
    missing, duplicated = [], []
    sents = sentences(chunk_body)
    for s in sents:
        ns = _normalize(s)
        hits = [k for k, v in norm_fields.items() if ns in v]
        dropped = any(ns.startswith(d) or d in ns for d in norm_drops)
        if not hits and not dropped:
            missing.append(s)
        elif len(hits) > 1:
            duplicated.append({"sentence": s, "fields": hits})
    return {
        "missing": missing,
        "duplicated": duplicated,
        "covered": len(sents) - len(missing),
        "total": len(sents),
    }
