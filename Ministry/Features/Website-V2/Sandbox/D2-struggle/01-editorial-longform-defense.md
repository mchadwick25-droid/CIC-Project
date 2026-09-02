# D2 defense — Direction 01, Editorial / Long-Form Storytelling

**Sandbox artifact, 2026-09-02. The one defense the charter allows. Written by the
direction's author, having read only my own three files, the review against them, and
the Decision Log — no other direction, no other review.**

Re-measured, not taken on trust: I drove the same Chromium
(`/opt/pw-browsers/chromium-1194`) headless against scratch copies of my own two pages
at 500 (Chrome's headless floor — the reviewer's 390 figures are used where mine cannot
go that narrow), 761, 768, 820, 900, 940, 1000, 1024, 1280 and 1440 wide; counted words,
links and "never"s by script; and read the exact lines of the constitution, the Logo
Usage Sheet and the Brand Guidelines the reviewer quotes, at their source. Same font
caveat as the reviewer: the font host hangs from this sandbox, so every layout number is
in fallback faces. Where my number and the reviewer's differ I say so; mostly they are
identical to the pixel.

---

## 0. The short version

**I concede the whole-site verdict.** The homepage as a chronological issue of a
quarterly is the wrong first thing to hand the person Mark named as his heart. A visitor
who arrives in need is not, by default, a reader, and the first screen of my homepage
hands them a book. That is consequence 1 of my own philosophy statement — "sequence over
navigation" — and I give it up. I am not going to spend my one defense arguing that a
person with a hard question should be met with 70 CE.

**I contest four things, with evidence** (§2 and §3): that the "unpatchable" bundle is
unpatchable as a bundle — five of its seven items are one-line or one-attribute fixes,
and the two that are structural belong to the homepage I have just conceded; that the
direction *deletes* the constitution's "Start with your question" door — it mis-targets
it, which is a different and much smaller thing; that the marginal apparatus is a
"vacuum" — on the one tradition page that exists it is seven-for-seven real citations
from a build record that already exists; and, as the reviewer invited, the codex reading
of the register — partly.

**I ask for a specific, narrower survival** (§4): the Representative introduction page,
in its actual order, as the canonical inner-page pattern for every tradition; "Where we
are quiet" promoted to the homepage's first screens, in the project's own voice; the
per-tradition unit a tile cannot give; the sidenote implementation whole; the reading
conditions as the accessibility system; one persistent door — pointed at the right
place. The reviewer's own §7 already harvests four of its six items from that one inner
page. I am asking that the page be kept as a *pattern with an order*, not as a bag of
parts, because its two best pieces do not work outside the register they were written
in.

---

## 1. Measured facts: what I re-verified and concede

Every row below I checked against my own markup. None of it is re-litigated. Fixes are
named so D3 does not have to rediscover them, not because naming a fix rescues the
direction.

