"""SS5.1 quick-reach segment (S5.3 = R7, shipped behind the parroting
gate per F3): every term's quick_meaning + id for the seated world, in
PLAIN register - deliberately the least parrotable form of each record
(SS5.3 rule 1) - so every term is reachable every turn at cache-read
rates. Per-turn retrieval narrows to deep bodies (the retriever strips
the Quick Meaning section it now duplicates).

Voice Rebuild Phase 0.3 (2026-08-08): the header sentence generalized
from Desert-hardcoded text (confirmed present verbatim in Papnoute's
deployed prompt at line 47, confirmed ABSENT from Chloe's/PAHC's) to
ctx["craft"]'s quick_reach-tagged block. A world without one renders
NOTHING AT ALL, same fix and same reason as grounding_anchor.py: a
bare bulleted term list with no framing sentence is a fragment, not a
faithful rendering of a world whose deployed prompt has no such
listing at all (confirmed for PAHC)."""


def render(ctx) -> str:
    header = next((b["text"] for b in ctx.get("craft", [])
                   if b["segment"] == "quick_reach"), None)
    if not header:
        return ""
    lines = [header]
    for tid, t in sorted(ctx["terms"].items()):
        # Markdown emphasis is typography for a page; this text is spoken.
        # 24 term records across five worlds wrap the headword in asterisks,
        # and two of them already reached Albina's DEPLOYED prompt as literal
        # '*' characters. Stripped in the render path rather than across the
        # records, same fix and same reason as grounding_anchor._cite.
        qm = (t.get("quick_meaning", "") or "").replace("*", "")
        if qm:
            lines.append(f"- {t['term']} [{tid}]: {qm}")
    return "\n".join(lines)


SEGMENT = {"name": "quick_reach", "cache_stability": "static",
           "eviction_priority": 2, "render": render,
           "sources": "this world's craft table (quick_reach-tagged header) + every term record's quick_meaning + id (plain register - the parroting guard's register separation)"}
