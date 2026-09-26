# D2 defense — Direction 01, Editorial / Long-Form Storytelling

**Sandbox artifact, 2026-09-02. The author's one defense, per the charter. Not a
ruling. Nothing here changes either mockup; the files stand as reviewed.**

I re-read my own `README.md`, `homepage.html`, and `representative-chloe.html`; the
review in full; and the Decision-Log in full, including Mark's two verbatim
2026-09-02 statements. I opened no other direction and no other review. To check the
reviewer's numbers I re-rendered both files in the same Chromium build the reviewer
used (`/opt/pw-browsers/chromium-1194`, via Playwright), under the same font caveat —
`fonts.googleapis.com` is blocked here, so widths and screen counts are in fallback
faces and the mechanisms are not. I also read the four governing texts the reviewer
quotes at the lines he cites (`CiC_Full_UX_Design_V1_0.md` §1, §5.1, §5.7 and the
§4.5 row; the Logo Usage Sheet's public-sentence rule; the Brand Guidelines' Never
and Always lists; the D0 note's seam D), the app's own deep-link contract in
`cic-poc/frontend/src/App.tsx`, and the House-Churches' Guided Starters draft that my
Chloe page says it drew from.

The short version: the reviewer is right about the verdict and about almost every
measurement, and I concede both without re-litigating. I contest four specific
framings where the review overstates what the files or the README say, because the
overstatements change what D3 should harvest. And I ask for a narrower survival than
the direction claimed for itself — named exactly, with the reasons.

---

## 1. Conceded — measured, reproduced, mine

I re-measured before conceding. Every line below reproduced. Where the review gives
a mechanism rather than a pixel, the mechanism is correct.

| Review § | Claim | My re-measurement | Concession |
|---|---|---|---|
| **4.1** | Running-head door pushed off-screen, unreachable, 761–~1000px | Row `scrollWidth` 1001 at 761, 768, 820, 900 and 1000px; door at x 758→1001; reachable again at 1024. `overflow-x:clip` on `body` removes the scroll port, so there is no way to pan to it. | **Fully conceded, and the worst thing in the files.** It is the live site's own documented header bug (`assets/style.css` line 356) reintroduced one breakpoint higher, and it amputates the direction's defining element on the device a long-form site is most read on. One media query and the removal of `overflow-x:clip` fix it; the fact that it shipped in a mockup that claims "one door, always in the same place" is the point. |
| **4.5** | Print stylesheet prints blank pages | Under `print` media after a 1.5s load with no scroll: hook and standfirst at opacity 1, every other `.reveal` block at 0. | Conceded. The README claims "a quarterly should print" and the print block never resets `.reveal`. One line missing. |
| **1.3** | Per-chapter conversation links indistinguishable from body text | `.chapter .begin a` computed `rgb(108,98,87)`, identical to its parent; underline `#E6DFD3` on parchment = **1.20:1**. | Conceded. I styled the direction's only per-tradition path into the product to disappear. This is not restraint; it is the restraint budget spent on the wrong element, exactly as the review says. |
| **1.1** | Contents is not "one screen below the masthead" | `#contents` at 2.3 screens (1440×900) and 3.4 screens (390×844). | Conceded. The README sentence is false as written. |
| **1.2** | Jump targets fade in after you arrive | `.js .reveal` starts at opacity 0 and transitions over 1100ms; an anchor jump lands on a block that has not yet intersected. | Conceded. Anchor and focus targets must render instantly; the reveal should only ever apply to blocks scrolled into, never jumped to. |
| **1.5** | "Target size ≥24×24 on every inline control" is false as stated | Inline link heights 18, 21, 22px on both viewports. | Conceded as an overstated README claim. Conformance rides on SC 2.5.8's inline exception; I should have said that rather than asserting a floor I only met on the padded controls. |
| **2.2A** | The ✲ marker breaks the one-grammar rule | Constitution §4.5 row: "citation hover/tap · full — same grammar, ✲ marker." §5.7: "no feature may introduce a sixth verb." My `a.cite` is a plain `href="#n"` jump. At ≥1100px the target is already visible in the margin, so the click only scrolls the reader's sentence off the top. | Conceded. Same glyph, same pigment, different verb — and my README's "nothing here contradicts the constitution's app rules" is wrong on the one rule the constitution set in bold. The fix is to put ✲ under the same `.lex` grammar I built for terms on the Chloe page (hover = the note as a card, click = the source in the side panel). That is more of this direction, not less. |
| **2.2B** | Public sentence never beside the mark at first contact; repurposed as ornament; absent from the Chloe page | Logo Usage Sheet line 14: "The mark never appears at first contact without this one plain sentence beside it." Homepage: running head has the mark alone; the sentence is a pull quote at line 348 with no mark; it repeats at the footer beside the mark. Chloe page: the sentence does not appear. | Conceded on all three counts. Using a protected line as a decorative pull quote was a misuse, not a stretch, and I did not flag it. The live site's header has the same first-contact gap (the Decision-Log records it); reproducing a known bug without naming it is my error. |
| **2.2C** | At ≤480px the Chloe page shows a bare ring, no wordmark | Verified: `.brand .wordmark` `display:none` at 390px, and the Chloe page has no masthead beneath it. | Conceded. The README's defense of the lockup ("the wordmark is the masthead directly beneath") is true of the homepage only. |
| **2.2D** | The Arriving motion plays in the footer, on load, to nobody | The keyframes are copied from the live stylesheet and are time-triggered; the footer is at ~13,000px desktop, ~20,000px phone. | Conceded. The README says "in the colophon"; the markup put it in the footer and never gated it on visibility. Either it stays in the header as the live site has it, or it plays when the footer intersects. |
| **2.2E** | Seven census tints never re-checked on the dark ground; ribbons vanish | Reproduced exactly: `#7A2E2E` 1.99, `#9d174d` 2.34, `#2B5F8A` 2.73, `#A0522D` 3.29, `#7c3aed` 3.24, `#0f766e` 3.38, `#b45309` 3.68 on `#17130F`. `--rep` is set inline per chapter and the dark block never redefines it; the kicker is rescued by a gold-leaf override that also erases the per-tradition color in dark mode. | Conceded. I found the light-mode half of the D1-closure's cross-validated bug and shipped the dark-mode half. |
| **2.2F** | Two type sizes under my own 13.6px floor | `.plate figcaption` .84rem = 13.44px; `.chapter-nav small` .82rem = 13.12px. | Conceded. |
| **2.2G** | `overflow-x:clip` hides overflow rather than preventing it | It is what made 4.1 silent. | Conceded. |
| **2.1 (3)** | Alegreya SC is a single point of failure | With the face absent, `.sc` renders letterspaced lowercase; no `font-variant-caps` fallback. | Conceded. `font-variant-caps:small-caps` on the fallback stack is the obvious guard and I did not write it. |
| **3.1** | Two of five homepage sidenotes are project admin; Plate VI's caption is a build-status line | Sidenotes n2 and n5 say "Numbers are checked with Mark before anything prints" and "this direction inherits that debt and pays it at build." Both are draft-tagged, and both are still notes to the coordinator printed in the margin of a public page. | Conceded — for the homepage. See §2.3 below for why I do not concede the generalization. |
| **3.3** | "About a twelve-minute read" overstates by ~60% | My count, rendered `article.article` text with draft tags, the hidden hint, and card text removed: **1,228 words** body-only (the review counted 1,518; either way, 5–8 minutes). With every sidenote, lexicon panel, the provenance block, caption and standfirst opened: 2,225 words, about 11 minutes. | Conceded. The figure was the everything-opened number, not a fabrication — but the person deciding whether to begin reads the body, and the review's real point is right regardless: a fee posted at the door is the wrong instrument for this audience. The label goes. |
| **4.2** | Phone homepage is 24.5 screens; first face at 5.5; Atlas gone from the mobile header | Reproduced: 20,692px; first portrait at screen 5.6; `.optional` links hidden ≤760px, so Atlas is reachable on a phone only from the contents list or the essay. | Conceded. The README named scanability as a sacrifice; it did not name that the Atlas — the site's second primary surface — loses its nav anchor on the most common device. |
| **4.3** | The contents routes to reading, never to a conversation | Every entry in `#contents` is an in-page anchor. | Conceded. This is the sharpest craft finding in the review and the cheapest to fix: the index needs a conversation link per chapter. |
| **4.4** | Level-2 card is sighted-only; `aria-expanded` with nothing exposed; smooth-scroll rides focus; Chloe page ≤760px hides the running title and the Contents link | All four reproduced. | Conceded. The Level-2 defect matters most: the constitution promises two tiers to everyone and I built the short tier for sighted users only. |
| **6.2** | The one door delivers a person in doubt to a seating field, while the working path is the invisible gray link | `App.tsx` lines 18–24, the app's own contract: `?worlds=<id>&mode=interview` → "straight into the conversation, no waiting place"; `?mode=table` → "the Table field, empty." D0 seam D: the multi-voice Table "does not yet exist on the new [engine] architecture." My homepage's running-head door and closing door both go to `?mode=table`. My Chloe page's running head goes to `mode=table` and its closing door goes to `mode=interview` — the same page contradicts itself. | **Conceded, and this is the finding that changed my mind, not the bug list.** I sent the person Mark named as his heart to an empty configuration screen for a surface that is not built, through the largest link on the page, and hid the path that works. Stretch 1 was not a governance footnote. It was the wrong decision, and I made it in the README on purpose. |
| **6.3** | The five "questions people bring" are four scholars and one person | The House-Churches' Guided Starters draft has a section titled **"For the Wrestling (hard questions welcome here)"** with five openers: "Isn't 'we're still arguing about it' just a nicer way of saying you don't actually know?" · "how can you honestly call yourselves the same church?" · the *ministrae* question · "isn't that just a death wish wearing religious language?" · "Only one chance at forgiveness after baptism?" I took two of those five and filled the other three slots from "First Visit" and "Going Deeper," and put the fear-question fifth. | Conceded. The reviewer is right about the selection, and the material to fix it is already in the tradition's own record — which cuts both ways: the direction did not lack doubter-shaped questions; I chose the historian's over them. |
| **4.6** | Six of seven "Read the introduction" links are dead | Mockup artifact, unscored by the reviewer. | Acknowledged as what it is: the content debt of §3.4, visible. |

Nothing in that table is a taste dispute. I am not spending the defense on any of it.

---

## 2. Contested — where the review overstates, with the evidence

### 2.1 "One door … that is the entire CTA inventory — false" (§1.4)

The README's sentence, in full: *"'Come and join us at the Table' sits in the running
head of every page, in madder, and returns as the closing line of the issue and of
each chapter; each chapter also carries a quiet 'begin a conversation with X · bring X
to the Table' line. That is the entire CTA inventory."* That is one running-head door,
one closing door, and two lines per chapter — 1 + 1 + (7 × 2) = 16 app handoffs, which
is exactly the count the review measured (9 `mode=table` + 7 `mode=interview`). The
README enumerates the inventory the review says it conceals. "One door" was always
the claim that there is one *primary* CTA phrase in one *fixed place*, not that the
page contains one link.

What the review actually found under this heading — that I kept 31 in-page anchors at
full visibility and dimmed the sixteen product links — is true and conceded in §1. I
contest only the charge that the README misrepresented the inventory. It did not, and
the distinction matters for D3: the *fixed-position door* idea is sound and worth
keeping; the *dimmed chapter lines* were a styling error, not a consequence of it.

### 2.2 "23 uses of 'never' … a run of disclaimers" (§3.2)

Counted from the rendered visible text of both pages with draft tags excluded: **12 on
the homepage, 8 on the Chloe page, 20 total.** (The review's 23 most likely includes
CSS comments — "never re-hidden," "never a centered modal" — which no visitor reads.)

Of the twenty, nine are Representatives describing history that did not settle —
*"Which pattern was truer we never agreed"* · *"never fully settled whose word binds"*
· *"Most of us were never asked"* · *"we never settled, and I will not settle it for
you now."* Those are the opposite of the denial shape the brand's Never list targets.
They are a voice refusing to claim more than its record holds, which is the
constitution's own "let the silence stand" done as prose.

About seven are the shape the review means: two "never pretends otherwise," "never a
person who lived," "never one person's biography," "no claim to be any woman its
sources name," "witness, never recruitment," "It will never try to convert you." The
Brand Guidelines' Always list exempts "a clarifying contrast naming what kind of thing
this is," and several of these are exactly that — but the review is right that stacked
across seven plate captions and a provenance block they read as a page apologizing for
itself. I concede those seven and the captions as a set. I contest the count and the
generalization to the Representatives' own speech, because that speech is the part of
the direction worth keeping and it should not be tarred with the captions.

### 2.3 "The apparatus is a vacuum … a structural property, not a drafting slip" (§3.1)

The review's evidence is the homepage. The Chloe page is the counter-evidence. Its
seven sidenotes are seven for seven sourcing: Polycarp *Philippians* 13 and *1 Clement*
for correspondence as the organizing force; *Didache* 9–10 for the table prayers;
Pliny *Letters* 10.96 for the outside account; Ignatius *Ephesians* 4 against *1
Clement* and Hermas for the bishop-or-council question; Pliny 10.96–97 and Trajan's
reply on exposure; *Didache* 1–7 on the Two Ways; the tradition's own Absent Stories
for the silences. Not one of them is admin. The mockup's own best-effort demonstration
leaked *where there was no record behind the text* — the homepage essays about the
project — and held *where there was one*.

So the structural lesson is real but it is not the one the review draws. It is not
"a visible margin fills with whatever the team is thinking about." It is "a visible
margin belongs only where a record stands behind the text — Representative pages, not
marketing essays." I concede the homepage apparatus entirely on that basis, and I ask
that the Chloe page's apparatus be judged on its own seven notes.

### 2.4 "Four of the five conditions delete the philosophy statement's own three consequences" (§8)

This is the review's central structural claim and it is the one I most need to
correct, because it decides whether the record says *the thesis is wrong* or *the
thesis is incomplete*. The README's three consequences are (1) sequence over
navigation, (2) apparatus visible in the margin, (3) one door in a fixed place.
Against the review's five conditions:

- **Fix §4.1** — a bug. Touches nothing.
- **Make conversation links the most visible, and put them in the contents** — the
  README already counted those links as part of the inventory (§2.1 above). Changing
  their color from ink-faded to madder and adding them to the index touches none of
  the three consequences.
- **Drop the periodical framing** (masthead, issue, plates, colophon, part-titles,
  Roman numerals, the byline) — none of those is one of the three consequences. They
  are the dress. The review itself keeps "the reading column, the sidenotes, the
  measure, the drop caps" — which is consequence (2) intact.
- **Lead with "Where we are quiet" and the AI disclosure, chronology below** — this
  reorders the *front matter*. The chapters remain in sequence. It modifies what
  precedes consequence (1), not consequence (1).
- **Add a question-shaped entry point** — this is the one condition that genuinely
  changes a consequence: (3) "one door" becomes a door and a question, and (1)
  sequence is no longer the *sole* organizing principle.

One of five, not four of five. I am not raising this to dodge the verdict — I accept
the verdict below. I raise it because D3 will read the review's sentence as "the
craft is excellent, the philosophy is wrong," when the evidence supports "the craft
is excellent, the dress is wrong for this audience, and the philosophy is missing
one thing." Those lead to different syntheses.

### 2.5 Two small factual corrections, for the record

The AI question is raised in the opening essay's **third** paragraph, not its fourth
(the review's §5 says fourth). And the byline "Introduced by Chloe · Household Leader"
is a category label the brand requires — the Representative must be labeled as the
speaker — so I keep that half of the byline and cut the reading time, rather than
cutting the byline whole as §6.4 suggests. Neither changes anything above.

---

## 3. The thesis — what I concede and what I hold

The review calls two charges unpatchable. I answer them separately, because they are
not equally true.

### 3.1 "The re-assessing audience is named once, at screen 22.8 of 24.5" — conceded whole

Reproduced: "anyone re-examining their faith" appears once, in the pilot paragraph
under the closing door, at screen 23.1 of 24.5 on a phone. The distress-support line
appears once, in the second essay, at screen 19.8. Nothing in the first five screens
addresses a person who arrived hurting.

The README named the cost, in its own words: *"someone who wants a conversation in ten
seconds gets less encouragement than any other plausible direction offers."* I priced
that sacrifice against the impatient visitor. Mark's 2026-09-02 statement says the
visitor I was describing is his heart — not impatient, but in need. That is the
misjudgment, and the review is right that it is not CSS. It is the consequence of
building for the charter goal this direction chose ("clear storytelling") and letting
the person who came with a question wait until the story was told. The direction was
commissioned before Mark's ruling was recorded; that is context, not a defense.

### 3.2 "Organized by chronology, priced in reading minutes, deletes the question door" — two-thirds conceded, one-third held

**Reading minutes: conceded.** The label goes, everywhere, for the reason in §1.

**The deleted door: conceded, and it is worse than the review says.** I removed the
constitution's *Start with your question* door on the theory that "the three doors
live in-app" (README, stretch 1). Two facts I should have checked defeat that: the
app's own contract makes `?mode=table` an empty seating field (App.tsx line 24), and
D0 seam D records that the app has *no guided-onboarding three-door threshold* built
either. So the question door I said would live in-app does not live anywhere. A
person with a question has no surface on the site or in the app that takes it. That
is a real D3 problem — whether the site routes a question itself, or the app builds
its threshold first — and I cannot wave at it; I can only stop claiming it was
handled.

**Chronology: held, with an argument.** The review reads chronological chapter order
as "a reader's ordering" that assumes interest rather than need. I think that
mistakes what the alternative would be. The other orderings available to a marketing
site — by theme, by "which tradition is for a doubter," by relevance to a question —
all pre-sort seven traditions by a need the site cannot know. That sorting is
exactly the job the constitution gives to the question door and its routing
(R.0–R.2c: the question held on screen, a proposal that names which traditions can
carry it *and why*). It is not a job for the information architecture. Chronology is
the one order that does not pretend to know the visitor's question; it is the order
the Atlas already uses; and it is honest about the material, which is a
four-century sequence in which Marius cannot exist before Chloe.

So the honest position is: chronology *under* a question is coherent, and chronology
*alone* is the failure. The review says fixing this "means giving up
sequence-over-navigation, and sequence-over-navigation *is* the direction." I say it
means sequence beneath a door that takes a question, which is what a serious book
with a real preface is. But I concede the review's stronger point beneath that: the
direction's first sentence — "the site is a book, and the visitor is a reader" — is
not the sentence for Mark's heart audience. The visitor is a guest, who may become a
reader. That is a different opening sentence, and I accept that it makes this a
different direction at the whole-site level.

### 3.3 The verdict

**I accept "dies as the spine" for the direction in its D1 form.** What I ask the
record to show is the cause of death: ordering and one wrong door — the front matter
that talks about the project before it talks to the person, and a primary CTA sent to
an empty field for an unbuilt surface. Not the register, not the reading conditions,
not the apparatus, not the chapter pages. Those are conceded on craft points that are
each a line or two, and on one dress question (§4) that I address separately. The
cause of death determines what D3 harvests, so I am precise about it.

---

## 4. Religious feel — where I disagree, and where I do not

The review flags this as its most interpretive judgment and asks to be pressed. I
press on the attributions and yield on the cumulative effect.

**What the review concedes first, and I hold it to:** no cross, dove, flame, glass or
steeple; no scripture as decoration; no worship vocabulary; no devotional address; no
"we believe"; the AI question raised by the site itself in the opening essay's third
paragraph before any Representative speaks. That is the Brand Guidelines' first
"Always," done. The register the review objects to is *formal*, and it names seven
devices. I take them one at a time.

**Contested — these are the grammar of the secular trade and scholarly book, in print
on every shelf today:**

- *Roman-numeral chapter heads.* Robinson's *Gilead*, Dickens, half the novels on a
  paperback table. The oversized watermark numeral behind a title is a magazine
  feature device, not a missal's.
- *Part-title pages.* Every novel over three hundred pages has them. The constitution's
  own phrase is "trade book," and a trade book has parts.
- *Drop caps.* *The New Yorker* opens every piece with one. The review itself says
  "keep … the drop caps if you must."
- *A central column with keyed marginal notes.* The review calls my implementation
  "Tufte-style" three times, and Tufte is the referent a web reader actually has —
  not the *glossa ordinaria*. The Talmud page and the Loeb facing-text are the other
  two live referents, and neither is a Christian liturgical object.
- *A colophon.* "A Note on the Type" closes every well-made Knopf hardcover. In my
  markup the word never appears on screen; the section is titled "Keeping the door
  open."

The constitution's line 50 — "a beautifully set trade book on parchment — warm,
unhurried, nothing antiquarian" — is real, and I take "nothing antiquarian"
seriously. But the review applies it to devices that are the current, ordinary
furniture of serious books, and the same line asks for a *book*. A trade book with
parts, numbered chapters, a reading measure, and notes is what "trade book" means.

**Conceded — these are mine, and they are the ones that tip it:**

1. **Numbered plates.** "Plate I–VII," full-column, with a ribbon. That is museum and
   monograph grammar, and combined with the locked portraits — a veiled woman holding a
   cup in both hands; a bearded man in undyed wool holding bread — it does push the
   images toward icon. The portraits are not my decision; presenting them at plate
   scale, numbered, is entirely mine, and the review is right that it is the single
   largest change in how they read. The plate numbering and the ribbon go; the
   portraits set smaller, captioned by name and role only.
2. **The "issue" conceit.** "The First Centuries · Seven Christian traditions" as an
   issue line under a masthead is a periodical's grammar, it is what §3.5 correctly
   says has no issue two designed, and it frames the reader as a subscriber. It goes.
3. **The closing spread's scale.** One protected sentence at 3.6rem, alone on a
   screen, after a long Christian-history read. The words are the constitution's own
   CTA register and stay; the review is right that at that scale and isolation the
   *shape* is a summons. Set at reading scale, beside a plain line about what happens
   when you click, it is a door and not an altar.
4. **Full-screen part-title pages** — conceded on scanability grounds (§4.2), not
   religious ones: a rule and a label do the same work at a fraction of a phone screen.

**The judgment call I cannot make for Mark.** He chose the manuscript palette and the
words "trade book on parchment," and the review's honest formulation — *"it looks like
the thing it is about, rather than like a place where you can ask about the thing"* —
is the right test. I would rather lose the plates, the issue line, and the scale of
the closing door than fail that test. What I would keep — the column, the measure,
the sidenotes, the numerals, the drop caps — is what makes a book *serious*, and
"engaging and trustworthy (scholar)" is Mark's own phrase for what he wants. If, with
the four concessions above applied, he still hears it as religious rather than
serious, then the reviewer's reading is the right one and the register goes with the
spine. I do not think that is the likely reading, but it is his to make, and I would
not want it made on the un-conceded version.

---

## 5. What I ask to survive — exactly

I am choosing the charter's second path: concede the whole-site direction, name the
parts. Each with the reason it earns its place under Mark's own two statements, and
with the fixes from §1 that it carries in.

**1. The Representative chapter page, as the inner-page pattern for every tradition
— whichever spine wins.** `representative-chloe.html` is the direction's real
argument and the review's own §6.5 and §7 say so. Rebuilt in this order: provenance
block first (AI disclosure at 13.70:1 before Chloe speaks — keep as is); then **"Where
we are quiet"** directly after the portrait and before the essay, per the review's own
condition; then the essay in sections; then the questions list rebuilt from the
tradition's **"For the Wrestling"** starters with the fear-question first and the
historian's questions after; then one door to `mode=interview` with "bring to the
Table" as the quiet second line. With the reading-time label cut, the ✲ marker under
the lexicon grammar, a screen-reader-reachable Level 2, the running title and
Contents link kept at ≤760px, and the wordmark kept at ≤480px.

Why this serves the heart audience: a person who left because the church lied to
them needs, before they ask anything, to see the thing refuse to lie. "Where we are
quiet" is that refusal in four hundred words, drawn from the tradition's own Absent
Stories, and the review calls it the strongest writing in D1. It exists because this
direction gave a Representative room to say it. That is "no pressure, just witness"
executed as text.

**2. The sidenote implementation, whole.** Note inside the paragraph after its
marker, floated to a reserved margin at ≥1100px, in-flow below — correct reading
order for assistive tech, which the review says almost nobody manages. With the
narrowing from §2.3: only on pages where a record stands behind the text.

**3. The Representative "we" register.** A voice that keeps disagreement visible
("I carry Rome's claim, Constantinople's, and Milan's alike, and I will not tell you
which one wins"), names what rests on one witness, and says when the record runs out.
This is "trustworthy (scholar)" without institutional distance — Mark's own
distinction — and it is the voice a doubter can trust precisely because it will not
close a question to win them.

**4. The index pattern, with conversation links.** The contents at phone width is,
by the review's account, the best thing on the homepage; it needs a "talk with X"
link per line. As a pattern for whatever the winning spine uses as its tradition
list.

**5. The reading conditions as V2's floor for any long text.** 20px/1.55 on a 38rem
measure, AAA (7:1) for running prose, reduced-motion parity, focus-not-obscured, a
clean heading outline. All verified by the review; none specific to this direction's
dress.

**6. The verified-against-data discipline and the draft-tag convention** — every
fact checked against `world-census.json`, every unreviewed line marked. The review
found no lie. That should be the standard for D3's copy whatever it looks like.

**What I give up, named so there is no ambiguity:** the periodical framing (masthead
issue line, "In this issue," numbered plates, ribbons, the colophon *as a section*);
sequence as the *sole* organizing principle of the homepage; stretch 1 in its
entirety (`mode=table` as the primary door, the question door "living in-app");
marginal apparatus on essays about the project; the footer motion; the reading-time
byline; the seven-caption disclaimer set; the full-screen part-title pages; and the
first sentence of the philosophy, "the visitor is a reader," which is not the
sentence for the person Mark named.

---

## 6. Closing

If the review had been the bug list alone I would have written "survives, fix the
nine things," and I think the reviewer would have too — he says as much. What the
bug list could not have told me, and the review did, is where the direction was
actually pointed. I built a beautiful room for someone who arrived curious, and I sent
the person who arrived hurting to an empty seating field through a link I had colored
to disappear, with a note saying it would take twelve minutes. That is not a craft
slip and I do not defend it.

What I defend is narrower: that the direction's *content* — Chloe's page, the silence
named, the sourcing in the margin, the voice that will not settle a question to win
you — is the most doubter-serving thing D1 produced, by the review's own reckoning,
and that it was produced *because* the direction gave a tradition room to speak at
length in its own voice. The direction put it in the wrong place and behind the
wrong door. Those are ordering and routing decisions, and they are the ones I
concede. The room itself should stand.

*— D1 author, Direction 01. One defense, filed.*
