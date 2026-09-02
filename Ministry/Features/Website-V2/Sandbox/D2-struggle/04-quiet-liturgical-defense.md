# D2 defense — Direction 04, Quiet-Liturgical

**Sandbox artifact. The author's one defense, per the charter. Not a ruling.
2026-09-02.**

Author of `04-quiet-liturgical/`. I read my own three files, the review
(`04-quiet-liturgical-review.md`) in full, and the Decision-Log in full. I opened no
other direction and no other review. Where the review cites a governing text (the
Logo Usage Sheet, the Brand Guidelines, the UX constitution), I read the cited lines
in the source rather than trusting either the review's paraphrase or my own memory.

**Method.** I re-ran the review's browser work against my own files: the same
Chromium (`chromium-1194`) under Playwright, both pages served over local HTTP, at
320 / 360 / 390 / 414 / 1440 px, with and without JavaScript, with real incremental
scrolling. Same caveat as the reviewer's: Google Fonts is unreachable from the
sandbox, so the fallback stack rendered; every number below was taken under that
condition and, where I compared against the review, our numbers agree to the pixel.
Where I disagree with the review it is not because we measured differently.

---

## 0. The verdict I am asking for, stated first

I am not asking for this direction to survive. **It dies, and it dies on its
premise, not only on its execution.** The reviewer's §5.1–5.3 is correct, and I
will say below exactly why, in my own words, including two findings against my own
work that the review missed and that make the kill more decisive, not less.

What I am asking for is three narrower things:

1. **An accurate record.** The review overstates in four places — one measurement
   is wrong, one WCAG citation is a category error, one word ("permanently") is
   false, and one brand-rule reading is one of two possible readings presented as
   the only one. None of these change the verdict. They should still be corrected,
   because a kill that rests on eight findings should rest on the ones that hold.
2. **A salvage list that is specific**, not "a restraint policy." The review
   already grants the discipline is portable. I want to name what, exactly, with the
   reason attached to each item, because "no hover lift" without its reason is taste
   and with its reason is a rule.
3. **The right cause of death on the certificate.** The review's title for the
   surviving thing — "restraint policy" — is right but under-describes what was
   separable. What survives is the constitution's own named register, *"warm,
   unhurried"* (§1, line 50), applied to the site. The Quiet was never the problem.
   The Liturgical was the direction, and the two were separable all along — just
   not into a direction.

---

## 1. The measured defects, verified one at a time against my own files

