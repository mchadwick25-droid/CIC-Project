Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: Sonnet 5.5
Reviewer agent: a39d62e79285ad3b3
Drafter agent: not recorded in the build state (`build/aec_Build_State.yaml` names the drafter model only)
Round: 4
Truncation check, method 1: full read of `Doc_02_Source_Ecology.md` (209 lines, matching `wc -l`; all ten `## ` sections present, §1 to §10) and `Source_Registry.md` (66 lines; 26 table rows, numbered 1 to 21 with sub-rows 6a, 8a, 11a, 11b, 14a; the three closing sections present)
Truncation check, method 2: byte and tail check: `wc -c` gives 43,364 bytes for Doc_02 and 23,196 for the Registry; `tail -c` shows Doc_02 ending on the §10 line "Held pending the project lead's confirmation, matching Step 0's status." and the Registry ending on its Living-document protocol sentence; sha256 `aa1e7f47…7f197a` and `e51ce0f4…112dec` at `origin/main` `5136d7f58`

# Review of Doc_02 — Source Ecology, with `Source_Registry.md` (`aec`): cap-ruling targeted recheck

**Authority.** Mark ruled on 2026-10-29 that Step 0, Doc_01 and Doc_02 had each used the three-round cap without clearing, and ordered one more targeted Opus review of Doc_01 and Doc_02. This review is that one. **Under that ruling it does not count toward the three-round cap.** If it does not clear, the result goes back to Mark with the open findings. No further rounds run on the build thread's own initiative. This file covers Doc_02 and its companion `Source_Registry.md`.

**Gate note.** The `roundcount` gate excuses a review file only when a System Hub Decision Log entry headed "Cap ruling" names it. No such entry for `aec` exists in `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md` at `origin/main` `5136d7f58`. Until one names this file, the gate will count it.

**Scope and method.** This is a targeted recheck. It takes each Doc_02 and Registry finding left open by Round 3 (`Doc02_Round3_Review.md`), checks it against the current text, and then checks what changed after Round 3. Every quotation, and every claim about what a vendored file or the corpus map holds, was re-read directly in `cic/texts/` and `cic/corpus-map/`. No drafter claim of "verified" was relied on. Counts were re-run, each by two methods. I edited no document.

---

## Round 3 findings: status

| Round 3 finding | Status | Evidence |
|---|---|---|
| M1. The corrected Socrates quote was cited to the endnote (`ii.ix.iv-p6`), not Socrates' text (`ii.ix.iv-p2`) | **Closed** | §3 cites `ii.ix.iv-p2`. "he limited his attention to the literal sense of scripture, avoiding that which was mystical" is in Socrates' body text there, verbatim. Registry row 14a correctly places the "literal and historical meaning" wording in the endnote `ii.ix.iv-p6`, verbatim. |
| M2. Palladius was called an independent witness for Olympias | **Closed** | §6 now calls him "a partisan of Chrysostom". "embroiled in the disturbance connected with the blessed John" and "to Rome because of the blessed bishop John" are verbatim in `palladius_lausiac-history_clarke1918.txt`. The line numbers are wrong (finding D5). |
| M3. The Theodoret wording was not updated for the Letters split, and still used date-based framing in places | **Closed in substance; one residue open** (non-blocking, D8) | §1, §6, §7 and §8 apply the subject-based split. §2 still says "out-of-window by date". |
| M4. The Ammianus corpus-map row was not on the branch, so the "47 rows" claims were false | **Closed as stated, but overtaken** (finding D1) | The Ammianus row is on the bucket. The documents now say 50 rows. The bucket holds 66. |
| M5. Row 11a was rated D for a named, located work, and rows 6a and 8a were rated C | **Closed** | Rows 11a, 6a and 8a are now B, and each says why the corpus-map's `provisional` status is not a reliability rating. |
| M6. Row 11b said the *Eranistes* and Letters were carried at `provisional` | **Closed** | Row 11b now says `assigned`. The corpus-map rows for *Eranistes* and *Letters of the Blessed Theodoret* are `confidence: assigned`. |
| L1. The Sabaniana clause was placed in "the same chapter" as Olympias | **Closed** | §6 now places it in Chapter XLI, "Holy Women", fifteen chapters before LVI. Correct: 56 − 41 = 15. |
| L2. Row 11a cited canon XIII's verification to Doc_01 §4; row 11b used "drawn to avoid" framing | **Closed** | Row 11a cites Step 0 §2 (A1). Row 11b now says the boundary "closes at 430 because the census says so". |
| L3. The Living-document protocol omitted rows 14–18 | **Closed in substance** | The protocol now lists rows 1, 3, 5–12 and 14–20 as B or C. Checked row by row: rows 2, 4, 13, 14a and 21 are the only A rows. The sentence "listed in `Doc_02_Source_Ecology.md` §9" is loose, since §9 does not list them by number. That is cosmetic, D9. |
| L3 (audit trail). Rows 1, 6a, 8a, 11 and 14 credited changes to Round 2 findings that do not exist | **Closed** | All round credits have been removed from the rows. |
| Narration clean-up (required before any disposition) | **Closed** | No correction narration remains in Doc_02 or the Registry. `tools/check_live_commentary.py --surface worlds` flags only protected status, date and route-cue lines. |

