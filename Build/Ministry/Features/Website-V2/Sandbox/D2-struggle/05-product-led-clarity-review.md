# D2 adversarial review — Direction 05, Product-Led Feature Clarity

**Sandbox artifact. Adversarial, by assignment. Not a ruling. 2026-09-02.**

Reviewer: Opus, D2 struggle phase. I reviewed `05-product-led-clarity/` only —
`README.md`, `homepage.html`, `meet-chloe.html`, each read in full. I did not open
the other four D1 folders and no other D2 review existed when I started (the
`D2-struggle/` folder did not exist; I created it to write this file). My job here
is to try to kill this direction. Where it survives an attack I say so, because an
attack that misses makes the ones that land easier to dismiss.

**Method note — the browser work is real.** Chromium (`/opt/pw-browsers/chromium-1194`)
with Playwright drove both files at 320 / 360 / 375 / 390 / 414 / 480 / 600 / 768 /
1280px, in `prefers-color-scheme: light` and `dark`. Contrast numbers below are
computed from *rendered* colors — each text node's own computed color composited
against its real painted ancestor background — not from reading the token table.
Tab order was walked key-by-key. Everything in Sections 2 and 4 marked "measured" is
measured, not inferred.

---

## Summary of what actually kills, before the argument

Six findings I consider load-bearing. Four are provable defects, two are judgment
calls I will argue for:

1. **The primary button is unreadable in dark mode — measured 2.69:1.** Every
   "Begin a conversation," "Come and join us at the Table," "Keeping the Door Open,"
   and the mock "Send" chip. Root cause is a one-line omission in the token block.
2. **The AI disclosure is absent from `meet-chloe.html` entirely** — the page this
   direction *designates* as the informed-decision page. Zero occurrences of "AI."
   This is the brand's single "Always … first" rule, dropped on the page with the
   highest intent.
3. **The site navigation is truncated on every phone width tested (320–414px)** with
   no scrollbar, no affordance, and no keyboard focus — on the direction whose
   philosophy sentence is "Mobile first."
4. **The "measured" step map measures the wrong thing.** One click, yes — after
   2,487px of scrolling to reach the first Begin button on a phone, and 5,768px to
   reach the AI disclosure.
5. **The homepage's IA is an academic's index** — seven humans sorted by century,
   with dates, regions, era bands, and a ten-era ruled table — at exactly the moment
   Mark has said his heart is the person with a hard question, not the academic.
6. **The hero's showcase paragraph is a communion liturgy.** The one piece of content
   that defines first impression is a description of a Sunday service.

Findings 1–4 are fixable in a day. Findings 5–6 are the direction's spine.

---

## 1. Charter-goal failures

The charter names four goals. This direction scores itself honestly on the first
three and, I think, deceives itself on the fourth.

### 1.1 It optimizes "easy access to features" past the point where it serves anything

The README's proudest sentence is the step map: *"Homepage → a real conversation in
one click … Map: one click. Giving: one scroll, one click."* That is true and it is
also the wrong measurement, and the direction should have caught this because its own
stated priority is mobile.

Measured, `homepage.html` at 390 × 844 (iPhone 14/15):

| Landmark | Distance from top | Screens of scroll |
|---|---|---|
| "Meet the Representatives" heading | 1,950px | 2.3 |
| **First "Begin a conversation" button** | **2,487px** | **2.9** |
| The Table block | 4,846px | 5.7 |
| **"Three things to know" — the AI disclosure** | **5,768px** | **6.8** |
| The map | 6,581px | 7.8 |
| Get Involved | 8,483px | 10.0 |
| Document height | 9,613px | 11.4 |

"One click" is a click count with the scroll cost silently omitted from the
denominator. A visitor on a phone does three full screens of work before the first
actionable thing appears, and the direction's *named sacrifice* ("a longer page …
seven rows in full instead of a carousel") frames that as a deliberate, minor cost
of doing the right thing. It is not minor: it is the majority of the experience. The
direction traded a carousel (which it correctly says hides content and fails
keyboards) for a 9,613px scroll, and then reported the trade as a win in a table
of click counts. That is the one methodological failure I would want the author to
answer for above all others, because it is the direction's own core competence —
measurement — used to flatter itself.

### 1.2 "Drawing visitors into a fascinating, life-changing journey" is the goal it
does not attempt

The README's answer to the fourth charter goal is: *"'Cutting-edge' means the
confidence of the clearest product sites — restraint, hierarchy, the product shown
plainly … The draw is the real exchange in the hero."*

Read that again. The direction's entire answer to *"draws visitors into the church's
story and Jesus' faithfulness"* is a **hero excerpt**. One paragraph. Everything
else on the page is apparatus: a picker, a numbered trust block, a ruled era table,
a what's-next list, a give block.

Count what the homepage actually asks a visitor to *feel* versus *do*. Measured: 32
focusable elements, of which **nine are filled madder primary buttons** — seven of
them identical, stacked in one vertical list. Against that: one 180-word excerpt and
six protected lines. The ratio is roughly nine invitations to act per one thing to be
moved by.

This matters more than a taste objection because the constitution states the test in
one sentence (§1, and repeated as "the one test every screen answers to"):

> *"a screen where features wait to be chosen serves the encounter; a screen where
> they compete for attention has made technology the point."*

Seven identical madder buttons in a vertical list is not features waiting to be
chosen. It is seven features competing. The direction's own philosophy — "one job
per section, one primary action per screen" — is stated and then broken on the
biggest section of the biggest page: `#meet` carries fifteen actions (7 Begin, 7
About, 1 Choose-your-seats), eight of them primary-weight.

