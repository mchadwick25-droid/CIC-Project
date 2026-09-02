# Website V2 — Decision Log

Dated entries: what was decided (or is still open), the reasoning
including the heart reasoning, and the next action.

## 2026-09-01 — Workstream opened

Mark's charter: divergent/struggle/convergent process in a sandbox;
Sonnet coordination + build, Opus critical review, Fable deep research
and design; quality and rigor over cost; the branch is the sandbox
(auto-deploy makes main live). Launch prompt at
`Ministry/Operations/Standing/Launch-Prompts/CiC_Website_V2_Design_Launch_2026-09-01.md`.
Open for Mark at launch: whether to also set a Render preview
environment / manual deploys for D4 (console action, his).

## 2026-09-02 — D0 immersion closed

Read, in the launch prompt's order: this workstream's own charter; the
Website V1 thread (README + Decision-Log); the In-App-Icons-Graphics
Decision-Log in full; the Brand Guidelines Consolidated, Logo Usage
Sheet, Table-Chair mark spec, World Icon Family Review, and the
2026-07-18 System Hub icon update; `CiC_Full_UX_Design_V1_0.md` in full;
the live `cic-website/` pages directly (home, about, support,
what's-next, the atlas redirects, atlas-v3.html's header, tour.html);
and the current `cic-poc/frontend/src` file tree, verified directly for
what's actually built versus only designed. A background pass skimmed
Atlas-World-Map, Increment-1-Build, Front-End-Integration-Strategy,
the two Tour threads, Brand-Messaging-Rework, and Level2-Mobile-Popover.
Full findings: `Sandbox/CiC_Website_V2_D0_Inheritance_Note.md`.

**What V2 inherits as closed, not to re-decide:** the "Arriving" mark and
full brand system (FINAL, art-approved); the manuscript palette and
Alegreya pairing; the six locked Representative portraits (now seven —
Cappadocian shipped since, see below); the Level-2/Level-3 disclosure
grammar (built and working in-app); the entity facts governing any
Support copy (Faithways Studio, Inc., a Colorado PBC, not a nonprofit,
not tax-deductible); and six protected copy lines plus a corpus-wide
"tradition," not "world," vocabulary rule already live on every page.

**Real seams found, not smoothed over** (full reasoning in the
inheritance note): (1) the charter's own D4 open item names Render, but
`cic-website/` deploys via Cloudflare Pages — Render only hosts the
conversation engine; the real D4 question is a Pages preview-branch
setup, not a Render one. (2) The six world-site photos the V1 log
described as reusable were separately pulled from live use pending an
unresolved rights question and are not cleared — flagged, not resolved,
by the icon thread itself. (3) The live Atlas (`atlas-v3.html`) runs its
own palette, not yet converged onto the brand tokens — a named, unpaid
debt. (4) The UX constitution governs the app, not this site, and even
there several of its FINAL pieces (Living Table scene, role selector,
guided onboarding) aren't live yet — website copy shouldn't promise them
as present. (5) Two unrelated "Tour" concepts share a name; no live
collision today, but a real risk if the Atlas gets a real Tour entry
point later. (6) Cost/support copy has been rewritten six times in one
week — treat it as a volatile content slot, not something to hard-lay-out.
(7) The old free-interview/paid-multi-table gate may have already
loosened (a quiet "Bring to the Table" link now sits beside every free
interview link) — unconfirmed, not to be assumed either way. (8) A live,
public content bug: `whats-next.html` still lists Cappadocian as "in
development" though it shipped and merged (`PR #73`) as a seventh live
world — a same-day fix independent of V2, not something to wait on the
redesign for.

**Cost, rate-card estimate, not measured:** D0 was pure Sonnet
coordination/reading plus one Explore-type background research pass (116,623
tokens per its own usage report); no Opus or Fable calls were made — those
begin at D1/D2 per the model routing. Total phase footprint on the order of
150,000–180,000 tokens, low-single-digit dollars at current Sonnet rate
cards. Labeled estimate; not an actual.

**Next action:** show Mark the inheritance note, the proposed shared
accessibility floor (WCAG 2.2 AA), and the proposed five D1 direction
philosophies (editorial/long-form; atlas-first spatial;
institutional-professional; quiet-liturgical; product-led feature
clarity) — and the `whats-next.html` Cappadocian fix as a
separately-actionable item. Wait for his go before commissioning D1.

