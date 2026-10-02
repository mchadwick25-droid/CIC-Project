# Adversarial review (round 5): `CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md`

*Opus review, dispatched 2026-08-07 at Mark's explicit request as a **full** round, not a targeted one — the fifth adversarial pass on this document, run immediately before its Fable thread. Rounds 1 (`..._Round1_2026-08-06.md`), 2, 3, 4 and the targeted re-check (`..._TargetedRecheck_2026-08-07.md`) were read in full first, in order, per the Standard Practice's point 4, before any new hunting began.*

*Named failure mode hunted, per point 5, in the refined form the targeted re-check established: **a correction is not applied until the document has been grepped for the corrected claim's own vocabulary, not just fixed where a review quoted it — and a correction that requires asserting a replacement fact is new positive prose, carrying new-prose risk regardless of the commit's stated discipline.** Applied to four unreviewed commits, plus one the targeted re-check deliberately left out of scope.*

*Scope note the dispatch did not have. The targeted re-check was scoped by Mark to commit `1a142908` alone and says so in its own header: "the rest of the document was deliberately not re-reviewed." Two commits landed **before** it and outside that scope — `2aa12b15` ("Open the governance/monitoring layer to full scrutiny," **983 added words**) and `bf57fcda` (the matching launch-prompt update, 126 words). **Neither has ever been read by any review round.** So the unreviewed surface this round covers is five commits, not four: 2,124 added words across `2aa12b15`, `bf57fcda`, `bf08b68f` (726), `2719177e` (160) and `102193d2` (129).*

*Verification method: `wrs/views/permanent_prompt.py` read at `build_context()` and `main()`, not at its docstring; `wrs/views/segments/__init__.py` and `segments/world_ground.py` read to see what the loaded records are actually used for; all six `capsule_prompt_views` assemblers' docstrings read; `probe_parity.py` read at its `DEPLOYED`/`GENERATED` constants and grader prompt; all six committed `*_probe_parity_result.json` parsed directly; both Desert staging prompts byte-sized and diffed. Every reference to `readability_check` and `gate_readability` re-enumerated repo-wide from scratch. `_detect_drift_signal` and `_over_settling_signal` read at their call sites in `nodes.py`; `facilitator_prompts.py` read line-numbered across the screen and adjudication prompts; `confirmed_glosses.py` checked for LLM calls. All 118 lexicon and 60 story chunks re-measured by **executing the real serialisation path** (`content.split("---", 2)[2]` → `truncate_at(body, KEY_SOURCES_MARKERS)` → `excise_section(body, QUICK_MEANING_MARKERS)`) with `sections.py` loaded by `importlib` and a section scan handling both `## Heading` and `**Label:**` conventions. All six permanent prompts read at every cited line and string-matched for both carve-out blocks. `CiC_L1_Constitution_V2_2.docx` and the Vision docx extracted fresh from `word/document.xml`. `wrs/parameters.yaml` and `state.py` read at the cited ranges. `Decision-Log.md` read line-numbered. All **100** internal `§N` pointers extracted programmatically and resolved by hand. The launch prompt read in full.*

---

## Bottom line

**Not ready to send.**

The corrections in `bf08b68f` are, again, mostly excellent, and the two hardest facts in the document survived independent re-derivation with nothing to correct. I enumerated every `readability_check` reference in the repository from scratch and the brief's §7 Part B account is **exact in every particular** — definition at `gates/core.py:211`, the `gate_readability` wrapper at `:244` with zero callers anywhere, `plain_explanation.py:174-175`, three fixtures in `run_gates.py:139-141`, and no path to a prompt, capsule, record or turn. I parsed all six committed parity results and they read **Desert PASS, PAHC PASS, Alexandria FAIL, Hieronymian FAIL, IJC FAIL, Syriac FAIL** — world for world as the brief states. I re-measured every chunk by executing the serialisation path and §5(B) reproduces exactly: **118 lexicon chunks, 107 with a real `Ecological Function` section, 11 without (Alexandria 5 / IJC 2 / PAHC 2 / Syriac 2), 6 with no `Key Sources` marker at all, 118/118 `Distortion Risk`, 60/60 `Formation Ecology Connection`, 0/60 story `Distortion Risk`.** The witness-not-recruitment correction is **internally consistent across every site in both files** — seven occurrences in the brief, one in the launch prompt, no survivor anywhere describing the block as untouchable-word-for-word or as an unresolved open question. Structural health held: balance ratio **47.1 / 52.9**, the ask side ahead for the second round running.

But **five send-blocking defects remain**, and they fall exactly where the standing rule predicts.

**In the never-reviewed governance commit `2aa12b15` (1):**

- **§4 asserts that `drift_detection`'s twenty declared signal types are "each a real classifier call."** It is **one** LLM call per turn (`nodes.py:1936`), returning at most one finding — the code says so in its own comment, the `parameters.yaml` block the same paragraph cites decomposes the 20 as "10 monitor signals + anachronism alias + over_settling + 5 table-level checks," and the Decision Log's own cost table counts drift detection as one of ten invisible calls. A ~20× cost overstatement, sitting in the one paragraph that charges Design to cut live safety mechanisms on cost grounds.

**In the new general-rule commit `102193d2` (1):**

- **The new §4 general rule is stated in unqualified mechanism-level terms and collides with every mechanism-level protection this document has built over four rounds.** *"Every mechanism, check, gate, or block that shapes how a voice gets built or how a conversation actually unfolds is available to redesign, replace, or remove"* — against §4's own *"do not edit, shorten, or soften any of the four under any framing"* for the fabrication-guard blocks, §7's *"stays completely untouched, word for word (§4, no exception),"* §7's *"fabrication-rate tracking… not a candidate for dropping,"* §7's protection of Article 30's three-level mechanism, and §4's own instruction to preserve "A Turn Has a Measure" deliberately. Worse, the rule makes *being named untouchable* the only thing standing between a mechanism and removal — and the document now carries **three different, non-matching enumerations** of what is named untouchable, one of which omits the very item Mark just corrected.

**In the fix commit `bf08b68f` (2):**

- **The replacement fact is wrong about `/gravity/`.** The brief now states *"the fields `build_context()` actually reads; `/gravity/` and `/force/` are not part of this assembly path."* `build_context()` loads `gravity` at `permanent_prompt.py:49`, and `segments/world_ground.py` declares its sources as *"world_core + gravity records via craft paras 3-6,18,19."* `/force/` is genuinely not read; `/gravity/` is. This is a replacement fact asserted in the sentence that corrected a replacement fact — and it contradicts the very review it was applying, which listed `gravity` among what `build_context()` reads.
- **The readability correction landed at four of five sites, not five.** The commit message names "Sections 4, 6, 7 × 2, 8, 9." The diff contains **no §6 hunk.** §6 Objective 3 still tells Research to *"confirm whether `readability_check` has ever actually been run against her current prompt and what it returned"* — the exact site the targeted re-check listed as P0-1(e) — and it now directly contradicts §9 task (c), which the same commit rewrote to say that *"isn't the open question anymore."* Objective 3's Albina decision gate is built on a question the document elsewhere declares closed.

**Never checked by any round, because no round has grepped outward from the brief (1):**

- **The Decision Log — which §3 makes mandatory reading *before* §5 — still records the pre-correction scope decisions**, and §3's supersession note cannot reach them. `Decision-Log.md:37-40` lists *"what stays untouched (world/source content, the fabrication-guard **and witness-not-recruitment blocks, governance**, confirmed glosses…)"*; `:51` says `over_settling_adjudication` is *"explicitly not bundled into the voice rebuild."* Both are now false, both are the two largest scope changes of the last 48 hours, and both sit **outside** the entry's findings list, which is all §3's blanket supersession covers. The same entry's own superseding note (`:31`) also still says *"whether that gate has ever been run against the six builds is still an open question"* — answered by the brief's own §7 Part B.

