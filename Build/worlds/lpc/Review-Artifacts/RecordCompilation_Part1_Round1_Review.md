# Record Compilation, Part 1 (Source + World_Core Records) — Round 1 Independent Adversarial Review

## Latin Pastoral-Congregational Christianity (`lpc`) — `Build/worlds/lpc/scripts/wb_lpc_s21.py` and `records/lpc/{source,world_core}/`

*Simulated review — informational only, not an Article 31 substitute.*

**Date:** 2026-09-24 · **Round:** 1 · **Deliverable under review:** 208 uncommitted record files (207 `source` + 1 `world_core`) and the generator script that produced them, drafted cold by a different agent from `Source_Registry.md`, `Source_Acquisition_Manifest.md`, and Doc_01/02/07.

---

# VERDICT: CLEARED REVIEW — no substantial-revision finding

**0 HIGH · 2 MEDIUM · 2 LOW · 1 COSMETIC.**

This compilation is unusually clean. I independently re-derived the Registry's own 212-row table by parsing it mechanically (not trusting the script's own count): 212 total rows, exactly 5 carrying Boundary Status "Excluded" (rows 28, 29, 98, 128, 204 — the same five the script and `world_core` name), and 1–212 with no gaps or duplicates. The 207 emitted `source` records map onto the 212-minus-5 Native rows with a perfect 1:1 bijection (checked via `external_ids.lpc_source_registry_row`): no omission, no extra emission, no duplicate. Every one of the 207 records' `citation_specificity` fields matches the Registry's own Confidence letter exactly (0 mismatches, checked programmatically across all 207). Every envelope field (`register: etic`, `schema_version: 2`, `status: draft`, `canon_cells: []`, `world_id`) is uniform and correct across all 207 records, and every `id` is unique and matches its filename. `world_core`'s eight `sources` references all resolve to real, correctly-populated source records.

I re-verified five direct quotations against their vendored source files, all accurate: Cyprian's conciliar preface ("judging no man, nor rejecting any one from the right of communion..."), the Knöll CSEL 33 Confessions opening ("Magnus es, domine, et laudabilis ualde"), the Hartel CSEL 3 Pars III *Vita* heading, Augustine's Letter XCIII coercion passage ("no one should be coerced"), and the *Codex Theodosianus* XVI.5.21 text ("denis libris auri viritim") at its claimed location. I sampled 34 further source records spanning all four Types (P/S/M/L) and all four populated Confidence letters (A/B/C/D), plus a targeted check of the four rows flagged as genuinely hard to categorize (6, 38, 43, 65) — all held up against their Registry rows without embellishment or unsupported upgrade. `world_core`'s `horizon`, `thinness`, `cautions`, and `formation_logic` fields were spot-checked against Doc_01 and Doc_02 directly (time window, Living Tradition Status date, the conciliar-authority open question, the Inferential-Thin material-evidence banding, the "recurring move" correctly *not* listed among the Gravity Spine, matching Doc_04's declining to advance it as a gravity) — all accurate, none overstated.

Two MEDIUM findings, both about internal-methodology precision rather than substantive fact, are below. Neither misrepresents a primary source, a sibling document, or a historical claim, and neither would block Phase Two.

---

# Method

I read `CLAUDE.md` in full first. I then read `Source_Registry.md` and `Source_Acquisition_Manifest.md` in full, Doc_01 in full (and Doc_02 §8–§9, Doc_07 §2D/§6 by targeted read), and `wb_lpc_s21.py`'s own docstring in full. I re-derived the Registry's row count, exclusion set, and Confidence-letter distribution mechanically by parsing the table's own pipe-delimited columns directly (not trusting the script's stated numbers), and cross-checked that derivation against the 207 emitted records' own `external_ids` field, `citation_specificity` field, and envelope fields, all programmatically, rather than by eye. I read `lpc.core.latin-pastoral-congregational-christianity.md` in full. I sampled 34 source records (a stratified draw across Type × Confidence buckets, oversampling the rarer M/L/D populations) plus the four rows the task specifically flagged as hard (6, 38, 43, 65), reading each against its own Registry row. I independently re-verified five direct quotations against the actual vendored `cic/texts/` files by direct grep, including line-number claims.

