# Doc_03 Review — Round 7 (complement and negative-claim recheck, cold)

**Document under review:** `witt_Doc_03_Lexicon_Candidate_List.md` (DRAFT, Revision 6), Lutheran Wittenberg & Its Congregations (Atlas VI.1, `witt`).
**Reviewer:** independent, no drafting involvement, no involvement in Rounds 1–6, no prior context on this document or on how its Revision 6 fixes were made.
**Date:** 2026-09-16.
**Scope:** exactly the four-item list §13's "Review requirement (next round)" sets, taken from Round 6's own "What a Round 7 check should and should not do" — (a) that §11 item 2 is the arithmetic complement of §13's declared read ranges **for every entry**, re-derived from the vendored files rather than from the document's cross-references; (b) that every "not cited by any entry"-style negative is grep-confirmed against the document's own 72 entries; (c) that §11 item 8 is checked against the **rows of `witt_Source_Registry.md`** it proposes to extend, not only against the files; (d) a spot-check that R6-1–R6-6 landed and introduced nothing new. Per that scoping, **nothing Round 5 or Round 6 already re-derived was re-opened**: the twelve §12 "read in full" boundaries, the seven "read in part" items, all six Large Catechism unit boundaries, the AC Article XXVII/XXVIII/Conclusion split, Hymn I's extent and the *Kurze Form* transition were taken as settled. The 606-citation sweep, the 24-citation sample, the body-vs-Appendix cross-check, the thesis-number enumeration, the Doc_01 §8.4/§8.5 comparison and a fresh full `Hy`/`Kurze Form`/`LC` locus sweep were **not** re-run.

**Method.** §10.3, §11, §12 and §13 read in full; entries 2.2, 2.5, 2.9, 3.5, 4.9, 6.7, 6.8, 7.3, 7.4, 9.1, 9.2, 9.3, 9.6 read in full. Every citation locus in the 72 entries carrying an explicit file code was extracted by script and bucketed by file, then tested against §13's declared ranges — the test that produced R7-5 and R7-6. §13's declared ranges were then re-derived as *structural* claims directly from the vendored files: the Large Catechism's Conclusion-of-the-Ten-Commandments and Creed part boundaries from `luther_large-catechism_bente-dau1921.txt`; *Secular Authority*'s and the *Earnest Exhortation*'s own part and work boundaries from `luther_works-v3-selected_various1930.txt`; *The Papacy at Rome*'s title and first section heading from `luther_works-v1-selected_jacobs-spaeth1915.txt`; the two Apology loci from `melanchthon_apology-augsburg-confession_bente-dau1921.txt`. `witt_Source_Registry.md` rows 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 31, 34, 37, 38 and 94 read directly for their Verification Notes, against §11 item 8 line by line. Every negative claim in the document — about its own entries and about the vendored files — was confirmed or refuted by grep, never by argument.

---

# VERDICT: SUBSTANTIAL REVISION REQUIRED

**7 substantial findings, 4 cosmetic, 3 observations.** As at Rounds 3, 4, 5 and 6, **nothing found in this round misquotes a source or misclassifies an entry**, and all but one of the findings are again coverage statements. But the verdict has moved, for three reasons stated plainly below.

## The core question, answered directly

Round 6's root-cause section named, precisely, what a pass closing this class would have to do: *"derive §11 item 2 wholly as the arithmetic complement of §13's declared ranges — every entry, not only the three added at Revision 5 — reconcile §11 item 8 against the Registry rows it proposes to extend rather than only against the files, and check the affirmative 'not cited by any entry' statements by grep."* Revision 6 did the third of those three completely, and the first two **only where Round 6's own findings pointed.**