| # | Review's claim | Verified? | What I found | Concede? |
|---|---|---|---|---|
| 1 | "Remembers" only on `before-you-sit.html`, not the homepage | **Yes** | `homepage.html`'s script is the side-door href and one IntersectionObserver; no storage call anywhere in it (`homepage_uses_storage: false`). The key `cic-threshold-crossed` is read and written only on the second page. | **Fully.** The README sentence "the slow walk is a first-time rite, not a tax" is false at the front door. This is the bug I am most embarrassed by, because the idea was right and I put it on the page a returning visitor does not land on. |
| 2 | "Door" clipped off-screen at 320/360px | **Yes — and worse than stated** | At 320px: `.order ol` scrollWidth 356 in a 320 box (36px over). Because the list is `justify-content:center`, the overflow splits: **Threshold begins at −28px, Door ends at 348px.** Dragging right reaches Door (`scrollLeft` max 36). But `scrollLeft` cannot go below 0, so **Threshold's left edge is unreachable by any input.** At 360px the same, at ±8px. At 390px it fits by 1px; at 414px it fits. | **Fully**, and I add the left-side failure the review did not report. The fix is `justify-content: safe center` or auto margins on the end items — a one-line flex-centering trap, but a real one, and I set the trap myself with `scrollbar-width:none`. |
| 3 | Forward control is the faintest thing on the page: 2.54:1 vs body text; underline 1.36:1 | **Partly** | The link text is `#6C6257` on parchment = **5.39:1** — it passes AA (1.4.3). "2.54:1 against the surrounding body text" is not a WCAG criterion, and there is no surrounding text: the link is alone in its paragraph. The underline, `--rule` composited to `#D6D2CB`, is **1.36:1** — I recomputed it; the review is exact. | **The underline, fully; the framing, no.** The text clears AA. But the review's design point is right regardless of the criterion: the sole way forward from four of six stations should not be the quietest element on the page, and an underline at 1.36:1 is not an underline. `--rule` should never color an interactive element (review §7.3 — I adopt it). |
| 4 | `aria-current` reads THRESHOLD through both silences; a 2.4.8 *Location* failure | **Half** | Under real incremental scrolling at 1440×900: THRESHOLD holds through silence-1 (y 600–1200); GREETING fires at y 1300; **TABLE holds through silence-2 (y 6100–6700), not THRESHOLD**; DOOR at 6800. The review's "both silences read THRESHOLD" is what you get by jumping the scroll position from 0 directly into silence-2 so the intermediate observers never fire; it is not what a visitor sees. On the phone the review is right: the hook `<h1>` (y 1662–1773) is on screen for roughly 200px of scroll (y 900–1000) while the marker still says THRESHOLD. Also: WCAG 2.4.8 concerns location *within a set of pages*; an in-page scroll-spy is outside its scope. | **The staleness, yes; the citation and the silence-2 measurement, no.** The marker rests through silences *by design* — I wrote "Silences are not stations; the marker does not move during one." But the review's underlying point survives the correction: a marker that admits the silences are not places is a marker admitting the silences are not anything. See §2.3. The phone lag is a band-tuning fix (`rootMargin`), and I'd make it. |
| 5 | Without JS the seat picker is inert and discards `?who=` | **Yes** | JS off, `?who=desert-monasticism`: no radio checked; button "Go to the Table"; href `?mode=table`; `form action` is `null`. Picking Alexandria by hand changes nothing. | **Fully.** The README's "the page complete without JavaScript" was true of the homepage and I wrote it as if it covered both. The fix is real and small: make it a GET form whose field is `name="worlds"` with a hidden `mode=interview`, submitting to the app — that emits exactly the deep-link grammar the app already parses. The `?who=` pre-check stays JS-only, which is acceptable degradation once the form itself works. |
| 6 | 3.4 MB of portraits, eager, for 44–132px circles | **Yes** | Seven files, **3,444,998 bytes**; `bethlehem.png` is 1,123,838 bytes at 748×748, displayed at 48px on the seat picker. No `loading="lazy"`, no `srcset`, no `decoding="async"`. | **Fully.** They are the live site's own assets, unchanged — and I did nothing to mitigate them, on a direction whose whole claim is that it costs the visitor less. |
| 7 | Three meaningful sizes under the constitution's 13px floor | **Yes** | `.order a` 12.48px; `.eyebrow` 12.8px; `.seat-era` 12.48px. §2.2 line 105: "Nothing smaller than 13px ever carries meaning." | **Fully.** Trivial to fix (`0.8125rem`), and the review is right that it is embarrassing in exactly the three places most specific to this direction. |
| 8 | Header side door forces a three-line mobile header; 232–258px of chrome "permanently" | **Header yes; "permanently" no** | Header 210px at 320, 183px at 360–414; the nav block is 125/99px — three lines. **But `.site-header` is `position: static`.** Only `.order` is sticky, and it is **49px**. After the first scroll the chrome tax is 49px (≈6% of 844), not 27–34%. | **The three-line header, fully** — 42 characters of italic in a flex nav was careless on a phone. The "permanently" is wrong and should come out of the record. |
| 9 | Five identical "Continue when you are ready" links (seven across both pages) | **Yes** | Five on the homepage, two on the second page, all identical text, all different targets. | **Fully.** 2.4.4 survives on context; a links-list rotor does not care about context. Visually-hidden suffixes fix it. |
| 10 | Protected lines repeated across the two pages within two minutes | **Yes** | "Where the historical record is thin…" (Greeting + §II); "We measure whether…" (Door + §III); the AI framing sentence near-verbatim on both. | **Fully.** I flagged "a second threshold" as stretch #3 and offered dropping it; I did not name repetition as its cost. "Repetition is what turns solemn into rote" is the right sentence. |
| 11 | Dark-mode census tints as rings: four under 3:1; README's "every pair actually used" is untrue | **Yes** | The seven `--seat` rings are absent from my contrast table. | **Fully.** The claim was overbroad. The finding belongs with the D1 cross-validated usage-rule gap and I would have wanted to catch it myself. |
| 12 | `scroll-behavior: smooth` animates a 7,553px traversal when the escape hatch is clicked | **Yes** | `html{scroll-behavior:smooth}` under `no-preference`; the marker links are plain anchors. | **Fully.** The escape should not itself be pacing. |
| 13 | `* { transition: none !important }` is a sledgehammer | **Yes** | It is. | **Fully**, as a build rule. In a mockup it was the fastest way to make a policy auditable; in a real stylesheet the policy is "do not write transitions," not a global override any component must fight. |
| 14 | Screen reader: silences are ~8 seconds each; nav label "The order of arrival" is spoken; 13 landmarks | **Yes** | The ARIA tree the review printed is what my markup produces. | **Fully**, and this is the sharpest small finding in the file: the one liturgical phrase I let reach a reader reaches only the reader who gets none of the atmosphere it was meant to pay for. |

