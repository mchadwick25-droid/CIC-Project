# Adversarial review: `CiC_System_Redesign_Pass1_Design_2026-07-26.md`

*Opus review, dispatched 2026-07-26 — the first adversarial pass on Fable's actual Pass 1 design output, not the brief. This is the most consequential artifact in the arc so far: Pass 2 (the build blueprint) starts from whatever survives this review. Verification method matches `Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md` — every load-bearing claim checked against its actual primary source (code, governance documents, transcripts, research docs), not trusted from the design document's own "verified" labels.*

**Process note, added after the fact:** this document was edited in place to mark its own findings "fixed" rather than left as a verbatim, closed record with fix-status tracked separately — a departure from the pattern used successfully on the brief's reviews (docs 18, 19), and the resulting lack of a pre-fix version made the fix pass harder to check. `21_Opus_Adversarial_Review_of_Pass1_Design_Round2.md` verified the fix pass this document's findings prompted, found the fix pass itself introduced two new errors (one of them the exact "record data with no record type" and "invented citation label" class of thing this project's review process exists to catch), and is preserved as its own separate, unedited document for exactly this reason. Read doc 21 for the full account of what that check found and fixed.

## Bottom line

**Fix three things first, then it's worth Mark's full review time.** This is a strong document — materially stronger than the brief was at the equivalent stage. The reviewer re-derived every load-bearing number reachable, opened every code file the design claims to have verified, and spot-checked 18 of Appendix B's ~25 governance defects against the actual source: **15 true, 3 partly true, 0 false.** It also silently *corrected* an error the brief carried (the reading floor is RCF Part Five, not Part Four). Its confidence discipline is genuine, not decorative.

But it had three real errors, two of which changed a recommendation rather than just a sentence. All three, plus all twelve P1 findings, were applied directly to the design document the same day — see the Decision Log's 2026-07-26 entry for what changed and why.

---

## P0 — fixed 2026-07-26

**1. Desert's Quick Meanings exist. All nine of them.** The document said, in six places (including its own "verified claims" table), that Desert never authored them. False — Desert uses a bold inline label (`**Quick Meaning:**`) instead of the `## Quick Meaning` heading the other worlds use, a format the original per-world audit's own search missed. All 104 chunks have Quick Meaning authored; the parser drop is format-dependent (80 of 104, four fenced-front-matter worlds), not an authoring gap. The irony: the design document correctly diagnosed the parser's format-dependence, then made the identical format-dependent mistake one paragraph later checking whether the content existed at all. Downstream: this removed one of three legs under §12's Desert-migration argument, corrected in place.

**2. Source Registry rows never enter the generation context — the citation chip is where they go.** The design claimed five registry rows (including "verified against publisher page" language) were serialized into a real transcript's generation context twice. Traced through `retriever.py` and `nodes.py`: resolved registry rows attach only to the participant-facing citation payload, never merge back into the prompt. What actually leaks is a different, smaller thing — the chunk's own `## Key Sources` section (~275 tokens), confirmed repeated verbatim in the real transcript's turns 5 and 7. The design decision (stop injecting this into voice materials) is still right; the evidence and the claimed cost saving were both overstated.

**3. Job 7 (anachronism boundary) had no actual schema.** The record types it depends on (`world_core`, `modern_term`) were named in the schema's own enum and used throughout the document's prose, but never given field tables — against the brief's own explicit bar ("concrete field-level specification tables where a schema is being defined"). Closed by adding full field-table subsections for both, plus moving `search_record`'s spec (previously only in prose in §4.3) into the schema section proper, plus converting `quote`, `voice_profile`, and `demonstration` from prose to tables.

---

## P1 — fixed 2026-07-26

1. **"Facilitator Governance §8 Rule 1" is a citation label that doesn't exist.** FG §8 is four prose paragraphs, not numbered rules — and §9.3 called it "Rule 1a," which in the cited research means a *different* rule set (Sacks/Schegloff/Jefferson 1974) entirely. Fixed to cite the actual sentence, not an invented rule number.
2. **"RCF Part Eight's nine probe categories" — it's eight.** Nine is the Construction Notes Template's count; the document's own Appendix B already said as much elsewhere, so this was a self-contradiction. Fixed.
3. **`must_not_retrieve` vs `do_not_retrieve_when`** — same field, two names in different sections. Unified on the one actually defined in the schema.
4. **`Jobs (§6)` collided with the design's own §6** (Facilitator governance) when it meant §2 (this document's own eight-jobs table). Fixed at all three sites.
5. **"§9's four-field block" meant §3.2** (the design's own §9 is the transcript pressure test, inherited unedited from the brief's numbering). Fixed.
6. **`voice_surface` was claimed on quote records that don't have it.** Fixed to name what quote records actually use for voice licensing (`text_translation` + `license`).
7. **The confirmed-gloss list was promised as "record data" three times with no record type behind it.** Given a concrete, minimal specification (Facilitator-owned keyed list, not a full schema record type) rather than left as an implied schema that didn't exist.
8. **Four relation fields with no stated relationship** (`relations[]`, `field_relations[]`, `interaction[]`, `connections[]`) — clarified as one envelope concept with per-record-type implementations, and named all four explicitly in the reciprocity gate, which previously covered only two of them.
9. **§10's objective-1 mapping cited the un-generalized half** of the brief's actual ask (which is about generalizing the registry pattern, not just the registry itself). Fixed to include the sections that actually do the generalizing.
10. **R7 (the quick-reach layer) — the document's own headline change — was missing from its own ordered retrieval plan.** Added, with doc 15's parroting-metric contingency preserved.
11. **§7's "untouched" claim on the safety pipeline didn't survive §6.6's own change** (Facilitator crisis-intercept turns entering the public transcript). Reconciled — the mechanism stays untouched; what's now stated plainly is what changes around it.
12. **A seventh and eighth judgment call were stated as decided rather than flagged for Mark**, when the document's own §12 already reserves this category for exactly this kind of call: retiring `MIN_MULTI_WORLD_TURNS` as a hard per-round floor (the single largest change to what a participant experiences at a multi-world table), and adopting/expanding the lens spine in §4.1. Both added to §12.