- **The grep work is clean.** Every negative claim in the document reproduces. §12's "No candidate entry cites a locus beyond the declared read range in any of the three" holds for Hymns I, IV and XXVI; §12's and §11 item 2's "9.6's citations... all inside 1741–1870" holds for every locus on that entry's Evidence line; §10.3's "nothing above cites them" holds for Zell (R55), the 1525 tract (R48) and *On the Jews and Their Lies* (R49) — R48 appears in exactly one Registry line, at entry 7.4, as a **bar**, which is not a citation. The source-file negatives reproduce exactly too: *sola fide*, *sola scriptura*, *sola gratia*, *simul justus* and "theology of the cross" return zero across all ten files; *Anfechtung* returns exactly one, at v2 5418; "Sacramentarian" returns exactly three in v1, at 10661, 10727 and 15611. **R6-1's fix is correct in both halves** — Hymn I is cited by exactly three entries, 2.5, 2.9 and 9.3, two of them Tier 1, all three inside 1258–1352, and nothing anywhere cites 1353–1430.
- **But the complement still does not hold, at four entries no prior round tested.** Two of them are large: the *Earnest Exhortation*'s unread remainder (roughly 900 lines) is declared **nowhere in the document**, though §13's own row labels the declared range "opening" only — the identical defect R5-2 found and Revision 5 fixed for the Large Catechism's Lord's Prayer and Baptism, surviving untouched in a third work; and the Large Catechism's own **Conclusion of the Ten Commandments** (LC 2380–2558) is declared neither read nor unread, in the one file the reconciliation was built around.
- **§11 item 8 was reconciled against R25 and R37 and against no other row.** Its R38 line omits two Apology loci this pass read that Registry row R38 does not record — one of them the four-line passage against which Round 1's headline S1 defect (an Apology quotation carrying the AC's wording) was corrected. That is R6-3(b)'s defect exactly, in the same list, one row over.
- **One finding runs in the overstating direction.** §13's v3 discovery row certifies the declared range 12100–12440 as "Secular Authority **II–IV**." Re-derived from the file, that range lies wholly inside the treatise's **Part One**: `PART TWO` stands at 13133, `PART THREE` at 13811, there is no Part Four, and no numbered subsection headings exist anywhere between the title at 11794 and 13133. Whatever "II–IV" was meant to name, it names structural units the declared range does not contain.

**This review does not itself declare a sixth recurrence of the escalated class, and a reviewer should not read R7-3 as one without a further determination.** R7-3 is a bracketed structural *label* inside a discovery-table cell, not a sentence of the form "read in full"; every citation drawn from that range is sound, correctly quoted and inside the range. But §13's Escalation check, as Revision 6 wrote it, states that Round 6 tested whether the escalated class recurred "**and found that it did not — anywhere.**" R7-3 is a coverage statement that overstates what was read, in §13's discovery table — the fourth of the four locations Round 5's root-cause analysis named, and the one location no round has ever swept for this class. Under the project's own rule that a blocking finding cannot be closed by self-certification, **whether R7-3 falls inside or outside OG-5's class needs independent re-confirmation, not a build-thread ruling.** That question, plus the two large undeclared unread spans, is why this round's verdict is not "MINOR ISSUES REMAIN."

**Stated for the record, so the finding count is not misread:** six of the seven substantial findings are of the same low-consequence kind Round 6 reported — coverage statements that mislead Doc_06 without putting any citation at risk. No evidence anywhere in this document is unwarranted on the strength of anything found this round.

---

# Substantial findings

## R7-1 — The *Earnest Exhortation*'s unread remainder (v3 ≈10751–11659, roughly 900 lines) is declared nowhere, though §13 itself labels the declared range "opening" only

**Locations:** §11 item 2 (by omission) and §13's v3 discovery row.

