""""Anachronism is computed per world from its time window; the dictionary
is fleet data, owned once" (spec M5). No world identifier in code (law 4) -
this takes the world's time_window and the fleet's modern_term records as
plain data and computes membership; it has no idea which world it's
running for.
"""
import re


def anachronistic_term_ids(modern_terms: dict[str, dict], world_time_window: dict) -> set[str]:
    """A modern term is anachronistic for a world if the term's own
    origin_year postdates the world's window (the term did not yet exist
    when this world's Representative would be speaking)."""
    end = world_time_window["end"]
    return {
        term["id"]
        for term in modern_terms.values()
        if term.get("record_type") == "modern_term" and term.get("origin_year") is not None and term["origin_year"] > end
    }


def _tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", (text or "").lower())


def _display_matches(display_tokens: list[str], term_tokens: list[str]) -> bool:
    """The record's own display term, appearing whole inside what the
    participant said. Contiguous run, not a set overlap: "the Trinity"
    contains ["trinity"], and "trinity" never matches "trinitarian" by
    prefix - a record that wants that spelling lists it in display_terms
    itself, which _fleet.modern.trinity already does."""
    if not term_tokens or len(term_tokens) > len(display_tokens):
        return False
    return any(
        display_tokens[i : i + len(term_tokens)] == term_tokens
        for i in range(len(display_tokens) - len(term_tokens) + 1)
    )


def resolve_term_ids(reader_modern_terms: list[dict], modern_terms: dict[str, dict]) -> list[dict]:
    """Give the reader's flagged terms the fleet's own record ids.

    The reader is instructed to return "term_id: a short snake_case id you
    invent for it" - so live it returns things like "trinity_doctrine" or
    "the_trinity", while engine.m5.routing intersects those against a set
    of fleet record ids (_fleet.modern.trinity). Measured live on
    2026-08-24: the intersection was empty every time, and bridge_turn -
    fully built and passing its own tests - could not be reached by any
    real session. This closes that seam in code rather than by asking the
    model to guess an id out of a catalogue it cannot see.

    The match is on the record's authored display_terms against the
    reader's own `display` field ("the term as the participant used it"),
    which is the pairing those two fields were named for. The invented
    term_id is deliberately NOT matched on: it is model-composed, and
    routing a bridge on it would be routing on invention again. A term
    with no match keeps whatever the reader gave it and simply never
    intersects - the same outcome as before, for the same reason.
    """
    by_display = [
        (_tokens(display_term), record["id"])
        for record in modern_terms.values()
        if record.get("record_type") == "modern_term"
        for display_term in record.get("display_terms") or []
    ]
    resolved = []
    for term in reader_modern_terms or []:
        display_tokens = _tokens(term.get("display"))
        match = next(
            (rid for term_tokens, rid in by_display if _display_matches(display_tokens, term_tokens)),
            None,
        )
        if match is None:
            resolved.append(dict(term))
            continue
        # The reader's own id is kept, not overwritten in silence - the
        # gate_decision event and any M7 audit can still see what the
        # model actually said before code renamed it.
        resolved.append({**term, "term_id": match, "reader_term_id": term.get("term_id")})
    return resolved


def terms_in_message(message: str, modern_terms: dict[str, dict], *, already_found=()) -> list[dict]:
    """Find the fleet's own modern terms in what the participant actually
    wrote, with no model in the loop.

    resolve_term_ids above fixes the id the reader returns; it cannot fix
    the reader not returning one. Measured on 2026-08-24, same world, same
    day, same question in identical words: the reader flagged "Trinity" on
    two attempts and returned modern_terms: [] on a third. The bridge is
    not a judgement call - the word is either in the message or it is not,
    and the fleet record's display_terms are the authored list of what
    counts. So this reads the message directly, and the reader's own
    flagging becomes a supplement rather than the sole gate.

    Known limit, stated rather than hidden: matching is on whole tokens, so
    "Trinitarianism" does not match the authored term "Trinitarian". A
    record that wants an inflection matched lists it in display_terms
    itself - the same rule resolve_term_ids follows, and the same reason:
    what counts as the word is the record's decision, not this function's.

    already_found excludes ids the reader's own flags already resolved to,
    so a term both paths see is carried once.
    """
    message_tokens = _tokens(message)
    found = []
    seen = set(already_found)
    for record in modern_terms.values():
        if record.get("record_type") != "modern_term" or record["id"] in seen:
            continue
        for display_term in record.get("display_terms") or []:
            if _display_matches(message_tokens, _tokens(display_term)):
                seen.add(record["id"])
                # `display` is the authored term that matched, not the
                # participant's own casing - nothing downstream reads it
                # (facilitator_turns.bridge_turn renders the record's own
                # display_terms), and inventing a surface form here would
                # be this function composing text, which it must not do.
                found.append({"term_id": record["id"], "display": display_term, "source": "message_scan"})
                break
    return found

def mentions_term(text: str, display_terms) -> bool:
    """Does this text carry one of these authored terms, by the same
    whole-token rule terms_in_message uses? One rule, one place: a word the
    scan counts as the term and a word the bridge bars from the voice must
    never be two different questions."""
    text_tokens = _tokens(text)
    return any(_display_matches(text_tokens, _tokens(term)) for term in display_terms or [])