---

## P2 — open, genuinely optional

Not applied. Full list in the review agent's original output, preserved in the Decision Log's 2026-07-26 entry: a mis-quoted phrase ("verified" vs "confirmed directly"), a cost-figure comparison across unlike quantities (lexicon-only vs. lexicon-plus-story words), a warrant for §6.6 that could cite FG §7 directly instead of arguing from inference, a doc 15 caveat about Sonnet 5's minimum cacheable prefix not yet carried into Pass 2 territory, the `anything_else` closing-turn defect being a regression rather than a never-built gap, a hardcoded-string count off by one, an Appendix B "disagree" that's actually a one-sided gap, a few more field-definition/usage mismatches, and a flag on §5.4's R0–R9 sequence as the closest thing in the document to a build sequence (defensible — inherited from doc 15's own prioritized list — but worth checking against the stop rule).

---

## What was verified and holds — worth stating, since this is mostly what the review found

**Code (confirmed directly):** `MIN_MULTI_WORLD_TURNS = 2` and its `must_continue` interlock; `build_public_transcript` skipping `facilitator` and returning the last 10 lines; `determine_turn_type` with "prefer single" called only from the non-streaming endpoint; zero readability implementation anywhere in the backend; five Desert files with `Do-Not-Retrieve-When: —`; three of six worlds uniformly Tier 1; the five-world ceiling capped at 3 in code; the audit endpoint unauthenticated and in-memory; the `anything_else` closing turn unreachable; `pending_guidance` as a last-writer-wins single slot; all 17 drift signals decomposing exactly as claimed; the retrieval batch-dilution failure fought three times in-code.

**Governance:** the Constitution file headed Version 2.3; FG §8 quoted verbatim; the V3.6→V3.7 diff confirmed as §10-only; §12's near-silent-room line verbatim; the five-world ceiling's own admission that no mechanism enforces it; Article 17's delegation clause and its pending-update footnote; Article 30 carrying no numeric reading-level floor.

**Research figures:** the retrieval cost figures verbatim from doc 15; the p<0.001 turn-selection result against both cited baselines; the ~86% restricted-offer figure; the LLM next-speaker F1 comparison; Character.AI's ~95% cache-hit figure; doc 10's genuine refutation of the latency-as-naturalness-driver claim; the verb-shaped/noun-shaped Ecological Function finding (Desert 9/9 vs. HAL 3/9).

**Transcripts, all three, in detail:** the three-world safety-script table (Facilitator-only intercept, PASS); Cross-World Roundtable PART II's two real reviewer-flagged defects (Kimon's "the schoolmen," Eumathios's unearned closing synthesis) and one genuine positive (Kimon→Cordus adjacency); the real two-world runtime session's exact turn order and repeated Key Sources block.
