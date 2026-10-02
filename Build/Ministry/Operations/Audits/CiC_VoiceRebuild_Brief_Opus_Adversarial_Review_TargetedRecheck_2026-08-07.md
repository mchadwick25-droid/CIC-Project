# Targeted re-check (post-round-4 fix pass): `CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md`

*Opus targeted re-check, dispatched 2026-08-07. Not a fifth full round — scoped by Mark's own instruction to commit `1a142908` ("Apply round-4 fixes — corrections only, plus honest retraction of one unverifiable count") on branch `claude/v9-postmortem-pta21n`, and to the seven P0s of `..._Round4_2026-08-07.md` that commit claims to close. Rounds 1–4 read; round 4 read in full first, per the Standard Practice's point 4. The rest of the document was deliberately not re-reviewed.*

*Verification method, per the Standard Practice's point 1 and round 4's own closing lesson (**verifying that a cited symbol exists and does what its docstring says is not the same as verifying it is wired to the thing the brief credits it with enforcing**): every caller of `readability_check` re-enumerated from scratch across the whole repository — including the uncalled `gate_readability` wrapper — without reference to round 4's table. All six `probe_parity` scripts and all six committed `*_probe_parity_result.json` files opened and parsed directly. All six per-world prompt/capsule assemblers' docstrings read. `wrs/views/permanent_prompt.py` read at `build_context()`, not just at its docstring. `wrs/records/hieronymian_world/` and `wrs/records/imperial_juridical_world/` enumerated directory by directory with per-directory record counts. `data/*/` enumerated for source-registry files. Lexicon and story chunks counted on disk. `wrs/parameters.yaml` read at the cited line range. Git tracking of the staging result files confirmed with `git ls-files`. Diff sized: **1,646 words added, 932 removed, net +714**; document now 10,900 words.*

---

## Bottom line

**Not clean. Not ready to send.**

The corrections themselves are excellent — better than any prior fix pass. **Every fix that deletes or re-points a claim holds up under independent re-derivation, without exception**, and the two hardest ones (items 5 and 6 of the dispatch) I re-derived from scratch and they are *exactly* right, down to the per-world pass/fail split. The four-round operating rule the project has now adopted is confirmed for a fifth commit on the deletion side.

But three send-blocking defects remain, and they fall into a pattern worth naming precisely, because it is a **sharper form** of the rule the project just adopted:

- **Two of the seven P0s were applied in one place and not in the other places that state the same corrected-away claim.** The `readability_check` correction landed in §7 Part B and nowhere else — §4, §7 Part A's per-world bullet, §8 and §9 all still describe the gate the old, now-falsified way, including the literal phrase **"already built, already wired"** that round 4 quoted as the defect. The Objective-3 contradiction was fixed on the §6 side only; §8 still says `readability_check` "is the instrument that actually tests Objective 3," which the corrected §6 now explicitly denies.
- **One P0 fix introduced a new P0-class factual error**, in the one sentence where the correction required asserting a *replacement* fact rather than deleting a wrong one. §7 Part A now claims `wrs/views/permanent_prompt.py` "already assembles **the current deployed prompt**" from the record layer. It does not. It writes a *staged* prompt to `staging/`, is hardcoded to Desert, and the deployed prompts are precisely the artifact `probe_parity` compares that staged output *against* — which the same commit, 220 lines later, reports as failing for four of six worlds.

**The refined rule.** Round 4's rule was "corrections hold, new positive prose doesn't." This commit is corrections-only by intent and by commit message, and it still produced one new P0 and left two others half-applied. The distinguishing feature is not "new prose" versus "correction" — it is **whether the correction can be executed by deleting or re-pointing, or whether it requires the document to assert a new positive fact in the wrong claim's place.** Deletions held 100%. Re-points held 100%. The two failures are (a) a replacement fact that was not checked (`permanent_prompt.py`), and (b) corrections that were applied at the site round 4 quoted rather than at every site that carries the claim. Roughly 500 words of the 1,646 added are genuinely new positive assertion; one P0 in 500 words is consistent with round 4's ~1-per-350 estimate.

### Fix-by-fix verdict

