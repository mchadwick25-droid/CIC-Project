# D2 adversarial review — Direction 06, "The Open Door" (the hybrid)

**Sandbox artifact. Adversarial, by assignment. Not a ruling. 2026-09-02.**

Reviewer: Opus. My brief was to try to kill this direction, and to give it the same
full discipline every original D1 direction got — not a lighter pass because it is
already a synthesis of prior critique. I read `06-hybrid-open-door/README.md`,
`homepage.html` and `tradition-chloe.html` in full; the Website V2 charter and the
whole `Decision-Log.md`; the D0 inheritance note; all five original D1 direction
READMEs; **all ten** D2 review/defense files; the struggle summary; the Brand
Guidelines Consolidated V1.0 and the Logo Usage Sheet V1.0; `CiC_Full_UX_Design_V1_0.md`
(§2.5a, §4.0, §5.1, §5.4, and the §3 state table's R.0–R.2c rows); and the live
`cic-website/` pages, `assets/style.css`, `_headers`, `data/world-census.json`, the
`records/pahc/*` and `engine/canon/records/canon_question/*` records the mockups quote, the
World 1 Guided Starters draft, `cic-poc/frontend/src/App.tsx` and `screens/Launch.tsx`,
and the `theon-confidence.png` capture itself.

**Method — the browser work is real.** Chromium `/opt/pw-browsers/chromium-1194`
(`chrome-linux/chrome`, passed as an explicit `executablePath`) driven by Playwright.
Both files rendered at 320 / 360 / 375 / 390 / 414 / 480 / 600 / 640 / 768 / 820 / 900 /
1024 / 1099 / 1280 / 1440 px, in `prefers-color-scheme: light` and `dark`, with and
without JavaScript, with and without `prefers-reduced-motion`, with touch emulation, and
with the CDP accessibility tree read directly. Contrast numbers are computed from
*rendered* colours — each text node's computed colour composited against its real
painted ancestor background — and separately re-derived from the raw hex values with the
WCAG relative-luminance formula in a standalone script, so the two methods check each
other. Google Fonts is unreachable from this sandbox, so every render is in fallback
faces: pixel heights are font-sensitive, ratios, DOM order, focus behaviour and semantics
are not. Same caveat every D2 reviewer stated, and the author states it too.

I will say at the top what I think is true, because it changes how the attacks below
should be read: **this is the best-measured artifact the workstream has produced, and
its self-assessment is, on the numbers, unusually honest.** I went looking for inflated
claims in §6 and §7 and mostly did not find them. Where I did, I say so precisely. The
attacks that land are not about craft. They are about whether the door it built is a
door.

---

## Summary — what I think kills, and what does not

Six findings I consider load-bearing. Two are structural; four are provable defects the
README's own measured list should have caught.

1. **The door is below the fold on every phone and most laptops.** Measured at 390×844,
   the input's top edge is at **897px** — 53px past the viewport. Subtract the 53px
   sandbox note that "would not ship" and its top edge sits at exactly 844: zero pixels
   visible. At a realistic iOS Safari viewport (390×740) the H2 "Start with your
   question" is the last thing on screen. At 390×660 **the words "Start with your
   question" are not on screen at all**. The README says "the input is at the fold."
   It is not at the fold; it is under it.
2. **The door does not open.** Submitting scrolls you ~1,000px down to a
   century-sorted directory. Choosing a person opens a **new tab** with no `q` in the
   URL, so the held question stays behind in the first tab and must be retyped from
   memory. Measured: the first real conversation link on a phone is at **2,627px** —
   *further down the page* than the 2,487px that the 05 review called that direction's
   central measurement failure.
3. **The person who just typed a hard question is answered with a scarcity notice.**
   Measured: after submit, the first screen at `#who` reads — held question, "Who would
   you like to ask?", scope line, then *"This is a pilot. We're intentionally looking
   for a limited number of participants…"* and *"Because of cost, we're asking each
   participant to keep to about five conversations for now."* The Brand Guidelines'
   Never list bans "urgency or scarcity." The copy is inherited; the flow that routes a
   confession straight into it is new.
4. **A visible rendering bug in the header, both pages, every width ≥641px.**
   `.site-nav a{display:inline-flex}` makes the `<span class="sd-long">` and the text
   after it anonymous flex items, and flex strips the whitespace between them. The
   returning-visitor door renders as **"Been here before?Go straight in →"**. Measured
   gap between the span's right edge and the text's left edge: **0.00px** at 1280 and
   at 700.
5. **Three parentage claims do not hold against the primary sources**, including one
   that credits two defenses with conceding something both of them explicitly
   contested. Details in §2.
6. **Two of the five D1 deaths are answered in copy and reproduced in structure.**
   The picker under the door is 05's row grammar intact — portrait ring, name, role,
   tradition, dates · region, one-line tile, action links, under era headings with
   century ranges. The IA the 05 review called "an academic's index" is still the
   answer the question door gives.

Findings 4 and most of §7 are a morning's work. Findings 1, 2 and 3 are the direction.

---

## 0. What verifies, so the attacks land

I checked the README's measured claims before attacking anything, because a review that
attacks an honest document by pretending it is dishonest is worthless. These all
reproduce:

- **Horizontal overflow: 0px at 320, 360, 390, 414, 768, 820, 1024, 1099, 1280 and
  1440, in both registers, on both pages.** `documentElement.scrollWidth` equals
  `clientWidth` at every one. Three D1 directions failed 1.4.10 Reflow; this one does
  not, and I tried to break it.
- **Text contrast: 0 failures.** I walked every rendered text node on both pages in both
  registers — 156 nodes on the homepage, 220 on the tradition page — composited each
  node's colour against its real painted background, and applied the large-text
  threshold correctly. Zero failures. Minimum in light: **5.37** (ink-faded on
  gold-wash). Minimum in dark: **5.66** (button text on the madder fill). Both are
  exactly the numbers §7 claims.
- **Nothing under 13px**, either page, either register. Zero nodes.
- **The §6 contrast table is correct to two decimals, every row.** I re-derived all
  nine light pairs across three grounds, all ten dark pairs across three grounds, the
  button pair, the seven light tints and the seven proposed dark tints independently
  from the hex values. Every published number matches. Including the ones that indict
  the palette: gold-leaf **4.52** on gold-wash, graphite **3.38** on parchment, the
  madder fill **2.69** against the dark surface, and the raw census tints in dark
  (Church and Empire **1.99**, Bethlehem **2.34**, Alexandria **2.73**). The 1.5px
  `#E08C74` edge is doing the 1.4.11 work on the dark button, as claimed — it measures
  6.79 against the surface it actually sits on (the README quotes 7.19, the
  against-ground figure; both clear 3:1).
- **The motion inventory is exact.** I enumerated every element's computed
  `animation-name` and `transition-duration`. Homepage: exactly two animations, both on
  the mark. Tradition page: **zero**. Under `prefers-reduced-motion: reduce`: **zero on
  both**. No transitions anywhere, and achieved by omission, not by a global
  `!important` — the 04 review's "sledgehammer" is genuinely not here.
- **The phone landmark table in §7 is accurate to the pixel.** H1 313, "Start with your
  question" 717, input bottom 945, chairs 1,861, first Ask 2,627, disclosure 7,232;
  tradition page 16,634px at 390×844. I got all of them.
- **41 tab stops on the homepage**, as claimed; none smaller than 24×24.
- **The lexicon's Level-2 defect that 01 conceded is genuinely fixed by construction.**
  Read straight out of the CDP accessibility tree at rest, with the card `display:none`:
  `button "episkopos"` carries the full gloss as its accessible **description**. A
  screen-reader user hears the short tier whether or not the card is painted. That is
  the thing 01 got wrong and this fixes, and it fixes it the hard way.
- **The lexicon's keyboard and touch grammar work.** Focus a term → card shows
  (`aria-expanded="true"`, `display:block`). Enter → panel opens, focus moves to the
  close control. Escape → panel closes, focus returns to the term. On a coarse pointer,
  first tap shows the card as a fixed popover inside the viewport (measured top 621,
  bottom 824 of 844), second tap opens the panel. No hidden card contributes a tab stop.
- **The skip link works.** After activating it, the next three Tab presses all land
  inside `<main>` — on the homepage the very first is the question input.
- **Print works.** Header, support block and skip link hidden; all six main sections
  present.
- **Every quotation I could check is verbatim.** All six homepage canon questions and
  all four on the tradition page match `engine/canon/records/canon_question/*-p-*` word for
  word, and all 23 P-cell records are indeed `canon_status: seed`. The three starter
  questions match the "For the Wrestling" openers in
  `CiC_W1_Guided_Starters_V0_1_DRAFT.md` word for word, and that file's own header does
  say "DRAFT — awaiting Mark's review. Not deployed." All four `honest_limit` statements
  and the `pahc.craft.chloe-voice` guard line and identity sentence are verbatim from
  the record store, and those records really are `status: draft`. Every census field —
  seven names, roles, tradition names, dates, regions, tints, the `sourcing` line, the
  `floorNote`, the `longDescription`, the `voices` list, the `legacy` paragraph and the
  two `experienceToday` links — matches `world-census.json`. **And the Theon
  transcription is exact.** I read the PNG directly and compared it line by line; every
  word of the Facilitator's two turns, the participant's question and Theon's three
  paragraphs is unaltered.
- **Reading level clears the brand's own floor.** Flesch–Kincaid on the rendered
  homepage body, draft tags stripped: **grade 8.2** (1,632 words, 104 sentences). The
  Brand Guidelines set a 10th-grade floor; the 03 review measured that direction at 11.6
  against a live site at 8.4. The tradition page is 10.1, which is the right place for a
  record page to sit.
- **The 03 review's two hardest content charges are answered.** "It never shows the
  product": this one does — a 499-word real captured exchange. The 1,352:585
  instrument-to-traditions word budget is inverted: measured by section, ~1,034 words on
  the traditions and the conversation against ~683 on the door, the disclosure, the map
  and the ask.
- **The 05 review's vocabulary count is answered.** doubt 2, leave 1, hypocrites 1,
  suffering 2, pray 1, re-examining 2 — against 0/0/0 in the direction that died partly
  for it. And the lede names Mark's person in the **first screen**: *"or with a question
  about faith you've carried for years — there is a chair."* 01 named that audience once,
  at screen 22.8 of 24.5. This names them at screen 0.4.

That is a real body of work, and none of what follows should be read as denying it.

---

## 1. Charter-goal failures — the self-assessed claims against the markup

### 1.1 "The input is at the fold" — no, and this is the direction's spine

README §4, under *Easy access to features*: *"On a 390×844 phone the door's heading is
in the first screen and the input is at the fold (§7)."*

Measured, homepage, first paint, no scroll:

| Viewport | Header height | H1 | "Start with your question" | Input top | Visible in screen one |
|---|---|---|---|---|---|
| 320×844 | 168px | 351 | **850** | **1,084** | mark caption, H1, lede |
| 390×844 | 168px | 313 | 717 | **897** | mark caption, H1, lede, eyebrow, H2, the "how" line |
| 390×740 *(real iOS Safari)* | 168px | 313 | 717 | **897** | …through the H2 only |
| 390×660 *(real Android Chrome)* | 168px | 313 | **717 — off screen** | **897** | mark caption, H1, lede |
| 1280×800 | 73px | 229 | 627 | **767** (bottom 815) | just fits, on a full-height window |
| 1440×900 *(real viewport ≈790)* | 73px | 229 | 627 | **767** (bottom 815) | **bottom edge clipped** |

I enumerated the actual visible text nodes rather than reasoning from the numbers. At
390×844 the first screen is: the mark's caption sentence, the H1, the three-line lede,
the eyebrow "THE WAY IN", the H2, and the "how" paragraph. **The input, the button and
all six offered questions are below.** At 390×660 the first screen is the mark's
caption, the H1 and the lede — and nothing that says a question can be asked here.

"At the fold" is doing more work than the word can bear. On the 390×844 figure the
README itself quotes, the input's *top* is 53px past the viewport bottom; strip the 53px
sandbox note and its top is at exactly 844 — the fold line, with zero pixels of the
control rendered. On no real phone, with browser chrome, is any part of that input
visible without a scroll.

Why this is the finding I would lead with: the direction's entire thesis, in its own
first sentence, is *"this hybrid's spine is that door, built… The homepage opens with the
protected hook and, directly beneath it, one real place to write a question."* The
hybrid's own philosophy §1 diagnoses all five parents as having "each led with
something" other than the question. This one leads with a hook and a lede and a caption
about the logo, and puts the question door in screen two. It is a better screen one than
04's (which had no headline at all) and than 01's and 03's. It is not the screen the
README describes.

The fix is not hard — the hero is 620px of centred display type on a phone; the mark
line, the H1 and the lede could all sit above a door that starts at ~500px. But it has
to be *made*, and the README's own measurement pass did not flag it because §7 records
the landmark positions without ever comparing them to the viewport.

### 1.2 "Easy access to features" — the click count, again, without the scroll cost

The 05 review's single sharpest methodological finding was that a step map counting
clicks and omitting scroll "measures the wrong thing." Its number was 2,487px to the
first "Begin a conversation" on a 390-wide phone.

Measured on this homepage at the same width: **the first "Ask Chloe" link is at
2,627px.** With the non-shipping sandbox note removed, 2,574px. Either figure is *larger*
than the number that convicted 05.

The hybrid does put six real, warm, question-shaped links at 1,212px, which 05 did not.
But those links do not go to a conversation (§1.3). The first door into the product is
farther down this page than on the page that was killed for it, and §4's claim —
*"a tapped question lands on the chairs; a tapped name is the app"* — makes that sound
like two steps when it is a 649px scroll, a seven-way decision among strangers sorted by
century, and then a new tab.

### 1.3 The door does not open — end to end, measured

I ran the whole flow. With JavaScript, at 390×844:

1. Type *"I don't know if I believe any of this anymore."* → submit.
2. `history.replaceState` writes `?q=I%20don%27t%20know…` to the URL. The `#held` block
   un-hides. Focus moves to `section#who` (`tabindex="-1"`). Scroll lands at y=1,845.
   All of that works exactly as §7 says.
3. What is now on screen, in order: **Your question, held:** · the question · **Who
   would you like to ask?** · "Seven Christian traditions from the Early Church and
   Imperial Church eras…" · **"This is a pilot. We're intentionally looking for a
   limited number of participants…"** · **"Because of cost, we're asking each
   participant to keep to about five conversations for now…"** · **THE EARLY CHURCH ERA ·
   70–312 CE** · Chloe.
4. Tap "Ask Chloe →". I read the resolved `href` after the question was held:
   `https://cic-engine.onrender.com/?worlds=post-apostolic-house-church&mode=interview`.
   **No `q`.** `target="_blank"`, so a new tab.
5. The visitor is now in a fresh tab, in a conversation room, with an empty input, and
   their question is in the *other* tab, 1,800px down a marketing page.

The README is honest that the question does not travel (§5, §8 item 5). What it does not
say, and what the flow makes true, is that **the held question is not merely
untransmitted — it is inaccessible at the moment it is needed.** A held question in tab
A cannot be copied into tab B without tab-switching and scrolling back to find it. For
someone who typed a sentence it took them a while to write, "type it twice" is optimistic:
it is "remember it, in a new tab, cold."

And this is the point where the parentage claim matters. §2 credits the offered-question
door to *"the 05 defense's 'offered, not typed' reading of the door (§3.2): real canon
questions, zero fake controls."* The 05 defense's actual design, in its own words, twice:

> *"Five P-cell canon questions, **each a real `?worlds=…&mode=interview` link**;
> constitution S0's own door, offered rather than typed."*
> *"The step map for the person in difficulty goes from 'scroll 2,487px, choose among
> seven centuries' to one click."*

The hybrid took the questions and dropped the property that made them a door. Its six
offered questions are `href="?q=…#who"` — same page, scroll to the picker. The parent
design put the person one tap from a conversation carrying their question; the child puts
them one tap from a list of seven strangers and a rationing notice. That is not a
refinement of the source; it is materially weaker than it, and the README presents it as
its execution.

### 1.4 Without JavaScript the door visibly discards the question

§4 claims *"the whole homepage present and usable without JavaScript, including the door
(a plain GET form)."* §7 is narrower and accurate: *"submitting lands the visitor at the
chairs with the question in the URL."*

Measured with JS disabled: the form submits to `homepage.html?q=I+pray+and+nothing+happens#who`,
the page reloads, the browser jumps to `#who` (y=1,845) — and **the input is empty, the
`#held` block is still `hidden`, and the question appears nowhere on the page.** All
seven names and ten app links are present in static markup, which is the 02 test and it
passes. But the door's *defining* behaviour — the constitution's R.0 grammar, "Your
question, held: … editable, never discarded" — is JavaScript-only.

The six offered questions degrade the same way: without JS each is a full page reload
that jumps 1,861px and shows the visitor nothing about the question they picked.

The hybrid's own §2 table cites *"the 04 review §4.6 killed a control that 'appears to
accept a choice and silently discards it' — so this one says in plain words what it
does."* It says in plain words that nothing is sent ahead. It does not say that in the
no-JS path the question is not held either. In the state where 04's picker was killed —
JavaScript off — this door behaves the same way 04's did: it takes the input and the
input disappears. Saying "nothing is sent ahead" does not cover "and nothing is kept."

### 1.5 Claims that fail measurement

Four, precisely:

**(a) "2.5.8 Target Size at 44px on every control" (§7) and "every control ≥44px" (§4)
are false.** Measured at 390px: on the homepage, "Map" in the nav is 35×49, "About" is
43×44, the "About — how it works" link is 332×**40**. On the tradition page, **fifteen**
controls are under 44px in one dimension — the two breadcrumb links (34px tall), the
four lexicon term buttons (29px tall), the two `experienceToday` links (20px tall), the
reviewer mailto (16px tall), and the nav pair.

To be exact about the standard: SC 2.5.8 requires **24×24** at AA and exempts inline
targets in a sentence. Most of the failures above are inline links in prose and are
exempt; the nav pair clears 24 in both dimensions. **Conformance holds.** What does not
hold is the claim, and this is precisely the finding the 01 review made against 01 —
*"'Target size ≥24×24 on every inline control' — false as stated"* — which 01's defense
conceded as "an overstated README claim." The hybrid read that exchange and made the same
overstatement one notch higher, on a document whose entire authority is that its numbers
are checkable.

**(b) "The AI sentence sits inside the door, before any link" (§2) is false.** I dumped
the DOM order of every `a[data-app]` and the `.ai-line`. Two app links precede it: the
header side door (`Been here before? Go straight in →`, visible to everyone, first-time
visitors included) and the hero's `welcome-back` link. The 05 review's §1.3 charge — *"a
visitor could reach the app without passing the disclosure"* — is answered for the
question links and the chairs, and reopened, one row higher, by the header. The 05
defense's phrasing that the hybrid quotes, *"so no door is passed without it,"* is not
true of this page.

**(c) "Reproduced verbatim (03's verbatim-and-flag rule)" is not what happened to the
dates.** §9 says: *"`world-census.json` carries Marius's dates as `c. 312-451` — hyphen,
no era marker… **Reproduced verbatim** (03's verbatim-and-flag rule); 04 silently added
the 'CE'."* The census string is `'c. 312-451'` with an ASCII hyphen. The page renders
`c. 312–451` with an **en dash**. The missing "CE" was preserved — the substantive half —
but the character was silently normalised, which is the same class of edit the sentence
criticises 04 for. Worse, `world-census.json` carries **Chilo's** dates as
`'c. 325-394 CE'`, also with an ASCII hyphen, and the page renders `c. 325–394 CE`. That
second silent normalisation is not flagged anywhere. A seams list that names one instance
of a discrepancy and silently fixes the identical one two rows down is not the
verbatim-and-flag rule; it is the rule applied to whichever instance the author noticed.

**(d) The proposed dark tints "would pass as text if ever needed" (§6) is true only
against one of two grounds.** All seven clear 4.5:1 against `--ground #17130F`
(4.54–4.60, exactly as published). Against `--surface #1E1913` they measure **4.29–4.34**
— all seven below AA as text. As rings they are fine everywhere, which is the actual use.
But the sentence promises a headroom the values do not have, in a table whose whole point
is that headroom claims get measured.

### 1.6 The rendering bug the measurement pass could not see

`.site-nav a{display:inline-flex}` — and the side door is
`<a …><span class="sd-long">Been here before? </span>Go straight in →</a>`. Inline-flex
makes the span and the following text node two anonymous flex items; the trailing space
inside the span is collapsed at the end of that item's inline content, and flex does not
put it back.

Measured on both pages: at 1280px the span's right edge is at 1009.42 and the text's left
edge is at 1009.42 — **gap 0.00px**. Same at 700px. The header of every page, at every
tablet and desktop width, reads **"Been here before?Go straight in →"**.

I raise it not because it is hard to fix (`&nbsp;`, or `gap` on the anchor, or move the
space outside the span) but because of what it says about the §7 measurement pass. That
pass measured contrast, overflow, tab order, heading outlines, font sizes and animation
counts — all of them things a script can enumerate. It did not measure whether the page
*looks right*, and the one element the direction adds to every header on the site has a
missing space in it. The screenshot shows it immediately.

---

## 2. Does the "named parentage" claim actually hold?

The README's §2 table is the document's central credibility instrument: forty-odd
structural decisions, each with a named source. I spot-checked far more than five —
roughly thirty — against the primary files. **The great majority hold, several of them
impressively.** Verified verbatim or in substance: the 02 review §2.1 crediting exactly
this mark-plus-sentence lockup as *"exactly what the Logo Usage Sheet prescribes"*; the
03 review §4.7's *"every number on it is a promise to keep it current"*; the 03 review
§1.2 *"It never shows the product"*; the 03 review §3.3's disclosure-vs-methodology
distinction (and the 03 defense §3 calling it "the sharpest thing in it"); the 05 review
§5.2's vocabulary table; the 05 review §2.4's *"one mark, in the hero, with the sentence
beside it, would satisfy the rule cleanly"*; the 05 review §2.1 killing the composer and
§5.1 killing the Sunday liturgy; the 05 review §2.6 verifying multi-voice Table in the
repo and not on the engine; the 04 review §4.6's *"appears to accept a choice and
silently discards it"*; the 04 review §7.3 on `--rule` never colouring an interactive
element; the 04 review §1.3 on the caption-not-headline reading; the 04 review §1.4's
*"materially better than the live horizontally-scrolling carousel for scanning, for
keyboard use and for screen readers"*; the 04 review §3.1 "sledgehammer"; the 02 review
§1.2 (the only two buttons ask for money) and §4.2 (*"a hard regression"*); the 01
review §7's *"Take it whole"* for the sidenotes, *"the single strongest piece of writing
produced in D1"* for "Where we are quiet", and *"better engineering than most published
Tufte-style work"*; the 01 defense §2.3's rule that a margin belongs only where a record
stands behind the text; the 04 defense items 2, 3, 4, 5, 7 and 10; the 02 defense §5.1,
§5.2 and §5.3; the 03 defense items 2, 3 and 10 and §2.5's founding sentence; the 05
defense §3.3's *"The honest hero today is Theon's."* Constitution §5.1's three co-equal
doors, §5.4's "one input box… theme chips, not question chips", the §3 state table's
R.0 *"Your question, held:"*, and §2.5a's anti-ghost scope all check out at the lines
cited, and `App.tsx parseDeepLink` really does read only `worlds` and `mode`.

That is a genuinely strong record and the author deserves it said plainly. Three claims
do not hold, and one of those three matters.

### 2.1 The antiquarian concession that neither defense made

> *"No 'Plate,' 'Register,' Roman numerals, lower-roman counters, Alegreya SC, drop
> caps, part-titles, or colophon | **01 defense §4 and 03 defense §2.1 conceded these as
> the antiquarian dress**."*

The 01 defense's §4 is explicitly split into "Contested" and "Conceded." Under
**Contested — these are the grammar of the secular trade and scholarly book**, it names,
one at a time: *Roman-numeral chapter heads* ("Robinson's *Gilead*, Dickens, half the
novels on a paperback table"), *part-title pages*, *drop caps* ("*The New Yorker* opens
every piece with one"), the keyed marginal column, and *a colophon* ("'A Note on the
Type' closes every well-made Knopf hardcover"). What it **conceded** was four things:
numbered plates, the "issue" conceit, the closing spread's scale, and full-screen
part-title pages — the last of those, in its own words, "on scanability grounds (§4.2),
**not religious ones**."

The 03 defense §2.1 is the same shape. It concedes "Plate I.", "Register" as a visible
eyebrow, lower-roman counters and the sticky marginal column — and then says, in the same
paragraph: *"Old-style figures, small caps and **Roman-numeral part numbers** are the
trade-book register the constitution asks for, not a departure from it."*

So the hybrid's decision may well be right — I think it is — but the sentence attributes
to two authors a concession they each argued against by name, in the section cited. This
is the one parentage claim I would call a misrepresentation rather than a slip, because
the whole point of the "named parentage" apparatus is that a reader can check whether the
hybrid is inheriting a settled finding or making a fresh call. Here it is making a fresh
call and filing it as inherited.

### 2.2 "Its exact rebuilt order" is not the order

> *"Tradition page order: who is speaking → where we are quiet → the hardest questions →
> in her own words → the record → the chair | **01 defense §5.1 (its exact rebuilt
> order)** merged with 03 defense §2.5."*

01 defense §5.1, verbatim: *"provenance block first… then **"Where we are quiet"**…
then **the essay in sections**; then **the questions list**… then one door."*

Provenance → quiet → **essay** → questions → door. The hybrid runs provenance → quiet →
**questions** → voice → record → door. The essay and the questions are swapped. The
hybrid's own §3 item 2 explains, well, why the long essay is not carried and is replaced
by record-backed statements — that is a defensible, argued departure. It is not "its
exact rebuilt order," and the reason to be picky is that §3 is titled *"Where the two
inner-page parents conflict, and what was decided"* and lists four conflicts. This is a
fifth, undeclared, with 01.

### 2.3 The fear question that is not there

> *"The questions list: the personal and hardest first, the historian's last | 01 review
> §6.3 ('four scholars and one person'); **01 defense §5.1 (the "For the Wrestling" set
> with the fear question first)**."*

The "For the Wrestling" set in `CiC_W1_Guided_Starters_V0_1_DRAFT.md` has five openers.
The hybrid uses three. The "fear question" — the one 01's defense says it wrongly "put
fifth", i.e. *"Wanting to be eaten alive by animals and calling it the truest way to
follow Jesus — isn't that just a death wish wearing religious language?"* (or, on the
other reading, *"Only one chance at forgiveness after baptism? What happens to someone
who fails a second time?"*) — **is absent from the page entirely**, on either reading. The
list does front-load the personal, which is the substance of the finding. But the cited
warrant names a specific ordering of a specific set, and neither the set nor the
question is on the page.

Also on this row: *"01 review §6.3 ('four scholars and one person')"* — that phrase does
not appear in the 01 review. It appears only in the 01 **defense's** paraphrase of the
review's §6.3 heading. Small, but it is the third citation in a row that points at the
right idea and the wrong document.

### 2.4 Three smaller citation slips, for the record

- *"03's §4, which its reviewer called 'the best-executed block on the page… lift
  whole'."* The reviewer wrote two separate sentences: *"The AI section (§4) is the
  best-executed block on the page"* and, several lines later, *"If this direction dies,
  §4 should be lifted whole into whatever wins."* Splicing them into one quotation with
  an ellipsis, and changing "lifted whole" to "lift whole," is a compression the
  quotation marks do not license. Substance correct.
- *"the fifth (04 §3.4) found it 'would have killed the direction even if the rubric had
  never been written'."* The defense says *"would have killed the direction **against
  Mark's audience ruling** even if the rubric had never been written."* Three words
  removed from inside a quotation without an ellipsis.
- *"05 defense §3.2 ('one primary, six text-link secondaries')"* and *"01 defense §6.2"*
  both point at sections that do not contain the quoted material; the first is in the 05
  defense's §1 concession table, the second is a row in the 01 defense's §1 table citing
  the *review's* §6.2. Trivial as substance; worth noting only because the apparatus
  invites the check.

---

## 3. Did it fix what killed the five, or relabel it?

I will take the brief's four sub-questions in order.

### 3.1 Does the question-first door feel genuinely primary?

**Partly. It is primary in the copy hierarchy and not in the layout.**

What is genuinely primary about it: it is the first `<section>` in `<main>` after the
hero; it carries the page's only filled button and the only form; the H2 is a whole
imperative sentence in display type; the first tab stop inside `<main>` is the input;
the six offered questions beneath it are, without qualification, the warmest and most
person-shaped content anywhere in D1 or D2. Nothing competes with it visually — there is
no carousel, no seven filled buttons, no map band, no status dashboard. On a desktop at
full window height it reads exactly as the README describes.

What is not primary about it: on every phone it is in screen two (§1.1); it is preceded
by 620–900px of hero, of which the first line of text is a sentence explaining the logo;
and, decisively, **it does not lead anywhere the picker does not already lead.** A door's
primacy is not measured by where it sits on the page but by what passing through it
does. Passing through this one moves you 1,000px down the same page, to the same seven
people, in the same century order, with your question repeated back at you as a
courtesy.

I want to be fair about the constraint. The constitution's S0 door was never designed to
open onto a picker — it opens onto R.1 (*considering*) and R.2a (*the proposal card:
which traditions can carry this question, and why*). That routing is genuinely unbuilt,
the README says so in §5, and building a fake version of it would have been the decoy
control the 05 review killed. Given that constraint, "hold the question honestly and
hand the visitor a list" may be the only truthful move available.

But the consequence has to be named without softening: **the phase's central finding was
not "put a text box on the homepage." It was that a homepage which leads with anything
other than a fast, direct, personal way to ask a hard question fails Mark's audience.**
This homepage leads with a text box, and then answers the question with a chronology.
Whether that clears the bar is exactly the judgment Mark has to make, and the README's
§4 sentence — *"The story is told in the order the person Mark named needs it"* — is
where I think it presses its case further than the artifact supports.

### 3.2 Does the merged tradition page resolve 01 vs 03, or inherit both problems?

**This is the strongest thing in the direction, and I could not break it.** Genuinely:

- The merge decision is right and argued (§3): voice before record, disclosure about the
  *tradition* before methodology about the *project*, which is the 03 review's own
  distinction adopted by 03's own defense.
- Both parents' fatal *mechanisms* are gone. 01's sticky running-head door and 03's 156px
  sticky seat bar are both absent; nothing on the page is sticky, so 2.4.11 Focus Not
  Obscured holds by construction and the two device-specific amputations cannot recur. I
  looked for a sticky-marginal collision like 03's flagship bug at 1280 and 1440 with
  real incremental scrolling; the sidenote floats and clears, and there is no collision.
- 01's conceded Level-2 defect is fixed by construction and verified in the AX tree.
- 01's ✲ jump-anchor — its own conceded "sixth verb" — is gone, and the ✲ appears only
  as a picture with a caption saying so.
- The apparatus obeys 01's own narrowed rule: every sidenote on the page sources a
  sentence to a record. None is project admin. I checked all of them.
- 03's finding aid is real and compact, in its founding order, one screen deep, and the
  confidence legend sits beside the contested list rather than before all content — the
  fix 03's defense asked for.

Two inherited problems survive, both small:

- **Length.** 16,634px at 390×844 — 19.7 screens, confirmed. The README declares it and
  hands D3 the trim decision, which is the right posture. But 03's own kill included
  "density below 900px," and this page is denser than 03's `tradition.html` was.
- **03's identical-link-text defect is reproduced on the homepage** and will be
  reproduced seven times over in production. See §7.3.

### 3.3 Is 04's liturgical vocabulary and structure genuinely absent?

**Yes. This is a clean pass and I tried hard to fail it.**

Grep and read-through: no "narthex," no "threshold" as a section name, no "ordo," no
"order of arrival," no rubric, no red italic instruction, no "Silence is kept," no
"Continue when you are ready," no order marker, no station names, no empty
minimum-height silence sections, no scroll-snap, no smooth scroll. The 04 review's own
finding was that the feeling came from *the ordo, the red-italic rubric and the printed
order — none of them words*. None of those three devices is present in any form. The
page has no imposed pacing: nothing is withheld, nothing is gated, and the visitor's
first possible action is on screen one (the header) and screen two (the door).

The one place 04's *discipline* is visible — no reveal-on-scroll, no hover lift, no
transitions, one filled control per screen — is exactly the thing 04's own defense asked
to carry forward, with its reason attached, and it is carried with the reason attached.

One residue, and it is small: **the first text on the page is still an explanation of the
mark.** *"The mark is a table; the opening is the way in — and it never closes."* sits
above the H1, and it is the first sentence a reader's eye lands on. That is structurally
the same move the 04 review §1.3 convicted — *"It explains the logo to a visitor who has
no reason yet to care that there is a logo"* — reduced by roughly 90%: it is 0.9rem, in
muted ink, beside a 52px mark, with the protected hook immediately beneath it at up to
3rem. It is the correct discharge of the Logo Usage Sheet's caption rule and I would not
kill anything for it. But if Mark reads screen one and asks "why is the first thing on
my homepage a sentence about my logo," that is the reason, and it is worth an explicit
choice rather than an inherited one.

### 3.4 Does 02's, 03's or 05's DNA come back under new packaging?

**02: no.** The Atlas is one link and one paragraph in a late section. No map band, no
canvas, no era bands, no threads, no "Where it stands on the Creed" on the homepage, no
palette debt entered. The 02 defense's own §5.2 band is explicitly left for D3 rather
than quietly built. This is the cleanest exclusion of the three.

**03: mostly no, on the homepage.** The method, the status dashboard, the ten-step grid,
the confidence scale as a preamble, the catalogue table, the Roman-numeral identifiers
and the FK-11.6 register are all absent from the front door. The record apparatus lives
one click deep, which is where 03's own defense said it belonged. Two faint traces: the
homepage's disclosure block is 296 words of institutional prose (correct per the brand's
"Always," and well-executed), and the tradition page uses "gravity," "Tensional,"
"Declined," "tested non-finding" and "the Representative says so" as visible copy — project
jargon on a public surface, which the Brand Guidelines' Never list names. "Gravity" is
defined in-line, which is the right mitigation; the rest are not.

**05: this is the one that comes back.** Look at what the picker actually is, rendered:
72px portrait ring · name · role in muted sans · tradition in italic · `dates ·
regions` in sans · a one-line prose tile · two action links — repeated seven times,
under two era headings carrying century ranges, sorted by `start` date.

That is, row for row, the structure the 05 review described and killed:

> *"It sorts human beings by century and offers regions and date spans as the primary
> selection metadata… They do not have a tradition preference. They have a question.
> There is no question-shaped door anywhere in this direction."*
> *"every unit of the page is a transaction shaped like a row: portrait, name, role,
> dates, one-line description, filled button."*

The hybrid answers the *second* half of that indictment properly. The filled buttons are
gone — the seven rows carry text links only, and the page's single filled control is the
door's. The 05 defense's fix ("one primary, six text-link secondaries") is implemented
more strictly than the defense proposed. That is a real change and it changes the feel of
the section a lot.

It does not answer the first half. The selection metadata is still century and region.
The organizing structure is still chronology. The question door sits above it rather than
replacing it, and — because the router is unbuilt — the door's *output* is that
structure. So the honest statement is: **05's IA survives intact, demoted from first
position to second, with a question box installed above it.** Whether "demoted and topped
with a question" is enough of a fix is the central open question of this direction, and
the README's §4 claim that the page is ordered "the way the person Mark named needs it"
does not engage with it.

One more 05 inheritance, this one a defect rather than a shape: see §4.4 on the Table
links.

---

## 4. Constitution and brand conflicts, and the rulings

### 4.1 The rulings that are framed honestly

Most of §8 is exemplary, and I want to be specific about why, because "flagged, not made
quietly" is easy to claim and this document mostly earns it:

- **Ruling 1 (the question door outranks the other S0 doors).** Correctly framed. §5.1
  really does say "equal size, equal weight, no default," this page really does rank
  them, and the README says so in those words rather than arguing the rank away. It is
  the single largest departure in the direction and it is the first item on the list.
- **Ruling 2 (seed-status canon questions on a public surface)** and **ruling 3 (the
  Guided Starters draft)** and **ruling 4 (`records/pahc/*` at `status: draft`)** — all
  three verified true against the files, all three correctly identified as Mark's call
  and not the author's.
- **Ruling 5 (`?q=` in the deep link).** Accurate: `parseDeepLink` reads `worlds` and
  `mode` and nothing else. Correctly filed as a D4 build item, with the copy consequence
  named.
- **Ruling 8 (the mark leaves the header)** — correct, and it is the fix for two Logo
  Usage Sheet breaks the Decision-Log already records against the live header.
- **Ruling 10 ("I want to believe in Jesus, but I can't")** — exactly the right thing to
  surface, framed without steering.
- **Ruling 11 (the `?mode=table` links)** — correctly reports the 05 review's actual
  finding rather than the D3 brief's inverted summary of it. §9's correction of that
  brief is right, and I verified it: the 05 review says *"The claim holds. Multi-voice
  Table is genuinely live in the shipped frontend,"* while the Decision-Log's
  hybridisation entry says the opposite. Good catch, honestly reported.

### 4.2 One stretch that should be a ruling and isn't

**The mark autoplays the joining at a visitor, and §8 does not mention it.**

The Logo Usage Sheet's never-list: *"the motion never replays unbidden and **never plays
the joining at a visitor**."* The hybrid's hero plays the full Arriving sequence on
arrival — `cic-buildC` at 800ms, then `cic-sitdown` at 2,400ms, then the breath — with
no visitor action.

This is not a new question. The 04 review raised it as "at minimum the case that
sentence was written to worry about." The 04 defense contested the reading on the merits
(twice over, with the file open) and then conceded the process point without reservation:

> *"What I concede is the process point: an undefined phrase in a never-list that could
> be read against my first screen **belonged on the stretch list for Mark, and I did not
> put it there**."*

The hybrid read that exchange — it cites the 04 defense eight times — and it also did not
put it there. §8 carries twelve rulings, including one about a `localStorage` courtesy
line. The one that a D2 defense specifically identified as belonging on a stretch list is
not among them. I think the author's substantive position is probably right (the brand's
own reference file autoplays the sequence, byte for byte, which the hybrid copies
faithfully). That is not the point. The point is that the process finding was made, in
writing, in a file this direction says it verified, and it did not survive the synthesis.

### 4.3 The "world" leak, and the rule the hybrid states and then breaks

Two visible occurrences of the banned word on `tradition-chloe.html`:

1. In the "The rooms themselves" silence: *"The catacombs, the house-churches you can
   visit today — those belong to a later **world**."* Verbatim from
   `pahc.limit.material-remains`.
2. In the *first sidenote on the page*: *"…every quote and claim behind them belongs to
   this **world's** own surviving voices."* Verbatim from `pahc.craft.chloe-voice`.

§9 flags the first and says: *"Left as the record has it (a record quote is not the
mockup's to edit); a records-layer fix, worth a task."* It does not mention the second at
all.

Set that beside §2's own adopted rule, which the hybrid quotes from the 05 defense and
files under "Copy marking":

> *"**a quote's provenance clears its facts, not its register**: nothing lifted from app
> code is filed as cleared."*

"World" is not a fact. It is register — the exact category the rule reserves. The 05
review's §2.2 killed this precise move: *"'Verbatim from a real source' is not the same
as 'cleared for this surface.'"* The hybrid states the rule better than 05 did, applies
it correctly to app code, and then publishes the banned word twice on a visitor-facing
page because a *record* said it. Flagging one of the two is better than 05's silence, and
worse than the rule the document adopted. The right move under its own rule is either to
elide with a bracket, or to paraphrase and cite, or to hold the quote until the
records-layer fix lands — and to say which, as a ruling for Mark.

### 4.4 The two Table deep links reproduce a defect D2 already measured and fixed

Both are exactly the hrefs the 05 review §2.6 measured and the 05 defense conceded in
full:

- Homepage: `Set your own table →` → `?mode=table`. Per `App.tsx`'s own contract comment,
  that is *"the Table field, empty."* Per `Launch.tsx:36`, `canConvene = seated.length >= 2`,
  and line 134 renders **"Seat at least two voices," disabled**. I verified all three in
  the source.
- Tradition page, **twice** (the seat line and the closing actions): `Bring Chloe to the
  Table →` → `?worlds=post-apostolic-house-church&mode=table`. That seats exactly one
  voice. The visitor lands on a screen whose primary button is disabled and whose label
  tells them they did it wrong — the 05 review's words, about the identical href.

The one-line fix (`?worlds=a,b&mode=table`, documented in a comment block at the top of
`App.tsx`) is in the record the hybrid says it read. §8 ruling 11 addresses a *different*
question about these links (whether the deployed engine matches the repo) and §9's seams
list, which names six other things, does not name this. The links are inherited verbatim
from the live site, which is a real defence of their *presence* — the 02 review called
their removal "a hard regression" and the hybrid is right to restore the general one. It
is not a defence of shipping a known-broken landing state that a D2 review measured,
named and priced at one line.

### 4.5 The transcript's ground, and "as it happened"

Two small things about §4 of the homepage, which is otherwise the best section on the
page.

First: the section is headed **"One exchange, as it happened"** and the caption says
*"Captured from a live conversation with Theon; the words are unchanged."* The words are
unchanged — I compared them to the PNG line by line. But the *capture* renders the
participant's turn in a blue-washed bubble and Theon's in a bordered card; the hybrid
re-renders both in the constitution's long-form, no-bubbles grammar. That grammar is
**designed and decided** (§4.1, "UPDATED — Mark, 2026-07-18") and is the right target.
It is not, on the evidence of the capture, what a visitor clicking through will actually
see. On a page whose contribution is "show the real interface," and under a D0 seam whose
rule is "don't let marketing language promise an in-app experience that isn't there yet,"
the phrase "as it happened" over a re-rendered UI deserves either a date on the capture
or a one-line note, and gets neither.

Second, and more precisely: the constitution's same paragraph says the transcript's
bubbles are struck and that *"`--gold-wash`/`--lapis-wash` remain in the palette for any
washed grounds elsewhere, but **the transcript no longer uses them**."* The hybrid sets
the whole exchange on `--gold-wash` inside a bordered box. Defensible as a *quotation*
frame rather than a transcript — a leaf of a book, which is the stated intent — but it is
the one ground the constitution explicitly removed from this element, and it is not among
the twelve rulings.

**Third, and this one is not small: the capture contains a warning the transcription
drops.** At the top of `theon-confidence.png`, in an orange-bordered band, is:

> *"Known limitation: refreshing this page or losing connection will lose your
> conversation. Stay in this one tab."*

It is not in the exchange, and it is not in the disclosure block's four "what is
unfinished" items — which cover external review, modes, later eras and the distress path,
none of which cost a visitor anything they have already said. Meanwhile **every app link
on both pages opens in a new tab**, which is exactly the situation the banner exists to
warn about. I could not find that string in the current `cic-poc/frontend/src`, so I
cannot assert the banner still ships — and that uncertainty is itself the argument for
dating the capture rather than presenting an August rendering as "as it happened." For
the person this direction is built for, "you may lose this conversation" is a more
consequential disclosure than "modes have not shipped," and it is the one the page does
not make.

### 4.6 Protected-line and copy repetition

The 04 review's finding — *"Repetition is what turns solemn into rote"* — is not in the
hybrid's inheritance list, and the homepage repeats:

- **"What it means for you is yours to own and share."** twice, fourteen lines apart,
  **inside the same `.before` section** — once inside the "Witness, never recruitment"
  bullet and once in the closing `.measure` paragraph. Both are visible in one screen at
  desktop width. This is a protected line used twice in one breath.
- The distress line twice on the homepage in two wordings (paraphrased in the margin
  note at line 474, verbatim in the disclosure at 504) and again verbatim on the
  tradition page.
- "Where the historical record is thin, we let the silence stand." once per page, which
  is fine.

### 4.7 One privacy nit, offered as a D3 item rather than a finding

The door's copy says *"It stays with you — nothing is sent ahead."* True of the app
hand-off. The script also writes the question into the page URL via
`history.replaceState('?q=' + encodeURIComponent(text))`, which puts it into browser
history, into anything the visitor copies or shares, and into any URL-logging analytics.
`cic-website/_headers` sets no `Referrer-Policy`, so the page relies on the modern browser
default (`strict-origin-when-cross-origin`) to keep the query string out of cross-origin
requests — which it does today, so this is not a live leak. But the promise is absolute
and the mechanism is not pinned. An explicit `Referrer-Policy: strict-origin` (or
`no-referrer` on the app links) plus a clause about the URL would make the sentence exact,
and exactness is what this page is trading on.

---

## 5. Fashionable versus professional, and the religious-feel test

### 5.1 Fashion

I ran the 05 review's own structural audit — the one that convicted 05 by its own thesis
— against this page:

| Product-marketing structural move | Present? |
|---|---|
| Hero: headline + subhead + two CTAs, left column | **No** — centred hook + lede, no CTA pair |
| Product screenshot in the hero's right column | **No** — the exchange is section four |
| Chat composer | **No** |
| Feature list where every row has its own filled CTA | **No** — text links only, one filled control on the page |
| Numbered "three things" three-column band | **No** — a two-column disclosure block, not numbered |
| Roadmap / "what's next" section | **No** — one link |
| Persistent sticky CTA | **No** — nothing is sticky |
| Section rhythm: eyebrow → H2 → one-line intro → content | **Yes**, six times |

Seven of eight gone. The one that remains — eyebrow/H2/intro — the 05 review itself
called "close to universal and I would not call [it] fashion." On this axis the hybrid
does what 05's defense said a fixed 05 would do, and does it more thoroughly than the
defense proposed.

Will it date? The typography, palette, hairlines and flat surfaces are the brand's and
will age as the brand ages. The one dating risk I can name is the *offered-questions
list* — a stack of italic prompt suggestions with arrows, beneath a single text input,
above a fold — which is recognisably the 2023–2026 assistant-landing-page pattern. It is
saved by the content (these are real, specific, painful human questions, not "Write me a
poem about…") and by the absence of a Send-shaped chat frame around it. But it is the
element I would expect to read as period in five years, and the direction should know
that its one genuinely novel surface is also its one fashionable one.

### 5.2 Religious feel

**This passes, and it passes more cleanly than any of the five parents.** I looked at
rendered screenshots at desktop and phone, in both registers, and read every line.

No cross, dove, flame, steeple, glass, ornament, illumination, drop cap, gold rule, small
cap, Roman numeral, plate, part-title, rubric, ordo, silence station, or devotional
address. No "we believe." No scripture as decoration. No second-person spiritual
instruction. The seven portraits are 72px rings in a directory row, not numbered plates —
which was the 01 defense's own diagnosis of what pushed its images toward icon, and this
avoids it. The captured exchange is a skeptic pressing a voice on its evidence, not a
Sunday liturgy narrated in the first person plural — the 05 review's worst-available-
excerpt problem, correctly solved with the material 05's own defense identified.

Two honest observations rather than findings:

- **The closing band on the tradition page** is the one place the register leans
  devotional: a centred, isolated section on vellum, eyebrow "THE TABLE", H2 *"Come and
  join us at the Table"* at up to 2.3rem, two buttons beneath. It is the only centred
  text block on a 16,000px left-aligned page, and it is a protected line in the CTA
  register. The 01 defense conceded that at 3.6rem and in isolation "the *shape* is a
  summons"; at 2.3rem, preceded by a plain sentence about what the reader has just read,
  I think it lands as a door. But it is the closest this direction comes, it is where 01
  also put it, and Mark should look at it rather than take my word.
- **The subject is religious and the site does not hide it.** The tradition page has nine
  occurrences of "doubt," five silences in a communal "we" voice, and 3,000 words about
  bishops and martyrdom. That is content, not register, and the 05 defense's argument
  holds: "the content will be religious." The register around it is a well-set page with
  a question on it, which is what Mark asked for.

The one word I would put to Mark: *"Come and join us at the Table"* is protected and
locked, and it is the most devotional-register string in the corpus. It appears once, at
the very end of an inner page, which is the least exposed placement available. That is
the right call.

---

## 6. Does it serve the person with hard questions, not just the scholar?

This was the phase's converged finding and the reason this direction exists. I will do
what the brief asks and walk it concretely.

**Someone is thirty-four. They stopped going to church eleven months ago after their
pastor covered something up. They have not said the sentence "I don't think I believe
this anymore" out loud to anyone. At 11pm they open a link a friend sent.**

**Seconds 0–10, on their phone (390×740, iOS Safari).** They see: a small ring-and-dot
mark with a sentence explaining what the mark means; *"Twenty centuries of the Church.
One table. A chair pulled out for you."*; three lines saying seven traditions speak from
their own letters, and *"Whether you come curious, with a sermon to write, or with a
question about faith you've carried for years — there is a chair."*; and, at the very
bottom edge, the words **Start with your question**.

That last clause of the lede is the best ten seconds this workstream has produced. It
names them, in the first screen, in their own terms, without a label — 01 named this
audience at screen 22.8; 03 and 05 never named them at all; 02 deleted the one live
sentence that did. Credit where it is due, plainly: **on the first-screen test, this
direction wins, and it wins by a wide margin.**

**Seconds 10–25.** They scroll one thumb-flick. Now they see the input, an unhelpfully
labelled but honest note ("nothing is sent ahead"), the AI sentence, and six questions.
Two of those six are theirs almost word for word: *"The people who taught me the faith
turned out to be hypocrites. Did that happen among you?"* and *"Did any of you ever want
to leave?"* This is the single best thing on the page. It is real, it is sourced, it is
specific, and no other direction in D1 came close.

**Seconds 25–40.** They tap "Did any of you ever want to leave?" The page scrolls
1,861px. Their question is repeated back to them under a lapis rule: **Your question,
held:** — which is a genuinely good moment, and the constitution's own design, built for
the first time.

And then, in the same screen, without another scroll:

> Who would you like to ask?
> Seven Christian traditions from the Early Church and Imperial Church eras…
> **This is a pilot. We're intentionally looking for a limited number of participants
> across four perspectives — general, pastor or teacher, academic, and anyone
> re-examining their faith.**
> **Because of cost, we're asking each participant to keep to about five conversations
> for now — we can't enforce this yet, only ask.**
> THE EARLY CHURCH ERA · 70–312 CE

They have just, for the first time, put down the thing they have not said out loud. The
site's next two sentences are a capacity notice and a rationing request.

I measured this rather than imagining it — those are the actual DOM nodes in the viewport
at y=1,845 after a submit at 390×844. The copy is inherited verbatim from the live site
and is not the author's; the 05 defense conceded its placement should be "above the rows,
where the live site has it," and the hybrid did exactly that. But the live site has no
question door, so on the live site nobody arrives at that paragraph mid-confession. **The
hybrid built a flow that routes the most vulnerable moment on the site directly into the
one paragraph on it that the Brand Guidelines' Never list ("urgency or scarcity") is
about.** That is a new harm created by a new flow, and it is not in §5's sacrifices or
§8's rulings.

**Seconds 40–90.** They read seven entries sorted by century, each with dates and
regions, and pick — on what basis? They have no tradition preference; the 05 review's
sentence applies verbatim. Say they pick Chloe, first in the list. They tap "Ask
Chloe →". A new tab opens. There is a conversation room with an empty box. Their question
is in the other tab.

**What they do next is the whole question.** Some fraction of them retypes it. Some
fraction types something smaller and safer, because saying it twice is harder than saying
it once. Some fraction closes the tab.

**So: does it serve them?** Better than any of the five, unambiguously, on naming, on
vocabulary, on register, on the absence of pressure, on what it refuses to promise, and
on the six questions. And the door it built is real in every respect except the two that
matter most at the end: it does not open onto an answer to the question, and it does not
carry the question through. The README is honest about both — §5 names the retyping, §5
names the missing ranking, §8 item 5 names the missing `q`. Honesty about a dead end is
better than concealment of one. It is not the same as a door.

I will put the fairest version of the counter-argument on the record, because the author
gets a defense and should aim at the real target: *the routing is unbuilt, building a
fake router would be the decoy control D2 killed, and a truthful hold-and-hand-off is the
best available move today.* I think that is right about the router. I do not think it is
right about the hand-off. `?q=` is one line in `parseDeepLink` and it is already flagged
as a D4 item; the offered questions could each have been a real
`?worlds=…&mode=interview` link today, as the 05 defense specified, at the cost of
choosing a tradition on the visitor's behalf. The direction chose "no default" (correctly,
per S0) and paid for it with a picker. That trade is arguable. It should have been
argued in §8 as ruling 13, not settled in §5 as a sacrifice.

---

## 7. Where a real visitor gets lost

### 7.1 First-time visitor

Covered above: the door is in screen two on a phone and clipped on a 900px-tall laptop;
the first conversation link is 2,627px down; the rationing paragraph is in the landing
zone of the door.

One more, small: **the header side door is a trap for a first-timer.** *"Been here
before? Go straight in →"* (rendered without the space, §1.6) is a live link to the app
root, visible to everyone, sitting before the AI disclosure in DOM order, and — unlike
every other app link on the page — it does **not** open in a new tab. A curious
first-time visitor who taps it leaves the marketing site entirely, having read nothing,
and lands on the app's launch screen. The 04 defense's item 4 asked for this as a
courtesy for returning participants; the hybrid also has a `localStorage`-gated
"welcome back" line in the hero that does the same job for exactly the right people.
Showing the header version to everyone is the belt to that braces, and it is the one
control on the page that can move a stranger into the product with zero disclosure.

### 7.2 Returning visitor

Well served, and I verified it: set `localStorage['cic-returning']='1'`, reload, and
*"Welcome back. Go straight in →"* renders in the hero, in `try/catch`, invisible to
everyone else. The header door is there too. The seven are always in the same order,
never in a carousel, never behind a sheet. The record page is one click. This is 04
defense items 3 and 4 executed correctly on the page they belong on.

One claim to correct: §2 says the side door is *"shortened so it costs no third header
row."* Measured by removing the element and re-measuring: at 320 and 390 the header is
168px with or without it — the third row is caused by the five base nav items, so the
claim holds. **At 480px it does not**: 168px with the side door, **118px without**. It
costs a 50px third row at exactly one breakpoint, unnoticed.

### 7.3 Screen reader and keyboard

Mostly excellent, verified from the CDP accessibility tree and by walking Tab key by key.
Clean heading outlines with every Representative as an H4 (02's review found none in the
outline); a skip link that actually delivers you into `<main>`; a real focus ring at 2px
madder / 3px offset, ≥5.86 in light and 7.19 in dark; no keyboard trap; no positive
`tabindex`; Escape returns focus; every new-tab hand-off carries a visually-hidden
announcement; Level 2 of the lexicon reaches assistive tech. Four real defects:

**(a) An orphaned visually-hidden sentence.** `tradition-chloe.html:390` is
`<p class="vh" id="lexhint">Lexicon term. Activate for the full entry.</p>`. I grepped:
**nothing references `lexhint`** — no `aria-describedby`, no `aria-labelledby`, no
script. It is a leftover from an earlier design. A screen-reader user in browse mode
reads it as a bare, contextless sentence in the middle of the "In her own words" section.
Small, and worth naming because §7 says the ARIA was verified in a snapshot.

**(b) The held question is never announced.** After submit, focus moves to
`section#who`, which is `aria-labelledby="who-title"` — so the announcement is "Who would
you like to ask?", and the held question, sitting above the heading inside the section, is
not read. There is no `aria-live`, no `role="status"`, and the `#held` block is revealed
by toggling `hidden`. The constitution's R.0 promises the question is "visible through
every routing state"; for a non-visual user the confirmation that the question was
received is simply absent. One `role="status"` on `#held` fixes it.

**(c) Seven "record" links, two accessible names.** Measured: `Her record →` ×2,
`His record →` ×5. Six of the seven point at the same in-page mockup note (correct for a
mockup) with `aria-describedby`, which patches the description but not the name. In
production, seven links to seven different pages with two distinct names is exactly the
03 review's §3.2/§4.6 finding — *"Seven identical 'Read the record →' links"* — which
03's defense conceded and fixed with a visually-hidden tradition name. The hybrid applies
that fix to the "Ask X" links (each names the person) and §7 claims 2.4.4 on that basis,
while leaving the other seven links in the same list unfixed and unmentioned. Since §5
says "the pattern is one page; the content is seven," this defect ships seven times.

**(d) The in-file comment describes a Tab path that does not exist.** The lexicon script's
comment says the `aria-expanded`-on-focus trick exists *"so Tab can travel from the term
into 'Full entry'."* The "Full entry" button carries `tabindex="-1"`. Measured: Tab from a
term goes to the *next term*, never into the card. No access is lost — Enter on the term
opens the panel, which is the better path anyway — but the comment documents behaviour the
markup forecloses, and §7's *"'Full entry' opens it too"* is true only for pointer and
touch.

### 7.4 Mobile

No overflow at any width; the header wraps and clips nothing (three D1 directions broke
this three ways); the lexicon card is a fixed popover that stays inside the viewport
(measured 621–824 of 844); targets are comfortable; the tap→card→panel sequence works.
The costs are the ones already named: 168px of header chrome at ≤480 (20% of the
viewport, though not sticky, so paid once), the door below the fold, and a 16,634px
tradition page.

### 7.5 Dark mode

I rendered both pages fully in `prefers-color-scheme: dark` and re-measured everything.
Zero text-contrast failures, zero sub-13px, zero overflow, minimum ratio 5.66. The dark
button's boundary is carried by its 1.5px edge, by design and not by accident, which is
the 05 failure avoided explicitly. This is the sixth independent dark register in the
workstream, and it is the first one that does not break — which is itself an argument for
§8 ruling 6 (D3 needs one dark ruling, not a seventh attempt).

---

## Verdict — my adversarial judgment, not a ruling

**It survives, and it should — but conditionally, and the conditions are structural, not
cosmetic. If they are not met, this direction fails the same test that killed its five
parents, just more quietly and with better numbers.**

The honest comparative statement first, because the brief asks for it and it is true:
**this is substantially stronger than any of the five.** It is the only direction in the
workstream with zero measured contrast failures, zero overflow, zero sub-13px text, a
working dark register, a complete and truthful motion inventory, a correct heading
outline, a lexicon that reaches assistive tech, a reading level inside the brand's floor,
and a contrast table I could not find an error in. It is the only one that names Mark's
person in the first screen, the only one that puts six real questions from the record in
front of them, and the only one that has ever built the constitution's R.0. Its parentage
apparatus is a real instrument: I checked roughly thirty citations and the large majority
hold. The tradition page is the best single artifact the phase has produced and I could
not break it.

It survives because — unlike its parents — its failures do not falsify its thesis. 01
died because "the visitor is a reader" was the wrong sentence. 02 died because a map is
the wrong-shaped keyhole. 03 died because its section order ranked audiences backwards.
04 died because the narthex was the wrong room. 05 died because its structure was
borrowed and its IA was an index. This direction's thesis — *put the door first* — is the
right one, and everything wrong with it is that the door is not first, is not yet a door,
and does not lead anywhere.

**What would have to change before I would drop the conditional:**

1. **Put the input in the first screen on a phone.** Not the heading — the input. It is
   at 897px on a 390×844 render and off-screen entirely at 390×660. The hero is 620px of
   centred display type; that is the budget to spend.
2. **Make the six offered questions real doors, or say why they aren't.** The 05 defense
   specified `?worlds=…&mode=interview` per question and the hybrid credits that design as
   its parent. If "no default" (S0) forbids choosing a tradition on the visitor's behalf,
   that is a legitimate answer — but it is ruling 13, argued in §8, not a line in §5.
3. **Move the pilot/rationing paragraph out of the door's landing zone.** Below the seven,
   or below the disclosure. A capacity notice is the wrong second sentence to say to
   someone who has just typed the hardest thing they have typed this year.
4. **Fix the four measured defects and correct the four overstated claims** — the header
   space bug, the orphaned `#lexhint`, the un-announced held question, the seven
   same-named record links; and the 44px claim, the "before any link" claim, the "at the
   fold" claim, and the "reproduced verbatim" claim about the census dates.
5. **Add the rulings that are missing**: the mark autoplaying the joining (the 04 defense
   explicitly said this belongs on a stretch list); the "world" quotes under the
   provenance-clears-facts-not-register rule the direction itself adopted; and the two
   `?mode=table` links that land on a disabled button, which D2 measured and priced at one
   line.

Two of those five (2 and, downstream, the `q` parameter) depend on build work outside this
page, and Mark should see that clearly: **the door cannot be finished on the marketing
site alone.** Until `parseDeepLink` reads `q`, the best this homepage can do is hold a
question and then ask the visitor to carry it across a tab boundary in their head. That is
a D4 dependency, not a design flaw, and the direction is right to have flagged it — but it
means "authorise this direction" and "authorise one line in `App.tsx`" are the same
decision, and the second one is where the door actually opens.

**One line, if only one is read:** the hybrid is the first direction to understand what
the phase found, and it built the room the door belongs in before it built the door.

*— Opus, D2 struggle phase. The author gets one defense before anything here is treated
as settled, same as every other direction in this process.*
