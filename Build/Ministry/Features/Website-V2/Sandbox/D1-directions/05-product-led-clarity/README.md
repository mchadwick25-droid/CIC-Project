# D1 Direction 05 — Product-Led Feature Clarity

**Sandbox artifact. Not a deliverable, not final. 2026-09-02.**
Files: this README · `homepage.html` · `meet-chloe.html` (the inner journey). Both
open directly from disk; portraits and live-page links resolve by relative path into
`cic-website/`. Nothing outside this folder was touched.

## The philosophy, in my own words

A visitor should be able to answer three questions in the first few seconds — *what is
this, what can I do here right now, how do I do it* — and then do it in the fewest
steps that are still clear. The site is organized around the brand's own participation
verbs, each a real entry point: **meet** a Representative and begin a conversation,
**explore** the map, see what's **next**, help keep the door open. One job per section.
One primary action per screen. The real interface, not a description of it. Mobile
first, because the fastest path has to be fast on a phone.

The claim this direction makes is that *clarity is a structural property, not a visual
style*. The clearest product sites are clear because of hierarchy, one-thing-per-section,
progressive disclosure, and showing the product — not because of gradient blobs and
geometric sans. Those come apart, and this direction pulls them apart on purpose: it
keeps the grammar of a clear product site and sets all of it in CiC's own register, a
well-set trade book on parchment.

**The step map, measured.** Homepage → a real conversation in **one click**: every
Representative row carries "Begin a conversation," deep-linking to the live app in
interview mode. Homepage → an informed decision → conversation in **two** (row →
`meet-chloe.html` → Begin). Map: one click. Giving: one scroll, one click, on the real
Stripe links. Nothing asks for an account.

## How it serves the four charter goals

**Accessibility.** Landmarks, skip link, ordered headings, visible 2px focus rings,
44px targets, no text in images, reduced-motion honored, a dark register with re-checked
contrast, every app hand-off announced as a new tab. Floor and math below.

**Clear storytelling.** Told in the order a first-time visitor needs: the hook line; a
real exchange, so the thing itself tells the story; who is at the table; then the three
things the brand says to raise first — an AI system, it shows its work, witness never
recruitment. Protected lines verbatim where they belong; the mark's public sentence
beside the mark at first contact, said once.

**Easy access to features.** The direction's strongest goal by design. The seven
Representatives are the first section after the hero, each with its own primary action;
the Table is the quieter second path, in the app's own words; Map, What's Next, and Give
each get one clear entry. Nothing hides behind a sheet or carousel or needs JavaScript.

**Professional, cutting-edge design that draws people in.** "Cutting-edge" means the
confidence of the clearest product sites — restraint, hierarchy, the product shown
plainly — in a register nobody else in this space uses. The draw is the real exchange in
the hero: Chloe describing an ordinary Sunday, a glossed term and a ✲ in view. A visitor
who reads that paragraph already knows what this is for.

## The tech-forward tension, treated directly

A product-led direction is the one most likely to import startup furniture by reflex.
Here is what I refused and what replaced it, so a reviewer can check rather than trust:

| Refused | Substituted |
|---|---|
| Gradient blobs, glassmorphism, glows, floating drop-shadow cards | Flat parchment; vellum surfaces; hairline rules; no shadows anywhere; 2–3px corners |
| Device-frame screenshots (browser chrome, laptop bezel) | The preview is a **ruled leaf of the book** with a running head, in the app's shipped transcript grammar |
| Geometric/tech sans headlines | Alegreya for every headline and all reading; Alegreya Sans only for labels and buttons — the locked pair, nothing added |
| Icon-tile feature grids | Numbered items in madder rings (the live site's convictions device), ruled lists, small-caps labels |
| Pill buttons, header "Get started," floating CTA | Squared 3px buttons; no header CTA; the one sticky element is phone-only and named below as a stretch |
| Logo rows, counters, testimonial carousels | None; the only numbers are dates and era spans |
| Scroll-reveal, parallax, hover-lift | No motion but the mark on arrival; hover and focus are color changes only |
| Status chips and badges | Status carried in sentences ("designed and built once, not yet shipped") |
| "Users," "chat," exclamation marks | "Conversation" always; the AI question raised in plain words |

What I **kept** because it is structure, not style: one primary action per screen; a
real interface preview above the fold; an on-page picker instead of a "learn more"
detour; marginalia annotating the preview instead of prose about features; a
per-Representative page whose whole job is one decision and one button.

## What it sacrifices, named

- **Slow reveal and atmosphere.** No essay, no unhurried opening. A visitor who wants
  to be *led* rather than *shown* gets less here.
- **The Living Table as an image.** No scene, no figures — those aren't shipped, and
  previewing them would be a lie. The "product shot" is text: truthful, but quieter.
- **The map as spine.** The Atlas is one entry among four, not the organizing metaphor.
- **Pacing warmth.** The three-column block is scannable at the cost of being brisk;
  the protected lines carry the warmth, the layout adds none.
- **A longer page.** Seven rows in full instead of a carousel — deliberate (carousels
  hide content and fail keyboards), but it costs vertical space on phone.

## Typography, color, motion — inside the locked system

**Type.** Alegreya 1.08rem/1.65 reading; `clamp(2rem, 4.6vw, 3rem)` `h1`; Alegreya
Sans labels 0.78–0.95rem, uppercase, 0.1em tracking (the live eyebrow device). Italic
"in" in the wordmark, per the lockup rule the live site currently misses. Nothing
meaningful below 13px.

**Color.** Exactly the constitution's §2.1 tokens. Madder is the one action accent;
hover goes to `--madder-deep`, not gold-leaf. Gold-leaf marks the Representative's
label, Tyrian the glossed terms, lapis "You." The seven census tradition colors appear
only as a thin portrait ring and a small label — never a fill or wash. The transcript
leaf sits on `--gold-wash`, the decided reading surface.

**Contrast, checked (light):** ink on parchment ≈ 13.6:1 · madder on parchment ≈ 5.9:1
· vellum on madder button ≈ 6.4:1 · ink-faded ≈ 5.4:1 · gold-leaf ≈ 4.5:1 (AA at the
margin; used bold, ≈ 4.9:1 on vellum) · Tyrian on gold-wash ≈ 6.6:1 · every census
color as text on parchment 4.9–8.4:1. **Dark:** ground `#17130F`, madder-light
`#E08C74` ≈ 7.2:1, faded `#B8AEA1` ≈ 8.5:1, gold-light `#E0A458` ≈ 8.5:1, Tyrian-light
on the dark wash ≈ 6.9:1. Census colors fail as text on dark (some ≈ 2:1), so dark
labels fall back to the light ink and rings gain a 1px hairline edge — not a glow.

**Motion.** The Arriving mark's build-and-seat on arrival, once, from the brand's own
reference; reduced-motion gets the completed still mark. Nothing else moves.

## Accessibility floor: WCAG 2.2 AA, with reasons

AA, designed to from the start rather than audited into. Built for specifically:
1.4.3/1.4.11 contrast in both registers; 2.4.7 and **2.4.11 Focus Not Obscured** (the
phone sticky bar leaves a clear band above it); **2.5.8 Target Size** at 44px on every
button and inline action; 1.3.1 landmarks and heading order; 2.1.1 keyboard-complete
with no JavaScript; 3.2.4 consistent nav; 1.4.12 text spacing (no fixed heights).

Not AAA, and here is why: 7:1 text contrast would forbid madder and gold-leaf as text
on parchment — the brand's own locked accents. AAA would cost the palette without
buying real access. Taken from AAA cheaply: every new-tab link announces itself
(3.2.5); nothing is timed or moving to disable.

## Honesty ledger — real, draft, and what needs Mark

**Real, not written by me:** all Representative data (`world-census.json`); Chloe's
doorway paragraph and thinness statement (`records/worlds.yaml`); the starter questions
(`records/_fleet/canon_question/`); the captured exchange (`assets/tour-captures/`,
already shipped by the site); the Table description (Launch.tsx); the "name is ours"
line (Arrival.tsx); the pairings (pairings.ts); every protected brand line; the support
copy and Stripe links (live `support.html`); the What's Next items; Chloe's source
titles (`records/pahc/source/`).

**Draft, marked in source** with `data-copy="draft"` (greppable, invisible): section
intros, the hero's second sentence, the map blurb, the marginalia, the "meet the
others" line. One draft line quotes a number — "about ten exchanges," from the engine's
turn cap — that needs Mark's confirmation before print, per the brand rule on numbers.

**Verified in code, flagged for Mark:**
1. The multi-voice Table is live in the shipped frontend (Launch.tsx, TableRoom.tsx;
   three live Table conversations recorded 2026-08-28). Shown as the quieter second
   path per that day's ruling. Whether it is *meant* to be public (seam G) is Mark's call.
2. Nothing previews the Living Table scene, role selector, or guided onboarding
   (seam D) — the shipped transcript grammar only.
3. The capture's role label is the older "Host of the Assembly"; the mockup uses the
   registry's "Household Leader" and quotes only the answer.
4. `whats-next.html` still lists Cappadocian as in development (seam H, held); this
   mockup shows Chilo live and names the two traditions actually in development.
5. The map preview uses brand tokens; the Atlas still runs its own palette (seam C) —
   a D4 debt if this direction is chosen.
6. Multi-world deep-link grammar is unconfirmed; pairing links go to `?mode=table`.
7. The seven rows are hardcoded so the file opens from disk; the build should read
   `world-census.json` at runtime as the live homepage does.
8. Only Chloe's inner page exists; the other six "About" links are unbuilt.

**Proposed stretches for Mark to rule on:**
- **A phone-only sticky "Begin" bar** on the Representative page. Quiet-chrome ethos
  leans against it; task completion leans for it. Drawn as a ruled foot of the page on
  vellum — no shadow, nothing floats; desktop never gets it. Cut it and the page still
  works.
- **A 66rem width** for the picker and map (the live site holds 40rem for text, 60rem
  for the hero). Reading text stays at 42rem; only product surfaces widen.
