"""S6.2/PAHC S2.8-equivalent - temporary PAHC Permanent Prompt + Capsule
assemblers (the SYR/HAL s62_*_capsule_prompt_views.py port).

DELIBERATELY TEMPORARY (the real SS5.1 segment assembly is S5.2-class):
proves the records can produce a voice-bearing prompt and stages a
generated prompt real enough for probe parity. Assembles from record
FIELDS only; demonstration records deliberately NOT read (their
dialogues are the Phase-5 Amma exchanges - the probe hold-out).

Like SYR/HAL, NO omitted-GAP handling needed: the telos and
living-traditions closes HAVE record homes (S2.7a carried the W1
prompt's own paras 43/45 onto world_core per CO-P2-05/17); prompt
coverage runs at zero GAPs. The living-traditions close is emitted as
a scaffold sentence in the prompt para-45 register (the record's text
carries facilitator-apparatus framing - 'the Article-29 gate', 'the
prompt's own' - that must never reach voice).
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from s62_pahc_chunk_views import load_records, STAGING  # noqa: E402

APPARATUS = re.compile(
    r"\s*\((?:[^)]*(?:Doc_|SS\d|Phase\s?\d|CO-0|CO-P2|Article\s?\d|"
    r"pahclex|pahcdemo|pahcstory|pahcgrav|pahcforce|pahcclaim|pahcfig|"
    r"Registry|G0\d|Strand [AB]|RCF|nodes\.py|Round[- ]?\d|scorer|"
    r"the S2\.\d|FLAG-\d|Construction Notes|World Profile|project lead|"
    r"the chunk|chunk |deployed prompt|live-test|the identity decision|"
    r"W1)[^)]*)\)")


def voice(text: str) -> str:
    out = APPARATUS.sub("", text or "")
    out = re.sub(r"\s{2,}", " ", out)
    return out.strip()


VOICE_FORBIDDEN = re.compile(
    r"Dominant Modern Reconstruction|the record store|Inferential[/-]Thin|"
    r"Reported-Experience Status|Widely Accepted|external review|"
    r"cross-check|deferred to|scholarship|scholarly|Doc_0|pahclex|"
    r"pahcclaim|pahcstory|pahcdemo|force_llm_vote|Tier[- ]\d|"
    r"single-source|Contested|Documented\b|the migration|"
    r"S2\.\d|the record's|Author.Gravity|the scorer|Round \d|"
    r"Strand [AB]\b|Registry [PS]\d|the Phase|Article.?\d", re.I)


def voice_strict(text: str) -> str:
    kept = [s for s in re.split(r"(?<=[.!?])\s+", voice(text))
            if s and not VOICE_FORBIDDEN.search(s)]
    return " ".join(kept)


def build_prompt() -> str:
    terms = {rid: rec for rid, (rec, _b, _p) in load_records("term").items()}
    claims = {rid: rec for rid, (rec, _b, _p)
              in load_records("contested_claim").items()}
    core = load_records("world_core")["pahccore001"][0]
    vp = load_records("voice_profile")["pahcvoice001"][0]
    sm = vp["speaking_model"]
    ident = vp.get("identity", {})

    role = ident.get("role_label", "").split(" (")[0]
    segs = []
    segs.append(
        f"Your name is {ident.get('persona_name', '')}. You are a {role}. "
        + voice_strict(sm["participants"]))
    tw = core.get("time_window", {})
    segs.append(
        f"Your span runs from the years just after the last of those who "
        f"walked with the Lord had died (about the year {tw.get('start_year')}"
        f" and the decades following) to about the year {tw.get('end_year')},"
        f" when a single bishop's office has begun, in place after place, to "
        f"be simply assumed rather than still argued for; nothing beyond "
        f"that edge exists for you. " + voice_strict(sm["setting"]))
    for cid in ("pahcclaim001", "pahcclaim002", "pahcclaim003"):
        segs.append(voice_strict(claims[cid]["claim"]))
    vocab = []
    for tid in ("pahclex003", "pahclex004", "pahclex001", "pahclex002",
                "pahclex007", "pahclex005"):
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
    # the household's measure (record homes: native_measure.typical_words
    # + the handful-of-short-sentences trait); the probe-parity catch:
    # without this seam the assembled voice elaborates past the deployed
    # voice's measure
    meas = next((t for t in vp.get("trait_rubric") or []
                 if "handful of short sentences" in (t.get("description") or "")),
                None)
    assert meas is not None, "measure trait record home missing"
    assert (vp.get("native_measure") or {}).get("typical_words") == 70
    # the Decision PAHC-4 guard (FLAG-034): the said-whole-and-left
    # genre rule extended to re-opening an already-given word; record
    # home asserted before emitting
    assert "said whole and then left" in (sm.get("genre") or ""), (
        "said-whole genre record home missing")
    segs.append(
        "A word you have already used and made plain, you leave "
        "standing. You do not circle back in a later turn to ask "
        "whether it was understood, or to re-open what you meant by "
        "it, unless the visitor themselves asks you. A teaching said "
        "whole is left whole; if a word's sense matters again, the "
        "clarity arrives inside the new answer, while the word is "
        "being used.")
    segs.append(
        "Your answers keep a household's measure. Most of what you say "
        "to a visitor fits in a handful of short sentences, said whole "
        "and then left; even your fullest answer stops at two short "
        "paragraphs. When more is truly needed, you let the visitor's "
        "next question draw it out.")
    # the carried-not-authored seam + the quiet territories (record
    # homes: the letter-writers trait_rubric entry + the named-silences
    # cautions - the SILENT VOICES rule and the no-ledgers fact); the
    # probe-parity catch: without this seam the assembled voice
    # attributes the letter-writers' arguments but still performs them
    # in full, breaking the deployed voice's refusal boundary
    carried = next((t for t in vp.get("trait_rubric") or []
                    if "letter-writers" in (t.get("description") or "")),
                   None)
    assert carried is not None, "carried-not-authored trait record home missing"
    cautions_all = " ".join(core.get("cautions") or [])
    assert "SILENT VOICES" in cautions_all, "silent-voices caution missing"
    assert "danger and orality" in cautions_all, (
        "formation-internal-thinness caution (the no-ledgers carrier) missing")
    segs.append(
        "There are territories where your own life has not "
        "concentrated. The sharpest arguments against the teachers you "
        "refuse, and for a single office's necessity, belong to "
        "particular men who set them down in their own name, under real "
        "threat. You have heard those arguments and lived inside "
        "communities they shaped; you hold their conclusions - but you "
        "did not write them, and you do not claim to have. Asked to "
        "argue them as your own, point by point, in a philosopher's "
        "manner, you decline plainly and give instead the plainer thing "
        "your own life gives you, at your own measure. Of those among "
        "you who serve rather than lead, or who never learned to write, "
        "you know mostly what others have said of them; you do not "
        "invent a voice for that silence. Of any office's ledgers or "
        "records there are none anywhere among us to speak from; "
        "nothing is kept among us but letters, written for a purpose "
        "and read aloud.")
    # the two-fears trait (record home: the trait_rubric entry naming
    # docetic doubt + mercy-exhaustion); asserted present before emitting
    fear = next((t for t in vp.get("trait_rubric") or []
                 if "Docetic" in (t.get("description") or "")), None)
    assert fear is not None, "two-fears trait record home missing"
    segs.append("Two fears you hold without choosing between them: "
                + voice_strict(fear["description"]))
    segs.append("Of the women the record keeps a word for: "
                + voice_strict(claims["pahcclaim005"]["claim"]) + " "
                + voice_strict(claims["pahcclaim005"]["concedes"]))
    segs.append("Of the meal that carries love's own name: "
                + voice_strict(claims["pahcclaim004"]["claim"]))
    telos = (core.get("telos") or {}).get("text", "")
    if telos:
        segs.append(voice_strict(telos))
    lt = (core.get("living_traditions") or {}).get("text", "")
    assert lt, "living_traditions record home missing"
    segs.append(
        "What you have lived gave rise, in time, to every church that "
        "would come after you; all of them, in their many and "
        "disagreeing forms, look back to rooms like yours and call them "
        "the pattern. What you speak is your life as you have lived it - "
        "not a ruling on what any later community believes or practices, "
        "not a judgment on how well any of them keeps what you handed "
        "on. Those communities have their own voice and their own "
        "account of themselves. You are not it. You are the ones who "
        "were there.")
    return "\n\n".join(s for s in segs if s.strip()) + "\n"


def build_capsule() -> str:
    terms = {rid: rec for rid, (rec, _b, _p) in load_records("term").items()}
    gravities = {rid: rec for rid, (rec, _b, _p)
                 in load_records("gravity").items()}
    stories = {rid: rec for rid, (rec, _b, _p)
               in load_records("story").items()}
    core = load_records("world_core")["pahccore001"][0]

    parts = ["# World Capsule Core - Post-Apostolic House-Church "
             "(generated view)"]
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
        verdict = re.sub(r",?\s*flagged for Doc_0\d [a-z]+\b", "", verdict)
        verdict = re.sub(r"^PASS[^-]*-\s*", "", verdict)
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
        vsurf = s.get("voice_surface", "").split(" Usage guidance")[0]
        st_lines.append(f"- {voice(s.get('title', ''))}: {voice(vsurf)}")
    parts.append("## What We Tell\n\n" + "\n".join(st_lines))
    return "\n\n".join(parts) + "\n"


def main():
    STAGING.mkdir(parents=True, exist_ok=True)
    p = STAGING / "pahc_Representative_Permanent_Prompt_generated.txt"
    c = STAGING / "pahc_World_Capsule_Core_generated.md"
    p.write_text(build_prompt(), encoding="utf-8", newline="\n")
    c.write_text(build_capsule(), encoding="utf-8", newline="\n")
    print(f"staged: {p.name} "
          f"({len(p.read_text(encoding='utf-8').split())} words), {c.name}")


if __name__ == "__main__":
    main()
