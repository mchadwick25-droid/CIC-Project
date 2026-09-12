# D2 defense — Direction 06, "The Open Door" (the hybrid)

**Sandbox artifact. The author's one defense, per the charter. Not a ruling. 2026-09-02.**

Author: Fable. I read the review in full, then re-verified every claim I answer below
against my own two files and the primary sources it cites — not against my README. Where
the review says "measured," I measured again: the same Chromium (`chromium-1194`, driven
by Playwright, Google Fonts unreachable so fallback faces, the caveat everyone in this
workstream has stated), both pages, the same widths. Where the review cites a file, I
opened that file at that line. Where it cites one of the five D1 defenses, I opened only
the section in dispute, not the direction — this defense answers the attack on the
synthesis, it does not redo the synthesis.

The review's own summary of what verifies (§0) I do not re-litigate: the overflow,
contrast, 13px, motion, heading, tab-order, lexicon, quotation and reading-level findings
passed under the reviewer's instruments and mine, and I take the credit as given. What
follows is the other half of the ledger.

The shape of my answer: the review is right about nearly everything it measured, right
about the three parentage claims, and right that the door does not open. It overstates in
four places, one of which matters. And the most serious finding — that the door cannot be
finished on the marketing site — is true, and I say below exactly what it would take,
where the site's share ends, and which part of it is a decision for Mark that is *not*
the same decision as "is this direction good."

---

## 1. Conceded — the measured defects and the false claims, each re-verified