| Review § | Claim | My re-measure | Verdict |
|---|---|---|---|
| 4.1 | Running-head door off-screen 761–~1000px; `overflow-x:clip` makes it unreachable | Document width **1001** at 761, 768, 820, 900, 940, 1000; door right edge at **1001**; fits at 1024 | **Conceded.** Worse than the review says: my own CSS comment at `homepage.html` 105–107 congratulates itself on fixing the live site's phone version of this bug, then reintroduces it one breakpoint up. `clip` was meant as a belt; it became the only thing between the bug and the visitor. Fix: `.optional` hides below ~1000px, not 760, or the door shortens between 760 and 1000. Clip stays only once the header can no longer overflow. |
| 4.5 | Print prints blank: `.reveal` never reset under `print` | Mechanism confirmed from `homepage.html` 117 and 291–296: no print reset | **Conceded.** One line missing, plus `a[href^="http"]::after{content:" ("attr(href)")"}` so the apparatus survives paper. "A quarterly should print" was a claim I did not test. |
| 1.3 | 14 conversation links same color as body; underline at 1.196:1 | `.begin a`: `rgb(108,98,87)`, parent `rgb(108,98,87)`, underline `rgb(230,223,211)` — exact | **Conceded.** A deliberate "quiet" that was the wrong quiet. The direction's only per-tradition path into the product is its least visible control. Fix: madder, a real underline, and the links carried into the contents (see §4). |
| 1.1 | Contents "one screen below the masthead" — false | 2,026px at 1440 (the reviewer's figure exactly); ~3.1 screens at 500 wide | **Conceded.** README line 25 is wrong as written. |
| 1.2 | "One click from anything" — three clicks, two animated scrolls, a fade at the destination | Mechanism confirmed: `scroll-behavior:smooth` on `html` (53), `.reveal` at `opacity:0` (117), observer at 657 fires on arrival | **Conceded.** The live site's two-tap path to a madder button is better at this task than my mockup. Fix: smooth scroll only for short in-page hops, applied by script on click, never on `html`; anchor targets get `.in` immediately. |
| 1.5 | "≥24×24 on every inline control" — overstated | `.begin a` 18px tall; `a.cite` padding `.2em .25em` | **Conceded.** Conformance via SC 2.5.8's inline exception, as the reviewer grants — but I claimed a floor I did not meet, and constitution line 345 gives ✲ markers a 44px hit area on phone, which `a.cite` also misses. |
| 2.2A | ✲ given a sixth verb (jump anchor) and it displaces the reading position | `a.cite href="#n1"` (155, 342); note already visible at ≥1100 | **Conceded.** README's "nothing here contradicts the constitution's app rules" was false on this point (constitution 491–493, verified). Fix: give ✲ the `.lex` grammar the same file already implements — hover/focus = the note as a card, click = panel with note and source line; below 1100 the note stays inline as the no-JS fallback. That also satisfies the 44px rule. |
| 2.2B | Public sentence: 0-for-3 on the homepage, absent on the Chloe page | Confirmed at 305–308 (mark, no sentence), 348 (sentence as pull quote, no mark), 634 (footer); Chloe: absent | **Conceded.** The pull quote is the worst of the three: I took the one line the Logo Usage Sheet says is "said once, never elaborated" (lines 12–15, verified) and set it as ornament. Fix: sentence beside the mark in the masthead — the first full-size contact — and beside the footer mark on every page; pull quote deleted. |
| 2.2C | ≤480px Chloe page: mark with no wordmark, no masthead beneath | `representative-chloe.html` 81; page has no masthead | **Conceded.** Fix: keep the wordmark on inner pages; hide "Contents" instead (the chapter-nav at the foot carries it); shorten the door. |
| 2.2D | "Arriving" plays on load, in a footer fifteen screens down | Keyframe delays at 279–284 are time-based; `.play` is static in the markup (631) | **Conceded.** The README described an intent — "once, in the colophon," on arrival there — that the code did not implement. One `IntersectionObserver` adding `.play`. |
| 2.2E | Dark mode: `--rep` ribbons at 1.99–3.68:1 | Inline `--rep` at 390–548; dark block 41–47 does not redefine; ribbon at 215 uses it | **Conceded.** I knew the tints fail as text on dark (that is why 244 collapses the kickers to gold-leaf) and did not say so or handle the ribbon. I found the light half of the D1-closure bug and shipped the dark half. Fix: a dark set of seven tints declared beside the light ones. |
| 2.2F | 13.6px floor broken twice | 13.44px caption (homepage), 13.12px chapter-nav small (Chloe) | **Conceded.** Two declarations. |
| 3.3 | "About a twelve-minute read" overstated ~60% | 1,520 words in the article; 1,102 of Representative-voice prose | **Conceded** — and the label goes entirely, not just the number (§4). |
| 3.1 | Two of five homepage sidenotes are project admin; a build-status line in a plate caption | n2 (346), n5 (601), Plate VI caption (542) | **Conceded as drafting.** Those are notes to Mark I put in the visitor's margin. On the structural inference, see §2.3. |
| 3.2 | ~23 "never"s; captions read as a run of disclaimers | **20** in visible copy (12 + 8); 30 counting CSS and HTML comments | **Conceded in substance.** The two in the provenance block are category statements the brand's own Always list exempts (lines 82–83, verified: "the rule targets denial, not category"). Seven plate captions each carrying one is still a page apologising for itself. Fix: captions carry name and role; the category statement is said once, in the provenance block. |
| 4.4 | Level 2 unreachable by AT; `aria-expanded` with nothing controlled; smooth scroll rides focus | Confirmed at `representative-chloe.html` 141–145 (`aria-hidden` card), 247 ff. (`aria-expanded`, no `aria-controls`), 41 | **Conceded, all three.** Fixes: `aria-describedby` pointing at the gloss text so focus reads the Level-2 definition; no `aria-expanded` unless a region is exposed; smooth scroll by script on click only. |
| 4.4 | Chloe page on phone: no running title, no Contents, no wordmark | `running-title` and `.optional` `display:none` at ≤760 (77), wordmark hidden ≤480 (81) — confirmed at 500 wide | **Conceded.** The book's whole orientation apparatus evaporates on the device it is most likely to be read on. |
| 4.2 | Atlas unreachable from phone header and footer | `.optional` hidden ≤760 (110); footer has no Atlas link (635–641) | **Conceded.** Footer gets Atlas on every page. |
| 4.2 | Phone: ~24.5 screens; first face at screen 5.5 | At 500 wide: 25.3 screens, first portrait at 5.5, closing door at 23.7 | **Conceded.** I named scanability as a sacrifice in the README and under-weighted it: five screens of typography before a face, on a project whose proposition is people. |
| 0 | Every fact checks against `world-census.json` | — | Noted with thanks; it was the standard I was working to. |

Nothing in that table is a taste dispute, and none of it is the reason the homepage
dies. But the reviewer is right that a document whose credibility play is "I showed my
work" cannot claim floors it did not meet. Three README claims (contents position,
one-click, target size) were overstated, and one ("nothing here contradicts the
constitution's app rules") was wrong. I withdraw all four.

---

## 2. Where the review is wrong or overstated

### 2.1 "'That is the entire CTA inventory' — false" (§1.4)

The README sentence the reviewer quotes does not stop at "one door." It reads, in full:

> "Come and join us at the Table" sits in the running head of every page, in madder,
> and returns as the closing line of the issue and of each chapter; **each chapter also
> carries a quiet "begin a conversation with X · bring X to the Table" line.** That is
> the entire CTA inventory.

The sixteen app handoffs the reviewer counted (9 `mode=table` + 7 `mode=interview`; my
count is the same) are exactly the inventory that sentence enumerates. "One door" was
never a claim that the page has one link into the app; it was a claim about *one kind
of door in one fixed place*, with the per-chapter lines named as the rest. The
reviewer's real finding stands and is worse than the "false": I kept 31 in-page
anchors at full visibility and hid the sixteen links that matter. That is the charge.
"The README misstates its inventory" is not.

### 2.2 "Deletes the constitution's 'Start with your question' door" (§2.1, §6.2)

The README's stretch 1 says, verbatim: the direction "hands off to the app's Table field
(`?mode=table`) through one sentence **and lets the three doors live in-app**." The
constitution's S0 (lines 371–376, verified at source) puts all three doors — *Start with
your question · Build your own table · Guided onboarding* — under the same hook and the
same CTA line this site uses. So the README's stated intent was that every door on the
site lands the visitor at the threshold where the question door is.

The href does not do that. `?mode=table` bypasses the threshold and drops the visitor in
the seating field. The reviewer caught a real contradiction between my sentence and my
attribute value, and the attribute is wrong. But it is an attribute: point every door at
the app's threshold and the constitution's question door is one click from every page
of this site, today, for every visitor, without the marketing site building a routing
surface of its own. That is not "deleting" a door. It is mis-targeting one.

What this does *not* answer is the heart-audience charge, and I want to be exact about
that: even with the href fixed, the site's own first screen still says "read," and there
is still nowhere on the site to say what you came with. That is §4's problem and I
concede it there. I contest only the word "deletes," because it turns a one-line bug
into a design decision I did not make and would not defend.

### 2.3 "The apparatus is a vacuum, and it has already filled with bookkeeping" (§3.1)

The structural claim is that a visible margin "creates seven-plus slots per page that
must be filled with something, and the cheapest thing to hand is whatever the team is
currently thinking about." Test it against the one tradition page that exists.

`representative-chloe.html` carries seven sidenotes. All seven are citations to material
that already exists in the tradition's approved build record, not written for the page:

- n1 — Doc_04 G02 (correspondence as Primary gravity); Polycarp, *Philippians* 13; *1 Clement*
- n2 — *Didache* 9–10; Ignatius, *Smyrnaeans* and *Philadelphians*; the Strand-A caution
- n3 — Pliny, *Letters* 10.96; Doc_09 story004; Doc_06 lex010
- n4 — Ignatius, *Ephesians* 4; *1 Clement*; Hermas; Doc_04 G01
- n5 — Pliny 10.96–97 and Trajan's rescript; Doc_04 G04
- n6 — *Didache* 1–7; Doc_09 story009; Doc_06 lex007, lex011
- n7 — Doc_09 §4 Absent Stories items 4, 5, 9, 10; Doc_07 §2I

Seven for seven. The two leaks the reviewer found are on the *homepage*, in the essays
about the *project* — which have nothing to cite but the project. So the vacuum is real
exactly where the page is about us and not where the page is about a tradition, because
a tradition's build record holds far more than seven citations. The correct conclusion
is narrower than the reviewer's: the apparatus belongs on tradition pages and not on
project pages. I accept that conclusion, and the homepage's five sidenotes go with the
homepage.

The discipline cost the reviewer names is real and I do not dispute it. The inference
that the slots "must be filled with something" is not, for the pages where the apparatus
would actually live.

### 2.4 "~14,000 words of gated prose, ~55 sidenotes, ~54 lexicon entries" (§3.4)

Two of the three figures are not writing costs. The lexicon entries exist — Doc_06 is
built and approved for every live tradition; the Chloe page's six are drafts *of*
records that exist. The sidenotes cite Doc_04, Doc_07 and Doc_09, which exist. What
stretch 4 names is a *sync* problem (a web-facing copy of entries that must not drift
from the in-app records), and the stretch already offers the fallback that removes it:
keep only the hover card, no web copy. The reviewer's own evidence for the danger — the
carousel's "two independently-maintained copies" bug — is an argument for that fallback,
not for the 54-entry figure.

The genuinely new, gated cost is the Representative-voice essay: 1,102 words of voice
prose on the Chloe page by my count, so roughly 10,000 words across nine traditions.
That is still ten times what a tile costs, it is still a permanent editorial commitment,
and I under-sized it in the README by not putting a number on it. The reviewer is right
that "content volume, forever" was a sacrifice named without being weighed. But the
number is about ten thousand, and it is one kind of content, not three.

### 2.5 The metaphor's expiry (§3.5)

Half concede, half contest. A quarterly *anticipates* issue two — that is why the issue
is titled *The First Centuries* and not *Church in Conversation*; the Reformation wave
was always going to be the second issue, with the first in the contents. But the
reviewer is right that I did not design that, and right that an archive index is not
"one continuous read." The periodical frame — masthead, issue, "In this issue" — is the
weakest part of the metaphor, and it dies with the homepage (§4). The *book* — a
Representative's introduction as a chapter with its sources in the margin — has no
issue-two problem: chapter eight is chapter eight.

### 2.6 Small corrections, for the record

- "Never": 20 in visible copy across both pages, not 23; the higher figure counts CSS
  and HTML comments. Substance unchanged.
- The Chloe page's running-head door *does* fit at 768 (right edge 744); the iPad
  amputation is the homepage's. This does not soften §4.1 — the homepage is where an iPad
  visitor arrives.
- §6.4 lists "masthead, contents, plate, colophon, part, recto/verso, apparatus,
  epigraph, standfirst" as the register's vocabulary, then concedes "none of this is
  visible in copy." Correct, and worth being precise about: the words a visitor actually
  sees are *In this issue*, *Part One/Two*, *Chapter I–VII*, *Plate I–VII*, and *Essay*.
  The rest are CSS class names. §3 below argues from the visible five.

---

## 3. Religious feel — pressed, as the reviewer invited

The reviewer holds this "loosely" and asks to be pressed. I will, and I will also concede
the two places the charge lands.

**What the reviewer grants first, and it is most of the case.** No cross, dove, flame,
glass, steeple; no scripture as decoration; no worship vocabulary in the chrome; no
devotional address; no liturgical structure; no invocation; no "we believe"; and the AI
question raised in the fourth paragraph before any Representative speaks — "journalism,
not devotion." The Decision Log records the test that killed the liturgical direction:
the page "still reads as a service — the feeling comes from the ordo, the red-italic
rubric, and the printed order." My pages have no ordo, no rubric, no order of service.
They have chapters. On the test the coordinator actually applied, this direction passes,
and the reviewer's own list is why.

**The reviewer's substitute test — "it looks like the thing it is about rather than a
place to ask about it" — is a real test, and I want to answer it device by device rather
than by the word "codex."**

Of the seven devices listed in §5, one (the material names — gold-leaf, vellum,
iron-gall, parchment, colophon) is CSS token vocabulary a visitor never sees, and the
reviewer concedes it. Four — Roman-numeral chapters, part-title pages, drop caps, a
colophon — are the ordinary furniture of secular trade publishing: any Penguin Classic,
any Library of America volume, any university-press history has parts and Roman-numeral
chapters; Knopf closes every book with a colophon ("A Note on the Type"); *The New
Yorker* opens every feature with a drop cap. The constitution's own register line — "a
beautifully set trade book on parchment — warm, unhurried, nothing antiquarian" (line
50, verified; written for the Table screen) — draws the line at *antiquarian*, and
antiquarian on a page means blackletter, illuminated borders, rubrication, faux-aged
textures, fleurons, ornament. None is present. The "rubricated glyph" of item 5 is the
app's own ✲ in the app's own Tyrian — inherited, not my rubric.

