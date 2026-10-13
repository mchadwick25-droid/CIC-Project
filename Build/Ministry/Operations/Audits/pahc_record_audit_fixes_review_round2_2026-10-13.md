Review round 2 (targeted recheck), pahc record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: PASS (0 BLOCKING, 1 NON-BLOCKING)

Scope: only the fields touched since round 1. These are the 19 patch entries plus two follow-up edits: pahc.figure.hermas bridge_line and pahc.story.one-eucharist-under-bishop tellable_as. Each was checked against the round 1 findings 1-16 (Build/Ministry/Operations/Audits/pahc_record_audit_fixes_review_round1_2026-10-13.md). Round-1 items 17 (story `text` readability) and 18 (YAML block reflow) were not fixed by choice and are registered instead. They are not rechecked here.

How the edits were checked:
- **YAML.** All front matter in records/pahc/*/*.md parses (0 failures).
- **Gates.** `python -m engine.m10.cli records pahc` gives PASS.
- **Readability.** Every touched spoken field was graded with `engine.m1.gates.grade_text`.
- **Facts.** Facts were checked by grep against the vendored files: anf01, anf02, anf07, anf09 (1 Clement), npnf201 and the Tacitus file.

## Round 1 findings, rechecked

1. **pahc.story.martyrdom-of-polycarp, tellable_as.** RESOLVED.
   - Now reads: "Afterward the church hoped to gather each year at the place where his bones were laid."
   - The yearly gathering is now stated as a hope, which matches Martyrdom 18 ("the Lord shall grant us to celebrate the anniversary") and the corrected lament-suffering demo.
   - Grade: FK 7.0 / FRE 68.5.
2. **pahc.demo.identity-collision-someone-like-me, exchange[1].** RESOLVED.
   - Now reads: "The way of life did not end at the water. It asked a person to seek out the faces of the saints day by day."
   - The second sentence is Didache 4:2 (anf07 l.12817: "seek out day by day the faces of the saints").
   - The claim about how members lived is gone, and so is the chiasmus.
   - Grade: FK 3.7 / FRE 91.0.
3. **pahc.source.anti-montanist-fragments, body.** RESOLVED.
   - Now reads "across Asia", which matches npnf201 HE V.16.10.
   - Nothing else in the body changed, and the caveats ("contested, not yet defeated", "no record may present their inner teaching as fairly known") are intact.
4. **pahc.demo.center-how-we-know, exchange[1].** RESOLVED.
   - Now reads "gathered ... read ... there was time ... It might be", in the past tense.
   - "Or" follows Justin (anf01 l.16504).
   - Grade: FK 4.9 / FRE 81.7.
5. **pahc.demo.center-jesus-as-god, exchange[1].** RESOLVED.
   - The "not an argument worked out" pivot is cut.
   - The closing pair is now one plain sentence: "We did call him God, and we cannot tell you we had settled how." It states an honest limit and is no longer a coined closer.
   - Grade: FK 4.8 / FRE 81.6.
6. **pahc.demo.identity-collision-womens-authority, exchange[1].** RESOLVED.
   - Now reads "Whether it cost the women who held that authority anything, our record does not say." It no longer assumes a cost.
   - Grade: FK 6.5 / FRE 75.3.
7. **pahc.figure.hermas, bridge_line.** RESOLVED.
   - Now reads: "A man in Rome who says he was once sold as a slave. He wrote down the visions he reported - ..."
   - This matches anf02 l.649 ("sold me to one Rhode in Rome") and the wording of the hermas-visions story. It no longer infers freed status.
   - The opening fragment follows the label style of the other bridge lines, for example tacitus.
   - Grade: FK 4.6 / FRE 86.9.
8. **pahc.figure.tacitus, bridge_line.** RESOLVED.
   - Now reads "he wrote that people came to pity them, since they seemed to die for one man's cruelty".
   - This follows tacitus l.68 ("there arose a feeling of compassion; for it was not, as it seemed, ... but to glut one man's cruelty").
   - Grade: FK 5.5 / FRE 77.7.
9. **pahc.witness.how-we-know and pahc.witness.reading-scripture, text.** RESOLVED.
   - Both now use Justin's "or" (anf01 l.16504).
   - Grades: FK 6.7 / FRE 76.8 and FK 6.3 / FRE 76.9.
10. **pahc.witness.who-was-jesus, text.** RESOLVED, with a hygiene note (see new finding 1 below).
    - Now reads "truly persecuted under Pilate", as in Trallians 9.
    - The three-beat summary closer is deleted.
    - Grade: FK 6.2 / FRE 74.3.
11. **pahc.quote.those-who-lived-reasonably-are-christians, modern_rendering.** RESOLVED.
    - Now reads "even though they were thought to be atheists", which matches the text's "even though".
    - Every clause is still rendered.
    - Grade: FK 7.9 / FRE 63.7.
12. **pahc.story.first-clement-corinthian-dispute, text.** RESOLVED.
    - Now reads "calls on those who started the revolt to submit to the presbyters" (1 Clem. 57: "Ye therefore, who laid the foundation of this sedition, submit yourselves to the presbyters").
    - FRE improved from 55.2 to 55.9. It is still under 60, which falls under registered item 17.
13. **pahc.story.hermas-visions, text.** RESOLVED.
    - Now reads "and names no single bishop". The argument from silence is now stated as silence.
14. **pahc.story.one-eucharist-under-bishop, tellable_as.** RESOLVED.
    - Now reads "Ignatius wrote to the churches that they should treat ...". The addressee is no longer misnamed.
    - "Follow the bishop as Jesus Christ follows the Father" matches anf01 l.8274 (Smyrn. 8).
    - Grade: FK 8.0 / FRE 67.0.
15. **pahc.term.ministrae, senses.personal.** RESOLVED.
    - The process-voice clause is gone. It now ends "The record keeps no name and no word of theirs."
    - Grade: FK 4.2 / FRE 82.5.
16. **pahc.term.two-ways, senses.personal.** RESOLVED.
    - "It asked for more than one yes" is cut.
    - The sourced Didache 4:2 sentence stays.
    - Grade: FK 3.1 / FRE 91.4.

No patch introduces new source drift, an AI tell, a tense error, or a readability failure in a gated field. No quote `text` and no participant turn was touched.

## New findings

1. **pahc.witness.who-was-jesus, text: trailing space.**
   - The value now ends with "...through Jesus, his servant. " because removing the closing sentence left its leading space behind.
   - NON-BLOCKING. This is hygiene only. It does not change the meaning or the grade, and the gates pass. Strip the trailing space before commit.
