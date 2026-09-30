---
name: cic-story-repository
description: Use whenever building, extending, or reviewing the Story Inventory or Story Repository (Doc_09) for a "Church in Conversation" (CiC) formation world. Trigger on "build the stories," "do the story inventory," "Doc_09," "story repository," narrative tiers, hagiographic material, or deployment story chunks. Also use when reviewing story work against the indexing bar: well-tiered stories are not a complete Doc_09 if a reviewer cannot confirm every story has a real tier justification, the Absent Stories question was answered, and nothing slipped in as invented narrative.
---

# CiC Story Repository construction (Process V2.0)

Doc_09 classifies every story a world can tell into one of four tiers, with a hard rule that there is no fifth: generated or invented narrative is never permitted, however well it would fit the voice. Each story needs a specific source, a tier justification, and usage guidance (remembered history, community tradition, formation-ideal account, or typical practice; confirm the current categories from the governing document). The deliverable also answers the "Absent Stories" question: what stories this world conspicuously lacks, in the way Article 20 already requires naming absent voices.

Before building, reread the current Blueprint and Construction Framework Doc_09 section. Do not rely on a remembered tier list.

Process: Sonnet 5.5 drafts. Opus 5.5 reviews, never the drafter, at high effort in round 1 and medium targeted rechecks after. Three review files at most (every review, recheck or spot-check file counts), then escalate to Mark. Run the gate layer before review: `python -m engine.m10.cli prereview <code> --doc N`, then `citations`, `claims`, `gaps`, `records` and `regate` on the world code, and `roundcount <code> N --check-new` before any new review file is written. See the `cic-build-cycle` skill. Use "Approved to proceed" only. Doc_09 sits before the Representative identity decision; that decision goes to Mark in the grounded-options format.

## Build each story faithfully to its tier

- Name the specific source. Re-verify every quote verbatim against `cic/texts/`.
- State the tier and why. A hagiographic account is not automatically Tier 3. Check what the governing document says distinguishes the tiers.
- State usage guidance, so a downstream builder knows what claim the story is licensed to support.
- No invented family, age, personal history, or anecdote. A detail not derivable from the sources does not belong.
- A composite carries its own element-to-source table. Outsider witnesses own their accounts. Boundary figures are declared.
- Stories are `story` records. Deployment chunks are generated from them, in the same shape as lexicon chunks (tier, retrieve-when, `prefer_instead` for redirects, `claim_guards` for claims the voice must never make). `tellable_as` text is plain: longest sentence 30 words or fewer, median 25 or fewer.
- A story used in a demonstration must be told: a real scene, real stakes, one concrete detail. It must not be summarized into a proposition with the story's name attached.

## The index bar: verify tier discipline without reading everything

No workbook. Build these as tables in the document and as generated views over the `story` records.

- **Story table,** one row per story: ID or slug, Tier, Source, Usage Guidance category, Retrieve-When, `prefer_instead` (for redirects), Confidence Level if the governing document ties one to tiers.
- **By Tier.** Every Tier 4 (Historically Grounded Reconstruction) story together. These carry the most inferential weight and deserve the most scrutiny.
- **No-Tier-5 audit.** Every story checked against the four permitted tiers. Anything that does not clearly fit is flagged, not left unclassified.
- **Source cross-reference.** Each story's source checked against the world's Source Registry, confirming it is Native to this world and not borrowed from a neighboring tradition.
- **Absent Stories check.** The required question answered with something substantive. This is the item most likely skipped under deadline pressure, because it is the one that adds no content. Every unresolved item goes into `Open_Gaps_Tracking.md`. The answer also feeds `facilitator_brief.formation_limitations`, which names whose voices the sources structurally omit (Constitution Article 20).

## What an independent review must check

- Does every story have a tier justification that engages the governing document's distinguishing criteria, not just a number?
- Does any story read as invented or composited rather than sourced?
- Is Absent Stories answered with specificity (what is missing and why), not "more stories could be added"?
- Do cited sources appear as Native entries in this world's Registry, with no uncaught cross-world borrowing?
- Does the review file carry the simulated-review label and the two-method truncation record?

A repository that reads well but has no way to verify tier discipline, or whose Absent Stories answer is a placeholder, is not finished. Flag it on structural grounds.
