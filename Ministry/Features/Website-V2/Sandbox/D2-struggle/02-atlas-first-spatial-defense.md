# D2 Defense — Direction 02, Atlas-First Spatial

**Author:** the direction's author (Fable), D2 struggle phase. **Answering:**
`Sandbox/D2-struggle/02-atlas-first-spatial-review.md`, read in full. **Blind
to** the other four directions and their reviews, per the charter.

**Method note, so the reviewer and Mark can check my work in turn.** I did not
argue from memory. I re-rendered my own `homepage.html` in the same headless
Chromium build the reviewer used (`/opt/pw-browsers/chromium-1194`) at 320 /
360 / 375 / 390 / 800 / 1440 CSS px, with JavaScript off, and with touch
emulation on; I computed contrast from the file's own token values with the
WCAG relative-luminance formula; I counted census edges and statuses directly
from `cic-website/data/world-census.json`; and I opened every governing file
the reviewer quotes (`CiC_Full_UX_Design_V1_0.md`, the Brand Guidelines, the
Icon & Table Template Spec, the live `index.html`, `style.css`, and
`atlas-v3.html`) at the lines cited. Where my numbers match the reviewer's I
say so and move on. Where they differ, or where a quoted rule turns out to
govern something other than what it was applied to, I say that too.

**The short version.** The measured bugs are real — every one I could
reproduce, I reproduced, and I found two more the reviewer did not. Five of
the reviewer's charges are wrong or materially overstated, and I show which,
against the source files. On the structural verdict I concede: the whole-site
homepage thesis dies, and not because of the bugs. I name exactly what
carries forward — the reviewer's own proposal, accepted and sharpened into a
brief, plus one narrow homepage component and six cross-cutting findings —
and I argue one point about the reevaluation audience where I think the
reviewer is wrong and it matters enough to put to Mark.

---

## 1. Conceded — measured, reproduced, no argument

I am not going to re-litigate what I could measure. The table is what I got in
my own render; the reviewer's figures are in the review and they agree.

