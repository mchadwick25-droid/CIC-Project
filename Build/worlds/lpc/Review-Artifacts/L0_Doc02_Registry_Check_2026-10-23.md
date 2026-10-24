Simulated review — informational only, not an Article 31 substitute.

# Doc_02 and Source Registry: Phase L0 item A check of the edits since 2026-09-13 (lpc)

- **Reviewer model:** Opus 5.5
- **Drafter model:** Sonnet 5.5
- **Drafter attribution note:** per `Doc02_Registry_Rulings_Recheck_2026-09-30.md`, whose header reads the commit trailers of the Library-thread edits. The 2026-09-30 merge edits (OG-26) carry no model attribution in `lpc_Decision_Log.md` or `Open_Gaps_Tracking.md`, so their drafter model is not confirmed.
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_01PdSKYEGnPNVAntVFg5ZReR (wrote none of the text under review)
- **Drafter agent:** Library-thread drafting worker and the 2026-09-30 merge of the two library threads
- **Round:** 34 (the Phase L0 item A check named in `build/lpc_Rebaseline_Declaration.md`; not a new revision cycle)
- **Truncation check, method 1:** structural count. Registry: 310 table lines (header, separator, 308 rows), every one with exactly 12 pipes; the numbered rows are exactly the set 1 to 308, no gap and no duplicate; the file ends on a complete sentence and a newline. Doc_02: headings §1 to §10 present, in order; §10 ends on a complete sentence and a newline (158 lines).
- **Truncation check, method 2:** byte and hash comparison against the committed blob at HEAD 2f0e42d2. `wc -c` equals `git cat-file -s` (Doc_02 91,218 bytes; Registry 463,386 bytes), and `git hash-object` equals `git rev-parse HEAD:<path>` for both (Doc_02 878db0af…, Registry 5abf70a0…). Neither file has uncommitted changes.
- **Date:** 2026-10-23
- **Documents:** `Build/worlds/lpc/Doc_02_Source_Ecology.md`, `Build/worlds/lpc/Source_Registry.md`, against `cic/corpus-map/` and `cic/texts/` as checked out at HEAD 2f0e42d2
- **Scope:** (1) whether the edits since 2026-09-13 leave Doc_02 and the Registry consistent with each other and with the corpus map (row numbers, counts, rights statements); (2) the Doc_02 §7 statement on the 258–391 gap; (3) which Doc_02 statements on Augustine's sermons would need a change order under the 2026-10-23 rulings D1–D5. No file under review was edited.
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.
- **Method:** scripts parsed the Registry table and the corpus-map YAML; every quoted locus was read in the vendored file. No WebSearch, no model API calls.

## Verdict

**Not clear.** 0 P0, 5 P1, 6 P2.

The project lead's rulings and the fixes asked for by the 2026-09-30 recheck mostly hold. Every row number Doc_02 cites points to the row it describes. Every `cic/texts/` path named in a Registry row exists. The census figures of 168 `tradition` entries and 166 distinct titles are right by two methods.

Four kinds of drift remain. Seven Registry rows say their file is not in the corpus map, and it now is. Doc_02's counts of vendored secondary works and Latin sermon witnesses predate the merge. The raw census has grown by two entries. And §7's claim about the 258–391 gap is contradicted by more rows than OG-25 names.

Nothing found invents a source or misstates the historical world. The contradictions are about what the files hold, not about what Augustine or Cyprian said.

## Q1. Consistency of Doc_02, the Registry and the corpus map

### Fixed since the 2026-09-30 recheck (old row numbers mapped through OG-26)

- P1-1 (old 265, now row 301). The Boundary Status is now `Excluded`, with a ground.
- P1-2 (Doc_02 line 47). The reason for row 267 is now given apart from the OCR reason.
- P1-3 (old 243–248, now rows 279–284). The Discovery cells now give channel, instrument and date only.
- P2-2. Line 47 now names the Caesarea sermon (row 306) as the exception.
- P2-3. Row 14 now cites line 16910.
- P2-4. Row 304 now quotes `PAO. 177, 12 ED. KNOELL` as printed.
- P2-5. Row 300's Boundary cell now reads `Native` alone.

### Verified clean

