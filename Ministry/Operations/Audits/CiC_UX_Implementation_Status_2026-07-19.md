# UX Implementation Status — 2026-07-19 (end of day)

**What this is:** a feature-by-feature account of everything that touches what a real
participant would actually see, click, hear, or experience — cross-referenced against
today's own hands-on testing (real API calls, real conversations, real clicks), not
just documentation. Where a status below differs from what a tracking doc claimed
earlier today, that's because it was checked directly and found otherwise — see the
correction entries throughout. Complements, doesn't replace,
`CiC_UX_to_Bedrock_Pilot_Readiness_2026-07-19.md` (V1.2, the deployment-critical-path
version of this same picture).

**Headline: the app went from completely broken to genuinely good today, in one
session.** Every message send was crashing at the start of today's testing. By the end,
five real, honest, well-cited conversations had been run against all five live worlds.
That's the real shape of today — not incremental polish, a floor-to-working recovery.

---

## 1. The two live things, and the gap between them

**The public website** (`churchinconversation.org` / `.com`) — live, real domain, real
visitors could reach it right now. Six pages (Home, About, Atlas, Tour, Support, Pilot).
The Atlas page runs the **actual** interactive World Orientation Map as of today
(replacing a placeholder slideshow) — a real, working, 178-entry scrolling census.
Pilot page live, collects interest via `mailto:`.

**The actual conversational app** (`cic-poc`) — runs only in a local dev environment
right now. **Not deployed anywhere a real visitor could reach.** This is the one gap
between the two: the public site's own copy already describes five live worlds and
invites people to the Pilot, but there is currently no live URL where a real visitor
lands in an actual conversation. Direct-API hosting is the decided path (Bedrock
dropped) but hasn't been stood up for `cic-poc` itself — only the marketing site is
actually deployed.

---

## 2. The journey, stage by stage

### S0 — Threshold (three co-equal doors)
Designed in full (Storyboard §S0, V1.0 §5.1), **zero code**. What actually runs today
skips straight to the world picker. Not tested today; unchanged from prior status.

### S1 — World Map
- **On the public website:** live, real, working — see §1 above.
- **Inside the app's own selection flow:** built and verified on an unmerged branch
  (Tier A — optional orientation view + handoff back into the app), not merged into
  `cic-poc`'s actual world-selector. Tier B (map as the *primary* selector) not started.

### S2 — Table setup (world/representative picker)
Live, functional — **but still the pre-redesign UI**: the "Single Representative /
Multiple Representatives" toggle and tile grid, not the emergent-seating redesign
Increment 1 specifies. Confirmed by direct inspection today, not assumption. **Alexandria
(Theon) is now the fifth card** — fixed today (was completely absent from the running
app despite being reported everywhere as installed; see §4).

### S3 — First question + routing
Question-First Entry (§R) fully designed, **zero code**. No routing exists today — a
typed question goes straight into the Table.

### S4 — The Table (the actual conversation) — see §3 below, the bulk of today's work

### S4-tour — Hosted Tour
**DEFERRED TO PHASE 2 — not part of the current build cycle (2026-07-22).** Mark
decided Hosted Tour is a second-tier (Phase 2+) feature, not something this launch
builds, and directed that all Tour-related content be taken out of the current build
cycle across documents, UX, and code planning. Kept below as the status record for when
Phase 2 takes this up.

Chloe demo built, self-contained; not reachable from the real conversation flow.
Unchanged today.

### S5 — The close
**New finding today, on top of what was already known:** the backend's Sensed Closing
Sequence logic was part of the same crash fixed today (§4) — it literally could not run
at all until today. Now that it can, **the frontend has no UI for it whatsoever.** When
a conversation ends, `TheTable.tsx` renders only *"The conversation has ended"* and a
"Return to World Selection" button — no reflection beat, no closing-resources offer, no
"door outward" framing. Even with the backend working, none of §5.6/§5.7's designed
closing experience has anywhere to render. This is a real, previously-unflagged gap.

---

## 3. Inside S4 — what today's testing actually found

