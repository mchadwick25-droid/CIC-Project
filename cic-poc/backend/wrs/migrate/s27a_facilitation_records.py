"""S2.7a - Facilitation Brief human-judgment records on world_core (blueprint S2.7a).

Pass 1 SS4.5: the Brief's genuinely human parts - pairing guidance (with
evidence links) and per-world cautions - authored AS RECORDS, early, not
recalled at the end of a 17-step sequence. Home: the world_core record
(Pass 1's SS3.11-style keyed structure - a schema decision the blueprint
made, inherited here).

Every pairing_guidance entry reflects a real cross-lens finding
(Doc_04/Doc_07/Doc_08/Doc_09b - read in full this build), never an
invented pairing; where a finding is flagged in its own source as
claim-pending-confirmation, the guidance carries that flag rather than
hardening it. evidence_links name the records that now carry the evidence
(preferred) plus the source-document locus.

Cautions come from Doc_09b/Doc_09c's own honestly-named gaps and the
Doc10/LiveTest record - each is a documented finding, not generic safety
boilerplate.

Touches: wrs/records/desert_world/world_core/desertcore001.md only
(fields added in place; existing fields preserved byte-for-byte via
YAML round-trip of only the new keys appended).
"""
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]

CORE = BACKEND / "wrs" / "records" / "desert_world" / "world_core" / "desertcore001.md"

PAIRING_GUIDANCE = [
 {"guidance": ("Pair with the Alexandrian catechetical world on scripture: "
               "practical, occasion-addressed engagement (a verse handed "
               "back as something to do) against systematic allegorical "
               "exegesis - the one cross-world contrast this world's own "
               "build documents explicitly, and the strongest divergence "
               "pairing in the contested-claim set. A table question on "
               "'how should scripture form a person' gets two genuinely "
               "different, well-evidenced answers."),
  "evidence_links": ["desertclaim006", "desertgrav007",
                     "Doc_01 SS8.1/SS4 (World #2 contrast)",
                     "Doc_07 SS7 (interpretation IS formation)"]},
 {"guidance": ("Pair with the Hieronymian ascetic-literary world to break "
               "the surface word 'ascetic': same vocabulary, genuinely "
               "different social structure (communal/non-elite, "
               "labor-sustained vs. elite patronage-network), transmission "
               "medium (oral saying vs. literary production), and language "
               "(Coptic vs. Latin). The pairing teaches that a shared word "
               "is not a shared formation logic."),
  "evidence_links": ["desertclaim001", "desertclaim004",
                     "Doc_01 SS8.1", "Doc_09b SS3 (vs. World #9)"]},
 {"guidance": ("Pair with the Imperial-Juridical world on authority: "
               "earned, person-based discernment against office, see-rank, "
               "and law - and use this world's own live internal tension "
               "(person- vs. office-based authority, never resolved in its "
               "own span) to keep the pairing honest: the desert is not a "
               "clean counter-example, it carries the office model inside "
               "itself. Their Tensional gravity 6 fights the same axis "
               "from the institutional side."),
  "evidence_links": ["desertclaim003", "desertgrav010",
                     "Doc_07 SS3 (three observations on gravity 10)",
                     "Imperial-Juridical Doc_04 SS4 (Tensional 6)"]},
 {"guidance": ("Pair with the Syriac world on where asceticism lives: "
               "covenanted ascetic life inside the town congregation "
               "against geographic withdrawal to marginal land - two "
               "ascetic Primaries that answer 'must you leave?' "
               "differently. Both sides are documented in each world's own "
               "Doc_04."),
  "evidence_links": ["desertclaim001",
                     "Syriac Doc_04 SS4 (Primary C2, covenanted ascetic life)",
                     "desertgrav001"]},
 {"guidance": ("Boundary-energy pairings (vs. Donatism or the "
               "Imperial-Juridical world) can contrast this world's "
               "inward-running boundary energy (against the thoughts) with "
               "outward-running boundary-drawing - but Doc_07 flags this "
               "cross-world characterization as this build's own claim "
               "pending confirmation, not an established parallel; a "
               "facilitator should frame it as an exploration, not a "
               "settled contrast."),
  "evidence_links": ["Doc_07 SS4 + SS12 item 1 (flag carried)",
                     "Doc_09b SS3 (vs. Worlds #4/#6, same flag)"]},
]

CAUTIONS = [
 ("Relational-safety review of this world's own content (spiritual combat, "
  "demonic imagery, ascetic self-denial) for encounter implications has "
  "NOT been performed - Doc_09c SS4 names it as a distinct, required, "
  "not-yet-done review. Facilitators should know the gap exists."),
 ("Living tradition, unbroken line: Coptic Orthodox monasticism descends "
  "directly from this world, and the living-tradition-differentiation "
  "review is an unperformed freeze-eligibility gate (Doc_09c SS4/SS7). The "
  "Representative's horizon closes c. 430 - before Ephesus and Chalcedon - "
  "and must never be read as commentary on any present-day communion's "
  "practice or on the disputes that later divided them."),
 ("The world's own named recruitment risk is diagnostic fusion sliding "
  "from self-description into participant-diagnosis (Doc10 S4). The "
  "Representative is calibrated against it; a facilitator should not "
  "invite it either (e.g. by asking the Representative to 'name what is "
  "going on in' a participant)."),
 ("Thin domains are honestly thin, not withheld: named women's material "
  "beyond a small set of preserved sayings, liturgical content beyond "
  "structure and rhythm, the Melitian community's interior life, ordinary "
  "non-literate participants' own first-person experience (Doc_09b SS2, "
  "Doc_09c SS5). Pressing the Representative to fill these will get honest "
  "refusal, not texture."),
 ("Named-figure boundary: the Representative carries exactly four vetted "
  "sayings whole (Moses/jug, Arsenius/flee-be-still, Sarah's answer, "
  "general community-life texture) and categorically declines to construct "
  "scenes for any other name - including well-known ones like Poemen or "
  "Sisoes (LiveTest_Scoring_Review 2026-07-11, fix 3). Participants asking "
  "for such stories will be declined in-voice; this is the system working, "
  "not a malfunction."),
 ("Anxiety and intrusive-thought conversations sit close to this world's "
  "core vocabulary (logismoi) and tempt a clinical mapping in either "
  "direction. The world's frame is not a clinical frame (the logismoi "
  "record's own distortion-risk pairing), and crisis disclosures get an "
  "in-voice redirection toward direct human support (Doc10 S7 "
  "relational-safety probe, Article 33)."),
]


def main() -> None:
    text = CORE.read_text(encoding="utf-8")
    parts = text.split("---\n")
    # parts[0] empty, parts[1] = front matter, rest = body
    fm = yaml.safe_load(parts[1])
    fm["pairing_guidance"] = PAIRING_GUIDANCE
    fm["cautions"] = CAUTIONS
    body = "---\n".join(parts[2:]).strip()
    if "S2.7a" not in body:
        body += ("\n\nS2.7a (2026-07-27): pairing_guidance + cautions "
                 "authored as records per Pass 1 SS4.5 - each guidance "
                 "entry reflects a documented cross-lens finding with "
                 "evidence links; cautions from Doc_09b/c's own named "
                 "gaps and the Doc10/LiveTest record.")
    new = "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True,
                                    width=100) + "---\n" + body + "\n"
    CORE.write_text(new, encoding="utf-8")
    print(f"world_core updated: {len(PAIRING_GUIDANCE)} pairing_guidance, "
          f"{len(CAUTIONS)} cautions")


if __name__ == "__main__":
    main()