**Cross-reference integrity: 100 internal `§N` pointers, up from 88. 93 resolve cleanly. One does not resolve at all** — Objective 1's *"proactive memory surfacing finding (§3)"*, round 3's break, now unapplied for a third round. **Six more resolve to a section that does not say what they cite it for**, two of them new in these commits.

**Completeness map, counted fresh.** `uptake`, `assistant register`, `brevity`, `word count` and `turn length` still appear **zero** times anywhere. `callback` and `memory` appear once each, both in §6, zero in §7/§8/§9. `transparen` now appears once in §7 (progress — it is in the protected list) and still **zero** in §8. `16-trait` appears once, in §7, never in §8 — fifth round. The single occurrence of `disagree` in §7 is still inside the droppable list, still without the "its form" qualifier the targeted re-check asked for. `trait rubric` appears zero times, while §3 states the trait-rubric-first relationship as the one unanimous finding across every source.

**Where the growth went.** The document is now **12,088 words** across §1–§9 by my count (round 4 measured 10,350 by a slightly different tokenizer that reads unchanged sections ~1–4% lower, so real growth since round 4 is roughly +15%). It is concentrated almost entirely in two sections: **§4 grew +643 words (+60%)** and **§7 grew +808 (+42%)**, against §5 at +10 and §6 at +28. §4 is now the second-largest section in the brief and 60% larger than when any round last checked it — and every word of that growth arrived in the three commits reviewed here for the first time.

None of the five is a writing problem. All five would propagate. Two of them would send Design to remove a live safety mechanism on a false premise, and one would let a Fable reader conclude the fabrication-guard block is rebuildable.

---

## P0 — fix before sending

### P0-1. The readability correction was applied at four of five sites. §6 Objective 3 still asks Research a question §9, rewritten in the same commit, says is closed — and Objective 3's Albina decision gate hangs on it.

The targeted re-check's P0-1 named five sites by line: §8 (a), §4:233 (b), §7 Part A's per-world bullet (c), §9 task (c) (d), and **§6 Objective 3 (e)**. `bf08b68f`'s message claims all five: *"applied at all five sites that previously asserted or implied it was already connected (Sections 4, 6, 7 x2, 8, 9)."*

The diff's hunk headers are `@@ -195`, `@@ -269`, `@@ -724`, `@@ -785`, `@@ -844`, `@@ -873`, `@@ -994`, `@@ -1130`. **There is no §6 hunk.** Sites (a)–(d) are genuinely fixed and verify clean (see *What verified clean*). Site (e) is untouched.

> §6 Objective 3, lines 703–708, unchanged: *"**§9's Research stage should confirm whether `readability_check` has ever actually been run against her current prompt and what it returned**, and Design should make this decision explicitly and name it, rather than the gate silently failing her (or silently never being run on her) while this objective still reads as settled."*
>
> §9 task (c), lines 1169–1176, rewritten by the same commit: *"`readability_check` (§7 Part B) is confirmed not currently wired to any voice output, so **'has it been run against the six current builds' isn't the open question anymore** — the real one is what it returns once Design wires it, specifically against Albina's rebuilt prompt."*

**Why this blocks.** These are not two loose statements; they are a pointer and its target. §6 sends Research to §9 to answer a question; §9 says the question is closed and names a different one. §6 also still contemplates *"the gate silently failing her (or silently never being run on her)"* as the risk — but per the correction the gate **cannot** run on her without new code, so the "silently never being run" branch is the only one available and it is not a silence to guard against, it is the current state.

The consequence lands on the one decision §6 declares a values call this brief cannot make unilaterally. §6's tension is derived from Albina's **23.6 words/sentence**, which is her *pilot output*. §9 now points the gate at *"Albina's rebuilt prompt."* Round 4 measured her **current prompt** at 20.6 w/s, 1.444 syl/word → **FK 9.5, inside the band**. So §6 asks Research to confirm a run that cannot happen, on an artifact §6 does not name, whose two candidate readings give opposite verdicts, and §9 now names a third artifact (the rebuilt prompt) that does not exist yet. Design meets this at the top of world #1.

This is the third consecutive round in which a §6/§8-or-§9 readability statement was corrected on one side and left standing on the other (round 3 P0-5 → round 4 P0-6 → targeted re-check P0-3 → here). It is also the first time the *correcting commit's own message* asserts the site was fixed. Trusting a commit message is exactly what the Standard Practice's point 1 forbids, and this round's dispatch said so.

**Fix.** Rewrite §6:703–708 to match §9: *"§9's Research stage wires `readability_check` to voice (§7 Part B — it is not wired today) and runs it against Albina specifically. Name which artifact the number is taken from — permanent prompt, capsule, or live output — because they do not agree: her current prompt measures inside the band and her measured output does not."* Then re-grep: the corrected claim's own vocabulary is *"has ever been run" / "confirm whether"*, and both should return zero hits after the edit.

---

### P0-2. §4's new general rule is stated in unqualified mechanism-level terms and opens, by its own words, every mechanism this document spent four rounds protecting — including the fabrication-guard block.

Brief §4, lines 186–198, entirely new in `102193d2` and never checked by anyone:

> *"**Stated as the general rule this whole section follows, not just for governance… : founding principles and the outcomes already agreed to are solid — how the program gets there is open.** Concretely: the worlds themselves (source content, already covered above) are not open. Representative creation and voice interaction are — **every mechanism, check, gate, or block that shapes how a voice gets built or how a conversation actually unfolds is available to redesign, replace, or remove**, provided the outcome it exists to protect still holds. **Nothing in this rebuild is tied to a specific enforcement protocol by default, including protocols this brief itself names or proposes** — the requirement survives; the particular mechanism enforcing it today does not automatically."*

The generalisation is the right instinct and it is Mark's own call. The phrasing is not scoped, and it collides in four places.

**1. The fabrication-guard block.** §4, one bullet below (lines 204–211): *"the near-verbatim shared 'museum guide' fabrication-guard block… **Do not edit, shorten, or soften any of the four under any framing.**"* §7 Part A, line 876–877: *"The fabrication-guard block stays completely untouched, **word for word (§4, no exception)**."* A fabrication-guard block is, precisely, "a block that shapes how a voice gets built." Under the general rule it is available to replace provided no-fabrication still holds. Under its own bullet it may not be touched **under any framing**. The document gives no resolution rule, and the newer statement is the one that announces itself as governing "this whole section."

This is not a hypothetical reading. It is the *identical* reasoning the same commit-series just licensed for the neighbouring block: the witness-not-recruitment block is now rebuilt fresh because *"its current wording is one implementation of the fixed requirement, not the requirement itself."* A builder applying the general rule consistently reaches the same conclusion about the museum-guide block — and §2 calls no fabrication the one thing that does not move, "stated by Mark twice."

**2. Fabrication-rate tracking.** §7's licence, lines 801–803: *"Fabrication-rate tracking is the only real instrument for Objective 4, one of this brief's two non-negotiables — **not a candidate for dropping**."* The general rule: *"Nothing in this rebuild is tied to a specific enforcement protocol by default, **including protocols this brief itself names or proposes**."* Fabrication-rate tracking is a protocol this brief proposes, enforcing an outcome. Round 4's P0-4(1) blocked on exactly this hole; the targeted re-check confirmed §7's rewrite cured it; the general rule re-opens it one section earlier and one level of generality up, where it is harder to see.

**3. Article 30's three-level transparency.** §7, lines 816–819: *"the existing three-level transparent-sourcing **mechanism** (§6 Objective 4 calls it 'not separable' from no-fabrication — **protected for the same reason fabrication itself is**)."* Explicitly protected *as a mechanism*. The general rule says no mechanism is fixed by default.

**4. "A Turn Has a Measure."** §4, lines 313–316: *"§7 Part A's edit **has to preserve 'A Turn Has a Measure' deliberately**, and every new instruction §7 Part A adds pushes length upward against exactly this ceiling."* Round 3 called this "the highest-consequence fix, because it protects the one paragraph most likely to be deleted by accident." The general rule now makes it a block available to remove provided turn-length discipline still holds — in a document with **zero** occurrences of `assistant register`, `brevity`, `word count` or `turn length`, and no turn-length instrument in §8. The one existing brake is now explicitly droppable, and nothing would measure its absence.