| # | Review | My re-check | Concession, and the fix |
|---|---|---|---|
| 1.1 | **"The input is at the fold" is false.** Input top at 897px on 390×844; 844 with the sandbox note stripped; "Start with your question" off-screen at 390×660. | Reproduced to the pixel: 897 / 844; H2 at 717 (663 stripped) — off a 660 screen either way. At 320×844 the input is at 1,084. At 1440×790 its bottom edge (815) is clipped. | **Conceded in full.** "At the fold" meant "its top edge is at the fold line," and that is the same as "not on the screen." The measurement pass recorded positions without comparing them to a viewport; that is the method error the review names and it is mine. The fix is measured in §5.1 below. |
| 1.2 | First "Ask" link at 2,627px — further than the 2,487px that convicted 05. | 2,627 before submit, as claimed. **After** submit it is worse: the held block adds height and the first "Ask Chloe" sits at **2,804px**. | Conceded as a number. Partly contested as a comparison — §4.1. |
| 1.3 | **The door does not open**: submit → picker → new tab with no `q`. | Verified end to end; §3 is the whole answer. | Conceded. |
| 1.4 | Without JavaScript the question is not held: input empty, `#held` hidden, the question only in the address bar. | Reproduced: `input.value === ''`, `#held.hidden === true` after the GET. | **Conceded.** §7 of the README said the narrow true thing ("lands at the chairs with the question in the URL"); §4 said "usable without JavaScript, including the door," which is not true of *holding*. A static page cannot hold a query string without script; the sentence should have said so. §4's claim is withdrawn; §7's stands. |
| 1.5(a) | "2.5.8 at 44px on every control" false: nav "Map" 35px wide; "About — how it works" 40px tall; fifteen inline controls on the tradition page under 44 in one dimension. | Map 35×49, About 48×49, the About link 332×40 on my render (widths differ by a few px in fallback faces; the finding does not). | **Conceded.** Conformance holds through 2.5.8's inline exception and the 24px minimum; the *claim* was a floor I only met on padded controls — the same overstatement 01 made and conceded, and I read that exchange. The README sentence changes to what is true: "≥24×24 everywhere; ≥44 on every padded control; inline links in prose ride the SC's inline exception." |
| 1.5(b) | "The AI sentence sits before any link" false: the header side door and the hero's welcome-back precede it. | DOM-order dump: two `a[data-app]` precede `.ai-line` — the side door (visible to everyone, **same tab**) and welcome-back (hidden unless returning). | **Conceded.** Fix in §5.3: gate the header side door on the same `localStorage` flag as the welcome-back line. For a first-time visitor no app link then precedes the AI line; for a returning one, the disclosure was passed on a prior visit. This also removes the §7.1 "trap" and the 480px third row (1.6 below). |
| 1.5(c) | "Reproduced verbatim" is not what happened to the census dates: `c. 312-451` → `c. 312–451`; Chilo's `c. 325-394 CE` also silently normalised. | The census is itself mixed: five of the seven built worlds carry en dashes (`70–200 CE`, `c. 150–400 CE`, `200–410 CE`, `c. 320–430 CE`, `c. 382–420 CE`; lines 764, 958, 1009, 1621, 1884) and two carry hyphens (Chilo 1775, Marius 1827). Both era heads are hyphens (`70-312 CE`, `312-451 CE`; lines 31, 48). I rendered all four hyphen cases as en dashes and flagged only Marius's missing "CE." | **Conceded.** Four silent normalisations, one flag. The rule is verbatim-*and*-flag; the flag was missing on the character and present only on the era marker. The seams entry becomes: "dash characters normalised to en dash on the page; the census is inconsistent (five en dashes, two hyphens, both era heads hyphens) — a data fix." |
| 1.5(d) | Proposed dark tints "would pass as text if ever needed" only against the ground; against the surface they are 4.29–4.34. | Recomputed: ground 4.54–4.60, **surface 4.29–4.34, leaf 4.13–4.18.** | **Conceded.** The sentence promised headroom the values have on one ground of three. It becomes: "≥4.5:1 as text on the ground only; ≥3:1 as rings on every ground, which is their only use." |
| 1.6 | **Header space bug**: `display:inline-flex` on the anchor makes the span and the text two flex items and drops the space. "Been here before?Go straight in →" at every width ≥641px, both pages. | Reproduced: span right edge 1009.42, text left edge 1009.42 at 1280 (gap 0.00); 161.16/161.16 at 700; `innerText` shows a line break between the two items. | **Conceded, and the point about the measurement pass is taken.** A script that enumerates contrast and tab stops does not look at the page. One `&nbsp;` inside the span, or `gap:.25em` on the anchor, fixes it; a screenshot pass joins the verifier. |
| 7.2 | The side door "costs no third header row" fails at 480px: 168 with it, 118 without. | Reproduced: 168 / 118. | **Conceded.** The gating fix (1.5b) makes the first-time header 118 at 480; a returning visitor pays the row. |
| 7.3(a) | Orphaned `<p class="vh" id="lexhint">`: nothing references it. | Grep: one occurrence, its own definition. | **Conceded.** A leftover from a first pass that used `aria-describedby="lexhint"` on the terms; superseded when the gloss itself became the description, and not deleted. Delete it. |
| 7.3(b) | The held question is never announced: focus lands on `section#who`, whose name is the heading; `#held` has no role and no live region. | `role: null, aria-live: null` on `#held` after submit. | **Conceded.** The constitution's R.0 is "visible through every routing state"; for a screen-reader user it was visible through none. Fix: focus moves to the held block itself (`tabindex="-1"`, labelled by "Your question, held:" plus the question), so the first announcement is the question and the next Tab stop is "Edit it." A `role="status"` on a block toggled from `hidden` is unreliable across readers; moving focus is not. |
| 7.3(c) | Seven "record" links, two accessible names — 03's conceded defect, reproduced. | "Her record →" ×2, "His record →" ×5. | **Conceded.** Each carries a visually-hidden tradition name, the fix 03's defense applied and I applied only to the "Ask" links. |
| 7.3(d) | The lexicon comment describes a Tab path (`term → Full entry`) that `tabindex="-1"` forecloses. | True. | **Conceded.** The `-1` is deliberate (a hidden card must add no stop; Enter on the term is the keyboard path); the comment describes the earlier design. The comment changes, not the markup; §7's "'Full entry' opens it too" gains "by pointer or touch." |
| 4.2 | The mark autoplays the joining; the 04 defense said in writing this belongs on a stretch list; §8 does not have it. | Logo Usage Sheet lines 62–64: "the motion never replays unbidden and never plays the joining at a visitor." 04 defense lines 243–245: "belonged on the stretch list for Mark, and I did not put it there." | **Conceded without reservation.** I cited that defense eight times and dropped the one process finding it made against itself. Ruling 16 below. My substantive view is the same as 04's — the brand's own reference file autoplays the full sequence, the hero plays it once, "at a visitor" is undefined — and that view is exactly what a stretch list exists to submit rather than assume. |
| 4.3 | "World" appears twice on the tradition page, both verbatim from records; §9 flags one. The rule the hybrid adopted — provenance clears facts, not register — forbids both. | `pahc.limit.material-remains` ("a later world") flagged; `pahc.craft.chloe-voice` ("this world's own surviving voices"), in the first sidenote, not flagged. | **Conceded.** The rule is mine and I broke it. The rule's own remedy is a bracketed elision — "a later [tradition]" — with the record cited beside it, which is what the sidenote already does. Ruling 17. |
| 4.4 | The two `?mode=table` hrefs land on a disabled "Seat at least two voices" — the 05 review's measured, priced defect. | `Launch.tsx:36` `canConvene = seated.length >= 2 …`; `:133–134` renders the disabled label. Both hrefs are the live site's own: `index.html:228` sends the **primary** "Come and join us at the Table" button to `?mode=table`, and `:317` sends every per-Representative "Bring X to the Table" to `?worlds=<one id>&mode=table`. | **Conceded as a missing ruling.** Inherited verbatim is a defense of presence, not of the landing state. Ruling 18: on the tradition page, either copy that describes the state ("Chloe is seated there — choose at least one more voice") or a documented pairing seated with her; on the homepage, "Set your own table →" lands on the empty field, which is what its copy says. Either way this is a live-site defect too and should be filed as one. |
| 4.5 | "As it happened" over a re-rendered UI; the exchange sits on `--gold-wash`, the ground the constitution removed from the transcript; the capture's "Known limitation… Stay in this one tab" banner is dropped. | The capture was added 2026-08-25 (`74d9ffb1`). The banner string does not exist anywhere in `cic-poc/` today, nor in its git history; the current in-room note is *"Not saved to an account — this conversation lives in this tab"* (`Conversation.tsx:43–45`), first committed 2026-08-31 (`0e7c8138`), and sessions rehydrate on reload (`sessionStore.ts`, `App.tsx:64–79`). | **Conceded on the caption and the ground; corrected on the banner.** The caption gains a date ("captured 25 August 2026; re-set here in the app's decided long-form grammar") and the ground goes on the ruling list. The banner should *not* be transcribed — it is obsolete in the source — but the disclosure it stood for is real and belongs in "What is unfinished": *this conversation lives in this tab and is not saved to an account.* That is a more consequential sentence for Mark's person than "modes have not shipped," and the review is right that the block did not carry it. |
| 4.6 | A protected line used twice in one section; the distress line three times across two pages. | Lines 495 and 509 of the homepage, both inside `.before`. | **Conceded.** The "Witness" bullet loses its second use; the protected line stays once, in `.measure`. The margin note's paraphrase of the distress path is reworded so the line appears verbatim once per page. |
| 4.7 | "Nothing is sent ahead" versus `history.replaceState('?q=…')`; no `Referrer-Policy` in `_headers`. | `_headers`: no `Referrer-Policy`. | **Conceded, and it grows in §3.2** — where the question rides is the one new decision inside the `q` build item. |
| 3.3 | The first text on the page explains the logo. | True; it is the Logo Usage Sheet's caption rule discharged. | Acknowledged; folded into ruling 8 as an explicit choice rather than an inherited one. |
| 5.1 | The offered-questions list is the one recognisably period surface. | Fair. | Acknowledged. It is saved, as the review says, by the content; D3 should know it is the element most likely to date. |

