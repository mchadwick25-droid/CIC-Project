Simulated review — informational only, not an Article 31 substitute.

**Reviewer model:** claude-opus-5-5
**Drafter model:** Sonnet 5.5
**Reviewer agent:** separate change-order recheck agent (Opus), targeted recheck at medium effort, 2026-10-01
**Drafter agent:** lpc change-order fixer thread, commits 190e49733, a922419a1 and 516d57880
**Round:** 2 (change-order verification pass 2, a targeted recheck; not a Doc_02 revision round and not a Doc_10 revision round)
**Truncation check, method 1:** shell `wc -l` and `tail -n 2` on the saved file; the closing sentinel line is present as the last line.
**Truncation check, method 2:** Python read of the whole file; counts the level-2 headings (8 expected) and confirms the text ends with the sentinel line and a newline.
**Scope:** only what changed since commit 9af959834 ("lpc: Opus verification of the council-date change order"), checked against the prior findings F1–F6, C1 and C2 in `Review-Artifacts/CouncilDate_ChangeOrder_Verification_2026-10-01.md`. Range: `git diff 9af959834..516d57880` (HEAD, clean working tree). Ledger entries checked: the verification-fixes and region-name entry (OG-73, 2026-10-01) and the role-label entry (OG-74, 2026-10-01). Also checked: the project lead's two rulings of 2026-10-01, on the self-naming line and on the role label.
**Status of this file:** a change-order verification by a separate agent. It is not a review round of Doc_02 or Doc_10 and does not count toward either document's round cap. Its file name carries no document prefix, so the `roundcount` gate does not count it.
**Overall verdict:** verified. Every prior finding is resolved, and both rulings hold on every live surface and in the compiled package. Nothing changed by accident. This recheck finds 0 HIGH, 0 MEDIUM, 3 LOW and 3 COSMETIC items (N1–N6). None blocks, and none needs a further recheck once applied.

## 1. Prior findings F1–F6, C1, C2

Each changed line was re-read in the repository and each cited locus was re-opened at source by its structure marker.

**Source loci, re-read.**
- NPNF104 (`npnf104_augustine-anti-manichaean-anti-donatist.xml`): `<div3 type="Chapter" n="7">` at line 19622; §25 opens at 19624. "decreed in our council," is at line 19628. `<note place="end" n="2521">` follows, and line 19631 reads verbatim: "That of Carthage, held June 26 (more correctly, probably June 15th or 16th), 401." It is an endnote in the markup.
- NPNF214 (`npnf214_seven-ecumenical-councils.xml`): `<div4 type="Canon" n="XCII">` at line 35786. Lines 35825–35831 carry "This synod sent a legation to the Princes against the / Donatists." and "The most glorious emperor Honorius Augustus, being consul for the sixth time, on the Calends of July, at Carthage ... Theasius and Euodius received a legation against the Donatists." The heading of Canon XCIII follows at 35847.
- Bruns 1839 (`codex-canonum-ecclesiae-africanae_bruns-pars1-1839.txt`): page header "CODEX ECCLESIAR AFRICANAE. 181" at 12631. Lines 12658–12663 carry "Haec synodus adversus Donatistas legationem ad principes dirigit. Gloriosissimo imperatore Honorio augusto sextum consule, Kalendas Julias *)". The canon heading "XCIHI." (OCR for XCIII) is at 12667. The apparatus at 12688–12689 reads "a. d. XVI. Kal. Jul. Hard. — VI. Kal. Jul. in textu Just. XH. Kal. Jul. Dion."
- Hefele-Leclercq (`hefele-leclercq_histoire-des-conciles-tome2-1-conciles-africains-slice-fra_1908.txt`): page header for section 116 at 4857. Lines 4882–4884 read "Au mois de juin de l'année 404, le IX* concile de Carthage ... députa aux empereurs ... Théase et Evode." Lines 3223–3227 date the fifth council to "le 15 ou le 16 juin de l'année 401", and line 3240 names "ce concile du mois de juin de l'année 401". Line 3463 reads "concile de Carthage eut lieu le 13 septembre 401".