I accept the honest caveat that the UX constitution binds the app and not this site
(D0 seam D). But the direction opts into that test itself — it claims the register
of "a well-set trade book on parchment," which is a direct quote from §1 of the same
paragraph the test lives in. You do not get to cite half a sentence.

### 1.3 The substance is skippable by design, and gets skipped

The most damning structural fact: a visitor can reach the app in one click from the
hero, from any of seven rows, or from the Table block — **without ever passing the
section that tells them this is an AI system.** That section sits at 5,768px, after
every one of those doors. The direction's README says it tells the story in the
order "the hook line; a real exchange; who is at the table; then the three things
the brand says to raise **first**." Its own sentence contains the contradiction. The
brand says raise it first; the direction puts it third, behind nine buttons.

Clarity-first design is very good at making substance optional. That is not a
hypothetical here — it is the measured layout.

### 1.4 What actually holds

Accessibility as a *stance* is the best of the four goals here and I want to be fair
about it: a real skip link, a real landmark set, no-JavaScript keyboard completeness,
44px targets on every button, `prefers-reduced-motion` honored on both the mark and
`scroll-behavior`, no carousel, no sheet, no focus trap, `rel="noopener"` and a
visually-hidden "(opens in a new tab)" on every app hand-off. Compared to the live
homepage — which puts the seven Representatives inside a horizontally scrolling
carousel that opens a `role="dialog"` sheet — this is a genuine, substantial
improvement for keyboard and screen-reader visitors. Section 4 will show where the
execution fails the stance, but the stance is right and it is this direction's
strongest real contribution to D3 regardless of whether the direction survives.

Storytelling clarity in the *copy* also holds. The protected lines are used verbatim
and in the right slots; the census data is accurate (I verified all seven
Representatives, roles, dates, colors, and the 292-movement / ten-era count against
`world-census.json` — "nearly three hundred" is correct); the "in development" list
correctly drops Cappadocian, which the live `whats-next.html` still gets wrong.

---

## 2. Constitution / brand conflicts

### 2.1 The tech-forward claim: it wins most of the argument, then loses on the one
element it built by hand

I checked the refusal table against the rendered markup rather than trusting it. Most
of it is true and verifiable: no `box-shadow` on any content surface (the only two
are `0 0 0 1px` hairline ring edges, which is a border, not a shadow), no gradients,
no glass, no pill radii (2–3px throughout), no header CTA, no scroll-reveal, no
hover-lift, no icon tiles, no logo row, no counters, no badges, Alegreya on every
headline. The numbered convictions device is genuinely the live site's own, not a
feature grid. That is a real refusal, honestly executed, and the "clarity is
structural, not stylistic" thesis is *mostly* earned.

**But it built a chat composer.** In the hero, inside the "leaf," at
`homepage.html:271`:

```html
<div class="composer" aria-hidden="true"><span class="box">Ask Chloe anything…</span><span class="send">Send</span></div>
```

A rounded input field with grey placeholder text reading "Ask Chloe anything…", and
a filled accent-colored **Send** button beside it. Rendered and screenshotted; it
reads exactly as it sounds.

This is the single most recognizable piece of AI-product furniture of 2024–2026. It
is the ChatGPT/Claude/Gemini/Copilot composer. The direction refused device frames as
too tech-forward and then drew the *interior* of the device — the one part everyone
recognizes. "The preview is a ruled leaf of the book with a running head" is true of
the transcript above it; it is not true of the composer, which is not a leaf of a
book and has no counterpart in any manuscript. A book does not have a Send button.

Two consequences beyond the aesthetic:

- **It is a decoy control.** It is `aria-hidden`, so screen-reader users are spared,
  but a sighted visitor sees a text field and will click into it and type. Nothing
  happens. The direction's own refusal list bans "device-frame screenshots" on the
  grounds that fake chrome is dishonest; a fake, non-functional input with a fake
  Send button is *more* dishonest than a laptop bezel, because a bezel doesn't invite
  a click.
- **It undercuts the one differentiator the direction claims.** The README's answer
  to "cutting-edge" is "a register nobody else in this space uses." The composer is
  the register everybody in this space uses. Delete those two spans and the leaf is
  genuinely distinctive. Keep them and the hero's first read is "an AI chat product,
  in sepia."

Constitution §2.5a's anti-ghost rule is about figures, so I will not stretch it here.
But the voice pair **"Technology but not seen — experience first, governance second,
mechanism third"** is directly inverted on the homepage. Rendered order is:
experience (the excerpt) → **mechanism** (three marginalia notes explaining what a
dotted underline does, what ✲ 5 means, how glosses behave — all in the hero, above
the fold on desktop) → features → governance at 5,768px. Mechanism is promoted to
second and governance demoted to fourth. The direction explains the UI before it
explains the ethics.

### 2.2 The vocabulary rule breaks, and it breaks by quoting the app

D0 §1 and the Brand-Messaging-Rework lock a corpus-wide **"world" → "Christian
tradition"** rename for visitor-facing copy. `homepage.html:414`, in the Table block,
visible to every visitor:

> *"It asks a little more of you than an interview, and gives back more than one
> **world** at a time."*

