# Step 0 Movement-Scope Confirmations, Apologist Pair — Round 6 Independent Adversarial Review

**Reviewed documents (revision of 2026-09-29):**
- `Build/worlds/grkap/Step0_Movement_Scope_Confirmation.md` (Atlas I.35), committed at `5f76ca01`, with `Build/worlds/_cross-world/dossiers/greek-apologists-second-century_Source_Readiness_Dossier.md` (same commit).
- `Build/worlds/latap/Step0_Movement_Scope_Confirmation.md` (Atlas I.43, absorbing I.17), uncommitted working-tree revision on top of `5f76ca01`, with `Build/worlds/_cross-world/dossiers/latin-apologists_Source_Readiness_Dossier.md` (also uncommitted).

**Prior rounds:** `Step0_Round1_Review.md` to `Step0_Round5_Review.md`. Round 5 returned NO SUBSTANTIAL REVISION REQUIRED for both documents as they then stood (R30–R35, all LOW). Both documents were since revised: a ruling pass after Round 5 (Justin co-ownership; Tertullian merger), then the 2026-09-29 revision (window slate, Tatian ruling, dating research, original-language witnesses, re-derived shelf counts).

**Reviewer:** independent isolated agent. No part in drafting, revising, or in Rounds 1–5.

**Scope.** Targeted recheck. Primary target: material added or changed after Round 5 (`git diff HEAD~1` for grkap; `git diff` for the latap working tree). Settled Round 1–5 ground is not reopened, except where the repository has changed under a claim the document still makes.

**Output location.** This review is written only to `Build/worlds/grkap/Review-Artifacts/`, as instructed. It is not duplicated into `latap/Review-Artifacts/`.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## Verdicts

- **I.35 (Second-Century Greek Apologists): SUBSTANTIAL REVISION REQUIRED.** No HIGH. Three MODERATE (R36–R38), six LOW. The shelf counts and "shelf items for the Library thread" in B1, B3 and the dossier are stale against the corpus map committed in the same commit, and contradict the document's own §4 item 8. A census quotation marked "verified verbatim" is no longer in the census. The finding that the Syriac record is "over-broad" rests on a reading its own context does not support.
- **I.43 (Latin Apologists): SUBSTANTIAL REVISION REQUIRED.** No HIGH. Four MODERATE (R45–R48), seven LOW. Tertullian's word counts cannot be reproduced by the method the document says it used, and the same method gives different figures (the header total moves from 1,194,575 to about 1,203,740). Two confidence tags are stronger than the document's own evidence. The header still attributes the document's commissioning to the project lead with no verifiable record. Three census quotations no longer match the census.

Neither verdict touches a Tier. Both Tiers stand on the evidence as re-derived. Every fix below is a local correction, not a rewrite.

---

## Part A — I.35 findings

### R36. [MODERATE] B1, B3 and the dossier report the shelf as it stood before this commit's own staging fixes. They contradict §4 item 8 and the corpus map.

**Where.** grkap §3 B1, "Completing the roster" (line 125) and the first bullet under it (line 129); §3 B3, "Counting method" (line 145); dossier §1 (line 50) and "Shelf items for the Library thread" (lines 108–115).

**What I checked.** Parsed `cic/corpus-map/greek-apologists-second-century.yaml` and every `_staging/*.yaml` row naming the entry.

**What I found.**
- Roles: the shelf holds **36 `tradition` and 3 `context`** rows. Step 0 B1 and dossier §1 both say 37 and 2 ("the English *Hortatory Address* row and the Ambrose row"). The third `context` row is the Otto 1879 *Hortatory Address* row (`justin-martyr_opera-addubitata-grc-lat_otto1879.yaml`, note "Ruled 2026-09-29 … held here as context").
- B1's bullet says that Otto row "is still `role: tradition` … an item for the Library thread (§4 item 8)". §4 item 8(a) says the same row "is now `context`". The map agrees with item 8.
- B3 says "three rows name this entry alone". There are **four**: the Ambrose `context` row, the Apollinaris English row, and **both** *Hortatory Address* `context` rows (anf01 and Otto 1879).
- Dossier lines 108–115 present all four shelf items (Otto row role, Tatian "Provisional because…" note, Aristides one-sided date, *Diognetus* one-sided range) as open, "named and not decided here", and claims "Step 0 §4 item 8 lists the same four". Item 8 says all four were corrected. The map confirms all four corrections (Tatian note now "The row is `assigned`…"; Aristides note gives Hadrian or Antoninus Pius; *Diognetus* note gives both sides). The dossier's own header says its state is "on top of commit `d1140c9f`", i.e. before `5f76ca01` changed these rows, yet it shipped in `5f76ca01`.

**Why it matters.** These are factual claims about the Library, and one is a binding instruction to another thread to fix something already fixed.

**Fix.** B1: "36 rows are `tradition` and 3 are `context` (both *Hortatory Address* rows and the Ambrose row)"; delete the "still `role: tradition`" sentence. B3: "four rows". Dossier §1: same counts; replace the "Shelf items" paragraph with a one-line pointer to Step 0 §4 item 8 (corrected 2026-09-29); fix the §5 "Slate items on the shelf" bullet to match.

### R37. [MODERATE] §1's naming-note quotation, marked "verified verbatim", is not in the census any more.

**Where.** grkap §1, "Naming note" (line 24).

**What I checked.** Parsed `cic-website/data/world-census.json`; searched every field of I.35 (and the whole file) for "genre rather than a community", "settlement with a bishop", "honest".

**What I found.** Zero hits anywhere in the census. I.35's `why` field is now entirely different ("For eighty years, Christian writers handed Roman emperors formal defenses…"). Round 5 verified the quotation in `why`; the census has been rewritten since. The objection itself survives only in `Build/worlds/_cross-world/NEEDS-RULING.md` line 24 ("The entry's own record states the objection against it — that apologetic is a genre rather than a community"), in different words.

**Why it matters.** CLAUDE.md: every quotation is re-verified verbatim before a record passes review, and "verified" is a claim to re-check. The substance (the genre-vs-community objection is live) is not in doubt, but the cited source and the verbatim claim are both wrong now.

