Simulated review — informational only, not an Article 31 substitute.

# Round 2 review of Doc_02 and the Source Registry (latap)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** an independent review session with fresh context. It wrote none of the text under review and took no part in Round 1.
- **Drafter agent:** Sonnet 5.5 library-stage worker
- **Round:** 2. This is a targeted recheck of what changed since Round 1 (`8476c699`), checked against the Round 1 findings.
- **Commit reviewed:** `9cc6ebd8494f8e928009e67fcd6954b517c0b4a8`, the head of `claude/latap-library-stage`.
- **Truncation check, method 1 (structure):**
  - Doc_02 has all 11 numbered `##` sections, from "1. Primary Sources" to "11. Disposition".
  - Doc_02 ends on the complete sentence "Draft. It is not approved to proceed, and it is not frozen."
  - The Registry's numbered rows run 1 to 74 with no gaps.
  - The Registry then has, in order: "Files behind the Discovery column", "Holdings dispositions", the new "Dossier cross-links" and "Saturation statement".
  - The Registry ends on the complete sentence "`Open_Gaps_Tracking.md` carries the finding."
- **Truncation check, method 2 (bytes and hashes):**
  - Doc_02 is 51,320 bytes. `git hash-object` gives `75479090f3e2…`, which equals `9cc6ebd8:Build/worlds/latap/Doc_02_Source_Ecology.md`.
  - The Registry is 84,968 bytes and hashes to `e30b1143319153e5…`, which equals the blob at `9cc6ebd8`.
- **Date:** 2026-10-29
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 is polish.

## Verdict

**Clear.** P0: 0. New P1: 2. New P2: 6.

The P0 is fixed, and I re-derived the fix from the vendored file. Ten of the eleven Round 1 P1s are fixed; F12 is fixed for Jerome only and stays open for Gennadius as a P2. Both new P1s are mechanical: a stale map count, and a Files-table line that this round broke. They must be fixed before the document is approved to proceed. Neither needs a full re-review; a check of those two lines is enough.

## P0 — F1, re-derived

**Fixed.**

**The ANF07 division matches the revised text.** `anf07_…xml` div2 `iii.vi` (line 10798) holds, in order:
- Four numbered prose fragments, I to IV, before the first div3: 509 words on the Step 0 method.
- The *Phoenix* (div3 `iii.vi.i`, headed "By an Uncertain Author. Attributed to Lactantius"): 2,285 words.
- The *Passion* poem (div3 `iii.vi.ii`, headed "Formerly Ascribed to Lactantius"): 961 words.
- The General Note (div3 `iii.vi.iii`): 177 words by Round 1's slice; 184 by mine, which runs up to the next `div1`.

**The General Note's scope is now stated correctly.**
- The Note reads "There is no ms authority for ascribing the above to Lactantius".
- Its remark on the "adoration of the cross" points to the *Passion* poem.
- Doc_02 §1, §2 and row 44 now say the file does not settle whether the Note reaches the *Phoenix*, and that it does not touch the prose fragments. That is correct.

**The arithmetic holds.** 281,255 + 509 = 281,764.

**Brandt, CSEL 27 part 2 fascicle 1.** The file prints:
- `CARMINA.` at line 10119
- `DE AVE PHOENICE.` at 10126
- `DE PASSIONE DOMINI.` at 10806
- `LIBRORVM PERDITORVM FRAGMENTA.` at 11021

The first item under that heading is Jerome's *Commentary on Galatians*, Book II, quoting "Lactantii nostri quae in tertio ad Probum uolumine…". That is the Latin of English fragment IV. Row 45's reading is correct, and its pointer to row 44 as the English twin is correct.

**Doc_02 §1 (Lactantius), §2, row 44, row 45 and the saturation statement** all now carry the three-part structure and the corrected counts.

**Staging rows.**
- Against `origin/main`, both staging files only add `locus_ids`, `language` and `date` keys.
- The title "Fragments of Lactantius", the role `tradition`, the confidence `assigned` and the atlas id are all back to main's values.
- The invented Latin-only lost-works row is gone, and it never existed on main.

**Transparency rule.** I compared every `cic/corpus-map/**/*.yaml` on `origin/main` with `9cc6ebd8`, keyed by file, source_file and row_id:
- main has 7,361 rows and the branch has 7,388.
- **No main row is missing.**
- No row has a changed `work`, `role`, `confidence` or `author`.
- Five rows change `atlas_ids`, each only by adding `latin-apologists` to an existing assignment: two Audollent scans and Monceaux Tomes I, II and III. No row was retitled or downgraded.

