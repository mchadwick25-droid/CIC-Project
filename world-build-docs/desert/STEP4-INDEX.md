# Desert Monasticism — Step 4 Index (Answering the Canon)

**Derived from:** 8 `story` records, 8 `quote` records, 12 `doctrinal_witness` records, and 3 `honest_limit` records (`records/desert/{story,quote,doctrinal_witness,honest_limit}/`) — this index is generated against those files and re-checked against them; the records are the source of truth. Re-derivation base for the 8 stories: the prior build's cleared `Doc_09a` (`World-Builds/Desert-Monasticism/CiC_W3_Doc09a_Story_Inventory.md`, two review rounds, APPROVED TO PROCEED) — every story re-verified this session against this build's own registered source records and, where possible, the vendored files directly, rather than carried forward unread. Quotes, doctrinal_witness, and honest_limit records have no prior-build direct equivalent at this granularity and were drafted fresh, but exclusively from material already independently verified either in this step or in Steps 2–3c/Doc_08.

**Scope note:** per this build's own "depth proportional to formation weight, not comprehensiveness for its own sake" principle (Doc_09a's own open item 1), this step targets the canon cells this corpus can genuinely answer or genuinely cannot, rather than maximizing record count. All 31 records trace to material already independently verified elsewhere in this build; none introduces a new primary-source claim without either a fresh direct verification against a vendored file (noted per record) or an explicit citation to an already-cleared registered record.

**Revision note:** this index reflects the state after Step 4 Round 1 review and its fix pass. The original draft (commit `08e69018`) held 27 records (6 quote, 9 doctrinal_witness, 4 honest_limit); the review found 10 substantial, 18 minor and 9 cosmetic defects (`reviews/Step4_Review_Round1.md`), concentrated in checkable claims about registered material the material did not actually carry. The fix pass added 6 records (2 quote, 3 doctrinal_witness, 1 honest_limit) built from vendored material the original draft had not opened, removed 2 honest_limit records superseded by that new material, and corrected the remainder in place. Net: 27 → 31 records.

## Stories

| record | tier | canon_cells | source |
|---|---|---|---|
| `desert.story.antony-call` | 1 | F4-I, F2-I | Vita SS2-3 |
| `desert.story.antony-withdrawal` | 1 | F4-I, F5-P | Vita SS3-4, SS12-13, SS49-50 |
| `desert.story.pachomius-founding` | 1 | F4-I, F3-I | Palladius ch. XXXII; pachomian-corpus; rousseau-pachomius |
| `desert.story.moses-leaking-jug` | 2 | F4-P | Apophthegmata (paraphrase-only) |
| `desert.story.arsenius-flee` | 2 | F4-I | Apophthegmata (paraphrase-only) |
| `desert.story.sarah-answer` | 2 | F6-P | Apophthegmata (paraphrase-only) |
| `desert.story.antony-tomb-combat` | 3 | F4-P | Vita SS8-10, SS12-13 |
| `desert.story.kellia-day` | 4 (reconstruction) | F4-I, F5-E | Apophthegmata; Kellia excavations; synaxis (term); Vita S3; Palladius ch. VII |

Tier distribution matches Doc_09a's own exactly: 3 Tier 1, 3 Tier 2, 1 Tier 3, 1 Tier 4 — no Tier 5, per the Story Repository Chunk Template's own bar against generated or illustrative narrative. Doc_09a's own Round 1 fix (the unsourced Story 4.1 diet element removed rather than retained-and-flagged) is carried forward as already corrected in `desert.story.kellia-day`, not reintroduced. Round 1 review Finding S3 found this same record retaining-and-flagging its synaxis element instead of sourcing or removing it, and its manual-labor element wholly unsourced — both are now sourced directly (synaxis to the registered `desert.term.synaxis` and Palladius ch. VII; manual labor to Vita S3 and Palladius ch. VII), closing the Tier 4 rule violation with real material rather than by removal.

## Quotes

