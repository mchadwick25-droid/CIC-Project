# CIC-Project — Working Rules

Read this before doing anything else. The program succeeds or fails on two things: scholarly rigor and clear, accessible conversation. Part 1 protects them. Never trade Part 1 for speed, cost, or convenience. Where rules in Parts 2–5 conflict, the earlier part wins.

1. **What never changes** — fidelity, voice, safety
2. **Before you start** — where things go, which model, budget
3. **While you work** — fixing, spending, building
4. **When you need Mark** — ask or act, how to ask
5. **Before you finish** — one checklist

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

- Aim for **CEFR B2, Flesch-Kincaid grade 8–10, Flesch Reading Ease ≥ 60**, in the register of BBC News or National Geographic. Grade 8 is a floor; flattening the world's voice is the real risk.
- Hold three things at once: **accessible**, **distinctive** (the world's own imagery and convictions), and **held** (no fabrication, no caving under pushback).
- Write sentences of about 12–20 words, never past ~25. One idea per paragraph. Introduce a term before using it. Use active voice and concrete verbs. Skip needless Greek and Latin.
- State uncertainty plainly. Show evidence naturally ("we believe this because…"). Say the complex idea plainly; don't swap it for a simpler one.
- Give a Representative its world's own hedges. Generic phrasing like "historians disagree" belongs to the Facilitator.
- Remove every AI tell: hedging filler, assistant cadence, disclaimers as a crutch.

Scoring and enforcement: `engine/m7/turn_readability.py`. Full standard: `Build/reference/method/Pass2-decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md` and `VR_1A_Writing_Standard_2026-08-09.md`.

### 1.3 Safety

- Never let a Representative handle real crisis or distress. The Facilitator recognizes risk and directs the person to human help, from a template, not free text. The Representative may stay warm in character.
- Near anything safety-adjacent, choose caution. Never make a redirect depend on the participant saying they're okay.
- Don't mistake a world's designed fierceness or disorientation for participant distress.
- Keep the protocol proportionate: as cheap as it can be while still catching the real event.

How it runs now: the Facilitator classifies acute distress and harmful dynamics every turn, the Representative stays silent on those turns, and code appends the crisis resources. Governing doc: `Archive/Syriac-Build-2026-07/L3D-Encounter-Methodology/CiC_L3D_Facilitator_Governance_V3.6.docx`.

---

## Part 2 — Before you start

### 2.1 Know where things go

| What you have | Where it goes |
|---|---|
| Code, data, or finished record | The live/canonical folders below. Nothing else goes in them. |
| Notes, decision logs, audits, review rounds, status reports | `Build/Ministry/` |
| A gap, open question, or review outcome | That world's `Open_Gaps_Tracking.md`, numbered, append-only |
| A fleet defect you aren't fixing now | An `ACCEPTED_OPEN` waiver with its owning finding |
| Something superseded | `Archive/`. Never delete without instruction. |
| Something for Mark to react to | An Artifact, not a repo file (see 4.2) |

**Live/canonical folders:** `engine/`, `cic/engine/`, `records/`, `packages/`, `canon/`, `fixtures/`, `cic/texts/`, `cic/corpus-map/`, `cic-poc/frontend/`, `cic-website/`, `Build/worlds/` (worlds without a registry code: `Build/World-Builds/<long-name>/`), `Build/reference/`, `Sandbox/` (code only; its notes go in `Build/Ministry/Features/<project>/`). The root `README.md` describes each one. If this list and the README disagree, fix the README first and log it in `Build/Ministry/Operations/Standing/CiC_Repo_Structure_Tracking.md`.

- If you find commentary or change history inside a live file, remove it. Don't add to it.
- If you edit a live file, also remove the commentary already in it. `tools/check_live_commentary.py` shows what's there.
- In gap entries, never renumber a merged entry. Cross-reference by subject and date, not number.

### 2.2 Use the right model

| Task | Model |
|---|---|
| Drafting and revising | Sonnet 5.5 |
| Doc_04 (Gravity Discovery), Doc_10 (Representative), and frame-setting design or research | Fable |
| Every adversarial review round | Opus 5.5. From round 2, a targeted recheck of what changed, at lower effort. |
| Every `modern_rendering` and re-rendering | Opus 5.5. Every clause, nothing added, one thought per sentence, nothing past ~25 words, no word whose modern sense misleads. |
| Package rebuilds, citation and log fixes, formatting, indexing | Haiku |

### 2.3 Check the budget

- Treat Max-200 as a hard cap. Never fall back on paid overage.
- The allowance resets Friday at 2:00 pm. Give at least half to building. Schedule heavy steps early in the week.
- Keep two ledgers per world: allowance share and metered dollars.
- Start a world only when the remaining build allocation covers a typical world plus a reserve. Build one world at a time. Run a second session only when the ledger shows the week can carry it.

Mark's own account practices: `Build/Ministry/Operations/Standing/CiC_Usage_Discipline.md`.

---

## Part 3 — While you work

### 3.1 Fix it right

- Find and fix the root cause. If it isn't clear, say so and investigate before touching code.
- If an earlier fix was wrong, undo it and redo it. Never stack a fix on a fix.
- No band-aids, workarounds, or "good enough for now." No shortcut that trades correctness for speed.
- If a path turns out wrong, rewind out of it rather than patching over it.

### 3.2 Spend money only like this

**Model calls (metered).**

1. Call the model only for a live quality test Mark has approved by name, with a cap.
2. Nothing else qualifies: no admission battery, grading run, meaning-fit measurement, baseline, or experiment.
3. If a gate can't pass without a model call, stop and ask.
4. The engine enforces this: a call outside a conversation needs `--live-test "<name>"` and `--cap-usd <n>` (decisions 54 and 56).

**Paid bulk runs** (text-to-speech, image or model batches).

1. Run a small sample. Get Mark's approval by ear or eye.
2. Pass every paid setting (voice or model id, generation settings) on the command. Never inherit them from the environment.
3. Make the run print its settings with item and character counts. Confirm from that output.
4. Verify the thing that was paid for. Matching files prove nothing about what produced them.

Why: `Build/Ministry/Operations/Standing/CiC_Governance_Rationale_Log.md`.

### 3.3 Keep the context lean

- Send exploration and research to subagents.
- On uncertain scope, explore read-only before implementing.
- Wait on PR and CI events. Don't poll.

### 3.4 Build a world

1. Kick off a world end-to-end: "build [World] end-to-end per cic-build-cycle discipline; self-govern per its own rules; stop only for an escalation category or a missing input."
2. Let the build self-govern. Stop only for the escalations in 4.1. Never self-assign Frozen status.
3. Present Representative identity and image as one packaged choice: 2–4 named candidates with trade-offs (`Representative_Construction_Notes_Template.md`). Ask once.
4. Doc_02 (Source Ecology) belongs to the Library thread. Source it ahead of need, following `Build/Ministry/Operations/Standing/CiC_Source_Research_Practice.md`.
5. Cap review at three rounds.
   - The bar is acceptable scholarly rigor. "Could be stronger," with nothing wrong, unsupported, or misleading, is not a finding.
   - Every review file counts toward three (the `roundcount` gate enforces it).
   - After three substantial rounds without clearing, stop and escalate. Don't run a fourth.
   - Exception: a review Mark orders in a "Cap ruling" entry in the System Hub Decision Log doesn't count.
   - Mechanics: the `cic-build-cycle` skill. Why: `CiC_Governance_Rationale_Log.md`.

### 3.5 Hand off to the next thread

1. Hand off at a stopping point where you can: a document approved, a PR merged, a batch done.
2. Fill in `Build/reference/L4-Templates/Session_Handoff_Template.md`. Keep it to one page.
3. Save it as `Build/Ministry/Operations/Handoffs/<YYYY-MM-DD>_<topic>.md` and commit it with the work.
4. Point to decisions, files, and PRs. Never copy a rule from this file into a handoff or launch prompt.
5. Starting from a handoff: read it first, then re-check its section 3 before building on it. If a claim fails, log it in `Open_Gaps_Tracking.md` and tell Mark.

---

## Part 4 — When you need Mark

### 4.1 Ask or act?

| Situation | Do this |
|---|---|
| CI/infra mechanical fix (config, workflow YAML, build script) | Just do it |
| Package rebuild after a `records/` edit | Just do it |
| Your own PR is green: merge into `live`, then `main`; update it if it falls behind; check the deploy | Just do it (2026-10-17) |
| A change Mark approved in chat, in a connected service (Tally and the like), including publishing | Just do it (2026-10-17) |
| Anything only a dashboard can do (Render, AWS, Cloudflare, GitHub settings) | Give Mark the exact steps |
| Session permissions (`.claude/settings.json`) | Give Mark the exact steps. A session can't change its own permissions. |
| Doc-hygiene problem in another thread's content | Flag it. Don't touch it. |
| Representative identity or title | Ask |
| Cross-world or portfolio-level decision | Ask |
| Governance or methodology change | Ask |
| A tension the pipeline can't close (including the review cap) | Ask |

Add a row only when a real new case shows up.

### 4.2 How to ask

1. Follow Sam Kaner's Diamond of Participation, Mark's own practice (`CiC_Governance_Rationale_Log.md`), and say which phase you're in when it isn't obvious:
   - **Divergent** — go wide first. Surface the real range of possibilities before narrowing to any one.
   - **Groan zone** — struggle with it honestly. Explore options, ask "what if," and sit with the trade-offs rather than resolving them too early.
   - **Convergent** — narrow down together, to a decision Mark has actually reached, not one reasoned through alone and handed over as settled.
2. Ask one decision at a time.
3. Ask with the `AskUserQuestion` tool, not in plain text. One question per call, with 2–4 options. Give each option a short label and a one-line trade-off in its description. Put your recommendation first, with "(Recommended)" at the end of its label. Use a 12-character-or-shorter header that names the decision. Turn on multi-select only when the choices really combine. Mark can always answer in his own words instead.
4. To compare options side by side (two wordings, two layouts, code), use the tool's preview on each option. If the material is too big even for that (a whole draft), show it as an Artifact first, then ask in the box.
5. Don't write a repo file just to get approval. Permanent review records (review rounds, decision logs, `Open_Gaps_Tracking.md`) are the exception.

### 4.3 After Mark decides

- "Converged, auto mode", or a clear equivalent Mark says directly, means final. Without it, keep checking.
- Once converged, execute the full scope without asking step by step.
- To change something already settled, name it as a **change order** with a reason. Never edit it quietly.
- Return to asking only for a decision not yet made, or a real need for direction or clarification.
- Until convergence, write nothing to a canonical record, commit nothing, and treat nothing as decided.

---

## Part 5 — Before you finish

- [ ] Every quote re-verified word for word against its vendored source.
- [ ] Contested claims tagged with `formation_confidence`.
- [ ] No commentary left in any live file you touched (`tools/check_live_commentary.py`).
- [ ] Every gap logged in `Open_Gaps_Tracking.md`; every unfixed fleet defect waived; no stale waivers.
- [ ] Truncation checked by two independent methods.
- [ ] "Approved to proceed," never "finalized." Nothing closes until Phase Five boundary testing and full-system review are both complete.
- [ ] A blocking finding cleared only by independent re-confirmation, never self-certification.
- [ ] One draft PR for the batch, pushed once after local checks pass, then marked ready (ruled 2026-10-05).
- [ ] If another thread picks this up, a handoff saved in `Build/Ministry/Operations/Handoffs/` (3.5).
