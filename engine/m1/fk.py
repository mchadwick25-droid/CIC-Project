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


def fk_grade(text: str) -> float:
    text = (text or "").strip()
    if not text:
        return 0.0
    words = _WORD.findall(text)
    if not words:
        return 0.0
    sentences = [s for s in _SENTENCE_END.split(text) if s.strip()]
    n_sentences = max(len(sentences), 1)
    n_words = len(words)
    n_syllables = sum(_count_syllables(w) for w in words)
    return 0.39 * (n_words / n_sentences) + 11.8 * (n_syllables / n_words) - 15.59
