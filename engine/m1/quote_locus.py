"""The locus check: a quote's `text` must occur at the lines of the vendored
file that the quote's own locus cites.

`gate_quote_verbatim` asks whether the text occurs anywhere in the file its
edition names. This gate asks the stricter question for a quote that names
a span (`cic/texts/<file>, lines N-M`, read by `engine.prose.locus_refs`): the
text must occur inside one of those cited spans, so the span a card links to
is the span that holds the words. The match is the same fixed grammar
`quote_verbatim.verify_quote_text` applies, run on the span alone, after the
same edition apparatus stripping `verify_quote_record` applies to the whole
file (an apparatus kind that needs the whole file, such as an endnote
sequence, finds nothing to strip in a span, so the span is matched as it is).
The gate's scope is the verbatim gate's: a quote below `verified-direct` has
been escalated because its words cannot be matched to the file mechanically,
so its span is not matched either. A quote
cited at two spans (an English edition and a Latin one) passes when its text
is in any one of them.

Every verbatim quote names its exact lines: a verbatim quote
whose locus names no machine-readable span fails, whatever its verification
state, since an escalated quote's card still links to the lines it came from.
`unchecked_quotes` lists them.
"""
from functools import lru_cache
from pathlib import Path

from engine.prose import locus_refs

from .quote_verbatim import (
    _REQUIRED_VERIFICATION_STATE,
    REPO_ROOT,
    strip_edition_apparatus,
    verify_quote_against_notes,
    verify_quote_text,
)


@lru_cache(maxsize=64)
def _file_lines(file: str) -> tuple[str, ...] | None:
    path = REPO_ROOT / file
    return tuple(path.read_text(encoding="utf-8", errors="replace").splitlines()) if path.is_file() else None


def cited_spans(quote_record: dict) -> list[dict]:
    return [ref for source in quote_record.get("sources") or [] for ref in locus_refs(source.get("locus") or "")]


def unchecked_quotes(records: dict) -> list[str]:
    """Verbatim quotes whose locus names no vendored span: nothing here can be checked for them."""
    return sorted(
        rid for rid, rec in records.items()
        if rec.get("record_type") == "quote" and rec.get("license") == "verbatim" and not cited_spans(rec)
    )


def gate_quote_locus(records, fleet, registry) -> list[str]:
    findings = []
    for rid, rec in sorted(records.items()):
        if rec.get("record_type") != "quote" or rec.get("license") != "verbatim":
            continue
        refs = cited_spans(rec)
        if not refs:
            findings.append(f"{rid}: verbatim quote names no line span; its locus must cite `cic/texts/<file>, lines N-M`")
            continue
        if (rec.get("confidence") or {}).get("verification_state") != _REQUIRED_VERIFICATION_STATE:
            continue
        text = rec.get("text") or ""
        if not text.strip():
            continue
        failed, unresolved = None, []
        verified = False
        for ref in refs:
            lines = _file_lines(ref["file"])
            first, last = (int(n) for n in ref["lines"].split("-"))
            if lines is None or first < 1 or last < first or last > len(lines):
                unresolved.append(f"{ref['file']}, lines {ref['lines']}")
                continue
            raw = strip_edition_apparatus("\n".join(lines[first - 1:last]), Path(ref["file"]).name)
            is_xml = Path(ref["file"]).suffix == ".xml"
            result = verify_quote_text(text, raw, source_is_xml=is_xml)
            if result.verified or verify_quote_against_notes(text, raw) is not None:
                verified = True
                break
            failed = failed or (ref, result)
        if verified:
            continue
        if failed:
            ref, result = failed
            findings.append(
                f"{rid}: text does not occur at its cited locus {ref['file']}, lines {ref['lines']} - "
                f"failed segment {result.failed_segment!r}; nearest span text: {result.nearest_context!r}"
                + (f"; spans that did not resolve: {', '.join(unresolved)}" if unresolved else "")
            )
        else:
            findings.append(f"{rid}: every cited span fails to resolve to lines of a vendored text: {', '.join(unresolved)}")
    return findings