| Finding | Where applied | What it now says | Verdict |
|---|---|---|---|
| F1 (MEDIUM) | Registry row 44, Verification Note | "XVI.5.52 is of 412 — eight years after the events §25 recounts on the 404 dating, eleven on the 401 dating, under different emperors." Exact prescribed wording. | Resolved |
| F2 (MEDIUM) | Doc_02 line 126 | "401 on NPNF's editorial endnote to Letter 185 §25 (n. 2521, ... line 19631: "That of Carthage, held June 26 (more correctly, probably June 15th or 16th), 401"), a year Augustine's own text does not give". The quotation matches line 19631 verbatim. The claim of a note on XVI.5.21 is gone. OG-73 records the correction to the earlier entry's "footnote and endnote". | Resolved |
| F3 (LOW) | Doc_02 line 126; Registry row 44 | Doc_02: "the Latin edition's apparatus gives three variant days, all in June (Registry rows 44 and 202; file lines 12688–12689)". Row 44: "reads *Kalendas Julias*, and its apparatus at lines 12688–12689 gives the variant days XVI, VI and XII Kal. Jul. (16, 26 and 20 June)". The pointer to §1 is gone. Both match the apparatus. | Resolved |
| F4 (MEDIUM) | Registry rows 26, 202, 247 | Row 247's Licensed For is the prescribed cell, ending "licensed for these dates and nothing more". Row 26's Licensed For and Verification Note carry the prescribed additions. Row 202 carries the Latin dating note and its June variants (lines 12658–12663, 12688–12689). Each cell covers the council-date use and claims nothing more. | Resolved (one LOW pointer gap, N1) |
| F5 (LOW) | Registry row 12, Licensed For | Opens "Augustine's own narrower solicitation of state power at the African council that petitioned the emperors" and names both datings, ending "so the date is Contested". The garbled opening is gone. | Resolved |
| F6 (LOW, extended to Doc_01 by the project lead) | Doc_01 lines 160, 182 and 206 | Line 160 names 401 (NPNF) and 404 (the Code of Canons note, lines 35826–35831, row 26; Hefele-Leclercq, row 247, lines 4882–4884), marks the year Contested and points to Doc_02 §8. Line 182 reads "NPNF's editorial note dates 401 and the Code of Canons dates 404 (Letter 185 §25; Contested, Doc_02 §8)". The Round 9 line now reads "the petition's non-grant (Letter 185 §26)", as the prior file's section 7 recommended. Every cited line holds. | Resolved (cosmetic N4, N5) |
| C1 | Doc_02 line 124 | "file lines 3223–3240 and 3463". | Resolved |
| C2 | Doc_02 line 17 | "(Registry row 247, file lines 4882–4884; Letter 185 §§25–26, ...)" in one parenthesis. | Resolved |

**Registry integrity.** Compared at 9af959834 and at HEAD. Rows 12, 26, 44, 202 and 247 are the only rows changed, and they sit on the same file lines (25, 39, 58, 267, 345). Their Confidence letters are unchanged: A, B, A, A, B. Each of the five rows has 12 pipes, and so does every other row. There are 355 numbered rows, 1 to 355, with no duplicate and no gap, identical in both versions. **Verified.**

**Correction to the prior file.** The prior verification placed Doc_01 line 160 in §5 and line 182 in §7. The headings say otherwise: §7 opens at line 144 and §8 at line 169. So line 160 is in §7, and line 182 is §8 item 12. OG-73 repeats the error (see N3). The prior file is a dated review record and stays as written.

## 2. The self-naming line (the project lead's ruling, 2026-10-01)

The ruled line is "I am a representative of the ordinary churches of Latin North Africa."

| Surface | Text found | Verdict |
|---|---|---|
| Voice record `records/lpc/voice_craft/lpc.craft.datus-voice.md`, self-reference note (line 44) | ends "'I am a representative of the ordinary churches of Latin North Africa.'" | Holds |
| Permanent Prompt, line 17 | "you give this answer, in these words: "I am a representative of the ordinary churches of Latin North Africa."" with the once-a-turn cadence | Holds |
| Doc_10, §1A probe 4 (line 87) | "The pass is the single sanctioned self-naming line, "I am a representative of the ordinary churches of Latin North Africa."" | Holds |
| Doc_10, §8 Calibration item 1 (line 390) | the same line, "at most once in a turn and only when asked what the voice is" | Holds |
| Voice Configuration (lines 10 and 39) | the same line in both places; the retired "the voice of the ordinary churches" quotation is gone from the Notes | Holds |
| Compiled prompt of the pinned package `packages/lpc/2026-10-01T16-52-45Z/compiled/prompt.txt` (named in `records/worlds/lpc.yaml`), line 45 | "'I am a representative of the ordinary churches of Latin North Africa.'" | Holds |

