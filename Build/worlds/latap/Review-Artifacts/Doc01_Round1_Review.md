Simulated review — informational only, not an Article 31 substitute.

# Round 1 review of Doc_01 (latap)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review session, fresh context (wrote none of the text under review)
- **Drafter agent:** Sonnet 5.5 library-stage worker
- **Round:** 1
- **Truncation check, method 1:** structural count. There are 10 `##` headings, numbered 1 to 10 in order (Formation World Identity through Disposition). The file has 218 lines and ends on the complete sentence "Draft. It is not approved to proceed, and it is not frozen." followed by a newline.
- **Truncation check, method 2:** the file is 34,727 bytes. Its git blob is `68bd56fc3987e54c52a12254609d27b2e9857e97`, which equals `git rev-parse HEAD:Build/worlds/latap/Doc_01_World_Identification_Boundaries_Orientation.md` at commit 9a3b3cb, and the committed size is 34,727. The working tree is clean.
- **Date:** 2026-10-29
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

**Not clear.** P0: 0. P1: 9. P2: 14.

The document has the shape Framework V7.4 Step 1 asks for. The quotations are sound: every one I re-checked matches its vendored division, once ANF notes that interrupt the text are taken out. The *Octavius* is dated as two Contested ranges, and the text never says the *Apology* "opens" the Latin case. The failures are of three kinds. First, the document claims records and ledger entries that do not exist. Second, its neighbour overlap claim is stale. Third, several tags, dates and counts are not what the sources or Step 0 give.

### P1 findings

**P1-1. Two cited record files do not exist.**
- *Where:* §2, line 35: "recorded in `Source_Registry.md`". §9 item 2, line 201: "recorded in `build/latap_Build_State.yaml`".
- *Evidence:* `Build/worlds/latap/` holds only `Doc_01_…md`, `Step0_Movement_Scope_Confirmation.md` and `Review-Artifacts/`. There is no `build/` folder, and `find` finds no `Source_Registry.md` for this world. The Source Registry is a Step 2 output (Build Process V2.0 §4, the table row for Step 2). Line 35 also claims that each date tag "was re-read against the vendored scholarship in this pass". Nothing records that re-reading.
- *Fix:* Delete both pointers, or create the records first. Do not claim a re-reading that no record shows.

**P1-2. The neighbour re-confirmation is said to be logged in three worlds' ledgers. It is logged in none.**
- *Where:* §7, lines 157, 158 and 159 ("Neighbour re-confirmation is logged in that world's `Open_Gaps_Tracking.md`"), and §9 item 12, line 214.
- *Evidence:* I searched `Build/worlds/pahc/`, `lpc/` and `ijc/Open_Gaps_Tracking.md` for "Latin Apolog", "latap", "I.43", Tertullian, Minucius and Lactantius. None of the three has an entry about this world. The only hits are unrelated LPC entries about LPC's own Tertullian comparandum (P1-3). This is a claim that an action happened when it did not. `tools/check_live_commentary.py --surface worlds` also flags lines 157 to 163 as REWRITE (change-history-cue and change-history-block).
- *Fix:* Remove the claim, or have the owning threads log the requests and then cite them by subject and date. Under CLAUDE.md, editing another world's ledger is "flag it, don't touch it".

**P1-3. The LPC distinctness claim is stale.**
- *Where:* §7, line 158: LPC "excludes Tertullian and the Passion … Both shelves keep their own weight." Line 155: "re-confirmed, not re-run, here".
- *Evidence:* `records/lpc/source/lpc.source.tertullian-de-pudicitia.md` now exists, merged in #1241 on 2026-10-29. It cites *On Modesty* ch. XXII, a work on this shelf that is also co-assigned to Montanism, as "comparandum evidence". `lpc.force.decian-persecution-libelli-system` and `lpc.gravity.confessor-authority-vs-episcopal-peace` cite it, and LPC's own ledger records this. Registry row 29 there is Excluded and licenses nothing, but an LPC gravity now rests partly on a work in this world. Step 0 §4 item 7's sweep predates this, so re-confirming without re-running missed it.
- *Fix:* Re-run the sweep for LPC. Disclose the *De Pudicitia* XXII comparandum use and the gravity it supports, and carry it as a cross-world question rather than "no change needed".

