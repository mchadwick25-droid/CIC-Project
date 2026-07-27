"""SS5.1 quick-reach segment (S5.3 = R7, shipped behind the parroting
gate per F3): every term's quick_meaning + id for the seated world, in
PLAIN register - deliberately the least parrotable form of each record
(SS5.3 rule 1) - so every term is reachable every turn at cache-read
rates. Per-turn retrieval narrows to deep bodies (the retriever strips
the Quick Meaning section it now duplicates)."""


def render(ctx) -> str:
    lines = ["Every word of this world's vocabulary, within reach at all "
             "times - each in plain terms (the full sense arrives when a "
             "word is genuinely in play):"]
    for tid, t in sorted(ctx["terms"].items()):
        qm = t.get("quick_meaning", "")
        if qm:
            lines.append(f"- {t['term']} [{tid}]: {qm}")
    return "\n".join(lines)


SEGMENT = {"name": "quick_reach", "cache_stability": "static",
           "eviction_priority": 2, "render": render,
           "sources": "every term record's quick_meaning + id (plain register - the parroting guard's register separation)"}