The direction's honesty ledger lists this under "Real, not written by me: … the Table
description (Launch.tsx)." I checked: it is verbatim from `Launch.tsx:97–101`. That
is exactly the problem. `Launch.tsx` is *in-app* copy written before/outside the
rename; lifting it verbatim onto a marketing page imports a banned word. "Verbatim
from a real source" is not the same as "cleared for this surface," and the direction's
whole honesty apparatus is built on treating those two as identical. This is the one
place where the apparatus produced a wrong answer, which makes it worth naming
precisely: the ledger has a category error in it, not just a typo.

### 2.3 The "pairings" are filed as real; the file itself says draft

`homepage.html:415–424` prints two pairings — "The school and the desert · Theon ·
Papnoute · **the proven pairing**" and "Two ways of knowing" — with their `why` text
verbatim. The ledger files these under "Real, not written by me: … the pairings
(pairings.ts)."

`cic-poc/frontend/src/data/pairings.ts:1–11`, the file's own header:

> *"carried verbatim in substance from the C6 pairing record … **DRAFT status: that
> document awaits Mark's sign-off**"*

So a marketing homepage is printing unapproved draft copy — including a quality claim
("the proven pairing") — filed on the "real" side of an honesty ledger whose entire
purpose is to keep exactly that from happening. This is a smaller finding than 2.2 but
it is the same failure mode twice, which suggests the ledger's rule is "did I type
this?" rather than "is this cleared?"

### 2.4 Two marks in the first viewport, one animating and one frozen

Measured at 390px: `.mark.play` at y=95 (34px) in the header, `.mark.still` at y=183
(48px) in the hero — 88px apart, both in the first screen. On load the header mark
draws its ring and seats its dot while an identical, larger, static copy sits directly
below it. The Logo Usage Sheet does not have a rule literally forbidding this, so I
will not claim a violation — but the adjacency principle it *does* state (two
table-metaphors in one composition "read as two brands") is plainly about not
duplicating the table figure, and this duplicates the actual mark. It reads as a
rendering bug, not a design.

The public sentence placement is also arguable rather than clearly wrong: the brand
says it is "said once beside the mark at **first contact**," and here first contact is
the header mark, with the sentence beside the *second* mark below. One mark, in the
hero, with the sentence beside it, would satisfy the rule cleanly and remove the
duplicate. Worth a ruling either way, not a kill.

### 2.5 What I checked and could not make into a finding

The breathing dot. `homepage.html:66` puts `breath 5.5s ease-in-out 3750ms infinite`
on the madder seat, and the brand never-list says the mark is "never … pulsed at alert
speed, or moved to attract a click." I went looking for a violation and there isn't
one: `Brand-Assets/CiC_Logo_Arriving_Motion_Reference.html:30` is character-identical
(`cic-breath 5.5s ease-in-out 3750ms infinite`), the live `assets/style.css:95` ships
the same, and the reference's own `aria-label` says "the dot sits down and **breathes**."
Correct implementation of the brand's own motion. Geometry checks out too
(viewBox 100, r31, 100° opening facing right, dot r6.5 at 88.5,50; the uniform
stroke-width-11 geometric variant is the correct one below 48px). The italic "in" in
the wordmark is a real, correct fix to something the live site currently gets wrong.

### 2.6 The multi-voice Table claim — I verified it, and it is TRUE

The brief asked me to test this hard because it is the kind of claim that quietly
promises something that isn't there. I read the code directly rather than the
completion report.

**The claim holds.** Multi-voice Table is genuinely live in the shipped frontend:

- `screens/Launch.tsx:95–137` — the real Table field: seat toggles, a
  `TABLE_SEAT_LIMIT = 3`, suggested seatings, a "Convene the Table" button gated on
  `seated.length >= 2`.
- `screens/TableRoom.tsx` (160 lines) — a working multi-voice room: per-voice speaker
  attribution by accent color, a `roundOpen` state while voices answer in turn, a
  five-round close ("a Table holds five rounds, and this one is complete"), a
  pluralized seated-arrival strip.
- `hooks/useTable.ts`, `data/pairings.ts`, `lib/sessionStore.ts` (`mode: 'interview' | 'table'`),
  and `App.tsx:176–191` routing a `'table'` screen. Merged history on `TableRoom.tsx`
  (`fde54467`, `4ea877ea`, `1d1d5179`).

Its two companion claims also hold: no `LivingTableScene`, no `RoleSelector`, no
`role_modes` anywhere in `cic-poc/frontend/src` (grep returns nothing), and nothing in
either mockup previews them. And the deep-link grammar it uses is real — `App.tsx:31–38`
parses `?worlds=` and `?mode=`, documented at `App.tsx:13–30`.

Two caveats worth putting on the record, neither of which is the direction's fault:

- I verified the **repository's** frontend. I cannot verify what is actually deployed
  at `cic-engine.onrender.com` from here — that needs a live check before any of these
  links ship.
- **The D0 note's seam D is now partly stale.** It quotes `whats-next.html` saying "the
  multi-voice Table experience does not yet exist on the new architecture." That
  sentence is no longer in `whats-next.html` (grep for "table" in that file returns one
  hit, the Cappadocian line). D3 should carry this correction forward: seam D's
  Living-Table/role-selector half is still live and true; its Table half is not.

**But the direction under-read its own evidence, and it cost it the feature.** Its
ledger item 6 says *"Multi-world deep-link grammar is unconfirmed; pairing links go to
`?mode=table`."* It is not unconfirmed — it is documented in a 17-line comment block at
the top of the same `App.tsx` the direction cites elsewhere: `?worlds=a,b[,c]&mode=table`
seats those voices and focuses the Table field. Because the author believed otherwise,
the two showcase pairings on the homepage are **inert text** — plain `<div>`s, no links,
no actions — and the only Table button goes to a bare `?mode=table`, landing the visitor
on an empty Table field with a disabled "Seat at least two voices" button.

