"""Shared helpers for the §5.1 segment renders."""
import re


def voice(text: str) -> str:
    """Strip scholarly apparatus before a field enters voice context -
    §5.1: doc citations / gravity codes never enter generation context."""
    out = re.sub(r"\s*\((?:Doc|LiveTest|SS|Article|app/|representative_)[^)]*\)",
                 "", str(text))
    return re.sub(r"\s{2,}", " ", out).strip()