**Other self-naming lines.** A search for "I am a representative", "I am the voice", "I am Datus" and "I am a bishop" across `Build/worlds/lpc/`, `records/lpc/`, `records/worlds/lpc.yaml` and the package finds no other live world line. The earlier line survives only as a quoted, excluded item in Doc_10 §3 (line 209) and in dated audit records.

One more line is present by design. Compiled prompt line 13 is the fleet pronoun rule, rendered from `records/_fleet/fleet_voice/_fleet.voice.fleet.md` with the registry's display name: "'I am a representative of Latin Pastoral-Congregational Christianity'". The Doc_10 round 1 review raised this as S9. The project lead's ruling on S9 (the S9 entry, 2026-10-01) records it as fleet practice: the same form, with the world's own name in the world note. Doc_10's Outstanding Concerns (line 372) say the same. It is not a new finding. Changing it would be a fleet-level question.

The voice record's identity field says "He is the voice of the ordinary churches of Latin North Africa". That sentence describes the voice in the third person, as an instruction to the model. It is not a line the voice speaks, and it does not compete with the ruled line.

**Verdict: holds.** One LOW item on the facilitator brief's cadence wording (N2).

## 3. The role label (the project lead's ruling, 2026-10-01)

**Live uses.** "Bishop of the Flock" now stands in all of these:
- the registry `role_label` (`records/worlds/lpc.yaml` line 18);
- the voice record's identity line (line 40);
- the facilitator brief's Datus quotation (line 319);
- Doc_10's title and role paragraph;
- the Voice Configuration header;
- the World Profile's cross-reference;
- Rep Phase 1 and Rep Phase 2;
- the Identity Options decision lines (6 and 61).

In the pinned package, the label appears in `compiled/prompt.txt` line 25, `compiled/capsule.md` line 3, `compiled/frame.json`, `compiled/repository.json`, `compiled/media/portrait.svg` and both record copies.

**No live "Kept Flock".** A search of the whole repository for "Kept Flock" finds no hit in `records/`, `packages/`, `canon/`, `fixtures/`, `engine/`, `cic-poc/frontend/` or `cic-website/`. The phrases "flock kept", "keeps its own" and "kept by a named" are absent from the records and the package.

**Remaining hits, all non-live:**
- the Identity Options history form (lines 6, 61, 100 and 122): "changed from", "as decided on 15 September 2026", "the first role label";
- dated review artifacts;
- earlier ledger entries;
- the Decision Log;
- three files under `Build/Ministry/`.

The portrait caption in the Decision Log and in `Datus_Portrait_Prompt.md` still reads "Kept Flock". OG-74 leaves it open for the project lead. It does not reach the frontend: no file under `cic-poc/` or `cic-website/` carries that caption or names Datus. The compiled `portrait.svg` already carries the new label. Doc_10 line 39, "the flock kept (G1)", is a gravity description, not the label. OG-74 rules it out of scope.

**Identity Options history form.** It reads clearly. The decided label is stated first. The earlier label is named as superseded on 1 October 2026, "not rejected on source grounds", and the 15 September caption is labelled as the caption of that date. The commentary scan (`tools/check_live_commentary.py --base 9af959834`) finds no REWRITE or ROUTE line in any changed file. These lines are PROTECTED.

