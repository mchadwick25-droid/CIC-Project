"""Decision 59, check 3: a reply that reproduces a demonstration is a
recitation, not an answer.

A world's demonstration records carry worked Representative turns. A reply
that runs RECITATION_WORDS or more consecutive words of one of them, word for
word, is reading the demonstration out. A run counts only through words the
world's other records do not also carry: a quote given in full is the record
speaking, however many demonstrations also quote it.

Deterministic, no model call. Words are normalised the way
engine.m4.grounding_net normalises a quoted span, after the reply's tags are
stripped.
"""
from engine.m4.grounding_net import _normalize, strip_tags
from engine.prose import all_text

RECITATION_WORDS = 20
# A run this long at the end of the text so far may still grow into a
# recitation, so a streamed reply holds the sentences it touches.
HOLD_WORDS = 8

DIRECTIVE_LINE = "Compose the answer from the records in front of you; do not reproduce a demonstration."

_NOT_EVIDENCE = frozenset({"demonstration", "voice_craft"})


def reply_words(text: str) -> list[str]:
    return _normalize(strip_tags(text)).split()


def _grams(word_lists: list[list[str]], size: int) -> set[tuple[str, ...]]:
    return {tuple(words[i : i + size]) for words in word_lists for i in range(len(words) - size + 1)}


class DemonstrationIndex:
    def __init__(self, repository_records: dict[str, dict]):
        demonstrations: list[list[str]] = []
        for rec in repository_records.values():
            if rec.get("record_type") == "demonstration":
                demonstrations += [
                    _normalize(turn.get("text") or "").split()
                    for turn in rec.get("exchange") or []
                    if turn.get("speaker") == "representative"
                ]
        self._recitation = _grams(demonstrations, RECITATION_WORDS)
        self._hold = _grams(demonstrations, HOLD_WORDS)
        self._records = repository_records
        self._evidence: str | None = None
        self._verdicts: dict[tuple[str, ...], bool] = {}

    @property
    def empty(self) -> bool:
        return not self._recitation

    def _demonstration_only(self, gram: tuple[str, ...]) -> bool:
        """Whether no other record carries these words in a row. The records'
        text is joined and normalised only when a run first matches."""
        if gram not in self._verdicts:
            if self._evidence is None:
                self._evidence = " | ".join(
                    _normalize(all_text(rec)) for rec in self._records.values() if rec.get("record_type") not in _NOT_EVIDENCE
                )
                self._evidence = f" {self._evidence} "
            self._verdicts[gram] = f" {' '.join(gram)} " not in self._evidence
        return self._verdicts[gram]

    def _is_run(self, grams: set[tuple[str, ...]], words: list[str], i: int, size: int) -> bool:
        gram = tuple(words[i : i + size])
        return gram in grams and self._demonstration_only(gram)

    def recitation_start(self, words: list[str]) -> int | None:
        """The index of the first word of the first run of RECITATION_WORDS
        or more consecutive words found in a demonstration, or None."""
        for i in range(len(words) - RECITATION_WORDS + 1):
            if self._is_run(self._recitation, words, i, RECITATION_WORDS):
                return i
        return None

    def hold_start(self, words: list[str]) -> int | None:
        """The index of the first word a streamed reply must not release yet:
        where a recitation begins, or where a run of demonstration words that
        reaches the end of `words` begins."""
        starts = [self.recitation_start(words)]
        chain_end = len(words) - HOLD_WORDS
        i = chain_end
        while i >= 0 and self._is_run(self._hold, words, i, HOLD_WORDS):
            i -= 1
        starts.append(i + 1 if i < chain_end else None)
        found = [start for start in starts if start is not None]
        return min(found) if found else None

    def is_recited(self, text: str) -> bool:
        return self.recitation_start(reply_words(text)) is not None
