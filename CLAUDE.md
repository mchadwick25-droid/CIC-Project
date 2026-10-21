# CIC-Project — Working Rules

Read this before doing anything else. The program succeeds or fails on two things: scholarly rigor and clear, accessible conversation.

- **1.1 and 1.2 are principles.** They hold together. Never trade one against the other, and never trade either away for speed, cost, or convenience.
- **1.3 Safety is a working protocol,** kept and built to be proportionate.
- The cost and scaling rules exist to buy more rigor and clarity, never to trade against either. A build that is cheaper, faster, or more automated but weaker on rigor or clarity is a failure the process didn't catch.

This file is laid out in working order:

1. **What never changes** — fidelity, voice, safety
2. **Before you start** — where things go, which model, budget
3. **While you work** — fixing, spending, building, handing off, checking
4. **When you need Mark** — ask or act, how to ask, governance vocabulary
5. **Before you finish** — one checklist

**Priority order is separate from that layout.** When two rules pull in different directions, the one higher in this list wins:

1. Never invent (1.1) and Write for the participant (1.2)
2. Safety (1.3)
3. Fix it right (3.1) and Check, then say (3.6)
4. Governance vocabulary and closure (4.4)
5. Keep the live/canonical surfaces clean (2.1)
6. Track gaps and exceptions (2.1)
7. How we work with Mark (4.1–4.3, 3.5)
8. Building a world (3.4, and the world-start rules in 2.3)
9. Usage and cost (2.2, 2.3, 3.2, 3.3) — these never override anything above them.

---

## Part 1 — What never changes

### 1.1 Never invent

- Do not invent family, age, history, or anecdote for a Representative. If a detail can't be derived from the completed world, leave it out.
- Re-verify every quote word for word against the vendored source file before a record passes review. Treat "quotes verified" as a claim to re-check.
- Tag contested or uncertain claims with `formation_confidence`: Documented / Widely Accepted / Dominant Modern Reconstruction / Contested / Inferential-Thin. Add a `contested_claim` record where warranted. Never present a disputed claim as settled.
- Record an absent claim with `honest_limit`, `absent_detail`, or `kind: absence`. "Not Attested" is not a sixth confidence level.
- Treat a polished, generic AI voice as a fabrication risk too.

Why: fabrication at moments of maximum stakes is the most serious failure this project recognizes.

### 1.2 Write for the participant

Applies to everything a participant sees: dialogue, UI text, instructions, onboarding.

- Write toward **CEFR B2, Flesch-Kincaid grade 8–10, Flesch Reading Ease ≥ 60**.
  - Register: BBC News or National Geographic. Serious, adult, vivid, clear, readable by a non-native speaker without simplifying the substance.
  - This is a principle to write toward, not a script this file runs.
  - Grade 8 is a floor worth staying above, not a target to hit exactly. Flattening the world's own voice is the real risk.
