# syr — Legacy participant-facing card (pre-redesign reference)

**Not part of the current M1/M2 record-native pipeline.** This is the participant-facing world/Representative copy from the **old, pre-redesign proof-of-concept app** (`cic-poc/backend/app/world_manifest.py`, on `build/phase-1`, lines 146-187 as of this branch's fetch). Mark confirmed this was already approved and shown to participants before this rebuild. It predates and is architecturally separate from the current spec's doorway build (Program Spec SS6, compiled from M2 at step 6-8) — logged here so step 5 (Representative voice build) and step 7.5/8 (doorway) start from it rather than rediscovering it, without being folded into this build's content-canon records now, since voice/doorway work is explicitly out of scope for this round.

## The entry, verbatim

```python
WorldManifestEntry(
    world_id="syriac-edessa-nisibis",
    world_name="Syriac Christianity",
    period="200–410 CE",
    region="Edessa & Nisibis",
    world_description=(
        "Edessa and Nisibis, 200 to 410 CE — in what is now southeastern Turkey — a "
        "community shaped by persecution under Persian rule, holding together through covenant vows "
        "and typological reading of Scripture. Their bishops were martyred, their see stood empty "
        "for decades, yet their teaching endured — carried in the hymns of Ephrem, the "
        "demonstrations of Aphrahat, and the witness of Jacob of Nisibis. Richest in the formal "
        "vocabulary, institutions, and disputes of a demanding covenant tradition — thinner on the "
        "everyday, personal texture of an ordinary member's life, since what survives is mostly "
        "doctrinal and institutional rather than personal."
    ),
    color="#b45309",
    data_dir_name="syriac_world",
    permanent_prompt_filename="syr_Representative_Permanent_Prompt_Yausep.txt",
    world_capsule_filename="syr_World_Capsule_Core.md",
    vector_store_name="syriac",
    representative_id="mar-yausep",
    representative_message_name="mar_yausep",
    representative_name="Mar Yausep",
    representative_title="Teacher of the Covenant Order",
    representative_description=(
        "Is a voice of Syriac Christianity, speaking as a teacher of the covenant order — "
        "formed within the community that reads Scripture by raza, the hidden truth bound within "
        "the old stories, keeps the qyama vow, and gathers under one harmonized Gospel. He carries "
        "this tradition's whole life, from Edessa to the Persian towns beyond."
    ),
    representative_intro=(
        "a teacher from the Syriac Christian tradition of Edessa and Nisibis, speaking from the "
        "period of 200-410 CE"
    ),
    facilitator_cautions=(
        "This world's later descendants include the Church of the East, Syriac Orthodox, and "
        "Chaldean Catholic communities - a participant from these backgrounds may experience this "
        "as living heritage rather than pure historical encounter. Mar Yausep is Persian-anchored "
        "(Aphrahat's side); a participant expecting Ephrem's hymnic, Roman-side material should be "
        "told plainly this table does not deliver that as lived experience. Aphrahat's own "
        "anti-Jewish polemical material is this world's most sensitive register and needs attentive "
        "handling. This Representative was deliberately built with real pastoral warmth, which the "
        "construction record itself flags as a plausible dependency/confidant-substitution "
        "amplifier - watch for escalating, exclusive-attachment patterns across sessions, not only "
        "single-turn distress."
    ),
),
```

## What this settles and what it doesn't

**Settles, consistent with the decision log already carried in this build:**
- Name and role: Mar Yausep, Teacher of the Covenant Order — matches the registry entry `records/worlds.yaml` (confirmed by Mark 2026-08-22).
- **The Representative's anchor is Persian (Aphrahat's side)**, not Roman/Edessene (Ephrem's side) — stated explicitly here for the first time in this build's own materials. This is new, useful information for step 5a's identity-emergence write-up: it means the voice build should NOT present Ephrem's hymnic corpus or Roman-side lived experience as this Representative's own, only as material the Representative knows and can speak of at a remove (comparable to how a Persian-side figure would relate to a Roman-side contemporary's writings). Doc_01's strand-singular finding still holds at the world-content level (this build's content canon draws on both sides evenly); the anchor choice is a voice-layer decision on top of that content, not a re-litigation of strand-singular.
- Safety-relevant: the anti-Jewish polemical material's sensitivity and a flagged pastoral-warmth/dependency-amplifier risk — both worth carrying into step 5's craft record and M5's safety design when that work begins.

**Does not settle, and is not being aligned now:**
- The exact wording of `world_core.thinness` (`records/syr/world_core/syr.core.syriac.md`) differs from this card's own thinness phrasing. Both are accurate to the same underlying facts at different altitudes (mine names specific gaps — ordinary believers, women's own words, the 373-410 years; this card generalizes to "everyday, personal texture... doctrinal and institutional rather than personal"). Per the spec, the compiled card's own thinness statement is meant to derive FROM `world_core.thinness` at compile time (Program Spec SS6) — so if this legacy wording is wanted verbatim or near-verbatim on the new card, that is a step-6+ compile/doorway decision, not a content-canon edit, and should be made then, with the actual compiler and card-generation code in view, not guessed at now.