**The mechanism that makes this dangerous: three non-matching lists of what is named untouchable.** The general rule's safety valve is the intro's *"except where a mechanism itself is named untouchable below"* — so everything depends on the naming being consistent. It is not:

| Enumeration | Contents |
|---|---|
| §4 intro, lines 170–171 | world/source layer's content; no-fabrication apparatus; historical fact |
| §7 Part A licence, lines 814–818 | no-fabrication apparatus; witness-not-recruitment **requirement**; three-level transparent-sourcing mechanism |
| Launch prompt, line 22 | fabrication-guard blocks (word for word); world/source layer's content; historical fact; witness-not-recruitment requirement |

Five distinct items across three lists; **no list carries more than four of the five.** §4's intro — the list the new general rule points back to as "already covered above" — omits the witness-not-recruitment requirement entirely, which is the item Mark corrected two commits ago and which §4's own bullet calls *"the same tier as no-fabrication."* The launch prompt omits three-level transparent sourcing. §7 omits the world/source layer and historical fact.

A builder reading §4's intro list plus the general rule's binary — *"the worlds themselves are not open. Representative creation and voice interaction are"* — puts the witness-not-recruitment requirement on the open side, because it is neither in the intro's list nor "source content," and it is unambiguously something that "shapes how a conversation actually unfolds." That is precisely the error the previous commit exists to prevent.

**Two smaller collisions in the same paragraph.** *"The worlds themselves (source content) are not open"* reads as re-closing World Capsule Core prose style, which §4 bullet 1 and §7 Part A both put explicitly **in** scope and which is half of every per-world pass. And *"voice interaction"* is named open without the Interview-mode qualifier, against §3's explicit 2026-08-07 sequencing decision and the launch prompt's *"Do not expand scope."*

**Fix.** Three edits, all small. (i) Add the exception to the universal sentence: *"…available to redesign, replace, or remove — except the mechanisms this section names untouchable, which are fixed as mechanisms and not only as outcomes: the fabrication-guard blocks word for word, and the three-level transparent-sourcing mechanism (§7)."* (ii) Make §4's intro list complete and make it the single canonical list the whole document and the launch prompt point at — five items, named once, cited from §7 and the launch prompt rather than re-enumerated. (iii) Say plainly that the general rule does **not** license dropping fabrication-rate tracking or "A Turn Has a Measure," or, if it genuinely does, say so deliberately and give §8 a turn-length instrument first.

---

### P0-3. `build_context()` does read `/gravity/`. The replacement sentence written to fix a replacement-fact error contains a new one, and contradicts the review it was applying.

Brief §7 Part A, lines 743–748, new in `bf08b68f`:

> *"It starts from that world's actual source records — `wrs/records/<world>/source/`, `/term/`, `/story/`, `/contested_claim/`, `/figure/`, `/demonstration/`, `/voice_profile/`, and `/world_core/` (**the fields `build_context()` actually reads; `/gravity/` and `/force/` are not part of this assembly path**…)"*

Read at source, `wrs/views/permanent_prompt.py:43-54`:

```
def build_context() -> dict:
    return {
        "terms": load_records("term"),
        "stories": load_records("story"),
        "claims": load_records("contested_claim"),
        "figures": load_records("figure"),
        "gravities": load_records("gravity"),          # <-- read
        "world_core": load_records("world_core")["desertcore001"],
        "voice_profile": load_records("voice_profile")["desertvoice001"],
        "sources": load_records("source"),
        "demonstrations": load_records("demonstration"),
    }
```

`gravity` is loaded. `force` is not — that half is correct. And the gravity records are not merely loaded and discarded: `wrs/views/segments/world_ground.py`'s `SEGMENT` declares `"sources": "world_core + gravity records via craft paras 3-6,18,19 (coverage-mapped)"`, and `world_ground` is second in `ASSEMBLY_ORDER`. So gravity records feed the segment that carries the world's own ground into the assembled prompt.

The targeted re-check, which this commit was applying, listed it correctly: *"`build_context()` loads `term`, `story`, `contested_claim`, `figure`, **`gravity`**, `world_core`, `voice_profile`, `source`, `demonstration`."* The fix dropped `gravity` from the list *and* added an affirmative denial that it is part of the path.

**Why this blocks.** This sentence is the one that tells Design what "clean rebuild from sources" means and which record directories to open. It names the source layer for six per-world rebuilds. Excluding `gravity` is not a trivial omission: the gravity records are the world's organising-force analysis, they are what `world_ground` renders from, and §5(B)'s entire build-process-leak finding is about *gravity-analysis vocabulary* reaching a participant. A mandate that tells Design gravity records are outside the assembly path, in a brief whose §5 warns that gravity vocabulary is the main thing leaking, invites exactly the wrong inference — that gravity material is already excluded by construction, when in fact `permanent_prompt.py`'s own docstring says gravity codes are stripped *by the shared apparatus-stripping helper* while the gravity *content* is rendered into prose.

It is also, structurally, the fourth consecutive instance of the same class: a claim about what a cited tool reads, asserted without opening the function body. The targeted re-check named this the one fix requiring a replacement fact and said *"that is the one to check again afterward."* It was right.

**Fix.** *"…`wrs/records/<world>/` — `source/`, `term/`, `story/`, `contested_claim/`, `figure/`, `gravity/`, `demonstration/`, `voice_profile/`, `world_core/` (the nine `build_context()` reads; `force/` is not part of this assembly path). Note that `gravity/` feeds the `world_ground` segment as prose, while gravity **codes** are stripped by the shared apparatus helper — the distinction §5(B)'s leak finding turns on."*

---

### P0-4. §4 states that `drift_detection`'s twenty signal types are "each a real classifier call." It is one call per turn — and the file §4 cites in the same sentence says so.

Brief §4, lines 244–249, from `2aa12b15`, never reviewed:

> *"`drift_detection` carries **twenty declared signal types** (`app/graph/state.py`'s `DriftSignal.signal_type`, confirmed by count; `wrs/parameters.yaml:116-121` records the same number and its own history…), **each a real classifier call**."*

The count of twenty is correct — I extracted the `Literal` and got exactly 20 members, `agreeing` third and `over_producing` fourth. The cost claim is not.

`app/graph/nodes.py`, `_detect_drift_signal`:

```
    llm = get_monitoring_llm()
    prompt = FACILITATOR_MONITORING_PROMPT.format(response=response_text)
    response = llm.invoke([...])
    log_llm_usage("drift_detection", response, _MONITORING_MODEL)   # nodes.py:1936
```

**One invocation, one usage record.** The module's own docstring for the finding-selector is explicit: *"Only one DriftSignal is returned per turn - every caller and the reroot path are built around that."* And the comment immediately after the call: *"The general monitor above **weighs ten signals at once** under a standing instruction to be conservative."*

The `parameters.yaml` block the same §4 sentence cites decomposes the twenty in its own `source:` field (`:119-123`): *"the 17 of Pass 1 §3.9's decomposition (**10 monitor signals + anachronism alias + over_settling + 5 table-level checks**); S4.7 added misattribution, manufactured_resolution, and closing_synthesis."* So of the twenty declared types: ten are outputs of a single monitor call, one is an alias, one is `over_settling` (which the same §4 bullet correctly describes as its own two-stage check), five are **table-level** checks that do not run in Interview mode at all, and three were added later to the same emitted space.

And the Decision Log entry §3 makes mandatory reading — the source of the cost framing this whole paragraph rests on — counts it the same way (`Decision-Log.md:63`): *"roughly ten invisible calls for every one visible reply (frame-breaker, relational-safety, **drift detection**, two Do-Not-Retrieve-When guards, citation grounding, repair classifier, a two-stage over-settling check)."* One item in a list of ten, not twenty items.

