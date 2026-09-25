# Record Compilation, Part 4 (Gravity + Force Records) — Round 1 Independent Adversarial Review

## Latin Pastoral-Congregational Christianity (`lpc`) — `worlds/lpc/scripts/wb_lpc_s25.py` and `records/lpc/gravity/`, `records/lpc/force/`

*Simulated review — informational only, not an Article 31 substitute.*

**Date:** 2026-09-25 · **Round:** 1 · **Deliverable under review:** 8 `gravity` and 17 `force` record files (25 total, uncommitted) and the generator script that produced them, drafted cold by a different agent from `Doc_04_Gravity_Discovery.md` and `Doc_08_Forces_Document.md`.

A prior pass this session already independently confirmed: the 8+17=25 file count; a clean `engine.m1.gates.run_all` (271 records load, only the pre-existing `gate-canon-coverage`, 28 findings, fires); the 8 gravity classifications against Doc_04's own text (4 Primary/3 Supporting/1 Tensional, including Candidate 5/G5's project-lead-ruled Supporting status and its `contested`/`Inferential-Thin` carrying); all 17 force IDs against `lpc_Force_Index.md`'s master table; and a spot-check of Force 1A-1 against the Force Index's own cell/gravity/relation data. Those points are not re-litigated below; this review covers what that pass did not check.

---

# VERDICT: CLEARED REVIEW — no substantial-revision finding

**0 HIGH · 1 MEDIUM · 1 LOW · 0 COSMETIC.**

I read `Doc_04_Gravity_Discovery.md` and `Doc_08_Forces_Document.md` in full, `lpc_Force_Index.md` in full, `wb_lpc_s25.py`'s own docstring and body in full, all 8 gravity and all 17 force records on disk, and cross-checked every `sources[]`/`relations[]` id against the full 271-record set (`records/lpc/{source,world_core,term,story,figure,quote,gravity,force}/`).

**The relations graph, independently recomputed from the 25 on-disk files' own `relations[]` fields (not from the script's docstring or the Index), matches the drafting agent's claim exactly:** 15 gravity↔gravity edges, 29 gravity↔force edges, 14 force↔force edges — 58 distinct edges total — and every one of the 58 is fully bidirectional (each target's own record lists the edge back), with zero one-way edges. The gravity↔gravity set was independently re-derived cell-by-cell from Doc_04 §6's 8×8 Interaction Matrix (every "Reinforcing"/"Competing"/"Reshaped by" cell, none of the "No demonstrated relationship" cells) and matches the script's 15-pair `RELATION_PAIRS` list exactly. The gravity↔force set matches Doc_08 §5's gravity-by-gravity list and `lpc_Force_Index.md` §3 exactly, including G4's five-force expansion of the prose set-reference "in truth every force in Cell 2A." The force↔force set matches Doc_08 §4's 14 named connections exactly, correctly excluding 2A-2's own deliberate non-connection.

**Every `sources[]`/`relations[]` target across all 25 records resolves to a real, existing record** — checked programmatically against all 271 loaded records, zero misses.

**Force 2B-1's asymmetric G2/G6-not-G7 finding is genuine, not an invented dramatization.** Doc_08 §5's own G6 entry states, in its own words: *"Round 3 removed 2B-1 from this list, arguing that Doc_04's family resemblance runs symmetrically to Candidates 6 and 7, so neither should carry it... The symmetry argument was wrong at a locus it did not read... G7's list correctly does not carry 2B-1, and its single-force origin stands on the 'Reshaped by' relation rather than on a symmetry that does not exist."* The compiled `Force 2B-1` and `G6` records' provenance notes describe exactly this history and no more than this history. Confirmed against Doc_08 §5's own text, not merely against the drafting agent's restatement of it.

