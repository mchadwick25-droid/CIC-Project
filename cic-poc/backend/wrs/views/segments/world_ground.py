"""§5.1 segment 2 - the world's own ground (world_core + gravities,
rendered emic from period_sense/voice_surface-register fields only).
Budget note: 3,000-5,000 tokens named "as today" - the record render
lands leaner because the removed scholarly apparatus was part of
"today"; measured in the manifest, declared in the artifact.

Register rule (the S5.2 G gate's first real catch): line-per-item
rendering for gravity and term listings - gluing them into one long
sentence drove the assembled prose to FK 13.3 / FRE 45.1 against the
deployed context's 9.0 / 68.7; formation verdicts only (explanatory
verdicts are etic register)."""
from ._common import voice

# §5.5: the prompt names the ORGANIZING vocabulary in running prose; the
# rest render as the world's-own-words listing (today's capsule depth,
# folded in - B-PARROT measured ~0 overlap on this configuration).
ORGANIZING_TERMS = ["desertlex001", "desertlex004", "desertlex005",
                    "desertlex006", "desertlex016"]


def render(ctx) -> str:
    core = ctx["world_core"]
    tw = core.get("time_window", {})
    fl = voice(core.get("formation_logic", "")).replace(
        'Doc_01 SS1 (verbatim): ', '').strip('"')
    parts = [
        f"Your temporal horizon runs from the years around {tw.get('start_year')} "
        f"until the years around {tw.get('end_year')}, and nothing within that "
        f"span is closed to you; what came after it is not yours. "
        f"The world you inhabit: {fl}",
        f"Where this world lives: {voice(core.get('horizon', ''))}",
    ]
    order = {"Primary": 0, "Supporting": 1, "Tensional": 2}
    gravities = sorted(ctx["gravities"].values(),
                       key=lambda g: (order.get(g.get("classification"), 3),
                                      g["id"]))
    prim = [g for g in gravities if g.get("classification") == "Primary"]
    parts.append("What organizes this world:\n" + "\n".join(
        f"- {g['name']}: {voice(g['six_tests']['formation']['verdict'])}"
        for g in prim))
    rest = [g for g in gravities if g.get("classification") != "Primary"]
    if rest:
        parts.append("Also at work, and in tension where it is in tension:\n"
                     + "\n".join(
            f"- {g['name']} ({g['classification']}): "
            f"{voice(g['six_tests']['formation']['verdict'])}" for g in rest))
    vs = [ctx["terms"][tid]["voice_surface"] for tid in ORGANIZING_TERMS
          if tid in ctx["terms"] and ctx["terms"][tid].get("voice_surface")]
    parts.append(" ".join(voice(v) for v in vs))
    words = [f"- {t['term']}: {voice(t['voice_surface'])}"
             for tid, t in sorted(ctx["terms"].items())
             if tid not in ORGANIZING_TERMS and t.get("voice_surface")]
    parts.append("The world's own words, as we speak them:\n"
                 + "\n".join(words))
    telos = core.get("telos", {})
    if telos.get("text"):
        parts.append(voice(telos["text"]))
    for caution in core.get("cautions", []):
        if "acilitator" in caution:
            continue
        parts.append(voice(caution))
    return "\n\n".join(parts)


SEGMENT = {"name": "world_ground", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "world_core (time_window, horizon, formation_logic, telos, cautions); gravity records Primary-first (formation verdicts only); all terms' voice_surface (organizing five in prose, rest listed)"}
