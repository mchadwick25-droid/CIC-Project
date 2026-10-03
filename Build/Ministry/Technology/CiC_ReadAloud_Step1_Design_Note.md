# Read-Aloud, Step 1 — Design Note

**Status: SUPERSEDED 2026-10-03. The feature was removed (see `CiC_FrontEnd_Decision_Log.md`, the entry "The free browser read-aloud is removed; the conversation has no voice"). The note below records what was built.**

**Earlier status: RULED 2026-09-22, engine-side verification done 2026-09-27,
awaiting Mark's own live-audio check.** Mark ruled on Q7 — Option A,
exactly, shown as a visible line under the bar (§7 below). Two
verifications were open: the Conversation Transparency Engine thread's
Stage 7 landing on `main`, and a real-browser check against a live
`engine/api` backend. On the first: Stage 7b (the engine streaming
module) merged 2026-09-25; Stage 7c (an SSE endpoint and frontend
streaming consumer) does not exist yet and, per the 2026-09-27 scoping
call, is treated as its own separate later step rather than a
precondition for this one — this feature never depended on live token
streaming to work (see §2). On the second: this session rebased
`read-aloud-step1` onto current `main` and drove it end to end in
headless Chromium against the real `engine/api` dev server (real
session, real message, real `alx`/Theon reply) — the control appeared,
spoke the reply sentence-by-sentence, and the disclosure line showed and
retired correctly. That confirms the wiring; it is not Mark's own ears on
real audio, which is the one verification left before this ships for
real participants. `VITE_READ_ALOUD` defaults off everywhere and is not
set in any deploy config (`render.yaml` checked — no reference to it).

**Origin.** Mark's ruling (2026-09-22): *"start with read-aloud free,
composite voice on the paid tier... test one step at a time."* This note
covers step one only — a free read-aloud option for conversation text, on
branch `read-aloud-step1`, behind `VITE_READ_ALOUD`. Composite
Representative voices, server-side text-to-speech, animation, and any paid
tier are out of scope here and nothing in this design reaches toward them.

**Frame.** Read-aloud means the participant's own browser speaks the text
already on screen, through the Web Speech API (`speechSynthesis`). Zero API
cost, no new backend, no audio files. The text stays on screen and stays
primary — this is Mark's own framing: the moat is the sourced text, the
voice sits alongside it, never replacing the transcript.

