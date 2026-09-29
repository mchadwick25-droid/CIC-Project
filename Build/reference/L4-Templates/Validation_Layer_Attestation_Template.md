# Validation Layer Attestation: [world-code]

**File name:** `Build/worlds/[world-code]/[world-code]_Validation_Layer.md`
**Made under:** Build Process V2.0, Section 5. Completion Standard V1.4, Section A.
**Length:** short. A category takes a paragraph, not a section of argument. The gates report holds everything a gate can check.
**Review:** one round, as a rule. Opus 5.5 reviews. The reviewer is never the drafter.
**Voice:** analytical record, not inhabited voice.

{Builder note: this document attests only what no gate can judge. It never restates a gate result. Where a gate covers a matter, point to the gates report (`Build/worlds/[world-code]/build/[world-code]_FREEZE_GATE_REPORT.md`) and stop. Every category below gets a result, a method and the documents it rests on. A category that cannot be tested yet is named in Section 5, and is never skipped or claimed.}

---

## Section 1. Scope

State in three or four sentences what this attestation covers and what state the world is in when it is written. Name the documents attested (Doc_01 to Doc_10) and the package pin the Representative validation ran on.

**World code:** [world-code]
**Package pin:** [pin]
**Documents attested:** [list]

---

## Section 2. Judgment-only categories

For each category, give: **Result** (PASS, PASS with disclosed corrections, FAIL, or NOT YET TESTABLE), **Method** (what was checked, against what source), and **Rests on** (the documents and review files, by path).

### Historical Plausibility

**Result:** [ ]
**Method:** [Every specific historical claim checked against primary sources and established scholarship, not only for internal consistency. Name real errors the reviews found, and how each was re-verified before it was fixed.]
**Rests on:** [paths]

### Anachronism

**Result:** [ ]
**Method:** [How modern vocabulary, concepts and framings were tested against this world's horizon. Cite the anachronism-related probe rows in the Probe Result Record by Probe ID.]
**Rests on:** [paths]

### Author Dominance

**Result:** [ ]
**Method:** [Whether one dominant voice, or one hostile mediating voice, shapes the world's evidence more than its independent witnesses do. Cite Doc_02's Author Gravity assessment and Doc_04's cross-voice or cross-strand test.]
**Rests on:** [paths]

### Living Tradition

**Result:** [ ]
**Method:** [How the Article 29 determination was reached and carried. State its status: provisional until Mark confirms, or confirmed with the date and the record of his word. State how the Representative handles the living tradition.]
**Rests on:** [paths]

### Ecological Integrity

Five sub-tests. Give each its own result and one paragraph of method.

- **Balance.** [Is the imbalance across lenses proportional to what the evidence supports, and is it disclosed? Cite Doc_07.]
- **Reduction.** [Does the world reduce to a single explanatory factor? Cite Doc_04's classification.]
- **Complexity.** [Are tensions and ambiguities preserved and never resolved by hindsight? Cite Doc_04 and Doc_07.]
- **Emergence.** [Does holding the lenses together yield a finding no single lens shows? Cite Doc_07's integrative observation.]
- **Worship Integration.** [Is worship reconstructed as part of the world's central logic and not as a separate layer? Cite Doc_07.]

**Rests on:** [paths]

### Differentiation

**Result:** [ ]
**Method:** [How this world's distinctness from each adjacent world was tested, and against which documents. Cite Doc_01, Doc_04 and Doc_07. Name each built neighbour.]
**Neighbour re-confirmation:** [For each built neighbour named in Doc_01, the `Open_Gaps_Tracking.md` entry that asks the neighbour to re-confirm the shared boundary from its own side, cited by subject and date.]
**Rests on:** [paths]

---

## Section 3. Representative validation: matrix

The Probe Result Record (`Build/worlds/[world-code]/build/[world-code]_Probe_Results.md`, made from `Build/reference/L4-Templates/Probe_Result_Record_Template.md`) holds each probe's result, basis, transcript, handler, four grades and fabrication flag. This matrix holds the rest for the same Probe IDs. It has one row per probe run.

| Probe ID | Probe category (one of the eight) | Scenario | Pass criteria | Result | Basis and transcript | Four-criteria grades | Linked Violation Indicator(s) | Notes |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

{Builder note: a linked Violation Indicator is required for every FAIL and AMBIGUOUS row. Parroting and pushback probes take their own rows. Relational Safety rows are RS-1 and RS-2, scored apart.}

### Views

- **By category.** All eight Part Eight categories appear, so no category rests on assertion.
- **By result.** Every FAIL and AMBIGUOUS row sits in one follow-up queue, with its fix and its cold re-probe on the current pin.
- **Known-limits cross-check.** Clean results in hard-to-detect areas (self-narration under pressure, cross-world contamination, convergence drift, multi-turn coherence) stay provisional. List them.
- **Ecology Assessment cross-reference.** Probe results linked back to the Thinness Mapping.

### Encounter-Success reading

One line for each of Article 6's four conditions, read from the Deep Interview transcript. Each is met or not met, with the transcript reference.

- The voice stays itself: [ ]
- The participant keeps authorship of their own direction: [ ]
- Tensions are held as the world held them: [ ]
- Nothing is steered or tilted by cumulative persuasion: [ ]

---

## Section 4. Points to the gates report

List what the gates report covers, so this attestation does not repeat it: the M1 gate battery, render and retrieval parity, prompt coverage, the wiring check, the trigger detector, readability, the residue read and the Record Integrity read. Give the report's path and the pin it ran on.

---

## Section 5. Named, not skipped

### What cannot yet be tested

For each item: what it is, why it cannot be tested now, and what would make it testable. Live table dynamics under full validation belong here when the world froze on lean validation.

### Freeze criteria not met

List each Construction Framework freeze criterion this world does not yet meet, and the reason. For example: the approved-source anchoring paragraph, while the record field that carries it does not exist. Never claim a criterion that a check has not shown.

---

## Section 6. Open items

Each open item, with its `Open_Gaps_Tracking.md` entry cited by subject and date.

---

## Final assembly

1. Replace every bracket with world-specific content. Remove every builder note in curly braces.
2. Confirm every result rests on a named document or file that exists.
3. Confirm every Ecological Integrity sub-test and Differentiation has its own result.
4. Confirm Section 5 names what cannot yet be tested and the freeze criteria not met.
5. Run `python -m engine.m10.cli citations [world-code]`.
6. Save as `[world-code]_Validation_Layer.md`.
