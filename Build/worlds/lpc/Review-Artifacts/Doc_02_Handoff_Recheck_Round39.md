Simulated review — informational only, not an Article 31 substitute.

# Doc_02 and Source Registry recheck: the Phase L1 handoff changes

- **Document:** `Build/worlds/lpc/Doc_02_Source_Ecology.md` and `Build/worlds/lpc/Source_Registry.md`, changes read as `git diff 5cc91f71 31fc57ae` (the changes are in `7191a6d5`)
- **Round:** 39
- **Reviewer:** Opus 5.5, for the whole run; no fallback to another model occurred
- **Reviewer model:** claude-opus-5-5
- **Reviewer agent:** independent recheck subagent, fresh context (drafted none of the changes)
- **Drafter:** the `lpc` build thread
- **Drafter model:** claude-opus-5-5
- **Drafter agent:** the `lpc` build thread's Phase L1 handoff pass (drafter model per the commit trailer of `7191a6d5`)
- **Date:** 2026-10-24
- **Scope:** every changed line in Doc_02 (10 lines) and in the Registry (105 changed lines, plus the new Holdings dispositions section, lines 415 to 476, 56 files). Covered: the removed quotation marks and new italics; the four corrected quotations (rows 194, 206, 212, 229); the Delehaye date and the Monceaux and Mansi title pages; each of the 56 dispositions against the file's head and its corpus-map placement; the *Soliloquies* addition to row 25. Neither document is otherwise re-reviewed.
- **Ordered by:** the project lead's Cap ruling of 2026-10-24 (`Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`, "Cap ruling: lpc Step 0, Doc_01 and Doc_02, one recheck of the Phase L1 handoff changes", the file's last entry)
- **Truncation check, method 1:** line and byte count with an end-of-file read. Doc_02: 160 lines, 98,230 bytes; ends "from reopening any of the three documents." Registry: 476 lines, 481,494 bytes; ends on the Tyconius disposition row, "places it in donatism.yaml only. |".
- **Truncation check, method 2:** hash comparison. `sha256sum` of each working file equals that of `git show 31fc57ae:<path>` (Doc_02 `4e08b6543634…`, Registry `25c127b21ddf…`).
- **Method limits:** no web search and no model call. The diff was split into per-line word changes by script. Each corrected quotation was matched against the named `cic/texts/` file by line number. Each disposition was checked with the file's header, a grep of the file for Carthage, Hippo, Cyprian and Augustine, and `grep -rl <stem> cic/corpus-map`. `python -m engine.m9.cli holdings lpc` was run (read-only) to confirm the report's lists. `python -m engine.m10.cli handoff lpc` was run at `31fc57ae`: all twelve checks and the declaration pass. The findings below are ones the gate does not test. Nothing edited except this file.

---

## 1. The four corrected Registry quotations

| Row (file line) | Quotation now | Vendored file, line | Result |
|---|---|---|---|
| 194 (259) | "YOL. III. PARS III. APPENDIX."; "VITA CAECILII CYPRIANI" with "(Pontio diacono iiiilgo adscripta)." on a following line | `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt`, lines 27, 40258, 40260 | Word for word, OCR letters kept |
| 206 (271) | "TOME PREMIER" and "TERTULLIEN ET LES ORIGINES," 1901 | `monceaux_histoire-litteraire-afrique-chretienne-tome1_1901.txt`, lines 64, 66, 75 | Word for word. The title page is confirmed. |
| 212 (277) | Préface "dated Toussaint 1920; the file's OCR reads "jeté de la Toussaint, .1920"" | `delehaye_passions-martyrs-genres-litteraires-fra_1921.txt`, line 117 ("Bruxelles, jeté de la Toussaint, .1920."), the Préface's close (it opens at line 97) | Word for word. The date statement is right: "fête de la Toussaint" is All Saints' Day, so the Préface is dated 1 November 1920 in substance, and the row now says only "Toussaint 1920". |
| 229 (294) | "Ab anno CCCCX. ad annum CCCCXXXI." | `mansi_sacrorum-conciliorum-collectio-tomus-4-410-431-lat_welter-facsimile1901.txt`, line 142 | Word for word. "TOMUS QUARTUS." is line 66 and "190!" is line 96, as the row says. The title page names "H. WELTER" with "A PARIS et a LEIPZIG", which matches "Welter facsimile (Paris and Leipzig, 1901)". |

