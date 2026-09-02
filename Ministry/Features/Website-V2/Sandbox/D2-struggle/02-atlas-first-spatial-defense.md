# D2 Defense — Direction 02, Atlas-First Spatial

**Author:** the direction's D1 author (Fable). **Defending:**
`Sandbox/D1-directions/02-atlas-first-spatial/` (README.md, homepage.html,
journey.html) against `Sandbox/D2-struggle/02-atlas-first-spatial-review.md`.
**One defense, per the charter.** I read only my own three files, the review,
and the Decision-Log, plus the shared governing sources the review cites
(`cic-website/index.html`, `world-census.json`, the constitution, the icon
spec, the Logo Usage Sheet, the D0 note) — no other direction, no other review.

**Method, so the reviewer can check my work back.** Every measured finding
below was re-verified against my own markup by file and line, not accepted from
the review. Where the reviewer rendered, I re-rendered the two headline claims
in the same headless Chromium (`/opt/pw-browsers/chromium-1194`): at 320 / 360 /
375 px the document is 390 px wide, and "Read as a list" widens it to 394 px;
with JavaScript off, `#eras` has zero children, the strings "Interview" and
"Chloe" do not occur, and exactly two `.btn` elements exist, both Stripe. I
re-derived the worst dark-mode contrast by hand: `#7A2E2E` on `#1E1913` is
1.87:1 (the reviewer said 1.88). I counted the census edge types myself:
formed 32 · transmitted to 15 · argued against 10 · in tension with 6 ·
contemporary with 6 — 69 edges, 16 adversarial, 23%. The reviewer's numbers are
right everywhere I could test them, and I will not spend this defense
re-litigating any of them.

---

## 0. The verdict, answered first

**I concede the whole-site verdict.** "The map is the doorway" — the claim in
my own `<title>` (homepage.html:6) — dies. The reason I accept is the
reviewer's first structural charge, not the bug list: a canvas is indexed by
*where* and *when*, and the person Mark named as his heart arrives with a
*what* and a *why*. There is no coordinate on this page for "was hell always
taught this way." My README named "nothing says start" as the direction's
largest bet and said it should be tested with real first-time visitors rather
than argued (journey.html, risks §1). Mark's 2026-09-02 words are that test's
result, and the bet lost. I also withdraw my own framing of that risk — "the
visitor who wants to be told what to do." The reviewer is right that wanting
to know what a site is *for* is the median behaviour, not neediness.

