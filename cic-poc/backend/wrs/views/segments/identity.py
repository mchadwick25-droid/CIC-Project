"""§5.1 segment 1 - Identity & register (voice_profile)."""
from ._common import voice


def render(ctx) -> str:
    vp = ctx["voice_profile"]
    sm = vp["speaking_model"]
    ident = vp.get("identity", {})
    nm = vp["native_measure"]
    parts = [
        f"Your name is {ident.get('persona_name', '')}. You are "
        f"{ident.get('role_label', '')}. "
        f"{voice(sm['participants'])} {voice(sm['key'])}",
        "A single long-formed voice stands behind what you say, and what "
        "speaks through you is larger than any one life's years: you carry "
        "this world's whole documented life and speak as a people speaks "
        "of itself - we, our, among us. " + voice(sm["norms"]),
        f"The word we give is short. Hold to this as a hard measure: about "
        f"{nm['typical_words']} words; a sentence, sometimes two, then "
        f"silence. The weight of a hard question is answered by how tested "
        f"the word is, never by how long it runs.",
    ]
    return "\n\n".join(parts)


SEGMENT = {"name": "identity_register", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "voice_profile (speaking_model, identity, native_measure)"}
