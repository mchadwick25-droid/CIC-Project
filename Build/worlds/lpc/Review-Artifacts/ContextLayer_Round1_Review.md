# Independent Adversarial Review — Round 1
## World Context Layer Chunks 001–005 (lpc)

**Documents reviewed:** Build/worlds/lpc/lpcctx001_the-making-of-a-catechumen.md, lpcctx002_the-questions-at-the-water.md, lpcctx003_what-the-water-seals.md, lpcctx004_the-road-walked-in-stages.md, lpcctx005_receiving-one-baptized-outside.md (branch `lpc-world-context-layer-round1`, PR #491)
**Reviewer:** isolated subagent, no prior context on this document set beyond the repository itself.
**Date:** 2026-09-24.

---

## Method

Read the L4 template (`Build/reference/L4-Templates/World_Context_Layer_Chunk_Template.md`) and the one existing precedent (`Build/worlds/cappadocian/cappadocianctx001_the-brotherhoods.md`) first, to establish the governing contract and structural precedent. Read all five new chunks in full. Read both grounding evidence documents in full (`Liturgical_Evidence_Read_Cyprian_2026-09-19.md`, ~234 lines; `Liturgical_Evidence_Read_Augustine_2026-09-19.md`, ~208 lines) and checked every quotation, paraphrase, and phase-attribution claim in the five chunks against them directly. Read the two always-present deployed artifacts (`lpc_World_Capsule_Core.md`, `lpc_Representative_Permanent_Prompt_Datus.txt`) to check redundancy and voice-idiom discipline (grepped for "Cyprian," "Augustine," "this world's," "characterized by," "scholars" — zero hits in any of the five chunks' Primary Content or front matter). Read `Doc_04_Gravity_Discovery.md` in full (all eight candidate gravities, §1–§7) and checked each chunk's Related Gravities claims against Doc_04's actual candidate definitions and quoted test language. Read `lpc_Rep_Phase7_Encounter_Ecology_Mapping.md` §3 and §6.3 (the disclosed open item these chunks are meant to close) and confirmed substance against it. Read the three named Lexicon-Chunks for redundancy checking. Counted Primary Content word counts programmatically and converted to an approximate token estimate.

---

## HIGH findings: 2, both concentrated in lpcctx003 — both independently re-verified by the build thread and applied

**H1 — lpcctx003 claims a quotation "in exactly these words" that is not exact.** Primary Content read: *"you have said what this is for in exactly these words: that they may obtain the Holy Spirit, and be perfected with the Lord's own seal."* The actual source (Cyprian to Jubaianus, Ep. LXXII §9, Finding 1.7 of the Cyprian evidence read) reads: *"obtain the Holy Spirit, and **are** perfected with **the Lord's seal**"* — no "own," "are" not "be." **Independently re-verified** by reading Finding 1.7 directly. **Fix applied:** corrected to the verbatim wording; the "exactly these words" framing kept only because it is now actually exact.

**H2 — lpcctx003 presents as a settled two-part sequence something the source evidence explicitly declines to resolve.** The chunk narrated chrism/anointing and the imposition of hands as two distinct, sequential acts ("you anoint them... **Then** you lay your own hand on them..."). Finding 1.7 states explicitly: *"the same act Finding 1.2's chrism/anointing may be a second name for, or a companion rite to; this document does not resolve which."* **Independently re-verified** against Finding 1.7 directly. **Fix applied:** rewritten to render this genuine uncertainty in voice ("whether the anointing and the laying-on of the hand are one completing act named twice, or two acts that answer one another, is not a distinction you have ever had to settle"), with the Confidence Note now disclosing the source's own non-resolution explicitly.

---

## MEDIUM findings: 5

**M1 — claimed alteration of a Doc_04 quotation in lpcctx001. Independently re-checked and found NOT to hold as stated; no fix applied.** The review compared lpcctx001's quoted fragment ("its own primary activity," attributed to "Doc_04's own dependency finding") against Doc_04 Candidate 1's own write-up ("Candidate 4... is **this office's own** primary activity," line 29). But lpcctx001 explicitly cites the *Dependency* finding under Candidate 4 (catechesis), not Candidate 1 — and that finding, at line 74, reads verbatim: *"Candidate 1 depends on this as **its own primary activity**."* The four-word quoted fragment is an exact match to the sentence lpcctx001 actually cites. The review appears to have checked the quote against a different, similar-but-distinct sentence in a different Candidate's own section. Consistent with this build thread's standing discipline of never dismissing a finding without independent re-verification: re-verification here supports dismissal, so no change was made and the finding is recorded as reviewed-and-not-held rather than silently dropped.

**M2 — lpcctx002 generalized phase-specific, exchange-specific evidence to "both exchanges." Applied.** The false-prophetess imitation evidence (Finding 1.8) is specifically about the *interrogation* being successfully imitated; nothing in the evidence read shows the *renunciation* exchange being imitated. The closing sentence's placement, immediately after discussing both exchanges together, read as if the imitation evidence backed both generically. **Fix applied:** rescoped to the interrogation alone, with a new sentence naming the false-prophetess episode specifically and the Confidence Note now stating the scoping explicitly.

**M3 — lpcctx003's Related Gravities section stretched G6 beyond its actual defined scope. Applied.** G6 in Doc_04 is specifically "Sacramental and Ordination Validity **Across the Boundary of the Church**," generated from the rebaptism/heresy-boundary dispute. lpcctx003's content is entirely about the *ordinary* post-baptismal completion given to someone already validly baptized inside the church — a case Finding 1.7 itself explicitly distinguishes from "the separate, contested case of converts from heresy/schism." **Fix applied:** reweighted to G1 (Pastoral Office) as primary, with G6 named only as a loose, explicitly-scoped adjacency ("this chunk is not the boundary dispute, only the everyday content the boundary dispute presupposes").

**M4 — Related-Chunks reciprocity gaps. Applied.** lpcctx001 listed lpcctx003 but lpcctx003 did not list lpcctx001 back; lpcctx005 listed lpcctx002 but lpcctx002 did not list lpcctx005 back. **Fix applied:** both reciprocal links added.

**M5 — lpcctx004 bundled two lexicon entries the lexicon itself warns not to conflate. Applied.** lpcctx004 is entirely about the confessors'/martyrs' letters of peace (`lpclex019`), not the Decian sacrifice-certificate (`lpclex017`, a different document travelling in the opposite direction). `lpclex017`'s own front matter explicitly warns against exactly this conflation. **Fix applied:** `lpclex017` removed from lpcctx004's Do-Not-Retrieve-When/Related-Chunks list, with the distinction stated explicitly in its place.

---

## COSMETIC findings: 2, not separately actioned

**C1 — lpcctx003 and lpcctx005 sit near the low end of the template's 300–600 token target.** lpcctx003 grew somewhat with the H1/H2 fix pass; lpcctx005 left as drafted, still within range.

**C2 — lpcctx001's lead-in before an unquoted paraphrase reads close to implying a direct quotation.** Noted; not changed, since no quotation marks are used and the sentence does not itself claim exactness.

---

## What checked out cleanly

- Every Capsule-Core-Complement quotation of the World Capsule Core itself (all five chunks) is verbatim-exact against the Core file.
- Phase attribution (Cyprian-phase vs. Augustine-phase, "earlier in your span" vs. "later in your span") is correct in all five chunks against the two evidence documents.
- Voice discipline is clean throughout: zero occurrences of "Cyprian," "Augustine," "this world's," "characterized by," or "scholars" anywhere in Primary Content or front matter across all five chunks.
- Genuine non-redundancy with the Core is confirmed for all five chunks.
- lpcctx005's claimed extension of the Core's font-tension passage is handled correctly — it explicitly scopes its resolution to the later voice only.
- lpcctx004's G8 quotation is an exact match to Doc_04 Candidate 8's own text.
- Redundancy check against the three named Lexicon-Chunks: lpcctx004 does genuinely different work from lpclex003.
- Retrieve-When/Do-Not-Retrieve-When conditions are genuinely distinguishing across all five chunks.
- All Related-Chunks filenames named actually exist under those exact names.

---

## Overall verdict

Substantial revision round (per `cic-build-cycle`'s own definition — the two HIGH findings changed a sourcing conclusion and corrected a fabricated-exactness claim). All findings independently re-verified against source before fixing; one (M1) was re-verified and found not to hold, and was left unchanged rather than fixed on the strength of the review's own assertion. The underlying grounding, phase attribution, and voice discipline were confirmed sound throughout — the defects were concentrated in specific, identifiable claims, mostly in a single chunk (lpcctx003), not a wholesale problem with the set's own method.

---

## Targeted recheck (isolated subagent, scoped to the fixes above)

**Verdict: 6 of 8 items PASS outright; 2 items PASS-on-substance with a small defect introduced by the fix pass itself.** All six substantive fixes (H1, H2, M2, M3, M4's two named gaps, M5) independently reconfirmed against their cited primary sources. The M1 non-fix was independently re-derived and agreed with. Two non-substantive defects found, both cross-reference accuracy issues rather than scholarly or fidelity problems: lpcctx002's Confidence Note misidentified which Primary Content paragraph the false-prophetess content sits in ("third" instead of "fifth," since the fix itself had added a new paragraph); and a third, previously-uncaught Related-Chunks reciprocity gap (lpcctx005 lacked a return link to lpcctx003, alongside the two gaps M4 had already fixed). Both corrected in a follow-up commit on the same branch; no scholarly claim, quotation, phase attribution, or voice-discipline finding required any further change. General fabrication/voice/consistency check: clean across all five chunks.
