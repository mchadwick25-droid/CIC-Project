# D2 Adversarial Review — Direction 02, Atlas-First Spatial

**Reviewer:** Opus, D2 struggle phase. **Under review:**
`Sandbox/D1-directions/02-atlas-first-spatial/` (README.md, homepage.html,
journey.html), read in full. **Blind to** the other four directions.

**What this is:** an adversarial review, written to kill the direction if it can
be killed. It is not balanced and does not try to be. It is also **not a
ruling** — the direction's author gets one defense before anything is decided,
and several findings below are fixable in an afternoon. What matters is which
ones aren't.

**Method note, stated so the author can check my work:** every claim about the
markup below was verified directly, not read off the README. `homepage.html` was
rendered in headless Chromium (`/opt/pw-browsers/chromium-1194`) at 320 / 360 /
375 / 390 / 800 / 901 / 1000 / 1440 CSS px, in light and dark, with and without
JavaScript, with touch emulation on and off. Contrast figures are computed from
the file's own token values with the WCAG relative-luminance formula. Census
claims were checked against `cic-website/data/world-census.json` directly. Where
I could not verify something I say so.

**Two things I will say up front, because the rest of this document is an
attack.** First: the data fidelity is genuinely excellent. Every count in this
mockup is real — 292 movements, per-era 21/22/18/22/27/23/30/29/51/49, exactly 6
census edges with both ends among the nine worlds shown, seven `Built & Live`
and two `Selected — Not Yet Built`. I tried to catch this direction inventing a
tradition or a number and could not. Second: two of its findings are real gifts
to the whole workstream regardless of what happens to the direction — the
`world-census.json` `ground`/`groundDark` seam (the census cycles three values
across ten eras, so the live Atlas has been painting non-approved grounds), and
the `--ink-faded-ground` token with its light-mode math. Those survive this
review intact and should be carried to D3 whichever direction wins.

Everything after this is the attack.

---

## 1. Charter-goal failures

### 1.1 "Easy access to features" — the page has no feature access at all until JavaScript runs

The direction's own law, stated twice (README §2, and in the file's header
comment): *"the map is a VIEW of a document, never the document. The DOM is an
ordered list of eras and stops… **remove the CSS and nothing is lost.**"*

The auditability test it proposes is the wrong test. Remove the CSS and nothing
is lost. Remove the **JavaScript** and *everything* is lost. I rendered the page
with `java_script_enabled=False`:

| Present in static HTML | Absent |
|---|---|
| the thesis plate (mark, h1, lede, orientation, legend) | **all ten era bands** |
| an empty `<ol class="eras">` | **all nine stops** |
| the edge plate + footer | **Chloe · Theon · Papnoute · Albina · Marius · Chilo · Mar Yausep** — no Representative name appears anywhere |
| two Stripe donation links | **every route into the app** — the string "Interview" does not occur |

The document the accessibility architecture rests on does not exist in the file.
It is manufactured at runtime by `renderEras()` from an inline `WORLDS` array —
and the README states the production build will `fetch` it from
`world-census.json` instead, which makes the dependency a *network* dependency
too. One CSP change, one script error, one failed fetch, one text-only or proxy
browser, and Church in Conversation's homepage is three paragraphs and two
donation buttons.

The live `index.html` has the same JS-built carousel, so this is partly
inherited — but the live page keeps a static `<h1>`, a static lede, and a static
`<a class="btn primary" href="atlas-v3.html">Come and join us at the Table</a>`
whose href is merely *upgraded* by script. The direction removes the last of
those. It is a regression against the page it replaces, on the charter's own
"growth" goal as well: there is nothing for a non-executing crawler, a link
preview, or a text extractor to index about the seven traditions this project
sells.

### 1.2 The only two buttons on the homepage ask for money

This is not rhetoric; I grepped it. `class="btn"` appears three times in
`homepage.html`. Two are in the static body:

```
<a class="btn secondary" href="https://donate.stripe.com/…">Keeping the Door Open — give once</a>
<a class="btn secondary" href="https://buy.stripe.com/…">Open the Door Wider — give monthly</a>
```

The third — `<a class="btn primary">Interview ${w.rep}</a>` — lives inside a
JavaScript template string in `panelHtml()`, and is reachable only after the
visitor scrolls into a band, hovers or taps a stop, and then clicks through to a
Level-3 panel.

So on a 4,635px-tall homepage the complete inventory of button-styled elements
is: two donation asks. Everything else is a text link. The Brand Guidelines say
*"the seeker's voice always outranks the donor's."* Mark says *"no pressure,
just witness."* The direction is not pressuring anyone in its **copy** — the ask
is quiet and the entity sentence is verbatim and correct. But the page's
**visual grammar** says the opposite of its copy: the only two things on it
shaped like an action are asks for money. That is a composition consequence, not
an intent, and it is the kind of thing nobody notices until it ships.

### 1.3 Accessibility: the direction fails WCAG 1.4.10 Reflow at the exact width the criterion names — while claiming to hold it

README §6: *"Also held: … **1.4.10 reflow (no horizontal scroll at any
width)**."* journey.html Beat 7: *"There is nothing to pinch, nothing to pan,
**no horizontal scroll anywhere**."*

Measured:

| viewport | `documentElement.scrollWidth` | `clientWidth` | overflow |
|---|---|---|---|
| **320px** (the 1.4.10 reference width) | 390 | 320 | **70px** |
| **360px** (most common Android) | 390 | 360 | **30px** |
| **375px** (iPhone SE 2/3, 12/13 mini) | 390 | 375 | **15px** |
| 390px | 390 | 390 | ok — first non-overflowing width |

Root cause, isolated: `.plate-title` is a nowrap flex row. At 320px the wordmark
measures 167.7px and `.plate-nav` measures 201.3px; with 25.6px of padding
that's 394.6px of content in a 320px box. `.hide-sm` correctly removes "How this
was made"; the remaining "Read as a list" button and "Get involved" link still
don't fit. One sticky header sets a 390px minimum document width for the whole
page.

Two consequences the direction did not price. First, 320 CSS px is also what a
1280px desktop looks like at **400% browser zoom** — the primary low-vision use
case 1.4.10 exists for. Second, pressing "Read as a list" at 320px makes it
*worse*: 394px. The accessible fallback is the more broken state.

This is one CSS fix. I raise it under charter goals rather than under "small
bugs" because of what it says about the direction's self-assessment: the README
lists 1.4.10 among criteria "also held," and the AAA criteria it makes binding
are argued at length. A floor was declared and never measured at the floor's own
test width.

### 1.4 Accessibility: the AAA "Location" criterion the direction makes binding is absent on phone and removable on desktop

README §6 elevates **2.4.8 Location (AAA)** to binding for the map region:
*"A canvas without 'where am I' is where non-visual and low-vision visitors get
lost: the year badge, sticky era heads, and the region summary make it
binding."* Three mechanisms. Measured:

- **The year badge is `display:none` below 640px.** On the phone form — which
  the direction itself says is *the only form* there — the primary location
  mechanism does not exist. Confirmed at 390×844: `getComputedStyle(#yearBadge)
  .display === 'none'`.
- **The year badge is empty at first paint at every width.** `updateBadge()`
  only fires on `scroll`, and at scrollY 0 the sample point (`innerHeight*0.45`)
  falls inside the 560px-tall `.thesis`, not inside any `.era`, so `best` is
  null and the badge is set to `''`. Measured `badge: ""` at 1440, 1024, 901,
  390 and 320 after full load. The location cue is blank until you move.
- **"Read as a list" removes the sticky era heads.** `body.list-view .erahead
  {position:static}`. So a visitor who takes the accessible fallback loses
  mechanism two, and on a phone they have already lost mechanism one — leaving
  only the `sr-only` region summary, which is a single static sentence, not a
  location indicator.

The AAA criterion is not merely unmet; it is *least* met in the mode offered to
the people it was adopted for.

### 1.5 The one accessibility claim I want to credit, because it's real

Every stop **is** a real `<button>` with a full accessible name, verified in the
rendered a11y-relevant markup: *"Chloe, Household Leader, The House-Churches,
70–200 CE, Antioch, Asia Minor, Rome. Open for conversation."* Focus mirrors
hover. Escape closes the panel and `panelTrigger.focus()` returns focus. Two
skip links, one of them "Skip past the map," which is the right instinct. Every
thread's confidence word and note *is* restated as a sentence in both entries it
joins (`edgeRow()`), so the drawn line genuinely is a picture of a paragraph.
Those are not decorations; they are the hard part, and they were done.

But see §4.3 — the DOM the direction is proud of hides the product.

---

## 2. Constitution / brand conflicts

### 2.1 The stretch list is not the problem. What isn't on it is.