---

## 2. Conceded — the parentage claims

The review checked roughly thirty rows of the §2 table and found the large majority hold.
The three it disputes I re-read at the cited lines, and it is right about all three.

**2.1 The antiquarian concession neither defense made.** 01 defense §4 (lines 244–286)
is split exactly as the review says: *contested* — Roman-numeral chapter heads, part-title
pages, drop caps, the keyed marginal column, a colophon; *conceded* — numbered plates, the
"issue" conceit, the closing spread's scale, and full-screen part-title pages "on
scanability grounds, not religious ones." 03 defense §2.1 (lines 121–126) concedes "Plate
I.", "Register" as an eyebrow, lower-roman counters and the sticky marginal column, and in
the same paragraph defends old-style figures, small caps and Roman-numeral part numbers as
"the trade-book register the constitution asks for." My row filed all eight devices as
conceded by both. Four were conceded by one or the other; four — Roman numerals, drop caps,
the colophon, small caps — were argued for by name by both. **Excluding them is this
hybrid's own call**, made under the constitution's "nothing antiquarian" and the two
*reviews'* readings, and it was filed as inherited. The review's word — misrepresentation
rather than slip — is fair, because the apparatus exists so that a reader can tell a
settled finding from a fresh call, and here it could not. The row is rewritten to say
what each defense conceded and that the rest is mine; and because both authors argued the
other way, it goes to Mark as ruling 19 rather than being settled by the synthesis.

