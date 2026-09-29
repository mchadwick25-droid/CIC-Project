---
name: cic-forces-index
description: Use whenever building, extending, or reviewing the Forces Document (Doc_08) for a "Church in Conversation" (CiC) formation world. Trigger on "build the forces analysis," "do the six-cell matrix," "Doc_08," initiating/ongoing/ending forces, transmission as a force, or forces-and-gravities synthesis. Also use when reviewing forces work against the indexing bar: a well-written six-cell matrix is not a complete Doc_08 if its cross-cell connections and gravity linkages can only be found by rereading the whole document.
---

# CiC Forces construction (Process V2.0)

The Forces Document (Doc_08) is a six-cell matrix, Initiating, Ongoing, and Ending crossed with External and Internal. Every force is documented at three layers (Historical Event, World's Own Experience, Formation Impact). Required synthesis sections connect forces to each other (Section 4, Cross-Cell Connections) and to every confirmed gravity from Doc_04 (Section 5, Forces-and-Gravities Synthesis).

This is relational data: which forces connect to which gravities and to which other forces, and at what confidence. Prose is the right form for the argument. But prose alone is slow to verify. The template's own completion checklist (Section 9) asks for checks like "every confirmed gravity connects to at least one force," which are slow to check by rereading and fast to check against a lookup.

Process: Sonnet 5.5 drafts. Opus 5.5 reviews, never the drafter, at high effort in round 1 and medium targeted rechecks after. Three rounds of substantial revision at most, then escalate to Mark. Run the gate layer before review: `python -m engine.m10.cli prereview <code> --doc N`, then `citations`, `claims`, `gaps`, `records` and `regate` on the world code, and `roundcount <code> N --check-new` before any new review file is written. See the `cic-build-cycle` skill. Use "Approved to proceed" only. Doc_08 is a forces integration point, so check the Forces Framework Section 4 entry for Step 8 before drafting.

## Build the six-cell matrix faithfully to the template

- All six cells populated: 1A/1B Initiating External/Internal, 2A/2B Ongoing External/Internal, 3A/3B Ending-or-Transforming External/Internal.
- Every force at all three layers.
- Layer 2 written strictly in the world's own vocabulary. No modern analytical framework imported.
- Transmission addressed as its own named force in both Cell 2B and Cell 3B, never folded into another entry.
- Depth proportional to formation impact (the Proportionality Principle). Not every force needs full treatment, but every force that does not gets a stated reason.
- Every quote re-verified verbatim against `cic/texts/`. Contested or thin claims carry the five-level `formation_confidence` tag.
- Apply the M4 lens spine (Completion Standard section F) where the standard calls for it.

## The index bar: connections must be lookupable

No workbook. Build these as tables inside Doc_08 and as generated views over the `force` and `gravity` records. They are derived from the same data as the prose, never a separate hand-kept list. The record store has no connection field, so the cross-cell connections live in Doc_08 (Process V2.0, Section 13).

- **Force table,** one row per force using the template's IDs (1A-1, 1A-2, 1B-1, and so on): Cell and Force Name; Confidence Level (matching what Layer 1 states); Connected Gravities by name (from Section 5); Cross-Cell Connections by force ID with direction (produces, intensifies, reacts to); Transmission-relevant yes/no, flagging the required 2B and 3B entries so they are never mistaken for optional.
- **By Confidence Level.** Every Contested and Inferential-Thin force together, so Section 7's confidence summary is checkable against the data.
- **By Connected Gravity,** inverted: one row per Doc_04 gravity listing every force that connects to it. A gravity with an empty row is what Section 9 calls "ecologically incomplete" and must show at a glance.
- **Cross-Cell Connection map.** Every Section 4 connection as a from/to pair.
- **Transmission Check.** A dedicated transmission entry exists in both 2B and 3B.

## What an independent review must check

- Does every force in the lookup appear in the prose matrix, and the reverse, with no drift?
- Does the by-Gravity view show every confirmed Doc_04 gravity with at least one connected force, and is any gap flagged and logged in `Open_Gaps_Tracking.md`?
- Are both transmission entries present as their own rows?
- Do the Cross-Cell Connections match Section 4 exactly, including direction?
- Does Layer 2 avoid modern analytical vocabulary? Spot-check several entries against the From-Within Principle.
- Does the review file carry the simulated-review label and the two-method truncation record?

A Forces Document that argues its connections well but has no lookup to check them against, or whose lookup does not match its prose, is not finished. Flag it on structural grounds.
