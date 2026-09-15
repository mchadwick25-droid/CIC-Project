# D2 adversarial review — Direction 03, Institutional-Professional / Scholarly Authority

**Sandbox artifact. Adversarial by assignment. Not a ruling. 2026-09-02.**

Reviewer: Opus, D2 struggle phase. I read `03-institutional-professional/` only —
`README.md`, `homepage.html`, `tradition.html`, each in full. I did not open any
other D1 direction folder. I glanced at the head of
`05-product-led-clarity-review.md` for file conventions after forming my own
findings; nothing in it informed the judgments below, which are about a completely
different direction.

My job is to try to kill this direction. Where an attack misses, I say so — an
attack that misses makes the ones that land easier to dismiss, and this direction
has real things going for it that deserve to be named accurately before they are
weighed against what is wrong.

**The author gets one defense before anything is decided. This is a prosecution
brief, not a verdict of the workstream.**

---

## Method note — the browser work is real, and so is the record-checking

Chromium (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`) driven by Playwright
with an explicit `executable_path`. Both files rendered at 1440×900, 1280×800,
1100, 1024, 820×1180 and 390×844, in `prefers-color-scheme: light` and `dark`.
Scroll depths, element geometry, sticky-overlap collisions, nav clipping, computed
font sizes and tab order were measured in the live DOM, not inferred from CSS.
Every contrast figure in README §5 was independently re-derived from the WCAG
relative-luminance formula. Every census string in the register was diffed against
`cic-website/data/world-census.json`. The Cappadocian admission claims were checked
against `worlds/cappadocian/CAPPADOCIAN_BUILD_LEDGER.md`. Anything below
labelled "measured" is measured.

---

## The short version — what I think actually kills, and what does not

**Load-bearing, in descending order:**

1. **The premise is aimed at the wrong person.** Mark, 2026-09-02, verbatim: *"my
   heart is those seeking answers to hard questions of faith, not accademics."*
   This direction's own first sentence: *"The site is a scholarly instrument, and it
   says so at first glance."* That is not a tension to be managed by warmth moves.
   It is the direction's spine pointed at the audience Mark explicitly deprioritised.
   Section 6.
2. **The flagship section is visually broken at ordinary desktop widths.** Measured
   at 1280 and 1440: the sticky marginal column slides down and lands *on top of*
   the register table — a 208 × 328px collision of overlapping, unreadable text,
   for the entire scroll through the seven traditions. On the one direction whose
   sole differentiator is "professional on sight." Section 4.1.
3. **"Jesus" appears once on the homepage, in the copyright line.** Meanwhile
   "Ante-Nicene," "Constantinian/Nicene," "ekklesia," "Gravity Discovery,"
   "Ecological Reconstruction" and "Dominant Modern Reconstruction" all appear
   above it. The direction stripped the warm, universally legible word and kept the
   seminary vocabulary. That is the wrong trade in both directions Mark named.
   Sections 1.3 and 5.
4. **On a phone, the traditions are 7.4 screens down, and their entry points are
   850px off-screen inside a nested scroller with no scrollbar.** The direction's
   "easy access to features — solved structurally" argument is desktop-only.
   Section 4.2.
5. **The two inverted voice pairs cannot take shelter under the marketing-site
   exemption.** The S0 exemption is real and I concede it. The Brand Guidelines are
   not app-scoped, and the direction's §6 quietly bundles all three asks as if they
   were one kind of ask. Section 2.
6. **The page's own stated rules are broken in its own CSS.** "Nothing under 13px
   carries meaning" — measured, eight distinct meaning-bearing styles run 11.5–12.8px,
   including every column header of the catalogue. "Every register action names the
   Representative" (its claimed AAA 2.4.9) — seven identical `Read the record →`
   links. "Gold never sets small text" — `.plate .rep .role` is gold at 11.5px.
   Section 3.2.

**Attacks I tried and dropped, stated so they are not re-run:** the contrast math is
correct (I re-derived all of it, to two decimals); the census strings are genuinely
verbatim, including the stale one it flagged rather than silently fixed; the
`259 records / 28-of-28` claims check out against the build ledger; the hero *is*
door-first, more so than the README admits; and `tradition.html` is a genuinely
excellent artifact that I think should survive this direction's death.

---

## 1. Charter-goal failures

The charter asks for "growth, accessibility, clear storytelling, easy feature access,
and professional top-tier design," and behind it the heart goal: draw visitors into
"the fascinating and life-changing journey of the church and how Jesus is faithful
to us."

### 1.1 It answers a question nobody has asked yet, at the cost of the one they came with

A first-time visitor arrives with one question: **what is this, and is it for me?**
A much smaller number of visitors, later, arrive with a second: **can I trust this?**

Direction 03 sequences the page for the second visitor. Measured order of what a
1440×900 desktop visitor scrolls past:

| Landmark | Desktop offset | Screens | Phone offset (390×844) | Screens |
|---|---|---|---|---|
| Hero CTA "Come and join us at the Table" | 780 | 0.9 | 799 | 0.9 |
| § 1 The ten-step method | 884 | 1.0 | 1,821 | 2.2 |
| § 2 The confidence scale legend | 2,238 | 2.5 | 4,785 | 5.7 |
| **§ 3 The register — the seven traditions** | **3,079** | **3.4** | **6,350** | **7.5** |
| First tradition's name | 3,598 | 4.0 | 6,742 | 8.0 |
| § 4 The AI question | 4,859 | 5.4 | 8,519 | 10.1 |
| Closing Table CTA | 6,277 | 7.0 | 10,770 | 12.8 |
| Page end | 7,284 | 8.1 | 12,251 | 14.5 |

(Subtract ~61px desktop / ~130px phone for the sandbox banner, which would not
ship. It does not change the shape.)

**Seven and a half phone screens to reach the list of who you can actually talk
to.** The ten-step method grid alone, stacked one card per row on phone, is 3.5
screens of internal project jargon. This is not a subtle mis-weighting; it is the
whole page.

### 1.2 It never shows the product

This is the failure I find hardest to argue around. The homepage explains, at 508
words, exactly how a tradition is manufactured. It explains, at 265 words, the
five-level vocabulary a claim will carry. It explains, at 296 words, what constrains
the AI. It nowhere shows **what a conversation is.** There is no sample question, no
sample turn, no image of the Table, no line of Chloe's actually spoken to a
visitor — the only demonstration of the disclosure grammar is a static paragraph
that *describes* a hover behaviour the page does not perform (both files contain
zero `<script>` tags; measured).

Word budget, measured from the rendered page (excluding the sandbox banner):

| What the words are about | Words |
|---|---|
| CiC's own method, apparatus, status and review posture (status band, frontispiece, §§1, 2, 4, 5) | **1,352** |
| The seven traditions themselves (§3, and much of that is column labels, identifiers, action links and four register-notes about census bugs) | **585** |
| Hero + closing CTA + Get Involved + colophon | 357 |

A homepage for a project about twenty centuries of the Church spends 2.3× more words
on how the sausage is made than on the sausage, and zero on what eating it is like.
"The fascinating and life-changing journey of the church" is not on this page. The
factory tour is.

The direction anticipates this in README §2 and answers: *"the story is the brand's
fourth message, the build is the product."* That is a real argument, and it is
wrong about the ordering. The Brand Guidelines list four messages **in order**. "The
build is the product" is the *fourth*. "The whole Church, in the open" is the first.
This homepage promotes message four to the top of the page and leaves message one
to a table.

### 1.3 The one word that carries the heart goal is in the copyright line

Measured, both files: the string "Jesus" occurs exactly once per page, in the
footer's inherited boilerplate — *"A safe space to explore faith and the story of
Jesus, part of Faithways Studio, Inc."* It appears nowhere in the hero, nowhere in
any section heading, nowhere in any body paragraph.

I want to be fair about the obvious defence: Mark also said *"i don't want the feel
of religion."* But he said **feel**, not **subject**. The trade this page makes is
the exact inverse of the one he asked for — it removes the warmest, plainest,
universally legible word in the vocabulary and keeps "Ante-Nicene Period,"
"Constantinian/Nicene Era," "ekklesia," "post-baptismal mercy," "eucharistia" and
"episkopos." It de-Christianises the *warmth* and keeps the *churchiness*. See
Section 5.

### 1.4 Reading level, measured

Flesch-Kincaid grade computed on rendered `<main>` text (imprecise on pages
containing tables — treat as indicative, not decisive):

| Page | FK grade | Avg words/sentence | Polysyllabic % |
|---|---|---|---|
| D03 homepage | **11.6** | 17.7 | 19.5 |
| D03 tradition.html | **14.4** | 22.9 | 22.4 |
| Live `index.html` | 8.4 | 15.3 | 12.4 |
| Live `about.html` | 12.8 | 19.4 | 22.4 |

The Brand Guidelines set a **10th-grade reading floor**. The homepage misses it by
about a grade and a half; the record page misses it by four and a half — upper-
undergraduate. And FK *understates* the real difficulty here, because it cannot see
that "Gravity Discovery," "Integrated Ecology Analysis" and "Dominant Modern
Reconstruction" are opaque *terms of art*, not merely long words. The live homepage
sits at 8.4 on the same brand. This direction moved the front door three grades up.

### 1.5 What it gets right on the charter, said plainly

- **Accessibility as practice, not audit.** Real `<table>` semantics with `scope`
  on every header, era `rowgroup`s, a real `<caption>`, skip link, `:focus-visible`
  everywhere, `prefers-reduced-motion` honoured on the mark and on `scroll-behavior`,
  print styles, `min-width: 0` on grid children so nothing blows out the page. At
  1440 and 1024 the document has **zero** horizontal overflow (measured; the only
  off-canvas element is the intentionally-offscreen skip link). This is above the
  level most production sites reach.
- **The contrast math is correct.** I re-derived all sixteen light-register and
  dark-register pairings in README §5 from the WCAG formula. Every one matches to
  two decimals — iron-gall 13.70, ink-faded 5.39, madder 5.86, Tyrian 6.67,
  gold-leaf 4.54, graphite 3.38, dark `#EDE5D6` 14.76, dark madder 5.18. `--graphite`
  is declared and then never used as text anywhere in either file (grepped). That
  is real rigor, not the appearance of it.
- **The AI section (§4) is the best-executed block on the page** and honours the
  brand's "Always" rule exactly: raise it yourself, show the work, then the caveat,
  side by side, with "what is unfinished, said plainly" given equal typographic
  weight. If this direction dies, §4 should be lifted whole into whatever wins.

---

## 2. Constitution and brand conflicts

The direction's README §6 lists three "proposed stretches" as a single block for
Mark to rule on. They are not the same kind of ask, and bundling them is the
weakest move in the document.

### 2.1 The S0 inversion — I concede this one

README §6.2 asks for a ruling on inverting S0's door-primacy. The direction is
right that `CiC_Full_UX_Design_V1_0.md` governs `cic-poc/frontend`, not
`cic-website/` — the D0 inheritance note says so at seam D, and the Website README
says so explicitly. §5.1's three co-equal doors (Start with your question · Build
your own table · Guided onboarding) describe app states that **are not built**, per
the same seam. You cannot bind a marketing site to a threshold whose doors do not
exist yet.