Fourteen claims: eleven concede in full, three concede in substance with a correction
to the record. Nothing in the table is a matter of taste.

---

## 2. The central claim — the ordo, and where the review is right

### 2.1 The argument the reviewer invited, made honestly

The review says the strongest available rebuttal is that *Threshold · Greeting ·
Table · Door* is a hospitality sequence, not an order of service, and that a cold
visitor sees four plain English words. I believe that argument, and here is the
evidence for it.

The mapping the review draws — Threshold → Gathering, Greeting → Word, Table →
Table, Door → Sending — is the **fourfold ordo**: Dix's *Shape of the Liturgy*
(1945) as received by the twentieth-century liturgical movement and printed into the
Lutheran Book of Worship (1978), the 1979 Book of Common Prayer, and the United
Methodist Book of Worship (1992). It is a seminary frame. It is not a lay
recognition. Ask a person leaving an evangelical church — and a large share of the
American reassessing audience is leaving exactly that — to name the four movements
of a service and they will say songs, announcements, sermon, altar call. Nothing in
my four words maps onto that. And the review's own mapping is imperfect at its
second term: **Greeting is not Word.** There is no reading in my Greeting, no sermon,
no proclamation; there is a hello and a disclosure. A doorstep, a hello, a table, a
way out is the shape of a dinner invitation. It is the shape of every house.

That is the argument. Here is its honest limit: I cannot prove the cold reading. I
have no user test; neither does the reviewer. On the four words alone we are two
people asserting what a stranger would see. Call it a draw.

### 2.2 And the draw does not matter, because the review's fallback wins outright

The review says: if you want the sequence, the rubric decides it. That is correct,
and I concede it without reservation.

*Silence is kept.* is not liturgical-*ish*. It is, word for word, a rubric of the
Anglican service books — the 1979 BCP's "Silence may be kept," Common Worship's
"Silence is kept." Nobody outside a service book says a silence is *kept*. Ordinary
English says pause, breathe, take a moment. I set it in red italic because red
italic is what rubrics are — I said so in my own README, proudly — and in the
passive-impersonal because that is the grammatical voice of an institution telling a
room what it will do. The review is right that this one line retro-reads the four
words around it: once you have seen a rubric, the doorstep becomes a narthex.

**And I add a finding against myself that the review missed.** The Brand Guidelines'
own *Never* list (Consolidated V1.0, line 70) already forbids **"Christianese or
project jargon."** *Silence is kept* is Christianese by any test — it is the dialect
of one tradition's service book, unintelligible as an instruction to anyone outside
it. I did not need Mark's 2026-09-02 ruling to be outside the rules. I was already
outside the brand's own text rules, and I had the file open when I wrote the line.

