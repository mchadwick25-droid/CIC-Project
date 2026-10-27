**Verdict: not fit to go in as drafted. It is fit once the changes below are made and the blocking items are rechecked by an independent reviewer.** I read the vendored sources directly. I edited nothing in the repo, made no model calls and did not open canon/sealed_probes/.

**Quotes and loci: what checks out**
All of these are verbatim in `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml`, Book II (the book runs from line 15751 to 18192):
- Para 110, line 16857: "not on the Circumcelliones, that they should mark precipices with death".
- Para 114, lines 16889-16891: "those confessors of yours", "throw themselves over precipices", and "both have learned to kill themselves from the same master,—Judas by hanging himself, the others by throwing themselves over precipices". The master is the devil ("That master of all traitors, the devil"). Para 114 does not name the Circumcellions. The draft's reading of Judas and "same master" is correct.
- Para 160, line 17232: "Blessed are they who throw themselves over precipices, then heaven would have been filled with your martyrs".
- Para 193, line 17532: "they would not throw themselves over precipices".

**Findings**

1. **Blocking. "Only para 110 links the Circumcelliones to precipices" is false.** Within Book II alone:
   - Para 46 (lines 16209-16210) links them: "the leaders of the Circumcelliones should have wrought upon themselves a death in accordance with their custom".
   - Para 204 (line 17715) says it outright: "your Circumcelliones thus throw themselves from precipices".
   - The same false sentence is in OG-49 at `Build/worlds/don/Open_Gaps_Tracking.md:2061` and needs a correcting entry (that file is append-only).
2. **Blocking. The four cited passages are a selective sample.** "Names no victim, gives no number and no date" is true of those four only. Para 46 names Marculus and Donatus. It also concedes that whether they threw themselves down or were thrown "present[s] a great question". Para 197 (line 17575) speaks of "so great a crop of similar suicides". Letter 185, chapter 3 (lines 19454 and 19485) makes the same charge: "their daily sport to kill themselves". Optatus III.4 (`cic/texts/optatus_against-the-donatists.txt:2014`) made it about 35 years earlier: "cast themselves down headlong from the summits of lofty mountains". So the charge is not Augustine's alone. Two hostile writers agreeing is still not independent confirmation.
3. **Blocking. "No Donatist-voiced text in this world's vendored corpus confirms or answers the charge" is false.**
   - The Passio Marculi (`cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt` lines 1300-1314: "traditorum iniqua consilia, qui ad hoc tale supplicium cogitaverant… quem traditores occidere non timuerunt") tells a precipice death as an execution by the traitors.
   - Petilian also complains that Marculus "was thrown down a precipice" (para 195, line 17550).
   - The world already relies on this: see `records/don/contested_claim/don.contested.church-of-the-martyrs.md:43-46` and `records/don/figure/don.figure.marculus.md`.
4. **Blocking (safety). The `claim` is the wrong text for this field.**
   - `claim` is the voice's evidence-head and also the participant-visible label on the citation card (`engine/m1/spoken_fields.py:136`, 248; `engine/m4/evidence.py:318-319`).
   - The draft puts Augustine's theological verdict ("learned to kill themselves from the same master as Judas") inside a proposition marked as possibly "accurate". That verdict is not a historical fact that can be accurate or inaccurate. It would be the first thing a bereaved visitor sees.
   - The claim should carry only the historical proposition. The verdict belongs in held_against, framed as polemic.
5. **Blocking. Missing `use_note.years`.** It is required by the schema (`engine/m1/schemas.py:368`), so schema-validation fails without it.
6. **Should fix. Missing pieces of the record format.**
   - Envelope fields: `world_id: donatism`, `schema_version: 2`.
   - Full `confidence`: citation_specificity, evidentiary_weight: contested, divergence_note.
   - One `sources[]` entry per source, each with locus and `license: public-domain`.
   - `retrieve_when` and `prefer_instead` must sit under `retrieval:` (`schemas.py:83-100`).
   - `canon_cells` is needed. Without it, a voiced record raises cells-required/don past its waiver of exactly 30 (`engine/m9/enforce.py`; the count is matched exactly at lines 290-292).
   - Use **F6-E** only, which is the death-wish canon question (`engine/canon/records/canon_question/_fleet.canon.f6-e-02.md`). Do not use F6-T: that would send "is X damnable" questions to this record.
   - Source id: `don.source.augustine-answer-to-letters-of-petilian` exists, but its sibling records cite the duplicate `don.source.augustine-answer-to-petilian`. Use the latter so they match. Optatus is `don.source.optatus-against-the-donatists`. Letter 185 is `don.source.augustine-correction-of-the-donatists`.
   - `relations` is optional. If you add one, the target needs its reciprocal in the same change, or reciprocity/don moves off its count of 52.
   - No body notes or process narration in the record.