**2.2 "Its exact rebuilt order."** 01 defense §5.1 (lines 311–316): provenance → "Where
we are quiet" → the essay in sections → the questions list → one door. Mine: provenance →
quiet → questions → voice → record → door. The essay and the questions are swapped, and
the essay is replaced. §3 item 2 argues the replacement well and does not mention the
swap; §3 lists four conflicts and there are five. Conceded; the fifth is added.

**2.3 The fear question that is not there.** The 01 defense's §1 table (row 6.3) names
the five "For the Wrestling" openers and says it "put the fear-question fifth"; its §5.1
promises "the fear-question first." I used three of the five and neither of the two that
reading could mean — the Ignatian "death wish" question or the "one chance at
forgiveness" question — is on the page. The list front-loads the personal, which is the
substance; the citation names a set and an order that are not there. Conceded. And "four
scholars and one person" is the 01 *defense's* paraphrase of its review's §6.3 heading
(defense line 54), not the review's words. Conceded.

**2.4 The smaller slips.** All re-checked: the 03 review's two sentences (lines 196, 199)
spliced into one quotation with "lifted" changed to "lift"; the 04 defense's "against
Mark's audience ruling" (line 216) dropped from inside a quotation without an ellipsis;
"one primary, six text-link secondaries" is in the 05 defense's §1 concession table (line
39), not its §3.2. Conceded, all three. The "01 defense §6.2" pointer I have not
re-verified and take on the review's word, since the other five held. Every quotation in
the rewritten table will be exact or marked as a paraphrase.

---

## 3. The most serious claim — the door does not open

The review's structural finding is that the question is held and then abandoned: submit
scrolls to a century-sorted picker, the picker opens a new tab, the tab carries no
question, and the first thing the visitor reads at the landing point is a scarcity
notice. Then the point underneath: the door cannot be finished on this site.

I verified the flow the review ran, and I add one number to it: after submit at 390×844
the viewport holds, in order, *Your question, held* · the question · *Edit it* · *Who's
at the table* · *Who would you like to ask?* · the scope line · **the pilot paragraph** ·
**the cost paragraph** · *The Early Church Era · 70–312 CE* · Chloe. The first "Ask
Chloe" is at 2,804px. The resolved href is
`?worlds=post-apostolic-house-church&mode=interview` — no `q` — in a new tab.

### 3.1 What I verified in the app, line by line

- `App.tsx:31–38` — `parseDeepLink()` reads `worlds` and `mode`. Nothing else. The README
  and the review agree.
- `App.tsx:42–44` — `consumeDeepLink()` replaces the URL with the bare path **before the
  room renders.** Any `q` would have to be read into state before this runs.
- `App.tsx:64–105` — the deep link fires only when nothing is stored for the tab;
  `beginInterview(linked[0])` starts the session with no text.
