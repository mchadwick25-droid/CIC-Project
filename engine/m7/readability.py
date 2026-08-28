"""Deterministic readability (Artifact-8 §3.3): Flesch-Kincaid grade and
Flesch Reading Ease, the two numbers the spec's register instruments name
(plain answer <= FK 10 / FRE >= 60; sourced grounding <= FK 14 / FRE >= 40
- the two-move SPLIT is phase 2; phase 1 reports whole-turn, report-only
per principle 10).

Self-contained on purpose: engine/prose.py owns the fleet's shared
measurement primitives and every grounding verdict flows through it, so a
syllable heuristic does NOT belong there - a readability tweak must never
be able to change what the net withholds. The syllable counter is the
standard vowel-group heuristic with the common silent-e adjustment; it is
honest about being a heuristic, which is fine for a report-only tendency
instrument and would not be fine for a bar (a bar waits on baselines,
principle 10, and would inherit exactly this documented counter so the
baseline and the bar measure the same thing).
"""
import re

_WORD = re.compile(r"[A-Za-z']+")
_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
_VOWEL_GROUP = re.compile(r"[aeiouy]+")

# Below this many words a segment reports as unscored, never as clean
# (spec §Instruments: "short segments report as unscored").
MIN_SCORABLE_WORDS = 30


def syllables(word: str) -> int:
    w = word.lower().strip("'")
    if not w:
        return 0
    count = len(_VOWEL_GROUP.findall(w))
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")) and count > 1:
        count -= 1
    return max(1, count)


def measure(text: str) -> dict:
    """Returns {"scored": bool, "words": n, "sentences": n, "fk_grade": x,
    "fre": x} - fk/fre absent when unscored."""
    words = _WORD.findall(text)
    sents = [s for s in _SENTENCE_SPLIT.split(text.strip()) if s.strip()]
    if len(words) < MIN_SCORABLE_WORDS or not sents:
        return {"scored": False, "words": len(words), "sentences": len(sents)}
    syl = sum(syllables(w) for w in words)
    wps = len(words) / len(sents)
    spw = syl / len(words)
    return {
        "scored": True,
        "words": len(words),
        "sentences": len(sents),
        "fk_grade": round(0.39 * wps + 11.8 * spw - 15.59, 2),
        "fre": round(206.835 - 1.015 * wps - 84.6 * spw, 2),
    }