**P1-4. *De mortibus* is named once without the authorship dispute, against a binding obligation.**
- *Where:* §7, line 150: "Lactantius … whose *On the Deaths of the Persecutors* belongs to another world".
- *Evidence:* Step 0 §4 item 6 says: "Doc_01 should name the authorship dispute wherever it mentions the work." Doc_01 line 159 itself promises: "This document names the authorship dispute wherever it names the work." Line 150 calls the work Lactantius's with no qualification.
- *Fix:* At line 150, add that Harnack holds the work is Lactantius's and Brandt denied it, or cross-refer to the line 159 statement.

**P1-5. The window's opening date carries two different tags, and one of them is not Step 0's.**
- *Where:* §2, line 31: "Confidence: Widely Accepted for the year." Table, line 39: "Dominant Modern Reconstruction for each year". The table header says "the tags are Step 0's".
- *Evidence:* Step 0 gives "Widely Accepted" to no Tertullian year. Its six uses of the tag cover Commodian's use of Cyprian, Arnobius's span, the pre-break status of two works, and Perpetua. Lactantius's *Institutes* also appear as WA in Step 0's table. Step 0 §4 item 8 tags the absolute Tertullian years as DMR. The only scholar cited for the year is Harnack ("197 Ende. Apologeticum", printed p. 295, file lines 16555 onward). One scholar does not make a reading Widely Accepted; Step 0's own logic on *De mortibus* says so.
- *Fix:* Tag the 197 date as Step 0 does, as DMR on Harnack, or cite more than one scholar and get the change reviewed. Make line 31 and line 39 agree.

**P1-6. The Cyprian date has no named scholar, does not come from Step 0, and goes past the vendored scholar's date.**
- *Where:* Table, line 42: "Cyprian, *Address to Demetrianus* | late 251 to 253 | Dominant Modern Reconstruction".
- *Evidence:* Step 0 gives no date for the *Address*. Doc_01 line 9 says "A date in this document is the date a named scholar gives". Harnack (printed p. 365, file lines 20646 to 20652) places it, "mit einiger Wahrscheinlichkeit", at "das Ende d. J. 251 oder den Anfang d. J. 252". No vendored source read gives 253.
- *Fix:* Give Harnack's late 251 or early 252 with its source, or name the scholar for 253. Mark the row as not from Step 0.

**P1-7. "Tertullian's thirty-two works" includes a pseudonymous work, and the share drawn from it overstates his corpus.**
- *Where:* §3, line 70 ("Tertullian's thirty-two works are 731,618 of 1,203,783 counted words, about 61 percent") and the table at line 39 ("Tertullian, thirty-two works | 197 to c. 222/3, in Harnack's table").
- *Evidence:* The 32 include the *Appendix of poems ascribed to Tertullian*, anf04 `iii.xi`, 32,001 words. Step 0 B1 calls it "pseudonymous verse". Doc_01 drops that disclosure. Harnack's table does not date those poems.
- *Recount, method 1:* Step 0's regex div2 extraction, which I re-implemented. Tertullian's 32 works come to 731,618, and the figure reproduces exactly. Against Marcion is 187,134. The percentages are right as arithmetic: 60.8% and 15.5%.
- *Recount, method 2:* an lxml parser over the same divisions. With notes included, Tertullian's 32 works come to 731,374 and Against Marcion to 187,127. With notes removed, the 40-work total is 1,046,740 and Tertullian's 32 works are 638,572 of it (61.0%).
- Without the *Appendix*, Tertullian's genuine works are 699,617 words, 58.1% of the 40-work total.
- *Fix:* Say 31 works plus the pseudonymous *Appendix*, or give both figures. State that the count includes ANF apparatus, and that only the *Octavius* has a second, independent count in Step 0. B1 says: "No second, independent run is claimed".

**P1-8. The heresy treatises are not "the largest single share of the counted corpus".**
- *Where:* §2, line 62.
- *Evidence:* The five works named are the *Prescription*, *Against Marcion*, *Against Hermogenes*, *Against the Valentinians* and *Against Praxeas*. By method 1 they come to 20,936 + 187,134 + 23,066 + 15,014 + 31,933 = 278,083 words. Lactantius's four works come to 285,187 (Step 0 B1; method 2 gives 285,144). With notes removed, the heresy group is 236,749 and Lactantius is 259,991. On either method, the plain comparison with another author's shelf shows the claim is false. No count supports it.
- *Fix:* Drop "largest", or state the count and what it is compared against. For example: "about 23 percent of the counted corpus, the largest block among Tertullian's works."