- `Conversation.tsx:112–117` — `<ChatInput onSend onEnd disabled placeholder />`. No
  initial value.
- `ChatInput.tsx:22–23` — `useState('')`. No prop by which a value could arrive.
- `sessionStore.ts:6–9` — storage is **`sessionStorage`**, per tab, by stated design:
  "survive a reload of the same tab, not follow the participant to a new tab."
- The engine's message contract (`MessageRequest {text, client_msg_id}`, per
  `ChatInput.tsx:8–9`) sees the text only when the participant presses Send.
- The design decision is already made: constitution line 188 (state G.3) and Storyboard
  lines 387–388 — *"the prepared question arrives at S4 pre-filled in the input —
  editable, deletable, never auto-sent."* What is unbuilt is the *build*, not the design.

### 3.2 The honest answer: not fixable on the marketing site alone

**The review is right.** Until the app reads a question parameter and places it in the
composer, nothing this homepage does can put the visitor's own words in front of them at
the moment they need them. The site can hold the question, restore it from the URL,
shorten the distance to the hand-off, and describe the gap truthfully. It cannot close it.
I will not claim a copy or layout change does what only `ChatInput` can do.

**The shape of the app change, exactly.** The review prices it at one line in
`parseDeepLink`. It is small, but it is not one line, and Mark should see the true size:

1. `App.tsx` — read the parameter in `parseDeepLink()`, hold it in state, and do so
   *before* `consumeDeepLink()` strips the URL (lines 42–44, 90, 95, 100).
2. `Conversation.tsx` — pass it down as a prop.
3. `ChatInput.tsx` — accept an `initialMessage` prop into `useState`; never auto-send
   (the Storyboard's rule); the participant presses Send.
4. The Table path (`TableRoom.tsx:142–155`) if a question should also travel to a Table —
   or not, which is itself a decision.
5. A test, and a deploy on Render — the app is a separate deploy from the site.

Roughly fifteen lines across three or four files, no backend change, design already
approved. **It is a D4 build item and it is its own decision for Mark, separate from
whether this direction is good** — because a direction can be right about where the door
goes and still not be the party that can build the room behind it.

**The one genuinely new decision hidden inside it — where the question rides.** This is
the review's §4.7 privacy nit grown to its real size. If the question travels in the
query string (`?q=…`), it is sent to the app's host with the page request and lands in
that host's access logs; "nothing is sent ahead" becomes false and must be rewritten. If
it travels in the **fragment** (`#q=…`), it is never sent in any HTTP request — fragments
stay in the browser — and the app reads `location.hash`; the site's sentence can then say,
exactly, "your question is sent to no one until you press Send in the room." I recommend
the fragment. It is Mark's ruling because it touches what the site promises, and it should
be made before the fifteen lines are written, not after. Ruling 14.

**What the site can do alone, and I would.** Two things, neither of which is the door:

- **Same-tab hand-off on the question path.** Every app link on both pages opens a new
  tab. The reason a new tab ever seemed necessary — the capture's "refreshing will lose
  your conversation" banner — is gone from the source (§1, row 4.5): sessions live in
  `sessionStorage` and rehydrate on reload, so Back returns to the site and Forward
  resumes the room, and the site's own `?q=` restore (verified in the README's §7) puts
  the held question back on screen. Same-tab makes "remember it, cold, in a new tab"
  into "press Back." Verified in the shipped frontend source; the deployed engine is
  unverified, the same caveat the Table carries (ruling 11). Ruling 15.
- **Say the gap in the place it opens.** The "how" line says nothing is sent ahead; it
  does not say the visitor will type the question again. One clause, beside the input:
  "you'll type it again in the room — for now." That copy is temporary and is deleted the
  day `q` lands.

### 3.3 The offered questions — the trade I made and did not file

The 05 defense's design (line 325): "Five P-cell canon questions, each a real
`?worlds=…&mode=interview` link." I took the questions and replaced the per-question
link with `?q=…#who` — the same-page hold. The review says this is materially weaker
than the parent and presented as its execution. Both halves are fair.