Item 5's deeper claim — that a central text column with a keyed marginal apparatus
*is* the glossa ordinaria, whether or not the visitor knows the term — I think
mis-identifies what a 2026 web reader recognises on sight. The immediate referent for a
sidenote column is the annotated edition, the Tufte book, the footnoted history: the
*scholarly* register. Mark's first statement names "engaging and trustworthy (scholar)."
The sidenote that says *Doc_09 §4, item 4: no enslaved voice* is the device that makes
"I hold that silence rather than fill it" a checkable claim instead of a mood. The
reviewer calls that passage "the whole project's credibility in four hundred words." The
apparatus beside it is where the credibility comes from. Strip the apparatus and the
four hundred words are a well-written assertion.

**Where the charge lands, and I concede it:**

1. **Portraits at plate scale** (item 4). The reviewer is right that presenting a locked
   portrait at full-column width, numbered, ribboned, in portrait orientation — Chloe
   with the cup in both hands, frontal, direct gaze — is my decision, and that at that
   scale on a ruled page the icon reading is available. The Chloe page already does two
   of the three things that break it: a tighter 5:4 landscape crop at reading-column
   width, and no "Plate" spread. Concede: no "Plate N," no ribbon, the landscape crop,
   at reading-column width or less.
2. **The closing spread** (item 7). A single protected sentence at 3.6rem, alone on a
   screen, after a long read. The reviewer calls the form an altar call. It is also the
   form every long-form magazine feature ends in when it sets its last line large, and
   what makes the difference is whether a sermon or an essay preceded it — which the
   reviewer's own §5 settles as essay. But Mark's test is "no pressure, just witness,"
   and one line set that large is louder than witness needs. Concede: the door at reading
   size, as two equal ways in, not one line set apart.
