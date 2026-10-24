Simulated review — informational only, not an Article 31 substitute.

# Doc_02 — Source Ecology (lpc), with its Source Registry: full review after change order CO-LPC-1

**Document:** `Build/worlds/lpc/Doc_02_Source_Ecology.md`, reviewed together with `Build/worlds/lpc/Source_Registry.md` (branch `claude/lpc-augustine-sermons-2026-10-23`, head `a0209b8d`; both last edited by CO-LPC-1 in `eb717583`)
**Round:** 36
**Reviewer:** Opus 5.5
**Reviewer model:** claude-opus-5-5
**Reviewer agent:** independent Opus 5.5 review subagent (workflow-spawned, full review, high effort); wrote none of the text under review
**Drafter:** Sonnet 5.5 drafters for CO-LPC-1, checked by the `lpc` build thread; the 2026-09-01 text and its revision rounds were drafted by the `lpc` build thread, and the 2026-09-29 and 2026-09-30 Registry rows by the `lpc` Library thread (per `lpc_Decision_Log.md` and `Review-Artifacts/L0_Doc02_Registry_Check_2026-10-23.md`)
**Drafter model:** Sonnet 5.5
**Drafter agent:** CO-LPC-1 Sonnet 5.5 drafter (Step 0, Doc_01, Doc_02, Source Registry file set)
**Date:** 2026-10-23
**Scope:** full review of Doc_02 and the Source Registry in their current state: factual and historical accuracy, quotations re-checked word for word against `cic/texts/`, consistency with the `lpc_Decision_Log.md` entries of 2026-10-23 (D1 to D5, the §7 ruling, CO-LPC-1) and with Doc_01, the Registry against `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` and `cic/texts/REGISTRY.yaml`, source attribution, the stage's job, Forces Framework integration, and whether CO-LPC-1's edits are correct and introduced no new error. Open_Gaps OG-28 to OG-51 and the prior Doc_02 review files (Round 30, the 2026-09-29 and 2026-09-30 checks, and the Round 34 Phase L0 check) were read. Readability targets were not scored: Doc_02 and the Registry are internal construction documents, not participant-facing text.
**Ordered by:** the project lead's Cap ruling of 2026-10-23 (System Hub Decision Log, "Cap ruling: lpc change order CO-LPC-1", which names this file)
**Truncation check, method 1:** structural count with end-of-file read. Doc_02: 160 lines, headings §1 to §10 present in order (lines 11, 33, 65, 79, 91, 105, 120, 124, 131, 150), and line 160 ends on a complete sentence. Registry: 308 numbered table rows, exactly the set 1 to 308 with no gap or duplicate, every row carrying 12 pipes; the file ends at line 413 on a complete sentence.
**Truncation check, method 2:** byte and hash comparison with the committed blob. `wc -c` equals `git cat-file -s HEAD:<path>` (Doc_02 97,428 bytes; Registry 464,961 bytes), and `git hash-object` equals `git rev-parse HEAD:<path>` (Doc_02 `4f80844d…`, Registry `cc33d18e…`). `git status` shows neither file modified.

## Method

Every quotation in Doc_02 §1, §2, §4 and §6 was searched in the vendored file it cites, with tags stripped and whitespace and quote marks normalised, then confirmed by its structural marker. The census was recounted with a YAML parser over every atlas file in `cic/corpus-map/`. The Registry's `cic/texts/` paths (112) were checked on disk and in `REGISTRY.yaml`. The seven corpus-map notes CO-LPC-1 wrote into rows 215 to 222 were checked against the map. The Latin sermon files were opened at their class and appendix markers. No WebSearch and no model API calls.

## What holds

- **The Round 34 P1 findings are fixed.** Rows 215 to 219, 221 and 222 now cite their corpus-map entries, and every entry name, role and confidence matches the map. §3's count of twenty works in twenty-nine files is right (29 Type S vendored rows, recounted). Line 49 now names PL 38, PL 39, Morin 1930 and PL 40, and the false "only Latin witness" sentence is gone. §7 is restated to Doc_01's test as the project lead ruled.
- **§7's facts check out.** Optatus is dated "c. 366-393" (`optatus_against-the-donatists.txt` line 5). Lauchert dates Carthage I "c. 345—348" and II "c. 387—390" (file lines 340, 342). `CTh` XVI.2.4 is headed "(321 lul. 3)", the OCR reading of Iul. (`theodosianus-16_mommsen-meyer1905.txt` line 83906). Mansi tom. 3 holds the council under Genethlius of 390 (line 15650).
- **The census figure for this world is right.** 215 raw, 168 `tradition`, 166 distinct titles and 47 `context`, by two methods. It is still the largest atlas file on all three counts.
- **Quotations verified word for word.** "your suffrage and God's judgment", "ancient venom", the 256 preface sentence, Pontius's acclamation sentence, "household companions" (`anf05`); Possidius ch. VIII (lines 2075 to 2077, 2131 to 2132), "probably not over thirty", "in all likelihood younger than his teacher and friend"; the Letter CCXI endnote (`npnf101`); *On Baptism* III.2 §2, the *Retractationes* II.18 quotation, "Anastasius fills to-day", and Letter 185 §25 as now quoted at Registry row 44 (`npnf104`); the Zonaras sentence at row 42 (`npnf214` line 37658); the corrected Soliloquies note at row 25 (map lines 1632 to 1634); Doc_01's "real, substantial differences" and "fully settled" at row 126. Sermons 280 and 281 are in PL 38 (`augustine_sermones-1-340-lat_migne-pl38.txt` lines 89935, 90170), as §6 now says. Row 19's "~308,000 words" and 97 sermon divisions match `npnf106` division `vii`.
- **The Forces Framework requirement is met.** §6's "Forces lens" paragraph names which sources speak to external forces, what the silences show, and what survivorship indicates. It is substantive.
- **Registry paths are sound.** All 112 `cic/texts/` files the Registry names exist and have a `REGISTRY.yaml` entry.