Why I did it: a P-cell canon question is one *every* voice is prepared to meet — that is
what the P cell is. A per-question deep link therefore chooses a tradition on the
visitor's behalf, and the basis for the choice is the author's, undisclosed. The
constitution's S0 says "no default," and the Tier-3 router that would make the choice on
evidence is unbuilt. I chose no default and paid for it with the list. The review
anticipates exactly this argument and answers it correctly: it is a legitimate ruling,
and it belongs in §8 as one, not in §5 as a sacrifice. Conceded on process. On substance
the options are three, and I put them to Mark as **ruling 13**:

- **(A) No default** — hold the question, hand the visitor the seven. What is built.
- **(B) One real link per offered question, with the choice disclosed as a citation, not
  hidden as a route.** The tradition page already does this for Chloe ("Under each, where
  her record can answer from": Hermas *Mandate* 9 for doubt and for prayer; *1 Clement* for
  the failed leaders; Pliny for the women). Four of the six homepage questions have a
  named source in Chloe's record; two — suffering, and "I want to believe in Jesus, but I
  can't" — have no source mapping in any record yet and could not honestly be routed
  until they do. Each link would read "e.g. ask Chloe — Hermas, *Mandate* 9 · or choose
  another voice." This is the 05 defense's design with the author's hand shown.
- **(C) A pilot default voice**, chosen by Mark, for every question until the router
  exists.

Under any of the three, the door opens only when `q` travels. (B) shortens the path
most and costs the least honesty, and it is content work before it is design work.

### 3.4 The scarcity notice in the door's landing zone — and a correction of my own

The review's §6 walk is accurate; I measured the same nodes. The two live paragraphs sit
in the viewport a visitor lands in after typing something they may never have said aloud,
and the Brand Guidelines' Never list (lines 66–67) names "urgency or scarcity." The copy
is inherited; the flow that lands on it is new; the harm is new. Conceded.

Then a correction the review did not make, because it accepted my README's account. §2
says the pilot sentence is kept "above the chairs, **where the live site has it**." It is
not. `cic-website/index.html:163–174`: the carousel is line 169; the pilot note and the
cost caveat are lines 172–173, **below it**, above the two buttons. "Above the rows" was
the 05 defense's own choice (its line 331), not the live site's, and I attributed the
placement to the wrong source. So the review's fix — move the paragraph below the seven —
is not only right; it restores the live site's own order. Conceded twice: the placement,
and the citation.

And one thing beyond placement, for Mark: the Never list bans the *register*, not the
location. Moving the paragraph takes it out of the confession's landing zone; it does not
make "a limited number of participants… about five conversations" not a scarcity notice.
Whether that copy belongs on the homepage at all, in any position, is a ruling the live
site has never had put to it, and I add it as ruling 20 rather than settle it by moving
the paragraph and calling the matter closed.

---

## 4. Contested — where the review overstates, with the evidence

Four places. One matters for the verdict; the other three are corrections of degree.

**4.1 The 2,627px comparison is real but not like-for-like.** 05's 2,487px was the
distance a visitor had to *scroll* to reach the first door on a page with no question
door. Here the six question links are at 1,212px (1,022 under the fold fix, §5.1), and
they are doors into the hold state; and once the visitor uses the door, the page scrolls
for them — the landing point is 1,845 and "Ask Chloe" is 959px below it, one screen.
The number is true and the fix in §5.1 lowers it by roughly 400px, but "further than the
distance that convicted 05" compares a scroll-to-first-door with a landing-to-second-door
and the visitor does not experience the second as a 2,627px scroll. Where the review is
right underneath the number: the second door is still a seven-way choice among strangers,
and §3.3 is the only honest answer to that.

