# Adversarial Review — `ijc` Record Set (branch `world/ijc`, 125 records)
**Reviewer:** isolated adversarial pass, 2026-08-21 · **Subject:** records/ijc/ (125 records) against records/_fleet/canon_question/ (83 questions, 28 cells), engine/m1/, Redesign-Spec/Artifact-1-Record-Schema.md, Doc_04's Interaction Matrix, the vendored corpus, and records/worlds.yaml.

## Verdict: SUBSTANTIAL REVISION REQUIRED

The mechanical claim is true (13/13 gates clean, independently reproduced and proven non-vacuous by seeded mutation). The record craft is high. But three compiled records make factual negative claims about the world's own record that the world's own registered sources refute; one canon cell is nominally covered by a record answering none of its six questions; and **no search_record anywhere documents a negative search for any honest-limited cell's subject matter** — the honest-limit apparatus is under-evidenced at its root.

## What was checked
Gate battery run directly and proven non-vacuous via 4 seeded mutations (each correctly caught by the intended gate). All 60 records with canon_cells read against the full verbatim text of all 83 canon questions. All 15 deliberately-empty-canon_cells records checked. All 7 honest-limited cells checked question-by-question against the record set AND against cic/texts/ directly. All 9 single-record-covered substantive cells checked question-by-question. All 15 Doc_04 §6 Interaction Matrix pairs checked against encoded relations. Every compiled field scanned for leakage, diffed against the alx exemplar. Registry entry checked against Artifact-1 §2, the record set, and the live census.json.

---

## HIGH

### H1 — `ijc.limit.f1-t-later-questions` factually refuted by the world's own registered sources on 2 of 3 questions

Claims original sin and eucharistic teaching are "later ages' battle lines" the record "does not fight on" — but Ambrose's *De Mysteriis* IX §§53-54 (vendored npnf210, Ambrose is Native) answers the transubstantiation question directly, and Leo's Sermon LXIII (vendored npnf212, Leo is registered) states original sin explicitly ("after the transmission of original sin to their descendants..."). The `alx` exemplar (earlier window!) carries a substantive original-sin witness; a later world honest-limiting the same cell on false grounds is not credible.

### H2 — `ijc.dw.f4-t-baptism-threshold` asserts a false negative: "church funding... not tithe-discipline" — Leo's Sermons VI-XI ("On the Collections") are a preached, dated, congregational giving discipline, already registered (`ijc.source.leo-sermons`, already cited elsewhere)

Same source also carries Sermons XII-XX/LXXXVI-XCIV "On the Fasts" — direct answer-ground for f4-i-04 (fasting), untouched by any record.

### H3 — `ijc.limit.f5-t-marriage-money`: "ascetic-marriage debates... belong to other worlds' corpora" is false for this world's own Ambrose (*Concerning Widows*, *Concerning Virgins*, *De Officiis* — same vendored volume as the registered Ambrose epistles); also the money half is answerable (*De Officiis* II.28, church plate melted for ransom) and the limit half-concedes this without recording it as coverage

### H4 — F6-P covered by exactly one record (`ijc.story.emperor-penance`) that answers NONE of the cell's six questions

