# D3 synthesis review — `CiC_Website_Design_V2.md` + `CiC_Website_V2_Storyboard.md`

**Sandbox artifact. The charter's own D3 gate: "Opus reviews the synthesis against
the charter, the constitution, and the struggle record." Not a ruling. 2026-09-02.**

Reviewer: Opus. Read in full: both D3 deliverables; the Website V2 `README.md` and
the whole `Decision-Log.md`; the D0 inheritance note; the hybrid's `README.md`,
`homepage.html` and `tradition-chloe.html`; its review and its defense; the D2
struggle summary; the five D1 direction READMEs and their ten D2 files (targeted,
for the kill lists and the cited rows); the Brand Guidelines Consolidated V1.0 and
the Logo Usage Sheet V1.0; `CiC_Full_UX_Design_V1_0.md`; the live `cic-website/`
pages, `assets/style.css`, `_headers`, `data/world-census.json`; the `records/*`
files the storyboard quotes; `engine/canon/records/canon_question/*`; the W1 Guided
Starters draft; and `cic-poc/frontend/src` (`App.tsx`, `Launch.tsx`,
`Conversation.tsx`, `ChatInput.tsx`, `lib/sessionStore.ts`).

**Method — the browser work and the arithmetic are real.** Chromium
`/opt/pw-browsers/chromium-1194` via Playwright with an explicit `executablePath`,
both hybrid files at 320 / 360 / 390 / 414 / 480 / 640 / 700 / 768 / 900 / 1024 /
1280 / 1440, at 844 / 800 / 740 / 660 / 896 / 1024 / 900 / 790 heights, light and
dark, fonts blocked (Google Fonts is unreachable here, as it was for every prior
reviewer — fallback faces; ratios, DOM order and semantics are not font-sensitive,
pixel heights are). Every contrast ratio in §6.2 was re-derived from the hex values
with the WCAG relative-luminance formula in a standalone script, *and* separately
by walking every rendered text node composited against its real painted ancestor
background. Record counts, statuses, word counts and quotations were read out of
the record store with a YAML parser, not eyeballed. Where I could not reproduce a
number I say exactly what I measured instead.

**Verdict, stated at the top so the findings read in proportion:**

> **READY TO FREEZE WITH NAMED REQUIRED FIXES.** Eleven of them, listed in §3. Every
> one is an edit to these two documents — no redesign, no new round, no re-litigation
> of anything D2 settled. The synthesis is faithful, the register is intact, nothing
> that was killed comes back, and the measurement discipline is, on the numbers I
> could check independently, the most accurate this workstream has produced. What the
> required fixes address is a small set of places where the record says more than it
> verified, less than a builder needs, or something its companion contradicts — and
> one page state that genuinely does not exist yet on paper.

---

## 0. What verifies — checked before anything is criticised

The D2 reviewer of the hybrid wrote that a review which attacks an honest document
by pretending it is dishonest is worthless. The same applies here, and the list is
long enough that it changes how §3 should be read.

