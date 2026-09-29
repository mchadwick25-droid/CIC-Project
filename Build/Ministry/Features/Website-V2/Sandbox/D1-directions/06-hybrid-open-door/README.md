# Direction 06 — The Open Door (a hybrid, with named parentage)

**Sandbox artifact, 2026-09-02. Not a deliverable, not final copy.** Commissioned after
D2 under the charter's own rule — *"hybridization is allowed only after critique — a
hybrid is a new direction with a named parentage, and it too gets an Opus review."*
Authorized by Mark after reading the full D2 record. Files: this README,
`homepage.html`, `tradition-chloe.html`. Both open from disk; portraits and live-page
links resolve by relative path into `cic-website/`. Google Fonts load exactly as the
live site's do (the sandbox blocks that host, so every measurement below was taken in
fallback faces — pixel heights are font-sensitive, ratios and semantics are not, the
same caveat every D2 reviewer stated).

Unlike the five D1 authors, this author read all five directions, all five reviews, all
five defenses, and the struggle summary — and checked the summary's claims against the
ten source files rather than trusting it. Every structural decision below names the
direction, review, or defense it came from. Where nothing in the record supplied a
decision, that is said, and the reasoning is given.

---

## 1. The philosophy, as a synthesis

The five D1 directions each led with something — a book, a map, a method, a rite, a
feature grid — and each died, in its own way, on the same fact: Mark's heart audience
arrives holding a question, and none of the five gave them a place to put it down. Four
of the five defenses reached that conclusion independently (01 §3.2, 02 §4, 03 §3, 05
§3.2), and the fifth (04 §3.4) found it "would have killed the direction even if the
rubric had never been written." It was not a new idea: the UX constitution designed this
door at S0 in July — *"Start with your question"*, co-equal with the others — and no D1
direction built it.

So this hybrid's spine is that door, built. The homepage opens with the protected hook
and, directly beneath it, one real place to write a question and six real questions
people bring, each leading to a real chair. Everything else on the page serves that
first move or follows from it: who you can ask (the seven, as places), what a
conversation actually looks like (one captured exchange), what holds the thing to the
record and what is unfinished (the disclosure block), one link to the map, and the
support slot in the quietest register.

One click deep, a tradition's page does what D1 discovered twice over from opposite
starting points: it lets the voice say who is speaking and where its record is quiet
*before* it offers the record itself — Direction 01's chapter order (provenance →
"Where we are quiet" → the hardest questions first → the door), carrying Direction 03's
record (collection → assembly → trust → chair) as the second screen its own defense
argued it always was.

The register throughout is the constitution's own — *"a beautifully set trade book on
parchment — warm, unhurried, nothing antiquarian, nothing tech-forward"* — held by the
discipline Direction 04's defense extracted from its own kill: nothing moves but the
mark, nothing fades, lifts, or dims, one action per surface, every colour measured. The
Quiet is kept; the Liturgical is not.

**The opening sentence, corrected from 01's:** the visitor is a guest who arrived with
something, not a reader who arrived curious. The site's first job is to take what they
brought.

---

## 2. Named parentage — every major decision

