# Launch Prompt — Fix the mobile Level-2→Level-3 tap grammar

Paste this into a fresh thread (Sonnet is fine — no need for Opus/Fable).

---

## Scope note

On phone, tapping a lexicon term or citation marker currently skips straight
to the full Level-3 panel/sheet. The spec (`CiC_Build_Handoff_Increment1_
V1_0.md` §3, now merged into `main`) calls for a two-step grammar instead:
**tap → the Level-2 popover (term/citation name + short summary + a "Full
entry →" action) → tap that action → Level-3 opens.** This is genuinely new
interaction code, not a container/positioning change, which is why it was
kept out of Increment 1 and split into its own thread.

**Found and diagnosed, not guessed at, by the Increment 1 build thread** —
see `Ministry/Features/Increment-1-Build/Decision-Log.md`, "Found, not
fixed: the phone Level-2→Level-3 tap grammar," for the original account.
This predates Increment 1 entirely; the interaction code was written
mouse-first from the start.

## What governs

- `CiC_Build_Handoff_Increment1_V1_0.md` §3 (`Ministry/Features/Full-UX-
  Design/Design/`) — the grammar this is closing the gap on. Read the
  desktop hover→click behavior it describes as the reference: this fix
  brings phone to parity with it, not inventing new behavior.
- Nothing else changes. Content, positioning, and the Level-3 panel/sheet
  itself (built in Increment 1) are correct as they are — this is purely
  about what happens on a tap *before* Level-3 opens.

## Current-state grounding — verified 2026-07-20, re-check before editing

- `cic-poc/frontend/src/components/LexiconHighlight.tsx` and
  `CitationMarker.tsx` are near-identical in shape: both wire only
  `onMouseEnter`/`onMouseLeave` (show/hide a Level-2 tooltip) and `onClick`
  (opens Level-3 directly via `onDetailClick`). Confirmed by direct grep —
  no touch-specific handling anywhere in either file.
- **The Level-2 popover already exists as a component** — `LexiconHighlight`
  renders a `.lexicon-tooltip` div (header/content/footer) today, shown on
  hover. Its footer currently reads "Click for full entry," desktop-worded.
  `CitationMarker.tsx` has the equivalent structure. You likely don't need
  to build a new Level-2 surface from scratch — you need to make the
  *existing* one reachable and actionable on a tap, and reword its footer
  action for touch.
- No touch/pointer-type detection exists anywhere in either file today —
  confirm this is still true before assuming it, in case something else has
  touched these files since.

## What to produce

1. On a touch device, a tap on a lexicon term or citation marker should show
   the existing Level-2 popover (not fire `onDetailClick`/open Level-3
   immediately).
2. The popover's footer becomes a real tappable action ("Full entry →") that
   opens Level-3 on a second tap.
3. Tapping elsewhere (outside the term and the open popover) dismisses it,
   the same way the existing hover state dismisses on mouse-leave.
4. Desktop hover→click behavior is unchanged — this is additive for touch,
   not a rework of the existing mouse path. However you distinguish "this is
   a touch interaction" is your call (a media query on `(hover: none) and
   (pointer: coarse)`, feature-detecting touch events, etc.) — pick
   whichever the codebase's existing patterns favor, don't invent a new
   convention if one's already in use elsewhere in `cic-poc/frontend`.
5. Verify the same way Increment 1 did: DOM/computed-state assertions
   against a real dev server at a phone viewport width, not just eyeballing
   a screenshot. If you can't stand up the real backend, the Increment 1
   thread's scratch mock-API approach (matching `world_manifest.py`'s real
   data and the real SSE event shape) is a reasonable model — just don't
   commit the mock itself.

## Coordination boundary

Stay inside these two components and their direct styling. Don't touch
`Level3Panel.tsx`, `TheTable.tsx`, or anything Increment 1 already built and
merged — this fix sits entirely upstream of where that work starts. If
something outside this scope looks wrong while you're in there, log it and
hand it back rather than fixing it inline.

## Logging

`Ministry/Features/Level2-Mobile-Popover/Decision-Log.md` (new — create
it), same dated-entry discipline as every other thread. Report back to
System Hub when done.
