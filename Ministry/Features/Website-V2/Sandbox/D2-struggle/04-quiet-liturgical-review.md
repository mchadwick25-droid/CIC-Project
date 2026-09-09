# D2 adversarial review — Direction 04, Quiet-Liturgical

**Sandbox artifact. Adversarial by assignment. Not a ruling — the author gets one
defense before anything is decided. 2026-09-02.**

Reviewer: Opus, D2 struggle phase. I read `04-quiet-liturgical/` only — `README.md`,
`homepage.html`, `before-you-sit.html`, each in full. I did not open any other D1
folder. I did read `05-product-led-clarity-review.md` for house format; nothing in it
informed a judgment here, and it concerns a completely different direction.

**Method note — the browser work is real.** Chromium
(`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`) driven by Playwright, both
files served over a local HTTP server (not `file://`, so the JS behaves), at 320 /
360 / 390 / 414 / 1440 px, in light and dark, with and without
`prefers-reduced-motion`, with and without JavaScript. Geometry, tab order, the ARIA
tree and computed colors are read out of the live DOM. Every contrast number below
is computed from hex values by the WCAG 2.x relative-luminance formula, not copied
from the README. **One caveat, stated up front:** the sandbox blocks
`fonts.googleapis.com`, so all renders used the fallback stack (Georgia / system-ui)
rather than Alegreya. Absolute pixel heights will shift a few percent with the real
faces loaded; every ratio and every comparison below is between measurements taken
under the same condition, so the comparisons hold. Where a finding depends on exact
text width — the order-marker clipping — I say so and give the margin.

---

## Summary: what actually kills, before the argument

Eight findings I consider load-bearing. Six are provable defects. Two are the
direction's spine, and those are the ones that matter.

1. **"The narthex remembers" is implemented on the wrong page.** All `localStorage`
   code lives in `before-you-sit.html`. `homepage.html` contains none. A returning
   visitor who types the domain walks all eight stations again, every time, forever.
   This is the strongest of the four side doors the README offers against the
   returning-visitor attack, and at the primary entry point it does not exist.
2. **The escape hatch is clipped off the screen on small phones.** Measured: at 320px
   and 360px the order marker's fourth item — **"Door"** — overflows a container with
   `scrollbar-width:none`, no arrow, no fade, no scrollbar. The one-click-to-the-end
   affordance is unreachable by touch at exactly the widths where a visitor needs it
   most.
3. **The site's only forward control is the faintest thing on the page.** "Continue
   when you are ready" is `#6C6257` — 2.54:1 against the surrounding body text — with
   an underline composited to `#D6D2CB`, **1.36:1** against the ground (dark mode:
   1.82:1 and 1.52:1). It is the sole way on from four of six homepage stations.
4. **`aria-current` deliberately lies through 18% of the page,** in a direction that
   adopts WCAG 2.4.8 *Location* as a binding AAA criterion. Measured: through both
   silences (1,530px of 8,620px) the marker reads THRESHOLD. On a phone it still reads
   THRESHOLD while the Greeting headline is on screen.
5. **Without JavaScript the seat picker is inert and silently discards the visitor's
   choice.** Measured with JS off and `?who=desert-monasticism`: no radio pre-checked,
   button reads "Go to the Table," href `?mode=table`. Selecting a radio by hand
   changes nothing — the form has no `action` and the href is only rewritten by
   script. The README claims "the page complete without JavaScript."
6. **The direction conflates two unrelated reasons for stillness.** The Living Table
   is still because it is *ground beneath a primary surface* and because of the
   anti-ghost representation rule (§4.0, §2.5a). Neither reason exists on a marketing
   page. The stillness is re-justified on a new premise — that arrival should be
   slow — which the constitution nowhere holds and in several places contradicts.
7. **Forced pacing is the exact inverse of the constitution's own Participant
   Agency value.** Every paced moment in `CiC_Full_UX_Design_V1_0.md` is
   participant-initiated and skippable. These two are neither. The README states the
   contradiction as a feature: *"the order unfolds at a pace the people did not
   choose."*
8. **The liturgical structure is load-bearing and cannot be stripped.** The author
   already removed every explicit religious word from the visible copy — I checked;
   "narthex," "liturgy," "rubric," "order of service" appear **zero times** in
   rendered text and only in code comments and class names — and the page still reads
   unmistakably as a service. That is the strongest possible evidence that the feeling
   is produced by structure and typographic convention, not vocabulary, and therefore
   that Mark's 2026-09-02 register ruling reaches the spine, not the copy.

Findings 1–5 are a day's work. Findings 6–8 are the direction.

---

## 0. What verifies, so the attacks land

I checked the direction's own claims against the files rather than trusting them, and
most of them hold. Saying so is not politeness; an attack that misses makes the ones
that land easier to dismiss.

- **The contrast table is honest.** Every one of the eight pairs in the README
  reproduces to two decimals: 13.70 / 5.86 / 5.39 / 4.54 / 6.33 / 13.24 / 15.35–8.45–
  7.19–8.47 / 14.76. Not one is rounded in the direction's favor.
- **The graphite finding is real and correctly measured.** `#8A837C` on parchment =
  **3.38:1**. This corroborates the cross-validated D1 finding already in the
  Decision-Log, from an independent computation.
- **The "Arriving" motion is byte-faithful** to
  `Brand-Assets/CiC_Logo_Arriving_Motion_Reference.html` — same delays (800/1300/600
  /2400/3750ms), same keyframes, same phantom-dot guard, same reduced-motion block.
  Nothing was invented.