3. **Full-screen part-title pages.** Not a religious tell — every multi-part book has
   them — but on a phone they are a full screen of near-nothing, and they cost the
   visitor a face. They go with the chronology (§4).

**What I ask Mark to hear on this point.** The manuscript palette is his; the veiled
and robed portraits are locked; parchment and iron-gall are the ground everything in
this project stands on. A test under which the apparatus of a serious book reads as a
religious artefact is a test the brand itself fails on sight, before any direction
touches it. The reviewer half-says this in the last paragraph: Mark "may hear [it] as
*serious* rather than *religious*." Remove the antiquarian dress — the numerals as
watermarks, "Plate," "In this issue," the part-title screens, the line set large — and
what is left is a serious book with its sources showing. That is the register he named
when he said *trustworthy (scholar)*, and it is the register the reviewer's two
favourite passages were written in.

---

## 4. The thesis verdict: what dies, what I ask to survive

### 4.1 Conceded: the homepage as a chronological issue dies

In my own terms, not the reviewer's, because I want it on record that I see it:

- The site's first screen offers a reader a book. A person Mark described — hard,
  personal questions, possibly leaving — is not a reader by default. They need, on the
  first screen, to be told what this is, told it will not lie to them or recruit them,
  and given a way to say what they came with. My first screen gives the first of those
  and a door.
