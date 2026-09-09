# D2 defense — Direction 03, Institutional-Professional / Scholarly Authority

**Sandbox artifact. The author's one defense, per the charter. Not a ruling. 2026-09-02.**

Author of direction 03. I read, in order: my own `README.md`, `homepage.html` and
`tradition.html`; the adversarial review `03-institutional-professional-review.md` in
full; and `Decision-Log.md` in full, including Mark's two verbatim 2026-09-02
statements. I opened no other direction's folder and no other review.

I did not take the reviewer's measurements on faith, because the charter's own rule
is that a claim gets checked against the files, not the prose. Same Chromium
(`/opt/pw-browsers/chromium-1194`), same viewports (1440×900, 1280×800, 390×844),
positions read from the live DOM. One disclosure about my own method, because it
turned out to be evidence: my first re-measurement pass reported **zero** overlap
between the marginal column and the register table at both desktop widths. It was
wrong. The page sets `scroll-behavior: smooth` on `html`, and a scripted
`window.scrollTo` under smooth scrolling never actually moved the page. When I
forced instant scrolling and logged the marginal's absolute position at every 50px
through the section, the collision reproduced to the pixel — 208 × 328, at both
widths. I raise this first because it is exactly the reviewer's closing point made
flesh: this defect is invisible to any check that does not physically scroll through
the section. I did not scroll through it. That is now measured, not alleged.

---

## The short version

**I concede the verdict on the homepage.** The structural charge — that the section
order is the thesis, and the section order ranks the academic above the person with
hard questions — is right, and I cannot close it with warmth moves, resequencing, or
craft fixes. The direction dies as a whole-site homepage.

**I contest five things, with evidence**, and they matter for what survives rather
than for whether the homepage does: the "seminary" reading of the register (the
reviewer's own §3.1 describes it as Getty/Wellcome, and most of the vocabulary cited
as seminary is the census's own verbatim public strings); the "Jesus in the
copyright line" charge (the live approved homepage has the identical single
occurrence in the identical line, and the reviewer's own §5 logic argues against a
front-door "Jesus" for the deconstructing reader); the "two moments of address"
count (there are at least seven); the confidence scale as "advance apology" (one
profile of the seeker, not the only one — though the ordering point holds for both);
and the claim that resequencing dissolves the direction (my own README's founding
sentence orders *collection → assembly → trust*; the built page inverted my own
thesis, which changes what the thesis is and therefore what carries forward).

**I ask for the narrower survival the reviewer already proposed, sharpened**: the
direction's thesis — the record shown whole before the chair is offered — is a
*second-screen* thesis. It belongs at the one point in the journey where the visitor
has already asked "can I trust this?", which is the tradition record page, and it is
wrong everywhere earlier. `tradition.html` is not salvage from a dead direction. It is
the direction, built in the right place. Section 4 names exactly what should carry
into D3 and what must not.

---

## 1. Conceded — every measured defect, verified against my own files

I checked each of these myself. Where I say "verified," I mean I reproduced the number.

