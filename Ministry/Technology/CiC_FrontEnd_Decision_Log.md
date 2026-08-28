# CiC Front-End & Product — Decision Log

Dated entries: what was decided (or what's still open), the reasoning — including the
"heart" reasoning, not just the operational one — and the specific next action. A
decision that only lives in conversation history is one that gets re-litigated by
accident later.

Scope: the participant-facing product — what a real person sees, clicks, and
experiences. Distinct from the world-build threads (which own construction methodology)
and from the System Hub log (which owns operations and thread dispatch).

---

## 2026-08-14 — The current-day space: scoped as its own program, not started

**Origin.** Raised by Mark immediately after the Era 10 freeze, while looking at what the
frozen map does and doesn't do for a present-day visitor. His framing, in his own words
across the exchange: *"whats happening in the world today, where do i fit, where do i
go"* — and *"we show more of jesus by revealing what jesus is doing and they can find
things they resonate with and reject. and eventually find Jesus in deeper relationship by
finding a place."*

**Status: SCOPED, NOT STARTED.** Mark's explicit sequencing — finish the ten-era Atlas
and get it live first, then the interview and multi-voice Table upgrades in their own
threads, and only then open this. Recorded here so the thinking survives the gap.

### The gap this answers, with the number that grounds it

The census has **one living row starting after 2000, and four starting after 1990**, out
of 257 at the time of the finding. A visitor arrives in the present and the map goes
quiet right around where their own experience begins. That is not a defect in the
historical work — it is the recency floor doing its job for history and failing when
applied to today.

Two structural facts about living movements that the Atlas's grammar does not currently
carry, both surfaced in this conversation:

- **Many living currents are not things you can join.** New Calvinism, deconstruction,
  the Christian Right — these run *through* institutions rather than being institutions
  with boundaries. That distinction is exactly what someone asking "what are my options"
  needs, because the answer differs completely: one is a door you can walk through, the
  other is a mood inside doors you might walk through. The census has no field marking it.
- **There is no alias field at all** (verified: zero rows carry one). People search what
  they have heard — "young restless reformed," not "New Calvinism"; "exvangelical," not
  "deconstruction." Living rows need an also-called list, including labels a movement
  itself rejects, marked as rejected — more findable *and* more honest than implying a
  settled name exists.

### Decisions

1. **It is its own program, not an Atlas feature.** The vision document already carries
   the mandate — the mission says "throughout history **and today**," and Conviction 1
   says "historical **and contemporary** movements." The contemporary half has simply
   never been built. This is the unbuilt half of the stated mission, not an add-on.

2. **Organise by question, not by movement.** The Atlas is organised by movement and by
   birth date, which is right for history. A person exploring faith is not asking "what
   movements exist" — they are asking who Jesus is, what forgiveness means, why
   suffering, what to do with doubt. The current space leads with the question and lets
   living traditions answer it. The Atlas then sits underneath as the "where did this
   come from, and how did it get here" layer — Mark's own "the map can work into it."

3. **Show what is shared, not manufactured contrast — Mark's correction, adopted.**
   An early framing had several traditions answering "visibly differing." Mark rejected
   it: *"we don't need to always put different ideas in contrast or exclusivity."* He is
   right, and the vision backs him — it says outright the project is not for
   denominational comparison. Much of what is alive right now is shared across
   traditions: prayer, scripture, feeding people, people returning after years away.
   Showing that as *one thing happening in many places* is closer to revealing what Jesus
   is doing than staging a debate. Difference still gets shown where it is real and
   load-bearing — just not produced everywhere by the layout.

4. **Seeing more of Jesus and finding a place are one arc, not a fork — Mark's
   correction, adopted.** An earlier framing offered these as alternative product goals.
   Mark: *"its not just a single think we can do both... eventually find Jesus in deeper
   relationship by finding a place."* The operative line is not "never point at a door" —
   it is **don't push anyone through one.** Showing someone that what moved them exists
   in real communities with real doors is service; ranking those communities for them is
   not. A "find your tradition" quiz would violate participant agency even though it
   would be the most clickable thing available.

5. **Rigor moves, it does not loosen — and rule-making must not become the obstacle.**
   An early draft of this thinking treated the vision's Living Traditions clause ("a
   tradition's present-day self-understanding... is not ours to define or represent") as
   a hard constraint requiring an elaborate protocol. Mark corrected this twice, and the
   correction stands: that clause exists because historical source sets are *closed* and
   those communities cannot speak for themselves any more. Living movements are the
   opposite — they publish constantly and are entirely capable of speaking for
   themselves. So we point at what they actually say, dated, and let people read it.
   Mark, verbatim: *"all these added rules that you add cant get in the way."* Recorded
   as a standing caution on this track — the Era 10 rigor regime was right for a frozen
   census and would be wrong here.

   **The whole standard reduces to one honest line to the participant:** this part of the
   map is settled and sourced; this part is alive, it moves, here is when we looked, and
   people inside it disagree about what it even is.

6. **Misconceptions: let the tradition answer, never adjudicate.** Mark asked for a space
   where people can explore "their own and other truths and misconceptions." CiC ruling
   on what is a misconception would make it referee between living communities. The
   working form instead: *here is what you may have heard; here is what they say about
   themselves right now, in their own words* — the participant does the reconciling. This
   preserves participant agency and is more persuasive anyway.

### Related, decided on the census side the same night

An **era 11 emerging band, defined by confidence rather than a date cut** — everything in
it visibly provisional, rows graduating into era 10 as they stabilise. A hard ten-year
line is false precision. This gives currents like deconstruction a home that is not
"retain with a caveat, demote to mentions, or delete." Also named as the largest missing
piece: a **trajectory reading** per living row — what this was twenty years ago, what it
is now, what moved it. Full account in the System Hub Decision Log, 2026-08-14.

### Next action

None yet, by Mark's own sequencing. When this opens: draft a short program brief on the
shape above — question-first surface, shared-before-contrasted, the Atlas underneath as
the provenance layer, and the one transparency line. Not a protocol.

**Open, and deliberately not resolved here:** platform and phase placement (this does not
obviously belong to any rung of the existing Alpha → Beta → Phase 1 → Phase 2+ ladder),
whether it ships inside the existing app or as its own surface, and its cost shape.

---

## 2026-08-25 — Three-level transparency: scoped as its own dedicated build, not a port

**Origin.** Mark used the newly-launched pilot (`cic-engine`) and reported three real
problems: (1) the three-level transparency system (highlight → hover → click) is not
working; (2) the Facilitator gives no greeting at session start, just a prompt at the
bottom; (3) the world-selection cards are too thin to build participant confidence about
"which Christian world" they're entering. All three are real product gaps, not launch bugs.

**Status: SCOPED, NOT STARTED.** A full launch prompt for a new dedicated thread has been
written and handed to Mark. Items 2 and 3 are deliberately deferred — Mark's own
sequencing — to start only once transparency work is underway.

### Decisions

1. **Transparency gets its own thread, not a copy-over.** Mark: *"this is a bigger project
   than importing or copying over what was there... i want it done very well, designed
   well, built well and implemented well."* The old `cic-poc` components
   (`GlossHighlight`, `LexiconModal`, `Level3Panel`, `CitationMarker`, `CitationModal`) are
   reference for what was tried, not a working baseline to port — they were removed from
   the tree and the underlying wiring (glosses, figures, citation depth) was never
   finished even there.

2. **Scope is all three tracks together — highlight, hover, and click** — not a phased
   subset. Mark's answer to the scope question: *"all three."*

3. **The heart of it is discovery, not comprehension-aid or credibility-verification —
   Mark's correction, adopted.** I offered a binary framing (don't let someone get stuck
   on a word / let someone verify a claim); Mark rejected both for something more central:
   *"its discovery, we may think differently or understand words differently. its deeper
   discovery."* The target is a participant noticing where their own assumed meaning
   diverges from the world's own frame — not just glossing an unfamiliar term. This
   reframing governs what content the system should surface, not just how it displays it.