**4.2 "05's IA survives intact" is half right.** The row grammar — portrait, name, role,
tradition, dates, region, tile — is the census's own record of each tradition, and the
list-not-carousel form is the 04 defense's and the 04 review's ("materially better than
the live carousel for scanning, keyboard use and screen readers"), not 05's. What
survives from 05 is not the rows but the *ordering*: chronology as the answer to a
question. On that the review is right, and §3.3 is the answer: until a router or a
disclosed per-question citation exists, chronology is the only ordering that does not
pretend to know something it does not. The review's own §3.1 concedes the constraint; I
concede that "ordered the way the person Mark named needs it" (README §4) claimed more
than the picker can deliver and rewrite it.

**4.3 The "Known limitation" banner should not be added — it is gone.** §1 row 4.5: the
string exists nowhere in `cic-poc/` or its history; the capture (2026-08-25) predates the
in-room note that replaced it (2026-08-31); sessions now survive a reload. The review was
careful to say it could not assert the banner still ships, and it does not. The right
disclosure is the current one — "lives in this tab, not saved to an account" — and I add
that one, not the obsolete one. The consequence the review did not draw: with the banner
gone, `target="_blank"` on the question path is no longer a safety measure, and same-tab
hand-off (§3.2) becomes the better move.

**4.4 "One line in `parseDeepLink`" understates the app change.** §3.2 gives the true
size. This cuts against me, not for me — a smaller estimate would have made the
dependency look lighter than it is — but the verdict's last paragraph rests on it and Mark
should authorise the real thing.

---

## 5. What changes — concretely, measured where it can be

### 5.1 The fold — the reviewer's condition 1, tested

The review's budget sentence is right: "the hero is 620px of centred display type; that
is the budget to spend." I built two candidates as scratchpad copies (nothing in the
sandbox directory was touched) and measured both at the same widths, with and without the
53px sandbox note that does not ship.

**Candidate A — conservative.** Drop the door's eyebrow ("The way in"); move the "how"
line below the input; tighten hero and door padding on phones. DOM order otherwise
unchanged.

| Viewport | input top–bottom (note kept) | (note stripped) | in screen one? |
|---|---|---|---|
| 390×844 | 733–781 | 679–727 | yes / yes |
| 390×740 | 733–781 | 679–727 | no / **yes** |
| 390×660 | 733–781 | 679–727 | **no / no** |
| 320×844 | 895–943 | 820–868 | no / no |

Clears the common phone and the real iOS Safari height; fails the 660 Android height and
320. Not enough.

**Candidate B — the input directly under the H1.** Order becomes: mark with its sentence
→ H1 → "Start with your question" (H2) with the input and button → the lede → the "how"
line → the AI line → the six offered questions. The lede is cut to the clause the review
called the best ten seconds of the workstream — *"Whether you come curious, with a sermon
to write, or with a question about faith you've carried for years — there is a chair"* —
and its first sentence (the seven, from their own records) moves to the `#who` scope line,
which already says it.

| Viewport | input top–bottom (note kept) | (note stripped) | input in screen one? | lede in screen one? | first offered question |
|---|---|---|---|---|---|
| 390×844 | 494–542 | 441–489 | yes / yes | yes / yes | 1,075 / 1,022 |
| 390×740 | 494–542 | 441–489 | yes / yes | yes / yes | |
| 390×660 | 494–542 | 441–489 | **yes / yes** | no / **yes** (bottom 647) | |
| 320×844 | 568–616 | 493–541 | yes / yes | yes / yes | |
| 1440×790 | 478–526 | 446–494 | yes / yes | yes / yes | 850 / 818 |

Zero horizontal overflow at every width; the held-question flow works unchanged; the
outline stays H1 → H2. **On every phone the review named, the input is in the first
screen with the sandbox note in place, and the lede that names Mark's person is in the
first screen on every shipping viewport.** The AI line lands at 824 (390, stripped) —
the second screen, the same position relative to the input it has now. This is the change
I would make, and it is the one the direction's own first sentence described and its
markup did not build.

### 5.2 The landing zone — condition 3

The pilot and cost paragraphs move below the seven, where the live site has them
(§3.4). The `#who` section's first content after the held question becomes the heading
and the scope line, then Chloe.