- Hold three things at once: **accessible**, **distinctive** (the world's own imagery and convictions), and **held** (no fabrication, no caving under pushback).
- Keep sentences short, averaging roughly 12–20 words. Nothing nested, nothing running past ~25 words. One idea per paragraph (1–4 sentences). Introduce a technical term before using it naturally. Use active voice and concrete verbs, not passives and nominalizations. Skip unnecessary Greek and Latin.
- State uncertainty plainly rather than hedging it into vagueness. Show evidence naturally ("we believe this because…") rather than arguing at length.
- Precise language beats impressive language. Say the complex idea plainly rather than trading it for a simpler one. Don't simplify the scholarship; lower the barrier to entering it.
- A Representative's hedge language is emic, not etic: the world's own way of naming its own uncertainty. Generic academic phrasing ("historians disagree") belongs to the Facilitator, who speaks from outside every world.
- Remove every AI tell: hedging filler, assistant-voice cadence, telltale LLM phrasing, disclaimers as a crutch. If a participant can hear the chatbot instead of the world's own voice, that is a defect, even if the content is accurate.

Scoring and enforcement: `engine/m7/turn_readability.py`. Full standard: `Build/reference/method/Pass2-decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md` and `VR_1A_Writing_Standard_2026-08-09.md`.

### 1.3 Safety

- Never let a Representative handle real crisis or distress. The Facilitator recognizes risk and directs the person to human help, from a template, not free text. The Representative may stay warm in character.
- Near anything safety-adjacent, choose caution. Never make a redirect depend on the participant saying they're okay.
- Don't mistake a world's designed fierceness or disorientation for participant distress.
- Keep the protocol proportionate: as cheap as it can be while still reliably catching the real event. A rare event does not raise the cost of ordinary turns beyond what detection needs.

How it runs now: the Facilitator classifies acute distress and harmful dynamics every turn, the Representative stays silent on those turns, and code appends the crisis resources. Governing doc: `Archive/Syriac-Build-2026-07/L3D-Encounter-Methodology/CiC_L3D_Facilitator_Governance_V3.6.docx`.

---

## Part 2 — Before you start

### 2.1 Know where things go

| What you have | Where it goes |
|---|---|
| Code, data, or finished record | The live/canonical folders below. Nothing else goes in them. |
| Notes, decision logs, audits, review rounds, status reports | `Build/Ministry/` |
| A gap, open question, or review outcome | That world's `Open_Gaps_Tracking.md`, numbered, append-only. Never left to live only in a conversation. |
| A fleet defect you aren't fixing now | An `ACCEPTED_OPEN` waiver with its owning finding |
| Something superseded | `Archive/`. Never delete without instruction. |
| Something for Mark to react to | An Artifact, not a repo file (see 4.2) |

**Live/canonical folders:**

- `engine/`, `cic/engine/` — the core engine and the corpus tools
- `records/`, `packages/`, `canon/`, `fixtures/` — world data, compiled packages, sealed probes, the fixture world
- `cic/texts/`, `cic/corpus-map/` — the Library
- `cic-poc/frontend/`, `cic-website/` — what Render and Cloudflare serve
- `Build/worlds/` — one home per world by registry code: construction documents once approved to proceed at `Build/worlds/<code>/`, the world's indexes, build log and source manifests at `Build/worlds/<code>/build/`, and the fleet-level `_cross-world/` documents. Worlds without a registry code stay at `Build/World-Builds/<long-name>/` until they get one.
- `Build/reference/` — the method and spec library. Read constantly, edited rarely. A template exists once, here.
- `Sandbox/` — next-version code only; its notes go in `Build/Ministry/Features/<project>/`

The root `README.md` is the map of the whole tree, and this list follows it. If they disagree, fix the README first, log it in `Build/Ministry/Operations/Standing/CiC_Repo_Structure_Tracking.md`, then fix this list.

- If you find commentary or change history inside a live file, remove it. Don't add to it.
- If you edit a live file, also remove the commentary already in it. `tools/check_live_commentary.py` shows what's there.
- In gap entries, never renumber a merged entry. Cross-reference by subject and date, not number.
- An unlisted fleet defect is new drift and fails the run. A stale waiver for something already fixed also fails; remove it.

### 2.2 Use the right model

| Task | Model |
|---|---|
| Drafting and revising | Sonnet 5.5 |
| Doc_04 (Gravity Discovery), Doc_10 (Representative), and other frame-setting design and research (below) | Fable |
| Every adversarial review round | Opus 5.5. From round 2, a targeted recheck of what changed, at lower effort. |
| Every `modern_rendering` and re-rendering | Opus 5.5. Every clause, nothing added, one thought per sentence, nothing past ~25 words, no word whose modern sense misleads. |
| Package rebuilds, citation and log fixes, formatting, indexing | Haiku |

**Fable is reserved** for complex design and research that sets the frame downstream:

- system or front-end redesign proposals
- comparative source-ecology and world-strategy research
- org and funding strategy

Use it where getting the frame right the first time avoids many cheaper rounds of rework later. Never use it for routine drafting or anything that repeats.

### 2.3 Check the budget

- Treat Max-200 as a hard cap. Get everything possible out of the flat fee; never fall back on paid overage.
- Context-window management matters at least as much as model choice. A bloated context costs more than a clean one, regardless of tier.
- The allowance resets Friday at 2:00 pm. Give at least half to building. Schedule heavy steps early in the week.
- Keep two ledgers per world: allowance share and metered dollars.
- Start a world only when the remaining build allocation covers a typical world plus a reserve.
- Build one world at a time by default. Run a second concurrent session only when the ledger shows the week can carry it.
- These are human-supervised sessions, not automated multi-agent orchestration.

Mark's own account practices: `Build/Ministry/Operations/Standing/CiC_Usage_Discipline.md`.

---

## Part 3 — While you work

### 3.1 Fix it right

- Find and fix the root cause. If it isn't clear, say so and investigate before touching code.
- If an earlier fix was wrong, undo it and redo it. Never stack a fix on a fix.
- No band-aids, workarounds, or "good enough for now." No shortcut that trades correctness or completeness for speed.
- If a path turns out wrong, back out of it with a checkpoint or `/rewind` rather than patching over it. That is "no fix on a fix," enforced mechanically.

### 3.2 Spend money only like this

**Model calls (metered).**

1. Conversations are the only spend (ruled 2026-10-06, decisions 54 and 56).
2. Outside a conversation, call the model only for a live quality test Mark has approved by name, with a cap.
3. Nothing else qualifies: no admission battery, grading run, meaning-fit measurement, baseline, or experiment, unless Mark has approved that run as a live test.
4. If a gate in the engine can't pass without a model call, stop and ask rather than run it.
5. Keys may stay in the shared environment. The engine refuses a model call outside a conversation unless the command carries `--live-test "<name>"` and `--cap-usd <n>`. It prints its settings first, stops at the cap, and logs the name.

**Paid bulk runs:** anything that spends real money in bulk on a metered outside service — text-to-speech, image or model batches, anything charged per item or character.

1. Run a small sample. Get Mark's approval by ear or eye.
2. Pass every paid setting (voice or model id, generation settings) on the command. Never inherit them from the environment.
3. Make the run print its settings with item and character counts. Confirm from that output.
4. Verify the thing that was paid for. Matching files prove nothing about what produced them.

Why: `Build/Ministry/Operations/Standing/CiC_Governance_Rationale_Log.md`.

**Asking for any spend.** This covers any request to spend: a model call outside a conversation, a live test, an admission run, or a paid bulk run.

1. Before you ask, explain the request to Mark in plain words. Say each of these:
   - what the run is and what it should produce;
   - why it was asked for: which rule or decision requires it, and who started it;
   - why now: what is still changing, and whether any of that would make the result stale;
   - the cost: the cap, how the estimate was made, what is old or wrong about it, and the likely real cost;
   - the cap's margin: the cap against the real cost in the latest ledger or report for the same worlds and model, in dollars and as a percent. If there is no such record, say so;
   - what happens if it stops early, and whether partial results are kept, checked by reading the code or a free dry run, never by spending;
   - where the output goes: a file, with the ledger path written in the request;
   - the other ways to get the result (hold, waive the gate, run a smaller sample, use a free check), each with its trade-offs;
   - your own recommendation, including "do not run it now".
2. Ask with `AskUserQuestion` after the explanation, in the same message. Offer "Explain more" and "Not now" beside the approval.
3. When the cap is $5 or more (Mark, 2026-10-20), ask Mark to say back in a line what the run does and what it costs. Do the same when the same run lost its results or went past its estimate before. If his line does not match, explain again.
4. A yes covers that one run at the cap Mark approved. It does not carry to a second attempt, a changed cap, or another run. A converged plan or "auto mode" is not a yes to spend. Paid bulk runs still start with the small sample.
5. A run that lost its results or went past its estimate is not repeated until the cause is fixed. A free check, with no model call, must show the fix works. If no free check can, say so in the request and let Mark decide. The next request says what the cause was and what the check showed.
6. Do not start a paid run while an unresolved item in that world's `Open_Gaps_Tracking.md`, or an unmerged change to files the run reads or to the code that handles its replies, would alter what the run measures. If one does, tell Mark and let him choose.
7. A paid run started without this explanation is a breach. Log it in `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md` and tell the thread that started the run, whatever it cost.

### 3.3 Keep the context lean

- Use `/compact` or `/clear` between unrelated pieces of work. Reach for these before reaching for a cheaper model.
- Send exploration and research to subagents so they don't bloat the main thread.
- On uncertain scope, use Plan Mode and explore read-only before implementing.
- Batch related work into one longer session instead of many short restarted ones. Short sessions lose the prompt cache and pay for context again every time.
- Spread heavy build and review days across the week instead of bursting most of a week's work into one or two days.
- Wait on PR and CI events. Don't poll.

### 3.4 Build a world

1. Kick off a world end-to-end: "build [World] end-to-end per cic-build-cycle discipline; self-govern per its own rules; stop only for an escalation category or a missing input."
2. Let the build self-govern. Stop only for a missing input or one of the four escalation categories: Representative identity or title, cross-world or portfolio-level decisions, governance or methodology changes, and tensions the pipeline can't close on its own. Never self-assign Frozen status.
3. Present Representative identity and image as one packaged choice: 2–4 named candidates with trade-offs (`Representative_Construction_Notes_Template.md`). Ask once.
4. Doc_02 (Source Ecology) belongs to the Library thread. Source it ahead of need, following `Build/Ministry/Operations/Standing/CiC_Source_Research_Practice.md`.
5. Cap review at three rounds.
   - The bar is acceptable scholarly rigor. "Could be stronger," with nothing wrong, unsupported, or misleading, is not a finding.
   - After three rounds of substantial revision without clearing review, stop and escalate. Don't attempt a fourth.
   - Every review file on a document counts toward the three, whatever its kind or verdict (the `roundcount` gate enforces it).
   - The one exception: once a document has escalated to Mark at the cap, a review he orders in his ruling does not count, when a "Cap ruling" entry in the System Hub Decision Log names its file.
   - Mechanics: the `cic-build-cycle` skill. Why: `CiC_Governance_Rationale_Log.md`.

### 3.5 Hand off to the next thread

1. Hand off at a stopping point where you can: a document approved, a PR merged, a batch done.
2. Fill in `Build/reference/L4-Templates/Session_Handoff_Template.md`. Keep it to one page.
3. Save it as `Build/Ministry/Operations/Handoffs/<YYYY-MM-DD>_<topic>.md` and commit it with the work.
4. Point to decisions, files, and PRs. Never copy a rule from this file into a handoff or launch prompt.
5. Starting from a handoff: read it first, then re-check its section 3 before building on it. If a claim fails, log it in `Open_Gaps_Tracking.md` and tell Mark.

### 3.6 Check, then say

1. Before you state something about the repo, a rule, a decision, or what a change affects, check it in this session against its source: the file, the decision-log entry, the config, the diff.
2. Name the source when you state it: "the 2026-10-02 ruling says…", "per `engine/Dockerfile`…".
3. If you haven't checked it, say so: "I haven't checked this; I assume…". Never present an assumption as fact.
4. Memory, an earlier thread, a handoff, or a launch prompt is a lead to check, not a source.
5. Don't attribute a rule to Mark unless a decision-log entry or his own words show he made it. Otherwise say "CLAUDE.md says…".

---

## Part 4 — When you need Mark

### 4.1 Ask or act?

| Situation | Do this |
|---|---|
| CI/infra mechanical fix (config, workflow YAML, build script) | Just do it |
| Package rebuild after a `records/` edit | Just do it |
| Your own PR is green: merge into `main`; update it if it falls behind; check the staging deploy | Just do it (2026-10-02, 2026-10-19) |
| Promoting `main` to `live` (production) | Mark's call, through `Build/Ministry/Operations/Standing/CiC_Promotion_Runbook.md`. Never open a PR into `live` yourself. |
| A change Mark approved in chat, in a connected service (Tally and the like), including publishing | Just do it (2026-10-17) |
| Anything only a dashboard can do (Render, AWS, Cloudflare, GitHub settings) | Give Mark the exact steps |
| Session permissions (`.claude/settings.json`) | Give Mark the exact steps. A session can't change its own permissions. |
| Doc-hygiene problem in another thread's content | Flag it. Don't touch it. |
| Representative identity or title | Ask |
| Cross-world or portfolio-level decision | Ask |
| Governance or methodology change | Ask |
| A tension the pipeline can't close (including the review cap) | Ask |

This table starts here and grows only when a real new case shows up, never speculatively.

### 4.2 How to ask

1. Follow Sam Kaner's Diamond of Participation, Mark's own practice (`CiC_Governance_Rationale_Log.md`), and say which phase you're in when it isn't obvious:
   - **Divergent** — go wide first. Surface the real range of possibilities before narrowing to any one.
   - **Groan zone** — struggle with it honestly. Explore options, ask "what if," and sit with the trade-offs rather than resolving them too early.
   - **Convergent** — narrow down together, to a decision Mark has actually reached, not one reasoned through alone and handed over as settled.
2. Ask one decision at a time.
3. Ask with the `AskUserQuestion` tool, not in plain text.
   - One question per call, with 2–4 options.
   - Give each option a short label and a one-line trade-off in its description.
   - Put your recommendation first, with "(Recommended)" at the end of its label.
   - Use a 12-character-or-shorter header that names the decision.
   - Turn on multi-select only when the choices really combine.
   - Mark can always answer in his own words instead.
   - A request for spend follows 3.2's explanation first, and only then the question box. The explanation is the one allowed text before the box.
4. To compare options side by side (two wordings, two layouts, code), use the tool's preview on each option. If the material is too big even for that (a whole draft), show it as an Artifact first, then ask in the box.
5. Don't write a repo file just to get approval. A file gets written only once it is the actual converged-on output. Permanent review records (review rounds, decision logs, `Open_Gaps_Tracking.md`) are the exception: they are lasting audit trail, not scratch material.

### 4.3 After Mark decides

- "Converged, auto mode", or a clear equivalent Mark says directly, means final. Without it, keep checking.
- Once converged, execute the full scope without asking step by step.
- To change something already settled, name it as a **change order** with a reason. Never edit it quietly.
- Return to asking only for a decision not yet made, or a real need for direction or clarification.
- Until convergence, write nothing to a canonical record, commit nothing, and treat nothing as decided.

### 4.4 Governance vocabulary and closure

- Say "Approved to proceed," never "finalized." That word is retired; don't use it.
- Nothing closes until both Phase Five boundary testing and full-system review are complete.
  - This is the whole-system and portfolio closure gate.
  - It is a much rarer scope than one document's own "Approved to proceed" under the build cycle's per-document self-governance.
  - One document proceeding doesn't mean anything has closed.
- A blocking review finding can't be dismissed by self-certification. It needs independent re-confirmation.
- A change to CLAUDE.md, a skill, a launch prompt, or a governance doc gets an independent review against the old text before anyone tells Mark what changed, or that nothing did.
- Truncation checks use two independent methods, not one.

---

## Part 5 — Before you finish

- [ ] Every quote re-verified word for word against its vendored source.
- [ ] Contested claims tagged with `formation_confidence`.
- [ ] No commentary left in any live file you touched (`tools/check_live_commentary.py`).
- [ ] Every gap logged in `Open_Gaps_Tracking.md`; every unfixed fleet defect waived; no stale waivers.
- [ ] Governance vocabulary, closure, blocking findings, and truncation handled as 4.4 says.
- [ ] One draft PR for the batch, pushed once after local checks pass, then marked ready (ruled 2026-10-05).
- [ ] If another thread picks this up, a handoff saved in `Build/Ministry/Operations/Handoffs/` (3.5).