**Ledger.**
- OG-3 and OG-19 are unchanged, so the ledger stays append-only.
- OG-21 corrects both by citing their titles, which is the subject-plus-date rule.
- OG-21 routes the Step 0 and Doc_01 correction to the project lead as a change order. That is right, because both documents are approved to proceed.

## Round 1 P1 findings

| # | Status | Basis |
|---|---|---|
| F2 Gebhardt and Knopf-Krüger rows | **Mostly fixed** | Row 46 lists both, with loci that match the files: Gebhardt line 3489 "Passio SS. Perpetuae et Felicitatis.", no. VII, which the file's content note confirms; Knopf line 2910 "PASSIO SS. FELICITATIS ET PERPETVAE.", under "8. Martyrium der Perpetua und Felicitas". Doc_02 §1 (the file-kind table) and §2 name both. The Files table still lacks both files (new P1 N2). |
| F3 Dossier §2 cross-links | **Fixed** | The new "Dossier cross-links" section gives each cross-link a line. Its facts match the staging files: the Robinson Perpetua row is `latin-apologists`/`assigned` and the Scillitan row is LPC/`provisional`; CIL VIII is `donatism` only, `context`, `provisional`; Monceaux IV–VI are `donatism`, `context`. Gate check 04 no longer raises cross-link findings. |
| F4 Dossier §5 items | **Fixed** | OG-20 and OG-22 carry all four items: I.33, `_fleet…against-praxeas`, the IJC dates and the stale references. Doc_02 §7 item 8 names them. Gate 09 passes. |
| F5 Narration | **Fixed** | Gate 11 passes. The commentary check reports REWRITE 0. |
| F6 Cyprian counts | **Fixed** | The *Address* (`iv.v.v`) is 7,823 words, or 7,301 with notes removed. *Idols* (`iv.v.vi`) is 3,395, or 2,987. Both reproduce exactly. |
| F7 "Most of Tertullian" | **Fixed** | See the CSEL 20 and CSEL 47 checks below. |
| F8 Arnobius on the soul | **Fixed** | See the Arnobius checks below. The census quotation "if Jerome is to be believed" is gone from Doc_02. |
| F9 "?297" | **Fixed** | Doc_02 §2 and row 62 now read "[a.d. 297–303.]". |
| F10 *Idols* authorship | **Fixed** | Contested in the §1 voice flags, §2, rows 36 and 37, and §8. The §8 citation (row 47, lines 18926–18936) is correct: line 18930 reads "Benson, Monceaux und Bardenhewer haben in neuester Zeit die Echtheit verteidigt". |
| F11 Article 4 check | **Fixed** | §7 now points to Doc_01 §8, which exists ("## 8. The Article 4 check"). |
| F12 Jerome and Gennadius Author Gravity | **Fixed for Jerome; partly for Gennadius** | Jerome has all five dimensions. Gennadius has one paragraph, not five dimensions (P2 N8). |

## New and changed claims checked against the sources

**Arnobius, Book II** (ANF06 div4 `xii.iii.ii.*`, notes stripped):
- Ch. XXXI opens "A certain neutral character, then, and undecided and doubtful nature of the soul". The quotation matches; Doc_02 lower-cases "a".
- Ch. XXXV opens "But, say my opponents, if souls are mortal and of neutral character". Doc_02 rightly calls this an objection.
- Ch. LXII has "nor is there any one besides who can give them length of days". This matches Doc_02's paraphrase "besides the Almighty" (line 45024 context).
- The locus "ANF06, Book II" is correct.
- Keeping Jerome to the conversion story, and the *Chronicle* alone to the dream and the bishop, matches rows 56 and 68.

**CSEL 20.** Lines 139–143 say the first volume holds the works "quae aut in solo Agobardino … seruantur aut nullis continentur libris manuscriptis hodie superstitibus, ita ut ad editionum ueterum … fidem recensenda sint". Lines 157–160 give "codex Parisinus latinus 1622 membranaceus saec. IX, qui Agobardinus … a primo possessore Agobardo episcopo Lugdunensi", which "cum aetate tum pretio longe uincit". Doc_02's sentences are accurate.

**CSEL 47.** Lines 119–123 give "duobus saeculi undecimi libris manuscriptis, Montepessulano codice (M) et Paterniacensi (P)", with the editio princeps and the third edition of Beatus Rhenanus. These are accurate. The two Florentine codices, cited as auxiliary witnesses, are omitted; that is not misleading.

**Jerome and Gennadius entry:**
- The NPNF glosses "Born about 160…" (line 40493) and "Flourished 196?" (40646) are verified.
- Gennadius "sicher zwischen 477 u. 494" is at Harnack line 24450, verified.
- One overstatement (P2 N3).