**I contest one thing at the thesis level, because it decides what survives.**
The review says a front door "contradicts the direction, whose entire declared
bet is 'there is no hero, nothing says start.'" That is not where the bet was
declared. README §3 lists "The hero and CTA stack. Nothing says 'start'" under
*What it deliberately sacrifices* — a cost accepted, with the cost named ("If
the bet is wrong, it's wrong at the front door"). The bet itself is §1: *"a
spatial, chronological canvas tells this project's story … faster and more
truthfully than any paragraph, before the visitor has read a word."* That is a
claim about the **shape as a storyteller** and about **the map as a view of a
document** (§2, §6). It is not a claim that doorlessness is a virtue. My page
title over-claimed, and I own that; but the direction has two separable layers
— (a) the map as the doorway, (b) the map as a document whose shape tells the
story — and only (a) is falsified by Mark's ruling. The reviewer's own
reassignment proposal depends on this separability: you cannot carry the
DOM-as-document law to `atlas-v3.html` unless it is detachable from the
doorway claim. It is.

**So the ask is (b), not (a): the narrower survival the reviewer proposed —
accepted, with preconditions I specify in §3 — plus one smaller carry-forward
of my own that I think is stronger than it sounds.** Everything else in this
document is either a plain concession or a specific contest with evidence.

---

## 1. Conceded — verified against my own files

Each row: what the review found, where it is in my code, what my own README or
journey claimed, and the concession. Nothing here is argued.

| # | Finding | In my files | My claim it falsifies | Concession |
|---|---|---|---|---|
| 1 | **1.4.10 reflow fails at 320/360/375.** `.plate-title` is a nowrap flex row; the wordmark (97) and the nav items (110) are `white-space:nowrap`; nothing wraps. | homepage.html:96–111 | README §6: "1.4.10 reflow (no horizontal scroll at any width)"; journey.html Beat 7: "no horizontal scroll anywhere" | **Conceded.** I declared the floor and never measured at the floor's own width. Re-rendered: 390 px document at 320; 394 px in list view — so the toggle overflows even at 390, which the reviewer did not add and I do. |
| 2 | **Without JavaScript the document does not exist.** `<ol id="eras">` is empty in the static file (376) and built by `renderEras()` (1041); "Interview" lives only in `panelHtml()` (1252). | 376, 1041, 1252 | README §6 equivalence rule, in spirit (see §2.1 below for what I did and did not claim) | **Conceded as a regression** against the live `index.html`, which keeps a static `<h1>`, lede and a static Table link. A document manufactured at runtime is a weaker document than my own law wanted. |
| 3 | **World tints rendered as text.** `#panel .p-title{color:var(--tint-text,…)}` (244) and `panelHtml()` sets `--tint-text` to the raw tint (1245). Never redefined for dark; Marius 1.87:1. | 244, 1245 | README §4: tints "never as text on a ground"; README §5: "Tints as non-text rings clear 3:1 everywhere" | **Conceded — false in my own code, in both modes.** |
| 4 | **Dark mode shipped, unaudited, unflagged.** Eight invented dark tokens (74–82); `--gold-wash` (60) not overridden; `--action:#E08C74` brightens madder while the mark's seat correctly uses `#CB6E52` (118). | 60, 74–82, 118 | README §5's audit stops at light mode; constitution line 92: "Dark mode: deferred, stated plainly"; Logo Usage Sheet line 60: "madder never brightened" | **Conceded.** Remove dark mode from anything that carries forward until the seven tints have a dark register — which constitution §10.2 already owns and my README §5 deferred to it. |
| 5 | **Sub-13px meaning.** `.78rem` = 12.48 px on `#panel h3` (250), the confidence tag `.cw` (257), `.cta-label` (261), `.p-status` (247), `.stop__status` (203); `.8rem` = 12.8 px on `.g-s` (227) and `.stop--journey` (204); `.76rem` = 12.16 px on `.axis` (153). | as listed | README §4: "nothing under 13px carries meaning"; constitution line 105 | **Conceded, and the two worst places are the ones the reviewer named:** the confidence word — this project's "confidence in words" carrier — and the protected line "Come and join us at the Table." |
| 6 | **`edgeRow()` prints any edge that is not `contemporary with` / `transmitted to` as "Formed"/"Formed by"** (1235–1236); `drawThreads()` draws it as a lineage curve (1133). Census: 16 of 69 edges are `argued against` or `in tension with`. | 1133, 1235–1236 | journey.html Beat 2: "no relationship rendered the census doesn't carry"; panel copy: "the map never draws a thread it can't defend" (1264) | **Conceded as the worst available class of bug for this project.** Latent today only because the six embedded edges (808–851) happen to be lineage/contemporary. The moment a build reads the census live, an argument prints as a descent. This is precondition #1 for any reassignment (§3). |
| 7 | **2.4.8 Location, least met where it was adopted for.** Badge `display:none` below 640 (108); empty at first paint because the sample point at scrollY 0 falls inside `.thesis` (1330–1337, boot at 1341); sticky era heads made static in list view (284). | 108, 284, 1330–1341 | README §6 makes 2.4.8 binding via "the year badge, sticky era heads, and the region summary" | **Conceded.** Two of three mechanisms are absent exactly in the phone and list modes. |
| 8 | **Dimming Representatives.** `.atlas.is-tracing .stop:not(.is-hot) .stop__btn{opacity:.55}` (216); `trace()` (1146) is not media-gated while `drawThreads()` returns early below 900 (1111), so phones dim six portraits with no thread to explain it. | 216, 1111, 1146 | Icon spec lines 73–75: "NO dimming of the others … a dimmed or faded figure reads as a spirit" | **Conceded.** The spec's scope is the Table scene, but these are the same seven locked faces and the reason transfers. It should have been on the stretch list. The phone case is a plain bug. |
| 9 | **"The grammar inside the map is unchanged."** Constitution §5.2 (lines 392–403) specifies first-visit overlay, edges on demand, persistent tray; phone: search + two filter chips, accordion rows, tray. I kept hover→click and legend-as-thesis and dropped the rest. | README §7 stretch 1 | — | **Withdrawn.** The grammar is materially changed in six places. The reviewer is also right that I chose §2.4's tap grammar over §5.2's and should have said so rather than claimed fidelity. |
| 10 | **Stretch 1 argued against the app constitution and was silent about the site decision.** `cic-website/index.html:14–19`: "The Table (conversation program) is primary; the Atlas is a supporting, secondary entry point reachable from nav only, not embedded in the hero. Built one decision at a time with Mark." | README §7 stretch 1 | — | **Conceded.** Mark would have been reversing his own 2026-07-25 decision and I did not tell him so. I am no longer asking him to reverse it. |
| 11 | **The general Table entrance is gone.** Every app link is `?worlds=<id>&mode=…` (1242, 1252–1253). The live page's primary CTA is `?mode=table` with no tradition preselected (`index.html:228`). | 1242 | — | **Conceded — a hard regression I had not noticed.** |
| 12 | **The pilot copy is gone.** `index.html:172–173` names "anyone re-examining their faith" and the five-conversation ask. Neither survives in my homepage. | — | — | **Conceded.** The one live sentence that names Mark's heart audience was deleted by rebuilding around a different idea and not diffing the copy. |
| 13 | **No Representative in the heading outline.** Stops are `<button>` in `<li>` (1099–1100); only era titles are `<h2>` (1051). | 1051, 1099–1100 | README §2's accessibility case | **Conceded.** Heading navigation surfaces the apparatus and hides the product. |
| 14 | **`role="tooltip"` containing a `<button>`**, and on touch that button is the primary Level-3 route. | 413, 1163, 229 | journey.html Beat 3 | **Conceded.** Wrong ARIA construct on the only mobile path. |
| 15 | **Arrow/Home/End layer without composite semantics** — all stops independently tabbable, keys `preventDefault`ed. | 1219–1228 | README §2: "arrow keys walk the timeline" | **Conceded.** Drop it; nine stops do not need it. |
| 16 | **Popover stranded on scroll** (`position:fixed`, positioned once, no scroll listener); **Back exits the site** from a modal bottom sheet (`replaceState`, 1280); **list toggle misreports state at 641–900** (the ≤900 media query, 285–295, already removed the layer that `body.list-view`, 277–284, claims to toggle); **glimpse z-index 60 renders under the panel's 80** (221, 234) while `is-tracing` dims the open entry's own card. | as listed | journey.html Beats 4, 7, 8 | **All conceded.** Beat 8's "never history spam" was the Atlas's shareable-view discipline applied where a modal needs `pushState`. Beat 4's "the map stays live" is over the constitution's Cards ≤1 budget (line 541). |
| 17 | **Sticky era head at 86% alpha** (167) composites what scrolls beneath, breaking the 7:1 claim in the state it renders in. | 167 | README §6: 1.4.6 binding on era grounds | **Conceded.** Make it opaque; the blur was a nicety. |
| 18 | **Half the legend has no referent.** `ic-question` and `ic-door` (366–367) are used only in the legend; `stopHtml()` emits only house/plans (1085). | 363–368, 1085 | README §2: "the legend is the thesis" | **Conceded.** Dead vocabulary on first contact, and the Closed-door line denies a suspicion nobody raised. |
| 19 | **Eight identical bands, eleven links to `atlas-v3.html`** (heads 1055; bands 1060; edge plate 390; panel 1267). | as listed | README §3 | **Conceded on dose.** Eight repetitions of one sentence is a ledger, not a map, and a 2.4.4 nuisance. |
| 20 | **The only two `.btn` in the static DOM are Stripe** (403–404). | 403–404 | Brand: "the seeker's voice always outranks the donor's" | **Conceded as a composition consequence** — nobody meant it, and the page does it. |
| 21 | **"The Atlas palette debt — paid down."** `atlas-v3.html` was not touched. | README §5 | — | **Overclaimed; corrected.** True statement: the homepage converged onto the brand tokens and the math is done; the Atlas file itself is untouched. Under reassignment the debt is paid *by* the rework, which is the point. |
| 22 | **The stretch list pointed at the wrong things.** Two of three barely needed a ruling; dimming, dark mode and the site-level reversal did. | README §7 | — | **Conceded.** |

That is the whole measured case, and it stands. I add one item the reviewer
missed, in the same spirit: the list-view toggle overflows at 390 px too, so
there is no phone width at which the accessible fallback is narrower than the
page.

---

## 2. Contested — with evidence

### 2.1 What I claimed about JavaScript, and what I did not

The review's §1.1 is careful: it says my auditability test ("remove the CSS and
nothing is lost") is the *wrong* test. The Decision-Log's one-line summary is
not careful: "an accessible fallback that deletes all content without
JavaScript despite claiming otherwise." Those are two different things and the
second is not a claim I made.

README §6's equivalence rule is: "every fact conveyed by position, color, or a
drawn thread is stated in words in the DOM. Auditable — remove the CSS and
nothing is lost." At runtime that is true, and the reviewer's own §1.5 confirms
it (every stop's accessible name, every thread's confidence restated in
`edgeRow()`). "Read as a list" is a JavaScript feature — a toggle — and on a
≥900 px desktop it does what it says. Its real defects are items 1 and 16
above. Nowhere in README or journey does the direction claim to work without
JavaScript.

I am not contesting the *finding*. A document built by `renderEras()` is a
weaker document than the law wanted, the production build's `fetch` would make
it a network dependency too, and it is a regression against the live page's
static CTA. I concede all of that in item 2. I contest only the record, so that
the kill is for the right reason: the direction's accessibility architecture
is real at runtime and absent before it, which is a build-pipeline failure to
fix by rendering the census at build time — not a fallback that lied.

### 2.2 "A confessional picture of history presented as geometry"

The review's §5 closes with: the h1's capital-C "the Church," plus the shape
journey.html describes ("everything hangs from the wide house at the top"),
"makes the page read as a single genealogical tree descending from one origin
… a *confessional* picture of history rather than a neutral one, presented as
geometry rather than as claim."

Two checks against the files.

First, the shape is drawn from exactly two census edges: House-Churches
→formed→ Alexandria, *Widely Accepted*, and House-Churches →formed→ Syriac,
*Contested* (homepage.html:810–822). The contested one is dashed on the canvas
(`.c-contested`, 210), and the word "Contested" is printed in both entries it
joins. The map does not assert a single origin; it draws two edges the census
carries, with their confidence words attached, one of them explicitly
disputed. That is the opposite of presenting a claim as geometry — it is
presenting a claim *as a claim, with its confidence stated*, which is the whole
point of the confidence apparatus.

Second, "Twenty centuries of the Church. One table. A chair pulled out for
you." is the **protected hero hook** — one of D0's six protected lines (D0 note
lines 50–56: "the hero hook"), and journey.html Beat 1 names it as "the
protected hook." The capital C is not this direction's copy and is not
available to any direction to change.