### 2.3 The silence dilemma — the thing I can say more precisely than the review did

The review makes two attacks on the silence stations that look separate: §2.2 (they
are forced pacing, against Participant Agency) and §3.2 (they are a picture of a
silence, not a silence). I want to show these are one finding, because seeing that
is what convinced me.

A silence station on a web page has no stable identity. **Either it holds you, or it
does not.**

- If it holds you — a timer, a gate, anything withheld — it is "pressure toward
  predetermined outcomes" and the constitution's governing value is violated. I did
  not build that; the reviewer verified I did not: no timing, nothing withheld, the
  way on printed at the bottom of every silence.
- If it does not hold you — and 765px on a desktop is one wheel gesture, 464px on a
  phone is one flick, which is what I built — then nobody keeps it. A silence nobody
  keeps is a `<section>` with `min-height:85vh` and a red line asserting a state
  nobody is in. That is the review's §3.2, and it is exact: the page describing its
  own effect is the tell.

There is no third state. I looked for one while writing this and there is not one:
a page cannot make a silence *happen*; it can only gate (agency) or decorate
(atmosphere). The device fails one test by passing the other. I concede both
findings because the device cannot escape either.

On the review's phrase "neither skippable" I will contest the *wording* only: the
silences are skippable exactly as any section of any page is, and nothing is gated.
But that concession is what makes them decoration, so it is a correction to the
sentence and not to the verdict.

### 2.4 Therefore the surgery in §5.3 is right

Remove the rubric, the silences, the order marker, the station names, and the five
"Continue when you are ready" links, and what remains is not a stripped-down
Quiet-Liturgical. I agree. What remains is a well-set page in the constitution's own
register — *"warm, unhurried, nothing antiquarian, nothing tech-forward"* — which is
the register every direction should have had before it added anything. The Quiet
was never a bet. The bet was the Liturgical, and the review has shown the bet loses
under Mark's ruling, under the brand's own Never list, and under its own logic.

One correction on the review's §5.2 list, for the record and not for the verdict:
"Continue when you are ready" is ordinary English in isolation — it is what a nurse
says, what a driving instructor says. It becomes the voice of a retreat leader only
when it is repeated five times under a rubric. Remove the rubric and it is a polite
link. I would still cut four of the five, for the screen-reader reason in row 9.

---

## 3. The constitution — partly wrong, mostly right, and worse for me than the review said

### 3.1 The narrow transfer that is real

The review says neither of §4.0's two reasons for stillness — one-primary-surface
budget, anti-ghost — exists on a marketing page. The first does not. The second
does, narrowly, and the constitution says so in its own scope line. §2.5a (line
135): *"The anti-ghost principle (**governs everything visual with a figure in
it**)."* The seven portraits on my homepage are figures. So "the seven never fade in,
lift on hover, glow, or dim, on any surface" is not house taste; it is the anti-ghost
rule applied where the rule says it applies. I want this carried forward *with its
reason attached* (§6, item 1), because without the reason it is indistinguishable
from a preference.

### 3.2 The pacing does not transfer — conceded in full

Everything past that narrow point, the review has right. §4.0's stillness is a
budget decision and a representation decision; neither says *slow*. I kept the
conclusion and swapped the premise, and the premise I swapped in — *"the order
unfolds at a pace the people did not choose"* — is, as the review says, the
constitution's prohibition restated approvingly. I wrote that sentence as a
description of how liturgy works and applied it to a visitor who did not ask for
liturgy. I concede the sentence in full. It is the thesis, and it is wrong.

### 3.3 The finding that makes it worse

Here is what I found reading §4.0 and §5.1 side by side, which the review's S0
argument gestures at but does not close.