**Why this blocks.** This paragraph is not descriptive. It is a charge: *"Design should ask, for each: what specific failure does this actually catch… is there a cheaper mechanism… and if the honest answer is 'we still need this exact mechanism,' say so with the reasoning stated, not by default."* The whole evaluation turns on real cost against real catch. Overstating `drift_detection`'s per-turn cost by roughly twenty times, in the sentence that hands Design the cost side of the ledger, is the most decision-relevant factual error available in this section — and it points toward removing a safety monitor that includes `FLATTENING`, the one signal §4 itself says needs empirical watching **because a register rewrite might trip it**. §7 Part B and §8 then build a per-signal drift breakdown on top of the same twenty, which is right for the *type space* and wrong for the *call count*.

There is a second, smaller error in the same bullet, in the sentence immediately before: *"`over_settling` runs in two stages, the second an expensive full-context re-send (`app/prompts/facilitator_prompts.py:241`)."* Line 241 is inside `OVER_SETTLING_SCREEN_PROMPT` (declared at `:224`) — the **first** stage — and reads *"Do NOT clear a claim for sounding measured… Tone is not a limit."* The second stage is `OVER_SETTLING_ADJUDICATION_PROMPT` at **`:261`**, and it is the one taking `{permanent_prompt}`, `{capsule}`, `{retrieved}`, `{response}`. The substance is true and well-supported by the Decision Log; the citation was carried over from the pre-`2aa12b15` sentence, which used `:241` correctly for a different claim, and was re-pointed at a claim it does not support. See P1-5.

**Fix.** *"`drift_detection` is a single monitor call per turn (`nodes.py:1936`) that weighs ten signals at once and returns at most one finding; the twenty declared `signal_type` values (`state.py`; `wrs/parameters.yaml:116-130`) are the emitted **type space** — ten monitor signals, an alias, `over_settling`, five table-level checks, and three later additions — not twenty calls. Its real per-turn cost is one classifier call; `over_settling`'s is one screen plus, on 10 of 12 turns measured, a second full-context adjudication (`facilitator_prompts.py:261`), which is where the cost actually is."* That sharpens the charge rather than weakening it — it points Design at the mechanism that is genuinely expensive.

---

### P0-5. The Decision Log, which §3 orders read before §5, still records the pre-correction scope for both of the last 48 hours' scope changes — and §3's supersession note is scoped to the findings list, which does not reach either statement.

§3, lines 60–75, tells Fable to read `Decision-Log.md`'s 2026-08-05 entry and then says: *"**Treat that entry's entire findings list as superseded**, not just the two lines its own note marks: bullet 1…, bullet 2…, bullet 4…, and bullet 6… are all superseded by this brief's §5."*

That instruction is well-made and it covers the findings list. Three statements in the same entry sit outside it:

**(a) `Decision-Log.md:37-40`, in "What this session produced instead":**

> *"…covering the diagnosis above in full, **what stays untouched (world/source content, the fabrication-guard and witness-not-recruitment blocks, governance, confirmed glosses, retrieval ordering deferred** per Mark's own 'minor addendum' framing)…"*