So on the direction that exists to remove steps: the one place where a real one-click
path was available and documented, it shipped a zero-click path instead. "The school
and the desert · the proven pairing" is presented as an invitation and cannot be
accepted.

The same misreading breaks `meet-chloe.html:220`, "Add Chloe to a Table →" → `?worlds=post-apostolic-house-church&mode=table`. Per `App.tsx:85–91` plus `Launch.tsx:36`, that
seats exactly one voice and `canConvene` requires two, so the visitor lands on a screen
whose primary button is disabled and whose label tells them they did it wrong.

---

## 3. Fashionable vs. professional

### 3.1 The thesis is right and I want to say so before attacking it

*"Clarity is a structural property, not a visual style"* is the single best sentence
in any part of this direction, and it is correct. Hierarchy, one-thing-per-section,
progressive disclosure and showing-the-product do separate cleanly from gradient blobs
and Inter. The direction pulls them apart further than I expected. If it dies, that
sentence should survive into D3.

### 3.2 But it imported more of the genre than it thinks, and the tells are structural,
not decorative — which is exactly its own argument turned against it

The direction defended itself against a *surface* audit (fonts, colors, shadows,
radii) and passed it. The audit that matters is the one its own thesis implies: if
clarity is structural, then SaaS-marketing DNA is also structural, and you cannot
launder it by changing the typeface. Run that audit:

| Product-marketing structural move | Present? | Where |
|---|---|---|
| Hero: headline + subhead + two CTAs (one filled, one outline), left column | ✔ | `homepage.html:249–255` |
| Product screenshot in the right column of the hero | ✔ | the leaf, `258–275` |
| Annotation callouts under the screenshot, three across | ✔ | `.notes`, three-column at ≥900px |
| Feature list where every row has its own CTA | ✔ | the seven `.rep` rows |
| Numbered "three things" band, three-column | ✔ | `.three`, `431–456` |
| "What's next / roadmap" section | ✔ | `488–500` |
| Persistent phone-only sticky bottom CTA | ✔ | `.foot-bar` (flagged as a stretch) |
| Section rhythm: eyebrow label → H2 → one-line intro → content | ✔ | every one of six sections |

That is the Stripe/Linear/Notion homepage skeleton, complete, in order, with nothing
missing. What has been changed is the *skin*: Alegreya instead of Inter, parchment
instead of white, madder instead of indigo, 3px corners instead of 8px, hairlines
instead of shadows. By the direction's own thesis — clarity is structure, not style —
that is the wrong half to have changed. It kept the genre and restyled it, then
argued that keeping the genre was fine *because* style and structure are separable.
The argument is self-defeating: if they are separable, then the structure is the
borrowed part.

### 3.3 The expiration date

Will it look dated in three years? The honest answer is **partly, and asymmetrically**.

- The typography, palette, hairline rules and flat surfaces are Alegreya-on-parchment
  and will age like the live site does — fine. That is inherited, locked, and not this
  direction's contribution.
- The *skeleton* above is dated on a known clock. The eyebrow-label → H2 →
  three-column-numbered-band → roadmap-list sequence is legible as a period style the
  way a 2013 flat-design page or a 2009 gradient-and-reflection page is. Ten years from
  now nobody will place a well-set trade book; anyone will place this section rhythm to
  within about two years.
- The composer is the fastest-aging element on the page by a wide margin. Chat-composer
  chrome is a 2023-onward artifact and will read as "the era when everything was a chat
  box" almost immediately.

The specific edge here: a project whose subject is twenty centuries and whose stated
register is a printed book is unusually exposed to period-dating, because the content
makes an implicit promise of durability that the layout then breaks. On a SaaS site
nobody minds that the page looks 2025; here the page is arguing, structurally, that
this is a product from a particular quarter. The manuscript register does not have
that problem — not because it is older, but because it is not tracking anything.

That said, I want to be precise about scale: this is the weakest of my six
load-bearing findings. Three of the eight rows in that table (a hero with two CTAs;
an eyebrow-H2-intro rhythm; a roadmap list) are close to universal and I would not
call them fashion. The composer and the seven-CTA feature list are the two that
genuinely date.

---

## 4. Where a real visitor gets lost

All measured in Chromium unless marked as reasoning.

### 4.1 The dark-mode primary button — 2.69:1, measured

The most serious defect in the direction, and it is one line.

The dark block redefines `--vellum: #1E1913` (both files, line 33) but **never
redefines `--madder`**. `.btn.primary` is `background: var(--madder); color: var(--vellum)`.
So in dark mode the button becomes near-black text on the unchanged madder fill:

| Element | Light | Dark (measured) | Required |
|---|---|---|---|
| `.btn.primary` label | 6.4:1 ✔ | **2.69:1 ✘** | 4.5:1 |
| `.leaf .composer .send` | 6.4:1 ✔ | **2.69:1 ✘** | 4.5:1 |
| `.btn.primary:hover` (→ `--madder-deep`) | ✔ | **~1.6:1 ✘** (reasoned; `--madder-deep` also undefined in dark) | 4.5:1 |

Twelve failing nodes on `homepage.html` in dark, two on `meet-chloe.html` — every
"Begin a conversation," "Come and join us at the Table," "Keeping the Door Open,"
"Send," and all seven visually-hidden "(opens in a new tab)" strings. Verified
visually as well as numerically: in the dark screenshot the hero CTA is a muddy
brown-on-brown slab.