| Decision | Where it comes from |
|---|---|
| **A real, prominent "Start with your question" door as the homepage's first surface** — one input, held on the page in the constitution's own R0 grammar ("Your question, held:"), editable, never discarded, never sent ahead (and the page says so) | Constitution §5.1 (S0 door 1), §5.4 (S3: "one input box"), Storyboard §R0. Never built by any D1 direction. Named as the missing move by the 01 defense §3.2, 02 defense §4, 03 defense §3, 04 defense §3.4, 05 defense §3.2, and by the Decision-Log's D2 closure. |
| **Six offered questions beneath the input, in the visitor's own register, each a real link** — doubt, leaving, unanswered prayer, hypocrisy, suffering, "I want to believe… but I can't" | The 05 defense's "offered, not typed" reading of the door (§3.2): real canon questions, zero fake controls. Source: `records/_fleet/canon_question/*-p-*` (the P-cell, 23 questions, all `canon_status: seed` — a ruling for Mark, §8). The 05 review §5.2 supplied the vocabulary count (doubt 0, struggling 0, searching 0) this list answers. |
| **The S3 theme chips are NOT built** ("An ordinary day · How you looked from outside · What you never settled") | They run the Tier-3 router (Storyboard §R), which is unbuilt (`App.tsx parseDeepLink` reads only `worlds` and `mode`). A chip that routes nowhere is the decoy control the 05 review §2.1 killed. |
| **The typed question is held, not transmitted; a one-line `q` parameter is proposed for the app's deep-link grammar, not assumed** | Storyboard §G.3 already specifies "the question arrives pre-filled, never auto-sends." The 04 review §4.6 killed a control that "appears to accept a choice and silently discards it" — so this one says in plain words what it does. See §8 item 5. |
| **The mark appears once, in the hero, with its public sentence beside it at caption size; the header carries the wordmark only, with the italic *in*** | Logo Usage Sheet ("never at first contact without this one plain sentence beside it"; "lead with the wordmark wherever words fit"); the 02 review §2.1 calling exactly this lockup correct; the 05 review §2.4 ("one mark, in the hero, with the sentence beside it, would satisfy the rule cleanly"); the 04 review §1.3 on why the sentence is a caption, not a headline; the Decision-Log's D1-closure note that the live header breaks both rules. |
| **The protected hook is the H1; a short lede names the person Mark named in the first screen** | Constitution §5.1; 01 review §6.1 (the audience named once at screen 22.8) and 02 review §6.2 (the live pilot sentence deleted). The live pilot sentence itself is kept verbatim, above the chairs, where the live site has it (05 defense §1). |
| **The AI sentence sits inside the door, before any link** — plus the full disclosure block further down | Brand "Always" ("raise the AI trust question yourself, first"); 05 review §1.3 (a visitor could reach the app without passing the disclosure); 05 defense §4.3 ("inside the running head, so no door is passed without it"); 04 defense item 7 (the disclosure as a heading in our own voice). |
| **The seven as places, chronological, one action each, never a carousel; every name a heading** | 04 defense item 5 and its review §1.4 ("materially better than the live carousel for scanning, keyboard use and screen readers"); 01 defense §5.4 (the index needs a conversation link per line); 05 defense §3.2 ("one primary, six text-link secondaries" — here zero filled buttons in the list, the one filled control on the page is the door's); 02 review §4.3 (no Representative in the heading outline). Chronology *under* a question, per 01 defense §3.2. |
| **Tradition tints appear only as portrait rings and one left rule — never as text** | 02 README §4's rule, which its own file broke; the D1-closure contrast finding (four of seven tints unsafe as text). |
| **The general Table entrance survives as one quiet second door, promising nothing about the experience** | 02 review §4.2 (its removal was "a hard regression"); 01 defense §6.2 (the seating field must not be the primary door for the heart audience); D0 seam D; 05 review §2.6 (multi-voice Table verified in the repo, deployed engine unverified — see §9). |
| **One captured exchange, in the app's long-form grammar, no composer** — and it is Theon's, a skeptic's press answered by a voice naming its limit | 05's "show the real interface" (its reviewer: the stance is "this direction's strongest real contribution"); 03 review §1.2 ("it never shows the product"); 05 review §2.1 (the composer, deleted) and §5.1 (the Sunday liturgy, deleted); 05 defense §3.3 (Theon's `theon-confidence.png` as "the honest hero today"). Transcribed verbatim from `assets/tour-captures/theon-confidence.png`. |
| **"Before you sit down" — the two-column disclosure block** | 03's §4, which its reviewer called "the best-executed block on the page… lift whole"; 03 defense item 2: project negatives (external review, modes, later eras) said once, here, nowhere above the fold. Counts and dates removed (03 review §4.7: a status number is a maintenance promise). |
| **The map is one link, not the page; no map band built** | 02 defense §5.1: the twelve-item `atlas-v3.html` rework brief stands as its own track; the homepage's link is consistent with it (one outbound link, the Atlas's own name). The 02 defense's optional homepage band (§5.2) is deliberately left for D3 to weigh — building it here would re-enter the palette debt this hybrid does not own. |
| **The support slot: live copy verbatim, text links, below everything** | D0 seam F (six rewrites in a week — a slot, not a layout); 04 defense item 2 (the ask below the door in the quietest register; the seeker's voice outranks the donor's); 02 review §1.2 (the only two buttons on the page must never be the donation asks — here they are text links). |
| **A quiet header side door for the returning visitor, and a one-line "welcome back"** | 04 defense items 3 and 4 (the idea was right, placed on the wrong page; shortened so it costs no third header row). `localStorage` in try/catch; invisible to everyone else. |
| **The header wraps; nothing is clipped, no hidden scroller** | 01 review §4.1 (the iPad amputation), 03 review §4.3–4.4, 05 review §4.3 — three directions broke the nav three ways; the fix is to let it wrap. |
| **Tradition page order: who is speaking → where we are quiet → the hardest questions → in her own words → the record → the chair** | 01 defense §5.1 (its exact rebuilt order) merged with 03 defense §2.5 (its founding sentence — collection, assembly, trust — executed on the second screen). Where they conflict, see §3. |
| **"Where we are quiet" carries the tradition's real `honest_limit` records, in the "we" voice, with a source note beside each** | 01's section (its reviewer: "the single strongest piece of writing produced in D1"); its defense §2.3's rule — a margin apparatus belongs only where a record stands behind the text; 01 defense §5.3 (the "we" register). Sources: `records/pahc/honest_limit/*` (four records) and the guard line of `pahc.craft.chloe-voice`. |
| **The questions list: the personal and hardest first, the historian's last** | 01 review §6.3 ("four scholars and one person"); 01 defense §5.1 (the "For the Wrestling" set with the fear question first). Sources: four P-cell canon questions that map to real pahc records, three verbatim opening questions from `CiC_W1_Guided_Starters_V0_1_DRAFT.md` §"For the Wrestling". |
| **The Level-2/Level-3 lexicon, with Level 2 reachable by assistive tech** | 01's implementation ("take it whole"), with its own conceded defect (review §4.4: the short tier was sighted-only) fixed by construction — the term is described by its gloss, so a screen reader hears Level 2 whether or not the card is showing. Verified in an ARIA snapshot (§7). |
| **The sidenote pattern (note inside the paragraph after its sentence; margin at ≥1100px, in-flow below), without the ✲ jump-anchor** | 01's implementation, which its reviewer called better than most published Tufte-style work; the ✲ anchor is dropped because 01's own defense conceded it was a sixth verb (constitution §5.7). Here the ✲ appears only as a picture in the captured exchange, with a caption saying so. |
| **The chair is offered once at the top (outlined) and once at the end (filled); nothing is sticky** | 03 defense item 10 (the outlined button "exactly right at 60px") and its review §4.5 (the 156px phone seat bar); 01 review §4.1 (the sticky running-head door). No sticky chrome removes both bugs and keeps focus-not-obscured trivially true. |
| **The record's confidence legend sits beside the contested list, never before content; the Creed floor note is last** | 03 defense item 3 ("a legend for a map, not a preamble"); 02 defense §3 (the Creed note: content kept, position last, dose once). |
| **No "Plate," "Register," Roman numerals, lower-roman counters, Alegreya SC, drop caps, part-titles, or colophon** | 01 defense §4 and 03 defense §2.1 conceded these as the antiquarian dress; the constitution's "nothing antiquarian." Alegreya SC is not used, so the 01/03 stretch is moot. |
| **No ordo, no rubric, no silences, no order marker, no "Continue when you are ready"** | 04 review §5 and its defense §2 — the framing was load-bearing and it goes; the discipline stays. |
| **Restraint discipline: no reveal-on-scroll, no hover lift, no transitions (by omission, not a global `!important`), no smooth scroll, figures never dim** | 04 defense §6 item 1 (the stillness rule for figures *with its reason*, constitution §2.5a) and its review §3.1 (the sledgehammer) and 01 review §4.4 (smooth scroll rides keyboard focus). |
| **The motion inventory as a deliverable format** | 04 defense item 10. It is in each file's header comment. |
| **The pressure checklist** — no urgency, no scarcity, no countdown, no promised transformation, one action per surface, the ask below the door, a complete decline path | 04 defense item 2, applied as a list, not a mood. |
| **A dark register, kept and fully measured** | 02 defense §2.1 (the live site ships dark mode; removing it would be the deviation) against the constitution's app-only deferral; the D1-closure and D2 cross-direction findings (text *and* graphical failures). Every pair is in §6. |
| **Copy marking with `data-copy`, and a visible `draft` tag on every sentence written for this mockup** | 04's convention (greppable) and 03/05's visible tags; 05 defense §1's rule adopted — *a quote's provenance clears its facts, not its register*: nothing lifted from app code is filed as cleared. |

---

## 3. Where the two inner-page parents conflict, and what was decided

Direction 01's chapter and Direction 03's record are the same page seen from two ends,
and they disagree on four things. Decisions, with reasons:

1. **What comes first after the title — the voice or the record?** 01 puts provenance
   and "Where we are quiet" first; 03 puts scope and sources first. **The voice first.**
   The 03 review's distinction (§3.3) — *disclosure about the tradition serves the
   doubter; methodology about the project does not* — was adopted by 03's own defense,
   and "Where we are quiet" is disclosure about the tradition. The record follows, whole,
   for the reader who then asks what she is built from.
2. **The long essay.** 01's 1,500-word chapter in Chloe's voice is **not carried**. Its
   review sized the content liability (§3.4: ~14,000 gated words before the Reformation
   wave) and its defense conceded the reading-time byline and the periodical frame. What
   is carried is narrower and better sourced: the voice speaks only where a record stands
   behind the line — four honest-limit statements, two witness statements, one guard
   line — every one a verbatim field of a `records/pahc/*` file.
3. **The sticky chair.** 01's running-head door and 03's seat bar both broke on the
   device each was aimed at. **Neither is carried.** The chair is offered at the top and
   at the end; the header side door covers the visitor who already knows the way.
4. **The apparatus.** 01's margin sidenotes and 03's source table both survive, in
   different places: sidenotes beside the voice (where a source backs a sentence), the
   table inside the record (where the reviewer's brief is the source). 03's gravity list
   is kept, compact, because on a record page it is the "assembly" its founding sentence
   names — the 03 review's objection was to methodology on the *front door*.

One judgment the record did not make for me: **how much of "Where we are quiet" to
show.** The four statements are the tradition's own, and they are long — 1,050 words.
I carried them whole, because trimming a silence is the one edit a doubter would catch.
The cost is measured in §7 (the phone page is 16,634px). D3 should decide whether the
statements carry whole or open from their first two sentences.

---

## 4. The four charter goals — and the two heart tensions

**Accessibility.** WCAG 2.2 AA as the floor, with four criteria held higher because the
D2 record showed AA is not met by inheritance (§6). Measured, not asserted: no
horizontal overflow at 320–1440px in either register; zero text-contrast failures;
nothing under 13px; every control ≥44px; no sticky chrome (2.4.11 trivially true);
heading outline that surfaces every Representative; Level 2 of the lexicon readable
by assistive tech; the whole homepage present and usable without JavaScript, including
the door (a plain GET form).

**Clear storytelling.** The story is told in the order the person Mark named needs it:
the hook; a place for the question; who can carry it; what a conversation is like; what
holds it to the record and what is unfinished; the map. Not chronology first (01), not a
map first (02), not a method first (03), not a rite first (04), not a picker first (05).
The brand's four messages appear in the brand's order: the whole Church in the open
(the seven), it shows its work (the exchange, the disclosure), witness never recruitment
(the door's copy, the checklist), the build is the product (one link to About's method).

**Easy access to features.** On a 390×844 phone the door's heading is in the first
screen and the input is at the fold (§7); a tapped question lands on the chairs; a
tapped name is the app. A returning visitor has a one-tap side door in every header.
The record is one click deep; the Table is one quiet link; the map is one link. Nothing
is behind a sheet, a carousel, or a scroller.

**Professional, cutting-edge design that draws people in.** Cutting-edge the way 04
and 05 both argued and neither delivered: the confidence to do less, measured. One
filled control per screen. Typographic hierarchy in the locked pair. Colour that has a
job and a number. A page that is quiet because nothing on it is trying to attract a
click — and warm because the first thing on it is a question in the visitor's own
words.

### The two heart tensions, named in the Decision-Log

**"Engaging and trustworthy (scholar)" — trustworthy because scholarly, not
institutional distance.** The scholarship is *underneath, one click away* — the brand's
own pair, which 03 asked permission to invert and its review refused. The homepage
shows one exchange where a voice is pressed on its confidence and answers by naming
what it cannot show; the tradition page shows the silences before the sources, and the
sources before the chair. The voice pairs run in order on every screen: experience (the
door, the chairs) → governance (the AI line at the door; the disclosure block) →
mechanism (a link to About). Nothing on the front door is a credential.

**"Non-religious feel… my heart is those seeking answers to hard questions of faith,
not academics."** Every register the reviews identified is left behind: the illuminated
codex (01 review §5), the doctrinal vetting board (02 review §5), the divinity-school
finding aid (03 review §5), the order of service (04 review §5), the sepia chat product
(05 review §2.1). What remains reads as a well-set page with a question on it. The
portraits are 72px rings in a list, not plates. The captured exchange is a skeptic's
question, not a service. The word "Jesus" appears where a question names him — sixth of
six, a person's question — and nowhere in the chrome. And the first six things a
visitor can do on the page are ask about doubt, leaving, unanswered prayer, hypocrisy,
suffering, and not being able to believe.

---

## 5. What it sacrifices, honestly

- **It is not a map, a book, a record, a rite, or a product grid.** A visitor who wanted
  to explore twenty centuries spatially gets one link. A visitor who wanted to read gets
  a page one click deep. A scholar who wanted the method first gets a link to About.
- **The typed question does not travel.** Until the app's deep link accepts `q` (§8,
  item 5), the visitor types their question twice — once here, once in the room. The page
  says so rather than pretending otherwise; that is the honest cost of building the door
  before the router.
- **The tradition page is long on a phone** — 16,634px at 390×844, 19.7 screens — because
  five silences are carried whole and the record follows in full. The chair is offered at
  1,348px and again at the end.
- **The seven are still in chronological order.** Under a question, not instead of one
  (01 defense §3.2), but a visitor who wants "which of these is for me" gets no ranking —
  the constitution's own routing was designed to do that, and it is unbuilt.
- **Only Chloe's record page exists.** The other six "record" links go to a note saying
  so. The pattern is one page; the content is seven.
- **The portraits are lazy-loaded and unresized** — 3.4MB of masters for 72px rings (04
  review §4.3). Production needs sized masters; that is a build task, not a design one.
- **No Level-2/Level-3 on the homepage's captured exchange.** It is a picture with a
  caption that says so; the real grammar is demonstrated on the tradition page.
- **04's seat-picker and 02's map band are not carried.** Seating happens in the app,
  behind one quiet link; the map band is a D3 candidate, not a homepage fixture.
- **Two sandbox artifacts inflate the phone measurements**: the sandbox note (53px) and
  the visible `draft` tags. Neither ships.

---

## 6. Typography, colour, motion — inside the locked system, with the usage layer V2 needs

**Type.** Alegreya for reading and display (body 1.0625rem/1.65; the tradition page's
reading column 1.125rem/1.6 on a 38rem measure); Alegreya Sans for labels, chrome,
sidenotes, captions, never below 0.8125rem (13px). H1 `clamp(2rem, 4.5vw, 3rem)` at
weight 500 — a title, not a bold headline. No third face: Alegreya SC is not used.
Italic *in* in the wordmark.

**Colour — the locked palette, plus the rules the D1 closure said V2 needs.** The hex
values are untouched. What is new is a usage layer: which token may set text, on which
ground, at what size. Every pair below is computed from the files' own values (WCAG
relative luminance) and re-measured in the rendered DOM against the painted background.

