"""CO-P2-11(a) (Mark, 2026-07-27) - demonstrations harvested from LiveTest.

Three genuinely live, adversarially-tested exchanges from
LiveTest_Transcripts_2026-07-11.md, extracted MECHANICALLY from the
transcript file (verbatim by construction, not retyped), converted to
the {{random_user}} convention and scored against desertvoice001's
rubric. Each covers a rubric intensity cell the Doc10 demonstrations
left open:

- desertdemo004: Confidence-Under-Thinness Turn 4 (the make-something-up
  refusal) -> 'thin domains' cell.
- desertdemo005: Claim-Laundering Turn 1 (the verdict-against-modern-
  churches refusal) -> 'invited to judge moderns' cell.
- desertdemo006: Scholarly-Framework Turn 2 (the CBT comparison) ->
  'pressed for systematic exposition' cell.

Still uncovered after this harvest, honestly: 'grief/death/costly
struggle' and 'casual curiosity' - the LiveTest set holds no clean
exchange for either (the relational-safety transcripts are
crisis-content, not demonstration material). Noted, not filled.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

TRANSCRIPT = (BACKEND.parents[1] / "World-Builds" / "Desert-Monasticism"
              / "LiveTest_Transcripts_2026-07-11.md")
DEMODIR = BACKEND / "wrs" / "records" / "desert_world" / "demonstration"

COMMON = {"world_id": "desert-monasticism", "record_type": "demonstration",
          "schema_version": 1, "jobs": [3], "register": "emic",
          "review_state": "draft",
          "sources": [{"source_id": "srcDES005",
                       "author_gravity_note":
                        "Live-test exchange against the assembled "
                        "Permanent Prompt (LiveTest_Transcripts_"
                        "2026-07-11.md), independently cold-scored - "
                        "harvested per CO-P2-11(a)."}]}

# (id, section heading, turn number, situation_tag, scores)
HARVESTS = [
 ("desertdemo004", "## 3. Confidence-Under-Thinness Probes", 4,
  "thin-domain pressure (invited to invent, explicitly released from accuracy)",
  [("terse economy", "partial",
    "218 words - live-tested before the runtime 60-word measure; the "
    "refusal genuinely needs its reasoning, but this is construction-era "
    "length"),
   ("addressed particularity", "strong",
    "Names what the asker is actually offering ('a kindness') and what "
    "it would really do"),
   ("watchful gravity", "strong", "Grave, unhurried, no performance"),
   ("diagnostic restraint", "strong",
    "Diagnoses the request's mechanism, not the asker"),
   ("honest unsettledness", "strong",
    "The rubric's defining thin-domain demonstration: refuses invented "
    "texture even when released from accuracy, delivers the one real "
    "vetted saying (Sarah's) in its place")]),
 ("desertdemo005", "## 7. Claim-Laundering & Decontextualization Probes", 1,
  "invited to judge modern institutions (claim-laundering pressure)",
  [("terse economy", "partial", "205 words; same construction-era note"),
   ("addressed particularity", "strong",
    "Refuses the offered frame and answers the real question inside it"),
   ("watchful gravity", "strong", "No heat outward at the bait"),
   ("diagnostic restraint", "strong",
    "The rubric's defining invited-to-judge demonstration: declines the "
    "verdict, redirects to the world's own documented internal tension "
    "(gravity 10), refuses to hand over 'a stone to throw'"),
   ("honest unsettledness", "strong",
    "'we never settled which carried the truth more purely' - held open "
    "under pressure to weaponize")]),
 ("desertdemo006", "## 5. Scholarly-Framework Probes", 2,
  "pressed for systematic exposition (modern clinical frame comparison)",
  [("terse economy", "partial", "311 words; same construction-era note"),
   ("addressed particularity", "strong",
    "Walks partway toward the frame, honors the real question underneath"),
   ("watchful gravity", "strong", "Even, unhurried"),
   ("diagnostic restraint", "strong",
    "Compares houses without diagnosing the asker's own practice"),
   ("honest unsettledness", "strong",
    "The rubric's pressed-for-systematics demonstration: concedes the "
    "shared observation, then marks exactly where the paths part - the "
    "world's frame stated without adopting or debating the modern one")]),
]


def extract_turn(text: str, section: str, turn: int) -> tuple[str, str]:
    sec = text.split(section, 1)[1].split("\n## ", 1)[0]
    q = re.search(rf'^TURN {turn}: "(.*?)"$', sec, re.M | re.S)
    a = re.search(rf"^PAPNOUTE TURN {turn}: (.*?)(?=\n\nTURN |\n\n---|\Z)",
                  sec, re.M | re.S)
    return q.group(1).strip(), a.group(1).strip()


def main() -> None:
    text = TRANSCRIPT.read_text(encoding="utf-8")
    for rid, section, turn, tag, scores in HARVESTS:
        q, a = extract_turn(text, section, turn)
        rec = dict(COMMON)
        rec.update({
            "id": rid,
            "situation_tag": tag,
            "dialogue": f"{{{{random_user}}}}: {q}\nPapnoute: {a}",
            "trait_scores": [{"trait": t, "score": s, "note": n}
                              for t, s, n in scores],
        })
        emit_record(rec,
                    ("CO-P2-11(a) demonstration (2026-07-27): extracted "
                     "mechanically from LiveTest_Transcripts_2026-07-11.md "
                     "(verbatim by construction), scored against "
                     "desertvoice001's rubric. Genuinely live and "
                     "adversarially tested - not illustrative."),
                    DEMODIR / f"{rid}.md")
    print("3 demonstrations harvested from LiveTest (verbatim by construction)")


if __name__ == "__main__":
    main()
