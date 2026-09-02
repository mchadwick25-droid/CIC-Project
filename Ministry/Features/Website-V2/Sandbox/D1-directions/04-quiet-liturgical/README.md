# Direction 04 — Quiet-Liturgical

**D1 sandbox artifact. Not a deliverable, not final copy, not to be merged.**
Files: this README, `homepage.html`, and `before-you-sit.html` (the one inner
journey). Both open directly in a browser; images and nav targets are
referenced relative to the repo.

## The philosophy, in my own words

The Living Table is built on a refusal: no camera, no glow, no vignette, no
dimming; everyone solid and present the whole time; the only cue a printed
nameplate going dark. That refusal is a posture, not a style, and this
direction carries it out of the app and onto the front door.

The site is treated as the narthex — the room you cross before the room where
the thing happens. A service opens with silence, then a greeting; the order
unfolds at a pace the people did not choose. So the homepage is written as an
**order of arrival**: *Threshold ·
(a silence) · Greeting · The Table · (a silence) · The Door*. The first screen
is the mark, its one public sentence, and nothing else. The silences are
literal: empty parchment given real height, one red rubric — *Silence is kept.*
— and the way on printed quietly beneath it. Nothing fades, slides, lifts,
counts down, or reveals on scroll; everything is present from the first paint.
The only thing that moves is the brand's own "Arriving" motion, once.

The bet: the charter's "life-changing journey" is better served by a visitor
who arrives *slowed* than by one who arrives *converted*. The site sets the
table; it does not close.

## Against the four charter goals

**Accessibility.** Slowness lives *in the shape of the page, never in a gate*:
no timers, nothing withheld until a delay passes, no auto-advance, no
interruptions — so three of WCAG 2.2's AAA timing-and-motion criteria come
free (listed under the floor). Scroll-snap is `proximity`, desktop-height
only, and off under `prefers-reduced-motion`. Contrast math is below.

**Clear storytelling.** The order *is* the story: a table, its way in, who is
seated, a door. The AI trust question is raised by us first, in the Greeting,
before the seven are named — the brand's "Always" made structural. Protected
lines are verbatim and never paraphrased (`data-copy="protected"` in the HTML;
my own prose is `data-copy="draft"`). The seven are set one at a time, in
order, as places at a table — never a carousel; a carousel is a hurry.

**Easy access to features — the real tension, treated directly.** Slow is not
always better. A returning participant, a pastor back for a fourth
conversation, a reviewer sent a link — none should walk the narthex twice.
Liturgy knows this: the order does not change for the faithful; they are
simply not catechized again. Four concrete side doors follow, each defensible
against D2:

1. **The side door in the header, every page** — *"Already know the way? Go to
   the Table →"* — a quiet text link straight to the app. Never a button.
2. **The order marker** (fixed left on wide screens, a sticky strip otherwise):
   four still words, one click to *Door* from anywhere.
3. **Each of the seven carries its own action** — *Sit down with Chloe* — at the
   place where the visitor meets her.
4. **The narthex remembers.** `before-you-sit.html` records (localStorage, in
   try/catch) the first seat taken from it; on later visits its first screen
   offers *Go straight in →*. The slow walk is a first-time rite, not a tax.

What stays slower: a first-time visitor is about eight screens from arrival to
the door, and the first screen carries no headline and no button. That cost is
chosen; D2 should price it.

**Professional / cutting-edge design that draws people in.** The edge is
restraint executed exactly: the lockup rule honored (italic *in*, which the
live header drops); the mark at first contact *with* its one sentence (the
Usage Sheet requires it; the live header shows the mark bare); the Living
Table's nameplate inversion as the site's only selection device; a motion
policy specific enough to audit. Cutting edge the way a well-set book is —
nothing on it will date.

## What it sacrifices, named

- **The above-the-fold convention.** No headline, no CTA, no proof on screen
  one. A five-second decider leaves. Search snippets still carry the hook (the
  `<h1>`, at the second station); the first paint does not.
- **Density.** Seven full rows, not seven cards. The page is long.
- **Conversion pressure.** None. The pilot ask and the support slot sit below
  the door in the quietest register on the page.
- **Motion-rich "modern."** Refused: no reveal-on-scroll, no hover lift, no
  transitions (`transition: none` globally).
- **The phone.** Silences shrink to 55vh and the marker becomes a strip; the
  philosophy is weaker in the hand than on a desk.

## Typography, color, motion — within the locked system

**Type.** Alegreya for everything read (body 1.125rem/1.75; the hook
`clamp(2rem, 4.6vw, 3.1rem)` at weight 500); Alegreya Sans for chrome, labels,
and the order marker. No new face. Rubrics — the red instructions of a service
book — are Alegreya italic in madder, used only for *Silence is kept.* and the
station eyebrows.