---

# MEDIUM Findings

## M1 — `verification_state: verified-via-authority` applied to five Confidence-C/D rows, outside the script's own documented mapping rule

**Where:** records for rows 41 (`acta-proconsularia-sancti-cypriani`, Confidence D), 45 (`possidius-vita-augustini-standing-reference`, C), 61 (`goldbacher-augustine-epistulae-standing-reference`, C), 65 (`lancel-actes-de-la-conference-de-carthage-411`, C), and 88 (`codex-theodosianus-latin-library-transcription`, C).

**What's wrong:** The script's own docstring states the mapping mechanically and exhaustively: `verified-via-authority` is used only for "Registry B where the underlying work IS vendored," and Confidence C/D rows get either `named-not-rechecked` (the default) or, if this build session directly opened and confirmed the object itself, `verified-direct` — no third option is named for C/D. All five of the rows above are C or D, not B, yet all five carry `verified-via-authority`. In each case the underlying pattern is the same and is a real one — a Confidence-C/D "standing reference" row whose actual content is vendored under a *different* row number (e.g. row 65's Migne PL11 *Gesta* file, row 45's Weiskotten Possidius now at row 192, row 61's Goldbacher CSEL volumes now at rows 193/195/196) — but the docstring's stated rule doesn't disclose or account for this extension. Row 65 in particular was directly opened and its own content independently verified this session (the delegate roster, the fourteen-act OCR-tolerant scan) — by the docstring's own stated exception, that should have produced `verified-direct`, not `verified-via-authority`.

**Why MEDIUM, not HIGH:** this does not overclaim confidence in the ancient-world evidence itself — if anything `verified-via-authority` sits below `verified-direct` on the conservative side, so no record over-asserts what was checked. It is a real, checkable gap between the script's own stated field-by-field methodology and its actual output, applied consistently enough across five rows to look like a deliberate, undisclosed convention rather than a random slip — worth naming and either folding into the docstring's rule or correcting to `verified-direct` (row 65 especially, where direct verification is extensive and stated in the record's own divergence_note).

## M2 — `rights_status` boilerplate cites a Manifest rule whose own stated preconditions several Confidence-B rows do not meet

**Where:** records for rows 30 (Brown), 31 (Lancel biography), 32 (Burns), 33 (Burns & Jensen), 36 (Shaw) — the earliest secondary-scholarship rows (Round 1, 2026-09-01/02) — all Confidence B, all carrying `rights_status: CONSULTATION_ONLY`, which quotes verbatim: *"every Native, **Confidence-C-or-below** Registry row whose Verification Note says 'in copyright' and 'consultation-only' or 'not a vendoring candidate' is in this category."*

**What's wrong:** none of these five rows is Confidence-C-or-below (all are B), and none of their own Registry Verification Notes contains the phrase "in copyright," "consultation-only," or "not a vendoring candidate" at all (checked directly against each row's own text) — the literal test the quoted rule states. The substantive classification is certainly correct (these are unquestionably in-copyright, never-vendored secondary monographs), but the record's own stated justification — quoting a rule "per that same rule" — doesn't actually cover these rows on either of its two stated conditions. From row 53 onward, the Registry's own rows do carry the literal trigger phrase, so the rule was evidently written with the later rows in mind and applied backward to the earlier ones without adjustment.

**Why MEDIUM, not HIGH:** no rights position is wrong in substance — nothing here risks a vendoring or licensing error — and the actual classification these five rows land on is the correct one regardless of which literal test is invoked. This is a documentation-precision gap (a boilerplate over-citing its own rule's coverage), not a fabricated or upgraded claim.

---

# LOW Findings

## L1 — Bibliotheca Hagiographica Latina (row 100) held uniformly CONSULTATION_ONLY despite disclosed mixed rights

The record's own `edition` field discloses "mixed rights... the base volumes and the 1911 Supplementum are public domain, the 1986 Novum Supplementum is in copyright," but `rights_status` still applies the single CONSULTATION_ONLY bucket to the whole row. This is explicitly disclosed as "a builder's judgment call rather than a review instruction" in the record's own divergence_note — a defensible conservative choice, not an error, but it leaves a real (public-domain) partial-vendoring opportunity unexploited without escalating it as an open item the way comparable cases elsewhere in the Registry (rows 64, 67) do.

## L2 — Two documented-departure rows (56, 88) inherit their special-case Confidence annotations correctly, but the pattern is fragile

Rows with an inline-annotated Confidence cell in the Registry (e.g. "**B** (raised from C...)", "**C** (running text reads clean...)") are correctly reduced to their bare letter in the compiled records' `citation_specificity` field (confirmed programmatically for all such rows). This is correct as done, but nothing in the schema or the record itself preserves *why* the letter was reduced — a future reader of the record alone, without the Registry, would not know these letters carry an inline qualifier. Not a defect in what was compiled, since the qualifying prose is carried in each record's own `divergence_note`; noted only because it is easy to lose track of on a future pass that edits `divergence_note` without checking the Registry cell it silently depends on.

---

# COSMETIC

The four rows the task flagged as "genuinely hard to categorize" (6, 38, 43, 65) are in fact handled with more disclosure and care than most of the Registry's C-level population — row 38's honest `unverified`/`Inferential-Thin`/`NO_EDITION_HELD` treatment and row 43's boundary-case Native reasoning are, if anything, exemplary rather than weak points. Worth noting so this finding is not read as "the hard rows are the weak rows" — here they are not.

---

# What I checked and found solid

- **Row-count and exclusion-set mechanical re-derivation:** 212 total rows; exactly rows 28, 29, 98, 128, 204 Excluded; 1–212 with no gaps or duplicates — independently parsed from the table, not taken from the script's or `world_core`'s own stated count.
- **207 source records ↔ 207 Native rows, exact bijection** — checked via `external_ids.lpc_source_registry_row`, zero omissions, zero duplicates, zero excluded rows leaked through.
- **`citation_specificity` field, all 207 records:** zero mismatches against the Registry's own Confidence letter.
- **Envelope fields, all 207 records:** `register: etic`, `schema_version: 2`, `status: draft`, `canon_cells: []`, `world_id` uniform and correct; all 207 `id` values unique and matching filename.
- **Five direct quotations, independently re-verified against the actual vendored files:** Cyprian's conciliar preface (anf05), the Knöll Confessions opening (row 197), the Hartel CSEL 3 Pars III *Vita* heading (row 194), Augustine's Letter XCIII coercion passage (npnf101), and *Codex Theodosianus* XVI.5.21 at its claimed line (theodosianus-16).
- **34-record stratified sample plus rows 6/38/43/65:** no fabricated author, work, edition, rights claim, or confidence upgrade found anywhere in the sample; every Licensed-For, divergence_note, and attribution_status claim checked against its Registry row held up.
- **`world_core` cross-checked against Doc_01/Doc_02/Doc_07:** time window (246–430, both endpoints), Living Tradition Status confirmation (2026-09-16), the three named authority-structure axes and the conciliar-authority open question, the century-gap disclosure (133 years, 258–391), the Inferential-Thin material-evidence banding (Doc_02 §8), and the "recurring move" correctly kept out of the Gravity Spine list (matching Doc_04's declining to advance it as a gravity) — all accurate, none overstated or misattributed.
- **No invented content anywhere:** no author, family, date, or anecdote asserted that the Registry, Manifest, or Doc_01/02/07 does not itself state.

---

# Recommended disposition

**Cleared Review.** M1 and M2 are cheap, fully diagnosed fixes (relabel five `verification_state` values, or extend the docstring's rule to cover them explicitly; and either correct the five B-confidence rows' `rights_status` boilerplate to a rule that actually fits them, or amend the Manifest's own quoted rule to state what it is evidently already being used for). Neither blocks proceeding to canon-cell tagging or Phase Two, and per this project's capped-review-cycle discipline a targeted recheck of the corrected fields (not a full re-review) is sufficient for Round 2, if a Round 2 is run at all before the fixes are folded into a later mechanical pass.