And the direction is more door-first than its own README claims. Measured: at both
1440×900 and 390×844, the protected hook — *"Twenty centuries of the Church. One
table. A chair pulled out for you."* — is the H1, above the fold, and the primary
madder button *"Come and join us at the Table"* is visible in the first viewport on
both. §5.1's own two protected strings are used correctly and in the right
positions. **The hero does not invert S0. Sections 1 and 2 do.** The README's §3
self-flagellation ("thirty seconds on a phone gets a status band and a method grid,
not a face") is harsher than the render. Attack withdrawn; the author should
correct their own README rather than accept credit for a sin they didn't commit.

### 2.2 The two voice-pair inversions cannot use the same exemption

This is where the bundling fails. The Brand Guidelines are **corpus-wide**. They
are not app-scoped, they are not superseded by the UX constitution, and D0 §1 lists
them as FINAL and "not open for D1 re-litigation." The marketing-site exemption that
legitimately covers S0 does not reach them.

**"Rigorous but not distracting — scholarship underneath, one click away."**
The direction's defence: what is shown first is the *shape* of the rigor while the
*depth* stays one click down, so "not distracting" holds even though "underneath"
does not. That re-reads "underneath" as depth-of-detail. It is not. "Underneath"
and "one click away" are both **positional**; the pair is a rule about *where the
scholarship sits relative to the person*, and the direction has moved it from
underneath to on top. Conceding half a pair and redefining the other half is not
satisfying the pair.

**"Technology but not seen — experience first, governance second, mechanism third."**
This one is worse, because the pair contains an explicit ordinal and the page
inverts it exactly:

| Brand order | This homepage |
|---|---|
| 1. Experience | §1 Mechanism (a ten-step pipeline) |
| 2. Governance | §2 Governance (Constitution Article 17's confidence vocabulary) |
| 3. Mechanism | Experience — **never** (see 1.2: no conversation is shown anywhere) |

Mechanism first, governance second, experience absent. The direction says it
inverted two pairs. It inverted one and deleted the third term of the other.

### 2.3 An unflagged violation: "nothing antiquarian"

`CiC_Full_UX_Design_V1_0.md` §1, the design stance in three sentences: *"The visual
register is a beautifully set trade book on parchment — warm, unhurried, **nothing
antiquarian**, nothing tech-forward."* This is a register rule, not an app
mechanic — it survives the marketing-site scope change intact, exactly as the voice
pairs do.

This direction is antiquarian by construction and by its own vocabulary: a
**frontispiece**, a **colophon**, **Plate I.**, a **register**, section numerals in
**Alegreya SC true small caps**, **old-style figures throughout**
(`font-feature-settings: "onum" 1` on `body`), Roman-numeral catalogue identifiers
(I.1, I.2, I.7), lower-roman counters on the declared limits, and marginal
numbering the README describes as "like a monograph." That is not "a beautifully
set trade book." That is a nineteenth-century critical edition.

The README's §6 flags three stretches for Mark. This is a fourth, and it went
unflagged. For a direction whose credibility rests on naming its own stretches
rather than making them quietly, missing this one costs more than the violation
itself.

### 2.4 "Say what it is, once, and stop"

Brand Never-list: *"denying a suspicion nobody raised — say what it is, once, and
stop."* Measured occurrences on the homepage of the external-review negative:

1. Status band, above the headline: "External academic review — not yet begun"
2. Frontispiece `<dl>`: "External academic review — *not yet begun*"
3. §1 method-status grid: "External academic review — Not yet begun."
4. §4 "What is unfinished": "External academic review has not begun."
5. §5, an entire section: "Independent review is the standard. It has not yet begun."

Five statements of one negative, on one page. "Representative Modes have not
shipped" appears twice. The honesty is admirable and the *repetition* is a rule
violation — and, worse, a tonal one: it reads as a project apologising for itself.

### 2.5 Project jargon on the front door, and "world" is back

Brand Never-list: *"Christianese or project jargon."* D0 §1: the corpus-wide
**"world" → "Christian tradition"** rename is live, applied across site pages and
`world-census.json`, and D1 authors were told to write "tradition."

The first section of this homepage is a ten-card grid of verbatim internal step
titles. Card 1 is **"World Identification, Boundaries, and Orientation."** The
pull-quote directly beneath the grid reads *"built only from the completed and
frozen **world's** ecology."* Cards 3–8 are "Lexicon Candidate List," "Gravity
Discovery," "Ecological Reconstruction," "Full Lexicon Development," "Integrated
Ecology Analysis," "Forces Document" — six consecutive headings that mean nothing
to anyone outside this repository.

The README's defence is that these are verbatim titles and verbatim material is
exempt. That gets the exemption backwards. "Verbatim" protects *approved public
copy* from paraphrase drift; it is not a licence to promote *internal* verbatim
strings to headline furniture on the front door. The rename exists precisely because
"world" confuses visitors — and this puts it in a 48px card at the top of the
homepage, which is the single most visible place on the site to break it.

The direction had an obvious out and did not take it: show the ten steps with
**plain-English titles and the verbatim framework titles one click down**, which is
what "scholarship underneath, one click away" was asking for in the first place.

---

## 3. Fashionable versus professional

The charter's phrase is "professional top-tier design." Mark's gloss, verbatim:
*"engaging and trustworthy (scholor)"* — trustworthy **because** scholarly, paired
with **engaging**, not cold.

### 3.1 The register it chose is itself a fashion

The direction presents itself as the anti-fashion option — "nothing is decorative,"
typography carries the hierarchy, ornament nearly absent. That framing is doing
work it hasn't earned. "Serious digital-humanities archive" is a *current* house
style with a recognisable signature: restrained grid, hairline rules, small caps,
marginal apparatus, and — the tell — **a status band of institutional counts
presented as the first content on the page.** Getty, Wellcome, Cooper Hewitt, every
Observable-adjacent data-humanities microsite of the last five years.

The tell here is the "State of the record" panel. Eight rows. Two of them —
"Movements surveyed for the Atlas: 292," "Eras with the Step 0 survey complete: 10
of 10" — are unactionable by any human outside this repository. "Eras with the Step 0
survey complete" is not information; it is *the appearance of information*, placed
where a hero image would go. That is decoration. The direction's own first principle
is "nothing is decorative," and it opens with a dashboard.

The frontispiece note preempts the obvious objection — *"Nothing here is an
engagement number; these describe the record, not its readers."* Technically true,
and it dodges the letter of the brand's "never engagement numbers as success" rule
while landing squarely in its spirit. "292 movements surveyed" is a scale-brag in a
lab coat.

### 3.2 Real professionalism versus its costume — measured

Here is the sharpest way I can put the distinction: **the direction's rigor about
its own subject matter is genuine and verified; its rigor about its own craft is
not.** Its own stated rules are broken in its own files.

| The direction's own rule | What the CSS/markup actually does |
|---|---|
| README §4: *"nothing under 13px carries meaning"* (also `CiC_Full_UX_Design_V1_0.md` §2.2) | **Measured, 8 distinct meaning-bearing styles run 11.5–12.8px**, including *every column header of the catalogue table* (11.52px: NO. · TRADITION · DATES·REGION · REPRESENTATIVE · EVIDENTIARY BASE · ACTIONS), the method-status labels (11.52px), "STATE OF THE RECORD" (12px), every tradition's formal name (12.8px), every Representative's role (12.8px), every era's date range (12.8px). |
| README §5: AAA 2.4.9 adopted — *"link purpose from link text alone — every register action names the Representative"* | **Seven identical `Read the record →` links**, pointing at two distinct destinations, none naming its tradition. `Begin with Chloe ↗` and `Bring Chloe to the Table` do name her; the *first* action in every row does not. |
| README §4: gold-leaf *"never sets small text"* | `tradition.html` `.plate .rep .role` — the "REPRESENTATIVE" label — is `var(--gold)` at `.72rem` (11.5px), bold. Measured 4.90:1 on vellum, so it clears AA; it breaks the direction's own rule and the 13px floor. |
| README §4: *"Every token is the brand's, used for the job the constitution assigns it… Tyrian for the confidence and transparency apparatus alone"* | `#7c3aed` is **hardcoded** as a status dot in `tradition.html` twice — the "OPEN FOR CONVERSATION" chip (line 116) and the seat bar's "Chloe is seated" dot (line 134). It is the House-Churches' census tint repurposed as generic UI chrome, it is not a brand token, it is not re-toned for dark mode (measured 3.06:1 on the dark ground — it clears 1.4.11 by 0.06), and it reads as purple, which is the one colour this direction says is reserved for the confidence apparatus alone. A purple dot meaning "status: open" is precisely the semantic collision the reservation exists to prevent. |
| README §1: *"Nothing is decorative"* | The eight-row "State of the record" dashboard; the 48px line emblems in the register, at which size three of the four bust illustrations are indistinguishable and none of the source-grounded objects is legible. |

The dark register is genuinely well-handled — I measured every dark pairing and they
all clear comfortably (`#EDE5D6` 14.76, ink-faded 8.45, madder 5.18 both as text and
flipped as button fill, Tyrian-light 9.45, gold 8.47). The one weak spot is the
hardcoded `#7c3aed` above.

### 3.3 Does it fight "warm… scholar-host at a table"?

Yes, and specifically it drops the **host**.

The brand's sound-like is "N.T. Wright · Tim Mackie · Justo González — a scholar-host
at a table. Warmth through shared discovery, not comfort." A scholar-host is a
*person who invites you in*. This homepage has the scholar and the table and no host.
There are exactly two moments of address on it — "The chair is yours" and "the record
stays open whether or not you ever sit down" — and both are excellent. Everything
between them is a third-person institutional voice describing procedure.

The direction's README §2 argues the warmth is placed rather than removed, in three
moves. I take each seriously:

1. **"The declared limits get the same typographic dignity as the strengths… a page
   that says 'here is what we cannot tell you' before 'come sit down' is safer for
   exactly that person."** This is the best sentence in the README and it is *true* —
   but it proves less than it claims. It establishes that **disclosure** serves the
   doubter. It does not establish that **methodology** serves the doubter. Those are
   different things. "The interior life of enslaved and non-literate members is held
   as named absence" is disclosure, it is beautiful, and it lands on
   `tradition.html` where it works. "Step 4 — Gravity Discovery: each candidate is
   tested six ways and classed Primary, Supporting, or Tensional" is methodology,
   and it lands on the homepage, where it answers a question about the vendor's
   process. And note what the homepage's *actual* lead disclosure is — not "here is
   what we cannot tell you about the early church," but "external academic review:
   not yet begun; Representative Modes: not yet shipped; census generated
   2026-08-02." That is a **changelog**, not a confession.
2. **"The human weight is carried by the record's own voices."** True — Ignatius
   under armed guard, "the homes of people history did not bother to write down,"
   Chloe's "where we sound most alive, we are also… at our thinnest." These are the
   most affecting lines in the whole direction. All of them are on `tradition.html`,
   at §3 and §6 of an inner page reached through a table row. **On the homepage,
   before §5, there is not one human voice.**
3. **"The chair is always visible and never pushed."** True on desktop, verifiably
   false on phone — see 4.2.

The direction's own README closes §2 with a test: *"If D2 finds those three moves
insufficient, the direction is cold and should be killed or hybridized, not warmed
with imagery it has no honest use for."* I find move 1 sound but misapplied, move 2
true but located on the wrong page, and move 3 broken on the platform where it
matters. By the direction's own stated test, that is a fail.

---

## 4. Where a real visitor gets lost — measured

### 4.1 The register collides with itself at 1280 and 1440 (severity: high)

**Measured, reproducible, both widths.** Scroll into the register section.
`.marginal` is `position: sticky; top: 1rem` in column 1 of a
`grid-template-columns: 13rem minmax(0,1fr)` grid. The register table is placed in
`.span-all { grid-column: 1 / -1 }` — so it occupies column 1 as well. As you scroll
the ~1,100px-tall section, the pinned marginal column **slides down over the table**.

Measured collision box: **208px wide × 328px tall**, at both 1280×800 and 1440×900,
at every scroll offset inside the section.

Rendered result: "Syriac Christianity" printed over "this table is"; "Era II · The
Imperial Church Era" printed over "record's own one-line"; and the marginal's live
link — "All 292 surveyed movements, in Church in History →" — sitting directly on
top of the "Church and Empire / Imperial and Juridical Christianity" row, where it
will also intercept clicks meant for the row beneath it.

This happens on the **only** section that answers "who can I talk to," at the two
most common desktop widths, on the direction whose entire argument is that it is
professional on sight. It disappears below 900px because `.marginal` goes static
there — so it is a desktop-only defect, on the platform this direction is aimed at.
It is a one-line fix (`.span-all` should start at column 2, or the marginal should
stop being sticky in that section), which makes it more damning rather than less:
nobody scrolled through their own flagship section on a normal monitor.

### 4.2 Phone: the register is a wall, and the doors are behind it

**Measured at 390×844.** The register table has `min-width: 64rem`. Its scroller is
390px wide with 1,073px of content. Measured column offsets inside the scroller:

| Column | Left edge inside scroller |
|---|---|
| NO. | 0 |
| Tradition | 114 |
| Dates · Region | 241 |
| Representative | 459 |
| Evidentiary base | 616 |
| **Actions** | **840** |

To reach *any* "Begin with Chloe ↗" or "Bring Chloe to the Table" link on a phone, a
visitor must horizontally scroll **850px inside a nested container**, per row, with
the page also scrolling vertically. Meanwhile `.masthead__cta` is `display: none`
below 640px.

So on a phone, the only reachable Table entry points are the generic hero button and
the generic closing CTA 12.8 screens down. **Every tradition-specific door is
off-screen.** The README's "Easy access to features — solved structurally… The Table
is one click from anywhere" is a desktop claim presented as a general one.

For contrast, the live homepage puts seven faces, each with its own interview link
and its own Bring-to-the-Table link, in a snap-scrolling carousel at roughly screen 2.

### 4.3 Phone navigation is effectively invisible

**Measured at 390×844:** `nav.nav` has `clientWidth: 125px` and `scrollWidth: 659px`,
`overflow-x: auto`, `scrollbar-width: none`, and `::-webkit-scrollbar { display: none }`.
Only "Home" is fully visible; "Traditions" is clipped mid-word. Method · Church in
History · Review · About · Get Involved are all off-screen, behind a horizontal swipe
with **no scrollbar, no chevron, no fade, no hamburger**. And the masthead CTA is
hidden at this width, so nothing else signals that the strip continues.

**Partial concession, because it matters:** this pattern is *inherited* — the live
`assets/style.css` does the same thing at ≤640px, with a code comment explaining why
(six links plus the wordmark previously pushed the whole page wider than the
viewport). This direction did not invent it. But it made it worse in two ways: it
added a seventh nav item and a masthead button that consume the space, and — see
next — it removed the width guard.

### 4.4 The desktop nav silently clips "Get Involved" at every width I tested

**Measured:** at 1440, 1280 and 1100, the last nav item "Get Involved" overflows the
nav's clip box and renders as "Get Involve". At 1024, "About" clips too. Root cause:
D03 applies `overflow-x: auto; scrollbar-width: none` to `nav.nav` at **all** widths,
where the live stylesheet scopes the same rule inside `@media (max-width: 640px)`.
At 1440 the nav needs 659px and gets 648.

So the site's giving/support link is visibly truncated on a plain 1440×900 desktop
render. On this direction. Where craft *is* the argument.

### 4.5 The record page's own contents list lands under its own sticky bar on phone

**Measured at 390×844, `tradition.html`.** The seat bar is `position: sticky; top: 0`
and, because `.seatbar .page` becomes `flex-direction: column` below 640px, it is
**156px tall — 18% of the viewport, permanently.** Section anchors carry
`scroll-margin-top: 5rem` (80px), calibrated against the desktop bar's measured 60px.

Result, measured by navigating to `#limits`: the "6 Declared limits" heading lands
**49px behind the sticky bar** and is not visible. The step-reference line beneath it
is also hidden. Every one of the ten in-record contents links has this behaviour on
phone. The finding-aid's own finding aid is broken on the platform where a
ten-section record most needs one.

Related, and worth Mark's eye rather than mine: a permanently-pinned 156px bar
containing a bordered "Begin an interview with Chloe" button, present at every scroll
position, is a strange fit for a direction whose thesis is *"the chair is always
visible and never pushed."* On desktop (60px, one line, outlined button) the posture
is exactly right. On phone it is the single most insistent element on the page.

### 4.6 Screen-reader navigation of the catalogue: the row header is the wrong cell

The register's row header is the Atlas identifier:
`<th scope="row" class="no">I.1</th>`. The tradition's name is in a `<td>`.

So a screen-reader user moving down the "Evidentiary base" column hears
*"Evidentiary base — I.1 — Moderate; communal voice rich, individual interior voice
thin"*, then *"I.2 — Rich (Clement, Origen)…"*. They must hold a mapping from Roman
numerals to traditions in their head across a seven-row, seven-column table. The
whole point of `scope="row"` is that the header re-announces the thing the row is
*about*. Here it re-announces a catalogue number the README itself says is "not a
ranking" and carries no meaning to a visitor.

Everything else in the table markup is right — `scope="col"` on all seven headers, a
real `<caption>`, `scope="rowgroup"` era bands in separate `<tbody>` elements, a
`visually-hidden` label on the emblem column, `role="img"` with descriptive
`aria-label` on every emblem SVG. Which makes this one wrong choice more conspicuous,
not less.

### 4.7 Smaller, verified

- **The disclosure grammar demo is inert.** Both files contain zero `<script>` tags.
  The `.lex` "ekklesia" span carries the dotted Tyrian underline that signals
  interactivity and does nothing; the ✲ mark is an anchor to `#confidence`, the
  section it already sits inside. The adjacent copy says *"Hover for the short entry;
  click for the full one, with sources and confidence — down to the footnote."* On a
  page whose thesis is "we show our work," the one demonstration of the flagship
  interaction is a promise the page does not keep. A static two-panel picture of the
  real Level-2/Level-3 grammar would cost nothing and deliver more.
- **The portrait's declared aspect ratio does not apply.** `.plate img` sets
  `aspect-ratio: 4/3`, but the `height="600"` HTML attribute maps to a presentational
  `height: 600px`, which wins. Measured: 410×600 at desktop, **318×600 at 390px — 71%
  of the phone viewport**, from a 530×530 source, hard-cropped by `object-fit: cover`.
  It happens to look fine; it is not doing what the CSS says.
- **602px of dead space** in `tradition.html`'s title block at 1440×900 (measured:
  title block 940px tall, left column 338px). The largest single void in either file,
  directly beside the page's most beautiful element.
- **A superseded certificate cited as current.** The homepage's method-status grid
  says *"The most recent tradition admitted (Cappadocian, 2026-08-31)…"*
  `CAPPADOCIAN_BUILD_LEDGER.md` §28–29 records that the post-rename recompile
  **invalidated** that certificate and a fresh M3 battery was run on **2026-09-01**;
  the registry now names 2026-09-01 as the operative one. The 259-records and 28/28
  figures are both correct — I verified them — but the date names a certificate the
  project's own record marks as superseded. Small. On a scholarly-authority homepage,
  it is the exact class of error this direction cannot afford, and it is a live
  demonstration of the maintenance burden a status-band homepage takes on: every
  number on it is a promise to keep it current.

---

## 5. Religious feel — does "scholarly instrument" read as neutral-academic?

Mark, verbatim: *"non religious (even though we are religious, i don't want the feel
of religion)."* The Decision-Log reads this correctly as a **formal** requirement —
how the thing feels on sight, independent of doctrinal content.