| # | Round-4 P0 | Verdict |
|---|---|---|
| 1 | Cost/complexity license (§7 Part A) | **6 of 7 sub-problems fixed.** Clean on non-negotiables, "this week," `over_settling`, three-level transparency, and the unestablished cost-goal premise. The §4 cost misattribution (round 4's P0-4(6)) is **unfixed**. |
| 2 | Clean-rebuild mandate (§7 Part A) | **Scoping, freeze-list collision, no-comparatives collision and witness-not-recruitment all clean.** Source list **introduces a new P0** (`permanent_prompt.py`). The `data/` Source-Registry claim is **true, verified**. |
| 3 | Objective 3 (§6) | **Opening sentence genuinely fixed.** The §8 contradiction is **half-fixed** — §6 moved, §8 did not. The other two components of round-4 P0-6 are untouched. |
| 4 | Ecological-Function leak filter (§7 Part A) | **Clean.** No contested count anywhere in §7; reads as a genuine open Research task; the two chunk-corpus counts it does state (118 / 60) are exact. One residual tension with §5(B). |
| 5 | `readability_check` not wired to voice | **Correction itself is exactly right — independently re-derived.** But applied in §7 Part B only; **four other sites still carry the falsified claim.** |
| 6 | Continuity-regression already exists | **Existence, mechanism and all six pass/fail results independently re-derived and exact.** The *interpretation* overclaims (P1-2). |
| 7 | Stale round counts (§8, §9) | **Clean.** Grepped every `round` occurrence; no stale count and no "round 2 still warranted" survives anywhere. |

---

## P0 — fix before sending

### P0-1. The `readability_check` correction was applied at the one site round 4 quoted and at none of the four other sites that state the same, now-falsified claim — including the phrase "already built, already wired" verbatim.

Round 4's P0-2 named the defect and, in its consequence 3, named two of the surviving sites by line. The commit message says *"readability_check corrected: not wired to Representative voice at all."* §7 Part B is corrected. Four other places are not.

**(a) §8, lines 951–955 — the sentence round 4 quoted as false, unchanged, plus a second defect (see P0-3):**

> *"**`readability_check` (`wrs/gates/core.py:211`)** — **already built, already wired** to Part Five's own numbers (`wrs/parameters.yaml:101-114`). Run it against baseline and rebuilt output for all six worlds..."*

Against §7 Part B, lines 858–864, in the same commit: *"it is not currently wired to Representative voice generation at all... No world's `voice_profile` record connects it to the permanent prompt or capsule."* The dispatch's own cheap general check — grep "already wired" — lands exactly here.

**(b) §4, line 233:** *"a hand-edit to `data/` that isn't mirrored into the matching `wrs/records/` entry desyncs the record layer the gates (**including the readability gate in §7 Part B**) read."* The readability gate reads no record layer. Verified: its two call sites take a rendered plain-explanation body and three string fixtures; it never opens a record.

**(c) §7 Part A, lines 828–832,** inside the per-world deliverable this commit rewrote: *"`wrs/views/probe_parity.py` and **the readability gate (§7 Part B) compare against the record layer**, and a `data/`-only edit desyncs the two."* Half true. `probe_parity` genuinely does; the readability gate compares nothing against anything in the record layer. The deliverable (update the `voice_profile` record in the same pass) survives on `probe_parity` alone, but half its stated justification is false — and it is false *by the authority of the section it cites*.

**(d) §9 task (c), lines 1087–1093:** *"confirm whether `readability_check` (§7 Part B) has ever actually been run against the six current builds — **a fact this brief could not establish and must not be guessed at**."* The brief now does establish it, in §7 Part B, from a direct caller enumeration, and says so. Round 4's fix instruction was explicit: *"convert §9(c) from 'find out' to 'wire it.'"* Unapplied. §7 Part B's *"Confirm this directly in Research rather than trust this brief's own account (§9)"* is a good instinct, but it points at a §9 task whose own wording still says the fact is unestablished.

**(e) §6 Objective 3, lines 643–648:** *"§9's Research stage should confirm whether `readability_check` has ever actually been run against her current prompt and what it returned."* Same shape. Per the correction, it has not and cannot be without new code; the Albina decision gate §6 builds on it therefore cannot fire as written.

**Why this blocks.** A Fable reader who reads §4 or §8 before §7 Part B gets the pre-correction fact, stated with equal confidence and with a file:line citation attached. §8 is the section that names the instruments, and §9 is the section that assigns the Research budget — the two places where a false wiring claim converts directly into wasted capped spend. This is structurally the same defect §3 spent two rounds fixing for the Decision Log and §8/§9 just fixed for the review record: a correction landed in one place and left superseded statements standing elsewhere with no superseding note.

**Fix.** Four edits. §8: *"already built and correctly implemented, sourced to Part Five's numbers (`wrs/parameters.yaml:102-114`) — but not wired to voice (§7 Part B); running it against baseline and rebuilt output is new work, not a re-run."* §4:233 and §7:830–831: drop the readability gate from both lockstep sentences and leave `probe_parity`, which is the one that actually reads the record layer. §9(c) and §6's Albina sentence: rewrite from "confirm whether it has been run" to "wire it to the six prompts and run it, then decide Albina."

---

### P0-2. New factual error, introduced by this commit, in the governing paragraph of §7 Part A: `wrs/views/permanent_prompt.py` does not assemble the current deployed prompt, and is not per-world.

Brief §7 Part A, lines 683–689, new in `1a142908`:

> *"It starts from that world's actual source records — `wrs/records/<world>/source/`, `/term/`, `/story/`, `/gravity/`, `/force/`, `/voice_profile/`, and `/world_core/` (the real per-world source material `wrs/views/permanent_prompt.py` **already assembles the current deployed prompt from**, per its own docstring: "same records → byte-identical outputs" — not a separate "Source Registry" file, which doesn't exist under `data/` for every world)"*

Three things are wrong, all checkable in one file.

**1. It assembles a staged prompt, not the deployed one.** `wrs/views/permanent_prompt.py`'s own docstring names its outputs: `staging/desert_Representative_Permanent_Prompt_S52.txt` and `staging/desert_prompt_segment_manifest.json`. The deployed prompts live in `data/<world>/*_Representative_Permanent_Prompt_*.txt`, which §4 line 230 correctly identifies as what the running app reads (`main.py:156`). These are different artifacts by construction — that is the entire reason `probe_parity` exists. `probe_parity.py:33-38` sets `DEPLOYED = data/desert_world/desert_Representative_Permanent_Prompt_Papnoute.txt` and `GENERATED = staging/desert_world/desert_Representative_Permanent_Prompt_generated.txt`, and its docstring's first line is *"deployed prompt vs. generated prompt - same voice?"*

**This contradicts the same commit's own §7 Part B, 220 lines later**, which reports that four of six worlds **FAIL** exactly that comparison. If `permanent_prompt.py` already assembled the deployed prompt, no world could fail, and the two lead acceptance worlds could not be among the failures.

**2. It is not "per-world."** `build_context()` (`permanent_prompt.py:44-55`) is hardcoded to Desert: `load_records("world_core")["desertcore001"]`, `load_records("voice_profile")["desertvoice001"]`. The Alexandria, Hieronymian, IJC, PAHC and Syriac assemblers are `s62_*_capsule_prompt_views.py`, and **every one of them — plus Desert's own `capsule_prompt_views.py` — opens with `DELIBERATELY TEMPORARY`**, e.g. `s62_hal_capsule_prompt_views.py:4-8`: *"DELIBERATELY TEMPORARY (the real SS5.1 segment assembly is S5.2-class): proves the records can produce a voice-bearing prompt and stages a generated prompt real enough for probe parity."* So the document points Design at a Desert-only S5.2 assembler as the per-world precedent, and never mentions that the five other worlds' assembly is done by scripts that describe themselves as scaffolding.

**3. The directory list does not match what the cited file reads.** `build_context()` loads `term`, `story`, `contested_claim`, `figure`, `gravity`, `world_core`, `voice_profile`, `source`, `demonstration`. The brief's list names **`/force/`, which it does not read**, and omits `contested_claim`, `figure` and `demonstration`, which it does.

**Why this blocks.** This is the sentence that tells Design what "clean rebuild from sources" means and what to build from. Taken at face value it says the deployed prompts *are already* record-assembled — which would make the whole Part A mandate a regeneration exercise rather than a rebuild, would make §4's lockstep bullet incoherent, and would make §7 Part B's headline 4-of-6 finding unreadable. It is also, precisely, the class round 4 identified as this process's highest-yield check: a claim about what a cited tool is wired to, asserted from its docstring without opening its body.

**Fix.** *"It starts from that world's actual source records — `wrs/records/<world>/` (`source/`, `term/`, `story/`, `gravity/`, `figure/`, `contested_claim/`, `voice_profile/`, `world_core/`) — the same layer the project's own prompt assemblers build a **staged** prompt from (`wrs/views/permanent_prompt.py` for Desert, at S5.2; `s62_*_capsule_prompt_views.py` for the other five, all self-described as deliberately temporary). Note what that means: the deployed prompts in `data/` were **not** produced from these records — `probe_parity` compares the two and four of six worlds diverge (§7 Part B). There is no separate 'Source Registry' file under `data/` for three of the six worlds."* Verified: the record directories the mandate should name all exist and are populated for both lead worlds — Albina 26 source / 15 term / 12 story / 10 gravity / 12 force / 1 voice_profile / 1 world_core; Marius 41 / 12 / 6 / 7 / 10 / 1 / 1.

---

### P0-3. §8 still calls `readability_check` "the instrument that actually tests Objective 3," which the corrected §6 now explicitly denies. Round-4 P0-6's contradiction was fixed on one side only, and is now inverted rather than resolved.

> §6, lines 594–600 (corrected this commit): *"Plainness and readability (below) are **necessary** for that, but **not sufficient** by themselves — **a conversation can pass every readability number `readability_check` reports (§7 Part B, §8) and still fail this objective completely**... passing the floor is a prerequisite this objective requires, not a substitute for the rest of it."*
>
> §8, lines 953–955 (untouched): *"Run it against baseline and rebuilt output for all six worlds; **this is the instrument that actually tests Objective 3**, which no metric named here tested before this revision."*

An instrument that can be passed in full by a conversation that fails the objective "completely" is not the instrument that tests the objective. §6's new wording is a genuine improvement — "necessary, not sufficient" is the right relation — but it makes §8's claim false rather than merely loose. Round 4's fix instruction named the §8 edit explicitly: *"Correct §8's readability bullet to say what it actually is — the instrument for Objective 3's **readability floor**, a necessary condition, not a test of the objective."* It was not made. This is now the **third consecutive round** in which §6 was restructured and §8's readability bullet was left carrying the pre-restructuring version (round 3 P0-5 → round 4 P0-6 → here).

Two components of round-4 P0-6 are also entirely unaddressed, and they are the two that make Objective 3 unfalsifiable:

- **The positive half still has no instrument.** §6 Objective 3 now states a goal — insight, connection, drawing out the participant's own perspective, depth, authenticity — and §6 declares it exactly as program-ending as Objective 4. §8's seven instruments are readability, the fabrication rate, the over-settling confirmed rate, per-signal drift, a term-reclarification tally, the continuity-regression pass, and the sustained-disagreement probe. Not one bears on insight, connection or depth. §8's own opening standard is *"Every prediction this brief or its Research stage makes needs to be falsifiable by an instrument actually named here"* (lines 942–943). Half the program fails that standard by §8's own words.
- **§6's tier rule still condemns §6's own floor.** Lines 549–552, untouched: *"if a check or a rule is making conversation more restrictive **without making it more honest**, that's an Objective-3 failure the apparatus itself caused."* The FK 8–10 floor is more restrictive and is not justified by honesty — §6 justifies it nine lines later as *"an access requirement."* Round 4's fix (add "or more accessible") is one clause and was not made.

**Fix.** §8: *"the instrument for Objective 3's readability **floor** — a necessary condition, not a test of the objective itself."* Then either name an instrument for the positive half (§7 Part B's 16-trait rubric is the candidate already in the document and still absent from §8 — round 2's P1-2, now fourth round) or state plainly that the positive half is judged rather than measured, and by whom. And add "or more accessible" to the tier rule.

---

## P1 — materially improves, not disqualifying

### P1-1. §7 Part A and §7 Part B contradict each other, in the same commit, on whether wiring the readability gate to voice is optional.

> §7 Part A, lines 724–727: *"`readability_check` is not currently wired to Representative voice generation at all... there is nothing yet to 'drop' there, only **a real decision about whether to build the connection**."*
>
> §7 Part B, lines 871–874: *"if it's confirmed unwired, wiring `readability_check` to the six voice prompts (or their `wrs/records/` assembly path) is real, concrete Design-stage work, **not optional**."*

Part A's sentence sits inside a paragraph whose whole function is granting permission to drop things, so "a real decision about whether to build the connection" reads as a soft licence to skip it — against Part B's flat "not optional," and against Objective 3 being one of the two non-negotiables. One of the two has to move. Given Objective 3's status, Part B is the one to keep.

### P1-2. §7 Part B presents the 4-of-6 parity failures as a live, participant-facing continuity break. What the instrument's own authors say it measures is whether the *records* carry the voice.

The mechanical description and the results are exactly right (see *What verified clean*). The interpretation is not:

> Lines 913–918: *"the Realness Study's governance lesson (personality is a versioned artifact; a voice change that reads as objectively better can still break continuity for a returning participant) **is not a future risk to guard against, it's already live, documented**, in the two worlds this thread starts with."*

No participant has ever encountered a record-assembled prompt. What is documented is that a staging artifact diverges from the deployed one. The generators say so themselves — `capsule_prompt_views.py:5-7`: *"producing a staged generated prompt real enough for probe-parity **to measure whether the RECORDS carry the voice**"*; `s62_alx_capsule_prompt_views.py:8-9`: *"a staged generated prompt real enough for probe-parity to measure whether the RECORDS carry the voice."* That is a migration-completeness measurement, not evidence that a deployed voice changed under a returning participant.

This matters for two downstream reads. First, it means the honest headline is *"our record layer does not yet reproduce four of six deployed voices"* — which is a real and consequential finding, and arguably a **more** relevant one to a rebuild that Part A now says starts from those records (see P0-2). Second, the brief tells Design to read the results **"cold"** (line 909) while omitting that the compared artifact was produced, in all six cases, by a script that calls itself `DELIBERATELY TEMPORARY`. Reading them cold without that caveat invites attributing to voice drift what may be assembler coverage.

Also: *"this is not a new mechanism to build"* is too flat. The harness exists as a migration-era staging script. What §7 Part B should require of the Framework is its **promotion** to a standing pre-merge gate — round 4's own fix wording, not carried.

### P1-3. The cost claim is still attributed to §4, which makes no cost claim. This is the one sub-problem of round-4 P0-4 the rewrite did not address.

> §7 Part A, lines 745–747: *"`over_settling_adjudication`'s second-stage check is **the single largest invisible cost line item after the main response itself (§4, 10-of-12-turns finding)**."*

§4 lines 270–275, read in full, contains the firing count and nothing about cost: *"fired on 10 of 12 turns in this session's live test — not a rare safety net in practice. Worth watching (§8)... but fixing the check itself is out of scope here."* Either the parenthetical cites only the firing count, in which case the cost ranking is now wholly unsourced, or it cites the cost ranking, in which case it misattributes. Round 4's fix — re-source to the Decision Log's own cost table — is one edit. Note this is the same misattribution §8 line 965 makes independently (*"the raw `over_settling_adjudication` firing count §4 already names as expensive-but-expected"*), round 3's P2-9, now unapplied for a **fourth** round; the document misattributes cost framing to §4 in two sections.

### P1-4. §7 Part A now says leak counts aren't trustworthy; §5(B) still states one as fact, unchanged.

§7 Part A, lines 762–766 (new): *"an attempt this session to enumerate the full scope produced two different counts from two different checks and **neither is trustworthy enough to state as fact here**... A full leak audit across all 118 lexicon and 60 story chunks is a genuine, unfinished Research-stage task."*

§5(B), line 344 (untouched): *"**at least a quarter of the 107 Ecological-Function chunks** carry internal build-process language."*

The retraction was the right judgement — withdrawing an unverifiable count rather than writing a second guess is the same discipline round 4 praised in the Albina arithmetic withdrawal. But it was applied in §7 and not in §5(B), so the document simultaneously asserts a count and disclaims counts of that kind. (For what it is worth, §5(B)'s claim is probably safe: round 4's independent measurement put 27 of 107 leaks inside the Ecological Function field, which is 25.2%. The problem is the document's stated epistemic position, not the number.) Either add "at least a quarter" to what §7 says is unverified, or state in §5(B) that the fraction is a lower-bound estimate pending the Research-stage audit.

### P1-5. The licence still permits dropping Objective 6's only instrument outright.

§7 Part A, lines 733–737, names *"per-signal drift telemetry and the sustained-disagreement probe"* as what Design may "question, simplify, or drop." §8 lines 1018–1020 calls the sustained-disagreement probe *"the actual instrument Objective 6 needs and didn't have before this revision."* Objective 6 is Tier 2, not a non-negotiable, so this is not the same defect round 4's P0-4(1) found — but round 4's fix wording listed *"the sustained-disagreement probe's **form**"* as the droppable thing, deliberately, and the brief dropped the qualifier. As written, the licence permits leaving Objective 6 with zero instruments, against §8's own falsifiability standard. Restore "its form."

*(Verified while checking this: "per-signal drift telemetry and the sustained-disagreement probe, both genuinely new verification proposals from this brief's own review process" is **accurate**. Round 1's P0 fix list, line 237, proposes "per-signal drift counts, which requires logging the signal type"; round 2 lines 222/233 establish Objective 6 had no instrument, which is what the probe answers. The rewritten premise is sound.)*

---

## P2 — polish

1. **§7 Part B, lines 919–924, misdescribes the existing script twelve lines after describing it correctly.** *"`probe_parity`'s own pass criterion checks the rebuilt voice against the current deployed one"* — it checks the *record-assembled* prompt against the deployed one; no rebuilt voice exists. The *implication* drawn (a deliberate register change would read as failure) is right and important. Reword to "applied to this rebuild, its criterion would compare..."
2. **"a test fixture" (§7 Part A, line 726) vs. "three fixtures" (§7 Part B, line 862)** — same commit, same fact, two numbers. Three is correct (`run_gates.py:139-141`).
3. **"both of §7's own lead acceptance worlds (Albina, Marius)" undercounts.** §8 lines 1002–1005 names **three** primary acceptance worlds — Albina, Marius **and Yausep** — and Syriac is also a FAIL. All three acceptance worlds fail parity, not two.
4. **`wrs/parameters.yaml:101-114` should be `:102-114`**, at §7 Part B line 856 and §8 line 952. Verified again: line 101 blank, `reading_floor:` at 102, block ends at 114. **Fifth round running.**
5. **"a separate 'Source Registry' file, which doesn't exist under `data/` for every world"** is scope-ambiguous English — it reads equally as "for no world." The intended meaning is correct and verified: `data/desert_world/sources.json`, `data/pahc_world/source_registry.json`, `data/syriac_world/source_registry.json` exist; Alexandria, Hieronymian and Imperial-Juridical have none. Say "for three of the six worlds."
6. **§4 was not amended alongside §7's `over_settling` reopening.** §4 line 274 still says *"fixing the check itself is out of scope here"*; §7 line 748 says that framing *"doesn't automatically survive"* the licence. §7 now states one clear position (the round-4 defect is fixed), but a reader of §4 alone still gets the closed one. One clause in §4 pointing at §7 closes it.
7. **§7 Part A line 761 repeats an imprecision round 4 logged as P1-3**: markerless chunks pass *"their whole body, internal notes included, through unfiltered."* `excise_section(body, QUICK_MEANING_MARKERS)` still runs, so Quick Meaning is removed. "Everything after the last content section" is the accurate form.
8. **Round-4 P0-6's three smaller problems survive**, all inside the paragraph this commit edited: item 3 still breaks the numbered list's parallelism by opening with an editorial note about its own sentence order; *"not a performance of any of those things"* and *"as seasoning, not performance"* still say the same thing four lines apart; *"the constraints below"* is still ambiguous between the rest of item 3 and objectives 4–6.
9. **§8 line 883** lists `readability_check` among *"the actual instruments this needs to run"* for Part Eight's new naturalness category, with no note that it is unwired to voice — a fifth, softer instance of P0-1's pattern.

---

## What verified clean

Stated plainly, because five of the seven fixes are genuinely good and two of them are the best-verified statements in the document.

**Fix 5 — `readability_check` is not wired to Representative voice. Re-derived from scratch, without reference to round 4's table. Exact.**

Every reference to the symbol in the repository, enumerated:

| Site | What it is |
|---|---|
| `wrs/gates/core.py:211` | the definition |
| `wrs/gates/core.py:244` | inside `gate_readability`, a wrapper with **zero callers anywhere in the repository** (confirmed repo-wide; its only other mentions are two audit documents and a task-board line recommending it be pointed at participant-facing surfaces) |
| `wrs/views/plain_explanation.py:174-175` | the Level-2 plain-explanation render for one lexicon term; reached only from `wrs/views/repository.py:195`, which builds `repository.json` |
| `wrs/gates/run_gates.py:139-141` | three string fixtures (`READABLE_TEXT`, `UNREADABLE_LONG`, `UNREADABLE_JARGON`) — a self-test that the gate works |

No path reaches a permanent prompt, a World Capsule Core, a `voice_profile` record, or Representative output. The record layer says so in its own words: five of six `voice_profile` records carry `reading_level_check: inherits reading_floor from wrs/parameters.yaml — a pointer, not a restatement`, and the sixth (`imperial_juridical_world/voice_profile/ijcvoice001.md`) carries **no such field at all** — which strengthens the brief's claim beyond what it states. **The brief's §7 Part B text is accurate in every particular.**

**Fix 6 — continuity-regression testing exists, has been run, and the results are as stated. Re-derived from scratch. Exact, including the per-world split.**

Six scripts committed (`probe_parity.py` + `s62_{alx,hal,ijc,pahc,syr}_probe_parity.py`). `probe_parity.py`'s docstring confirms every element the brief attributes to it, verbatim: *"deployed prompt vs. generated prompt - same voice?"*; *"two independent trials, blind grading"*; *"the two responses are presented as A/B in a seeded-shuffled order (grader never told which is deployed); grader must answer SAME-VOICE / DIFFERENT-VOICE on **register, measure, refusal behavior, and vocabulary**"*; *"parity holds if no probe gets DIFFERENT-VOICE on both trials."* All eighteen `staging/*parity*` files are tracked in git (`git ls-files`, confirmed).

Parsed directly from the committed JSON:

| Result file | World | `probes_failing_both_trials` | `parity` |
|---|---|---|---|
| `probe_parity_result.json` | Desert / Papnoute | 0 | **PASS** |
| `s62_pahc_probe_parity_result.json` | PAHC / Chloe | 0 | **PASS** |
| `s62_alx_probe_parity_result.json` | Alexandria / Theon | 2 | **FAIL** |
| `s62_hal_probe_parity_result.json` | Hieronymian / Albina | 1 | **FAIL** |
| `s62_ijc_probe_parity_result.json` | Imperial-Juridical / Marius | 1 | **FAIL** |
| `s62_syr_probe_parity_result.json` | Syriac / Yausep | 2 | **FAIL** |

**Desert pass, PAHC pass, Alexandria / Hieronymian / IJC / Syriac fail — exactly as the brief states, world for world.** The pass-criterion tension the brief flags for Design is real and correctly identified.

**Fix 7 — clean, and checked exhaustively.** Every occurrence of `round` in the document extracted and read. §9 lines 1137–1151 and §8 lines 1029–1037 both now state four rounds with the correct file range. §7's old "three adversarial-review rounds" is gone with the rewritten licence. **No "round 2 still warranted," no stale count, and no surviving instruction to read round 1 as the account of record survives anywhere.** §8 line 943's *"A round-1 Opus adversarial review... produced six per-world conversation-improvement predictions"* is a historical statement about round 1's own content, not a stale count — correctly left alone. The added operating-rule paragraph and the *"check whether a round 5 exists before treating round 4 as the last word"* clause are both good additions and neither overclaims.

**Fix 4 — clean.** §7 Part A's filter is now a general requirement (*"filtered against internal build-process language reaching a participant, stated as a general requirement, not a two-pattern list"*), the two known patterns are demoted to examples, and the audit is logged as *"a genuine, unfinished Research-stage task."* **No contested count appears anywhere in §7** — not 109, not 107, not 46, not "roughly a quarter." The two corpus counts it does state are exact on disk: **118 lexicon chunks** (Alexandria 50 / Desert 18 / Hieronymian 15 / PAHC 13 / IJC 12 / Syriac 10) and **60 story chunks** (PAHC 13 / Hieronymian 12 / Alexandria 10 / Desert 10 / Syriac 9 / IJC 6). Choosing to retract rather than re-guess was the right call and is the second time this document has made it.

**Fix 2 — everything except the source list.**
- **Scoping is fixed and does more work than it claims.** *"it governs the per-world bullet below specifically"* plus the explicit carve-out of `_HOW_YOU_ENGAGE` and the Facilitator fix closes round-4 P0-3(b). It also closes **P0-3(c) as a side effect**: both preservation instructions round 4 said collided with "no comparative diffing" — §4's *"§7 Part A's edit has to preserve 'A Turn Has a Measure' deliberately"* and §7's *"folded into the existing 'Let the Question Set the Shape, Not a Habit' section"* — live inside `_HOW_YOU_ENGAGE`, which the new scoping removes from the mandate. The italicised *"this* design process" at line 697 reinforces it. Clean.
- **The freeze-list collision is fixed.** *"Write the identity, era, vocabulary, register, and reasoning-mode **prose** fresh"* + *"The **facts** those paragraphs carry — who each Representative is, what span they speak from, their world's real terms — are given, per §4, not rebuilt"* quotes §4's own list back at it. No collision remains.
- **The witness-not-recruitment permission now matches §4 exactly.** §4: *"leave its content alone; it's fine if register work touches its sentence rhythm the same way it touches surrounding prose."* §7: *"§4 already permits register work to reach its sentence rhythm the same as surrounding prose, and that permission still holds here; 'untouched' means the substance, not a ban on the same register pass touching its phrasing."* Correct, and the fabrication-guard block is separately and correctly frozen word for word.
- **The record directories are real.** All seven named subdirectories exist and are populated for both spot-checked lead worlds (counts in P0-2). **The Source-Registry claim is true**: verified by direct `ls` of all six `data/<world>/` directories — three carry one, three do not, and the three that do not are Alexandria, Hieronymian and Imperial-Juridical, i.e. worlds #1 and #2 of §7's own sequence plus Theon's.

**Fix 3 — the opening sentence is genuinely fixed, not merely different.** Old: *"the conversation itself has to read and engage the participant as a real modern person."* New: *"the Representative has to actually engage the participant as the real modern person they are."* The zeugma is gone — one verb, one object, one complement, and the complement now unambiguously modifies the participant. Critically, this also removes the adapt-vs-dilute inversion round 4 flagged: the modern person is now the participant, which aligns with §1's *"speaking to a person who lives now"* instead of implying the Representative should sound modern. Read cold, it parses on the first pass. (The trailing appositive chain — *"honest, drawing out the truth..., carrying..., natural and deep and authentic"* — technically hangs off "connection" rather than "the Representative," but both readings point the same direction. P2 at most.)

**Fix 1 — six of seven sub-problems closed.** The non-negotiables are protected by name (*"Fabrication-rate tracking is the only real instrument for Objective 4... not a candidate for dropping"*; readability removed from the droppable list entirely). *"This week"* is gone. The unestablished premise *"lowering cost and complexity is an explicit goal of this rebuild"* is gone. `three-level-sourcing checks` is gone and replaced with *"the existing three-level transparent-sourcing mechanism (§6 Objective 4 calls it 'not separable' from no-fabrication — protected for the same reason fabrication itself is)"* — which now resolves correctly against §6. **`over_settling` now states exactly one position** and does so with an honest account of why (*"§4's 'out of scope' framing predates this cost/complexity license and doesn't automatically survive it, but reopening it is Design's call to make explicitly"*). And §6 line 553's pointer — *"see Part A's cost/complexity license (§7), which exists precisely so this tradeoff doesn't happen by default"* — now largely resolves, because everything the licence protects is content-honesty apparatus and everything it releases is verification overhead. Round 4's P0-4(2) is substantially cured.

---

## Why this pass still found what it found

The dispatch asked for a genuine verdict on whether the seven fixes are clean. They are not, and the reason is specific enough to be actionable rather than discouraging.

**The deletions and re-points are perfect.** Every fix that removed a false claim, narrowed a scope, or re-pointed a citation survived independent re-derivation with nothing to correct — including the two I was asked to derive from scratch, which are the most consequential facts in the document and are now among its best-sourced statements. That is five rounds running with no counterexample. The operating rule §9 now states is correct and earned.

**The failures are all one step past deletion.** P0-2 is a *replacement fact* asserted from a docstring without opening the file's body — the exact check round 4 identified as this process's highest-yield addition, applied to `readability_check` and `probe_parity` in the same commit and not applied to `permanent_prompt.py` two paragraphs earlier. P0-1 and P0-3 are corrections *landed at the site the review quoted* rather than at every site carrying the claim — four surviving instances for readability, one for Objective 3.

**So the rule wants one more clause.** "Corrections hold, new positive prose doesn't" is right but under-specified. The refinement this pass supports:

> A correction that can be executed as a deletion or a re-point is safe. A correction that requires asserting a replacement fact is new positive prose and carries new-prose risk regardless of the commit's stated discipline. And a correction is not applied until it is applied at **every** site that states the claim — grep the document for the corrected claim's own vocabulary before closing the finding, not just the line the review quoted.

**What this means for the next pass.** P0-1 and P0-3 are pure deletions and re-points across five identified lines — the safe class, and they should hold. P0-2 requires one replacement sentence and is therefore the one to check again afterward; the correct facts are enumerated above so it can be written from this document rather than re-derived. P1-1 through P1-5 are single-clause edits. **If the next fix commit is confined to those, a further targeted re-check of P0-2's replacement sentence alone is proportionate; a sixth full round is not.** If it again reaches for new framing, the rule says what happens.

---

## Recommended fix list, in order

1. **Rewrite §7 Part A's source-list parenthetical** — staged not deployed, Desert-only S5.2 plus five deliberately-temporary siblings, and the record directories corrected to what `build_context()` actually reads. **(P0-2)** The only fix here that requires writing a new positive claim; write it from the enumeration above.
2. **Apply the readability correction at the four remaining sites** — §8:951, §4:233, §7:830–831, §9(c):1087, and §6:643. **(P0-1)** Pure deletions and re-points.
3. **§8's Objective-3 claim** — "the instrument for Objective 3's readability floor, a necessary condition, not a test of the objective." Then name an instrument for the positive half or say plainly it is judged, and add "or more accessible" to §6's tier rule. **(P0-3)**
4. **Reconcile §7 Part A's "whether to build the connection" with §7 Part B's "not optional."** **(P1-1)**
5. **§7 Part B's continuity-regression bullet** — state what the parity failures actually measure (the record layer's fidelity, per the assemblers' own docstrings), add the "deliberately temporary" caveat to "read cold," and require the instrument's *promotion* to a standing pre-merge gate rather than saying flatly it is not new. **(P1-2)**
6. **Re-source the `over_settling` cost claim to the Decision Log**, in both §7 and §8. **(P1-3)**
7. **Reconcile §5(B)'s "at least a quarter" with §7's retraction**, and restore "its form" to the sustained-disagreement probe in the licence. **(P1-4, P1-5)**
8. **Sweep the P2s** — starting with `parameters.yaml:102`, now in its fifth round, and the three-acceptance-worlds undercount.