**The colour system is exact, every row.** I re-derived all nine light tokens against
all three light grounds, all ten dark tokens against all three dark grounds, the
button pair, the seven light tradition tints and the seven proposed dark tints —
**sixty-two published ratios, zero mismatches to two decimals.** Including the ones
that indict the palette: gold-leaf 4.52 on gold-wash, graphite 3.38 on parchment,
the madder fill at 2.85 vs ground and 2.69 vs surface, and the raw census tints in
dark (Church and Empire 1.99, Bethlehem 2.34, Alexandria 2.73 — and Syriac 3.68, so
§6.2's "all seven under 3.7" is exact, not rounded in its own favour). The corrected
dark-tint sentence the defense promised is delivered and true: 4.54–4.60 on the
ground, 4.29–4.34 on the surface, 4.13–4.18 on the leaf, ≥3:1 as rings everywhere.

**The rendered-node walk reproduces.** Homepage minimum **5.37 light / 5.66 dark**;
tradition page **5.39 light / 5.66 dark**; **zero failures** on either page in either
register; **zero text nodes under 13px**. These are the exact figures §12 and
Appendix B publish. Overflow is 0px at every width I tested on both pages in both
registers.

**The motion inventory is true.** Tradition page: zero animations, zero transitions.
Homepage: two animated elements, both the mark, zero transitions, achieved by
omission and not by a global override.

**The structural claims hold.** Tradition page: 33 tab stops, exactly as claimed.
Homepage heading outline H1 → H2 → H2 → H3×2 → H4×7 → H2×4, no skipped levels. The
first "Ask" link on the unfixed hybrid sits at **2,627px** and the question input's
top edge at **897px at 390×844** — the review's own two numbers, reproduced to the
pixel, which is what §12 claims for the unfixed baseline.

**The data claims are the most impressive part, and they are correct.** Every one of
these I checked directly and every one is exact:

- The seven-chairs table: all seven census ids, names, roles, tradition names, dates
  (including Marius's `c. 312-451` and Chilo's `c. 325-394 CE` with their hyphens
  and Marius's missing era marker), regions, tint hexes and portrait filenames.
- The record-store table: **156 / 192 / 183 / 182 / 190 / 259 / 173** records per
  tradition, and the per-type counts (`honest_limit` 4/3/4/7/6/2/4,
  `doctrinal_witness` 17/13/22/12/16/26/16, `term` 13/51/10/12/18/39/23,
  `voice_craft` 1×7) — every single cell right, and **every record in all seven is
  `status: draft`**, so ruling 4 is framed on fact.
- The two record-store id seams (`cappadocian-trinitarian`, `imperial-juridical`)
  are real; the Bethlehem `sourcing` really does still say "four built worlds";
  the census era heads really do carry hyphens.
- All six homepage canon questions and both tradition-page canon questions are
  **verbatim** in `engine/canon/records/canon_question/`, and all 23 P-cell questions are
  `canon_status: seed`. All three W1 starters are verbatim, and that file's header
  really does say "DRAFT — awaiting Mark's review. Not deployed."
- The PAHC `sourcing` line, `floorNote`, `voices` list and both `experienceToday`
  links are verbatim from the census. The `pahc.craft.chloe-voice` identity sentence
  is verbatim with ruling 17's bracketed elision correctly placed.
- The app claims: `parseDeepLink()` reads only `worlds` and `mode`;
  `consumeDeepLink()` strips before render; `ChatInput` is `useState('')` with no
  prop; `canConvene = seated.length >= 2` and line 134 renders "Seat at least two
  voices" disabled; `sessionStore` is `sessionStorage` by stated design;
  `Conversation.tsx`'s in-tab note is the current one. The four-line deep-link
  contract in §4.3 matches `App.tsx`'s own header comment exactly.
- The live-site claims: `_headers` has no `Referrer-Policy`; there is no `404.html`;
  the pilot and cost paragraphs really are **below** the carousel (index.html
  169/172–173), so §1.2's correction of the hybrid's parentage claim is right;
  `support.html` really does carry a different footer line; `pilot-feedback.html`'s
  footer nav really does omit Feedback and Privacy; the three ad hoc `--muted` dark
  fixes are at index.html:48, support.html:204, pilot-feedback.html:29; the live H1
  really does capitalise "Church" while the constitution's §5.1 quotes "church"
  (ruling 25 is correct); `whats-next.html`'s meta really does say "three new
  worlds" and its Atlas sentence really does contradict `support.html`'s.

**The tradition-page landmark numbers are genuine re-measurements, and I can prove
it.** Appendix B's figures sit at a constant **+29px** from what the current file
measures (seat line 1,348 identical; silences 2,383 vs my 2,383 measured to the
section; record and closing likewise; page height 16,663 vs 16,634). A uniform +29
below the "Who is speaking" section and zero above it is exactly the signature of
one added line-wrap in that section — which is precisely where ruling 17's
`this [tradition's]` elision was applied. That is a fingerprint of an honest
re-render of a modified copy, not a copied number.

**Fidelity to the struggle record is clean.** I checked the register against the
hybrid's README §8 (rulings 1–12), the defense's §5.4 (13–20), the review's five
conditions and its unnumbered findings, and the decisions the record explicitly left
to D3. **Nothing is dropped and nothing is mislabelled DECIDED except one cell**
(finding R11). Only rulings 5 and 14 carry DECIDED, and 14 is correctly cited to
Mark's own Decision-Log entry. The four parentage corrections in §1.2 match the
defense's §2 and §3.4 word for word in substance, including the one the review
called a misrepresentation — and it is correctly re-filed as ruling 19 (Mark's call)
rather than quietly kept as inherited. All five review conditions are met: the fold
fix is applied and works, the offered-questions trade is ruling 13, the pilot copy
is below the seven, all four measured defects and all four overstated claims are
corrected, and the three missing rulings (16, 17, 18) are added.

**Nothing that was killed comes back.** I grepped and read for each:
04's liturgical apparatus is absent — zero occurrences of narthex, ordo, rubric,
order marker, station, "Silence is kept," "Continue when you are ready," scroll-snap
or the global `transition:none` anywhere in either document except the "what died"
list itself. 02's map is one link in a late section with no band (ruling 23, argued).
03's method, status dashboard, confidence-scale preamble and catalogue table are all
one click deep or absent, and the confidence legend sits beside the contested list.
05's SaaS skeleton is gone on seven of the eight structural tests its own review ran;
its chronology-first ordering survives, and the synthesis says so out loud in §3.2,
§9 and ruling 13 rather than claiming a fix it does not have. That is the right
posture and it is the same one the defense took.

That is a real body of work and none of §3 denies it.

---

## 1. The question the charter actually asks — does it still serve the heart audience?

**Yes, and measurably better than the defended hybrid did.** Three of the D2
review's structural harms against Mark's named person are closed here, not softened:

1. **The door is in the first screen.** I reconstructed the reorder §12 and the
   defense's Candidate B describe — sandbox note stripped, side door gated, door
   eyebrow dropped, H2 and input directly under the H1, the lede cut to its final
   clause and moved beneath the input, its first sentence to the `#who` scope line —
   and measured. The input's top edge lands in the first screen at **320×844,
   360×800, 390×844, 390×740, 390×660, 414×896, 768×1024, 1280×800 and 1440×790**.
   That is the claim, and it holds; see R3 for why my absolute pixel figures are
   higher than §12's and why that makes the conclusion *stronger*, not weaker.
2. **The scarcity paragraph is out of the confession's landing zone**, moved below
   the seven — which, as the defense established and I confirmed against
   `index.html:169–173`, also restores the live site's own order. And ruling 20 does
   not stop there: it puts the register itself to Mark with a re-draft offered.
3. **No app link precedes the AI disclosure on the homepage**, because both the
   header side door and the welcome-back line are gated on the returning flag. I
   confirmed the two offending links in the unfixed hybrid are exactly the two the
   review named, and the gate removes both for a first-time visitor.

The content that made the hybrid win the first-screen test is intact and unhedged:
the lede naming the person Mark named, the six real questions in their own words,
the captured exchange as a skeptic's press. The register test passes as cleanly as
it did for the hybrid — a well-set page with a question on it.

**What the generalisation costs.** From one tradition to seven, the *register* does
not dilute; the *population* does, in ways the storyboard sees at the field level
but does not always draw out. The silences run 2 to 7 per tradition, so a
Cappadocian page has three where Chloe has five and Church and Empire has eight, and
the template's whole argument is "the silences, whole, said first" (r10). The
per-tradition question mapping, portrait captions and record clearances are named as
content work (rulings 3, 4, 13) — correctly. The one place the generalisation leaves
a real hole is the launch state itself (R1), and the one place it leaves an unowned
body of content is the reviewer's-brief material (R7).

From one homepage mockup to a full storyboard, nothing is lost and the carried pages
are handled with restraint — About, Get Involved, What's Next, Privacy and Pilot
Feedback take the chrome and the usage layer and almost no new words, which is the
right instinct for a page whose copy has been rewritten six times in a week.

---

## 2. Internal consistency between the two documents

Mostly tight; the two documents agree on the breakpoint system, the states, the copy
tags, the doors, the rulings numbering and the measurement caveat. Four real
disagreements, all in §3: the type table versus the type the storyboard specifies
(R2), the header heights (R3), the H3 count in the record section (r2), and the
lexicon target-size rule (r1). Two smaller pointer errors (r4, r13).

---

## 3. Required fixes before freeze

All eleven are edits to these two files. None requires re-measuring the design, and
none reopens a D2 question.

### R1 — The homepage's launch state under ruling 4 is not specified anywhere

Ruling 4 recommends that each tradition page ships only when its own quoted records
clear, and storyboard §2.10 handles that correctly *for the tradition page* ("The
page does not exist; the homepage chair shows no record link. No placeholder.").
The homepage does not carry the consequence. §1.3h's record link is described as
"present only when that tradition's page exists," but:

- §1.8's states table has no row for it.
- §1.9's screen-reader walk and keyboard path describe seven chairs with two actions
  each and **40 tab stops**. At launch, on D3's own recommendation, the homepage
  most likely has one record link and six chairs with one action — **34 stops**, an
  asymmetric list, and a different reading order.
- §3.3's step map states "**The record | one click | from any chair**" without
  qualification. That is true only after all seven clear.

This is the single most likely shipping configuration of the site's most important
page, and it is the one page state the storyboard does not draw. Add the row, give
the reduced keyboard path, and say what an unlinked chair looks like (nothing? the
tile alone?). Qualify §3.3's row.

### R2 — §6.1's H3 row does not describe the type the storyboard actually specifies

§6.1 sets "H3 / H4 | Alegreya 500→700 | 1.15rem / 1.25rem." The reference
implementation — which the storyboard specifies section by section — sets:

| Heading | Actual treatment |
|---|---|
| Homepage era heads (H3 ×2) | **Alegreya Sans, 0.8125rem, uppercase, letterspaced, 700** |
| Homepage margin notes (H3 ×4, §1.4f–i) | the same sans label |
| Tradition silences (H3 ×5, §2.5d) | Alegreya 700, 1.15rem ✓ |
| Tradition record sub-heads (§2.8) | Alegreya Sans, 1.05rem, uppercase |
| Chair names (H4 ×7) | Alegreya 700, 1.25rem ✓ |

A builder following §6.1 literally would set the era heads and the four margin-note
heads in 1.15rem serif and change the look of two sections. The row is also
ambiguous on its own terms: the table's column is "Size / leading" and every other
row gives a unitless leading (1.65, 1.12), so "1.15rem / 1.25rem" reads equally as
two sizes — which would put H4 *above* H3 in the scale. Split the row by context and
give the leadings.

Related, and cheap: §1.2h calls the offered-questions label a "small caps-style sans
label" while §6.1 says "no small caps" and ruling 19 puts small caps to Mark. Say
"uppercase, letterspaced sans" (r6).

### R3 — The header heights contradict each other, contradict the 44px rule, and are not reproducible from §12's own inputs

Three figures are in play for the same chrome:

- §4.2 and §12: **110px** at 320–390 (two nav rows), **61px** at 414, **41px** at
  768 / 1280 / 1440. Storyboard S.2 repeats these.
- §8's breakpoint table: "**≤480 | … header 118px** (one nav row from 414; two at
  ≤390)" — which, on its own parenthetical, describes a one-row header at 414–480
  and therefore contradicts §12's 61px for the same band.
- Storyboard S.2 and design R-A4: "Nav links are **44px-tall targets**." **A 41px
  header cannot contain 44px-tall nav links.**

And none of 110 / 61 / 41 is reproducible from the artifact §12 says it measured.
Applying exactly the fixes §12 lists (including the gated side door), I measure the
header at **168px at 320, 360, 390 and 414** (two nav rows — and the review's §7.2
finding is confirmed: gating the side door changes nothing at 320–414, and costs a
row only at 480, where I get 118 gated versus 168 ungated, which is where §8's 118
evidently comes from), **118px at 480–640**, and **73px at 700–1440**. The
difference from §12's column is a near-constant ~58px on phones and ~32px on
desktop — the signature of a chrome change (tighter nav padding, most likely) that
§12's list of applied fixes does not include.

**This does not endanger the fold claim; it strengthens it.** With a header 58px
*taller* than the one §12 reports, the input still lands in the first screen at
every viewport named, including 390×660 and 320×844. So the load-bearing conclusion
survives with margin to spare. What needs fixing is the record: state the chrome
change in §12's list and re-measure the header column, reconcile §8's 118 with
§4.2's 110/61, and make the header height and the 44px nav-link rule consistent.

### R4 — The fifth silence is an undeclared elision of a record quote

Storyboard §2.5d files "**One voice, under guard** (91 words, the guard line of
`pahc.craft.chloe-voice`)" as `[RECORD — verbatim, status: draft in the store]`.
The record's `guard` field is **102 words** and opens:

> *"The one fleet floor line, absolutely: honest thinness over invented depth."*

The page begins at the next sentence — "What our own life did not leave behind…".
The 91-word figure is the *elided* length. Dropping that opening is the right call
(it is internal build jargon and would trip the Never list), but under §0.1's own
definition of the tag ("quoted exactly"), under ruling 17's own precedent (a
bracketed elision, declared, with the record cited), and under §1.2's own promise
that "every quotation there is exact or marked as a paraphrase," it has to be
declared. This is the same class of finding the D2 review made about the census
dashes — one instance flagged, an identical one silently normalised — and the
synthesis is otherwise scrupulous about exactly this.

### R5 — The pressure checklist's item 8 is violated by the tradition page's own specified order

§3.7 item 8 is stated as binding on every surface: "The AI question raised by us,
first, before any conversation link." The brand's own "Always" says the same. The
homepage honours it (verified). The tradition page does not, and its order is D3's
own specification, not an accident:

| Element | Position (measured, 390×844) |
|---|---|
| §2.2b "Begin a conversation with Chloe" (`?worlds=…&mode=interview`) | **1,423px** |
| §2.2c "Bring Chloe to a Table" | **1,477px** |
| §2.4's H2 "An AI system, speaking for a whole people" | **1,603px** |

A visitor who arrives at a tradition page directly — a shared link, a search result,
which is exactly what seven indexed pages are *for* — can enter a conversation
having passed no AI disclosure at all. This is the 05 review's §1.3 charge
("a visitor could reach the app without passing the disclosure") reappearing one
page over. Either put a one-line AI sentence above the seat line (the homepage's
1.2g pattern already exists), or name the exception in §3.7 and argue it.

### R6 — No sanitisation or length rule for the restored `#q=` fragment

The design turns a free-text field into a shareable, bookmarkable URL and asks D4 to
rebuild that path fragment-first. §5.1 specifies `maxlength` 280 on the input and
nothing at all about the value read back out of the fragment. The reference script
is safe (`.trim().slice(0, 280)` and `heldQ.textContent = text`), but the reference
script is the thing being replaced, and the frozen record is what D4 builds from.
State it: truncate to 280, render with `textContent` and never `innerHTML`, and say
what an over-long, empty or undecodable fragment does. For a page whose entire
thesis is "the question you typed, held and shareable," an unstated escaping rule is
the wrong thing to leave to the build.

### R7 — The `[BRIEF]` material has no clearance gate, never reaches Mark, and has no verified source for six of seven traditions

§2.8 — the sources table with Standing and Disclosed dependency, the seven gravities
with their Primary / Supporting / Tensional / Declined classifications, the contested
list, and the four "press first" questions — is tagged `[BRIEF — the tradition's
reviewer's brief, arranged]`. That material is:

- participant-facing evidentiary claims, on all seven pages;
- **excluded from Appendix A** by its own preamble ("Verbatim, live, census, record,
  canon, starters, capture and **brief** material is not listed"), so Mark's
  approval pass never sees it;
- covered by **none** of the content-clearance rulings (2, 3, 4), which name canon
  questions, starters and record text and stop there;
- traceable to no file. I searched the repository: there is no artifact named a
  reviewer's brief for any tradition. The nearest per-build artifacts are
  Facilitation Briefs, which exist for five of the seven — **Imperial-Juridical and
  Syriac have none**. The `[BRIEF]` tag's own definition says "for Chloe, the
  House-Churches build's," and the hybrid's file comment says "via D1-03," which
  points at Direction 03's compilation rather than at a primary source.

Every other body of content on this page is named down to the record id. This one
is not. Either name the source file per tradition and add a clearance ruling
alongside 2/3/4, or say plainly that §2.8's brief-derived sub-sections are Chloe-only
until the artifact exists for the other six — which would be a real change to what
the template promises.

### R8 — D0 seam G is the one seam that disappears

The D0 note's seams are otherwise all carried: A → ruling 32, B → ruling 33, C →
§11.2, D → §5.2/§11.4, E → storyboard §8, F → §1.7/§4, H → §11.4. **G is gone.** It
read:

> *"The business-model gate on multi-Representative tables may have already
> loosened, unconfirmed… Worth confirming with Mark rather than assuming either way
> before D1 designs entry points around it."*

V2 promotes "Set your own table" to a **named third door** in §4.3 and puts "Bring
{Name} to a Table" on all seven tradition pages, twice each — designing entry points
around precisely the thing D0 said not to assume either way. Ruling 11 answers a
different question (is the multi-voice code live), ruling 18 a third (does the
single-seat landing state work). Neither asks whether a free interview entry point
should surface the Table at all. It is a decision with a real tradeoff outside
design, which is §0.2's own definition of ⚠ OPEN FOR MARK. Add it.

### R9 — The storyboard carries ⚠ items that never reach the register

§10 states "Nothing dropped," and Mark's freeze pass is organised around §10 plus
Appendix A. Three items needing his decision live only in the storyboard's prose:

- §5's **two content checks marked ⚠** — `whats-next.html`'s meta description still
  saying "three new worlds," and the `whats-next.html` / `support.html` contradiction
  about the Atlas's scope. Both verified real; neither is in §10.
- S.3's "**Mark to confirm the entity line as the single footer line**," which is a
  copy change to two live pages.

Add them, or add one line in §10 pointing at the storyboard's page-level ⚠ items so
the register's completeness claim stays true.

### R10 — No `<title>` or `<meta name="description">` for any new page

The storyboard specifies seven new tradition pages and a new 404 and gives neither a
title nor a description for any of them, though the live site carries both on every
page in a consistent form (`X — Church in Conversation`) and both are participant-
facing copy under the draft-and-approve rule. Seven pages whose entire purpose is to
be found, shared and linked from a chair are the last place to leave the shared
string unspecified. (There is no OG/Twitter-card convention on the live site to
inherit, so none is owed — but the title and description are.)

### R11 — Ruling 5 is marked DECIDED for something Mark has not decided

The register's ruling 5 ("The question in the deep link") reads **DECIDED — see 14**.
What Mark decided on 2026-09-02 is the *transport* — fragment, never query string.
The Decision-Log is explicit that the change order itself is not authorised: "the
actual `App.tsx` change… is D4's to build when this increment is scheduled, not done
here," and §5.2/§11.1 agree ("its own decision to schedule, its own deploy"). The D2
review's closing paragraph names this as the decision Mark most needs to see:
*"'authorise this direction' and 'authorise one line in App.tsx' are the same
decision, and the second one is where the door actually opens."* Filing it under
DECIDED is the one cell in a 33-row register that reads as settled when it is not.
Split it: 5 stays DECIDED as to mechanism, and the change order's authorisation is an
⚠ OPEN FOR MARK item with D3's recommendation (schedule it; the door is unfinished
without it).

---

## 4. Recommended, not blocking

**r1 — Lexicon and breadcrumb target sizes.** §2.11 asserts "the lexicon buttons
carry a 44px hit area on phone per the constitution's §2.4." The constitution does
require that (§2.4, and §7 item 9: "44px padded hit areas on all inline marks"), but
R-A4's ≥44px list does not include them, §12's verification passes them under the
inline exception, and the reference measures them at **74×29, 86×29, 67×29 and
92×29**. The assertion is stated, not applied, and not verified. Same for the
tradition page's breadcrumb links at **34px tall** — nav links under R-A4's own
wording, and unmentioned in §2.11's touch paragraph. Put the lexicon terms, the ✲
and the breadcrumb in R-A4's list, or say why they ride the exception.

**r2 — The record section's H3 count.** §2's outline and §2.11 both say the record
section carries **8 H3s**; §2.8 enumerates **7** (c, d, e, f, g, i, j — h is a
label). The reference has 8 because "Where this record is contested, by its own
account" is its own H3, folded into 2.8g in the table. Restore it or fix the count.

**r3 — Two word counts, two methods, one row.** §2.7c gives "297 words" for
`pahc.witness.what-we-never-settled`; the record's `text` field is **184 words**, and
297 is the rendered count *including* the four lexicon glosses. Its companion (106
for `doubt-and-asking`) is a pure record count and is exact. Use one method.

**r4 — §1.5g's cross-reference is off by one row.** The protected line the hybrid
used twice was "What it means for you is yours to own and share," which now appears
once at **1.5o**, not 1.5n. The fix itself is correctly applied — I confirmed the
duplication in the hybrid at homepage lines 495 and 509 and it is gone here.

**r5 — "Two animations" is three animation-names.** The mark carries `cic-buildC` on
one element and `cic-sitdown, cic-breath` on another: two animated elements, three
names. §6.3's inventory row describes the breath, so the inventory is complete — but
§7.3 item 4 tells the verifier "the inventory must equal §6.3," and a script
asserting exactly two would fail. Say two elements, three names.

**r6 — "small caps-style"** (§1.2h) beside ruling 19's exclusion of small caps. See R2.

**r7 — "Three doors, ranked" is a slightly larger stretch than ruling 1 states.**
§4.3 names *Start with your question · Choose a voice · Set your own table*. The
constitution's three co-equal S0 doors are *Start with your question · Build your own
table · **Guided onboarding***. The site keeps two, substitutes a chronological
picker for the third, and drops guided onboarding entirely — correctly, since the D0
note records that it is not built, and the hybrid said so in its §10. Neither D3
document says it. One clause in ruling 1 closes it.

**r8 — The re-set transcript grammar departs from the constitution's, for good
reasons, unnamed.** §1.4d/1.4e say the leaf is "set in the app's decided long-form
grammar." Constitution §4.1 specifies the Representative's label as "a **gold
small-caps** label (name · world)" and the Facilitator as "centered, italic,
**graphite**." V2's own usage layer (gold-leaf never sets small text; graphite never
sets text) and ruling 19 (no small caps) make both impossible, so the storyboard
correctly renders ink-with-a-gold-rule and italic muted. Both departures are right;
neither is named. One line in §6.2 or a register note.

