# Doc_03 (Lexicon Candidate List) — Round 1 Independent Adversarial Review

**Simulated review — informational only, not an Article 31 substitute.**

Reviewer: independent adversarial AI subagent (did not author Doc_03 or the index).
Date: 2026-07-17.
Artifacts reviewed:
- `Build/worlds/alx/Doc_03_Lexicon_Candidate_List.md` (read in full)
- `Build/worlds/alx/Lexicon_Candidate_Index.xlsx` (all 6 sheets inspected via openpyxl)
Context read: Doc_01, Doc_02 (relevant sections), Open_Gaps_Tracking.md, Framework V7.3 Step 3, Constitution Art. 3/17/26.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

One substantial finding (Finding 1 — a citation/sourcing-attribution inversion in §4 that contradicts the already-cleared Doc_01 §1.2). Everything else — Step-3 completeness, the roster↔index match, the [CT] discipline, the counts, the Author-Gravity screens, Article 3 hygiene — is clean. The substantial item is narrow and localized to one parenthetical; it is not a structural failure of the document.

---

## Index drift check (stated explicitly, as required)

**The .xlsx index MATCHES the .md roster on every load-bearing field.** A programmatic row-by-row comparison of all 130 candidates found:
- **Terms:** identical set, 130 = 130, no term in one and not the other.
- **Preliminary tiers:** zero mismatches (44 Tier-1 / 86 Tier-2 in both; `By Tier` sheet agrees).
- **Tags (AS/SC/DR/TC/RT/PV/CT + CB flag):** zero mismatches across all 130 rows.
- **CT set:** identical 7 in both (Candidates sheet `CT=Y`, `By Tag` CT list, and `CT Contest-Type Check` sheet all agree with §4).
- **CB set:** identical 12 in both (Candidates sheet, `By Tag` CB list, `Cross-Build` sheet, and §3 all agree).
- **CT-contest text:** present for all 7 CT rows; no non-CT row carries contest text.

The only differences found were representational, not substantive: (a) the md AG column uses an em-dash "—" where the xlsx leaves the cell blank (equivalent — "no single dominant voice"); (b) the xlsx AG column drops the parenthetical risk-qualifiers the md carries (see Finding 3, cosmetic). **No tier, tag, CT, or CB drift exists.**

---

## Findings

### Finding 1 — [SUBSTANTIAL] §4 item 7 (Didaskaleion) inverts the scholar-to-position mapping and contradicts the already-cleared Doc_01 §1.2

**Location:** Doc_03 §4, contest #7 (Catechetical School / Didaskaleion). (The xlsx `CT-Contest-Type` cell for this term is fine — it carries no scholar attribution.)

**Text as written:** "Whether it was a formal institution with a continuous succession *or* a looser teaching tradition retrospectively formalized by Eusebius is genuinely contested (**van den Broek 1995, van den Hoek 1997 vs. Scholten 1995**) — the direct lexicon-level expression of Doc_01 §1.2."

**What's wrong:** The clause states two poles ("formal institution…" first, "looser…" second), then lists "(van den Broek, van den Hoek vs. Scholten)." On the natural positional reading, van den Broek + van den Hoek attach to the *first* pole — "formal institution with a continuous succession." **That is the exact opposite of their actual positions**, and it contradicts Doc_01 §1.2, which this line claims to be "the direct lexicon-level expression" of.

Per Doc_01 §1.2 (cleared) and web verification:
- **van den Broek (1995)** calls "the whole idea of a Christian school with a succession of teachers… completely false, at least until the second decade of the third century" — i.e., he *denies* the formal-institution-with-succession picture (the "looser" pole).
- **van den Hoek (1997)** quotes that judgment approvingly and reconstructs an *informal* pre-Origen teaching milieu — same side as van den Broek.
- **Scholten (1995)** is the one who holds there *was* an institution — "not a facility for preparing baptismal candidates, but the theological university of the church" (confirmed via the JbAC 38 summary) — while rejecting the "catechetical" label.

So the real disagreement is: {van den Broek, van den Hoek} = *no* formal institution/succession (Eusebian picture retrojected) **vs.** {Scholten} = there *was* an institution (but a theological school, not a catechumen school). The "vs." grouping is correct, but Doc_03's **pole ordering makes the two most-recently-corrected scholars land on the wrong pole.** Doc_02 §3.6 reinforces this: it is precisely the *Eusebian orderly-succession* picture that "has been questioned by modern scholars," i.e. the pole vdB/vdH reject.