| Claim (review §) | My reproduction | Standing |
|---|---|---|
| 1.4.10 reflow fails at 320/360/375 (§1.3) | `scrollWidth` 390 at all three → 70 / 30 / 15 px overflow. Cause as stated: `.plate-title` nowrap flex. | **Conceded.** README §6 claimed it "held"; it was never measured at the criterion's own width. |
| "Read as a list" makes it worse (§1.3) | 394 px after toggle at 320, 360, 375 — **and at 390**, which the reviewer did not note. Second cause, which the reviewer did not isolate: `body.list-view .stops{grid-template-columns:repeat(auto-fill,minmax(19rem,1fr))}` outranks the ≤640px `.stops{grid-template-columns:1fr}` on specificity, so the accessible fallback forces a 304 px minimum column on every phone. | **Conceded**, and worse than reported. |
| No JavaScript = no content (§1.1) | `#eras` has 0 children; none of the seven names, nor the string "Interview", appears in `body.innerText`. | **Conceded.** The equivalence rule ("remove the CSS and nothing is lost") tested the wrong axis. Regression against live `index.html`, whose primary CTA is static markup upgraded by script. |
| Year badge empty at first paint; hidden ≤640; list view unsticks era heads (§1.4) | `badge === ''` at every width after load; `#yearBadge{display:none}` at ≤640 (line 108); `body.list-view .erahead{position:static}` (line 284). | **Conceded.** One qualification below in §2, but the AAA criterion I made binding is least met in the mode built for its audience. |
| Toggle misreports state at 641–900 px (§4.5) | At 800: label "Show the map", `aria-pressed="true"`, threads 0, axis hidden — the 900 px media query wins regardless. | **Conceded.** A control lying to assistive tech, in the direction's accessibility door. |
| Sub-13px on meaning-carrying text (§2.4) | Seven selectors at .76–.8rem = 12.16–12.8 px at the 16 px root, including `.cta-label` ("Come and join us at the Table") and `.cw` (the confidence word). | **Conceded.** My own README §4 rule, broken in my own file, on the two worst places to break it. |
| Sticky era head at 86% opacity breaks the 7:1 claim (§2.4) | `background:color-mix(in srgb,var(--eg) 86%,transparent)` (line 167). | **Conceded.** Not measurable in the state it renders in; fix is an opaque ground. |
| Phone dims with no threads to explain it (§2.1b) | Touch tap on Alexandria at 390: 5 cards at 55%, 0 thread paths (the reviewer's 6 came from a stop with fewer relations; both are right). | **Conceded.** `trace()` is not media-gated. |
| Popover strands on scroll (§4.4) | Glimpse top 188 px before and after a 700 px scroll; `hidden === false`. | **Conceded.** `position:fixed`, never re-positioned, never hidden on scroll. |
| Back exits the site from a modal sheet (§4.4) | `history.replaceState` only (line 1280); no `popstate` handler. | **Conceded.** I chose `replaceState` for the Atlas's "never history spam" discipline and got the wrong half of it. |
| `role="tooltip"` containing the mobile Level-3 button (§4.3) | `glimpseHtml()` emits `<button class="g-full">`; `@media (hover:none)` shows it. | **Conceded.** Wrong construct on the only mobile path. |
| Arrow/Home/End layer on non-composite buttons (§4.3) | Lines 1219–1228; no roving `tabindex`, no composite role. | **Conceded.** At best neutral; sold as a feature. |
| Panel open + hover = three states, glimpse behind panel, subject dimmed (§4.6) | z-index 60 vs 80; `trace()` not suppressed while panel open. | **Conceded.** Over the five-count budget (§8 "Cards ≤1", constitution line 541). |
| Two legend symbols with no referent on the page (§3) | `stopHtml()` emits only `ic-house` / `ic-plans` (line 1085). | **Conceded.** |
| Eight empty bands, 63% of the phone atlas region; eleven links to `atlas-v3.html` (§3, §4.4) | Structural; counted. | **Conceded** on dose and count. |
| The only `.btn`-styled elements in static markup are two donation asks (§1.2) | Two `btn secondary` Stripe links at lines 403–404; the `btn primary` lives in `panelHtml()`. | **Conceded.** A composition consequence, and exactly the kind nobody notices until it ships. |
| The most CTA-shaped thing above the fold is the list escape hatch (§3) | The `.silence` button is the only madder-underlined string in the first viewport. | **Conceded.** I placed the accessibility door where the pitch should be. |
| General `?mode=table` entrance removed (§4.2) | Grep: the only `mode=table` is per-tradition inside `panelHtml()`. Live `index.html` line 228 has the general one. | **Conceded. Hard regression.** |
| Pilot / four-perspectives / five-conversations copy deleted (§6.2) | Grep for "re-examining", "five conversations": zero hits; "pilot" only in the footer link. Live lines 172–173 carry both. | **Conceded, with no defense.** The one live sentence naming Mark's heart audience is gone from the page and I did not notice. |
| "Paid down" the palette debt (§3) | README §5 says paid; the same paragraph defers application to D3. | **Conceded.** Designed, not applied. |
| "The grammar inside the map is unchanged" (§2.2) | Constitution §5.2 (lines 393–400) lists first-visit overlay, hover card → click panel, edges on demand, persistent tray, legend-as-thesis; phone: search + two filter chips, accordion rows, persistent tray. I kept two of five and none of the phone furniture. | **Withdrawn.** What I meant — the §2.4 disclosure grammar (hover = short, click = full, Level-3 alongside) — is unchanged; the §5.2 furniture is not, in six places. Mark should rule on stretch #1 with the six named. |
| The 2026-07-25 `index.html` decision belongs in stretch #1 (§2.3) | Lines 15–18, verbatim: "the Atlas is a supporting, secondary entry point reachable from nav only, not embedded in the hero." | **Conceded.** Stretch #1 argued against the app constitution, which does not govern here, and was silent about the site decision, which does. Mark would be reversing something; he should be told so. |

**The `edgeRow()` fallthrough (§6.4) — conceded, and sharpened against me.**
The reviewer's census count is exact: 32 formed · 15 transmitted to · 10
argued against · 6 contemporary with · 6 in tension with. Sixteen of
sixty-nine edges (23%) fall through to "Formed / Formed by," and
`drawThreads()` draws them as lineage. Two things the review did not say. The
first makes it worse: the live Atlas *already carries the grammar I dropped* —
`atlas-v3.html` line 1654 `const tension=edges.filter(e=>e.type==="in tension
with"||e.type==="argued against")`, rendered at line 1686 as "Traditions it
stood in tension with." I was converging from that file and lost a category it
had. The second corrects the timeline: Donatism has **no** census edges at all,
and Latin Pastoral's two are `transmitted to` and `contemporary with` — so the
next two builds do not trigger the bug. It bites the first time a built world
has an adversarial edge to another built world. Latent longer than the review
implies; still a bug that must not ship on a page whose second message is "it
shows its work."

---

## 2. Contested — with the source files open

Five charges are wrong or materially overstated. None of them rescues the
homepage; all of them matter for what Mark is told he is ruling on.

### 2.1 Dark mode is not "invented" and the constitution's deferral does not govern this surface

The review (§2.1c): *"It ships a full dark mode. The constitution deliberately
does not have one."* The quoted rule — Full UX Design §2.1, lines 92–94 —
reads in full: *"Dark mode: deferred, stated plainly. The parchment ground is
the brand. The map/tour 'old leather' dark register exists as precedent (and
the icons ship dark variants, §2.5); nothing here blocks a dark app variant and
nothing ships one now."* That governs the **app** (D0 seam 4: the constitution
governs `cic-poc/frontend`, not `cic-website/` — the review itself relies on
that scoping in §2.3). The live **website** ships dark mode today:
`index.html` lines 48, 81, 96; `style.css` lines 336–354; `atlas-v3.html`
line 60 — all `@media (prefers-color-scheme: dark)`. The D0 note's warning
about "two real dark-mode contrast bugs caught and fixed after the fact" is a
warning about a dark mode that exists. A direction that removed it would be
the deviation.