**r9 — A census seam §11.3 misses.** §2.1e derives the status line from `statusWord`.
Six traditions carry "Open for conversation"; **Cappadocian carries "Built & Live"**
(it is also the only entry with `glyph: "live"` and a `.jpg` in `entry.icon` where
the other six carry world-icon SVG paths). Rendered as specified, Chilo's page reads
"Built & Live — you can sit down with this tradition now" — internal jargon on a
participant surface, and the Never list names project jargon. Add it to §11.3.

**r10 — The silences do not generalise evenly.** Chloe has 4 `honest_limit` records
plus the guard = five sections. Cappadocian has **2** (three sections); Church and
Empire has **7** (eight). §2's table shows the numbers; the template never says what
"the silences, whole, said first" looks like at three or at eight, and §9's page-
length sacrifice is computed only for Chloe. One sentence.

**r11 — The reading-level floor is not in the verifier.** The Brand Guidelines set a
10th-grade reading floor; the D2 reviews measured it (8.2 homepage / 10.1 tradition
on the hybrid). §7.3 drops the check, though D3 wrote ~85 new participant-facing
lines. I measured D3's drafted copy at roughly grade 5–6 overall, with the record-
page apparatus (2.8f, 2.8g) running 11–15, which is where a record page belongs — so
nothing is broken. The check still belongs in the list.