**Octavius voice flag.** The ANF chapter headings bear it out:
- XIV: Caecilius urges and Minucius answers.
- XV: Caecilius retorts on Minucius.
- XXXIX: the narrator's frame.
- XL: Caecilius "exclaims that he is vanquished … professes the Christian religion".
- XLI: the close.

Doc_02 §1 is now correct. Registry row 33 is not (P2 N5).

**Manifest** (`build/latap_Handoff_Manifest.md`). It exists and its paths resolve; `records/worlds/latap.yaml` exists. It is still a skeleton: the 12-check table and the Outcome table are blank (P2 N7).

**Ledger, last three entries:**
- OG-20 is accurate apart from one loose clause (P2 N6).
- OG-21 is accurate; its counts reproduce.
- OG-22 is accurate: the Jerome notices on Arnobius (rows 56 and 60) contain nothing on the soul.

## New P1

**N1. The corpus-map counts in Doc_02 §1 are now stale.**
- §1 says the map carries the works "on 117 rows", with 98 `tradition`, 85 `assigned` and 13 `provisional`.
- Those are Round 1's figures. They included the invented lost-works row and the two Fragments rows downgraded to `provisional`.
- After this round's correct restoration, `cic/corpus-map/latin-apologists.yaml` has:
  - 116 rows
  - 97 `tradition`, 16 `context`, 3 `transmission`
  - tradition rows: 86 `assigned` and 11 `provisional`
- **Fix:** restate the four figures.

**N2. The Files table points the Perpetua files at row 45. This round introduced the error.**
- The diff changes `| 1-9, 11-23, 46 | anf03_tertullian.xml |` to `… 45` and `| 46, 64 | …robinson1891.txt |` to `| 45, 64 |`.
- Row 45 is Brandt's *Carmina*/*Fragmenta*, and the *Passion* is row 46. Both anf03 and Robinson belong to row 46.
- So row 46 now has no file in the Files table.
- The F2 files `gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt` and `knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt` have no Files-table line at all.
- **Fix:**
  - Restore 46 on the anf03 and Robinson lines.
  - Add a line for each of the Gebhardt and Knopf files, row 46.

## Round 1 P2 items

| # | Status |
|---|---|
| 1 | The 16 context rows and the Perpetua rows are now accounted for. The count itself is stale (N1). |
| 2 | Fixed (§1 line 13). |
| 3 | Fixed (row 54: "six named works…, four of them on the shelf"). |
| 4 | Fixed (row 47 cites 24931; row 52 cites 24931–24932, where "paradoxen Ansatz" is printed). |
| 5 | Fixed (the spurious `69` row is removed). |
| 6 | Fixed. All four typos are gone. |
| 7 | **Partly fixed.** The Commodian repetition is gone. §7 item 5 still states the date of the break twice. |
| 8 | Fixed (header exception for rows 32 and 44). |
| 9 | Fixed (header names rows 63 and 65). |
| 10 | Fixed. No bare "OG-N" remains in either document. |
| 11 | Fixed (Inferential-Thin). |
| 12 | Fixed (`str.split()`, no locale). |
| 13 | **Partly fixed.** Doc_02 is fixed; Registry row 33 is not (N5). |
| 14 | Fixed (CSEL 4: Sabaeus first edited Arnobius from the codex). |
| 15 | Fixed ("even approximately intact"). |
| 16 | **Partly fixed.** Doc_02 is fixed. The Registry's "Not yet counted" paragraph still says it "adds no corpus count of its own" and then gives counts. |
| 17 | **Not fixed.** §1 ("it is not Tertullian's (§2)") and §2 Tertullian *Limitations* ("The *Appendix* poems are not his") still say this flatly. The file heads one poem "Author Uncertain" and prints no author for the others. §2's own verse subsection and §8 treat authorship as an absence. |
| 18 | Fixed. The thin-evidence map is added and the process quotability vocabulary is used. |

## New P2

- **N3.** Doc_02 §2, the Jerome *Influence* line, calls *Letter* LXXXIV "the only outside judgment on Lactantius's doctrine". Row 58, Jerome's chiliasm notice, is also an outside report on Lactantius's doctrine, and §2 Lactantius cites it.
- **N4.** Two statements about fragment sources are not quite right.
  - Row 44 says each prose fragment is "a later author quoting or reporting Lactantius, and the source is named in the editor's note after it". OG-21 and Doc_02 §1 say "quoted through later authors".
  - Fragments II, III and IV are sourced to Maximus Victorinus, Rufinus the grammarian and Jerome.
  - Fragment I's note names only "Muratorii Antiquit. Ital. med. æv." This is Muratori's eighteenth-century collection, not a later ancient author.