## Verified at source this round (holds)

- §1, Eutropius (`npnf109` `xv.iii-p5`): "'Vanity of vanities, all is vanity'—it is always seasonable to utter this but more especially at the present time. Where are now the brilliant surroundings of thy consulship? where are the gleaming torches?" Verbatim. The document's extra quotation marks around the second clause are punctuation only. Row 4's `xv.iii-p11` "continually made war upon the Church has taken refuge within it" is verbatim.
- §1 and row 2, the Romans 12:20 homily (`npnf109` `xiii.ii`): `xiii.ii-p31` opens "Bear in mind then the things which are said here". "by so doing thou shalt heap coals of fire on his head" is present in the homily (file lines 16347 and 16424, the second inside `xiii.ii-p34`).
- §1 and row 1, Matthew Homily II (`npnf110` `iii.v-p2`/`p3`) opens on "The book of the generation of Jesus Christ, the Son of David, the Son of Abraham." Verbatim.
- §2, magister militum (`npnf109` `iii.ii-p9`): "His father, Secundus, was a distinguished military officer (magister militum) in the imperial army of Syria, and died". Verbatim.
- §4, *Adversus Judaeos*: `npnf109` `xix.ii-p12` speaks of "a certain discourse against the Jews, held in the month of September of the year 386" and then works through the Paschal-table problem. Socrates VI.3 (`ii.ix.iv-p2`): "While he continued in the capacity of a reader he composed the book Against the Jews." Both support the document's narrowed wording.
- §6, Olympias (Lausiac History, Chapter LVI): "[THAT] most venerable and devoted lady", "Seleucus the ex-count", "Ablavius the ex-prefect", "dispersed all her goods and gave to the poor", "instructed many women, addressed priests reverently, and honoured bishops". Verbatim; only the initial capitals are lowered. The Sabaniana clause is verbatim.
- §6, Eunomius's *First Apology* and Philostorgius: both files are present in `cic/texts/`, and neither is on this world's bucket.
- §1 and row 1: the bucket's Chrysostom series rows number 17 on `npnf110`–`npnf114`, matching the row's list.
- Row 13, Ammianus: Book XXII heads line 14773; the anger and the church closure are at 16184–16188; the *Misopogon* at 16236–16237. The Book XXVII.3 assignment to `imperial-juridical-christianity` exists.
- Rows 3, 4 and 9: the Statues, Eutropius, Olympias and Innocent rows are also on `imperial-juridical-christianity.yaml`, as stated.
- Rows 6a, 8a, 10, 12, 19 and 20: each corpus-map note matches what the row says about it. The Palladius *Dialogue* is now `confidence: assigned`, which the row does not contradict.