**r12 — Two claims want a qualifier.** §4.2's "the next Tab lands… on the question
input (verified)" is true for a first-time visitor; for a returning one the
welcome-back link comes first, as §1.9's own keyboard path correctly shows. And
§3.3's "The record | one click | from any chair" is R1.

**r13 — "storyboard §G.3 / §R"** in §5.2 points at `CiC_Full_UX_Storyboard_V1_0.md`,
not at this document's own companion, which §0 calls "the storyboard." In a record
about to be frozen, name the file.

**r14 — §2.3's nav is not in §2.12's page height.** "The page is 16,663px… navigable
by §2.3" pairs a measurement taken without the "On this page" nav with the feature
that makes the length navigable. Trivial, but say so.

**r15 — One cross-feature interaction.** On a tradition page reached with `#q=`
(§2.2), clicking an "On this page" link (§2.3) replaces the fragment and drops the
held question from the URL. The chair hrefs are built at load so they keep it, but
sharing or bookmarking from that point loses the question. One build note.

**r16 — For Mark's copy pass, not a fix.** A few drafted lines stack two negations in
one sentence — §2.1h ("a painted portrait, not a photograph: a face from this
tradition, not one person"), §2.4b ("a voice, not a person who lived"). The Never
list bans "stacked 'not X, it's Y' contrast as a sentence shape," and the Always list
explicitly permits "a clarifying contrast naming what kind of thing this is," which
is what these are. Defensible; worth his eye rather than a rule.

---

## 5. On draft-and-approve discipline

Strong, and consistently applied. 84 `[DRAFT COPY — pending Mark's approval]` tags in
the body, every one of them collected in Appendix A; ten register tags in all, each
defined in §0.1 or the storyboard's Conventions; the two provenance tags the
storyboard adds are declared where they are added. I checked every
`[LIVE — carried unchanged]` string against the live site — all present, all exact —
and every `[VERBATIM — locked, Brand Guidelines]` line against the Brand Guidelines:
the hook, the two measurement/testimony lines, the silence line, "Come and join us at
the Table" and the mark's public sentence are all verbatim and correctly placed, and
the one protected line the hybrid used twice now appears once. Nothing drafted reads
as decided.

The two failures of the discipline are both above: **R4** (a record quote tagged
verbatim that is silently elided) and **R7** (a whole body of participant-facing
content that is neither drafted, nor gated, nor sourced, and therefore never reaches
the approval pass at all). Both are fixable inside the tag system that already
exists.

---

## 6. Verdict

**Ready to freeze with the eleven required fixes in §3.**

The honest comparative statement, because it is true and it matters for how the list
above reads: **this is the most accurate document this workstream has produced.**
Sixty-two contrast ratios exact. Seven traditions' record counts exact to the file.
Eight canon questions and three starters verbatim. Every census field right,
including the ugly ones the record would rather have tidied. A landmark table whose
own +29px offset traces to the one change it says it made. A rulings register that
carries all twenty inherited items plus thirteen more, that marks only what Mark
actually ruled as DECIDED, and that hands back to him — with a recommendation and a
reason — every question the process could not answer for him. It applies each of the
D2 review's five conditions, and it applies them where the fix actually lands rather
than where it was easiest.

It also does the thing the charter's convergence gate exists to test: the door is
first *and* in the first screen; the confession is not answered with a rationing
notice; the AI question is raised before any way in; and the one thing the site
cannot fix alone is named as the app's, sized honestly, and put to Mark as its own
decision.

Six of the eleven required fixes are precision — a type row, a header column, an
elision, a cross-reference, a register cell, a title tag. Five are substance: the
launch state the site will actually ship in (**R1**), an AI disclosure a direct
arrival can walk past (**R5**), an escaping rule for the one string the whole design
puts in a URL (**R6**), a body of evidentiary content with no owner and no gate
(**R7**), and the business question V2 quietly designed entry points around (**R8**).
None of the five requires re-deciding anything. All five require someone to write
down what is already true.

**One line, if only one is read:** the synthesis converged what the struggle earned,
and the places it needs correcting are places it wrote down less than it knew — not
places it got the design wrong.

*— Opus, D3 gate. Every ratio was recomputed, every record count read from the
store, every quotation opened at its source, and every pixel figure measured in
the same Chromium the D2 reviewers used. Nothing outside this file was written.*