Why this is worse than a normal bug: the README states *"a dark register with
re-checked contrast"* and prints a dark contrast table — "ground `#17130F`,
madder-light `#E08C74` ≈ 7.2:1, faded `#B8AEA1` ≈ 8.5:1 …". Every number in that
table is a *text token*. Not one of them is the primary button, because the author
checked the tokens they had redefined and never checked the component whose fill they
hadn't. That is precisely the failure mode the D0 note warned about — *"the live
site's own history already shows two real dark-mode contrast bugs caught and fixed
after the fact"* — reproduced, in a direction that answered that warning with "AA,
designed to from the start rather than audited into."

### 4.2 Graphite as body text — 3.36:1, measured, and this direction had the warning

Measured failures in light mode:

| Node | Text | Ratio |
|---|---|---|
| `.leaf .fac` (`meet-chloe:272`) | "I'm glad you're here. Come in, settle wherever feels right." | **3.36:1** |
| `.leaf .fac` (`meet-chloe:273`) | The full 60-word Facilitator welcome | **3.36:1** |
| `.leaf .foot` (both files) | "Not saved to an account — this conversation lives in this tab" | **3.36:1** |
| `.leaf .composer .box` | "Ask Chloe anything…" | 3.65:1 |
| `.slug` (sandbox chrome only) | — | 3.38:1 |

`--graphite: #8A837C` is the constitution's Facilitator pigment — correct semantic
choice, and it is legitimately the Facilitator's color at the Table. But on
`--gold-wash #FBF2E2` at 15px it is 3.36:1, and here it is carrying two paragraphs of
real prose, not a label.

The aggravating fact is on the record already. The Decision Log's D1-closure entry
records a cross-validated finding — *"graphite (3.38:1, fails AA everywhere as text)"*
— found independently by at least three of the five directions while building. This
direction's contrast table lists ink, madder, vellum-on-madder, ink-faded, gold-leaf,
Tyrian and all seven census colors. **It does not list graphite**, and it uses
graphite as body text on the inner page. Either it found the problem and didn't apply
it, or it published a contrast table with the one failing color omitted. Neither is
good, and both are worse in a direction whose accessibility case is its second-best
argument.

Also at the margin, measured: gold-leaf `#B45309` on `--gold-wash` is **4.52:1** for
`.leaf .who` ("Chloe · Household Leader") and `.cite` ("✲ 5"), and **4.54:1** for
`.rep .trad` on parchment. Those pass — by 0.02 and 0.04. The README calls this "AA at
the margin," which is honest, but the margin is smaller than a browser's rounding and
smaller than any future palette nudge. Any change to the wash tone silently breaks
them.

### 4.3 The mobile visitor: the navigation does not work on any phone

Measured, `nav.site-nav`, links cut off past the right edge with `scrollbar-width: none`
and `::-webkit-scrollbar { display: none }`:

| Viewport | Visible nav width | Content width | Cut off |
|---|---|---|---|
| 320px | 45px | 386px | **all four** |
| 360px (most common Android) | 85px | 386px | **all four** |
| 375px (iPhone SE/mini) | 100px | 386px | **all four** |
| 390px (iPhone 14/15) | 115px | 386px | **all four** |
| 414px | 139px | 386px | Map, What's Next, Get Involved |
| 480px | 205px | 386px | What's Next, Get Involved |
| 600px | 325px | 386px | Get Involved |
| 768px | 423px | 423px | none |

At 320px the header renders the literal string "**Repre**" — a word cut mid-syllable —
and nothing else. Screenshotted. `.brand { flex-shrink: 0 }` guarantees the nav takes
the entire squeeze.

Three compounding problems:

1. **No affordance.** Both scrollbar-hiding rules are set, so there is no visual signal
   that the rail scrolls. A visitor sees a truncated word and concludes the page is
   broken.
2. **Not keyboard-operable.** Measured: `tabindex` is `null` on the scroller. A
   scrollable region with no focusable child inside the overflow cannot be reached by
   keyboard — a WCAG 2.1.1 failure the live site avoids by not having a scroller here
   at all.
3. **On `meet-chloe.html` it is a dead end.** The homepage survives because Map,
   What's Next and Get Involved also exist as in-page sections a visitor can scroll to.
   `meet-chloe.html` has no such sections. Measured at 390px, the only outbound links
   on that entire page are the breadcrumb, the six other Representatives' Begin links,
   "All seven Representatives," and four footer links. **Map, What's Next and Get
   Involved are unreachable from the inner page on every phone.** A visitor who lands
   on `/meet-chloe` from a search result and wants to know who runs this cannot get to
   About or Get Involved through the header at all.

This is the finding I would lead with if I had one sentence, because the direction's
philosophy paragraph ends *"Mobile first, because the fastest path has to be fast on a
phone,"* and its self-scored accessibility section claims "3.2.4 consistent nav." The
nav is consistent; it is also absent.

### 4.4 The screen-reader / keyboard visitor

**Heading navigation on `meet-chloe.html` skips the two most important blocks.**
Measured heading tree, complete:

```
H1  Chloe
H2  Start anywhere
H2  What a conversation looks like
H2  Whose words these are
H2  Six more chairs at the table
```