§13's v3 row declares: *"10641–10750 (**Earnest Exhortation opening**)."* The word "opening" is §13's own. R5-2's finding was exactly this shape: ranges §13 labels "opening" whose remainders were never carried into the unread-sections list. Revision 5 fixed the Large Catechism's two instances (Lord's Prayer, Baptism) and Round 6 confirmed both. **A third instance was never in either pass's scope and is still open.**

Re-derived from `luther_works-v3-selected_various1930.txt`: the *Earnest Exhortation* section runs from its heading (10441, per Registry row R19) to just before `INTRODUCTION` at **11674**, which opens *Secular Authority*. The declared read range covers 10641–10750. **Roughly 10751–11659 — about 900 lines, the largest single undeclared unread span in this document — is unread and named in no list.**

The string "Earnest Exhortation" occurs exactly **twice** in the whole of Doc_03: once in §0's Discipline 1 paragraph and once in §13's v3 row. It is absent from §11 item 2, from §11 item 8 and from §12. By contrast, §11 item 2 does carry *"the Teutonic Order exhortation beyond its opening (R24),"* which is the same case in the same row of the same table — so the list's own convention exists and was simply not applied here.

**Consequence.** This is the sole source of entry **7.4**, the document's clearest `[PV]` case, whose own AG line calls it *"period-bound to 1521–22 in this library, a real coverage limit for Doc_04."* Doc_06 is told that limit is a property of the library; it is in fact substantially a property of what was read. Nothing in 7.4 is unwarranted — all four of its v3 loci sit inside 10641–10750, and its one further locus (10554–10594) is honestly attributed to Registry row R44 and "not re-read."

## R7-2 — §11 item 2 omits the Large Catechism's Conclusion of the Ten Commandments (LC 2380–2558)

**Locations:** §11 item 2 (by omission), against §13's LC row.

§11 item 2's LC sentence, as R6-2 rewrote it, names: the First Commandment's remainder (521–680); the Second, Third, Seventh, Eighth, Ninth and Tenth Commandments in full; the Fourth, Fifth and Sixth beyond the two excerpts; the Second Article; the Lord's Prayer's and Baptism's remainders. Re-derived directly from `luther_large-catechism_bente-dau1921.txt`:

| Heading | Line |
|---|---|
| Ninth and Tenth Commandments (per Round 6's derivation, not re-opened) | 2241 |
| ` Conclusion of the Ten Commandments.` | **2380** |
| `Part Second. OF THE CREED.` | **2559** |
| `Article I.` | 2594 |
| `Article II.` | **2684** |
| `Article III.` | 2756 |

§13 declares LC 1615–1730 read and then nothing again until 2559. **LC 2380–2558 — the Catechism's own Conclusion of the Ten Commandments, 179 lines — is therefore unread, and it is neither one of the Ten Commandments nor the Second Article, so no clause of §11 item 2 reaches it.** The list is not the complement.

This is not an empty span. Its argument bears directly on three existing entries: *"so that outside of the Ten Commandments no work or thing can be good or pleasing to God"* (**2385–2386**, quoted verbatim from the file) on **2.3 good works**, and *"Let us see now what our great saints can boast of their spiritual orders and their great and grievous works which they have invented and set up"* (**2387–2389**) on **8.4 "spiritual"/*Geysterey*** and **8.5 perfection**.

**No citation is at risk:** no `LC` locus anywhere in the 72 entries falls between 1727 and 2604.

## R7-3 — §13's v3 row certifies "Secular Authority II–IV" for a range that lies wholly inside the treatise's Part One; §11 item 2 and §11 item 8 then mis-name which part is unread

**Locations:** §13's v3 discovery row; §11 item 2; §11 item 8's R20 line.

**(a) The read-label.** §13's v3 row reads: *"12100–12440 (**Secular Authority II–IV**)."* Re-derived from `luther_works-v3-selected_various1930.txt`:

- `SECULAR AUTHORITY:` / `TO WHAT EXTENT IT SHOULD BE OBEYED.` — **11794**
- `LETTER OF DEDICATION` — 11804; `THE TREATISE` — 11898
- `PART TWO` / `How Far Secular Authority Extends` — **13133**
- `PART THREE` — **13811**
- No Part Four exists. No line matching a bare roman numeral occurs anywhere between 11794 and 13133.

The declared range 12100–12440 therefore sits **entirely inside Part One**, roughly 340 lines of a treatise of about 2,640. Read at face value the label certifies three named structural units, two of which begin more than 690 lines past the declared range's end and one of which does not exist. I could not reconcile "II–IV" with anything in the file; if it was meant to name something other than the treatise's parts, it is in any case not a checkable claim, which is the form R5-1 named and Revision 5's §11 item 8 rewrite was built to eliminate.

**This is the one finding of the round that runs in the overstating direction**, and it sits in the one of Round 5's four named locations that no round has swept for this class. Graded substantial because it changes a scope boundary and because of what §13's own Escalation check currently says about it (see the core-question section above). Graded no higher because **no evidence depends on it**: entry 7.1's three v3 loci (12123–12127, 12139–12141, 12371–12374), 8.5's (12133–12136), 3.2's (12184–12186), 2.6's (12239–12241) and 7.2's (12300–12306) all sit inside 12100–12440, all are Part One material, and 7.1's own definition quotes Part One's argument ("We must divide all the children of Adam into two classes").

**(b) Which part is unread.** §11 item 2 reads *"*Secular Authority* beyond 12100–12440 (R20), **including its third part on the limits of obedience**,"* and §11 item 8's R20 line repeats *"not the treatise's third part on the limits of obedience."* Part **Two** is the part on limits — its own heading is *"How Far Secular Authority Extends,"* and its opening sentence calls it *"the main part of this treatise."* Part **Three** opens *"Now that we know the limits of secular authority, it is time also to inquire **how a prince should use it**."* Both cross-references point Doc_06 at the wrong part.

## R7-4 — §11 item 8's R38 line omits two Apology loci this pass read that Registry row R38 does not record — including the locus of Round 1's S1 correction

**Location:** §11 item 8, *"Proposed as Verification-Note extensions for the Registry owner to apply."* This is the list with a live route into `witt_Source_Registry.md`, **APPROVED TO PROCEED**; it is the location and the risk R5-1 named and R6-3 re-found.

§11 item 8's last entry reads, in full: *"R38 (Apology 552–771, 1108–1125, 4896–4935, now read)."*

§13's Ap discovery row declares **five** loci read this pass: *"552–771 (Article IV opening); 1108–1125 (faith alone); **4700–4730** (extended to include 6.8's 'fanatical opinions of the Anabaptists' at 4729 — corrected, Round 1 S5); 4896–4935 (Article XII opening); **6492–6495** (corrected quotation — see 6.8, Round 1 S1)."*

Registry row R38's own Verification Note records read: *"TOC 52–89, greeting 92–129, Articles I–II 137–184, Article XXIV 8488–8567,"* with verbatim checks at 97, 155–157, 4701, 5915–5916, 7595, 8490–8494, 8512–8514 and 8531. **It records neither 4729 nor 6492–6496.** Under item 8's own stated purpose — "loci the Registry records as unread that this pass has now read" — both belong in the line, and both are omitted.

The second omission is the consequential one. Ap 6492–6496 is quoted at length in entry **6.8**, and is where Round 1's finding **S1** — the review's own headline defect, an Apology quotation that had carried AC Article V's wording — was corrected. I re-derived it: the file reads at 6492–6496 *"…against fanatical men, who dream that the Holy Ghost / is given not through the Word, but because of certain preparations of / their own, if they sit unoccupied and silent in obscure places, / waiting for illumination, as the Enthusiasts formerly taught, and the / Anabaptists now teach."* Applied as drafted, §11 item 8 would leave the Registry with no record that the single most consequential verification this document performed was performed at all.

**The same understatement is carried at §11 item 1**, the Apology's own coverage paragraph: *"Only its Article IV opening (552–771), the 'faith alone' passages (1108–1125), Article XII's opening (4896–4935), **one grep-located line at 4729**, and the lines the Registry already verified were read."* §13 declares the range 4700–4730, not one line; and 6492–6495 is omitted entirely and is not covered by the trailing clause, since R38 does not record it.

**Direction and severity.** Both are **under**statements, as R6-3 was — they would make the Registry record less coverage than exists, not more, and neither is a fabrication risk. They are false statements about another document's contents in the one list built to be copied into it, written in the revision whose whole purpose was to reconcile that list against those rows.

## R7-5 — R6-2's own fix names the wrong citing entry: 6.5 cites nothing in either span, and 7.3, which does, is named nowhere

**Locations:** §11 item 2's R6-2 correction, and §13's LC row Result column.

§11 item 2 now reads: *"six cited loci fall inside them (entries 6.1, **6.5**, 8.2, 8.3, 8.4 — including LC 1630, the very locus Round 1's S5 fix extended the range to cover)."*

Grep-confirmed against all 72 entries, the `LC` loci inside LC 1045–1060 and LC 1615–1730 and the entries that carry them are:

| Locus | Entry |
|---|---|
| LC 1051–1052 ("this estate of fatherhood and motherhood") | 6.1 |
| **LC 1051–1060** | **7.3** obedience / "obey God rather than men" / honor |
| LC 1630 ("the religious estate") | 8.4 |
| LC 1687–1716; 1723–1725 | 8.3 |
| LC 1713–1716 | 6.1 |
| LC 1721–1727 | 8.2 |

**Entry 6.5** (pastor / preacher / "care-takers of souls") cites exactly one `LC` locus, LC 43–47, and nothing in either span. **Entry 7.3** cites LC 1051–1060 and is named in neither location.

**It is the same error twice, independently.** §13's LC row Result column lists *"…6.1, 6.3, 6.5, 6.6, 6.7, 6.8, 6.9, 7.5, 8.1–8.4 (1630)…"* — **7.3 is absent there too**, although 7.3 draws an Evidence locus from the LC and 7.5 (which does) is listed.

This is precisely the class task (b) exists for: a claim about which entries cite a locus, carried forward from a review report's own wording rather than re-grepped when it was written into the canonical document. Nothing is unwarranted — 7.3's citation is sound and inside a declared-read range — but a Doc_06 builder following §11 item 2's own pointer will open the wrong entry and find nothing there.

## R7-6 — §11 item 2 fails the complement test at two further entries, in opposite directions

**(a) *Bondage* — the list over-sweeps.** §11 item 2 reads *"*Bondage* beyond its opening sections (R34; every quotation there needs a character-level re-check)."* §13's Co row declares four loci read: *"269–398 (Luther's introduction); 730–809 (assertion; abstruse Scripture); **5212–5228, 14740–14775** (grep-located 'two kingdoms')."* The last two are not opening sections by any reading, and **Co 14748–14750 is cited by entries 2.9 and 7.1** — 7.1 being a `[CT]`-tagged Tier 1 entry whose whole "two kingdoms" distinction rests on it. This is R6-2's shape exactly: the unread list declares unread a zone §13 declares read and the document's own entries cite. Nothing is unwarranted; the defect is that the list tells Doc_06 to go and read material this pass already read and used.

**(b) *The Papacy at Rome* — the list under-sweeps, by 81 lines.** §11 item 2 reads *"*The Papacy at Rome* beyond its introduction (v1 12975–14690, R8) — the treatise's own argument, **unread past 12974**."* Re-derived from `luther_works-v1-selected_jacobs-spaeth1915.txt`: the treatise's own title, `TO THE PAPACY AT ROME`, stands at **12694**; the declared read range opens at **12775**, exactly on the heading `THE STATEMENT OF THE CASE`. **v1 12694–12774 is unread treatise material, named in no list**, while the item's own wording ("unread past 12974") implies coverage up to 12974. §12 supplies the boundary that makes this visible — it states the treatise "runs from its title at 12694" — so the two sections disagree.

Graded together because they are one defect with two signs, and both are what task (a) asks about. **No citation is affected in either case:** every v1 `Papacy` locus in the entries (12786–12788, 12786–12792, 12879–12880) sits at or above 12775, and the two `Co` loci are honestly sourced.

## R7-7 — §10.3's claim that "the Holy Ghost" appears in five named entries' Evidence lines is false for four of the five

**Location:** §10.3, "Terms considered and deliberately not carried," final long bullet — the passage that grounds the Doc_06 recommendation on whether the Holy Ghost and the person of Christ warrant standalone entries.

It reads: *"the term 'the Holy Ghost' already appears inside several existing entries' **Evidence lines** (2.9, 5.1, 6.9, 6.8, 9.6) without being gathered under its own headword."*

Grep-confirmed across all 72 entries, for "Holy Ghost" and "Holy Spirit" together:

| Entry named | Where it actually appears |
|---|---|
| 2.9 | **Preliminary definition** only ("no power, without the Holy Ghost, to work the righteousness of God") — not the Evidence line |
| 5.1 | **Nowhere in the entry** |
| 6.9 | **Nowhere in the entry** |
| 6.8 | Evidence line — correct (AC 253–255; Ap 6492–6496) |
| 9.6 | **Nowhere in the entry** |

Two entries whose Evidence lines **do** carry it — **3.1** (AC 247–248, *"through the Word and Sacraments, as through instruments, the Holy Ghost is given"*) and **6.3** (LC 2763, *"the Holy Ghost, with His office"*) — are not named. So the claim is right about one of five, and misses two it should have caught.

This is R6-1's class with the sign reversed: an affirmative statement about which entries cite something, asserted rather than grepped. It is the ground the document gives for not adding the entry now, and Doc_06 is directed to *"read AC I and III and decide."* A builder who opens 5.1, 6.9 or 9.6 expecting to find the term gathered there will find nothing.

---

# Cosmetic findings

## R7-8 — R6-4's fix moved the prose boundary numbers as well as the ranges, so three items now contradict their own parentheticals

R6-4 correctly corrected three unread-tail **ranges** in §11 item 2 (Hymn IV to 1697–1740, Hymn V to 1871–1991, Hymn XXVI to 3720–3756 — all three verified as exact complements of §13's 1647–1696, 1741–1870 and 3660–3719). It also changed each item's introductory phrase, which it did not need to:

- *"Hymn IV **beyond 1697** (Hy 1697–1740)"* — read literally, "beyond 1697" excludes 1697, which the parenthetical includes.
- *"Hymn V **beyond 1871** (Hy 1871–1991)"* — same.
- *"Hymn XXVI **beyond 3720** (Hy 3720–3756)"* — same.

The two items in the same sentence that R6-4 did not touch use the opposite and correct convention: *"the Fourth Preface **beyond 1124** (Hy 1125–1178)"* and *"Hymn I **beyond 1352** (Hy 1353–1430)."* One line each, no unread substance, no citation affected — noted only because it is R6-4's own fix generating a new inconsistency inside the sentence it was fixing.

## R7-9 — §11 item 8's header sentence is falsified by its own R15 line

§11 item 8's header states: *"Every entry below now states either an explicit locus (a narrow, checkable claim) or, where a named section was read only in part, says so explicitly with the actual sub-range."* Its R15 line states neither: *"R15 (Sermons 1, 2, 5 and 8, now read)."* That is the exact form R5-1 named as "how both findings survived Rounds 3–5's sweeps" — a section named by title and claimed read, with no line extent. The **content** is true and independently checkable (§12 gives all four ranges, each verified at Rounds 4–6), so this is graded cosmetic; the header's universal claim is not.

Also in the same list: **R11 (*Christian Nobility*, 2117–2416)** omits v2 **5790–5830**, which §13 declares read this pass and which Registry row R11 records as unread ("text not read this session"). Those lines are the treatise's editorial footnotes, so the consequence is small — but it is the same omission as R7-4, one row up.

## R7-10 — entry 6.8's "Ap 6492–6495" is one line short of the quotation it gives

Entry 6.8 quotes the Apology through *"…and the Anabaptists now teach"* and cites it as **Ap 6492–6495**. Re-derived from the file: the quotation begins at 6492 and its final clause, `Anabaptists now teach.`, stands at **6496**. The locus should be 6492–6496. Nothing is misquoted — the text is verbatim-exact against the file, including the S1 correction — and no coverage claim turns on it.

## R7-11 — §13's read-record does not carry entry 9.2's one grep-located locus

Entry 9.2 cites **v2 5418** (*"the word occurs exactly once across all ten files, at v2 5418"* — independently confirmed this round). §13's v2 row names its grep-located loci explicitly and lists two, **10562–10566 and 7026**; 5418 is not among them, and §13's builder-grep row, which does declare the *Anfechtung* sweep as a channel, omits 9.2 from its Result column. This is the class of Round 2's N8, Round 3's R3-5 and Round 4's R4-6 — a locus outside every declared direct-read range, disclosed honestly in the entry but not carried into §13's own read-record. Cosmetic by parity with all three precedents.

---

# The Round 6 fixes, checked (task d)

**R6-1 — landed, and correct in both halves.** §11 item 2 now names the true tail (Hy 1353–1430) and the three citing entries; §12's hymn bullet carries the same correction with the loci and tiers. Grep-confirmed: exactly three entries cite Hymn I — 2.5 (Hy 1292–1293), 2.9 (Hy 1286–1287), 9.3 (Hy 1288–1290) — all inside the declared-read 1258–1352, and 2.5 and 9.3 are Tier 1 on their own `Tier (est.)` lines. Nothing cites 1353–1430. **Clean.**

**R6-2 — landed, but carries a misattribution.** The two excerpts are correctly carved out of the LC gap and the ranges match §13 exactly. The citing-entry list does not — see **R7-5**.

**R6-3 — (a) landed and is exactly right; (b) landed for R25 and was not swept.** §11 item 8's R37 line now reads that the Conclusion *"is not this document's to claim either way: Registry row R37 itself already records 'Conclusion 1531–1567 read,' with the signatories verified verbatim."* I read R37 directly: its Verification Note reads *"Preface 47–161, Article headings 166–1271, Article XX 494–617, Article XXIII 707–782, Conclusion 1531–1567 read,"* and records *"signatories (1559–1567)"* among the verbatim checks. The document's sentence is an exact match, and the same correction is carried at §11 item 2, §12 and §13's AC row. **The highest-stakes half of this fix is clean.** R25 now carries both LC excerpts and the "only" is gone. But the reconciliation-against-the-Registry that R6-3 asked for was applied to R25 and R37 and to no other row — see **R7-4** and **R7-9**.

**R6-4 — landed; the three ranges are exact complements; the prose was over-corrected.** See **R7-8**.

**R6-5 — landed and correct.** §11 item 2 now gives the *Kurze Form*'s unread section as **v2 13342–14402**, the exact complement of §13's declared 13172–13341, with the reasoning stated inline. The three-line front-end overlap Round 6 found is closed.

**R6-6 — landed in all three locations.** LC Article III's close is stated as **2989** at §11 item 8 and §13 (Article III's heading at 2756, `Part Third. OF PRAYER.` at 2991 — re-derived this round in passing while deriving the Creed part boundaries for R7-2); the Lord's Prayer's close is stated as **3758** and its unread remainder as **3006–3759**, which is the exact complement of §13's 2756–3005 and 3760–3925. **Clean.**

**Round 6's observation — landed and verified.** §13's Drafting-basis bullet now reads *"Doc_02 §1, §2, §3, §12.1, §12.3, §15, §16 read,"* with the three added sections named and each tied to the place in Doc_03 that draws on it.

**Light spot-check, offered but not the point of the round:** the stated word count **32,750** reproduces exactly (`wc -w`), the second consecutive revision in which it has. The document carries **72** entries by script count, as stated.

---

# Observations

**N7-1 — OG-2 has roughly doubled since its own headline figure was written, and is now materially understated.** `Open_Gaps_Tracking.md` OG-2 is titled *"~40 inline 'corrected, Round N Sx/Nx'-style change-history markers"* and records that *"Round 3 counted 38 bolded inline fix markers."* This round's count of inline references carrying a finding number (`Round N` followed by an `S`/`N`/`R`/`C` number) returns **92**, distributed roughly 30 / 8 / 12 / 11 / 13 / 15 across Rounds 1–6. **Not re-litigated and not a defect to fix in this round**, per the brief and per Rounds 4–6; flagged only because OG-2's own body predicts the accretion ("the deferral itself is accreting round over round, not static") while its headline and its cited count no longer describe the document. It remains a disclosed, deliberate deferral and a precondition on disposition.

**N7-2 — entry 9.1's *Fourteen of Consolation* pointer is handled correctly, and is worth naming as the house convention.** 9.1's Evidence line ends *"The *Fourteen of Consolation* (v1 3994 ff.) **was not read**."* I confirmed v1 3994 is that work's own title line, that it falls outside every declared v1 read range, and that §11 item 2 lists the work as unread (R5) while 9.1's Registry line reads "5 (unread)." This is the same correct formula entry 6.9 uses for LC 3504, applied to a locus that is pointed at rather than quoted. It is what R7-11 and R7-6(a) should look like.

**N7-3 — the front matter of the hymns file and the AC's preface are Registry territory and are correctly left out of §11 item 2.** Hy 1–889 and AC 1–165 are declared read by Registry rows R27 and R37, drawn on at entry 4.9 and §10.3 with explicit "per R45/R47/R94" attributions, and not claimed as read by this pass. No finding; recorded so a later pass deriving the complement mechanically does not mistake them for gaps.

---

# Root cause

Round 6 diagnosed this precisely and the diagnosis still holds, one level down. Revision 5 asked *"is every statement that something was read true?"* and answered it completely. Revision 6 asked *"is every statement that something was not read true?"* — and answered it **for the entries Round 6's three findings named**: Hymn I, the two LC commandment excerpts, the AC Conclusion, R25, the three hymn tails, the *Kurze Form*. It did not answer it for the entries no finding had pointed at. So the *Earnest Exhortation*, the LC's Conclusion of the Ten Commandments, *Bondage*, *The Papacy at Rome*, R38 and R11 are all still carrying the pre-Round-6 description, and §10.3 and §13's v3 row have never been swept for the claim type at all.

**The shape is now four rounds old and is worth naming exactly, because it is no longer "the fix went where the finding pointed."** Rounds 5 and 6 both told the build thread to sweep *the claim type across every entry*, in those words. Both times the sweep was run over the specific entries each report itemised and then stopped. The remaining work is not another patch; it is one mechanical derivation. §13's discovery table already contains every declared range. §11 item 2 should be **generated** from it — sorted, subtracted, with each residual span named against the file's own structural headings — rather than edited. Every finding in this round except R7-3, R7-5 and R7-7 would have been impossible to write if it had been.

Two things are worth saying against any inference that this round reopens OG-5 on its own authority:

1. **Six of the seven substantial findings are Round 6's direction, not Round 5's.** They understate coverage, mislead Doc_06 about what to read, and leave nothing unwarranted. The seventh, R7-3, overstates — but it is a structural label in a table cell, not a "read in full" sentence, and every citation drawn from the range it labels is sound. Whether it belongs to the escalated class is a determination this review deliberately does not make.
2. **Every one of these defects predates the pass that missed it.** The *Earnest Exhortation* omission, the LC Conclusion omission, the *Bondage* and *Papacy* descriptions, §11 item 8's R38 and R15 lines and §13's "II–IV" label all date from Revision 0 through Revision 4. Revision 6 introduced exactly one new defect, R7-8, and one carried-forward misattribution, R7-5.

---

# What a Round 8 check should and should not do

Offered only so the option is costed; if no further pass is authorized, this section is moot.

1. **Re-derive nothing Rounds 5, 6 or 7 has already re-derived.** The twelve §12 boundaries, the seven "read in part" items, all six LC unit boundaries, the LC Creed part boundaries, the AC Article XXVII/XXVIII/Conclusion split, Hymn I's extent, the *Kurze Form* transition, *Secular Authority*'s three part boundaries, the *Earnest Exhortation*'s extent, *The Papacy at Rome*'s title and first heading, and the two Apology loci are all now confirmed against the files.
2. **Check that §11 item 2 was regenerated from §13 rather than edited again.** The test is cheap and total: sort §13's declared ranges per file, subtract, and confirm every residual span is named. If three or fewer entries changed, it was edited.
3. **Check §11 item 8 against every Registry row it names, not only R25, R37 and R38** — R3, R4, R6, R7, R9, R10, R11, R12, R13, R15, R16, R20, R23 and R24 were read this round for their Verification Notes and only R11 and R15 carried anything; a closing pass should confirm that independently rather than on this review's word.
4. **Resolve "Secular Authority II–IV" one way or the other, and record which.** Either it names something in the edition that I could not find, in which case say what; or it is wrong, in which case the correction is a scope-boundary change and the OG-5 question in §13's Escalation check needs re-answering by someone other than the thread that wrote it.
5. **Re-grep the affirmative positives, not only the negatives.** R7-5 and R7-7 are both "entries X, Y, Z cite this" claims that no round had ever tested. There are a small number of them.
6. Do **not** re-run the 606-citation sweep, the 24-citation sample, the body-vs-Appendix cross-check, the thesis-number enumeration, the Doc_01 §8.4/§8.5 comparison, the Framework paragraph 97 check, this round's negative-claim greps or its full per-file citation bucketing — all came back clean.
7. N5 remains open by design, owned at OG-2, and does not need re-litigating; but see **N7-1** — its recorded magnitude is now roughly half the true figure, and the entry is the place to correct that, not this document.

---

**Disposition: none claimed by this review.** This report is a finding, not a ruling; it does not dispose the document. Under the project's governance rule, no finding above may be closed by self-certification; each needs independent re-confirmation — **R7-3 most of all**, since §13's own Escalation check currently records the escalated class as not having recurred anywhere, and R7-3 is a coverage overstatement in a location that check did not cover. This review takes no position on whether that reopens OG-5; it records the fact and leaves the determination where CO-022's fourth escalation category puts it.
