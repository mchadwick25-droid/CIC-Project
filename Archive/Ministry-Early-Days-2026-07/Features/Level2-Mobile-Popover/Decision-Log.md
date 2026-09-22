# Decision Log — Level-2 Mobile Popover Fix

## 2026-07-20 — Two-step tap grammar built and verified against the real merged app

**What this is:** the build thread dispatched by `Ministry/Features/
Level2-Mobile-Popover/Launch-Prompts/CiC_Level2_Mobile_Popover_Thread_
Launch_2026-07-20.md`, closing the gap the Increment 1 build thread found
and flagged (`Ministry/Features/Increment-1-Build/Decision-Log.md`,
"Found, not fixed: the phone Level-2→Level-3 tap grammar") — on phone, a
tap on a lexicon term or citation marker was skipping straight to
Level-3 instead of the spec'd tap → Level-2 popover → tap "Full entry" →
Level-3.

**Branch/base:** built directly on `main` at `61ec011` (Increment 1
merged, this thread's own dispatch logged). The worktree this thread
started in had branched *before* Increment 1 merged — caught before any
edits landed, by re-checking the "current-state grounding" against the
actual running app rather than trusting the launch prompt's file
excerpts alone. Fixed with `git stash` (isolating the three real edits)
+ `git merge --ff-only main` (worktree HEAD was a strict ancestor of
`main`, so this was a clean fast-forward, no divergent history) +
`git stash pop` (a clean three-way auto-merge in `table.css`, no
conflict markers, hand-verified). Logged here because it cost real time
to catch and could bite a future single-purpose thread the same way if
its worktree is cut before a sibling thread's merge lands.

**What was built** (`cic-poc/frontend/src/components/LexiconHighlight.tsx`,
`CitationMarker.tsx`, `cic-poc/frontend/src/styles/table.css`):

- A `lastPointerTypeRef` on each component, updated by a new
  `onPointerDown` handler, tracking whether the *most recent* pointer
  interaction on that term/marker was touch, mouse, or pen —
  per-interaction, not a one-time device or viewport check.
- `handleClick` branches on that ref (read fresh at call time, see the
  stale-closure note below): touch → `setShowTooltip(true)` only, never
  `onDetailClick`; mouse → unchanged, calls `onDetailClick` immediately
  (today's desktop behavior, since hover already showed Level-2).
- The popover's footer (`.lexicon-tooltip__footer` /
  `.citation-tooltip__footer`) changed from an inert `<div>` to a real
  `<button type="button">` with its own `onClick` (`stopPropagation` +
  close the popover + call `onDetailClick`) — this is what opens Level-3
  on touch. Label reads "Full entry →" when the last interaction was
  touch, unchanged "Click for full entry" / "Click for full sources"
  otherwise.
- A touch-only `useEffect` on each component adds a capture-phase
  `document` `pointerdown` listener while the popover is open, closing it
  on any tap outside the term/marker's own DOM subtree (which already
  contains the popover, since it's rendered as a child span/div) — the
  touch equivalent of desktop's `onMouseLeave`. Desktop doesn't get this
  listener (gated on `isTouch()`), since `onMouseLeave` already covers it
  and there's no reason to add extra document-level listeners on every
  desktop hover.
- `table.css`: both tooltip boxes are `pointer-events: none` (intentional
  — on desktop this lets a click pass through the hovering tooltip to the
  underlying term/marker span, which is what makes today's "hover shows
  Level-2, click opens Level-3" grammar work at all). Converting the
  footer into a real button meant it needed its own `pointer-events:
  auto` carve-out, or it would be visually present but untappable on
  touch. Reset the rest of the button's default chrome (border, background,
  full-width, text-align) to reproduce the original `<div>`'s exact box
  model rather than accepting default browser button styling.

**A real bug caught by testing, not just reasoning:** the first version
computed `const isTouch = lastPointerTypeRef.current === 'touch'` once at
the top of the component body and used that constant inside `handleClick`.
This is a classic stale-closure trap — mutating a ref does *not* itself
trigger a re-render, so `handleClick`'s closure (fixed at whatever render
last ran before the tap) still held the value from *before* `onPointerDown`
updated the ref. A synthetic touch tap (`pointerdown` with
`pointerType: 'touch'`, then `click`) still opened Level-3 directly,
reproducing the original bug under the "fixed" code. Caught by asserting
DOM state after a real dispatched interaction, not by reading the diff.
Fixed by making `isTouch` a function that reads `lastPointerTypeRef.current`
fresh every time it's called, inside `handleClick`, inside the outside-tap
effect's gate, and inside the footer label's JSX — never captured as a
plain value. Left as an explicit comment in both files so it isn't
reintroduced.

