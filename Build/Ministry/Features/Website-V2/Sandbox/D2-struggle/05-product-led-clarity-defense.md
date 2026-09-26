# D2 defense — Direction 05, Product-Led Feature Clarity

**Sandbox artifact. The author's one defense, per the charter. Not a ruling. 2026-09-02.**

I wrote `05-product-led-clarity/` (README, `homepage.html`, `meet-chloe.html`). I read
the review in full, then re-ran its measurements myself before answering any of them:
the contrast pairs by computation from the token values, and the navigation, focus
order, and scroll positions in Chromium (`/opt/pw-browsers/chromium-1194`, Playwright
1.56) at 320/390/414 × 844. Where my numbers match the reviewer's I say "reproduced";
where they don't I show mine. I opened no other direction's folder and no other review.
I did open the app code, the engine, the brand guidelines, the constitution, the fleet
canon, and the live site — all governing files my brief pointed me to — because several
of the reviewer's claims and several of my own turn on what is actually there.

The short version, so nobody has to hunt for it: **the reviewer's measured findings are
correct and I concede every one of them. Three of the reviewer's framings are wrong or
overstated and I show why. The structural charge about the SaaS skeleton narrows, on the
reviewer's own accounting, to two removable elements and is not fatal. The structural
charge about Mark's heart audience is the one that lands, and I concede it — with one
disagreement about what fixing it leaves behind, which is the thing I am actually asking
Mark to weigh.**

---

## 1. Conceded — verified against my own files

I am not going to argue with numbers I can reproduce. Each row is what I checked, and
what I found.

| Reviewer's claim | What I verified | Concession |
|---|---|---|
| Dark-mode primary button 2.69:1 | Reproduced exactly: dark redefines `--vellum` to `#1E1913` (both files, line 33) and never `--madder` or `--madder-deep`. Text on fill = 2.69:1. Hover = **1.92:1** by my computation (reviewer reasoned ~1.6; both fail). | **Full.** The README's dark table lists only the text tokens I had redefined. I checked what I touched, not the component I hadn't. That is the exact failure the D0 note warned about, and my README answered the warning with "designed to from the start." One token — button text to `#FEFCF8` — gives 6.33:1 in both registers. |
| "AI" absent from `meet-chloe.html` | Grep: zero occurrences in the file. On the homepage the word appears once in body copy (`homepage.html:438`), at **5,768px** on a 390-wide phone (reproduced exactly). Brand Guidelines line 78: *"Raise the AI trust question yourself, first."* | **Full.** The page whose only job is an informed decision does not say what the visitor is deciding about. For the record, not as excuse: the live `index.html` says "AI" nowhere; only `about.html:92` does. My homepage raised it and stopped short. The inner page is the worse failure. |
| Nav truncated on every phone | Reproduced exactly: visible rail 45 / 115 / 139px vs. 386px of links at 320 / 390 / 414. `.brand{flex-shrink:0}` gives the nav the whole squeeze; both scrollbar-hiding rules are set. | **Substance conceded** — no affordance means broken in practice. One sub-claim is wrong; see §2A. |
| Graphite as prose, 3.36:1 | Reproduced: `#8A837C` on `--gold-wash` 3.36:1, on parchment 3.38:1, on vellum 3.65:1. (Dark register: `#A39B92` on `#241D15` is 6.07:1 — a light-mode-only failure.) | **Full.** My contrast table omitted graphite; I did not check it. I was not one of the three directions that found it. `.fac` and `.foot` in `--ink-faded` would be 5.37:1 on the wash. Graphite goes back to being a hairline pigment, not a text one. |
| Deep-link grammar under-read | `App.tsx:13–30` documents `?worlds=a,b[,c]&mode=table` in a comment block at the top of the same file I cited elsewhere. `Launch.tsx:36`: `canConvene = seated.length >= 2`; line 134 renders "Seat at least two voices" disabled. | **Full, and plainly.** My ledger item 6 said "unconfirmed." It was confirmed seventeen lines from the top of the file I was reading. The two showcase pairings are inert `<div>`s; the Table button lands on an empty field with a disabled button; "Add Chloe to a Table" seats one voice and shows the visitor a label telling them they did it wrong. On the direction that exists to remove steps, I shipped a zero-click path where a one-click path was documented. The fix is the direction's thesis: `?worlds=alexandria-catechetical,desert-monasticism&mode=table` makes "the school and the desert" a real invitation. |
| "world" leak | `homepage.html:414`, verbatim from `Launch.tsx:100`. The Decision-Log's D0 entry records the corpus-wide "tradition, not world" rule as live on every page. | **Full**, and the reviewer's diagnosis is right: my ledger's test was "did I type this," not "is this cleared for this surface." Same failure for the pairings — `pairings.ts:4–5` says *"DRAFT status: that document awaits Mark's sign-off"* and I filed "the proven pairing" as real. The rule I should have had: **a quote's provenance clears its facts, not its register.** Every string lifted from app code gets re-filed as draft-for-this-surface. |
| The composer | `homepage.html:271`: two `<span>`s, `aria-hidden`, a drawn box and a filled "Send." | **Full, and it is worse than the reviewer said.** I compared it to the real capture. The shipped placeholder is *"Share your thoughts or ask a question…"* Mine says *"Ask Chloe anything…"* — invented copy, not marked draft, on the one element I built by hand, on the direction whose sentence is "the real interface, not a description of it." Delete both spans. The leaf itself becomes the link into the room, so a visitor who taps where the composer was gets the real one. |
| Seven filled primaries | Counted: nine `.btn.primary` on the page (hero, seven rows, give), plus the drawn Send. `#meet` carries fifteen actions. | **Full.** "One primary action per screen" is my own sentence, broken by my own biggest section. The constitution's "features wait to be chosen / compete for attention" test applies once I borrow its register, and seven identical madder buttons compete. One primary, six text-link secondaries — the grammar `meet-chloe.html` already uses for "Meet the others," which the reviewer did not attack. |
| Headings, `aria-label`, hidden marginalia | Confirmed by reading: seven `.label` eyebrows are `<p>`; era bands are `<div>`; `aria-label` sits on `div.leaf`, `span.cite`, `div.foot-bar`; `homepage.html:282` hides the only subject of its sentence. `meet-chloe.html:288` gets it right, which proves the homepage one is an oversight. | **Full.** Labels become `<h2>`/`<h3>`; the leaf's name moves to `<figure aria-labelledby>`; the glyph gets visible text. |
| Two marks in the first viewport | Header `.mark.play` and hero `.mark.still`, 88px apart. Brand Guidelines line 99: the public sentence is *"said once beside the mark at first contact."* | **Conceded** as reading like a rendering bug. One mark, in the hero, sentence beside it. |
| Pilot note mid-funnel | `homepage.html:407`, after seven invitations, before the Table. Live copy, verbatim. | **Conceded** on placement. Above the rows, where the live site has it. |
| Six "About" pages unbuilt | Ledger item 8 says so. | **True**, and the reviewer's inference is fair: the two-step path is demonstrated once, on the page missing the AI line. |