- **N5.** Row 38's "Read at" still lists only Book I chs. 1, 28, 41 and 60 and Book II ch. 65. It does not list Book II chs. XXXI, XXXV and LXII, on which Doc_02 §7 item 2 and §2 now rest. Row 33 still gives the frame as "chs. I-IV, XIV-XV, XXXIX-XLI" in both Licensed-For and Voices, which does not match Doc_02's corrected flag.
- **N6.** OG-20 says Doc_02 §1 shows that "the figure 285,187 behind" the census's "just under half a million words" counts two poems. The census figure is far above 285,187, so 285,187 is not "behind" it. Step 0 §4 item 1 only sets the two figures side by side.
- **N7.** The handoff manifest has a contradiction and a stale entry.
  - Check 1 reads "Its registry entry at the registry entry for `latap` (not yet created) exists", but the field table and the file both show the entry exists.
  - The Step 2 row says "Doc02_Round1_Review.md when filed", but that file is filed.
  - Gate check 12 flags the missing Step 2 round and date.
- **N8.**
  - Gennadius gets one paragraph, not the five dimensions. He is the sole notice on Commodian.
  - The "Thin-evidence map" paragraph sits outside any numbered section, between §8 and §9.

## Tool runs

- **`python -m engine.m10.cli gaps latap`:** `gaps: PASS`, exit 0.
- **`python -m engine.m10.cli handoff latap --skip-quotes`:** exit 1, 6 min 25 s.
  - **PASS:** 03-step1, 05-dossier, 06-corpus-map, 07-texts, 09-open-questions, 10-ledger, 11-narration.
  - **01-identity: FAIL.** `safety_adjacent` is unset. This is the project lead's call.
  - **02-step0: FAIL.** Step 0 has 7 review files against a cap of 3, and its round 7 file lacks "Approved to proceed". This is outside Doc_02's scope.
  - **04-step2: FAIL, 1 finding.** The Round 1 review does not say "Approved to proceed", which is expected at this stage. The two cross-link findings from Round 1 are gone.
  - **08-quotes: INCOMPLETE**, skipped as instructed.
  - **12-manifest: FAIL.** The Step 2 round or date is missing (N7).
- **`python cic/engine/corpus_map_merge.py --check`:** exit 0. "2955 distinct work(s) → 3889 assignment(s) across 192 Atlas entry(ies) [check only, nothing written]". That is one fewer than Round 1's 2956/3890, consistent with the invented row being removed.
- **`python tools/check_live_commentary.py --surface worlds --base origin/main --enforce`:** exit 0. "worlds: 926 hits (KEEP 74, REWRITE 0, ROUTE 0, PROTECTED 852)".
  - The latap entries are: the Doc_02 line 291 route-cue (PROTECTED), the Registry line 6 date (PROTECTED), the Registry row dates (KEEP), and Doc_01 and ledger entries (PROTECTED).
- No paid model API was called and no text index was built.

## Not verified

- **Gate check 08 (quotes):** skipped by `--skip-quotes`. Every new quotation in this round was matched by hand: Arnobius II.31, II.35 and II.62, CSEL 20, CSEL 47, Brandt line 11021, Harnack lines 18930 and 24450, and the NPNF glosses. The full quote gate has not run on Steps 0 to 2.
- **Gebhardt and Knopf-Krüger:** only the headings were checked. Their Latin texts were not read, and the drafter says the same.
- **Footnote-removed counts:** the *Octavius* 22,305, Arnobius 104,704 and Tertullian 638,816 of 1,047,034 are unchanged since Round 1. My div2 slices gave 22,316 and 104,734, which agree to within boundary and tokenising.
- **"Died 325":** the Lactantius gloss's full wording at npnf203 line 41033 was not read past "Died".
- **Doc_01 §8:** I confirmed the section exists. I did not re-read it to confirm it quotes all five commitments verbatim.
- **Carried from Round 1 and still not checked:**
  - the rights lines in each file header
  - `NEEDS-RULING.md`
  - Constitution V2.3, which is not in `Build/reference/L1-Foundation/`
  - post-1930 scholarship
  - the Licensed-For readings behind the A rows for Tertullian rows 1–31
  - Brewer's own words: Harnack quotes him at line 24928 as "um 458—460 in Südgallien", while row 52 gives "between 458 and 466, at Arles" from Brewer's file. Round 1 accepted the row; I did not reopen it.
