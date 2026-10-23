Review round 2 (targeted recheck), hal record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: PASSED - 0 BLOCKING, 2 NON-BLOCKING. Round 1 BLOCKING 1 is independently re-confirmed as fixed.

Scope: `git diff 4bfd8de..HEAD -- records/hal` (commit e01061a), 19 record files. The working tree is clean. Only what changed was rechecked against the round 1 findings. New wording was checked by grep against cic/texts/ (npnf206 Ep108 sec 6, Ep127 secs 7 and 13, Letter CXXXV headnote; npnf203 Rufinus to Anastasius). Every changed spoken field was scored with grade_text.

Mechanical checks, all clean:
- Schema gate: `gates.gate_schema_validation(loader.load_world_records('hal'),{},None)` returns `[]`. YAML parses, and every changed key sits where it did before.
- Readability: every changed spoken field passes. FK 5.1-9.1, FRE 60.4-80.0. The lowest FRE is hal.figure.marcella bridge_line (FK 8.0 / FRE 60.4). The highest FK is hal.demo.suffering (FK 9.1 / FRE 66.5).
- No new claim was found outside the cited source or another hal record. No AI tell was added. The fixes removed two tells (NB 2, NB 11). Tense is past and in the we-voice throughout.

## Round 1 findings, disposition

- BLOCKING 1, hal.story.journey-to-bethlehem text: applied exactly as proposed. The spring clause is gone. "went down to the harbor at Portus" matches npnf206 l.20969 ("she went down to Portus"). The text no longer clashes with hal.story.rome-crisis or Apology III.22. FK 6.3 / FRE 78.7. Re-confirmed.
- NB 1, born-again: applied. dw.practices text, demo.born-again exchange[1] and the narrowed Against the Pelagians locus now agree ("We spoke of being born again in baptism"). The positions and use_note lines still say the old thing. Out of scope, but not yet logged (see NB 2 below).
- NB 2, demo.born-again exchange[3]: applied. The turn ends at "the old loves stayed with him."
- NB 3, demo.someone-like-me: applied as proposed. "taking up the ascetic life" and "said fasting had killed her" follow Ep39 and the crowd's words (l.8112). The duplicate sentence is gone.
- NB 4, dw.was-jesus-god: applied. The "true physician" sentence and the Apology I.26 locus are removed. Ep22 secs 1, 25, 39 and Ep108 sec 10 are added. A double space was left behind (NB 1 below).
- NB 5, dw.inner-life: the Ep125 sentence was cut, which is an acceptable equivalent. No log entry is needed for it now. A double space was left behind (NB 1 below).
- NB 6, dw.empire: applied. "with the sun" matches Ep22 sec 28. "Some people thought Paula had gone mad" matches Ep108 sec 19.
- NB 7:
  - demo.hell: applied as proposed.
  - demo.suffering: applied. "the taking of the city had found her poor, not made her so" is verbatim from l.26369. "thanked God" is a fair reading, because the same sentence has her thanking God and then "thankful too". "pillaged and partly burned" matches the Letter CXXXV headnote (l.28393, "pillaged and partially burned").
  - demo.jesus: the penitent sentence is cut. A double space was left behind (NB 1 below).
  - demo.marriage-ending: applied.
  - story.rome-crisis: applied.
  - hal.dw.jesus `positions` ("physician to the penitent") is out of scope and not yet logged (see NB 2 below).
- NB 8, story.oea-gourd loci: applied as proposed.
- NB 9, figure.marcella bridge_line: applied. "priests sometimes among them" follows Ep127 sec 7 (l.26187, "including sometimes priests").
- NB 10, term.monasterium: the plain_meaning is applied as proposed, and sec 10 is added to the Ep108 locus.
- NB 11, story.desert-romances: applied. The closer is cut. The line now has a trailing space, but YAML strips it from a plain scalar, so it does not reach the field.
- NB 12, term.grammaticus and term.praeceptor loci: applied.
- NB 13, quote rufinus-writes-because-rome-is-where-the-news-is: applied. "that may have been aimed at" renders "which may have been directed against" (npnf203 l.45945). Nothing is added.
- NB 14, figure.paula-younger: note only. No change was expected.

## BLOCKING

None.

## NON-BLOCKING

1. **Double spaces left by sentence cuts** (hygiene, participant-facing)
   - hal.demo.jesus exchange (representative turn): `To the virgin among us he is the Bridegroom.  To the scholar he is the Word`
   - hal.dw.inner-life text: `a text to wrestle with.  On prayer that meets silence`
   - hal.dw.was-jesus-god text: `the blood by which we were bought back.  That is near to the later language`
   - A folded (`>-`) scalar keeps a double space inside a line, so all three reach the spoken field.
   - Proposed: reduce each to a single space. While in these files, rewrap the unwrapped long lines in the edited fields (demo.hell, demo.marriage-ending, demo.someone-like-me, demo.suffering, figure.marcella, the rufinus quote) to the file's width. This is cosmetic only, and the parsed text does not change.

2. **Out-of-scope items not yet logged** (gap tracking)
   - hal.dw.practices `positions[0]` ("baptism and datable conversion carry what \"born again\" carries") and `use_note.means` ("parallel being born again") still say the old thing. The text now says the world spoke of being born again in baptism (Against the Pelagians III.15, 19).
   - hal.dw.jesus `positions` ("physician to the penitent") has no locus in the record's sources. This pass removed the matching sentence from dw.jesus, dw.was-jesus-god and demo.jesus.
   - Build/worlds/hal/Open_Gaps_Tracking.md has no entry for either. Round 1's disposition asked for them to be logged if they were not fixed.
   - Proposed: append one numbered entry for each to Build/worlds/hal/Open_Gaps_Tracking.md. Cite subject and date (hal record audit fixes review, 2026-10-13), and name the field and the source locus above.

## Disposition

Approved to proceed for this wording pass. BLOCKING 1 is independently re-confirmed as fixed. Apply NB 1 and NB 2 in the next commit on this branch. Neither needs a further review round. The package rebuild after the records/ edits remains a default action.
