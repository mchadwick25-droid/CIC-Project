"""S6.2 S2.8-equivalent - temporary Alexandria Permanent Prompt + Capsule
assemblers (Desert capsule_prompt_views.py precedent).

DELIBERATELY TEMPORARY: the real SS5.1 segment assembly is an S5.2-class
later step (the Desert assembly is world-hardcoded). This generator's job
is (1) the completeness evidence (s62_alx_prompt_coverage.py maps the
deployed prompt; this assembler proves the records can produce a
voice-bearing prompt) and (2) a staged generated prompt real enough for
probe-parity to measure whether the RECORDS carry the voice. It assembles
from record FIELDS only - no prose authored beyond section scaffolding;
demonstration records are deliberately NOT read (their dialogues are
Phase-5 exchanges - reading them would break the probe hold-out).

GAP handling, matching the coverage map: the telos close and the
living-traditions close are OMITTED (no record home - the two named GAPs;
probe parity therefore also measures what their absence costs, evidence
for the S2.9-equivalent CO).
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from s62_alx_chunk_views import load_records, STAGING  # noqa: E402

APPARATUS = re.compile(
    r"\s*\((?:[^)]*(?:Doc_|SS\d|Phase\s?\d|OG-\d|CO-0|CO-P2|Article\s?\d|"
    r"alexlex|alexdemo|alexstory|alexgrav|alexforce|alexclaim|srcALX|RCF|"
    r"nodes\.py|the 4\.2|the 5\.1|Round-?\s?[12]|retested|scorer|"
    r"confirmation review|project-lead)[^)]*)\)")


def voice(text: str) -> str:
    out = APPARATUS.sub("", text or "")
    out = re.sub(r"\s{2,}", " ", out)
    return out.strip()


VOICE_FORBIDDEN = re.compile(
    r"Dominant Modern Reconstruction|the record|Inferential-Thin|"
    r"Reported-Experience Status|Widely Accepted|external review|"
    r"cross-check|deferred to", re.I)


def voice_strict(text: str) -> str:
    """Sentence-level guard for claim-field text entering VOICE ground
    statements: any sentence carrying record-apparatus vocabulary is
    dropped whole (the deployed prompt renders the same content in-world;
    matching that is S5-class assembly craft, not this temporary
    generator's job - dropping beats leaking)."""
    kept = [s for s in re.split(r"(?<=[.!?])\s+", voice(text))
            if s and not VOICE_FORBIDDEN.search(s)]
    return " ".join(kept)


def first(rec_map):
    return next(iter(rec_map.values()))[0]


def build_prompt() -> str:
    terms = {rid: rec for rid, (rec, _b) in load_records("term").items()}
    claims = {rid: rec for rid, (rec, _b) in load_records("contested_claim").items()}
    gravities = {rid: rec for rid, (rec, _b) in load_records("gravity").items()}
    core = load_records("world_core")["alexcore001"][0]
    vp = load_records("voice_profile")["alexvoice001"][0]
    sm = vp["speaking_model"]
    ident = vp.get("identity", {})

    role = ident.get("role_label", "").split(" - the ROLE")[0]
    segs = []
    segs.append(
        f"Your name is {ident.get('persona_name', '')}. You keep the work of a "
        f"{role}. {voice(sm['participants'])}")
    tw = core.get("time_window", {})
    segs.append(
        f"Your span runs from the years around {tw.get('start_year')} to the "
        f"years around {tw.get('end_year')}, and everything within it is yours "
        f"to draw on; nothing beyond its edge exists for you. "
        + voice(sm["setting"]))
    # formation_logic carries the world-facing claim in quotes plus an etic
    # apparatus clause ("the record is heavily weighted...") - only the
    # quoted portion may enter voice context (Violation-Indicator guard)
    fl = core.get("formation_logic", "")
    qm = re.search(r'"([^"]+)"', fl)
    fl_voice = qm.group(1) if qm else re.sub(r"^Doc_01 [^:]*: ", "", fl)
    segs.append("The world you speak from: " + voice(fl_voice)
                + " - persisting across the settlement of 325 and beyond.")
    # the two Primary claims ARE the world's ground, in its own register
    for cid in ("alexclaim001", "alexclaim002"):
        segs.append(voice_strict(claims[cid]["claim"]))
    # supporting centers
    segs.append("Beneath all of it runs a trust: "
                + voice(terms["alexlex002"]["quick_meaning"]))
    segs.append("And holding the whole together: "
                + voice(terms["alexlex001"]["quick_meaning"]))
    # the held tensions, in the concedes register
    segs.append("We carry tensions we do not close. "
                + voice_strict(claims["alexclaim004"]["concedes"]) + " "
                + voice_strict(claims["alexclaim001"]["concedes"]))
    # vocabulary quick-reach
    vocab = []
    for tid in ("alexlex005", "alexlex008", "alexlex004", "alexlex011"):
        t = terms[tid]
        vocab.append(f"{t['term']}: {voice(t['quick_meaning'])}")
    segs.append("The words we think in - " + " | ".join(vocab))
    # engagement
    segs.append(voice(sm["act_sequence"]) + " " + voice(sm["genre"]))
    segs.append(voice(sm["key"]) + " " + voice(sm["instrumentalities"]))
    segs.append(voice(sm["ends"]))
    segs.append(voice(sm["norms"]))
    # thinness
    thin = next(t for t in vp["trait_rubric"]
                if t["trait"] == "honest thinness as internal quiet")
    lines = [voice(thin["description"])]
    for i in thin.get("intensities", []):
        lines.append(f"{voice(i['situation'])}: {voice(i['intensity'])}.")
    segs.append("Where our life did not dwell - " + " ".join(lines))
    # pressure responses
    for cid in ("alexclaim003", "alexclaim005"):
        segs.append("What we hold: " + voice_strict(claims[cid]["claim"])
                    + " When pushed: " + voice_strict(claims[cid]["pressure_response"]))
    return "\n\n".join(s for s in segs if s.strip()) + "\n"


def build_capsule() -> str:
    terms = {rid: rec for rid, (rec, _b) in load_records("term").items()}
    gravities = {rid: rec for rid, (rec, _b) in load_records("gravity").items()}
    stories = {rid: rec for rid, (rec, _b) in load_records("story").items()}
    core = load_records("world_core")["alexcore001"][0]

    parts = ["# World Capsule Core - Alexandria (generated view)"]
    parts.append("## The World You Inhabit\n\n"
                 + voice(re.sub(r"^Doc_01 [^:]*: ", "",
                                core.get("formation_logic", ""))))
    order = {"Primary": 0, "Supporting": 1, "Tensional": 2}
    ranked = sorted((g for g in gravities.values()
                     if g["classification"] in order),
                    key=lambda g: (order[g["classification"]], g["id"]))
    lines = []
    for g in ranked:
        lines.append(f"- **{voice(g['name'])}** ({g['classification']}): "
                     f"{voice(g['six_tests']['formation']['verdict'])}")
    parts.append("## What Organizes Everything\n\n" + "\n".join(lines))
    vs_lines = []
    for tid in sorted(terms):
        t = terms[tid]
        if (t.get("retrieval") or {}).get("tier") == 1 and t.get("world_meaning"):
            vs_lines.append(f"**{t['term']}** - {voice(t['quick_meaning'])}")
    parts.append("## The World's Own Words\n\n" + "\n\n".join(vs_lines[:12]))
    st_lines = []
    for sid in sorted(stories):
        s = stories[sid]
        vsurf = s.get("voice_surface", "").split(" Usage guidance")[0]
        st_lines.append(f"- {voice(s.get('title', ''))}: {voice(vsurf)}")
    parts.append("## What We Tell\n\n" + "\n".join(st_lines))
    return "\n\n".join(parts) + "\n"


def main():
    STAGING.mkdir(parents=True, exist_ok=True)
    p = STAGING / "alex_Representative_Permanent_Prompt_generated.txt"
    c = STAGING / "alex_World_Capsule_Core_generated.md"
    p.write_text(build_prompt(), encoding="utf-8", newline="\n")
    c.write_text(build_capsule(), encoding="utf-8", newline="\n")
    print(f"staged: {p.name} ({len(p.read_text(encoding='utf-8').split())} words), "
          f"{c.name}")


if __name__ == "__main__":
    main()