Twelve rows. None of them re-litigated. The reviewer said the first four are a day's
work; with the deep-link and ledger corrections it is closer to two. All of them are
fixes to execution, and I am not asking for credit for defects I can fix.

---

## 2. Contested — with the measurements

Three framings in the review are wrong or overstated. I raise them because the record
should be accurate, not because any of them changes the verdict on its own.

### 2A. "Not keyboard-operable — a WCAG 2.1.1 failure." Wrong.

Measured in Chromium, both files, all three widths: pressing Tab from the top reaches
every one of the four nav links (`activeElement` inside `nav.site-nav` for each), and
focusing a link scrolls the rail to it — `scrollLeft` 317 / 271 / 161 at 320 / 390 /
414. At 390px "Get Involved" ends fully inside the visible rail. 2.1.1 is satisfied
because the overflow region contains focusable children; `tabindex` on the scroller
is only needed when it doesn't. A horizontal swipe also works — programmatic
`scrollLeft` reaches 341 / 271 / 247.

What is true, and what I conceded above: at 320px a 95px link cannot fit a 45px window,
so it is reached-but-clipped; and there is no visual affordance, so a pointer visitor
will not discover the swipe. "Unreachable on every phone" overstates this. The defect
is discoverability, not operability, and the fix differs — a wrapping nav, not a
`tabindex`. I want that on the record because the wrong citation would produce the
wrong fix.

### 2B. "Three full screens of work before the first actionable thing appears." Wrong.

Measured at 390 × 844: the hero's primary button, *"Come and join us at the Table,"*
sits at **566px** — inside the first screen — and it is an anchor to `#meet`. The first
actionable thing is on screen one, and it jumps the visitor past the 2,000px the
reviewer's table counts. The reviewer's scroll numbers are real (I reproduced 2,487px
and 5,768px exactly); the framing omits the one control designed to make them moot.

What is true in the charge: after the jump, the first Begin is about 450px below the
section heading, so the honest step count from the top of the phone page is **two
clicks and half a screen, not one.** The README should have said "one click from any
row; two from the top of the page." That is a correction to the step map, not a
refutation of it — and the reviewer is right that the map counted the flattering unit.