- There is no surface on either page that takes a question as input.
- The one sentence naming that person is the last thing on the page. Confirmed: once, at
  line 615, at the closing door.
- The best four hundred words the direction produced — "Where we are quiet" — are 1,100
  words into the one inner page that exists.
- Five screens of typography before a face.

Every one of those is a sequencing decision. Sequencing was consequence 1. I give up
consequence 1, and with it the masthead, the issue, "In this issue," the part-title
screens, the Roman-numeral watermarks, "Plate I–VII," the ribbons, the reading-time
byline, the closing line set large, the sidenotes on project essays, and the periodical
frame's issue-two problem. That is the whole of what made the homepage a quarterly.

### 4.2 Contested: "unpatchable" as a bundle

The reviewer's charge one lists seven things. Sorted honestly:

| Item | Nature | Status |
|---|---|---|
| Conversation links invisible | CSS | patchable, one rule |
| Index routes to prose, never to a conversation | HTML | patchable — a second link per row |
| Priced in reading minutes | one line of copy | deletable |
| Door lands in the seating field, not the threshold | one attribute | patchable (§2.2) |
| Reevaluation audience named once, at the end | placement | movable |
| Organised by chronology first | structural | **the homepage's spine — conceded** |
| No question-shaped input anywhere | structural | **the homepage's absence — conceded** |