## Findings

### P1-1. Doc_02 states the Augustine-text rule for the whole world; Doc_01 limits it to questions about Augustine

- **File and line:** `Build/worlds/lpc/Doc_02_Source_Ecology.md:13`.
- **Evidence:** Doc_02 line 13 reads "The Representative answers only from what Augustine's own text says." Doc_01 line 26 reads "On questions about Augustine, the Representative, Datus, answers only from what Augustine's own text says." The CO-LPC-1 entry in `lpc_Decision_Log.md` (line 2495) records that the build thread narrowed this sentence in Doc_01 so that "the Augustine-text boundary applies to questions about Augustine, not to the whole world." The narrowing was not carried into Doc_02.
- **Why it matters:** As written, Doc_02 bars the Representative from Cyprian, Pontius, the councils and the martyr acts, which are half this world. Doc_10 builds from Doc_01 and Doc_02, and the two now disagree on a scope rule the project lead set.
- **Fix:** Use Doc_01's wording: "On questions about Augustine, the Representative answers only from what Augustine's own text says."

### P1-2. The sermon scope includes Sermones 364 to 396 and excludes them, and it points the appendix exclusion at the wrong part of the files

- **File and line:** `Doc_02_Source_Ecology.md:13`, `:19`, `:49`.
- **Evidence:**
  - Lines 13 and 19 put "the Maurist *Sermones* 1 to 396" inside the scope.
  - Line 49 excludes "The Maurist appendix of doubtful sermons (the end of PL 39; Classis V of row 265)".
  - In row 265's file, Classis V is the *Sermones dubii*. Its heading is at `augustine_sermones-ad-populum-lat_migne-gaume1841-t5.txt` lines 117124 to 117125 ("CLASSIS V." / "SERXffONES DUBII."), and its first sermon is "SERMO CCCLXIV" (line 117130). Classis V is therefore Sermones 364 to 396, inside the 1 to 396 that lines 13 and 19 include.
  - The Maurist Appendix is a separate block. PL 39's contents list "Sermones dubii. 1639" and then "Appendix. — Sermones supposititii." from col. 1735 (`augustine_sermones-341-396-et-appendix-lat_migne-pl39.txt` lines 192 and 196). In row 265 the Appendix starts about line 124390 (running heads "APPENDIX."), with its own class numbering from line 124451.
  - The corpus map keeps the two blocks apart: "Sermones dubii (Maurist Classis V, Migne printing, tome V)" (map line 1577) and "Augustine's Sermones 341-396 and the Maurist Appendix of doubtful sermons" (map line 300). OG-46 places "the doubtful sermons" at about line 124456, which is the Appendix, not Classis V.
  - D4 (`lpc_Decision_Log.md`, 2026-10-23) excludes "the Maurist appendix of doubtful sermons", which could mean either block.
- **Why it matters:** The boundary CO-LPC-1 was written to set contradicts itself inside one document. Whether 33 sermons the Maurists themselves doubted are in or out cannot be read from it. Registry row 265 already says the Classis V sermons "are not licensed as Augustine's".
- **Fix:** Ask the project lead one question: does D4 exclude the *Sermones dubii* (364 to 396), the Appendix of *supposititii*, or both? Then state the scope by number (for example, "Sermones 1 to 363, Classes I to IV") and name each excluded block by its own marker: PL 39 col. 1639 and row 265 line 117124 for the *dubii*; PL 39 col. 1735 and row 265 from about line 124390 for the Appendix. Doc_01 line 26 uses the same "1 to 396" wording, so the Doc_01 change-order review should carry the same fix.

### P1-3. Doc_02 calls the Latin sermon files "the quote base", against the scan-quality rule and against the Registry's own licences

