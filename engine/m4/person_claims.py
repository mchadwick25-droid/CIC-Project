"""Claims about a named person that the sentence's own records do not make.

Two shapes, each read against the records a sentence is tagged to:

- credited: a named figure of the world is the subject of a speaking,
  writing or teaching verb ("Justin said the apostles preached..."). The
  person must be the speaker of a tagged quote record, the tagged figure
  record itself, or named in the tagged record's own passage that carries
  what the sentence says: its best-matching sentence or the one before it,
  which may introduce the speaker ("One of us, Ignatius, put it with great
  force."). pahc Q2 (14 October) credited 1 Clement 42's
  apostolic chain to Justin, whom the cited witness names only for the
  Sunday reading.
- reason: a "because" clause in a sentence about a person (a named figure,
  or he, she or they) gives a reason the tagged records do not hold: no
  one sentence of them carries most of the clause's content words. ijc Q5
  (14 October) wrote "He signed because he judged the word could bear an
  orthodox meaning"; the witness gives no reason for the signature.

Report-only. Run over every sentence of the 13 and 14 October drafts, the
check did not reach a clean result (some flags are true claims the records
carry in other words), so it cuts nothing: engine.m7.offline_checks logs
its flags for review. Deterministic; no model call.
"""
import re

from engine.m4.grounding_net import (
    QuotationIndex,
    _occurrences,
    _stem,
    _word_sequence,
)
from engine.prose import all_text, sentences as split_sentences

# Verbs that credit words or a teaching to their subject.
CREDIT_VERBS = frozenset({
    "said", "says", "wrote", "writes", "taught", "teaches", "preached", "preaches", "declared", "declares",
    "explained", "explains", "argued", "argues", "insisted", "insists", "confessed", "confesses", "told", "tells",
    "sang", "sings", "answered", "replied", "warned", "urged", "affirmed", "affirms", "maintained", "held", "holds",
    "called", "calls", "named", "described", "describes",
})
SUBJECT_WINDOW = 4
_TOKEN = re.compile(r"[a-z0-9]+")
_PERSON_PRONOUNS = frozenset({"he", "she", "they", "him", "her", "them"})
_BECAUSE = re.compile(r"\bbecause\b", re.IGNORECASE)
_CLAUSE_END = re.compile(r"[,;:.!?—–]|\s-\s|\bnot because\b|\bbecause\b", re.IGNORECASE)
# A reason is held when one record sentence carries this share of the
# because-clause's content words, and at least REASON_MIN of them.
REASON_SHARE = 0.6
REASON_MIN = 2


def _record_sentences(record: dict) -> list[str]:
    return split_sentences(all_text(record))


def _names_figure(text: str, fids: set[str], index: QuotationIndex) -> bool:
    tokens = _TOKEN.findall(text.lower())
    aliases = index._figure_aliases()
    return any(_occurrences(tokens, alias) for fid in fids for alias in aliases.get(fid, ()))


def _credited(sentence: str, index: QuotationIndex) -> list[tuple[set[str], str]]:
    """(figure ids, the name as written) for each credit verb whose subject,
    within SUBJECT_WINDOW words before it, is one of the world's figures."""
    tokens = _TOKEN.findall(sentence.lower())
    names: list[tuple[int, int, set[str]]] = []
    for fid, aliases in index._figure_aliases().items():
        for alias in aliases:
            names += [(start, end, {fid}) for start, end in _occurrences(tokens, alias)]
    found = []
    for i, token in enumerate(tokens):
        if token not in CREDIT_VERBS:
            continue
        before = [n for n in names if 0 <= i - n[1] <= SUBJECT_WINDOW - 1]
        if before:
            nearest = max(before, key=lambda n: (n[1], n[1] - n[0]))
            same = [n for n in before if n[0] == nearest[0] and n[1] == nearest[1]]
            found.append((set().union(*(n[2] for n in same)), " ".join(tokens[nearest[0]:nearest[1]])))
    return found


def _carries(sentence: str, fids: set[str], tags: list[str], records: dict[str, dict], index: QuotationIndex) -> bool:
    words = set(_word_sequence(sentence))
    for tag in tags:
        record = records.get(tag) or {}
        if tag in fids:
            return True
        if record.get("record_type") == "quote" and index.speaker_ids(record) & fids:
            return True
        passages = _record_sentences(record)
        scores = [len(words & set(_word_sequence(p))) for p in passages]
        if not scores or not max(scores):
            continue
        best = max(scores)
        for i, score in enumerate(scores):
            if score == best and _names_figure(" ".join(passages[max(i - 1, 0): i + 1]), fids, index):
                return True
    return False


def _reasons(sentence: str, index: QuotationIndex) -> list[str]:
    """The because-clauses of a sentence whose clause before "because" is
    about a person."""
    found = []
    for match in _BECAUSE.finditer(sentence):
        head = re.split(r"[;:.!?]", sentence[: match.start()])[-1]
        head_tokens = set(_TOKEN.findall(head.lower()))
        if not (head_tokens & _PERSON_PRONOUNS or index._figure_aliases() and _credited_name(head, index)):
            continue
        rest = sentence[match.end():]
        end = _CLAUSE_END.search(rest)
        found.append(rest[: end.start()] if end else rest)
    return found


def _credited_name(text: str, index: QuotationIndex) -> bool:
    tokens = _TOKEN.findall(text.lower())
    return any(_occurrences(tokens, alias) for aliases in index._figure_aliases().values() for alias in aliases)


def _reason_held(clause: str, tags: list[str], records: dict[str, dict], index: QuotationIndex) -> bool:
    names = {_stem(token) for aliases in index._figure_aliases().values() for alias in aliases for token in alias}
    words = set(_word_sequence(clause)) - names
    if len(words) < REASON_MIN:
        return True
    need = max(REASON_MIN, REASON_SHARE * len(words))
    return any(
        len(words & set(_word_sequence(p))) >= need
        for tag in tags for p in _record_sentences(records.get(tag) or {})
    )


def person_claim_flags(text: str, tags: list[str], records: dict[str, dict], index: QuotationIndex) -> list[dict]:
    """The flags for one sentence: {"class": "credited", "person"} or
    {"class": "reason", "clause"}. An untagged sentence has no records to
    read it against and is engine.m4.uncited_claims's to report."""
    if not tags:
        return []
    flags = []
    for fids, name in _credited(text, index):
        if not _carries(text, fids, tags, records, index):
            flags.append({"class": "credited", "person": name})
    for clause in _reasons(text, index):
        if not _reason_held(clause, tags, records, index):
            flags.append({"class": "reason", "clause": clause.strip()})
    return flags


def find_person_claim_flags(sentences: list[dict], *, repository_records: dict[str, dict]) -> list[dict]:
    """Report-only, over a net result's "sentences": each sentence shown to
    the participant (any verdict but a quotation drop, which removes it)
    with a flag, as {"sentence", "tags", "flags"}. A placed quote's own
    sentence is the placed-quote check's (grounding_net) and is skipped."""
    from engine.m4.grounding_net import QUOTATION_DROP_REASONS

    index = QuotationIndex(repository_records)
    out = []
    for entry in sentences:
        if entry.get("placed_quote") or (entry.get("verdict") == "withhold" and entry.get("why") in QUOTATION_DROP_REASONS):
            continue
        flags = person_claim_flags(entry["sentence"], entry.get("tags") or [], repository_records, index)
        if flags:
            out.append({"sentence": entry["sentence"], "tags": entry.get("tags") or [], "flags": flags})
    return out
