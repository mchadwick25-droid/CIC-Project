Simulated review — informational only, not an Article 31 substitute.

# Round 1 review of Doc_02 and the Source Registry (latap)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** an independent review session with fresh context. It wrote none of the text under review.
- **Drafter agent:** Sonnet 5.5 library-stage worker
- **Round:** 1
- **Truncation check, method 1:** Doc_02 has all 11 `##` headings, numbered 1 to 11 in order. They run from "1. Primary Sources" (line 11) to "11. Disposition" (line 293), and the file ends on the complete sentence "Draft. It is not approved to proceed, and it is not frozen." The Registry's 74 numbered rows run 1 to 74 with no gaps. It also has the sections "Files behind the Discovery column" (line 95), "Holdings dispositions" (line 137) and "Saturation statement" (line 214), and it ends on the complete sentence "`Open_Gaps_Tracking.md` carries the finding."
- **Truncation check, method 2:** Doc_02 is 44,952 bytes. `git hash-object` gives `835d666c2ddf02e0af1678cd4bd814f7f0a86900`, which equals `HEAD:Build/worlds/latap/Doc_02_Source_Ecology.md`. The Registry is 81,146 bytes and hashes to `617337dddc0338285cb342ff2ab824aee39120a6`, which equals `HEAD:Build/worlds/latap/Source_Registry.md`. HEAD is `8476c699`.
- **Date:** 2026-10-29
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

**Not clear.** P0: 1. P1: 11. P2: 18.

Most dates, counts and loci check out against the vendored files, and the Step 0 word-count method reproduces exactly. The blocking problem is the "correction to Step 0" on Lactantius's "Fragments". It is itself wrong, and it has already been written into the corpus map and into two ledger entries (OG-3 and OG-19), one of which routes it to the project lead.

## P0

**F1. The ANF07 "Fragments of Lactantius" really do contain fragments of lost works. The "correction" built on the opposite claim is false.**
- `anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` div2 `iii.vi` (line 10798) does not open with the poems. Before its first div3 it prints four numbered prose fragments, 509 words on the Step 0 method:
  - I: "Fear, love, joy, sadness…"
  - II: Lactantius on metres.
  - III: Firmianus writing to Probus on comic metres.
  - IV: "the sentiments of our Lactantius… in his third volume to Probus," on the Galatians.
- Fragment IV is the same Jerome-quoted passage that Registry row 45 reads as the "first item" of the Latin *Librorum perditorum fragmenta*.
- The division splits 509 (fragments) + 2,285 (*Phoenix*) + 961 (*Passion* poem) + 177 (General Note) = 3,932.
- So these statements are wrong:
  - Doc_02 §1, "A correction to Step 0": "The genuine total is 281,255". It omits about 509 words of genuine fragments.
  - Doc_02 §1: "The Latin fragments of his lost works… are on the shelf in Latin only (row 45)". An English text exists.
  - Doc_02 §10 item 7.
  - Registry row 44, which reads only "the opening of both poems and the editor's General Note".
  - Registry row 45.
  - The Registry saturation statement: "two Latin poems… not fragments of lost works; the 3,932 words… are the poems".
- The General Note's scope is also overstated. It reads "There is no ms authority for ascribing **the above** to Lactantius". It sits directly after the *Passion* poem, and the *Phoenix* is headed "By an Uncertain Author. Attributed to Lactantius". Doc_02 §1 and row 44 apply the note to both poems.
- **Propagation.** On this branch, `cic/corpus-map/latin-apologists.yaml` (from the staging edit) does three things:
  - It retitles the ANF07 row as "Lactantius, Carmina…".
  - It downgrades that row from `assigned` to `provisional`.
  - Its new lost-works row says "Latin only; no English twin is vendored."
- On `origin/main` the row was "Fragments of Lactantius", `assigned`. OG-3 states the error as a finding and sends it to the project lead as an unresolved tension.
- **Fix.** Undo the staging change instead of patching it. Re-read the division in full. Then restate both the pairing and the count:
  - The English fragments I–IV pair with the Latin row 45.
  - The poems pair with the Latin *Carmina*.
  - Correct OG-3 and OG-19 in the ledger's append-only way.

## P1

**F2. Two Perpetua witnesses that the corpus map assigns have no Registry line.**
- The map assigns two Latin witnesses of the *Passion* to this world, both `tradition`/`assigned`:
  - `gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt` (line 3489, no. VII)
  - `knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt` (line 2910, no. 8)
