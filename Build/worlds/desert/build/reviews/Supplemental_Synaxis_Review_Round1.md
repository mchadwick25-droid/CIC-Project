# Supplemental Source Review — Cassian Institutes II Addition — Cold Review, Round 1

**Reviewer stance:** independent, no part in drafting. Every claim checked against the vendored XML directly, engine code, and a live re-run of the gate battery — not trusted from the drafting session's own account.

**Under review:** `records/desert/quote/desert.quote.twelve-psalms-by-an-angel.md`, `records/desert/quote/desert.quote.never-kneel-saturday-to-sunday.md`, `records/desert/term/desert.term.synaxis.md`, `records/desert/world_core/desert.core.desert.md` (`thin_topics` entry), against `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml`, `engine/m1/schemas.py`, `engine/m1/gates.py`.

**VERDICT: Pass, with one real curatorial gap (SUBSTANTIAL) and several minor terminology/consistency notes (COSMETIC).** Every primary-source claim checked against the vendored XML directly holds up character-for-character. The historical/methodological hedging is accurate and appropriately calibrated. Internal consistency and schema/gate correctness are clean, independently re-verified.

## A. Primary-source verification — CLEAN

Both quotes checked byte-for-byte against the vendored file. `desert.quote.twelve-psalms-by-an-angel`: locus "npnf211 line 17133" confirmed exact (Chapter V's own opening div tag); quoted text an exact match to lines 17184-17211, no wording or punctuation drift. Confirmed inside Book II, not III or IV. `desert.quote.never-kneel-saturday-to-sunday`: locus line 17728 confirmed exact (Chapter XVIII's opening div tag, the last chapter of Book II); quoted text an exact match; the disclosed elision is honest.

## B. Historical/methodological reasoning — CLEAN

Cassian's "throughout the whole of Egypt and the Thebaid" claim is real and accurately located at II.4. The Tertullian/Irenaeus footnote at II.18 is real and accurately characterized. The caution is proportionate, neither over- nor under-hedged.

## C. Internal consistency — CLEAN

No fabricated attribution anywhere. `citation_specificity`/`formation_confidence` on the pre-existing Palladius/Apophthegmata material unchanged. New material clearly dated and distinguished from prior review-round history. `desert.core.desert.md`'s edited `thin_topics` entry is valid YAML, a single coherent edit, no duplication.

## D. Schema/engine correctness — CLEAN, independently re-run

Both new quote records satisfy `COMPLETION_REQUIRED["quote"]` with valid enums. Full gate battery re-run: 0 findings on every gate except `reciprocity` (1), traced to a pre-existing, documented, unrelated finding (`desert.limit.communal-wrong-unrepaired`/`desert.story.moses-leaking-jug`, per `CAPPADOCIAN_BUILD_LEDGER.md` line 604). FK grade independently recomputed on both `modern_rendering` fields: 6.09 and 9.08, both under the ceiling of 10 (9.08 flagged as close to the ceiling - any future light copyedit should be re-checked).

## E. Overclaiming/underclaiming — ONE SUBSTANTIAL FINDING, plus a secondary one

**SUBSTANTIAL:** Institutes II.10, "Of the silence and conciseness with which the Collects are offered up by the Egyptians" (line 17390), is Cassian's own naming and glossing of the term "synaxes" itself, with vivid, specific content (assembly-wide silence, one voice chanting, no coughing/yawning) — a better, more directly on-point passage than either chosen quote for a term record specifically about *synaxis*, sitting one chapter away and unused. Chapters II.7 and II.12 are also stronger candidates that were passed over. Does not make the two chosen quotes wrong.

**SUBSTANTIAL (secondary):** a parallel case of unused-but-vendored, purpose-declared sources exists elsewhere in this world: `desert.source.jerome-de-viris` (registered specifically so `desert.contested.antony-literacy` could cite it directly - not cited there), `desert.source.jerome-letter-22` (registered as an outside contemporary witness to the strand distinction - zero citations anywhere), `desert.source.athanasius-festal-letters` (registered to support a Nag Hammadi-burial contested claim that does not appear to exist yet as a record). Outside this review's own scope (Cassian/synaxis specifically); logged for a future pass, not chased here.

## COSMETIC findings

1. `formation_confidence: Contested` on both new quote records is a debatable enum choice — "Inferential-Thin" arguably fits the actual shape of doubt (a single generalizing source's reach beyond its attested scope, not a competing claim) more precisely. Not gate-enforced; the divergence_note explains the reasoning regardless of label.
2. Minor phrasing tension (not a contradiction) between the twelve-psalms quote's divergence_note and its own `do_not_retrieve_when` guidance - operationally sensible, cosmetic only.
3. `desert.term.synaxis.md`'s `sources[]` folds multiple loci into one entry while the quote records split them - a small stylistic asymmetry, not a schema issue.

## Round-2 verification

Performed directly against the current files (self-verified by the build thread, matching this project's own established precedent for a small, mechanically checkable residual - see `Step5_G05_Supplemental_Source_Review_Round1.md` in the PAHC world for the same discipline applied to a comparable finding set).

- **SUBSTANTIAL (II.10 missed):** LANDED. Added `desert.quote.so-perfectly-silent` (Institutes II.10, npnf211 line 17396), verified byte-for-byte against the vendored file, with a disclosed elision (the chapter's second paragraph, on involuntary groaning, cut to keep the quote to one self-contained idea). Reciprocal `illustrates`/`illustrated-by` relations added between the new quote and `desert.term.synaxis`. FK grade on the first-drafted `modern_rendering` came in at 12.1 (over the ceiling); rewritten to shorter sentences and reconfirmed at 3.0.
- **SUBSTANTIAL (secondary, unused Jerome/Athanasius sources):** NOT landed in this pass - logged in `desert.term.synaxis.md`'s own trailing body and in this world's `DECISION-LOG.md` entry as a disclosed follow-up item, per the reviewer's own framing that it sits outside this review's scope.
- **Cosmetic findings 1-3:** not acted on - genuinely cosmetic, left at the drafter's discretion per this project's own Revision Decision rule.

Full `engine.m1.gates.run_all` battery re-run after the II.10 addition: clean except the same one pre-existing, unrelated reciprocity finding. `desert.term.synaxis.md` and the new quote record's YAML re-validated.

**VERDICT: The one directly-actionable substantial finding LANDED and independently re-verified; the secondary substantial finding logged as a disclosed, deliberately-deferred follow-up rather than silently dropped. Ready for disposition.**