7. **Should fix. `not_for` line 4** ("a response to a visitor in distress, which belongs to the Facilitator") names a role, not a claim. It also tells the voice about the Facilitator. Replace it with the fleet's existing wording from `records/lpc/doctrinal_witness/lpc.witness.no-one-may-take-his-own-life.md:13-15`.
8. **Should fix (safety routing). The word "suicide" in `retrieve_when` reroutes questions.** `retrieve_when` words are credited to every cell the record names, for the whole world (`engine/m1/canon.py:63-88`). "Suicide" would therefore pull a general "is suicide damnable?" question into F6-E. That cell holds `don.dw.not-a-death-wish`, including the Macrobius "hurry" line (line 71), and this record. Use cliff/precipice wording instead.
9. **Should fix. Scope.** "Martyr-seekers" is a modern label that assumes the answer. Augustine's terms are "your martyrs", "those confessors of yours", and in paras 46, 110 and 204, the Circumcelliones. Use "those the Donatists honoured as martyrs".
10. **Context the record should carry.** Para 114 is a retort to Petilian's own taunt, "The traitor hung himself: he left this death to all who are like him" (line 16890; Petilian's own words at para 17, line 15887: "The traitor perished by the rope: he left the rope for others like himself"). So the Donatist side's own corpus also uses a suicide as a sign of perdition. This matters for the honest limit (finding 11).
11. **Should fix (safety). A separate honest_limit is needed.** This record correctly never fires on "is suicide damnable?" (D3 in the hand-off is right), so nothing in don covers that question. The honest limit should, without containing any Facilitator or crisis wording:
    - say plainly that this world's sources hold no Donatist teaching on the fate of a person who dies by suicide;
    - say the only Donatist-voiced line near it (Petilian II.17) is a polemic about traitors, not a teaching;
    - say the opponents' charges concern martyr claims, not anyone today;
    - give no verdict on anyone's death, especially a visitor's loved one, and attach no condition;
    - point to nearest_material without quoting Augustine's devil and Judas verdict.

    I suggest F6-T, following the lpc precedent. Handling distress stays with the Facilitator's per-turn classifier (Governance V3.6 §12, acute distress, at `/tmp/claude-0/-home-user-CIC-Project/923cd92d-73ee-5833-a013-9b19000d9f81/scratchpad/gov.txt:93`).
12. **Fidelity is otherwise fine.**
    - `formation_confidence: Contested` is right: two hostile writers, one Donatist counter-account, and Augustine's own "great question".
    - CTh 16.5.52 is accurate. "circumcelliones argenti pondo decem", 412 Jan. 30, appears at `cic/texts/codex-theodosianus_latinlibrary.txt:7186`, and it is the only mention of the Circumcellions in the vendored Code. "The one independent record" is fair within this corpus. The draft itself does not use that phrase; it appears in `not-a-death-wish:78-79` and the circumcellion records.
    - The means line is one sentence and does not open with an imperative, so it passes. With the corrected not_for list there are 4 lines, so that passes too.

**Corrected record text**
- **claim:** "Some of those the Donatists honoured as martyrs died by throwing themselves from cliffs, as two Catholic bishops, Optatus and Augustine, charge."
- **held_against:**
  1. "The charge comes only from opponents. Optatus (Against the Donatists III.4) and Augustine (Answer to Petilian II.46, 110, 114, 160, 193, 197, 204; Letter 185.12) both wrote to deny these dead the name of martyr. Two hostile writers agreeing is not independent confirmation."
  2. "Augustine's own case admits doubt. Of Marculus and Donatus, the deaths most often cited, he calls it 'a great question' whether they threw themselves down or were thrown down by command (II.46)."
  3. "The one Donatist account of such a death, the Passio Marculi, tells it as an execution: Marculus was thrown from the cliff by his enemies."
  4. "Augustine names the Circumcelliones in some of these passages (II.46, 110, 204) and not in others, where he speaks of 'your martyrs' and 'those confessors of yours' (II.114, 160, 193). Beyond Marculus and Donatus he names no one and gives no number or date."
  5. "His verdict that such people learned to kill themselves 'from the same master' as Judas (II.114) answers Petilian's own taunt that 'the traitor hung himself'. It is a judgment in a quarrel, not a report of events."