- **Census, two methods.** A YAML parse and `grep` counts of `latin-pastoral-congregational-christianity.yaml` agree: 168 `tradition` entries and 166 distinct `tradition` titles. `latin-apologists.yaml` is 100/97/45 and `the-society-of-jesus.yaml` is 87/82/82, as Doc_02 line 13 states.
- **Optatus quotations.** Both quotations in Doc_02 line 23 are verbatim in the corpus map. The `lpc` note (lines 2826–2830) reads "this entry … is the census's home for that tradition" and "Mark may prefer another Latin home for a Numidian polemicist". The `donatism.yaml` note (lines 841–842, wrapped) reads "Assigned twice with different roles, deliberately (worker brief invited exactly this)".
- **Row ranges.** All of these match: rows 253–256 and 302–308 (eleven Petschenig works), rows 254–256 and 303–308 (nine Latin-only works), rows 257–264, 265–266, 269–270, 285–299 and 302. So does the second-witness arithmetic 12 + 27 + 16 = 55.
- **Rights.** Rows 285–301 state CC BY-SA 4.0 for the Leipzig TEI files. This matches the file headers (for example, `optatus_libri-vii-lat_ziwsa1893-csel26-tei.txt` line 5, and the licence element at line 49). Row 219's date-only rights reasoning (1930 + 95 years = public domain on 1 January 2026) is arithmetically right.
- **Status lines.** The status lines of both files cite the three check artifacts and the 0/3/6 verdict correctly. Both also say that no review covers the 2026-09-30 merge. That is accurate, and this file is the first to do so.

### Findings

**P1-1. Rows 215, 216, 217, 218, 219, 221 and 222 say "Not assigned to this world in the corpus map." The merged map assigns all seven.**
`latin-pastoral-congregational-christianity.yaml` carries entries for each file:

| Row | File | Corpus-map entry |
|---|---|---|
| 215 | Zycha CSEL 41 | `tradition`, `provisional` |
| 216 | PL 38 | `tradition`, `assigned` |
| 217 | PL 39 | `tradition`, `provisional` |
| 218 | PL 40 | `tradition`, `provisional` |
| 219 | Morin 1930 | `tradition`, `provisional` |
| 221 | Christopher 1926 | `context`, `provisional` |
| 222 | Gebhardt 1902 | three `tradition`, `provisional` entries |

OG-24 records that rows 215–252 were "staged and merged on 2026-09-30". The Verification Notes were not updated after that. Each note should be restated against the current map.

**P1-2. Doc_02 §3 line 73: "Fifteen older, public-domain secondary works are now vendored in full, in seventeen volumes or files."**
That was true of the branch before the merge. The merged Registry has 29 vendored secondary rows (Type S). Line 73 leaves out these works:
- Ribbeck (row 236);
- Duchesne, three tomes (rows 240–242);
- Harnack's *Mission* (row 243);
- Hefele–Leclercq, two slices (rows 247–248);
- Bardenhewer, two slices (rows 249–250).

It also leaves out three second scans of works it does name: rows 224, 238 and 239, the twins of rows 278, 275 and 277. On the merged Registry the figure is about twenty works in 29 files. OG-26 says only the §1 census was recounted at the merge. §3 was not.

**P1-3. Doc_02 §2 line 47 does not match the vendored Latin sermon files.**
- The sentence on Latin sermon witnesses names rows 265, 267 and 268 only. It leaves out PL 38 (row 216), PL 39 (row 217) and Morin's 1930 *Sermones post Maurinos reperti* (row 219), all vendored and all in this world's map.
- "Still not vendored in any Latin edition: … the sermons outside the Migne and Morin and Caillau collections that rows 265, 267 and 268 vendor, apart from the Caesarea sermon (row 306)." Row 219 contradicts this. It is a different Morin collection from row 267's 1917 *Guelferbytani*. Its praefatio lists twelve post-Maurist collections and counts "sexcenti et quadraginta" new sermons (file lines 222–275).
- "Row 267 is a first edition and the only Latin witness of the sermons it holds." This is not established now that row 219 is vendored. Row 219's file names "Guelferb. 4096 … recognitus" as a witness for at least one sermon it edits (line 2559). Whether the two files overlap has not been checked.
- The catechetical sentence names Krüger (row 220) for *De catechizandis rudibus*. PL 40 (row 218) also holds it, and is not named.

