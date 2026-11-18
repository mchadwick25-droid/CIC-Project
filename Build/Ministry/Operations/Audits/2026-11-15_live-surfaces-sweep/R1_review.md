# Live-surfaces sweep — independent review, round 1

Reviewer model: Opus
Round: 1
Scope: `git diff origin/main...HEAD` on `claude/live-surfaces-sweep` (427d8aaa, 967b4f49), checked against `R1_changes.md` and `Moved_Notes.md`. Read and grep only.

## Verdict: PASS WITH FIXES

The sweep is careful. No source text changed, no engine code or emitted string changed, and every cut passage is in `Moved_Notes.md` verbatim. Four substantial findings need fixing before merge: two rewrites changed what a line claims, one checker bug hides four Library headers from the check, and one edited header still carries a false open item.

## Findings

**1. SUBSTANTIAL — The Cyprian Pars III rewrite now names the wrong index as the largest.**
`cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt:9`, now: "(2) three indices, the largest of them a scriptural index (INDEX SCRIPTORVM ...), ... and a word/phrase index (INDEX VERBORVM ..., roughly 20% of the file, the largest of the three)". In the original, "the largest of them" was the index an earlier draft had left out, the word index. The sentence now contradicts itself.
Fix: "(2) three indices: a scriptural index (INDEX SCRIPTORVM, line 18617), a name/subject index (...), and a word/phrase index (..., roughly 20% of the file, the largest of the three)". Line count unchanged.

**2. SUBSTANTIAL — ijc Source Registry row 30 now claims more verification than the record holds.**
`Build/worlds/ijc/Source_Registry.md:43`. Before: "Title confirmed 2026-08-05 ... publisher/series/year added." After: "Title, publisher, series and year confirmed". The new `BUILD-LOG.md` entry says, correctly, that publisher, series and year "were added then". So the registry now says more was checked than the record supports.
Fix: "Title confirmed; publisher, series and year added at that check; not independently re-collated against the book's own text, so B, not A".

**3. SUBSTANTIAL — `_library_header_end` skips four boxed headers entirely.**
The search for the closing rule stops at line 120. Four boxed headers close later than that (counted from line 1): `pachomius_rules-ethiopic_schodde1885.txt` (about 130), `origen_de-oratione-grc_koetschau1899.txt` (about 137), `gregory-great_epistolae-selectae_turchi1907.txt` (about 138) and `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` (about 144). For each, the fallback returns the first blank line, which is line 2, right after the opening rule. That leaves a one-line header, so nothing in these four files is scanned. What it hides: origen:123-126 ("WHY THIS EXISTS: vendored by a research session (session_01WLxh...), 2026-09-08, after an adversarial review ... found ..."), and pl11:89 ("flagged as an open item"). The section 4 count for cic-texts (8) is too low as a result.
Fix: when line 1 is a rule, look for the closing rule anywhere in the bytes read, not just the first 120 lines. Never fall back to the first blank line for a boxed header. Add a test with a boxed header longer than 120 lines.