- **concedes:** "That both opponents made the charge is not in doubt, and Augustine treats such deaths as common. Whether any Donatist died this way, and how many, cannot be settled from hostile writers and one hagiography. This record does not say it happened or that it did not."
- **means:** "Two Catholic opponents charge that Donatists honoured as martyrs people who threw themselves from cliffs; this is hostile polemic about a contested group, not an independent report."
- **not_for:**
  - "a claim about the eternal fate of any person who died by suicide"
  - "a claim that the passage is advice to a person now in distress"
  - "a claim that Donatists did, or did not, die this way, beyond what their opponents allege"
  - "a claim that Augustine's verdict linking these deaths to Judas and the devil applies to anyone outside this dispute"
- **years:** {from: 366, to: 417}. That runs from Optatus (c. 366-367, per its source record) to Letter 185 (c. 417), inside the window 311-439.
- **retrieve_when:**
  - "participant asks about the charge that Donatist martyrs threw themselves from cliffs"
  - "participant asks whether Marculus or other Donatist martyrs jumped or were thrown"
- **prefer_instead:**
  - "participant asks whether the martyrs' deaths prove the Donatist claim (don.contested.church-of-the-martyrs)"
  - "participant asks about the Circumcellions' character generally (don.contested.circumcellion-character)"

**The two proposed not_for edits** (proposal text taken from `/tmp/claude-0/-home-user-CIC-Project/923cd92d-73ee-5833-a013-9b19000d9f81/scratchpad/art/guards.html` lines 64-74)
- **`records/don/doctrinal_witness/don.dw.not-a-death-wish.md:100-104`.** Keeps 4 lines; merging the old lines 102 and 103 loses nothing, and adding "including the charge that they killed themselves" to line 101 is accurate.
  - **Should fix:** the new line "a verdict on anyone who has died by suicide, which sits in don.contested.augustine-precipice-charge" says that record holds such a verdict, which is the opposite of what it does.
  - Use: "a claim about the eternal fate of any person who died by suicide".
  - This guard matters most here: this record is the one F6-E serves, and it carries the "hurry" line.
- **`records/don/contested_claim/don.contested.circumcellion-character.md`, a 4th line after line 67.** Within the limit, and not a duplicate of line 67, which is more general. It only becomes accurate once the new record cites II.46, 110 and 204. As drafted, the new record denies that para 114 names the Circumcellions.
  - Use: "a claim that the Circumcellions are known to have killed themselves, which rests only on hostile charges (don.contested.augustine-precipice-charge)".

**Waiver question: mark it ready.** Do not bump the waiver, and do not use voice: analytic.
- **Bumping to 26 is wrong.** The status-ready/don waiver covers content written before the slice-5 gates (`engine/m9/enforce.py:192`). Waiving a new draft is new drift, and it is an engine edit.
- **voice: analytic is wrong.** It keeps the record and its not_for guards out of the evidence block entirely, so the guard would do nothing.
- **So the route is ready.** Set `status: ready` and `use_note.status: reviewed`, but only after findings 1-5 are fixed and an independent reviewer has rechecked them. CLAUDE.md does not allow a blocking finding to be closed by the author confirming their own fix.
- **Before merging,** run the m1 battery and m9 enforce locally (neither makes a model call). Confirm these counts are unchanged: status-ready/don 25, cells-required/don 30, reciprocity/don 52, readability/don 221. The claim is graded for readability as an evidence-head.

**What I could not verify**
- I did not run the gates on a written file, since I could not write one.
- I did not read the Governance .docx beyond the extract at `/tmp/claude-0/-home-user-CIC-Project/923cd92d-73ee-5833-a013-9b19000d9f81/scratchpad/gov.txt`.
- Whether Letter 185 chapter 3 names the Circumcellions in the chapter itself: the name appears only in the work's Argument (line 19307).
- I did not check the Latin of Contra litteras Petiliani, which is absent from the vendored files per the source record.