### 2C. "You do not get to cite half a sentence." Half right.

The "features wait to be chosen" test is the constitution's preamble (line 25); the
"beautifully set trade book on parchment" sentence is §1 (line 50). They are not the
same paragraph. But the jab lands on §1 itself: the sentence I borrowed the register
from continues *"— warm, unhurried, nothing antiquarian, nothing tech-forward,"* and I
owe the whole sentence. The reviewer's substantive point — that opting into the
register opts me into the test — I accept. Under that test the seven-primary stack
fails, which is why it is conceded in §1.

### 2D. Two smaller corrections

- "Technology but not seen — experience first, governance second, mechanism third"
  (Brand Guidelines line 36) is *partially* inverted, not fully. Two of the three
  hero marginalia are governance stated in place, not mechanism: *"every answer ends
  with the letters and records it was built from — open them, check them"* is the
  brand's "shows its work"; *"Where it's thin"* is a protected governance line. Only
  "a dotted term opens a gloss" is mechanism. What the hero is missing is the AI
  sentence specifically. Conceded as to the sentence; contested as to the ordering.
- The "twelve failing nodes in dark" include seven `.vh` strings — clipped to 1×1px,
  never painted. Contrast does not apply to text that is not rendered. Five real
  failing nodes on the homepage, two on the inner page. The verdict is unchanged; the
  count is not.

---

## 3. The two structural charges, answered directly

### 3.1 "The skeleton is Stripe/Linear, and your own thesis convicts you" — not fatal, and here is the evidence

The reviewer's syllogism is: clarity is structure, not style; therefore SaaS DNA is
also structural; therefore restyling the structure launders nothing; and "if they are
separable, then the structure is the borrowed part."

The last clause is true, and I said it first. README, philosophy paragraph: *"it keeps
the grammar of a clear product site and sets all of it in CiC's own register."* README,
"What I kept because it is structure, not style," names the five borrowed structures
by name. The refusal table sits under the heading "The tech-forward tension" and is a
table of style refusals **because the rule it answers is a style rule** — "nothing
tech-forward" (constitution §1) governs how the thing looks and feels, and the brand's
never-list is vocabulary and posture. The thesis was never "we avoided product-site
structure." It was "product structure is where the clarity lives; tech-forward lives
in the styling; keep one, refuse the other." The reviewer calls this self-defeating.
It is only self-defeating if borrowed structure itself reads as tech-forward.

Does it? The reviewer's own accounting answers: three of the eight skeleton rows are
*"close to universal and I would not call them fashion"*; the numbered block is
*"genuinely the live site's own"*; the interface layer is *"the cleanest of the
registers I can imagine for this project"*; and the two elements that *"genuinely
date"* are **the composer and the seven-CTA list.** Both are conceded in §1 and both
are deletions, not redesigns.

What remains after those two deletions: a hero with a real transcript, a ruled picker
with one primary, a numbered trust block the live site already uses, a map entry, a
what's-next list, a give block. The reviewer's table calls that skeleton "complete, in
order, with nothing missing," and in the next section calls most of its rows universal.
Both cannot be the kill. A page that answers *what is this, what can I do, how* in that
order is not a period style. A chat composer is. So the structural charge narrows, on
the reviewer's own evidence, to two removable elements.

Where I concede structurally — and this is the real inheritance from the genre, more
than any section rhythm: **the ordering.** The skeleton shows the catalogue before the
governance and offers no door to the visitor who does not have a tradition preference.
"Show the SKUs first" is a product-site reflex, and it is fixed by reordering, not by
abandoning the grammar. Which is §3.2.

### 3.2 "The IA is a scholar's finding aid; no question-shaped door" — this one lands

I verified the charge against my own files and against the material I had.

**The vocabulary count reproduces.** Zero doubt / struggling / searching. One
"re-examining," inside the inherited pilot note. One "distress," the fourth of four
margin notes, on page two, in faded ink.

**The chronological IA is as described.** Era bands with century ranges, seven rows
sorted by start date carrying dates and regions, a ten-era ruled table with Roman
numerals.

**I had the material and did not use it.** The fleet canon
(`records/_fleet/canon_question/`) holds 93 questions; 23 are P-cell — the personal
cell. Among them:

- *"I grew up being told doubt was sin. Was there room among your people for doubt?"*
- *"What did you do when you couldn't believe what your own church taught?"*
- *"I want to believe in Jesus, but I can't. What would you say to me?"*
- *"Would Jesus have wanted anything to do with someone like me?"*
- *"I pray and nothing happens. Did your people know that silence?"*
- *"The people who taught me the faith turned out to be hypocrites. Did that happen…"*
- *"Did any of you ever want to leave?"*
- *"How do I forgive someone who isn't sorry?"*