**P1-4. Doc_02 §7 line 120 is contradicted by the Registry.** See Q2 below. It is rated P1 because it is a false statement of fact about the record in a canonical document.

**P1-5. The Gesta act count differs between the corpus map and the Registry.**
Registry row 65 now says thirteen acts (OG-27). The corpus-map notes still say "at least fourteen numbered acts" (`latin-pastoral-congregational-christianity.yaml` line 1792; `donatism.yaml` line 461). The map is generated, so the fix belongs in the staging file. It is not Doc_02's. OG-24 lists other "fourteen" copies but not these two.

**P2-1. The census in Doc_02 §1 line 13 is stale by two entries.**
Line 13 says 213 raw entries, 45 of them `context`. The map now holds 215 raw entries, 47 `context`, by both methods. The two additions are both `context` and both come from the "Shared-Events Era 2 batch":
- the Council of Arles (314), from Mansi tom. 2 (map line 1798);
- Monceaux tome VII (map line 2802).

Neither has a Registry row. This also makes stale line 73's claim that Monceaux's later tomes "sit on the Donatism shelf only": tome VII is now on this world's shelf. Doc_02 itself says a later count is recomputed, so this is rated P2.

**P2-2. Rows 303–308 are at A with no stated reason.**
The recheck's P2-1 asked for each row's Confidence sentence. These rows still give none. The only "Confidence" text in their Verification Notes is the comparison clause about row 193.

**P2-3. Row 265 puts `CLASSIS V` and `SERMONES DUBII` both at line 117125.**
In the file, line 117124 is `CLASSIS  V.` and line 117125 is `SERXffONES  DUBII.`. The recheck's P2-6 was "fixed" by moving both markers to 117125. They should be split instead.

**P2-4. Row 265's Licensed-For points to "rows 266–268" for sermons found after the Maurists.**
After renumbering, row 266 is the Tractates on John. The post-Maurist sermon rows are 267 and 268, with rows 189 and 219.

**P2-5. Doc_02 never states the rights of the TEI files it names.**
Doc_02 names sixteen Leipzig TEI files (rows 285–300) and has no "BY-SA" anywhere. Line 29 frames the Latin witnesses under "a clean public-domain original". Line 150 cites a "public-domain-only vendoring rule (`cic/texts/README.md`)". The Registry rows are right; Doc_02 is silent. Outside this scope: `cic/texts/README.md` line 17 says "PUBLIC DOMAIN ONLY", while `cic/texts/INTAKE.md` line 98 calls CC BY-SA sources vendorable. The two library-rule files disagree.

**P2-6. Row 216's licence sentence and line 47 classify the sermon Latin differently.**
Rows 216–219 say `INTAKE.md` treats a clean public-domain original as primary evidence, and that scan quality decides. Line 47 calls the Sermons "second witnesses only". Both can be true for these noisy scans. But a reader cannot tell from either file which sermon files are barred for quoting and which merely need a visual check. This matters under D5 (Q3).

## Q2. Doc_02 §7 line 120 and the 258–391 gap (open item; not decided here)

**The statement.** "This document discharges that binding directly: no primary source named at §1 above, and no row in `Source_Registry.md`, dates from within this 133-year gap."

**What Doc_01 actually binds.** Doc_01 line 110 says: "What is genuinely missing is a surviving voice, continuous with Cyprian's own ordinary-pastoral mode, from within this world's own boundary, for roughly 133 years." It asks Doc_02 to name "an honest silence in *this world's own record*". The binding is about an ordinary-pastoral voice. §7 restates it as a blanket claim about the dates of every source and every row, and that blanket claim is false.

**The contradiction.**

1. **§1 itself names a source from inside the gap.** Doc_02 line 23 names Optatus.
   - The `lpc` corpus-map note dates him "c. 366-393" (line 2827). The vendored file's header gives the same range (`optatus_against-the-donatists.txt` line 5).
   - The editor's note says the first edition was "written about 370 a.d.". The name of Siricius, "who became Pope in 383", was added in the second edition (line 1425).
   - OG-25's "366 to 384" is not the wording of any vendored file. On every vendored dating, the work falls inside 258–391.
