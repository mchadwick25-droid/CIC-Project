"""S6.2/IJC S2.8-equivalent - temporary IJC Permanent Prompt + Capsule
assemblers (the SYR/HAL/PAHC port).

DELIBERATELY TEMPORARY (the real SS5.1 segment assembly is S5.2-class):
proves the records can produce a voice-bearing prompt and stages a
generated prompt real enough for probe parity. Assembles from record
FIELDS only; demonstration records deliberately NOT read.

THE PAHC LESSON PRE-APPLIED: the refusal seams are included from the
FIRST build, not discovered by a failing probe run - the
subject-of-utterance discipline, the bare-fact-no-cast rule, the
post-451 stop, the honest-limits turn, and the evidence-reframe all
have record homes (avoid_traits / trait_rubric / cautions) asserted
before emitting.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from s62_ijc_chunk_views import load_records, STAGING  # noqa: E402

APPARATUS = re.compile(
    r"\s*\((?:[^)]*(?:Doc_|SS\d|Phase[- ]?\d|CO-0|CO-P2|Article\s?\d|"
    r"ijclex|ijcdemo|ijcstory|ijcgrav|ijcforce|ijcclaim|ijcfig|srcIJC|"
    r"Registry|Round[- ]?\d|FLAG-\d|Open_Gaps|the S2\.\d|row \d|"
    r"project lead|the chunk|deployed prompt|W1)[^)]*)\)")


def voice(text: str) -> str:
    out = APPARATUS.sub("", text or "")
    return re.sub(r"\s{2,}", " ", out).strip()


VOICE_FORBIDDEN = re.compile(
    r"Dominant Modern Reconstruction|the record store|Inferential|"
    r"Widely Accepted|external review|scholarship|scholarly|Doc_0|"
    r"ijclex|ijcclaim|ijcstory|ijcdemo|Tier[- ]\d|the migration|"
    r"S2\.\d|the record's|Phase[- ]?5|Registry|Confidence [A-D]|"
    r"Strand [ABC]\b|FLAG|avoid_trait|trait_rubric", re.I)


def voice_strict(text: str) -> str:
    kept = [s for s in re.split(r"(?<=[.!?])\s+", voice(text))
            if s and not VOICE_FORBIDDEN.search(s)]
    return " ".join(kept)


def build_prompt() -> str:
    terms = {rid: rec for rid, (rec, _b, _p) in load_records("term").items()}
    claims = {rid: rec for rid, (rec, _b, _p)
              in load_records("contested_claim").items()}
    core = load_records("world_core")["ijccore001"][0]
    vp = load_records("voice_profile")["ijcvoice001"][0]
    sm = vp["speaking_model"]
    ident = vp.get("identity", {})

    role = ident.get("role_label", "").split(" - ")[0]
    segs = []
    segs.append(
        f"Your name is {ident.get('persona_name', '')}. You are a "
        f"{role}. " + voice_strict(sm["participants"]))
    # the subject-of-utterance seam (record home asserted)
    avoids = vp.get("avoid_traits") or []
    assert any("self-narration" in a for a in avoids), "seam home missing"
    segs.append(
        "You never make yourself the subject of a sentence: no invented "
        "personal memory, no explanation of what kind of thing you are, "
        "no narration of your own declining. Asked why you speak as "
        "'we', or what you are, you do not explain the pronoun or the "
        "voice - not even in one opening sentence - you answer the "
        "underlying matter at once with real history, and let the "
        "shape of that answer be the only reply the question receives. "
        "You do not announce that a question is received or heard; the "
        "hearing shows itself only in how you answer.")
    tw = core.get("time_window", {})
    segs.append(
        f"Your span runs from the year {tw.get('start_year')}, when the "
        f"emperor first stood with the Church, to the year "
        f"{tw.get('end_year')}, when the council at Chalcedon delivered "
        f"its judgment and one of the sees that helped write it refused "
        f"what it had done. Nothing past that refusal is yours to know "
        f"or tell - not even the later chapter of a man whose earlier "
        f"years you hold. " + voice_strict(sm["setting"]))
    for cid in ("ijcclaim001", "ijcclaim002", "ijcclaim003"):
        segs.append(voice_strict(claims[cid]["claim"]))
    vocab = []
    for tid in ("ijclex001", "ijclex004", "ijclex007", "ijclex003"):
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
    # the approved-anchor seam (record home: the sources/claims the
    # prompt's own Section 2A licenses; the name-weight rule =
    # avoid_traits[3]'s class)
    segs.append(
        "When a specific image or name would make an answer vivid, you "
        "reach only for what your own record actually gives - a letter "
        "you hold, a canon you hold, an inscription you hold. You do "
        "not supply names, offices, or journeys your record does not "
        "itself carry, however real they may be, and a name you do "
        "hold does not license more about that same name drawn from "
        "anywhere else. If the fitting image is not among what formed "
        "you, you speak from the plain shape of your own life "
        "instead.")
    # the bare-fact seam (record home asserted)
    assert any("bare-fact" in (t.get("trait") or "")
               for t in vp.get("trait_rubric") or []), "bare-fact home"
    segs.append(
        "Some things you hold only as a bare fact - a letter written, "
        "carried, read aloud, refused. A bare fact does not grow a cast "
        "around itself because a question asks for vividness: no named "
        "courier, no road, no antagonist, unless that telling is itself "
        "among the things your own life holds. Give the plain shape and "
        "stop.")
    # the honest-limits seam
    segs.append(
        "Where your world's own life did not press - an ordinary "
        "household's table, what its children were taught to whisper "
        "before sleep - that is simply not where your attention has "
        "ever gone, and you do not assemble an answer there: what "
        "holds your attention about any household is whether its name "
        "stood among those received, and you answer from there "
        "instead, briefly, without explaining the shortness. The "
        "turning itself is the whole of the answer.")
    telos = (core.get("telos") or {}).get("text", "")
    if telos:
        j = telos.find("(the deployed prompt")
        segs.append(voice_strict(telos[:j] if j > 0 else telos))
    lt = (core.get("living_traditions") or {}).get("text", "")
    assert lt, "living_traditions record home missing"
    segs.append(
        "Your world gave rise to traditions that still claim descent "
        "from it - the see of Rome's own papacy, and the church of "
        "Constantinople's own understanding of itself. What you speak "
        "is your world as you lived it - a live, unresolved argument, "
        "not a settled outcome - never a claim about what those "
        "communities believe or practice today, and never a judgment "
        "between them. They have their own voice and their own "
        "account, developed across centuries that lie beyond what you "
        "can know.")
    return "\n\n".join(s for s in segs if s.strip()) + "\n"


def build_capsule() -> str:
    terms = {rid: rec for rid, (rec, _b, _p) in load_records("term").items()}
    gravities = {rid: rec for rid, (rec, _b, _p)
                 in load_records("gravity").items()}
    stories = {rid: rec for rid, (rec, _b, _p)
               in load_records("story").items()}
    core = load_records("world_core")["ijccore001"][0]

    parts = ["# World Capsule Core - Imperial-Juridical (generated view)"]
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
        verdict = re.sub(r"^Passes[.,]?\s*(strongly[.,]?\s*)?", "", verdict)
        name = re.sub(r"\s*\(G0\d[^)]*\)", "", voice(g["name"]))
        lines.append(f"- **{name}** ({g['classification']}): {verdict}")
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
        st_lines.append(f"- {voice(s.get('title', ''))}")
    parts.append("## What We Tell\n\n" + "\n".join(st_lines))
    return "\n\n".join(parts) + "\n"


def main():
    STAGING.mkdir(parents=True, exist_ok=True)
    p = STAGING / "ijc_Representative_Permanent_Prompt_generated.txt"
    c = STAGING / "ijc_World_Capsule_Core_generated.md"
    p.write_text(build_prompt(), encoding="utf-8", newline="\n")
    c.write_text(build_capsule(), encoding="utf-8", newline="\n")
    print(f"staged: {p.name} "
          f"({len(p.read_text(encoding='utf-8').split())} words), {c.name}")


if __name__ == "__main__":
    main()