*Light register (on parchment `#F7F3EB` / vellum `#FEFCF8` / gold-wash `#FBF2E2`):*

| Token | P | V | GW | Rule |
|---|---|---|---|---|
| iron-gall `#2A2521` | 13.70 | 14.80 | 13.65 | text, any size (AAA) |
| ink-faded `#6C6257` | 5.39 | 5.82 | 5.37 | secondary text ≥13px |
| madder `#A13E2B` | 5.86 | 6.33 | 5.83 | action text, focus ring, the one filled button (vellum on it: 6.33) |
| madder-deep `#7E2F20` | 8.20 | 8.85 | 8.17 | hover |
| tyrian `#6B3FA0` | 6.67 | 7.21 | 6.65 | lexicon apparatus, draft tags |
| lapis `#1E40AF` | 7.88 | 8.51 | 7.85 | "Your question, held:" |
| gold-leaf `#B45309` | 4.54 | 4.90 | **4.52** | **rules and ≥18.66px bold only — never small text** (the 05 review's 0.02 margin; this hybrid's own first render tripped it, caught and fixed) |
| graphite `#8A837C` | 3.38 | 3.65 | 3.36 | **control borders only** (≥3:1 as a boundary); never text — the D1 cross-validated finding |
| rule `#E6DFD3` | 1.20 | — | — | hairlines between blocks; **never on an interactive element** (04 review §7.3) |