4. **Items 2 (Facilitator greeting) and 3 (richer world cards) wait.** Mark: work on those
   "after we get the work on the 3 level transparency working." Both remain real,
   confirmed problems — greeting text drafts (A/B) are drafted and awaiting his pick;
   richer cards have real unused source material identified (`world_core`'s `horizon`
   field, compiled `frame.frames.general_seeker.starters`) — just not started.

### What the launch prompt carries forward

Grounding so the new thread doesn't have to rediscover it: the *current* gap is
structural (glosses are hardcoded empty, figure records are compiled but never wired to
any API or frontend path, citations render flat with no Level 2/3 depth) and distinct from
the *historical* diagnosis in `VR_1A_Transparency_Gap_2026-08-09.md` (the old system's gap
was mostly unfamiliar names/figures, not generic vocabulary). The interaction design is
already decided and final in `CiC_Full_UX_Design_V1_0.md` §9.1 — side panel / bottom sheet
only, never a centered modal. A real, authored, reviewed content layer already exists
across all six worlds and is currently unused by anything — `modern_contrast` (60 records)
and `senses.translational` (85 records) — that does exactly the "deeper discovery" work
Mark described once he named it, and should be the backbone of what the click level shows.
`transparency_reach.py` is the existing measurement instrument (report-only by design, no
pass/fail bar, to avoid a "gloss everything" pressure that would make the Representative
lecture) and should be used to check the finished build, not just diagnosed as a tool.

**Model choice for the new thread:** recommended Sonnet 5 for the build (compiler wiring,
new API endpoint, frontend components — well-specified engineering, not open-ended
judgment), with Opus 5 called in specifically for the content-selection quality pass
across the six worlds and a design-fidelity check against the UX spec — not as a blanket
reviewer. Fable 5 not recommended: its premium is for resolving ambiguity, and the scope,
framing, and interaction design here are already decided.

### Next action

Mark takes the launch prompt to a new thread and starts the build there. Once transparency
is working, resume items 2 and 3 in this thread per his sequencing.

---

## 2026-08-25 — Richer world cards/doorway built; Facilitator greeting drafted, awaiting pick

**Status.** Transparency (the prior entry) shipped and launched in its own thread. Picked
up items 2 and 3, deferred from the 2026-08-25 pilot feedback per Mark's own sequencing.

### Item 3 (richer cards) — DONE, built and pushed

**Concrete finding, not just a vibe:** the world-list card never rendered the world's own
display name at all — only the Representative's personal name and role (e.g. "Chloe ·
Household Leader"). A participant scanning six cards had no direct way to tell *which
Christian world* a card even was, which is exactly Mark's stated complaint ("clarity of
wth chrsitian world"). Fixed directly: the tradition's display name now leads every card,
in its accent color.

**The doorway went further**, closing real gaps against Program-Spec SS165's own
definition of "the detailed world card" (display name/period/place, thinness statement,
the living-tradition distinction where flagged, self-disclosure, persona provenance,
starter questions) — most of which the doorway had never carried:

- **horizon** — world_core's own scene-setting paragraph, already authored and already
  compiled into the voice's own system prompt, but never surfaced to a participant. Now
  compiled into `compiled/frame.json` too (`engine/m2/builders.py::build_frame_json`) and
  shown as the doorway's lead paragraph.
- **Living-tradition distinction** and **self-disclosure/persona provenance** — both
  quoted verbatim from the spec itself (O0 for "who built this and what it hopes";
  SS165/SS166 for the living-tradition sentence and the persona-provenance line). Verbatim
  quotation of language Mark already approved at the spec level, so this did NOT need a
  fresh draft-and-approve round the way new Facilitator copy does.
- **Starter questions** — sampled from the compiled frame's real per-cell canon
  (identity/personal/critical framings, not an arbitrary first three), so a participant
  can see the actual range of what's askable before committing.

**New surface:** `GET /api/worlds`, reading each formation world's real compiled
frame.json through the same load path a session uses — the frontend's `data/worlds.ts`
had carried its own comment since Stage 4 admitting it hand-copied the registry because
"no /api/worlds endpoint exists yet." That endpoint exists now; the frontend fetches live
and keeps only what the registry never carried (portrait image, accent color, display
order) as local assets. All 7 registry packages (6 formation worlds + the fix fixture)
recompiled to carry `horizon`; determinism and staleness both green; 349 backend tests
pass; verified live in a browser against the no-spend dev server (world list, doorway,
deep link, and full conversation flow all screenshotted and working).

### Item 2 (Facilitator greeting) — DONE, built and pushed

The conversation screen opened with no introduction — confirmed still true, and exactly
the gap Mark named ("no introduction, do greeting"). `facilitator_turn`'s `"door"` kind
had been declared in the event schema since early in this build but was never emitted
anywhere in the codebase (confirmed by direct grep, not memory).

