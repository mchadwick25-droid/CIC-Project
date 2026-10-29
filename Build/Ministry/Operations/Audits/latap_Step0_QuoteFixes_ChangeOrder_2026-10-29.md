# Change order: Step 0 quotation findings, latap — 2026-10-29

## 1. Name

Handoff check 8 (quote verification) reports 24 findings for `latap`, all in `Build/worlds/latap/Step0_Movement_Scope_Confirmation.md`. None is in Doc_01 or Doc_02. Step 0 is a settled document (Approved to proceed after Round 7). This is a named change order, not a quiet edit. It touches only the quotation spans listed in section 4.

## 2. Ruling

Mark ruled the shape on 2026-10-29: the 24 quote findings are fixed by a named change order, nothing else in Step 0 is touched, and one targeted Opus review follows that does not count toward the cap of three. The coordination thread files the System Hub Decision Log entry for the ruling.

## 3. Scope

- In scope: the 24 findings, as 21 listed edits (section 4) in one file.
- Out of scope: every other word of Step 0; Doc_01; Doc_02; the Source Registry; the checker (`engine/m10/quotes.py`); the corpus map; every record.
- No claim, confidence rating, scope boundary or sourcing conclusion in Step 0 changes. Three quotations are corrected to what the source says (findings 16, 19, 20) and one emphasis mark is restored (finding 5). Two quotations whose origin cannot be found are no longer set as quotations (findings 1 and 9).

## 4. Findings, classification and evidence

Classes. A: a genuine quotation of a vendored source that the checker cannot read because of markup. B: a quotation of text that is not a vendored source (a corpus-map note, a record, a decision-log heading, a method document, a review file, or a book not in the library); the checker's project-text pool holds only `Build/worlds/_cross-world/`, `Build/reference/` (without review-named files), `CLAUDE.md`, the census and the L1 and Framework `.docx` files, so it cannot find these. C: the quotation is wrong. D: no source for the quotation exists in the tree.

Every row was checked word for word against the real file by hand. Line numbers are lines of the named file on `main` at 987e9c147.