README §7 asks Mark to rule on three stretches. Two of them barely need a
ruling: the mark-plus-sentence lockup with the wordmark alone in the plate is
*exactly* what the Logo Usage Sheet prescribes ("the mark never appears at first
contact without this one plain sentence beside it"; "lead with [the wordmark]
wherever words fit"), and `--ink-faded-ground` is a well-argued addition with
correct math. Meanwhile three genuine stretches of FINAL rules were made
**silently**:

**(a) It dims the Representatives. The spec forbids exactly that, in those
words.** `CiC_World_Icon_and_Table_Template_Spec_V0_1.md` §1:

> "**No camera, no glow, no vignette, no spotlight, and NO dimming of the
> others** — every figure stays fully solid and present the entire time (**a
> dimmed or faded figure reads as a spirit**; §0)."

Full UX Design §2.5a restates it as Mark's own rule: *"these must feel like real
people at a table, not spirits or ghosts."*

The direction's signature interaction is
`.atlas.is-tracing .stop:not(.is-hot) .stop__btn{opacity:.55}`. I measured it at
390px: tapping one row drops **6 of the 9 portrait cards to 55% opacity**. And
`journey.html` Beat 3 knows it is dimming and has tuned the number: *"the 55%
step-back replaces the Atlas's 18%, because on a page that is also the homepage
the rest of the map must stay readable."* The direction chose a value against a
readability constraint and never checked it against the rule that forbids the
behavior.

Yes, the rule's stated scope is the Living Table scene. But the objects being
faded here are the seven **locked, painterly, art-approved Representative
portraits** — the same faces — and the rule's stated reason ("a dimmed or faded
figure reads as a spirit") transfers exactly. This is precisely the class of
thing the D1 brief said must be "flagged explicitly as a ruling for Mark, not
made quietly."

**(b) On phone it dims for no visible reason.** `drawThreads()` returns early
below 900px (`threads: 0` measured at 390px), but `trace()` is not media-gated.
So on every phone and tablet, tapping a Representative fades six other
Representatives to 55% with **no threads on screen to explain the highlight**.
The dimming has lost its rationale and kept its ghost.

**(c) It ships a full dark mode. The constitution deliberately does not have
one, and the one it ships is broken.** Full UX Design §2.1: *"**Dark mode:
deferred, stated plainly.** The parchment ground is the brand… nothing here
blocks a dark app variant and **nothing ships one now**."* The direction ships
eight invented dark tokens under `@media (prefers-color-scheme:dark)` without
flagging it — and the audit that makes README §5 impressive stops at the light
mode. Computed against the file's own values:

*World tints, dark mode.* The seven tints come straight from the census and are
**never redefined** for dark. Against the dark surface `#1E1913`:

| Representative | tint | vs `#1E1913` | as ring (needs 3:1) | as `.p-title` text (needs 4.5:1) |
|---|---|---|---|---|
| Marius · Church and Empire | `#7A2E2E` | **1.88** | fail | fail |
| Albina · Bethlehem Circle | `#9d174d` | **2.21** | fail | fail |
| Theon · Alexandria | `#2B5F8A` | **2.58** | fail | fail |
| *(plans fallback)* | `#6C6257` | **2.93** | fail | — |
| Chloe · House-Churches | `#7c3aed` | 3.06 | pass | fail |
| Chilo · Cappadocians | `#A0522D` | 3.11 | pass | fail |
| Papnoute · The Desert | `#0f766e` | 3.19 | pass | fail |
| Mar Yausep · Syriac | `#b45309` | 3.47 | pass | fail |

Three consequences. (i) `#panel .p-title{color:var(--tint-text)}` renders every
Representative's *title line* in the raw world tint — **all seven fail AA in
dark mode**, Marius at 1.88:1, which is functionally unreadable. This also
directly falsifies README §4's promise: *"world tints appear only as rings,
left-rules, portrait borders — **never as text on a ground**."* They are text,
in the panel, in the direction's own code. (ii) The tint is also the
`box-shadow:0 0 0 2px var(--tint)` used for both `:hover` and the `is-hot` trace
highlight — so for Marius, Albina and Theon the direction's marquee interaction
is *invisible* in dark mode. (iii) README §5 states *"Tints as non-text rings
clear 3:1 everywhere (worst 3.75)."* "Everywhere" is false in the very file that
says it.

*Two more dark-mode misses, same cause.* `--gold-wash:#FBF2E2` is not
overridden, so in dark mode `#panel .p-tile` (the teaser) and every
`.stop__portrait` background render as bright cream blocks inside an otherwise
`#17130F` page. And `--madder`/`--vellum` are not overridden, so the primary
"Interview" button keeps its light fill: internally fine (6.33:1) but its
boundary against the dark panel is **2.69:1**, under the 3:1 that WCAG 1.4.11
requires for the visual information that identifies a control.

*And a brand-record deviation nobody flagged.* The Logo Usage Sheet and Brand
Guidelines define exactly one dark madder — `#CB6E52`, "the dark register." The
direction uses `#CB6E52` correctly for the mark's dot and then invents
`--action:#E08C74` / `--action-hover:#F0A98F` for every link, focus ring and
underline. "Madder never brightened" is on the never-list. The sanctioned value
clears AA on its own grounds (5.18:1 on `#17130F`, 4.89:1 on `#1E1913`), so the
invention isn't even necessary. Two brightened madders, in the same file as the
correct one, unflagged — while a single grey gets escalated to Mark.

D0 §4 warned about exactly this: *"the live site's own history already shows two
real dark-mode contrast bugs caught and fixed after the fact… Each D1 direction
should state its floor and show its contrast math for its own accent choices,
**not assume the existing tokens are safe by inheritance**." The direction showed
its math for the mode it designed and inherited its way into a worse version of
the two bugs already caught on this site.

### 2.2 "The grammar inside the map is unchanged" — it isn't, and the difference is checkable

Stretch #1's whole defense rests on this sentence. §5.2 of the constitution
specifies the map's decided grammar as *"first-visit overlay, hover card → click
panel, edges on demand, persistent tray, legend-as-thesis,"* and the phone form
as *"**search + two filter chips (era · status)**; the ten eras as **accordion
rows**; … Bottom: the same **persistent tray** + handoff contract."*

What the direction actually keeps: hover card → click panel, legend-as-thesis.
What it drops without saying so: the first-visit overlay; the persistent tray;
edges-*on-demand* (threads are drawn always, at 55% opacity, not on request);
search; the two filter chips; and the accordion behaviour itself — nothing
collapses, the "accordion" is ten permanently-expanded bands.

The README nonetheless cites the authority twice — *"Below 640px the list form
is the only form — **the constitution's era-accordion**, a different form, not a
shrink"* — and journey.html Beat 7 grounds the whole phone design in *"Full UX
Design §5.2 and §7.2."* This is a citation to a spec the artifact does not
implement. Whatever Mark rules on stretch #1, he should not be told the grammar
is unchanged, because it is materially changed in six places.

(One place the divergence is *correct*: §5.2's "tap = a bottom-sheet glimpse"
contradicts §2.4's "tap = the Level-2 popover, 'Full entry →' = Level 3." The
direction picked §2.4, which is the better reading. Say that, rather than
claiming fidelity.)

### 2.3 Table-primacy: the strongest counter-evidence is a comment in the file being replaced, and the stretch list doesn't cite it

Stretch #1 argues the site is "a different room" from the app, so §5.2's
never-auto-opened rule doesn't bind. As a reading of D0 §2.D that is defensible
— the constitution governs `cic-poc/frontend`, not `cic-website/`.

But there is a **website-level** decision on exactly this question, dated and
made with Mark, sitting in `cic-website/index.html` lines 15–18:

> "Home — pilot-invitation rebuild, 2026-07-25. **The Table (conversation
> program) is primary; the Atlas is a supporting, secondary entry point
> reachable from nav only, not embedded in the hero.** Built one decision at a
> time with Mark; see the Front-End Strategy thread's decision log."