**My honest answer: it escapes "devotional" cleanly and lands in "seminary." That is
a worse place for Mark's stated heart audience, not a better one.**

**What it gets right.** There is no liturgical structure, no prayer, no scripture
citation, no invitation to believe anything, no cross, no dove, no flame. The mark is
used correctly and its public sentence appears beside it at first contact, as the
Logo Usage Sheet requires. The one motion on the page is the approved "Arriving"
animation. Nothing here reads as a church website. If the test were "does it feel
like a devotional product," it passes.

**What it gets wrong.** The test is not "devotional." It is "the feel of religion,"
and religion has more than one institutional register. This page's register is the
**divinity-school special collections finding aid**. The evidence is cumulative and
formal, not incidental:

- Parchment ground + Alegreya + true small caps + old-style figures + Roman-numeral
  identifiers + "colophon" + "frontispiece" + "Plate I." + marginal numbering. Read
  in combination, with early-church content, that is manuscript/scriptorium
  iconography. The constitution's "nothing antiquarian" rule exists precisely to
  prevent this landing (§2.3 above).
- Era bands labelled by ecclesiastical periodisation — "The Ante-Nicene Period," "The
  Constantinian/Nicene Era."
- A "Standing on the Nicene Creed" floor note on the record page — a *doctrinal
  positioning statement*, presented as archival metadata.