All four are correct. The old normalized forms are gone, as the Process V2.0 Quotations rule asks.

---

## 2. Removed quotation marks and new italics

| Where | Result | Evidence |
|---|---|---|
| Doc_02 line 25 (Optatus notes) | Meaning kept | Matches `latin-pastoral...yaml:2825` to `:2830` and `donatism.yaml:841` to `:842`. |
| Doc_02 line 27 (Council of Carthage note) | Note paraphrased rightly; one pointer now wrong | The paraphrase matches `yaml:1875` to `:1877`. See N5 for "§8 below". |
| Doc_02 lines 29, 39, 40, 47, 56, 122, 135 | Meaning kept | Each keeps its named source (corpus map, Doc_01, Doc_01 §5, row 38's Licensed-For). The corpus-map wording on lines 29 and 56 matches `yaml:2932` and the Pontius note. |
| Doc_02 line 97 (Doc_01 §2 disclosure) | Meaning kept, voice shifted | See N5. |
| Registry line 6 | Meaning kept | A template phrase, now plain prose. |
| Registry rows 5, 10, 12, 15, 23, 25, 27, 28, 29, 42 (lines 18 to 56) | Meaning kept | Each corpus-map paraphrase was matched to its note (for example row 15 to `yaml:1242` to `:1243`; row 23 to `yaml:1452` to `:1454`; row 28 to `yaml:2932` to `:2934`). Row 29 now says "the wording is Doc_01's own", which keeps the attribution. |
| Registry row 44 (line 58) | Meaning kept | The sibling Registry's row 16 is still named as the speaker. |
| Registry rows 99, 103, 200, 204, 210 (lines 140, 144, 265, 269, 275) | Meaning kept | Each keeps its source (Doc_02's own risk statement, the copyright verso, the task brief, a Decision Log entry title). |
| Registry rows 111 to 190 (lines 155 to 252) | Readable, consistent | Article titles move from quotation marks to italics, with italic words inside each title set roman. No title text changed. |
| Registry lines 285 to 373 (33 OCR-count lines) | Meaning kept | The double quotation mark leaves the code span and is named in words. The character set is the same. |

No sentence now presents a quoted ruling or another document's claim as Doc_02's or the Registry's own, apart from the pointer shift in N5.

---

## 3. Holdings dispositions (56 files)

The section has 56 rows: 47 Out of scope, 9 Deferred, as OG-59 says. `holdings lpc` lists the same "not yet assessed" files that no Registry row names. Every reason was checked against the file's head and its corpus-map placement.

**True and rightly placed (50 files).** The other 42 Out of scope rows (Greek, Syriac, Egyptian-desert, Cappadocian, Antiochene, Alexandrian, Gallic and later-Roman files): each reason is true, each corpus-map placement is as stated, and none bears on Carthage or Hippo in 246 to 430, on Cyprian's or Augustine's own words, or on OG-54. The Deferred rows for Arnobius (`anf06`), Lactantius (`anf07`), the *Collatio cum Maximino*, Monceaux tomes VI to VII, Eusebius VII.3 (`npnf201`), `npnf203`, Jerome's letters (`npnf206`) and Ambrose (`npnf210`) are right, and their quoted headings are real (for example Eusebius's chapter title, and the De viris illustribus titles "Cyprian the bishop.", "Pontius the deacon." and "Augustine the bishop."). `npnf206` also holds letters headed "From Augustine", so Augustine's own words are in it; Deferred covers that.

**The six rows below need attention.**

### N1 (P1). Monceaux tomes IV, V and VI are marked Out of scope, against row 56 and on a false reason for tome V

- **Where:** Registry lines 445, 446 and 447 (`monceaux_...tome4_1912.txt`, `...tome5_1920.txt`, `...tome6_1922.txt`), each "Out of scope", each ending "Registry row 56 already names this volume as vendored and unlicensed here."
- **Evidence:**
  - Row 56 (line 71) holds the seven-volume *Histoire littéraire* as **Native**, "Not currently licensed for a specific claim", and says "vols. IV–VI are vendored in the shared corpus". Native and unlicensed is in scope. The dispositions cite row 56 and then contradict it.
  - Tome V's reason calls the volume "a study of Optatus and the first Donatist writers, which is the don world's territory". Optatus is not only the don world's. This world holds him Native at rows 27, 64 and 300, Doc_02 §7 (line 122) names him as the gap's first dated row, and Doc_02 §1 (line 25) keeps his placement open. The don corpus map's own note on tome V calls it "the volume of this series most directly on" Optatus (`donatism.yaml:784` to `:786`).
  - All three volumes bear on this world's place and time: Carthage and Hippo 303 to 430 (the file greps give 821, 163 and 385 lines naming Carthage; 1,429, 334 and 971 naming Augustine). Step 0 §2 A5 and §4 item 2 bind this world to reconstruct the Donatist schism from its own side. Tome V bears on the OG-54 silence assessment through Optatus, and tome IV through the gap's history.
- **Why P1:** handoff check 4 asks for "out of scope with a reason". These reasons contradict the Registry's own row 56, and tome V's is false. The task's own test applies to all three: each bears on this world's place and time, and tome V on OG-54.
- **Fix:** mark all three Deferred, as tomes VI to VII already are. For example: "Deferred. Modern history of Donatism in Africa (tome V: Optatus, Native here at rows 27, 64 and 300). Row 56 holds the series Native and unlicensed. Revisit for the OG-54 assessment and for any claim on the schism."

### N2 (P2). Tyconius should be Deferred

- **Where:** line 476: "Out of scope | Tyconius's Book of Rules; the file names him Donatist-affiliated, so it is the Donatism world's territory."
- **Evidence:** the reason's facts are true (file header, `donatism.yaml:936` to `:950`). But the same corpus-map note says "Augustine himself drew on it". Augustine's *On Christian Doctrine* (row 16, Native) takes up Tyconius's rules in its Book III. The file header dates his condemnation to c. 380, inside the 258 to 391 gap, in Africa. Arnobius, also inside the gap, is Deferred on that ground.
- **Why P2:** the reason is not false, and Augustine's own text already carries what he took from Tyconius. The category is still wrong by the test this section applies to Arnobius.
- **Fix:** "Deferred. Donatist-milieu work, c. 380, that Augustine draws on in *On Christian Doctrine* III (row 16). Revisit if a claim needs Tyconius's own wording or for OG-54."

### N3 (P2). `npnf211` should be Deferred

- **Where:** line 466: "Out of scope | Sulpicius Severus, Vincent of Lerins and Cassian: Gaul."
- **Evidence:** the volume carries two passages on this world. Sulpicius's first Dialogue has Postumianus land in Africa, go to Carthage "to visit those localities connected with the saints, and, above all, to worship at the tomb ... of the martyr Cyprian" (c. 400; file text near the "great desire to go to Carthage" passage). Vincent's *Commonitorium* §16 discusses "Agrippinus, bishop of Carthage" and the rebaptism question. The Eusebius row (line 456) is Deferred on the same kind of later, outside report of Cyprian's rebaptism position.
- **Why P2:** "Gaul" is true. The bearing is narrow. But the disposition is inconsistent with the Eusebius row, and the Sulpicius passage is a contemporary witness of Carthage.
- **Fix:** "Deferred. Gallic volume; Sulpicius, Dialogue I, describes a visit to Cyprian's tomb at Carthage c. 400, and Vincent's Commonitorium 16 reports the Carthage rebaptism question. Revisit if a claim needs either."

### N4 (P2). The Boyd reason names the wrong build and the wrong G3

- **Where:** line 431: "vendored by this build as a substitute for the Mommsen-Meyer edition (Source_Acquisition_Manifest G3)".
- **Evidence:** Boyd was vendored by the Donatism build as a substitute under its own G3 (`Build/worlds/don/Source_Acquisition_Manifest.md:23` and `:65`). This world's G3 is Possidius (`Build/worlds/lpc/Source_Acquisition_Manifest.md:29`). Row 44 itself says the G3 request was the sibling build's. The corpus map places Boyd only in `donatism.yaml`. The Deferred disposition is right; the provenance is false.
- **Fix:** "vendored by the sibling Donatism build as a substitute for the Mommsen-Meyer edition (its Source_Acquisition_Manifest G3)".

### N5 (P2). Two de-quoted Doc_01 passages now speak with Doc_01's pointers in Doc_02's voice

- **Where:** Doc_02 line 27: "— what remains open is the Optatus placement question and the duplicated Council-of-Carthage-under-Cyprian corpus-map rows, both genuinely Doc_02's, carried forward again at §8 below." Doc_02 line 97: "per Doc_01 §2's own disclosure — how deeply that substrate culture ... is a genuine open question for Doc_02's Source Asymmetry work, not resolved or assumed here."
- **Evidence:** both were Doc_01's words in marks. "§8 below" meant Doc_01 §8. In Doc_02 it now points to Doc_02 §8, the Confidence Map, which does not carry these items; Doc_02 carries them at §9 (line 145 area). On line 97, Doc_02 now names itself in the third person and says "here", and the next sentence repeats "That question is not resolved".
- **Why P2:** the next sentence on line 27 names Doc_01 §8 item 2, so a careful reader can recover the sense. Nothing is misstated about a source.
- **Fix:** line 27: "...hands them to §8 as unresolved, saying both are genuinely Doc_02's and carrying them forward at its own §8." Line 97: "per Doc_01 §2's own disclosure, which leaves to this document how deeply that substrate culture shaped ordinary congregational life. That question is not resolved; it is open at §6 and §9 below."

---

## 4. The *Soliloquies* addition to row 25

Row 25 now names "*Soliloquies* (*Soliloquia*, in `npnf107_augustine-homilies-john-soliloquies.xml`)". The file holds the *Soliloquies* (heading at file line 444; the editor's note at line 416). The corpus map places the work in that file at "div1 5 — Two Books of Soliloquies" (`yaml:1626` to `:1637`). The addition is true and adds no claim.

### N6 (P2). The addition makes `npnf107` "drawn on" through a row that licenses nothing

- **Where:** Registry line 38 (row 25).
- **Evidence:** `npnf107` was named in no row before this change. `holdings lpc` now lists it as "drawn on". Row 25 is "Not currently licensed for a specific claim". The file's main content, the 124 Tractates on John, sits at row 21, which still does not name the file. The label is the tool's, but a reader of the holdings report would think the file is used.
- **Fix:** name `npnf107` in row 21 as well, where the file is the Tractates' source, or note in row 25 that the file is named for location only.

---

## 5. Other lines in the diff

### N7 (P2). Row 204 still carries a normalized quotation of scanned Latin

- **Where:** line 269 (row 204): "Praesente bis et Claudiano consulibus, XVI Kalendas Augustas...", "quoted here in normalized form".
- **Evidence:** the Quotations rule says a quotation of scanned Latin keeps the scan's letters. The row itself says the scan reads "xvI" and splits "Augus-"/"tas". The gate passes it only because the file's own header repeats the normalized form. The same fix was made at row 194 and not here. This line changed in the diff (the task-brief phrase), so it falls inside this recheck.
- **Fix:** quote the scan's own letters, or drop the marks and describe the opening formula.

### N8 (P2). Row 5 keeps three corpus-map notes in quotation marks

- **Where:** line 18 (row 5): "reworks Tertullian's *De Patientia*", "following Tertullian's dress treatises", "compiles Tertullian and Minucius Felix".
- **Evidence:** all three are corpus-map notes (`yaml:2337`, `:2347`, `:2400`), and all three are word for word. The rule forbids marks around a corpus-map note. The change removed the marks from the fourth note in the same list ("dependent on Tertullian's *De Oratione*").
- **Fix:** drop the marks from the other three, as for the fourth.

---

## Summary

The four corrected Registry quotations match their vendored files word for word, and the Delehaye date and the Monceaux and Mansi title pages are confirmed. The removal of marks keeps every attribution in Doc_02 and the Registry, with two pointer shifts in Doc_02 (N5). The *Soliloquies* addition is true (N6 is a labelling point). Of the 56 holdings dispositions, 50 are right. Three Monceaux volumes are marked Out of scope against the Registry's own row 56, and tome V on a false reason, though Optatus is Native here and bears on OG-54 (N1, P1). Tyconius and `npnf211` should be Deferred (N2, N3), and the Boyd row names the wrong build (N4).

Counts: 0 P0, 1 P1 (N1), 7 P2 (N2 to N8).

VERDICT: Substantial revision required
