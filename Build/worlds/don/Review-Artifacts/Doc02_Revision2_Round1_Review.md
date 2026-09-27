# Doc_02 Revision (2026-09-07, G3/Gesta/Gregory/Monceaux integration) — Round 1 Review

**Reviewer:** independent, cold adversarial subagent — no drafting context, instructed to independently re-derive every claim against the primary vendored sources rather than diff-check the document's own citations.

**Scope:** the 2026-09-07 revision to `Build/worlds/don/Doc_02_Source_Ecology.md`, integrating four newly-vendored sources found this session: the Mommsen & Meyer *Codex Theodosianus* XVI critical edition (Registry row 51), the *Gesta Collationis Carthaginiensis* (Registry row 55), a 1907 selection of Gregory the Great's letters (Registry row 54), and two further Monceaux volumes with partial content read (Registry rows 52–53).

---

## Verdict: SUBSTANTIAL REVISION REQUIRED, narrow

One confirmed High finding — a fabricated/misattributed quotation, the exact recurring failure mode this world's own `don_Decision_Log.md` has tracked repeatedly across Step0, Doc_01, Doc_02, Doc_04, Doc_05, and Doc_09. Everything else checked — the Theodosianus fine schedule, all ten cited Gesta act numbers and the act-50 and act-268-270 quotations, all four Gregory letters (numbers, correspondents, dates, content), the Monceaux Tome VI Emeritus/Primianus material, the arithmetic, and the Source_Registry.md row citations (51–55) — verified accurate against the primary vendored files themselves, independently re-derived rather than diff-checked against the document's own citations.

## High

**1. Fabricated quotation attributed to Source_Registry.md row 55, which does not contain it.**

- **Where:** `Build/worlds/don/Doc_02_Source_Ecology.md`, §1, line 22: *"This world's own recurring OCR-quality caution applies with unusual force here — row 55's own Verification Note flags this specific scan as 'notably poor... more so than most other files in this corpus' — so the act 50 rendering above should be treated as a careful reading of a difficult scan, not a settled critical-edition text, until visually cross-checked."*
- **What's wrong:** The phrase "notably poor... more so than most other files in this corpus" appears nowhere in `Source_Registry.md`. Row 55's actual OCR-relevant content is: *"Confidence held at B, not A, because most of this volume has NOT been read this session"* and *"the precise column boundary separating the Gesta's own acts from Balduin's own following 'Historia Collationis' was not established (this scan's OCR'd column markers are not reliably sequential enough for confident automated boundary-finding in the time available)"* — a caveat about incomplete reading and column-boundary uncertainty, not a comparative OCR-quality judgment, and certainly not the quoted words.
- **What the source actually says instead:** The matching phrase ("notably poor even by this corpus's own standards for 19th-century Migne scans") actually lives in `cic/texts/REGISTRY.yaml`'s own entry for this same vendored file, not in `Source_Registry.md`. The revision misattributed a caveat the build thread itself wrote in one registry to the wrong registry, presenting it in quotation marks as if sourced to the World-Build's own Source Registry specifically.
- **Fix:** Either cite `cic/texts/REGISTRY.yaml` correctly for this caveat, or write one actually grounded in what `Source_Registry.md` row 55 itself says.

## Medium

**2. The Gesta "recognition formula" is presented as one uniform quoted phrase; the primary text shows it isn't.**

- **Where:** `Doc_02_Source_Ecology.md` §1, line 22: *"...each closed by his own recognition formula ('*Emeritus episcopus recognovi*' — 'I, Emeritus the bishop, have reviewed [this record]')."* — describing all ten cited acts (20, 24, 26, 50, 99, 108, 121, 253, 266, 268).
- **What's wrong:** Direct inspection of `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` shows the closing formula is not uniform. At minimum acts **50, 253, and 266** — three of the ten specifically cited — close not with the bare phrase but with the legally qualified **"Emeritus episcopus salva appellatione recognovi"** ("...having reserved [my right of] appeal, I have reviewed [this record]"):
  - Line 126853: "Emeritus episcopus salva oppellatione recognovi." (act 50)
  - Line 129619–129620 / 129627: "Emeritus episcopus salva appellatione recognovi." (act 253, twice)
  - Line 130309–130310: "Emeritus episcopus salva appellatione recognovi." (act 266)
  Only acts 26, 108, 121, and 268 confirmably close with the bare phrase the document quotes.
- **Why it matters:** "Salva appellatione" ("with appeal reserved") is a substantive procedural qualifier — Emeritus is not unconditionally accepting the recorded proceedings but explicitly preserving his right to contest them. Presenting one fixed Latin phrase in quotation marks as "his own recognition formula" for all ten acts erases a genuine and recurring variation in the primary text, in a paragraph whose own argument (§6: the Gesta as a "differently-mediated evidentiary channel," closer to a court transcript than to Augustine's polemic) would actually be reinforced, not weakened, by disclosing that Emeritus was routinely signing under protest.
- **Fix:** Either drop the quotation marks and describe the formula descriptively, or quote the "salva appellatione" variant as the more representative closing form given it appears in a meaningful fraction of the acts checked.

## Low

None risen to a level worth reporting — the acts-list count, the Theodosianus fine-schedule structure (nine gold-denominated ranks vs. Circumcellions alone in silver), the Monceaux Emeritus/Primianus chapter attributions and quotations, all four Gregory letter numbers/correspondents/dates, the *agonistici*-absence checks in both the Theodosianus and Petschenig files, and the 153–155-year arithmetic all checked out exactly as stated.

## Verified accurate (for the record)

- **Theodosianus 16.5.52** (`theodosianus-16_mommsen-meyer1905.txt`): confirmed verbatim — nine ranks (illustres 50, spectabiles 40, senatores 30, clarissimi 20, sacerdotales 30, principales 20, decuriones 5, negotiatores 5, plebei 5) all "auri pondo," then "circumcelliones argenti pondo decem" — exactly as the document states.
- **Gesta act numbers for Emeritus** (`pl11-zeno...migne.txt`): all ten cited acts (20, 24, 26, 50, 99, 108, 121, 253, 266, 268) directly located and confirmed opening "N. Emeritus episcopus dixit"; "Emeritus" occurs 28 times file-wide, matching the decision log's own count.
- **Act 50 quotation and paraphrase**: "Magno [ar]gnmento vc-rilas occullaiur" (OCR) = "Magno argumento veritas occultatur," in a passage genuinely about the opposing side declining to disclose its legates' "nomina... ordinem... mandatum" — matches the document's summary and translation exactly.
- **Acts 268–270 quote**: verbatim match.
- **Gregory letters**: Ewald II.46, IV.32, IV.35, Hartmann V.3 — all confirmed present with matching content and dates.
- **Monceaux Tome VI**: the Emeritus/Petilian "principal champion" quote and all biographical details confirmed verbatim; Chapter III genuinely Primianus, Chapter IV genuinely Emeritus.
- **Source_Registry.md rows 51–55**: all five row numbers and their content match Doc_02's citations exactly.
- **Arithmetic**: 592–439 = 153; 594–439 = 155.
