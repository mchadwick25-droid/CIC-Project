# CiC Voice Rebuild — Checkpoint 1B (Desert assembly-proof)

**Run:** 2026-08-08. Desert's assembler is the Blueprint's designated
canary: no other world's assembler is trusted before Desert's holds. This
checkpoint re-checks both halves of Phase 1B's stated pass bar against
live data, not memory.

## The Blueprint's exact pass bar

> assembled Desert prompt remains byte-identical to deployed (machinery
> didn't drift it); his 8-turn battery re-run holds at his Research-stage
> profile (0/8 failure measures). On fail: the segment design iterates
> until Desert holds; no other world's assembler is trusted before
> Desert's is.

## Verdict: PASS on both halves.

## 1. Byte-identity

Re-run live this session: `python3 assembly_identity.py` →
`[assembly-identity] Desert: PASS - byte-identical to deployed`. Nothing
has touched Desert's records or assembler since Checkpoint 0 confirmed
the same result minutes earlier in this session, so this is confirmation,
not a new finding.

## 2. The 8-turn battery re-run against Research's original three failure measures

Research's baseline (`CiC_VoiceRebuild_Stage1_Research_Findings_2026-08-08.md:543-561`)
defines Papnoute's "0 of 8" as zero instances, across all eight turns, of:
**term-first openers**, **reclarification openers**, and **false
referents** — plus register holding under the FK floor on every turn.

This session's already-committed six-world baseline probe
(`voice_rebuild_research_probe_results.json`, commit `6cb943e`) ran
Desert's identical 8-turn battery through the now-fully-generalized Phase
0 assembly machinery. Checked against Research's three measures:

| Measure | Automated signal | Manual read | Result |
|---|---|---|---|
| Term-first openers | `technical_term_in_first_sentence=False` on all 8 turns | Confirmed — every turn opens on plain narration, not a term (e.g. turn 3: "Not sorrow that ends in itself. We called it penthos..." — the term lands second sentence) | 0/8 |
| Reclarification openers | `reclarify_opener_patterns=[]` on all 8 turns | Confirmed — no turn opens re-stating or re-framing the question back | 0/8 |
| False referents | not automated (Research's own note: the regex "scored 0/8 where manual read found 1/8" at Research stage — regex is a floor only, manual read is mandatory) | Full transcript read turn-by-turn: turn 5 attributes the cracked-jar story correctly to "Abba Moses," never claimed as Papnoute's own; turn 9 explicitly refuses to fabricate a failure-story the participant invited ("Our record does not give us that story whole... I will not build you the second out of the first"); turn 13's "boy at the cell" story is framed as received tradition ("in every telling we keep"), not invented and not misattributed | 0/8 |

**Register held on every turn:** FK 1.88–7.31 (all eight comfortably under
the project floor), matching Research's original 1.4–6.7 range closely
enough to call the same profile — the small widening is consistent with
a different 8-question set, not a regression. FRE 77.95–98.29.

**No-fabrication discipline held as naturalness, not against it** — the
same pattern Research flagged as the system working correctly at turn 7
of the original run reappears here at turn 9 (declining to invent a
monk's-collapse story) and turn 13 (framing the boy story as received
telling rather than fresh invention), both unprompted refusals delivered
in Papnoute's own voice rather than as visible apparatus.

**Length ceiling: ~~zero retries fired~~ — CORRECTED 2026-08-08, this
claim was wrong.** The original text read: *"zero retries fired
(`total_ceilinged_turns: 0`) — no turn approached Papnoute's 60-word
ceiling closely enough to trigger regeneration."* That inference is
false. The instrument read zero because **the length-ceiling mechanism
does not exist in the code path the probe used**, not because no turn
tripped it. In fact **all 8 of Papnoute's turns exceeded his 60-word
ceiling** (max 170 words, 2.8×), and all 8 sat above the 1.5× retry
trigger. See
`CiC_VoiceRebuild_CeilingPathFinding_2026-08-08.md` for the full finding.

**This does not change 1B's verdict.** The pass bar is Research's three
failure measures (term-first openers, reclarification openers, false
referents) plus byte-identity — none of which depend on the ceiling
instrument, and all of which were verified from the transcript text
itself. Research's own Papnoute baseline likewise recorded turns of
"42–187 words" against the same 60-word ceiling, so the baseline and
this re-run are at least measuring the same (unenforced) condition. What
the correction removes is a supporting claim that was never part of the
bar and that I stated with more confidence than the data supported.

## What's explicitly NOT counted here

`over_settling` (screened=8, confirmed=2, rate=0.25) is a Phase 0.4
instrument that did not exist at Research stage — it is not one of
Research's three failure measures and is not compared against the
original "0/8." It's logged for its own sake (a slightly lower rate than
Research's `over_settling_adjudication` 3/8, for what that's worth), not
scored against this checkpoint's pass bar.

## Bottom line

Desert holds. Byte-identity confirmed live; the 8-turn re-run scores 0/8
on all three of Research's original failure measures via both the
automated signals and a full manual transcript read (the latter required
per Research's own documented caution that the regex alone under-counts).
The canary passes — Phase 2's per-world passes may proceed once their own
turn arrives, in the risk order already set (Albina → Marius → Theon →
Papnoute → Chloe → Yausep), without re-litigating Desert's machinery.