---

## New findings

### D1. Blocking (substantial). The bucket holds 66 work-rows, not 50, and the Registry covers only 50.

**Location.** Doc_02 §1: "holds 50 work-rows". The Registry header: "holds 50 work-rows … Every one of the 50 rows is covered by exactly one row below." The same figure appears in `Open_Gaps_Tracking.md` entry 15.

**Evidence, two methods.**
1. Parsing `cic/corpus-map/antiochene-exegetical-christianity-chrysostom-ce.yaml` with PyYAML gives `len(works) == 66`.
2. Counting `^- row_id:` lines with `grep -c` gives 66.

Mapping each corpus-map row to a Registry row by source file leaves 16 rows uncovered:

| Kind | Rows | Role and confidence |
|---|---|---|
| Mansi tom. 5: the Conciliabulum Ephesinum (431); the *Synodicon adversus tragoediam Irenaei* | 2 | `tradition`, `provisional` |
| Barhebraeus, *Chronicon Ecclesiasticum* I; Barhadbeshabba, PO 9.5 | 2 | `context` |
| PG 47: early treatises and the *Dialogus*; PG 52: letters from exile | 3 | `tradition`, `provisional`, Greek |
| Cyril, *Five Tomes* and *Three Epistles* (Pusey) | 2 | `context` |
| The Ethiopic Synaxarium I | 1 | `context` |
| Marius Mercator, PL 48 | 1 | `context` |
| Nestorius: the *Bazaar of Heracleides*, Nau's *Livre d'Héraclide*, Loofs's *Nestoriana* | 3 | `tradition`, `provisional` |
| Socrates, Greek (Hussey 1853); Sozomen, Greek (Hussey 1860) | 2 | `context` |

That makes 66 − 16 = 50. The Registry did cover the earlier 50, but its completeness claim is now false. Five of the uncovered rows place Antiochene-party material in this world as `tradition` (Doc_01 finding N4). Those need a Boundary Status the Registry has not given them. The shallow checkout cannot date when the rows arrived. Their notes tag several as "Shared-Events Era 2 batch".

**Required.** Give every uncovered row a Registry row, or a grouped row where the treatment is uniform, with Type, Confidence, Boundary Status and Licensed-For, and correct the count. The Boundary Status of the five Antiochene-party `tradition` rows waits on Doc_01 N4.

### D2. Blocking (substantial). §8 holdings disposition: the figures are stale, eleven in-scope files have no disposition, and Table D has 83 rows, not 84.

**Location.** §8 opening: "reports 431 vendored files: 2 by design, 103 in scope but unread, 42 out of window and 284 with no coverage entry"; "Table D gives each remaining 'in scope, unread' file its own line." §9 item 6: "Table D for the 84 others". `Open_Gaps_Tracking.md` entry 11(d) repeats the claim.

**Evidence.** `python -m engine.m9.cli holdings aec` at `origin/main` `5136d7f58` reports 1,522 vendored files: 2 by design, 113 in scope but unread, 51 out of window, 1,356 with no coverage entry. Comparing the 113 against every file named in §8, eleven have no disposition:

- `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml`
- `augustine_arian-sermon-collatio-maximinum-pl42-lat_migne1886.txt`
- `basil_opera-omnia-pg29-grc-lat_migne1857.txt`
- `basil_opera-omnia-pg31-grc-lat_migne1857.txt`
- `gregory-nazianzen_epistulae-carmina-pg37-grc-lat_migne1857.txt`
- `gregory-nazianzen_orationes-27-45-pg36-grc-lat_migne1858.txt`
- `gregory-nazianzen_orationes-pg35-grc-lat_migne1857.txt`
- `gregory-nyssa_opera-omnia-pg44-grc-lat_migne1858.txt`
- `gregory-nyssa_opera-omnia-pg45-grc-lat_migne1858.txt`
- `gregory-nyssa_opera-omnia-pg46-grc-lat_migne1863.txt`
- `monceaux_histoire-litteraire-afrique-chretienne-tomes6-7-fra_1922-1923.txt`