Missing: "Where she speaks from" (`.label`, a `<p>`) and "What this voice knows well —
and doesn't" (`.thin .k`, a `<p>`). Those two blocks contain, respectively, the
registry's doorway paragraph — the single richest piece of storytelling anywhere in
this direction — and the honest-limits statement, which is the load-bearing trust
content on the page. A screen-reader user navigating by headings (the primary
navigation strategy for most such users on a long page) is offered "Start anywhere"
and "Six more chairs" and is never offered either of those. The direction's floor
claims "1.3.1 landmarks and heading order." Landmarks yes; heading order, no — the
`.label` eyebrow device is styled as a heading in seven places and marked up as a
heading in none.

Same pattern, milder, on `homepage.html`: the era bands ("The Early Church Era ·
70–312 CE") are `<div>`s, so the seven Representatives arrive as a flat run of seven
H3s with the entire chronological structure — the direction's organizing idea —
invisible to heading navigation.

**`aria-label` on generic elements, ignored by assistive tech.** Measured, three
instances where `aria-label` sits on an element with no role and therefore an implicit
`role="generic"`, where ARIA prohibits naming:

- `div.leaf aria-label="An excerpt from a conversation with Chloe"` (homepage)
- `div.leaf aria-label="A conversation with Chloe"` (meet-chloe)
- `span.cite aria-label="five sources"` (both files, and it is the *only* explanation
  of what ✲ 5 means inside the transcript)
- `div.foot-bar aria-label="Begin"` (meet-chloe)

Consequence: the transcript preview has no accessible name at all. A screen-reader
user encounters, with no framing whatsoever, "You. What was it actually like to be
part of your church, day to day? Chloe, Household Leader. Ordinary, mostly…" — 180
words of first-person historical voice with nothing announcing that this is a *sample*
rather than a live conversation they are now in. On the page whose whole purpose is
disclosing that this is an AI, that is the worst possible place to lose the frame.
The `<figcaption>` does say "An excerpt from a conversation with Chloe, as it
happened" — but it comes *after* the whole transcript. Fix is trivial (`role="figure"`
is already implied by `<figure>`; move the caption's substance to an `aria-labelledby`
or just put a real heading above the leaf) which is why it is worth naming.

And `✲ 5` announces as its raw glyph — most screen readers say something like "black
six pointed star, five" or skip it silently. The homepage marginalia that would explain
it is itself broken (next finding).

**The homepage marginalia are semantically empty for screen readers.** `homepage.html:281–284`:

```html
<p class="k"><span class="gloss" aria-hidden="true">a dotted term</span></p>
<p>opens a short gloss in the tradition's own words — and a full entry one tap further, if you want it.</p>
```

The first paragraph's only content is `aria-hidden`, so it reads as nothing. A screen
reader announces: *"opens a short gloss in the tradition's own words — and a full entry
one tap further, if you want it."* A sentence with no subject. The equivalent note on
`meet-chloe.html:288` is **not** aria-hidden and reads correctly, which tells me this
is an oversight rather than a decision — but it means the homepage's entire explanation
of the disclosure grammar (which the D0 note identifies as the app's real, built,
load-bearing UX contract) is delivered to screen-reader users as a dangling predicate.

**What survives the accessibility attack.** In fairness, and because I went looking:
tab order matches DOM and visual order on both pages at both breakpoints; no keyboard
trap; no positive `tabindex`; focus ring is a visible 2px madder with 3px offset;
`prefers-reduced-motion` correctly kills both the mark animation and smooth scrolling;
all interactive targets measure ≥44px except one inline link inside a sentence, which
2.5.8 explicitly exempts. And the 2.4.11 claim about the phone sticky bar **holds** —
I walked all 60 tab stops at 390px and the only element the bar overlapped was the
bar's own button. I would still add `scroll-padding-bottom` to `html`, because
`scrollPaddingBottom` measures `auto` and the pass currently depends on Chromium's
scroll-into-view heuristics rather than on anything the CSS guarantees, but the claim
as stated is not false.

### 4.5 The first-time visitor who wants context before committing

This visitor is the one the direction structurally cannot serve, and the failure is
not accidental — it is the direction's design.

They arrive, read the hook, read 180 words of Chloe, and scroll. At 1,950px they meet
"Seven Christian traditions, each in its own voice" and seven rows. Each row offers
"Begin a conversation" (filled, primary) and "About [Name] →" (a text link). They want
the second one. Six of the seven "About" links — `meet-theon.html`, `meet-mar-yausep.html`,
`meet-marius.html`, `meet-papnoute.html`, `meet-chilo.html`, `meet-albina.html` — **do
not exist.** The direction's ledger discloses this (item 8, "Only Chloe's inner page
exists"), which is honest for a mockup. But it means the direction's own two-step path
("row → About → Begin") has been demonstrated exactly once out of seven, and the
demonstration is the page missing the AI disclosure. If those six pages are the answer
to the "context before committing" objection, they are also the answer nobody has
built or reviewed.

More structurally: **there is no "I don't know which one" door anywhere.** The homepage
offers a 7-way choice with no default, no recommendation, no "start here," and no
question-first entry. The direction explicitly refused a "learn more detour" as a
step to be eliminated. For a visitor whose actual state is "I don't know what I'm
looking at yet," every one of the nine primary buttons is premature, and the direction
has removed the one affordance — a slower door — that would have served them.

### 4.6 The returning visitor

The best-served case, and I will grant it: seven rows always in the same order, all
present, no carousel to re-scroll, deep links straight into the app, `#meet` and
`#support` as stable fragments, nothing hidden behind a sheet. A returning visitor who
knows they want Papnoute gets there faster than on the live site. This is a real win
and the clearest evidence for the direction's thesis.