The word "doubt" exists in the corpus, twice in one question. I put zero P-cell
questions on the homepage and one on the inner page, third of seven sections.

**And the app itself does better than my page for it.** `Conversation.tsx:13–17`
shows every arriving visitor three starters spanning the -I, -P, -E cells — one
personal question in the first screen of the room, by design: *"a nervous participant
benefits more from seeing the range of what's askable than from an arbitrary sample."*
`builders.py:845–855` compiles those starters from the same fleet canon records. So the
shipped room greets a visitor with a personal question, and the homepage I built to
show that room greets them with seven date ranges. On a direction whose discipline is
"show the real interface," I showed the room's transcript and hid the room's door.

**The constitution already specifies the door.** S0, lines 373–377 — beneath the same
hook line and the same CTA register I used — *"Doors (equal size, equal weight, no
default): **Start with your question** · Build your own table · Guided onboarding."*
S3: *"question door: one input + three theme chips."* Line 639 lists it as *"Later, own
gates: question-first door + proposal card."* It is not built: `parseDeepLink`
(`App.tsx:31–38`) reads only `worlds` and `mode` — there is no `?q=` — and
`ChatInput.tsx:2–6` records the guided-starters sheet as dropped, DRAFT. So the thing
the reviewer says *"a product-led direction should have been best positioned to
find"* was in the governing document as a decided door, and I organized the homepage
around the second door only.

**Why I didn't — the honest reason, not a defense.** The discipline "show only what's
built" made me read the question-first flow as un-showable, because the typed-question
→ proposed-Table routing is unbuilt. That is correct about the *typed* door. It is
wrong about the *offered* door: real canon questions, each a real deep link into a real
interview, is buildable today with zero fake controls — the very standard I failed with
the composer. I applied the honesty rule at the wrong grain, and the cost was the one
visitor Mark named.

**On "transactional":** conceded in mechanism, exactly as the reviewer describes it.
It is not the fonts; it is the repetition — seven identical rows, seven identical
filled buttons, is a checkout. The census lines inside those rows are not transactional
(*"communities who left settled village life to wage a lifelong combat against the
thoughts that trouble a person from within"*); they would carry the warmth if the
button stopped shouting over them.

**On "no default":** the reviewer faults the picker for no default, no "start here."
The constitution's S0 says "no default" for its doors, and I would hold to that. The
fix is a question door of equal weight, not a recommended Representative.

**Where I disagree with the reviewer — the one thing I am asking Mark to weigh.** The
review says: do all of this *"and what remains is no longer Product-Led Feature Clarity
— it is an editorial or a threshold direction that kept this one's measurement
discipline."* I think that is wrong, and it matters for what survives.

A homepage whose first section is *"Bring the question you have"* — five real P-cell
questions, each a real deep link — above a picker for the visitor who already knows
whom they want, is this direction's method applied to Mark's heart visitor instead of
the returning one. Its three questions (*what is this, what can I do right now, how*)
are answered for that visitor faster than for anyone else on the page: one tap on the
question that is theirs. The step map for the person in difficulty goes from "scroll
2,487px, choose among seven centuries" to one click. That is not editorial. It is not a
threshold. It is **more** product-led, not less — because "feature access" for this
product was never "pick a tradition"; it was "ask your question," and the constitution
had already said so. What dies is not the method or the grammar. It is the assumption
that the first question a visitor answers is *which* rather than *what's on your mind.*

### 3.3 The hero excerpt — concede the choice, contest the principle

**Contest the principle.** Mark's ruling, as the Decision-Log records it, is about form:
*"not devotional, liturgical, or churchy, whatever the words say,"* and *"even though we
are religious."* The excerpt is a historical voice describing her community's week. It
addresses no one, asks nothing of the visitor, ends with a question back to them, and
is set inside a transcript frame that announces it as one voice among seven. It is not
the site speaking. The product *is* seven such voices; a visitor who sits with any of
them will hear about the meal within a few exchanges, and a homepage that hides that is
previewing a different product. The reviewer conceded the interface layer is the
cleanest available. The charge is about content, and the content will be religious.

**Concede the choice, and it is a worse choice than the reviewer knew.** Two shipped
captures exist in `cic-website/assets/tour-captures/`. I used one. The other,
`theon-confidence.png`, is Theon answering *"What's the actual evidence for how
confident we can be about that practice? How sure are you, really?"* — and answering
it: *"Where the pattern is concerned, our confidence is real. Where a particular soul's
road through it is concerned, we have the outline and not the portrait — and we would
rather tell you that plainly than paint a face onto it that was never there."* A
skeptic's question, answered by the thing showing its work and naming its limit — the
brand's whole "Always" paragraph in one exchange, with a ✲ 3 at the end. It was in the
same folder. I chose the tour of a Sunday because "ordinary, mostly" disarms; I should
have chosen the one where the voice is pressed and doesn't flinch.

The reviewer's suggested canon question (*"I'm far from everyone I love…"*) would be
better still — if a real capture answered it. None does, and a marketing page must not
fabricate an exchange. The honest hero today is Theon's. And the reviewer's deeper point
stands regardless: a deconstructing visitor might have left over exactly that liturgy —
not because it is religious, but because it came *first.* A first exchange should be
the visitor's kind of question.

**On the portraits as "a gallery of saints":** I'd push back lightly. Seven painterly
faces on parchment, each with a name and a job title, in a ruled list, reads as a cast
list. But the reviewer flagged it as secondary and inherited, and I'll leave it there.

---

## 4. What I am asking to survive, and what dies

**Dies, and I am not defending it:** the hero as built (composer, liturgy-first
excerpt, duplicate mark); the tradition-first ordering; the seven-primary picker; the
step map's accounting; the ledger's "verbatim = cleared" rule; the whole-site
direction in its D1 shape.

**Survives, with evidence:**

1. **The method.** Refusal table, honesty ledger (with the register rule added),
   deep-link verification, per-surface contrast math, the accessibility stance. The
   reviewer granted this; I will not argue it further.

2. **The inner page's anatomy** — `meet-chloe.html` as a shape: one decision block,
   one button; the registry's doorway paragraph; the thinness box; three canon
   questions; one real exchange with marginalia; sources in two columns; the "name is
   ours" line; six other chairs. The reviewer attacked its defects (no AI line,
   graphite prose, heading tree, the one-seat Table link, the dead-end nav) and every
   one is a one-line fix. The reviewer did not attack its shape — and called its two
   central blocks *"the single richest piece of storytelling anywhere in this
   direction"* and *"the load-bearing trust content on the page."* This page should be
   the template for all seven, whichever homepage Mark picks.