**Why this is substantial (not cosmetic):** it is an Article 28 citation-integrity matter — it misrepresents which scholar holds which position and, read naturally, flatly contradicts an already-cleared upstream document while claiming to express it. This is the *same class* of defect Doc_01's own Round 1 caught ("an inverted representation of Scholten"; a van den Hoek/van den Broek misattribution). The CT tag and the "historical scope" contest-type are correct; only the scholar-pole attribution is defective.

**Concrete fix:** Reword to make the mapping explicit and match Doc_01 §1.2's three-way structure, e.g.: "van den Broek (1995) and van den Hoek (1997) reject the formal-institution-with-teacher-succession picture as a Eusebian retrojection (a looser, informal pre-Origen teaching milieu); Scholten (1995) holds there *was* an institution but that it was the church's advanced theological school, not a catechumen ('catechetical') school." Do not present it as a clean two-camp split on the "institution: yes/no" axis with the poles ordered so vdB/vdH read as institution-defenders.

---

### Finding 2 — [COSMETIC] The 553-condemnation locus is stated more flatly than the sibling documents' temporal/scholarly precision warrants

**Location:** §3 one-liner for Apokatastasis ("contested and condemned (553)"); §4 item 1 ("propositions associated with it were condemned at the Second Council of Constantinople (553)"); §4 item 3 (Nous, "the same position condemned in 553"); xlsx `CT-Contest-Type` cells for Apokatastasis ("condemned 553") and Nous ("condemned in 553").

