# jes — Step 0 change order, "Step 0 §4 item 5: the Generals' correspondence and the end of Ignatius's letters" (2026-09-30)

This file holds the reasoning, the before and after text, and the process record for one change order to `Build/worlds/jes/Step0_Movement_Scope_Confirmation.md` (Approved to proceed, not Frozen). It also records how the file-code `jes` was assigned. The live files carry the corrected wording only.

## 1. Name

**Step 0 §4 item 5: the Generals' correspondence and the end of Ignatius's letters (2026-09-30).** It is a change order to a document at Approved to proceed. It changes the substance of one claim, so it is named here and not made as a quiet edit. The ledger entry that supersedes the affected sentences is item 30 in `Build/worlds/jes/Open_Gaps_Tracking.md`, "Step 0 change order 'Step 0 §4 item 5: the Generals' correspondence and the end of Ignatius's letters' (2026-09-30)".

## 2. Reasoning

Step 0 §4 item 5 said that nothing vendored gives Lainez's own voice as General, nor Borgia's or Mercurian's, and that Ignatius's own vendored letters end in 1547. The Round 1 review of Doc_01, Doc_02, the Registry and the ledger (`Build/worlds/jes/Review-Artifacts/Round1_Review.md`, finding P1-1 and Scope 8) showed that both statements are wrong as written. The change order rests on four facts, each re-counted or re-read against `cic/texts/` for this revision.

1. **Ignatius's letters.** The Latin *Monumenta Ignatiana* volume (`ignatius-loyola_epistolae-et-instructiones-v22-lat_1903.txt`) has as its last fully dated letter no. 256, to Philip, prince of Spain, headed "ROMA 28 FEBRUARII 1548" (lines 38788–38789). No. 257 is headed "PATER JOANNES DE POLANCO EX COMM." and is dated "EXEUNTE FEBRUARIO AUT INEUNTE MARTIO 1548" (lines 38857–38859). It is Polanco's, on Ignatius's commission, and not Ignatius's own. No. 258, to Bobadilla, is dated only "ROMA FEBRUARIO AUT MARTIO I548" (lines 39005–39008), and it is in Ignatius's own first person. So the last dated letter under his name is 28 February 1548, and one undated letter of February or March 1548 follows. This differs from the Round 1 review in one point: the review treats the March item as the only later item and does not mention no. 258.
2. **The editors' own words.** The Salmeron Tomus Secundus Prooemium (`salmeron_epistolae-v3-lat_1906.txt`, lines 230–237) says the volume prints more than 200 letters to Salmeron, "quarum pars maxima ex praepositorum generalium regestis deprompta est", most of them drawn from the registers of the Generals. The Lainez Praefatio says that his letters as vicar and General are mostly taken from the registers and written in his name by a secretary (`lainez_epistolae-et-acta-v1-lat_1912.txt`, lines 521–537). The Salmeron Tomus Primus Praefatio calls Polanco's letters "ex commissione generalium praepositorum scriptae" (`salmeron_epistolae-v2-lat_1906.txt`, lines 1709–1710).
3. **The counts.** They were made by two independent methods over the OCR headings of the two Salmeron volumes. Method A starts from the sender's heading line and reads the addressee line below it. Method B starts from the addressee line ("PATRI ALPHONSO SALMERONI", read with a similarity threshold to allow for OCR damage) and reads the sender line above it. Results, letters to Salmeron:

   | Sender | Tomus | Method A | Method B | Figure used |
   |---|---|---|---|---|
   | Lainez | Primus | 17 (2 as vicar, 15 as General; one of the 15 is addressed to Salmeron and Madridius together) | 16 (the joint letter is not caught) | 17 |
   | Polanco "ex comm." | Primus | 146 strict, 156 with damaged headings read | 154 (includes headings without the formula) | about 150 |
   | Polanco "ex comm." | Secundus | 12 | 14 (includes the 2 headed by his name alone, as vicar in 1572) | 12, plus 2 as vicar in 1572 |
   | Borgia | Secundus | 49 (7 as vicar general, 42 as General) | 49 | 49 |
   | Mercurian | Secundus | 89 | 88, plus 1 heading split across words | about 88 (86 to 89) |
   | Aquaviva | Secundus | 19 | 19 | 18 to 19 |

   Dates: Polanco, Tomus Primus, 17 December 1556 to 21 January 1565; of the 146 read in full, 112 carry a legible year of 1556–61, 22 carry 1564 or 1565, and 12 carry no legible year; none is dated 1562 or 1563. Lainez as vicar, 19 March 1557 and 13 February 1558; as General, 6 November 1558 to 6 January 1565. Borgia as vicar general, 18 February to 26 May 1565; as General, 18 November 1565 to 10 March 1571. Mercurian, 9 October 1573 to 27 May 1580. Aquaviva, 20 May 1581 to 14 July 1584. The Tomus Secundus Prooemium (lines 274–276) says that Borgia was elected vicar general by the professed fathers at Rome after Lainez died.
