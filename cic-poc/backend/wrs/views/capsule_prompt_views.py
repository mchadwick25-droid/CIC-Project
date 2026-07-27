"""S2.8 - temporary Permanent Prompt + Capsule Core assemblers (SS5.1 order).

DELIBERATELY TEMPORARY (blueprint S2.8): S5.2 replaces the prompt view
with the real SS5.1 assembly. This generator's job is the completeness
proof (see prompt_coverage.py) plus producing a staged generated prompt
real enough for probe-parity to measure whether the RECORDS carry the
voice. It assembles from record fields only - no prose is authored here
beyond section scaffolding. Known GAP handling, matching the coverage
map: the identity line's persona name/role are passed as documented
literals (no record home - S2.9 CO), and the telos paragraph is OMITTED
(no record home - S2.9 CO); probe parity therefore also measures what
its absence costs, which is evidence for that CO.

The capsule view assembles the same SS5.1 'world's own ground' material
at fuller depth (gravities Primary-first, formation logic, strands,
voice_surface bodies). Hand-authored capsule prose will not round-trip -
the S2.8 capsule parity is a SECTION-level classified comparison,
recorded in the checkpoint artifact.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

import re

from chunk_views import load_records, STAGING  # noqa: E402


def voice(text: str) -> str:
    """Strip scholarly apparatus from a field before it enters voice
    context - SS5.1: doc citations / gravity codes never enter generation
    context. The records carry them (etic layer); the view removes them."""
    out = re.sub(r"\s*\((?:Doc|LiveTest|SS|Article|app/|representative_)[^)]*\)",
                 "", text)
    return re.sub(r"\s{2,}", " ", out).strip()

# GAP literals, documented (see prompt_coverage.py P1) - no record home yet
PERSONA_NAME = "Papnoute"
PERSONA_ROLE = "an abba, an elder among the desert communities of Egypt"


def _terms_by_id():
    return load_records("term")


def build_prompt() -> str:
    terms = _terms_by_id()
    stories = load_records("story")
    claims = load_records("contested_claim")
    figures = load_records("figure")
    core = load_records("world_core")["desertcore001"]
    vp = load_records("voice_profile")["desertvoice001"]
    sm = vp["speaking_model"]

    segs: list[str] = []
    # Identity & register (voice_profile; persona literals are the flagged GAP)
    segs.append(
        f"Your name is {PERSONA_NAME}. You are {PERSONA_ROLE}. "
        f"{voice(sm['participants'])} {voice(sm['key'])}")
    segs.append(
        "A single long-formed voice stands behind what you say, and what "
        "speaks through you is larger than any one life's years: you carry "
        "this world's whole documented life and speak as a people speaks "
        "of itself - we, our, among us. " + voice(sm["norms"]))
    # The world's own ground (world_core + gravities, Primary first)
    tw = core.get("time_window", {})
    fl = voice(core.get("formation_logic", ""))
    fl = fl.replace("Doc_01 SS1 (verbatim): ", "").strip('"')
    segs.append(
        f"Your temporal horizon runs from the years around {tw.get('start_year')} "
        f"until the years around {tw.get('end_year')}, and nothing within that "
        f"span is closed to you; what came after it is not yours. "
        f"The world you inhabit: {fl}")
    gravities = load_records("gravity")
    prim = [g for g in gravities.values() if g.get("classification") == "Primary"]
    ground = []
    for g in prim:
        ground.append(f"{g['name']}: {voice(g['six_tests']['test_3']['verdict'])}")
    segs.append("What organizes this world - " + " | ".join(ground))
    # Contestation (contested_claim renders)
    for cid in sorted(claims):
        c = claims[cid]
        segs.append(
            f"What we hold: {voice(c['claim'])} When pushed: {voice(c['pressure_response'])} "
            f"What we concede: {voice(c['concedes'])}")
    # Grounding anchor (load-bearing genuine sources)
    segs.append(
        "You draw only on this world's own vetted record - the sayings "
        "and lives as this world's own documents carry them, never on "
        "another world's more famous words.")
    # Quick-reach layer (every term's quick_meaning)
    qr = [f"{t['term']}: {t['quick_meaning']}" for t in terms.values()]
    segs.append("The vocabulary through which we understand everything - " +
                " ".join(qr))
    # Voice surfaces (emic register carriers)
    vs = [t["voice_surface"] for t in terms.values() if t.get("voice_surface")]
    segs.append(" ".join(vs[:5]))
    # Native measure
    nm = vp["native_measure"]
    segs.append(
        f"The word we give is short. Hold to this as a hard measure: about "
        f"{nm['typical_words']} words; a sentence, sometimes two, then "
        f"silence. The weight of a hard question is answered by how tested "
        f"the word is, never by how long it runs.")
    # Stories + categorical guards (from records)
    vetted = []
    for sid in ("desertstory004", "desertstory005", "desertstory006"):
        s = stories[sid]
        vetted.append(f"{s['title']} - {s['text']}")
    segs.append(
        "A story belongs to the one who lived it, and we will not move it "
        "onto another's name. We carry a small number of sayings whole, "
        "tested and kept: " + " ".join(vetted))
    unnarratable = [f["names"][0]["name"] if isinstance(f.get("names"), list)
                    and f["names"] else "" for f in figures.values()
                    if not f.get("narratable")]
    segs.append(
        "If pressed for a scene or saying beyond what we actually carry, "
        "we will not build one to satisfy the asking, however plainly the "
        "name is known to us - " +
        ", ".join(n for n in unnarratable if n) +
        " are names our record gives us without a story that is ours to "
        "tell. A name alone is not a story, and we say so plainly.")
    # Cautions - voice-renderable ones only: facilitator-addressed cautions
    # (unperformed-review notices) belong to the Brief view, not the
    # Representative's own prompt (temporary-generator judgment, recorded
    # in the S2.8 artifact)
    for caution in core.get("cautions", []):
        if "Facilitator" in caution or "facilitator" in caution:
            continue
        segs.append(voice(caution))
    return "\n\n".join(segs) + "\n"


def build_capsule() -> str:
    core = load_records("world_core")["desertcore001"]
    gravities = load_records("gravity")
    terms = _terms_by_id()
    parts = ["# World Capsule Core (generated view) - Desert Monasticism",
             "", "## The World You Inhabit", "",
             str(core.get("formation_logic", "")), "",
             "## What Organizes Everything", ""]
    order = {"Primary": 0, "Supporting": 1, "Tensional": 2}
    for g in sorted(gravities.values(),
                    key=lambda g: (order.get(g.get("classification"), 3), g["id"])):
        parts.append(f"- **{g['name']}** ({g['classification']}): "
                     f"{g['six_tests']['test_3']['verdict']}; "
                     f"{g['six_tests']['test_4']['verdict']}")
    parts += ["", "## The World's Own Words", ""]
    for t in terms.values():
        parts.append(f"- {t['term']}: {t.get('voice_surface', '')}")
    parts += ["", "## Cautions", ""]
    for c in core.get("cautions", []):
        parts.append(f"- {c}")
    return "\n".join(parts) + "\n"


def main() -> None:
    STAGING.mkdir(parents=True, exist_ok=True)
    (STAGING / "desert_Representative_Permanent_Prompt_generated.txt").write_text(
        build_prompt(), encoding="utf-8")
    (STAGING / "desert_World_Capsule_Core_generated.md").write_text(
        build_capsule(), encoding="utf-8")
    print(f"staged generated prompt + capsule -> {STAGING}")


if __name__ == "__main__":
    main()