The tag is a loose thematic association exactly of the kind the project rule prohibits. f6-p-06 (a woman's authority and its cost) is fully answerable from already-built, untagged material: `ijc.figure.pulcheria` and `ijc.figure.justina`, both `narratable: true`.

### H5 — Structural: no search_record documents a negative search for ANY honest-limited cell's subject matter

All 16 search_records are work/volume-scoped, never topic/cell-scoped. This is the root cause of H1-H3 — the honest limits assert "our record is silent" when the actual gap is "nobody searched." **Single most consequential fix in this review.**

---

## MEDIUM
- **M1** F5-P single-record coverage: stretch on one question, silent on the other; `ijc.term.communio` and the letter-corpus already answer f5-p-02 (distance/connection) untagged
- **M2** `ijc.quote.jerome-damasus-verses` F5-E tag is a loose association (quote mentions no inscription/archaeology at all; real job is `illustrates -> figure.damasus`)
- **M3** `ijc.limit.c-p-jesus-to-you` answers only 1 of 3 cell questions; Leo's Nativity preaching (2nd-person address) is unregistered nearest_material
- **M4** Fleet-architecture leakage into compiled fields BEYOND the alx precedent: `ijc.dw.f2-i-how-we-read.text` names "other Christian worlds"; `ijc.limit.f5-t-marriage-money.statement` names "worlds that kept them"; `ijc.core...thinness` names "other formation worlds"; `cautions` §6 names three sibling worlds by name plus rights language — alx's leakage is confined to `world_core.cautions` only, this extends into `doctrinal_witness.text` and `honest_limit.statement`, fields alx keeps clean
- **M5** Doctrinal-witness retrieval tiers: 6 of 7 are tier 2 vs. alx's 13/13 at tier 1, unexplained in any record or BUILD-LOG
- **M6** Two Doc_04 matrix relationships (2↔4, 3↔4 — both explicitly "reshaping" per Doc_04's own Round-1-forced correction) flattened to undifferentiated `associated-with`, re-introducing the ambiguity that correction removed; `tension-with` is available and fits
- **M7** All 7 `contested_claim.divergence_partners` are empty, including the two (`primacy-reception`, `canon-28-meaning`) that the registry's own living-tradition rationale explicitly names divergence partners for
- **M8** Per-question gaps in single-record cells: F2-T (Genesis-as-science unanswered), F4-T (see H2), F6-T (hell and divorce/remarriage unanswered, divorce material exists per H3), F5-E (f5-e-02 "how do historians know" unanswered though the true answer is stated elsewhere untagged)

## LOW
- **L1** Dangling ref: `ijc.figure.justina` → `ijc.limit.f5-women-own-words` (doesn't exist; real id is `f5-ordinary-day`) — only dangling id in the whole set
- **L2** `ijc.story.altar-of-victory` F3-I tag is loose; F3-E would be the honest home
- **L3** `ijc.quote.leo-rome-apostles` illustrates sacramental-institutional-tension but not primacy-claiming, which it fits more directly
- **L4** F5-I carries both an honest_limit and a contested_claim tag — harmless but semantically odd
- **L5** Registry `role_label: "Deacon of the Letters"` drops "Apocrisiarius" from Mark's own recorded 2026-07-22 decision, present only in the comment
- **L6** All 19 sources are `register: emic`; alx flags 4/20 `etic`; Symmachus's Memorial (an opposing-side text) has no source record of its own
- **L7** Matrix cells 1↔4, 1↔5 (asymmetric per Doc_04) flattened to symmetric `associated-with` — defensible, no asymmetric type exists in the closed vocabulary
- **L8** `ijc.dw.f4-t-baptism-threshold.text` addresses "a modern asker" in third person inside compiled answer-ground — reads as describing the translation task rather than the world speaking

## What is right (stated so fixes don't damage it)
Every deliberately-empty canon_cells is correctly empty and reasoned in-body. Relation directionality clean across all 24 illustrated-by/illustrates pairs, zero backwards. Doc_04 matrix encoded faithfully at presence/absence level (10/10 present, 5/5 correctly absent); the one gravity-gravity tension-with is exactly the matrix's one Competing cell. Rights discipline genuinely fail-closed. Registry entry correct and well-evidenced against the live census.json. All 125 records world_id-consistent, status:draft, sensible registers. Retrieval blocks present on all 27 chunk-feeding records. The build log's self-description is honest, including flagging that a cold review was the natural next step — which this is.

## Fix ordering
1. H5 first (root cause of H1-H3) — run the missing cell-scoped searches.
2. H1, H2, H3 — correct the three false compiled assertions; decide per cell whether new material becomes coverage or narrows the limit.
3. H4 — F6-P needs a real witness or a real limit, not a stretched tag.
4. M1-M3, M8 — tag corrections and single-record-cell gaps.
5. M4-M7, L1-L8 — the rest.
