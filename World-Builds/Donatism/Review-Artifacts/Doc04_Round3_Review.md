# Doc_04 — Gravity Discovery: Round 3 Independent Adversarial Review (Confirming Pass)
## Donatism Formation World

**Reviewed document:** `Doc_04_Gravity_Discovery.md` + companion `Gravity_Index.xlsx` (status at review: DRAFT — pending independent adversarial review; this is the post-Round-2-fix state, commit `0420a514`)
**Reviewed against:** `Doc_01_World_Identification_Boundaries_Orientation.md` §5 (six-cell sketch, read directly), `Doc_03_Lexicon_Candidate_List.md` §1 and §5 (read directly), `Gravity_Index.xlsx` (read directly via openpyxl, all four sheets), and the document's own internal cross-references. `Doc04_Round1_Review.md` and `Doc04_Round2_Review.md` were read for format and to know what was claimed fixed, but every claim was independently re-verified against the documents themselves — including diffing commit `0420a514` directly against its parent to see exactly what the Round 2 fix pass changed, rather than trusting either round's or the task brief's own account of it.
**Scope:** per the task brief, this is a **narrow confirming pass** on five specific claimed fixes (Round 2's H1, M1, M2, M3, L1), plus a clean-documents re-grep and a final arithmetic/cross-reference sanity check. Round 1's and Round 2's own substantive findings (G3's three-vs-four-texts count, G5's original orphaning, the Frend fabrication, etc.) are not re-litigated except where needed to confirm the five fixes didn't disturb them.
**Simulated review — informational only, not an Article 31 substitute.**

---

## Verdict: SUBSTANTIAL REVISION REQUIRED (narrow — one new one-word defect)

Four of the five claimed fixes are genuinely, correctly, and cleanly applied, with no new inconsistency introduced anywhere else in the document or the workbook. The fifth (M3 — the G5 lexicon-forwarding clause in §7) is also *substantively* applied — Doc_03's actual Tier-2 listing and §1 section location are both accurately cited — but the sentence the fix added contains its own new, independently checkable arithmetic error: it says the G5 lexicon term should be reconsidered for Tier-1 "alongside the other **four** terms just named," when the same sentence, two clauses earlier, actually names **five** terms (Traditor/Traditio, Rebaptism, Church/Ecclesia, Martyr/Martyrdom, Bishop/Episcopus). This is a one-word, one-location fix (change "four" to "five"), does not touch any classification, and does not require re-verifying anything else in the document — but it is a genuine, newly-introduced defect, in the same family of numeric-precision slip this specific document has now produced in all three review rounds (G3's inflated text count in Round 1, G3's leftover "four/three" figures in Round 2, and now this).

**Counts:** 0 High-severity, 1 Medium-severity, 0 Low-severity findings.

---

## Verification of the five claimed fixes

### 1. H1 (Round 2) — §3.3's "four texts"/"three Primaries" correction — VERIFIED CLEAN

§3.3's Confidence/Gravity Cross-Check bullet (line 81) now reads "three separate Donatist-voiced or -authored texts" and "of the four Primary gravities in this document." I independently diffed commit `0420a514` against its parent and confirmed this is exactly, and only, the change made to that sentence — both numbers flipped, nothing else touched.

I then swept the entire document for every other instance of this figure to confirm no new mismatch was created:
- Line 31 (§1 candidate table): "three distinct Donatist-authored/voiced texts" — consistent.
- Line 75 (§3.3 Repetition test): "three distinct Donatist-voiced or Donatist-authored texts" — consistent.
- Line 136: "Primary (4)" — consistent.
- Line 149 (§4 index table): "the strongest evidentiary base of the four Primaries," "three distinct Donatist-voiced texts" — consistent.
- Line 169 (§5 Cross-Voice): "passes most cleanly of all four Primaries," "three distinct texts plus epigraphy" — consistent.
- Line 222 (closing line): "4 Primary" — consistent.
- `Gravity_Index.xlsx` Candidates sheet, G3 row (AG-Risk column): "three distinct Donatist-voiced/authored texts... strongest evidentiary base of the four Primaries" — consistent (this sheet was never wrong; the fix only had to touch the .md).

No other "four texts"/"three Primaries" instance exists anywhere in the document. Genuinely and completely fixed.

### 2. M1 (Round 2) — Interaction Matrix cells G3×T1 and D-A×T1 — VERIFIED CLEAN

I did not trust the .md's own claim about the workbook; I opened `Gravity_Index.xlsx` directly with openpyxl and read the Interaction Matrix sheet's full grid. Current state:

```
G3  row: G1=R G2=– G3=— G4=R G5=R D-A=– T1=–  T2=–
D-A row: G1=– G2=– G3=– G4=– G5=R D-A=— T1=–  T2=R
```

Both G3×T1 and D-A×T1 are now `–` ("no demonstrated relationship"), and the matrix remains symmetric (T1×G3 and T1×D-A are also `–`). I confirmed by extracting the pre-Round-2-fix version of the workbook (`git show 6110a3bb:...Gravity_Index.xlsx`) that these were the *only* two cells changed by the fix — every other cell is byte-identical in relationship-type terms.

I then re-ran the "no isolated row" check the document claims to satisfy (§6 line 183, and the workbook's own legend note): T1's row now has exactly one non-empty cell (G5×T1 = R) — still a demonstrated relationship, so T1's row is not empty. D-A's row still has G5 (R) and T2 (R). No row in the 8×8 matrix is entirely `–`. The fix did not create a new isolated-row problem.

I also independently re-confirmed (matching Round 2's own finding) that neither §3.3 (G3's Interaction test), §3.5 (D-A's Interaction test), nor §6's prose anywhere argues a G3↔T1 or D-A↔T1 relationship — the correction to "–" is the right fix (removing the unargued cells) rather than needing new prose. Genuinely and cleanly fixed, no side effects.

### 3. M2 (Round 2) — T1/T2 Forces-connection bullets in §3.6 — VERIFIED CLEAN, content checked directly against Doc_01 §5

Both bullets are present (lines 113–114). I read Doc_01 §5's own six-cell sketch table directly (not the prior rounds' paraphrase of it) to check the new content against it line-for-line:

- **T2's claim** — "Cell 2B ... the Maximianist fracture (393–398), internal to G4's own conciliar machinery (the Bagai and Cebarsussi sentences), not one imposed by any external force" — matches Doc_01 §5's Cell 2B text almost verbatim: "...the internal Maximianist fracture — the fracture opens at Cebarsussi in 393 and the suppression campaign proper runs 394–398 ... alongside his quotation of the Cebarsussi and Bagai sentences." Directly and precisely grounded.
- **T1's claim** — "Spans Cells 1B through 2B... the 361 Julian petition and the 390s Maximianist-era invocation... belong to... Cells 2A (external, oscillating imperial policy) and 2B (internal, the Maximianist fracture)." Doc_01 §5's Cell 2A text names "Julian's 361 toleration" explicitly, and Cell 2B's text explicitly includes "the mainstream party's own use of imperial/proconsular legal machinery against it [the Maximianists]" — i.e., the 390s invocation. Both instances are correctly and specifically traceable to Doc_01 §5's own cell content, not invented. The claim that the 313 Anulinus *relatio* "falls at the same founding-dispute moment as Cell 1B's own rigorist rupture" is explicitly and correctly flagged in the same sentence as a temporal-proximity argument, not a claim that Cell 1B's own text names the *relatio* (it doesn't — Cell 1B's own content is the rigorist reading of Cyprian and the 311/312 rupture) — the document is honest about this being its own synthesis, exactly as Round 2 required ("briefly arguing it... rather than only asserting it").

I also confirmed the `Gravity_Index.xlsx` Candidates sheet's own pre-existing Forces-Connection values for T1 ("...spanning Cells 1B through 2B") and T2 ("Cell 2B — the Maximianist fracture...") match the new .md prose closely — the fix correctly ported the workbook's own data into argued prose rather than inventing new content. Genuinely and correctly fixed.

*(One pre-existing, out-of-scope observation, not attributable to this fix: §7's own Doc_08 forces-map summary line lists T1 only under "2B... T1, T2 all operate here," not also under 1B, despite §3.6 now stating T1 spans 1B through 2B. I confirmed via the commit diff that this §7 line was not touched by the Round 2 fix pass — it already read this way before M2 was applied — so it is not a new inconsistency the fix introduced, and per the task's scope is not re-litigated here as a finding.)*

### 4. M3 (Round 2) — §7's G5 lexicon-forwarding clause — MOSTLY CLEAN, but contains a new numeric error

§7's "To Doc_06 (Full Lexicon)" item now ends: "...G5's own Primary classification here, reached after Doc_03 §1 provisionally placed Refusal of Imperial Legitimacy at Tier 2, supports reconsidering that term for full Tier-1 treatment as well, alongside the other four terms just named."

I checked every factual component of this clause directly against `Doc_03_Lexicon_Candidate_List.md`, not against either round's account of it:
- **"Refusal of Imperial Legitimacy" is at Tier 2** — confirmed directly: `Doc_03_Lexicon_Candidate_List.md` line 77, Cluster 5's table, lists it with Tier column value `2`. Accurate.
- **"Doc_03 §1"** — confirmed accurate: that table is inside `## 1. Candidate Roster` (line 31), which is genuinely §1, not §5 (§5 is a different table — "Candidates Flagged for Full Tier-1 Treatment," lines 110–112 — which does *not* list Refusal of Imperial Legitimacy at all among its six preliminary Tier-1 candidates: Traditor/Traditio, Rebaptism, Church/Ecclesia, Martyr/Martyrdom, Bishop/Episcopus, and Agonistici). The document correctly cites §1 (where the Tier-2 assignment actually lives), not §5 (which is silent on this term) — a genuinely careful, correct citation, not a copy-paste of the neighboring "Doc_03 §5" citation already used earlier in the same sentence for the other five terms.

**But the count at the end of the clause is wrong.** "The other four terms just named" refers back to the list earlier in the same sentence: "Traditor/Traditio, Rebaptism, Church/Ecclesia, Martyr/Martyrdom, and Bishop/Episcopus" — that is **five** terms, not four (Agonistici/Circumcellion is named separately, in its own scope-qualification clause, not as part of this corroboration list, so it cannot be the missing fifth that would make "four" work either way you count it). I verified this by direct enumeration of the comma-separated list and by cross-checking against Doc_03 §5's own six-item preliminary list (the five terms named here are exactly Doc_03 §5's six minus Agonistici, which Doc_04 treats separately) — five terms, not four, under any reading.

**Why this matters:** This is a new, self-contained arithmetic error, not present before the Round 2 fix (the pre-fix sentence ended at "...character claims)." with no term-count claim at all — I confirmed this via the commit diff). It is exactly the same *species* of defect this document has now produced in all three review rounds — a small, precise, checkable count, stated wrong, next to the correct data it should have been counted from. It carries no classification risk and is trivially fixable, but it should not go out uncorrected a third time in the same document.

**Fix:** change "the other four terms just named" to "the other five terms just named" (or drop the number and say "the other terms just named") in §7's Doc_06 item.

### 5. L1 (Round 2) — §3.6/§3.7 heading levels — VERIFIED CLEAN

Confirmed directly: `### 3.6 The Two Tensional Gravities` (line 109) and `### 3.7 G5 — Refusal of Imperial/State Religious Legitimacy → **PRIMARY**` (line 118) are both level-3 headings, matching siblings §3.1–§3.5 (all `###`). Verified via `grep -n "^#"` across the whole file — the heading ladder is now `##` (top-level: 0–8) → `###` (3.1–3.7) with no stray level-2 subsection anywhere inside §3. Genuinely fixed, no side effects (heading level was never load-bearing for any cross-reference, as Round 2 itself noted, and remains so).

---

## Additional checks per the task brief

**Clean-documents re-grep.** Grepped the full document body (case-insensitive) for `round 1`, `round 2`, `round 3`, `previously`, `as an ai`, `this revision`, `review found`, `has been fixed/corrected/revised`, `per the review`, `reviewer noted` — zero matches. No process-commentary leakage anywhere in the body.

**Overall arithmetic sanity check.**
- §1's candidate-generation table lists exactly 10 candidates: G1, G2, G3, G4, G5, D-A, D-B, D-C, T1, T2.
- §4's Classification Summary tally: Primary (4) + Supporting (2) + Tensional (2) + Not advanced (2) = 10. Matches.
- §4's "Required index table" independently lists the same 10 candidates as rows. Matches.
- The companion workbook's "By Classification" sheet's own count block (Primary 4 / Supporting 2 / Tensional 2 / Not advanced 2 = 10) matches both the .md and its own row listing above the count block.
- Closing line (line 222): "4 Primary, 2 Supporting, 2 Tensional, 2 not advanced" — matches.

**Cross-reference resolution.** Extracted every `§3.\d` occurrence in the document (18 total, at lines 34, 37, 38, 57, 58, 59, 71, 113, 114, 128, 167, 168, 170, 171, 172, 177, 210, 218) and confirmed every one resolves to a section that actually exists (§3.1 through §3.7 all present as real `###` subsections). No dangling reference.

---

## What verified clean (beyond the five targeted fixes)

- **The companion workbook's other two sheets** ("By Classification," "By Cross-Check Flag") were read directly and match the .md's own Classification Summary and named divergences (G1, G5, D-A) exactly — no drift introduced by the Round 2 fix, which touched only the Interaction Matrix sheet.
- **The Interaction Matrix's byte-level diff** against the pre-Round-2-fix workbook confirms the fix changed exactly the two cells it claimed to change (G3×T1, D-A×T1, and their symmetric counterparts) and nothing else — no accidental collateral change to any other cell.
- **Doc_01 §5's six-cell sketch** was read in full and independently used to check both new Forces-connection bullets; both check out as accurate, specific readings of that sketch's actual cell content, not invented or misattributed.
- **Doc_03's Tier structure** was read in full (§1's Candidate Roster and §5's Tier-1 preliminary flag list) to check the new G5 lexicon clause; the Tier-2 assignment and the §1 section citation are both accurate — only the trailing count is wrong (see M3 above).

---

## Recommendation

Apply the one-word fix to §7 ("four" → "five," or reword to avoid the count), then this document should be cleared. None of Round 1's or Round 2's own structural findings were disturbed by this fix pass, and four of the five targeted fixes are fully clean on independent re-verification — this is not a re-opening of the document's substance, only a final one-line correction before disposition.

**Not yet CLEARED** — pending that one-word correction. Once applied, no further review pass should be needed on substance; a trivial re-check of that single line would suffice to confirm.

---

*End of review.*