What *is* fair in this section, and I conceded it in item 6: the shape
currently drawable from seven early traditions cannot show disagreement,
because the adversarial-edge grammar was never designed. So brand message #1
("real disagreement") is not told by the shape. That is an incompleteness in
the drawing grammar, not a confession smuggled in as geometry — and the fix is
the same one item 6 demands.

### 2.3 "A denominational vetting board" — mostly accepted, two things contested

**Accepted, and I take the reviewer's fix as written.** The Closed-door legend
entry on a page with no closed door is dead vocabulary that denies a suspicion
nobody raised — cut it until a closed-door entry is actually rendered. "Where
it stands on the Creed" as a mandatory `<h3>` above Lineage in every entry
(1262) makes the creed look like the sort key. My own thesis — shape speaks
before words — applied to my own panel says the heading does its damage before
the generous content is read. The reviewer's rename and its move below Sources
are right. I would go one step further: the fact that the project builds from
a Nicene base belongs stated *once*, plainly, in "How this was made" — because
the seeker Mark describes is exactly the person who will eventually ask "so who
decides who's in?", and hiding that a boundary exists would be less honest,
not more. It does not belong in a legend and it does not belong as a per-entry
scorecard.

**Contested (i): this is the Atlas's mechanism, so the reviewer's own survival
path carries it.** `floorNote` is a census field; the four-status legend is the
Atlas's legend; the entry template (about, voices, legacy, Creed, lineage,
visit, sources) is the Atlas's uniform template, inherited whole (journey.html
Beat 5). Reassigning this direction as the `atlas-v3.html` brief moves the
"vetting board" onto the Atlas unchanged. So this is not a homepage-versus-
Atlas distinction; it is a naming-and-placement fix that has to be made
wherever the grammar lives, and I specify it as a precondition of the
reassignment in §3 so it is not lost in the move.

