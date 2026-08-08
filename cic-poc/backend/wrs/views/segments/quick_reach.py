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
only the derived term list."""


def render(ctx) -> str:
    header = next((b["text"] for b in ctx.get("craft", [])
                   if b["segment"] == "quick_reach"), None)
    lines = [header] if header else []
    for tid, t in sorted(ctx["terms"].items()):
        qm = t.get("quick_meaning", "")
        if qm:
            lines.append(f"- {t['term']} [{tid}]: {qm}")
    return "\n".join(lines)


SEGMENT = {"name": "quick_reach", "cache_stability": "static",
           "eviction_priority": 2, "render": render,
           "sources": "this world's craft table (quick_reach-tagged header) + every term record's quick_meaning + id (plain register - the parroting guard's register separation)"}
