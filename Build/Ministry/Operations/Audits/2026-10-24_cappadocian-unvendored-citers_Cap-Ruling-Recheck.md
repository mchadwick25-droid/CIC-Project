# Cappadocian unvendored-citers: cap-ruling recheck of R3-1 and R3-2

- **Ordered under:** "Cap ruling: cappadocian unvendored-citers, one recheck of the last two fixes" (2026-10-24), `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`. This recheck does not count toward the review cap.
- **Date:** 2026-10-24
- **Reviewer:** independent Opus context (no part in drafting rounds 1-3 or the fixes)
- **Scope:** only R3-1, R3-2, exact application of the round 3 wording, and the regate. Fix commit checked: `5ca7db92`. A later commit (`6fedcd05`) touches only `Build/worlds/cappadocian/Open_Gaps_Tracking.md`; `git diff 5ca7db92 HEAD -- records/` is empty.

Path key: N208 = `cic/texts/npnf208_basil-letters-select-works.xml`.

## Verdict

**PASS.** Both sentences are true against N208. The R3-2 note agrees with the record's own evidential and locus. The round 3 wording was applied exactly, and nothing else in `records/` changed. Regate passes.

## 1. R3-1: voice-craft guard

Record: `records/cappadocian/voice_craft/cappadocian.voice.craft.md:51-52`, now "Our preaching against greed reaches us only in extracts, and our famine sermon only in summary."

- **"Preaching against greed ... only in extracts": true.**
  - N208:6227-6228: "Homily VI., on Luke xii. 18, is on selfish wealth and greed."
  - N208:6230 "Beware, says the preacher," opens a quoted extract marked "§ 3" (N208:6230-6231). It runs to "in the day of distress.”" (N208:6283). A second extract, "The conclusion is" marked "§ 8" (N208:6285-6287), runs to "Amen.”" (N208:6317). These are two section extracts, not the whole homily.
  - N208:6848: "Homily VII., against the rich, follows much the same line of argument as VI." A quoted extract follows from N208:6855 "“I am filled with amazement,” says the preacher" to N208:6924 "woman’s fancies?”".
- **"Our famine sermon only in summary": true.**
  - N208:6926-6927: "Homily VIII., on the Famine and Drought, belongs to the disastrous year 368." N208:6926-6935 is third-person summary. The only quoted words are Amos's: "The lion hath roared: who will not fear?" (N208:6931-6932). No words of Basil are quoted.
  - The earlier Prolegomena mention also holds no quotation. N208:1844-1845: "He describes it with eloquence in his Homily *On the Famine and Drought*." N208:1849-1852 is narrative ("hoarded grain in the hope of selling at famine prices. These Basil moved to open their stores.").
- The guard now matches `term.philoptochia` evidential ("The famine homily itself, Homily VIII, is only summarized there.").

## 2. R3-2: `term.philoptochia` divergence_note

Record: `records/cappadocian/term/cappadocian.term.philoptochia.md:15-19`. Statement by statement:

| Statement | True? | Evidence |
|---|---|---|
| No open-license translation of the whole set is vendored (Source Registry row 16) | Yes | N208 holds only extracts and summaries in the Prolegomena; Registry row 16 (`Build/worlds/cappadocian/cappadocian_Source_Registry.md:55`) records that the homilies' own text is not vendored. |
| The npnf208 Prolegomena quotes long English extracts of Homilies VI and VII | Yes | VI: N208:6230-6283 and 6285-6317. VII: N208:6855-6924. Both are long. |
| (npnf208 xml:6227-6310, 6848 onward) | Yes | 6227 is the Homily VI heading; the conclusion extract continues to 6317, so 6310 is a slightly short end bound but it lands inside the extract and misstates nothing. 6848 is the Homily VII heading. |
| Only summarizes Homily VIII on the famine (6926-6935) | Yes | As in section 1. |
| Wording within those extracts is checkable; other wording rests on general scholarly knowledge | Yes | This follows from the above. |

**Consistent with the record:**
- The evidential (lines 64-67) reads "Long extracts of Homilies VI and VII are quoted in English in the Basil volume of the Nicene and Post-Nicene Fathers. The famine homily itself, Homily VIII, is only summarized there."
- The locus for `basil-moral-famine-homilies` (line 32) reads "not held whole; extracts of Homilies VI and VII are quoted in the npnf208 Prolegomena".
- `not_for` (line 80) reads "the famine homilies' sharpest lines as checked quotations". This is still right, because the famine homily is summary only.

## 3. Exact application

I checked this by script against the backticked replacement spans in the Round 3 findings table.
- The R3-1 replacement lines match exactly (`voice.craft` lines 51-52).
- The five R3-2 replacement lines match exactly (`philoptochia` lines 15-19).
- `git diff HEAD~1 HEAD` for `5ca7db92` touches only those two records in `records/`: voice.craft has 2 lines changed and philoptochia has 5. Its other files are the Round 3 audit file and the decision-log entry.

## Regate

`python -m engine.m10.cli regate cappadocian --base origin/main`: **PASS**. All readability notes say "not a regression, already failed at the base and unchanged". This includes the voice.craft note, which is on `characteristic_concerns[4]`, not the guard.

## Non-blocking observation (outside the ordered scope; log, do not reopen)

The npnf208 Prolegomena also quotes Basil's Second Homily on Psalm xiv (xv), against usury, almost whole. See N208:5057-5059 ("The Second Homily on Psalm xiv. (xv.) has a special interest in view of the denunciation of usury") and the quotation from N208:5066 "St. Basil proceeds;—“In depicting the character of the perfect man" to N208:5288 "Amen.”".

Registry row 16 lists "against usury" in its homily set. It also says the only occurrences are "third-person scholarly description" and that "No open English translation of these homilies is vendored". For the usury homily, that is not accurate.

This does not make either rechecked sentence false:
- The guard's "only in extracts" still holds.
- `philoptochia` cites only Homilies VI-VIII and makes no usury claim.

Registry row 16 should be corrected separately. Any record that treats usury-homily wording as uncheckable should also be corrected.
