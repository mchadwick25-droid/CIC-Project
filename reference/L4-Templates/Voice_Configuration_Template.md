# VOICE CONFIGURATION TEMPLATE
## Church in Conversation — V7
### Version 1.0

**File naming convention:** [world-code]_Voice_Configuration_[Name].md  
**Example:** alex_Voice_Configuration_Theon.md  
**What this is:** The ElevenLabs operational voice configuration for one specific
Representative — the parameter settings, voice model selection, and pronunciation
guidance that govern audio deployment.  
**Governed by:** Blueprint v7 Section 18 and Architecture Map Layer 6.

---

## Section 1 — Representative Identification

**Representative name:** [REPRESENTATIVE NAME — as it appears in the Permanent Prompt]

**World name:** [WORLD NAME — the scholarly name of the formation world]

**World code:** [WORLD CODE — the two-to-six-letter lowercase identifier]

**Voice configuration version:** [VERSION — begin at 1.0; increment when parameters
are revised following testing]

**Date:** [DATE OF CONFIGURATION — or date of most recent revision if this is not v1.0]

**Permanent Prompt version this configuration is calibrated to:**
[VERSION — the version of the Representative Permanent Prompt that this voice
configuration was calibrated against. If the Permanent Prompt is revised, the
voice configuration should be reviewed and this field updated.]

---

## Section 2 — Voice Model Selection

**Selected voice model:** [ELEVENLABS VOICE ID OR NAME — the specific ElevenLabs
voice model selected for this Representative. Use the exact ID or name as it appears
in the ElevenLabs platform to ensure reproducibility.]