**Fix.** Re-source to NEEDS-RULING.md and quote it exactly, or state that the census once carried the objection and no longer does. Drop "verified verbatim".

### R38. [MODERATE] The finding that the Syriac record's clause is "over-broad" rests on a reading that the record's own context does not support.

**Where.** grkap §2 A2, "What the Syriac record's sentence can bear" (line 74); §4 item 2 (line 203); dossier §5 first bullet; and the Library decision log entry "Window slate … approved", paragraph **Changed** (append-only, so it stays as written).

**What I checked.** Read `records/syr/source/syr.source.tatian-address-to-greeks.md` lines 44–52 and `records/syr/figure/syr.figure.tatian.md` lines 36–44 (records read-only). Grepped all of `records/syr/` for "Justin" (4 occurrences in 3 files, all naming him as Tatian's teacher; none about his death) and for any citation of *HE* IV.16.

**What I found.** The clause sits inside the paragraph "THE ENCRATITE CHARGE, HANDLED HONESTLY. Eusebius accuses him of it … it is an apology addressed to Greeks, written before the events Eusebius describes". The sentence before it names the Encratite charge, and the companion figure record cites exactly "Eusebius IV.29 carries the Encratite heresy charge against him personally". Nothing in `records/syr/` refers to *HE* IV.16 or to Justin's death. Read in its own paragraph, "the events Eusebius describes" are the Encratite events. On the document's own analysis that claim is "reasonably supported". Reading (a), Justin's death by Crescens's plot, is not a reading the record invites. The grkap text calls the clause "ambiguous" and "not supported as worded"; the dossier and the log flatly say it "holds for the break … and not for Justin's death" and is "over-broad".

The record's real, checkable defect is the one the document also names: "Eusebius accuses him of it". The earliest accuser is Irenaeus (*AH* I.28.1, verified below), whom Eusebius quotes (*HE* IV.29.2–3). The record's `formation_confidence: Documented` is also over-strong for a relative-date claim that §2 A2 itself tags Dominant Modern Reconstruction.

**Why it matters.** This is a characterization of a live built world's canonical record. It is now written into an append-only log and two documents. It would send the Syriac thread after a defect of the wrong kind.

**Fix.** In grkap §2 A2 and §4 item 2 and in the dossier: say the clause, read in its own paragraph, refers to the Encratite charge and is supported there as a Dominant Modern Reconstruction (not Documented); say that out of context it could be misread as covering Justin's death, which the record does not claim; keep the "Irenaeus, followed by Eusebius" correction as the real defect. The log cannot be rewritten; if the Library thread agrees, it records a new entry that refines "over-broad" (append-only rule).

### R39. [LOW] The Justin ruling paragraph still says a cross-build flag "is added" to `pahc.figure.justin.md` as part of the ruling. That is the kind of sentence Mark's 2026-09-29 ruling excludes from a world's own records.

**Where.** grkap §3 B3, "Ruling: Justin is co-owned" (line 169), sentence beginning "A cross-build flag is added".

**What I found.** `records/pahc/figure/pahc.figure.justin.md` lines 44–46 do carry the flag ("Justin belongs at least as much to the Second-Century Greek Apologists world … the Antony model"). The next paragraph (line 171) reports the new ruling and that the flag's fate is flagged to Mark. But the ruling paragraph itself still presents the flag as a standing part of the ruling, in the present tense and as "an addition on Antony's own precedent". A Doc_01 builder reading only the ruling paragraph would take the flag as endorsed.

**Fix.** Recast in the past tense: the flag was added under the earlier ruling; whether it stays is Mark's open decision (LIBRARY-DECISION-LOG.md, "Cross-world ownership is recorded in the references…", **Follow-up not ruled**). Also cite the only written record of the Justin ruling itself (see Part C, item 4).

### R40. [LOW] §6 counts "four entries dated 2026-09-29" that bear on the document. There are three; two of the four names are the same entry.

**Where.** grkap §6, "Revision of 2026-09-29" (line 235); dossier header line 15 ("four entries of that date").

**What I found.** The log holds five 2026-09-29 entries. Three bear on the Apologists: the window slate, the cross-world-ownership entry, and the Tatian entry. "Cross-world ownership in the references" and "the entry recording where ownership is written" are the same entry (line 51). The other two 2026-09-29 entries concern Ottoman Orthodoxy.

**Fix.** "three entries".

### R41. [LOW] Puech is cited at "pp. ~100–101". The passage is on p. 151.

**Where.** grkap §2 A2, public-domain scholarship list (line 62).

**What I found.** In `lesapologistesgr00puec_djvu.txt` the passage ("c'est dans les deux ou trois années antérieures qu'on peut placer avec quelque vraisemblance cette composition"; "les termes dans lesquels il parle de Justin nous inclinent à croire que celui-ci était déjà mort"; rejection of "les hypothèses de Harnack") runs under the running head "TATIEN 151". The content is attributed correctly; only the page is wrong.

**Fix.** "p. 151".

### R42. [LOW] Two quotations are not verbatim: a word inserted inside quotation marks, and a word substituted.

**Where.** (a) grkap §4 item 4, Ambrose bullet (line 213). (b) §6, §3 B3 change note (line 240).

**What I found.** (a) The document quotes the inscription as "A memorial (hypomnemata) which Ambrose, a chief man of Greece, wrote: …". In `anf08` (69480–69485) "(hypomnemata)" is not in the text; the Greek ὑπομνήματα is in an editor's footnote. (b) The Tatian shelf note that "no longer exists" is quoted as "the project lead may want a ruling on where his voice sits". The note read "Mark may want a ruling…" (Round 5 quotes it verbatim).

**Fix.** (a) Use square brackets for the gloss, or move it outside the quotation. (b) Quote the old note as it read, or paraphrase it without quotation marks.

### R43. [LOW] "'original founder' of the Severians (IV.29.6)" narrows what Eusebius says.

**Where.** grkap §2 A2, line 74.

**What I found.** `npnf201` 26422–26426: "But their original founder, Tatian, formed a certain combination and collection of the Gospels". McGiffert's notes on IV.29.4–6 read "their" as the Encratites in the wide sense and call Eusebius's link of Tatian to the Severians "quite out of the question". Presenting "original founder" as Eusebius calling Tatian founder *of the Severians* takes one side of a reading McGiffert disputes, in a paragraph about how far the Syriac record's wording can be trusted.

**Fix.** "as 'original founder' of the Encratite current, into which he folds the Severians (IV.29.4–6)".

### R44. [LOW] The grkap dossier still calls Commodian's *Carmen apologeticum* "the one Commodian work explicitly not vendored".

**Where.** grkap dossier §4, Commodian row.

**What I found.** The Latin of the *Carmen* is on the shelf since 2026-09-29 (`commodian_carmen-apologeticum-lat_dombart1887-csel-tei.txt` and the CSEL 15 scan; two rows on `latin-apologists.yaml`). What is missing is an English translation, which is what the Latin dossier now says.

**Fix.** "the one Commodian work with no English translation; its Latin was vendored 2026-09-29".

*Cosmetic, not findings (I.35):*
- Tier paragraph (line 196): Tatian is placed in two of the "four groups" ("unclaimed by any PAHC record" and "claimed in a built world's own records at lighter weight"), and the lead-in says all four groups "carry their own, lighter claims elsewhere", which the first group, by definition, does not. The roster sentence runs to about 130 words. One sentence per group would fix both.
- Zahn 1881 is the only scholarly citation in §2 A2 without an archive.org id. Bardenhewer (p. 58) independently confirms the locus ("Forschungen … Erlangen, 1881, i. 268 ff."), which fits pp. 275–280. I could not locate Forschungen I on archive.org to check the quotation "etwa um 150" (see Verifications).

---

## Part B — I.43 findings

### R45. [MODERATE] Tertullian's word counts cannot be reproduced by the method the document says it used. That method gives different figures, and it confirms the corpus map's 187k for *Against Marcion*, not the document's 183,788.

**Where.** latap header (line 3); §3 B1 Tertullian paragraph (line 77), "Combined total" (line 79), "methodological note"; Section B conclusion (line 125); dossier §1 table and "What the 1,194,575 figure covers".

**What I checked.** The document's stated method: "the text between one work's own opening `<div2>` tag and the next", tags removed, whitespace tokens counted, "the same practice this document uses throughout for the original four authors' figures". I ran exactly that over `anf03`, `anf04`, `anf06` and `anf07` (regex tag strip, stop at `</div1>`, whitespace split; lxml is not installed in this container).

**What I found.** The method reproduces the original four **to the word**: *Octavius* 23,819; *Instructiones* 15,008; Arnobius 140,826; Lactantius fragments 3,932 (the three larger Lactantius works come within 15 words). It does **not** reproduce the Tertullian figures:

| work | document | same method | difference |
|---|---|---|---|
| *Five Books Against Marcion* | 183,788 | 187,134 | +3,346 |
| *Apology* | 38,392 | 38,163 | −229 |
| *A Treatise on the Soul* | 49,399 | 49,425 | +26 |
| *On the Resurrection of the Flesh* | 45,592 | 46,242 | +650 |
| *Ad Nationes* | 34,840 | 34,919 | +79 |
| *Appendix* (poems) | 31,817 | 32,001 | +184 |
| *Against Praxeas* | 31,174 | 31,933 | +759 |
| *On Modesty* | 25,582 | 26,183 | +601 |
| *Against Hermogenes* | 22,941 | 23,066 | +125 |
| *An Answer to the Jews* | 21,645 | 22,346 | +701 |
| *Prescription* | 20,653 | 20,936 | +283 |
| *On the Flesh of Christ* | 20,055 | 20,148 | +93 |
| *On Monogamy* | 13,554 | 13,766 | +212 |
| *Ad Martyras* | 2,700 | 2,677 | −23 |
| *Passion of Perpetua* | 7,299 | 7,325 | +26 |
| **All 32 Tertullian works** | **722,479** | **731,618** | +9,139 |
| **Combined (464,797 + 32 + Passion)** | **1,194,575** | **1,203,740** | +9,165 |

The differences run in both directions, so they are not one systematic offset. Excluding `<note>` elements, or joining at tags instead of splitting, does not reproduce the document's figures either (e.g. *Apology* 38,062 or 37,182; *Marcion* 184,268 or 157,388). The document also says its 183,788 is "the more precise" figure and "close to, and confirming" the map's "187k". The stated method gives 187,134, which confirms the map and not the document.

Separately, the "methodological note" says the method is "confirmed accurate to within a few dozen words" and cites 23,819 against 23,959 and 15,008 against 15,117. Those differences are 140 and 109 words.

**Why it matters.** The header, B1 and the Tier all carry 1,194,575 as a figure "recounted directly … not merely asserted". It is not reproducible. The Tier does not move: either total is well over a million words.

**Fix.** Re-run the extraction with the method written out exactly (tag handling, tokenizer, boundaries), publish per-work figures from that run, and correct the header, B1, the Tier sentence and the dossier table. Drop "more precise" and "confirming" unless the re-run supports them. Replace "a few dozen words" with the real differences.

### R46. [MODERATE] Two confidence tags are stronger than the document's own cited evidence.

**Where.** (a) §4 item 1, Commodian (line 146): "That he wrote after Cyprian's death (258) and after the *Octavius* is `Widely Accepted` among the public-domain authors named". (b) §4 item 5 dating table (line 176): *De mortibus persecutorum* "`Widely Accepted` for 313–314".

**What I checked.** (a) Dombart's preface in `commodian_carmina-lat_dombart-csel15.txt` (lines 145–152, 203–213, 283–287, 11902–11909); Harnack, *Geschichte der altchristlichen Litteratur* II.2 (archive.org `p2geschichtedera02harnuoft`); Monceaux III (vendored, lines 37333–37390, 37704–37716); the document's own table. (b) The document's own table row.

**What I found.**
- (a) Among the authors the item itself names, the "after 258" claim is held by Harnack ("Also kann er nicht vor c. 260 geschrieben haben"), Monceaux ("ne sont pas antérieurs à 260") and Aubé (260). It is **contradicted** by the rest of the list. Dombart dates the poems "media fere parte tertii post Christum saeculi" and reads the "seventh persecution" as Decius's (249–251). Ebert has 249 for the *Carmen* and the *Instructiones* earlier. Teuffel–Schwabe has c. 238. Bardenhewer, in the table, has "about the middle of the third century". Harnack himself reports that before him "Fast alle Gelehrten … stimmten ihm [Ebert, 249] bei". Dombart's lines 205–212 and 285–286, cited as support, show only that Commodian used Cyprian's writings and read Tertullian and Minucius. That makes him later than those writings, not later than Cyprian's death. The "after the *Octavius*" half does rest on Dombart line 285 ("Tertullianeae et Minucianae lectionis … uestigia"), but it is not independent of the Minucius date question.
- (b) The row names three authorities: Harnack for 313–314, and Seeck (317–321) and Brandt (April 315) dissenting. One supporting source against two named dissents is not Widely Accepted.

**Fix.** (a) Split the tag. "After the *Octavius* and using Cyprian's writings": Widely Accepted. "After Cyprian's death (258)": Contested (Harnack, Monceaux, Aubé against Dombart, Ebert, Teuffel–Schwabe, Bardenhewer). (b) Tag 313–314 as Dominant Modern Reconstruction at most, or Contested with the three dates stated.

### R47. [MODERATE] The header still says "Prepared at the project lead's direct request". No verifiable record of that request exists. The I.35 revision removed the identical sentence for exactly that reason; I.35's treatment is right.

**Where.** latap header (line 3).

**What I checked.** `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md` (all entries); `Build/Ministry/Operations/Standing/*.md` (grep "Apologist", "Tertullian", "direct request", "I.17"); the Round 1–5 artifacts; the git log. The clone is shallow (811 commits, starting 2026-09-20), so the 2026-09-10 drafting commits are not reachable.

**What I found.** The only written trace is `CiC_System_Hub_Decision_Log.md`, entry "2026-09-26 — Two cross-world rulings' attribution…". It **quotes the Step 0's own phrase** ("leaving only 'prepared at the project lead's direct request,' which describes who commissioned the document") and adds no independent evidence of the request: no quotation of Mark, no date, no thread. A record that restates the document's own claim does not verify it. `cic-build-cycle` names "content fabricated-attributed to 'the project lead'" as a failure mode and sets the bar as "a real, checkable record, not a claim". The two sibling documents now make opposite choices on the same unverified sentence.

**Fix.** Delete the sentence, as I.35 did, and record the removal in §6. If Mark confirms that he commissioned both assessments, the Library thread records his words in a log entry. The sentence can then return in both documents with a citation.

### R48. [MODERATE] Three census quotations no longer match the census.

**Where.** latap §0 (line 12): registered "as 'the least thin of the five gaps'". §1 naming note (line 20): "the census's own registration text names this candidate's honest objection as *stronger* than I.35's". §2 A5 (line 61): "the census's own I.43 `legacy` field already says … 'the Latin vocabulary of Christian argument was largely made here, and in Tertullian's hands at the same time'".

**What I checked.** Parsed `cic-website/data/world-census.json` and searched I.43 and the whole file.

**What I found.** "least thin" appears nowhere in the census. The nearest text is NEEDS-RULING.md line 49, "The least thin of the five". I.43's `legacy` now reads "The Latin vocabulary of Christian argument was made here. Tertullian coined most of the technical words…". "largely" and "in Tertullian's hands at the same time" are gone, and so is the document's inference that "'at the same time' now folds directly into 'here'". No census field carries the genre-vs-community objection or its "stronger" comparison. The census was rewritten for the merger after Round 5 verified these strings. The claims are not fabricated, but the quotations and the present-tense "already says" are now false.

**Fix.** Re-quote the current `legacy` (it supports the same point more directly), cite NEEDS-RULING.md for "least thin" with its exact words, and re-source the naming note or say the census no longer carries it.

### R49. [LOW] Monceaux: "only … volumes I and III is in `cic/texts/`". All six volumes are vendored.

**Where.** latap §3 B1 "Still missing" (line 94). The dossier §2 names I and III accurately as the ones cited, but also implies they are the only ones.

**What I found.** `cic/texts/` holds `monceaux_histoire-litteraire-afrique-chretienne-tome1_1901.txt` through `tome6_1922.txt`.

**Fix.** "Monceaux's *Histoire littéraire* (all six volumes vendored; volumes I and III cited here)".

### R50. [LOW] "eleven author keys across 39 works" on I.35's shelf. It is 17 works in 39 rows.

**Where.** latap §3 B3, I.35 bullet (line 107).

**What I found.** Parsed shelf: 11 author keys, **17 works, 39 rows**. The I.35 Step 0 says 17 and 39 correctly.

**Fix.** "eleven author keys across 17 works (39 rows)".

### R51. [LOW] The Minucius lower limit is tagged `Documented`, but the date it yields (c. 160) is an inference the sentence itself labels as one.

**Where.** §4 item 1, first paragraph (line 133).

**What I found.** The Fronto mentions are verified (Halm TEI line 927, *Cirtensis nostri … oratio*; lines 3476–3477, *tuus Fronto*). The textual fact is Documented. "Not earlier than … about 160" rests on Fronto's dates, which the document says are "an inference; Fronto's dates are not in the vendored files".

**Fix.** Tag the mention Documented and the c. 160 limit Widely Accepted or Dominant Modern Reconstruction.

### R52. [LOW] Wallis (ANF04) is listed as proposing "about 166". He states that date only as the consequence of one hypothesis.

**Where.** §4 item 1 table, pole A (line 137); "ANF04 itself gives two dates, Coxe's and Wallis's".

**What I found.** `anf04` 17131–17146: "The date of its composition is still a matter of keen dispute … If, on the other hand, Tertullian borrowed from Minucius, the *Octavius* was written probably about the year 166". Wallis sets out both conditionals and adopts neither. Coxe's "[a.d. 210.]" is a real proposal (17040–17062, verified).

**Fix.** Move Wallis out of pole A, or list him as "states both conditionals (c. 166 if Minucius is first; early third century if Tertullian is first)".

### R53. [LOW] A Latin quotation silently corrects its source file.

**Where.** §4 item 5, "Two spirits, and a caution" (line 167): "deinde fecit alterum, in quo indoles diuinae stirpis non permansit" (Brandt's TEI, lines 7395–7397).

**What I found.** Line 7395 reads "deinde fecit **alterom**". The correction is certainly right, but the file is the one the document names as "the preferred base for quoting".

**Fix.** Quote as found with "[alterum]", or note the OCR slip.

### R54. [LOW] The list of census phrases for the census owner to correct is incomplete.

**Where.** §4 item 1, rule (a) (line 144); §6 last paragraph; dossier §5 "Stale references elsewhere".

**What I found.** Besides the phrases the document lists (`voices` "opened the whole enterprise in 197"; `why` "The argument he opened ran a further century, through Minucius Felix's dialogue"; the edge note "opens the Latin case"), the census also says: I.43 `relationsSummary` "Tertullian, whose Latin apologetic writing opened the tradition … before the other authors continued it"; I.43 `longDescription` "Roughly a generation on … Minucius Felix", which settles the pole-B order; and I.17 `relationsSummary` "opened the entire tradition of Latin Christian argument". The edge's own confidence is "Documented".

**Fix.** Add the three phrases, and the edge's `Documented` tag, to the list put to the project lead.

### R55. [LOW] Quotation truncated with a changed stop.

**Where.** §4 item 1 (line 131): "Three of the five are barely datable: Minucius Felix within a century, Commodian within three centuries."

**What I found.** The census continues after a semicolon: "…within three centuries; Tertullian's own dates, roughly 197 to 220, are the best anchored of the set." The full sentence names only two of its "three". Cutting it at a full stop hides that inconsistency, which is the census's own.

**Fix.** Quote to the semicolon with an ellipsis, and note that the census names only two.

*Cosmetic, not findings (I.43):* §2 A5 says "the same **Article 5** principle §2 A5 of I.35's own sibling document states". The principle is Methodology Section A5, not a Constitution article.

---

## Part C — Attribution discipline (scope item 4)

Every place either Step 0 attributes something to the project lead or to Mark, and whether a checkable record exists.

| # | Where | Attribution | Record found | Wording safe? |
|---|---|---|---|---|
| 1 | grkap §2 A5 (line 98); latap §4 item 1 (line 131) | Mark's words on the slate: "yes, approve the slate and proceed" | LIBRARY-DECISION-LOG.md, 2026-09-29 "Window slate…", quoted verbatim | **Yes.** Both quote it exactly. The slate texts both documents quote are the Library's summary in that entry, not Mark's words, and both present them as "the slate", not as his words. Correct. |
| 2 | grkap §3 B3 (line 171); dossier §5 | Mark's words on cross-world ownership: "that shouldnt be something he says…" | Same log, "Cross-world ownership is recorded in the references…", verbatim, including his spelling | **Yes.** |
| 3 | grkap §3 B3 (line 175), §4 item 2, §6; dossier §5 | Tatian ruling: "if a voice influcences three worlds…" | Same log, "A voice may belong to several worlds…", verbatim | **Yes, with a caveat the document already states.** The co-ownership reading and the general rule are the Library's reading, "stated back to Mark in the session for correction". No record shows he confirmed it. grkap says exactly this at line 175. §6's "resolved by Mark's ruling of 2026-09-29" is supported by the log's own heading. |
| 4 | grkap §3 B3, §4 item 1, §6 ("Two ruling passes followed, recording a direct ruling on the Justin question") | Justin co-ownership | `CiC_System_Hub_Decision_Log.md`, 2026-09-26 entry, records it as "Mark's ruling (2026-09-10)". That entry was written by the cleanup gate from the documents' own earlier text and quotes no words of Mark's. No log entry quotes him on Justin. | **Safe as worded**: the current text does not name Mark. But it should cite the Hub log entry as its only record. The Justin ruling is a cross-world decision; if the Hub entry is not accepted as a record, it needs Mark's confirmation in his own words. |
| 5 | latap §2 A5, §4 item 4, §6 ("The ruling is the disposition"; "A ruling pass followed the fifth round") | Tertullian/Article 21 merger; census I.17 status change | Same Hub log entry, same derivative character ("Mark's ruling (2026-09-10)"). The census does show I.17 as "Within Another World (A5)". | **Safe as worded**: Mark is not named. Same recommendation as row 4. |
| 6 | latap header (line 3) | "Prepared at the project lead's direct request" | None independent (R47) | **No.** Remove, as grkap did. |
| 7 | grkap §6 (line 237) | Records the removal of the "direct request" sentence as unverifiable | — | **Right.** |
| 8 | latap §4 item 6; §6 last paragraph; grkap §3 B3 (line 171) | Matters "for the project lead" / "flagged to Mark" | Log "Follow-up not ruled" for the cross-build flags | **Yes.** These route open decisions to Mark rather than attribute decisions to him. |
| 9 | Corpus-map notes quoted by grkap §2 A5 ("Ruled 2026-09-29 (Mark approved the Apologists window slate…)") | Slate approval | Log entry 1 | **Yes.** (See Part E on the note's form.) |

**Which treatment of "direct request" is right.** Removal, as grkap did. The skill's bar is "a real, checkable record, not a claim". The only record is a later log entry that repeats the sentence. The sentence is probably true, but probability is not the bar, and the pair should not disagree on the same fact.

---

## Part D — Consistency (scope item 5)

- **grkap Step 0 ↔ dossier.** Consistent on 17 works, 39 rows, 22 original-language rows (6 primary, 16 second), the Apollinaris rows, the Tatian ruling, the Syriac sentence and the cross-build flags. They are consistently **wrong together** on roles 37/2 (R36). They contradict each other on the four shelf items: Step 0 §4 item 8 says corrected, dossier says open (R36).
- **latap Step 0 ↔ dossier.** Consistent: 43 works, 96 rows, 42/54, per-author counts, 94/2 roles, 6 provisional / 37 assigned, 16 CSEL + 15 Oehler-only + 1 no-Latin (recounted), Montanism seven, LPC's two Cyprian works, Perpetua, CIL8 note. Both carry the unreproducible word counts (R45).
- **Between the two Step 0s.** Aristo (three entries, same note), Tatian, Justin and the Perpetua/Cyprian statements agree. latap's "39 works" for I.35 is wrong (R50). latap's I.35 bullet ("no figure overlap") holds: none of latap's seven author keys is on the I.35 shelf.
- **Against the approved slate (decision log).** Hortatory Address as `context`: the map agrees (both grkap rows `context`; PAHC rows unchanged). Ambrose leaves the roster, Greek Apologists row `context`, Syriac `transmission` kept: agrees. Minucius and Commodian stay, Contested: agrees (Commodian `provisional` on both works; Minucius `assigned`, its date Contested in text). "Doc_01 must not say Tertullian's 197 *Apology* 'opens' the Latin case": latap binds it at §4 item 1 rule (a), and I found no residual "opens"/"opening work" claim in latap's own voice (the diff removes the three earlier ones). The list for the census owner is incomplete (R54).
- **Against the Syriac world's records.** See R38. The "over-broad" characterization does not survive a reading of the record in its own paragraph.

---

## Part E — Escalations (scope item 6)

1. **Cross-build flags already in canonical records**: `pahc.figure.justin.md` lines 44–46 and `alx.figure.antony.md`. These are exactly what Mark's 2026-09-29 ruling excludes ("he talks from his own world perpsective only, it is noted in the references"). Already flagged to Mark in the log. **Needs the project lead.** The documents correctly leave it open. grkap's ruling paragraph should stop presenting the flag as part of the ruling (R39).
2. **Justin co-ownership and the Tertullian merger (I.17 → I.43)** are both cross-world/portfolio decisions (the second changed a census status). Their only written record is a derivative Hub-log entry with no quotation of Mark (Part C rows 4–5). **Needs the project lead only for confirmation**, if the Hub entry is not accepted as the record. Nothing in the revision treats either as newly decided.
3. **Tatian co-ownership as a general rule** ("a voice that shaped several worlds of one era is a shared feature"). The log records this as the Library's reading, stated back for correction, with no confirmation on file. grkap applies it only to Tatian and says so. latap does not rely on it. **No new escalation**, but it should not be applied to any third figure until Mark confirms.
4. **Census wording** ("opened"/"opens", and R54's additional phrases) and **IJC's Lactantius record** (authorship dispute unstated; `author` field dated from an NPNF gloss). Both documents route these to the project lead and edit nothing. **Correctly escalated.**
5. **The Syriac record** (R38). Any change to `syr.source.tatian-address-to-greeks.md` belongs to the Syriac world's own thread. The Library log cannot be rewritten, so a refinement needs a new entry. This is a cross-world matter; **flag to the project lead** with R38's corrected characterization.
6. **Review-cycle cap.** Both documents cleared Round 5. This is the first call for substantial revision since, and it is triggered by new material (the slate, the dating research, the merged corpus). I do not read it as a fourth consecutive substantial round under the cap. But the documents have now been through six rounds, and the project lead may want to say how the cap counts a document that cleared and then took on new material. **Named, not decided here.**
7. **Out of scope, flagged not touched (CLAUDE.md default: doc-hygiene on content that isn't this thread's).** Several corpus-map notes on the Greek Apologists shelf now carry process narration inside a canonical, generated file, e.g. the Ambrose row: "Ruled 2026-09-29 (Mark approved …) … Earlier note follows." `tools/check_live_commentary.py` should be run on `cic/corpus-map/`; this belongs to the Library thread.

No Representative identity or title decision is present in either document. No governance or methodology change is made. §5 of each (the "third mode" question) is correctly left to System Hub.

---

## Part F — Fabrication, register and the job of a Step 0 (scope items 7 and 8)

- **Invented detail.** None found. Every ancient quotation sampled matches its vendored file (Part G). All scholarly positions sampled are attributed to the right author, except the page (R41), the Wallis conditional (R52) and the Commodian tag (R46).
- **Register.** The new material is mostly plain and short-sentenced, a clear improvement on earlier revisions. Remaining over-long sentences that hide claims: the grkap Tier roster sentence (about 130 words, see Part A cosmetic notes), and latap §2 A2's Tertullian paragraph, which is untouched ground. No disclaimer-as-crutch or assistant cadence in the new text. The "UNVERIFIED, from memory" markers for post-1930 scholarship are honest limits, not crutches.
- **Does each still do a Step 0's job?** Yes. Both keep tier reasoning, source sufficiency (now with original-language witnesses stated by header status), overlap with every built world (re-swept, with method), and disclosure obligations. **Tier changes are stated, not silent.** grkap removes "conditional on one remaining ruling" and says why (§6, the Tatian ruling). latap moves the dating condition from "remaining" to "supplied, awaiting review" and says so. Neither change is wrong, and neither is affected by the findings above.

---

## Part G — Verifications performed (reproducible)

**Corpus maps** (Python `yaml`, `cic/corpus-map/*.yaml` and all `_staging/*.yaml` `assignments`):
- `greek-apologists-second-century.yaml`: 17 works, 39 rows; 17 ANF rows, 22 other; confidence 13 works assigned / 4 provisional (rows 32/7); roles by row 36 `tradition` / 3 `context`; 11 author keys (justin_martyr 6, athenagoras 2, nine others 1).
- Cross-join by title across `_staging/`: PAHC 16 of 17 (all but Ambrose); Syriac 2 (Tatian, Ambrose); union 17; alone 0; third buckets `ebionite-nazoraean-current` (Aristo) and `montanism-the-new-prophecy` (Apollinaris, `context` rows). Rows naming grkap alone: 4 (Ambrose; Apollinaris anf08; *Hortatory* anf01; *Hortatory* Otto 1879).
- Notes verified verbatim: Tatian (grkap, pahc, syr identical, "The row is `assigned`…"); Aristides (both readings); *Diognetus* (both sides); *Hortatory* anf01 and Otto 1879 (`context`, "Ruled 2026-09-29"); *Discourse* and *Sole Government*; Ambrose.
- `post-apostolic-house-church.yaml`: 8 `justin_martyr` works in 14 rows (6 with an original-language row), plus `martyrdom_of_justin`; Tertullian *Apology* 2 rows, *Marcion* 3 rows, both `provisional`.
- `latin-apologists.yaml`: 43 works, 96 rows, 42 ANF / 54 other; authors Tertullian 32, Lactantius 4, Commodian 2, Cyprian 2, Arnobius 1, felix 1, passion_of_perpetua 1; roles 94 `tradition` / 2 `transmission` (*Vanity of Idols*); 6 provisional works; 42 of 43 with an original-language row (the *Appendix* has none); Tertullian 16 CSEL + 15 Oehler-only (list matches latap's fifteen exactly) + 1.
- Montanism co-assignment: 7 works (*Fasting*, *Modesty*, *Monogamy* `assigned`; *Veiling*, *Exhortation*, *De Fuga*, *Praxeas* `provisional`). LPC: *Ad Demetrianum* `assigned`, *Vanity* `provisional`/`tradition`, Hartel whole-volume row. The "On Patience" title collision with LPC is Augustine's *De patientia*, not a shared work. `tertullian-s-voice.yaml` absent.

**Census** (`cic-website/data/world-census.json`, `movements`): I.35 `voices`, `sourcing`, `why` (naming-note text absent, R37); I.43 `voices` (Tertullian first, "opened the whole enterprise in 197"), `region` (Carthage first), `sourcing` ("Three of the five…"), `why`, `legacy` (R48), `relationsSummary`, `longDescription` (R54); I.17 status "Within Another World (A5)", "roughly 197 to 220"; edge tertullian-s-voice→latin-apologists ("opens the Latin case", `Documented`); I.33 `documentedStories` *On Modesty* ch. 1 note verbatim; I.33 dossier: 0 hits for Minucius/Octavius.

**Ancient quotations and lines, grkap (20 sampled, all verbatim at the cited lines unless noted):** Irenaeus *AH* I.28.1 (`anf01` 33656–33675) and III.23.8 (43903–43913); Eusebius *HE* IV.16 notes (`npnf201` 23758–23784, "very difficult to determine", Rusticus 163; 23897 "puts himself on a level"); *Address* 18–19 quoted by Eusebius (24063–24077); *HE* IV.28 end (26183–26186); McGiffert on the *Chronicle* 172 and on Harnack's 152–153 (26213–26234, 26491–26495); McGiffert on IV.29 wine and "incorrect, if we are to accept Irenæus' account" (26281–26313); IV.29.6 "original founder" (26424, R43); Jerome *De vir.* 29 (`npnf203` 40084–40100); ANF02 "[a.d. 110–172.]" (5527–5528) and "established about a.d. 166" (5657); *Address* ch. 4 (5822–5823), 18 (6526), 19 (6548–6554), 25 (6820), 35 (7252); Otto 1851 "paullo post Iustini Martyris mortem" (1374–1375); Otto 1879 "maximeque ob stili differentiam" (211–214); ANF01 second-class notice (13900–13909); McGiffert on the *Discourse* and *Hortatory* (24268–24290); Ambrose endnote and inscription (`anf08` 69466–69486; R42); Aristides Syriac heading (Harris–Robinson 2140–2141); *HE* IV.3.3 note (21073–21090); Quadratus note (20996–21015); Melito note (25743–25775).

**Ancient quotations and lines, latap (22 sampled):** Jerome *Ep.* 84.7 (`npnf206` 19196–19212, verbatim including the "Institutes" sentence); *Ep.* 70.5 (16714–16718); *De vir.* 18 (`npnf203` 39878–39886), 53 (40489–40519), 58 (40642–40653, "Flourished 196?" gloss), 79 (41017–41022), 80 (41028–41056, "Died 325" gloss, Crispus); Gennadius 15 (42419–42432); Dombart preface 145–152, 203–213, 283–287, note 11902–11909; Arnobius I.13 (TEI 468–472), II.71 (4585–4589), IV.36 (7433–7438); Brandt TEI V.1.22 (22700–22707), VII (35341–35343, 35378–35383), II.8.4 (7394–7398, R53); Brandt CSEL 19 prolegomena (588–602; Brandt "prorsus negarem"); Halm TEI 9.6 (925–928) and 31.2 (3475–3478); ANF04 Coxe (17040–17062), Wallis (17120–17165, R52), Cirta gloss (17655–17657); ANF06 *Chronicle* passage (39060–39082) and "[a.d. 297–303.]" (38994); ANF07 V.1 "no ignoble rank among pleaders" (4470); Robinson "natale tunc Getae Caesaris" (1733–1738) and "highest degree probable" (3354–3365); ANF03 Perpetua "editor … not its author" and "about the year 202" (59447–59462); Waltzing "exeuntis saeculi secundi" (274–275). No Octavius/Apologeticum parallel passage is quoted in latap; the priority question was checked through the ANF04 notices and SHK instead.

**Scholarship against public-domain scans** (archive.org `_djvu.txt`, ids as given; vendored Monceaux):
- grkap (10): Harnack 1897 `b1geschichtederalt02harn`: Tatian "nicht später als c. 155", "Zwingend … nicht … wahrscheinlich ist sie nicht" (18070–18188), 12th year of Marcus = March 172/3 (18275); Quadratus "glaublich, aber nichts weniger als erwiesen" (17340–17356); Aristo 135–170, "um 140 nahe", "Wahrscheinlich war der Verfasser selbst ein Judenchrist" (17205–17222); Aristides 138–161 (17413–17455); *Hortatory* "2. Jahrh. lieber nicht angehört" (30169; the document's German word order differs, meaning unchanged); *Sole Government* "kaum möglich", "wirklich durchschlagende Gründe … kann ich nicht finden" (30140–30150); *Diognetus* "auf das 3. Jahrhundert oder frühestens auf den Schluss des 2." (30286–30294); Ambrose "griechischer Buleut Ambrosius im 3. Jahrh. … vor Diocletian's und Konstantin's Zeit", "Wer dieser Ambrosius gewesen ist, wissen wir nicht" (30336–30356). Harnack 1904 `p2geschichtedera02harnuoft`: *Hortatory* 221–302, later half (9068–9108). Bardenhewer 1908 `patrologyliveswo00bardrich`: Tatian pp. 57–58 ("probably in 172", "outside Rome (c. 35), and about 165", "more or less completely withdrawn"); pp. 53–54 (*Discourse* "may possibly belong to the second century", Ambrosius revision; *Hortatory* "very probably … end of the second or the beginning of the third"; Schürer, Völter, Dräseke, Asmus, Widmann). Puech 1912 `lesapologistesgr00puec`: Tatian c. 170–172 on p. 151 (R41); *Hortatory* "période 260–300", p. 233. Zahn 1881: *Forschungen* I not found on archive.org (searched `creator:Zahn`; the 1881 hit `forschungenzurge0000zahn` is Teil IV); Bardenhewer independently confirms "i. 268 ff." — **not verified**.
- latap (9): Harnack 1904 II.2: Commodian "nicht vor c. 260", Aubé 260, Kraus, Brewer 458/466, Jülicher 250–350, "Fast alle Gelehrten … stimmten ihm bei", "Der Ebertsche Ansatz aber (249) ist unhaltbar", Brewer quoted "um 458–460 in Südgallien", "paradoxen Ansatz" (24580–24925); Minucius "zwischen Maximinus Thrax und Decius", Cirta "zweifelhaft" (18520–18545), Schultze note (18287–18288); Arnobius *Chronicle* Latin "obsidibus pietatis foedus" and "zum Erweise seiner jüngst gewonnenen Christlichkeit" (23341–23346); Perpetua "Der Montanismus des Redaktors ist m. E. unverkennbar" (18068); Tertullian break "nicht später als 207/8", *De virg. vel.* and *De exhort.* pre-break (14720–14776). Schanz–Hosius–Krüger III 1922 `geschichtederrom00scha`: "zu einem allgemein anerkannten Ergebnis nicht geführt" (20506–20507), "über anderthalb Jahrhunderte auseinander" (20614–20615), Schanz before 161 / Hadrian, the editors Dombart, Baehrens, Boenig and Waltzing for the second century, *On Modesty* Callistus "das überwiegend Wahrscheinliche", Esser for Zephyrinus (23005–23020). Monceaux I (vendored): proposals note (32371–32395), "entre 213 et 250" (33090–33096), Cirta "probable, n'est pas certaine" (32919–32962), Perpetua "7 mars 203" (5622–5627), Tertullian table (17640–17720). Monceaux III: Ebert 249 (37333–37337), "ne sauraient guère être postérieures à l'année 313" (37384–37390), "entre 260 et 313", 305–313 "très vraisemblable" (37704–37716). Dombart and Waltzing as above. Not checked: Teuffel–Schwabe, Brewer 1906 table of contents, Bardenhewer 1901 (Fraktur), Boissier, Massebieau, Neumann (all as reported through the sources above).

**Records** (read-only): `records/pahc/` has 16 record-type directories; case-insensitive counts after re-joining hyphen-wrapped lines and deleting `anf0*` filename strings reproduce grkap's figures exactly: Justin 136/29, Melito 18/4, Quadratus 2/1, Aristo 2/1, Apollinaris 3/1, Theophilus 2/2 (`pahc.witness.jesus-as-god` line 67, `pahc.demo.center-jesus-as-god` line 45), Tatian, Athenagoras, Aristides, Diognetus and Ambrose 0. `records/syr/` Justin 4/3, all as Tatian's teacher. `_fleet` Theophilus source, contested-claim and modern-term records present. Tertullian in PAHC: two source records `etic`/`corroborating`, "never as a Native voice", "three core regions"; cited by exactly the five records latap names. `_fleet.source.tertullian-against-praxeas` `etic`/`load-bearing`/`Documented`, "does not carry the Latin text", cited by `_fleet.modern.trinity` and `_fleet.contested.theophilus-triad-referent`. `ijc.source.lactantius-de-mortibus` id in 10 IJC files. `lpc.core…` line 434 names `tertullian-s-voice` for Perpetua. `gallic.term.trial` and `desert.quote.never-kneel-saturday-to-sunday` as latap describes. `syr.source.tatian-address-to-greeks` lines 44–52 and `syr.figure.tatian` lines 36–44 (R38). `pahc.figure.justin` lines 42–46.

**Word counts:** div2-boundary extraction as described in R45, over `anf03`, `anf04`, `anf06`, `anf07`.

**Attribution:** LIBRARY-DECISION-LOG.md read in full for 2026-09-29; grep of `Build/Ministry/Operations/Standing/*.md` and all of `Build/**/*.md` for "direct request", "Mark's ruling (2026-09-10)", "Apologist", "Tertullian", "I.17"; `CiC_System_Hub_Decision_Log.md` 2026-09-26 entry read; `git show b9ad408c` diff read for the removed attributions; the repository is shallow (811 commits), so the 2026-09-10 commits are unavailable.

**Round 5 carry-over re-tested:** R30 (wine now attributed to McGiffert's note, §4 item 3) resolved; R31–R33 moot (§6 rewritten); R34 resolved (the Tier now names the Ambrose outcome); R35 resolved (latap B4 now cites §2 A5 "above" only). The Round 5 cosmetic note on §4 item 7's four subtypes is resolved (now sixteen directories).
