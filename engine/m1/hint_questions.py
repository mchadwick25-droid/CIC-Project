"""A retrieve_when line says what a participant asks. A line that names
another record, or describes the conversation instead of the question, adds
no question to the record's cell vocabulary and can pull the record in for
words of the record it names."""
from __future__ import annotations

import re

_RECORD_ID = re.compile(
    r"\b[a-z]{2,12}\.(?:story|quote|term|witness|dw|force|gravity|limit|contested|figure|demo|demonstration|source|core|ambient|voice)\.[a-z0-9][\w.-]*",
    re.IGNORECASE,
)
_DESCRIBES_CONVERSATION = re.compile(r"^\s*(?:the\s+)?(?:conversation|representative)\b", re.IGNORECASE)


def non_question_reason(line: str) -> str | None:
    """Why a retrieve_when line is not a question a participant asks, or None."""
    if _RECORD_ID.search(line):
        return "names a record"
    if _DESCRIBES_CONVERSATION.search(line):
        return "describes the conversation"
    return None


def non_question_hits(records: dict[str, dict]) -> list[tuple[str, str, str]]:
    """(record id, line, reason) for every retrieve_when line that is not a question."""
    hits = []
    for rid, rec in sorted(records.items()):
        for line in (rec.get("retrieval") or {}).get("retrieve_when") or []:
            if isinstance(line, str) and (reason := non_question_reason(line)):
                hits.append((rid, line, reason))
    return hits