- **File and line:** `Doc_02_Source_Ecology.md:49`, also `:31`.
- **Evidence:**
  - Line 49: "The Latin sermon files are the quote base for the sermon scope". Line 31: "For the sermons, the Latin files are the base for quoting under the sermon scope".
  - `cic/texts/INTAKE.md` lines 43 to 46: "Scan quality decides quotability, not language. A garbled OCR scan … stays second witness until a clean witness of the same work is vendored."
  - Registry row 265 (`Source_Registry.md:330`): "licensed for locating the Latin behind a sermon that row 19 cites … and for nothing more: the file is not a quotable text."
  - Row 268 (`:333`) is "licensed for no claim about Augustine's own preaching". Line 49 handles row 268 correctly.
  - The file headers say the same. Row 265's file (line 9): "the file is a second witness, not a quotable text, until a passage is checked". Caillau's file (line 9): "second witness only".
  - Line 31 also lists the same sermon files among the "Latin-language second witnesses", so the paragraph classes them both ways at once.
- **Why it matters:** Under D5 every sermon quote the room speaks carries a Latin reference, and the quote gate verifies the Latin against the vendored file. Doc_02 tells downstream builders that these files are a base for quoting. The rule and the Registry say they are second witnesses, which a page-image check does not by itself change. The Round 34 check raised this (its P2-6) and asked for a per-file quoting status; the change order added the opposite general statement instead.
- **Fix:** Give each sermon file its status in the Registry's terms:
  - row 265: locating only;
  - row 268: finding aid only;
  - rows 216, 217, 219 and 267: second witness until a passage is verified against the page image, under `INTAKE.md` §2.

  Then say plainly that a sermon quote record can be made only from a passage that clears that rule. Remove "second witnesses" from the line 31 list for the sermons, or keep it and drop "quote base". Do not keep both.

### P1-4. "Sermons preached to his own congregations at Hippo and Carthage" was widened without a source, and its only licence is circular

- **File and line:** `Doc_02_Source_Ecology.md:19`; `Source_Registry.md:32` (row 19).
- **Evidence:**
  - Before CO-LPC-1, line 19 said "most delivered to his own congregations at Hippo and Carthage". It now says the 97 are "sermons preached to his own congregations at Hippo and Carthage", without "most".
  - Row 19's Licensed-For cites "Doc_02 §1" for the same words, so each file licenses the other.
  - The Round 34 check (Q3, line 17) said this claim "must be verified before it is widened".
  - In `npnf106`, the only place headings on the 97 sermons are Carthage: "Delivered at Carthage in the Restituta" (line 15408), and "Delivered at the Table of St. Cyprian" (lines 17969, 19865). No sermon heading names Hippo.
  - Carthage was Aurelius's see, not Augustine's, so the Carthage sermons were not preached to "his own" congregation.
- **Why it matters:** The change order removed a hedge and turned a claim with no vendored source into a universal one.
- **Fix:** Restore a bounded claim and give it a real locus. For example: "most preached at Hippo, some at Carthage (`npnf106` headings at lines 15408, 17969 and 19865)". Alternatively, drop the place clause. Rewrite row 19's Licensed-For so it no longer cites Doc_02 back.

### P1-5. "against his own wishes" appears as a quotation from Augustine's letters, and the words are not in them

- **File and line:** `Doc_02_Source_Ecology.md:19`.
- **Evidence:**
  - Line 19 says Doc_01 "directly quotes and re-verifies Augustine's own account of his ordination — presbyter in 391 "against his own wishes," by congregational seizure … (Letters XXXI §4 and CCXIII §4, Registry row 11)".
  - A full search of `npnf101_augustine-confessions-letters.xml` finds no "against his own wishes", "against my wish" or "against my will" about his ordination.
  - The words are Doc_01's own prose, used there without quotation marks ("ordained *presbyter*, against his own wishes, in 391").
- **Why it matters:** The sentence attaches quotation marks to a paraphrase in a clause that says Augustine is being quoted. This fault is older than CO-LPC-1. The handoff quote check did not catch it because the phrase is under five words.
- **Fix:** Remove the quotation marks and state it as a paraphrase. Alternatively, quote what the cited letters actually say, with its locus.

### P2-1. The Psalm exposition is cited to the Latin row, not the English one

- **Where:** `Doc_02_Source_Ecology.md:19`.
- **Finding:** The line says "~695,000 words of Psalm exposition … held under their own rows (201 and 21)". The ~695,000-word English body is row 20 (`Source_Registry.md:33`). Row 201 is Migne's Latin (`:266`).
- **Fix:** Cite rows 20 and 21, and name row 201 as the Latin if it is wanted.

### P2-2. §3 calls all twenty-nine secondary files Confidence C, but twelve are B

