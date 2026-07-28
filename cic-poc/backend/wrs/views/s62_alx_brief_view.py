"""S6.2 S2.8-equivalent - Alexandria World Facilitation Brief render
(staged; Desert brief_view.py precedent - populated from the S2.7a
records, not empty). Facilitator-facing: the etic apparatus stays IN
(this is the one view where citations belong). The S5.5-class deployed
render (facilitation_brief.py is desert-hardcoded) is a later step.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from s62_alx_chunk_views import load_records, STAGING  # noqa: E402


def build_brief() -> str:
    core = load_records("world_core")["alexcore001"][0]
    vp = load_records("voice_profile")["alexvoice001"][0]
    claims = {rid: rec for rid, (rec, _b)
              in load_records("contested_claim").items()}
    gravities = {rid: rec for rid, (rec, _b) in load_records("gravity").items()}

    parts = ["# World Facilitation Brief — Alexandria Catechetical (generated view)",
             "\n## The voice at the table\n"]
    ident = vp.get("identity", {})
    parts.append(f"**{ident.get('persona_name')}** — {ident.get('role_label')}")
    parts.append(f"\nRegister: {vp['register_determination']['register']}")
    parts.append(f"\nTypical measure: ~{vp['native_measure']['typical_words']} "
                 f"words. {vp['native_measure']['note']}")

    parts.append("\n## The world's confirmed gravities\n")
    order = {"Primary": 0, "Supporting": 1, "Tensional": 2}
    for g in sorted((g for g in gravities.values()
                     if g["classification"] in order),
                    key=lambda g: (order[g["classification"]], g["id"])):
        parts.append(f"- **{g['name']}** — {g['classification']}")

    parts.append("\n## Pairing guidance (S2.7a records, evidence-linked)\n")
    for pg in core.get("pairing_guidance", []):
        parts.append(f"- {pg['guidance']}")
        parts.append(f"  - *evidence:* {'; '.join(pg['evidence_links'])}")

    parts.append("\n## Cautions (record-derived)\n")
    for c in core.get("cautions", []):
        parts.append(f"- {c}")

    parts.append("\n## Held positions at the table (contested_claim set)\n")
    for cid in sorted(claims):
        c = claims[cid]
        parts.append(f"### {cid}\n")
        parts.append(f"**Held:** {c['claim']}\n")
        parts.append(f"**Concedes:** {c['concedes']}\n")
        for dp in c.get("divergence_partners", []):
            ref = f" → `{dp['partner_claim_id']}`" if dp.get("partner_claim_id") else ""
            parts.append(f"- vs **{dp['world_id']}**{ref}: {dp['note']}")
        parts.append("")
    return "\n".join(parts) + "\n"


def main():
    STAGING.mkdir(parents=True, exist_ok=True)
    out = STAGING / "alex_Facilitation_Brief_generated.md"
    out.write_text(build_brief(), encoding="utf-8", newline="\n")
    print(f"staged: {out.name} ({len(out.read_text(encoding='utf-8').splitlines())} lines)")


if __name__ == "__main__":
    main()
