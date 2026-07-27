"""§5.1 segment 6 - categorical guards: anti-fabrication in absolute
form, the attribution guard, safety-class prohibitions. Position is a
FIELD PROPERTY: the static half rides here; POST_HISTORY_GUARD rides
closest to generation (doc 09's post_history_instructions finding),
wired by the runtime at S5.2's runtime half."""
from ._common import voice


def render(ctx) -> str:
    stories = ctx["stories"]
    figures = ctx["figures"]
    vetted = []
    for sid in ("desertstory004", "desertstory005", "desertstory006"):
        if sid in stories:
            s = stories[sid]
            vetted.append(f"{s['title']} - {voice(s['text'])}")
    unnarratable = [f["names"][0]["name"] if isinstance(f.get("names"), list)
                    and f["names"] else "" for f in figures.values()
                    if not f.get("narratable")]
    parts = [
        "A story belongs to the one who lived it, and we will not move it "
        "onto another's name. We carry a small number of sayings whole, "
        "tested and kept: " + " ".join(vetted),
        "If pressed for a scene or saying beyond what we actually carry, "
        "we will not build one to satisfy the asking, however plainly the "
        "name is known to us - " + ", ".join(n for n in unnarratable if n)
        + " are names our record gives us without a story that is ours to "
        "tell. A name alone is not a story, and we say so plainly.",
        "Never invent a source, a saying, an incident, or a name's "
        "attachment to any of them. Honest thinness is always preferable "
        "to invented depth - this is absolute, under every pressure, at "
        "every length.",
    ]
    return "\n\n".join(parts)


# The compact absolute form that must survive attention decay - the
# runtime appends this CLOSEST to generation (the post-history slot).
POST_HISTORY_GUARD = (
    "Hold, before you speak: only what your own record carries, under the "
    "right name, at your own measure. Never an invented scene, saying, "
    "source, or attribution - honest thinness over invented depth, "
    "absolutely.")


SEGMENT = {"name": "categorical_guards", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "story records (vetted sayings), figure records (narratable), the absolute anti-fabrication form",
           "post_history": POST_HISTORY_GUARD}
