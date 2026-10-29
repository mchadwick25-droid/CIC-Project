Simulated review — informational only, not an Article 31 substitute.

# Step 0 Movement-Scope Confirmation, latap — Cap-ruling targeted review

**Reviewer model:** Opus 5.5
**Drafter model:** Sonnet 5.5
**Reviewer agent:** cap-ruling review worker, latap Step 0 (isolated; no part in the change order or PR #1304)
**Drafter agent:** latap Step 0 quote-fixes worker (PR #1304)
**Round:** 8 (cap-ruling targeted review; by Mark's ruling of 2026-10-29 it does not count toward the cap of three)
**Truncation check, method 1:** replay of the 21 change-order edits on the pre-PR file, compared byte for byte with the merged file
**Truncation check, method 2:** character-level difflib opcodes of the pre-PR and merged files, each changed region tested for containment inside one edit's old span

**Ruling.** Mark ruled on 2026-10-29 that the 24 check-8 quotation findings in Step 0 are fixed by a named change order (`Build/Ministry/Operations/Audits/latap_Step0_QuoteFixes_ChangeOrder_2026-10-29.md`), nothing else in Step 0 is touched, and one targeted Opus review follows that does not count toward the cap. If it clears, Step 0 is approved to proceed.

**Reviewed:** `Build/worlds/latap/Step0_Movement_Scope_Confirmation.md` as merged by PR #1304 (`d5ef04a8d`), unchanged on `main` since; the change order; the named source files.

**Verdict: Approved to proceed** (Step 0 only; not Frozen). Nothing blocking remains in the change order's scope. The six pre-existing check-8 flags are genuine quotations and are listed for Mark below.

## 1. The 24 rows

Each row was checked against the named file. The vendored texts were read from `cic/texts/` on `main`. Row 17 was read at archive.org.

| # | Result | Evidence |
|---|---|---|
| 1 | verified (D) | The phrase occurs on `main` only in Step 0 and the change order (`git grep`, `git log -S`). The census `voices` field now opens with Tertullian. Paraphrase disclosed. |
| 2 | verified (B) | Round1 review line 248 holds all three phrases. Line 253 repeats the third. |
| 3 | verified (B) | Hub log line 5569, verbatim heading. |
| 4 | verified (B) | lpc `Source_Registry.md` line 42. |
| 5 | verified (B/C) | Line 42. The ellipsis omits "(Doc_01 §2, §6) —". The source has *forging* in italics, now restored. |
| 6 | verified (B) | `.docx` paragraph 26 (under "Section B — Seed Screening and Tiering") begins "Scope, stated up front: this is a phase-level process, run once when the project opens a new release phase, never a per-world process." |
| 7 | verified (B) | Corpus map lines 96–97. |
| 8 | verified (B) | Corpus map lines 164–166. The ellipsis omits the parenthesis and the dash. |
| 9 | verified (D) | The phrase occurs on `main` only in Step 0 and the change order. Its claim is assessed in §3. |
| 10 | verified (B) | Corpus map line 848 and staging line 392; [t] is right. |
| 11 | verified (B) | Corpus map lines 954–955. |
| 12 | verified (B) | pahc Apology record. The words are at lines 29–30, inside the note at 27–30. |
| 13 | verified (B) | Same file, line 16. |
| 14 | verified (B) | pahc `world_core` lines 91–93. The ellipses also drop "are" before "unknown". The meaning is kept. |
| 15 | verified (B) | ijc record lines 40–41. |
| 16 | verified (C) | The new text matches map lines 398–405 and staging lines 60–69. The superseded-version claim holds: `Build/worlds/latap/Review-Artifacts/Step0_Round1_Review.md` lines 66 and 228 quote the map's earlier note, "RULED BY MARK 2026-08-27: Lactantius lives in `latin-apologists` (I.43)... THE RULING SPLITS THE AUTHOR, WHICH IS WHAT `per work` MEANS". |
| 17 | verified (B) | archive.org `geschichtederrom00scha` full text, lines 23280–23281: "…geführt haben, gehen über anderthalb Jahrhunderte auseinander." Page marker 269 follows. The change order's line numbers are one higher, which is immaterial. |
| 18 | verified (A) | Arnobius TEI lines 7436–7437. The words are right once `<lb n="10"/>` is removed. It stays flagged, as the change order says. |
| 19 | verified (C) | npnf203 lines 39881–39885 print "Irenæus". |
| 20 | verified (C) | npnf203 lines 41051–41053 print "Cæsar". |
| 21 | verified (A) | Lactantius TEI line 7395 "deinde fecit alterom,"; apparatus line 7423 "deinde fecit alterum]". |
| 22 | verified (B) | `_fleet` record line 32. |
| 23 | verified (B) | Round1 review line 359. |
| 24 | verified (B) | Corpus map lines 874–875. |

All 24 verified; no defect. Classification counts are confirmed: A 2, B 17, C 3, D 2.

## 2. "Nothing else touched": holds

Document: `d5ef04a8d^1` against `d5ef04a8d`. The pre-PR file is identical to the file at `987e9c147`, whose line numbers the change order uses.

- Method 1: each of the 21 old strings occurs once. Replaying the edits reproduces the merged file byte for byte.
- Method 2: there are 83 changed character regions, none outside an edit's old span. The 14 changed lines are exactly the lines the table names.

Note (not blocking): E18 adds a comma inside the quotation ("alterom,"). The source has it. The change order's "leaves the Latin words unchanged" is true of the words.

## 3. Finding 9's claim: supported

The sentence now reads "none of these four texts primarily describes Christian worship practice". The four texts are the ones the census `sourcing` field names: the *Octavius*, the *Instructiones*, *Against the Heathen* and the *Divine Institutes*.

The document's own evidence supports the claim:

- It describes the four as apologetic or polemical works (§3 B2 "apologetic-argument register").
- It quotes the map calling the *Instructiones* "acrostic verse instruction" (line 75).
- It gives no worship-practice evidence from any of the four.

"Primarily" is the right strength. These works touch worship in passing (for example, the *Octavius* on the charge that Christians have no altars), but none is about it.

The claim is neither overstated nor wrong. Doc_02 should treat it as Step 0's own characterisation, not as a sourced claim. That is a note, not a finding.

## 4. Quotation-mark convention

**Single marks.** There are 21 single-marked quotations in Step 0, and every one names its file.

- Lines are given everywhere except three places, where the source has no line numbers or is outside the library: the `.docx` (named by paragraph), the outside German book (named by archive.org item and marked not vendored), and 'Scope, stated up front' (a paragraph label, not a quotation of content). This is acceptable.

**Double marks.** Double-marked quotations of vendored sources are applied consistently within the 21 edits.

- Step 0 as a whole still double-marks some quotations of project files that the checker's pool covers: the census, the L1 Constitution, `LIBRARY-DECISION-LOG.md` and `NEEDS-RULING.md` (check-8 notes list 15).
- So the change order's section 5 statement that double marks mean a vendored source describes its own edits, not the whole document. Step 0 does not state the convention itself, so nothing in Step 0 misleads.
- Making the whole document consistent would touch text outside this order. Not blocking. Listed for Mark (§6).

## 5. Remaining check-8 flags

The 31-versus-7 discrepancy from the paused run is settled. On a full checkout of `main` at `637d4a306`, `python -m engine.m10.cli handoff latap` reports **7** check-8 findings.

The earlier 31 came from the sparse checkout, which lacked `CLAUDE.md` and `cic-website/data/world-census.json`, both in the checker's project-text pool (`engine/m10/quotes.py`, `_project_texts`). It was not a defect in Step 0.

The 7 are:

| Flag | Source checked | Class | Severity |
|---|---|---|---|
| "nam nostra quidem scripta cur ignibus meruerunt dari? cur immaniter conuenticula dirui" | finding 18 above | A: genuine; the checker cannot read the tag | not blocking; stays flagged by the order |
| "et tandem veluti quibusdam obsidibus pietatis foedus impetravit" | Harnack, *Chronologie* II (1904), line 23357 of the vendored file `harnack_geschichte-der-altchristlichen-litteratur-chronologie-band2-deu_1904.txt` (in the library `texts` directory) on the `claude/latap-library-stage` branch | genuine; source not vendored on `main` | not blocking |
| "zum Erweise seiner jüngst gewonnenen Christlichkeit" | same file, lines 23352–23353 | genuine; not vendored on `main` | not blocking |
| "Also kann er nicht vor c. 260 geschrieben haben" | same file, line 24803 | genuine; not vendored on `main` | not blocking |
| "Der Montanismus des Redaktors ist m. E. unverkennbar" | same file, line 18079 | genuine; not vendored on `main` | not blocking |
| "ne sont pas antérieurs à 260" | `cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome3_1905.txt` line 37712, on `main` | genuine; the file is vendored but Step 0 cites it as "Monceaux III" without its `cic/texts/` path, so the checker never tries it | not blocking |
| "C'est donc entre 260 et 313" | same file, line 37704 (prints C’est with a curly apostrophe) | genuine; same cause | not blocking |

The words were checked with OCR line-break hyphens and runs of spaces joined. The page loci Step 0 gives for Harnack were not re-checked here.

The last six are outside the 24 findings and the 21 edits. They are pre-existing, not defects of the change order. None is wrong or unsourced.

The four Harnack flags should clear when the library-stage branch vendors the *Chronologie* on `main`. The two Monceaux flags need Step 0 to cite the file path. That edit is outside this order, so it is Mark's call.

## 6. For Mark (not blocking)

1. The two Monceaux quotations: whether to add the `cic/texts/` path in Step 0 by a later change order.
2. The double-marked project-file quotations outside this order (§4): whether to bring all of Step 0 onto the single/double convention.
3. Build state: `latap` has no `build/latap_Build_State.yaml` on `main`, and this order does not create one. This file and the System Hub entry are the record of the disposition.

## 7. Methods

- **Completeness of the diff:** two independent methods, as in the header.
- **Count of check-8 flags:** a full checkout run of `handoff latap`, set against the cause of the sparse run's higher count. The cause was found by reading `_project_texts`.
- **Rows:** each read by hand from the named file. Absence claims (rows 1, 9) were checked by `git grep` on `main` and by `git log -S`.
- **Single-mark pass:** a regex listing of every ‘…’ span with its surrounding text.