- Untranslated Greek as a display feature: `episkopos · presbyteros · ekklesia ·
  eucharistia`, set in italic Tyrian chips.
- The confidence vocabulary itself: "Documented / Widely Accepted / Dominant Modern
  Reconstruction / Contested / Inferential-Thin" is the vocabulary of a *theological
  faculty*. It is exactly right inside a conversation and it is a graduate-seminar
  register on a front door.

Here is why the specific landing matters more than the general one. For a *general
interest* visitor, "neutral-academic archive" is a fine and even flattering read. For
Mark's named heart audience — someone **re-assessing, deconstructing** — a seminary
register is not neutral ground. It is the aesthetic of the institution that
credentialed the thing they are currently coming apart over. A page that opens by
establishing scholarly authority, in the visual language of a theological library,
is not read by that person as "safe because rigorous." It is read as "this is run by
the people who already have the answer, and they are showing me their credentials
before they will talk to me."

The direction argued (§2, move 1) that a page which discloses its limits first is
*safer* for exactly that person. I said above I think that is true of disclosure. It
is not true of **authority display**, and this page leads with authority display —
counts, method, apparatus, a firewall quotation from an internal Change Order, a
28-of-28 pass rate. That is a credentials wall. For someone in doubt, a credentials
wall is the specific thing that makes a room feel like the room they left.