Not "not the hero" — *"not embedded in the hero"*, decided deliberately, one
decision at a time, with Mark. The direction proposes to make the Atlas the
entire page. That is a direct reversal, and it is the single most relevant fact
Mark would need in order to rule on stretch #1. It is not in stretch #1. The
direction argues against the app constitution, which does not govern here, and
is silent about the site decision, which does.

I do not think this kills the stretch by itself — Mark is entitled to reverse
himself, and a redesign is exactly when you would. But he should be told he is
reversing something, not asked to approve a novelty.

### 2.4 Two smaller FINAL-rule breaks

**"Nothing smaller than 13px ever carries meaning"** (Full UX Design §2.2, also
restated as the direction's own rule in README §4: *"nothing under 13px carries
meaning"*). At the 16px root the file ships, violated in at least seven places:

| selector | size | what it carries |
|---|---|---|
| `#panel h3` | .78rem = **12.48px** | every panel section heading — "About this tradition", "Where it stands on the Creed", "Sources" |
| `#panel .edge .cw` | 12.48px | **the confidence word** — "Contested", "Documented". The project's "confidence always in words" carrier. |
| `#panel .p-doors .cta-label` | 12.48px | **"Come and join us at the Table"** — a protected verbatim line |
| `#panel .p-status`, `.stop__status` | 12.48px | "Open for conversation" / "Chosen — not yet built" |
| `#glimpse .g-s` | .8rem = 12.8px | the status word in the Level-2 glimpse |
| `.stop--journey` | 12.8px | "from Rome, 385 — the circle sails east" |
| `.axis` ticks | .76rem = **12.16px** | Milan · Rome · Alexandria · Bethlehem — the only visual carrier of the west→east geography |

All uppercase and letter-spaced, which makes them harder, not easier. A protected
brand line and the confidence apparatus are the two worst places to spend the
budget.

**The AAA 7:1 claim is invalidated by the direction's own sticky header.**
README §6 makes 1.4.6 (7:1) binding "for text on era grounds," and §5 reports
`--ink-faded-ground` at 7.25:1 on Era I. But `.erahead` is
`background: color-mix(in srgb, var(--eg) 86%, transparent)` with a 2px backdrop
blur — measured live as `color(srgb … / 0.86)`. In the sticky state, 14% of
whatever scrolls beneath composites through. Computed:

| what's behind the sticky head | composited ground | `#4A433C` on it |
|---|---|---|
| a vellum card | `#F1E1BD` | 7.52 ✓ |
| a Marius-tinted card edge | `#DFC4A0` | **5.81** ✗ |
| iron-gall body text | `#D3C39F` | **5.59** ✗ |
| a dark region of a portrait | `#CEBE9A` | **5.31** ✗ |

Still AA. Not the AAA the direction argued for and adopted, and not measurable
at all in the state it actually renders in. On phone this is visible, not
theoretical: in my 390px capture, body text and a stop card are plainly ghosting
through the Era II sticky head.

---

## 3. Fashionable vs. professional

The craft is real. This is a restrained, well-set page — Alegreya throughout,
the era grounds used the way §2.5c says era grounds are for ("the era tint is
the atlas's job"), motion limited to the mark's authorised build-and-breathe and
a 220ms panel slide, `prefers-reduced-motion` honoured everywhere I checked. It
does not look like a template. If the question is "does it look cheap," no.

The question is whether "the homepage IS the map" is a *clearer* way to invite
someone in, or a striking way that costs clarity. Here is what the first
1440×900 viewport actually contains, from my capture:

wordmark · three nav items · the mark and its sentence · the h1 · the lede · a
four-sentence paragraph teaching a coordinate system ("Time runs downward; west
is to the left, east to the right") · a four-item legend · the silence line ·
the axis with nine city labels at 12.16px · the Era I head with its tag, dates
and three events · and **one** Representative card, cut off by the fold.

Zero buttons. Zero doors. One partially visible person. Before a visitor can act
they must (a) learn that this page is a map, (b) learn its axes, (c) learn a
four-symbol legend, (d) scroll.

Three specific things push this from "confident" to "novelty":

**The most CTA-shaped element above the fold is an escape hatch from the
thesis.** Look at the capture: the only madder, underlined, action-coloured
string on the first screen is *"Prefer a list? Read the map as a list."* The
direction's own first screen offers, as its most prominent affordance, an exit
from the idea the direction is built on. That is not confidence; that is a
hedge, and it reads as one.

**Half the legend describes symbols that never appear.** The legend has four
entries: House, Plans, **Question**, **Closed door**. `stopHtml()` emits exactly
two icons: `ic-house` for live worlds and `ic-plans` for selected ones.
`ic-question` and `ic-door` are defined in the `<defs>` and used **only in the
legend itself**. So on first contact the visitor is taught a four-symbol
vocabulary, half of which has no referent on the page. And the largest,
densest block in that legend — visually the heaviest thing in the whole thesis
plate — is the one for a symbol that isn't there:

> "**Closed door** — outside the Nicene base this project builds from; the
> grounds are always stated, and exclusion is never a judgment of unimportance."

That is also a textbook instance of the Brand Guidelines' *"denying a suspicion
nobody raised — say what it is, once, and stop."* A visitor eight seconds into
the site has not yet wondered whether anyone was excluded.

**Eight identical rows of nothing.** Measured on phone: the compressed bands
(Eras III–X) total **2,131px of the atlas region's 3,405px — 63%**. Eight
consecutive rows, each reading "*N* traditions on record · none built yet · the
era survey is complete · See them on the full map →". In the full-page dark
capture this section is unmistakable: it reads as a project-status ledger, not a
map. The honesty instinct is right and I'd defend it against a reviewer who
called it "negative." The *dose* is wrong: a homepage should not spend 63% of
its primary surface, and eight repetitions of one sentence, telling a first-time
visitor what does not exist yet.

**And the deepest structural incoherence: the page whose thesis is "this is the
map" links out to a different map eleven times.** Two era heads carry "All *N*
traditions of this era on the full map →", eight compressed bands carry "See
them on the full map →", the edge plate carries "Open the full map — every
tradition, all ten eras →", and every panel ends with "This entry on the full
map →". Eleven links to `atlas-v3.html`, eight of them with identical text (a
2.4.4 nuisance in a links list, at minimum). A visitor's honest inference is
that this page is not the map; it is a *teaser* for the map, and the real one is
elsewhere.

Which brings the palette debt back. `atlas-v3.html` today runs `--bg:#f3ecdc`,
`--gold:#83662a`, `--ink:#3a3020`, `font: 14px/1.45 Georgia` — verified in the
file. README §5 says the debt is *"paid down, with the math."* It isn't paid; it
is deferred ("In D3, `atlas-v3.html` adopts this token block") while the
direction opens **eleven** front doors onto the unconverged page. Of the five
directions, this is the one whose core journeys route through the debt most
often, and it is the one claiming to have settled it.

---

## 4. Where a real visitor gets lost

### 4.1 First-time visitor, desktop

Lands on a canvas with no door. Reads two sentences of geography instruction.
Learns four symbols, two of which are fictional. Scrolls. Finds Chloe. Hovers.
Gets a card. Clicks. Gets a panel. Finds "Interview Chloe."

That is four deliberate actions and roughly 900px of scroll to reach the first
thing they can actually do — and it only happens if they were curious enough to
poke a card that looks like a label. The direction names this as risk #1 and
calls it "the visitor who wants to be told what to do." That framing is the
problem: wanting to know what a website is *for* is not neediness, it is the
median behaviour, and the direction has no measurement to set against it.

### 4.2 Returning visitor who wants one specific conversation, fast

Deep links are a genuine improvement over the live site — `#alexandria-catechetical`
scrolls to the stop and opens the panel, and I verified it works. Credit where
it's due; nothing on the live homepage is addressable that way.

But that only serves someone who already saved a link. A returning visitor who
remembers "the desert guy" gets: no search (acknowledged), no A–Z, no name list
above the fold, no filter. They scroll ~1,600px on desktop / ~2,200px on phone
into Era II, scan nine cards, tap twice on phone, then find the button. The
direction argues search is "right at seven stops, wrong past a dozen." I'd push
back on the premise: search is not only for *finding among many*, it is for
**arriving with a name in your head**, which is the returning-visitor case at
any n.

And there is a harder omission. Every app link on this page is
`?worlds=<id>&mode=…`. The live homepage's primary CTA is
`LIVE_APP_URL + '/?mode=table'` — the general entrance, no tradition
preselected. **The direction removes it entirely.** A visitor who does not want
to choose a tradition cannot get into the app from this homepage at all. That is
a hard regression, and it lands on exactly the visitor discussed in §6.

### 4.3 Screen-reader user

The heading outline, rendered and read back:

```
H1  Twenty centuries of the Church. One table. A chair pulled out for you.
H2  The Early Church Era
H2  The Imperial Church Era
H2  The Age of Monks and Empires
H2  The Early Medieval Era
H2  The High Medieval Era
H2  The Late Medieval Era
H2  The Reformation Era
H2  The Enlightenment & Awakening Era
H2  The Missionary Era
H2  The Global Church Era
H2  The edge of the map
H3  What's next    H3  How this map was made    H3  Get involved
```

**Not one of the seven Representatives is in it.** A screen-reader user
navigating by heading — the single most common way blind users skim a page —
hears ten era names and three plate names and never encounters Chloe, Theon,
Papnoute, Albina, Marius, Chilo or Mar Yausep. The fastest AT navigation mode
surfaces the *apparatus* and hides the *product*. Eight of those ten H2s
introduce a band containing nothing.

By Tab: 26 stops to traverse the page, and the last eight before the edge plate
are eight links reading "See them on the full map →" — identical text, identical
destination.

Two more real problems in the AT layer:

- **`#glimpse` is `role="tooltip"` and contains a `<button>`.** On touch,
  `@media (hover:none){#glimpse .g-full{display:block}}` makes that button the
  *primary route to Level 3*. WAI-ARIA is explicit that a tooltip must not
  contain interactive content, and the same node is simultaneously wired as the
  button's `aria-describedby` target, where its content is flattened to a
  description string. So the mobile Level-3 entry point lives inside a node that
  is also being announced as a description. It is reachable by swipe
  exploration, so I would not call it a blocker — but it is the wrong construct,
  and it is the *only* construct on the mobile path.
- **Arrow keys, Home and End are hijacked.** `atlas.addEventListener('keydown')`
  calls `preventDefault()` on ArrowUp/Down/Left/Right/Home/End when focus is on
  a `.stop__btn`, and moves focus + `scrollIntoView`. But the stops are **not** a
  composite widget — no `role="listbox"`/`toolbar`, no roving `tabindex`; all
  nine are independently tabbable (verified in the tab sequence). So this is a
  non-standard arrow layer bolted on top of ordinary Tab access, it steals arrow
  keys from readers in forms/focus mode, and it removes Home/End's normal
  jump-to-top/bottom. The README sells this as an accessibility feature. It is
  at best neutral.

### 4.4 Mobile — the worst surface, measured

At 390×844, verified:

| | measured |
|---|---|
| document height | **6,671px = 7.9 screens** |
| scroll depth to `#edge` (About / How this was made / Get involved) | **4,284px = 5.1 screens** |
| empty "none built yet" bands, as share of the atlas region | **2,131 / 3,405 = 63%** |
| year badge | `display:none` |
| "How this was made" in nav | hidden (`.hide-sm`) |

So on a phone, the route to the project's credibility content — the "how it's
built," the "is a Representative an AI? Yes," the academic-review disclosure —
is **not in the nav at all** and requires five screens of scroll, most of it
past bands announcing nothing exists. For Mark's "trustworthy (scholar)" value,
the trust material is the least reachable thing on the phone.

And the primary mobile interaction has a reproducible bug. `#glimpse` is
`position:fixed`, positioned once at tap time from the row's bounding rect, and
`hideGlimpse` is never wired to `scroll`. Measured: tap Alexandria, glimpse
appears at viewport top 505px; scroll 700px; **glimpse still at top 505px**
while its row is now at −633px, off-screen above. My capture shows a 302px
opaque card titled "Theon · Alexandria" floating over "The Early Medieval Era."
Tapping outside the atlas does dismiss it — but scrolling, the dominant phone
gesture, does not, and the popover simply rides down the page covering unrelated
content.

**Back does not close the panel.** `openPanel` uses `history.replaceState`, so
no history entry is pushed (`history.length` unchanged, verified). On phone the
panel is a full modal bottom sheet with a scrim (`aria-modal="true"`, scrim on —
verified) and Back is the universal gesture for dismissing one. Here Back exits
the site. I confirmed this the hard way: after `go_back()` the page context was
gone.

### 4.5 The "read as a list" fallback, tested — it lies at tablet widths

Measured at 800px, before and after pressing "Read as a list":

| | before | after |
|---|---|---|
| `.axis` display | `none` | `none` |
| threads | 0 | 0 |
| `.erahead` position | **sticky** | **static** |
| grid columns | 2 | 2 |
| document height | 4,361 | 4,368 |
| button label | "Read as a list" | **"Show the map"** |
| `aria-pressed` | false | **true** |

Between 641px and 900px the spatial layer is *already* removed by the media
query. Pressing the toggle therefore changes essentially nothing — except that it
strips the sticky era head, i.e. it removes a location cue and gives nothing
back. And the control now reads **"Show the map"** and reports `aria-pressed=
true`, promising a map it can never show at that width, because the 900px media
query overrides `body.list-view` regardless.

That is a control that misreports its own state to everyone, including
assistive technology, across the entire tablet and small-laptop range — and the
direction's whole accessibility story rests on this control being the honest
door out.

### 4.6 One interaction that is a bug being described as a feature

journey.html Beat 4: *"The map stays live behind it; the visitor can keep
hovering other stops with the panel open."* Verified at 1440px with Theon's
panel open, hovering Papnoute: `glimpse.hidden === false`, `glimpse` z-index 60
vs `panel` z-index 80 (so it renders **behind** the panel wherever they
overlap — and the panel occupies the right 440px, which is where the eastern
stops live), and `atlas.is-tracing === true`, meaning Theon's own card is now
dimmed to 55% while his entry is open. Three simultaneous contextual states, one
of them partly occluded, one of them contradicting the panel. Against the
constitution's five-count check (§8: "Cards ≤1"), this is over budget, and the
journey document presents it as a virtue.

---

## 5. Religious feel

Mark: *"non religious (even though we are religious, i don't want the feel of
religion)."*

**On the register itself, this direction is the safest of anything I can
imagine here, and I want to say so plainly before I attack it.** There is no
liturgy, no order of service, no imposed silence, no devotional pacing, no
candle-lit stillness. The typography is a trade book, the structure is a
timeline, and the verbs are "hover," "click," "read as a list." Era bands and
thread lines are not churchy. If the risk register says "which of these five
will feel like a church," this one is at the bottom.

But that is not the only way to fail Mark's test, and this direction finds the
other way.

**It doesn't feel devotional. It feels like a doctrinal vetting board.** Two
things do it, both structural rather than tonal:

1. **The homepage's legend teaches doctrinal exclusion as one of four primitives.**
   The fourth thing a visitor learns about how to read this project — before
   they have met anybody — is: *"**Closed door** — outside the Nicene base this
   project builds from; the grounds are always stated, and exclusion is never a
   judgment of unimportance."* It is the largest block in the legend, it sits in
   the first viewport, and (§3) **no closed door exists anywhere on the page.**
   The project is teaching a boundary-maintenance vocabulary it does not need to
   use yet.
2. **Every single Representative entry carries a mandatory creedal-standing
   field.** `panelHtml()` emits, unconditionally, `<h3>Where it stands on the
   Creed</h3>` — for all nine entries, positioned *above* "Lineage" and
   "Sources." So the fixed schema by which this project describes a tradition
   includes: name, dates, place, story, voices, legacy, **and how it scores on
   the Creed.**

To be fair to the direction: the *content* of those floor notes is generous and
carefully non-judgmental ("Donatism held the same Nicene doctrine as its rivals
— the dispute was about who could validly serve as clergy"). That's good
writing, and it's inherited census text, not invented here.

But the direction's own thesis is that **shape communicates before words do**
(README §2: "The four messages are told by shape"). Apply that test to itself.
The shape says: this project sorts Christian movements by whether they pass the
Creed, and reserves a symbol for the ones that don't. For the person Mark named
as his heart — someone re-assessing, quite possibly re-assessing *the creed
itself*, quite possibly leaving a community over exactly this kind of
line-drawing — the visible governing schema of the front page is orthodoxy
adjudication. That is not the smell of incense. It is the smell of a
denominational review committee, and it is arguably worse for that audience.

This is the most fixable of my major findings — rename the section ("Where it
sits in the historical Christian mainstream"), drop the closed-door legend entry
until a closed door actually appears, move the creedal note below Sources — and
it would largely go away. But it is real, it is on the first screen, and the
direction does not see it, because the direction was written for a reader who
finds the Nicene boundary interesting rather than painful.

**One smaller version of the same thing.** The h1's "the Church" (capital C),
combined with the shape journey.html brags about — *"everything hangs from the
wide house at the top"* — makes the page read as a single genealogical tree
descending from one origin. That is not devotional either, but it is a
*confessional* picture of history rather than a neutral one, presented as
geometry rather than as claim.

---

## 6. Does it serve the person with hard questions, or over-serve the scholar?

This is where I think the direction dies, and not because of any bug above.

### 6.1 The entry model is indexed on the wrong axis

A map — any map — is indexed by **where** and **when**. This one is explicitly
so: `x` from longitude 8°E→43°E, `row` by start year, an axis reading "Milan ·
Carthage · Rome · Constantinople · Alexandria · Bethlehem · Antioch · Edessa ·
Nisibis," and an instruction sentence teaching the visitor those two axes before
anything else.

Mark's heart audience is indexed on neither. Someone re-assessing their faith
arrives with a **what** and a **why**: *did God command genocide · why does the
church treat women like this · was hell always taught this way · can I be honest
about doubt and still belong · is any of this actually true.* There is no
coordinate on this map for a single one of those. To use this homepage that
person must first translate a pain into a century and a city — which is
precisely the translation they cannot make, because if they could, they'd be a
historian rather than someone in trouble.

The constitution's own S0 knows this. Its three co-equal doors are **"Start with
your question" · "Build your own table" · "Guided onboarding"** — and the
question door is first. This direction has **zero** question-shaped doors, no
"Ask the Facilitator" equivalent, no theme chips, no "not sure where to start."
Its total inventory of front-page verbs is: hover, click, read as a list, give
once, give monthly.

### 6.2 It deletes the only sentence on the live site that speaks to that audience

The live `index.html` carries, today, publicly:

> "This is a pilot. We're intentionally looking for a limited number of
> participants across four perspectives — general, pastor or teacher, academic,
> and **anyone re-examining their faith**."

and:

> "Because of cost, we're asking each participant to keep to about five
> conversations for now — we can't enforce this yet, only ask."

I grepped the direction's homepage for both. Neither survives; "re-examining,"
"perspectives," and "five conversations" return zero hits, and "pilot" appears
once, in a footer link to `pilot-feedback.html`.

So the redesign silently removes (a) the single line on the live site that names
Mark's heart audience and tells them they are wanted, and (b) a live honesty
disclosure about a real constraint. Both are the kind of thing that disappears
when a page is rebuilt around a different organising idea and nobody diffs the
copy. Both are exactly the values Mark restated on 2026-09-02: the reevaluation
audience, and "no pressure, just witness" — which includes witnessing to your
own limits.

### 6.3 Does it at least over-serve the academic?

Partly, and in the least useful way. It gives the academic the *apparatus* —
confidence words, lineage edges, ten-era survey counts, source-richness notes,
a longitude axis — while giving them **no search, no filters, no citations, no
bibliography, and 63% empty bands**. A genuine scholar wants `atlas-v3.html`,
which has search and all 292 movements; this page's honest role for them is a
signpost to it (eleven times over). So the direction pays the academic-facing
cost in register without collecting the academic-facing benefit. It is not that
it serves scholars instead of seekers. It serves *the idea of scholarship* — the
look of a research instrument — and neither audience fully.

### 6.4 The relationship grammar will misstate the record the first time it's stressed

This is a correctness defect, and it goes to "trustworthy (scholar)" directly.
`edgeRow()`:

```js
const verb = e.from===id
  ? (e.type==='contemporary with' ? 'Contemporary with'
    : e.type==='transmitted to'   ? 'Passed on to'
    : 'Formed')
  : (e.type==='contemporary with' ? 'Contemporary with'
    : e.type==='transmitted to'   ? 'Received from'
    : 'Formed by');
```

Everything that is not `contemporary with` or `transmitted to` falls through to
"Formed" / "Formed by." The census carries five edge types:

```
formed 32 · transmitted to 15 · argued against 10 · contemporary with 6 · in tension with 6
```

**Sixteen of sixty-nine census edges — 23% — would be printed as "Formed by."**
`Cappadocians —argued against→ Anomoean-Eunomian Christianity` renders as
"**Formed** Anomoean-Eunomian Christianity." An argument becomes a descent. And
`drawThreads()` has the matching gap: its type classes are only
`t-contemporary` and `t-lineage`, so an "argued against" edge is drawn as an
ordinary solid lineage curve, visually indistinguishable from "formed."

Today this is latent — all six edges among the seven live worlds are
formed/transmitted/contemporary, so nothing renders wrong. But the README says
the production build reads `world-census.json` live, and the direction's own
"What's next" plate names the two builds that come next. The moment the
adversarial edges are in scope, the map inverts relationships. On a page whose
second brand message is *"It shows its work,"* and whose author's proudest claim
is *"the map never draws a thread it can't defend,"* this is the worst available
class of bug.

It also undercuts the storytelling claim structurally. Brand message #1 is *"The
whole Church, in the open — many movements, one table, **real disagreement**."*
The shape this map can currently draw from seven early-church traditions is a
harmonious genealogical tree: one origin at the top, everything descending, no
conflict anywhere. The word "disagreement" does not appear on the page. The
direction claims the shape tells the four messages before a word is read; the
shape tells message #1 backwards, and the grammar to tell it correctly hasn't
been designed.

---

## Verdict

**Adversarial judgment, not a ruling. The author gets a defense.**

**The homepage thesis dies. The work does not.**

Almost everything in sections 1–4 is repairable in a day or two: one flex-wrap
fixes the 320px reflow; a dark-tint map fixes the eight contrast failures; a
`scroll` listener fixes the stranded popover; `pushState` fixes the Back button;
media-gating `trace()` fixes the phone dimming; deleting two legend rows fixes
the dead vocabulary; a rem bump fixes the 13px floor. If those were the whole
case, I'd say strengthen and keep.

They aren't. Three things are load-bearing and not patchable inside this
direction:

1. **The entry axis is wrong for the stated heart audience.** A map is indexed
   by *where* and *when*. Someone re-assessing their faith arrives with a *what*
   and a *why*. There is no coordinate on this page for "did God command
   genocide" or "was hell always taught this way," and no question-shaped door
   anywhere — while the constitution's own threshold makes "Start with your
   question" the first of three. Adding a search box or a "Start here" button
   doesn't fix this; it *contradicts* the direction, whose entire declared bet
   is "there is no hero, nothing says start." You cannot bolt a front door onto
   a thesis that is "the absence of a front door is the point."
2. **The direction is a better brief for `atlas-v3.html` than for a homepage,
   and it says so eleven times.** Eleven links to the real map, from a page
   whose claim is to *be* the map, is the artifact telling on itself.
3. **The composition inverts the project's own priority.** The only two buttons
   on the page ask for money; the only route to a Representative runs through
   JavaScript, three interactions deep; and the redesign deletes the one live
   sentence that says "anyone re-examining their faith" is wanted here. Nobody
   intended any of that. It is what the page does.

**What I would do with it instead, and I mean this as a real recommendation, not
a consolation:** reassign it. `atlas-v3.html` is an unpaid, named debt (D0 §2.C)
— off-palette, Georgia, 14px, its own token set — and this direction is the best
brief for repairing it that anyone is going to write. Almost every strength here
is an Atlas strength: the converged era grounds, the DOM-as-document law, the
per-stop accessible names, the deep-link-per-tradition, the confidence-in-words
lineage rows, the phone list form, the census `ground` seam, the
`--ink-faded-ground` token. Ship it as the Atlas, and let the homepage be
something that opens with a question.

**What would have to change for me to withdraw the verdict** (i.e. what a
defense would have to show, not merely assert):

- A **question-shaped door in the first viewport** that is not a map coordinate
  — and an argument for why that does not falsify the direction's own stated
  bet.
- The general `?mode=table` entrance restored, and the pilot / four-perspectives
  copy restored.
- The eleven outbound links to `atlas-v3.html` reduced to one, or the palette
  debt actually paid in D1 rather than promised for D3.
- The eight empty bands compressed to one honest line, not eight repetitions.
- The dimming of Representative portraits either removed or **put on the stretch
  list for Mark**, with the icon spec's "NO dimming of the others" quoted.
- The dark mode either removed (matching the constitution's deliberate deferral)
  or fully audited, including the seven tints and the invented `#E08C74`.
- The §5.2 fidelity claim withdrawn or corrected, so Mark rules on stretch #1
  knowing the grammar *has* changed — and knowing that `index.html`'s own
  2026-07-25 decision ("the Atlas is a supporting, secondary entry point… not
  embedded in the hero") is what he'd be reversing.

Even granting all of that, I think the direction would arrive somewhere close to
where a different direction starts. That is my honest read, and it is why I say
it dies rather than that it needs work. But I have been wrong about a thesis
before, and this one was executed with more care and more verifiable honesty
than most things I review. The author should get their defense on the record.
