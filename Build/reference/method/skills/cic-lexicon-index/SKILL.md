---
name: cic-lexicon-index
description: Use whenever building, extending, or reviewing the Interpretive Lexicon or Deployment Lexicon for a "Church in Conversation" (CiC) formation world. Trigger on "build the glossary," "do the lexicon," "vocabulary list," "deployment lexicon chunks," Step 3, Doc_03, Doc_06, or the world's terms. Also use when reviewing lexicon work against the indexing bar: per-term files are not a complete lexicon if a builder or reviewer cannot filter by tier, tag, or risk flag without opening every file.
---

# CiC Lexicon construction (Process V2.0)

Each term in a world's lexicon is one `term` record, and its deployment chunk is generated from that record. The record carries real structure: Term, World-Code, Tier (1/2/3), Tags (AS Signature Vocabulary, SC Shared Vocabulary, DR High Distortion Risk, TC Technical Concept, RT Likely Runtime Term, PV Plural Voices, CT Contested Tradition), Aliases, Related-Terms, Retrieve-When, and for redirects `prefer_instead`, with `claim_guards` for claims the voice must never make.

That structure is good. The job of this skill is to make questions like "which CT terms have their Contest Type filled in" and "which terms cite only one dominant source" answerable without opening every file.

Read `CiC_Record_Native_World_Build_Process_V2.0` and the `cic-build-cycle` skill first. Drafting is Sonnet 5.5. Review is Opus 5.5, never the drafter, at high effort in round 1 and medium targeted rechecks after, with a hard cap of three review files (every review, recheck or spot-check file counts) and then escalation to Mark. Gate-layer commands run before review: `python -m engine.m10.cli prereview <code> --doc N`, then `citations`, `claims`, `gaps`, `records` and `regate` on the world code, and `roundcount <code> N --check-new` before any new review file is written. Say "Approved to proceed," never any other closing word. Zero fabrication.

## Build each term faithfully to the template

Follow the Deployment Lexicon Chunk Template exactly. Candidate terms come from the Source Registry's Native rows, never from raw Doc_02, because Doc_02 can still name excluded sources.

- **Quick Meaning.** One runtime-facing sentence.
- **World Meaning.** Level 2 depth, written from inside the world's own ecology. No analytical-distance markers such as "scholars believe" or "the sources indicate."
- **Ecological Function.** What else depends on the term.
- **Distortion Risk.** Modern Hearing versus World Hearing, as two contrasting lines, never blended.
- **Key Sources.** Tier 1 and 2 only, cited specifically, with an Author Gravity risk note where one source dominates. Every quote is re-verified verbatim against the vendored source in `cic/texts/`.
- **CT Contest Type.** Only if the CT tag applies. If it applies, the section is not optional: state which of the four contest types applies and describe the actual contest.
- **Reported-Experience Status.** Only where the meaning is historically uncertain but formationally central.

Every term on a record's `anachronistic_term_ids` needs a modern-sense gloss for its hover card. The Representative never defines the modern word in a spoken turn. Name another tradition in a record only where this world's own sources do.

Run the alias-safety preflight (Rules A/B) when aliases are first authored, so no retrofit is needed later. Any modern-English rendering is authored by Opus 5.5 and checked in a separate Opus pass.

## The index bar: lookup without opening every file

There is no workbook and no hand-kept master list. The index is derived from the same records the chunks come from, as generated views or as a plain markdown or yaml lookup file in the world's build folder that is rebuilt from the records, never edited by hand. It must let a reader filter on:

- **Per term:** Term, World-Code, Tier, each tag as its own yes/no field (never one comma-separated cell), Aliases, Related-Terms, Source-Registry cross-reference (which Registry entries the Key Sources match, once a Registry exists), and Author-Gravity-Risk (yes/no, taken from whether Key Sources flags single-source dominance).
- **By Tier.** Tier 1 (full ecological treatment) distinguishable at a glance from Tier 3 (Quick Meaning only).
- **By Tag.** Every CT term together, every DR term together, and so on. This answers "show me every contested term" in seconds.
- **CT Contest Type check.** Every CT-tagged term beside whether its Contest Type section is actually filled in. This is the most common gap, because the tag is applied more often than the contest is specified. Complete this audit before Doc_06 clears review.
- **Related-Terms reciprocity.** If A lists B, B should generally list A. Flag any one-way link. Do not leave it silently one-directional.

## What an independent review must check

- Is the index derived from the same records as the chunks, not a separately kept list that has drifted?
- Does every CT-tagged term have its Contest Type section actually completed?
- Does every World Meaning read from inside the world, with no analytical-distance markers?
- Are Related-Terms links checked for reciprocity, with one-way links flagged?
- Does Author-Gravity-Risk in the index match each term's Key Sources note, and is it never blank by default?
- Does the review file carry the simulated-review label and the two-method truncation record?

A lexicon that reads well term by term but has no queryable index, or an index out of sync with the records, is not finished. Flag it on structural grounds even when the entries are good.