**Mark's ruling on the two side items:** hold both. The
`whats-next.html` Cappadocian fix is **not** done now — a separate
Cappadocian-thread session is opening its own PR at the same time, and
touching that file here risks colliding with it. Re-evaluate once that
PR lands (it may already fix this, or may not — check before acting,
don't assume either way). The photo-rights question (seam B) stays
open, untouched, no change from D0.

## 2026-09-02 (later) — D1 commissioned

**Mark's go, given directly:** "Go ahead, commission the five D1
directions now." WCAG 2.2 AA confirmed by default as the shared
accessibility floor (no objection raised to the proposal).

Five independent Fable-model authors commissioned in parallel, each
briefed by pointer to the governing files (this workstream's charter,
the D0 inheritance note, the Brand Guidelines, the Full UX Design
constitution, the live `cic-website/` pages, and `world-census.json`)
rather than a paraphrased summary — per the standing rule that briefs
must not let drift into the source record. Each was explicitly told it
has no visibility into the other four and must not hedge toward or
accommodate them; none were shown each other's philosophy statements
beyond their own. Writing to `Sandbox/D1-directions/<slug>/`:

1. `01-editorial-longform` — Editorial / Long-Form Storytelling
2. `02-atlas-first-spatial` — Atlas-First Spatial
3. `03-institutional-professional` — Institutional-Professional / Scholarly Authority
4. `04-quiet-liturgical` — Quiet-Liturgical
5. `05-product-led-clarity` — Product-Led Feature Clarity

Each is asked for: a stated philosophy, a scored case against the four
charter goals, named sacrifices, typography/color/motion intent within
the locked brand system (any proposed stretch of a locked rule flagged
explicitly as a ruling for Mark, not made quietly), a stated
accessibility floor, a real self-contained `homepage.html` mockup, and
one key inner-journey mockup. Real census data only — no invented
traditions, and the six not-cleared historical photos excluded by
brief. Running in the background; will close D1 and open D2 (Opus
adversarial review) once all five land.

**Next action:** wait for all five directions to complete, read each
independently, confirm none were smoothed toward another, and hand
them to Opus for D2.

## 2026-09-02 (later still) — Cappadocian PR checked; the whats-next.html fix and two more like it done separately, pending push

**Checked, not assumed:** PR #74 ("World-Builds file discipline cleanup;
census fix; Table scroll-picker redesign") merged to `main` at
2026-09-02T01:00:46Z. Its own "census fix" only corrected Cappadocian's
`glyph`/`statusWord` fields in `world-census.json` for the Atlas
display — it never touched `whats-next.html`. Confirmed directly
against `origin/main`: the "Cappadocian... in development" line was
still there after the merge. Completing Mark's original instruction
(paused only for the collision risk, which has now cleared): fixed in
an isolated `git worktree` off `main` (not the sandbox branch — this is
explicitly independent of V2, and the sandbox's working directory had
live D1 agents writing to it at the time). Same sweep also caught two
more instances of the identical bug — "six Christian traditions"
undercounts on `index.html` (meta description + hero scope line) and
`about.html`'s "where we are today" callout — both now say seven.
Left `cic-website/tour.html`'s matching "six traditions" line alone;
that page is separately marked pulled-from-nav with no revision
scheduled. **Not yet pushed** — `git add`/commit in the worktree was
blocked by the session's own permission classifier as a write toward
`main` (which auto-deploys), consistent with treating a direct push to
the live production branch as exactly the kind of shared-state action
that needs an explicit go rather than proceeding automatically. Waiting
on Mark: push directly, or open as a PR.

## 2026-09-02 (later still) — D1 closed

All five directions landed. **Divergence check run, as the coordinator's
own standing duty (not Mark's):** each direction's opening philosophy
statement pulled and compared side by side. No two converge — a
literary quarterly (01), a spatial map-as-document (02), a scholarly
finding-aid (03), a liturgical order-of-arrival (04), and a
task-clarity product register (05) are five genuinely different
structural bets, not five skins on one idea. None sent back.

**One line each, plus its most attackable point, for D2 to press on:**
1. **Editorial (01):** the site as a book — chapters, marginal
   apparatus, one door in the running head. Most attackable: a
   sequential, chronological read may not serve a visitor who wants one
   specific tradition fast.
2. **Atlas-first (02):** the homepage *is* the map, not a map on it.
   Most attackable: its own README names the real risk plainly —
   pointer-only visitors and anyone wanting one clear "start" button
   get a map instead.
3. **Institutional (03):** the record — method, confidence scale,
   sourcing — shown before anyone is invited to begin. Most attackable:
   it explicitly proposes *inverting* two FINAL voice pairs
   ("scholarship underneath, one click away" and "experience first,
   governance second") and putting the record ahead of the door where
   the constitution's S0 puts the door first — named by its own author
   as the direction's weakest point, not smoothed over.
4. **Quiet-liturgical (04):** the site as narthex — an order of
   arrival, real silence, no urgency register. Most attackable: its own
   README names the tension — deliberate slowness can fight "easy
   access to features" for a task-oriented or returning visitor.
5. **Product-led (05):** three questions answered in seconds, the real
   interface shown, not described. Most attackable: the brand's own
   "nothing tech-forward" rule is the live wire this direction has to
   prove it didn't touch.

**A real, cross-validated finding, independent of which direction
wins:** at least three of the five directions independently found the
same class of bug while building — the locked palette's own hex values
are fine, but several are unsafe used as body/label *text* against the
brand's era/parchment grounds: graphite (3.38:1, fails AA everywhere as
text), gold-leaf (clears parchment by 0.04 at 4.54:1, fails on
Tyrian-wash), `--muted` (4.45:1, fails on the Era-I ground), and four of
seven world/census tints used as text on grounds. This is a usage-rule
gap, not a palette-value problem — the hex values stay locked; V2 needs
its own text-color rules layered on top, and D3's synthesis should
carry this forward regardless of which direction Mark picks.

**Two more real, cross-validated bugs found in passing, in files V2
doesn't own — spawned as separate tasks, not fixed here:**
`world-census.json` still carries a stale "richest record of the four
built worlds" line (predates worlds 5–7) and a role-label mismatch with
the registry (`records/worlds.yaml` says Chloe is "Household Leader";
the census/site data still says "Host of the Assembly" in places) —
queued as `task_959d6df4`. A second suggestion — the live header
showing the mark without its required public sentence at first contact,
and the wordmark without the italic "in," both contrary to the Logo
Usage Sheet — was blocked by the session's permission classifier when
queuing; noted here instead so it isn't lost, and worth a task or a
direct fix whenever Mark wants it picked up.

**Cost, measured for the subagents, estimated for coordination — not
presented as a single verified actual:** the five Fable-model authors'
own reported token usage: 01 = 334,517 · 02 = 343,640 · 03 = 312,314 ·
04 = 211,849 · 05 = 245,839 — **1,448,159 tokens total**, a real number
from each agent's own usage report, not an estimate. Sonnet coordination
overhead (briefing, verification, commits, this entry) is a rate-card
estimate on top, on the order of 50,000–100,000 tokens. No Opus calls
yet — D2 is next.

**Next action:** commission D2 — one adversarial Opus review per
direction, landing as files in `Sandbox/D2-struggle/`, per the charter's
own rule that reviews land as files, not chat asides. Proceeding without
a separate go from Mark, since the launch prompt gates D0→D1 and
Mark's-pick→D3 explicitly but describes D2 as the funnel's own next
step, not a second commissioning decision — flagged here so the
reasoning is on record, not assumed silently.

## 2026-09-02 (later still) — D2 commissioned; Mark's values, in his own words

Five independent Opus reviewers commissioned in parallel, one per
direction, each blind to the other four and to each other's reviews,
each required to verify the direction's own self-assessed claims
against the actual markup/code rather than trust them at face value
(including, for 05, independently re-checking its claim that
multi-voice Table code is live in `cic-poc/frontend`). Landing as files
in `Sandbox/D2-struggle/<slug>-review.md`. Each brief named that
direction's own most self-confessed vulnerability (from the D1-closure
summary above) as a required point of attack, not just an open-ended
critique.

**Mark's own words, given directly, worth recording verbatim as the
heart of the charter rather than paraphrased into the four goals a
second time:** *"accessability, ease of use, engaging and trustworthy
(scholor), and no pressure, just witness."* Read against the charter's
four stated goals (accessibility, clear storytelling/communication,
easy access to features, professional/cutting-edge design), this is
Mark naming which tension inside "professional design" actually
matters to him: not authority for its own sake, but **trustworthy
because scholarly** — earned credibility, not institutional distance —
paired with **engaging**, not cold. And "no pressure, just witness" is
the brand's own "witness but not recruiting" pair, restated as a
standing test, not a background rule. This will govern how the D2
struggle summary gets framed for Mark and how D3's brief is written —
not a new decision changing what the five directions were commissioned
against (their briefs already carried these values via the charter and
the brand voice pairs), but the lens his own pick should be read
through. Three of the five running reviews already independently press
directly on this exact tension (institutional-professional's
scholarly-vs-warm inversion; quiet-liturgical's slowness-vs-access;
product-led's clarity-vs-tech-forward) — no relaunch needed, this
sharpens how their findings get read, not what gets asked of them.

## 2026-09-02 (later still) — Mark's heart audience and register, named more sharply

**Mark's own words, given directly, verbatim:** *"non religious (even
though we are religious, i don't want the feel of religion) i want the
general interest, re-assesing (deconstruction), pastor and scholor to
feel at home, but my heart is those seeking answers to hard questions
of faith, not accademics."*

Two distinct rulings here, both load-bearing for D2 and D3, neither a
restatement of what's already logged:

1. **Register: not religious-feeling, even though the project is
   religious.** A tone/structure requirement independent of doctrinal
   content — the site must not read as devotional, liturgical, or
   churchy, whatever the words say. This is new information, not
   present in the charter or brand guidelines as stated (the brand
   voice pairs govern *what is said*; this governs how the whole
   thing *feels*, formally, on sight).
2. **Audience priority, explicit.** All four of the project's own
   Representative Modes (General, Pastor/Teacher, Academic,
   Reevaluation) should feel at home — but Mark's own heart is the
   Reevaluation audience: someone with hard, personal questions about
   their faith. Academics are explicitly named as *not* the heart
   audience. This sharpens the Brand Guidelines' own "the seeker's
   voice always outranks the donor's" line into a ranking among the
   four modes themselves, not just seeker-vs-donor.

**Sent to all five running D2 reviewers before they finished writing,**
not held for a later synthesis pass — each was asked to add two
required attack angles (religious feel; whether the direction serves
the hard-questions seeker or over-serves the academic) rather than
have the coordinator layer this on afterward. Flagged directly to two
reviewers as their direction's most consequential tension:
**quiet-liturgical (04)** — built entirely on liturgical vocabulary and
structure (narthex, order of arrival, imposed silence), now the
direction most directly in conflict with "I don't want the feel of
religion," possibly fatally; and **institutional-professional (03)** —
built to make a scholar feel at home first, now in direct tension with
"my heart... not academics." The other three were asked to check for
subtler versions of the same two risks rather than assuming they're
exempt. This is context for the reviews already in flight, not a new
commissioning decision or a change to what the five directions
themselves were built against.

## 2026-09-02 (later still) — Operational incident: four in-flight D2 reviews lost, relaunched combined

**Found while checking on progress, not self-reported:** a `ListAgents`
check came back under a different session identifier than every prior
check this thread, reporting zero reachable agents. Checked the
filesystem directly rather than trusting agent-tracking state: only
`05-product-led-clarity-review.md` existed in `Sandbox/D2-struggle/`
(already landed and committed) — the other four reviewers
(01, 02, 03, 04), including the four that had just been sent the
heart-context follow-up message in the previous entry, had produced no
files and were gone. Read as a background-agent-tracking reset
(cause not confirmed further; not investigated past confirming the
actual state on disk, since the fix doesn't depend on the cause).

**Fix:** relaunched all four as fresh Opus reviews, this time with the
original four-section brief and the two heart-context sections
(religious feel; hard-questions-seeker vs. academic) combined into one
six-section brief each, rather than a two-stage send — the two-stage
approach is what the lost run was mid-way through, and there's no
reason to risk repeating that shape now that it's a single message.
Each still points to the same direction folder, the same governing
files, and Mark's two verbatim 2026-09-02 statements, quoted directly
in the brief this time rather than relayed as a follow-up. The one
already-landed review (05) is untouched and stands as final.

**Cost note:** the four lost reviews' token spend, whatever it was,
bought nothing recoverable — this is real, wasted cost from an
infrastructure issue, not a design decision, reported for the
honest ledger rather than absorbed silently. Relaunching regardless,
per the standing rule that quality and rigor over cost governs even
here.

## 2026-09-02 (later still) — All five D2 reviews landed: every direction dies at the whole-site level, every direction leaves real salvage

All five adversarial reviews are in, each independently rendering both
mockups in headless Chromium, measuring real contrast/overflow/tab-order
rather than trusting the direction's own self-assessment, and each
required to weigh in on Mark's non-religious-feel and hard-questions-
audience rulings. One line each:

1. **Editorial (01):** *survives as a source of parts, dies as the
   spine.* A hard bug (the running head's door pushed off-screen and
   unreachable on iPad portrait), a broken print stylesheet, per-
   tradition "begin a conversation" links rendered at 1.196:1 contrast
   — invisible — and two charges the reviewer calls unpatchable: it
   organizes by chronology and prices itself in reading minutes,
   deleting the constitution's own "Start with your question" door, and
   names the re-assessing/reevaluation audience once, at 93% of the way
   down the page.
2. **Atlas-first (02):** *dies as a homepage; reassign as the
   `atlas-v3.html` rework brief.* A real horizontal-overflow bug the
   README denied outright, an accessible fallback that deletes all
   content without JavaScript despite claiming otherwise, dark-mode
   tint-as-text failures to 1.88:1, and a "Where it stands on the
   Creed" mechanism the reviewer calls a denominational vetting board —
   arguably worse for a deconstructing visitor than any direction's
   incense.
3. **Institutional (03):** *dies as a homepage direction, survives as
   an inner-page pattern.* The kill is structural: its own section
   order ranks audiences the exact inverse of Mark's stated heart
   priority. A real sticky-marginal collision on its flagship section,
   per-tradition entry points 850px off-screen on phone with the CTA
   hidden, and a word-budget count of 1,352 words about the instrument
   to 585 about the traditions, with zero showing an actual
   conversation.
4. **Quiet-liturgical (04):** *dies as a direction, survives as a
   policy.* The most decisive kill: the author had already stripped
   every liturgical word from the visible copy, and the page still
   reads as a service — the feeling comes from the ordo, the red-italic
   rubric, and the printed order, none of them words. The constitution's
   own stillness rule doesn't transfer (it's grounded in a specific
   ground-layer/anti-ghost reason absent on a marketing page), and every
   paced beat in the real constitution is participant-initiated while
   this direction's two are neither.
5. **Product-led (05):** *dies as a whole-site direction, survives as a
   method to extract.* A dark-mode primary-button contrast failure at
   2.69:1, the AI disclosure absent from the direction's own designated
   informed-decision page, and — against Mark's heart-audience note —
   an IA that reads as a scholar's finding aid with no question-shaped
   door.

**Every direction died at the whole-site level. Every direction left
real, specific, named salvage** — this is not five failures, it's D1
and D2 doing exactly what the charter asked of a genuine divergent/
struggle process: five honest, different bets, each falsified in a
different way, each leaving something true behind. Two new
cross-direction findings for D3 regardless of outcome: (a) the D1
text-contrast finding (§ D1 closure) now extends to dark-mode
*graphical* elements too — four of seven census tints fail 3:1 as
rings/underlines in dark mode, not just as text; (b) at least three
reviews independently converge on the same structural diagnosis in
different words — a direction that leads with anything other than a
clear, fast, personal way to ask a hard question fails Mark's stated
heart audience, regardless of how well-crafted or professional it is.

**Next step, per the charter's own D2 rule, not a new decision:**
"Authors may file one defense each; a direction that cannot be
defended dies." No direction has had its defense yet — none of the
above verdicts are final. Commissioning one Fable defense per
direction next, each seeing only its own direction and its own review
(not the other four), before any kill is treated as settled or any
hybridization is considered.

## 2026-09-02 (later still) — Defense round hit a rate limit; retried clean

All five defense agents failed on their first launch with HTTP 429
(`claude-fable-5-1` session limit, resets 3:50am UTC) — each had barely
started reading its own files, so no partial or corrupted output was at
risk. Checked the clock directly rather than guessing (03:57 UTC,
already past reset) and relaunched all five with the identical briefs.
No content was lost this time, unlike the earlier D2 review incident —
these failed before writing anything.