What stands from §2.1c: the seven tints are never redefined for dark, and my
audit stopped at light. My own numbers on `#1E1913`: Marius 1.88, Albina 2.21,
Theon 2.58, plans-grey 2.93 — four of eight under 3:1 even as rings; all seven
under 4.5 as text. `--gold-wash` and the primary button's boundary (2.69:1)
also lack dark values. **Conceded** as a failure; **contested** as a novelty.

### 2.2 `#E08C74` is the live site's own dark madder, not mine

The review: *"The direction uses `#CB6E52` correctly for the mark's dot and
then invents `--action:#E08C74` / `--action-hover:#F0A98F`… Two brightened
madders, in the same file as the correct one, unflagged."* `cic-website/
assets/style.css`, lines 343–348, inside the dark block:

```
/* --madder/--gold-leaf stay unchanged (button fills need the darker value for
   contrast against light text) - these overrides lighten the SAME hues only
   where they're used as text/border color on the near-black background. */
a, .hero .eyebrow, .page-section .eyebrow, .btn.secondary,
ol.convictions li::before, .world-card .name { color: #E08C74; }
a:hover { color: #F0A98F; }
```

Those are my two values, verbatim, with the live site's own rationale. And
"madder never brightened" (Brand Guidelines line 143) sits in the **mark's**
never-list — between "the opening never narrowed, closed, or pointed anywhere
but right" and "never on photography without a parchment or ink plate" — which
is exactly why the seat dot is `#CB6E52` and nothing else is. The direction
inherited the site's dark accent and honored the mark's rule.

The reviewer's underlying observation is still worth carrying: `#CB6E52`
clears AA as text on every dark ground I ship (5.18 on `#17130F`, 4.89 on
`#1E1913`, 4.80 on the Era I dark ground), so the site *could* retire
`#E08C74` and use the sanctioned register for links too. That is a site-wide
question for Mark, surfaced by this review. It is not a charge against this
direction.

### 2.3 Tint-as-text passes AA in light mode; the README sentence was sloppy, not false

The review: *"all seven fail AA… This also directly falsifies README §4's
promise: 'world tints appear only as rings, left-rules, portrait borders —
never as text on a ground.'"* The `.p-title` line renders the tint as text on
the panel's vellum **surface** (`#FEFCF8`), not on an era ground. Measured
there: Mar Yausep 4.90 (worst), Papnoute 5.34, Chilo 5.48, Chloe 5.56, Theon
6.60, Albina 7.69, Marius 9.08 — all seven clear 4.5:1 in light mode. The
failures are dark-mode only, and there they are severe. The honest correction
to §4 is: *tint is used as text in one place; it clears AA on vellum in light;
it was never measured in dark, where it fails.* "All seven fail" is true of
dark and false of light, and the review does not distinguish.

### 2.4 The dimming is not a silent break of a rule that governs this surface — but it belongs on the stretch list, with a stronger rule than the reviewer asked for

The review quotes the Icon & Table Template Spec §1a: *"NO dimming of the
others — every figure stays fully solid and present the entire time (a dimmed
or faded figure reads as a spirit)."* The subject of that section (lines
68–76) is the Living Table scene's speaker cue — the nameplate inversion — and
the rule is that *no other cue* marks the speaker. On the map surface, the
precedent runs the other way: `atlas-v3.html` line 224, `body.tracing
.node:not(.hot){opacity:.18}` — the live Atlas ghosts every non-traced node,
portraits included, to **18%**. I raised that to 55% because the portraits are
on this map. The review calls that "choosing a value against a readability
constraint" and never checking the rule; the record shows a surface where the
rule was never applied at all.

The reviewer is right about the thing that matters, though: the rule's
*reason* transfers to the seven locked portraits exactly, and I should have
flagged it as a ruling rather than tuned it. So I go further than the review
asks. The rule I would put to Mark: **a Representative's portrait is never
dimmed, on any surface** — the trace steps back the card ground and the
threads only; the face stays at 100%. That rule indicts atlas-v3's 18% today
as much as my 55%, and it belongs in whatever survives.

### 2.5 The Creed heading and the Closed-door legend are the live Atlas's; what is mine is their placement

The review (§5) treats both as this direction's mechanism. `atlas-v3.html`
line 1683: `<h4>Where it stands on the Creed</h4>` — same heading, same
`floorNote` field. Line 541: the Closed-door sentence, word for word. All 292
census entries carry a `floorNote`; four carry the status `Excluded —
Doctrinal Floor (C1)` and twenty-eight `Floor Question (register)` — closed
doors and open questions exist in the record, just not among my nine. The
mechanism exists because the project's selection criterion exists and is
disclosed.

What *is* mine, and wrong: (1) I promoted the four-symbol key from a
**collapsed `<details>` in the Atlas's footer** — where, per the comment at
lines 525–530, Mark himself moved it back on 2026-08-05 because the one-line
orientation above the fold was enough — to the first viewport, as the thesis;
(2) I placed the Creed section one notch higher than the Atlas does (above
Visit, where the Atlas has it after). Both concessions are in §3, where the
argument about the audience belongs.

### 2.6 One qualification on Location (§1.4)

On the phone form the sticky era head *is* the location cue; the badge would
duplicate it in a 56 px plate that cannot hold it, which is why it is hidden
there. That is a defensible design and the README should have said so. It
does not rescue the finding: list view removes the sticky head too, and the
badge is empty at first paint everywhere. Conceded on the substance.

---

## 3. Religious feel and the heart audience — where I agree, and where I don't

**Where I agree.** The reviewer's shape test is fair and I accept it against
my own thesis. A first-viewport legend whose heaviest item describes
exclusion, for a symbol that is not on the page, is "denying a suspicion
nobody raised — say what it is, once, and stop" (Brand Guidelines line 72),
which is on the brand's own never-list. The legend must teach only what is on
screen; the Closed-door row returns when a closed door does. And "once, and
stop" is violated a second way: the legend says it once, and then every panel
says it again, above Lineage and Sources. Placement conceded: the Creed note
goes below Sources, as the last thing an entry says, not the governing schema
of the first screen.

**Where I disagree, and think it matters enough to put to Mark.** The
mechanism itself is not a vetting board, and euphemizing or removing it would
be worse for exactly the person Mark named. The reevaluation visitor's most
*founded* fear of a religious site is not doctrine; it is undisclosed
gatekeeping — warmth at the door, a line discovered later. This project has a
line (the Nicene base), and the mechanism says so, states the grounds, and says
in the same breath that exclusion is never a judgment of unimportance. That is
what "witness, not recruitment" looks like structurally: say what you are. The
reviewer's suggested rename — "Where it sits in the historical Christian
mainstream" — is the euphemism: "mainstream" is a normative claim dressed as a
neutral one, and it is the opposite of "it shows its work." The heading should
stay what the Atlas calls it, and the content — which the reviewer credits,
rightly: "the hard questions here are about power, not about doctrine" is
precisely what a deconstructing reader needs a church-history site to admit —
should stay. The fix is dose and position, not deletion.

This is a real disagreement between the review and the defense, and neither
the shape test nor this argument settles it. It is Mark's audience and his
call: *does the honest line, stated once and late, read to that visitor as a
vetting board, or as the absence of a trap?* I think the latter. It should be
tested with the people it is for.

**"The Church, capital C."** The h1 is the protected hook, verbatim — Brand
Guidelines line 61, live `index.html` line 159. Not this direction's to
change. (For the record: the constitution's S0 at line 373 quotes the same
line with a lowercase "church." That is a drift in the record, noted for D3.)

---

## 4. The structural verdict, answered directly

The kill, in the reviewer's words: a map is indexed by *where* and *when*;
Mark's heart audience arrives with a *what* and a *why*; and "you cannot bolt
a front door onto a thesis that is 'the absence of a front door is the
point.'"

Two corrections, then the concession.

**Correction one: the thesis was never "no door."** The file's title is *the
map is the doorway*. What README §3 sacrificed was the hero and the CTA
*stack* — not a door. A single quiet general entrance in the thesis plate —
"Or bring your question straight to the Table →", the live site's own
`?mode=table` — is not a hero, does not contradict the bet, and should never
have been removed. So "adding a door contradicts the direction" is not quite
right. One door is compatible with this direction.

**Correction two: the deconstructor's question is more historical than the
review allows.** "Was hell always taught this way." "Did the church always
treat women like this." "Was it always like this." The operative word is
*always*, and "always" is a claim about time. The map's answer to "always" is
its whole vertical axis: there was no always; the Church has been two hundred
and ninety-two things; three of the seven people at this table are women of
the first four centuries, and the page shows that by portrait before a word
is read. That is a real answer, by shape, and it is the answer the
reevaluation visitor least expects a religious site to give. I do not think
"there is no coordinate on this map for a single one of those" is right. There
is one coordinate for all of them, and it is the one that runs downward.

**The concession.** It is the answer to the *background* question, not the
*foreground* one. The person Mark named arrives with a specific what and why,
often in pain, and needs a fast, personal way to ask it. The map cannot lead
with that. Anything that leads with it makes the map the second thing on the
page — and a map that is the second thing on the page is exactly what README
§1 rejected in its first sentence: "not a map on the homepage." I can restore
a door. I cannot make the map *lead* with a question and still be this
direction. The reviewer is right that the repaired version "arrives somewhere
close to where a different direction starts," and the Decision Log's
cross-review finding — that a direction which leads with anything other than
a clear, fast, personal way to ask a hard question fails the heart audience —
is the same conclusion from three independent angles.

**The whole-site homepage thesis dies.** Not because the reviewer measured
well, though the reviewer did; every measured bug above is patchable inside
the direction. It dies because Mark's 2026-09-02 statement is the tiebreaker,
and a map is the wrong-shaped keyhole for the person he named. I would rather
say that plainly than defend a front door I now believe opens onto the wrong
room.

---

## 5. What survives, named exactly

Two things, in priority order, and six findings that carry regardless.

### 5.1 The `atlas-v3.html` rework brief — the reviewer's proposal, accepted and sharpened

The reviewer offered this as "a real recommendation, not a consolation." I
take it as one, and I add the specifics that turn it from a reassignment into
a brief. Ship on the Atlas:

- **The converged token block.** Chrome on the brand tokens; era bands on the
  ten approved grounds (`#EFDDB3`→`#DEE7EC`, dark `#241A0C`→`#141A20`);
  Alegreya throughout; `--ink-faded-ground:#4A433C` (≥7.2:1 on all ten light
  grounds) with dark `#B8AEA1` (≥7.8). Retires `--bg:#f3ecdc / --gold:#83662a
  / --ink:#3a3020 / Georgia 14px`. The palette debt is paid where it lives.
- **The DOM-as-document law, corrected by this review.** The document must
  exist *without* script: prerender the era/stop list from the census at
  build time; script upgrades it. "Remove the CSS and nothing is lost" and
  "remove the JavaScript and nothing is lost" are both the test.
- **Per-stop accessible names**, kept as built — the part the reviewer
  called "the hard part, and they were done." Plus: each stop's name as a
  heading under its era's heading, so heading-navigation surfaces the seven
  people, not only the apparatus.
- **Deep link per tradition**, with `pushState` on open and `popstate` to
  close, so Back closes the sheet instead of leaving the site.
- **Lineage in words with all five census types.** Keep the Atlas's own
  four-heading split — shaped it / it shaped / stood in tension with /
  contemporaries — never the two-verb collapse. Draw tension and
  argued-against edges in a third stroke so brand message #1's "real
  disagreement" is drawable, which today it is not, on either page.
- **The portrait rule**: never dim a Representative's portrait; the trace
  steps back card ground and threads only. Put to Mark, because it also
  changes atlas-v3's current 18%.
- **The phone form as the list**, with the list/map toggle hidden below 900
  px where the list is the only form.
- **Level-2 on touch** as a non-modal popover region with a real "Full
  entry" control — not `role="tooltip"` with a button inside it.
- **The 13 px floor honored in the panel**: the confidence word and the
  protected CTA label at ≥13 px.
- **Opaque sticky era heads**, so 7:1 is measurable in the state it renders.
- **The Creed note kept — heading, content — and moved below Sources; the
  icon key teaches what is on screen.** The audience question in §3 goes to
  Mark alongside.
- **Eleven outbound links become zero**, because on the real map there is
  nothing to link out to.

### 5.2 One narrow homepage component: the built-map band

Not the direction — a section. Eras I–II only: the seven houses, the two
plans, the six census edges, on the two approved grounds, deep-linkable,
DOM-as-document, threads in words. Its job on a homepage is to be the answer
to the one question the heart audience actually brings — *was it always like
this?* — and it belongs **under** whatever question-shaped first screen D3
builds, never above it. What earns it a place: it is the only artifact in D1
that shows "many movements, one table" by shape in a single viewport, with the
accessible mechanics already built. What it must shed to earn it: the eight
empty bands (one honest line — "Eras III–X: 249 traditions on record, none
built yet" — or nothing), the legend-as-thesis, and the axis-instruction
paragraph. I name this as a component available to D3, not as a claim that
this direction survives as a direction.

### 5.3 Cross-cutting findings to carry whichever direction wins

The reviewer already carried two (the census `ground`/`groundDark` seam and
the `--ink-faded-ground` token). This exchange adds:

1. **Dark-mode audit of the seven tints as graphics and text.** Four of eight
   fail 3:1 as rings on `#1E1913`; all seven fail 4.5:1 as text. The site
   needs either a dark tint map in the census or a rule that tints are never
   text in dark. `--gold-wash` and the primary button's 2.69:1 boundary need
   dark values on every page that uses them.
2. **The site's dark madder.** The live site uses `#E08C74` / `#F0A98F`
   (`style.css` 346–348); the brand's sanctioned dark register `#CB6E52`
   clears AA as text on every dark ground shipped. Whether the site should
   adopt the sanctioned value site-wide is a question for Mark, surfaced by
   this review.
3. **The portrait-dimming rule** (§2.4 above) — atlas-v3 ghosts portraits to
   18% today.
4. **The `edgeRow()` lesson as a build rule**: any page that renders census
   edges must handle all five types or refuse to render the edge. Atlas-v3
   does; the homepage carousel and this mockup did not.
5. **The protected hook's capitalization drift** between the Brand
   Guidelines / live h1 ("Church") and constitution S0 line 373 ("church").
6. **The legend/Creed placement question for the reevaluation audience** —
   a genuine open question, not settled by the review or this defense, and
   worth a real test with real visitors.

---

## 6. The reviewer's withdrawal conditions, answered one by one

| Condition | Answer |
|---|---|
| A question-shaped door in the first viewport, and why it doesn't falsify the bet | One quiet general door is compatible with the bet (§4, correction one). A door that *leads* is not, and that is the one the heart audience needs. Conceded — this is why the homepage dies. |
| `?mode=table` restored; pilot / four-perspectives copy restored | Yes, and in any survivor. No defense was offered for their removal because none exists. |
| Eleven links to one, or the debt paid in D1 | On the Atlas, zero; the debt is paid where it lives (§5.1). |
| Eight bands to one line | Yes (§5.2). |
| Dimming on the stretch list with the icon spec quoted | Yes — with a stronger rule than asked, and applied to atlas-v3's 18% too (§2.4). |
| Dark mode removed or fully audited | Audited, not removed — removal would be the deviation from the live site (§2.1). Tint audit numbers are in §2.1 and §5.3. |
| §5.2 fidelity claim withdrawn; the 2026-07-25 decision cited | Withdrawn; cited (§1, last two rows). |

*"Even granting all of that, I think the direction would arrive somewhere
close to where a different direction starts."* Agreed.

---

## 7. What I got wrong as an author, said once

The README declared a floor and never measured it at the floor's width;
claimed a fidelity to §5.2 it did not have; called a debt paid that was only
designed; wrote "never as text" about a thing that is text; dropped a lineage
category the file I was converging from already carried; and removed the one
live sentence that names Mark's heart audience without diffing the copy. The
work that was done well — and the reviewer named it: the data fidelity, the
accessible names, the confidence-in-words rows, the deep links, the token
math — was done well at the level of a map. The failure was at the level of
the door. That is the right thing to have learned in D2, and the map should
go back to being what it is good at being.
