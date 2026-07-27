"""S2.8 - World Facilitation Brief render (Pass 1 SS3.9's least-finished view).

Generated from voice_profile, contested_claim.divergence_partners,
gravities, and the S2.7a world_core records (pairing_guidance + cautions)
- populated, not empty, for the first time. Facilitator-facing: the etic
apparatus stays IN (this is the one view where citations belong).

Per the S2.7a review's P3: the boundary-energy pairing renders naming only
the Imperial-Juridical partner as its live example, with the Doc_07
characterization kept as the flagged exploration it is (Donatism/World #4
is not an active current-discipline world - the CO-024 rule).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from chunk_views import load_records, STAGING  # noqa: E402


def build_brief() -> str:
    core = load_records("world_core")["desertcore001"]
    vp = load_records("voice_profile")["desertvoice001"]
    claims = load_records("contested_claim")
    gravities = load_records("gravity")

    parts = ["# World Facilitation Brief — Desert Monasticism (generated view)",
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
    parts += ["", "## Cautions (S2.7a records)", ""]
    for c in core.get("cautions", []):
        parts.append(f"- {c}")
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


def main() -> None:
    STAGING.mkdir(parents=True, exist_ok=True)
    out = STAGING / "desert_Facilitation_Brief_generated.md"
    out.write_text(build_brief(), encoding="utf-8")
    print(f"staged Facilitation Brief -> {out}")


if __name__ == "__main__":
    main()