**P1-9. Quotations lack a `cic:` locus in their paragraph, against the Library-stage quotation rule.**
- *Where:* §4 Finding, line 91: "a disciple of Arnobius" and "his pupil Lactantius". §2, line 47: "Flourished 196?".
- *Evidence:* All three are verbatim. "a disciple of Arnobius" is in `npnf203…:v.iii.lxxxii`. "Flourished 196?" is in `npnf203…:v.iii.lx`. "his pupil Lactantius" is in `npnf206` Ep. 70. But the paragraphs cite only other loci. Build Process V2.0, "Quotations", says to cite `cic:<file>:<locus>` in the same paragraph so the gate can confirm the quotation inside the named division.
- *Fix:* Add the three loci. For Ep. 70, add its `npnf206` division id.

### P2 findings

1. **Rule letters mislabelled (line 47, §9 item 4).** Doc_01 relabels Step 0 §4 item 1's rules. Step 0's (a) is the no-"opens" rule and the census list, (b) is the two ranges, and (c) is the two editorial statements. §9 item 4 then sends the census phrases to "rule (c)", which is the wrong rule. Line 47 also says "Two ANF04 editorial statements … the NPNF gloss", which contradicts itself. *Fix:* use Step 0's letters, and say "one NPNF gloss and one ANF04 note".
2. **Wrong section cited for "best-anchored date" (line 31).** The phrase is not in Step 0 §3 B1. It is in §2 A5 and the Section B conclusion. *Fix:* correct the reference.
3. **The opening boundary leaves something out (lines 31 and 32).** On Harnack's own table, *Ad martyras* (early 197) and *Ad nationes* (summer or autumn 197) come before the *Apology* (late 197). His note 2 allows that some works of 198 to 202/3 may be from c. 195 to 197. The text reads as if only the *Octavius* could be earlier. *Fix:* say so in one sentence.
4. **The Carthage locus does not support the claim (line 51).** `anf05…:iv.v.v`, the *Address* itself, does not name Carthage. *Fix:* cite a locus that does, or drop the address.
5. **"Almighty" attributed to Minucius (line 171).** "Almighty" and "omnipotent" do not occur anywhere in the ANF *Octavius*, `iv.iii` with notes removed. Ch. XVIII explicitly declines "Father": "If I were to call Him Father, you would judge Him to be earthly". *Fix:* attribute "the Almighty" to Commodian alone, and quote Minucius's refusal.
6. **Wrong chapter for the Spirit and the Virgin (line 189).** The text says Lactantius names the Spirit as the one who conceived Christ in the Virgin, "Book IV ch. XI". Ch. XI has only the Spirit filling the prophets. The Virgin passage is ch. XII. *Fix:* cite ch. XI and ch. XII separately.
7. **Confidence vocabulary misattributed (line 9).** Constitution V2.3's Article 17 does not list the five levels; the words do not appear in the docx. The canonical token is "Inferential-Thin" (`engine/m10/claims.py:26` and Forces Framework V1.1). The document writes "Inferential/Thin". *Fix:* cite the right source and spell the token as the engine does.
8. **§6 calls itself Layer 1 but tags no force.** Forces Framework V1.1 says "Every force documented at Layer 1 carries its confidence level explicitly. Sources are named." Only the date of the break is tagged. Material exists to tag others: for example, Harnack's "c. 190–c. 195 Übertritt" for the conversion. *Fix:* tag each cell, or call the section a preliminary identification without the Layer 1 label.
9. ***On the Vanity of Idols* called Cyprian's with no dispute (lines 88 and 151, "two Cyprian works").** Harnack (p. 337) doubts the ascription, and the map records it as disputed. *Fix:* say "ascribed to Cyprian".
10. **Process narration.** Line 35 has "in this pass". Line 155 has "re-confirmed, not re-run, here". The live-commentary checker flags lines 157 to 163. *Fix:* rewrite these as plain statements of what is so.
11. **The Lactantius Article 4 result is stated more strongly than Step 0 allows (lines 174, 194 and 210).** Clause 2 is marked "Shown" with no mention of the II.8 passage that Step 0 §2 A2 ties to the floor (God "produced" a spirit, then "made another"). §9 item 8 calls the dualist passages "manuscript-only". But II.8.4 stands in Brandt's constituted text (Step 0 §4 item 5); only the fuller dualism is manuscript-only. *Fix:* add the disclosure, and separate the constituted-text passage from the manuscript-only ones.
12. **Uncited claims from the census or the builder.** These are: the Passion "travelled with Tertullian's writings" (line 17, the census's "transmitted alongside"); "Commodian wrote catechism in verse" (line 17); "Greek is the older Christian language of the region" (line 56); and Lactantius Book IV "continues the argument of Tertullian's *Apology* ch. 21" (line 153). The last is an untagged inference. *Fix:* source each one, or tag it as the builder's own.
13. **Wrong heading reference for §8.** The heading cites "Step 0 §4 item 1", which is about dating. The Article 4 obligations are §2 A2 and §4 item 3. *Fix:* correct the reference.
14. **Speaker unclear (line 126).** The text says the charge "is stated in the *Octavius*, where the speaker says …". The quoted words are Octavius's Christian rebuttal at ch. XXIX, not the pagan's charge, which Caecilius makes at ch. IX. *Fix:* name the speaker, and cite ch. IX for the charge.

### Verified against the sources

- **Quotations re-checked word for word with notes removed, all matching their division:**
  - Arnobius I.1, I.28, II.65 and I.41, and the human-shape objection in I.60.
  - Tertullian *Apology* 17, 21 and 23, and *Against Praxeas* (`v.ix.ii`), both passages.
  - Lactantius V.1, and IV.12, IV.13 and IV.18. The third day is in ch. XIX.
  - Commodian `v.ii.xliii` and `v.ii.xxxiii`.
  - Jerome, *De viris illustribus* 53, 58, 79 and 80, Ep. 84 and Ep. 70.
  - The *Octavius* XXIX passage.
  - Constitution Articles 4, 21 and 22, and the five commitments.
  - The census `legacy` sentence and its `informalName`.
- **The Minucius counts, by two methods.** The raw XML of `iv.iii` has "Christ" twice ("Christ." and "Christ's"), "Crucifi-" three times, of which one is a repeat of a heading in an attribute, and "Jesus", "Son of God" and incarnation language never. The parser text has four occurrences in all, which are the ch. IX heading, the Athenagoras footnote, the ch. XXIX gloss and the ch. XXXVII heading. With notes removed, only the heading occurrences remain.
- **Other counts.** Commodian has "Christ" 42 times with notes removed and "Jesus" never. "Pilate" and "Holy Spirit" or "Holy Ghost" are absent from Arnobius, and the Spirit names from the *Octavius* and the *Instructiones*.
- **Harnack.** He gives the *Apology* as end of 197. His table lists Greek versions of *De spectaculis*, *De baptismo* and *De virginibus velandis*. He gives the break as 207/8, places *On Exhortation to Chastity* and *On the Veiling of Virgins* before the break (204 to 206/7), and reports that *Quod idola* copies the *Octavius* in chapters 1 to 9 and the *Apology* in chapters 10 to 15 (p. 337). He says Lactantius gave up public teaching after the edict, dates the *Epitome* after summer 313, has the Gaul move about 317, and names Trier.
- **Anchors.** The Tuburbium and Carthage note to the Passion, and the Ostia setting.
- **Corpus map.** `python cic/engine/corpus_map_merge.py --check` exits 0. The bucket holds 113 rows on 60 works. These are Tertullian's 32 (including the *Appendix*), both Cyprian works, the Passion (English and Robinson), the *Octavius*, both Commodian poems, Arnobius, and Lactantius's four (no *De mortibus*). The Montanism bucket holds the seven co-assigned works.

### Not verified

- I did not open the date ranges for Commodian, the *Octavius* and Arnobius in Monceaux or in Schanz–Hosius–Krüger. I checked them against Step 0 only.
- I did not check Monceaux's 213 for the break.
- I did not re-verify the claim that the visions of Perpetua and Saturus are their own writing.
- I checked the Kroymann Latin (*trinitatis*, *substantiae*, *personas* near line 11686) only for whether the words are present, not for the reading.
- I did not check Step 0 §2 A2's statement about Tertullian's attack on the bishop's authority to forgive.
- I did not check whether the Article 4 wording matches the Step 0 header word for word.
- I did not consult any post-1930 scholarship.