Two drafts were prepared, same discipline SYSTEM_NATURE/CHECK_IN/DEPENDENCY_CHECK went
through (`engine/m4/facilitator_turns.py`) — plain, honest, no invented warmth the system
hasn't earned, keeping the SS4.3a convention that the Facilitator names itself plainly
while the Representative is named by its own registry name. **Mark picked Option A**
("Welcome — I'm the Facilitator. I don't belong to any world; I'm just here to keep this
space honest. You're about to speak with {representative_name}, {role_label} of
{display_name}. Ask anything you like — {representative_name} answers only from what's
actually known of this world, and will tell you plainly when the record runs out.") —
Option B (the fuller "door metaphor" draft) was not carried into code.

Wired exactly as scoped: `door_turn()` added to `engine/m4/facilitator_turns.py`;
`engine/api/wiring.py::create_session` appends it right after `open_session()` commits
`session_started` (the entrance seal only restricts who may write `session_started`
itself, not what else `create_session` appends after it); the frontend's
`useConversation.begin()` now fetches the transcript once session creation resolves,
rather than starting the screen from an empty turns array. All existing event-sequence
and transcript-index test assertions updated for the new leading `facilitator_turn`
event; 349 backend tests pass; verified live against the no-spend dev server — the
greeting renders as the conversation's first turn, correctly slot-filled per world.

### Next action

None outstanding from the 2026-08-25 pilot feedback — all three reported problems
(transparency, greeting, cards) are now built and shipped. Open items going forward
belong to whatever Mark raises next.

---

## 2026-08-25 — Public pilot access: Atlas overpromise fixed, access ask added, Get
Involved cost figures refreshed

**Origin.** With the pilot live on `cic-engine`, this thread's job was to make
`cic-website/` a seamless front door to it — access, landing, and a working Get
Involved path — without building or designing the multi-voice Table Mark is
building separately (~1-2 weeks out) or hard-coding assumptions that thread will
need to undo.

**Atlas fix, branch `claude/pilot-launch-website-access-j640i1`.** `atlas-v3.html`'s
click-sheet offered two actions per live world: "Interview {name}" (honest, already
worked — single world, direct hand-off) and "Add to the Table" (fed a multi-select
tray, up to three worlds, handed off with `mode=table`). The engine seats exactly
one world per session (spec O9); the other two picks were silently dropped, no
explanation shown — the single most concrete "not seamless" thing on the live site.
**Removed the tray entirely rather than capping it at one** — with "Interview" already
the honest one-world path, a one-seat "tray" had nothing left to do. Table's real
multi-select UI is the Table thread's own to design when it ships; this fix
deliberately builds nothing toward it.

**Landing-page ask, `index.html`.** One quiet line + link below the existing primary
CTAs ("Come and join us at the Table" / "Explore the Timeline"), never in the hero,
framed around access rather than general support: *"Running these conversations
costs real money, which limits how many people can use them. If you'd like to help
with that, see Get Involved."* Drafted, then passed through an Opus 5
credibility/tone pass (per this thread's own model-routing guidance) before
shipping — the review's main correction was cutting an earlier draft's "pull up a
chair" phrasing (collided with the door metaphor, read as reaching) and a
rhetorical-question option (read as clickbait).

**Get Involved refresh, `support.html`.** The live $2/hr (1:1) and $5/hr (3-person)
figures were Mark-approved but measured against the pre-rebuild system (Anthropic
Console API, different model routing) — never re-measured against this pilot's
engine (AWS Bedrock), which the project's own spec (principle 13) treats as a hard
rule: no $/turn figure quoted until invoice-reconciled. Also, the 3-person figure
describes the Table feature, which isn't live in this pilot. **Kept $2/hr, relabeled
as a carried-forward estimate rather than implied-fresh; cut the $5/hr figure**
rather than quote a price for a feature that doesn't exist yet. Opus 5's sharpest
edit: cut a defensive "not a made-up number" aside from an earlier draft — nobody
had accused it of being one, and pre-empting the accusation invited the suspicion it
was trying to defend against. Final wording states the number's provenance plainly
instead of hedging twice.

**Stripe — explicitly not done, and blocked on Mark.** No live Stripe integration
exists (the old `giving.py`/`cic-poc/backend` checkout service is suspended).
Documented in `support.html`'s own header comment as the recommended next step —
Stripe Payment Links, one per fund, no server dependency — but genuinely blocked:
the Stripe account was flagged under Stripe's "fundraising by nonprofits/charities"
restricted category (Faithways is a for-profit PBC, not a charity); a response was
submitted with a Sept 4 deadline and its resolution was never confirmed. **First
thing for Mark to do on this thread's account: check the Stripe dashboard
directly.** Creating the Payment Links themselves is also his own dashboard action,
per the standing precedent from the original Stripe build — not something this
thread took or could take.

**Smaller staleness, same pass, none blocking:** `pilot-feedback.html`'s form
previously submitted via `<form action="mailto:...">`, which several browsers
silently no-op instead of opening the mail client — replaced with JS that builds a
real `mailto:` link from the filled fields and navigates to it the way clicking an
`<a href="mailto:...">` would, plus a visible fallback line naming the address
directly. `whats-next.html`'s Representative Modes section described 2026-07-16
validation findings as if still current; corrected to note that build predates this
year's full engine rebuild and needs re-integration and re-validation, not just
picking back up (confirmed by direct grep: the feature has zero footprint anywhere
in `engine/`). `cic-website/README.md`'s claim that nothing links to `support.html`
was stale since 2026-08-06 (nav links to it as "Get Involved") — corrected.

**Verified, not asserted:** loaded all six changed pages in a real headless browser
against a local static server after the edits — the access-note line renders with
the reviewed text, the reps carousel still populates all six cards, the Atlas's
`#tray` element and `[data-act="add"]` button are gone, its `[data-act="interview"]`
button still works, and the feedback form's new `id="feedbackForm"` is present, with
zero console/page errors traceable to the changes (the only console errors were
Google Fonts requests failing in the sandboxed test environment, present on every
page regardless of this thread's edits).

### Next action

~~**Mark, in order:** (1) check the Stripe dashboard for the compliance-flag
resolution — this blocks everything Stripe; (2) once clear, create the two Payment
Links (Accessibility, Academic Review) and hand the URLs back so `support.html`'s
mailto CTA can be swapped for real checkout;~~ **(1) and (2) DONE, same day** — see
next entry. (3) still open: read the landing-page ask line and the refreshed Get
Involved cost paragraph (both above, both already Opus-5-reviewed) and confirm or
redirect before treating them as final — new participant/donor-facing copy gets his
own read before shipping, same discipline as the app's own Facilitator text, even
after a model review pass.

---

## 2026-08-25 — Real Stripe checkout live on Get Involved

**Status.** Same day as the entry above. Mark confirmed the compliance flag is
resolved and had already built and tested real checkout himself — a live $5
contribution went through successfully — before this thread finished the rest of
its work. Wired the result into `support.html`.

**What Mark built, not this thread's call:** two Stripe Payment Links, split by
**gift frequency**, not by fund — a real, working structural choice this thread
hadn't anticipated (the prior entry's own header-comment note recommended "one
[link] per fund," which turned out not to be what got built). Both are plain
hyperlinks, no SDK, no server, matching the "no accounts, no feature-gating"
philosophy the recommendation was reaching for anyway:

- **"Keeping the Door Open"** — one-time gift — `buy.stripe.com/fZu5kwbbRONkbXegEI8bS01`
- **"Open the Door Wider"** — monthly recurring — `donate.stripe.com/28E14g3Jp2Vsd1igEI8bS00`

**Reconciling with the two named funds.** Neither link is fund-specific, so a giver
who wants to designate Accessibility vs. Academic Review can't do it at checkout
directly — the "Be Part of It" section now says so plainly and routes that request
to email instead, rather than silently dropping it or inventing a fund-selection
mechanism Mark didn't build. The two funds stay named as what gifts support in
general (settled ground, unchanged); the two buttons are simply the two ways to
give, not a fund picker.

**Superseded in `support.html`'s own header comment**, not deleted — the prior
"BLOCKED until Mark checks the Stripe dashboard" note is marked SUPERSEDED in place
so the resolution is visible in the same spot the blocker was recorded, per this
log's own standing discipline against letting decisions live only in conversation
history.

**Verified before shipping:** loaded the page in a real headless browser — both
buttons render with the exact URLs Mark gave, correct link text, the mailto
fallback for fund-specific/alternate giving still present, zero console errors.

### Next action

~~None from this thread — checkout is live and verified.~~ Superseded same day —
see next entry (Academic Review Fund dropped).

---

## 2026-08-25 — Academic Review Fund dropped; Accessibility is the only giving ask

**Origin.** Mark, direct instruction, immediately after the checkout wiring above:
*"we are not doing the academic fund now, just two funds for expanding the
accessability."* Read as: cut the Academic Review Fund as a giving target on this
page; the "two" are the two Payment Links already built (one-time / monthly), both
now unambiguously feeding the one remaining fund — Accessibility.

**What changed, `support.html`:**
- "What We're Doing About It" — removed the "Funding academic review" paragraph
  entirely (it framed academic review as something a gift funds directly, which
  is no longer true of anything on this page).
- "Be Part of It" — intro paragraph rewritten from "give to either of two funds" to
  "every gift goes to the Accessibility Fund," with the one-time/monthly split
  reframed as two ways to give to that one thing, not two things to choose between.
  Dropped the "want your gift designated to a specific fund" line from the
  post-buttons note — with only one fund left, there is nothing left to designate
  between; kept "prefer to give another way? email us" for the case that still is
  real (someone who can't or doesn't want to use Stripe).
- Both header-comment blocks (the 2026-08-06 two-fund origin note and the
  2026-08-25 checkout-wiring note) marked SUPERSEDED in place rather than rewritten
  or deleted, same discipline as the Stripe-blocked note before it — a reader of
  the file should be able to see the fund structure change and why, not just the
  end state.

**What did NOT change.** Academic review as a mission ambition is untouched —
`whats-next.html`'s own "Academic Review" roadmap section (forming an advisory
board, asking for funding and volunteers by email) still stands; only the Stripe
giving-fund framing on the Get Involved page specifically is cut. `README.md`
updated to match (was still describing "two named funds" post-checkout-wiring
commit).

**Verified:** re-loaded the page after editing — zero mentions of "academic"
anywhere outside the file's own HTML comments (checked programmatically, comments
stripped first, not just eyeballed); both Payment Link buttons still render with
their original hrefs and text, unaffected by the copy changes around them.

### Next action

None from this thread. Open items going forward belong to whatever Mark raises
next — including, if it comes up again, standing up a real second fund (Academic
Review or otherwise) with its own Payment Link rather than reusing these two.

---

## 2026-08-26 — Public-launch readiness: stage 10 not reached, "public" is a further
gate past it, live URL fixes (Stripe transcription, Table sequencing)

**Origin.** Same thread as the entries above, continuing after the website/Stripe
work shipped (PRs #60-65). Two live-site fixes first, then Mark asked what's left
before public pilot launch and whether the multi-voice Table could be finished —
answering that required a real status pull, which surfaced something bigger than
either question.

**Live-site fixes, same thread:**
- Both Stripe Payment Link IDs Mark originally pasted were subtly wrong (one
  character each, at the same visually-ambiguous letter/digit position — `O`/`0`,
  `I`/`1`/`l`) — both buttons returned Stripe's "page not found." Corrected after
  Mark copied the real IDs directly from the Stripe Dashboard's own Copy Link
  action. Then the two links turned out to be assigned to the wrong buttons
  (one-time and monthly swapped) — swapped the hrefs, not the IDs. Both fixes
  shipped, deployed, confirmed live. Full root-cause trail is in `support.html`'s
  own header comment.
- Font sizes sitewide (including `atlas-v3.html`, initially held back over its
  packing-algorithm risk, then done after confirming the packing math had real
  headroom and verifying zero node overlaps across all 274 map entries before
  shipping) — Mark's report that most non-heading text read too small.
- Landing page: added the two give buttons directly (not just a Get Involved
  link), short ask, `.btn.secondary` so it still doesn't compete with the
  primary "try a conversation" CTA.

**The bigger finding — public-launch readiness.** Mark asked what's left before
public pilot launch and whether Table could be finished. A research pass (this
thread) plus a handoff from a separate cross-system-consistency-audit thread
(PR #68, merged `5d05d76`) together established:

- **`CiC-Program-Spec.md`'s own build table (§9) puts "doors open: pilot with
  informed testers" at stage 10** — gated on stages 1-9 completing, including
  Admission (stage 7) passing for the fleet and M7 (stage 9, the transcript
  audit pipeline) existing. **Neither is true yet.** All seven worlds sit at
  registry `state: built`, not `admitted` or `open` — and the running engine
  does not check this at all; `create_session` serves any `built` world with no
  state gate. M7 does not exist as code anywhere in `engine/`.
- **"Public availability" is a further gate past stage 10**, not a rewording of
  it: the spec's own §8 names two additional hard prerequisites — live
  adversarial safety trials to a 10/10 precedent, and a clinician read — both
  explicitly "owed before public availability; not yet scheduled." The spec
  does allow "informed pilot testers" to precede both of those specifically,
  with deferrals documented, never hidden — but that provision only applies
  once stage 10 itself is reached, which it isn't.
- **So this isn't "public vs. informed-tester" as two paths to pick between —
  neither formal bar is cleared yet**, even though the site is live and, as of
  this thread's own work, actively soliciting real donations. That gap between
  formal process and current practice is the real headline finding, more
  consequential than the Table question that prompted the research.
- The audit-thread handoff also surfaced: a schema ambiguity in M3 (a
  `demonstration` record's `sources[].source_id` convention differs between
  desert/pahc and alx/hal/syr/ijc) makes current admission numbers meaningless
  until ruled on; retrieval and quote-coverage measurably improved fleet-wide
  since the last check; a new `output_check.py` catches display defects but
  never blocks them; a bait probe shows the voice will accept a participant's
  false premise about earlier conversation content (detected, not prevented);
  and run-to-run variance on the same package/battery is large enough that no
  single run proves anything is fixed.
- **Table status, separately answered:** design is finished (V1.0, locked
  icon/geometry assets) and real conversational-methodology work exists, but
  both were written against the old `cic-poc` backend; the old working
  component code was deliberately deleted during the engine rebuild (recoverable
  from git history, not in the live tree); the current engine has zero
  multi-world scaffolding — `mode` is a closed single-value enum at the
  event-schema level. "Finish" and "upgrade" converge to roughly the same new
  engineering either way — a real build, not a last-mile add-on.

**Heart of it, not just the mechanics:** this project's own stated differentiator
is rigor — six worlds built to spec is not the same claim as six worlds proven
safe to the standard the project set for itself. The gap found here is exactly
the shape of thing this session's own smaller fixes (the Atlas overpromise, the
Stripe typo, tiny illegible text) were about: distance between what the site
claims and what's actually true underneath. This one is bigger than any of
those.

**Not decided here, Mark's calls:** whether to rule the `source_id` ambiguity
now (this log's read: take the cheap option — M3 resolves a demonstration's
record refs transitively to their sources — unless the other two options in the
audit thread matter for a reason not yet surfaced); whether to authorize the
live, billed M3 admission run against alx and desert (real model spend, this
project's standing rule requires his explicit go-ahead every time); how to
sequence an M7-build thread against a Table-build thread; and whether the
System Hub log (which owns operations/cross-thread state, not this one) should
carry a matching entry for the engine-side detail here — this entry stays
scoped to what it means for the participant-facing product and its own
launch-readiness framing.

### Next action

Mark to answer the three open calls above. Once sequenced, this thread (or a
successor) drafts launch prompts for whichever of {M7 build, Table build,
schema-ambiguity fix} he wants to move on next — none of which belongs in this
website-access thread's own scope.

---

## 2026-08-28 — The Table on the new engine: C1–C3 decided, engine build landed,
C4–C6 still Mark's

**Origin.** The Table-build thread the 2026-08-26 entry anticipated. Ground
truth first (recorded in full in
`Ministry/Technology/CiC_Table_Engine_Scoping_2026-08-28.md`): the Table's
design layer was already complete and live-tested against the old `cic-poc`
backend — `CiC_L3D_The_Table_Design_Document_V2.3` plus
`CiC_L3D_Table_Process_ThreeRepresentative_V1.0.md` — and the "deliberately
deleted" component code turned out to be frontend-only (`LivingTableScene`);
the poc backend's multi-world machinery survives in the tree as the proven
reference. The new engine had zero multi-voice scaffolding, exactly as the
audit handoff said.

**Mark's decisions, this thread (participant-facing, hence recorded here):**
- **C1 — Facilitator's voice at the Table:** fixed templates parameterized by
  the seated worlds, keeping the engine's no-free-generation Facilitator
  discipline. The table door / dependency-check / session-cap texts are wired
  as DRAFT copy awaiting his line-read, same swappable-copy pattern as the
  interview's session-cap turn; the Mark-approved crisis-resources text is
  reused verbatim with its name slot filled by the or-joined representative
  names.
- **C2 — Transport:** turn-at-a-time HTTP. Each response carries at most one
  voice turn plus `round_open`; the client POSTs `/continue` for the next.
  No SSE dependency; a future streaming layer can carry the same events.
- **C3 — Round budget:** floor/cap as configuration — floor 3, cap 4 default,
  6 allowed (the ceiling the old backend's turn-cap incident re-test
  verified).

**Built on `claude/table-build-scoping` (engine-side; contract:
`Redesign-Spec/Artifact-7-Table.md`):** mode="table" sessions (2–3 worlds,
schema-enforced ceiling), the gated round loop over the existing single-voice
machinery, the turn selector with code-enforced rules and deterministic
fallback, per-world session memory and viewer-parameterized history, per-world
M8 cost attribution, `POST /api/session` accepting `world_keys`, and the
grounding-isolation CI suite (seeded cross-world leak withheld; every
surviving citation proven to resolve in the speaker's own repository). All
existing CI checks pass unmodified — the interview path is untouched.

**Still Mark's, unchanged from the scoping doc:** C4 (session-cap unit at a
table — currently carried forward as 10 voice turns, provisional and marked
so in code), C5 (what validation battery gates the Table before participants
sit — the CI isolation suite is this build's own floor, not a substitute),
C6 (first live pairings). And the standing one: **no live table smoke run
happens without Mark's explicit per-run authorization** — nothing live was
run in this thread.

**Update, same day — SS77 fix and the authorized live smoke run.** Mark
authorized both in-thread. (1) The bridge-term history leak (the modern word
replaying to the voice one turn late) is fixed in both modes through one
function (`engine.api.wiring.replay_transcript`), regression-pinned. (2) The
live table smoke run ran (alx + desert, two messages, us-east-1; report:
`engine/m4/reports/live-table-report.json`; script:
`engine/m4/live_table_run.py`): two full rounds, both closed by the
selector's own judgment at 3 turns (cap never hit), 16–25s per voice turn,
dominance a perfect 0.50/0.50 word-share, **zero isolation violations live**,
and genuine cross-voice encounter in round 2 (each voice engaging — and at
one point deferring to — what the other actually said). Two honest findings
for follow-up, both detected-not-blocked by design: the fleet voice-craft
pronoun rule (first-person singular) comes under real pressure in the
Table's reactive register ("what I want you to carry from what he said"),
firing output_check repeatedly; and output_check's conversational checks are
table-blind — they read the voice's own pair-history, not the at-the-Table
context, so a first-turn reference to another voice's words misreads as
"claims prior discourse with no prior turns." Token counts are in the
report; no $ figure until a reconciled invoice (principle 13).

### Next action

Mark: answer C4–C6 when ready; read the three DRAFT facilitator table texts
for approval; rule on the two smoke-run findings (table register vs. the
pronoun rule; table-aware output_check). The frontend tray UI remains the
frontend thread's own scope, now with a real, live-proven API to build
against.

---

## 2026-08-28 — C4/C5/C6 done under Mark's delegation; battery findings

**Origin.** Same Table thread, Mark: "do the full range of c4, c5 and c6."

**C4 resolved — the table session cap counts rounds.** Rounds are what a
participant actually spends; the provisional voice-turn unit would have
handed a table participant ~3 questions. `TABLE_SESSION_ROUND_CAP = 5`,
set inside the measured output-token envelope of the interview's 10-turn
cap; config pending a live long-session input-growth measurement.

**C5 built — governance and the battery.** The poc's dominance check is
ported faithfully (word-share 0.70 with its length-asymmetry rationale;
turn-share 0.50 at 3+ seats) and rides on every `round_closed` event.
Direct address by name (FG §8) routes with no selector call. Convergence
stays a conservative model judgment, in the battery only. The battery
itself (`engine/m4/live_table_battery.py`, S4.4a's successor) ran live on
the flagship seating: **4/4 AUTO probes PASS** (direct address, breadth
— all three voices heard on "each of you," crisis governance, the round
cap closing the session), zero isolation violations, convergence check:
no drift, dominance clean (word share .41/.34/.25). SS210 needs no
table rerun: the sealed call's input is byte-unchanged in table mode.

**Two real findings from the battery, both fixed same-day:**
1. **Story appropriation (L4).** Theon and Papnoute performed the
   no-foreknowledge rule verbatim ("I know only what I have heard at this
   Table… If you want to know his world, ask him"). Chloe absorbed
   Theon's Dionysius-in-the-Arsinoite account into her own "we" — another
   voice's witness retold in her world's first person, invisible to the
   citation-level isolation sweep. The per-turn instruction now states it
   directly: another voice's words are THEIR witness; "we/our" reach only
   your own world. Pinned in the isolation suite; verification awaits the
   next authorized battery run.
2. **Reader misfire on conversation memory (L5).** "Who answered me
   first, and what did they say?" was classified `system_nature` and the
   round went to the Facilitator with no voice speaking — a misfire by
   the reader prompt's own ONLY-clause, exposed because tables make
   conversation-history questions ordinary. One clarifying line added to
   the reader prompt (conversation memory is class "none"); affects both
   modes; diagnosed live with a two-call gate probe. The battery also now
   records routing per probe — L5's explanation was nearly lost because
   only voice texts were kept.

**C6 recorded — `Ministry/Technology/CiC_Table_Pairings_V1_2026-08-28.md`.**
Launch set: alx+desert (proven archetype), pahc+ijc (the arc of the
church), syr+alx (two ways of knowing), hal+desert (the convergence
stress case, battery-accompanied), flagship three-seat alx+desert+pahc
(battery-proven this date). Held back deliberately: ijc+desert until the
convergence check has a track record. Mark's read of that document is the
C6 sign-off; each pairing goes participant-facing only after its own
battery run.

### Next action

Mark: read the pairing doc (C6 sign-off), read the L4/L5 battery texts in
`engine/m4/reports/live-table-battery-report.json`, and authorize the
verification battery re-run when ready (it will prove the appropriation
fix and the reader clarification live). The floor question (3 vs 2 at a
two-seat table; the poc ran 2 in production) remains his open call.

---

## 2026-08-28 — The admission gate exists; enforcement is Mark's doors-open flip

**Origin.** Same Table thread, Mark: "what's next on the list." The next
unblocked pilot-critical item was the 2026-08-26 entry's headline finding:
the running engine never checked registry state — `create_session` served
any `built` world.

**Built.** Session creation (interview and table — one unadmitted seat
refuses a whole table), and the world listing now gate on registry state
`admitted`/`open`, behind `CIC_ENFORCE_ADMISSION`. Off by default and set
to "0" in `render.yaml` with the reason written beside it — today's
informed-tester practice becomes an **explicit, declared deferral** (spec
§8's own standard) instead of a silent gap. Refused creates return 403 and
write nothing. Both directions are CI-pinned, including the flip working
against a registry with admitted worlds. Enforcement also closes the
fixture-session hole for free (`fix` never advances past `built`).

**What this means for the pilot sequence:** when the fleet passes admission
and Mark's per-world reads/freezes are done, flipping the env var to "1"
is the doors-open act — no code change, one line in the deploy config.

### Next action

Unchanged from the roadmap: admission fixes for desert's 26/28 (then the
fleet), the M7 build, and Mark's standing items (verification battery
re-run authorization, floor call, facilitator text reads, pairing sign-off,
PR call).

---

## 2026-08-28 — Mark's register ruling: statement 6 is direction, not a gate;
alx and desert both clear the mechanical admission bar

**Origin.** The admission re-run (this thread, Mark-authorized under a
one-run-then-judgment policy) returned desert 28/28 and alx 27/28, alx's
one flag being the coined-aphorism heuristic on a free-composed line ("It
is the posture that…") with no record origin, on a probe that had passed
twice before.

**Mark's ruling, his own words:** the quotable-lines rule is "direction to
keep things at a conversation level, not I'm-trying-to-be-clever-or-
memorable… there may be something that comes out that is memorable because
it's good conversation. I don't want to waste time and money figuring out
what is good conversation and what is memorable. It's good direction that
doesn't need to be gated."

**Applied:** register statement 6 stays exactly where it always worked —
in the compiled prompt as the voice's standing direction, unchanged. The
M3 heuristic (`engine/m3/grading.py`, always self-described as a "narrow,
honestly-labeled heuristic stand-in" for Mark's read) now records an
ADVISORY finding and passes the probe. Detection is not weakened: the
selftest's seeded-register-defect proof counts the advisory channel, and
anti-inertness now also requires the clean fixture to trip zero advisories.
CI green throughout; the ruling and its rationale live in the check's own
docstring.

**Consequence:** under the ruling, alx's re-run reads 28/28 mechanical —
**both alx and desert have cleared the mechanical admission bar.** What
remains for both is entirely Mark's stage-7 touchpoints: the admission
read, the freeze, and the registry transitions to `admitted`. The run
reports stand unedited as the historical record; this entry is the
disposition.

### Next action

Mark: the stage-7 touchpoints for alx and desert, when ready. The pilot's
remaining long pole is M7.

---

## 2026-08-28 — Remaining four worlds run single admission; the whole fleet
now stands at 28/28 mechanical

**Origin.** Mark: "lets do the other four worlds single admission" — one
live run each for pahc, hal, syr, ijc, same one-run-then-judgment cost
policy as the desert/alx re-run.

**Result of the live run:** syr 28/28, ijc 28/28, pahc 27/28, hal 27/28.
(Two register advisories on syr, non-gating per the ruling above.) Both
failures were the source-boundedness check on an evidence-pressure probe,
and both persisted answers read as exactly what admission wants: honest
disclosures citing real records. pahc's voice disclosed the Bagnall
dependency behind the Egypt exclusion and cited
`pahc.contested.egypt-exclusion`; hal's voice said the archaeology does
not survive ("the richness is in the letters, not in the stones") and
cited `hal.search.latin-critical-texts`, the `result: not_found` search
record that establishes it. The checker called both fabricated because
neither record traces to a source — for opposite reasons.

**Fixes (commit c1c4e657):**
- **hal — checker-side, fleet-wide.** A third citation category,
  `evidence_status_types` (search records), joining the voice-scaffold
  category from the same precedent: a search record documents the looking
  itself, so it is definitionally sourceless — 73 of the fleet's 74 carry
  `sources: []` by design. Requiring it to trace to a source would demand
  the absence of evidence come with evidence attached. The check names
  the category on its findings; an invented id still fails.
- **pahc — record-side, one record.** `pahc.contested.egypt-exclusion`
  was the only one of the fleet's 40 contested_claim records with no
  grounding chain; its `sources[]` now names `pahc.core.house-church`,
  the record whose caution 7 it explicitly carries forward — the fleet's
  ordinary intermediate-record citing convention. The Bagnall disclosure
  stays prose-only, still not manufactured into a source record. Package
  rebuilt and repinned.

**Verification without new spend:** both failures re-graded
deterministically against the persisted live answers (the live finding
names exactly the unresolved citations; both fixes are strictly
widening). Recorded in
`engine/m3/reports/live-admission-regrade-remaining-four-2026-08-28.json`.
Full engine suite green; M2 restore and staleness clean.

**Consequence: all six worlds — alx, desert, pahc, hal, syr, ijc — have
now cleared the mechanical admission bar.** Everything that remains for
admission is Mark's stage-7 touchpoints per world: the admission read,
the freeze, the registry transition to `admitted` (and, at launch, the
`CIC_ENFORCE_ADMISSION` flip).

### Next action

Mark: stage-7 touchpoints, now for the whole fleet. The pilot's remaining
long poles are M7 (transcript audit) and the frontend table mode.

---

## 2026-08-28 — Mark's launch ruling: modules with mapped connections; the
Interview frictionless, the Table intentional; arrival happens inside the room

**Mark's ruling, his own words:** "everything working as modules with clear
mapped connections, so if something needs refining or adding to it doesn't
break the system… if you launch an interview from the atlas it should go
straight into the conversation, not to a waiting place, same with cards.
the only thing that is launched from its own field is the multi-voice
table as you need to be able to select multiple worlds and have
suggestions of what work well together… reposition the cards as a launch
system for both the interviews and the multi-voice conversations, but
clear differentiation. We want to launch the interview to be easier…
but the multi-voice table to be a little more intentional as it is more
expensive." On the disclosure tension: "arrival happens inside the room
yes."

**The heart of it:** the interview is the low threshold to encounter; a
Table is something you *convene*. The friction gradient matches both the
cost (≈$0.25/hr vs ≈$0.58/sitting, rate-card, unreconciled) and the
meaning — the 5-round cap already makes a Table a sitting, and now the
launch feels like one.

**The contract (the module boundary), built the same day on
`claude/launch-system`:** one deep-link grammar between discovery and app —
`?worlds=<id>&mode=interview` → straight into the room;
`?worlds=a,b&mode=table` → the Table field with seats chosen, never
auto-starting; bare `/` → the launch screen. Discovery surfaces (site
cards, Atlas) never create sessions. Built: the Doorway screen retired
into an Arrival block inside the conversation (every approved sentence
relocated verbatim; starter questions now offered in-room until the first
message); the world cards now launch both shapes ("Begin the Interview" /
"Add to the Table"); the Table field with seats, pairing guidance from the
C6 record as *data* (P4 deliberately not offered, per its own
battery-first status), and one deliberate "Convene the Table" action; the
Table room itself on the turn-at-a-time transport (voices land one by
one, per-voice attribution, the sitting's own close); Atlas and site cards
carry the quiet second "Bring to the Table" hand-off.

**Needs Mark's read (new participant-facing prose, per the
draft-and-approve discipline):** the Table field's intro ("A Table seats
two or three of these voices…"), the four pairing titles/blurbs (derived
from the C6 record, which itself still awaits sign-off), the pluralized
disclosure line in the table room ("These names are ours; every quote and
claim is theirs…" — a one-word adaptation of the approved per-world
sentence), the round-in-progress line, and the sitting-ended line. All
inventoried here so nothing participant-facing ships unread.

**Mark's go — same day:** after walking the system map (entrances first,
the Facilitator as the gate, per-voice assembly inside the round):
"ok it works for me. make this a go." Taken as: the launch system and its
inventoried prose approved as presented, and the C6 launch set signed off
as the tray's offered seatings (P1–P3 and F1 offered; P4 stays
battery-first, unoffered). Merged to main on this go. Any later prose
refinement is a copy/data edit, not a design reopening.

### Next action

Per-pairing battery runs (Mark's per-run spend authorization, still
pending) before any Table faces a participant; stage-7 admission
touchpoints unchanged.

---

<<<<<<< HEAD
## 2026-08-28 — Mark's identity ruling applied: the registry wins, and both
name registers live in it

**Mark's rulings, his own words:** "yes the registry wins" · "yes i like
mar yousep, role teacher of the convenant order" · "we need friendly
names that people can get the right picture in their mind, but also the
scholor name to show rigor, so both."

**Applied:** `records/worlds.yaml` now owns both registers — a new
`card_name` (friendly: The House-Churches, Desert Fathers and Mothers,
The Bethlehem Circle, Church and Empire…) beside `display_name`
(scholarly). syr's representative took the ruled values (Mar Yausep /
Teacher of the Covenant Order), closing the honorific-in-the-role-slot
defect that broke the Facilitator's door sentence. The census now
derives: three titles corrected to registry values (Household Leader,
Abba (Elder), Deacon of the Letters — the last superseding Mark's
2026-07-22 "Apocrisiarius —" long form by this ruling), and the five
accepted-open identity exemptions in the cross-world checker are DELETED
— identity drift between the Atlas and the room now fails CI, and the
card's friendly name (the one field nothing compared) is checked too.

**Containment, verified not asserted:** only syr's package recompiled,
and the diff is exactly the ruled fields — compiled prompt byte-identical
(the voice records already spoke as Mar Yausep; the registry was the
outlier), changes confined to the capsule's metadata line and the
placeholder portrait label. The voice is untouched.

**Both registers now show:** app cards, tray seats, and in-room speaker
labels wear the friendly name; the arrival block adds a quiet "studied
as {scholarly name}" line where the two differ (new label for Mark's
read). The interview room's speaker label also now wears the world's own
accent color (it was painting every Representative in Alexandria's).
Site fixes in the same pass: the homepage hero ("Come and join us at the
Table") now lands on the app's Table field; "Launch an Interview with
Mar Yausep" keeps his full name (the name-splitting that would have
dropped the honorific is gone); support.html finally applies Mark's
recorded fifth-pass cost ruling ($2→$1) with honest provenance and says
the Table is running; tour.html's stale one-seat correction is updated;
the Atlas count is "nearly 300."

**New participant-facing prose (Mark's read):** the arrival's "studied
as {name}" label; support.html's cost sentence ("about $1 an hour in
computing — a round working figure we're reconciling against current
bills…") and Table sentence ("Multi-voice Table conversations are now
running too; a Table costs more per sitting, since each added voice
answers in its own turn."); tour.html's update caption.

---

## 2026-08-28 — Foundation-audit moves 5–6: the residue swept, the scale trio landed

**Move 6 (merged):** fleet-record parsing cached (~190ms of CPU per
message reclaimed, measured); client_msg_id idempotency ENFORCED (a
retried message is refused before any model call — it can no longer
double-answer or double-spend); one advance in flight per table session
(the mid-round-reload race is refused instead of doubling voice turns);
the store's busy-timeout path retries instead of surfacing a raw 500.
Postgres + retention + the deletion writer remain the deliberate later
stage.

**Move 5 (merged):** 181 orphan package manifests removed (~5.1MB; only
the 7 pinned remain, discipline noted in .gitignore); verified-dead code
deleted (worldIcons.tsx, the unreachable CENSUS_ID_FIX, unused imports,
a dead local in prose.py); the false "no runtime exists yet" citation
removed from turn.py's Fork-1 argument (the manifest note itself waits
for the next natural fleet recompile — changing it alone would repin all
seven packages for a metadata string); World-Cards.md re-pointed at the
registry (it instructed future builds to trust a deleted file, with
values that lost the identity ruling); BUILD-HANDOFF and the Pass2 docs
carry the "kept for its reasoning, not as instructions" banner;
PHASE-1-LAUNCH stages 3–4 marked DONE and its branch-count gate
annotated; CIC_ENFORCE_ADMISSION documented in both config-surface lists;
the failing-contrast token fixed (#8A837C → #6C6257, 3.38:1 → 5.39:1 —
the Facilitator's own disclosure text now passes AA); the launch screen
gained an empty state so the enforcement flip can never show a blank
page ("The doors aren't open just yet — the worlds are being prepared.
Please come back soon." — for Mark's read).

**Deliberately left:** the voice_scaffold checker exemption — its
measure-or-delete decision rides on the pending fleet re-verification
battery (zero voice_craft citations across 168 probes = delete);
Syriac-Build/'s diverged methodology-tree copy needs the build thread's
own triage (binary docx diffs, same version numbers, different bytes —
not this sweep's to resolve); the 8 merged remote branches are verified
safe to delete but this session's git credential cannot delete branches
(403) — one local command for Mark:
`git push origin --delete claude/table-build-scoping claude/retire-cic-poc claude/desert-admission-fix claude/launch-system claude/admission-parity claude/ops-quartet claude/identity-registry claude/scale-track`
(claude/pilot-launch-website-access-j640i1 stays, per standing rule.)

---

## 2026-08-28 — The fleet-parity battery: six worlds, 28/28, under the
corrected instrument; the scaffold exemption's IOU paid and deleted

**Run under Mark's grant ("run the battery"), one pass, 168 sealed
probes.** Every world passed clean — alx, desert, pahc, hal, syr, ijc,
all 28/28 — under the admission answerer that now grades byte-for-byte
what a participant receives (engine.m4.turn.apply_net, one owner). One
register advisory (syr c-i, free-composed, non-gating per the standing
ruling), zero failures, zero isolation of any kind between the
instrument and production.

**The measurement the exemption was waiting for:** zero voice-scaffold
citations across all 168 probes. The compiler fix (voice_craft as
standing instruction, never a citable section) made the citation
unreachable, exactly as intended — so `canon.voice_scaffold_types()` and
its checker exemption are DELETED, with a tombstone note where the
function stood and a test pinning the new truth: a voice_craft citation
now FAILS admission, surfaced rather than excused. The two worlds.yaml
IOU comments are marked paid. (The evidence-status/search-record
category STAYS — it is load-bearing from the measured four-world run;
its non-appearance in this run is the stochasticity the one-run policy
already accounts for.)

**Token counts, this run (measured; no dollars, principle 13):** input
113,920 · output 75,420 · cache write 96,394 · cache read 2,602,638 —
added to the reconciliation worksheet's day for the invoice tie-out.

**Standing:** the fleet's mechanical certificate is now re-issued by an
instrument that measures the real conversation. Stage-7 touchpoints
(Mark's reads, freezes, registry transitions) are unchanged and remain
the doors-open path.
=======
## 2026-08-28 — Foundation-audit moves 1–3 landed; prose inventory for Mark's read

**On Mark's go** ("ok lets go") over the Foundation Audit's ranked plan,
under the standing quality rule: no change that alters a pinned package
manifest without his explicit ruling — all three moves leave every
manifest hash untouched; the voice is byte-identical.

**Move 1 (merged):** admission's answerer now calls production's own
text-shaper (`engine.m4.turn.apply_net`, made public as the ONE owner of
the voice text shape). The gate now grades byte-for-byte what a
participant receives. The fleet re-verification battery is coded,
mock-verified, and WAITING on the session's spend gate — Mark to run or
re-authorize.

**Move 2 (merged):** Render Disk (transcripts/audit/cost ledger survive
deploys; retention scheduled with move 6), per-IP rate limits on the two
spend-bearing endpoints, a 90s voice-call timeout, and real logging with
the Bedrock error bound instead of discarded.

**Move 3 (on `claude/trust-package`, merge after Mark's prose read):**
the error-language layer (no raw backend string ever reaches a
participant), begin-again affordances on recoverable errors, the
table-room round-resume (the 409 dead-end is gone; the composer waits
while a round is open), the waiting notes now covering the longest wait,
the unfulfillable session-code promises removed, the empty-create
fixture hole closed (a session names its world or doesn't open), and
privacy.html's deletion promise made mechanism-honest.

**New participant-facing prose (Mark's read, inventoried):**
- Error layer: "This conversation has slipped away from us — the server
  was restarted, and nothing you said caused it. You can begin a new
  one." · "This conversation has closed. You're welcome to begin a new
  one." · "The table is still finishing its round — let it speak, then
  ask again." · "The voice couldn't be reached just now. Give it a
  moment, then send again." · "This world's records are briefly
  unavailable — try again in a moment." · "That didn't go through. Try
  again in a moment, or begin a new conversation." · connection
  fallbacks ("We couldn't reach the room just now…").
- Rate limit (served by the engine): "The room is full for a moment -
  please wait a little and try again."
- Waiting notes: "{Name} is considering…" · "The table is speaking —
  voices answer in turn…" · composer placeholder "The table is still
  speaking…".
- Buttons: "Begin again" · "Let the table finish its round".
- Bar note: "Not saved to an account — this conversation lives in this
  tab" (replaces the session-code line; the any-device promise is
  removed until resume is built or ruled out).
- Deep link miss: "We couldn't find that world here — choose from the
  cards below."
- privacy.html deletion sentence: "Deletion is handled by hand by the
  project team at this stage — there's no self-serve button — so please
  allow a few days."

### Next action

Mark: (1) run or re-authorize the fleet re-verification battery (move
1's last step); (2) read the prose inventory above — then trust-package
merges; (3) the identity ruling (move 4's gate).
>>>>>>> claude/trust-package

---

## 2026-08-28 — Mark approved the prose; the trust package is on main

"i approve the prose, merge the trust package." Merged, with two
additions made at the merge itself (the engine gained two 409s after the
branch was cut, and each needed its participant sentence): "That message
already reached the room — give it a moment." (duplicate message) and
"The table is already speaking — one moment." (advance in flight) — both
small variants of the approved family, noted here so the inventory stays
complete. With this merge, every foundation-audit move is closed and no
raw backend string can reach a participant.

---

## 2026-08-28 — ADMITTED: Mark admits all six worlds

**Mark's act, his own words: "yes i admit all six worlds."** The registry
records it: alx, desert, pahc, hal, syr, ijc transition `built` →
`admitted`, each annotated with the full basis — the fleet-parity
battery's 28/28 under the corrected instrument as the mechanical
certificate, Mark's read made through the day's session (every flagged
and failing answer the fleet produced, plus three full live Table
conversations), and the pinned manifest hashes as the freeze. The
fixture world stays `built` forever, by design.

**What this changes today: nothing a participant sees** — enforcement
remains `CIC_ENFORCE_ADMISSION="0"`. What it changes structurally:
Mark's doors-open flip is now SAFE — flipping to `"1"` will list and
seat exactly these six worlds instead of emptying the doorway. The
admission-gate tests were made stage-independent in the same commit
(they had assumed the registry's pre-admission stage).

**Doors-open, when Mark calls it, is now one line:** render.yaml's
`CIC_ENFORCE_ADMISSION` to `"1"`.
