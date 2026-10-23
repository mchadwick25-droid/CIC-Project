Review round 3, ijc record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: BLOCKING

Scope: targeted recheck of the uncommitted `use_note.means` pass (`git diff`, 9 files under records/ijc), as described in /tmp/claude-0/s/changes_means.md. The scope rule from the project lead was applied: change `means` only where it contradicts the record's corrected spoken fields or its source, and make it say what the corrected field says in one plain sentence. Each of the 9 edits was checked against the record's current spoken fields, its formation_confidence, and the vendored text in cic/texts/ by grep (npnf101 Conf. IX.7 l.13741-13776; npnf210 Sermo c. Aux. 36 l.42659-42664 and argument l.42094; npnf202 Sozomen VII.25 l.42146-42206; npnf203 Theodoret V.17 from l.16499; npnf201 VC IV.61-62 l.6766, ~67742-67790). The `means` of the other 46 non-quote records were then read against this pass's corrected fields (`git diff origin/main HEAD -- records/ijc` and /tmp/claude-0/s/changes_*.md). The 38 quote records were not re-read in this round.

Mechanical checks, all clean:
- Only `use_note.means` lines changed: `git diff -U0` shows 9 removed and 9 added lines, all `means:`. No not_for, years or other field was touched.
- All records load. `load_world_records('ijc')` returns 186 records.

## Findings

1. **ijc.term.imperator-intra-ecclesiam, use_note.means** - BLOCKING (misquote of a formula this pass corrected)
   - Current: `"The emperor is within the Church, not over it" is what Ambrose said in the 386 basilica crisis, calling the emperor a son of the Church.`
   - The rest of the sentence is right. Sermo c. Aux. 36 (npnf210 l.42660-42664) has "the Emperor should be called the son of the Church" and the 386 setting. The discipline and altar claim has gone, as it should.
   - However, the quoted formula still says "not over it". The vendored sentence is "For the Emperor is within the Church, not above it" (l.42663-42664). This pass changed plain_meaning from "not over the Church" to "not above it" (changes_fig_term.md), and quick_meaning also says "above". This edit rewrote the sentence but kept the pre-correction wording inside quotation marks.
   - Suggested: `"The emperor is within the Church, not above it" is what Ambrose said in the 386 basilica crisis, calling the emperor a son of the Church.`

2. **ijc.limit.f5-ordinary-day, use_note.means** - BLOCKING (missed by the pass; contradicts a corrected statement)
   - Current: `The record, from courts and bishops, noticed ordinary people mostly in a basilica or a riot, so an ordinary day was lived, not written.`
   - The statement now ends "those lives were lived, and our record does not hold them. We will not invent them." That wording was chosen in round 2 (finding 16) so that the world claims neither that the writing was never made nor that it was lost. "lived, not written" brings back the very claim the correction removed: that nothing was ever written.
   - changes_means.md lists this record as "checked and found fine", so the pass missed it.
   - Suggested: `The record, from courts and bishops, noticed ordinary people mostly in a basilica or a riot, so an ordinary day was lived, but our record does not hold it.`

3. **ijc.story.emperor-penance, use_note.means** - NON-BLOCKING (wording, optional)
   - Current: `...Ambrose's own letter demanded the emperor's repentance; Sozomen and Theodoret say Theodosius did it, and the dramatic public scene is their later telling.`
   - The substance is correct. Ep. LI shows only the demand. Sozomen VII.25 (l.42164, 42197) and Theodoret V.17 give the penance.
   - "did it" points back to "repentance", which reads awkwardly. The record text has the same phrase, but there it follows "repentance, shown".
   - Suggested: `...Sozomen and Theodoret say Theodosius did penance, and the dramatic public scene is their later telling.`

4. **ijc.limit.inner-life, use_note.means** - NON-BLOCKING (consistency, optional)
   - Current: `...it shows public worship, such as psalm-singing under siege, and forgiveness that followed shown repentance.`
   - This is not a contradiction, because psalm-singing is part of what Conf. IX.7 says. However, the statement now reads "sang hymns and psalms together", and this pass aligned reading-alone and vigil-in-basilica to "hymns and psalms".
   - Suggested: `...it shows public worship, such as singing hymns and psalms under siege, and forgiveness that followed shown repentance.`

5. **Residual contradictions in fields outside `means`** - NON-BLOCKING here (out of this pass's scope). These should be logged in Build/worlds/ijc/Open_Gaps_Tracking.md or fixed in a later spoken-field pass. Each one keeps a claim this pass corrected elsewhere:
   - ijc.story.emperor-penance, modern_contrast: "This world's own contemporary record is quieter: a private letter demanding repentance, and the fact of the emperor's submission." The corrected text and tier justification place the submission with the later historians, not the contemporary letter.
   - ijc.term.imperator-intra-ecclesiam, senses.informational: "The congregation held the building through a night under siege, sustained by singing." This pass removed "night" from the reading-alone, vigil-in-basilica and f5-ordinary-day fields as unsourced in Conf. IX.7.
   - ijc.story.vigil-in-basilica, retrieval.retrieve_when: "Milan's own hymn-singing custom, begun that night". This has the same "night" issue. It is a retrieval cue, not spoken text.
   - ijc.dw.baptism-threshold, positions[0]: "unrepeatable, consequential, and therefore often deferred". This keeps the Gibbon-note causal reading that the corrected text marks as "a later reading, not Eusebius's".
   - ijc.dw.women-authority-cost, sources/divergence_note: the new `means` ("named in some accounts") is supported by the vendored corpus beyond the volume's chronology. Conf. IX.7 (npnf101 l.13751-13766) names "Justina, the mother of the boy Emperor Valentinian" as persecuting Ambrose. The record does not cite it. Adding it would give the attribution an ancient warrant. This is not a defect in `means`.

## Checked and clean

The following 7 of the 9 edits were checked and are clean:
- ijc.limit.reading-alone: matches the statement and Conf. IX.7 l.13770-13772 ("hymns and psalms should be sung"). No "night" remains.
- ijc.story.vigil-in-basilica: matches the text and Conf. IX.7. The 386 date is the record's own stated chronology, and its divergence from the edition is disclosed in absent_detail.
- ijc.dw.baptism-threshold: matches the text's closing lines ("a datable, decisive crossing from outside to inside ... Many of our men put it off, and our sources do not always say why"). The unsourced "unrepeatable" and awe motive are gone. Eusebius gives only the Jordan reason (npnf201 l.6766).
- ijc.dw.how-we-read: matches "Both sides argued it from the same texts". It no longer calls both sides Nicene.
- ijc.dw.women-authority-cost: "named in some accounts" fits the text's "What came down to us names her", the divergence_note, and Conf. IX.7. "Young son" fits "mother of a young emperor".
- ijc.term.haeresis: matches senses.translational ("We hold it open") and Widely Accepted confidence. The overclaim "one act" is removed.
- ijc.term.martyrium: matches plain_meaning and quick_meaning ("modern scholars read"). Jerome ch. 103 names no shrine.

The other non-quote `means` fields are consistent with this pass's corrected fields: all 7 contested claims, the other 9 doctrinal witnesses, all 6 gravities, the 5 other limits besides f5-ordinary-day and inner-life, the 10 other stories and the 7 other terms. Specific checks:
- jesus-to-you ("survives") matches its statement ("do not survive").
- later-questions ("in this record") is scoped like its corrected statement.
- emperor-builds-another-basilica (330, no soldiers) matches its text.
- callinicum-synagogue ("those who burned") matches "Christians burned".
- tome-that-would-not-bend and term.tomus fit "Leo's reached Chalcedon without him".
