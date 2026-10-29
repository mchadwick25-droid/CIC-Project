import re
import unicodedata
from dataclasses import dataclass

from .prompting import CONTEXT_WORD_LIMIT

STEM_LENGTH = 5
NOVEL_WORD_RATIO_LIMIT = 0.3

STRUCTURAL_WORDS = frozenset(
    """
    passage passages section sections chapter chapters book books letter letters sermon sermons homily homilies
    treatise work works text author division part parts follows follow follows preceding following before after
    begins opens continues closes ends concludes introduces discusses describes argues explains addresses answers
    develops turns moves returns urges warns exhorts appeals responds cites quotes reports recounts presents states
    gives offers sets continues builds comes leads follows reads speaks writes written preceded followed earlier
    later within between about concerning regarding where while which whose their there these those other another
    ahead opening closing middle early final general particular specific briefly further again also still
    """.split()
)
_WORD = re.compile(r"[^\W\d_]+(?:['’-][^\W\d_]+)*|\d+", re.UNICODE)


@dataclass(frozen=True)
class CheckResult:
    status: str
    reasons: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return self.status == "ok"


def fold(word: str) -> str:
    decomposed = unicodedata.normalize("NFKD", word.casefold())
    return "".join(c for c in decomposed if not unicodedata.combining(c))


def vocabulary(text: str) -> tuple[set[str], set[str]]:
    words = {fold(w) for w in _WORD.findall(text)}
    stems = {w[:STEM_LENGTH] for w in words if len(w) >= STEM_LENGTH}
    return words, stems


def _supplied(word: str, words: set[str], stems: set[str]) -> bool:
    folded = fold(word)
    return folded in words or (len(folded) >= STEM_LENGTH and folded[:STEM_LENGTH] in stems)


def check_context_line(line: str, supplied_text: str) -> CheckResult:
    words, stems = vocabulary(supplied_text)
    tokens = _WORD.findall(line)
    reasons = []
    if not tokens:
        return CheckResult("flagged", ("empty",))
    if len(tokens) > CONTEXT_WORD_LIMIT + 20:
        reasons.append(f"too_long:{len(tokens)}_words")
    entities = [t for i, t in enumerate(tokens) if i > 0 and t[0].isupper() and fold(t) not in STRUCTURAL_WORDS]
    entities += [t for t in tokens if t.isdigit()]
    for entity in dict.fromkeys(entities):
        if not _supplied(entity, words, stems):
            reasons.append(f"entity_not_supplied:{entity}")
    content = [t for t in tokens if len(t) >= 6 and not t[0].isupper() and fold(t) not in STRUCTURAL_WORDS]
    novel = [t for t in content if not _supplied(t, words, stems)]
    if content and len(novel) / len(content) > NOVEL_WORD_RATIO_LIMIT:
        reasons.append("novel_vocabulary:" + ",".join(dict.fromkeys(novel))[:80])
    return CheckResult("flagged" if reasons else "ok", tuple(reasons))
