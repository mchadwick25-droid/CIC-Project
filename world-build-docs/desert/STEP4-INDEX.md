# Desert Monasticism — Step 4 Index (Answering the Canon)

**Derived from:** 8 `story` records, 6 `quote` records, 9 `doctrinal_witness` records, and 4 `honest_limit` records (`records/desert/{story,quote,doctrinal_witness,honest_limit}/`) — this index is generated against those files and re-checked against them; the records are the source of truth. Re-derivation base for the 8 stories: the prior build's cleared `Doc_09a` (`World-Builds/Desert-Monasticism/CiC_W3_Doc09a_Story_Inventory.md`, two review rounds, APPROVED TO PROCEED) — every story re-verified this session against this build's own registered source records and, where possible, the vendored files directly, rather than carried forward unread. Quotes, doctrinal_witness, and honest_limit records have no prior-build direct equivalent at this granularity and were drafted fresh, but exclusively from material already independently verified either in this step or in Steps 2–3c/Doc_08.

**Scope note:** per this build's own "depth proportional to formation weight, not comprehensiveness for its own sake" principle (Doc_09a's own open item 1), this step targets the canon cells this corpus can genuinely answer or genuinely cannot, rather than maximizing record count. All 27 records trace to material already independently verified elsewhere in this build; none introduces a new primary-source claim without either a fresh direct verification against a vendored file (noted per record) or an explicit citation to an already-cleared registered record.

## Stories

| record | tier | canon_cells | source |
|---|---|---|---|
| `desert.story.antony-call` | 1 | F4-I, F2-I | Vita SS2-3 |
| `desert.story.antony-withdrawal` | 1 | F4-I, F5-P | Vita SS3-4, SS12-13, SS49-50 |
| `desert.story.pachomius-founding` | 1 | F4-I, F3-I | Palladius ch. XXXII; pachomian-corpus |
| `desert.story.moses-leaking-jug` | 2 | F4-P | Apophthegmata (paraphrase-only) |
| `desert.story.arsenius-flee` | 2 | F4-I | Apophthegmata (paraphrase-only) |
| `desert.story.sarah-answer` | 2 | F6-P | Apophthegmata (paraphrase-only) |
| `desert.story.antony-tomb-combat` | 3 | F4-P | Vita SS8-10, SS12-13 |
| `desert.story.kellia-day` | 4 (reconstruction) | F4-I, F5-E | Apophthegmata; Kellia excavations |

Tier distribution matches Doc_09a's own exactly: 3 Tier 1, 3 Tier 2, 1 Tier 3, 1 Tier 4 — no Tier 5, per the Story Repository Chunk Template's own bar against generated or illustrative narrative. Doc_09a's own Round 1 fix (the unsourced Story 4.1 diet element removed rather than retained-and-flagged) is carried forward as already corrected in `desert.story.kellia-day`, not reintroduced.

## Quotes

| record | license | speaker | canon_cells |
|---|---|---|---|
| `desert.quote.antony-not-worsted` | verbatim | `desert.figure.antony` | F4-P |
| `desert.quote.antony-dying-daily` | verbatim | `desert.figure.antony` | F4-I |
| `desert.quote.antony-arians-serpents` | verbatim | `desert.figure.antony` | F3-T, F1-T |
| `desert.quote.sarah-man-among-you` | paraphrase-only | `desert.figure.sarah` | F6-P |
| `desert.quote.moses-sins-run-out` | paraphrase-only | "Abba Moses (Apophthegmata Patrum)" | F4-P |
| `desert.quote.arsenius-flee-tace-quiesce` | paraphrase-only | "a voice Arsenius reports having heard" | F4-I |

Three verbatim quotes, all independently re-verified directly against the vendored `npnf204_athanasius-select-works-letters.xml` this session (not carried forward from any prior citation without re-opening the file). Three paraphrase-only quotes, all from `desert.source.apophthegmata-patrum`, which carries no vendored edition and whose own hard rule bars any verbatim-quote claim against it — matching the discipline already established for `desert.figure.sarah`'s own saying at Step 3c.

## Doctrinal witnesses

| record | canon_cells | basis |
|---|---|---|
| `desert.dw.c-i-jesus` | C-I | Matthew 19:21 heard as command; "dying daily" as lived pattern |
| `desert.dw.c-e-writings` | C-E | no independent scripture; applied, non-systematic reading mode |
| `desert.dw.f1-i-god` | F1-I | anti-Arian boundary-drawing + Evagrian contemplative vocabulary (theoria, apatheia) |
| `desert.dw.f1-e-councils` | F1-E | conciliar/episcopal authority decided; desert participants refused rather than legislated |
| `desert.dw.f3-p-melitian-power` | F3-P | the Melitian schism, engaged honestly rather than defended |
| `desert.dw.f3-e-strangest` | F3-E | total, immediate renunciation and extended physical seclusion |
| `desert.dw.f4-e-apostolic` | F4-E | no claimed apostolic line; a real, humbler predecessor practice instead |
| `desert.dw.f6-i-never-settled` | F6-I | the person-vs-office authority tension, stated directly |
| `desert.dw.f6-e-death-wish` | F6-E | total struggle as total self-offering, not death-seeking |