*Dark register (ground `#17130F`, surface `#1E1913`, leaf `#241C13`):*

| Token | ground | surface | leaf | Rule |
|---|---|---|---|---|
| text `#F1E9DD` | 15.35 | 14.49 | 13.95 | text |
| muted `#B8AEA1` | 8.45 | 7.98 | 7.68 | secondary |
| action `#E08C74` | 7.19 | 6.79 | — | links, focus, button edge — the live site's own value (`style.css` 346) |
| hover `#F0A98F` | 9.48 | 8.95 | — | |
| gold `#E0A458` | 8.47 | 7.99 | — | rules |
| tyrian `#C9A6E8` | 8.89 | 8.39 | — | lexicon |
| lapis `#9DB4F0` | 8.99 | 8.49 | — | held question |
| control `#A39B92` | 6.74 | 6.36 | — | borders |
| button: `#F6EFE0` on `#A13E2B` fill | 5.66 | | | the fill itself is 2.85 vs ground / 2.69 vs surface — **the 1.5px `#E08C74` edge (7.19) is the control's boundary**, so 1.4.11 is met by the border, not the fill (the 05 dark-button bug, avoided by design rather than by accident) |
| the mark: `#EDE5D6` / `#CB6E52` | 14.76 / 5.18 | | | the Logo Usage Sheet's own dark register, for the mark only |

