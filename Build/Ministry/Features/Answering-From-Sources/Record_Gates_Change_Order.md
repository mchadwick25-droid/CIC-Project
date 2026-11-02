# Record gates change order: a quote's text at its cited locus, and a review file for every rendering

Named change order. Mark's choice (choice box, 2026-11-01, relayed by the coordination thread): the two mechanical defect checks become engine gates for the record stage; hedges and years stay writing rules checked by the independent reader. No new passes beyond these two. Decision-Log entry 62 records the choice.

## What changes

Two gates join `engine.m1.gates.GATES`. Each is a machine check with no model call, written in the `gate_*(records, fleet, registry) -> list[str]` shape of every other gate.

1. `quote-locus` (`engine/m1/quote_locus.py`). A verbatim quote whose locus names a vendored span (`cic/texts/<file>, lines N-M`, read by `engine.prose.locus_refs`) must have its `text` occur inside one of its cited spans. The match is the fixed grammar `quote_verbatim.verify_quote_text` already applies (whitespace, case, punctuation variants, ellipsis, bracketed insertions, verse numbers, apparatus), run on the span alone, with the translator's-note fallback the verbatim gate uses. A quote cited at two spans (an English and a Latin edition) passes when any one holds the text. A span that does not resolve to lines of a vendored file is a finding.
2. `rendering-review` (`engine/m1/rendering_review.py`). A record carrying a `modern_rendering` passes only when a rendering review log in its world's `Review-Artifacts/` folder (`Rendering_Review_Log*.md`, the format of `Build/worlds/lpc/Review-Artifacts/Rendering_Review_Log_86_2026-11-01.md`) has a row naming the record, and at least one review file that row names exists in that folder, mentions Opus, and mentions the record. A fixture world is skipped.

## Why

`quote-verbatim` asks whether a quote's words occur anywhere in the file its edition names. A card links to the cited span, so the span has to be the place the words are. The earlier work found four lpc quotes whose locus names only the first line of a passage that runs on. The rendering log exists for lpc so that "reviewed" can be checked one record at a time; the gate keeps it checkable and makes the other worlds meet it.

## Fleet check, before registering

Run on all 13 built worlds (the 12 built worlds and the `fix` fixture):

| World | quote-locus findings | verbatim quotes with no span (not checked) | rendering-review findings |
|---|---|---|---|
| alx | 0 | 26 | 26 |
| cappadocian | 0 | 21 | 21 |
| desert | 1 | 57 | 61 |
| don | 0 | 5 | 5 |
| fix | 0 | 2 | 0 (fixture, skipped) |
| gallic | 0 | 110 | 110 |
| hal | 0 | 32 | 32 |
| ijc | 0 | 39 | 39 |
| lpc | 4 | 0 | 0 |
| pahc | 0 | 25 | 25 |
| rzg | 0 | 6 | 6 |
| syr | 0 | 34 | 34 |
| witt | 0 | 7 | 13 |

Each current failure is registered as a dated `ACCEPTED_OPEN` waiver in `engine/m9/enforce.py`, with an owner, as the repo rules require:

- `m1:quote-locus/lpc` (4, deadline 2026-12-14, `approved_by` the project lead, since lpc is not grandfathered): `bishop-of-bishops`, `ancient-venom-against-my-episcopate` and two more cite one line of a passage that runs on. Library widens each span.
- `m1:quote-locus/desert` (1, deadline 2026-12-14): `arsenius-flee-tace-quiesce` is not on its cited line of the Budge edition.
- `m1:rendering-review/<world>` for the 11 worlds above (counts as in the table, deadline 2027-03-15): each world's build thread writes the per-rendering review log, as Library did for lpc.

## What the gate does not reach

A verbatim quote whose locus names no span cannot be checked here. Outside lpc, desert and witt that is every quote (the third column above, 364 quotes). Registering the missing spans is Library work and a separate decision: it would turn those quotes into findings, so it is put to Mark, not done here.

## Restage

Registering a gate changes `validation/gates-report.json`, which is baked into every pinned package. Every world's package is rebuilt and re-pinned in the pull request (13 worlds). No record, no card and no spoken text changes.

## Keeps transparency

Nothing a participant reads changes. The gates run at the record stage only.

## Authority

Mark's choice of 2026-11-01 (above), relayed by the coordination thread. The gate shapes and the waiver deadlines are the engine thread's reading of it and are open to change.