Table D has **83** rows, counted two ways: `grep -c '| Deferred |'` gives 83, and counting the table's backticked file rows between "### Table D" and "## 9." gives 83. The text says 84. `ammianus-marcellinus_roman-history_yonge1862.txt` and the Neale liturgies file, both named in §8's first table, are no longer in the in-scope-unread list.

**Why it matters.** §8's claim that every in-scope, unread file has its own disposition is a completeness claim, and it is false. The count claim is false too. Both have to be true, and dated, for the holdings disposition to mean anything.

**Required.** Re-run the holdings report, date its figures, give each of the eleven files a disposition, and correct the Table D count in §8, §9 item 6, and the entry 11(d) restatement in the tracking file. That last is the build thread's own append, not an edit to the old entry.

### D3. Blocking (substantial). §1 and Registry row 11a: a letter is called "independently verified present", but only its title is in the file.

**Location.** Doc_02 §1, Theodoret paragraph: "e.g. John of Antioch's letter to Nestorius and Theodoret's own letters from Ephesus, independently verified present in the vendored file". Registry row 11a: "for example `iv.x.cl` … The four letter loci are present in `npnf203`".

**Evidence.** As in Doc_01 N2: `npnf203` `iv.x.cl` (lines 36058–36075) holds only the title line "CXLIX is 'Copy of the Letter written by John, Bishop of Antioch, to Nestorius.'", one sentence and a note. The letter is not printed. Letter CL, Theodoret to John of Antioch, February 431, is at `iv.x.cli`.

**Required.** Correct the example and the row 11a locus in step with Doc_01.

### D4. Blocking (substantial). Registry row 11a, and Doc_02 §1 and §6: the condemned-content disclosure is scoped narrower than Constantinople II canon XIII.

**Location.** Row 11a, Comparandum Note: "Condemned-content status must be disclosed wherever the Counter-statements are drawn on". Row 11a, Licensed For: "The Letters' Nestorian-controversy correspondence is not named at that council". Doc_02 §1: "the Counter-statements specifically are … condemned material". Doc_02 §6: "a live, condemned-content edge case".

**Evidence.** As in Doc_01 N3. `npnf214` `xii.vii-p36` (The Capitula of the Council, XIII) condemns by description "the impious writings of Theodoret, directed against the true faith and against the first holy Synod of Ephesus and against St. Cyril and his XII. Anathemas, and [defends] that which he has written in defence of the impious Theodore and Nestorius". The 430–431 letters in row 11a include a letter from Ephesus attacking that synod (`iv.x.clxiii`) and a letter to Nestorius refusing to assent "to what has been done unjustly and illegally against your holiness" (`iv.x.clxxiii`). Both fall inside that description.

**Required.** Extend the disclosure to the Letters material the canon's wording reaches, in step with Doc_01.

### D5. Non-blocking (cosmetic). §6 and Registry row 21: Lausiac History line loci point at chapter headings, not at the quoted lines.

**Location.** §6 cites `line547` (Olympias), `line419` (Chapter XXXV), `line579` (Chapter LXI) and `line473` (Sabaniana). Row 21 cites line 477 (Sabaniana), `line419` and `line579`.

**Evidence.** In `palladius_lausiac-history_clarke1918.txt`, lines 419, 473, 547 and 579 are the headings for Chapters XXXV, XLI, LVI and LXI. The quoted words are at lines 427 ("embroiled in the disturbance connected with the blessed John"), 477 (Sabaniana), 549 (Olympias) and 583 ("to Rome because of the blessed bishop John"). The corpus-map row already carries 427, 477, 547–549 and 583. The quotations and chapters are right. Only the line numbers are off.

### D6. Non-blocking (cosmetic). §1 and the Registry header: the exact word counts no longer reproduce.