Every doctrinal_witness in this set is reasoned directly from an already-registered record in this build (a story, quote, gravity, force, term, or contested_claim record already cleared or verified this session) rather than from a fresh, independently-sourced claim — stated explicitly in each record's own body note. Two (`desert.dw.f1-e-councils`, `desert.dw.f3-p-melitian-power`) extend an existing record's own scope (respectively: internal governance to the wider church; the Melitian force's own Layer 2 reading to a direct first-person acknowledgment) and name that extension explicitly in their own `tensions` field or body note rather than presenting it as a claim the underlying source makes directly.

## Honest limits

| record | canon_cells | why |
|---|---|---|
| `desert.limit.c-t-doubt-and-doctrine` | C-P, C-T, F1-P | no confessional or systematic-doctrinal genre survives in this world's own voice |
| `desert.limit.f2-scripture-detail` | F2-P, F2-T | no source addresses scriptural difficulty, textual violence, or scriptural authority as such |
| `desert.limit.f4-t-born-again-and-end` | F4-T | no tithing detail (total renunciation logic excludes it); no developed eschatology |
| `desert.limit.f6-t-divorce-and-outsiders` | F6-T | boundary-drawing material addresses rival Christians, not outsiders generally or divorce |

Four honest_limit records cover seven cells by grouping genuinely related gaps under one honest statement each, rather than multiplying thin, repetitive records — matching this build's own economy-of-record principle. `engine/m1/canon.py`'s `classify_cell` treats a cell as covered if *any* substantive record or *exactly one* honest_limit claims it; no cell in this document is claimed by more than one honest_limit.

## Canon coverage

**All 18 cells blank at the start of this step are now covered.** 9 by a new doctrinal_witness record, 7 by a new honest_limit record (grouped into 4 records), and 2 (F1-T, F3-T) incidentally by `desert.quote.antony-arians-serpents`. `engine/m1/canon.py`'s `gate_canon_coverage` reports **0 blank cells** across all 86 fleet cells - the same state independently confirmed for the Alexandria build's own finished corpus (checked this session: 137 records, 0 blank cells). This is the first point in this build where that parity is reached.

## Reciprocity and referential integrity

Re-derived mechanically from all 109 record front matters: **274** directed relation ends corpus-wide over **137** distinct pairs (up from 198/99 before this step); **76** ends over **38** pairs involve a Step 4 record (story, quote, doctrinal_witness, or honest_limit). Every `illustrates`/`illustrated-by`, `associated-with`, and other typed relation this step declared is reciprocated on the target record - checked against `RELATION_INVERSE` for every end individually, zero dangling. Full gate battery: **13 gates, 0 findings** across all 109 records, including `gate_reciprocity`, `gate_readability` (the FK-grade ceiling on every `honest_limit.statement`), `gate_quote_recording` (every quote's `license`/`speaker_or_author` pair), `gate_narratability` (every story's tier/justification/tellable_as/text), and `gate_no_build_attribution` (no jargon-leak in any `story.tellable_as`/`text`, `doctrinal_witness.text`, or `honest_limit.statement` - `quote.text` is outside that gate's own field map but was hand-checked and found clean, since every quote's `text` is either a direct primary-source excerpt or a close paraphrase of one, not build commentary).

## Open items carried forward

1. Doc_09a's own open item 1 (whether the Tier 2 saying set should be expanded beyond three) is not resolved here - this step kept the same three sayings Doc_09a selected, illustrative rather than exhaustive by the same stated principle.
2. Doc_09a's own open item 2 (the Pachomian Lives' version-priority question) remains unresolved, carried forward from Doc_01 §10/Doc_02 §1.2 and now also from `desert.force.formation-at-scale`'s own identical carry-forward.
3. `desert.dw.f1-e-councils` and `desert.dw.f3-p-melitian-power` each extend an existing record's own evidentiary scope by one reasoned step (see the Doctrinal witnesses section above) - both extensions are named explicitly in the records themselves, not concealed, but both are a heavier inferential lift than this build's other Step 4 records and are flagged here for a reviewer's particular attention.
4. This step's own honest_limit records name several genuine content gaps (personal doubt-narrative, scriptural-difficulty engagement, tithing/eschatology detail, divorce) that a later step or audit, working from new source material, could close - not treated as permanently closed questions.
5. Per the standing build-sequence instruction, this step does **not** build `voice_craft` or `demonstration` records, and does not attempt compilation or admission. That is the explicit stopping point for this build thread.

## Review rounds note (applied)

*(populated after this step's own adversarial review rounds, per this build's standing discipline)*
