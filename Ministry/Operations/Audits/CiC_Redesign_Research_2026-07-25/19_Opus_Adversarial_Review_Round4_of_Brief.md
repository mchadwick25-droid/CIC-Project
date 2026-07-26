# Adversarial review (round 4, hoped final): `CiC_System_Redesign_Fable_Brief_2026-07-25.md`

*Opus review, dispatched 2026-07-26 — the fourth adversarial pass, explicitly hoped to be the last before the brief is sent. Scoped to re-derive all 31 of round 3's findings against their sources (checking whether the rapid fix pass introduced new errors while correcting old ones — round 2 caught exactly this happening once already) and to adversarially check the brand-new §10 deliverable 10. Read `18_Opus_Adversarial_Review_Round3_of_Brief.md` and `Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md` first for calibration and method.*

## Bottom line

**Not ready to send.** Three P0s. Two are exactly the failure this round was dispatched to hunt — new errors introduced while fixing old ones. The third is a delivery defect that would make everything else moot.

The most consequential: **every fix from all three prior review rounds, research docs 12–18, and deliverable 10 exist only on local `main`, which is 21 commits ahead of `origin/main`.** The brief on GitHub is still the pre-round-1 draft. Round 3's P0 #5 was closed as "Mark confirmed repo access," but committed ≠ pushed.

The rest of the round-3 fix pass largely landed correctly — 27 of 31 findings re-verified clean against their sources. Deliverable 10 is genuinely additive and all four of its cited numbers check out.

---

## P0 — fix before sending

**1. The redesigned brief and 7 of the 18 research documents are not on the remote. Repo-access delivery would hand Fable the pre-round-1 draft.**

`git status -sb` → `## main...origin/main [ahead 21]`. What `origin/main` (commit `d1b9b4c`, 2026-07-25 22:13) actually contains, verified by `git show`:

- The brief at 3,216 words, not the current ~9,700. Nine sections, not ten — no §3 governing-documents section (round 1's P0), "seven jobs" not eight, "Phase 1" ×5 and "Pass 1" ×0 (the naming collision round 1 flagged).
- The confirmed-gloss mechanism misattribution — one of round 1's two fabrications — still present.
- Research docs 12, 13, 14, 15, 16, 17, 18 absent entirely. Only 00–11 are pushed.
- The new `Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md` absent.

**Fix: `git push origin main`** before sending — or, if delivery is the local working tree rather than a clone, say so explicitly, since §10 deliverable 8 already depends on that distinction.

**2. §4's rewritten certainty-distortion clause assigned two roles of one adjudicator to two different adjudicators — verified against the running code, not just doc 13.**

`cic-poc/backend/app/prompts/facilitator_prompts.py` L215 (FABRICATION): fails toward *finding* when uncertain. L293 (OVER_SETTLING): fails toward *clearing*, "deliberately opposite" to FABRICATION. The over-settling mechanism is **both** the thing that catches certainty inflation **and** the thing with the clearing bias. The fabrication adjudicator has neither. Doc 13's "CiC is defending both directions" is an argument about the over-settling mechanism's own two-part design, not about the adjudicator *pair*. **Fixed 2026-07-26** — §4 now names FABRICATION and OVER_SETTLING explicitly, with the clearing bias and the inflation-catching both attributed to OVER_SETTLING alone, and the fabrication adjudicator's bias named as a separate axis.

**3. The required-reading count was stale, and doc 18 — an adversarial review headed "Not ready to send" about this brief — was sitting in the corpus unflagged.** The same defect round 2 caught and fixed for doc 11. **Fixed 2026-07-26** — preamble now says "eighteen documents," and the doc-11 historical flag now explicitly covers doc 18 too.

---

## P1 — materially improves the result

**4. §8 objective 1's source-discovery half had no deliverable in §10, which calls itself "the actual output contract."** Objective 1 requires a reproducible search record; no deliverable designed one — deliverable 3 is scoped to fan-out-drift document types, deliverable 9 measures discovery coverage, §9's `discovery_channel` records only the outcome of a search, not the search itself. **Fixed 2026-07-26** — deliverable 1 now explicitly includes a search-strategy record.

**5. §9's Louw & Nida rescoping was factually wrong about CiC's own world list.** Checked against the six deployed lexicons directly: three worlds are Greek-vocabulary (PAHC, Desert, Alexandria), Hieronymian-Ascetic-Literary is entirely Latin (the brief's contrast clause silently placed it on the Greek side), and Imperial-Juridical is bilingual, not simply "the Latin-juridical world." Also, Louw & Nida is a New Testament lexicon — offering it as the closest analogue for patristic-Greek worlds cuts against the brief's own preceding sentence, which argues patristic Greek needed a dedicated lexicon precisely because general ones didn't cover it. **Fixed 2026-07-26** — the per-world clause dropped; doc 13's actual, principle-level framing restored (adopt the organizing principle, not this specific lexicon, since no single published instrument covers all six worlds' mixed vocabulary).

**6. §10 deliverable 3's doc-17 warrant asserted a unanimity doc 17's own §2a contradicts in a bolded heading** ("'Build the world before the character' is not an established principle. The opposite is closer to consensus."). Doc 17 is internally inconsistent on this point; the brief inherited only the favorable half, stated more assertively than doc 17 itself does. **Fixed 2026-07-26** — softened to "leans toward... or is silent," with doc 17's own minority-view caveat named explicitly. Also restored: doc 17's REAL GAP that today's per-world gate loop is strictly forward-only despite the methodology's own claim elsewhere that the workflow isn't strictly linear.

**7. Deliverable 10 reopened the fabricated-numbers risk that round 3's P0 #4 had just closed in deliverable 9** — asking for clearing thresholds on metrics deliverable 9 says explicitly have no baseline yet. **Fixed 2026-07-26** — deliverable 10 now names *which* metrics gate a freeze, explicitly deferring threshold values until real baselines exist.

---

## P2 — polish (not yet applied; genuinely optional)

- `discovery_channel` mis-mapped in the §9 field table to Cross-reference/consistency; belongs to Repository/reference.
- §7 and §5c disagree on whether the runtime or the parser drops Quick Meaning (it's the parser, per doc 15 / `indexer.py:117-118`).
- `attribution_status` field values should be `genuine | dubium | spurium | anonymous` (doc 12 line 336) — the brief now has CPG's *description* right but the field's own enum still drops `anonymous`.
- "a tested shape for this" (LoC Observe→Reflect→Question) overstates doc 12, which claims only "a stated design intent," not a tested shape.
- §10 deliverable 5: doc 16 maps CiC's plain endpoint onto EQUAL and the streaming selector onto SS-by-proxy — one baseline each, not "neither baseline cleanly" for both.
- §3's "a second, worse bottleneck" has no antecedent inside its own bullet; the first bottleneck is fourteen lines away in a different list.
- The Lampe hedge could note doc 13 endorses the four-field block outright (line 183: "That fix is correct and this audit does not reopen it") — the hedge is honest but slightly undersells its own support.
- Relative recall is Medium confidence in doc 14; §10 deliverable 9 states it flat.
- Deliverable 10 and deliverable 3's Freeze Criterion (doc 17 rec 1) need one sentence sequencing them so Fable doesn't produce two competing definitions of "frozen."
- "every verification gate in this project's actual history" (§8 objective 1, deliverable 10) — doc 04 says "the pattern across the whole set," not literally every one.
- "zero of nine Desert terms" — doc 15 counts chunks, not terms; same practical meaning, worth matching the source's noun.
- §9's consolidated field table caption says "the fields above" but also includes `eviction_priority`/`cache_stability`, which live in §7.

---

## Structural checks

**Cross-reference integrity: clean.** All 47 `§N` occurrences and all 12 deliverable-number references resolve correctly. Nothing broke when deliverable 10 was added.

**Objective-to-deliverable completeness: complete**, once P1 #4 above is applied. Objective 1 → deliverables 1, 3, 10; 2 → 2; 3 → 1, 2; 4 → 4; 5 → 5; 6 → 7. The double-mapping (objective 1 → three deliverables) has precedent (deliverable 2 already maps to two objectives).

**Balance ratio: 42.5% / 57.5%** (4,108 words preamble+§1–§5 / 5,568 words §6–§10) — the ask outweighs the diagnosis by a wider margin than at any prior round (round 3: 46.5/53.5; round 1: ~68/32).

**Total length and orientation load: up.** Brief ~9,700 words (from 8,306 at round 3). Required reading now 18 documents plus an index, ~856KB, ~112,000 words. Real but supportable — provided P0 #1 is resolved.

---

## Deliverable 10, assessed on the merits

All four cited numbers verified against source (Quick Meaning 0/9 Desert → doc 15 line 65; Author-Gravity 7–100% → doc 03 line 39; World Facilitation Brief 2/6 → doc 17 lines 27, 261; "table" zero times in V7.4 → doc 17's count table). Doc 04's reactive-vs-prospective framing is genuinely supported. It's additive, not a restatement: deliverable 1 defines the schema but not requiredness tiers; deliverable 3 defines gates but not which must pass to freeze; deliverable 9 defines metrics but not thresholds. Deliverable 10 is the only one that sets required-vs-optional and a freeze bar. Needed the threshold caveat (P1 #7, now applied) and the sequencing note against deliverable 3's Freeze Criterion (P2, still open) — not removal.

---

## Prioritized fix list

**Before sending (P0):**
1. **`git push origin main`** — or state explicitly that delivery is the working tree, not a clone. **Open — needs Mark's explicit go-ahead before pushing to the remote.**
2. ~~Rewrite §4's certainty-distortion clause...~~ **Closed 2026-07-26.**
3. ~~Correct the preamble to "eighteen documents"...~~ **Closed 2026-07-26.**

**Materially improves it (P1) — all four closed 2026-07-26:** #4 (search-strategy record added to deliverable 1), #5 (Louw & Nida per-world clause dropped, principle-level framing restored), #6 (doc-17 warrant softened, forward-only gate-loop gap restored), #7 (deliverable 10's threshold values deferred to post-baseline).

**Polish (P2):** the twelve items above — genuinely optional, none blocking.
