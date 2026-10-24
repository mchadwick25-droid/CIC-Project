Simulated review — informational only, not an Article 31 substitute.

# Doc_02 and Source Registry recheck: the holdings-disposition fixes

- **Document:** `Build/worlds/lpc/Source_Registry.md` and `Build/worlds/lpc/Doc_02_Source_Ecology.md`, with the Step 0 and Doc_01 P2 fixes; changes read as the uncommitted `git diff` against `50ab82e5`
- **Round:** 40
- **Reviewer:** Opus 5.5, for the whole run; no fallback to another model occurred
- **Reviewer model:** claude-opus-5-5
- **Reviewer agent:** independent recheck subagent, fresh context (drafted none of the fixes)
- **Drafter:** the `lpc` build thread
- **Drafter agent:** the `lpc` build thread's fix pass for Round 39, Step 0 Round 8 and Doc_01 Round 17
- **Date:** 2026-10-24
- **Scope:** only the 17 changed lines: Registry lines 18, 34, 269, 431, 445, 446, 447, 466 and 476; Doc_02 lines 27 and 97; Step 0 lines 40, 109, 110 and 163; Doc_01 lines 164 and 167. Each is checked against the prior finding it answers. Nothing else in the four files is re-reviewed.
- **Ordered by:** the project lead's Cap ruling of 2026-10-24 (`Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`, "Cap ruling: lpc Doc_02, a recheck of the holdings-disposition fixes", the file's last entry)
- **Prior findings:** `Doc_02_Handoff_Recheck_Round39.md` N1 (P1), N2 to N8 (P2); `Step0_Handoff_Recheck_Round8.md` N1 to N4 (P2); `Doc_01_Handoff_Recheck_Round17.md` N11 and N12 (P2)
- **Truncation check, method 1:** line and byte count with an end-of-file read. Registry 476 lines, 481,481 bytes, ends "...Tyconius's own wording or for OG-54. |". Doc_02 160 lines, 98,043 bytes, ends "...from reopening any of the three documents." Step 0 179 lines, 63,383 bytes, ends "...whenever Mark chooses to make it." Doc_01 208 lines, 108,927 bytes, ends "...direct re-examination of the sources."
- **Truncation check, method 2:** line count against `HEAD` plus `git diff --numstat`. Each file has the same line count as at `50ab82e5` (476, 160, 179, 208), and the numstat shows equal insertions and deletions (9/9, 2/2, 4/4, 2/2). No line was lost or added.
- **Method limits:** no web search and no model call. Every new claim was checked in the named `cic/texts/` file, corpus-map note, Registry row, Open_Gaps entry or Manifest. `python -m engine.m10.cli handoff lpc` was run read-only on the working tree: eleven checks and the declaration pass; check 4 fails only because the latest Doc_02 review (Round 39) does not say "Approved to proceed", which this file answers. `git status` was the same before and after the run. Nothing edited except this file.

---

## 1. The Round 39 findings (Doc_02 and the Registry)