| Reviewer's claim | What I found in my own files | Verdict |
|---|---|---|
| **4.1** Sticky marginal collides with the register at 1280 and 1440, 208 × 328 | Verified, instant scroll, both widths. Worst overlap 208 × 328 at 400px into the section. The marginal travels 1,331px (absolute top 3,079 → 4,410) while the table starts at 3,431. Screenshot at 500px: the "3 / REGISTER" numeral and paragraphs overprint rows I.1–I.2; the "All 292 surveyed movements" link sits on row I.7 where it will intercept clicks. Chrome constrains a sticky grid item to the grid *container*, not its grid area; I assumed the area. | **Conceded in full.** Verified three one-line fixes at 1440, all to 0 × 0: `#register .marginal { position: static }` (keeps the table at 1,152px); `#register .span-all { grid-column: 2 / -1 }` (table drops to 886px); or marginal spanning both rows with the table in column 2. The first is right for this section — the table is a plate, and the marginal has no business travelling beside it. |
| **4.2** Phone: doors 840px off-screen in a nested scroller, masthead CTA hidden | Verified at 390×844. Scroller 390px wide, 1,073px of content, Actions column at 840px; `.masthead__cta` computes `display: none`; register section top at 6,072px, first tradition name at 6,742px on a 12,251px page. | **Conceded.** README §2's "the Table is one click from anywhere" is a desktop sentence. README §3 named "density below 900px" as a sacrifice but did not name that the thing being sacrificed was every tradition-specific door. |
| **4.3–4.4** Nav clips "Get Involved" at desktop; phone nav invisible | Verified: `nav.nav` clientWidth 648, scrollWidth 659, last link 11px past the clip edge at 1440 *and* 1280 — "Get Involve." Root cause as stated: I applied the live stylesheet's ≤640px overflow rule at all widths. **One the reviewer did not catch:** at 1440 the masthead's "Begin a conversation" button wraps to two lines. | **Conceded**, plus one self-reported. |
| **4.5** Record page: 156px seat bar on phone; anchors land 49px behind it | Verified with real hash navigation: seat bar 156px; `#limits`, `#sources`, `#review` headings hidden by 49–50px. The `scroll-margin-top: 5rem` was calibrated against the 60px desktop bar. | **Conceded.** And the reviewer's tonal point is right: a 156px pinned bar with a bordered button is the most insistent element on the page, on the direction whose thesis is "never pushed." |
| **4.6** Row header is the identifier, not the name | `<th scope="row" class="no">I.1</th>`; name in a `<td>`. | **Conceded.** It compounds the 2.4.9 failure below: under 2.4.4 the programmatically determined context for "Read the record →" is "I.1 / Actions," which still does not name the tradition. |
| **3.2** "Nothing under 13px carries meaning" — broken | Verified, and undercounted. Computed sizes on the homepage below 13px: the status band's `dt` labels at **11.00px** (×7 — lower than anything the reviewer listed), register column headers 11.52 (×6), method-status labels 11.52 (×3), `.scale__ends`, `.slot .label`, "State of the record" `h2` at 12, the frontispiece note at 12, the two `cite`s at 12.48/12.8, tradition formal names, Representative roles and era ranges at 12.8. | **Conceded in full.** My rule, my constitution citation (§2.2, line 105), my CSS. |
| **3.2** AAA 2.4.9 — "every register action names the Representative" | Seven identical "Read the record →" links; six carry a `title` attribute, which is not link text. | **Conceded.** Fix: tradition name as the row header, and `Read the record<span class="visually-hidden"> of the House-Churches</span>` on each. |
| **3.2** Gold-leaf sets small text | `.plate .rep .role`: `var(--gold)` at `.72rem`, bold. | **Conceded.** |
| **3.2** `#7c3aed` hardcoded as a status dot, twice | `tradition.html` lines 116 and 134. It is the House-Churches' census tint (the homepage row uses it as `--row-color`). I meant it as "Chloe's colour"; nothing on the page says so; it reads as the reserved purple. | **Conceded.** Either a labelled tradition tint via variable, or ink/madder. |
| **4.7** Portrait `height="600"` defeats `aspect-ratio: 4/3`; 602px dead space | Verified: 410 × 600 as built. With `height: auto` added to `.plate img`: 410 × 307, title block 940 → 647px, dead space 602 → 309. The reviewer's two findings are one bug. | **Conceded**, and the fix closes half of the second finding too. |
| **4.7** Superseded Cappadocian certificate cited as current | `CAPPADOCIAN_BUILD_LEDGER.md` §28 names the rename as invalidating the 08-31 certificate; §29 re-admits on 2026-09-01. My 08-31 is Mark's original admission act, not the operative certificate. | **Conceded.** The larger point is the one to keep: a status-band homepage turns every number into a maintenance promise, and I broke one within two days of writing it. |
| **4.7** The disclosure-grammar demo is inert | Zero `<script>` tags; the dotted underline signals an interaction the page does not perform; the ✲ anchors to the section it sits in. | **Conceded.** A static two-panel picture of the real Level-2/Level-3 grammar is the right replacement. |
| **2.4** The external-review negative stated five times | Status band, frontispiece, method-status grid, §4 "unfinished," and §5's heading. The band and frontispiece duplicate each other by construction — the band was meant as the phone colophon and the frontispiece as the desktop one, and both render on desktop, 300px apart. | **Conceded.** Say it once, in §4's "unfinished" column, which is the block the reviewer wants kept. |
| **2.5** "World" on a 48px card; verbatim exemption read backwards | Card 1 is "World Identification, Boundaries, and Orientation"; the Step 10 pull-quote says "frozen world's ecology." README §7 shows I knew and chose it. | **Conceded.** "Verbatim" protects approved public copy from drift; it does not license internal strings on the front door. The reviewer's fix — plain-English titles, verbatim titles one click down — is what the voice pair asked for. |
| **1.2** Word budget 1,352 : 585, zero words showing a conversation | Verified to the word: 36 + 94 + 508 + 265 + 296 + 153 = 1,352 against 585 (376 of them in the table itself). Setting aside §4 (brand-required) and §5 (the reviewer's-brief ask), method + scale + status + frontispiece is still 903 : 585. No sample question, no sample turn, anywhere. | **Conceded.** |
| **1.2** The four messages are ranked, and I promoted the fourth | Brand Guidelines line 43: the heading is literally "The four messages, in order." | **Conceded.** README §2 cited message four as if the order were mine to choose. |
| **1.4** FK grade 11.6 against a 10th-grade floor | Floor confirmed at Brand Guidelines line 41. The live homepage sits at 8.4. | **Conceded** for the homepage; it is the front door. |
| **3.1** The frontispiece dashboard is decoration by my own rule | "Eras with the Step 0 survey complete: 10 of 10" is internal. Two of eight rows mean nothing outside the repository. | **Conceded** for the panel. "7 traditions / 292 movements" are the Atlas's own scope facts and belong wherever the Atlas states its scope — not as the first content on the page. |
| **2.2** My "underneath = depth" re-reading of the voice pair | "Underneath" and "one click away" are both positional. I conceded half the pair and redefined the other half. | **Conceded.** And the reviewer's finding that the *experience* term of "experience first, governance second, mechanism third" is not inverted but absent is sharper than my own §6.1 and correct. |

Nothing in this table is disputed. The reviewer said these are a morning's work; they
are. But I accept the reviewer's harder reading of them: on a direction whose whole
argument is "professional on sight," a flagship section that overprints itself on an
ordinary monitor is not a bug list, it is a hole in the argument.

---

## 2. Contested or corrected — with the evidence

### 2.1 "Seminary" — the reviewer describes the same register two ways

Section 3.1 of the review says the register is "a *current* house style with a
recognisable signature… Getty, Wellcome, Cooper Hewitt, every Observable-adjacent
data-humanities microsite." Section 5 says it is "the divinity-school special
collections finding aid." Those are not the same claim. Getty and Wellcome are
secular; the form the reviewer identifies in §3.1 is the neutral-academic archive —
exactly the register Mark's "trustworthy (scholar)" asks for and exactly the one his
"not the feel of religion" permits. What flips it to "seminary" in §5 is the
*content*: early-church traditions, patristic names, an era called Ante-Nicene. That
content is the project. Any register laid over it — editorial, spatial, product — will
carry some ecclesial association, because the subject is the Church.

Then the specific evidence. Most of what §5 lists as seminary vocabulary is not mine:

- **The Roman-numeral identifiers.** `world-census.json` line 759: `"atlasId": "I.1"`.
  These are the Atlas's own public identifiers, already live on `atlas-v3.html`.
- **"The Ante-Nicene Period" / "The Constantinian/Nicene Era."** Census lines 30 and
  47, field `academicName`. The census's own era subtitles, verbatim.
- **The "Standing on the Nicene Creed" floor note.** Census line 785, field
  `floorNote`, verbatim; every built tradition carries one; the Atlas shows them.
- **"Household Leader."** Census line 791, `representativeTitle`.
- **The five confidence labels.** Constitution Article 17, verbatim, and the reviewer
  concedes they are "exactly right inside a conversation" — which is where every
  visitor will meet them.
- **`episkopos · presbyteros · ekklesia · eucharistia`.** The World 1 reviewer's brief's
  Tier 1 terms — the four words Chloe will not translate away. They sit on
  `tradition.html` §7, the page the reviewer wants carried forward nearly whole, and
  they are a truthful preview of the product, not a display feature.

What *is* mine, and what I concede: "Plate I." in a visible figcaption; "Register" as
a visible eyebrow; lower-roman counters on the declared limits; Alegreya SC numerals
in a sticky marginal column the README itself called "like a monograph"; and
`font-feature-settings: "onum"` on the body. Old-style figures, small caps and
Roman-numeral part numbers are the trade-book register the constitution asks for, not
a departure from it. "Plate I.," the lower-roman counters and the marginal column are
the departure, and **the reviewer is right that I did not flag them**. README §6 lists
three stretches. This was a fourth. For a direction whose credibility rests on naming
its stretches, missing one costs more than the stretch. Conceded. ("Frontispiece" and
"colophon" occur only in class names, CSS comments and the README — a visitor never
sees either word.)

So on the register itself I disagree with the label and agree with the effect. The
form is neutral-academic. But the reviewer's real argument in §5 does not depend on
the label. It is that *authority display of any kind* before something person-shaped
to ask makes the room feel like the room the doubter left. I would add one
qualification: for most people deconstructing out of a confident church, the room
they left is the church, not the archive; historical-critical scholarship is more
often their companion than their adversary. That is why the neutral-academic register
is safer ground for that reader than the reviewer allows. It does not rescue the
page, because a credentials wall is a credentials wall whether the credentials are
ecclesial or academic, and my homepage is one. I contest the diagnosis; I accept the
prognosis.

### 2.2 "Jesus once, in the copyright line" — the live homepage is identical

`cic-website/index.html` line 201: the approved, live homepage contains the string
"Jesus" exactly once, in exactly the same footer line ("A safe space to explore faith
and the story of Jesus, part of Faithways Studio, Inc."). That line is not among the
six protected strings (Brand Guidelines lines 55–62); it is inherited boilerplate on
both pages. Direction 03 did not "strip" the word; it inherited the live site's
treatment of it to the letter.

And the reviewer's own §5 argument cuts against the proposed remedy. If a seminary
register reads to the deconstructing visitor as "the room they left," a front door
that leads with "Jesus" reads as that room more directly still. Mark's "I don't want
the feel of religion" is at least as much about that word on a hero as about small
caps. So I contest the charge as framed.

What I concede underneath it is more serious than the word count. The charter's
heart goal is "the fascinating and life-changing journey of the church and how Jesus
is faithful to us." My README §2 claims that story is "carried by the record's
voices — Ignatius writing under guard, the unnamed householders… Chloe's own 'where
we sound most alive.'" Every one of those lines is on `tradition.html`. **There is no
line on the homepage that carries the heart goal at all** — not the word, not the
substance. The reviewer's 3.3 finding ("on the homepage, before §5, there is not one
human voice") is exact, and it is the version of 1.3 that lands.

### 2.3 "Exactly two moments of address" — overstated

The review says the homepage addresses the visitor "exactly" twice. Measured on the
rendered `<main>` plus the closing CTA: twelve second-person pronouns, in at least
seven distinct addresses — "The chair is yours"; "You will meet these five words
inside every conversation"; "Open the record before you sit down, or sit down first";
"corrected before it reaches you"; "direct you toward real human support"; "What it
means for you is yours to own and share" (a protected line); "we would welcome your
eye"; "whether or not you ever sit down." A small correction, and I make it only
because the charter values the count being right.

The substance I concede whole. None of those addresses is a *host*. They are an
institutional "we" describing procedure to a "you." The brand's sound-like is a
scholar-host at a table; this page has the scholar and the table. The person who
pulls the chair out is missing from the homepage, and present on the record page,
where "Chloe is seated. Begin when you're ready — or read on" is her.

### 2.4 The confidence scale as "advance apology" — one profile of the seeker

Section 6.1 argues that a five-level scale shown before any content "tells someone
already in doubt: everything you are about to hear is graded… and we will not resolve
the disagreements," and that for "a person whose faith is unravelling and who came
looking for somewhere solid to stand" that is an apology in advance.

That is one real profile of the heart audience. There is another, at least as common:
the person who was handed certainty, found it did not survive contact with the
sources, and is now angry at everyone who was certain. For that person, "here is what
is documented, here is what is contested, here is where we cannot tell you" is not an
apology. It is the first religious voice they have met that did not lie to them.
README §2 was written for that person, and I still think it is right about them. The
reviewer chose the other profile and wrote as if it were the only one.

But the reviewer's second formulation holds for both profiles and I concede it: on
the homepage the scale is **a legend without a map**. It precedes every piece of
content it could label. On `tradition.html` the same legend sits beside the
contested-ground list and the declared limits — the map — and there it does for both
kinds of seeker exactly what it should. The scale is not the problem. Its position is.

### 2.5 "The resequenced page is no longer this direction" — my own README says otherwise

Section 6.3 argues that putting the register above the method and the scale "ends
the direction's own thesis," because README §1 makes the order the thesis. Read the
founding sentence again:

> "A serious research library's digital exhibit does not open with a mood; it opens
> with **what the collection is, how it was assembled, and how much of it can be
> trusted**."

That is an order: collection, then assembly, then trust. The collection is the seven
traditions. Assembly is the method. Trust is the confidence scale. The page I built
runs method (§1), scale (§2), traditions (§3) — it inverts the sentence it claims to
take "whole," and treats eight counts in a side panel as "what the collection is."
The reviewer's §3.1 catch that the panel is the appearance of information rather than
information bites here too: I confused the collection with its inventory.

So register-first is not the dissolution of the direction. It is the direction's own
order, which I failed to follow. I raise this not to save the homepage — it does not.
A catalogue table with an evidentiary-base column is still not "a clear, fast,
personal way to ask a hard question" (Decision-Log, D2 closure, finding b), and a
register-first homepage would still fail the heart audience; the reviewer's verdict
stands unchanged. I raise it because it changes what the thesis *is*, and therefore
what survives: `tradition.html` runs scope → sources → voices → gravities → contested
ground → limits → Representative → chair. That is collection, assembly, trust, then
the invitation — the founding sentence executed correctly, at the one point in the
journey where the visitor has already chosen a tradition and is asking whether to
trust it. It is not a good artifact that happened to survive a bad direction. It is
what the direction was for.

### 2.6 Two smaller corrections

- **"Bundled three asks as one kind of ask."** README §6 lists them as three numbered
  items and names §6.1 as "the direction's most attackable point." They were not
  presented as one ask. The substance — that the S0 exemption in §6.2 does not reach
  the voice pairs in §6.1 — I never claimed and do not claim now; §6.1's actual defense
  was the "depth" re-reading, which I conceded in §1 above.
- **The S0 withdrawal.** Accepted with thanks. The hero is door-first: protected hook as
  the H1, primary button in the first viewport at both widths. README §3's "thirty
  seconds on a phone gets a status band and a method grid, not a face" was harsher
  than the render, and the README should say so.

---

## 3. The structural verdict, answered directly

The charge: the direction's thesis is its section order; the section order ranks
audiences; the ranking is the exact inverse of Mark's own — *"my heart is those
seeking answers to hard questions of faith, not academics."*

**The charge is right, and I cannot close it.** Here is why, in the reviewer's own
terms rather than a restatement of mine.

The distinction the review draws in §3.3 between **disclosure** and **methodology** is
the sharpest thing in it, and it is the thing that undoes README §2's first warmth
move. I argued that a page which says "here is what we cannot tell you" before "come
sit down" is safer for the person whose faith is unravelling. That is true of
disclosure *about the tradition* — "the interior life of enslaved and non-literate
members is held as named absence" — and that disclosure lives on `tradition.html`.
What the homepage leads with is not that. It is methodology ("each candidate is
tested six ways and classed Primary, Supporting, or Tensional") and disclosure *about
the project* — a review board not yet begun, modes not yet shipped, a census date. The
reviewer calls the latter a changelog rather than a confession. That is the right
word. And measured on a phone, the changelog's worst line — "External academic review:
not yet begun" — sits in the status band at 197px, above the H1 at 429px. The first
thing a phone visitor learns about this project is a negative status about an
academic review board they did not ask about. I built that, on purpose, as the
"colophon at first glance." For the heart audience it is the single worst element in
either file, and it is entirely mine.

Then the first person-shaped thing. On a phone it is Chloe's name, in a table cell,
at 6,742px. The reviewer's (a)/(b) framing — the doubter needs permission and
something person-shaped to ask — is exactly right, and the review's finding that the
page delivers (a) "superbly" and (b) not at all is the verdict in one line.

**An honest note on the process, not an excuse.** The Decision-Log records Mark's
heart-audience statement arriving while D2 was already running. But the ranking was
not new to my brief. The Brand Guidelines' "Who we're writing to" (lines 85–90) says:
*"Silently prioritized: the person whose faith is unraveling."* I read that sentence
and README §3 then listed "the seeker who wants to feel before reading" as the
direction's first deliberate sacrifice. I sacrificed the brand's own silently
prioritized reader, by name, as the bet. The bet was whether scholarly-first could be
made warm enough for that reader without imagery. The answer, measured, is that it
cannot on a front door and can on a record page. That is a result; it is what a
divergent bet is commissioned to produce. But I should not pretend I did not know
whom I was betting against.

**My own test, applied.** README §2 set it: "If D2 finds those three moves
insufficient, the direction is cold and should be killed or hybridized, not warmed
with imagery it has no honest use for." The reviewer found move one sound but applied
to the wrong content, move two true but on the wrong page, move three false on phone.
Having re-measured all three, I find the same. I wrote the test; I take the result.
The two outcomes it allowed were killed or hybridized. This defense asks for the
second, on the terms below.

So: **option (b).** The whole-site homepage dies. What survives is not parts pulled
from a wreck but the direction's thesis relocated to where its own founding sentence
put it — after the visitor has chosen — with the homepage's job redefined as getting
the person with a hard question to that page, fast, by a door shaped like their
question. What that door looks like is D3's question and the other directions'
territory; I have not seen them and will not guess.

---

## 4. What carries forward — exactly — and what the attack adds to it

Everything below is named with its required fix. Items 1–7 are the reviewer's own
salvage list, accepted, with specifics added. Items 8–10 are mine.

1. **`tradition.html`, nearly whole, as the pattern for every tradition record page.**
   Record before chair: scope → sources → voices → gravities → contested ground →
   declared limits → what you will see → the Representative → review status → the
   Table. Required fixes before it is a pattern rather than a mockup: seat bar not
   sticky below 640px, or collapsed to one line, with anchor offsets derived from the
   bar's real height (verified: 156px bar, 49px of every heading hidden); `height:
   auto` on `.plate img` (verified: closes 293px of the 602px void); the
   "Representative" role label at ≥13px in ink, not gold; the two hardcoded `#7c3aed`
   dots replaced by a labelled tradition tint or by madder; "Plate I." replaced by a
   plain caption; lower-roman counters replaced by arabic; the inert grammar demo
   replaced by a static two-panel picture of the real Level-2/Level-3 grammar.
2. **§4, the AI disclosure block, verbatim** — and the rule it embodies, which the
   review exposed: *project-status* negatives (external review, modes, later eras)
   are said once, here, in the "unfinished" column, and nowhere above the fold of any
   page. The status band and frontispiece are the counter-example and do not carry.
3. **The confidence glyph set and the word-plus-glyph discipline** — placed beside the
   content it labels, never before it. The scale is a legend for a map, not a
   preamble.
4. **Declared limits given the strengths' typographic dignity** — with the reviewer's
   distinction adopted as a rule: disclosure about the *tradition* may lead a page;
   disclosure about the *project* is said once, per item 2.
5. **"Where a reviewer might press first"** — the four published attack questions, as
   a per-record pattern with the reviewer's-brief email. Unusual on the public face of
   an AI product, and the part of "cutting-edge" this direction can honestly claim.
6. **Verbatim-and-flag** — reproduce the census string, flag the stale one, never fix
   it silently. Already done for "four built worlds"; now queued as a task per the
   Decision-Log.
7. **README §5's contrast table as the shared V2 text-colour rule**, together with the
   13px floor *enforced* rather than declared. My own homepage has eleven-pixel labels
   in its first hundred pixels; the floor needs a lint, not a sentence.
8. **The register — as the "Traditions" index page, not as the homepage.** The nav
   already points "Traditions" somewhere; it should be a page whose job is the pastor's
   and scholar's question ("which tradition, on what evidence?"). Required: the
   tradition name as the row header; link text that names the tradition; the marginal
   column not sticky; and below 900px, rows become stacked entries with all three
   doors visible — not a 1,073px horizontal scroller with the doors at 840px.
9. **The method — as an inner Method page**, reached from About's "how it works": the
   Step 0 gate, the ten steps and the Step 10 firewall quotation, with plain-English
   titles on the cards and the verbatim framework titles beneath, "tradition"
   throughout the visible copy. This is what "scholarship underneath, one click away"
   asked for, and the reviewer's fix is the right one.
10. **The seat-bar posture on desktop** — outlined button, "Begin when you're ready —
    or read on," the filled button reserved for after the record. The "witness, not
    recruiting" pair made physical; the reviewer called it exactly right at 60px.

**What must not carry:** the status band and the frontispiece dashboard on any
homepage; the sticky marginal column as a section grammar; the method grid as a
first section; the scale as a second section; "Plate," "Register," lower-roman and
the monograph numerals; any count on a public page that is not generated from the
census at runtime.

---

## 5. Corrections owed to my own README

The reviewer asked that I correct the README rather than accept credit or blame it
does not deserve. Both directions apply.

- **§1** claims the page takes the research-library order "whole." It inverts it.
- **§2, "Easy access to features — solved structurally."** True at ≥900px; false on a
  phone, where every tradition-specific door is inside a nested scroller and the
  masthead button is hidden.
- **§3** overstates the sacrifice: the hero is door-first at both widths, hook as H1,
  primary button in the first viewport.
- **§4, "nothing under 13px carries meaning,"** and **§5, AAA 2.4.9 adopted,** are
  both false as built.
- **§6** is missing a fourth stretch — "nothing antiquarian" — which should have been
  flagged for Mark alongside the other three.
- **§7** should record the collision, the nav clip, the 156px seat bar, the portrait
  height attribute and the superseded certificate date as seams found in review, not
  smoothed.

---

## Closing

The reviewer wrote that the parts worth keeping are parts, and the whole is aimed at
the wrong person. I have checked every number in that review against my own files and
found one overstated, four attributed to me that belong to the census, one label I
think is the wrong word for the right problem, and the rest exact. The whole is aimed
at the wrong person. But the direction's own founding sentence — the collection, how
it was assembled, how much of it can be trusted, and only then the chair — was never
a homepage sentence. It is what a person deserves to be shown at the moment they have
chosen whom to sit with, and `tradition.html` shows it to them. Take that page, fix
what is listed, make it the pattern for all seven records, and let the front door be
built for the person Mark named.