**Color.** The manuscript palette unchanged: parchment ground, iron-gall text,
madder as the one action accent and rubric ink, gold-leaf for the tradition
name beside each Representative (the brand's "Representative voice" pigment),
ink-faded for secondary text. Portrait ring hues are each entry's own census
color, as the live carousel already uses them — the Atlas palette debt (seam
C), inherited and named. Dark mode reuses the live site's proven values.

**Motion — the entire inventory.**

| What | Moves? | Why |
|---|---|---|
| "Arriving" mark, hero, ~170px | Once per arrival, exactly per the brand reference (800ms wait · 1300ms build · 600ms sit). Its slow breath continues. | The one sanctioned motion. The breath stays because the brand says the dot is the guest, alive — not mine to still. |
| Header | Nothing; wordmark only | So the mark is never on screen twice, never plays twice. |
| Scroll | Smooth + soft snap, **only** ≥900×700 and `no-preference` | The visitor's own act, unhurried; never a snap they didn't scroll toward. |
| Order marker / chosen seat | Instant solid inversion | The Living Table's nameplate device; nothing slides. |
| Hover / focus | Instant color or border swap | No lift, no transition. |
| The chair, `before-you-sit.html` | Pulled up once, per the companion reference; never breathes | That page's one motion; its header is wordmark-only, so the adjacency guard holds by construction. |
| `prefers-reduced-motion` | Still mark, still chair, no smooth scroll, no snap | The brand rule, applied to the whole page. |

Nothing else moves.

## Accessibility floor

**WCAG 2.2 AA, plus four AAA criteria adopted as binding because the philosophy
already demands them:** 2.2.3 No Timing, 2.2.4 Interruptions, 2.3.3 Animation
from Interactions, 2.4.8 Location. AAA contrast is not claimed globally — the
locked accents don't reach 7:1 — though body text does.

Contrast, computed, for every pair actually used:

| Pair | Ratio | AA text? |
|---|---|---|
| iron-gall `#2A2521` on parchment `#F7F3EB` | 13.70:1 | yes (AAA) |
| madder `#A13E2B` on parchment (rubrics, links, eyebrows) | 5.86:1 | yes |
| ink-faded `#6C6257` on parchment (secondary) | 5.39:1 | yes |
| gold-leaf `#B45309` on parchment (tradition names, 1.125rem) | 4.54:1 | yes, narrowly |
| vellum on madder fill (the button) | 6.33:1 | yes |
| inversion `#F6EFE0` on `#2A2521` | 13.24:1 | yes |
| dark: `#F1E9DD` / `#B8AEA1` / `#E08C74` / `#E0A458` on `#17130F` | 15.35 / 8.45 / 7.19 / 8.47 | yes |
| dark inversion `#17130F` on `#EDE5D6` | 14.76:1 | yes |

**One finding to carry out of this folder:** graphite `#8A837C`, the
constitution's Facilitator color, measures **3.38:1** on parchment and 3.36:1
on gold-wash — below AA for body text (it passes only at ≥24px, or 18.66px
bold). This mockup sets no graphite text below that size. The in-app
transcript sets the Facilitator's lines in graphite at 1.0625rem — an
app-thread question, out of scope here, but real and worth logging.

Also built in: skip link; one `<h1>`; landmarks; 24×24 targets (2.5.8); a
visible madder focus ring; `scroll-padding-top` so the sticky strip never
obscures focus (2.4.11); real alt text; the page complete without JavaScript.

## Proposed stretches — for Mark to rule on

1. **The mark leaves the homepage header.** It plays in the hero at first
   contact *with* its public sentence; the header carries the wordmark only.
   A departure from the live header convention, not from any brand rule.
2. **The soft scroll-snap.** Technically a scroll the visitor did not make.
   Gated hard; if "no motion" reads as absolute for the site, it goes.
3. **A second threshold.** `before-you-sit.html` says on the site part of what
   the app's onboarding/consent screen (X.1) says. Accept two thresholds, let
   the seven's links bypass it, or drop it and keep only the homepage's door.
4. **Where the chair motion plays.** The Usage Sheet leaves placement to the
   UX thread; the narthex is proposed as an empty state (seat not yet taken).
5. **Seam G mirrored, not decided.** Free interview primary, quiet "bring them
   to the Table" second, exactly as the live sheet does.

Not done, on purpose: the six historical-site photos (not cleared); any
composed multi-seat table scene (it would promise the Living Table before it
ships — seam D); any "in development" status claim (seam H).