### 3a. The core loop — was completely broken, now fixed
Every message send crashed (`state.closing_stage` referenced a field that didn't exist;
two entire graph modules, `closing_sequence.py` and `modern_term_bridge.py`, were
missing outright — casualties of today's earlier file-loss incident, never redone).
**Fixed and verified live** with real conversations. Committed (`e596c25`), not yet
pushed.

### 3b. Transcript UI
Still the old gradient chat-bubble style for Representative/participant turns
(confirmed via computed CSS, not just visual impression) — Increment 1 (long-form,
no-bubbles redesign) not merged.

### 3c. Three-Level Transparency — mixed, and unevenly built
| Content type | Status |
|---|---|
| Lexicon terms | **Fully built and verified live today** — inline dotted-underline highlighting, hover popover, click-through modal, all working |
| Citations (aggregate, end-of-turn `✲` marker) | **Built and verified live today** — opens correctly, shows real sourcing |
| Stories | Only covered by the same aggregate marker, never inline-highlighted — but the onboarding screen's own copy promises inline highlighting for "claims and stories," which isn't what's built. Tier/confidence data is computed by the backend and silently dropped before reaching the frontend. |
| Quotes | Don't exist as a distinct type anywhere in the code |
| General references (not tied to a retrieved lexicon/story chunk) | No standalone disclosure exists — an unsourced-sounding claim with nothing retrieved for it looks identical to an unsourced statement |

### 3d. The anachronism bridge
**Verified live and working correctly** today, unprompted, in a real conversation —
caught a modern-doctrine reading, named it as later, gave the neutral modern gloss,
handed back cleanly. This is the fixed module from §3a doing its actual job.

### 3e. Representative voice quality — extensively live-tested today
20 real academic-tier questions, run in full sequence, across all 4 pre-existing worlds
(Chloe, Mar Yausep, Papnoute, Albina) — not mocked, not summarized.
- **19 of 20 answers were excellent**: honest, specific, well-cited, repeatedly
  surfacing real historical nuance unprompted (Jerome's actual "ivy/gourd" controversy,
  Evagrius's real posthumous condemnation, Paula/Eustochium's letters surviving only
  through Jerome's hand, the real Ignatius-vs-conciliar-eldership leadership tension
  held open rather than smoothed).
- **1 reproducible failure, identical across all 4 worlds**: the same curriculum
  question ("Where does documentation end and inference begin for you?") broke
  character every single time, with the Representative describing the platform's own
  construction methodology in the third person instead of answering in-world. Root
  cause identified, two fix directions proposed, handed to System Hub —
  `CiC_System_Hub_Handoff_RepresentativeSelfReference_2026-07-19.md`. Not yet fixed.

### 3f. Representative Modes (role selection)
Built on a branch, mock-verified only. **Battery A (the real validation run) has never
been executed.** Per Mark's own full-feature-set scope decision, this is now required
for P1, not optional — and it's the single longest-lead-time item with zero upstream
dependency, meaning it's also the thing most worth starting immediately rather than last.

### 3g. Guided Questions UI ("Don't know what to ask?")
Content complete (Curriculum V1.0, 100 questions — the same curriculum today's academic
testing drew from). **Zero UI code.** Hard-gated on Representative Modes (3f) landing
first, since a role-served question walk needs a role to exist.

### 3h. Alexandria / Theon
**Was completely absent from the running app** despite being reported as installed
everywhere (dashboard, task board, the public website's own copy) — no manifest entry,
no data folder. **Fixed and verified live today**: all 57 world-data files restored, the
manifest entry restored from a verbatim earlier read of the same file, two hand-synced
frontend registries fixed, a real conversation with Theon run successfully. Not yet
pushed to origin.

---

## 4. Cross-cutting / infrastructure (not part of the visible journey, but shapes it)

- **Hosting**: Bedrock dropped, direct Anthropic API decided. Stood up for the
  marketing site only; not yet for `cic-poc` itself.
- **Accounts/sign-in** (Supabase): built, smoke-tested, gracefully no-ops until
  configured — needs Mark's own Supabase/Render account creation to go further
  (standing constraint: not something to do on his behalf).
- **Per-tester session/API capping**: code exists (`session_cap.py`), needs populating
  once real hosting exists.
- **Relational-safety / governance (Article 33) and drift monitoring**: not exercised
  by today's testing — today's questions were academic/historiographic, not distress or
  frame-breaking probes. No new information either way; still resting on prior
  validation rounds.

---

## 5. What "full implementation" actually requires from here

Given Mark's own scope decision (P1 launches with the full feature set, not the minimum
path), the real remaining list, roughly in the order it actually unblocks:

1. **Say go on Battery A** — zero dependency, longest lead time, the one thing most
   worth not leaving for last.
2. **Fix the Representative self-reference frame-break** (§3e) — small, scoped, already
   diagnosed.
3. **Build Increment 1** (long-form transcript, table bar, Level-3 panels, token swap) —
   spec is implementation-ready.
4. **Build the S5 closing-sequence frontend** (§S5 above) — newly discovered gap; the
   backend can run it now, nothing renders it yet.
5. **Stand up direct-API hosting for `cic-poc` itself**, not just the marketing site.
6. Once Battery A passes + Increment 1 lands: **Increment 2** (role selection) merges.
7. Once Increment 2 lands + Guided Questions content is validated: **Increment 3**
   (the actual question-sheet UI).
8. ~~**Hosted Tour integration**,~~ **Question-First Entry**, **Guided Onboarding** — all
   fully designed, zero code, none hard-blocking the others. **Hosted Tour removed —
   DEFERRED TO PHASE 2 (2026-07-22); see §S4-tour above.**
9. **Push today's three fixes** (the crash, Alexandria, and whatever comes out of #2) to
   origin — currently local-only.

Nothing above is a design gap. Every item has an approved spec, a storyboard state, or
(for #2) a full diagnosis already in hand. What's left is entirely build → validate →
merge, same as this morning's readiness report concluded — just with a longer, more
accurate list now that today's live testing surfaced real gaps (#2, #4) that no document
had caught before actually running the thing.

## Document log

- **V1.0 (2026-07-19, end of day):** First edition, produced after a full day that
  moved from "every message crashes" to "five real, live-tested, mostly-excellent
  conversations across all five worlds." Synthesizes the day's fixes (closing-sequence
  crash, Alexandria install, the frame-break diagnosis) against the existing design
  record. Requested by Mark: "a ux status update on everything that impacts the user
  experience, including features and add-ons... where are we at with total
  implementation."