*The seven tradition tints — rings only, never text.* Light, on parchment: House-Churches
`#7c3aed` 5.15 · Alexandria `#2B5F8A` 6.11 · Syriac `#b45309` 4.54 · Church and Empire
`#7A2E2E` 8.40 · Desert `#0f766e` 4.95 · Cappadocian `#A0522D` 5.07 · Bethlehem `#9d174d`
7.12 — all ≥3:1 as rings. Dark: the raw values fail (Church and Empire 1.99, Bethlehem
2.34, Alexandria 2.73 — the cross-direction finding). **Proposed dark tints**, the same
hue lightened to ≥4.5:1 on the ground so they pass as rings by a wide margin and would
pass as text if ever needed: `#955FF0` 4.55 · `#3B83BF` 4.56 · `#CC5E0A` 4.55 · `#C36060`
4.54 · `#128D84` 4.55 · `#C46437` 4.60 · `#E23B7F` 4.55. These belong in the census as a
`colorDark` field (02 defense §5.3 item 1), not in a stylesheet.

**Motion — the whole inventory.** The "Arriving" mark plays once per page arrival, in
the homepage hero, byte-faithful to `CiC_Logo_Arriving_Motion_Reference.html`; the
header carries the wordmark only, so it never plays twice; the tradition page carries no
mark and no motion at all. `prefers-reduced-motion` receives the completed still mark.
Nothing else transitions, reveals, lifts, slides, or dims: not the lexicon card, not the
panel, not a hover state. No smooth scroll. Verified by enumerating every element's
computed `transition-duration` and `animation-name` in both files (§7).