Two dents. First, they still scroll ~2,500px on a phone to reach the rows, because the
hero cannot be skipped and the direction refused a header CTA. Second — and this is
the one the author should sit with — the pilot note sits at `homepage.html:407`,
*after* all seven invitations to begin:

> *"…we're asking each participant to keep to about five conversations for now."*

A returning visitor is by definition someone using up that allowance. They read seven
invitations and then a rationing notice. It is live copy, verbatim, so the words are
not the direction's fault; the *placement* — mid-funnel, immediately after the seven
buttons, immediately before the Table upsell — is. On the live site it sits under the
carousel and before the CTAs, which is gentler. And the brand never-list bans "urgency
or scarcity"; "a limited number of participants" is inherited, but this layout amplifies
it into the conversion path rather than damping it.

---

## 5. Mark's two added constraints

Folding in Mark's later note: *"non religious (even though we are religious, i don't
want the feel of religion) i want the general interest, re-assesing (deconstruction),
pastor and scholor to feel at home, but my heart is those seeking answers to hard
questions of faith, not accademics."*

### 5.1 Religious feel — mostly clear, with one real and one structural problem

**The chrome is clean.** No crosses, doves, flames, ornament, drop caps, illumination,
Cinzel, gold rules, or liturgical vocabulary in the interface layer. Labels are plain
("Meet the Representatives," "Explore the map," "Where we're headed"). The one
devotional-register phrase in the whole build — "Come and join us at the Table" — is a
locked protected line. On the narrow question Mark asked, this direction is the
cleanest of the registers I can imagine for this project. Genuine credit.

**But the hero's showcase paragraph is a communion liturgy.** This is not a small
thing, because the excerpt is the direction's *entire* answer to the fourth charter
goal, and it is the first substantive prose a visitor reads. What it says:

> *"On the day named for the sun, we gather under whatever roof will hold us… Someone
> reads: the words of the prophets… Whoever presides speaks a while after, urging us
> toward what we just heard. **We stand together and pray. Then bread and wine mixed
> with water are brought, thanks is given over them, and we eat together — that is the
> center of the day, the thing everything else circles around.**"*

Preaching, corporate prayer, and the Eucharist, in order, described from inside, in
the first person plural. Someone who is deconstructing — who may have left a church
over precisely this liturgy, and who came to this site because it promised history
rather than worship — opens the homepage and the first real content is a service they
are inside of, narrated by "we."

The direction chose this deliberately: *"The draw is the real exchange in the hero:
Chloe describing an ordinary Sunday."* Against Mark's constraint that reads as the
single worst available excerpt. And the alternative was in the direction's own hands —
`meet-chloe.html` itself surfaces three canon questions, one of which
(*"I'm far from everyone I love. What held your people together across distances?"*) is
warm, non-liturgical, universally legible, and would have made a far better hero. The
direction found the better material and put it on page two.

Secondary, and inherited rather than chosen: this direction gives the seven painterly
portraits more prominence than any surface currently live — seven full rows at 64px
with colored rings, and 176px on the inner page. Robed figures in soft painterly
portraits, arranged in a vertical list with names and roles, reads closer to a
gallery of saints than the live carousel does. The portraits are locked and not this
direction's decision; the decision to make them the dominant repeated visual element
is.

### 5.2 The person with hard questions — this is where I think the direction actually dies

This is the sharpest attack I have, and it is separate from the tech-forward one. It
is not about whether the page looks like a startup. It is about what the page *offers*
to someone in real difficulty.

**Measured vocabulary across both files, ~1,000 lines:**

| Word | Occurrences |
|---|---|
| doubt | 0 |
| struggling / wrestling | 0 |
| searching | 0 |
| deconstruct / re-examining | 1 (inside the inherited pilot-rationing note) |
| crisis, hurt, pain | 0 |
| "hard" | 1 — *"its testimony, beautiful and hard alike"*, a protected line about the traditions, not the visitor |
| "safe" | 2, both in the boilerplate footer line (plus one CSS `env(safe-area-inset-bottom)`) |

Nothing on either page acknowledges that a visitor might arrive carrying something
difficult. The one exception is a marginal note on `meet-chloe.html` — *"if a
conversation touches real distress — steps in to point toward real human support"* —
which is the **fourth of four** sidebar notes, set in faded ink at 15.7px, in the right
rail on desktop and below a 400-word transcript on phone. That is the entire safety
signal in the direction.

**The three-things block is aimed at the wrong person.** "Before you sit down / Three
things to know" is: (1) this is an AI system; (2) it shows its work; (3) witness, never
recruitment. All three are institutional-trust messages — the answers a *skeptic* or a
*scholar* needs. All three are correct and all three are required. But not one of them
speaks to the person Mark named. There is no "you can bring anything here." No "no one
will push you." No "you don't have to believe anything to sit down." The closest is the
protected line *"What it means for you is yours to own and share"* — which is a
statement about interpretive autonomy, correct and locked, and not the same as an
invitation to someone in pain.

**And the information architecture is an academic's index.** This is the part I think
is unanswerable. The homepage's entire organizing structure is chronological:

- Two era bands with century ranges ("The Early Church Era · 70–312 CE")
- Seven rows sorted by `start` date, each carrying dates and geographic regions
- A ten-row ruled table of eras from 70 CE to the present, with Roman numerals
- "Nearly three hundred Christian movements across ten eras"

