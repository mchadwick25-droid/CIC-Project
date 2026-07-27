"""Parroting metric (Pass 1 SS5.3; built at S1.3 per F7).

n-gram overlap between prompt material and spoken turns: the fraction of
the spoken text's word n-grams that appear verbatim in the source material.
Deterministic, no LLM. The metric returns a score; the pass/fail ceiling is
TBD-pending-baseline (wrs/parameters.yaml, metric `parroting_overlap`) and
is set at S6.6 from B-PARROT (S5.1). Until then, R7's tolerance is F3's
no-directional-worsening rule.

Default n=6 words: long enough that shared stock phrases ("in the desert")
don't count, short enough that a recited sentence does. n is a parameter of
the instrument, reported alongside every score - never compare scores taken
at different n.
"""
import re


def _ngrams(text: str, n: int):
    words = re.findall(r"[a-z0-9']+", text.lower())
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


def parroting_score(source_text: str, spoken_text: str, n: int = 6) -> dict:
    """Fraction of spoken n-grams present verbatim in the source material.

    Returns {n, spoken_ngrams, overlapping, score}. score = overlapping /
    spoken_ngrams (0.0 when the spoken text is shorter than n words -
    nothing recitable at this n).
    """
    spoken = _ngrams(spoken_text, n)
    if not spoken:
        return {"n": n, "spoken_ngrams": 0, "overlapping": 0, "score": 0.0}
    src = _ngrams(source_text, n)
    overlap = len(spoken & src)
    return {
        "n": n,
        "spoken_ngrams": len(spoken),
        "overlapping": overlap,
        "score": round(overlap / len(spoken), 4),
    }
