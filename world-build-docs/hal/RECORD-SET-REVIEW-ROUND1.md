# hal Record Set — Independent Adversarial Review, Round 1

**Reviewed:** the complete records/hal/ record set (139 records), branch world/hal, 2026-08-21.
**Reviewer:** fresh Agent invocation, no drafting context, full read access to the vendored texts, the cleared prior-build documents, and the record set itself.
**Verdict: Targeted fixes.** No gravity classification, force placement, story tier, or contested-claim resolution requires re-deriving. Two fabrication-adjacent findings (S1/S2/S3) and a tail of minor/cosmetic drift.

---

## [S] Substantial findings

**[S1] hal.figure.rufinus — wrong date and wrong "naming" claim for the Peri Archon preface.**
Record said the preface (400) named Jerome as Origen's admirer. Correct: the preface dates to 398, and it describes Jerome without naming him (the NPNF editor's own headnote says "clearly described," not named) — matching the record set's own `hal.story.rufinus-rupture` ("named no one, and everyone knew he meant Jerome"). Internal contradiction on a checkable fact.

**[S2] hal.force.origenist-controversy — same "naming" error**, in the manifestations list.

**[S3] Invented quotation-marked strings not in the source, in two records.**
`hal.source.attack-letters-416` and `hal.force.pelagian-attack` both put "my own monastery has been destroyed" in quotation marks as Jerome's wording; that exact string is not in Ep. 138 or 139. (The proper quote record, `hal.quote.house-destroyed`, is correct and verbatim.) By this corpus's own fabricated-gloss precedent (Ep. 77.6), a quoted string not in the source is a defect even when substantively faithful.

## [M] Minor findings

- **[M1]** Off-by-one section number: `hal.quote.partially-acquired-hebrew` and `hal.quote.paula-hebrew-psalms` cite Ep. 108 "sec. 26"; the passage falls at §27 against the cited edition.
- **[M2]** Dangling cross-reference in `hal.term.monachus`: `hal.limit.f5-unnamed-residents` does not exist.
- **[M3]** `hal.dw.f3-t-one-church` locus misattributes "a man truly Catholic" to Dialogue I ch. VIII; it's ch. VII (only the parish-under-Jerusalem line is ch. VIII).
- **[M4]** `hal.dw.f4-t-practices` uses an image ("the head of the empire cut off") from the Ezekiel preface but doesn't cite `hal.source.vulgate-prefaces`.
- **[M5]** `hal.dw.f4-e-apostolic` verifies an Ep. 127 line in its body but doesn't list `hal.source.jerome-ep127` in sources[].
- **[M6]** `hal.story.marcella-death` imports "which the conquerors had made a place of refuge" from the Orosius/Augustine tradition, not from Ep. 127 (the sole cited source), which says only "that you might find there either a place of safety... or a tomb."
- **[M7]** `hal.story.attack-416` and `hal.quote.innocent-ravages` phrase Ep. 137 as an answer "to them"/"his answer" when it addresses John of Jerusalem, not the women.

## [C] Cosmetic

- **[C1]** `hal.quote.city-taken` says "two editorial footnote insertions elided"; there is one.
- **[C2]** `hal.quote.hindered-by-jerome` has an undisclosed footnote-number artifact ("Paula,276") in the source text not mentioned as elided.
- **[C3]** `hal.core.hieronymian` caution 6 says "the vendored Jerome volume" — build-infrastructure wording inside a compiled field.
- **[C4]** Apology dating given as "401-402" vs the cleared Doc_02's "401-403" — a harmless divergence toward standard scholarship.
- **[C5]** `hal.quote.helmeted-preface` body gloss conflates the F2-T and F2-I canon question texts.

## What was checked and came back clean

Quote fidelity (all 19 `quote` records plus 12 body-level quoted snippets, verified programmatically against the vendored texts); gravity classifications vs. Doc_04 (exact match, no upgrades, no invented tension-with); forces vs. Doc_08 (12/12 cells, both Round-corrected placements intact, the one disclosed residual index drift confirmed real in Doc_08 itself); story tiers vs. Doc_09a (12/12, no Tier 5); every contested item (Hebrew fluency, Ep. 46 authorship, Marcella agency, Origenist substance, Paula totality, Paula-Jerome relationship, all contested dates) carried open everywhere, none asserted as fact; hospital/hospice discipline (no conflation); 24 spot-checked file loci exact; the Marcella-letter enumeration exact; compiled-field discipline (one hit: C3); canon_cells sanity (~20 checked, no systematic over/under-tagging beyond C5); fabrication hunt beyond S1-S3/M6 found nothing untraceable.

## Disposition

All eight findings (S1-S3, M1-M7 minus M7 folded with M6's fix, C1-C5) were fixed directly on this branch following this review — see the commit that follows this file. Cosmetic/minor: applied directly, no further review round per protocol. The two substantial findings (S1/S2 naming error; S3 pseudo-quotes) were corrected and the fixed text re-verified against the vendored files before commit, not merely relabeled.