§4.0 (line 252): the Living Table scene is *"the populated, still descendant of the
approved landing hero."* §5.1 (lines 371–376): that landing hero carries *"the
protected hook as the headline"* and *"three co-equal doors under the hero"* —
**Start with your question · Build your own table · Guided onboarding** — door
first. So the constitution's own stillness lives, by its own account, on a
door-first, headline-first surface. Stillness and door-first were never in tension
in the source text. **My direction invented that tension**, took the stillness, and
removed the door — and then flagged four smaller stretches for Mark's ruling while
making the largest one quietly. The review called it the unflagged S0 inversion. I
would put it more strongly: I cited a text as my warrant that contained, three
hundred lines away, the exact layout I was departing from.

### 3.4 And there is no question-shaped door at all

The review did not press this, but the Decision-Log's cross-direction finding does
and it applies to me: §5.1's first door is *Start with your question*, and **neither
of my pages has one.** A visitor arriving with a hard, personal question — Mark's
named heart — can meet seven Representatives, cross two thresholds, and take a
seat, and at no point is there a place to put the question down. This omission
would have killed the direction against Mark's audience ruling even if the rubric
had never been written. I name it here so it is on my side of the ledger.

---

## 4. Three brand rulings the review raised

### 4.1 "The joining" — a contest, held modestly

The Usage Sheet's never-list (line 62–63): *"the motion never replays unbidden and
never plays the joining at a visitor."* The review reads "the joining" as
`cic-sitdown`, the dot settling, and says my autoplay is "at minimum the case that
sentence was written to worry about."

"The joining" is not defined anywhere in the brand files — I searched. Two readings
are available. (a) The review's: the joining is the sit-down. (b) Mine: the joining
is the guest *entering the ring* — the one motion the brand refuses to depict in
any state (Usage Sheet, line 30: the dot is "never inside the ring in any state";
my CSS comment, line 154: "The dot never enters the ring"). Under (b), the sit-down
is not the joining; it is the dot settling *at the threshold*, and the state it
produces is the sheet's own permitted still state, *"table built, guest seated."*

Two facts favor (b), or at least make (a) costly. First, the brand's own
implementation reference autoplays the full sequence on load, once per arrival — the
review verified my copy is byte-faithful. If (a) is right, the brand's reference file
violates the brand's never-list, and the fix belongs to the brand thread, not to
this direction. Second, "replays unbidden" is honored by construction: the header
carries no mark, so it cannot play twice. **What I concede is the process point:** an
undefined phrase in a never-list that could be read against my first screen belonged
on the stretch list for Mark, and I did not put it there.

### 4.2 Caption rule, not headline rule — conceded

Usage Sheet, line 14: *"The mark never appears at first contact without this one
plain sentence **beside** it."* Brand Guidelines, line 99: *"said once **beside** the
mark at first contact."* Beside. It is a caption rule, exactly as the review says,
and I promoted the caption to the entire first screen. For the first 800ms of the
brand's own timing, that screen is a red dot and a sentence about a ring that is not
there yet. I concede.

### 4.3 Governance order — a small contest, with the file

The review (§2.5) says I put governance "at the top of station II." The Greeting's
order in the file is hook (line 300) → one-breath sentence (301) → doorway line
(302) → trust block (304–309). Governance is at the *bottom* of the Greeting, after
the experience is named; mechanism (the ten-step process) is on the second page.
The voice pair — experience first, governance second, mechanism third — is honored
in sequence within the station. The tension the review names is real only at the
level of "before the seven are introduced," and the *Always* list is explicit that
we raise the AI question first. Minor; noted for accuracy.

---

## 5. The heart audience — conceded, in my own words

The review's §6.2 is the paragraph I cannot answer, so I will not try. The site
decides when the visitor is ready and calls the decision theirs. For a person whose
grievance may be precisely that an institution once told them how to feel and when,
that is not incidental. I designed for a real person — the contemplative arrival,
someone with time and quiet who wants to be prepared before they speak. That person
exists. Mark did not name them. He named the person holding a question, and my
homepage makes that person carry it through eight screens before offering a chair,
and never offers them a place to set it down.

The review's distinction — *no pressure and no imposition are not the same thing* —
is the sentence I would want to carry out of this file above every other. I removed
every pressure to act and added a pressure to feel, and because the second was
framed as care it was harder to object to. That is correct.