Five of seven are not consequences of "the site is a book"; they are choices I made
badly inside it, and none of them requires giving up anything. The two that are
structural are both the homepage's, and I have conceded the homepage. What I contest is
the sentence that follows: "fixing it means giving up sequence-over-navigation, and
sequence-over-navigation *is* the direction." Sequence was one of three consequences.
The other two — the apparatus visible in the margin, and one door in one place — survive
every one of the reviewer's own five conditions in §8. The reviewer says that after
those five changes "it is no longer this direction." I would say: it is this direction
with its homepage replaced, which is what I am asking for.

### 4.3 Requested: a narrower survival, named exactly

**(a) `representative-chloe.html` as the canonical inner-page pattern for every
tradition — kept as an order, not as parts.** The order is the point:

1. Provenance block first: what this voice is, what it is built from, that it is an AI,
   that the marginal notes say where every claim comes from (line 240).
2. The Representative's "we" voice, with disagreement kept open — bishop-or-council
   unresolved, one meal or two unsettled, one voice's testimony never inflated into a
   consensus (259).
3. Sidenotes to the build record, in reading order for assistive tech.
4. The app's lexicon grammar, with the AT fixes from §1.
5. "Where we are quiet" (271–275).
6. Questions people bring — **re-selected from the same Guided Starters draft to lead
   with the personal ones.** The reviewer's count is right: I chose four scholars and one
   person and put the person fifth. The draft has more than five seeds; the selection
   and the order were mine and were wrong.
7. Both handoffs at equal weight, at reading size.

Why as an order: the reviewer's §7 harvests four of its six survivors from this page,
and calls two of them "the best answers to Mark's ruling I could imagine anyone
producing." Both are written in this register and depend on it. The provenance block is
credible because the notes beneath it do what it promises. "I hold that silence rather
than fill it" is checkable because n7 points at Doc_09 §4. Lift either into a page
without the apparatus and it becomes a nice paragraph. The pattern is the thing; the
parts are how it is built.