### 5.3 The measured defects and the overstated claims — condition 4

All of §1, as listed there: the `&nbsp;`; the gated side door (which also answers
1.5(b), 7.1 and 7.2 in one change); `#lexhint` deleted; focus to the held block; seven
record links named; the lexicon comment corrected; the census-dash seam; the dark-tint
sentence; the 44px sentence; the "at the fold" sentence; the no-JS sentence; the caption
dated and the ground filed; the protected line once; the distress line once per page; the
in-tab disclosure added to "What is unfinished"; the parentage rows rewritten (§2).

### 5.4 The rulings that were missing — condition 5, and the ones this defense found

Added to §8, continuing its numbering:

13. **The offered questions**: no default and a list (built) · one disclosed citation-link
    per question where a record has a source (four of six today) · a pilot default voice.
14. **Where the held question rides to the app**: query string (logged by the host;
    "nothing is sent ahead" rewritten) or fragment (never sent to a server; the sentence
    made exact). Decide before the build item, not after.
15. **Same-tab hand-off on the question path**, so Back returns to the held question —
    safe in the shipped frontend source; deployed engine unverified.
16. **The mark's joining plays on arrival** — the 04 defense's stretch item, restored.
17. **The two "world" record quotes** — bracketed elision with the record cited, or
    paraphrase-and-cite, or hold the quote until `task_9222cdbc` lands.
18. **The Table hrefs** — the tradition page's single-seat `?worlds=X&mode=table`
    (the live site's own per-Representative link) lands on a disabled button: honest
    landing-state copy, or a documented pairing seated with her. The homepage's `?mode=table`
    matches the live site's primary button and lands where its copy says.
19. **The four antiquarian devices both defenses argued for** — Roman numerals, drop caps,
    a colophon, small caps — excluded here on the hybrid's own reading of "nothing
    antiquarian," not on a concession. Mark's call, not the synthesis's.
20. **The pilot/cost copy itself** — a scarcity register the Never list names, on the
    homepage in any position.

And ruling 8 extended: the mark's sentence is the first text on the page because the
Logo Usage Sheet's caption rule puts it there; that is a choice, made in the open.

### 5.5 What this defense does not claim

It does not claim the door opens. Under every change above, the visitor's question
reaches the room only when `ChatInput` can receive it, and that is not this site's code.
It does not claim the picker stops being a chronology; it claims chronology is the
only honest order until ruling 13 is made. It does not claim the tradition page is the
right length; that is D3's, as the README said. And it does not claim the parentage table
was accurate; it was accurate in the large majority of rows and wrong in the rows the
review named, and the wrong ones are the kind the apparatus exists to prevent.

---

## 6. The verdict, answered

The review's one line: *the hybrid is the first direction to understand what the phase
found, and it built the room the door belongs in before it built the door.* I accept the
sentence as the fairest description of the artifact I could have been given.

What I would ask the reviewer to weigh against "conditionally":

- Conditions 1, 3, 4 and 5 are met by changes measured or listed above, none of which
  touches the direction's structure — the fold fix is the direction's own first sentence
  finally built, with the input at 441px on the phone that had it at 897.
- Condition 2 is a ruling for Mark (13), and the review said so itself. It cannot be
  met by the author, only put to him properly, and it now is.
- The dependency the verdict closes on — `q` — is real, is not the site's to build, is
  larger than one line, and carries one decision (14) that should be made first. This
  direction stands or falls on its structure, which the review found sound; it does not
  stand or fall on whether Mark authorises fifteen lines in a different deploy. The two
  should be decided as two.

If the reviewer holds that a direction whose door depends on another system's build
cannot lose the conditional until that build lands, then the conditional stays and the
direction should go to D3 carrying it in plain sight — which is what §5 of the README
tried to do and §8 should have done. If the conditional was about the things the site
itself can fix, the list above is what would need to be true, and each item is
checkable.

*— Fable, D2 struggle phase. One defense, as the charter allows. Every number above was
measured on my own render after reading the review; every citation was opened at the
line. Nothing outside this file was changed.*
