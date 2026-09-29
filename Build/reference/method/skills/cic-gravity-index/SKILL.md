---
name: cic-gravity-index
description: Use for Gravity Discovery (Doc_04, Construction Framework Part III) in a "Church in Conversation" (CiC) formation world. Trigger on "do Doc_04," "run gravity discovery," "test the candidate gravities," "six-test assessment," or Primary/Supporting/Tensional classification. Also use when reviewing gravity work: a well-argued classification is not a complete Doc_04 if a reviewer must reread the whole document to see how two candidates relate, or whether the Confidence/Gravity Cross-Check was applied to every Primary claim.
---

# CiC Gravity Discovery construction (Process V2.0)

Gravity Discovery (Construction Framework Part III, Doc_04) finds what a formation world actually organizes around, as distinct from topics that merely recur. Every candidate comes from traceable Source Ecology evidence, never general impression. It is tested against six named tests (Repetition, Dependency, Formation, Explanatory, Persistence, Interaction), cross-checked against the fixed five-level confidence vocabulary, tested for cross-strand status under Constitution Article 21, and classified Primary, Supporting, or Tensional.

Strength and evidence are separate properties. A candidate is not Primary unless its evidence independently reaches Documented, Widely Accepted, or substantially supported Dominant Modern Reconstruction. When the two diverge, the divergence is flagged and never resolved by upgrading.

This is a many-to-many structure. Every candidate stands in a stated relationship (reinforcing, competing, reshaping) to every other, and the Framework says a candidate with no traceable relationship to anything is a sign the list was built from impression. A document that argues each candidate in its own paragraph loses exactly that structure.

## Process and routing

Doc_04 is one of the two documents Fable drafts (the other is Doc_10). Opus 5.5 reviews, never the drafter: high effort in round 1, medium targeted rechecks in rounds 2 and 3, then escalate to Mark. No fourth round. Read the `cic-build-cycle` skill for the full cycle, and run the gate layer before review: `python -m engine.m10.cli prereview`, `citations`, `gaps`, `records`, `regate`. Use "Approved to proceed" only.

The structural template is `Build/reference/L3B-World-Build-Methodology/Doc_04_Gravity_Discovery_Template_V1.0.md`. Follow it. It fixes where each required check lives, not what the answer is. Before drafting, reread the current Construction Framework Part III directly (test names, classification thresholds) and the Forces Framework Step 4 entry. Do not work from a remembered version.

## Build the candidate list and testing from evidence

- Generate candidates only from elements recurring across several Doc_02 and/or Doc_03 evidence streams, or from documented patterns of attention-presence and attention-absence. Never from general familiarity.
- Flag any candidate visible mainly in one stream, or proposed by one major voice, as an Author Gravity risk at generation, not after testing.
- Record candidates considered and not advanced, with reasons. This section is required even if empty.
- Run all six tests on every candidate. Interaction means the relationship to every other candidate is specifically named as reinforcing, competing, or reshaping, not "coexists." Where the world has confirmed strands, score per strand where results diverge.
- Apply the Confidence/Gravity Cross-Check to every candidate heading toward Primary.
- Apply the Article 21 cross-strand test to every candidate. A gravity confirmed in one strand cannot be world-level Primary. A strand-singular world uses a declared, justified substitute.
- The Forces Framework separately requires a forces-connection notation for every confirmed gravity: how it held, shifted, intensified, or fractured under the forces already identified. This is the Step 4 integration point. It is not a seventh test. A blank here is a completion failure.
- Sourcing follows the corpus rules: every quote re-verified verbatim against `cic/texts/`; contested claims carry the five-level `formation_confidence` tag and a `contested_claim` record where warranted.

## The index bar: check without rereading

No workbook. Build these inside Doc_04 as tables, and in the record store as `gravity` records with generated views.

- **Classification Summary table** (required by the template), one row per tested candidate: Candidate, Six-Test verdict, Cross-Check result, Cross-Strand (or substitute) status, Classification.
- **Candidate table:** ID and name; Source Ecology streams; Author Gravity flag; result on each test per strand; evidential confidence level; cross-strand status; final classification (Primary, Supporting, Tensional, did not reach gravity status); Cross-Check outcome; forces-connection notation.
- **Interaction Matrix**, every candidate against every other: reinforcing, competing, reshaping, or no demonstrated relationship. A row that is entirely "no demonstrated relationship" must be visible as a thin row here, not buried in prose.
- **By Classification.** Primary, Supporting, and Tensional each in their own group, so the full Tensional set (the persistent counter-forces) is checkable as a set.
- **By Cross-Check flag.** Every candidate where strength and confidence diverge, so a reviewer can confirm each was flagged and not quietly resolved.
- **Cross-build sheet.** Where this world's gravities refer to, or are referred to by, a neighboring world's built material (as when a candidate's world-attribution was held open for this step): what was resolved, what remains open, and what action items this document creates for another world's maintainer. Open items go into `Open_Gaps_Tracking.md`.
- **Open Items Carried Forward** (required): everything the document could not close.

## What an independent review must check

- Was every candidate generated from named, traceable streams, with Author Gravity risk flagged at generation?
- Does the Interaction Matrix show a demonstrated relationship for every candidate that reached classification, or is one sitting with no connection to anything?
- Was the Cross-Check applied to every Primary, with any divergence named and not resolved by upgrading?
- Was Article 21 checked for every candidate, with no world-level Primary resting on single-strand evidence?
- Does every confirmed gravity have its forces-connection notation?
- If the document restates any claim from another document, does the wording match or is the difference disclosed?
- Does the review file carry the simulated-review label and the two-method truncation record?

A Doc_04 that argues well but gives a reviewer no single place to confirm every candidate got every check is not finished. Flag it on structural grounds.