| # | Step 0 line | Quoted words | Class | Evidence | Edit |
|---|---|---|---|---|---|
| 1 | 16 | belonging to his own entry rather than to this one | D | Not found in the tree. The census `voices` field for `latin-apologists` (`cic-website/data/world-census.json`, movements[2].voices[0]) now names Tertullian first; the earlier wording is gone, and history before 2026-10-27 is squashed (`git log -S` finds the phrase only in the squash commit, inside Step 0). | E1 |
| 2 | 43 | on his own text's own evidence | B | `Build/worlds/latap/Review-Artifacts/Step0_Round1_Review.md` line 248 (also 253), where the Round 1 review quotes the first draft's wording. Verbatim. The two shorter phrases beside it (four words each) sit in the same line 248. | E2 |
| 3 | 59 | Two cross-world rulings' attribution, dropped during the small-worlds cleanup batch, recorded here instead of back in the Step0 documents | B | `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md` line 5569, the heading of the 2026-09-26 entry. Verbatim. | E3 |
| 4 | 61 | wrote as a lay apologist rather than this world's own bishop-centered pastoral office | B | `Build/worlds/lpc/Source_Registry.md` line 42 (row 29). Verbatim. | E4, E5 |
| 5 | 61 | per Step 0's own attribution... is credited with forging this world's own theological vocabulary, not with speaking as this world's own voice | B and C | Same line 42. Words verbatim around the ellipsis, which omits `(Doc_01 §2, §6) —`. The source sets forging in italics; Step 0 had it in bold, so the emphasis was altered inside the quotation. Restored to italics. | E4, E5 |
| 6 | 71 | a phase-level process... never a per-world process | B | `Build/reference/L3B-World-Build-Methodology/CiC_L3B_Step0_Movement_Scope_Methodology_V1.0.docx`, Section B, the paragraph beginning "Scope, stated up front": "this is a phase-level process, run once when the project opens a new release phase, never a per-world process." Verbatim with the ellipsis. | E6 |
| 7 | 75 | The entry is right if the usual 3rd-c. North African dating holds and wrong if the 5th-c. Gallic one does. Nothing in the corpus settles it | B | `cic/corpus-map/latin-apologists.yaml` lines 93-97 (the Instructiones row note; the sentence breaks across lines 96-97). Verbatim. | E7 |
| 8 | 83 | A genuine apology addressed to a hostile pagan outsider ... squarely the genre this entry exists to hold | B | `cic/corpus-map/latin-apologists.yaml` lines 164-166 (the Address to Demetrianus row note). Verbatim; the ellipsis omits the parenthesis about Demetrianus and the dash. | E8 |
| 9 | 98 | none of these four texts primarily describes Christian worship practice | D | Not found anywhere in the tree (searched the whole repository, including the corpus map, the census, the dossier and all seven Step 0 reviews). No source for the quotation marks exists. | E9 |
| 10 | 98 | the earliest surviving treatise devoted to baptism | B | `cic/corpus-map/latin-apologists.yaml` line 848 (also `cic/corpus-map/_staging/anf03_tertullian.yaml` line 392): "The earliest surviving treatise devoted to baptism." Verbatim except that the source begins with a capital T; the new text shows that as [t]. | E10 |
| 11 | 98 | noted here, not assigned there | B | `cic/corpus-map/latin-apologists.yaml` lines 954-955 (the On Modesty row note). Verbatim. | E11 |
| 12 | 106 | never as a Native voice of this world's own communities | B | `records/pahc/source/pahc.source.tertullian-apologeticus.md` lines 27-30 (the Boundary discipline note). Verbatim. | E12 |
| 13 | 106 | from outside this world's three core regions | B | Same file, line 16 (the `author` field). Verbatim. | E12 |
| 14 | 106 | OUT-OF-WINDOW TRAP... the systematic treatise mode... unknown to this world's own voices | B | `records/pahc/world_core/pahc.core.house-church.md` lines 91-93 (the YAML doubled apostrophe in world''s reads as world's). Verbatim, three fragments in order. | E12 |
| 15 | 110 | the world's most direct witness to its own legal beginning | B | `records/ijc/source/ijc.source.lactantius-de-mortibus.md` lines 40-41. Verbatim. | E13 |
| 16 | 110 | Lactantius lives in latin-apologists... THE RULING SPLITS THE AUTHOR, WHICH IS WHAT per work MEANS. Lactantius' apologetic corpus moves; Of the Manner in Which the Persecutors Died does NOT. That is the Athanasius case the schema names | C | `cic/corpus-map/latin-apologists.yaml` lines 398-405 reads: "Lactantius lives in `latin-apologists` (I.43): ... This splits the author by work, which is what `per work` means. Lactantius' apologetic corpus is here; *Of the Manner in Which the Persecutors Died* is not. That is the Athanasius case the schema names - ...". The capitals, "THE RULING SPLITS", "moves" and "does NOT" are not in the current map or in `cic/corpus-map/_staging/anf07_lactantius-apostolic-constitutions-didache-liturgies.yaml` lines 60-69; the quoted wording is a superseded version. The meaning is the same. Corrected to the current note. | E14 |
| 17 | 140 | gehen über anderthalb Jahrhunderte auseinander | B (source not vendored) | Schanz-Hosius-Krüger, Geschichte der römischen Literatur III (1922), archive.org item `geschichtederrom00scha`, full-text file lines 23281-23282 (the page marker 269 follows at line 23288): "...gehen über anderthalb Jahrhunderte auseinander." Verbatim. The book is not in `cic/texts`. | E15 |
| 18 | 161 | nam nostra quidem scripta cur ignibus meruerunt dari? cur immaniter conuenticula dirui | A | `cic/texts/arnobius_adversus-nationes-lat_reifferscheid1875-csel-tei.txt` lines 7436-7437: "nam nostra quidem scripta cur ignibus <lb n="10"/> / meruerunt dari? cur immaniter conuenticula dirui, in quibus". Verbatim once the tags are removed (checked by hand). The checker reads the file as plain text and the line-number tag `<lb n="10"/>` falls inside the quotation. Step 0 already cites TEI lines 7434-7437. | none |
| 19 | 167 | Irenaeus and Apollinaris and others who say that after the resurrection the Lord will reign in the flesh with the saints, follow him. Tertullian also in his work On the hope of the faithful, Victorinus of Petau and Lactantius follow this view | C | `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` lines 39881-39885. The edition prints Irenæus with the ligature. Step 0 had spelled it Irenaeus inside the quotation. Corrected to the source spelling. | E16 |
| 20 | 167 | In his extreme old age he was tutor to Crispus Caesar a son of Constantine in Gaul | C | Same file, lines 41051-41053. The edition prints Cæsar with the ligature. Corrected to the source spelling. | E17 |
| 21 | 167 | deinde fecit alterom [sic; the apparatus at line 7423 reads alterum], in quo indoles diuinae stirpis non permansit | A | `cic/texts/lactantius_divinae-institutiones-lat_brandt1890-csel-tei.txt` lines 7395-7396: "deinde fecit alterom,  <lb/> in quo indoles diuinae stirpis non permansit." The apparatus at line 7423 reads "deinde fecit alterum]". Verbatim. The checker fails on the bracketed editorial insertion set inside the quotation. The new text puts the insertion outside the quotation marks and leaves the Latin words unchanged. | E18 |
| 22 | 182 | does not carry the Latin text | B | `engine/m5/records/source/_fleet.source.tertullian-against-praxeas.md` line 32: "it does not carry the Latin text". Verbatim. | E19 |
| 23 | 182 | the nineteen Era 1 entries not already checked by the drafts | B | `Build/worlds/latap/Review-Artifacts/Step0_Round1_Review.md` line 359 (section C8): "Of the nineteen Era 1 entries not already checked by the drafts, **five carry real bearing**...". Verbatim. The file belongs to this world, which the checker leaves out of its project-text pool on purpose. | E20 |
| 24 | 197 | transitional rather than openly sectarian | B | `cic/corpus-map/latin-apologists.yaml` lines 874-875 (the On Exhortation to Chastity row note). Verbatim. | E21 |