- **Reduced motion is correct, measured.** With `prefers-reduced-motion: reduce`:
  `scroll-behavior: auto`, `scroll-snap-type: none`, ring `stroke-dasharray:
  260px, 100px` (completed), seat `matrix(1,0,0,1,0,0)` (settled), breath off. That is
  exactly what the Logo Usage Sheet requires ("the completed still mark, table built,
  guest seated").
- **The adjacency guard holds by construction.** `before-you-sit.html` carries the
  wordmark only; no Arriving mark anywhere on it; the chair does not breathe. Correct.
- **The census data is accurate.** All seven ids, names, titles, tradition names,
  subtitles, date ranges, regions and entry colors match
  `cic-website/data/world-census.json` exactly, in correct chronological order within
  correct eras. No invented traditions. (One unmarked edit: Marius's dates gain a "CE"
  the census omits. Trivial.)
- **The deep-link grammar is real.** I verified `?worlds=<id>&mode=interview`,
  `?worlds=a,b&mode=table` and bare `?mode=table` in
  `cic-poc/frontend/src/App.tsx` (`parseDeepLink`, lines 18–36, 80–85). The links work.
- **The protected lines are verbatim**, all six of the ones used, and `data-copy`
  marking is applied consistently and honestly — draft prose is labeled draft.
- **The lockup rule is fixed.** The italic *in* is present, which the live header
  drops. Good catch, correctly executed.
- **The unshipped is not promised.** No composed multi-seat Table scene, no Living
  Table language, no "in development" status claims, none of the six uncleared photos.
  Seams D, B and H are respected.
- **Keyboard order is clean.** 30 tab stops on the homepage, in DOM order, all
  logical; skip link works; focus ring 5.86:1; `scroll-padding-top` prevents the
  sticky strip from covering a focused target. This is better than most production
  sites.

That is a real craftsman's file. Now the attack.

---

## 1. Charter-goal failures

### 1.1 "Easy access to features" — the measurement, not the argument

The README treats this as the direction's known weak point and offers four side
doors. Rather than argue about the philosophy, I measured the paths. All numbers are
document-coordinate pixels at 390×844 (a current mid-size phone) and 1440×900, with
the same font condition on every page.

| Path | Distance to the primary action |
|---|---|
| **Live site**, mobile | CTA at **1,295px**; ≈500px of actual scrolling; one page, one tap |
| **Live site**, desktop | CTA at 1,174px in a 1,712px document |
| **D04 homepage**, mobile | door button at **8,761px** in a **9,813px** document (89% down) |
| **D04 homepage**, desktop | door button at **7,635px** in an **8,620px** document (89% down) |
| **D04 full first-time path**, mobile | 9,813px page → second page 5,224px, button at 4,744px |

Actual scrolling required, first-time mobile visitor, front door to the app:
≈7,970px + ≈3,950px = **≈11,900px across two page loads**, versus ≈500px and one
page on the live site. That is roughly **24× the scrolling** to reach the same
destination.

Best case using the direction's own fast lane — a "Sit down with Chloe" link at
3,841px, then `before-you-sit.html?who=…`, then the seat button at 4,744px — is
≈6,990px, still ~14×.

The document is 4.8–5.0× the live site's length. The `<h1>` — the protected hook,
the sentence that says what the project is — sits at 1,870px (desktop) / 1,662px
(mobile). More than two full screens down.

### 1.2 The four side doors, checked one at a time

**1. The header side door — works, with two costs.** *"Already know the way? Go to
the Table →"* is real, points at `?mode=table` (verified live grammar), and is the
only genuine one-tap shortcut in the file. Two costs. (a) It is 42 characters of
italic text in a flex nav, which forces the mobile header to **three lines: 183px at
360–414px, 210px at 320px**. With the sticky order strip that is **232–258px of
chrome before the first pixel of content** — 27% of a 844px viewport, 34% of a 760px
one. (b) It bypasses the Greeting, and therefore bypasses the AI disclosure the
README calls "the brand's 'Always' made structural." The direction's structural
answer to the trust rule and its answer to the speed problem are mutually exclusive:
you get one or the other, never both.

**2. The order marker — partially broken, and it misreports position.** Measured
overflow of `.order ol`: at **320px**, 356px of content in a 320px box; at **360px**,
376px in 360px. The clipped item at both widths is **"Door."** The container has
`overflow-x:auto; scrollbar-width:none` — no scrollbar, no arrow, no gradient, no
hint. A touch user has no way to know the item is there. (Keyboard users recover:
focus scrolls it into view. Touch users do not.) 360px is iPhone SE / 12 mini /
much of the Android midrange; 320px is also what any 640px viewport becomes at 200%
zoom, which puts this inside WCAG 1.4.10 *Reflow* territory. With Alegreya Sans
loaded instead of the fallback the strings will most likely be *wider*, not
narrower — the margin at 360px is only 16px.

**3. Per-Representative "Sit down with X" — the best idea in the file, and it is not
a shortcut to the app.** It is a shortcut to the *second* threshold. `Sit down with
Chloe` lands on `before-you-sit.html?who=…`, which is another 4,744px and another
five stations before the seat button. It cuts the walk by about 40% and still ends
in a second rite.

**4. "The narthex remembers" — not implemented where it is needed.** This is the
finding I would put first if I could only make one. `homepage.html` contains **no
storage code at all**; its entire script is the side-door href and an
IntersectionObserver. The `cic-threshold-crossed` key is read and written only inside
`before-you-sit.html`. A returning visitor's actual behavior is to type the domain or
click a bookmark, which lands them on the homepage — where nothing is remembered, and
where they must scroll 8,761px again to reach the door that leads to the page that
does remember them. The README's sentence — *"The slow walk is a first-time rite, not
a tax"* — is false at the front door. It is a tax, levied on every visit, and the
receipt is on the wrong page.

So: of four claimed mitigations, one works with a real cost, one is broken on small
phones and lies about your location, one shortens the walk without ending it, and one
is absent from the page that needs it. The README says "That cost is chosen; D2
should price it." The price is 24× the scrolling and a returning-visitor experience
identical to a first-time one.

### 1.3 The site gets in its own way at the moment of first contact

The Arriving motion holds the ring at `opacity: 0` for **800ms**. I screenshotted the
first paint. For most of the first second the entire website is: a wordmark, a nav, a
**single small red dot** in the middle of an empty parchment field, and a sentence
reading *"The mark is a table; the opening is the way in — and it never closes."*

That sentence is describing an object that is not on screen yet.

The Logo Usage Sheet's rule is *"The mark never appears at first contact without this
one plain sentence beside it."* That is a **caption rule** — it protects the mark from
being shown bare. This direction has read it as a **headline rule** and promoted an
internal brand-explanation sentence to the position of the site's entire above-the-fold
message. It explains the logo to a visitor who has no reason yet to care that there
is a logo. Nothing on screen one says what Church in Conversation is, does, or offers.
For a pilot actively trying to grow participation, whose growth mechanism is shared
links, the first paint of a shared link is content-free.

### 1.4 "Clear storytelling" — the goal it genuinely serves, with one hole

The order *is* legible; the seven-place chronological list is materially better than
the live horizontally-scrolling carousel for scanning, for keyboard use and for screen
readers; the era headings are real `<h3>`s; the trust block is well argued. This is
the direction's strongest charter goal and I am not going to pretend otherwise.

The hole: the README's defense of the missing above-the-fold is *"Search snippets
still carry the hook (the `<h1>`, at the second station); the first paint does not."*
That is true of Google. It is not true of the thing that actually matters here — a
person opening a link a friend sent them, which is the pilot's growth path. They do
not get a snippet. They get the dot.

### 1.5 "Professional / cutting-edge" — real craft, wrong claim

The craft is real. But the README's warrant — *"Cutting edge the way a well-set book
is — nothing on it will date"* — is a claim about the wrong parts. The typography and
palette will not date; they are the brand's, and they are good. The **scroll grammar**
will. See §3.

---

## 2. Constitution and brand conflicts

### 2.1 Two different reasons for stillness, silently merged

This is the direction's central intellectual move and I think it is a substitution,
not an extension.

`CiC_Full_UX_Design_V1_0.md` §4.0 gives the Living Table's stillness **two** reasons,
both of them exact and both of them local:

1. **It is ground beneath a primary surface.** "The transcript is the sole primary
   surface; the scene is the populated, still descendant of the approved landing
   hero." And, explicitly: *"with nothing moving, the scene is unambiguously ground —
   it adds no primary surface and consumes no card slot."* The stillness exists to
   satisfy the five-count's one-primary-surface rule. It is a **budget** decision.
2. **The anti-ghost rule** (§2.5a): "these must feel like real people at a table, not
   spirits or ghosts… no lighting or glow." Figures stay solid; the speaker is marked
   by a nameplate inverting rather than by glow or dimming. That is a **representation**
   decision — about how a person is depicted, not about how fast a page unfolds.

Neither reason survives the move to a marketing page. There is no transcript here for
the page to be ground beneath; there is no primary surface being protected from
competition; there are no figures whose personhood is at stake in whether a section
fades in. The direction keeps the *conclusion* — nothing moves — and swaps in a new
premise: that arrival should be slow, because a service opens with silence.

That premise is not in the constitution. It is not in the Brand Guidelines. It is an
argument from ecclesial practice, made in the README explicitly (*"A service opens
with silence, then a greeting; the order unfolds at a pace the people did not
choose"*). The direction is not extending §4.0's logic; it is borrowing §4.0's
vocabulary to license a different decision. The Decision-Log's D1 closure called this
direction's most attackable point "slowness vs. access." I think the deeper one is
this: the authority it cites does not say what it needs it to say.

### 2.2 Forced pacing is the inverse of the constitution's stated governing value

The constitution names its governing values in its own preamble, and one of them is
**Participant Agency — "conditions for discovery, not pressure toward predetermined
outcomes."** Every paced moment the document designs obeys it:

- Guided onboarding G.1–G.3: *"One beat at a time, everything skippable, standing
  escapes to the map and the question door."*
- The reflection beat (§5.6): *"one optional question… private by default, never a
  form,"* skippable in one action.
- Closing resources: *"ask, never push… a decline is a complete, graceful path."*
- Level-3 panels: *"Participant-initiated only."*
- The map (§5.2): *"on-request always, never auto-opened."*
- The tour (§5.5): *"Entry only by consent… decline final for the session, never
  re-pressed."*
- Even the next-questions card: *"Typing dismisses instantly."*

Every one of those is **opt-in**. This direction's two silences are **opt-out**, and
they are opt-out in the weakest sense: they sit directly in the scroll path (765px
desktop / 464px mobile each) and the exit is either a 1.36:1-underlined gray link or
an order marker that is clipped on small phones and displays the wrong station while
you are inside them.

The README's own philosophy sentence — *"the order unfolds at a pace the people did
not choose"* — is, word for word, "pressure toward predetermined outcomes" restated
approvingly. The direction did not notice that it had written the constitution's
prohibition as its thesis.

### 2.3 The S0 inversion, unnamed

§5.1 designs the Threshold as: the protected hook **as the headline**, three co-equal
doors on the primary surface, CTA register beneath. Door first.

This direction removes the headline from the first surface entirely and puts the
single door at station IV, at 89% of the page. That is a larger departure from the
constitution than any of the four stretches the README *does* flag (mark out of the
header, soft snap, a second threshold, chair placement), and it is not flagged at all.

I note for the record that per the Decision-Log's D1 closure, direction 03 named its
S0 inversion explicitly as its own weakest point. This one made the bigger inversion
and did not name it. The charter's rule is that a proposed stretch of a locked rule
is "flagged explicitly as a ruling for Mark, not made quietly." This one was made
quietly.

The mitigating fact, which I will grant: seam D says the constitution governs the app,
not this site. Fine — but then the direction cannot lean on §4.0 for authority in
one breath and disclaim §5.1's jurisdiction in the next. It cited the constitution as
its warrant. It is bound by the citation.

### 2.4 The motion rule, and a ruling that should have been surfaced

The Logo Usage Sheet's never-list includes: *"the motion never replays unbidden and
never plays the joining at a visitor."*

This direction autoplays the full sequence — including `cic-sitdown`, which *is* the
joining — on every page arrival, at 176px, as the sole content of screen one, with the
breath looping forever after.

I want to be fair: the brand's own implementation reference autoplays on load, and
says "one motion, once per page arrival," so the direction is faithful to the
reference file. But the Usage Sheet sentence exists separately and says something the
reference does not, and "the joining, played at a visitor who did not ask, as the
entire first screen of the site, forever breathing" is at minimum the case that
sentence was written to worry about. The direction surfaced four stretches for Mark's
ruling. This is a fifth and it is not on the list.

### 2.5 One voice pair inverted without argument

Brand voice pair four: **"Technology but not seen — experience first, governance
second, mechanism third."** The direction puts governance — the AI disclosure, the
real-time-monitoring line, the silence-stands line — at the top of station II, before
the visitor has met a single Representative or seen anything of the experience. The
brand's "Always" list does say raise the AI question yourself, first. The two rules
are in genuine tension and the direction resolves it in one direction without
noticing there was a tension. Modest, but it is the same pattern: assertion where an
argument was owed.

### 2.6 Three violations of the constitution's own type floor

§2.2: *"Nothing smaller than 13px ever carries meaning."* Measured computed sizes:

| Element | Size | Carries meaning? |
|---|---|---|
| `.order a` — the whole order marker | **12.48px** | yes: it is the page's navigation |
| `.eyebrow` — "The Greeting" / "The Table" / "The Door" | **12.8px** | yes: they are the station names |
| `.seat-era` — era bands on the seat picker | **12.48px** | yes: it is the only grouping cue |

A direction whose entire legitimacy claim is faithfulness to the constitution breaks
its one numeric typography rule three times, in the three places most specific to
this direction's own design.

---

## 3. Fashionable versus professional

### 3.1 Name the trend precisely

Full-viewport scroll stations, proximity snap, a "breathing" beat between sections, a
short centered serif line alone in a lot of white, a fixed left-rail progress marker,
and a "scroll to continue" cue is not a neutral or timeless grammar. It is the
signature register of the 2019–2024 agency portfolio, the luxury fragrance
microsite, the wellness app landing page and the Awwwards submission. "Slow" has been
a mass-market visual style for at least five years. It is *currently* fashionable —
which is precisely why it reads as tasteful right now, and precisely why it will read
as dated in four.

The README's defense — *"Cutting edge the way a well-set book is — nothing on it will
date"* — protects the wrong assets. The Alegreya setting and the manuscript palette
will not date; they belong to the brand and they are genuinely well done. The scroll
grammar will. And a well-set book is exactly the wrong analogy for it: a book does not
snap, does not gate, and above all **lets you flip.** You can hold a book open at the
index. This page's structure is a slideshow, and the slideshow is the fashion.

Two specifics under this heading:

- `*, *::before, *::after { transition: none !important }` is not restraint, it is a
  sledgehammer. It kills every transition any downstream component would ever want,
  including focus-state easing, and it does so with `!important`, so any real build
  will have to fight it. Restraint is choosing not to add transitions. This is
  forbidding them globally, which is a different and less professional thing.
- The soft snap is conceded in the README as *"technically a scroll the visitor did
  not make."* Combined with `scroll-behavior: smooth` on `html`, clicking "Door" in
  the order marker animates a 7,553px traversal. The direction's own escape hatch is
  itself a piece of pacing.

### 3.2 Real reverence and the picture of reverence

Here is the distinction I think matters most, and it is not a matter of taste.

Reverence in a liturgy is **communal, participatory, and chosen.** The silence is kept
*by people, together*, and everyone in the room walked in on purpose. It costs the
participants something and it is theirs.

A silence on a website is kept by nobody. It is a `<section>` with `min-height: 85vh`
and no children but a red italic line asserting that silence is being kept. Nothing
is happening. No one is present. The visitor is not participating in a silence; they
are looking at a picture of one, alone, on a device, probably while doing something
else.

That gap — between an act and a depiction of an act — is the exact definition of
"atmospheric." When a page tells you what interior state it is producing in you, that
is the tell. "Silence is kept." is the site describing its own effect, which is what
mood-board design does and what real design never needs to do.

I want to be precise about the accusation. I am not saying the direction is
insincere; I think it is entirely sincere. I am saying that sincerity does not convert
a blank div into a shared silence, and that a page which asserts its own reverence has
already substituted the sign for the thing.

### 3.3 It fights participant agency, and says so

Covered in §2.2, but it belongs here too, because this is the point where fashion and
principle meet. The fashionable version of "slow" and the constitution's version of
"unhurried" are opposites. The constitution's is *"warm, unhurried"* — a *register*,
a quality of the writing and spacing, applied to content the participant controls the
pace of. This direction's is *tempo control*, applied to a visitor who did not ask.
The first is hospitality. The second is stage management. The README calls the second
one hospitality, and that is the confusion at the heart of the file.

---

## 4. Where a real visitor gets lost

Five scenarios. Numbers are measured, not estimated.

### 4.1 First-time visitor in a hurry, desktop

Arrives from a search result or a shared link. Screen one, for the first 800ms: a red
dot. After 3 seconds: a large C, and a sentence explaining that the C is a table. No
statement of what this is. No headline (it is 1,870px away). No action (7,635px away).
The one link on screen is 14.7px gray text with a 1.36:1 underline reading "Continue
when you are ready."

There is no five-second answer to "what is this site." The README names this sacrifice
honestly ("A five-second decider leaves"). I am pricing it: for a pilot whose stated
goal is growing participation, the front door answers no question in the window where
most visitors decide.

### 4.2 Returning participant

Pastor coming back for a fourth conversation. Types the domain. Lands on the homepage.
**Nothing is remembered** (§1.2, finding 4). The escape is one italic gray line in the
header, which on their phone is on the third line of a 183px header. If they miss it,
they walk 8,761px and land on a *second* threshold page which says "Three things, said
once" — and then says them again, for the fourth time. That page does remember them,
and offers "Go straight in," which is the right idea 8,761px too late.

A second cost here that the README does not name: a visitor who walks the whole path
reads **three protected lines twice within two minutes** — "Where the historical
record is thin, we let the silence stand" (homepage Greeting *and* before-you-sit §II),
"We measure whether each Christian movement…" (homepage Door *and* before-you-sit §III),
and the AI framing sentence ("a conversation with a tradition's witness, not with a
person") near-verbatim on both pages. Two thresholds means saying the same solemn
things twice. Repetition is what turns solemn into rote.

### 4.3 Mobile visitor, slow connection

Both pages load **3.4 MB of portraits eagerly** — seven PNG/JPGs of 511–748px natural
width, no `loading="lazy"`, no `decoding="async"`, no `srcset` — displayed at 132px
(homepage desktop), 104px (homepage mobile), and **44px** (the seat picker). The
bethlehem PNG alone is 1.12 MB for a 44px circle.

The specific hazard the brief asks about is real but not quite where you would guess.
The silence stations do not look broken, because they are not blank: the rubric and
the link are inline HTML and paint immediately. What looks broken is **screen one for
the first 800ms** (one dot, no ring), and what is genuinely confusing is that this
design's deliberate emptiness and a half-loaded page are visually the same thing. A
visitor whose fonts have not swapped and whose portraits are still arriving is looking
at a page whose intended appearance is "mostly empty on purpose," with no way to tell
the two apart. The design has removed its own loading signal.

Add the chrome tax: 232px (390px wide) to 258px (320px wide) of header plus sticky
strip above the first content pixel — 27%–34% of the viewport, permanently.

And at 360px, the "Door" shortcut is off-screen with no affordance.

### 4.4 Screen-reader user — I ran it, and the finding is not what I expected

I dumped the ARIA tree of both pages. Here is exactly what a screen reader encounters
at a silence station, verbatim from the snapshot:

```
- region "A silence":
  - paragraph: Silence is kept.
  - paragraph:
    - link "Continue when you are ready":
      - /url: "#greeting"
```

**So, honestly: no, the silences are not empty content to tab through.** They are one
short sentence and one link each — about eight seconds of speech. The 765px of visual
blankness does not exist in the accessibility tree at all.

That is the interesting result, and it cuts harder than a simple accessibility
complaint would have. **The direction's entire central experience is a purely visual
effect that its own accessibility layer erases.** A blind visitor gets none of the
pacing, none of the held breath, none of the "arriving slowed" that the README calls
the bet. What they get instead is only the *costs* of the structure:

- **Five links named "Continue when you are ready"** on the homepage with five
  different destinations (plus two more on the second page). In a links-list rotor —
  how many screen-reader users navigate — this is five identical rows. 2.4.4 *Link
  Purpose (In Context)* survives on the in-context escape clause; 2.4.9 does not; and
  in practice this is the single most common complaint screen-reader users make about
  a page.
- **Thirteen landmarks on a marketing homepage**, two of them named **"A silence"** —
  duplicate landmark names, both content-free, both cluttering the region rotor.
- **A location indicator that is wrong 18% of the time,** in a direction that adopted
  2.4.8 *Location* as a binding criterion. Measured: through both silences the marker
  reports THRESHOLD. On mobile it still reports THRESHOLD while the Greeting `<h1>` is
  on screen. Announcing the wrong location is worse than announcing none.
- The nav is labeled **"The order of arrival,"** so the liturgical framing is one of
  the few things that *does* reach this user, spoken aloud, with none of the
  compensating atmosphere.
- The seat picker's era bands are `<p>`s, not headings, so heading navigation gives
  seven ungrouped radios.

Net: the aesthetic is invisible to this user; the tax is fully visible. That is an
unusually clean form of the "atmospheric" charge in §3.2 — an effect that only exists
for people who can see it is, by definition, decoration.

### 4.5 Keyboard-only user

Genuinely good, and I will say so: 30 tab stops in DOM order, all logical, no traps,
skip link present and working, `:focus-visible` ring at 5.86:1, `scroll-padding-top`
so the sticky strip never covers a focused target, `.order a` at exactly the 24px
2.5.8 floor, and the seat rows are `<label>`-wrapped so the whole 104px row is the
target rather than the 18px radio. This is above the standard of most shipped sites.

Two costs. (a) The clipped "Door" is recoverable by keyboard — focus scrolls it into
view — so this failure is touch-specific, which is worth knowing but does not fix it.
(b) `scroll-behavior: smooth` means every anchor activation animates; a keyboard user
tabbing to "Door" and pressing Enter watches a 7,553px traversal.

### 4.6 Visitor with JavaScript blocked or failing

Measured, JS off, URL `before-you-sit.html?who=desert-monasticism` (i.e. someone who
clicked "Sit down with Papnoute" on the homepage):

- No radio pre-checked.
- Button reads **"Go to the Table."** Not "Sit down with Papnoute."
- `href` = `https://cic-engine.onrender.com/?mode=table` — Papnoute is gone.
- Selecting a radio manually **changes nothing**: `<form onsubmit="return false">` has
  no `action`, and the href is only rewritten by script.

So without JS the seat picker is not degraded, it is **inert and misleading** — a
control that appears to accept a choice and silently discards it. The homepage is
genuinely fine without JS (four still anchors, everything reachable); this page is not,
and the README's claim is "the page complete without JavaScript."

---

## 5. The religious feel — the central question

The brief asks three things: does the structure inevitably produce a devotional
feeling independent of the words; can the discipline be kept while stripping the
framing; is the framing load-bearing. I will answer all three, and the answers are
yes, no, and yes.

### 5.1 The author already ran the experiment, and it failed

This is the strongest evidence available and it is in the direction's own files.

I grepped the rendered text of both pages, comments and CSS stripped, for the entire
liturgical lexicon. Result:

| Word | In rendered text | In code comments / class names |
|---|---|---|
| narthex | **0** | 4 |
| liturgy / liturgical | **0** | 3 |
| rubric | **0** | 23 |
| order of service | **0** | 2 |
| worship, prayer, sanctuary, sacrament, altar, congregation, devotion, holy, sacred, reverent | **0** | 0 |

The author was scrupulous. Not one explicitly religious word reaches a visitor. Every
liturgical term lives in the source, addressed to the reviewer, never to the reader.

**And the page still reads unmistakably as a service.** That is the finding. If
stripping the vocabulary were sufficient, this direction would already have passed
Mark's test, because the vocabulary is already stripped. It did not pass, because the
vocabulary was never what produced the feeling.

### 5.2 What actually produces it — none of it lexical

1. **The shape of the page is an ordo.** Threshold → (silence) → Greeting → Table →
   (silence) → Door is Gathering → Word → Table → Sending with two beats of held
   silence. Anyone who has been to a liturgical service recognizes this in about four
   seconds without being able to say why. Anyone who *left* one recognizes it faster,
   and with feeling. The recognition does not require the word "narthex"; it requires
   only the sequence, which is right there on the left rail in four capitalized words.
2. **The rubric is a genuine typographic convention, not an aesthetic choice.**
   "Silence is kept." set in red italic *is* a rubric — from *ruber*, red, the color
   service books have printed their instructions in for a thousand years. The README
   says so proudly: "Rubrics — the red instructions of a service book." It is also in
   the passive-impersonal voice of liturgical direction ("the people stand," "silence
   is kept") — the grammatical voice of an institution telling a room what it will do.
   You cannot use that convention and not summon what it belongs to; the convention
   has no other home.
3. **The order marker is a printed order of service.** Four station names down the
   left margin, plus the line *"Two silences are kept along the way."* That is a
   bulletin. It exists to tell you in advance what the room will do to you and when.
4. **"Continue when you are ready," five times,** is the register of a retreat leader
   or a guided meditation. It is kind. It is also unmistakably the voice of someone
   managing your interior state.
5. **One short centered sentence per screen in a lot of white** is, in 2026, the
   shared visual grammar of devotional and contemplative-prayer apps. That association
   is not the direction's fault, but it is the direction's problem.

### 5.3 Can the discipline survive without the framing?

Do the surgery honestly. Remove: the two silence stations, the rubric, the order
marker, the four station names, the eyebrows ("The Greeting," "The Table," "The
Door"), and the five "Continue when you are ready" links.

What remains: `transition: none`, no reveal-on-scroll, no hover lift, exact contrast
math, a chronological seven-place list, a good seat picker, the lockup fix, honest
copy marking, a faithful motion implementation.

Every one of those is a **production value.** Not one of them is a direction. There is
no bet left, no structural thesis, nothing that distinguishes the result from any
other direction that also declined to add gratuitous motion. The philosophy paragraph
— *"the site is treated as the narthex… the order unfolds at a pace the people did not
choose"* — is 100% framing. Delete the framing and the philosophy paragraph is empty.

So the answer is clean and I will not hedge it: **the liturgical structure is
load-bearing. Removing it does not produce a stripped-down Quiet-Liturgical; it
produces a restraint policy that belongs to no direction in particular.** Which,
incidentally, is the most useful thing to say about this file in D3: its discipline is
portable and its shape is not.

### 5.4 The tell in the reasoning

One more, because it is diagnostic rather than rhetorical. The README's defense of the
side door reads: *"Liturgy knows this: the order does not change for the faithful;
they are simply not catechized again."*

That is a product decision justified by ecclesiology, addressed to a reviewer, about a
marketing page. When the reasoning is ecclesial the artifact will be too, however
carefully the surface vocabulary is scrubbed. Mark's ruling — *"a tone/structure
requirement independent of doctrinal content… the site must not read as devotional,
liturgical, or churchy, whatever the words say"* — is aimed with unusual precision at
exactly this file.

---

## 6. Does forced pacing serve someone in real crisis?

The brief says not to soften this. I won't.

### 6.1 The heart audience is disproportionately people leaving rooms shaped like this

Mark's words: *"my heart is those seeking answers to hard questions of faith."* The
Brand Guidelines' silent priority: *"the person whose faith is unraveling."* The
Representative Mode is *Reevaluation* — the artifact formerly called *deconstructing*.

That population has a specific and well-documented relationship to liturgical form.
For a large fraction of it, an order of service is not neutral atmosphere. It is the
shape of the institution they are working out how to stand at a distance from — the
thing that told them where to sit, when to be quiet, and how to feel. Some of them
love it and miss it. Many of them flinch.

This site opens by putting that person through a threshold-crossing rite, keeping a
silence over them, greeting them, and telling them to continue when they are ready —
before it has told them what it is. It performs the institution before it earns the
right to. The performance is beautiful and it is exactly the wrong first move for the
person it most wants.

### 6.2 The pacing takes away the one thing that person arrived with

Someone with a hard, personal question arrives with the question already formed. They
have been carrying it, sometimes for years. What they want is to put it down
somewhere.

This site's answer is: cross a threshold, keep a silence, be greeted, be introduced to
seven people in chronological order, keep a second silence, and then, at 89% of the
page, be told *"When you are ready."*

But it is not their readiness. The README says so: *"the order unfolds at a pace the
people did not choose."* The site decides when they are ready and calls the decision
theirs. For someone whose grievance may be precisely that an institution once told
them how to feel and when, that inversion is not incidental — it is the wound,
restaged, in beautiful typography.

And because it is framed as care, it is harder to object to. "This is for your
benefit; we slowed you down for your own good" is not less patronizing than a popup.
It is more, because a popup does not claim to know what you need.

### 6.3 "No pressure, just witness" — half a pass, and the half it fails is the harder one

Credit where it is owed, unreservedly: on **pressure** this direction may be the best
of any register available. No urgency, no scarcity, no countdown, no conversion push,
no promised transformation, the support ask demoted below the door in the quietest
type on the page, "Not today — back to the door" designed as a complete and graceful
path. That is genuinely admirable and it is a real reading of Mark's value.

But **no pressure and no imposition are not the same thing.** Removing pressure to
*act* while adding pressure to *feel a particular way* is a trade, not a win. A Begin
button asks you to do something and you can decline in a quarter second. A silence
station tells you what interior state to occupy and stands 765px tall while you
disagree with it. The second is the heavier imposition, and it is the one this
direction adds.

The "witness" half fares no better. Witness is testimony offered to someone who
remains free. A rite of arrival is not testimony; it is formation. The direction has
substituted the second for the first while keeping the first's vocabulary.

### 6.4 The distress path, measured

The direction's own before-you-sit copy carries the right line: *"If a conversation
touches real distress, a separate, clearly-labeled voice steps in to direct you toward
real human support."* Good, and correctly placed on the page before the conversation.

Where it lands: 2,126px down the **second** page, behind three movements and reached
only after a silence. For someone arriving in real distress, the measured order of
first contact is: a red dot; a sentence about a logo; a blank screen reading "Silence
is kept"; a headline; an AI disclosure; seven biographies; a second blank screen
reading "Silence is kept"; a door; a second page; three more movements; a third
"Silence is kept"; and then a seat. The safety line is roughly a dozen screens from
first paint.

I do not think the direction is careless about that person. I think it has designed
for an *idealized* version of them — someone contemplative, unhurried, with time and
quiet, who wants to be prepared before they speak. That person exists. They are not
who Mark named.

### 6.5 The comparative question, answered directly

The brief asks whether this direction's thesis conflicts with Mark's heart audience
more than any other direction's does. Working only from the five philosophy
descriptions in the D0 inheritance note and the Decision-Log's D1 closure summary —
I have not seen the other four files — **yes, and the reason is categorical rather
than a matter of degree.**

Institutional-Professional (03) conflicts with an audience **priority**: it
over-serves the academic. That is a weighting problem. Weighting can be re-tuned —
put the record one click behind the door instead of in front of it — and 03 is still
recognizably 03.

Quiet-Liturgical (04) conflicts with a **register prohibition that names its own
structural device.** Mark said the site must not feel liturgical. This direction's
structural device is a liturgy. There is no re-tuning available, because the thing to
be removed is the thing that makes it this direction (§5.3).

You can re-weight an audience. You cannot re-weight a liturgy into not being one.

---

## 7. Findings worth carrying out of this folder regardless of the verdict

Independent of which direction Mark picks, three things here should survive into D3:

1. **The graphite finding, independently confirmed.** `#8A837C` = 3.38:1 on
   parchment; the in-app transcript sets the Facilitator in graphite at 1.0625rem.
   Already logged from D1; this is a second, independent computation agreeing.
2. **New: the seven census tints are unmeasured in dark mode, and four are under
   3:1.** Used here as 2px identity rings on portraits, unchanged from the census
   values, against `--ground #17130F`: **Church and Empire `#7A2E2E` = 1.99:1**,
   Bethlehem `#9d174d` = 2.34:1, Alexandria `#2B5F8A` = 2.73:1, House-Churches
   `#7c3aed` = 3.24:1, Cappadocia `#A0522D` = 3.29:1, Desert `#0f766e` = 3.38:1,
   Syriac `#b45309` = 3.68:1. Whether 1.4.11 bites depends on whether the ring is
   doing identity work; the direction says it is ("the Representative voice
   pigment"). Either way, the README's claim of contrast math "for every pair
   actually used" is not true — these seven are absent from the table. This extends
   the D1 cross-validated finding from *text* usage to *dark-mode graphical* usage
   and belongs in the same V2 usage-rule layer.
3. **New: `--rule` is used as a load-bearing visible boundary and is invisible.**
   `rgba(42,37,33,.16)` composites to `#D6D2CB` = **1.36:1** against parchment
   (dark: `#3A3530` = 1.52:1). It is fine as a hairline between rows. It is not fine
   as the `text-decoration-color` of the site's primary forward control, nor as the
   sole border of the `.returning` callout. Any V2 stylesheet should carry a rule
   that `--rule` never distinguishes an interactive element.

---

## Verdict

**Dies — as a direction. Survives — as a policy.** This is my adversarial judgment,
not a ruling; the author gets one defense before anything is decided, and there are
two places I would want that defense to push back (below).

**Why it dies.** Not on craft. The craft is the best-executed set of details I have
seen described in this workstream: honest contrast math that reproduces exactly, a
byte-faithful motion implementation, a correct reduced-motion path, a clean tab order,
accurate census data, verified deep links, a real lockup fix, and no promises about
unshipped features. If this direction dies it does not die for sloppiness.

It dies for three reasons, in order of weight:

1. **Mark's register ruling reaches the spine, not the copy** (§5). The author already
   removed every religious word from the visible text — zero occurrences, verified —
   and the page still reads as a service, because the feeling is produced by the ordo,
   the rubric, and the printed order, none of which are words. Strip those and no
   direction remains (§5.3). The framing is load-bearing. That is the fatal fact, and
   it is fatal regardless of every other finding in this file.
2. **The thesis contradicts the constitution's governing value while citing the
   constitution as its warrant** (§2.1–2.2). Every paced beat the constitution designs
   is participant-initiated and skippable, under a value the document names in its own
   preamble. This direction's two are neither, and its philosophy sentence — "a pace
   the people did not choose" — restates the prohibition approvingly.
3. **It serves Mark's named heart audience worst of the available registers** (§6).
   The person with a hard question arrives holding it and wants to put it down. This
   site holds them at the door and calls it hospitality. And for the specific slice of
   that audience that is stepping back from a church, the site is shaped like the
   thing they are stepping back from — before it has said what it is.

**What would have to change for me to withdraw the kill**, offered honestly so the
author knows the target: delete the two silence stations and the rubric; delete the
order marker and the four station names; put the hook headline and one door on the
first surface per §5.1; and fix the six measured defects — the homepage-side
"remembers," the ≤360px "Door" clipping, the 1.36:1 link underline, the inert no-JS
seat picker, the eager 3.4 MB of portraits, and the three sub-13px meaningful type
sizes, plus the stale `aria-current` and the five identical link names.

Do all of that and what is left is not Quiet-Liturgical. It is a restraint *policy* —
no reveal-on-scroll, no hover lift, no transitions, measured contrast, one action per
screen, nothing that moves to attract a click — that any of the other four directions
could adopt wholesale, and probably should. **That is this direction's real
contribution to D3: its discipline, not its shape.** The seven-place chronological
list and the seat picker are also better artifacts than what is live today and are
worth lifting on their own merits.

**Two places I expect a good defense, and where I would listen.**

First, the author could argue that I have over-read the ordo — that Threshold /
Greeting / Table / Door is a *hospitality* sequence (a doorway, a welcome, a table, a
way out) that reads as liturgical only to someone primed by the README, and that a
cold visitor sees four plain English words. That is the strongest available rebuttal
and it is not nothing. My answer is the rubric: "Silence is kept," in red italic, in
the passive-impersonal, is not ambiguous, and it is the one element that retro-reads
the other three as a service. If the defense wants to keep the sequence, it has to
give up the rubric and the silences — and at that point see §5.3.

Second, the author could argue that I priced the slowness against the wrong
benchmark — that the live site's 500px-to-CTA is a *conversion* metric and the charter
asked for a "life-changing journey," not a funnel. Fair. But the charter asked for
four things and "easy access to features" is one of them in Mark's own list, and the
returning-visitor case (§4.2) is not a conversion metric — it is the same person, the
fourth time, walking 8,761px because the memory was built on the wrong page. That one
is not philosophy. That one is a bug.

---

*Reviewer's note on scope: I did not modify any file outside this one, and touched no
git state. Absolute pixel measurements were taken with Google Fonts unreachable
(sandbox proxy), so Alegreya was not loaded; all comparisons are like-for-like under
that same condition, and the one width-sensitive finding (order-marker clipping at
320/360px) is called out with its margin — 36px and 16px of overflow respectively,
with the real face likely to widen, not narrow, the strings.*
