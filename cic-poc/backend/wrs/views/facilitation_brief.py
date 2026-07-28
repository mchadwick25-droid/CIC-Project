"""S5.5 - the World Facilitation Brief, live (Pass 1 SS3.9 + blueprint S5.5).

Two deployed outputs for the migrated world, both generated views
(regenerate, never hand-edit; --check byte-compares without writing):

  data/desert_world/desert_Facilitation_Brief_generated.md
      the full facilitator-facing Brief - voice, pairing guidance,
      cautions, divergence bank, gravity structure. The etic apparatus
      stays IN: this is the one view where citations belong.

  data/desert_world/facilitator_cautions_generated.txt
      the operational cautions distillation the RUNTIME speaks from -
      app/world_manifest.py reads this file for migrated worlds instead
      of its hand-condensed string (fail-open to that string if the file
      is absent). This is the S5.5 blueprint line "facilitator_cautions
      ... becomes a render" made literal.

Content rule for the cautions render: every S2.7a caution record lands,
whole, in record order - they were authored as facilitator-facing
operational cautions and are richer than the hand string on five of its
six fronts. The sixth (the Evagrius posthumous-condemnation boundary)
has NO record home - FLAG-015 - and rides as a verbatim parked addendum
under a marked delimiter until Mark's CO gives it one. Nothing the
facilitator holds today is lost; nothing is silently invented.

Supersedes wrs/views/brief_view.py (the S2.8 staging-parity stager,
untouched here per the declared file set; S6.5 retirement candidate).

Deterministic: same records -> byte-identical outputs.

Usage (from cic-poc/backend):
  python wrs/views/facilitation_brief.py            # write both views
  python wrs/views/facilitation_brief.py --check    # verify deployed current
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
for p in (str(HERE), str(BACKEND)):
    if p not in sys.path:
        sys.path.insert(0, p)

from chunk_views import load_records  # noqa: E402

DATA_DIR = BACKEND / "data" / "desert_world"

# FLAG-015: hand-authored caution content with no record home yet, parked
# verbatim (source: app/world_manifest.py's Desert facilitator_cautions,
# the sentence the S2.7a records do not cover). Remove when the CO lands.
FLAG015_DELIM = ("[Parked per FLAG-015 - hand-authored caution with no "
                 "record home yet; verbatim from app/world_manifest.py:]")
FLAG015_EVAGRIUS = (
    "Evagrius Ponticus is a contested figure (posthumously condemned as "
    "an Origenist over a century after this world's own close); Papnoute "
    "has no knowledge of that later condemnation and should not be "
    "expected to address it."
)


def build_cautions_text() -> str:
    """The runtime cautions block: every S2.7a caution record, whole, in
    record order, plus the FLAG-015 parked addendum."""
    core = load_records("world_core")["desertcore001"]
    parts = [c.strip() for c in core.get("cautions", [])]
    parts.append(f"{FLAG015_DELIM} {FLAG015_EVAGRIUS}")
    return "\n\n".join(parts) + "\n"


def build_brief() -> str:
    core = load_records("world_core")["desertcore001"]
    vp = load_records("voice_profile")["desertvoice001"]
    claims = load_records("contested_claim")
    gravities = load_records("gravity")

    parts = ["# World Facilitation Brief — Desert Monasticism",
             "",
             "Generated view (S5.5) — regenerate via "
             "`wrs/views/facilitation_brief.py`, never hand-edit.",
             "",
             "## Voice at the table", ""]
    parts.append(f"- Register: {vp['register_determination']['register']}")
    nm = vp["native_measure"]
    parts.append(f"- Native measure: ~{nm['typical_words']} words. {nm['note']}")
    parts.append("- Traits: " + "; ".join(t["trait"] for t in vp["trait_rubric"]))
    parts += ["", "## Pairing guidance (S2.7a records, evidence-linked)", ""]
    for pg in core.get("pairing_guidance", []):
        guidance = pg["guidance"]
        if "Donatism" in guidance:
            guidance += (" [Render note per CO-024/S2.7a review P3: name only "
                         "currently-active worlds as live partners - the "
                         "Imperial-Juridical pairing is the actionable one.]")
        parts.append(f"- {guidance}")
        parts.append(f"  - Evidence: {'; '.join(pg['evidence_links'])}")
    parts += ["", "## Cautions (S2.7a records; runtime-spoken block below "
                  "is generated from these same rows)", ""]
    for c in core.get("cautions", []):
        parts.append(f"- {c.strip()}")
    parts.append(f"- {FLAG015_DELIM} {FLAG015_EVAGRIUS}")
    parts += ["", "## Where this world genuinely diverges (table-question bank)", ""]
    for cid in sorted(claims):
        c = claims[cid]
        for dp in c.get("divergence_partners", []):
            parts.append(f"- vs **{dp['world_id']}** (on: {c['claim'][:80]}…): "
                         f"{dp['note']}")
    parts += ["", "## Gravity structure (for facilitator orientation)", ""]
    order = {"Primary": 0, "Supporting": 1, "Tensional": 2}
    for g in sorted(gravities.values(),
                    key=lambda g: (order.get(g.get("classification"), 3), g["id"])):
        parts.append(f"- {g['name']} — {g['classification']}")
    return "\n".join(parts) + "\n"


def main(argv: list[str]) -> int:
    check = "--check" in argv
    outputs = {
        DATA_DIR / "desert_Facilitation_Brief_generated.md": build_brief(),
        DATA_DIR / "facilitator_cautions_generated.txt": build_cautions_text(),
    }
    stale = []
    for path, text in outputs.items():
        if check:
            current = path.read_text(encoding="utf-8") if path.exists() else None
            if current != text:
                stale.append(path.name)
        else:
            path.write_text(text, encoding="utf-8", newline="\n")
            print(f"written: {path}")
    if check:
        if stale:
            print(f"STALE: {', '.join(stale)} - regenerate with "
                  "python wrs/views/facilitation_brief.py")
            return 1
        print("current: Brief + cautions byte-match regeneration")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
