"""CO-P2-05 (Mark, 2026-07-27, Alternative A) - telos onto world_core.

The Christ-Ward Telos is world-scoped per Mark's call: `telos {text,
status, review_flag}` on desertcore001. The text is Doc10 Section 5's
"How This World's Inhabitation Opens Toward the One It Witnesses"
paragraph VERBATIM (the derivation's own statement - no re-authoring);
status carries Doc10 S5's provisional state, and review_flag carries its
pending-external-review language condensed-verbatim. Idempotent.

(The identity half of this CO lands on voice_profile via
s27_voice_records.py, re-emitted alongside this script.)
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
CORE = BACKEND / "wrs" / "records" / "desert_world" / "world_core" / "desertcore001.md"

TELOS = {
 "text": ("What withdrawal empties a life toward is not emptiness. Antony "
          "did not leave his village to arrive at nothing; he left because "
          "one verse, heard once, addressed him directly, and everything "
          "after was the long work of staying reachable by that address. "
          "Every thought stripped away in the discipline of the logismoi "
          "is stripped away so that what remains is not a purified self "
          "admiring its own stillness, but a person still standing where "
          "the first word found them, listening for it again. Discernment "
          "does not end in a technique perfected; it ends in a person who "
          "has become quiet enough to hear who is speaking. What "
          "Papnoute's whole formation moves toward, when it moves most "
          "fully into itself, is not withdrawal for its own sake — it is "
          "the silence in which the One who first called is still "
          "calling."),
 "status": "provisional",
 "review_flag": ("Doc10 S5 (verbatim-condensed): carries the open flag of "
                 "Constitution v7.4.1 (Provisional) - adversarial AI "
                 "review only, which the Constitution classifies as "
                 "non-validating; provisional pending external scholarly "
                 "review by scholars with formation-theology expertise. "
                 "Grounded in Antony's attested Matthew 19:21 pattern, "
                 "not the unconfirmed wilderness/exile typology (Doc_05 "
                 "SS12 item 1)."),
}


def main() -> None:
    text = CORE.read_text(encoding="utf-8")
    parts = text.split("---\n")
    fm = yaml.safe_load(parts[1])
    fm["telos"] = TELOS
    body = "---\n".join(parts[2:]).rstrip("\n")
    if "CO-P2-05" not in body:
        body += ("\n\nCO-P2-05 (2026-07-27, Alternative A): telos added - "
                 "Doc10 S5's own paragraph verbatim, provisional flag "
                 "carried.")
    CORE.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False,
                                              allow_unicode=True, width=100)
                    + "---\n" + body + "\n", encoding="utf-8")
    print("world_core.telos set (provisional)")


if __name__ == "__main__":
    main()
