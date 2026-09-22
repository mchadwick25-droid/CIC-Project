# Read-Aloud, Step 1 — Design Note

**Status: PROPOSED, awaiting Mark.** Nothing here ships until Mark rules on
Q7 (the disclosure sentence) and the flag is deliberately turned on for a
real environment. `VITE_READ_ALOUD` defaults off everywhere.

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

## 7. Disclosure — ESCALATED, not shipped

**This is not decided here.** Per the brief, participant-facing wording is
Mark's call, not this thread's. `ReadAloudControl.tsx` and `lib/
readAloud.ts` carry no participant-facing disclosure copy anywhere, even
though the flag defaults off — the sentence is drafted below for the
artifact page, not wired into any component.

**Where it would attach:** the natural spot is the first time the control
ever renders in a session — e.g. a one-line note directly under
`.conversation__bar` the first time `ReadAloudControl` mounts, or a
`title`/`aria-describedby` on the button itself. Which of those (a
persistent visible line vs. a tooltip-style description) is itself a
small open question worth Mark's input, not just the sentence's wording.

**Draft options** (for Mark to react to, not to treat as decided):

- **A.** *"This reads the words on screen aloud in your device's own
  voice — it isn't {representative_name} speaking."*
- **B.** *"Read aloud uses your browser's built-in voice to read this text
  out loud — a generic voice, not a recording of {representative_name}."*
- **C.** *"This button has your browser read the text aloud in its own
  voice. It's your device speaking, not {representative_name}."*

Recommendation if asked: **A**, shortest and states the one fact that
actually matters (not a real voice, not the Representative) without
over-explaining. All three are B2/grade-8-appropriate by the same
standard the rest of participant-facing copy in this project is held to.

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

- `npm test` (vitest): 46/46 passing, including 14 new tests across
  `lib/readAloud.test.ts` (sentence chunking, cancellation, the
  no-speech-synthesis fallback, the crisis-turn-length case, the metric
  event) and `components/ReadAloudControl.test.tsx` (voice-availability
  gating, play/stop toggle, turn-key reset, unmount cleanup).
- `npm run build` (tsc + vite build): clean.
- `npm run lint`: **could not run** — this checkout has no ESLint
  configuration file at all (`eslint . --ext ts,tsx` fails with "ESLint
  couldn't find a configuration file"), a pre-existing gap unrelated to
  this change; flagging it rather than silently skipping it or fixing it
  as a drive-by (out of this thread's scope).
- **Not yet done:** the dev server was not run against a live
  `engine/api` backend, so the control has not been seen actually
  speaking in a real browser. This is a Web Speech API feature, and jsdom
  (the test environment) has no real speech synthesis to exercise end to
  end — the unit/component tests above stub it. A manual check in an
  actual browser (with a real backend, or against the fixture world) is
  owed before this flag is ever turned on anywhere real.

## Open items for Mark

1. **Disclosure sentence (Q7) — required before shipping at all.** Pick
   one of A/B/C above, edit it, or reject the idea of a persistent
   sentence in favor of something else entirely.
2. **Disclosure placement** — a visible line under the bar the first time
   the control appears, vs. a `title`/description on the button itself.
3. **Play/Stop vs. Play/Pause/Stop (Q3)** — this note recommends the
   simpler 2-state version for reliability; overrule if a real pause
   matters enough to accept the cross-browser risk.
4. **Header vs. turn-level (Q3)** — this note recommends the global
   header control; overrule if replaying older turns matters enough now
   to accept adding a row to Facilitator turns.
