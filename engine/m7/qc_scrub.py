"""Deterministic scrubbing for the quality-control store: what a participant
types may name themselves or someone else, and the QC store keeps no way
back to a person. Emails, phone numbers and web addresses become fixed
placeholders, and a capitalised word becomes [name] unless it is ordinary
English, a name the world's own records or the fleet registry use, or (at
the start of a sentence) a common opening word. A rare opening word is
sometimes scrubbed too; privacy wins that trade. Same input, same output,
always.
"""
import re

EMAIL = re.compile(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b")
URL = re.compile(r"\b(?:https?://|www\.)\S+", re.IGNORECASE)
PHONE = re.compile(r"(?<!\w)\+?\d[\d\s().-]{6,}\d(?!\w)")
_WORD = re.compile(r"[A-Z][a-zA-Z'’-]+")
_SENTENCE_START = re.compile(r"(?:^|[.!?]\s+|\n\s*)$")

# Capitalised words that are ordinary English, not names.
COMMON = frozenset("""
I I'm I've I'd I'll Im Ive Id Ill OK Okay Yes No Hello Hi Thanks Thank Please Sorry Mr Mrs Ms Dr
Monday Tuesday Wednesday Thursday Friday Saturday Sunday January February March April May June July
August September October November December English Latin Greek Hebrew Christian Christians Christianity
Church God Lord Jesus Christ Bible Scripture Scriptures Gospel Gospels Holy Spirit Father Son Trinity
Catholic Protestant Orthodox Pope Easter Christmas Lent Sabbath Old New Testament
""".split())

# Ordinary words that open a sentence; any other capitalised word at the
# start of a sentence is treated like a name unless it is known.
OPENERS = frozenset("""
A About Actually After Again All Also Although An And Any Are As At Because Before Being Both But By Can
Could Did Do Does Even Every Explain Describe Few For From Give Had Has Have He Her Here His How However
If Imagine In Is It Its Just Let Like Many May Maybe Might More Most Much Must My Never No Not Now Of On
Call Compare Email Help Look Read Say See Show Speak Talk Teach Write
Once One Only Or Other Our Perhaps Please Really She Should Since So Some Still Suppose Tell Than That The
Their Then There These They This Those Though Through To Today Two Very Was We Were What When Where Whether
Which While Who Whom Whose Why Will With Would Yes Yet You Your
""".split())


def known_names(texts) -> frozenset[str]:
    """Every capitalised word in the given texts (a world's records, the
    registry's names): names the conversation may legitimately use."""
    found = set()
    for text in texts:
        found.update(_WORD.findall(text or ""))
    return frozenset(found)


def scrub(text: str, known: frozenset[str] = frozenset()) -> str:
    text = EMAIL.sub("[email]", text)
    text = URL.sub("[link]", text)
    text = PHONE.sub("[phone]", text)
    out, last = [], 0
    for m in _WORD.finditer(text):
        word = m.group(0)
        out.append(text[last:m.start()])
        at_start = _SENTENCE_START.search(text[:m.start()]) is not None
        bare = word[:-2] if word.endswith(("'s", "’s")) else word
        keep = word in COMMON or bare in COMMON or word in known or bare in known or (at_start and word in OPENERS)
        out.append(word if keep else "[name]")
        last = m.end()
    out.append(text[last:])
    return "".join(out)
