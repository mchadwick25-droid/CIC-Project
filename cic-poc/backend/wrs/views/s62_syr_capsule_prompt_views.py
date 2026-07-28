"""S6.2/SYR S2.8-equivalent - temporary Syriac Permanent Prompt + Capsule
assemblers (the ALX s62_alx_capsule_prompt_views.py port).

DELIBERATELY TEMPORARY (the real SS5.1 segment assembly is S5.2-class):
proves the records can produce a voice-bearing prompt and stages a
generated prompt real enough for probe parity. Assembles from record
FIELDS only; demonstration records deliberately NOT read (their
dialogues are the Phase-5 exchanges - the probe hold-out).

Syriac difference from ALX: NO omitted-GAP handling needed - the telos
and living-traditions closes HAVE record homes (S2.7a applied the
CO-P2-05/17 standing conventions), so the generated prompt includes
both; prompt coverage runs at zero GAPs.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from s62_syr_chunk_views import load_records, STAGING  # noqa: E402

APPARATUS = re.compile(
    r"\s*\((?:[^)]*(?:Doc_|SS\d|Phase\s?\d|CO-0|CO-P2|Article\s?\d|"
    r"syrlex|syrdemo|syrstory|syrgrav|syrforce|syrclaim|srcSYR|RCF|"
    r"nodes\.py|Retest|retest|scorer|the S2\.\d|FLAG-\d|"
    r"Construction Notes|project-lead|the chunk|chunk |deployed prompt|guide parable|deletion test)[^)]*)\)")


def voice(text: str) -> str:
    out = APPARATUS.sub("", text or "")
    out = re.sub(r"\s{2,}", " ", out)
    return out.strip()


VOICE_FORBIDDEN = re.compile(
    r"Dominant Modern Reconstruction|the record store|Inferential-Thin|"
    r"Reported-Experience Status|Widely Accepted|external review|"
    r"cross-check|deferred to|scholarship|Doc_0|syrlex|syrclaim|"
    r"force_llm_vote|Standing Distortion-Risk|Contested rather than Documented", re.I)


def voice_strict(text: str) -> str:
    kept = [s for s in re.split(r"(?<=[.!?])\s+", voice(text))
            if s and not VOICE_FORBIDDEN.search(s)]
    return " ".join(kept)


def build_prompt() -> str:
    terms = {rid: rec for rid, (rec, _b, _p) in load_records("term").items()}
    claims = {rid: rec for rid, (rec, _b, _p) in load_records("contested_claim").items()}
    core = load_records("world_core")["syrcore001"][0]
    vp = load_records("voice_profile")["syrvoice001"][0]
    sm = vp["speaking_model"]
    ident = vp.get("identity", {})

    role = ident.get("role_label", "").split(" - the deployed")[0]
    segs = []
    segs.append(
        f"Your name is {ident.get('persona_name', '')}. You are a {role}. "
        + voice_strict(sm["participants"]))
    tw = core.get("time_window", {})
    segs.append(
        f"Your span runs from the years around {tw.get('start_year')} to "
        f"the synod of {tw.get('end_year')} that has, in your hearing, "
        f"just now set the Persian church in order; nothing beyond its "
        f"edge exists for you. " + voice_strict(sm["setting"]))
    fl = core.get("formation_logic", "")
    qm = re.search(r'"([^"]+)"', fl)
    fl_voice = qm.group(1) if qm else re.sub(r"^Doc_01 [^:]*: ", "", fl)
    segs.append("The world you speak from: " + voice_strict(fl_voice))
    for cid in ("syrclaim001", "syrclaim002"):
        segs.append(voice_strict(claims[cid]["claim"]))
    segs.append("The Gospel among us: "
                + voice_strict(terms["syrlex006"]["quick_meaning"]))
    segs.append("And the name the vow points toward: "
                + voice_strict(terms["syrlex007"]["quick_meaning"]))
    segs.append("We carry tensions we do not close. "
                + voice_strict(claims["syrclaim004"]["concedes"]) + " "
                + voice_strict(claims["syrclaim001"]["concedes"]))
    vocab = []
    for tid in ("syrlex001", "syrlex002", "syrlex003"):
        t = terms[tid]
        vocab.append(f"{t['term']}: {voice_strict(t['quick_meaning'])}")
    segs.append("The words we think in - " + " | ".join(vocab))
    segs.append(voice_strict(sm["act_sequence"]) + " " + voice_strict(sm["genre"]))
    segs.append(voice_strict(sm["key"]) + " " + voice_strict(sm["instrumentalities"]))
    segs.append(voice_strict(sm["ends"]))
    segs.append(voice_strict(sm["norms"]))
    segs.append("What we hold about our own record's fault: "
                + voice_strict(claims["syrclaim005"]["claim"]) + " "
                + voice_strict(claims["syrclaim005"]["concedes"]))
    telos = (core.get("telos") or {}).get("text", "")
    if telos:
        segs.append(voice_strict(telos))
    lt = (core.get("living_traditions") or {}).get("text", "")
    if lt:
        segs.append("Of what came after: what has grown from this life "
                    "continues on in places and under names you have "
                    "never heard; their account of themselves is not "
                    "yours to give.")
    return "\n\n".join(s for s in segs if s.strip()) + "\n"


def build_capsule() -> str:
    terms = {rid: rec for rid, (rec, _b, _p) in load_records("term").items()}
    gravities = {rid: rec for rid, (rec, _b, _p) in load_records("gravity").items()}
    stories = {rid: rec for rid, (rec, _b, _p) in load_records("story").items()}
    core = load_records("world_core")["syrcore001"][0]

    parts = ["# World Capsule Core - Syriac (generated view)"]
    parts.append("## The World You Inhabit\n\n"
                 + voice(re.sub(r"^Doc_01 [^:]*: ", "",
                                core.get("formation_logic", ""))))
    order = {"Primary": 0, "Supporting": 1, "Tensional": 2}
    ranked = sorted((g for g in gravities.values()
                     if g.get("classification") in order),
                    key=lambda g: (order[g["classification"]], g["id"]))
    lines = []
    for g in ranked:
        lines.append(f"- **{voice(g['name'])}** ({g['classification']}): "
                     f"{voice(g['six_tests']['formation']['verdict'])}")
    parts.append("## What Organizes Everything\n\n" + "\n".join(lines))
    vs_lines = []
    for tid in sorted(terms):
        t = terms[tid]
        if (t.get("retrieval") or {}).get("tier") in (1, 2):
            vs_lines.append(f"**{t['term']}** - {voice(t['quick_meaning'])}")
    parts.append("## The World's Own Words\n\n" + "\n\n".join(vs_lines))
    st_lines = []
    for sid in sorted(stories):
        s = stories[sid]
        vsurf = s.get("voice_surface", "").split(" Usage guidance")[0]
        st_lines.append(f"- {voice(s.get('title', ''))}: {voice(vsurf)}")
    parts.append("## What We Tell\n\n" + "\n".join(st_lines))
    return "\n\n".join(parts) + "\n"


def main():
    STAGING.mkdir(parents=True, exist_ok=True)
    p = STAGING / "syr_Representative_Permanent_Prompt_generated.txt"
    c = STAGING / "syr_World_Capsule_Core_generated.md"
    p.write_text(build_prompt(), encoding="utf-8", newline="\n")
    c.write_text(build_capsule(), encoding="utf-8", newline="\n")
    print(f"staged: {p.name} ({len(p.read_text(encoding='utf-8').split())} words), "
          f"{c.name}")


if __name__ == "__main__":
    main()
