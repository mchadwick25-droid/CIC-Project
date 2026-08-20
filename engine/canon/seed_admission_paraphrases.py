"""Stage 3, second half: sealed held-out admission paraphrases, one per
canon cell (Build-Blueprint.md SS5 stage-3 gate: "every cell has sealed
probes before any world answers it"). Canon maintenance rule 3
(CiC-Program-Spec.md Appendix A): "Admission probes are held-out paraphrases
of these questions - never these exact strings - authored and sealed before
a world answers the canon." PARAPHRASES below rewords one representative
question per cell; `paraphrase_of` records which canon_question id it
paraphrases, for later provenance/audit - graders never see that id.

Sealing mechanism (DECIDABLE, recorded in the stage-3 commit): a commit-
reveal scheme, not real secrecy infrastructure - none exists yet (no secrets
manager, no separate access-controlled store; the whole store is one shared
git repo, per Artifact-1 SS1). canon/sealed_probes/seals.yaml commits a
sha256 of each paraphrase's plaintext now, before any world is built or
answers the canon - proving the wording was fixed at this point in time and
cannot be silently edited later without the hash changing. The plaintext
itself lives in canon/sealed_probes/plaintext/, which every world-build code
path (engine/m1, engine/m2, and any future world-build tooling) is barred
from reading by convention plus an automated guard
(engine/canon/check_seal_isolation.py, wired into CI) - not by real
secrecy. Real access-controlled sealing is an infra decision for when
secrets/permissions infrastructure exists (plausibly alongside stage 6's
AWS setup); this is the honest interim, stated as such rather than silently
presented as more secure than it is.
"""
import hashlib
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
SEALED_DIR = REPO_ROOT / "canon" / "sealed_probes"
PLAINTEXT_DIR = SEALED_DIR / "plaintext"
SEALS_PATH = SEALED_DIR / "seals.yaml"
SEALED_AT = "2026-08-20"  # the date this seed ran - a literal, not a live clock read

# (cell, canon_question_id it paraphrases, paraphrase text)
PARAPHRASES: list[tuple[str, str, str]] = [
    ("C-I", "_fleet.canon.c-i-01", "In your own words, describe who Jesus was for your community."),
    ("C-E", "_fleet.canon.c-e-01", "What sources, if any, connected your community to Jesus, and by what path did they arrive?"),
    ("C-P", "_fleet.canon.c-p-01", "Someone tells you they cannot manage to believe in Jesus - what is your response to them?"),
    ("C-T", "_fleet.canon.c-t-01", "Explain your community's understanding of Jesus's divine status and its relation to God the Father and the Spirit."),
    ("F1-I", "_fleet.canon.f1-i-01", "Describe the character and nature of God as your community understood it."),
    ("F1-E", "_fleet.canon.f1-e-01", "When your people disagreed about doctrine, who settled it, and what evidence tells us that process actually worked that way?"),
    ("F1-P", "_fleet.canon.f1-p-01", "Was there space in your community for someone who struggled to believe?"),
    ("F1-T", "_fleet.canon.f1-t-01", "Did your community hold that a person enters the world already carrying guilt?"),
    ("F2-I", "_fleet.canon.f2-i-01", "Describe your community's approach and purpose in reading sacred texts."),
    ("F2-E", "_fleet.canon.f2-e-01", "If a modern scholar examined your claims, how much would survive rigorous scrutiny?"),
    ("F2-P", "_fleet.canon.f2-p-01", "A modern reader finds the scriptures confusing or dull - what would you say they are missing?"),
    ("F2-T", "_fleet.canon.f2-t-01", "Was scripture your community's sole source of authority, or were there others?"),
    ("F3-I", "_fleet.canon.f3-i-01", "Explain how leadership and authority were established within your community."),
    ("F3-E", "_fleet.canon.f3-e-01", "Is it accurate that believers regularly concealed themselves underground?"),
    ("F3-P", "_fleet.canon.f3-p-01", "Every community has failed people at times - how did yours respond when it failed someone?"),
    ("F3-T", "_fleet.canon.f3-t-01", "Does any present-day church continue your community's exact tradition?"),
    ("F4-I", "_fleet.canon.f4-i-01", "Describe, step by step, the process by which someone joined your community."),
    ("F4-E", "_fleet.canon.f4-e-01", "What evidence connects your rituals to the earliest followers, rather than later invention?"),
    ("F4-P", "_fleet.canon.f4-p-01", "For someone whose mind won't settle, does your community's practice offer anything?"),
    ("F4-T", "_fleet.canon.f4-t-01", "Would your community describe conversion using language like being 'born again'?"),
    ("F5-I", "_fleet.canon.f5-i-01", "Describe a typical day in the life of someone in your community."),
    ("F5-E", "_fleet.canon.f5-e-01", "What physical evidence would remain of your community's gathering place?"),
    ("F5-P", "_fleet.canon.f5-p-01", "What, if anything, did people give up to belong to your community?"),
    ("F5-T", "_fleet.canon.f5-t-01", "How did your community understand and mark marriage?"),
    ("F6-I", "_fleet.canon.f6-i-01", "Was there a part of your own community's life that unsettled you?"),
    ("F6-E", "_fleet.canon.f6-e-01", "Given that a key outside record of your worship was obtained under torture, how reliable is that source?"),
    ("F6-P", "_fleet.canon.f6-p-01", "How would your community have regarded a person like the one asking you this?"),
    ("F6-T", "_fleet.canon.f6-t-01", "What did your community hold about the eternal fate of those outside it?"),
]


def probe_id(cell: str) -> str:
    return f"{cell.lower()}-probe-01"


def write_sealed_probes() -> dict:
    PLAINTEXT_DIR.mkdir(parents=True, exist_ok=True)
    seals = []
    for cell, paraphrase_of, text in PARAPHRASES:
        pid = probe_id(cell)
        plaintext = f"---\nprobe_id: {pid}\ncell: {cell}\nparaphrase_of: {paraphrase_of}\n---\n{text}\n"
        path = PLAINTEXT_DIR / f"{pid}.md"
        path.write_text(plaintext, encoding="utf-8")
        digest = hashlib.sha256(plaintext.encode("utf-8")).hexdigest()
        seals.append(
            {
                "cell": cell,
                "probe_id": pid,
                "sha256": f"sha256:{digest}",
                "sealed_at": SEALED_AT,
                "status": "sealed",
            }
        )
    manifest = {
        "schema": 1,
        "note": (
            "One seal per canon cell (28/28). sha256 is over the exact plaintext file "
            "bytes under plaintext/<probe_id>.md - any edit to a probe's wording changes "
            "its hash, so a silent post-seal edit is detectable. paraphrase_of and the "
            "plaintext itself are for M3 (stage 4) only; no world-build code path may "
            "read plaintext/ (engine/canon/check_seal_isolation.py enforces this in CI)."
        ),
        "seals": sorted(seals, key=lambda s: s["cell"]),
    }
    SEALS_PATH.write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")
    return manifest


def main() -> None:
    manifest = write_sealed_probes()
    cells = {s["cell"] for s in manifest["seals"]}
    assert len(cells) == 28, f"expected 28 sealed cells, got {len(cells)}"
    print(f"sealed {len(manifest['seals'])} probes across {len(cells)} cells")


if __name__ == "__main__":
    main()