3. **The homepage below the hero, reordered.** Question door → picker (one primary) →
   the AI sentence *inside the leaf's running head*, so no door is passed without it,
   with the three-things block kept as the fuller statement → Table, wired → map →
   next → give. That is the reviewer's own withdrawal list, item for item, plus the
   ordering.

4. **Three corrections to the shared record** the reviewer put there and I confirm:
   seam D is partly stale (Table live; Living Table / role selector / guided onboarding
   not); the deployed engine at `cic-engine.onrender.com` needs a live check before any
   `?mode=table` link ships; and the fleet canon's `canon_status` enum is
   `seed | vetted | retired` (`schemas.py:320`) with every fleet question at `seed` —
   already served publicly in-room by `builders.py`, so no new exposure, but Mark
   should know the status before those questions go on a marketing page.

**Needs Mark, not me:** whether an offered-question door built from `seed`-status canon
questions is cleared for the public surface; and whether P-cell questions on a homepage
brush the brand's "never" on *"finding the right answers"* — they are questions, not
promises, but he should rule on it rather than have me decide.

---

## 5. The reviewer's withdrawal list, taken

All seven, plus three the reviewer did not ask for:

| Reviewer asked | Answer |
|---|---|
| Replace the hero excerpt with a question-led opening | Theon's confidence exchange — real, shipped, a skeptic's question. |
| Add a question-first door above the picker | Five P-cell canon questions, each a real `?worlds=…&mode=interview` link; constitution S0's own door, offered rather than typed. |
| AI disclosure above the first Begin, and on `meet-chloe.html` | In the leaf's running head on both pages; the three-things block stays as the fuller statement. |
| Delete the composer, keep the leaf | Deleted; the leaf becomes the link. |
| Dark tokens, graphite, headings, `aria-label`s, marginalia, nav | All as §1. |
| Wire the pairings | `?worlds=a,b&mode=table` per `App.tsx:21–23`. |
| Re-file app-quoted copy as draft; fix "world" | Done, with the rule: provenance clears facts, not register. |
| *(not asked)* | One primary per screen, restored. Pilot note above the rows. One mark. The step map restated in clicks *and* screens. |

---

## 6. One sentence

The reviewer is right that this direction, as built, served the returning visitor and
the scholar and left Mark's heart visitor a chronology; the reviewer is wrong that
fixing that makes it something other than product-led — it makes it product-led for the
first time, because the product's real first feature was always the question, and the
constitution had already put that door in front of the picker before I moved it behind.