4. **The letters' character.** They are register copies, in Italian and Spanish, addressed with a handful of exceptions to one provincial, Salmeron. No volume of any General's own correspondence is vendored.

The correction cuts against a reviewed Step 0 finding (Step 0 Review Round 3, finding S1), and the Round 1 reviewer routed it as an escalation to the project lead. It is applied here to item 5 only, as instructed for this revision.

## 3. Before and after, verbatim

**Before** (Step 0 §4 item 5, from commit d040f3c77):

> 5. **The global/missionary sourcing gap after Xavier's death (binding on Doc_02).** Per §3 B2/B5: the vendored corpus's own missionary/global voice is concentrated in the founding generation, to Xavier's 1552 death. Institutional/administrative material is dense to 1556 (Lainez Tomus I, Polanco Tomus V; Ignatius's own vendored letters end in 1547), runs to 1562 through Nadal's letters, and after that rests on Salmeron's letters alone, to c. 1585. Nothing vendored gives Lainez's own voice as General (1558–65), nor Borgia's or Mercurian's, and nothing missionary/global extends past Xavier. The Jesuit Relations (a plausible PD lead, unchecked) should be assessed before claiming sustained global reach across the full window.

**After:**

> 5. **The global/missionary sourcing gap after Xavier's death (binding on Doc_02).** Per §3 B2/B5: the vendored corpus's own missionary/global voice is concentrated in the founding generation, to Xavier's 1552 death. Institutional material is dense to 1556 (Lainez Tomus Primus, Polanco Tomus Quintus; Ignatius's own vendored letters end in the Latin *Monumenta* volume on 28 February 1548, with one undated letter of February or March 1548 after it, and in 1547 in the English selection), runs to 1562 through Nadal's letters, and after that rests on Salmeron's two volumes alone, to February 1585. Those volumes print the Roman centre's letters to Salmeron as register copies, in Italian and Spanish, mostly written by secretaries in the General's name: about 150 by Polanco on the General's commission (1556–65, with 12 more to 1570), 17 by Lainez (2 as vicar in 1557–58 and 15 as General, 1558–65), 49 by Borgia (7 as vicar general in 1565 and 42 as General, 1565–71), about 88 by Mercurian (1573–80) and 18 to 19 by Aquaviva (1581–84). No volume of any General's own correspondence is vendored, and these letters are, with a handful of exceptions, addressed to one provincial. Nothing missionary/global extends past Xavier. The Jesuit Relations (a plausible PD lead, unchecked) should be assessed before claiming sustained global reach across the full window.

**Differences from the wording the Round 1 review proposed.** The review's wording read "about 146 by Polanco on the General's commission (1556–65), about 15 by Lainez as General (1558–65), about 42 by Borgia as General (1565–71, with 7 more as vicar general in 1565), about 86 by Mercurian (1573–80) and about 18 by Aquaviva (1581–84)", and said that the last letter dated 28 February 1548 was Ignatius's last. The wording above uses the two-method recount of section 2: Polanco "about 150" (146 to 156 by the counts, and 12 more in Tomus Secundus), Lainez 17 in all (2 as vicar), Borgia 49 in all, Mercurian "about 88" (86 to 89), Aquaviva "18 to 19", and it adds the undated letter of February or March 1548. It replaces "c. 1585" with "February 1585", the month in which the volumes' last correspondent died, as the Tomus Secundus Prooemium says (lines 217–226).

