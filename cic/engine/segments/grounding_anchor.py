"""SS5.1 segment 4 - the grounding anchor: a short-sentence-register
wrapper (Desert's own craft prose) around a DERIVED list (CO-016's
mechanism) from source records where attribution_status = genuine.

Voice Rebuild Phase 0.3 (2026-08-08): generalized from a Desert-only
module (which hardcoded its wrapper sentences directly - confirmed
present verbatim in Papnoute's deployed prompt at line 45, and
confirmed ABSENT from Chloe's/PAHC's deployed prompt entirely, so
reusing it unconditionally for every world would have injected
Desert-authored prose into worlds that don't have this content today)
to read ctx["craft"]'s grounding_anchor-tagged blocks for the wrapper
text. A world whose craft table has no such block renders NOTHING AT
ALL for this segment - confirmed by testing against PAHC's real source
records, not assumed: rendering the derived list without its wrapper
produced an orphaned fragment ("The genuinely attributed core of that
record is small and known to us: ...") with no framing sentence, which
is worse than omitting the segment. A wrapper is required for any
content to render."""
from ._common import voice  # noqa: F401  (kept: shared strip helper for future per-world use)

# Voice Rebuild Phase 2, found during Marius's pass (2026-08-08).
#
# This list is spoken to the Representative as "the genuinely attributed
# core of THIS WORLD'S OWN vetted record". The filter read
# attribution_status alone, which answers a different question - whether
# an attribution is genuine rather than pseudonymous - and says nothing
# about whether a document belongs to the world at all. Two classes of
# record therefore qualified as a world's own:
#
#   source_type 'S' - modern secondary scholarship (149 records fleet-
#   wide). This was not hypothetical: Papnoute's DEPLOYED prompt named
#   "David Brakke - Athanasius and the Politics of Asceticism (Oxford:
#   Clarendon Press, 1995; reissued as ...)" and Rubenson's 1995 monograph
#   inside his own record - publishers, years and reissue histories handed
#   to a 4th-century monk as things his world wrote. Only Desert rendered
#   any today; every other world was spared by sort order alone, not by
#   the filter, since the list truncates at the first 8 by id.
#
#   build-authored artifacts - records whose author IS this build
#   (srcDES025, the build's own English rendering of 'fuge, tace,
#   quiesce', licensed paraphrase-only to a single anchor; srcALX033).
#   These carry source_type 'M' and no field distinguished them, so they
#   are now marked in_world_record: false at the record and honoured here.
#   Excluding 'S' without this would have PROMOTED srcDES025 into
#   Desert's rendered list - a worse leak than the one being fixed.
#
# P (primary) and M (material/documentary - papyri, archaeology, coinage)
# both genuinely belong to a world's record and both stay.
_NOT_OUR_RECORD = {"S"}


def _renderable(s: dict) -> bool:
    return (s.get("attribution_status") == "genuine"
            and s.get("source_type") not in _NOT_OUR_RECORD
            and s.get("in_world_record") is not False)


def _cite(s: dict) -> str:
    """Author and title as one spoken phrase.

    Two render defects fixed here rather than by editing 254 records:
    34 genuine records repeat the author inside work_title ("Eusebius of
    Caesarea" + "Eusebius of Caesarea, Ecclesiastical History" rendered as
    "Eusebius of Caesarea - Eusebius of Caesarea, ..."), which was ALL
    EIGHT of Marius's entries; and 26 carry markdown asterisks, which are
    typography for a page, not for a prompt that is spoken."""
    author = (s.get("work_author") or "").strip()
    title = (s.get("work_title") or s.get("title") or "").strip()
    if author and title.startswith(author):
        # Only a genuine repetition, never a possessive. "Jerome" +
        # "Jerome's biblical commentaries" is one phrase, not the name
        # twice; stripping it there yields "Jerome - 's biblical
        # commentaries". Require a separator after the name.
        rest = title[len(author):]
        if rest[:1] in {",", ";", ":"} or rest[:3] in {" - ", " – "}:
            title = rest.lstrip(" ,;:-–").strip()
    joined = f"{author}{' - ' if author and title else ''}{title}"
    return joined.replace("*", "")


def render(ctx) -> str:
    blocks = {b.get("role"): b["text"] for b in ctx.get("craft", [])
             if b["segment"] == "grounding_anchor"}
    if "open" not in blocks:
        return ""

    genuine = []
    for sid in sorted(ctx["sources"]):
        s = ctx["sources"][sid]
        if not _renderable(s):
            continue
        cite = _cite(s)
        if cite:
            genuine.append(cite)

    parts = [blocks["open"]]
    if genuine:
        parts.append("The genuinely attributed core of that record is small "
                     "and known to us: " + "; ".join(genuine[:8]) + ".")
    if "close" in blocks:
        parts.append(blocks["close"])
    return " ".join(parts)


SEGMENT = {"name": "grounding_anchor", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "this world's craft table (grounding_anchor-tagged wrapper text) + source records (attribution_status = genuine), derived list"}
