# D2 adversarial review — Direction 01, Editorial / Long-Form Storytelling

**Sandbox artifact, 2026-09-02. Adversarial by commission: my job was to try to kill
this direction, not to be balanced. Nothing here is a ruling. The author gets one
defense before anything is decided.**

Reviewed: `Sandbox/D1-directions/01-editorial-longform/` — `README.md`,
`homepage.html` (666 lines), `representative-chloe.html` (399 lines), all read in
full. Read against `Website-V2/README.md`, `Website-V2/Decision-Log.md` in full
(including both of Mark's verbatim 2026-09-02 entries), the D0 Inheritance Note,
`CiC_Brand_Guidelines_Consolidated_V1_0.md`, `CiC_Logo_Usage_Sheet_V1_0.md`,
`CiC_Full_UX_Design_V1_0.md`, the live `cic-website/*.html` + `assets/style.css`,
and `cic-website/data/world-census.json` directly. I did **not** open any other
D1 direction and did **not** read `05-product-led-clarity-review.md`, so no part of
this is calibrated against another reviewer's standard.

---

## 0. Method, and what I could and could not verify

Chromium (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`) via Playwright,
`executablePath` passed explicitly. Both files rendered at 320 / 360 / 390×844 /
479 / 481 / 640 / 760 / 761 / 768×1024 / 820×1180 / 900 / 901 / 1000 / 1024 / 1100 /
1280 / 1440×900 / 1700, in light and dark `prefers-color-scheme`, with and without
`prefers-reduced-motion`, with and without JavaScript, and under `print` media.
Real keyboard `Tab` traversal, a Chrome-DevTools-Protocol full accessibility tree,
computed-style contrast measured against the actual painted background, and a
generated print PDF.

**The honest caveat: the sandbox blocks `fonts.googleapis.com`, so every render was
in fallback faces** (DejaVu substituting Alegreya / Alegreya Sans; Alegreya SC absent
entirely, so `.sc` degraded to letterspaced lowercase rather than true small caps).
That affects **only** the numbers that depend on glyph widths and line-breaking:
page heights, screen counts, and the exact pixel width at which the header breaks.
It does **not** affect contrast ratios, computed colors, DOM/AX semantics, tab
order, focus behaviour, print-media computed opacity, link decoration colors, or
whether an element overflows its container — all of which are font-independent and
all of which I measured directly. Where a finding is font-sensitive I say so and
give the mechanism, not just the pixel.

I also cross-checked every factual claim the mockup makes — tradition names, dates,
regions, Representative names and titles, hex tints, portrait pixel dimensions, the
Atlas movement count, the "two more in development" list — against
`world-census.json`. **They are all correct**, including the two-not-three
development count that contradicts the still-stale live `whats-next.html`. The
author verified against data rather than a planning doc, and said so in the draft
tag. That is the standard, and I am not going to pretend otherwise in order to land
a hit.

---

## 1. Charter-goal failures — the README's claims against the actual markup

I tested the five self-assessed claims. Three are false as built, one is true but
irrelevant, one is true.

### 1.1 "The contents page … one screen below the masthead" — false, by 2× to 3×

Measured document-Y of `#contents`:

| viewport | `#contents` at | screens down |
|---|---|---|
| 1440×900 | 2026px | 2.3 |
| 390×844 | 2860px | **3.4** |

Between the masthead and the contents sit five essay paragraphs, two sidenotes and
a pull quote. On the device most people will actually use, the index of the book is
three and a half screens into the book. The header "Contents" link mitigates it —
but see 1.2 for what that link actually costs.

### 1.2 "A returning visitor is one click from anything" — false; it is three clicks and two waits

Traced the real path for *"I want to talk to Papnoute again"*:

1. Click **Contents** in the running head. `html{scroll-behavior:smooth}` (line 53)
   animates ~2,800px on a phone.
2. Click **Desert Fathers and Mothers**. Smooth-scroll again, ~4,700px on a phone.
3. The destination chapter is `.reveal` and starts at `opacity:0` (line 117).
   **Measured:** 700ms after arriving at a jumped-to chapter, computed opacity was
   `0.388`; it does not reach `1` until roughly 1.5–2s after arrival. Your
   destination fades in *after* you get there.
4. Now find **"begin a conversation with Papnoute"** — and this is the real failure:

### 1.3 "Easy access to features" — the 14 conversation links are visually indistinguishable from body text

`.chapter .begin a` (line 242) sets `color:var(--ink-faded)` and
`text-decoration-color:var(--rule)`. Measured computed values on every one of the
14 per-chapter handoff links:

```
color            rgb(108, 98, 87)   ← identical to parent .begin text color
parentColor      rgb(108, 98, 87)
text-decoration  underline, color rgb(230, 223, 211)   ← #E6DFD3
```

`#E6DFD3` against parchment `#F7F3EB` is **1.196:1**. So the underline — the only
non-color affordance — is effectively invisible, and the link color is *exactly*
the color of the words around it. In the sentence "Or begin a conversation with
Chloe · bring Chloe to the Table", nothing distinguishes the link from the "Or".

These 14 links are the direction's only per-tradition path into the product. They
are the least visible interactive elements on the page — quieter than the Atlas
link, quieter than the two Stripe buttons, quieter than the footer's Privacy link.
A direction whose stated third goal is *easy access to features* has styled feature
access to disappear. This is not a taste dispute; it is a measured 1.196:1 and an
exact color match, and it is a WCAG 1.4.1 (Use of Color, **Level A**) problem in
substance even if an auditor grants that a 1.196:1 underline technically counts as
a non-color cue.

### 1.4 "One door, always in the same place… that is the entire CTA inventory" — false

Measured link inventory on `homepage.html`: **57 links**, of which

| kind | count |
|---|---|
| in-page anchors (contents, sidenote targets, essay jumps) | 31 |
| app handoffs `?mode=table` | 9 |
| app handoffs `?mode=interview` | 7 |
| Stripe | 2 |
| Atlas | 2 |
| mailto | 3 |
| other pages | 3 |

Sixteen separate app handoffs, not one door. The "one door" is a rhetorical frame
in the README, not a property of the artifact. That would be fine — 57 links on a
2,663-word page is normal — except that the direction *spent* its restraint budget
on the wrong thing: it kept 31 in-page anchors at full visibility and hid the
sixteen links that lead to the product.

### 1.5 "Target size ≥24×24 on every inline control" — false as stated

Measured heights of real focusables on the homepage: "begin a conversation with X"
**18px**, "bring X to the Table" **18px**, "Read X's introduction →" **21px**,
"Open the Atlas →" **22px**, colophon mailto **22px**, footer mailto **16px**.
That is roughly twenty controls under the claimed floor.

Being fair: WCAG 2.2 SC 2.5.8's *inline* and *spacing* exceptions probably keep the
page conformant (I measured the vertical gap between the "Read" line and the
"begin" line at 13px, which clears the 24px-circle spacing test at 32.5px between
centers). So this is not a conformance failure — it is the README asserting a floor
it did not meet, in a document whose whole credibility play is "I showed my work."

### 1.6 What is actually true

- **"Screen-reader users can traverse by headings alone"** — verified. Clean
  outline: H1 masthead → H2 hook / contents / Part One → H3 ×3 → H2 Part Two →
  H3 ×4 → H2 ×5 essays. No skipped levels, no empty headings exposed to AT.
- **"Sidenotes read in order"** — verified in the AX tree. Every `role="note"` sits
  immediately after its `✲` link and at a paragraph boundary, so a screen reader
  reads sentence → marker → note → next paragraph. This is a genuinely good
  solution to a problem most published Tufte-style implementations get wrong.
- **"Running prose held to AAA"** — verified: iron-gall on parchment = **13.70:1**;
  the dark register measured 15.35:1. Real.
- **Reduced motion** — verified clean: all 24 reveal blocks at opacity 1, the mark's
  seat animation `none`, `scroll-behavior:auto`. No games.
- **Focus not obscured (2.4.11)** — verified: `scroll-padding-top:4.5rem` works;
  60 real Tab presses produced zero body elements trapped under the sticky head.

---

## 2. Constitution and brand conflicts

### 2.1 The five declared stretches

**Stretch 1 — one door instead of the constitution's three (S0).** Defensible *as a
website-vs-app distinction* (the constitution governs `cic-poc/frontend`, not
`cic-website/`, per its own README and D0 seam D). But the README does not name the
consequence, and the consequence is the worst one available given Mark's
2026-09-02 audience ruling. The three co-equal S0 doors are **Start with your
question** · **Build your own table** · **Guided onboarding**. The one this
direction deletes and does not replace is *Start with your question* — the only
door in the whole designed system built for a person who arrives with a question
rather than curiosity. See §6.

**Stretch 2 — both `mode=interview` and `mode=table` per chapter, inheriting seam G
unresolved.** Correctly flagged, correctly reversible ("the second link is cut
everywhere with no layout consequence"). No objection. This is how a stretch should
be written.

**Stretch 3 — Alegreya SC.** Same OFL superfamily, same foundry, not on the brand's
list. Trivially rulable. But note the practical consequence I hit: with Alegreya SC
absent, `.sc` falls back through `'Alegreya', Georgia, serif` with
`text-transform:lowercase` — which renders as *plain lowercase letterspaced text*,
not small caps. Every kicker, dateline, part label, plate label, contents numeral,
and byline on both pages depends on this face. If Mark declines the addition, or if
the font fails to load, the entire small-caps layer of the design silently
degrades to letterspaced lowercase. There is no `font-variant-caps` fallback. That
is a single-point-of-failure on the direction's signature typographic device.

**Stretch 4 — Lexicon Level-3 on the marketing site.** Correctly flagged as needing
a web-facing copy of the entries. Under-sized: see §3.4.

**Stretch 5 — inheriting and paying the Atlas palette debt.** Fine, and honest.

### 2.2 The stretches it did NOT flag — and these are the real ones

**A. The `✲` citation marker is given a sixth verb. This breaks the constitution's
one-grammar rule directly.**

`CiC_Full_UX_Design_V1_0.md` §4.5 puts citations under the *same* disclosure
grammar as lexicon terms: "same grammar, ✲ marker" — hover = Level-2 card, click =
Level-3 panel. §5.7 states it as law: *"Lexicon…, inline citations (the ✲ marker),
story/quote sourcing, map statuses, tour cartouches, closing resources: one grammar,
five applications, **no feature may introduce a sixth verb**."*

The direction implements lexicon terms with the real grammar (`.lex` button, hover
card, click panel — correct, and it is good work). It then implements the `✲`
marker as **a plain jump anchor** (`a.cite`, line 155, `href="#n1"`). Same glyph,
same Tyrian pigment, same visual promise — different verb. The README claims
"Nothing here contradicts the constitution's app rules." This does, in the one place
the constitution wrote the rule in bold.

**And the verb it introduces is worse than no verb.** Measured: with the citation
marker centered in the viewport, clicking it scrolled the page **386px**, to bring
a margin note that was *already visible* (measured at `top:72px`, `float:right`)
to the top of the screen — pushing the sentence you were reading off the top. A
control that looks like the app's transparency affordance, does not do what that
affordance does, and actively displaces your reading position. On narrow screens,
where the note is already inline directly beneath, it is a pure no-op.

**B. The Logo Usage Sheet's one hard copy rule is broken three ways on one page.**

The rule, stated identically in both brand documents and marked FINAL: *"The mark
never appears at first contact without this one plain sentence beside it"* —
*"The mark is a table; the opening is the way in — and it never closes"* — *"said
once beside the mark at first contact, never elaborated."*

In `homepage.html`:
1. **First contact is the running head at y=11.** The mark appears there with no
   sentence. (The live site does this too — the Decision-Log's D1-closure entry
   already flags it as a real bug worth fixing. This direction reproduces it and
   does not flag it.)
2. **The sentence appears as a decorative pull quote** at line 348, ~1.6 screens
   down, set in 1.6rem centered italic between two rules — with **no mark beside
   it**. A protected brand line repurposed as typographic ornament, detached from
   the thing it explains.
3. **It appears a second time** at line 634, beside the footer mark. So it is said
   twice, once away from the mark and once at the bottom, and never at first
   contact. "Said once beside the mark at first contact" is 0-for-3.

In `representative-chloe.html`: **the sentence does not appear at all.** The mark is
in the running head (line 205); the footer is a bare copyright row. A visitor
arriving on this page from search — which, for a page titled "The House-Churches —
Chapter I", is a very likely entry — meets the mark with no public sentence anywhere
on the page.

**C. At ≤480px the Chloe page shows the mark with no wordmark anywhere.**
`@media (max-width:480px){ .brand .wordmark{display:none} }` (chloe line 81). The
README defends this on the homepage — "the wordmark is the masthead directly
beneath" — which is true *there*. The Chloe page has no masthead. So on a phone the
key inner page carries a 32px ring and nothing else, against the Logo Usage Sheet's
R6: *"In most contexts the wordmark carries more identity than the mark — lead with
it wherever words fit."* Combined with (B), the direction's most likely deep-link
landing page, on the most likely device, presents the identity as a bare ring with
neither wordmark nor public sentence.

**D. The "Arriving" motion plays where nobody can see it.** The direction moved the
animated mark from the header (where the live site has it) to the footer, line 631,
class `play`. The CSS animation (lines 279–284, copied verbatim from
`assets/style.css`) is **time-triggered on load**, not scroll-triggered. The footer
sits at y=12,929 on desktop and y≈20,000 on a phone. So the build sequence — ring
drawn, guest arrives, sits — completes 3.7 seconds after load, roughly fifteen
screens below the viewport, and is never seen by anyone. By the time a reader
scrolls there, the dot has been running `cic-breath … infinite` for several minutes.
The README says the mark "plays the brand's own sequence once, in the colophon."
It plays it once, to nobody, in the footer. This is the direction's own change from
the live site's behaviour, and it makes the brand's signature motion dead weight.

**E. Dark mode: the seven census tints are never re-checked against the dark
ground, and three of them vanish.** The `--rep` custom property is set inline on
each chapter article (lines 390, 415, 440, 473, 498, 523, 548) and the dark block
(lines 41–47) does not redefine it. The plate ribbon (`background:var(--rep)`,
line 215) therefore keeps its light-mode value on `#17130F`:

| tradition | tint | on parchment | **on dark ground** |
|---|---|---|---|
| Church and Empire | `#7A2E2E` | 8.40 | **1.99** |
| Bethlehem Circle | `#9d174d` | 7.12 | **2.34** |
| Alexandria | `#2B5F8A` | 6.11 | **2.73** |
| Cappadocian | `#A0522D` | 5.07 | 3.29 |
| House-Churches | `#7c3aed` | 5.15 | 3.24 |
| Desert | `#0f766e` | 4.95 | 3.38 |
| Syriac | `#b45309` | 4.54 | 3.68 |

The README's contrast section states "all seven pass AA on parchment (4.54–8.40:1)"
— verified exactly right — and then lists five dark-register tokens, none of which
are these. The kicker is rescued in dark mode by an override at line 244 (all seven
collapse to gold-leaf, which also silently destroys the per-tradition color idea in
dark mode); the ribbon is not. In dark mode the Church-and-Empire ribbon is a 6px
bar at 1.99:1 — a black stripe on a black page.

This is precisely the class of bug the D1 closure flagged as *cross-validated across
three directions*: "four of seven world/census tints [fail] as text on grounds."
The direction found the light-mode half of it and shipped the dark-mode half.

**F. Two content-size floors the direction sets for itself and then breaks.**
README: "nothing under 13.6px carrying meaning." Measured: `.plate figcaption`
= **13.44px** on the homepage (line 219) — and plate captions carry real content,
including the only place a Representative's role title appears in each chapter
opening. `.chapter-nav small` = **13.1px** on the Chloe page (line 191). Both clear
the constitution's own 13px floor; neither clears the direction's stated 13.6px.

**G. `overflow-x:clip` on `body`** (homepage line 56, chloe line 43) is not a brand
conflict, but it is the mechanism that turns §4.1's layout bug from visible to
invisible. Noted here because it is a deliberate choice to hide overflow rather
than prevent it, in a direction whose second brand message is "it shows its work."

---

## 3. Fashionable or professional?

**The craft is real, and I am not going to pretend it isn't.** The sidenote
implementation (note inside the paragraph after the marker, floated into a reserved
margin at ≥1100px, falling to an indented in-flow note below) is genuinely better
engineering than most published Tufte-style work: it gets margin notes *and*
correct reading order for assistive tech, which almost nobody manages. The heading
outline is clean. The reduced-motion handling is correct and complete. The
lexicon's tap→popover→full-entry chain reproduces the app's phone grammar
faithfully, including the `(hover: none)` branch. Focus returns to the invoking
element on panel close. The contrast math in the README is, where it exists, honest
and reproducible — I checked every number and found no lie.

So the charge is not "fashionable veneer." It is narrower and, I think, worse.

### 3.1 The apparatus is a vacuum, and in the mockup it has already filled with internal bookkeeping

Of the five sidenotes on the homepage, **two are not scholarship — they are project
admin printed in the margin of a public page**:

> ✲ Live traditions and dates are read from the same census the Atlas uses; the
> count here is seven as of 2 September 2026. **Numbers are checked with Mark
> before anything prints.**

> ✲ The movement count is the live site's own figure and is checked with Mark
> before print. **The Atlas currently runs its own palette; this direction inherits
> that debt and pays it at build**, so the map reads as a fold-out of this same book.

A visitor is being told, in the marginal apparatus of the "scholarly edition," about
the project's internal numbers-approval workflow, a named person on the team, and an
unpaid CSS palette debt. Two of five. The same pattern is in the plate captions:
*"Plate VI. Chilo… **The seventh tradition, live since August 2026.**"* — a build
status line dressed as a museum label.

This is a structural property, not a drafting slip. A visible margin apparatus
creates seven-plus slots per page that must be filled with something, and the
cheapest thing to hand is whatever the team is currently thinking about. Nine
traditions × seven notes each is 60+ marginal slots that a draft-and-approve
discipline — the same one the D0 note records rewriting the support copy **six
times in one week** — must keep full of genuine scholarship, forever. The mockup
is the direction's own best-effort demonstration, and it already leaks.

### 3.2 The captions are a run of disclaimers

Across the seven plate captions: *"a voice for a whole people, never one person's
biography"* · *"The honorific is part of the name"* · *"A voice of the circle, and
no claim to be any woman its sources name"* · plus the build-status note. I counted
**23 uses of "never" across the two pages**, many in the exact denial shape the
brand's Never list warns against — *"denying a suspicion nobody raised — say what it
is, once, and stop"* and *"stacked 'not X, it's Y' contrast as a sentence shape,
even when true — it reads as generated, not crafted."* The Chloe provenance block
alone stacks two: *"Chloe is a voice, and never a person who lived… She is an AI
system, and never pretends otherwise."*

The brand rule does exempt clarifying category statements, and several of these
qualify. But the cumulative effect of a visitor reading seven plate captions is a
page that keeps apologising for itself. That is not scholarly confidence; it is
anxiety in a serif face.

### 3.3 The one number it prints overstates its own demand by 60%

`representative-chloe.html` line 227: **"About a twelve-minute read."** Measured
article body, excluding draft tags, lexicon card text, and the visually-hidden
hint: **1,518 words**. At 200 wpm that is 7.6 minutes; at 240 wpm, 6.3. Twelve
minutes implies ~127 wpm.

Of all the numbers to inflate, this is the worst one for this direction. Its single
largest vulnerability is looking like homework. It has voluntarily printed, above
the fold, a label that makes the reading nearly twice as expensive as it is. And
per the brand's Always list — *"Numbers: check with Mark before print"* — it printed
one anyway, in a page that elsewhere puts "checked with Mark before print" in a
sidenote.

### 3.4 The content liability is larger than the README's own accounting

The README names the risk ("Content volume, forever") but does not size it. Sized,
from the Chloe page as the unit: **1,518 words of Representative-voice prose ·
7 sidenotes (297 words) · 6 lexicon entries with source lines · 5 curated question
openers**, all of which the README concedes "would go through the same
draft-and-approve gate as any participant-facing text."

× 9 traditions (7 live, 2 selected-not-yet-built, confirmed in the census) =
**~14,000 words of gated Representative-voice prose, ~55 sidenotes, ~54 lexicon
entries** before the Reformation wave, which is on the roadmap. And stretch 4 means
the lexicon entries must exist in a *second*, web-facing copy that stays in sync
with the in-app records — a duplication the site has already been bitten by (the
homepage carousel's own code comment cites "two independently-maintained copies of
this data" as a prior bug).

That is not a sacrifice. That is a permanent, unfunded editorial department, in a
project whose Decision-Log records that independent academic review "needs both
funding and volunteers" and is not yet funded.

### 3.5 The metaphor has a built-in expiry the direction does not design for

The site *is* "Issue: The First Centuries." Periodicals have issue two. The
roadmap guarantees it: two more ancient traditions, then seven Reformation
traditions. What happens then? Either every new tradition is appended to Issue One
forever — the phone homepage is already **24.5 screens** at seven chapters, so
sixteen chapters is ~50 screens — or the site fragments into issues and the
homepage becomes a magazine archive index, which is a completely different
information architecture that this direction has not designed and whose whole point
(sequence, one continuous read) it destroys. The README's "content volume, forever"
sacrifice covers the writing cost. It does not cover the fact that the organising
metaphor breaks on contact with the roadmap.

---

## 4. Where a real visitor gets lost

### 4.1 THE HARD BUG: on an iPad in portrait, the one door is off-screen and unreachable

This is the finding I would lead with if I could only keep one.

The running head lays out `brand + 5 nav links + separator + door` in a
`display:flex` row with `white-space:nowrap` on every link (lines 99–104). The only
mitigation is `@media (max-width:760px)`, which hides the four `.optional` links.
**Above 760px there is no wrap fallback at all.** Measured:

| viewport | required document width | door position | reachable? |
|---|---|---|---|
| **768×1024** (iPad portrait) | **1001px** | x = 758 → 1001 | **NO** |
| **820×1180** (iPad Air portrait) | **1001px** | x = 758 → 1001 | **NO** |
| 1024×768 | 1024px | 758 → 1001 | yes |

And because `body{overflow-x:clip}` (line 56) — `clip`, not `hidden`, so no scroll
port is created at all — **there is no way to pan to it.** The screenshot at 768px
shows the header ending on the letter "C" at the right edge, mid-word.

So: on the single most likely device for a long-form-reading website, in the
orientation people read in, the direction's defining element — *"one door, always in
the same place… the running head keeps the door at top right at every scroll
position"* — is silently amputated. No scrollbar, no overflow indicator, no error.
Just gone. On that device the only way into the product is to scroll 22 screens to
the closing door, or to find one of the invisible gray per-chapter links from §1.3.

**Font caveat, stated precisely:** the exact upper bound of the broken band is
font-dependent (measured 761–~1000px in fallback faces; Alegreya Sans is somewhat
narrower, so with real fonts I estimate the band closes nearer ~930px). The
mechanism is not font-dependent, and neither is the lower bound: at 761px, one pixel
above the media query, six nowrap links plus a 243px door plus the wordmark must
fit in 761px, and no plausible font makes that true. There is a guaranteed
unmitigated band immediately above 760px. This is also, structurally, the *exact*
bug the live `assets/style.css` documents fixing at line 356 — *"Six nav links plus
the wordmark don't fit a phone width no matter how far gap/font shrink - previously
this silently pushed the whole page wider than the viewport"* — reintroduced one
breakpoint higher.

Same root cause, secondary symptom: at 200% text-only zoom on a 1280px viewport the
document blows out to 1971px. (Page-zoom reflow to 320 CSS px is clean — SC 1.4.10
passes.)

### 4.2 First-time visitor, phone

Measured heights at 390×844 — **20,692px, 24.5 screens**:

| landmark | screen |
|---|---|
| masthead | 0.1 |
| the hook | 0.6 |
| contents | **3.4** |
| Part One | 4.9 |
| Chapter I (first image on the page) | **5.5** |
| Chapter IV | 11.1 |
| Chapter VII | 16.1 |
| the closing door | **22.8** |
| colophon / give | 23.4 |

**The first human face appears at screen 5.5.** The first five screens are
typography: an issue line, a wordmark, a strap, a rule, a hook, a standfirst, and
five essay paragraphs. On the homepage of a project whose entire proposition is
*people you can sit down with*, a phone visitor scrolls through five screens of
prose before meeting one.

**On mobile the header loses four of six links.** `.head-nav a.optional` is hidden
at ≤760px, so About, What's Next, **Atlas** and Get Involved all disappear.
Verified at 390px: `navVisible = ['Contents', 'Come and join us at the Table →']`.
The Atlas — the site's second primary surface, nav-anchored on the live site — is
reachable on a phone only via the contents list at screen 3.4, or via the Atlas
essay at screen 20.8. The footer has no Atlas link either.

### 4.3 Returning visitor who wants one conversation, fast

Traced in §1.2: three clicks, two animated scrolls, one 1.5–2s fade, ending on an
18px-tall link the same color as the paragraph around it. Compare the live site's
current path: scroll the carousel, tap a card, tap "Launch an Interview with X" —
two taps, and the CTA is a filled madder button.

The D1 closure named this direction's most attackable point as *"a sequential,
chronological read may not serve a visitor who wants one specific tradition fast."*
I can confirm it, and sharpen it: the problem is not the chronology, which the
contents page genuinely solves — the contents at 390px is the best thing on the
page, a clean I–VII index with names and dates. The problem is that the contents
page **routes you to reading, not to talking.** Every one of its twelve entries is
an in-page anchor to prose. There is not a single "begin a conversation" link in the
index. The one navigational surface built for the hurried visitor deliberately does
not contain the thing the hurried visitor came for.

### 4.4 Screen reader and keyboard

Mostly good, with three real defects.

**Good, verified:** clean heading outline; named landmarks (`nav` "Site", `nav`
"Chapters", `article` "Chloe's introduction"); sidenotes exposed as `role="note"`
in correct reading order; lexicon buttons announce correctly as *"assembly, button,
collapsed, Lexicon term. Activate for the full entry"* (the `aria-hidden` on the
card correctly keeps the tooltip text out of the accessible name — I checked this
in the CDP AX tree specifically because I expected it to be broken, and it isn't);
`aria-hidden` panel invisible to AT when closed and correctly absent from the tab
order; focus returns to the invoking button on close; Escape works.

**Defect 1 — the keyboard/AT user cannot reach Level 2.** The Level-2 card is
`aria-hidden="true"`. A sighted mouse user gets hover = short gloss. A sighted
keyboard user gets the card visually on `:focus-visible`. A screen-reader user gets
**nothing at Level 2** — their only path to a definition is activating the button
and taking the full Level-3 panel. The constitution's grammar promises two tiers to
everyone; here the short tier is sighted-only.

**Defect 2 — `aria-expanded` on a button that controls nothing exposed.** Every
`.lex` carries `aria-expanded="false"` with no `aria-controls` and an `aria-hidden`
expandable region. On a touch device with a screen reader (`hover: none` branch,
line 381), the first activation sets `aria-expanded="true"` and reveals a region the
AT cannot see — the user is told "expanded" and given nothing. Second activation
opens the panel. The state is a lie for exactly the users who depend on it.

**Defect 3 — `scroll-behavior:smooth` applies to focus scrolling.** Measured: Tab
from the header's last item to the first `✲` at y=1432 triggers a ~1,400px animated
scroll; Tab from the last contents link (y=2760) to "Read Chloe's introduction"
(y=3909) another ~1,100px. A keyboard user traversing 57 focusables rides
continuous animation, and repeatedly lands focus on elements that are still fading
in from `opacity:0`. Not a conformance failure, genuinely unpleasant.

**One more orientation loss:** on the Chloe page at ≤760px, both the running title
(*"Chapter I · The House-Churches"*) and the Contents link are `display:none`
(line 77). So on a phone, the key inner page has no "where am I" indicator and no
visible way back to the index except a 32px unlabeled ring. Add §2.2C: no wordmark
either. The book metaphor's entire orientation apparatus — running head, running
title, contents — evaporates on the device most people will use it on.

### 4.5 Anyone who prints — a feature the README specifically claims

README: *"a print stylesheet — a quarterly should print."* The print block is at
lines 291–296. It hides the running head and draft tags, sets black-on-white, and
avoids breaking inside chapters. **It does not reset `.reveal`.**

Measured directly: load the homepage, do not scroll, wait 1.5s, then emulate print
media. Computed opacity of the reveal blocks:

```
hook            1
standfirst      1
dropcap         0.43
contents        0
part-1          0
ch-1 … ch-7     0    (all seven)
built           0
claim           0
atlas / next    0
door / colophon 0
```

I generated the PDF: **24 pages**, of which the masthead, hook and standfirst carry
ink and essentially everything else is blank parchment. A visitor who hits Ctrl+P
on arrival — which is what a reader does with a long-form piece they intend to read
later, which is the exact behaviour this direction is designed to invite — prints
24 blank pages. The one-line fix (`@media print{ .reveal{opacity:1!important;
transform:none!important} }`) is missing.

Secondary: the print block sets `a{color:#000; text-decoration:none}` and prints no
URLs, so nothing in the printout indicates a link existed or where it went. For a
"quarterly that should print," the apparatus does not survive the paper.

### 4.6 Six of seven "Read the full introduction" links are dead

Chapters II–VII link to `#ch-2` … `#ch-7` — themselves. Only Chapter II carries
`aria-describedby="mock-note"`; the explanatory note itself (line 573) sits *after*
Chapter VII, so five of the six give no warning at all. This is a mockup artifact
and I am not scoring it as a defect. I record it because of what it means: the
direction's key inner journey exists exactly once, and the other six are the
content debt of §3.4 rendered as broken links.

---

## 5. Religious feel — Mark's "I don't want the feel of religion"

This is where I expected the direction to be safe and found it is not.

The obvious devotional tells are all absent, and I want to be explicit about that
before I attack: **no cross, dove, flame, stained glass, or steeple; no scripture
verse as decoration; no worship vocabulary in the chrome; no second-person
devotional address ("come, weary one"); no liturgical structure or invocation; no
"we believe"; nothing that reads as evangelical or contemporary-church design.**
The direction also does the most secular thing available — the opening essay raises
the AI question *fourth paragraph, unprompted, before any Representative speaks*.
That is journalism, not devotion.

But Mark's ruling is explicitly about *formal* feel, not content: *"i don't want the
feel of religion."* And the register this direction chooses is not neutral
literary-modern. It is a **manuscript codex**, and the manuscript codex is the most
identifiably ecclesiastical page format in Western history. Concretely, the choices
that create it — all of them the direction's own, not inherited from the locked
palette:

1. **Roman-numeral chapters** (I–VII), rendered as huge watermark glyphs
   (lines 221–229, `clamp(5rem,11vw,8.5rem)`).
2. **Part-title pages** — full screens carrying only "Part One / The Early Church
   Era / 70–312 ce" (lines 196–201). This is the front-matter grammar of a Bible or
   a missal far more than of a magazine.
3. **Drop caps on every essay** (`::first-letter` at 4.6em, line 164) — the
   secular-modern version of the illuminated initial, and it reads as the initial.
4. **"Plate I. … Plate VII."** — plate numbering plus full-column painted portraits
   of veiled and robed figures, softly lit, frontal, direct gaze, holding an object
   (a cup, bread, a book). At plate size on a page of ruled marginal glosses, Chloe
   with the cup in both hands reads uncomfortably close to an icon. The portraits
   are locked and not this direction's decision; **presenting them at full-column
   plate scale, numbered, with a ribbon, is entirely this direction's decision**,
   and it is the single largest change in how those images read.
5. **A central authoritative text column with marginal apparatus keyed by a
   rubricated glyph.** The README calls this "a scholarly edition." Its actual
   historical referent is the *glossa ordinaria* — the glossed Bible. A visitor does
   not need to know the term to feel it; the form is legible.
6. **Gold-leaf, vellum, iron-gall, parchment, a colophon** as literal named
   materials. The palette is locked, but naming the tokens is not the same as
   building "plates," a "colophon," and part-title pages out of them.
7. **The closing spread.** After a 12-minute read, one screen containing a single
   sentence at 3.6rem, centered, alone, with a thin madder rule under it, above a
   breathing madder dot. The words are protected brand copy and are fine. **The
   form is an altar call** — a long address, then a single large invitation set
   apart on its own page. That shape is not neutral.

None of this is "churchy" in the sense Mark is most likely fearing (contemporary
evangelical, praise-band, welcome-team). It is churchy in the older sense:
**cathedral library, altar missal, Book of Hours.** If Mark's test is *does this
feel like religion on sight, before I read a word* — the honest answer for this
direction is that it feels like a religious *artefact*, which for a project about
the church and Jesus' faithfulness may be exactly the trap: it looks like the thing
it is about, rather than like a place where you can ask about the thing.

There is a real defense available here and the author should make it: some of this
register is the brand's, not the direction's, and the direction is arguably just
executing the constitution's own stated register ("a beautifully set trade book on
parchment") more literally than anyone else will. My counter is that the
constitution says **trade book** — and specifies "nothing antiquarian." Plates,
part-titles, Roman numerals, drop caps and a colophon are not a trade book. They
are an antiquarian one.

---

## 6. Does it serve the person with hard questions, or the academic?

**It serves the academic. Not by content — by structure, by what it asks of the
visitor first, and by what it never asks them at all.** This is my strongest
objection after §4.1, and unlike §4.1 it cannot be patched.

### 6.1 The one place the heart audience is named is at screen 22.8 of 24.5

I grepped both pages. The phrase *"anyone re-examining their faith"* appears exactly
once, in the door section's quiet paragraph (line 615) — **document-Y 19,266 on a
phone, screen 22.8 of 24.5.** The line about distress support — *"If a conversation
touches real distress, a separate, clearly-labeled voice steps in to direct you
toward real human support"* — appears once, in essay two (line 595), screen ~19.

A person in genuine crisis will not reach either. The direction's own philosophy
requires that they read seven chapters first.

### 6.2 Everything is organised by chronology; nothing is organised by a question

The README states it plainly and proudly: *"you meet Chloe first because 70 CE comes
first."* That is a reader's ordering. It assumes the visitor's relationship to the
material is *interest*. A person re-assessing their faith does not arrive with a
period; they arrive with a question — *did the church always treat women like this?
who decided any of this? did anyone back then also not believe and stay anyway?* —
and there is no surface anywhere on either page that takes a question as input.

This is where deleted stretch 1 stops being a governance footnote and becomes the
central charge. The constitution's S0 offers three co-equal doors, and one of them
is **"Start with your question."** The constitution designed the routing behind it
(R.0–R.2c: the question held on screen, editable, never discarded; an honest
considering line; a proposal card that names which traditions can carry it and
*why*, with sourcing reasons). That entire apparatus exists, is approved, and is
designed for precisely the person Mark named as his heart. This direction removes
all three doors and substitutes one link to `?mode=table` — the app's **seating
field**. So the single door on every page of the site delivers a person in doubt to
a configuration screen where they must choose whom to seat before they can say
anything.

And per D0 seam D, the multi-voice Table experience *does not yet exist on the new
architecture*. So the direction's one door leads to the least-finished surface in
the product, while the fast, working, instant path — `mode=interview` — is one of
the 18px gray links from §1.3.

### 6.3 The five "questions people bring" are mostly a history quiz

The Chloe page's `.questions` list (lines 279–285) is the closest thing in either
file to meeting a real person. Reading them as a person in crisis would:

1. *"How did you even know what other churches, far away, were doing or believing?"*
   — historical curiosity.
2. *"Who was actually in charge of your church — one leader, or something more like
   a board?"* — polity history.
3. *"Was it actually dangerous to be a Christian back then, day to day, or is that
   exaggerated?"* — historical myth-busting.
4. *"The clearest outside account of your worship came from torturing two enslaved
   women. Doesn't that taint everything we think we know from it?"* — **genuinely
   hard, and genuinely good.** But it is a *source-criticism* question. It is a
   scholar's question with a moral edge, not a doubter's question.
5. *"Only one chance at forgiveness after baptism? What happens to someone who fails
   a second time?"* — **the only one that touches a real person's real fear**, and
   it is fifth.

Four of five are questions you ask because the past is interesting. One is a
question you ask because you are afraid. The direction is choosing, in the one
place where it lets a visitor see themselves in a list, to show them four scholars
and one person.

### 6.4 The register itself keeps score against the doubter

- **"About a twelve-minute read"** in the byline, over-stated by 60% (§3.3). To
  someone with the energy of a person in crisis, that is a fee posted at the door.
- **A byline at all.** "Introduced by Chloe · Household Leader" is the grammar of a
  contributor credit. It positions the reader as an *audience*, not a guest.
- **The whole site as "Issue: The First Centuries."** Periodicals are for
  subscribers — people already inside the conversation. A person who is losing
  their faith is not looking for the new issue.
- **A vocabulary that assumes a reader's confidence:** masthead, contents, plate,
  colophon, part, recto/verso, apparatus, epigraph, standfirst. None of this is
  visible in copy, but the *shape* it produces is a page that expects to be
  navigated by someone who already knows how books work and enjoys that they do.

### 6.5 What genuinely serves the heart audience — and it is real

I will not pretend this direction has nothing. Two things in it are the best
answers to Mark's ruling I could imagine anyone producing:

**"Where we are quiet"** (Chloe, lines 271–275) is outstanding. *"No enslaved member
of any of our households left a single word in their own voice… Perhaps two in every
hundred of us could have written the texts we did, and everything you know of us
passed through those few or through an enemy… I hold that silence rather than fill
it."* A person who left the church because it lied to them will read that and
understand that this thing does not lie. That is the whole project's credibility in
four hundred words, and it belongs in whatever direction wins.

**The provenance block** (line 240) — the AI disclosure raised first, in iron-gall
at 13.70:1, before Chloe speaks a word — is the correct posture and the correct
placement.

But both are *inside* the twelve-minute read, on the one page of nine that exists.
Neither is on the homepage's first five screens. A direction that put "Where we are
quiet" at the top and the chronology underneath would be a different, and much
better, answer to Mark's ruling. This one has it at the bottom of chapter one.

---

## 7. What survives, honestly

So that the author's defense has something to build on, and so the D3 synthesis can
harvest it whichever direction wins:

1. **The sidenote implementation.** Margin apparatus with correct AT reading order.
   Take it whole.
2. **"Where we are quiet"** as a content pattern, and the idea that a tradition's
   absent stories are part of its testimony. This is the single strongest piece of
   writing produced in D1 as far as I can see, and it is the direction's own.
3. **The provenance block** — AI disclosure first, in the Representative's own
   introduction, at full contrast.
4. **The contents page at phone width.** A clean numbered index with names and
   dates. It just needs conversation links in it.
5. **Verified-against-data discipline.** Every fact in both files checks out against
   `world-census.json`, including the two-not-three development count that
   contradicts the live site. The draft tags are honest and specific.
6. **AAA prose contrast, reduced-motion parity, focus-not-obscured, clean heading
   outline, correct panel-not-modal Level 3.** All verified, all real.

---

## 8. Verdict — adversarial, not final

**It survives, barely, and only as a source of parts — not as the spine of V2.**

The bugs, taken alone, are all fixable and several are one-liners: the print reset,
the header wrap above 760px, the `.begin` link color, the `--rep` dark override, the
`✲` grammar, the twelve-minute label, the footer motion trigger, the public sentence
on the Chloe page. If that were the whole indictment I would say "survives, fix
these nine things," and the direction's craft would carry it. A reviewer who only
ran a linter would say exactly that.

It does not survive on the two things that cannot be patched, both of which land
directly on Mark's own 2026-09-02 words:

**One — "my heart is those seeking answers to hard questions of faith, not
accademics."** This direction is organised by chronology, priced in reading minutes,
addressed to a reader, and it deletes the one designed door built for a person with
a question in order to substitute a seating field. Its index routes to prose, never
to a conversation. Its per-tradition conversation links are, measurably, the same
color as the paragraph around them. The one sentence naming the re-assessing
audience is at screen 22.8 of 24.5. Every one of those is a structural consequence
of "the site is a book, and the visitor is a reader" — which is a beautiful premise
that quietly assumes the visitor arrived out of interest rather than need. You
cannot fix that with CSS; fixing it means giving up sequence-over-navigation, and
sequence-over-navigation *is* the direction.

**Two — "non religious… i don't want the feel of religion."** Plates, part-title
pages, Roman numerals, drop caps, a colophon, a rubricated marginal gloss around a
central authoritative column, and full-column frontal portraits of robed figures
with a cup and with bread. Individually defensible; together, an illuminated codex.
It is not the churchiness Mark is probably picturing, and it is arguably the harder
one to escape, because it is the register in which the material *actually lives* and
therefore the one this project will drift toward unless someone rules against it.
The constitution says "trade book… nothing antiquarian." This is antiquarian.

**What would have to change for me to withdraw the verdict**, in the author's own
terms — and I think this is a real, buildable defense, not a rhetorical concession:

- Put "Where we are quiet" and the AI disclosure in the first two screens, and the
  chronology below them. Lead with the honesty, not with 70 CE.
- Add a question-shaped entry point. Either restore the constitution's
  *Start with your question* door, or put one input on the homepage that routes.
  Without this, the direction cannot claim the heart audience at all.
- Make the conversation links the most visible links on each chapter, not the least.
  Madder, not ink-faded; and put them in the contents.
- Drop the periodical framing — masthead, issue, plates, colophon, part-titles,
  Roman numerals, the twelve-minute byline. Keep the reading column, the sidenotes,
  the measure, the drop caps if you must. That is a trade book. The rest is a codex.
- Fix §4.1 before anything else, because it is a live amputation on iPad and it
  would ship.

If those five happen, what is left is a strong, warm, honestly-sourced long-form
site — and it is no longer this direction, because four of the five delete the
philosophy statement's own three consequences. That is my actual finding: **the
craft is excellent and should be harvested; the thesis is wrong for the audience
Mark named eight hours ago.**

I hold this loosely on exactly one point, and the author should press me on it: the
religious-feel charge in §5 is the most interpretive thing in this review, and I may
be over-reading a manuscript register that Mark, who chose the manuscript palette
himself, may hear as *serious* rather than *religious*. Everything else here is
measured.

*— Opus adversarial review, D2. One defense is owed before any decision.*