**Contested (ii): "arguably worse for a deconstructing visitor than any
direction's incense" is the one claim in the review without a measurement.**
The reviewer measured pixels, ratios and scroll depths for everything else and
measured a reaction here. I do not say it is wrong; I say it is untested, and
that the reviewer's own concessions in the same section — the register is "the
safest of anything I can imagine here," the note content is "generous and
carefully non-judgmental" — cut against "worse than incense." The fix is cheap
enough that the strength of the claim does not matter for the outcome. It
matters only for how the direction's register is recorded going into Mark's
pick: on the reviewer's own evidence, this is the direction least likely to
feel like a church, with one inherited heading in the wrong place.

### 2.4 "Over-serves the academic" — the reviewer's own §6.3 says otherwise, and that decides what carries

The review's §6.3 finds the page gives the academic "the apparatus" without
the tools — no search, no filters, no bibliography — and concludes it serves
"the idea of scholarship" and neither audience. I accept the conclusion and
draw a different lesson from it. Confidence in words, "the map never draws a
thread it can't defend," plans shown as plans, "where the record is thin, we
let the silence stand" — these are not academic-facing. They are **witness**
mechanisms: the way a project earns trust from someone who has been burned by
confident answers, which is precisely the person Mark named. That does not
rescue the homepage — the entry axis is still wrong, and the reviewer's §6.1
stands. It decides what should survive the kill: the trust apparatus is for the
seeker, and it belongs wherever the seven houses are shown.