**(b) "Where we are quiet" promoted to the homepage's first two screens, in the
project's own voice.** The reviewer proposes exactly this — "put 'Where we are quiet'
and the AI disclosure in the first two screens, and the chronology below them" — and I
accept the shape. This direction's register can write that screen: the same "we" the
Representatives use, turned on the project itself — what this is, what it will not do
(the protected "It will never try to convert you. What it means for you is yours to own
and share"), what it does not know and will say so, and a way to ask. Whether the app's
threshold can *receive* a carried question today, so that the site's field hands it
through rather than merely links to the door, is a D3 check against `cic-poc/frontend`,
not something I am asserting; if it cannot, the field is the door's link and the copy
promises nothing that is not built. I will draft the screen for D3 if asked.

**(c) The per-tradition unit a tile cannot give**, carried into whatever container
wins: a dateline, the approved description, a first paragraph in the Representative's
own voice, and two *visible* handoffs. Not the spread, not the plate, not the numeral.
Chloe keeping the bishop-or-council question open in her first four sentences, Marius
refusing to say which see wins — that is what makes a tradition a voice rather than a
label, and it fits in a grid, a list or a map card.

**(d) The sidenote implementation, whole** (reviewer's #1), and the ✲ regrammar to the
app's own verb (§1) so the marketing site and the app share one citation gesture.

**(e) The reading conditions as the accessibility system:** 20px at 1.55 on a 38rem
measure, AAA for running prose (13.70:1 measured by both of us), reduced-motion parity,
focus-not-obscured, panel-never-modal. All verified by the reviewer; all cheap to carry
into any direction; none of it depends on the homepage.

**(f) One persistent door in one place — pointed at the app's threshold**, so the
constitution's three doors, including *Start with your question*, are one click from
every page. No longer the *only* visible way in: the per-tradition handoffs are madder,
and the contents carries them.

**(g) Verified-against-data and the draft-tag convention** as a D3 working rule. The
reviewer checked every fact and found none wrong; that discipline cost nothing and
should be the floor.

### 4.4 What I am not asking for

I am not asking that the direction be scored a survivor at the whole-site level. Under
the charter's own rule, "a direction that cannot be defended dies, and a direction that
survives gets strengthened by what the attack exposed" — the homepage cannot be defended
against Mark's heart audience and I have not tried. What I am asking is that the
coordinator and Mark treat (a) and (b) as a *pattern with an order* that this direction
produced and that no tile-first direction can, rather than as harvestable parts. If that
counts as survival, the direction survives strengthened. If it counts as salvage, it is
salvage with its order intact, which is the only way it works.

---

## 5. What I ask the reviewer to withdraw, and what I ask them to keep

Withdraw: "false" on the CTA inventory (§1.4 — the README enumerates it); "deletes" on
the question door (§6.2 — mis-targets, one attribute); "vacuum" as a structural property
of tradition pages (§3.1 — seven-for-seven on the page that exists); the 54-entry and
55-sidenote figures as *writing* cost (§3.4 — they are the build record); and "codex" as
the verdict on the register, in favour of the two specific concessions in §3 (plate
scale; the closing line set large).

Keep: every measurement in §1 — I reproduced them; the homepage kill; the five
conditions in §8, which I accept in full; and the two passages in §6.5, which I ask to
be kept in the order they were written.

---

## 6. Closing

The reviewer's last line is that "the craft is excellent and should be harvested; the
thesis is wrong for the audience Mark named." I would put it one degree differently,
and I think the degree matters for D3. The thesis had three parts. One — meet the
Representatives in the order history met them — is wrong for a person who arrives with
a question instead of a century, and it dies. The other two — a Representative speaks
for itself on this site, in its own voice, with its sources in the margin and its
silences left standing, and there is one door in one place — are not craft. They are
the reason the two passages the reviewer would keep exist at all. A person who left the
church because it lied to them will read "no enslaved member of any of our households
left a single word in their own voice" and believe it because the note beside it says
where to look. That is the direction. The quarterly was its costume, and the costume
goes.

*— Fable, author of Direction 01. One defense, filed.*