**Where it lives.** Frontend only, `cic-poc/frontend/src/`. Nothing in
`engine/`, `records/`, `packages/`, or `cic-website/` was touched. This
does not conflict with the Conversation Transparency Engine thread's Stage
7 (streaming) or the transparency marks (`WitnessMark`, `StoryMark`,
`GlossMark`, `Level2Card`, R17's element budget) — see Q1–Q3 for exactly
why.

---

## 1. What gets spoken

**Answer: `turn.text` verbatim — never the rendered DOM.**

`ConversationTurn.text` (`hooks/useConversation.ts`) is the raw string the
engine actually produced, before `VoiceTurnBody.tsx` decorates it. Checked
against `VoiceTurnBody.tsx` directly: the citation mark (`✲`,
`StoryMark`/`WitnessMark`) is an element the renderer *adds next to* the
sentence that earned it — it is never a substring of `text`. A figure or
gloss mark (`FigureBridgeMark`/`GlossMark`) wraps a substring that's
already in `text` (the matched name itself, dotted-underlined) — it adds
no new characters, just a clickable wrapper. The General References list
and the Level 2/3 cards read from `citations`/`transparency`, never from
`text`. So `text` is already exactly "the voice text only" the brief asks
for — there is nothing to strip, because nothing was ever added to that
string in the first place. Reading `turn.text` directly (in
`ReadAloudControl`, sourced from the screen's own `turns` array) is both
the simplest implementation and the only one that can't drift out of sync
with whatever VoiceTurnBody's two renderers (legacy or anchor-driven) do
next — it doesn't touch either renderer at all.

**Facilitator turns: yes, including safety turns, in full, never
truncated.** A Facilitator turn's `text` is exactly what
`engine/m4/crisis_resources.py` composed (`ACUTE_DISTRESS_RESOURCES`,
`_A2`, `_CONTINUATION`) — fixed, code-appended text, never a model
generation. `Conversation.tsx`/`TableRoom.tsx` render it with
`facilitatorParagraphs(text)` (a plain `split('\n\n')`), and read-aloud
speaks the same underlying string, split into sentences instead of
paragraphs (see Q2's chunking). Nothing in the read-aloud path
special-cases `kind: 'safety'` to skip or shorten it — there is no branch
that could.

**Participant turns are not spoken.** The brief doesn't ask for this, and
a participant reading their own just-typed words back is redundant, not an
accessibility win. `latestSpokenTurn()` (`Conversation.tsx`/`TableRoom.tsx`)
skips `speaker === 'participant'` for this reason.

## 2. When it speaks

**Answer: on demand, one control, per completed turn — sentence-chunked
internally, never mid-sentence.**

Concretely, `lib/readAloud.ts`'s `speakText` splits `text` into sentences
(`/(?<=[.!?])\s+/`, the same construction `VoiceTurnBody.tsx`'s own
`countSentences` already uses for R17's element cap) and queues one
`SpeechSynthesisUtterance` per sentence via `speechSynthesis.speak()`,
rather than one utterance for the whole turn. Two independent reasons converged
on the same design, not one:

- **Correctness for Q1's "never truncated" guarantee.** Chrome has a
  long-standing bug where a single utterance longer than roughly 15
  seconds of speech silently stops
  ([chromium bug 679437](https://bugs.chromium.org/p/chromium/issues/detail?id=679437)).
  A multi-paragraph safety turn is exactly the text this project can least
  afford to cut off mid-sentence. Chunking sidesteps the bug entirely — no
  browser truncates a several-second sentence.
- **This step's own scope boundary against Stage 7.** The brief's framing
  ("speak only completed sentences or the completed turn, never a partial
  sentence") is exactly the granularity streaming will eventually need.
  Building the sentence-level queue now, gated to fire only after a turn
  is already complete, means Stage 7's own thread inherits a queue that
  already speaks in finished units — it only has to decide *when* to call
  `speakText` per-partial-turn, not invent chunking from scratch.

This step never speaks a turn before it's finished streaming in — the
control isn't even rendered until `turns` already contains the completed
entry (`useConversation`'s `send`/`begin` only append a turn once the
response has fully arrived; there is no partial-turn state in this
non-streaming API surface today). If Stage 7 introduces incremental text,
its own thread decides when "completed" fires; nothing here assumes
streaming exists or blocks it from landing later.

## 3. One control, not many

**Recommendation: one *global* control, in the conversation bar header —
not a per-turn button.**

This was the one real either/or in this design, so here are both options
argued honestly:

**Option A — turn-level button** (one per voice/Facilitator turn, e.g. in
the `turn__speaker` row). Pro: lets a participant replay *any* earlier
turn, not just the latest one; visually ties the control to the text it
reads. Con, and the reason it's not the recommendation: a Facilitator turn
has **no speaker row at all** — `Conversation.tsx`/`TableRoom.tsx` render
`facilitatorParagraphs(text)` as bare `<p>` tags, and the code comment
right above it is explicit: *"Facilitator turns are deliberately
UNLABELED — a participant learns to recognize the voice by how it reads,
not by a name tag"* (`CiC_Full_UX_Design_V1_0.md`, "talking not
texting"). A turn-level button would have to add a row that design
intentionally left out, for exactly the turns (safety redirects) where
adding new visual weight is least appropriate. It also multiplies R17's
own concern — a second, independent axis of per-turn on-screen chrome
growing alongside the transparency marks it already caps.

**Option B (recommended) — one global control**, rendered once in
`.conversation__bar` (next to `BrandMark`, grouped with the session note
in a new `.conversation__bar-right` wrapper), always targeting the latest
completed voice/Facilitator turn. It never touches Facilitator markup, it
is trivially "one global control, not many" by construction, and it
naturally enforces "only one thing speaks at a time" (there's exactly one
instance, so there's no cross-instance state to coordinate).

**Cost of Option B, stated plainly:** a participant cannot replay an
*older* turn in this step — only whatever is currently last. That's a
real, acknowledged limitation, not an oversight. Q8's usage metric is
exactly the signal that would justify building turn-level replay later
(if people are replaying the *same* turn a lot, or asking for older ones,
that's the case for Option A next); building it speculatively now would
be exactly the "no shortcuts, no features beyond what's needed" CLAUDE.md
already asks this project to avoid.

**Play / pause / stop — recommend two states (Play ⇄ Stop), not three.**
The brief asks for play, pause, and stop on the one control. Real pause/
resume support in `speechSynthesis` is inconsistent across engines —
notably unreliable on Android Chrome and effectively non-functional on
several mobile Safari versions (a paused utterance can silently fail to
resume). Building a pause state that quietly breaks on a meaningful slice
of phones is worse than not offering it. `ReadAloudControl` implements a
2-state toggle instead: click while idle → play; click while playing →
`cancelReadAloud()` (a real stop, not a pause) and back to idle. This is
one control, keyboard-operable (a native `<button>`), and never leaves a
participant stuck on a broken pause. If usage data or a specific
complaint later shows pause is actually wanted, it's addable without
changing this control's shape — a third `aria-pressed` state on the same
button, not a redesign. Flagging this as a place Mark may want to
overrule the recommendation, since the brief named pause specifically.

## 4. Screen readers

**Answer: nothing auto-plays, ever — so there is no double-speech to
detect or defer.** The control is a plain `<button>`. A participant
already using a screen reader hears it announced exactly like "Send" or
"Leave for now" (`ChatInput.tsx`) — silent until they choose to activate
it. There is deliberately no JavaScript screen-reader detection anywhere
in this implementation: reliably detecting a screen reader from the page
is not actually possible, and branching behavior on a guess is itself an
anti-pattern this design avoids rather than attempts. "Nothing auto-plays"
is enforced structurally, not just documented — `ReadAloudControl` has no
effect that calls `speakText` on mount, on props change other than the
one that resets state, or on any event other than its own `onClick`.

## 5. Accessibility standard (WCAG 2.2 AA)

Checked directly, not assumed:

- **Name, role, value.** Native `<button>` (`role="button"` implicit).
  Its accessible name *is* its visible text, which changes with state
  ("Read aloud" / "Stop reading") rather than being announced separately
  — same pattern `ChatInput.tsx`'s Send button already uses
  (`{disabled ? 'Sending…' : 'Send'}`). `aria-pressed` carries the
  play/idle value (`false`/`true`) per the WCAG 4.1.2 toggle-button
  pattern.
- **Focus visible (2.4.7 / 2.4.11).** Checked `app.css` for a global
  `outline: none` reset — there is none. Every button in this app,
  including this one, gets the browser's own default focus indicator;
  `.world-card` is the only element that layers a *custom* one on top,
  and this control doesn't need to duplicate that since the UA default is
  already sufficient and consistent with every other button on this
  screen (Send, Leave, the starter chips).
- **No motion.** No animation on state change — the label swaps text
  instantly, same as Send/Sending…. Nothing here needs a
  `prefers-reduced-motion` guard because nothing moves.
- **Target size (2.5.8).** `.read-aloud-control` is `min-height: 44px;
  min-width: 44px` — the same 44px floor `app.css` already uses for
  `.composer-row textarea`, `.level3__close`, and `.level2-card__full-entry`.
- **Works at phone width.** `.conversation__bar-right` is a flex row with
  `gap`, inside the existing `.conversation__bar` (`flex; align-items:
  center; justify-content: space-between`) — no fixed widths, no new
  breakpoint. Exercised in the component tests (jsdom, no real viewport)
  and by inspection against the existing 640px phone breakpoint
  (`useBreakpoint.ts`); a real-device screenshot pass is still owed before
  this ships for real (see "Verification" below).

## 6. Voice choice

**Answer: the browser's own default voice for the page — no picker, no
selection UI at all.** `SpeechSynthesisUtterance.voice` is never assigned
anywhere in `lib/readAloud.ts` — by construction, this can't offer a
voice picker even by accident, because there's no code path that reads a
choice and applies it. No gendered or "character" voice option exists in
this step, matching Mark's own sequencing (composite voice is explicitly
the *paid-tier* step, not this one).

## 7. Disclosure — RULED, wired in

**Mark's ruling (2026-09-22): Option A, exactly** — *"This reads the words
on screen aloud in your device's own voice — it isn't {representative_name}
speaking."* Shown as a **visible one-line note under the conversation
bar**, not a tooltip and not `aria-describedby` alone (Mark's own reason,
stated directly: a touch participant never sees either). The control's own
accessible name (§5) is untouched by this — the disclosure is a separate
line, not the button's label.

**Implementation.** `lib/readAloud.ts`'s `readAloudDisclosureText()` holds
the ruled sentence verbatim — not a prop a caller can override, the same
"a wording change is a change order" discipline every other approved
participant-facing string in this project already gets.
`components/ReadAloudDisclosure.tsx` renders it directly under
`.conversation__bar` (`Conversation.tsx`/`TableRoom.tsx`), gated on the
same voice-availability check `ReadAloudControl` uses (no disclosure about
a control that isn't actually showing).

**"The first time" is tied to the control's first target turn, not to
every render:** the note shows while `turnKey` is still whatever it was
when `ReadAloudDisclosure` mounted, and disappears for good the moment a
new turn becomes the latest one — one disclosure per session, not a
permanent banner repeated on every subsequent turn. `sessionStorage`
(`cic_read_aloud_disclosure_seen`) remembers "already shown" across a
reload of the same tab, matching `lib/sessionStore.ts`'s own established
"survive a reload, not a new tab" scope — without it, reloading
mid-conversation while the note is still up would look like a second
"first time" once React state resets.

**The Table's multi-voice edge case (not covered by the ruling, resolved
here as plumbing, not wording):** a Table sitting seats more than one
Representative, and the sentence's single `{representative_name}` slot
can't name all of them. Worse, the very first turn in *every* session —
interview or Table — is the Facilitator's own door turn
(`useConversation.ts`'s `begin()`), before any seated voice has spoken at
all, which is exactly the moment the disclosure is meant to show. For
Table sessions, `TableRoom.tsx` names the **first seated voice**
(`seatedWorlds[0].representativeName`) — a deterministic, documented
simplification, not a claim that voice specifically said anything. The
interview `Conversation.tsx` case has no such ambiguity: one Representative
per session, named directly regardless of which turn is currently latest,
the same way `engine/m4/crisis_resources.py`'s own `{representative_name}`
slot already works for the Facilitator's safety turns.

## 8. Measurement

**Answer: one number — the share of conversations with at least one
`read-aloud` play.**

No UX-telemetry pipeline exists yet in `cic-poc/frontend` — checked:
`engine/api`'s own `cic_api_events.db` (`config.py`,
`CIC_API_EVENTS_DB`) stores conversation transcript events for replay/
audit, not client-side UX interaction events, and there is no analytics
endpoint anywhere in `engine/api` to send this to. Building that pipeline
is out of this step's scope (and out of this thread's territory —
frontend only).

What this step actually built: `recordReadAloudPlay()`
(`lib/readAloud.ts`) dispatches exactly one `window` `CustomEvent`
(`'cic:read-aloud-play'`) each time a play starts. Nothing currently
listens for it. This is a single, already-named integration point for
whichever future thread wires up real analytics — it does not invent an
analytics pipeline, per the brief's own "do not build analytics beyond a
single client event if one already exists" (none exists; this is that one
event, stopped short of a sink).

---

## Verification

- `npm test` (vitest): 52/52 passing, including 20 new tests across
  `lib/readAloud.test.ts` (sentence chunking, cancellation, the
  no-speech-synthesis fallback, the crisis-turn-length case, the metric
  event, the disclosure text and its seen-tracking),
  `components/ReadAloudControl.test.tsx` (voice-availability gating,
  play/stop toggle, turn-key reset, unmount cleanup), and
  `components/ReadAloudDisclosure.test.tsx` (shows on first target turn,
  disappears on the next one, doesn't reappear on a fresh mount once
  already seen in the same tab).
- `npm run build` (tsc + vite build): clean.
- `npm run lint`: **could not run** — this checkout has no ESLint
  configuration file at all (`eslint . --ext ts,tsx` fails with "ESLint
  couldn't find a configuration file"), a pre-existing gap unrelated to
  this change; flagging it rather than silently skipping it or fixing it
  as a drive-by (out of this thread's scope).
- **Not yet done — the actual merge gate:** the dev server was not run
  against a live `engine/api` backend, so the control has not been heard
  actually speaking in a real browser. This is a Web Speech API feature,
  and jsdom (the test environment) has no real speech synthesis to
  exercise end to end — the unit/component tests above stub it. Per
  Mark's ruling, this PR does not merge until (a) the Conversation
  Transparency Engine thread's Stage 7 (streaming) has landed on `main`,
  and (b) Mark has heard the control speak in a real browser against a
  live backend and recorded what he heard.

## Open items — resolved and remaining

**Resolved by Mark's ruling (2026-09-22):**

1. **Disclosure sentence (Q7)** — Option A, exactly, now wired in behind
   the flag (§7 above).
2. **Disclosure placement** — a visible line under the bar, not a
   tooltip or `aria-describedby` alone.
3. **Play/Stop vs. Play/Pause/Stop (Q3)** — this note's recommendation
   stands: Play/Stop only.
4. **Header vs. turn-level (Q3)** — this note's recommendation stands:
   one global header control.

**Still remaining — not decisions, verifications:**

1. Stage 7 (streaming) landing on `main`.
2. Mark hearing the control speak in a real browser against a live
   `engine/api` backend, and recording what he heard.

The PR stays a draft until both are true. `VITE_READ_ALOUD` is not to be
turned on in any deploy config before then.