Where I would keep one thing from §6: the review credits the direction, on
*pressure* alone, as possibly the best of any register available. I want that
credited as a checklist, not an atmosphere (§6, item 2).

---

## 6. What I ask to carry forward — specific, with the reason attached

Not "a restraint policy." These, by name:

1. **The stillness rule for figures, with its reason.** The seven Representatives
   never fade in, lift on hover, glow, or dim, on any surface — because §2.5a
   governs "everything visual with a figure in it," and the marketing page has
   figures in it. Everything else in the restraint policy (no reveal-on-scroll, no
   transitions as a default, instant state changes) is house style, kept because it
   reads as unhurried; it should be labeled house style, not constitution.
2. **The pressure inventory, as a D3 checklist.** No urgency, no scarcity, no
   countdown, no conversion push, no promised transformation, one action per
   surface, the support ask below the door in the quietest register on the page,
   and a decline path that is complete and graceful (*Not today — back to the
   door*). The review says this may be the best reading of "no pressure, just
   witness" available; it should be tested against every surviving direction as a
   list, not felt as a mood.
3. **The site remembers — on the homepage, first screen.** The pilot asks each
   participant for about five conversations; that is four returns per participant,
   and the live site has no return path at all. The idea was right and I put it on
   the wrong page. Fixed, it is a one-line courtesy at the top of the front door
   for a visitor the site has seen before, in `localStorage` inside try/catch,
   invisible to everyone else.
4. **The header side door, shortened.** "Already know the way? Go to the Table →"
   is the right concept — a quiet one-tap route for the returning participant that
   is text, never a button — at a length that does not cost three nav lines on a
   phone.
5. **The seven as places, chronological, one at a time, each with its own action.**
   The review grants this is materially better than the live carousel for scanning,
   keyboard use, and screen readers. Never a carousel; a carousel is a hurry.
6. **The seat picker with the nameplate inversion — as a GET form.** Field
   `name="worlds"`, hidden `mode=interview`, submitting to the app: it then emits the
   app's own deep-link grammar and works without JavaScript. The inversion is the
   Living Table's own device and the one selection cue the constitution endorses.
7. **The AI disclosure as a heading in our own voice, before the seven are
   named.** *You will be in conversation with an AI system.* — the *Always* rule made
   structural, in the greeting register rather than the footer register.
8. **Two brand-compliance findings for the live header, regardless of direction:**
   the italic *in* in the wordmark (the live header drops it) and the mark never
   bare at first contact (the live header shows it bare). Already noted in the
   Decision-Log; this file is a second independent flag.
9. **Three contrast rules for the V2 usage layer:** graphite `#8A837C` never as text
   below 24px (3.38:1 on parchment — my finding, the review's independent
   confirmation); `--rule` never colors an interactive element (the review's
   finding — I adopt it); the seven census tints measured in dark mode before any
   use as rings, underlines, or borders (the review's finding, extending the D1
   cross-validated gap from text to graphics).
10. **The motion inventory as a deliverable format.** A table: every motion on the
    page, whether it moves, why, and what `prefers-reduced-motion` receives. The
    review confirmed mine was complete and byte-faithful; the format is the part
    worth keeping.

Items 1, 2, 3, 6, 7, and 10 are not in the review's own salvage list. I ask that
they be added to it.

---

## 7. Verdict, in one paragraph

**Dies, including the premise.** Not for sloppiness — the review is generous about
the craft and I will accept the generosity — but because the narthex was the wrong
room. The person Mark named is not crossing a threshold into a church. They are
standing outside one, holding a question, and my front door asked them to keep a
silence before it told them what the building was. The four plain words might have
survived on their own; the red line under them could not, and the brand's own Never
list had already said so. The discipline goes to D3 with its reasons attached. The
shape does not go anywhere.

---

*Author's note on scope: I wrote only this file, touched no git state, and modified
nothing in `04-quiet-liturgical/`. Measurement scripts ran from the session
scratchpad against local HTTP copies of my own two pages; nothing was changed on
disk to take a reading.*