And the inversion in 1.3 sharpens it: the page removed "Jesus" (warm, plain,
universally legible — and the thing the charter's own heart goal names) and kept
"Ante-Nicene," "eucharistia," "post-baptismal mercy" and "the Nicene Creed" (cold,
in-group, seminary). If you were deliberately trying to satisfy the letter of "no
feel of religion" while maximally violating its spirit, this is what you would build.

---

## 6. Does it over-serve the academic at the expense of the person with hard questions?

**Yes. I think this is fatal to the direction as constituted, independent of craft
quality, and I do not think it can be fixed by adjusting the warmth.**

The ranking is not ambiguous. Mark, verbatim, 2026-09-02:

> *"i want the general interest, re-assesing (deconstruction), pastor and scholor to
> feel at home, but my heart is those seeking answers to hard questions of faith,
> **not accademics**."*

Direction 03, its own first sentence:

> *"The site is a scholarly instrument, and it says so at first glance."*

And its own §2 scoring of the professional-design goal:

> *"Professional on sight, to a pastor, a professor, or a skeptical reevaluator."*

Note the order even there. Pastor, professor, then reevaluator — and "skeptical
reevaluator," which is the academic's *description* of a person in doubt, not that
person's description of themselves. Someone whose faith is unravelling does not
experience themselves as conducting a skeptical reevaluation. They experience
themselves as frightened, or angry, or exhausted, or lonely. The direction's own
prose about that person is written from outside them.

### 6.1 The mechanism of the failure, not just the mismatch

I want to be precise about *how* it fails, because "it's too academic" is a vibe and
this is an argument.

Someone arriving in real doubt needs two things in the first thirty seconds:
**(a) permission** — evidence they will not be sold to, managed, or corrected; and
**(b) something person-shaped to ask.**

Direction 03 delivers (a) superbly. The "no pressure, just witness" posture is real
and verifiable in the markup: no email capture, no modal, no scarcity, no countdown,
"the record stays open whether or not you ever sit down," and the seat bar's
outlined-not-filled button. Genuinely, this is the best "no pressure" execution I
could imagine anyone building. Mark's fourth value is fully served.

It fails (b) completely above 7.4 phone screens. The first person-shaped thing on
the page is Chloe's name, in a table cell, in the "Representative" column, at
6,742px on a phone. Not a face. Not a voice. A cell.

And there is a third, worse effect, which is the one I would put in front of Mark.
**Leading with the confidence scale pre-frames every future answer as provisional.**
Inside a conversation, the five-level scale is a guardrail and it is the project's
single best trust asset. Placed on the homepage as the second thing, before any
content it could label, it is a legend without a map — and what it tells someone
already in doubt is: *everything you are about to hear is graded, some of it is
"Inferential / Thin," and we will not resolve the disagreements.*

For an academic, that is a feature. It is why a scholar would trust this project over
any competitor. For a person whose faith is unravelling and who came looking for
somewhere solid to stand, it is an **advance apology**. The brand's own ordering rule
covers exactly this and the page-level order breaks it: *"Show the work before the
caveat."* Inside §4 the direction honours that rule beautifully — "What holds it" left,
"What is unfinished" right. At page level it does the reverse: the caveat apparatus
(§2) precedes any of the work it would caveat (§3), and the status band puts
"External academic review — not yet begun" *above the headline* on a phone. The very
first thing a phone visitor learns about this project is a negative status disclosure
about an academic review board they never asked about.

### 6.2 Who this page is *actually* optimised for

Test it against the four Representative Modes:

| Mode | Served by this homepage? |
|---|---|
| **Academic** | **Exceptionally.** The method grid, the Article 17 vocabulary, the evidentiary-base column, the declined gravity kept on record, the published "where a reviewer might press first," the 28/28 battery, the reviewer's-brief email. There is no better page on the internet for a patristics scholar deciding whether to take this seriously. |
| **Pastor / Teacher** | Well. The record page is a superb sermon-prep artifact. |
| **General interest** | Poorly. 11.6 FK, 8 desktop screens, a factory tour before the product, and no answer to "what is it like." |
| **Reevaluation (Mark's heart)** | **Actively badly**, per 6.1 and Section 5. |

The page is a perfect inversion of the stated ranking.

### 6.3 Is this fatal, or fixable?

I pushed hard on whether a resequence saves it: put the register first, method third,
confidence apparatus behind a link. And I think the honest answer is that the
resequenced page **is no longer this direction.** README §1 is explicit that the
order *is* the thesis — *"A serious research library's digital exhibit does not open
with a mood; it opens with what the collection is, how it was assembled, and how much
of it can be trusted."* Move the method and the scale below the register and you have
an editorial or product-led homepage that happens to have good apparatus underneath —
which is precisely the arrangement the Brand Guidelines' "scholarship underneath, one
click away" pair asked for in the first place, and which the direction's §6 asked
permission to invert.

So: the fix for the fatal problem is the un-inversion of the stretch the direction
requested. That is not a revision. That is a concession that the stretch should not
have been granted.

**One thing that must not die with it.** `tradition.html` is the best artifact in
this direction and, I suspect, one of the better ones in the whole D1 set. As a
*record page reached after a visitor has chosen a tradition*, its sequencing is not
inverted at all — a person who clicked "The House-Churches" has already asked "can I
trust this?", and scope → sources → voices → gravities → contested ground → declared
limits → the Representative is the right answer to it. It has the portrait, the human
voices, "where we sound most alive, we are also, in one specific and disclosed way, at
our thinnest," the four published attack questions, and the chair pulled out the whole
way down. Everything that is wrong with the homepage is right on this page, because
the page sits at the point in the journey where the homepage's posture actually
belongs. Whatever wins D3 should take this page nearly whole (with 4.5, 4.7 and the
gold-at-11.5px fixed).

---

## Verdict — mine, adversarially, not a ruling

**Dies as a homepage direction. Survives, and should be harvested, as an inner-page
pattern and as an apparatus standard.**

Not because it is cold, and not because it is badly made. It is better made than its
critics will assume, and I have said so specifically: the accessibility floor is real
practice rather than a late audit, the contrast math is correct to two decimals, the
census strings are verifiably verbatim including one the direction flagged rather
than silently corrected, the 259-record and 28-of-28 claims check out against the
build ledger, the AI disclosure section is the best-written block anyone will produce
in this phase, and the "no pressure, just witness" posture is executed more faithfully
here than I could design it myself.

It dies for one reason, and the reason is structural rather than aesthetic: **the
direction's thesis is its section order, and its section order is a ranking of
audiences that inverts Mark's own.** He said the academic is not the heart. This page
is built so a scholar feels at home first, by design, on purpose, argued for in the
README. The three warmth moves offered in defence are — measured against the built
files — one sound argument misapplied to the wrong content, one true claim located on
the wrong page, and one that is verifiably false on phone. The direction's own README
set the test for exactly this and named the consequence: *"If D2 finds those three
moves insufficient, the direction is cold and should be killed or hybridized, not
warmed with imagery it has no honest use for."* I find them insufficient. I take the
author at their word.

And the craft defects sharpen rather than soften that judgment. A direction that wins
on rigor cannot ship a flagship section that collides with itself at 1280 and 1440, a
nav that clips its own giving link on a plain desktop render, a contents list that
lands behind its own sticky bar, a claimed AAA success criterion falsified seven times
in one table, and a 13px floor broken by its own column headers. Those are all
one-line fixes; that is the problem. They mean nobody scrolled the built page on an
ordinary monitor or a phone. For any other direction that is a bug list. For this one
it is a hole in the argument.

**If Mark wants it to survive anyway, the minimum is not a revision:**
1. Register first, above the method and the scale — which un-does stretch §6.1 and
   ends the direction's own thesis.
2. Show a conversation on the homepage. Anything. One real exchange.
3. Faces, at a size where a face reads. The locked portraits exist and are already in
   production use.
4. Plain-English step titles with the verbatim framework titles one click down;
   "world" off the front door.
5. Fix §§4.1–4.6 before anyone else looks at it.
6. Say the external-review negative once.

Items 2, 3 and 4 are the other directions' territory. Item 1 dissolves this one. That
is what I mean by "dies": not that it is worthless, but that the parts of it worth
keeping are parts, and the whole is aimed at the wrong person.

**What I would carry into D3 regardless of what wins:** `tradition.html` almost
entire; §4's AI disclosure block verbatim; the confidence-scale glyph set and the
word+glyph no-colour-alone discipline; the "declared limits given the same
typographic dignity as the strengths" principle; the practice of reproducing a census
string verbatim and flagging it rather than quietly fixing it; and the contrast-math
table in README §5, which is the most rigorous accessibility artifact I have seen in
this repository and should become the shared V2 text-colour rule the D1 closure entry
already says is needed.

---

*Reviewer's note: this is one adversarial read, written to attack. The author of
direction 03 gets a defense before anything is decided, and several of my findings
above are craft defects they could close in a morning. The findings in Sections 5 and
6 are the ones I do not think a defense can close, and they are the ones I would ask
Mark to rule on directly.*
