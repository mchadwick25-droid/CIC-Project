# Targeted re-check #3 (post-`ff0784bb` fix commit): `CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md`

*Opus targeted re-check, dispatched 2026-08-07. Not a sixth full round — scoped to the single commit that has landed since targeted re-check #2 and has never been reviewed: `ff0784bb` ("Apply second targeted re-check's fixes"). Rounds 1–5, targeted re-check #1 and targeted re-check #2 read first, per the Standard Practice's point 4; `18c4830e` (Mark's own P0-2 resolution) and `b6959d04` (the Section 4 split) re-read in full diff so the fixes could be judged against what they were supposed to restore, not against `ff0784bb`'s own account of itself. The rest of the document was deliberately not re-reviewed.*

*Verification method, per points 1 and 3: each of the three named fixes re-derived from the current file rather than from the commit message. The relocated `permanent_prompt.py`/`probe_parity.py` paragraph diffed word-by-word (`difflib`) against its pre-commit text and cross-checked against what rounds 4/5 and targeted re-check #1 independently established about that file. The whole document grepped fresh for every protection phrasing the last three passes were chasing — `not a candidate for dropping`, `completely out of scope`, `non-negotiable`, `under any framing`, `untouchable`, `off limits`, `word for word`, `preserv*`, `protected`, `exempt`, `must`/`has to`, `as-is`, `not optional` — 20 patterns, every hit read in context. Pointer counts, token counts, balance ratio and long-sentence duplication recomputed on pre- and post-commit copies. Diff sized: **67 insertions, 52 deletions** across the brief and the launch prompt; no other file touched.*

---

## Bottom line

**All three named fixes are clean. The document no longer contains a single surviving mechanism-level protection — I checked exhaustively, and that class of defect, which has consumed the last three passes, is closed. But the commit also made a *fourth* change nobody asked me to derive from a prior finding — the new §4.2 scope-clarification paragraph — and that paragraph carries four P1s, including an orphaned self-reference to a phrase the same commit deleted.**

Stated as plainly as the Standard Practice's point 6 requires:

1. **Fix 1 (§7 Part A's license) — clean.** Fabrication-rate tracking's specific implementation is now named inside the "open, goal-fixed" enumeration with an accurate parenthetical (*"the goal it verifies is fixed; the mechanism is not"*), and the sentence that contradicted it is gone. Nothing anywhere in the brief now calls fabrication-rate tracking, or any other named mechanism, an exception. The only surviving *"under any framing"* (line 179) is attached to the **goal** (no fabrication), which is exactly right.
2. **Fix 2 (§5's `fabrication_adjudication`) — clean.** The new wording resolves correctly against both cited targets, and it now describes the check the way §6 Objective 4 does — as an instrument verifying a fixed goal, not as a protected thing in itself.
3. **Fix 3 (the relocated paragraph) — clean, and better than it needed to be.** Every fact survives byte-identical: staging path, Desert hardcoding, `DELIBERATELY TEMPORARY` on the other five, the four-of-six parity failure, and the "right thing to build from / not yet what the system runs on" pair. The relocation also silently repaired a broken code span (`` `wrs/ views/permanent_prompt.py` ``, mid-backtick line break) that would have rendered literally. The repaired sentence is grammatically sound. The relocation introduced no new grammatical seam.
4. **Fix 4 (the new §4.2 intro paragraph) — not clean.** This is the one place in the diff where the assistant wrote fresh assertions rather than restoring or correcting existing ones, and it is — for the third commit running — exactly where the document breaks. Its first sentence points at a license "below" by quoting a phrase (*"none of it is a limit"*) that **this same commit deleted**; it mislabels one of the two defect bullets in a way a prior round already flagged as stale; and it makes §4 contradict its own preamble two paragraphs above.

**The pattern, stated for the record.** Targeted re-check #1's rule was "deletions and re-points hold; new positive assertions don't." Re-check #2 added "a pure reorganization is safe for facts and unsafe for scope." This commit confirms both and adds nothing new: the three restorations and corrections held perfectly; the one paragraph of new prose did not. **Four fix commits, four times the same split.**

**Is the document ready to send to Fable?** Effectively yes, and I am not softening that because it is the eighth pass. **No P0 survives anywhere I looked.** By the Standard Practice's own vocabulary, P1 is "materially improves the result but isn't disqualifying" — so the honest verdict is: **the brief is sendable, and it should not be sent until §4.2's intro paragraph gets one rewrite, because that rewrite is four sentences and costs nothing.** One item genuinely remains open and is not a review's to close (P1-4, "A Turn Has a Measure"). It is Mark's decision, it can be answered inside the Fable thread rather than blocking the send, and it should be named to Fable as open rather than left reading as decided.

**A fourth targeted re-check is not warranted.** Whoever writes the §4.2 replacement paragraph should re-read it once against §4:171–174 and §4.2:328–346 before committing. That is proportionate.

---

## Findings

### P1-1. The new §4.2 paragraph's first sentence quotes a license "below" that this same commit deleted. Orphaned reference, in the opening line of the fix.

> **§4.2, lines 206–207:** *"Two different kinds of bullets follow, and the **"none of it is a limit"** license below applies to only one of them."*

The phrase `none of it is a limit` **does not appear anywhere below line 206** — or anywhere in the document. It was `b6959d04`'s wording (*"**None of it is a limit.** Rewrite, replace, simplify, or drop any of it"*), and `ff0784bb` replaced it with *"those are genuinely open: **rewrite, replace, simplify, or drop any of them...**"* in the very next sentence. Verified by whole-file grep: `not a limit` → zero hits; `none of it` → two hits, line 206 (this reference) and line 845 (§7's unrelated *"none of it is off-limits by default"*).

A builder reading §4.2 top-down is told a specific, scare-quoted license exists below and applies to only one kind of bullet, then never encounters it. The nearest text with that shape is §4's preamble at line 172 — *above*, not below — and it says something different (*"it isn't a second, quieter list of limits"*).

This is precisely the failure mode this commit was fixing in §5 — a citation to language that no longer exists — reintroduced eleven lines into §4.2 by the fix itself.

**Fix.** Drop the scare quotes and the "below": *"Two different kinds of bullets follow, and the openness license in this section applies to only one of them."* One-line edit.

### P1-2. "The two handed-off defects" is wrong for one of the two, and re-states a claim targeted re-check #2 already marked stale.

> **§4.2, lines 212–215:** *"A few bullets are different in kind — retrieval ordering, the `wrs/` record-layer lockstep requirement, and **the two handed-off defects** aren't mechanisms achieving a §4.1 goal at all, they're process and scope notes with their own reasoning stated inline..."*

Against the bullet it describes, **§4.2 lines 337–346**:

> *"`over_settling_adjudication` fired on 10 of 12 turns... and, per the governance-layer evaluation above, **no longer out of scope by default**... Design should evaluate it as part of the governance-layer scrutiny above, **not treat it as a separate, untouchable defect log entry**."*

Defect 1 (the `CitationModal.tsx` `key_sources` leak, lines 331–336) is genuinely handed off. Defect 2 is explicitly **not** — it was opened by `2aa12b15` and its own bullet says so in bold. It is also, contrary to "aren't mechanisms achieving a §4.1 goal at all," the firing rate of `over_settling`, which **§7:848–852** names as *"the one already-measured, most consequential case"* and instructs Design to *"evaluate it as part of this same license, not as a special case needing separate permission."*

So the new paragraph tells Fable that a bullet is outside the openness license which §7 tells Fable is the flagship case *inside* it. Targeted re-check #2 flagged the identical staleness at its P2-7 (about §3:63's *"the two adjacent defects (§4) this brief carves out of scope"*) — that pointer is still unfixed at **§3, line 63**, and the new §4.2 paragraph now makes it a second instance rather than a lone one.

**Fix.** *"...retrieval ordering, the `wrs/` record-layer lockstep requirement, and the `key_sources` defect handed off for separate triage..."* — and note that the second defect bullet is inside the license, not outside it. While there, fix §3:63.

### P1-3. §4 now contradicts its own preamble two paragraphs later — and §4.1's "One scope boundary, not a fifth fixed item" and the launch prompt's mirror of it are both wrong as a result.

> **§4, lines 170–174:** *"§4.1 is short because that's the real size of the constraint — **four things, no more**. §4.2 is long, but **it isn't a second, quieter list of limits** — it's what currently exists, read as context Design needs before rebuilding it, not permission to ask for."*

> **§4.1, line 193:** *"**One scope boundary, not a fifth fixed item** — not protected, just not this thread's."*

> **§4.2, lines 212–219 (new):** four named bullets are carved out of the openness license, with *"Read each bullet for what it actually says rather than assuming this section's general openness overrides a bullet's own explicit instruction."*

The substance of the new paragraph is right — targeted re-check #2's P1-1 correctly showed that "None of it is a limit" over-reached across four process/scope notes. But it was inserted without touching the two sentences 20 and 40 lines above that promise the opposite. §4 now says, in the same section: the constraint is four things and §4.2 is not a second list of limits; and: here are four more items in §4.2 whose instructions override the general openness.

This propagates. **Launch prompt, line 22:** *"One scope boundary, not a protection: the front-end transparency UI..."* — a faithful mirror of §4.1:193, and now numerically wrong against §4.2's new intro for the same reason §4.1:193 is. The launch prompt also tells Fable *"Read §4 in full before touching any file; it draws this line precisely"* — which is now the one thing §4 does not do.

**Fix.** One clause in §4's preamble: *"...it isn't a second, quieter list of limits — apart from a handful of working instructions for this thread, flagged as such in §4.2's own intro."* And *"One scope boundary among §4.1's own four"* at line 193, or a pointer forward.

### P1-4. The new paragraph re-protects "A Turn Has a Measure" — the half of round 5's P0-2 that Mark's resolution never answered — and states a precedence rule that is the exact inverse of §7's.

> **§4.2, lines 215–219 (new):** *"...and the interview-vs-table pacing bullet **specifically instructs *preserving* "A Turn Has a Measure" deliberately**. **Read each bullet for what it actually says rather than assuming this section's general openness overrides a bullet's own explicit instruction.**"*

> **§7 Part A, lines 825–826:** *"**This license covers everything in this section, without named exceptions for specific mechanisms**..."*

Two things are wrong here, and the second is the one that matters.

**First, a precedence inversion.** §4.2 now says a bullet's own instruction beats the section-level license. §7 says the license beats any named exception. These are opposite rules about the same kind of conflict, stated 610 lines apart, both in bold. The block containing "A Turn Has a Measure" (`representative_prompts.py:59-60`) is rewritten by §7 Part A's own "Pilot first, isolated" bullet at line 854, so §7's license does reach it — the conflict is live, not hypothetical. (A narrower reading survives: §7's *enumeration* covers "every mechanism currently achieving any of those goals," and a turn-length ceiling achieves none of §4.1's four. That reading reconciles them, which is why this is P1 and not P0 — but Fable should not have to construct it.)

**Second, and more seriously: this is a decision being taken on Mark's behalf.** Round 5's P0-2 named exactly two items as needing Mark rather than an edit — fabrication-rate tracking and "A Turn Has a Measure" (Round5 lines 82, 415). I read `18c4830e`'s full diff: Mark's resolution enumerates the fabrication-guard blocks' wording, the three-level sourcing apparatus's implementation, **the fabrication-rate check's specific mechanism**, and every governance/monitoring check. **It never mentions turn length, in the commit message or in a single line of the diff.** So one half of round 5's P0-2 was answered and the other half was not.

`ff0784bb` closes the answered half and, in the same commit, hardens the unanswered half in the direction of preservation. Under Mark's own stated rule — *"the end goals are fixed. The *form* used to reach them is not"* (§4:167–170) — a turn-length ceiling is form, and no §4.1 goal requires one. Targeted re-check #2 recommended this wording, so this is not a lapse in following review; it is the review having recommended something that quietly resolves an open question.

For what it is worth on the merits: §4.2's own argument for preservation is real (every instruction §7 Part A adds pushes length up against this ceiling, and I confirmed **§8 still names no turn-length or turn-count instrument** — grep of lines 1040–1160 returns nothing measuring turn length). But "there is no instrument to catch its loss" is an argument for *adding an instrument*, not for exempting a mechanism from the general rule.

**Fix.** Either (a) restate it as a warning rather than a protection — *"§7 Part A's edit will delete the system's only turn-length ceiling unless it deliberately decides otherwise; that is a decision to make and record, not an accident to allow"* — which is fully consistent with Mark's rule and loses nothing; or (b) take it to Mark as the open half of round 5's P0-2. (a) is available now and does not need him. Do not leave it reading as settled in one section and prohibited in another.

### P2-1. Number-agreement slip introduced by the fix.

> **§4.2, lines 209–211:** *"rewrite, replace, simplify, or drop **any of them**, provided whatever replaces **it** is verified..."*

Pre-commit text read *"any of it — provided whatever replaces it"* and agreed. The edit pluralized the first half only. Two words.

### P2-2. The relocated paragraph now says "above" twice about the same thing.

> **§7 Part A, lines 782–792:** *"One real correction **about the source records above**, not a restatement..."* … *"**The records above** are still the right thing for Design to build from..."*

"about the source records above" was added to give the relocated paragraph a locator, which it needed — but the paragraph already ended with "The records above." Harmless, visible on a careful read. Trim either one.

### P2-3. §7's license says it covers "this section" while enumerating mechanisms from §4.2 and §8 — and a one-word fix here would also give the document the doc-wide reach re-check #2 asked for.

> **§7, lines 825–826:** *"This license covers everything in **this section**..."*

Its own enumeration (lines 832–839) then names `over_settling`, `citation_grounding`, `drift_detection`, `confirmed_glosses` (all §4.2 bullets), **fabrication-rate tracking** (a §8 instrument, lines 1066–1072), and the drift-telemetry and disagreement-probe proposals (also §8). The stated scope is narrower than the list it governs — so the clause that closes re-check #2's P0-1 sits inside a sentence that, read strictly, does not reach the thing it names.

No harm follows today, because nothing contests it: the protection sentence is gone and nothing else claims one. But targeted re-check #2's preferred remedy was doc-wide reach, and this commit took the local remedy instead. **Changing `this section` to `this brief` costs one word and closes both.** Recommended.

Related and smaller: **§4:167** still reads *"One rule governs this entire section"* while §7:828 and the launch prompt both treat it as the document's governing rule. Same one-word class of fix.

### P2-4. `probe_parity` retains an ambiguous non-optional phrasing five lines above the "no named exceptions" sentence.

> **§7, lines 818–821:** *"Continuity-regression testing is not new either — `wrs/views/probe_parity.py` already runs it for all six worlds, with real committed results (§7 Part B) that Design needs to read before deciding anything about it, **not treat as an optional new instrument**."*

Intended meaning (and the correct one, given the preceding *"is not new either"*): don't mistake an existing, already-run instrument for a new optional add-on. But parsed the other way it reads as "this instrument is not optional," which is the shape the last three passes have been removing. *"...before deciding anything about it, rather than treating it as a new instrument still to be built"* removes the ambiguity. Flagged because the dispatch asked for a fourth instance of the pattern and this is the only near-miss the sweep turned up — it is not a genuine surviving protection.

### P2-5. Two of re-check #2's restorations landed in §7 rather than the §4 locations it recommended; §4 still lacks both.

`ff0784bb` restored the permissive framing (*"Achieving a fixed goal a different, better, or cheaper way is the actual point of this rebuild, not a risk to guard against"*) and Mark's scope line (*"this is not the worlds, it's everything about how a voice gets built and how a conversation unfolds"*) — both faithful to the deleted originals, both verified against `b6959d04`'s diff. Both went into **§7:841–845**.

Re-check #2's P1-2 and P2-4 asked for them in §4's governing rule or §4.2's preamble, because §4 is the section a reader consults for scope. Consequences, both minor: §4 still states no outer boundary for what the rebuild may touch, and **§4.2's preamble still ends on the cautionary clause** (*"not just assumed to because it reads better or costs less"*, line 211) with no permissive counterweight — which was the specific complaint of P2-4. The document as a whole now says both things, so nothing is missing; they are just in the section that already read as permissive rather than the one that reads as restrictive.

### P2-6. §5's replacement wording adds a third instance of the one-versus-four friction.

> **§5, lines 534–536:** *"the instrument verifying **the one goal this brief calls genuinely fixed with no exception** (§4.1: no fabrication, ever; §6 Objective 4)"*

Supportable — §4.1:179 is the only one of the four tagged *"Absolute, under any framing,"* and §2:43 says *"One thing does not move."* But the brief now says, in three places: one thing does not move (§2:43), four things are fixed and no more (§4.1:176), and one goal is fixed with no exception (§5:535). Targeted re-check #2 raised the first pair as its P2-6; this is the same friction, one instance larger. No contradiction with §6 — Objective 3's equal weight (§6:613–618) is a priority claim, not a §4.1 fixedness claim — verified.

### P2-7. The launch prompt's re-check count goes stale again the moment this file lands. Third occurrence.

**Launch prompt, lines 6–8 and 30:** *"five full Opus adversarial rounds plus **two** targeted re-checks"* / *"Read all **seven** review files."* Both correct as of `ff0784bb`; both wrong once this file is committed. The same line was corrected by `b1fc74c6` and again by `ff0784bb`.

**Fix, once:** *"Read every review file in `Ministry/Operations/Audits/` matching `CiC_VoiceRebuild_Brief_Opus_Adversarial_Review_*` — full rounds and targeted re-checks alike."* Stops the recurrence permanently.

### P2-8. Cosmetic line-wrap debris left by the §5 and §7 edits.

Orphaned short lines at **§5:537** (*"where the prototype"*) and **§7:769** (*"spoken** (§4) — identity, era,"*). Markdown renders these fine; they are visible in the source and are a sloppiness tell in a document that is otherwise consistently wrapped. Reflow both paragraphs.

---

## Verdict on each dispatch item

**1a. Does the §7 license paragraph now read as internally consistent?** **Yes.** Verified two ways.

The contradicting sentence — *"Fabrication-rate tracking is the only real instrument for Objective 4, one of this brief's two non-negotiables — not a candidate for dropping"* — is gone in full (`not a candidate for dropping` → zero hits document-wide). Its replacement, **§7:832–839**, folds fabrication-rate tracking into the enumeration of what is open, with a parenthetical that states the goal/mechanism split correctly rather than asserting it: *"**including fabrication-rate tracking's specific implementation** (the goal it verifies is fixed; the mechanism is not)."* The claim is also true on its own terms — it is a measurement instrument, and the parenthetical says so rather than miscasting it as an achieving mechanism.

The commit also fixed something it did not claim: the deleted sentence's "one of this brief's two non-negotiables" was false against §6 (which defines the two as **Objectives 3 and 4**, at lines 607–612). The only surviving statement of that shape is **§8:1070**, *"the actual instrument for Objective 4, one of the two parallel non-negotiable priorities named in §6"* — which attributes non-negotiability to the **objective**, matching §6 exactly, and does not protect the instrument. That resolves cleanly.

And the sentence the license now had to be consistent with — *"Design may question, simplify, or drop either"* about the two new proposals — was deleted from the preceding paragraph, but the proposals are now named inside the license's own enumeration (*"the drift telemetry and disagreement-probe proposals above"*, line 838), so nothing was lost. Checked.

**1b. Does §5's `fabrication_adjudication` description now reflect what §4.1/§6 Objective 4 actually say?** **Yes, on both pointers.**

| Claim | Cited to | What the target says | Verdict |
|---|---|---|---|
| the goal is fixed with no exception | §4.1: no fabrication, ever | **§4.1:178–179** — *"**No fabrication, ever.** ... Absolute, under any framing."* | Resolves |
| same | §6 Objective 4 | **§6:721–722** — *"No fabrication, ever, is fixed — the goal, **not any particular mechanism teaching it** (§4)."* | Resolves |
| `fabrication_adjudication` is the instrument verifying it | (implicit) | **§8:1066–1072** — *"the actual instrument for Objective 4"* | Consistent |

All three failures re-check #2 found in the old clause are gone: `fabrication_adjudication` is no longer claimed to be named in §4 (it never was), no governance check is called out of scope, and the Objective 4 half now agrees with §6's goal-not-mechanism framing instead of contradicting it. The one residue is the "one goal" phrasing (P2-6).

**1c. Does the relocated paragraph still contain every fact?** **Yes — verified by word-level diff against the pre-commit text, not by placement.**

| Fact | Established by | Present at §7:782–792 |
|---|---|---|
| writes a separate staging file `staging/desert_Representative_Permanent_Prompt_S52.txt` | Recheck#1 line 70; Round5 line 363 | Yes, verbatim |
| hardcoded to Desert (`desertcore001`/`desertvoice001`) | Recheck#1 line 74; Round5 line 363 | Yes, verbatim |
| the other five worlds' assemblers each open with `DELIBERATELY TEMPORARY` | Recheck#1 line 74; Round5 lines 228, 363 | Yes, verbatim |
| `probe_parity.py` compares assembled-from-records against deployed | Round4 P0-1 | Yes, verbatim |
| four of six worlds already show that comparison failing | Round4 lines 29, 60–65 | Yes, verbatim |
| records are still the right thing to build from / not yet what the system runs on | Recheck#1 P0-2 | Yes, verbatim |

`difflib` over the normalized paragraph returns exactly **two** deltas, both improvements: `"One real correction,"` → `"One real correction about the source records above,"` (a locator the relocation required), and `` `wrs/\nviews/permanent_prompt.py` `` → `` `wrs/views/permanent_prompt.py` `` — a code span that had been broken across a line and would have rendered as `wrs/ views/permanent_prompt.py`. That second repair is real and is not mentioned in the commit message. Document-wide occurrence counts unchanged (`permanent_prompt.py` 2→2, `DELIBERATELY` 1→1, `probe_parity` 8→8, `One real correction` 1→1), so nothing was duplicated or left behind.

Round 5's P1-2 — that `probe_parity.py` actually compares against `capsule_prompt_views.py`'s `_generated.txt`, not `permanent_prompt.py`'s `_S52.txt` — is **still unapplied** in this paragraph. Pre-existing, already filed, explicitly not re-litigated here; noting it only so the next reader does not mistake its survival for something this commit did.

**2. Is the relocated sentence grammatically clean on a fresh read?** **Yes. No new seam.**

The repaired sentence, read cold: *"It starts from that world's actual source records — [parenthetical] — and from this brief's own principles (§1, §2, §6), and writes the *prose, register, and delivery* fresh."* Subject `It`, compound predicate `starts from A … and from B, and writes C fresh`. The dangling *"and writes"* with no subject is gone. The parenthetical is long but closes properly.

I checked the three seams the dispatch named:
- **Orphaned reference:** none. *"about the source records above"* resolves to the immediately preceding paragraph, which is where the records list is.
- **Repeated phrase:** one, minor — "above" twice in the same paragraph (P2-2).
- **A paragraph that now ends oddly:** no. The paragraph that now follows the insertion, **§7:794**, opens *"This matters concretely, not just procedurally: Mark's own stated concern is that six builds have accumulated assumption rules that were never actually necessary..."* Its antecedent moved — it used to follow the no-comparative-diffing paragraph, and now follows the records-vs-deployed correction. I read the join fresh expecting a mismatch and did not find one: "the records are the right thing to build from, though not what the system runs on **— this matters concretely**, because the current prompts have accumulated rules the sources don't support" is a coherent, arguably tighter chain than the original. Judged clean.

**3. Is the new §4.2 scope-clarification paragraph accurate?** **Its list is complete; two of its four categorizations are wrong or contestable, and it contradicts §4's preamble.**

Coverage first — I enumerated all eight §4.2 bullets against the paragraph:

| §4.2 bullet | Kind | Named as process/scope? | Correct? |
|---|---|---|---|
| Fabrication guards, current state (221–230) | mechanism | no | Correct |
| Witness-not-recruitment, current state (231–240) | mechanism | no | Correct |
| Governance/monitoring layer (241–276) | mechanism | no | Correct |
| Confirmed inline glosses (277–283) | mechanism | no | Correct |
| Retrieval ordering (284–291) | scope note | yes | Correct |
| `wrs/` lockstep (292–301) | process requirement | yes | Correct — and it closes re-check #2's specific worry, since §7:933–937 cites §4 as authority for it |
| Interview-vs-table pacing (303–327) | mixed | yes, via the "preserve" clause | Accurate as description; see **P1-4** for what it does |
| Two adjacent defects (328–346) | one handed off, one explicitly reopened | yes, both | **Wrong for defect 2 — P1-2** |

It misses nothing. It wrongly includes half of one bullet (P1-2). It correctly describes the "preserve" instruction but thereby takes a position on an open decision (P1-4). And it introduces one new contradiction: with **§4:171–174** and **§4.1:193**, which promise §4.2 is not a second list of limits and that there is exactly one scope boundary (P1-3). It introduces no contradiction with **§4.1's four fixed goals** themselves — none of the four carved-out bullets is a §4.1-goal-serving mechanism, so the license's proviso is untouched — and no contradiction with §9:1213–1218, which asks for a recommendation on the four governance mechanisms, all of which remain fully open.

**4. Does a fourth or fifth instance of the pattern survive?** **No. Verified exhaustively.**

Twenty patterns grepped across all 1,273 lines, every hit read in context:

| Pattern | Hits | Status |
|---|---|---|
| `not a candidate for dropping` | 0 | Removed |
| `completely out of scope` | 0 | Removed |
| `word for word` | 0 | Removed by `18c4830e` |
| `untouchable` | 2 | Both **negations** (§4.1:201 *"not because anything about it is untouchable"*; §4.2:346 *"not treat it as a separate, untouchable defect log entry"*) |
| `under any framing` | 1 | §4.1:179 — applied to the **goal**, correct |
| `non-negotiable` | 2 | §6:607 and §8:1070 — both applied to **Objectives**, both resolve to §6:607–612, correct |
| `off-limits` | 1 | §7:845 — *"none of it is off-limits by default"*, a negation |
| `protected` | 1 | §4.1:193 — *"not protected"* |
| `preserv*` | 4 | §4.2:216, 315, 324 (the "A Turn Has a Measure" cluster, **P1-4**); §7:909 *"rather than preserving its current wording"* |
| `exempt` | 2 | Both negations (§5:503, §7:932 *"not a standing exemption"*) |
| `must` / `has to` / `have to` | 18 | All read; only §4.2:292/301 (`wrs/` lockstep) and §4.2:324 ("A Turn Has a Measure") are mechanism-level mandates, and both are now explicitly categorized by the new paragraph |
| `not optional` | 3 | §3:92 and §6:735 are about scope, not mechanisms; §7:820 is the ambiguous parse at **P2-4** |
| `as-is`, `never moves`, `stays fixed`, `not open`, `don't touch`, `leave alone`, `no exception` | 0–1 each | §7:828 *"What actually stays fixed"* introduces the goals list; rest zero |

**The class is closed.** Nothing in the brief now protects a specific mechanism as a mechanism. The only remaining item in that neighborhood is "A Turn Has a Measure," and it is not worded as a protection — it is worded as an instruction to §7 Part A, which is why the greps do not catch it and why it needs the separate treatment at P1-4.

**5. Is the launch prompt accurate and consistent with the brief?** **Accurate; consistent with one inherited exception.**

- *"five full Opus adversarial rounds plus two targeted re-checks"* and *"Read all seven review files"* — arithmetic correct (5 + 2 = 7), and I confirmed all seven named files exist on disk at exactly the cited paths. Goes stale on this file landing (**P2-7**).
- New clause: *"one targeted re-check even found that a purely-organizational edit had silently dropped the sentence carrying a prior decision"* — a fair and accurate summary of re-check #2's P0-1. Not an overclaim.
- Line 22's open-mechanism enumeration does **not** include fabrication-rate tracking, while §7:833 now does. Not false — the sentence is *"Everything else is open, **including**…"*, non-exhaustive, and the general rule covers it. But `18c4830e` propagated exactly this class of correction into the launch prompt and `ff0784bb` did not. Optional; add four words if it is being edited anyway.
- Line 22's *"One scope boundary, not a protection"* is a faithful mirror of §4.1:193 and is wrong only because §4.1:193 is now wrong (**P1-3**). Fixing §4 fixes this.
- Everything else in the file — the clean-rebuild framing, Interview-mode-only, §6's priority structure, the two load-bearing facts, the §9 staging — re-checked against the brief's current text and consistent.

**6. Structural check.** **The smallest, most surgical commit in this document's history.**

- Balance ratio **58.8 / 41.2 → 58.9 / 41.1** on my tokenizer (a different cut point from re-check #2's, so compare the *delta*, not the absolute): **+0.1** toward the framing side, from 137 net tokens added, all in §4.2 and §7. Round 1's 68/32 failure mode remains absent.
- `§N` pointers **103 → 105**, and the arithmetic is exactly what the diff predicts and nothing else: `§4` −1 (§5's dead `(§4, Objective 4)`), `§4.1` +2 (§4.2's new intro, §5's replacement), `§6` +1 (§5's replacement). No pointer added or removed anywhere else.
- **Zero duplicated long sentences** document-wide — the relocation left no copy behind.
- Every citation, quoted string, count and file path in the touched regions survived; I checked each individually.

---

## What to fix, in order

1. **§4.2:206** — drop the orphaned `"none of it is a limit"` quotation and the "below." **(P1-1)** — one line, and the most embarrassing of these if it ships.
2. **§4.2:213–215** — *"the two handed-off defects"* → the `key_sources` defect only; the `over_settling_adjudication` bullet is inside the license, not outside it. Fix **§3:63** in the same pass. **(P1-2)**
3. **§4:172–174 and §4.1:193** — reconcile with §4.2's new carve-outs, or the section contradicts itself and the launch prompt inherits it. **(P1-3)**
4. **§4.2:215–219 and/or §4.2:324** — restate "A Turn Has a Measure" as a decision Design must make and record, not a mechanism it must preserve; or take it to Mark as the unanswered half of round 5's P0-2. **(P1-4)** — **the one item on this list that is not a reviewer's to close.**
5. **§7:825** — `this section` → `this brief`. One word, and it gives the license the doc-wide reach targeted re-check #2 asked for. **(P2-3)**
6. **Launch prompt lines 6–8, 30** — replace the counts with a glob so this stops recurring every pass. **(P2-7)**
7. P2s at discretion: the `any of them / replaces it` slip (P2-1); the doubled "above" (P2-2); `probe_parity`'s "not optional" parse (P2-4); moving the permissive line and Mark's scope line into §4 as well (P2-5); the one-versus-four phrasing (P2-6); reflowing §5:537 and §7:769 (P2-8).

**Is a fourth targeted re-check warranted?** **No.** Items 1–3 and 5–6 are deletions, re-points and one-word substitutions — the class that has held 100% across five fix commits. Item 4 is a decision, not an edit. The only thing that needs a second pair of eyes is the replacement text for §4.2's intro, and one careful re-read against §4:171–174 and §4.2:328–346 by whoever writes it is proportionate. **Five full rounds and three targeted re-checks is enough. Send it after item 1–4.**