**Capsule Core line 3.** The old phrase was "the flock kept by a named man who is answerable for it, and the flock that keeps its own." The new one is "a flock in the care of a named man who answers for it, and a flock that holds on to its own, even those who fall."
- **Faithful.** It keeps both halves: a man who answers for his people, and a people that does not let go of its own. "Even those who fall" makes plain what "keeps its own" meant, and the later paragraphs bear it out: "both were still yours, still in the room afterward"; the road back that "is not withheld forever"; "disciplining and receiving back those who fail" in the same paragraph. It adds no claim the Capsule does not already make.
- **Plain and warm.** "In the care of" and "holds on to" are concrete, everyday verbs. They replace a passive participle and a nominal ("is answerable").
- **Consistent.** It matches the next paragraph's "placed in a particular man's care, and he is answerable for them and to them".
- **Readability.** Measured with `engine/m7/readability.py`. The sentence is 38 words, FK 13.8, FRE 63.6 (the old one was 31 words, FK 12.1, FRE 63.5). The paragraph is 107 words in 6 sentences, FK 9.2, FRE 60.7. The paragraph sits inside the band. The sentence runs past the ~25-word guide (COSMETIC, N6).
- The Capsule Core is not compiled into the package. `compiled/capsule.md` is a different, generated header. The Capsule is model-facing support text.

**Verdict: holds.**

## 4. Nothing else changed by accident

Files in the range (17), against the ledger:

| File | Ledger | Verdict |
|---|---|---|
| Doc_01, Doc_02, Source_Registry | OG-73 (F1–F6, C1, C2) | Accounted |
| Permanent Prompt | OG-73 (region name) | Accounted |
| Doc_10, Voice Configuration, voice record | OG-73 (region name) and OG-74 (label) | Accounted |
| facilitator brief, World Profile, Rep Phase 1, Rep Phase 2, Identity Options, Capsule Core | OG-74 | Accounted |
| `records/worlds/lpc.yaml` | OG-74 (role_label); repin in OG-73 and OG-74 | Accounted |
| `packages/lpc/.../manifest.json` (15-26-09Z, then 16-42-33Z, renamed to 16-52-45Z) | repin | Accounted |
| `Open_Gaps_Tracking.md` | OG-73 and OG-74 appended; no earlier line changed | Accounted |
| `build/lpc_Prereview_Doc10.txt` | not named | Header line only (the prereview commit hash); regenerated by the prereview gate. Mechanical. |

The word-level diff of every file shows only the edits the ledger names. Doc_02 changed at lines 17, 124 and 126 only. Doc_01 changed at lines 160, 182 and 206 only. Doc_10 changed in four places: the title, the role paragraph, probe 4, and §8 item 1. No other record changed. **Verdict: clean.**

Two observations, neither a finding of this change order:
- **Package provenance stamp.** The pinned package's `records_commit` and `_generated_by` name 190e49733. That commit's `lpc.yaml` still reads "Bishop of the Kept Flock", but the compiled bytes carry "Bishop of the Flock". The package was built from the working tree before a922419a1 was committed, and the compiler stamps git HEAD rather than the tree. The bytes are right: staleness-check and determinism-check both pass on the current records. Only the stamp is off. This is how the fleet compiler works, not an lpc defect.
- **Doc_01's status note** still sends readers to `lpc_Decision_Log.md` as "the authoritative, append-only record" of post-disposition edits. That log has no entry dated 2026-10-01. The record of the F6 edit is OG-73. The pointer predates this range and is process narration in a canonical file. Under the default actions, a doc-hygiene item outside this thread's own edits is flagged, not touched.

## 5. Gates

All run at HEAD 516d57880 on a clean tree.

- `records lpc`: PASS.
- `regate lpc`: PASS. 274 public-facing fields checked; 150 edited fields below FK 8 are reported, not failed.
- `gaps lpc`: PASS.
- `claims lpc`: PASS (113 derived, 113 registered, 1 registered but unverified).
- `deployed lpc`: PASS, pin 2026-10-01T16-52-45Z, prompt read from disk.
- `staleness-check`: lpc `stale: false`, empty diff; no world stale.
- `determinism-check lpc`: `pass: true`, no differing paths.
- `citations lpc`: FAIL, 10 findings. These are the 10 known findings: unknown ids in `Open_Gaps_Tracking.md` (7, all at lines before 2223, outside OG-73 and OG-74), `Step0_Movement_Scope_Confirmation.md` (2) and `lpc_Decision_Log.md` (1). None is new. On the ten changed build documents, `citations lpc` with explicit paths passes.

## 6. Findings with exact wording for each fix