**Gravity six-test language spot-checked against Doc_04's own stated results for G1, G2, G3, G4, G6, and G7** (in addition to G5, already checked by the prior pass): every Repetition/Dependency/Formation/Explanatory/Persistence/Interaction verdict and every Confidence/Gravity Cross-Check result in the compiled records is a faithful condensation of Doc_04 §3's own language for that candidate, including verbatim-quoted phrases ("thin across the span, not bounded within it," "a real temporal boundary, not a gap in the search," the shepherd/flock quotation, the 256 preface's egalitarian formula). No paraphrase found that drifts from what Doc_04 actually concludes.

**Schema compliance, checked against `engine/m1/schemas.py` directly:** every gravity record's `classification` and every force record's `kind`/`matrix_cell` fall inside their declared enums; every `confidence.citation_specificity`, `verification_state`, `evidentiary_weight`, and `formation_confidence` value falls inside its enum (`evidentiary_weight: contested` used only for G5, `load-bearing` elsewhere, matching the docstring's own claim); `register: etic`, `canon_cells: []`, `status: draft` uniform and correct.

**The disclosed empty-sources/empty-relations decisions, checked against Doc_08 §5's own text directly, are correctly executed in the actual records**, with one caveat (M1, below). On disk: `sources[]` is empty for exactly four forces — 1A-2, 1B-3, 2B-3, 3B-2 (1B-3 because Tertullian's corpus is Registry row 29, Boundary Status EXCLUDED, with no compiled `lpc.source.tertullian-*` record) — and no gravity↔force relation exists for exactly three forces — 2B-3, 2B-5, 3B-2 — matching Doc_08 §5's "cross-cutting rather than gravity-specific" disposition for the two Transmission forces and Doc_04 §2's declined-to-advance finding for 2B-3. **Force 2B-5 itself is not among the empty-sources forces** — it carries two real sources (Cyprian's Epistles; Knöll's *Retractationes* edition) — and the compiled record is correct on this point.

---

# Method

I read `CLAUDE.md` in full first. I then read `Doc_04_Gravity_Discovery.md` and `Doc_08_Forces_Document.md` in full, `lpc_Force_Index.md` in full, `wb_lpc_s25.py`'s own docstring and body in full (all 1589 lines), and the relevant `gravity`/`force`/envelope sections of `engine/m1/schemas.py`. I read `RecordCompilation_Part2_Round1_Review.md` for reporting format. I extracted every gravity and force record's YAML front matter programmatically (not by trusting the script's stated intent) to independently recompute the relations graph, check bidirectionality, check cross-reference resolution against all 271 loaded records, and check every enum value against the schema. I read all 25 records' `sources[]`/`relations[]`/`confidence` blocks directly from disk.

---

# MEDIUM Finding

## M1 — The script's own docstring misstates, in its own commentary, which forces "carry NO gravity connection at all"

**Where:** `wb_lpc_s25.py`, docstring, "RELATIONS" §2 (GRAVITY ↔ FORCE), around line 224.

**What's wrong:** The docstring reads: *"Three forces (1A-2, 1B-3, 2B-3, 2B-5, 3B-2 -- five, not three) carry NO gravity connection at all, per Doc_08 §5's own gravity-by-gravity list and lpc_Force_Index.md §1's own 'Connected Gravities: --' entries for exactly these five rows."* This is false on its face and self-contradicted two paragraphs earlier in the same docstring's own INPUTS section, by the Force Index's own Master Table, and by the script's own `RELATION_PAIRS` list immediately below: **Force 1A-2 connects to G1** and **Force 1B-3 connects to G4** — both correctly present as `(G1, F1A2)` and `(G4, F1B3)` in `RELATION_PAIRS`, and both correctly present in the actual compiled records (`lpc.force.standing-legal-condition-unlicensed-religion.md` lists `lpc.gravity.pastoral-office-flock-keeping` in `relations[]`; `lpc.force.inherited-latin-theological-vocabulary.md` lists `lpc.gravity.preaching-and-catechesis`). Only **three** forces actually have no gravity connection — 2B-3, 2B-5, 3B-2 — confirmed directly against the Force Index Master Table's "Connected Gravities: —" rows and against every one of the 25 compiled records' own `relations[]` fields. The docstring's self-correcting parenthetical ("five, not three") went the wrong direction: the correct count is three, not five.

**Why MEDIUM, not HIGH:** the error lives entirely in the script's own explanatory commentary, not in the code that generates records (`RELATION_PAIRS`) or in any compiled `.md` file. I verified, by direct extraction of all 25 records' `relations[]` fields and by re-running the bidirectionality/edge-count check against them, that the actual output is correct throughout — no gravity, force, or relation is misrepresented in any record a reviewer or downstream builder would actually read. In a fabrication-intolerant project, a script comment that asserts "confirmed directly rather than assumed" and is then wrong is still worth catching and correcting, since it is exactly the kind of self-verification claim this project's own discipline depends on being trustworthy — but it does not touch the scholarly record itself.

---

# LOW Finding

## L1 — A provenance-note aside about G4's Interaction Matrix profile is imprecisely worded, though the record's own data is correct

**Where:** `wb_lpc_s25.py`, `G4`'s own provenance note (body text passed to `emit_gravity`).

**What's wrong:** The note states relations[] "carries the gravity<->gravity edge (G7) -- the Interaction Matrix's own weak/narrow profile for this candidate means it shares a demonstrated relationship with only one other gravity, per Doc_04 §6's own row for Candidate 4." Read standalone, this implies G4 has only one gravity-level relationship in total. In fact Doc_04 §6's own row for Candidate 4 shows three: Reinforcing with G1, Reinforcing with G2, and Reinforcing with G7 — the note's "only one other gravity" is true only in the incremental sense that G1 and G2 were already captured as edges when earlier rows (1 and 2) were processed, so G7 is the only *new* edge contributed at G4's own row. The compiled record's own `relations[]` field is unaffected and correct (it does carry G1, G2, and G7, confirmed on disk).

**Why LOW:** this is a wording imprecision in an internal provenance comment, not a misstatement in any field a downstream reader or gate consumes, and does not change any classification, confidence, or connection claim.

---

# What I checked and found solid

- **25 records ↔ 8 gravities + 17 forces**, matching Doc_04 §4 and Doc_08 §3/§9 exactly, no omission or extra emission.
- **Relations graph, independently recomputed from the 25 disk files directly:** 15 gravity↔gravity + 29 gravity↔force + 14 force↔force = 58 edges, all fully bidirectional, zero one-way or missing-reciprocal edges.
- **Gravity↔gravity edges verified cell-by-cell against Doc_04 §6's own 8×8 Interaction Matrix**, not merely against the script's own restatement of it.
- **Gravity↔force edges verified against Doc_08 §5's own prose and `lpc_Force_Index.md` §3**, including G4's set-reference expansion.
- **Force↔force edges verified against Doc_08 §4's own 14-row table**, with 2A-2's deliberate non-connection correctly excluded from `relations[]` and correctly named in that force's own body text instead.
- **Cross-reference resolution:** every `sources[]`/`relations[]` target across all 25 new records resolves to a real record in the full 271-record set, zero misses.
- **Force 2B-1's Round-3-reversal-found-wrong history:** confirmed genuine against Doc_08 §5's own text, not an invented dramatization.
- **Six-test language for G1, G2, G3, G4, G6, G7 (plus G5, per the prior pass):** faithful to Doc_04 §3's own stated results, including verbatim quotations, no drift.
- **Disclosed empty-sources/empty-relations decisions:** correctly executed on disk for all five named forces individually (four empty-sources: 1A-2, 1B-3, 2B-3, 3B-2; three no-gravity-relation: 2B-3, 2B-5, 3B-2), checked against Doc_08 §5's own text.
- **Schema compliance:** all `classification`/`kind`/`matrix_cell` and all `confidence.*` enum values fall inside `engine/m1/schemas.py`'s declared sets; `register`, `canon_cells`, `status`, `world_id` uniform and correct.
- **No invented content anywhere:** no gravity classification, confidence rating, quotation, or force connection found in any of the 25 records that Doc_04 or Doc_08 does not itself state.

---

# Recommended disposition

**Cleared Review.** M1 is a documentation-precision defect confined to the script's own docstring commentary — it should be corrected (the correct count is three forces with no gravity connection, not five, and 1A-2/1B-3 should not be listed among them) before this script is treated as a template for a future world's own Part 4 pass, since a future reader relying on the docstring rather than re-deriving the count would be misled. It does not affect any compiled record and does not block proceeding. L1 is a similar but lower-stakes wording note. Per this project's capped-review-cycle discipline, a targeted recheck of the corrected docstring text (not a full re-review) is sufficient for a Round 2, if one is run before this script is folded into a later mechanical pass or reused as a precedent for another world.