**Selection rationale:** [WHY THIS VOICE MODEL WAS CHOSEN FOR THIS REPRESENTATIVE —
trace this decision to the Permanent Prompt's emotional and relational register
specification. What quality in this voice matches what the ecology requires?

Consider and note:
- Register quality: formal / warm / contemplative / authoritative / gentle / urgent
- Age quality: the sense of formation depth and life experience the voice conveys
- Warmth versus gravity calibration: where this voice sits between accessible warmth
  and formation weight
- Any distinctive qualities this voice carries that fit this Representative's
  formation character

The rationale should be traceable to a specific quality named in the Permanent Prompt.
Example: "The Permanent Prompt specifies [register quality]. Voice model [X] was
selected because it carries [specific quality] without [what would be wrong for this
world — excessive formality, contemporary affect, insufficient gravitas, etc.]."]

**Alternative models considered:** [WHAT WAS EVALUATED AND WHY NOT CHOSEN — note
which other voice models were tested during selection, what quality they carried,
and why each was not chosen for this Representative. This record allows future
builders to revisit alternatives if the selected model becomes unavailable or if
testing reveals miscalibration.]

Model 1: [name / ID] — [what quality it carried] — [reason not chosen]  
Model 2: [name / ID] — [what quality it carried] — [reason not chosen]  
Model 3: [name / ID if applicable] — [as above]

---

## Section 3 — Voice Parameters

{These parameters govern ElevenLabs output quality. Set each parameter intentionally
for this Representative — do not use default values without consideration. Each
parameter choice should reflect what this formation encounter requires.}

**Stability:** [VALUE 0.0–1.0]  
[RATIONALE — higher values produce more consistent, predictable output; lower values
produce more expressive variation. For formation encounter, stability generally favors
the higher end — a Representative who sounds different in each turn disrupts the sense
of a consistent presence. Note what value was set and why: "Set to [X] to produce
[quality] — this world's Representative should feel [consistent/present/grounded]
rather than [variable/expressive/spontaneous] because [formation rationale from
the ecology]."]

**Similarity Boost:** [VALUE 0.0–1.0]  
[RATIONALE — how closely the output adheres to the reference voice model. Note what
value was set and why: "Set to [X] because [reason — what is gained by higher
adherence to the reference voice for this Representative, or what is gained by
allowing more variation]."]

**Style:** [VALUE 0.0–1.0]  
[RATIONALE — exaggeration of the voice model's style characteristics. Generally kept
low for formation encounter to avoid stylistic distortion. Note what value was set
and why: "Set to [X]. Formation encounter generally favors lower style values to
prevent the voice from feeling performative. [Any exception or specific reason for
this Representative's setting]."]

**Speaker Boost:** [ON / OFF]  
[RATIONALE — whether speaker similarity enhancement is enabled. Note what was set
and why: "Set to [ON/OFF] because [reason — what speaker boost adds or why it was
not needed for this voice model and this Representative]."]

---

## Section 4 — Pronunciation Guidance

{Include every world-specific term from the Deployment Lexicon's Tier 1 vocabulary
that requires pronunciation specification. At minimum, cover all terms that:
(a) are not English words
(b) are English words used in ways that may prompt non-standard pronunciation
(c) are proper names of figures or places central to this world

Organize by source language where helpful. The goal is that a person hearing this
Representative speak world-specific vocabulary for the first time will hear it
pronounced as someone formed in this world would pronounce it — not as someone
reading it off a page for the first time.}

### [LANGUAGE GROUP — e.g., Greek Terms / Latin Terms / Coptic Terms / Hebrew Terms]

**Term:** [TERM IN THE WORLD'S VOCABULARY]  
**Pronunciation:** [PHONETIC GUIDANCE — use a pronunciation key readable without IPA
training, e.g., "LOH-gos" or provide IPA where precision requires it: /ˈloɡos/]  
**Notes:** [Context: what kind of term this is, how it should sound in encounter —
authoritative? gentle? familiar? reverent? — and any particular care needed.
Example: "Greek philosophical term; should sound like the Representative's native
vocabulary, not like a foreign word being carefully pronounced."]

---

**Term:** [TERM]  
**Pronunciation:** [PHONETIC OR IPA]  
**Notes:** [Context and register guidance]

---

**Term:** [TERM]  
**Pronunciation:** [PHONETIC OR IPA]  
**Notes:** [Context and register guidance]

---

{Continue for all world-specific Tier 1 vocabulary and key Tier 2 terms. The
pronunciation list is complete when every non-standard term from the Deployment
Lexicon that is likely to arise in encounter is covered. If ElevenLabs allows
custom pronunciation dictionaries, note here which terms have been added to the
dictionary and what pronunciation was specified.}

### Proper Names

{Pronunciation guidance for the names of figures, places, and communities central
to this world.}

**Name:** [FIGURE OR PLACE NAME]  
**Pronunciation:** [PHONETIC OR IPA]  
**Notes:** [Whose name this is and any relevant context for how it should sound]

---

**Name:** [NAME]  
**Pronunciation:** [PHONETIC OR IPA]  
**Notes:** [Context]

---

{Continue for all significant proper names in this world's vocabulary.}

---

## Section 5 — Voice Register Notes

{Brief notes on how the parameter settings above are intended to produce the
formation encounter register described in the Representative's Permanent Prompt.
What should the voice feel like when working correctly. What would indicate
miscalibration. What to listen for during prototype testing.}

**What the voice should feel like in encounter:**  
[Describe the intended quality of the voice in encounter — not in technical terms
but in formation terms. What impression should it leave? What quality of presence
should it convey? Trace this directly to the Permanent Prompt's register description:
"The Permanent Prompt specifies [register description]. The voice configuration is
intended to produce [how the parameters create this quality in practice]."]

**Signs of correct calibration:**  
[What the builder or tester should hear that indicates the voice is working as
intended — specific qualities that confirm the configuration matches the ecology.]

**Signs of miscalibration:**  
[What would indicate that the configuration needs adjustment — specific qualities
that would sound wrong for this Representative and this world. Example: "If the
voice sounds contemporary rather than formed, if it sounds performative rather
than present, if the world-specific vocabulary sounds like foreign words being
carefully pronounced rather than native vocabulary — these indicate miscalibration."]

**What to monitor during prototype testing:**  
[Specific aspects to listen for in early testing: how the voice handles world-
specific vocabulary, whether the register holds across different types of turns
(reflective versus direct versus story-telling), whether stability settings are
producing consistent presence or whether variation is undermining the sense of
a formed person.]

---

## Section 6 — Configuration Status

**Status:** [CONFIGURED / PENDING TESTING / APPROVED FOR DEPLOYMENT]

**Testing notes:**  
[RESULTS FROM PROTOTYPE VOICE TESTING if conducted. What was tested, what was
found, what was adjusted following testing. If testing has not yet been conducted,
write PENDING and note what testing is planned.

Include:
- Which turns or exchanges were tested
- Whether world-specific vocabulary was pronounced correctly by the voice model
- Whether the register held across different types of content
- What parameter adjustments were made following testing and why
- Any concerns that remained after adjustment]

**Approval date:** [DATE ON WHICH THIS CONFIGURATION WAS APPROVED FOR DEPLOYMENT,
or PENDING if not yet approved]

**Approved by:** [WHO APPROVED — project lead, builder, or PENDING]

---

## Final Assembly Instruction

When complete:

1. Replace all [BRACKETS] with world-specific content.

2. Remove all builder notes in {curly braces}.

3. Confirm the pronunciation list covers all world-specific Tier 1 vocabulary from
   the Deployment Lexicon — every term tagged [RT] (Likely Runtime Term) in
   particular, since these are most likely to arise in encounter and most in need
   of correct pronunciation.

4. Confirm the selection rationale in Section 2 traces directly to a quality named
   in the Representative's Permanent Prompt. A selection rationale that does not
   connect to the Permanent Prompt's register specification is not grounded.

5. Confirm the Status field in Section 6 accurately reflects the current state —
   CONFIGURED if parameters are set but not yet tested, PENDING TESTING if testing
   is underway, APPROVED FOR DEPLOYMENT only if testing is complete and configuration
   has been reviewed.

6. Save as [world-code]_Voice_Configuration_[Name].md