### 2.5 Context, not excuse

The Decision-Log records that Mark's heart-audience statement arrived after D1
was commissioned and was sent to the D2 reviewers, not the D1 authors. The
direction was built against the charter's four goals and named its bet in
those terms. That does not make the bet right; it makes the kill clean. The
direction did what a divergent phase asks — placed a real bet and named the
cost — and the cost came due.

---

## 3. What carries forward, exactly

Two carry-forwards. The first is the reviewer's proposal, accepted with
preconditions. The second is mine, smaller, and optional. If D3 has room for
only one, take the first.

### A. The `atlas-v3.html` rework brief — accepted

The constitution already expects this: §5.2, line 396 — *"When the map is next
edited it adopts the era-ground palette (§2.5c)."* This direction is that edit,
drawn. What carries:

- The converged palette: ten approved era grounds and the brand tokens
  (homepage.html:57–73), Alegreya throughout, Georgia gone.
- The **map-as-view-of-a-document law**, but built **static-first**: the ten
  eras and every stop rendered from the census at build time, so the document
  exists before any script runs (fixes item 2 at the root).
- Per-stop accessible names (1082–1084); an `<h3>` per stop wrapping the
  button so heading navigation reaches every Representative (fixes item 13).
- A deep link per tradition (1307–1309), with `pushState` where a modal is
  open (fixes item 16).
