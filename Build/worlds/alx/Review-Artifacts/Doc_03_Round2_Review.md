# Doc_03 (Lexicon Candidate List) — Round 2 Independent Adversarial Review (Confirmation)

**Simulated review — informational only, not an Article 31 substitute.**

Reviewer: independent adversarial AI subagent (did not author Doc_03 or the index).
Date: 2026-07-17.
Round: 2 (confirmation). Round 1 returned SUBSTANTIAL REVISION REQUIRED (1 substantial + 2 cosmetic).
Artifacts reviewed:
- `Build/worlds/alx/Doc_03_Lexicon_Candidate_List.md` (read in full, incl. the new Revision Log)
- `Build/worlds/alx/Lexicon_Candidate_Index.xlsx` (all 6 sheets inspected via openpyxl)
- `Review-Artifacts/Doc_03_Round1_Review.md` (the review being confirmed)

---

## VERDICT: CLEARED (no further substantial revision called for)

The Round 1 substantial finding is **RESOLVED** in both the `.md` and the `.xlsx`; both cosmetic items are applied acceptably; the index still matches the roster on every load-bearing field with zero drift; and no new defect or regression was introduced. No further revision is called for before Doc_04.

---

## Round 1 substantial finding — RESOLVED

**Finding 1 (Round 1):** §4 #7 (Catechetical School / Didaskaleion) inverted the scholar-to-pole mapping — van den Broek (1995) / van den Hoek (1997) read positionally as attaching to the *formal-institution* pole (the exact inverse of their positions), contradicting the already-cleared Doc_01 §1.2 while claiming to express it.

**Status: RESOLVED.** The mapping is now explicit and correct, and no longer depends on pole ordering.

Corrected text in the **.md** (§4 #7):
> "van den Broek (1995) and van den Hoek (1997) deny a formal institution with teacher-succession before Origen (a more informal teaching milieu), while Scholten (1995) affirms an institution but argues it was the church's advanced *theological* school, not a school for catechumens — the direct lexicon-level expression of Doc_01 §1.2, carrying that document's corrected scholar mapping."

Corrected text in the **.xlsx** (`CT Contest-Type Check` sheet, Didaskaleion row; identical wording in the `Candidates` sheet `CT-Contest-Type` cell):
> "Historical scope — van den Broek (1995) & van den Hoek (1997) deny a formal institution w/ succession before Origen; Scholten (1995) affirms an institution but as an advanced theological (not catechumen) school. Eusebius HIGH AG risk. Matches Doc_01 sec 1.2."

Both now place van den Broek + van den Hoek on the **deny-formal-institution** side and Scholten on the **affirm-a-(theological)-institution** side — consistent with Doc_01 §1.2 and with Doc_02 §3.6 (the *Eusebian orderly-succession* picture is the one modern scholars question).

**Web reconfirmation (this round):** van den Broek holds the idea of "a Christian school with a succession of teachers… is completely false, at least until the second decade of the third century" (denies the succession/formal-institution picture); Scholten holds the Alexandrian institution "does not prepare candidates for baptism but is the theological academy of the church" (affirms an institution, but a theological rather than catechumen school). The corrected mapping matches the scholarship exactly. The fix also propagated into the "Matches Doc_01 sec 1.2" self-attestation, which is now accurate rather than contradicted.

---

## Cosmetic items — applied acceptably

1. **§4 #1 Apokatastasis / 553 locus (Round 1 Finding 2).** The .md now states: "condemned in the sixth-century anti-Origenist controversy (the anathemas of 543/553 — whose precise conciliar status, i.e. Justinian's 543 synod versus the official acts of the Second Council of Constantinople in 553, is itself debated in the scholarship)." The .xlsx `Apokatastasis` CT-Contest-Type cell matches: "condemned in the 6th-c. anti-Origenist controversy (anathemas of 543/553, precise conciliar status debated)." The conciliar-status caveat is present in both. **Applied.**

2. **.xlsx `Author-Gravity-Risk` qualifiers (Round 1 Finding 3).** The column now carries the qualifiers the .md tables carry, confirmed by cell inspection: `Eusebius (HIGH)` on Presbyter, Deacon, Succession, and Catechetical School/Didaskaleion; `Athanasius (post-325)` on Incarnation; `Origen (sole systematic)` on Apokatastasis. **Applied.**

---

## Index integrity re-check (programmatic) — no drift, no regression

A fresh row-by-row comparison of the `Candidates` sheet against the .md roster:
- **Roster:** 130 data rows in both; identical term set (0 terms only-in-md, 0 only-in-xlsx).
- **Tiers:** 44 Tier-1 / 86 Tier-2 in both; zero tier mismatches across all 130 terms.
- **Tags (AS/SC/DR/TC/RT/PV/CT):** zero tag-set mismatches across all 130 terms.
- **CB flag:** 12 in both; zero mismatches.
- **CT set:** identical 7 in both (Nous, Logikos/Rational Nature, Fall/Descent, Restoration [deferred], Apokatastasis, Homoousios/Consubstantial, Catechetical School/Didaskaleion); the `CT Contest-Type Check` sheet lists all 7 with a specified contest-type and matches §4.
- **Total load-bearing field mismatches: 0.**

**"Theon"/Representative leak:** none in the roster. The only occurrences of "Theon" in the .md are two meta-references in the Revision Log and build-discipline note documenting that Representative-specific "Theon" content was *excluded* ("All Representative-specific (\"Theon\") content in that source has been excluded"; "…tested clean, with no 'Theon' leak"). These are exclusion attestations, not leaked content. Spot-check of the one-line meanings surfaces no Representative-level or forward-projected specificity.

---

## New findings

**None.** No new substantial finding; no new cosmetic finding; no regression introduced by the Round 1 → Round 2 pass.

- **New SUBSTANTIAL:** 0
- **New COSMETIC:** 0
- **Total new findings: 0**

---

*Simulated review — informational only, not an Article 31 substitute (Constitution Article 31).*
