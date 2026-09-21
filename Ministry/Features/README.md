# Ministry/Features — index

One folder per in-development, not-yet-core-app feature. Each folder holds
everything about that feature — design, decision log, launch prompts, exploration
code references — until a deliberate, logged step merges it into `cic-poc/`,
`cic-website/`, or `worlds/`. Check a feature's own `Integration-Notes.md` for
exactly what has and hasn't crossed that line.

| Feature | Status |
|---|---|
| [Atlas-World-Map](Atlas-World-Map/README.md) | Live on `cic-website/`; deeper app integration built, unmerged, gated on a Tier A/B scope decision |
| [Guided-Questions](Guided-Questions/README.md) | Content-complete, no UI code yet; original gating condition (Representative Modes landing) no longer applies — Representative-Modes was dropped 2026-09-21; re-scope this row when its next step is decided |
| [Hosted-Tour](Hosted-Tour/README.md) | Phase One demo built (Chloe), not integrated |
| [Full-UX-Design](Full-UX-Design/README.md) | V1.0 approved; visual identity live in `cic-poc/`/`cic-website/` |
| [Prototype-Testing](Prototype-Testing/README.md) | Active pilot program |
| [Website](Website/README.md) | Active; a held-back launch prompt awaits a world-build dependency |

Not here: Communication/Branding, Marketplace, Organization, Funding, and
Scholarly-Review stay as their own top-level Ministry domains — they're not scattered
the way these were, so they didn't need this treatment.

Dropped 2026-09-21 (Mark's own call): Brand-Messaging-Rework (done through
another process), Representative-Modes (4-lane rollout too complex, not
valued), Backend and Front-End-Integration-Strategy (both superseded — the
project now runs on Amazon Bedrock). Tour-Experience-Module-Phase2 moved to
`Archive/Tour-Experience-Module-Phase2/` — not dropped, just on hold for a
while and likely to come back as a different approach.