**Why per-interaction pointer-type tracking, not a media query or
viewport-width check (Increment 1's own established convention for
"phone"):** tried `window.matchMedia('(hover: none) and (pointer: coarse)')`
first, since that's the technically-correct "does this device support
hover" signal. It does not respond to the Browser-pane test tool's
viewport resize (confirmed directly: `matchMedia('(pointer: coarse)')`
read `false` even at a 375×812 resized viewport, while `navigator.
maxTouchPoints` read `10` — the test host reports itself as touch-capable
at the navigator level but not through CSS media features under this
tool's resize, at least in this environment). That made it untestable
here without eyeballing a screenshot, which the spec's own verification
bar rules out. Viewport-width breakpoints (the pattern Increment 1 uses
everywhere else, e.g. `Level3Panel`'s 900px side-panel/sheet split) were
considered too, but width is a proxy for touch, not touch itself — a
desktop user who narrows their browser window would wrongly get the tap
grammar. Per-interaction `pointerType` (via `onPointerDown`) is both the
more correct signal (a real phone always reports `touch`; a real desktop
mouse always reports `mouse`; a hybrid touch+mouse device gets the right
grammar for whichever input actually triggered the tap) and the only one
of the three that's exercisable against this dev environment: dispatching
a synthetic `PointerEvent` with `pointerType: 'touch'` reliably reaches
React's handler and reflects the real interaction, without needing real
device emulation. No existing touch/pointer-type convention was found
anywhere else in `cic-poc/frontend` to defer to instead (confirmed by
grep before starting, per the launch prompt's own instruction to
re-check rather than assume).

**Keyboard/accessibility default:** `lastPointerTypeRef` defaults to
`'mouse'`, so a keyboard-triggered click (`Enter` on a focused term, no
preceding `pointerdown`) gets today's desktop behavior — Level-3 opens
directly — rather than landing a keyboard user on a popover whose only
next action (tap the "Full entry" button) has no obvious keyboard
equivalent bound to it. Not asked for by the spec either way; chosen to
avoid a plausible new keyboard-accessibility regression.

**How this was verified — real merged app, real dev server, DOM/computed-
state assertions, not eyeballing:**

- `npx tsc --noEmit` — clean.
- `npm run build` (`tsc && vite build`) — clean, real production bundle
  produced.
- Ran the actual Vite dev server against the real, current (Increment-1-
  merged) `cic-poc/frontend` source, at a 375×812 phone viewport, using a
  small dependency-free stdlib-only Python mock backend (scratch-only,
  never committed) serving two real worlds' names/colors/periods from
  `world_manifest.py` and a canned assistant turn containing a real
  lexicon term (`raza`) and two citations, matching `StartSessionResponse`/
  `Message`/`Citation` shapes from `types/conversation.ts`.
- **Found and worked around a real environment hazard, not a code bug:**
  a genuine `cic-poc-backend` uvicorn dev server from another session was
  already running on port 8000 in the shared checkout. Windows allowed
  both it and this thread's own mock to simultaneously bind and `LISTEN`
  on `127.0.0.1:8000`, with requests routing unpredictably between the
  two (confirmed by comparing response bodies — the real backend's full
  paragraph world descriptions vs. the mock's short-form ones showed up
  interchangeably). Never touched or killed the other session's backend.
  Instead moved this thread's mock to port 18000 and temporarily
  retargeted `vite.config.ts`'s dev proxy to match, verified, then
  reverted `vite.config.ts` to its original committed state (`git
  checkout --`) before any commit — confirmed via `git diff` showing an
  empty diff on that file post-revert. Worth flagging to System Hub: a
  stray backend from a prior session can silently answer a later
  session's "isolated" mock-backed testing on this machine, which cost
  real time here and could recur for the next thread that assumes a
  freshly-bound port is actually isolated.
- With that isolated, drove the real rendered page via dispatched native
  `PointerEvent`/`MouseEvent`s (through `javascript_tool`, since
  `computer`'s click/screenshot actions were unreliable this session —
  same issue Increment 1's own log notes; DOM assertions were used
  instead, not screenshots) and asserted on actual DOM/class state after
  each:
  - Touch tap (`pointerType: 'touch'`) on the `raza` lexicon-term span →
    `.lexicon-tooltip` appears, its footer is a `<button>` reading "Full
    entry →", and `.level3-backdrop` (the Level-3 open indicator) does
    **not** appear. This is the exact assertion that caught the
    stale-closure bug above — it failed on the first version.
  - Tap on that footer button → `.level3-backdrop` appears with the real
    full lexicon entry content, and `.lexicon-tooltip` closes.
  - Fresh tap to reopen, then a tap on `document.body` (outside both the
    term and the popover) → `.lexicon-tooltip` closes.
  - `mouseover`/`mouseout` (no prior touch on that element) → popover
    opens/closes exactly as before this fix, footer still reads "Click
    for full entry" — confirmed desktop wording/behavior is byte-for-byte
    unchanged.
  - A `pointerType: 'mouse'` `pointerdown` + `click` on the term (no
    hover first) → `.level3-backdrop` opens directly, matching today's
    desktop click behavior exactly.
  - All five checks above repeated for `CitationMarker`
    (`.citation-marker` / `.citation-tooltip`) against the same session's
    two-citation turn — identical results, including the real citation
    detail (source names, term) rendering in Level-3.
- **One genuine test-order artifact, not a code bug, worth recording
  honestly rather than hiding:** an early combined test dispatched a
  touch tap on `CitationMarker`, then a `mouseover` in the *same* script
  run, and the footer read "Full entry →" during that hover — because
  `lastPointerTypeRef` only updates on `pointerdown`, and hovering with a
  mouse (no click) never fires one, so the ref still held `'touch'` from
  moments earlier in that same test. Re-ran the hover check alone,
  against a freshly reloaded page with no prior touch interaction on that
  component instance, and got the correct "Click for full sources" both
  times (lexicon and citation). The underlying *click* grammar was never
  wrong in the contaminated run either — `pointerdown` always precedes
  the click that actually opens or doesn't open Level-3, so the decision
  is always correct per-interaction; only the footer's preview *label*
  can transiently lag on a hybrid device that mixes touch and mouse
  without clicking in between, which real single-input-type phones and
  desktops can never produce. Accepted as a known, narrow limitation of
  the per-interaction approach rather than engineered around further —
  see "Found but not fixed" below.

### Deviations from the spec, and why

None substantive. Stayed entirely inside `LexiconHighlight.tsx`,
`CitationMarker.tsx`, and the two tooltip-footer rules in `table.css`,
per the coordination boundary. The one markup change outside a pure
event-handler edit — the footer `<div>` becoming a `<button>` — was
necessary to satisfy requirement 2 ("a real tappable action") and is
still confined to "these two components and their direct styling" as
instructed; desktop's net behavior through that footer is unchanged
(clicking it already bubbled up to open Level-3 before this fix; now it
does so via its own handler, same result, verified above).

### Found but not fixed — logged and handed back, per the launch prompt's own instruction

- **The shared-port backend hazard described above** isn't a code defect
  in `cic-poc` itself, but it's a real environment/workflow gap worth
  System Hub's attention: nothing currently stops two dev-server
  instances (a real backend and a thread's own scratch mock, or two
  threads' real backends) from both binding `127.0.0.1:8000` on this
  Windows machine and silently splitting traffic. A future thread that
  assumes "my mock is the only thing on this port" could get
  intermittently wrong data, or worse, accidentally exercise someone
  else's real Anthropic API key/session, without any error to signal it.
- **The per-interaction `pointerType` tracking's hybrid-device label lag**
  (previous section) — cosmetic only, footer label can transiently show
  the wrong wording on a device that mixes touch and mouse without a
  click in between; the actual open/no-open grammar is never affected.
  Not fixed further since it requires a real hybrid touch+mouse device to
  ever manifest, isn't covered by the spec either way, and any fix (e.g.
  also updating the ref on hover) would blur the "most recent pointer
  interaction" signal in the other direction (a mouse just passing over a
  touch-primary phone's term — not a real scenario — would incorrectly
  flip it back to desktop mode).
- **`computer`-tool clicks and screenshots were unreliable this session**
  (coordinates that should have hit a button/card sometimes registered
  nothing; `screenshot` timed out repeatedly against a page that
  `get_page_text`/DOM checks confirmed was rendering correctly). Same
  symptom Increment 1's own Decision Log recorded independently. Worked
  around with `javascript_tool`-dispatched native events and direct DOM
  assertions throughout, per the spec's own verification bar. Not
  diagnosed further — outside this thread's scope, and a second
  independent report of the same symptom is probably worth someone
  looking at the tool itself rather than either build thread guessing at
  a per-page cause.
