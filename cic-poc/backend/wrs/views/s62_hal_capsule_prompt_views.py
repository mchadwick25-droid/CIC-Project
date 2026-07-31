"""S6.2/HAL S2.8-equivalent - temporary HAL Permanent Prompt + Capsule
assemblers (the SYR s62_syr_capsule_prompt_views.py port).

DELIBERATELY TEMPORARY (the real SS5.1 segment assembly is S5.2-class):
proves the records can produce a voice-bearing prompt and stages a
generated prompt real enough for probe parity. Assembles from record
FIELDS only; demonstration records deliberately NOT read (their
dialogues are the Phase-5 exchanges - the probe hold-out).

Like SYR, NO omitted-GAP handling needed: the telos and
living-traditions closes HAVE record homes (S2.7a applied the
CO-P2-05/17 standing conventions); prompt coverage runs at zero GAPs.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from s62_hal_chunk_views import load_records, STAGING  # noqa: E402

APPARATUS = re.compile(
    r"\s*\((?:[^)]*(?:Doc_|SS\d|Phase\s?\d|CO-0|CO-P2|Article\s?\d|"
    r"hallex|haldemo|halstory|halgrav|halforce|halclaim|halfig|srcHAL|"
    r"RCF|nodes\.py|Round[- ]?\d|scorer|the S2\.\d|FLAG-\d|"
    r"Construction Notes|World Profile|project lead|the chunk|chunk |"
    r"deployed prompt|live-test|the identity decision)[^)]*)\)")


def voice(text: str) -> str:
    out = APPARATUS.sub("", text or "")
    out = re.sub(r"\s{2,}", " ", out)
    return out.strip()


VOICE_FORBIDDEN = re.compile(
    r"Dominant Modern Reconstruction|the record store|Inferential[/-]Thin|"
    r"Reported-Experience Status|Widely Accepted|external review|"
    r"cross-check|deferred to|scholarship|scholarly|Doc_0|hallex|"
    r"halclaim|halstory|haldemo|force_llm_vote|Tier[- ]\d|"
    r"single-source|post-mortem|Contested|Documented\b|the migration|"
    r"S2\.\d|the record's|Author.Gravity|the scorer|Round \d", re.I)


def voice_strict(text: str) -> str:
    kept = [s for s in re.split(r"(?<=[.!?])\s+", voice(text))
            if s and not VOICE_FORBIDDEN.search(s)]
    return " ".join(kept)


def build_prompt() -> str:
    terms = {rid: rec for rid, (rec, _b, _p) in load_records("term").items()}
    claims = {rid: rec for rid, (rec, _b, _p)
              in load_records("contested_claim").items()}
    core = load_records("world_core")["halcore001"][0]
    vp = load_records("voice_profile")["halvoice001"][0]
    sm = vp["speaking_model"]
    ident = vp.get("identity", {})

    role = ident.get("role_label", "").split(" - ")[0]
    segs = []
    segs.append(
        f"Your name is {ident.get('persona_name', '')}. You are a {role}. "
        + voice_strict(sm["participants"]))
    tw = core.get("time_window", {})
    segs.append(
        f"Your span runs from the year {tw.get('start_year')}, when a "
        f"scholar first came among us in Rome, to the year "
        f"{tw.get('end_year')}, when the deaths that closed our "
        f"household's own generation at Bethlehem ended it; nothing "
        f"beyond that edge exists for you. " + voice_strict(sm["setting"]))
    for cid in ("halclaim001", "halclaim002", "halclaim003"):
        segs.append(voice_strict(claims[cid]["claim"]))
    vocab = []
    for tid in ("hallex03", "hallex01", "hallex06", "hallex07", "hallex11"):
        t = terms[tid]
        name = re.sub(r"\s*\([^)]*\)", "", t["term"]).strip()
        vocab.append(f"{name}: {voice_strict(t['quick_meaning'])}")
    segs.append("The words we think in - " + " | ".join(vocab))
    segs.append(voice_strict(sm["act_sequence"]) + " "
                + voice_strict(sm["genre"]))
    segs.append(voice_strict(sm["key"]) + " "
                + voice_strict(sm["instrumentalities"]))
    segs.append(voice_strict(sm["ends"]))
    segs.append(voice_strict(sm["norms"]))
    segs.append("We hold a tension we cannot resolve. "
                + voice_strict(claims["halclaim001"]["concedes"]))
    segs.append("Of the quarrels that cost us most: "
                + voice_strict(claims["halclaim004"]["claim"]))
    segs.append("Of the widow the clergy consulted: "
                + voice_strict(claims["halclaim005"]["claim"]) + " "
                + voice_strict(claims["halclaim005"]["concedes"]))
    telos = (core.get("telos") or {}).get("text", "")
    if telos:
        segs.append(voice_strict(telos))
    lt = (core.get("living_traditions") or {}).get("text", "")
    if lt:
        segs.append("Our household does not give rise directly to a "
                    "tradition with present-day institutional adherents "
                    "who would claim it as their own. You speak from "
                    "your formation; what you say is not any living "
                    "community's present-day identity.")
    return "\n\n".join(s for s in segs if s.strip()) + "\n"


def build_capsule() -> str:
    terms = {rid: rec for rid, (rec, _b, _p) in load_records("term").items()}
    gravities = {rid: rec for rid, (rec, _b, _p)
                 in load_records("gravity").items()}
    stories = {rid: rec for rid, (rec, _b, _p)
               in load_records("story").items()}
    core = load_records("world_core")["halcore001"][0]

    parts = ["# World Capsule Core - Hieronymian (generated view)"]
    parts.append("## The World You Inhabit\n\n"
                 + voice(re.sub(r"^Doc_01 [^:]*: ", "",
                                core.get("formation_logic", ""))))
    order = {"Primary": 0, "Supporting": 1, "Tensional": 2}
    ranked = sorted((g for g in gravities.values()
                     if g.get("classification") in order),
                    key=lambda g: (order[g["classification"]], g["id"]))
    lines = []
    for g in ranked:
        verdict = voice(g["six_tests"]["formation"]["verdict"])
        # leak-scan catch (the SYR two-leaks precedent): G1's formation
        # verdict carries an unparenthesized apparatus clause - strip
        # the review-routing phrase, keep the substance
        verdict = re.sub(r",?\s*flagged for Doc_0\d [a-z]+\b", "", verdict)
        verdict = re.sub(r"^PASS[^-]*-\s*", "", verdict)
        lines.append(f"- **{voice(g['name'])}** ({g['classification']}): "
                     f"{verdict}")
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
    p = STAGING / "hal_Representative_Permanent_Prompt_generated.txt"
    c = STAGING / "hal_World_Capsule_Core_generated.md"
    p.write_text(build_prompt(), encoding="utf-8", newline="\n")
    c.write_text(build_capsule(), encoding="utf-8", newline="\n")
    print(f"staged: {p.name} "
          f"({len(p.read_text(encoding='utf-8').split())} words), {c.name}")


if __name__ == "__main__":
    main()
