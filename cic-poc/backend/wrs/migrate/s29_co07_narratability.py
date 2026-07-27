"""CO-P2-07 (Mark, 2026-07-27) - narratability resolutions.

Split by what the record actually holds (the recommendation Mark
adopted):

- Syncletica and Theodora: allusion-only story records (desertstory009/
  010). The build's own documents attest that named sayings of theirs are
  a genuine, if thin, part of the Apophthegmata tradition (Doc_02 SS1.6;
  the geron/abba/amma chunk's own plural-voices flag) but carry NO
  individual saying text for either - so the story text states exactly
  that attested fact and nothing more, and `tellable_as: allusion-only`
  licenses acknowledgment without scene-telling or quotation. No saying
  is invented, no Vita material imported from outside the build's record.
  Their figure records gain the story_ids; `narratable` stays false
  (correct - nothing is scene-tellable).

- Poemen and Sisoes: `accepted_refusal_note` on their figure records -
  the live-tested categorical guard's refusal IS the design (LiveTest
  fix 3); the note documents Mark's acceptance so the gate goes quiet by
  recorded decision, not suppression.

Figure records are s24 emissions edited in place here; if s24 is ever
re-run, re-run this script after it. Idempotent.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

STORYDIR = BACKEND / "wrs" / "records" / "desert_world" / "story"
FIGDIR = BACKEND / "wrs" / "records" / "desert_world" / "figure"

COMMON = {"world_id": "desert-monasticism", "record_type": "story",
          "schema_version": 1, "jobs": [1, 2, 3], "register": "emic",
          "review_state": "draft", "cache_stability": "static"}

ALLUSIONS = [
 dict(
  id="desertstory009",
  title="Amma Syncletica among the named mothers (allusion only)",
  owner="desertfig007", figure_name="Syncletica"),
 dict(
  id="desertstory010",
  title="Amma Theodora among the named mothers (allusion only)",
  owner="desertfig008", figure_name="Theodora"),
]

REFUSALS = {
 "desertfig009": ("Poemen", "the wider Apophthegmata corpus outside this "
                             "build's vetted record"),
 "desertfig010": ("Sisoes", "the wider Apophthegmata corpus outside this "
                             "build's vetted record"),
}


def allusion_record(a: dict) -> dict:
    n = a["figure_name"]
    rec = dict(COMMON)
    rec.update({
     "id": a["id"], "title": a["title"],
     "narrative_tier": {
      "tier": 2,
      "justification": (
       f"Named amma genuinely attested: Widely Accepted that {n} and her "
       f"sayings are a real, if thin, part of the Apophthegmata tradition "
       f"(Doc_02 §1.6; Doc_06 §1.6's plural-voices flag); Inferential / Thin "
       f"for any claim beyond what the surviving sayings themselves state. "
       f"No individual saying of hers is vetted into this build's record - "
       f"which is why this record licenses allusion only, never "
       f"scene-telling or quotation (CO-P2-07).")},
     "text": (
      f"The tradition preserves sayings under Amma {n}'s name - she is "
      f"one of the named mothers whose tested words the Apophthegmata "
      f"kept, transmitted through the same later-compiled apparatus as "
      f"the male-attributed sayings, with a much smaller surviving "
      f"sample. This build carries none of her individual sayings whole; "
      f"what can be told is that she is real, named, and attested, and "
      f"that her material is thin - said plainly rather than filled."),
     "attested_occasion": (
      "None carried - her attestation in this build is corpus-level (the "
      "ammas' sayings within the Apophthegmata tradition, srcDES006); no "
      "individual saying with its occasion is vetted into the record."),
     "tellable_as": "allusion-only",
     "voice_surface": (
      f"Amma {n} is among the named mothers whose tested words the "
      f"tradition kept. What we can tell of her is real but thin, and we "
      f"say so plainly rather than filling the silence."),
     "retrieval": {
      "tier": 2,
      "retrieve_when": [
       f"participant asks about {n} by name, or about the desert "
       f"mothers/ammas beyond Sarah"],
      "do_not_retrieve_when": [
       {"condition_type": "sense-disambiguation",
        "text": ("participant asks for a specific saying or scene of "
                 "hers - the record licenses acknowledgment only; the "
                 "honest-thinness answer is the content")}],
      "force_llm_vote": False},
     "sources": [
      {"source_id": "srcDES006",
       "author_gravity_note": (
        "Widely Accepted that the named ammas and their sayings are a "
        "genuine, if thin, part of the Apophthegmata tradition; "
        "Inferential / Thin beyond what the sayings themselves state "
        "(Doc_02 §1.6).")}],
     "owner_figure_id": a["owner"],
    })
    return rec


def main() -> None:
    for a in ALLUSIONS:
        emit_record(allusion_record(a),
                    ("CO-P2-07 allusion-only story record (2026-07-27): "
                     "attested-fact text only - no saying invented, no "
                     "material imported from outside the build's record."),
                    STORYDIR / f"{a['id']}.md")
    # figure updates
    for a in ALLUSIONS:
        p = FIGDIR / f"{a['owner']}.md"
        text = p.read_text(encoding="utf-8")
        parts = text.split("---\n")
        fm = yaml.safe_load(parts[1])
        ids = fm.setdefault("story_ids", [])
        if a["id"] not in ids:
            ids.append(a["id"])
            body = "---\n".join(parts[2:]).rstrip("\n")
            body += (f"\n\nCO-P2-07 (2026-07-27): allusion-only story "
                     f"{a['id']} linked; narratable stays false - nothing "
                     f"is scene-tellable, allusion is the license.")
            p.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False,
                                                   allow_unicode=True,
                                                   width=100)
                         + "---\n" + body + "\n", encoding="utf-8")
    for fid, (name, corpus) in REFUSALS.items():
        p = FIGDIR / f"{fid}.md"
        text = p.read_text(encoding="utf-8")
        parts = text.split("---\n")
        fm = yaml.safe_load(parts[1])
        if not fm.get("accepted_refusal_note"):
            fm["accepted_refusal_note"] = (
             f"Accepted refusal (CO-P2-07, Mark, 2026-07-27): {name} is "
             f"named in the Permanent Prompt precisely as a name the "
             f"Representative will NOT build scenes for - the live-tested "
             f"categorical guard (LiveTest fix 3) is the design, and its "
             f"in-voice refusal is the correct behavior. His material in "
             f"{corpus} stays unvetted; no story record is authored.")
            body = "---\n".join(parts[2:]).rstrip("\n")
            body += ("\n\nCO-P2-07 (2026-07-27): accepted-refusal "
                     "recorded; the narratability gate is quiet by "
                     "documented decision.")
            p.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False,
                                                   allow_unicode=True,
                                                   width=100)
                         + "---\n" + body + "\n", encoding="utf-8")
    print("2 allusion stories emitted; 2 figures linked; 2 accepted-refusals recorded")


if __name__ == "__main__":
    main()