- Neither appears in row 46, in the Files table or in Doc_02. Doc_02 §1 and §2 name Robinson as the only second witness.
- Process V2.0 Step 2 requires that every package item has a Registry line. The holdings report also lists both files, and the second Gebhardt scan, as "no coverage entry". The Registry should say so.

**F3. `handoff-04-step2`: two dossier §2 cross-links have no Registry line.**
- The cross-links are the repointed Robinson staging slug and the CIL VIII Numidia volume.
- CIL VIII has a holdings-disposition line, but it has no Registry row.

**F4. Dossier §5 questions are not all carried forward.**
- `handoff-09-open-questions` fails: the dossier §5 item "Stale references elsewhere" is in neither `NEEDS-RULING.md` nor `Open_Gaps_Tracking.md`.
- Separately, I found no mention in Doc_02, the Registry or `Open_Gaps_Tracking.md` of three other §5 items:
  - the I.33 touchpoint (*On Modesty* in I.33's Callistus story)
  - `_fleet.source.tertullian-against-praxeas` ("does not carry the Latin text")
  - IJC's undisputed c. 250–325 dates for the author of *De mortibus*

  The gate did not flag these three, so they may sit elsewhere. I did not check `NEEDS-RULING.md`.

**F5. `handoff-11-narration`: process narration in files that become canonical.**
- Doc_02 line 223: change-history cue ("No built world's record is edited here").
- Doc_02 line 263: ISO date ("A network check on 2026-10-29…").
- Registry line 87 (row 68): ISO date.

**F6. The footnote-removed word counts for Cyprian are wrong.**
- Doc_02 §1 gives 3,522 words for the *Address* and 1,787 for *On the Vanity of Idols*.
- The *Address* div3 (`anf05` `iv.v.v`) holds 47 notes, which total 522 words. With them removed it is about 7,301 words, not 3,522. *Idols* (`iv.v.vi`) comes to about 2,987.
- The Step 0-method figures (7,823 and 3,395) reproduce exactly.

**F7. "Most of what survives of Tertullian rests on one Paris manuscript" (§2) goes beyond the cited source.**
- CSEL 20 lines 136–160 say three things:
  - The Agobardinus is the best manuscript.
  - The works in the first volume survive in it alone, or in no manuscript at all (resting on old editions).
  - The other volumes rest on other traditions.
- CSEL 47 lines 119–123 put its works on the Montpellier and Paterniacensis manuscripts.
- Nothing read supports "most".

**F8. The source of Arnobius's soul doctrine is misattributed (§7 item 2).**
- §7 item 2 says the doctrine "is attributed on Jerome's report, with the condition 'if Jerome is to be believed'".
- The quoted condition is census wording (`world-census.json`, I.43 `longDescription`). It qualifies the conversion-and-bishop story, not the soul doctrine.
- Jerome's vendored notices (rows 56 and 60) say nothing about the soul.
- No Book II passage on the soul was read: row 38 reads Book II ch. 65 only.
- The wording comes from Step 0 §4 item 2, but Doc_02 states it as fact. It should do three things:
  - Rest the doctrine on a read Book II locus.
  - Keep Jerome to the conversion story.
  - Not quote census wording as if it came from a source.

**F9. A dating note is misquoted.**
- Doc_02 §2 gives "A.D. ?297–303" and Registry row 62 gives "[A.D. ?297-303.]".
- The file prints "[a.d. 297–303.]" (`anf06…xml` lines 38993–38994), with no question mark.
- The added "?" changes the meaning of the note.

**F10. A disputed claim about *On the Vanity of Idols* is presented as settled.**
- Rows 36–37 tag the authorship of *On the Vanity of Idols* as Contested. Harnack, line 18930, reports that Benson, Monceaux and Bardenhewer defend it as Cyprian's.
- Yet three passages say flatly that it is not Cyprian's:
  - Doc_02 §1 (voice flags): "Its words are not Cyprian's argument".
  - Row 36 Licensed-For: "Never Cyprian's own argument".
  - §2 Cyprian Limitations.
- §8 has no row for the authorship.

**F11. Doc_02 has no Article 4 check and does not point to one.**
- Process V2.0 ("Doc_02 checks") says: "Its Article 4 check quotes the five commitments verbatim and states each result at its own strength."
- Doc_01 §8 holds the check. Doc_02 neither carries it nor states that it stands there.

**F12. Jerome and Gennadius have no Author Gravity entries as narrative sources.**
- Framework V7.4 Part II (v1.6) requires five-dimension Author Gravity entries for historians who shape how a world is known.
- Jerome supplies the Montanist lapse, the teacher–pupil link, the Crispus tutorship and the *Chronicle* story. Gennadius supplies the Commodian notice.
- §4 discusses them only briefly.

## P2

1. §1 says the map "carries them on 117 rows". The 117 include 16 `context` rows for scholarship and testimony (Registry rows 47–61). They also include the two Perpetua rows from F2, which have no Registry line.
2. §1 says "Only the ancient testimony is primary". The Registry also types rows 63–65 and 68–72 as P, among them CSEL 69/70 Tertullian.
3. Row 54 says Jerome names "four named works against the church". He names six titles, four of them on the shelf.
4. Row 52 cites Harnack line 24920 for "paradoxical". The word is at lines 24931–24932.
5. The holdings-disposition table has a row for a file named `69`. It was parsed from the report's summary count, and it gives a disposition for a file that does not exist.
6. Typos: the saturation statement has "(rows 44)". Row 46 ends "themselves..". Row 44's Source reads "Lactantius, *Lactantius, Carmina…". §2 (Lactantius Transmission) has a stray comma before "(`lactantius…".
7. §2 Commodian repeats itself: "in verse… in rough verse". §7 item 5 states the date of the break twice.
8. Registry header line 15 says a row with no Licensed-For "does not carry an A". Rows 32 and 44 carry A with "None as … voice".
9. Registry header line 3 says vendored works assigned only to another world are not entered. Rows 63 and 65 are such works, entered as Excluded comparanda.
10. Doc_02 and the Registry cross-reference the ledger by bare "OG-N". CLAUDE.md requires subject plus date.
11. In §8, the "Tertullian trained as an advocate" Tag cell is neither one of the five levels nor a stated absence.
12. Template step 6 requires the counting locale to be stated. It is not stated.
13. The *Octavius* voice flag calls chs. XIV–XV and XXXIX–XLI the frame. Caecilius speaks in XV and XL.
14. "The first printing was by Faustus Sabaeus in 1543" is about the *Octavius*. The cited CSEL 4 lines 252–255 say he first edited Arnobius, so the *Octavius* claim is an inference.
15. Robinson's "in only one manuscript has it survived **even approximately intact**" becomes "survives in its original form in one manuscript only".
16. Doc_02 §1 says "Word counts… come from the Registry's Files table". That table holds no counts, and the Registry says it "adds no corpus count of its own", while Doc_02 does add counts.
17. §1 says the *Appendix* is "not Tertullian's" without a tag. The file's own heading says only "Author Uncertain".
18. There is no named thin-evidence map, and `Inferential-Thin` is never used. The per-file quotability flags do not use the process vocabulary (verbatim-ready / second witness only / unusable).

## Checked and found correct

**Word counts.**
- The Step 0 method reproduces 1,203,783 for the 40 works.
- It also reproduces Tertullian 731,618, *Against Marcion* 187,134, the heresy treatises 278,083, the *Octavius* 23,819, Arnobius 140,826, the *Instructiones* 15,008, the *Passion* 7,325 and the *Appendix* 32,001.
- Lactantius 242,005 + 20,397 + 18,853 = 281,255 reproduces. F1 is about what that total leaves out, not the arithmetic.
- The Cyprian figures 7,823 and 3,395 reproduce.
- The Commodian Latin figures reproduce once notes are removed: *Carmen* 7,334 and *Instructiones* 9,434.
- My footnote-removed totals (1,047,571 overall; Tertullian 639,275) agree with Doc_02's to within tokenising.

**Map counts.** 117 rows; 98 tradition, 3 transmission, 16 context; 85 assigned and 13 provisional tradition rows. Oehler holds 21 works (15 of them only there), CSEL 20 holds 10 and CSEL 47 holds 6, and 31 of the 32 Tertullian works have Latin.

**Loci, all matching:**
- CSEL 20 (Agobardinus, Paris lat. 1622)
- CSEL 47 (M, P, Beatus Rhenanus)
- CSEL 4 (Paris lat. 1661, Sabaeus 1543)
- Boenig 145–153
- Dombart 488–542 (the Cheltenham codex; Paris 8304 and Vossianus, both 17th century)
- Brandt CSEL 19, 214–223 and 588–603
- Robinson 190–222 and 740–750
- Harnack 14590, 18347, 18398, 18548, 18919–18936, 20650–20653, 23402, 23530, 23638, 23707, 23922, 24450, 24601, 24803, 24857–24870
- Monceaux I 5625, 32370, 33090–33095; II 14237–14245, 15399; III 21743, 26146, 37704
- Schanz–Hosius–Krüger 25924–25926
- Brewer 197, 1613, 2689, and "arelatensisch" in the title
- Audollent (Ottawa scan) 47640–47710 and the four Tertullian lines
- npnf203: chs. LIII, LVIII, LXXIX, LXXX, XVIII and Gennadius XV
- npnf206: Letter LXX (397) and LXXXIV.7
- ANF04 "[a.d. 210.]", "Possibly as late as a.d. 230" and "[a.d. 240.]"
- ANF07 *Institutes* V.1 on Tertullian

**Registry row numbers.** Every Registry row number cited in Doc_02 points at the intended row. One ambiguity: "follow the *Apology* (row 47)" means "on Harnack's report".

**Step 0 §4 bindings.**
- Items 1, 3, 5, 8 and 9 are met as written.
- Item 2 is met except for the wording in F8.
- Doc_01 is not reopened. Doc_02 only records that Doc_01 §3 repeats 285,187. That record needs revisiting under F1.

**Transparency rule.** I compared every `cic/corpus-map/*.yaml` on this branch with `origin/main`:
- No file is missing here.
- No (source_file, row_id) pair on main is missing here: 3,488 pairs on main, 3,500 here, 0 dropped.
- One ANF07 Lactantius row keeps its row_id but has been retitled and downgraded (F1).

## Tool runs

- `python -m engine.m10.cli gaps latap`: `gaps: PASS`, exit 0.
- `python -m engine.m10.cli handoff latap`: exit 1, about 10 minutes.
  - Passing checks: 05-dossier, 06-corpus-map, 07-texts and 10-ledger.
  - 01-identity: FAIL, `safety_adjacent` unset. This is expected and is the project lead's call.
  - 02-step0: FAIL. Step 0 has 7 review files against a cap of 3, and its round 7 file lacks "Approved to proceed".
  - 03-step1: FAIL. The Doc01 round 3 file lacks a `Disposition: Approved to proceed` line.
  - 04-step2: FAIL, 3 findings: no review file yet, and the two dossier §2 cross-links in F3.
  - 08-quotes: FAIL, 24 findings, all in Step 0. The only Doc_02 note is the census quotation "if Jerome is to be believed".
  - 09-open-questions: FAIL, 1 finding (F4).
  - 11-narration: FAIL, 3 findings (F5).
  - 12-manifest: FAIL, the manifest does not exist yet.
- `python cic/engine/corpus_map_merge.py --check`: exit 0, "2956 distinct work(s) → 3890 assignment(s) across 192 Atlas entry(ies) [check only, nothing written]".
- `python tools/check_live_commentary.py --surface worlds .`: exit 2. The trailing `.` is rejected ("unrecognized arguments: ."). Run without it, it exits 0 and reports:
  - Doc_02: REWRITE at 223 (change-history-cue), REWRITE at 263 (iso-date), PROTECTED at 273 (route-cue).
  - Registry: PROTECTED at 6, KEEP iso-date on rows 20 onward.
- I also ran `python -m engine.m9.cli holdings latap`, read-only, to check the dispositions: 2 by design, 69 in scope and unread, 95 out of window, 1,359 with no coverage entry. All 69 unread files have a disposition line, plus the spurious `69` row (P2 item 5).
- No paid model API was called, and no text index was built.

## Not verified

- **Not reread:** the Licensed-For chapter readings behind the A rows for Tertullian rows 1–31; the passages were not reopened.
- **Not rerun:**
  - the *Octavius* Christology count (Doc_01 §8 confirmed it)
  - Harnack's Tertullian table at lines 16536–16651, row by row
  - Monceaux's Tertullian table
  - Schanz–Hosius–Krüger pp. 267–269
- **Taken from Step 0, not checked:**
  - Wallis's conditionals
  - the location of Coxe's ANF03 "editor" remark
  - Harnack on the *Passion* (pp. 321–324)
  - the *Passion* ch. V statement on the martyrs' writing, beyond the translator's notice
- **Other unread passages:**
  - the Book VII chiliasm loci in Brandt's TEI
  - row 45 beyond its heading
  - the Robinson pp. 60–95 boundaries
- **Not checked at all:**
  - the CC BY-SA and public-domain rights lines in each file header
  - `NEEDS-RULING.md`, for the §5 items in F4
  - Constitution V2.3, which the documents cite but which is not in `Build/reference/L1-Foundation/` (only V2_2 is there)
  - post-1930 scholarship (none consulted)
- **Approximate:** my footnote-removed counts used a non-greedy regex, not an XML parser.