2. **Rows 27, 64 and 300 (Optatus, all Native)** contradict the claim. These are the rows OG-25 names.
3. **Row 301 (Excluded)** is a row too: Ziwsa's appendix of documents of the schism. The `donatism.yaml` note on the English appendix dates those documents "305-c. 330" (`donatism.yaml` line 17). Row 223 (Excluded, PL 8 *Monumenta*, "years 303–340") is the same case.
4. **Rows OG-25 does not name, found in this check:**
   - **Row 25** (Native, "flagged"). Its own Verification Note says the *Soliloquies* "was written 386–387 at Cassiciacum".
   - **Row 22** (Native). It includes *On the Morals of the Catholic Church* and *of the Manichaeans*, both headed "A.D. 388" in `npnf104` (lines 590, 598, 1354, 2253).
   - **Row 235** (Native, Lauchert). Its Licensed-For names "Carthage I–III". The file dates "Carthago I., c. 345—348" and "Carthago II., c. 387—390" (lines 340, 342).
   - **Row 228** (Native, Mansi tom. 3). Its Licensed-For names "Carthage I sub Grato". Row 59 (Munier, "a. 345 – a. 525") covers the same councils.
   - **Rows 44 and 88** (*Codex Theodosianus*). They contain constitutions from inside the gap, for example XVI.2.4 (321), line 83906. Row 44's licensed content, XVI.5.21, is from 392.
   - **The census** (no Registry row) now holds the Council of Arles (314) on this world's shelf (P2-1).

Under any reading of "dates from", meaning either written in the gap or recording events of the gap, several Native rows contradict line 120.

**Options for the project lead.**

- **Option 1. Restate §7 to Doc_01's own test.** §7 would say that no surviving ordinary-pastoral voice from this world's boundary survives for the gap. It would then list the gap-dated rows by name and say why none is that voice:
  - Optatus is anti-Donatist polemic from Milevis;
  - the councils of Carthage I and II are canons, not a voice;
  - the *Soliloquies* and *De moribus* were written in Italy before Augustine's return.

  This changes Doc_02 only. It needs a judgement Doc_02 does not yet make: whether a Catholic Numidian bishop writing c. 366–393 is "within this world's own boundary" (Doc_01 bounds the world to "Carthage and Hippo Regius, Latin-speaking Roman North Africa").
- **Option 2. Keep the blanket claim and change the Registry.** The gap-dated rows would move to Excluded or Named Comparandum: Optatus to the Donatism context home, and the councils and pre-391 works likewise. This reverses the census's `tradition` placement of Optatus. It is a corpus-map, cross-world change outside this build thread's authority. It also strains row 25's and row 22's existing Native dispositions.
- **Option 3. Revise Doc_01's binding by change order.** The gap would be named as a thin Catholic record (Optatus, Carthage I and II), not an "honest silence". Doc_05 and the Representative's construction would then hold a thin record, not a silence. Doc_01 already needs a change order under D1, so this could ride with it.
- **Option 4. Log it and leave line 120 as written until the D1 change order.** This keeps a known-false sentence in a canonical file for an indefinite time.

**Reviewer's non-binding recommendation:** Option 1, carried in the same change order as D1. It keeps Doc_01's actual test and makes §7 true. It also brings the boundary judgement on Optatus to the project lead as one question. The decision is the project lead's.

## Q3. Doc_02 statements on Augustine's sermon corpus that D1–D5 would touch (change-order list; no change made)

The D1 entry in `lpc_Decision_Log.md` (2026-10-23) already says D1 moves a scope boundary of Doc_01 and Doc_02. That makes it a change order with its own review file. These are the Doc_02 statements it would reach:

| Line | Statement | Why it needs a change order |
|---|---|---|
| 7 | "grounded in `Doc_01_World_Identification_Boundaries_Orientation.md` …, whose c. 246–430 boundary and strand-singular finding this document does not redraw" | D1 widens Doc_01's scope from pastoral life to the whole sermon corpus. Doc_02's statement of what it inherits from Doc_01 must follow the Doc_01 change order. |
| 13 | The census figures (213 raw / 168 / 166), and "Maurist sermons and tractates in Migne (rows 265–266, three entries)" as second witnesses | The sermon files PL 38 and PL 39, Morin 1930 and the Gaume/Migne tome V (row 265) become the working corpus, not second witnesses. The census is also stale already (P2-1). |
| 13 | Dolbeau's 26 sermons "(neither vendored; Registry rows 49–50)", and "rows 11 and 19 (the general-correspondence and sermon bodies) are qualified accordingly" | Under D1, "all of Augustine's sermons" has to say plainly that the Dolbeau sermons (1996, in copyright, row 50) are out of reach. Row 19 (the 97 sermons of `npnf106`) stops being "the sermon body". |
| 17 | "~97 sermons and ~695,000 words of Psalm exposition, preached and dictated, most delivered to his own congregations at Hippo and Carthage; 124 Tractates on John" | (a) The ~97 becomes the first stage of a larger corpus (D4). (b) D1 does not say whether the *Enarrationes* and the Tractates count as "sermons". The change order should decide. (c) "Most delivered … at Hippo and Carthage" is licensed only by row 19, whose Licensed-For cites Doc_02 §1 back. It must be verified before it is widened. |
| 29 | The list of Latin second witnesses (no sermon file in it); "Under `cic/texts/INTAKE.md`'s current rule a clean public-domain original can be primary evidence …"; "No specific claim in this document is revised on this basis; the additions are disclosed … not exploited for new content" | D5 makes the Latin source reference part of every quote the room speaks, and D1 makes the Latin sermons the basis of new modern renderings. Both reverse "not exploited". The list must name the sermon files. |
| 47 | "the Sermons (row 19) … are vendored in Latin as **second witnesses only** … rows 265, 267 and 268 for the Sermons"; "Still not vendored in any Latin edition: … the sermons outside the Migne and Morin and Caillau collections …" | Already inaccurate (P1-3). Under D1 and D5 the Latin sermon files are the quote base. Each file's quoting status must be stated per file: Caillau "about one word in five or six misread" (row 268); PL 38 headings misread (OG-28); Morin 1917 and 1930. The authenticity of Caillau's and the appendix's sermons is left open (row 268; OG-28 "Authenticity"). D4 excludes the Maurist appendix of doubtful sermons, and line 47 does not say so. |
| 108 | "Augustine's own Sermons 280–281, preached on Perpetua and Felicitas, are native, in-boundary preaching material … at Confidence C and not independently re-read (row 122's own flag)" | The claim rests on a secondary article (row 122, in copyright, not vendored). Under D1 the sermons themselves are in scope. `npnf106` does not hold them: a search for "Perpetua" finds only an endnote on the Carthage basilica, line 15417. So the primary row must be a Latin file (PL 38, row 216, or row 265), and it must be read. |
| 135 (§9 item 5) | Whether "Sermons 280–281 on Perpetua and Felicitas (Registry row 122 …)" meet the load-bearing threshold | This follows from line 108. Under D1 it becomes a question about the primary text, not one held open on a secondary citation. |
| 136 (§9 item 6) and 154 (§10) | The field-bibliography sweep "run in part" and "knowingly partial" | A whole-corpus sermon scope needs a sermon inventory. The instruments in the Registry are Verbraken (row 92), Drobner (row 93), Boodts (row 130) and *CPL* (row 57). OG-24 says *CPL* was not opened. The saturation statement would need a sermon-specific pass, or a stated limit. |
| 150 (§10) | "None of the three documents touches Representative identity", and the portfolio-level test | D2 (the role removed) and D3 (the Reformation boundary with `rzg`) were decided by the project lead. If the change order brings either into Doc_02, the escalation assessment must record it. If neither comes in, the change order should say so. |

These were checked and need no change for D1: line 15 (Cyprian), lines 19–27, line 73 (secondary works), line 120 (§7; Q2 is a separate issue), and lines 131–133.

## Not verified

- I did not check whether row 219 (Morin 1930) and row 267 (Morin 1917) hold the same sermons. Only line 2559 was read.
- I did not recompute the OCR counts in rows 265–268 and 303–308.
- I did not re-read Doc_02 §§4–6 and §8 for content beyond the sermon and gap statements.
- I did not run `tools/check_live_commentary.py` in this check.
- The drafter model of the 2026-09-30 merge edits is unconfirmed (header note).