**Evidence.** On `npnf110` alone, `LC_ALL=POSIX wc -w` now gives 534,065 (the document says 535,125), and a tag-stripped whitespace split gives 483,878 (it says 484,393). For the six volumes, the Registry header's 3,339,085, 3,357,623 and 3,035,294 now re-run as 3,332,586, 3,351,124 and 3,032,271. The volumes were changed by the CCEL header clean-up (PR #1179, 2026-10-26, with a follow-up on 2026-10-27). No claim depends on the exact figure. Re-run and date the counts.

### D7. Non-blocking, but required by CLAUDE.md's tracking rule. §1 promises an open item that is not in §9.

**Location.** §1, end of the Theodoret paragraph: "the corpus-map's own existing confidence tags for the *Eranistes* and Letters specifically should be revisited against this finding … carried in §9 rather than silently corrected".

**Evidence.** None of §9's ten items carries it, and no `Open_Gaps_Tracking.md` entry does either. Entry 7(b) restates the boundary finding, not the corpus-map revisit. A gap that the document says is carried, but that is carried nowhere, has gone quiet. Adding the item changes no claim.

### D8. Non-blocking (alignment). §2 keeps the date-based framing left over from Round 3 M3.

**Location.** §2, Theodoret: "most of his own carried material either out-of-window by date or a live edge case".

**Evidence.** Doc_01 §4 and Doc_02 §1, §6 and §8 all exclude the *Eranistes* and the bulk of the Letters "by subject". The classification is the same either way, so only the stated ground needs to change.

### D9. Non-blocking (cosmetic). Registry, Living-document protocol.

"Rows 1, 3, 5 to 12, 14, 15 to 20 … are listed in `Doc_02_Source_Ecology.md` §9". §9 does not list them by number. Item 3 covers them as a group. Re-point the sentence or list them.

---

## Verdict

**Doc_02 and `Source_Registry.md`: did not clear. Not Approved to proceed.**

Of the eleven Round 3 items, all are closed or closed in substance. Two leave residue: M3's leaves D8, and M4 is overtaken by D1. Four new findings are blocking (substantial): D1, D2, D3 and D4. D5 to D9 are non-blocking and can be applied directly without a further review. Under Mark's ruling of 2026-10-29, no further round runs on the build thread's own initiative. The open findings go back to Mark.

Open blocking findings for Mark, exactly:

1. **D1.** The world's corpus-map bucket holds 66 work-rows, not 50 (PyYAML and `grep -c '^- row_id:'` agree). Sixteen rows have no Registry row: Mansi ×2, Barhebraeus, Barhadbeshabba, PG 47 ×2, PG 52, Cyril (Pusey) ×2, the Ethiopic Synaxarium, Marius Mercator, Nestorius ×3, and Socrates and Sozomen in Greek. Five of them are Antiochene-party `tradition` rows whose Boundary Status depends on Doc_01 N4.
2. **D2.** §8's holdings figures (431 / 2 / 103 / 42 / 284) are stale against the current report (1,522 / 2 / 113 / 51 / 1,356). Eleven in-scope, unread files have no disposition. Table D has 83 rows, not the 84 that §8, §9 item 6 and the tracking file claim.
3. **D3.** §1 and row 11a: "John of Antioch's letter to Nestorius" at `npnf203` `iv.x.cl` is called verified present, but only its title is in the file. Use `iv.x.cli`.
4. **D4.** Row 11a, and §1 and §6: Constantinople II canon XIII condemns by description, and its description reaches Theodoret's anti-Ephesus and pro-Nestorius letters, so the condemned-content disclosure limited to the Counter-statements is too narrow.

Non-blocking items to apply directly: D5 (Lausiac line loci 427, 477, 549, 583), D6 (re-run and date the word counts), D7 (add the corpus-map confidence-tag revisit to §9 and the tracking file), D8 (§2 "by date" becomes "by subject"), D9 (the Registry's §9 pointer).