That is a finding aid. It sorts human beings by century and offers regions and date
spans as the primary selection metadata. It is genuinely excellent for the scholar and
good for the pastor. For the person whose actual state is *"I don't know if I believe
any of this anymore and I don't know who to ask"* — Mark's named heart — it presents a
chronology quiz as the price of entry. They do not have a tradition preference. They
have a question. There is no question-shaped door anywhere in this direction.

**And the direction had the material.** `engine/canon/records/canon_question/` exists; the
direction read it and used three of its questions. Those questions are the one asset
in this whole build that speaks to a person rather than to a curriculum. They appear
once, on page two, in section three of seven, below the fold, as a ruled list under
the label "Questions you might ask." A direction whose entire discipline is "put the
one thing that matters first, remove the steps to it" put the only emotionally warm
door it found seven sections deep on a page six of seven visitors can't reach because
those pages don't exist.

**Does the crisp product register feel transactional?** Yes, and I want to name the
specific mechanism rather than hand-wave at "tone." It is not the fonts. It is that
every unit of the page is a *transaction shaped like a row*: portrait, name, role,
dates, one-line description, filled button. Seven of them, ruled, identical, stacked.
That is the visual grammar of a directory listing — a booking page, a provider search,
a course catalogue. Someone in genuine difficulty scrolling past seven identical
rows with seven identical red buttons is being asked to *select a service*. The word
"Begin," repeated nine times in filled madder, is the vocabulary of a checkout.

The live site is worse at nearly everything else and better at this one thing, almost
by accident: its carousel shows two or three faces at a time, and clicking one opens a
sheet that gives you that one person's paragraph before it gives you a button. It
slows you down at the moment of choosing a person. This direction removes that pause
on purpose and counts the removal as a win in its step map.

That is the deepest problem with the direction, and it is not a bug. It is the thesis
working exactly as designed, against the one visitor Mark says matters most.

---

## Verdict — my adversarial judgment, not a ruling

**It dies as a whole-site direction. It survives, and should survive, as a discipline
to be extracted.**

To be clear about what I am *not* saying. This is not sloppy work — it is the most
verifiable of anything I have read in this workstream. Its honesty ledger is a real
instrument, its refusal table is largely true when checked line by line, its
multi-voice Table claim is correct and I confirmed it in the shipped code, and its
accessibility *stance* is a real improvement on the live site. The four defects in
Section 4.1–4.4 are all fixable in a day and none of them is why it dies.

It dies on the two things a day cannot fix:

1. **Its structure is a product-marketing skeleton, and its own thesis is what proves
   this.** The direction argues that clarity is structure, not style, and then defends
   itself by pointing at style — fonts, colors, radii, shadows. Run its own test on its
   own page and the structure is the Stripe/Linear homepage in order and complete, with
   a chat composer in the hero. You cannot argue that structure is what matters and
   then borrow the structure.

2. **Its information architecture serves the academic and gives the person in crisis
   nothing.** Zero occurrences of doubt, struggling, searching. One buried marginal note
   about distress. A seven-way chronological choice, sorted by century, with regions and
   date spans as the selection metadata, and no question-shaped door — while the
   question-shaped material sat in the repo, was found by this author, and was placed
   on page two of a two-page mockup where six of seven paths lead to files that do not
   exist. Against Mark's stated heart this is not a tuning problem; it is the spine.

And the hero — the one paragraph carrying the whole "draws visitors in" charter goal —
is a communion service narrated in the first person plural, chosen deliberately, on a
site Mark has just said must not feel religious.

**What would have to change for me to withdraw the kill** (offered honestly, because
the author gets a defense and should know what target to aim at):

- Replace the hero excerpt with a question-led opening. Not a liturgy. The canon
  questions are right there.
- Add a question-first door to the homepage, above the picker, for the visitor who
  does not know which tradition they want. This is the actual missing feature, and it
  is the one thing a *product-led* direction should have been best positioned to find.
- Move the AI disclosure above the first Begin button on the homepage, and put it on
  `meet-chloe.html` at all.
- Delete the composer. Keep the leaf.
- Fix `--madder`/`--madder-deep` in the dark block; stop using graphite for prose; make
  the seven `.label` eyebrows real headings; move the `aria-label`s onto elements that
  can carry them; unhide the marginalia; give the nav a real phone treatment.
- Wire the pairings: `?worlds=a,b&mode=table` is documented in `App.tsx` and works.
- Re-file "the Table description," the pairings, and anything else quoted from app
  code as *draft for this surface* rather than *real*, and fix the "world" leak.

Do all of that and what remains is no longer Product-Led Feature Clarity — it is an
editorial or a threshold direction that kept this one's measurement discipline. Which
is, I suspect, the right outcome: **this direction's contribution to D3 is its method,
not its shape.** The refusal table, the honesty ledger, the deep-link verification, the
per-surface contrast math and the accessibility floor are all worth taking forward
whichever direction Mark picks. The homepage is not.

**One correction for the record, independent of this verdict:** D0 seam D is now
partly stale. Multi-voice Table *is* live in `cic-poc/frontend/src` (Launch.tsx table
field, TableRoom.tsx, useTable.ts, App.tsx routing, merged), and `whats-next.html` no
longer carries the "does not yet exist" sentence the D0 note quotes. The Living Table
scene, role selector and guided onboarding remain genuinely absent, so the rest of
seam D holds. Whether the deployed engine at `cic-engine.onrender.com` matches the
repo is unverified from here and needs a live check before any direction ships a
`?mode=table` link. This direction found the Table correctly and deserves the credit
for it — and then under-read the deep-link grammar sitting in the same file and shipped
inert pairings because of it.