| record | license | speaker | canon_cells |
|---|---|---|---|
| `desert.quote.antony-not-worsted` | verbatim | `desert.figure.antony` | F4-P |
| `desert.quote.antony-dying-daily` | verbatim | `desert.figure.antony` | F4-I |
| `desert.quote.antony-arians-serpents` | verbatim | `desert.figure.antony` | F3-T |
| `desert.quote.antony-nicene-formula` | verbatim | `desert.figure.antony` | C-T |
| `desert.quote.pachomius-angel-tablet` | verbatim | (an angel, per Pachomius's own account as Palladius reports it) | — |
| `desert.quote.sarah-man-among-you` | paraphrase-only | `desert.figure.sarah` | F6-P |
| `desert.quote.moses-sins-run-out` | paraphrase-only | "Abba Moses" | F4-P |
| `desert.quote.arsenius-flee-tace-quiesce` | paraphrase-only | "a voice Arsenius reports having heard" | F4-I |

Four verbatim Vita quotes and one verbatim Palladius quote, all independently re-verified directly against their vendored files. Three paraphrase-only quotes, all from `desert.source.apophthegmata-patrum`, which carries no vendored edition and whose own hard rule bars any verbatim-quote claim against it — matching the discipline already established for `desert.figure.sarah`'s own saying at Step 3c.

Round 1 review Finding S8 found `antony-arians-serpents` claiming `canon_cells: [F3-T, F1-T]` though its text answers none of F1-T's three fleet questions; the F1-T claim is removed (now `[F3-T]` only), and F1-T is answered honestly instead by the new `desert.limit.f1-t-original-sin-eucharist-faith` below. Finding S6 found `desert.story.pachomius-founding`'s body citing a quote record that did not exist; `desert.quote.pachomius-angel-tablet` is now built from the vendored passage that citation pointed at. Finding S2 found `antony-arians-serpents`'s body falsely denying that Vita S69 (inside its own cited locus) states a positive Trinitarian formula; the new `desert.quote.antony-nicene-formula` supplies that formula directly, verbatim. Finding S5 found two of the three verbatim quotes silently splicing non-adjacent vendored text without the ellipsis marker this step's own convention uses elsewhere; both are now marked. Finding M8 found two paraphrase quotes' `speaker_or_author` carrying a parenthetical provenance tag that compiles directly into `quotes.json`; both removed, provenance kept in `sources[]`/`divergence_note` only. Finding M16 found `antony-not-worsted` missing its reciprocal relation to `desert.figure.antony`; added.

## Doctrinal witnesses

| record | canon_cells | basis |
|---|---|---|
| `desert.dw.c-i-jesus` | C-I | Matthew 19:21 heard as command; "dying daily" as lived pattern |
| `desert.dw.c-p-someone-like-me` | C-P | Moses the Robber and Paul the Simple — a violent or unremarkable past not disqualifying |
| `desert.dw.c-e-writings` | C-E | no independent scripture; applied, non-systematic reading mode, with the Evagrian Antirrhetikos named as its one applied exception |
| `desert.dw.f1-i-god` | F1-I | anti-Arian boundary-drawing (refusal, and one public argument) + the positive Nicene formula + Evagrian contemplative vocabulary (theoria, apatheia) |
| `desert.dw.f1-e-councils` | F1-E | conciliar/episcopal authority decided; desert participants both refused communion at home and, once, argued publicly at episcopal summons |
| `desert.dw.f3-p-melitian-power` | F3-P | the Melitian schism, engaged honestly, carrying that source's own unverified-assumption caution rather than stating it as a finding |
| `desert.dw.f3-e-strangest` | F3-E | total renunciation given away close together, not gradually; years of sought seclusion behind a built-up entrance |
| `desert.dw.f4-e-apostolic` | F4-E | no claimed apostolic line; a real, humbler predecessor practice instead |
| `desert.dw.f4-t-judgment-and-resurrection` | F4-T | judgment and bodily resurrection taught directly and repeatedly, not withheld |
| `desert.dw.f6-i-never-settled` | F6-I | the person-vs-office authority tension, stated directly, with the original hedges restored |
| `desert.dw.f6-e-death-wish` | F6-E | total struggle as total self-offering, not death-seeking |
| `desert.dw.f6-t-marriage-ending` | F6-T | a marriage ended by the other spouse's unfaithfulness was not held against the one who was betrayed |

Every doctrinal_witness in this set is reasoned directly from an already-registered record in this build (a story, quote, gravity, force, term, or contested_claim record already cleared or verified this session, or a vendored source file opened directly) rather than from a fresh, unverified claim — stated explicitly in each record's own body note. Two (`desert.dw.f1-e-councils`, `desert.dw.f3-p-melitian-power`) extend an existing record's own scope (respectively: internal governance to the wider church; the Melitian force's own Layer 2 reading to a direct first-person acknowledgment) and name that extension explicitly in their own `tensions` field or body note rather than presenting it as a claim the underlying source makes directly.

Round 1 review Findings S1 and S4 found the corpus's original two `honest_limit` records for F6-T and F4-T declaring silences that vendored Palladius and the Vita respectively fill at length; those two honest_limit records are removed and replaced by `desert.dw.f6-t-marriage-ending` and `desert.dw.f4-t-judgment-and-resurrection`, drawn from material opened directly for the fix. Finding M17 found the C-P cell's one answerable sub-question (would Jesus have wanted someone like me) had real material the original honest_limit had not opened; `desert.dw.c-p-someone-like-me` now answers it, narrowing `desert.limit.c-t-doubt-and-doctrine`'s own C-P claim to match. Findings S7, S9, S2 (the three "illusory fix" cases — a false self-certifying sentence written in the same edit as the claim it certifies) are corrected in `f3-p-melitian-power`, `f6-i-never-settled`, and `f1-e-councils`/`f1-i-god` respectively. Finding S10 added the unconditional Inferential/Thin bound `desert.source.apophthegmata-patrum` requires to every compiled field carrying its material. Finding M9 removed bare build meta-language ("this record," "this witness," a bare record id) from every affected `tensions` field.

## Honest limits

| record | canon_cells | why |
|---|---|---|
| `desert.limit.c-t-doubt-and-doctrine` | C-T, F1-P | no confessional or systematic-doctrinal genre survives in this world's own voice (narrowed from an original C-P claim, now answered substantively above) |
| `desert.limit.f2-scripture-detail` | F2-P, F2-T | no source addresses scriptural difficulty, textual violence, or scriptural authority as such |
| `desert.limit.f1-t-original-sin-eucharist-faith` | F1-T | no source addresses original sin, eucharistic theology, or faith-versus-works as such |

Three honest_limit records cover five cells, grouping genuinely related gaps under one honest statement each rather than multiplying thin, repetitive records — matching this build's own economy-of-record principle. `engine/m1/canon.py`'s `classify_cell` treats a cell as covered if *any* substantive record or *exactly one* honest_limit claims it; no cell in this document is claimed by more than one honest_limit.

## Canon coverage

**All 18 cells blank at the start of this step are now covered.** 13 by a substantive record (story, quote, or doctrinal_witness) and 5 by a new honest_limit record (grouped into 3 records). `engine/m1/canon.py`'s `gate_canon_coverage` reports **0 blank cells** across all **28 distinct canon cells** `canon.valid_cells()` returns (`records/_fleet/canon_question/` holds 86 individual `canon_question` records, mapping many-to-one onto those 28 cells — the two counts are different things; Round 1 review Finding M6 caught the original draft conflating them).

The same 0-blank-cells state was independently confirmed for the Alexandria build's own finished corpus (137 records) earlier in this session, by temporarily copying its `records/alx/` tree into this branch's working directory as `records/alx_check_tmp/`, running the gate battery against it, and deleting the copy afterward — that check is not re-derivable directly on this branch, since only `records/desert/` and `records/_fleet/` exist here (Round 1 review Finding C7).

## Reciprocity and referential integrity

Re-derived mechanically from all 113 record front matters: **286** directed relation ends corpus-wide over **143** distinct pairs; **88** ends over **44** pairs involve a Step 4 record (story, quote, doctrinal_witness, or honest_limit). Every `illustrates`/`illustrated-by`, `associated-with`, and other typed relation this step declared is reciprocated on the target record - checked against `RELATION_INVERSE` for every end individually, zero dangling. Full gate battery: **13 gates, 0 findings** across all 113 records, including `gate_reciprocity`, `gate_readability` (the FK-grade ceiling on every `honest_limit.statement`), `gate_quote_recording` (every quote's `license`/`speaker_or_author` pair), `gate_narratability` (every story's tier/justification/tellable_as/text), and `gate_no_build_attribution` (no jargon-leak in any `story.tellable_as`/`text`, `doctrinal_witness.text`, or `honest_limit.statement` - `quote.text` is outside that gate's own field map but was hand-checked and found clean, as are `doctrinal_witness.positions`/`tensions`, also outside the field map by design and re-checked by hand per Round 1 review Finding M9).

## Open items carried forward

1. Doc_09a's own open item 1 (whether the Tier 2 saying set should be expanded beyond three) is not resolved here - this step kept the same three sayings Doc_09a selected, illustrative rather than exhaustive by the same stated principle.
2. Doc_09a's own open item 2 (the Pachomian Lives' version-priority question) remains unresolved, carried forward from Doc_01 §10/Doc_02 §1.2 and now also from `desert.force.formation-at-scale`'s own identical carry-forward.
3. `desert.dw.f1-e-councils` and `desert.dw.f3-p-melitian-power` each extend an existing record's own evidentiary scope by one reasoned step (see the Doctrinal witnesses section above) - both extensions are named explicitly in the records themselves, not concealed, but both are a heavier inferential lift than this build's other Step 4 records and are flagged here for a reviewer's particular attention.
4. This step's own honest_limit records name genuine content gaps (personal doubt-narrative and a developed Christology, scriptural-difficulty engagement, original sin/eucharist/faith-versus-works) that a later step or audit, working from new source material, could close - not treated as permanently closed questions.
5. Per the standing build-sequence instruction, this step does **not** build `voice_craft` or `demonstration` records, and does not attempt compilation or admission. That is the explicit stopping point for this build thread.

## Review rounds note (applied)

**Round 1** (`reviews/Step4_Review_Round1.md`, opus, adversarial, no part in drafting): verdict SUBSTANTIAL REVISION REQUIRED — 10 substantial, 18 minor, 9 cosmetic findings against the original 27-record draft (commit `08e69018`). The fabrication sweep, the Apophthegmata paraphrase-only discipline, `quote.text`'s jargon check, reciprocity, the canon arithmetic, the tier distribution, the tension-with discipline and the gate battery were all independently re-derived and found clean; what failed was this build's own documented recurring defect — a checkable claim about registered material the material does not carry — appearing at unprecedented concentration (8 of 10 substantial findings in compiled-facing content, specifically in `honest_limit`/`doctrinal_witness` records making false absence-claims the corpus's own vendored sources contradicted). All 10 substantial, all 18 minor, and all 9 cosmetic findings are fixed in this revision: 6 new records built from vendored material the original draft never opened (2 quote, 3 doctrinal_witness, 1 honest_limit), 2 honest_limit records removed as superseded, and the remainder corrected in place. Gate battery re-run clean: 113 records, 0 non-coverage findings, 0 blank cells.