| Finding | Fixed? | Checked against | Result |
|---|---|---|---|
| N1 (P1), Monceaux tomes IV to VI Out of scope | Yes | Row 56 (line 71: Native, "Not currently licensed", "vols. IV–VI are vendored"); Optatus at rows 27, 64 and 300 (lines 40, 87, 365), each Native; tome V title page "TOME CINQUIÈME" (file line 99); OG-54 (Open_Gaps line 1763) | All three are now Deferred with a reason that agrees with row 56. Tome V no longer calls Optatus the don world's. "Revisit for the OG-54 assessment" is right: OG-54 assesses tractatus ascribed to Optatus. The three rows now match the tomes VI to VII row. **Closed.** |
| N2 (P2), Tyconius | Yes | File header (lines 6 to 7: condemned by Parmenian and a Donatist council c. 380); Burkitt's own date section (file line ~667: "Tyconius wrote before 383 AD") and line 15528 ("an African who flourished about 380 AD"); `npnf102` lines 53014 to 53019 (*On Christian Doctrine* III.30, "The Rules of Tichonius the Donatist Examined", chs. 30 to 37); row 16 (*On Christian Doctrine* I to IV, Native) | "c. 380" is supported by the file. Augustine's use of Tyconius in Book III is real and row 16 holds that work. "Donatist-milieu" fits the header, which leaves his formal standing open. **Closed.** |
| N3 (P2), `npnf211` | Yes, with one citation point | Sulpicius, Dialogue I (div3 at file line 2535): "a great desire to go to Carthage, to visit those localities connected with the saints, and, above all, to worship at the tomb of the martyr Cyprian" (lines 2657 to 2661, Latin note "Ad sepulchrum Cypriani martyris adorare"). Vincent, section [16.] (line 12513): "Agrippinus, bishop of Carthage ... held the doctrine ... that Baptism ought to be repeated", with Stephen's resistance following | Both passages are real and say what the row says. "c. 400" is not stated in the file; it rests on the usual dating of the Dialogues (c. 404, the speaker back from a journey begun "three years before"), and a "c." date in a disposition reason is fair. See R40-N2 for the "Commonitorium 16" locus. **Closed**, one P2 below. |
| N4 (P2), Boyd provenance | Yes | `Build/worlds/don/Source_Acquisition_Manifest.md` G3 (Boyd as the Mommsen-Meyer substitute); `Build/worlds/lpc/Source_Acquisition_Manifest.md` G3 is Possidius | Now names the sibling Donatism build and "its" G3. True. **Closed.** |
| N5 (P2), Doc_02 lines 27 and 97 | Line 27 yes; line 97 partly | Doc_01 line 168 (World #4 bullet: "what remains open is the Optatus placement question ... and the duplicated Council-of-Carthage-under-Cyprian corpus-map rows ... both genuinely Doc_02's, carried forward again at §8 below"); Doc_01 line 37 (§2 disclosure); Doc_02 §6 line 112, §8 line 128, §9 lines 131 to 149 | Line 27 now says "carrying them forward at its own §8", so the pointer is Doc_01's. The paraphrase is true. The sentence still says "§8" twice ("hands them to §8 ... at its own §8"); the second resolves the first, so it reads, if a little heavily. Line 97 no longer names Doc_02 in the third person. But its new pointer "open at §6 and §9 below" is half wrong: §9 does not carry the substrate question. See R40-N1. |
| N6 (P2), `npnf107` drawn on through an unlicensed row | Yes | `npnf107` div1 "Lectures or Tractates on the Gospel According to St. John" (file line 455); lpc corpus map `yaml:1709` to `:1720` (Tractates, "124 tractates (~412,000 words)", `source_file: npnf107_...`) | Row 21 now names the file after the Tractates' word count, which is the corpus map's own figure for that work. Attribution true. The row's other three works sit partly in `npnf107` (Ten Homilies, file line 13626) and partly in `npnf106`; the row claims only the Tractates' file, so nothing false is added. **Closed.** |
| N7 (P2), row 204 normalized Latin | Yes | `perpetua-scillitan-martyrs-lat-grc_robinson1891.txt` line 7375: "Praesente bis et Claudiano consulibus, xvI Kalendas Augus-" | The quotation is gone. "Names the consuls and gives the date as the sixteenth day before the Kalends of August" describes the formula rightly (Praesens, consul for the second time, and Claudianus; XVI Kal. Aug.). The OCR disclosure that follows still makes sense as a note on the scan. **Closed.** |
| N8 (P2), row 5 corpus-map notes in marks | Yes | lpc corpus map `yaml:2337`, `:2347`, `:2400` | Line 18 has no quotation marks left. Each paraphrase keeps the note's sense and is still credited to "the corpus map's own notes". **Closed.** |

### R40-N1 (P2). Doc_02 line 97 points to §9 for a question §9 does not carry

- **Where:** Doc_02 line 97: "That question is not resolved; it is open at §6 and §9 below."
- **Evidence:** §6 carries it (line 112, "The Punic- and Berber-speaking rural substrate, named but not resolved"). §9 (lines 131 to 149) does not name the substrate question; its item 11 discharges Doc_01 §8 item 3, the source-skew disclosure, at §6. The question is held open at §8, the Confidence Map, under **Contested** (line 128: "the exact extent to which the Punic/Berber substrate culture shaped ordinary congregational life specifically (§5, §6 above)"). The wrong pointer came from Round 39's own suggested wording, which the fix followed.
- **Why P2:** it is the same kind of pointer slip N5 named. Nothing is misstated about a source, and §6 is right.
- **Fix:** "it is open at §6 and §8 below."

### R40-N2 (P2). "Commonitorium 16" sends a reader to the wrong chapter of this file

- **Where:** Registry line 466: "Vincent's Commonitorium 16 reports the Carthage rebaptism question."
- **Evidence:** in `npnf211` the passage is section [16.] (line 12513) inside "Chapter VI. The example of Pope Stephen in resisting the Iteration of Baptism" (div2 at line 12470). The file's "Chapter XVI" (line 13293) is "Recapitulation of what was said of the Catholic Faith and of divers Heresies". A reader who takes "16" as a chapter finds the wrong text. Again, the wording was Round 39's.
- **Why P2:** the claim is true; only the locus is ambiguous.
- **Fix:** "Vincent's Commonitorium, ch. 6 (§16), reports the Carthage rebaptism question."

---

## 2. The Step 0 and Doc_01 P2 fixes

| Finding | Fixed? | Checked against | Result |
|---|---|---|---|
| Step 0 R8 N1, line 110 Council of Carthage note | Yes | lpc corpus map `yaml:1875` to `:1877` | Now reads "because the Donatists claimed this council's baptismal doctrine as their patrimony". It no longer makes Donatism the thing claimed by both sides. Matches the note and Doc_02 line 27. **Closed.** |
| Step 0 R8 N2, line 109 "this volume" | Yes | lpc corpus map `yaml:939` and `:950` ("17 letters, ~52,892 words"; "the largest single thing in this volume after the Confessions"), `source_file: npnf101_augustine-confessions-letters.xml` (`:951`) | Now "the largest single item in the `npnf101` volume after the Confessions, per the corpus map". Referent and credit both right. **Closed.** |
| Step 0 R8 N3, line 163 IJC imperative | Yes | `records/ijc/source/ijc.source.augustine-confessions.md` line 39 ("do not extend this license.") | Now "and telling the reader not to extend the license". The instruction is the IJC record's again. **Closed.** |
| Step 0 R8 N4, line 40 marks on corpus-map notes | Yes | `yaml:2337`, `:2347` | No marks remain on line 40. "*De Bono Patientiae* reworks Tertullian's *De Patientia*" and "*De Habitu Virginum* follows Tertullian's dress treatises" keep the notes' sense, credited to the corpus map. **Closed.** |
| Doc_01 R17 N11, line 164 Letter 185 | Yes | ijc corpus map `imperial-juridical-christianity.yaml:186` to `:194` ("Direct evidence for the ijc world's core question — the church's use of imperial law") | The note is now credited to the ijc map, not this world's. The judgment "the strongest documented datum on the side this reframing does not favor" is now a separate sentence in Doc_01's own voice. **Closed.** |
| Doc_01 R17 N12, line 167 "this volume" | Yes | as Step 0 N2 | Same wording as Step 0 line 109. **Closed.** |

---

## 3. Sentences and readability

Every changed line was read whole. No fix leaves a broken sentence. The nine Registry lines are short, plain statements; the new disposition reasons run 10 to 25 words a sentence, with one idea each. Step 0 lines 40, 110 and 163 and Doc_01 line 164 are shorter or plainer than before; Doc_01 line 164 gains a full stop that splits a long clause in two.

One observation, not a finding. Doc_02 line 97 keeps the earlier verbless fragment ("A Romanized provincial society with real underlying Punic and Berber populations, per Doc_01 §2's own disclosure, which leaves to this document how deeply that substrate culture shaped ordinary congregational life."), now 31 words. It is construction prose, not participant-facing, and it reads clearly.

---

## 4. Outside the changed lines

### R40-N3 (P2). OG-59's holdings counts and Phase L2 list are now out of date

- **Where:** `Build/worlds/lpc/Open_Gaps_Tracking.md` OG-59 (line 1808): "56 files: 47 out of scope, 9 deferred"; and its "Deferred holdings to weigh in Phase L2" list (line 1811), which names only Arnobius, Lactantius and the *Collatio cum Maximino*.
- **Evidence:** the section now holds 42 Out of scope and 14 Deferred (counted by script over the table's Disposition column). Monceaux tomes IV and V, Tyconius and `npnf211` are newly Deferred and are not on the Phase L2 list.
- **Why P2:** the Registry is right; the tracking record lags it. Entries are append-only, so OG-59 stays as written.
- **Fix:** log the recount and the five newly Deferred files in a new Open_Gaps entry, citing this round by subject and date.

---

## Summary

Every prior finding is fixed. The P1 is closed: Monceaux tomes IV to VI are Deferred with a reason that agrees with row 56 and holds Optatus rightly as Native here. The Tyconius and `npnf211` reasons were checked in the vendored files: Tyconius c. 380 (Burkitt: before 383), Augustine's use of him in *On Christian Doctrine* III.30 to 37, Sulpicius's visit to Cyprian's tomb in Dialogue I, and Vincent's report of Agrippinus and rebaptism. The row 21 file attribution and the row 204 description of the consular formula are true. The Step 0 and Doc_01 fixes are all true to their sources. Two pointer slips came in with Round 39's own suggested wording (R40-N1, R40-N2), and the OG-59 counts now lag the Registry (R40-N3). None misstates a source.

Counts: 0 P0, 0 P1, 3 P2 (R40-N1 to R40-N3). Prior findings closed: Round 39 N1 to N8, Step 0 Round 8 N1 to N4, Doc_01 Round 17 N11 and N12.

VERDICT: Approved to proceed