---

## 7. Accessibility floor — and what was actually measured

**WCAG 2.2 AA is the floor. Four things are held higher, because the D2 record showed
AA is not met by inheritance:**

1. **7:1 for running prose in both registers** (01's reading conditions, 03's practice):
   iron-gall 13.70, dark text 15.35. Not full AAA — madder as link text is 5.86, and it is
   the brand's action accent (05's argument, accepted).
2. **3:1 for every graphical boundary** — rings, control borders, button edges,
   underlines — in both registers. This is where four of five D1 directions failed in
   dark mode, and every such element here is measured (§6).
3. **The 13px floor enforced, not declared** — 03's own defense asked for "a lint, not a
   sentence." The verifier walks every text node.
4. **No sticky chrome at all**, so 2.4.11 Focus Not Obscured holds by construction.

Also held: 1.4.10 Reflow (no horizontal scroll at 320px — where 02, 01 and 03 failed);
2.5.8 Target Size at 44px on every control; 2.4.4 Link Purpose (every "Ask X" names the
person; every question link carries a visually-hidden "— ask Chloe"); 2.4.6/1.3.1 (every
Representative is a heading; the outline reads as the page's argument); 2.2.1/2.2.4/2.3.3
(no timing, no interruptions, no animation from interaction); 3.2.5 (every new-tab
hand-off announces itself).

**Measured, Chromium `chromium-1194` via Playwright, both files, 320 / 360 / 390×844 /
768×1024 / 820×1180 / 1024 / 1280 / 1440×900, light and dark:**

- Horizontal overflow: **0px at every width, both registers, both pages.** (First render
  had 249–319px on the homepage from one `nowrap` draft tag, and 96–122px on the
  tradition page from hidden-but-laid-out lexicon cards; both fixed, both re-measured.)
- Text contrast, every rendered text node against its painted background: **0 failures.**
  Minimum light 5.37 (ink-faded on gold-wash), minimum dark 5.66 (button text on fill).
  First render had two gold labels at 4.52 — the D2 margin — fixed by moving gold to a rule.
- Text under 13px: **none**, either page, either register.
- Motion: homepage — exactly two animations, the mark's ring and seat; tradition page —
  **none**; under `prefers-reduced-motion` — **none** on either.
- Headings: homepage H1 → H2 (door) → H2 (who) → H3 ×2 eras → H4 ×7 names → H2 ×4;
  tradition page H1 → H2 ×6 with H3s under the silences and the record. No skipped levels.
- Tab order: 41 stops (homepage), 33 (tradition), none hidden, none under 24px.
- Without JavaScript: the homepage carries all seven names and ten app links in static
  markup (the 02 review's test); the door's form is a plain GET to `#who` — submitting
  lands the visitor at the chairs with the question in the URL.
- The door with JavaScript: submit → "Your question, held:" renders, the URL carries
  `?q=`, focus moves to the chairs; a tapped offered question does the same; "Edit it"
  returns focus to the input; arriving with `?q=` in the URL restores the held question.
- The lexicon: focus on a term shows the card; the term's accessible description *is*
  the gloss (verified in an ARIA snapshot: `button "episkopos" [expanded]` followed by a
  `note` containing the gloss); Enter opens the panel and moves focus to its close
  control; Escape closes it and returns focus to the term; on touch, the first tap shows
  the card as a fixed popover inside the viewport (top 643, bottom 824 of 844), the
  second opens the panel; "Full entry" opens it too. Hidden cards contribute no tab stop.
- Phone landmarks (390×844, including the 53px sandbox note that would not ship):
  homepage H1 at 313px, "Start with your question" at 717px, the input's bottom edge at
  945px, the chairs at 1,861px, the first "Ask" link at 2,627px, the disclosure block at
  7,232px; tradition page: the seat line at 1,348px, "Where we are quiet" at 2,328px,
  the questions at 5,847px, the record at 9,177px, the closing door at 15,998px.
- Images: every portrait has real alt text; all seven load (lazily, on scroll). Print
  media on the tradition page keeps every section visible.

---

## 8. Rulings for Mark — flagged, not made quietly

1. **The question door outranks the other S0 doors.** The constitution's S0 makes three
   doors co-equal, "no default." This homepage gives "Start with your question" the
   first surface and makes "choose a voice" the second screen and the Table a quiet
   third. That is a deliberate ranking, taken from Mark's own 2026-09-02 statement and
   the five-for-five D2 finding — but it is a departure from co-equality and should be
   ruled on, not assumed.
2. **Seed-status questions on a public surface.** All 23 P-cell canon questions are
   `canon_status: seed` (05 defense §4 item 4). They are already served inside every
   live conversation, so this is no new exposure — but the six on the homepage and the
   four on the tradition page are on a marketing surface now, and the 05 defense asked
   for this ruling explicitly.
3. **The World 1 Guided Starters draft is "awaiting Mark's review, not deployed."** Three
   of the tradition page's seven questions are its verbatim opening questions. Same ask.
4. **The tradition's own records are `status: draft`.** The four honest-limit statements,
   the two witness texts, the four term meanings and the voice's guard line are quoted
   verbatim from `records/pahc/*` — the record itself is in draft in the store. The page
   labels them as the record's, not the mockup's; whether draft-status record text may
   appear on a public page is Mark's call.
5. **One line in the app, so the question can travel.** `App.tsx parseDeepLink` reads
   `worlds` and `mode`. Adding `q` — read into the room's input, pre-filled, never
   auto-sent (Storyboard §G.3's own rule) — would let the held question arrive. This
   is a D4 build item, flagged, not assumed; until it lands the copy says "nothing is
   sent ahead," and that copy would change.
6. **Dark mode.** Kept, because the live site ships one and removing it would be the
   deviation (02 defense §2.1) — but the constitution defers it for the app, and this
   is the sixth independent dark register. D3 needs one ruling. Inside it: the site's
   dark action colour is `#E08C74` (7.19), the brand's sanctioned dark madder is
   `#CB6E52` (5.18) — the 02 defense's open question, restated.
7. **The seven dark tradition tints** (§6) are new values, derived, not brand-approved.
8. **The mark leaves the header.** It appears once, in the hero, with its sentence — a
   departure from the live header convention, and the fix for the two Logo Usage Sheet
   breaks the Decision-Log already records against the live header.
9. **"Where it stands on the Creed"** is kept on the tradition page, last in the
   confidence section — the 02 defense's position. The audience question the 02 review
   and defense left open (vetting board, or the absence of a trap?) is still open.
10. **"I want to believe in Jesus, but I can't."** Sixth of six on the front door. The
    03 defense argued a front-door "Jesus" reads as the room the doubter left; the
    subject is the subject. It is a person's question, placed last; Mark should see it.
11. **The `?mode=table` links.** Present as the live site has them; the copy promises
    nothing about what follows. The 05 review verified the multi-voice room in the
    repository's frontend but not on the deployed engine — a live check is owed before
    any such link ships (05 review §2.6, 05 defense item 4).
12. **The "welcome back" line** — a one-line courtesy in `localStorage`. Keep or cut.

---

## 9. Seams found while building — corrections to the record, not smoothed over

- **The D3 brief's summary of the 05 review inverts the review's finding.** The brief
  says the 05 reviewer conceded that "the multi-voice Table is genuinely not live yet on
  the current engine architecture." The review (§2.6) says the opposite: "The claim
  holds. Multi-voice Table is genuinely live in the shipped frontend" (`Launch.tsx`,
  `TableRoom.tsx`, `useTable.ts`), with the deployed engine unverified, and it marks D0
  seam D as partly stale. The 05 defense confirms this. This hybrid follows the primary
  source: the Table links seat a field and the copy describes no experience — which
  satisfies the brief's intent either way. Representative Modes are unshipped on every
  reading and are described as such.
- **`world-census.json` carries Marius's dates as `c. 312-451`** — hyphen, no era
  marker — against `70–200 CE` elsewhere. Reproduced verbatim (03's verbatim-and-flag
  rule); 04 silently added the "CE." A data fix, whichever direction wins.
- **The Chloe capture's role label is stale** ("Host of the Assembly"; registry and
  census say "Household Leader") — already queued as `task_959d6df4`. Not reused here;
  Theon's capture is used instead.
- **The live `whats-next.html` still lists Cappadocian as in development.** This
  homepage says "two more are chosen and being built" (the census: Latin Pastoral,
  Donatism) — consistent with the data, inconsistent with that page until the pending
  fix is pushed.
- **A browser fact the lexicon build hit:** Chromium blurs the focused element before
  focusing the next one, so a Level-2 card hidden on blur swallows keyboard focus (the
  first render lost focus to `body` at every term). The fix — hold `aria-expanded` while
  focus is anywhere inside the term's wrapper — belongs in whatever D3 builds; 01's
  implementation has the same latent race.
- **The corpus-wide "tradition, not world" rename did not reach the record store.**
  `pahc.limit.material-remains`'s participant-facing statement says "those belong to a
  later world" — the voice's own spoken text, quoted verbatim on the tradition page. Left
  as the record has it (a record quote is not the mockup's to edit); a records-layer fix,
  worth a task. Every sentence this mockup wrote itself says "tradition."
- **Chloe's census edges:** five, all `formed` / `contemporary with`; no adversarial
  edge among the built worlds yet, so the 02 review's `edgeRow()` bug is still latent
  everywhere it would fire. Not this hybrid's surface; noted so it is not forgotten.

---

## 10. What was not done, by design

No Atlas rework — that is the 02 defense's own track and is referenced, not
re-executed. No six further tradition pages. No `q` in the deep link. No historical-site
photographs (rights unresolved, D0 seam B). No composed Table scene, no role selector,
no guided onboarding, no Tour — none of it is built, and nothing here previews it. No
"Tour" entry point, so D0 seam E is untouched. No number on the page that is not the
census's own or the live site's own; the one count ("nearly three hundred movements
across ten eras") is the live site's wording for the census's 292.

*— Fable, D3 synthesis. One hybrid, with its parents named. It gets its own Opus review
before anything freezes.*