**N1 — LOW. The pointers in Registry rows 26 and 247 omit Doc_01.** Both cells license the claim, but they name only Doc_02. Doc_01 §7 (line 160) now cites rows 26 and 247 for the 404 dating.
Row 247, Licensed For: replace "cited at Doc_02 §1 and §8." with "cited at Doc_01 §7 and Doc_02 §1 and §8."
Row 26, Licensed For: replace "404 (Doc_02 §1, §8)" with "404 (Doc_01 §7; Doc_02 §1, §8)".
Confidence letters and pipe counts stay as they are.

**N2 — LOW. The facilitator brief gives the self-naming cadence loosely.** The Datus quotation (line 319), in the line OG-74 edited, says "except for one plain line, used once, when someone asks what he is". The ruled cadence is at most once in a turn. "Used once" can be read as once in a conversation, which was the earlier, retired cadence.
Replace "except for one plain line, used once, when someone asks what he is." with "except for one plain line, used at most once in a turn, when someone asks what he is."
A rebuild and repin follow, since this is a record edit.

**N3 — LOW. OG-73 names the wrong Doc_01 sections.** It says "Doc_01 sections 5 and 7 now name both datings". Line 160 is in §7, and line 182 is §8 item 12. The error comes from the prior verification file.
The ledger is append-only. The entry that logs this recheck should say: "Correction to the entry on the council-date verification fixes (2026-10-01): the Doc_01 edits are in section 7 (line 160) and section 8, item 12 (line 182), not sections 5 and 7. The verification file of the same date carries the same slip. Both stand as written."

**N4 — COSMETIC. Doc_01 line 160 is now hard to follow.** "Dated 401 by ... and 404 by ..., a dating Hefele-Leclercq also gives ..., not by Augustine's own text" puts about fifty words between "dated" and "not by". This is optional.
Replace the text from "dated 401 by NPNF's editorial footnote" through "(the year is Contested, Doc_02 §8)" with: "Augustine's own text does not date it; NPNF's editorial endnote at Letter 185 §25 dates it 401, and the note before Canon XCIII in the Code of Canons of the African Church (`npnf214_seven-ecumenical-councils.xml` lines 35826–35831, Registry row 26) dates it 404, as does Hefele-Leclercq (June 404; Registry row 247, file lines 4882–4884), so the year is Contested (Doc_02 §8)".

**N5 — COSMETIC. "Footnote" and "endnote" are both used for the same note.** The markup is `<note place="end">`. Doc_02 line 126 and Registry rows 12 and 44 say "endnote". Doc_02 line 17 and Doc_01 line 160 still say "footnote". (Doc_01's wording came from the prior file's own F6 text.) This is optional.
In Doc_02 line 17 and Doc_01 line 160, replace "NPNF's editorial footnote" with "NPNF's editorial endnote". N4's wording already does this for line 160.

**N6 — COSMETIC. Capsule Core line 3 runs to 38 words.** The two halves also read as "a flock ... and a flock". This is optional and the project lead's call.
Replace the first sentence with: "You live as part of the ordinary church of Latin North Africa. It is a flock in the care of a named man who answers for it, and it holds on to its own, even those who fall." That gives two sentences, of 12 and 26 words.

## 7. What follows

The change order on the council date, its extension to Doc_01, and both rulings of 2026-10-01 are verified. No MEDIUM finding remains, so no further recheck is needed. N1–N3 can be applied as low-severity record corrections. N2 touches a record, so it needs a rebuild and repin, which is a default action. N3 goes into the ledger entry for this recheck. N4–N6 are optional. The outcome of this recheck belongs in `Open_Gaps_Tracking.md` as a new numbered entry. It should cite the entries on the council-date verification fixes and on the role label by subject and date.

The two most recent commits are titled "in-progress checkpoint ... (agent still running)". This recheck checked HEAD 516d57880 on a clean tree. Any later commit from that agent falls outside it.

## 8. Closing

Truncation checks on the saved file. Method 1 (shell): `wc -l`, and `tail -n 2` shows this line and the sentinel. Method 2 (Python): 8 level-2 headings, and the text ends with the sentinel and a newline. Both are recorded in the report that delivers this file. End of file, eight level-2 sections.
END OF CouncilDate_LabelChange_Recheck_2026-10-01