- **Where:** `Doc_02_Source_Ecology.md:75`.
- **Finding:** Rows 224, 236, 238 to 243 and 247 to 250 are Confidence B in the Registry. The change order widened the list and kept the old "Confidence C" label.
- **Fix:** Say "Confidence B or C, per row".

### P2-3. The census comparison names the wrong next-largest file

- **Where:** `Doc_02_Source_Ecology.md:15`.
- **Finding:** The line says `latin-apologists.yaml` (100/97/45) is next-largest by raw and by `tradition` entries, and `the-society-of-jesus.yaml` is next by distinct titles at 87/82/82. At HEAD, `the-society-of-jesus.yaml` holds 123 raw, 99 `tradition` and 99 distinct titles, so it is next-largest on all three counts. It grew in the Library commits merged after CO-LPC-1 (`1e33a9ad`, `e40dcaff`). The headline claim, that this world is the largest, still holds.
- **Fix:** Recount the comparators by the stated method, or drop the comparator figures and keep the headline claim.

### P2-4. "The Gaume 1841 printing" does not match row 265's imprint

- **Where:** `Doc_02_Source_Ecology.md:13`, `:31`, `:49`.
- **Finding:** Registry row 265 gives "Paris: J.-P. Migne, Petit-Montrouge, 1841", and the corpus map calls it "Migne printing, tome V" (map line 1556). Its title is the same Migne Augustine *Tomus quintus* that rows 216 and 217 hold in the 1845 and 1863 printings (row 216: "*Tomus Quintus (Pars Prior)*, *Patrologiae Tomus XXXVIII*"). The text calls it Gaume's and lists it beside rows 216 and 217 as though it were a separate edition.
- **Fix:** Call it "Migne's 1841 first printing of the same Tomus V (row 265)". Doc_01 line 26 needs the same correction.

### P2-5. §7 still says the gap is attested through Donatism's sources, not this world's, and then lists this world's Native rows from the gap

- **Where:** `Doc_02_Source_Ecology.md:122`.
- **Finding:** The line says the interval is "richly attested — through sources that are Donatism's own territory (World #4), not this world's". The restated text then names Native rows 27, 64, 300, 228 and 235 from the gap.
- **Fix:** Qualify it: "mostly through sources that are Donatism's territory; the rows of this world that date from the gap are named below, and none is that voice." Also say that the list is not exhaustive. Row 11, for example, holds Augustine's letters of 386 to 390.

### P2-6. Both status lines say no review covers the 2026-09-30 merge

- **Where:** `Doc_02_Source_Ecology.md:3`; `Source_Registry.md:3`.
- **Finding:** `Review-Artifacts/L0_Doc02_Registry_Check_2026-10-23.md` (the Round 34 check) now covers the merge, and this file covers CO-LPC-1. Neither status line names either one.
- **Fix:** Restate current status only and cite the latest review file. Leave the history to the Decision Log.

### P2-7. Three Round 34 P2 findings on the Registry are still open and are not tracked

- **Where:** `Source_Registry.md:330` (row 265); `:368` to `:373` (rows 303 to 308).
- **Finding:**
  - Row 265 still points to "rows 266–268" for post-Maurist sermons, but row 266 is the Tractates on John.
  - Row 265 still puts `CLASSIS V` and `SERMONES DUBII` both at line 117125. The file has them at lines 117124 and 117125.
  - Rows 303 to 308 are still at Confidence A with no Confidence sentence.

  OG-39 tracks only the Round 34 P1 findings.
- **Fix:** Correct them in the next Registry edit, or log them under OG-39.

### P2-8. Process narration remains in the canonical file

- **Where:** `Doc_02_Source_Ecology.md:133`, `:138`, `:154`, `:160`.
- **Finding:** These lines carry process history:
  - §9 item 1: "With this build session's own network access confirmed working for the first time".
  - §9 item 6: the Round 14 to Round 18 history.
  - §10: "for the first time since Round 14" and the Round 30 account.

  `tools/check_live_commentary.py` marks these lines PROTECTED, so they do not fail the gate. They are still review history inside a canonical file, which CLAUDE.md routes to the Decision Log.
- **Fix:** Keep each current fact and move the history to `lpc_Decision_Log.md`. This needs the project lead's word if PROTECTED is meant to exempt them.

### P2-9. §1 counts the Morin 1917 file in the sermon scope without excluding its nine non-Augustinian *tractatus*

- **Where:** `Doc_02_Source_Ecology.md:13`.
- **Finding:** Row 267 holds 33 sermons plus "nine further tractatus" that its title page gives to Optatus, Quodvultdeus and others. Row 267 is licensed for "the thirty-three sermons only". Line 13 names "Morin 1917, row 267" with no limit.
- **Fix:** Add "(the 33 sermons only)".

## Counts

0 P0, 5 P1, 9 P2.

## VERDICT: Substantial revision required