- Lineage rows in words with confidence tags (1233–1238) — at ≥13 px, and with
  the verb table completed for all five census edge types.
- The phone list form as §5.2 actually specifies it: search, era and status
  chips, accordion rows, tray — not my reduced version.
- `--ink-faded-ground` (`#4A433C`, ≥7.2:1 on all ten grounds) as a named
  token; the `world-census.json` `ground`/`groundDark` seam fixed. The
  reviewer credits both; they carry regardless.

Preconditions, in order, before the rework is called done:

1. **Design the adversarial-edge grammar first.** The Atlas carries all 69
   edges, 16 of them adversarial. `edgeRow()` and `drawThreads()` must handle
   "argued against" and "in tension with" as their own verbs and their own
   line treatment. Nothing else in the brief matters if an argument prints as
   a descent.
2. **No dimming of portraits.** Ring highlight only. If any dimming survives,
   it goes on Mark's stretch list with the icon spec quoted.
3. **No dark mode** until the seven tints have a dark register (constitution
   §10.2).
4. **"Where it stands on the Creed" renamed and moved below Sources; the
   Nicene-base statement said once in the method text; the Closed-door legend
   entry rendered only where a closed-door entry exists.**
5. Sticky era heads opaque; every sub-13 px size raised; the tooltip replaced
   with a non-modal dialog on touch; the arrow-key layer removed; the popover
   dismissed on scroll; the list toggle hidden below the width at which it
   can do anything.

### B. The seven-house map as the homepage's second plate — proposed, smaller

Not the doorway. Below whatever question-shaped first viewport wins, the
section the live site currently fills with a Representative carousel — "who
you can sit down with" — becomes Eras I–II of this map: seven houses, two
plans, six threads, the DOM-as-document law, deep links, lineage in words.
Eras III–X collapse to one honest sentence at the plate's edge with one link to
the full Atlas.

Why it is worth carrying instead of a carousel: it shows where, when and who
came from whom in one glance, which a carousel cannot; it is keyboard- and
AT-honest by construction; every stop is a place that can be sent. Why it does
not re-import the kill: the entry-axis problem is a first-viewport problem. A
browse surface reached *after* a question-shaped door is a second way in for
a visitor who has already been offered the first, and browse-by-where/when is
a fine second way. What I would cut from it: the west/east axis teaching, the
legend beyond House and Plans, the empty bands, the dimming. What I would keep:
the shape.

Honest caveat: B is untested and is my proposal. A is the safer reassignment.

### Two regressions that belong in every direction's D3 brief, not only mine

The general `?mode=table` entrance and the "anyone re-examining their faith"
sentence are the cheapest way any homepage serves the heart audience. My
mockup deleted both by accident. Whatever direction Mark picks, D3 should diff
its copy against the live page for exactly these two.

---

## 4. For Mark, in one paragraph

The map was the wrong front door and the right document. Everything the review
measured is real and is conceded above by file and line. The structural kill
stands: a where/when canvas cannot be the first thing a person with a hard
question meets, and I am no longer asking you to reverse your 2026-07-25
decision that the Atlas is not the hero. What the direction got right — the
map as a view of a document, confidence in words, plans shown as plans, a
sendable place for every tradition, the era-ground palette the constitution
already says the Atlas adopts next — should be reassigned to the Atlas rework,
with the adversarial-edge grammar designed first and the Creed heading moved
and renamed, and could also serve as the homepage's second plate under a
question-shaped door. Of my three stretches, only `--ink-faded-ground` still
needs your ruling; the other two were the wrong things to ask about.
