Review round 2, ijc record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: PASS WITH NON-BLOCKING

Scope: targeted recheck of commit be646da (`git diff HEAD~1 HEAD -- records/ijc`, 13 files) against the round 1 findings. Only the changed fields were rechecked. Each was compared with the vendored text in cic/texts/ by grep, graded with `engine.m1.gates.grade_text`, and read for tells and tense.

Readability on every touched field passes (FK <= 10, FRE >= 60). The lowest is ijc.dw.ancient-custom text (FK 7.5, FRE 64.8).

## Round 1 BLOCKING findings

1. **ijc.quote.no-power-but-of-god, modern_rendering** - fixed.
   - The text now reads "There should be rulers, with some ruling and others ruled. All things should not just be carried on in one confusion..."
   - This matches npnf111 l.53988-53991 ("For that there should be rulers ... that all things should not just be carried on in one confusion"). FK 4.8, FRE 81.3.

2. **ijc.quote.chalcedon-definition, modern_rendering** - fixed. "one Person and one subsistence" is restored.

3. **ijc.quote.nicene-creed, modern_rendering** - fixed. "came down [from heaven]" and "And [we believe] in the Holy Spirit" are restored with Percival's brackets.

4. **ijc.demo.reading-confusion, exchange[1]** - fixed for part (a).
   - The turn now uses the ijc.limit.reading-alone wording: "kept watch in the church and sang hymns and psalms together, so that sorrow would not wear them down."
   - This matches Conf. IX.7 (npnf101 l.13766-13773).
   - Part (b), the dangling participant turn, is routed to the gaps log (see below).

5. **ijc.dw.ancient-custom, text** - fixed.
   - The text now reads "Damasus wrote verse. Modern scholars read it as a way to make his see's apostolic memory visible."
   - The Jerome entry supports "wrote verse". The modern reading is now attributed, which agrees with ijc.figure.damasus, ijc.term.martyrium and ijc.term.primatus.

6. **ijc.term.homoios, sources[0].locus** - fixed.
   - The locus now reads "De Synodis: the Ancyra anathemas of 358 and Hilary's comment on likeness (sec. 73)".
   - The false "both pro-Nicene" claim and the file/line commentary are gone.

## Round 1 NON-BLOCKING items 7-10, 12-14

7. **ijc.demo.reading-confusion, exchange[3]** - fixed with option (b).
   - The turn now reads "two ways ... said the creed together ... sang hymns and psalms".
   - This now matches ijc.dw.how-we-read ("confessing the creed and singing hymns and psalms together"). FK 2.9, FRE 92.5.
   - Option (a), restoring the read-aloud channel from Ep. XX, remains available later. It is not a defect.

8. **ijc.demo.bread-and-cup, exchange[1]** - fixed.
   - The quoted words now match ijc.quote.ambrose-blessing-changes-nature's modern_rendering, from "This is not what nature made" through "After it, it is called Blood."
   - It drops only the rendering's lead-in, "Let us prove that". That cut is acceptable inside a speaker's quotation.
   - "another nature is named" matches npnf210 l.33266.

9. **ijc.figure.damasus, bridge_line** - fixed.
   - The text now reads "Modern scholars link that verse to Rome's care for the martyrs' graves. Jerome himself does not."
   - This is consistent with the record's floruit ("the martyr-epigram program"). FK 3.7, FRE 83.1.

10. **ijc.dw.marriage-ranked, text** - fixed.
    - "calls each one good" is restored, and the "but" is removed.
    - This matches npnf210 l.45071-45076.

12. **ijc.demo.want-to-believe, exchange[1]** - fixed.
    - The Leo lines are now verbatim: "Let the saint exult in that he draws near to victory. Let the sinner be glad in that he is invited to pardon. Let the gentile take courage in that he is called to life."
    - Source: npnf212 l.14508-14510.

13. **ijc.demo.ordinary-day, exchange[1] vs ijc.limit.f5-ordinary-day, statement** - fixed.
    - The two texts are now identical, including "mostly two empresses".
    - The limit's body note ("The record reads 'two empresses' ... without implying the record names no other woman") does not conflict with "mostly". No change is needed.

14. **ijc.limit.marriage-money, statement** - fixed. "a fair share of that wealth for the poor" restores the antecedent.

## New in this commit

16. **ijc.demo.want-to-believe, exchange[1], and ijc.limit.f5-ordinary-day / ijc.demo.ordinary-day** - NON-BLOCKING (consistency, optional)
    - Want-to-believe current: `Those pages do not survive, for you or for anyone before you.` This was changed from "were never written". It was not a round 1 item.
    - Limit/demo current: `those lives were lived, and nobody wrote them down.`
    - Each wording is defensible on its own, and neither fails the bar. However, one now implies that lost pages once existed, and the other asserts that nothing was ever written. The world should take one position on whether ordinary believers' writing was never made or was lost. The safest version claims neither.
    - Suggested, want-to-believe: `Our record does not hold those pages, for you or for anyone before you.`
    - Suggested, limit and demo (identical): `those lives were lived, and our record does not hold them. We will not invent them.`

## Items routed to Open_Gaps_Tracking (not fixed in records)

Logging each of these in Build/worlds/ijc/Open_Gaps_Tracking.md for the project lead is the right course. Recording it there clears them for this review cycle. None of them makes the current record text false.

- **Item 11, Ep. LXIII scope.**
  - Fixing this means widening ijc.source.ambrose-epistles `work` to license a letter it does not now list. That is a change to a source record's licensed scope, which needs a ruling, not a wording fix.
  - Also log the stale build fields on ijc.quote.the-rewards-of-virginity-the-merits-of-widowhood: use_note.years {377, 380}, the not_for "treatise" wording, and the "ch. IV.40-41" body note.
  - The quote text itself was verified verbatim at npnf210 l.45069-45076.
- **Item 15, locus convention.**
  - Whether loci on participant source cards carry vendored file/line references is a world-wide (arguably fleet-wide) convention. That makes it a methodology decision, so logging it is correct.
  - The round 1 check stands: every line number it checked points to the right passage, so nothing currently shown is wrong in substance.
- **Item 4(b), ijc.demo.reading-confusion participant turn 2.**
  - The turn "So even your most famous bishop struggled with it. But he was a trained scholar." still answers a representative turn that no longer exists.
  - Participant turns cannot be edited in this pass, so the choice is to rebuild or retire the demo. That needs the project lead.
  - The log entry should also note that the demo's body note is stale ("the Augustine struggle answered first"). Until the ruling, the demo should not be treated as a clean exemplar.

## Clean

All 13 files in the commit are clean apart from finding 16: the 6 blocking fixes and items 7, 8, 9, 10, 12, 13 and 14. No quote `text:` line changed. No participant turn changed.