Counts: A 2 (findings 18, 21), B 17 (finding 5 included, with an emphasis correction), C 3 (findings 16, 19, 20), D 2 (findings 1, 9). Total 24.

## 5. How each class is handled

- **A, finding 21:** the words are unchanged. The bracketed insertion `[sic; ...]` moves outside the quotation marks, so the checker reads two plain spans. The first span is three words and is not checked by the tool; it was checked by hand (table, finding 21).
- **A, finding 18:** no edit. The words are right and the checker cannot read the `<lb n="10"/>` tag inside them. Splitting the quotation at the line break would present one continuous sentence as two. The finding stays flagged. Reading the file with tags removed (a change to the checker) would clear it, and that is outside this order.
- **B:** the words stay exactly as the source has them. Two changes make the status plain. The quotation marks change from double (“”) to single (‘’), and the file and lines are named at the quotation. The convention: double quotation marks mean a quotation of a vendored source in `cic/texts/`, which the gate checks word for word; single quotation marks mean a quotation of a named project file or of a named outside book, which this change order checked by hand. The gate does not check single-marked quotations, so the evidence in section 4 is the record that they were checked. Adding these files to the checker's project-text pool would let the gate check them again; that is a change to how the build process works, so it is Mark's call and is not part of this order.
- **C:** the quotation is corrected to the source (spelling with the ligature, current wording of the map note, italics for forging). The double marks stay on findings 19 and 20, which are quotations of vendored sources, so the gate checks the corrected text.
- **D:** the quotation marks come off. Finding 1 becomes a statement in Step 0's own words with a short note that the earlier census wording is not preserved. Finding 9 becomes the document's own statement. Both keep their meaning. No source is invented. The Opus review should confirm that the claim in finding 9 (the four original authors' texts do not mainly describe worship practice) stands on the evidence in the document, since it no longer has a quotation behind it.

## 6. Edits, exact old text and exact new text

All edits are in `Build/worlds/latap/Step0_Movement_Scope_Confirmation.md`. Each old string occurs exactly once in the file. Nothing outside these strings changes.

**E1** (line 16; finding 1)

Old:

```
where the census previously named him fifth and separately, "belonging to his own entry rather than to this one." That field
```

New:

```
where the census previously named him fifth and separately, as belonging to his own entry rather than to this one (the earlier census wording is not preserved, so this is a paraphrase). That field
```

**E2** (line 43; finding 2)

Old:

```
that he wrote it "by his own admission," "at his bishop's insistence," or that his freshly-converted, uncatechized status is established "on his own text's own evidence" — all three belong
```

New:

```
that he wrote it ‘by his own admission,’ ‘at his bishop's insistence,’ or that his freshly-converted, uncatechized status is established ‘on his own text's own evidence’ (the first draft's wording, quoted in `Build/worlds/latap/Review-Artifacts/Step0_Round1_Review.md`, B6, line 248) — all three belong
```

**E3** (line 59; finding 3)

Old:

```
System Hub decision log entry "Two cross-world rulings' attribution, dropped during the small-worlds cleanup batch, recorded here instead of back in the Step0 documents" (`Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`).
```

New:

```
System Hub decision log entry ‘Two cross-world rulings' attribution, dropped during the small-worlds cleanup batch, recorded here instead of back in the Step0 documents’ (`Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`, entry heading at line 5569).
```

**E4** (line 61; finding 4, 5)

Old:

```
`Source_Registry.md` row 29 classifies
```

New:

```
`Source_Registry.md` row 29 (line 42) classifies
```

**E5** (line 61; finding 4, 5)

Old:

```
(2) he "wrote as a lay apologist rather than this world's own bishop-centered pastoral office"; and (3) "per Step 0's own attribution... is credited with **forging** this world's own theological vocabulary, not with speaking as this world's own voice."
```

New:

```
(2) he ‘wrote as a lay apologist rather than this world's own bishop-centered pastoral office’; and (3) ‘per Step 0's own attribution... is credited with *forging* this world's own theological vocabulary, not with speaking as this world's own voice.’
```

**E6** (line 71; finding 6)

Old:

```
Section B's own text states this is "a phase-level process... never a per-world process."
```

New:

```
Section B's own text (`Build/reference/L3B-World-Build-Methodology/CiC_L3B_Step0_Movement_Scope_Methodology_V1.0.docx`, the paragraph beginning ‘Scope, stated up front’) states this is ‘a phase-level process... never a per-world process.’
```

**E7** (line 75; finding 7)

Old:

```
with the map's own stated reason: "The entry is right if the usual 3rd-c. North African dating holds and wrong if the 5th-c. Gallic one does. Nothing in the corpus settles it."
```

New:

```
with the map's own stated reason (`cic/corpus-map/latin-apologists.yaml`, lines 93–97): ‘The entry is right if the usual 3rd-c. North African dating holds and wrong if the 5th-c. Gallic one does. Nothing in the corpus settles it.’
```

**E8** (line 83; finding 8)

Old:

```
reads, in part, "A genuine apology addressed to a hostile pagan outsider ... squarely the genre this entry exists to hold."
```

New:

```
reads, in part (`cic/corpus-map/latin-apologists.yaml`, lines 164–166), ‘A genuine apology addressed to a hostile pagan outsider ... squarely the genre this entry exists to hold.’
```

**E9** (line 98; finding 9)

Old:

```
("none of these four texts primarily describes Christian worship practice")
```

New:

```
(none of these four texts primarily describes Christian worship practice)
```

**E10** (line 98; finding 10)

Old:

```
*On Baptism* is, on the corpus map's own note, "the earliest surviving treatise devoted to baptism" anywhere in the vendored library
```

New:

```
*On Baptism* is, on the corpus map's own note (`cic/corpus-map/latin-apologists.yaml`, line 848), ‘[t]he earliest surviving treatise devoted to baptism’ anywhere in the vendored library
```

**E11** (line 98; finding 11)

Old:

```
per the corpus map's own note, "noted here, not assigned there")
```

New:

```
per the corpus map's own note (`cic/corpus-map/latin-apologists.yaml`, lines 954–955), ‘noted here, not assigned there’)
```

**E12** (line 106; finding 12, 13, 14)

Old:

```
and "never as a Native voice of this world's own communities" — the *Apology*'s own note calls him a writer "from outside this world's three core regions," and PAHC's own `world_core` record separately names Tertullian, alongside Irenaeus, as belonging to an "OUT-OF-WINDOW TRAP... the systematic treatise mode... unknown to this world's own voices."
```

New:

```
and ‘never as a Native voice of this world's own communities’ (`records/pahc/source/pahc.source.tertullian-apologeticus.md`, lines 27–30) — the *Apology*'s own note calls him a writer ‘from outside this world's three core regions’ (line 16 of the same file), and PAHC's own `world_core` record (`records/pahc/world_core/pahc.core.house-church.md`, lines 91–93) separately names Tertullian, alongside Irenaeus, as belonging to an ‘OUT-OF-WINDOW TRAP... the systematic treatise mode... unknown to this world's own voices.’
```

**E13** (line 110; finding 15)

Old:

```
which IJC calls "the world's most direct witness to its own legal beginning." The boundary
```

New:

```
which IJC calls ‘the world's most direct witness to its own legal beginning’ (`records/ijc/source/ijc.source.lactantius-de-mortibus.md`, lines 40–41). The boundary
```

**E14** (line 110; finding 16)

Old:

```
in this candidate's own corpus map: "Lactantius lives in `latin-apologists`... THE RULING SPLITS THE AUTHOR, WHICH IS WHAT `per work` MEANS. Lactantius' apologetic corpus moves; *Of the Manner in Which the Persecutors Died* does NOT. That is the Athanasius case the schema names."
```

New:

```
in this candidate's own corpus map (`cic/corpus-map/latin-apologists.yaml`, lines 398–405): ‘Lactantius lives in `latin-apologists` (I.43)... This splits the author by work, which is what `per work` means. Lactantius' apologetic corpus is here; *Of the Manner in Which the Persecutors Died* is not. That is the Athanasius case the schema names’.
```

**E15** (line 140; finding 17)

Old:

```
and that the proposals "gehen über anderthalb Jahrhunderte auseinander."
```

New:

```
and that the proposals ‘gehen über anderthalb Jahrhunderte auseinander’ (the German text, read at archive.org as `geschichtederrom00scha`, is not vendored).
```

**E16** (line 167; finding 19)

Old:

```
"Irenaeus and Apollinaris and others who say
```

New:

```
"Irenæus and Apollinaris and others who say
```

**E17** (line 167; finding 20)

Old:

```
"In his extreme old age he was tutor to Crispus Caesar a son of Constantine in Gaul"
```

New:

```
"In his extreme old age he was tutor to Crispus Cæsar a son of Constantine in Gaul"
```

**E18** (line 167; finding 21)

Old:

```
"deinde fecit alterom [sic; the apparatus at line 7423 reads *alterum*], in quo indoles diuinae stirpis non permansit"
```

New:

```
"deinde fecit alterom," [sic; the apparatus at line 7423 reads *alterum*] "in quo indoles diuinae stirpis non permansit"
```

**E19** (line 182; finding 22)

Old:

```
The record notes that the ANF03 edition "does not carry the Latin text";
```

New:

```
The record notes (`engine/m5/records/source/_fleet.source.tertullian-against-praxeas.md`, line 32) that the ANF03 edition ‘does not carry the Latin text’;
```

**E20** (line 182; finding 23)

Old:

```
whose own stated scope was "the nineteen Era 1 entries not already checked by the drafts,"
```

New:

```
whose own stated scope (`Build/worlds/latap/Review-Artifacts/Step0_Round1_Review.md`, C8, line 359) was ‘the nineteen Era 1 entries not already checked by the drafts,’
```

**E21** (line 197; finding 24)

Old:

```
the map's own note calls *On Exhortation to Chastity* "transitional rather than openly sectarian."
```

New:

```
the map's own note (`cic/corpus-map/latin-apologists.yaml`, lines 874–875) calls *On Exhortation to Chastity* ‘transitional rather than openly sectarian.’
```

## 7. Source access and transparency

Every quotation in Step 0 stays traceable to a file and a locus. Quotations of vendored sources keep their double marks and are checked by the gate. The B and D rows now name the file and lines at the quotation, or say that the earlier wording is not preserved. The vendored-source quotations that carry a ligature are corrected to the printed spelling, so a reader who opens the file finds the same letters. The one outside book (Schanz-Hosius-Krüger) is named with its archive.org item and is marked as not vendored. No quotation is removed without saying why, and no quotation text changes meaning.

## 8. Verification

1. Before applying: each old string is confirmed to occur exactly once, on the stated line.
2. After applying: `git diff` on the file shows only the 21 listed spans (checked by a script that rebuilds the file from the old text plus the 21 edits and compares it with the working file byte for byte).
3. After applying: `python -m engine.m10.cli handoff latap` is run without `--skip-quotes`. Expected: the check 8 count falls from 24 to 1 (finding 18). The result is recorded in the report that accompanies the pull request.
4. Gates run before the push: `python tools/check_live_commentary.py`, `tools/check_paths.py` with `--baseline tools/check_paths_baseline.txt`, and `python -m engine.m10.cli gaps latap`.

## 9. Review that follows

One targeted Opus review of this change order and the Step 0 diff, filed at `Build/worlds/latap/Review-Artifacts/Step0_CapRuling_Review.md`. By Mark's ruling it does not count toward the cap of three. It is run by a different worker. The review checks each of the 24 rows against the named file, the 21 edits against the "nothing else touched" rule, and the unchecked claim in finding 9. The coordination thread files the Decision Log entry that names the review file.

## 10. Ledger

The entry is appended to `Build/worlds/latap/Open_Gaps_Tracking.md`, as the last item of the pull request.