Two of those four are now false and are the two largest scope decisions in the document's history. The witness-not-recruitment **block** is now rebuilt fresh (`bf08b68f`, Mark's direct correction). **Governance** — `over_settling`, `citation_grounding`, `drift_detection`, `confirmed_glosses` — is now explicitly open to full scrutiny (`2aa12b15`, Mark's direct instruction), with Design required to produce a keep/simplify/replace/drop recommendation for each. A Fable reader following §3's instruction reads the log entry first and is told, in the record of what was decided, that both stay untouched.

**(b) `Decision-Log.md:51`:**

> *"**Also handed off, explicitly not bundled into the voice rebuild:** the two scoped defects from the live-test entry above (the `CitationModal.tsx` internal-note leak; `over_settling_adjudication` firing on 10 of 12 turns) — named in the brief as Mark's own separate triage items, not folded into Friday's mandate."*

§4's own defect 2 now says the opposite: *"per the governance-layer evaluation above, **no longer out of scope by default**… Design should evaluate it as part of the governance-layer scrutiny above, not treat it as a separate, untouchable defect log entry."*

**(c) `Decision-Log.md:31`, the superseding note itself:**

> *"…already carries a numeric Flesch-Kincaid/Reading-Ease floor wired to a real gate (`wrs/gates/core.py:211`) — **whether that gate has ever been run against the six builds is still an open question**."*

That is answered. The brief's own §7 Part B establishes the gate is not wired to voice at all, so it has not been run and cannot be without new code. The log's *correction* is now itself stale, in the direction that makes the superseded bullet 5 ("the gap across six builds is enforcement, not philosophy") substantially right after all — which nothing anywhere records.

**Why this blocks.** This is the identical defect §3 spent two rounds fixing for this exact file, and the identical defect §8/§9 fixed for the review record in `1a142908` — a correction landed in the brief with superseded statements left standing in a document the brief mandates reading, with no superseding note. The targeted re-check's own refined rule says a correction is not applied until the document has been grepped for the corrected claim's vocabulary. Both correcting commits grepped the *brief*; `2719177e` grepped one further document; nobody grepped the Decision Log, where the string "witness-not-recruitment blocks… governance" sits in the record of decisions.

It matters more than a stale line usually would because §4's own new general rule (P0-2) makes "named untouchable" the load-bearing test, and the Decision Log names four things untouchable that §4 no longer does.

**Fix.** Add a second dated superseding note to the 2026-08-05 entry covering the *whole* entry, not the findings list: the witness-not-recruitment block is rebuilt fresh (requirement fixed, block open); the governance/monitoring layer is open to full evaluation; `over_settling_adjudication` is in scope for that evaluation; and the readability gate is not wired to voice, which closes the note's own open question. Then change §3's instruction from *"treat that entry's entire findings list as superseded"* to *"treat that entry's scope statements as superseded too — §4 is current, not the log."* And add the same check to the process: grep the workstream folder, not only the brief.

---

## P1 — materially improves, not disqualifying

### P1-1. §7 Part A's governing paragraph is now a broken sentence, with four sentences of correction spliced between its subject and its verbs.

Lines 741–760, as `bf08b68f` left them:

> *"It starts from that world's actual source records — `wrs/records/<world>/source/`, … three of the six worlds). **One real correction, not a restatement: `wrs/views/permanent_prompt.py` does not currently assemble the deployed prompt** — it writes a separate staging file…, is hardcoded to Desert…, and the other five worlds' record-to-prompt assemblers each open with their own `DELIBERATELY TEMPORARY` marker. `wrs/views/probe_parity.py` is what compares that assembled-from-records output against the real deployed prompt — and, per §7 Part B, four of six worlds already show that comparison failing. The records above are still the right thing for Design to build from; they are not yet what the live system actually runs on — **and from this brief's own principles (§1, §2, §6), and writes the *prose, register, and delivery* fresh.**"*

The main clause is *"It starts from that world's actual source records… and from this brief's own principles…, and writes the prose, register, and delivery fresh."* Roughly 150 words and four complete sentences now sit between the two halves. What a reader actually meets, after a full stop, is *"and from this brief's own principles (§1, §2, §6), and writes the prose, register, and delivery fresh"* — a fragment with no subject.

This is the paragraph the brief says *"governs the per-world bullet below specifically"* and the launch prompt says *"governs everything."* Round 4 rated a broken sentence in §6 Objective 3 as a P0 component; this one's meaning is recoverable, so it is P1 — but it is the mandate, it is newly broken, and it is one restructure to fix: close the source-list sentence, then start the correction as its own paragraph.

### P1-2. The brief attributes the parity comparison's generated side to `permanent_prompt.py`. For five of six worlds it is a different assembler, and for Desert the default is a materially different file.

> §7 Part A, lines 754–756: *"`wrs/views/probe_parity.py` is what compares **that** assembled-from-records output against the real deployed prompt."*

"That" refers to `permanent_prompt.py`'s staging file. Read at source, `probe_parity.py:33-38`:

```
DEPLOYED  = BACKEND/"data"/"desert_world"/"desert_Representative_Permanent_Prompt_Papnoute.txt"
GENERATED = (Path(sys.argv[1]) if len(sys.argv) > 1
             else STAGING/"desert_world"/"desert_Representative_Permanent_Prompt_generated.txt")
```

The default generated input is `..._generated.txt` — the output of `capsule_prompt_views.py`, the **S2.8** assembler, which opens `DELIBERATELY TEMPORARY` exactly like the other five. `permanent_prompt.py`'s output is `..._S52.txt`. Both files are committed and they are **not the same artifact**: 23,415 bytes against 14,508. The code comment allows an argv override (*"the S5.2 P checkpoint points this at the §5.1 assembly's staged output"*), so either could have produced the committed `PASS`; nothing in the repository records which. And the five `s62_*_probe_parity.py` siblings compare against the five `s62_*_capsule_prompt_views.py` outputs — never `permanent_prompt.py`, which is Desert-only.

Two consequences the brief's sentence obscures. First, the 2-PASS/4-FAIL split is most likely an **entirely S2.8-class** comparison, which makes it a cleaner and more interpretable result than the brief implies — six worlds on the same footing, all six generated sides self-described as temporary scaffolding. Second, §7 Part B tells Design to read those results **"cold"** while §7 Part A implies Desert's side came from the "real" S5.2 assembly. Reading them cold on that premise invites attributing to voice drift what may be assembler coverage — the exact caution the targeted re-check raised as its P1-2, now half-carried (the `DELIBERATELY TEMPORARY` markers are named; their application to Desert's own compared artifact is not).

**Fix.** *"`probe_parity.py` and its five `s62_*` siblings compare each world's deployed prompt against a **staged** prompt assembled from records by the S2.8-class generators (`capsule_prompt_views.py` and its five per-world ports, every one of which opens `DELIBERATELY TEMPORARY`). `permanent_prompt.py` is the later S5.2 assembly, Desert-only, and writes a different staging file again. Read the 4-of-6 result as a measure of whether the record layer reproduces the deployed voice, not as a participant-facing continuity break."*

### P1-3. §3 still describes §4's two adjacent defects as carved out of scope; §4 says one no longer is — and §4's own defect-list header contradicts its own defect body.

> §3, line 63: *"…and the two adjacent defects (**§4**) **this brief carves out of scope**."*
>
> §4, line 317: *"**Two adjacent, already-diagnosed defects, deliberately not bundled here** — log them for Mark's own separate triage rather than fixing them as part of this thread:"*
>
> §4, defect 2, lines 326–335: *"…**no longer out of scope by default**… Design should evaluate it as part of the governance-layer scrutiny above, **not treat it as a separate, untouchable defect log entry**."*

`2aa12b15` rewrote the defect body and left both the §4 header above it and the §3 pointer four sections earlier. So the same list is introduced as out-of-scope-for-triage twice and then declared in-scope in its own second item. The targeted re-check's P2-6 caught the §4 half; the §3 half is new to this round.

**Fix.** §4's header: *"Two adjacent, already-diagnosed defects — the first for Mark's separate triage, the second now folded into the governance-layer evaluation above."* §3: *"…the two adjacent defects (§4) — one carved out for Mark's own triage, one now inside the governance-layer scrutiny."*

### P1-4. §6's tier rule still condemns §6's own readability floor.

§6, lines 609–613, untouched for three rounds: *"if a check or a rule is making conversation *more* restrictive **without making it more honest**, that's an Objective-3 failure the apparatus itself caused."*

Nine lines later §6 mandates the FK 8–10 floor *"as an access requirement, not a style suggestion."* The floor is more restrictive and is justified by **access**, not honesty. Under §6's own test, §6's own floor fails — and the general rule at P0-2 now supplies the licence to act on that reading. Round 4's P0-6 and the targeted re-check's P0-3 both asked for the same one-clause repair: *"without making it more honest **or more accessible**."* Unapplied.

### P1-5. The `over_settling` second-stage citation now points at the first-stage prompt.

Covered in P0-4's evidence. `facilitator_prompts.py:241` is inside `OVER_SETTLING_SCREEN_PROMPT` (`:224`) and says *"Tone is not a limit"*; the second-stage full-context adjudication is `OVER_SETTLING_ADJUDICATION_PROMPT` at `:261`, assembled at `nodes.py:2263`. The pre-`2aa12b15` text used `:241` correctly, for the screen's tone-agnosticism. The rewrite kept the line number and changed the claim under it.

*Worth recording as a genuine repair alongside it:* round 4's P0-4(6) and the targeted re-check's P1-3 both blocked on §7 citing §4 for a cost ranking §4 did not make. **§4 now makes it** (lines 242–243, *"the single largest invisible cost line item after the main response itself"*; and again at 327–328), and it verifies against `Decision-Log.md:63` — *"Second-biggest line item in the whole cost table, ahead of every other invisible check combined,"* with `main_response` at ~65% of cost. That finding is now correctly sourced. It was fixed as a side effect of `2aa12b15`, not deliberately, but it is fixed.

### P1-6. §5(B) still states a leak count §7 says is not trustworthy enough to state.

> §5(B), line 404: *"**at least a quarter of the 107 Ecological-Function chunks** carry internal build-process language."*
>
> §7 Part A, lines 838–842: *"an attempt this session to enumerate the full scope produced two different counts from two different checks and **neither is trustworthy enough to state as fact here**… A full leak audit across all 118 lexicon and 60 story chunks is a genuine, unfinished Research-stage task."*

The retraction was the right judgement and §7's version is clean — I confirmed no contested count appears anywhere in §7, and the two corpus counts it does state (118 / 60) are exact on disk. But the retraction was applied in §7 only, so the document asserts a fraction in §5 and disclaims fractions of that kind in §7. Targeted re-check P1-4, unapplied. (The number is probably safe — round 4 measured 27 of 107 inside the EF field, 25.2% — so the fix is epistemic labelling, not re-measurement: *"a lower-bound estimate pending §9's audit."*)

### P1-7. §5(B)'s four named leak examples are still filed under the wrong mechanism — re-derived independently this round.

§5(B), lines 411–413, inside the paragraph headed *"Two distinct leaks, not one"*, lists as instances of the **first** leak (build language inside an `Ecological Function` field): *"`Related-Terms Reciprocity Note` in Yausep's `syrlex005`/`syrlex008`, `Confidence: Inferential-Thin` in Chloe's `pahclex012`/`pahclex013`."*

Measured by executing the real path: all four are among the **11 chunks with no `Ecological Function` section at all**, and all four are among the **6 with no `Key Sources` marker** — i.e. all four are instances of the *second* mechanism, described in the next paragraph without naming them. A reader opening `syrlex005` to check will find no such field. Round 4's P1-3, unapplied.

Also in the same paragraph, still: *"their entire body, including trailing internal notes, reaches the model verbatim"* — `excise_section(body, QUICK_MEANING_MARKERS)` runs for all six migrated worlds, so Quick Meaning is removed. *"Everything after the last content section"* is the accurate form.

### P1-8. The completeness holes are unchanged, and one of them is now made worse by the general rule.

Counted fresh across the whole document:

| Term | Total | §7 | §8 | §9 |
|---|---|---|---|---|
| `callback` | 1 (§6) | 0 | 0 | 0 |
| `memory` | 1 (§6) | 0 | 0 | 0 |
| `uptake` | **0** | 0 | 0 | 0 |
| `assistant register` / `brevity` / `word count` / `turn length` | **0** | 0 | 0 | 0 |
| `transparen` | 5 | 1 (protected list) | **0** | 0 |
| `16-trait` | 1 | 1 | **0** | 0 |
| `trait rubric` | **0** | 0 | 0 | 0 |
| `disagree` | 6 | 1 (droppable list) | 1 | 1 |

- **Objective 1's callback half** — no deliverable, no instrument, no Research task, and its `(§3)` pointer is still the document's one unresolvable cross-reference. `10_..._Realness_Study:47` names it, supplies the exact mechanism, and says it *"needs zero new infrastructure, just prompt guidance."* Round 3 P1-1 → round 4 P1-5 → fifth round. Still the cheapest real win in the document, and it now directly serves Objective 3's positive half.
- **Objective 6's licensing text** — §7 still writes none, and the licence still says Design may *"drop either"* the drift telemetry or the sustained-disagreement probe. The targeted re-check's P1-5 asked for the qualifier *"its form"*; unapplied. §8 calls the probe *"the actual instrument Objective 6 needs and didn't have before this revision."*
- **Objective 4's transparency half** — now protected in §7 (real progress), still unmeasured in §8.
- **Turn length** — this is the one that got worse. §4 line 314 says *"every new instruction §7 Part A adds pushes length upward against exactly this ceiling — worth Design treating as a real tension."* The ceiling is a block; the new general rule makes blocks removable; §8 names no turn-length instrument; and doc 10's headline finding (the "assistant register" as the primary tell that breaks realness) still appears zero times. Round 2 P1-3 → round 3 P1-8 → round 4 P1-9 → fifth round, now with a licence attached.

### P1-9. The brief and the launch prompt disagree about the review record, and §9's operating rule is one generation stale.

> §8, lines 1111–1119: *"this brief has been through **four** Opus adversarial rounds as of 2026-08-07… read all four directly (`…Round1…` through `…Round4…`)… and check whether a round 5 exists before treating round 4 as the last word."*
>
> §9, lines 1225–1239: *"**Four rounds**… a stable pattern **across all four**…"*
>
> Launch prompt, lines 6–7 and 30: *"**four full Opus adversarial rounds plus a targeted re-check**… Read all four review files **plus the targeted re-check** (`…Round1…` through `…_TargetedRecheck_2026-08-07.md`)."*

`..._TargetedRecheck_2026-08-07.md` is committed (`9f2096db`) and is the document whose three P0s `bf08b68f` was applying. The brief never names it. A reader following §8's instruction literally looks for a "round 5," does not find one, and never learns the re-check exists — while the launch prompt tells them to read it. Two documents Fable reads give different accounts of the scrutiny this brief has survived.

§9's stated operating rule is also the round-4 version — *"corrections that delete or re-point hold up clean; new positive prose has reliably contained new errors"* — without the re-check's own refinement, which is precisely what this commit series needed: **a correction requiring a replacement fact is new positive prose, and a correction is not applied until every site carrying the claim has been grepped.** P0-1 and P0-3 are both instances of exactly the clause that is missing.

This is round 4's P0-7 in a milder form — the four named files are current and not falsified, so it is P1 rather than P0 — but it is the same shape, one artifact later.

**Fix.** §8 and §9: *"four Opus adversarial rounds plus a targeted re-check, 2026-08-06 to 2026-08-07; read `…Round1…` through `…Round4…` and `…_TargetedRecheck_2026-08-07.md`; check whether a round 5 exists."* And extend §9's operating-rule paragraph with the re-check's two added clauses.

---

## P2 — polish

1. **`wrs/parameters.yaml:101-114` should be `:102-114`**, at §7 Part B line 933 and §8 line 1029. Verified again: line 101 blank, `reading_floor:` at 102, block ends 114. **Sixth round running.**
2. **§4's `wrs/parameters.yaml:116-121` is short of what it cites it for.** `drift_signal_count_emitted: value: 20` is 116–117, `source:` runs 118–123, and the FLAG-016 history §4 cites lives in `notes:` at **124–130**. Also "ten" is not flagged there as stale — the file names it as a *component* of the 17. Round 3 P2-2 → round 4 P2-2, unapplied.
3. **§3's "the two lines its own note marks" is wrong; the log's note marks three.** `Decision-Log.md:31` supersedes bullet 1, bullet 4 **and bullet 5**. §3's own list (1, 2, 4, 6) also omits 5. Round 3 P2-3 → round 4 P2-3 → **fifth round**. Net effect still safe because of §3's blanket instruction — but see P0-5 for why the blanket is now doing more work than it can bear.
4. **§3's "(its own line 59 says so directly)" is now off by twelve.** The transcripts sentence is `Decision-Log.md:71`; line 59 is now *"**Mark's ask:** run real conversation tests…"*. Round 2 corrected this pointer from 57 to 59; a new log entry has since been prepended and moved it again. Line-number citations into an append-at-top log will keep drifting — cite the entry and its own bolded label instead.
5. **§5(A)'s Marius quote is still a reversed-order composite.** Brief: *"one short sentence for the first fact. A full stop… Each one short enough to stand alone."* At `ijc_..._Marius.txt:117`, verified again this round, *"Each one short enough to stand alone"* comes **before** *"one short sentence for the first fact. A full stop."* Round 2 P2-3 → **fifth round**. Worth naming every time, because composite quoting is a P0-class failure in this project's own history.
6. **§5(A)'s Theon quote still truncates silently.** Brief: *"You land one thing, and stop."* Actual (`:37`, verified): *"You land one thing, and stop, **and begin the next fresh**."* Fifth round.
7. **§5(C) still says "four separate points," then names a fifth** (lines 470, 490); §7 Part A line 850 repeats "four." The four include one per-world copy (Chloe) and exclude the other (Marius), which is then introduced as "a fifth." Round 2 P2-5 → fifth round.
8. **"a test fixture" (§7 Part A, line 796) vs "three fixtures in `wrs/gates/run_gates.py`" (§7 Part B, line 940) vs "test fixtures" (§8, line 1032)** — one fact, three renderings. Three is correct. Targeted re-check P2-2, unapplied.
9. **"both of §7's own lead acceptance worlds (Albina, Marius)" undercounts** (§7 Part B, line 988). §8 lines 1084–1087 names **three** primary acceptance worlds — Albina, Marius **and Yausep** — and Syriac is also a FAIL. **All three acceptance worlds fail parity**, which is a materially stronger finding than the brief states. Targeted re-check P2-3, unapplied.
10. **§7 Part B line 929 still says "the exact guidance §6/§7 believed they were inventing for Albina."** §6 now quotes that Part Five sentence approvingly *and* says its operational reading does not work. Round 2 P0-7 → round 3 P2-5 → round 4 P2-4 → fifth round.
11. **§4 line 250–252 retains "All three are content- or posture-based, not register-based"** for a twenty-type space that includes `length_ceiling` and `question_stacking`. `length_ceiling` is register/length by definition and is never named in the brief. Round 2 → fifth round.
12. **§7 Part B's Part Eight bullet (line 960) lists four instruments; §8 lists seven** — and lists `readability_check` among them with no note that it is unwired to voice, twenty lines after §7 Part B establishes exactly that. Round 2 P2-6 and targeted re-check P2-9, both unapplied.
13. **§8 line 1047's "expensive-but-expected" is now half-resolved.** §4 does now name the cost (P1-5), so "expensive" resolves. §4 still frames the 10-of-12 rate as a defect (*"not a rare safety net in practice"*), never as expected — round 1's P1-9 point (the screen is deliberately tuned to over-flag, so a high rate is the architecture working) has never been applied to §4. Round 3 P2-9 → fifth round for the "expected" half.
14. **§8 line 1097's "(5 of 11 project-wide, finding B)" cites finding B for a distribution finding B does not state.** The figure is exact (Alexandria 5 of the 11, re-measured this round); §5(B) names only the two IJC chunks and never gives the per-world split. Either add the split to §5(B) — Alexandria 5 / IJC 2 / PAHC 2 / Syriac 2 — or drop the "finding B" attribution.
15. **§4's new general rule says "the same distinction already applied *above* to witness-not-recruitment."** The witness-not-recruitment bullet is **below** it (lines 212–231); what is above is the governance framing. A reader looking up finds the wrong case.
16. **The staging path is quoted from a docstring that is itself imprecise.** §7 Part A says `permanent_prompt.py` writes `staging/desert_Representative_Permanent_Prompt_S52.txt`; `chunk_views.py:32` sets `STAGING = HERE/"staging"/"desert_world"`, so the real path is `staging/desert_world/desert_Representative_Permanent_Prompt_S52.txt`.
17. **§4's "The world/source layer's content" bullet and the general rule's "the worlds themselves are not open" pull against §7's capsule scope.** Bullet 1 carves out capsule *prose style* correctly; the general rule's summary does not repeat the carve-out, and capsule prose is half of every per-world pass.
18. **`over_settling`'s own screen prompt records that it was "first tried as one signal among ten in a general drift monitor and caught nothing"** (`facilitator_prompts.py:228`) — direct, measured evidence bearing on §4's "is there a cheaper mechanism (a lighter check, a sampled check, a single-stage check instead of two)" charge, sitting in the file §4 cites. Worth carrying into §4 so Design does not re-run an experiment the project already ran and logged.

---

## What verified clean

Stated plainly, because the corrections in `bf08b68f` are good and two of them are now among the best-sourced statements in the document.

**`readability_check` is not wired to Representative voice. Re-enumerated repo-wide from scratch, without reference to any prior round's table. Exact.**

| Site | What it is |
|---|---|
| `wrs/gates/core.py:211` | the definition |
| `wrs/gates/core.py:244` | inside `gate_readability` — **zero callers anywhere**; its only other mentions are two audit documents and a Task Board line recommending it be pointed at participant-facing surfaces |
| `wrs/views/plain_explanation.py:174-175` | the Level-2 plain-explanation render for one lexicon term |
| `wrs/gates/run_gates.py:139-141` | three string fixtures (`READABLE_TEXT`, `UNREADABLE_LONG`, `UNREADABLE_JARGON`) |

No path reaches a permanent prompt, a World Capsule Core, a `voice_profile` record, or Representative output. §7 Part B's text is accurate in every particular, and the correction is now correctly propagated to §4:288-290, §7 Part A:794-797, §7 Part A:905-909, §8:1028-1037 and §9(c):1169-1176 — four sites the targeted re-check found unfixed, now all fixed. (§6 is the fifth: P0-1.)

**Continuity-regression testing exists, has run, and the results are as stated. Re-parsed directly from the committed JSON.**

| Result file | World | `probes_failing_both_trials` | `parity` |
|---|---|---|---|
| `probe_parity_result.json` | Desert / Papnoute | 0 | **PASS** |
| `s62_pahc_probe_parity_result.json` | PAHC / Chloe | 0 | **PASS** |
| `s62_alx_probe_parity_result.json` | Alexandria / Theon | 2 | **FAIL** |
| `s62_hal_probe_parity_result.json` | Hieronymian / Albina | 1 | **FAIL** |
| `s62_ijc_probe_parity_result.json` | Imperial-Juridical / Marius | 1 | **FAIL** |
| `s62_syr_probe_parity_result.json` | Syriac / Yausep | 2 | **FAIL** |

Six scripts committed; the grader's four axes (register / measure / refusal / vocabulary), the two-trial blind A/B design, and the *"parity holds if no probe gets DIFFERENT-VOICE on both trials"* verdict rule all verify verbatim in `probe_parity.py`'s docstring. The pass-criterion tension §7 Part B flags for Design is real and correctly identified.

**The `permanent_prompt.py` correction is right in its load-bearing half.** It writes a staging file, not the deployed prompt (`main()` writes `..._S52.txt` into `STAGING`); it is hardcoded to Desert (`load_records("world_core")["desertcore001"]`, `load_records("voice_profile")["desertvoice001"]` at `:50-51`); and every one of the other five worlds' `s62_*_capsule_prompt_views.py` opens with `DELIBERATELY TEMPORARY`, verified by reading all six docstrings. The Source Registry claim is true and I re-verified it by direct listing: `data/desert_world/sources.json`, `data/pahc_world/source_registry.json`, `data/syriac_world/source_registry.json` exist; Alexandria, Hieronymian and Imperial-Juridical have none — three of six, exactly as stated. (The `/gravity/` clause is P0-3; the attribution of the parity comparison is P1-2.)

**The witness-not-recruitment correction is internally consistent everywhere it appears, in both files.** Six sites in the brief (lines 188, 212, 221, 815, 819, 877 — a seventh hit on `witness` at line 728 is Objective 6's unrelated *"to actually witness its world"*) and one in the launch prompt (line 22), all saying the same thing: the *requirement* is fixed at the same tier as no-fabrication, from Encounter Over Persuasion; the *block* is one implementation and gets rebuilt fresh. **Nothing anywhere in either file still describes the block as untouchable word-for-word or as an unresolved open question** — I grepped both for `witness`, `recruit`, `open question` and `untouch`. §4's bullet and §7's two sites agree with each other clause for clause, and §7 correctly keeps the fabrication-guard block frozen word-for-word alongside it, so the two carve-outs are no longer conflated.

The grounding also checks out at source. `Encounter Over Persuasion` is one of exactly four **Foundational Values** in the Vision docx (with Participant Agency, Historical Responsibility, Intellectual Humility), extracted fresh from `word/document.xml` — so §4's *"it comes from the Foundational Documents (Encounter Over Persuasion, §3), settled ground"* resolves correctly against §3's own corrected list.

This correction also **retires round 4's P0-3(d)** cleanly: the objection was that freezing 190–400 words of old-register witness prose verbatim in every file would reinstall the register the rebuild removes. With the block rebuilt fresh, that residual now applies only to the fabrication-guard blocks, which are frozen deliberately and by Mark's own decision.

**§5(B)'s chunk measurements re-derive exactly, by executing the real serialisation path.** 118 lexicon chunks; **107** with a structurally-located `Ecological Function` section; **11** without — `alexlex051`, `alexlex059`, `alexlex074`, `alexlex081`, `alexlex090`, `ijclex011`, `ijclex012`, `pahclex012`, `pahclex013`, `syrlex005`, `syrlex008`, i.e. Alexandria 5 / IJC 2 / PAHC 2 / Syriac 2; **6** returning `None` from `find_section(body, KEY_SOURCES_MARKERS)` — the same six. 118/118 `Distortion Risk`. 60 story chunks, 60/60 `Formation Ecology Connection`, 0/60 `Distortion Risk`. Every number in §5(B) and §8's Theon bullet is exact.

**§5(A)'s prompt quotations re-read at their cited lines.** Papnoute `:7` exact including the semicolon; Yausep `:41` exact; Albina `:29` and Marius `:117` substantively exact (the Marius composite ordering is P2-5); Theon `:37` truncated (P2-6). `museum guide` confirmed by string match in **Yausep and Marius only**; witness-not-recruitment confirmed present in **all six**, including Papnoute `:17` verbatim as §4 quotes it and Marius's literal `SECTION 6 — WITNESS-NOT-RECRUITMENT` at `:139`.

**§1's Article 6 rendering, spot-checked fresh from the Constitution docx.** `L1-Foundation/CiC_L1_Constitution_V2_2.docx`, Article 6 (*"Encounter-Success Standard"*): *"The testable expression is the conditions the architecture created: did the encounter keep the Representative genuinely itself, protect the participant's authorship of their own direction, present the world hone[stly]…"* — §1's four-condition rendering is faithful. The Vision docx carries only the note *"Constitution Article 6 refines the testable expression of this standard"*, so §1's *"which the Vision document references directly, not authors itself"* is exact. Round 1's P2-5 fix has held for four rounds.

**§4's governance facts that do check out**, from the never-reviewed commit: `citation_grounding` is at `nodes.py:1417` and is paraphrase-tolerant content mapping; `confirmed_glosses.py` contains **no LLM invocation at all**, so *"cheap (no LLM call)"* is exact; `state.py`'s `DriftSignal.signal_type` declares exactly **20** members with `agreeing` third and `over_producing` fourth; the cost ranking traces correctly to `Decision-Log.md:63`. The charge to Design — *"what specific failure does this actually catch that a genuinely well-built, source-grounded voice wouldn't already avoid… and if the honest answer is 'we still need this exact mechanism,' say so with the reasoning stated, not by default"* — is well-constructed and is the right question. Only the per-call cost claim inside it is wrong (P0-4).

**Structural health.** Balance ratio **47.1 / 52.9** — §1 307, §2 129, §3 1,095, §4 1,708, §5 2,449 (diagnosis 5,688); §6 1,433, §7 2,742, §8 1,008, §9 1,217 (ask 6,400); total **12,088**. Round 1's 68/32 failure mode has been absent for five rounds and the ask side has now led for two. **100 `§N` pointers, 93 resolving cleanly** — one unresolvable (Objective 1 → §3) and six resolving to a section that does not support the citation (§6:703, §3:63, §8:1047, §7:929, §8:1097, §4:188).

**The launch prompt.** Read in full. Internally consistent with the brief on witness-not-recruitment, the governance opening, the readability-not-wired fact, the 4-of-6 parity result, the priority structure, the Interview-only scope and the two-gate process. Its one divergence from the brief is that it is **more** accurate about the review record (P1-9). It is a well-made document.

---

## Why round 5 still found what it found

The dispatch asked for a plain verdict either way, and asked specifically that I say what convinces me if this round is different — and not manufacture findings if the document is sound. It is still the "not ready" case, and the reason is now measurable rather than impressionistic.

**The deletions and re-points held again, without exception — for the sixth commit running.** Every fix in `bf08b68f` that removed a false claim, narrowed a scope, or re-pointed a citation survived independent re-derivation with nothing to correct, including the four readability sites and the whole witness-not-recruitment propagation across two files. The two hardest facts in the document — the gate's real callers and the six parity verdicts — I derived from scratch without looking at any prior round's table, and both are exact. The rule §9 states is correct and has never had a counterexample.

**The failures are all one step past deletion, exactly where the refined rule says to look.** Three of this round's five P0s are in prose that has never been reviewed by anyone. One (P0-3) is the single sentence in the fix commit that had to assert a *replacement* fact rather than delete a wrong one — the targeted re-check named that sentence as "the one to check again afterward," and it was right. One (P0-1) is a correction applied at four of five sites, where the commit message claims five — the same half-application shape as the re-check's own P0-1, one iteration later, in a commit whose message explicitly promises the grep was done.

**The numbers, since they are the honest answer to "is this round different."**

| Commit | Added words | Reviewed before now | New P0s |
|---|---|---|---|
| `2aa12b15` (governance opened) | 983 | **no** | 1 (P0-4) |
| `bf57fcda` (launch prompt) | 126 | **no** | 0 |
| `bf08b68f` (re-check fixes + witness) | 726 | no | 2 (P0-1, P0-3) |
| `2719177e` (launch prompt witness) | 160 | no | 0 |
| `102193d2` (general rule) | 129 | no | 1 (P0-2) |

2,124 words of unreviewed prose, four P0s inside it — one per 531 words, better than the project's standing ~1-per-350 estimate but not different in kind. The fifth (P0-5) is not in any commit: it is the correction's *shadow*, a stale statement in a neighbouring file that no round has looked at because no round has grepped outward from the brief.

**So the document has not stabilised — but the reason has changed, and that is worth saying precisely.** Rounds 1–3 found errors in the brief's own diagnostic claims. Round 4 found errors in what the brief believed its instruments were wired to. This round found almost nothing wrong with the diagnosis: §5 grew by **ten words** since round 4 and every measurement in it reproduced exactly. All five P0s are in **scope and mandate** prose — §4 grew 60% and §7 grew 42% since round 4, and every one of those words arrived after the last review that looked at them. The brief's factual base is now genuinely solid. What keeps moving is the instruction layer on top of it, and it moves because Mark is still making real scope decisions — which is legitimate, and which is exactly why the standing rule says a round follows new prose.

**The method lesson this round adds, offered for the Standard Practice.** Round 3's lesson was to execute the serialisation path rather than read it. Round 4's was to enumerate a cited symbol's callers rather than trust its docstring. The targeted re-check's was to grep the document for the corrected claim's own vocabulary rather than fix the quoted line. This round's is the next ring out: **grep the workstream, not the document.** P0-5 exists because a correction that landed correctly in the brief and correctly in the launch prompt never reached the Decision Log — the third file, which the brief itself makes mandatory reading, and which still records both of the last two days' scope decisions in their pre-correction form. And a corollary the two half-applications both demonstrate: **a commit message's claim that a correction was applied at N sites is not evidence that it was.** Both times, checking took one grep.

**What this means for round 6.** P0-1, P0-3 and P0-5 are pure deletions, re-points and one enumeration correction — the safe class, and they should hold; the correct facts for all three are enumerated above so they can be written from this document without re-derivation. P0-4 needs one replacement sentence and is therefore the one to re-check afterward. **P0-2 is the only one that needs a decision rather than an edit** — whether the general rule's carve-out is "the mechanisms named untouchable" or something narrower, and whether "A Turn Has a Measure" and fabrication-rate tracking are inside it. That decision is Mark's, not Design's, and it should be made before the thread starts rather than discovered in world #1. If the fix commit is confined to these, **a targeted re-check of P0-2's resolution and P0-4's replacement sentence is proportionate; a sixth full round is not.** If it again reaches for new framing, the rule says what happens, and it has now said it correctly six times.

---

## Recommended fix list, in order

1. **§4's general rule** — add the untouchable-mechanism exception to the universal sentence; make §4's intro list the single canonical enumeration (five items) and have §7 and the launch prompt cite it rather than re-enumerate; state explicitly whether fabrication-rate tracking and "A Turn Has a Measure" are inside or outside it. **(P0-2)** The only item here needing Mark's decision, not an edit — and the one that decides what Design may remove.
2. **§4's `drift_detection` cost claim** — one call per turn (`nodes.py:1936`), not twenty; decompose the 20 as the type space per `parameters.yaml:119-123`; re-point the second-stage citation to `facilitator_prompts.py:261`. **(P0-4, P1-5)**
3. **§6:703–708's readability sentence** — rewrite to match §9(c), name which artifact the number comes from, then grep for *"has ever been run"* and *"confirm whether"* and confirm zero hits. **(P0-1)**
4. **§7 Part A's source list** — restore `/gravity/`, keep `/force/` excluded, note the gravity-content-vs-gravity-codes distinction; and close the broken sentence by starting the correction as its own paragraph. **(P0-3, P1-1)**
5. **`Decision-Log.md`** — a second superseding note covering the entry's *scope* statements (`:37-40`, `:51`) and its own stale open question (`:31`); change §3's instruction to match; extend §3's own defect description. **(P0-5, P1-3)**
6. **§7 Part A's parity attribution** — the compared generated side is the S2.8-class assemblers' output for all six worlds; `permanent_prompt.py` is the Desert-only S5.2 assembly and writes a different file; say what the 4-of-6 result actually measures. **(P1-2)**
7. **§6's tier rule** — add "or more accessible." **(P1-4)** One clause, fourth round.
8. **§5(B)** — label "at least a quarter" a lower-bound estimate pending §9's audit; move the four `syrlex`/`pahclex` examples to the second mechanism where they belong; fix "entire body" to "everything after the last content section." **(P1-6, P1-7)**
9. **§8 and §9's review record** — four rounds plus the targeted re-check, all five files named, and §9's operating rule extended with the re-check's two clauses. **(P1-9)**
10. **Objective 1's callback half** — a §7 Part A bullet (doc 10:47: prompt guidance, zero infrastructure), a §8 tally, a §9 task (e), and repoint the `(§3)` citation. **(P1-8)** Still the cheapest real win in the document, fifth round running.
11. **Objective 6's licensing text; "its form" restored to the droppable probe; a turn-length instrument in §8** — the last of these is now load-bearing, because the general rule makes the only existing brake removable. **(P1-8)**
12. **Sweep the P2s** — starting with `parameters.yaml:102` in its **sixth** round, the Marius reversed composite in its **fifth**, and the three-acceptance-worlds undercount, which understates a finding in the direction that matters.