**4. SUBSTANTIAL — An edited header still says a vendored file is "NOT YET VENDORED".**
`cic/texts/vonsoden_prosopographie-afrikanischer-episkopat-deu_1909.txt`, Content note (this change edited the same header's Provenance note): "NOT YET VENDORED, flagged for a future round rather than acted on unilaterally: ... 'Der Ketzertaufstreit ...' (pp. 1-42)". That article is vendored as `vonsoden_ketzertaufstreit-rom-karthago-deu_1909.txt` (REGISTRY.yaml, date_added 2026-09-29). The line is false now, and the PR's own rule says an edit removes the file's commentary. The checker misses it: ROUTE_CUES has `not yet (resolved|fixed|answered|acquired)` but not "vendored", and has no cue for "flagged for a future round". Section 5 doesn't list it either.
Fix: rewrite it in place as a pointer ("The same volume's earlier von Soden article ... (pp. 1-42) is vendored separately as `vonsoden_ketzertaufstreit-rom-karthago-deu_1909.txt`"). Add `vendored` to the `not yet` cue. List the stale REGISTRY note at REGISTRY.yaml:1884 (protected) in section 5.

**5. MINOR — Section 5 names one header with the superseded evidence rule; thirteen carry it.**
Section 5 names only nestle1904. The phrasing "never primary evidence" or "evidence language is English" also appears in the headers of csel57 (line 9) and harnack (line 9), both edited in this change. It also appears in ausbund, borromeo, busch, faber, three kempis files, piccolomini, pius-v and ribadeneira (all within the first 30 lines).
Fix: list all thirteen in section 5 and in Open-Gaps entry 280, as one content correction for Mark.

**6. MINOR — One open item from the README is now tracked nowhere.**
"Currently unlinked from the site nav — needs a content refresh" (old `cic-website/README.md`, about line 16) was cut. It survives only in `Moved_Notes.md`. Open-Gaps 280 carries the three "Known follow-ups" but not this one. CLAUDE.md says an open item lives in a gaps tracker, not in an audit file.
Fix: add a bullet to entry 280: "support.html needs a content refresh before it is linked again."

**7. MINOR — The claim that every repair is tested is not quite true.**
The System Hub entry says the nine false-positive repairs came "each tested", and R1_changes section 3 says the same. Two of the nine have no test: the "caught by the OCR/scan" exclusion and the "Mark's own" + gospel-noun exclusion. Three new data rules have no test either: the Source-line `pr-ref`, REGISTRY `evidence`/`date_added` protection, and the one-line change-history rule in REGISTRY.
Fix: add the five tests, or correct the wording in both places.

**8. MINOR — Template placeholder detection reaches too far.**
`_template_placeholder_lines` treats any line containing `[` as a placeholder. That includes Markdown links, `[ ]` checkboxes, and `\[` inside code spans. An unclosed bracket carries the depth to the end of the file. Two cases today: `L4-Templates/Deployment_Lexicon_Chunk_Template.md` from line 59 to the end, through a nested `[term]`/`[brief ...` typo, and `Redesign-Spec/Glossary-Story-Quote-Template.md` from line 191, through an escaped `\[` in a regex. Only `route-cue` is excused, so the leak is narrow, but it is a real blind spot.
Fix: reset depth at headings, blank lines and `---`. Skip `[...](...)`, `[ ]`/`[x]` and text inside backticks.

**9. MINOR — `_registry_notes_lines` swallows whole entries.**
Eight REGISTRY entries open with `- date_added:` at indent 0, for example REGISTRY.yaml:11029. `key_indent` becomes 0, so the entry's `filename`, `notes` and `supplied_by` lines are all marked PROTECTED. The docstring promises that other fields are scanned.
Fix: for the `- key:` form, set `key_indent` to the column of the key itself (indent + 2).

**10. MINOR — Two date carve-outs are wider than their stated purpose.**
(a) `_CODE_SPAN_WITH_DATE` also excuses a bare date in backticks, such as `` `2026-09-25` ``. Require at least one non-date character in the span. (b) In Library headers, `iso-date` and `builder-thread` count as data on every header line. That lets dated change narration through, for example `evagrius_praktikos_dysinger.txt:7-17` ("(Fixed 2026-09-03: the original header ... caught when it surfaced ...)"). Limit `builder-thread` to the Source line. Have `_scan_library_header` honour CHANGE_HISTORY_CUES, or add a "Fixed <date>" cue.

**11. MINOR — The new verb list misses an adverb form.**
`Build/worlds/witt/witt_Phase5_Boundary_Testing_Validation_DRAFT.md:385`, "has not yet been comprehensively assessed", is a real open item and no longer matches.
Fix: allow an optional `\w+ly ` before the verb, and add `assessed` and `opened`.

**12. MINOR — Three wording slips in rewritten comments and headers.**
(a) `engine/m1/quote_verbatim.py:110`, "Two of the three source-side patterns (not the stray backslash)", implies the backslash is a source-side pattern. The next sentence calls it a record-authoring bug. Better: "Two of the three patterns (the source-side ones)". (b) Didymus, line 45: "The Greek text is not in this file" overstates. The Greek column was scanned; it OCR'd into Latin-script noise. Better: "No Greek characters survive in this file's OCR", which keeps the line count. (c) Session ids are cut unevenly. Cyprian Pars III lost its sibling-session sentence, and with it the plain fact that closely related material from the same edition was vendored separately. CSEL 34/44, prosper, didymus and origen keep `session_01WLxh...`. Either keep that fact in plain words in Pars III, or treat all of them the same way.

## Checked and found sound

- All 45 `cic/texts/*.txt` edits: every hunk has equal before and after counts (`git diff -U0` hunk headers), and every hunk starts at or before line 80, inside the header. No body line is touched. Didymus is 87,579 lines before and after.
- Every "SECOND WITNESS" and OCR caveat survives, with only the "(Mark's OCR ruling, 2026-09-25)" wrapper removed. That covers the abdisho, aquino, assemani, barlow, boehmer, franck, gerlach, the four hubmaier files, morebath, perkins, racovian, riedemann, rogers, schwenckfeld, servetus, smith and sudermann headers. The Source lines for csel57, possidius and cyprian Pars I-II still name the archive.org items (CSEL57, sanctiaugustiniv00possrich, sthascicaecilic01hartgoog) and keep the "not Google" and character-match bases. The Getty barcode disclosures, the Letter 185 scope and the Perpetua assignment all survive.
- `cic/texts/INTAKE.md`: the rule text is intact. The 2026-09-25 ruling and the framing it replaced are in `LIBRARY-DECISION-LOG.md` (section at line 704). The R33 quotation is in `Moved_Notes.md`.
- `engine/`: 25 files, comments and docstrings only. No code or string changed, including `REDIRECT_TO_REAL_PEOPLE`. Design reasons are kept in present tense (`live_table_battery.py`, `schemas.py`, `output_check.py`, `prose.py`).
- `Moved_Notes.md` has one section per changed live file (45 Library, 25 engine, README, ijc), and the passages are verbatim. The BUILD-LOG entry exists. Open-Gaps 280 carries the three README follow-ups, and its number follows main's 279.
- Nothing touches `cft-website/`, `records/`, packages, spoken fields or scoring. Release 45 territory is untouched, and the `--enforce` sequencing risk is disclosed accurately.
- The BASELINES.md hand labels (lines 10 and 14) are right to read KEEP: the date belongs to the tag and branch names.
- The site reader-text walk handles keys, id-like values, `","` separators and escaped quotes. The slug lookarounds prevent partial matches. Short census ids (`mar-aba-i`, `the-baptists`) are unlikely in prose. Stylesheets are rightly excluded. The 256 KB header read covers 1,825 files, about 0.47 GB, which is acceptable.
- The `pr-ref`, `session-branch`, `review-finding`, `mark-provenance` and `earlier-version` patterns are narrow. I found no false alarms (no `.claude/<hyphenated>` paths on any surface).
- The section 5 deferrals that need a decision are correctly left for Mark: spoken record fields, record bodies, REGISTRY notes, the hadewijch and optatus rights lines, census wording, and the Sandbox card.