**What's wrong / evidence:** Modern scholarship (Richard Price and others) holds that the fifteen anti-Origenist anathemas are **not** part of the official acts of the ecumenical Second Council of Constantinople (553) — they do not appear in that council's official minutes; the substantive anti-Origenist condemnations are more securely attributed to the 543 Home Synod under Justinian (and Justinian's 543/544 edict), with the 553 council's formal role over Origenism itself contested. The doc's §4 item 1 hedges reasonably ("propositions associated with it were condemned"), but the "(553)" locus, and the flatter §3/xlsx phrasings, assert the traditional attribution without the qualification the term's own contest-type ("meaning + present-tradition relationship") invites.

**Why cosmetic (not substantial):** the core claim — that propositions associated with Origen's apokatastasis were condemned in the mid-6th-century anti-Origenist campaign — is true, and "553" is the standard shorthand; nothing about the CT tag, tier, or the term's inclusion changes. But for a build whose Doc_01/Doc_02 were praised for temporal precision, tightening this is warranted.

**Concrete fix:** Add a half-clause where the locus is first stated, e.g. "…condemned in the anti-Origenist anathemas of the 543 synod under Justinian, traditionally associated with (though not clearly part of the official acts of) the Second Council of Constantinople, 553." Mirror it in the two xlsx cells.

**Sources:** https://en.wikipedia.org/wiki/Synod_of_Constantinople_(543) ; https://afkimel.wordpress.com/2026/01/05/apokatastasis-origen-and-the-fifth-ecumenical-council-part-1/ ; https://rethinkinghell.com/2015/08/11/conditional-immortality-origen-and-the-second-council-of-constantinople/

---

### Finding 3 — [COSMETIC] The xlsx AG column drops the risk-level qualifiers the md carries

**Location:** `Candidates` sheet, `Author-Gravity-Risk (dominant)` column, rows for Presbyter, Deacon, Succession, Catechetical School/Didaskaleion (md "Eusebius (HIGH)" → xlsx "Eusebius"); Incarnation (md "Athanasius (post-325)" → "Athanasius"); Apokatastasis (md "Origen (sole systematic)" → "Origen").

**What's wrong:** The queryable index loses the "HIGH" / "post-325" / "sole systematic" qualifiers that carry the actual screening weight. A reviewer filtering the index for HIGH-risk institutional terms cannot recover them from the AG column alone.

**Why cosmetic:** the information is preserved elsewhere — §2, the README, and (for the CT terms) the `CT-Contest-Type` cells all carry the HIGH/SYSTEMIC/post-325 qualifiers; the Eusebius-HIGH screen is unambiguous in the roster prose. No screen is lost, only its index-column redundancy.

**Concrete fix:** Add a risk-level to the AG column (e.g. "Eusebius (HIGH)") or a separate `AG-Risk-Level` column so the index is filterable on it.

---

## Checks that PASSED (no defect)

1. **Step 3 completeness (Framework Step 3).** Delivers recurring terms, preliminary definitions, initial tier *estimates*, tags, and Author-Gravity risk flags. Correctly framed as a *candidate* list, not the full lexicon (§0). Correctly assigns **no** permanent `alexlex` numbers (§0.1 states numbering is Doc_06). Tiers correctly framed as preliminary/pending Doc_04 (§0.2, §5, README). Strand attribution correctly stated **N/A (strand-singular)** with the desert question surfaced as the CB flag (§0.3) — matches Doc_01.
2. **Index discipline.** Queryable master `.xlsx` present; each tag (AS/SC/DR/TC/RT/PV/CT) is its own filterable Y/N column, CB its own column; dedicated `CT Contest-Type Check` and `Cross-Build` sheets; README documents candidate-stage scope. Counts confirmed against the actual sheet: **130 candidates** (130 data rows), **7 CT**, **12 CB**, 44/86 tiers. All match the .md. Every CT row has its contest specified; no CT term lacks a contest (the most common lexicon gap — absent here).
3. **[CT] discipline (Article 26).** All 7 CT candidates (Nous, Logikos, Fall/Descent, Restoration[deferred], Apokatastasis, Homoousios, Catechetical School/Didaskaleion) carry the CT tag in **both** the .md and the .xlsx and have a contest statement in both. The draft's claim to have corrected the Alexandria-v7 defect (6 contested / 1 tagged) is borne out: 7 assessed, 7 tagged. Contest descriptions are accurate except the §4 #7 scholar-pole issue (Finding 1); the Apokatastasis/553 and didaskaleion contests are otherwise substantively right.
4. **Cross-consistency with Doc_01 & Doc_02.** Didaskaleion CT ↔ Doc_01 §1.2 Contested finding (see Finding 1 for the one attribution flaw); Eusebius HIGH on Presbyter/Deacon/Succession/Didaskaleion ↔ Doc_02 §3.6 (exact match, including the "institutional/succession/biographical" scoping); Origen SYSTEMIC ↔ Doc_02 §3.1; CB cluster ↔ Doc_01 §3.3 held-open desert-attribution (all 12 CB notes cite Doc_01 §3.3 + Art. 3); Homoousios located post-325 (Nicaea 325) ↔ Doc_01/Doc_02 temporal precision. No contradiction except Finding 1.
5. **Constitutional compliance.** Article 3 — spot-check of all 130 one-line meanings found **no** "Theon"/Representative content or forward-projected specificity; definitions read as world-level (OG-2 satisfied). Article 26 — handled (above). Article 17 — tier/flag framing is explicitly preliminary/confidence-appropriate.
6. **Internal accuracy.** AS and SC form a clean partition (49 + 81 = 130, zero terms tagged both, zero tagged neither) — no AS/SC mis-tag. Cluster counts sum to 130 (20+16+10+8+18+21+19+18). PV (5) restricted to genuinely plural-voice terms (Logos, Scripture, Theosis, Soul, Nous). The Evagrian eight-*logismoi* attribution (Demons) is historically correct and correctly CB-flagged. No one-line meaning found to be historically wrong or an overclaim. The roster is comprehensive against Doc_02's 12 streams; no obvious required term is missing (a positively-valued "true gnosis" boundary term is arguably latent, but "Knowledge/Gnosis" + "Heresy" cover the space — not a defect).

---

## Summary count

- **SUBSTANTIAL:** 1 (Finding 1 — §4 #7 Didaskaleion scholar-pole inversion vs. Doc_01 §1.2 / Article 28).
- **COSMETIC:** 2 (Finding 2 — 553-condemnation locus precision; Finding 3 — xlsx AG column drops risk qualifiers).
- **Index drift:** none on any load-bearing field (terms, tiers, tags, CT, CB, CT-contest all match). Only em-dash-vs-blank equivalence and the Finding-3 qualifier drop.

**Disposition recommendation:** revise Finding 1 before proceeding to Doc_04; Findings 2–3 can be folded into the same pass. All are localized; no re-architecture of the roster or index is needed.

*Simulated review — informational only, not an Article 31 substitute (Constitution Article 31).*