## 4. Wording-only edits to Step 0 made in the same commit

These edits remove dated provenance and the project lead's name from live-file sentences so that the file passes `tools/check_live_commentary.py --enforce`, which fails a change that edits a live file and leaves flagged commentary in it. They change no claim. The provenance they carried is recorded here.

| Step 0 line | Removed provenance | After |
|---|---|---|
| §0 (line 11) | "Mark", and the date 2026-09-15 of the selection | "Selected directly by the project lead from the Era VII survey roster, one of six candidates chosen together for the project's first build run past its existing 70–451 CE window." |
| §2 A4 (line 39) | "Mark", and the date 2026-09-15 | "The project lead selected this candidate directly, as one of six candidates chosen together for this batch (§0 above). No record establishes the project lead's own specific reasoning." |
| §3 B1 (line 57) | "Mark's 2026-09-25 scan-quality ruling" | "the Library's scan-quality ruling (`Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md` point 5)". The ruling is dated 2026-09-25 in that log. |
| §3 B1 (line 59) | the date 2026-09-25 for the nine works | "the nine later additions". They were vendored on 2026-09-25. |
| §4 item 1 (line 85) | "Mark's 2026-09-25 scan-quality ruling" | "the Library's scan-quality ruling" |
| §4 item 3 (line 87) | the open-item cue "not an open item" | "with nothing left to decide" |
| §4 item 6 (line 90) | "Mark's own reasoning" | "the project lead's own reasoning" |

## 5. What the change order does not do

- It does not amend Step 0 §3 B2, §3 B5 or the Tier conclusion. B2 carries the sentence "Nothing vendored gives Lainez's own voice as General (1558–65), nor that of his successors Borgia (1565–72) and Mercurian (1573–80)", and B5 and the conclusion carry the same claim in other words. They need the project lead's decision on whether the change order extends to them.
- It does not unfreeze or freeze anything. Step 0 stays at Approved to proceed.
- It is not confirmed by the project lead. No record in this repository shows the project lead's approval of this change order. It was applied on the instruction of the coordinating agent of session_019FXuEebrCDmzYe987sNAxL, and it stays open for the project lead's confirmation.
- The sentence "No volume of any General's own correspondence is vendored" is true of the shelf at commit d040f3c77, on which the Round 1 review and this change order rest. The Library acquisition commit d767495c8 adds volumes of the Generals (*Lainii Monumenta* Tomi 2–8, Borgia Tomi 3–5) to `cic/texts/`. Step 0 §5 says a vendoring pass leaves the document stale until it is resynced. That resync is a separate step for the project lead and the build thread.

## 6. Assignment of the file-code `jes`

The project lead's answer in the session's choice box, given in session_019FXuEebrCDmzYe987sNAxL on 2026-09-30, was exactly "jes (Recommended)". The question was "Which code should I give them before starting Doc_01?" The options were "jes (Recommended)", "soj" and "Other". The Round 1 review could not confirm the assignment from any record outside the drafting session, and this section is that record. `build/jes_Build_State.yaml` cites it.

## 7. Related files

- `Build/worlds/jes/Review-Artifacts/Round1_Review.md`
- `Build/worlds/jes/Step0_Movement_Scope_Confirmation.md` (§4 item 5 after this change order)
- `Build/worlds/jes/Open_Gaps_Tracking.md`, section G
- `Build/Ministry/Operations/Audits/SocietyOfJesus_Step0_Correction_2026-09-30.md`
- `Build/Ministry/Operations/Audits/jes_Steps1-2_Draft_2026-09-30.md`
