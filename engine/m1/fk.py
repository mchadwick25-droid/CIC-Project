"""Flesch-Kincaid grade level, computed from a self-contained syllable
heuristic (vowel-group counting) rather than a dictionary lookup: this
tooling has to run hermetically in CI with no network (this repo's own CI
already states that value explicitly - see .github/workflows/ci.yml's
repository-views-current job comment), and textstat's current cmudict
backend requires a network fetch that this environment's proxy refuses on
SSRF grounds. Standard formula; accuracy is "good enough to gate obviously
dense prose," not lexicographic precision.
"""
import re

_VOWEL_RUN = re.compile(r"[aeiouy]+")
_WORD = re.compile(r"[a-zA-Z']+")
_SENTENCE_END = re.compile(r"[.!?]+")


def _count_syllables(word: str) -> int:
    word = word.lower()
    word = re.sub(r"[^a-z]", "", word)
    if not word:
        return 0
    syllables = len(_VOWEL_RUN.findall(word))
    if word.endswith("e") and not word.endswith("le") and syllables > 1:
        syllables -= 1
    return max(syllables, 1)


def _counts(text: str) -> tuple[int, int, int] | None:
    """(n_words, n_sentences, n_syllables), or None for empty/word-less
    text - shared groundwork for fk_grade and fre_score so the two numbers
    the North Star decision names together (reference/method/Pass2-
    decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md: "FK grade
    band 8-10, FRE >= 60, per emitted turn") are always computed from the
    identical word/sentence/syllable count, never two slightly different
    tokenizations of the same text."""
    text = (text or "").strip()
    if not text:
        return None
    words = _WORD.findall(text)
    if not words:
        return None
    sentences = [s for s in _SENTENCE_END.split(text) if s.strip()]
    n_sentences = max(len(sentences), 1)
    n_words = len(words)
    n_syllables = sum(_count_syllables(w) for w in words)
    return n_words, n_sentences, n_syllables


def fk_grade(text: str) -> float:
    counts = _counts(text)
    if counts is None:
        return 0.0
    n_words, n_sentences, n_syllables = counts
    return 0.39 * (n_words / n_sentences) + 11.8 * (n_syllables / n_words) - 15.59


def fre_score(text: str) -> float:
    """Flesch Reading Ease, the North Star decision's own second number
    (FRE >= 60, the same "hard edge" ruling as fk_grade's FK <= 10 - see
    that decision's RULED section: "Any single emitted turn breaching FK
    <= 10 / FRE >= 60 fails"). Standard formula, same words-per-sentence /
    syllables-per-word terms fk_grade already computes - engine/m7/
    readability.py's own `measure()` already uses this identical formula
    for a live conversation turn; this is the record-field-grading twin
    of that number, not a second, independently-tuned one."""
    counts = _counts(text)
    if counts is None:
        return 100.0
    n_words, n_sentences, n_syllables = counts
    return 206.835 - 1.015 * (n_words / n_sentences) - 84.6 * (n_syllables / n_words)
