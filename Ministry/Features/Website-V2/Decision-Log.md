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

## 2026-09-02 (later still) — D2 closed: all five defenses landed, struggle summary written

All five defenses in. Every direction conceded the whole-site-homepage
kill in some form — none argued the reviewer was wrong about that.
Full record, per-direction verdicts, and the choice now in front of
Mark: `Sandbox/D2-struggle/CiC_Website_V2_D2_Struggle_Summary.md`.

**The headline finding, not manufactured by this coordinator:** four of
the five defenses, independently, without being asked to converge on
anything, concluded the homepage's real missing move is a fast, direct,
question-first door — before chronology, before a map, before a
method, before a threshold ritual. The existing UX constitution
already designs this exact door at S0 ("Start with your question," a
co-equal door with the others). None of the five D1 directions built
it prominently. Two cross-direction technical findings also confirmed
regardless of outcome: the D1 text-contrast bug extends to dark-mode
graphical elements (rings, underlines, not just text), and every
direction that touched dark mode broke it in its own way — the brand
record's "dark mode: deferred" note needs a real ruling in D3, not five
more ad hoc attempts.

**No direction survives whole.** This is not a process failure — five
different, well-built bets, each tested hard, each falsified
differently, matches exactly what the charter asked a genuine
divergent/struggle process to do. Per the charter's own D2 rule
("Mark reads the survivors and the struggle record and picks... do not
pre-collapse the choice for him"), three real paths are laid out in the
summary without picking among them: (A) authorize a hybrid direction —
synthesized from the named survivors, itself getting its own Opus
review before D3; (B) pick one direction and repair it narrowly; (C)
re-diverge fresh, informed by what D2 found. **Recommendation given,
clearly marked as a recommendation, not a foregone conclusion:** (A),
reasoned both on craft (the convergent question-first finding, real
salvage across four directions that a single-direction pick would
discard) and on heart (Mark's stated audience wants to put a hard
question down, not read a map or a method first).

**Next action:** Mark reads the struggle summary and the five
review/defense pairs, and picks — or redirects. D3 (Fable synthesis,
Opus review of the synthesis, Mark's freeze) does not start until he
does.

## 2026-09-02 (later still) — Mark picks Option A: hybridize

**Mark's ruling, given directly:** "Go ahead with option A." Commissioned
one Fable synthesis — not another five-way blind diverge, a single
hybrid with named parentage, per the charter's own D2 rule. Unlike D1's
authors, this author was explicitly given all five D1 directions and
all ten D2 review/defense files, plus the struggle summary, and told to
verify the summary's claims against the primary files rather than trust
it alone.

**What it's asked to synthesize, each piece credited to its source:**
a real, prominent question-first S0 door (constitution §5.1's own
design, never built by any D1 direction — the phase's clearest
finding); a Representative/tradition inner page merging 01's
chapter-essay pattern and 03's `tradition.html` (collection → assembly
→ trust → chair, one click deep, not the homepage); the Atlas
explicitly excluded from the homepage and left to 02's own twelve-item
rework brief as a separate track; 04's restraint discipline (no
gratuitous motion, one action per screen, a real contrast floor) with
its liturgical vocabulary and structure explicitly excluded — that
direction died for cause, not craft, and its skin doesn't survive even
though its discipline does; and 05's conceded fact that multi-voice
Table and Representative Modes aren't live, so no copy may promise
either. Writing to `Sandbox/D1-directions/06-hybrid-open-door/`.

**Next action:** once landed, this hybrid gets its own full Opus
adversarial review (and, if real problems surface, its own one-shot
defense) — the same discipline every D1 direction got, not a lighter
pass because it's already synthesized from prior critique. Only after
that does D3 proper (Fable's full Design V2 doc + storyboard) begin.

## 2026-09-02 (later still) — Hybrid landed; Opus review commissioned

**Landed:** `Sandbox/D1-directions/06-hybrid-open-door/` — a real,
verified question-first S0 door as the homepage's first surface (a
working GET form, no JS required, the question held on-page per the
storyboard's R0 grammar) for the first time in this workstream;
`tradition-chloe.html` synthesizing 01's chapter order and 03's record
into one page; a full parentage table; measured contrast tables for
both registers (seven derived dark-safe tradition tints); twelve
rulings for Mark. Verified in headless Chromium at eight widths, light
and dark: zero overflow, zero contrast failures, nothing under 13px,
door works with JS off.

**Two things found in passing, not part of this direction's own
scope:** a corpus-wide "tradition, not world" rename that never reached
the record store's own spoken text (`pahc.limit.material-remains` still
says "a later world," quoted verbatim on the tradition page) — queued
as a separate task, `task_9222cdbc`; and a correction to how this
brief itself paraphrased a D2 finding about the multi-voice Table's
live status — the hybrid's author caught the discrepancy and followed
the primary review rather than the paraphrase, flagged honestly rather
than silently resolved.

**Commissioned, same day:** the hybrid's own full Opus adversarial
review, explicitly told not to go easy on it for being a synthesis —
required to spot-check the "named parentage" claims against the actual
five original directions, and to test specifically whether the
question-first door and the merged tradition page actually resolve what
killed their parents or just relabel it. Landing in
`Sandbox/D2-struggle/06-hybrid-open-door-review.md`.

## 2026-09-02 (later still) — Hybrid review lands: survives, conditionally; one real cross-system dependency surfaced

**Verdict: survives, conditionally.** Genuinely much stronger than its
five parents — most of the hybrid's own self-assessment independently
reproduced (zero overflow at 320–1440 both registers, zero text-contrast
failures, verbatim record quotations, an exact motion inventory).

**Real defects found, not fatal but real:** the question input sits
below the fold on short phone viewports (897px top at 390×844; the
words "Start with your question" entirely off-screen at 390×660); a
header CSS bug collapsing spacing between two elements at every width
≥641px on both pages; three parentage claims that don't hold up against
the originals cited; and Direction 05's information architecture
surviving intact underneath the question box rather than being replaced
as claimed.

**The one finding load-bearing enough to flag directly, for Mark, not
just for the defense round:** submitting a question routes through a
century-sorted picker to a new browser tab with **no question parameter
carried over** — the visitor has to retype or remember what they just
asked — landing first on a scarcity notice the brand's own Never list
bans, with the first real conversation link at 2,627px (further than
the distance that convicted Direction 05's whole information
architecture). The reviewer's own framing: **"the door cannot be
finished on the marketing site alone"** until the app's own deep-link
handling reads a question parameter. This is a real cross-system
dependency between the website (this workstream) and the conversation
app (`cic-poc/frontend`, `App.tsx`'s deep-link contract) — not
something a website mockup or copy fix can close on its own. Sent to
the hybrid's author as part of its one-shot defense with explicit
instruction not to claim a design-only fix for a technical gap that
isn't actually closed; flagged here for Mark's own awareness regardless
of how the defense answers it, since it may need its own change order
against the app, separate from whether this design direction is good.

**Commissioned:** the hybrid's one-shot defense, per the standing rule.
Landing in `Sandbox/D2-struggle/06-hybrid-open-door-defense.md`.

## 2026-09-02 (later still) — D2 fully closed: hybrid defended, one decision surfaced for Mark

**The defense lands, and concedes nearly everything, re-verified
independently rather than taken on the review's word:** the fold, the
header flex-whitespace bug, the un-announced held question, all three
disputed parentage claims, the dark-tint headroom sentence, both stale
"world" quotes, and more. Two of the review's claims contested with
real evidence and won: no "known limitation" banner exists anywhere in
`cic-poc/`'s history to transcribe, and one distance comparison wasn't
like-for-like. A measured, verified fix for the fold defect is already
in hand (input directly under the H1, in-screen on every shipping phone
height, zero overflow).

**The cross-system dependency is now confirmed in the actual app code,
not just asserted:** `App.tsx`'s `parseDeepLink` reads only
`worlds`/`mode`; `consumeDeepLink` strips the URL before render;
`ChatInput.tsx` takes no initial-value prop. The question genuinely
cannot reach the composer today. This is **not fixable on the marketing
site alone** — a real app change (roughly 3–4 files) plus a Render
deploy, not the one-line fix the review guessed at.

**One real, live decision inside that fix, surfaced rather than made
silently:** should the held question travel to the app as a **query
string** (`?q=`, which lands in host/server logs) or a **URL fragment**
(`#q=`, which a browser never sends to a server)? The defense
recommends the fragment, on privacy grounds consistent with the
project's own "nothing is sent ahead" posture. This is a real technical
decision with a real privacy tradeoff, not a design question — it's
being put to Mark, not decided here.

**D2 is now closed in full**, for the hybrid and for the whole
directions-and-hybrid arc: five directions diverged, five struggled and
defended, one hybrid synthesized with named parentage, that hybrid
struggled and defended in turn. What remains before D3: Mark's read of
where this landed, and his ruling on the query-string-vs-fragment
question (and, separately, whether/when to greenlight the small
app-side change it requires).

**Mark's ruling: use the fragment.** DECIDED — the held question
travels to the app as a URL fragment (`#q=`), never a query string,
per the defense's own privacy reasoning. This is a design/protocol
decision, not yet a build instruction — the actual `App.tsx` change
(parseDeepLink reading the fragment, ChatInput accepting an initial
value) is D4's to build when this increment is scheduled, not done
here. This was the last open item from D2. **D3 opens next**: Fable
synthesizes the defended hybrid into Website Design V2 — the full
design document plus the page-by-page storyboard — filed in
`Ministry/Features/Website-V2/` proper, not Sandbox, per the charter's
own file discipline and draft-and-approve rule for participant-facing
copy.

## 2026-09-02 (later still) — D3 commissioned

One Fable synthesis, pointed at the defended hybrid
(`Sandbox/D1-directions/06-hybrid-open-door/`) as its primary source —
not re-deriving from the five original directions, converging what
already survived struggle. Asked to apply the hybrid's own review and
defense findings as fixes (the verified fold layout, the header CSS
fix, corrected parentage and distance claims), resolve or explicitly
flag every accumulated "ruling for Mark" across the hybrid's README,
review, and defense (~20 items) rather than silently dropping any, and
build to the fragment ruling above. Two deliverables, in
`Ministry/Features/Website-V2/` proper: `CiC_Website_Design_V2.md` (the
full design document) and `CiC_Website_V2_Storyboard.md` (every page,
every state, copy register, accessibility and responsive behavior).
Draft-and-approve required on all participant-facing copy — locked
brand lines quoted verbatim and marked distinctly from drafted prose.
The Atlas is referenced as its own separate rework track (Direction
02's twelve-item brief), not rebuilt here.

**Next action:** once both files land, Opus reviews the synthesis
against the charter, the constitution, and the full struggle record.
Then Mark freezes it — after the freeze, changes need a change order,
not quiet edits.

## 2026-09-02 (later still) — D3 lands: Design V2 + Storyboard, verified

Both filed in `Ministry/Features/Website-V2/` proper:
`CiC_Website_Design_V2.md` (990 lines) and `CiC_Website_V2_Storyboard.md`
(908 lines). Verified in headless Chromium against a scratch copy of
the hybrid with the defense's fixes actually applied, not assumed: the
fold fix reproduces the review's own numbers (question input at
456–504px vs. 897px unfixed), zero overflow and zero contrast failures
across both pages and both registers, nothing under 13px, the held
question announced to screen readers, no query string anywhere — built
to the fragment ruling. 85 `[DRAFT COPY]` lines flagged for Mark's
approval pass; locked brand lines tagged verbatim, distinctly.

**Rulings register: 33 items, none dropped.** 2 DECIDED (the fragment
and its build item), 13 flagged ⚠ OPEN FOR MARK each with a
recommendation (headline ones: the S0 door ranking as a
website-only stretch of the constitution; the draft-status records
gate governing all seven tradition pages; whether the fleet's
seed-status canon questions are cleared for a marketing surface; the
derived dark tints; the mark's autoplay; the pilot/cost scarcity copy,
with an offered re-draft; needing the Cloudflare Pages preview
environment before D4 starts), the rest RECOMMENDED with reasons
stated.

**Three findings surfaced, not resolved here, none this workstream's
to fix:** `whats-next.html` and `support.html` contradict each other on
the Atlas's scope, and `whats-next.html`'s own meta description still
says "three new worlds" — the same class of staleness as the earlier
Cappadocian fix, in a different spot; two traditions' record-store ids
differ from their `world-census.json` ids (`cappadocian-trinitarian`
vs. the census id, `imperial-juridical` likewise) — the eventual build
must join on both; and a CSS rule (`.site-nav a{display:inline-flex}`)
that would have silently defeated the gated side door's `hidden`
attribute, caught in verification before it could ship. A fourth,
already queued as `task_c8e50b7d`: the live site's per-Representative
Table links land on a disabled "Seat at least two voices" button today.

**Next action:** Opus reviews the synthesis against the charter, the
constitution, and the full struggle record, per the standing rule.
Then it goes to Mark to read and, if ready, freeze.

## 2026-09-02 (later still) — D3 synthesis review commissioned

One Opus review of both D3 documents together, checked against the
hybrid, its review/defense, the five original directions, the brand
system, and the constitution — verifying fidelity (nothing killed
quietly reintroduced), internal consistency between the two documents,
a spot-check of the synthesis's own verification claims, draft-and-
approve discipline, and whether it still serves the heart audience as
well as the hybrid did once generalized from one tradition to seven and
from one mockup to a full storyboard. Landing in
`Sandbox/D2-struggle/D3-synthesis-review.md` (kept in Sandbox as
process material; the two reviewed deliverables stay in place
regardless of the verdict). Required a clear verdict: freeze as-is,
freeze with named fixes, or not ready.

## 2026-09-02 (later still) — D3 fix pass commissioned

Opus's verdict: ready to freeze with eleven named required fixes (R1,
R5, R6, R7, R8 substantive; R2, R3, R4, R9, R10, R11 precision), all
edits to the two existing D3 documents, nothing D2 settled reopened.
Headline items: the homepage doesn't yet distinguish its one-tradition
launch state from its eventual seven-page end state; the tradition
page's own order puts two conversation links before the AI disclosure
for a direct arrival; the question fragment has no escaping/length
rule; the reviewer's-brief material traces to no real file; and D0's
paid-tier Table gate (seam G) quietly disappeared while a new door was
promoted, needing an explicit ruling rather than a silent assumption.

Commissioned one Fable fix pass, briefed with the full review and told
to apply the eleven required fixes plus the sixteen non-blocking items
where quick, without relitigating anything the review confirmed or
reopening the struggle record's settled decisions. Editing the two
documents in place.

**Next action:** once the fix pass lands, this coordinator spot-checks
it against the review's own required-fix list, then it goes to Mark to
read and freeze.

## 2026-09-02 (later still) — D3 fix pass landed and spot-checked; ready for Mark's freeze

All eleven required fixes applied and verified in place (design doc
990→1192 lines, storyboard 908→1004 lines), plus all sixteen
non-blocking items and two further slips the author caught in its own
re-measurement. Coordinator spot-check confirms rulings 34–39 are
present, correctly framed, and match the review's own required-fix
list. Both documents' status blocks now read: reviewed by Opus, fixes
applied, awaiting Mark's freeze.

**D3 is complete. This is the freeze gate** — the charter's own
"after the freeze, changes need a change order, not quiet edits" line
starts to apply once Mark rules. Register carries 39 rulings total;
most consequential for his read, surfaced directly rather than left to
be found: ruling 34 (authorize the app's `#q=` change order — a small,
real change in `cic-poc/frontend`, D4's to build once scheduled),
ruling 35 (the paid-tier multi-voice-Table gate — a business-model
question this design assumed loosened but never had confirmed), ruling
36 (reviewer's-brief content clearance — real briefs exist for four
traditions, none for three, and none of the four are cleared for a
participant surface yet), and ruling 32 (the Cloudflare Pages preview
environment D0 already flagged — D4 can't start safely without it).
The remaining rulings are content-clearance and copy-register calls,
each already carrying its own recommendation in the document.

**Next action:** Mark reads both documents (or this ledger's summary
first) and rules — freeze, freeze with named changes, or hold.

## 2026-09-02 (later still) — FROZEN

**Mark's ruling, given directly: "Freeze it."** `CiC_Website_Design_V2.md`
and `CiC_Website_V2_Storyboard.md`, as they stand at commit `560efeb5`
plus the two status-block edits recording the freeze itself, are now the
binding design reference for D4. Per the charter: from here, changes need
a change order in this log, not quiet edits to the documents.

**What the freeze does and doesn't cover, stated plainly so it isn't
assumed either way later:** it fixes the two documents' shape and content
as the reference to build from. It does **not** silently resolve the
roughly twenty ⚠ OPEN FOR MARK items still in the rulings register (content
clearance, the paid-tier Table gate, the reviewer's-brief material, the
app change order, etc.) — each stays a real open decision, to be brought
to Mark as D4 reaches it, or sooner if he'd rather clear them ahead of
time. Silence on an item is not approval of its RECOMMENDED default.

**The one item that blocks D4 from starting at all, restated one more
time because it's a console action only Mark can take:** ruling 32 /
D0 seam A — a Cloudflare Pages preview build for `claude/website-v2-sandbox`
(or a manual-deploys switch), so build increments can be read before they
touch the live site. `cic-website/` deploys via Cloudflare Pages, not
Render — the charter's own original assumption. Nothing else is
outstanding to open D4; this is the next concrete step.

D0 → D1 (five directions) → D2 (five reviews, five defenses, one hybrid,
its review, its defense) → D3 (synthesis, review, fix pass) is complete,
frozen, and on record. D4 begins once the Pages preview question is
settled.

## 2026-09-02 (later still) — Change order: Cloudflare Worker, not Pages

**Correction to the frozen record**, per the charter's own rule that
changes after freeze need a change order, not a quiet edit. Mark
pasted the actual Cloudflare dashboard page while checking on the
preview-build question: the live site is a **Cloudflare Worker with
static assets** using Workers Builds for its Git integration — not
the classic "Cloudflare Pages" product this workstream assumed since
D0 (the dashboard fields shown are unambiguously Workers-only
language: "Variables cannot be added to a Worker that only has static
assets," Runtime/Compatibility-date/Compatibility-flags sections).
Functionally the same fix still applies — Workers Builds supports
per-branch preview deployments the same way Pages does, gated on the
Production branch being set correctly — so this doesn't change what
Mark needs to check, only the correct name for it. Corrected in
`CiC_Website_Design_V2.md` (ruling 32, the 404-page row) and the D0
inheritance note. Still open: Mark confirming the Production branch
value and checking the Deployments tab for a sandbox-branch preview
URL.

## 2026-09-02 (later still) — Non-production branch builds enabled

Mark enabled "Builds for non-production branches" on the Cloudflare
Worker's Build settings, after confirming Production branch = `main`
and finding the deploy command for that toggle. Per Cloudflare's own
docs (developers.cloudflare.com/workers/ci-cd/builds/build-branches/,
/workers/versions-and-deployments/preview-urls/ — fetched via search,
direct fetch to the docs domain is blocked by this session's egress
proxy), this defaults to `npx wrangler versions upload` for
non-production branches — a preview-only command, distinct from the
production branch's `npx wrangler deploy`, that uploads a new Worker
version with its own stable preview URL and does not shift production
traffic. Flagged for Mark to confirm the non-production command
actually reads as the safe default, not a leftover from the August
incident when this same toggle was previously enabled with the
unconditional deploy command.

Pushing this entry now to trigger a real build under the new setting;
next check is the Deployments tab for a preview URL tied to
`claude/website-v2-sandbox`.

## 2026-09-02 (later still) — Preview pipeline diagnosed and fixed

**Root cause found via a live failed build, not guessed:** a real build
on an unrelated branch (`claude/cic-tour-encouraging-reading-x5dxmw`,
triggered once "Builds for non-production branches" was enabled) failed
with "Missing entry-point to Worker script or to assets directory."
Comparing it against a successful `main` build's own log showed why:
`wrangler deploy` (production's command) runs a smart auto-detect step
that finds `cic-website` as the static output directory and generates
an ephemeral `wrangler.jsonc` for that build only (never committed to
git — there is no wrangler config file anywhere in this repo, confirmed
directly). `wrangler versions upload` (the non-production "Version
command," a distinct dashboard field from "Deploy command") has no such
auto-detect step and needs the assets directory named explicitly.

**Fix, applied by Mark:** the Version command changed from
`npx wrangler versions upload` to
`npx wrangler versions upload --assets=cic-website`, matching what
production's own auto-detect already resolves to. Production's Deploy
command is untouched.

Pushing this entry now as the real test of the fix; next check is the
Deployments/build log for a clean, successful build on
`claude/website-v2-sandbox` with its own preview URL.

## 2026-09-02 (later still) — Preview pipeline shelved; D4 begins

**Mark's ruling: option 1 — skip the live preview, start D4.** After
extensive diagnosis (the real Version-command bug found and fixed;
confirmed the toggle fires for other branches; ruled out a
cic-website/-scoped watch path by testing with a real file change;
still nothing built for `claude/website-v2-sandbox` specifically across
four separate pushes) the remaining cause is most likely a
branch-specific quirk in Cloudflare's own webhook tracking, not
anything fixable from the settings visible in this session. Not
pursued further — diminishing returns against real D4 progress.

**Verification for D4, in place of a live preview:** the same
discipline already used through D1–D3 — local rendering in headless
Chromium (pre-installed at `/opt/pw-browsers`), contrast and overflow
checks, accessibility-tree inspection, and screenshots shared directly
in conversation. No live URL; Mark reads each increment's rendered
result before it merges, per the charter's own D4 rule, just via
screenshots/local review rather than a hosted preview.

**D4 starts now.** Building to the frozen `CiC_Website_Design_V2.md`
and `CiC_Website_V2_Storyboard.md`, using the defended hybrid's
`homepage.html`/`tradition-chloe.html` as structural reference — **not**
as-is, since the D3 review's fixes (the fold fix, the header CSS
correction, AI-disclosure-before-conversation-links ordering, the
launch-state distinction, the `#q=` fragment protocol) were written
into the design documents, not back into the hybrid's own mockup
files. First increment: the homepage.

## 2026-09-02 (later still) — D4 Increment 1: the real homepage built

`cic-website/index.html` rewritten in full, following storyboard §1 and
design record §5/§6/§7 line by line rather than copying the hybrid
mockup. Structural corrections made relative to the hybrid, each traced
to a specific spec item:

- **Fragment-only door, no `<form>`.** The hybrid's `<form method="get"
  action="#who">` and its `?q=` query-string JS are gone. The input
  sits in a plain `<div>`; the control is a button-styled `<a
  href="#who">`; Enter in the input and each offered question are
  wired the same way. Every hold writes `#q=<encoded>` via
  `history.replaceState` only — never a query string (§5.1, ruling 14).
  Verified: no `?` ever appears in the URL through the hold/offered/
  restore/empty-submit paths.
- **The real §5.1 algorithm**, not the hybrid's approximation: decode
  in `try/catch`, `.trim().slice(0,280)`, render via `textContent`/
  `.value` only, normalise the URL on arrival without scrolling. Every
  "Ask *Name*" href gains `#q=<held text>` once a question is held
  (verified — this is current on-page behaviour per §5.1, independent
  of the app-side change order in §5.2/ruling 34, which is not
  authorised and not touched here).
- **Same-tab hand-off (ruling 15).** Dropped `target="_blank"` and the
  "(opens in a new tab)" announcements from every app link — the
  hybrid still had these; the design record recommends same-tab now
  that sessions rehydrate on reload.
- **Launch state (ruling 4).** Only Chloe's chair carries a second
  action ("Her record →", linking to `traditions/post-apostolic-house-
  church.html`, not yet built — next increment). The other six end at
  "Ask *Name* →"; no `#mock-note`, no placeholder, nothing greyed.
- **The fold fix**, applied as the fix-pass specified: the lede moved
  out of the hero into the door (after the input/button row); the pilot
  note and cost caveat moved below the seven chairs, not above; the
  hero's first sentence given to the "who" section's scope line
  instead.
- **The disclosure block corrected**: the "Witness, never recruitment"
  bullet no longer duplicates the protected closing line (that line now
  appears once, at the end of the section); a new fifth bullet, "Lives
  in one browser tab, not an account," added to the unfinished column
  per storyboard 1.5k; the dated caption ("on 25 August 2026") restored
  on the exchange capture.
- **Mark removed from the header** (ruling 8) — the wordmark is plain
  text; the "Arriving" mark plays once, only in the hero, beside its
  own sentence.
- **`.site-nav a[hidden]{display:none}`** added (§11.6) so the gated
  side door is actually hidden, not just `inline-flex`ed into empty
  space; the mobile chrome tightening from the fix pass (nav `.9rem`,
  header row and door padding, input `flex-basis:11rem` ≤640px)
  applied as specified.
- **Real relative paths** throughout (`assets/...`, `about.html`,
  etc.) in place of the hybrid's sandbox-depth `../../../../../../`
  paths; title and meta description corrected to storyboard §S.6
  exactly (the pending "six→seven" fix folded in here, so the separate
  unpushed `main`-branch fix is superseded for this file); no sandbox
  note, no visible `draft` tags (kept as invisible `data-copy`
  provenance attributes only); support-slot links are plain text, never
  buttons (the live site's current button styling was not carried
  over, per storyboard 1.7).
- **Fully self-contained** — inline CSS, no dependency on the shared
  `assets/style.css` — so it can't collide with pages not yet rebuilt.

**Verified locally** (headless Chromium, `/opt/pw-browsers`, no live
preview per the ruling above): zero horizontal overflow at 320–1440px,
both registers; heading outline is one clean H1→H2→H2(H3×2→H4×7)→
H2(H3×4)→H2(H3×2)→H2→H2 with no skipped levels; skip link moves focus
into `<main>`; hold/offered/restore/empty-submit flows all behave per
§5.1 and §1.8's state table (including the no-scroll-on-arrival
invariant); no-JS hrefs degrade to plain `#who` jumps; spot-checked
contrast ratios all clear the 4.5:1 floor (most clear 7:1; the
muted/secondary tone holds its documented 5.39/8.45, as approved in
the design record). Screenshots (mobile and desktop, both registers)
shared with Mark for review before this merges.

**Known, expected gap:** Chloe's "Her record" link points to
`traditions/post-apostolic-house-church.html`, which doesn't exist yet
— that's Increment 2. **Still open, unchanged by this increment:**
rulings 34/35/36/37-39, the photo-rights question (seam B), and content
clearance for the canon/starter questions.

## 2026-09-02 (later still) — Palette question raised; ruling: less-yellow ground only

**Mark's question, looking at the built homepage:** does the manuscript
palette (parchment, madder, gold-leaf) actually serve who the project
is trying to reach, given the "no religion feel" goal — and does it
even hold up once the site's own "twenty centuries" reaches the
missions era or the modern era, not just the first four centuries it's
built for today?

**A comparison mockup was built and shared** (not committed to the
repo — a published Artifact, "Manuscript or Daylight"): the same three
cards (the real Chloe; two invented, clearly-labeled stand-ins for a
1930s East Africa mission figure and a modern São Paulo house-church
pastor) rendered in the current manuscript system side by side with an
alternate "daylight" system (less-yellow paper ground, plain white
cards, a clay accent instead of madder, a muted era-tag family instead
of the current jewel-tone chair tints, Fraunces/Public Sans instead of
Alegreya/Alegreya Sans). The recommendation offered was to move the
whole chrome to the alternate system, since parchment reads as
period-true for Early Church but starts arguing with the content by
the time the timeline reaches a pastor with a phone number.

**Mark's ruling: adopt only the less-yellow ground; keep every other
color — including all seven per-tradition/per-era tint colors — as
they are now.** Not the wholesale swap recommended; a single, scoped
change.

**Applied to `cic-website/index.html`:** `--parchment` `#F7F3EB` →
`#F6F6F2`; `--vellum` `#FEFCF8` → `#FFFFFF`. Nothing else touched —
`--ink`, `--ink-faded`, `--madder` (and its hover/edge), `--gold-leaf`,
`--gold-wash` (the exchange leaf's own background, read as content
styling rather than "the background"), `--tyrian`, `--lapis`,
`--graphite`, `--rule`, and all seven chair tints (light and dark) are
byte-for-byte unchanged. Dark register also left untouched — Mark's
comment was made against the light-mode comparison only, and nothing
he said reached dark mode.

**Re-verified, not just assumed:** the new pair only improves the
already-documented ratios (recomputed, not eyeballed) —
ground/ink 13.99 (was 13.70), ground/muted 5.50 (was 5.39),
ground/madder 5.98 (was 5.86); the white surface clears further still.
No regression against any number the design record already locked in.
Re-screenshotted the door/hero at 1280×900 to confirm no visual
breakage — clean.

This is a real, if small, deviation from the frozen `CiC_Website_Design_V2.md`
§6.2 color tables (which name `#F7F3EB`/`#FEFCF8` as the verified
light-register ground/surface). Recorded here as the change order;
§6.2's token table needs the same two-value edit the next time that
document is opened, so the frozen record doesn't quietly drift from
what's actually shipping.

## 2026-09-02 (later still) — Change order: "who" before the door

**Mark's objection to the built homepage:** the question door is the first
thing on the page, but the question it asks for hangs — nothing happens
with it until a tradition is picked — and the real heart of this project is
*who* you're sitting with, not a question typed into empty air. Sharpened
on push-back: a blank "ask a question" box doesn't fail because visitors
lack questions, it fails because they don't yet have the context to know
what's worth asking or who could actually answer it. "I want to ask her
something, because I trust she has the context to answer it" — that
sentence needs the *her* established before the question makes sense.

**Ruling: swap §1.2 (the door) and §1.3 ("Who would you like to ask?") —
who leads.** Agreed on the merits, not just accepted: the visitor now meets
the seven immediately after the hero, then reaches the question door
already knowing who's at the table. The one accepted cost: someone who
arrives already carrying a specific question no longer gets the instant
"type it right now" landing spot — they meet the seven first. The offered
six hard questions still give an on-ramp once they reach the door.

**Also ruled, same conversation — the chairs regroup as a gallery:** at
more than ten traditions across more eras, a single stacked column (the
launch build's actual shape) would make people scroll past everyone to
find one voice. New rule: **vertically by era, horizontally by each
tradition's start date within the era** — each era is a row, chronological
left to right, wrapping to a second row under the same era heading if an
era outgrows one row's width, rather than lengthening a shared column.

**Applied to `cic-website/index.html`:**
- The `<section class="who">` block (held-block, eyebrow, H2, scope, both
  era groups, pilot note, cost caveat, second door) moved to immediately
  after the hero; `<section class="door">` (the question input, offered
  questions) now follows it. No copy changed except what the reorder
  itself implies — the door's own H2/lede/how-line/AI-line/offered
  questions are byte-for-byte the same text, just relocated.
- `.chairs` changed from a block list to
  `grid-template-columns:repeat(auto-fill,minmax(150px,1fr))` — each
  `<ol class="chairs">` (one per era) is now a row of tiles instead of a
  stacked column; `.chair` itself changed from portrait-beside-text to a
  compact vertical tile (portrait, name, role, tradition, dates, a
  2-line-clamped tile sentence, actions). The tile sentence stays full
  census-verbatim text in the DOM — the clamp is CSS-only, so a screen
  reader still gets the whole sentence; only the sighted layout truncates.
  `.who`'s own max-width widened from the 44rem single-column measure to
  the 64rem chrome width to give the grid room; the section's own prose
  (h2, scope, pilot note, held block) stays pinned to the narrower
  measure for readability.
- The held-question mechanism (`hold()`/`setHeld()`, the `#q=` fragment
  protocol, restoring from a shared URL, the no-JS fallback) is
  functionally unchanged — it already scrolled to and focused `#who`
  after a hold, which now means scrolling *up* to the chairs (they
  precede the door in the DOM) instead of down. No code change was needed
  for this; `scrollIntoView`/`.focus()` don't care about direction.

**Verified locally** (headless Chromium): zero horizontal overflow at
320–1440px; heading outline now runs H1 → H2 "Who would you like to ask?"
(H3 era ×2, H4 name ×7) → H2 "Start with your question" → H2 "What a
conversation looks like" → ... with no skipped levels; the grid shows all
3 of era 1's chairs on one row and all 4 of era 2's on one row at
1024px+, 2 per row at 390px (era 1: 2+1, era 2: 2+2) — real scroll
reduction, not just reflow; held/offered/restore/empty-submit all
re-tested end to end post-reorder — hash, held-block text, focus, and the
Ask-link `#q=` rewrite all still fire correctly with the new scroll
direction. Portraits confirmed loading correctly (an early screenshot
showed two blank circles — traced to the screenshot tool's own lazy-load
timing, not a page bug; all seven decode and render once given a moment).

**Recorded as a real deviation from the frozen storyboard**, not a quiet
edit: `CiC_Website_V2_Storyboard.md` §1's "Purpose" and "Order of the page"
updated in place, with an explicit change-order note. Flagged there and
here: §1.8's state table, §1.9's accessibility walk-through and keyboard
tab-stop counts, and §1.10 still describe the *pre-swap* order and have
not been re-verified against the new one — real work, not yet done, before
either document is fully trustworthy again on those specifics.

## 2026-09-02 (later still) — The gallery caps its own height, doesn't grow the page

**Mark's follow-up, looking at the rebuilt gallery:** two era rows today is
fine, but the project's own "twenty centuries" horizon means eras will
keep being added — left unchecked, the page could end up with 50+ rows
stacked down the homepage. The rows need to scroll off the screen instead
of lengthening the page; two rows is the right amount to show at once,
now.

**Fix: `.who-gallery` wraps both era groups in a fixed-height,
internally-scrolling container** (`overflow-y:auto`), sized per breakpoint
to exactly fit today's two eras with no scrollbar at all — a third era (or
a fourth, or a fiftieth) extends the *scrollable* content past that cap
instead of pushing the door, the exchange, the disclosure, and everything
below it further down the page. The homepage's own total length stays
bounded regardless of how many traditions or eras the project adds later;
only the gallery's internal scroll grows.

Heights are measured, not guessed — real jumps happen where the grid's
`auto-fill` column count changes, and those jumps don't line up with the
breakpoints already in the stylesheet, so this component gets its own:

| Width | Today's 2-era height (measured) | Cap set |
|---|---|---|
| ≤480px | 1070–1505 (worst case at 320) | 1560px |
| 481–699px | 1041–1338 (worst case at 481) | 1380px |
| ≥700px | 724–765 | 800px |

The first attempt used the existing 640/680 breakpoints and left a gap at
681–699px where the grid was still in its narrower-tier wrapping (1041px
tall) but the cap had already dropped to the desktop 800px value, clipping
content that should have fit with no scroll. Caught by testing every
width in that gap, not just the round numbers, and fixed by moving the
breakpoint to 699px, where the content itself actually transitions.

**Verified locally, both the no-scroll-today case and the mechanism
itself:** every width from 320–1440px (plus the specific 660–710px range
around the fixed breakpoint) shows `scrollHeight === clientHeight` — no
scrollbar, exactly as today's two eras should render. A synthetic third
era injected via script (test-only, never committed) confirmed the
container correctly switches to an internal scroll once content exceeds
the cap, while the page's own total height barely moves. `padding-right`
and a matching negative margin keep the scrollbar (when one eventually
appears) from overlapping the rightmost column.

Not yet built, and worth naming rather than leaving implicit: there is no
visible "more eras below" affordance beyond the native scrollbar, since
nothing scrolls today. Worth a second look — a subtle edge fade, or just
confirming the native scrollbar reads clearly enough — once a real third
era makes the scroll live.

## 2026-09-02 (later still) — One era at a time, with a next/previous pointer

**Mark's follow-up, same conversation:** even two eras stacked is more
screen than it needs to be — show one era's row at a time, scrolled off
rather than stacked, with a "next era" control to move between them.

**Built:** each era (heading + its chairs) now wraps in its own
`.era-group`; `.who-gallery` shows exactly one at a time via
`scroll-snap-type: y mandatory` (each group `scroll-snap-align: start`)
sized per breakpoint to fit the taller of today's two eras — 420px
≥700px, 760px 481–699px, 820px ≤480px, the same measured-per-tier
discipline as the two-era version this replaces. Below the gallery, an
era-nav row (`← Previous era` / `The {Era} · N of M` / `Next era →`)
moves between them: a real `<button>` pair, hidden by default and
revealed only once JavaScript confirms it can wire them up — the same
progressive-enhancement idiom already used for the returning-visitor side
door. Clicking Next/Previous scrolls the gallery so that era's heading is
flush with the top and moves focus there (`tabindex="-1"` on the
era-group, `aria-labelledby` its heading) — the visitor caused the state
change, so a screen reader hears it via focus moving, not a live region
(the same rule the held-question flow already follows).

**Without JavaScript**, the buttons never appear, but nothing is lost:
`.who-gallery` is a plain native scroll region (`tabindex="0"` so it's
keyboard-reachable — arrow keys and Page Down/Up scroll it once focused),
and every era, every name, every link is still in the static markup,
reachable by wheel, touch, or Tab. R-A10 holds without any extra work
here, same as everywhere else on this page.

**A real bug, caught before shipping, not after:** the first version set
each tier's `max-height` to fit the *taller* of the two eras and stopped
there. Clicking "Next era" from era 1 (`Household Leader` era, 3 chairs)
to era 2 (`Deacon of the Letters` era, 4 chairs, shorter overall at most
widths) landed mid-viewport, not flush — era 2 simply doesn't have enough
of its *own* height to fill a viewport sized for era 1, and there's
nothing after it, so the browser clamps `scrollTop` before era 2's top
ever reaches the container's top. Confirmed directly (`scrollTop` stuck
at the clamped max regardless of the value the script asked for) rather
than assumed. Fixed with `padding-bottom` on the gallery — 94/117/209px
per tier, `viewport height − era 2's own measured height` at that tier —
giving the last era enough trailing space to scroll fully into place.
**This padding is keyed to era 2 specifically being last**; the day a
third era is added and something else becomes last, both the max-height
tier table and this padding need re-measuring together, not just the
former.

**Verified**, not assumed: zero horizontal overflow 320–1440px; every
tier's gallery genuinely scrolls (`scrollHeight > clientHeight` at all
widths, confirming one-era-at-a-time is real, not just visually
coincidental); Next from era 1 lands with era 2's heading exactly flush
(`scrollTop` matches era 2's measured offset, not clamped short) and
focus/labels/disabled-state all update correctly and *stay* correct
across time (re-checked at multiple delays — the debounced scroll
listener doesn't fight a button click's own state); Previous returns
cleanly to `scrollTop: 0`; the held-question flow re-tested end to end
inside the new nested structure with no regressions; no-JS confirmed via
`javaScriptEnabled: false` — era-nav stays hidden, all seven Ask links
present, native scroll still active. A nice side effect, not designed
in: at the default (era 1) scroll position, era 2's heading and the top
sliver of its portraits peek over the gallery's bottom edge on every
tested width — a genuine "there's more" cue that costs nothing extra.

## 2026-09-03 — Reverted to both eras shown; the peek goes, the pointer stays

**Mark, after using the one-era-at-a-time build:** two rows is fine to
show at once — for now, with exactly two eras, show both in full. Don't
show the top of the next row (the peek from the entry above was a miss,
not a feature); add a next/previous era pointer for whenever a third era
actually doesn't fit.

**Reverted:** the gallery no longer shows one era at a time. It shows as
many whole eras as fit — today, both — with the same `.era-group` /
`scroll-snap-align` structure and the same Previous/Next control kept
from the last build, but its job changed: the control now only appears
when content genuinely doesn't fit (`gallery.scrollHeight >
gallery.clientHeight`), not on a fixed "always show one" rule. With
exactly two eras and both fitting inside the measured per-tier caps
(800/1380/1560px, same numbers as the *first* gallery-capping change
order two entries above), the control stays hidden today — nothing to
point to yet.

**The height is computed from real content, not just capped by CSS**, so
the cutoff always lands on an era boundary and never mid-era: a
`sizeGallery()` pass sums each `.era-group`'s actual rendered height
against the same per-tier target, stopping at the last one that still
fits whole, and sets that exact sum as `max-height`. The CSS values
above are the no-JS fallback only — they happen to already show both of
today's eras with no scrollbar on their own, which is what let the
first version of this ship without JS depending on it for correctness.

**Two more real bugs, both caught by testing an actual third era rather
than trusting the logic on paper:**

1. **The last-era clamp, again, in a new shape.** Sizing the container
   to fit as many eras as possible (not just one) reintroduces the same
   clamp the one-era build hit: whichever era ends up last after a Next
   click may not have enough of its own height to reach the container's
   top, since nothing follows it. Fixed the same way — `padding-bottom`
   sized to `(the fitted height) − (last era's own height)` — but this
   time computed dynamically in `sizeGallery()` off the *actual* last
   `.era-group`, not hand-measured per tier, since which era is last now
   depends on where the visitor has scrolled to, not just on today's
   fixed set of two.
2. **That padding leaked into the two-era case.** The first pass applied
   it unconditionally, which added real padding even when both eras
   already fit with room to spare — reintroducing a phantom scrollbar
   for exactly the case this whole change order exists to avoid. Caught
   by re-running the plain two-era overflow sweep after adding the fix
   for bug 1, not by only testing the three-era path. Fixed by gating
   the padding on there actually being more content than the fitted
   height (`total content height > fit`) — zero today, real once a third
   era doesn't fit.
3. **Previous didn't reverse Next.** Landing on a lone trailing era (say,
   era 3 alone, once one exists) and clicking Previous stepped back by a
   single era-index, landing on "era 2–3" rather than back on the
   original "era 1–2" page Next came from. Fixed by having Previous
   compute the largest page that fits *ending* at the current top,
   mirroring how Next computes the next page — verified by walking
   forward then back through a real three-era test file and checking the
   label and `scrollTop` matched the starting state exactly, not just
   "some earlier state."
4. **The nav row didn't actually hide.** `eraNav.hidden = true` doesn't
   hide anything when `.era-nav{display:flex}` has equal-or-higher
   specificity than the `[hidden]` UA rule it needs to beat — the exact
   bug the design record's §11.6 already named once for
   `.site-nav a[hidden]`, recurring here because the fix was applied to
   one selector and not generalised. Missed by every `getAttribute
   ('hidden')` check in this pass (the attribute *was* set correctly)
   and only caught by actually looking at a screenshot, where the label
   text was plainly sitting on the page it was supposed to be absent
   from. Fixed with the matching `.era-nav[hidden]{display:none}` rule.
   **Worth a real pass over the rest of the stylesheet for the same
   pattern** rather than fixing it a third time somewhere else later —
   done: every other `hidden`-bearing element (`#welcome-back`, `#held`,
   `.side-door` via the existing `.site-nav a[hidden]` rule) sets no
   competing `display` of its own, so none of them share this bug;
   `.era-nav` was the only other offender.

**Verified after all four fixes, against both a real two-era build and a
real (not runtime-injected) three-era test file** — a first injection
attempt via `appendChild` in a live page missed real bugs because the
page's own script had already cached its `.era-group` list before the
injection ran, so it silently ignored the new era; switching to an
actual third `.era-group` written into a scratch copy of the file
before load is what surfaced bugs 1–3 above. Confirmed: two-era case is
pixel-identical to before this whole entry (`scrollHeight === clientHeight`
at every breakpoint, nav genuinely invisible, not just attribute-hidden);
three-era case shows eras 1–2, Next lands exactly flush on era 3 alone,
Previous returns exactly to the original 1–2 view (same label, same
`scrollTop: 0`); held-question flow and no-JS fallback both re-confirmed
with no regressions.

## 2026-09-03 — Homepage change order: "have a conversation with," not "ask"

**Mark's ruling:** the H2 over the seven chairs should read "Who would you
like to have a conversation with?", not "Who would you like to ask?" — the
project's own name is *Church in Conversation*; a question is how a visitor
starts, but the conversation itself is the point, and the heading should
say so rather than naming the mechanism.

**Applied to `cic-website/index.html`** (the H2 is `[DRAFT COPY — pending
Mark's approval]`, exactly the register this kind of edit is for) and to
`CiC_Website_V2_Storyboard.md` §1.3 everywhere the old wording was quoted
— the section heading itself, the copy row (with this ruling noted inline),
the fold-measurement note, the accessibility walk-through, and Appendix A's
draft-copy index. Nothing else on the page changed — the eyebrow "Who's at
the table," the scope line, and every "Ask {Name} →" chair action keep
their current wording; only the section H2 moved. Verified live.

## 2026-09-03 — D4 Increment 2: Chloe's tradition page built

**Built:** `cic-website/traditions/post-apostolic-house-church.html` —
Increment 2, following storyboard §2 (the tradition-page template, Chloe
as its reference instance) line by line, using the defended hybrid's
`tradition-chloe.html` as structural reference only, the same discipline
as Increment 1. This is the page the homepage's "Her record →" link has
pointed to since Increment 1; it now resolves.

**Corrections made relative to the hybrid, each traced to a specific spec
item, mirroring the homepage's own fix list:**

- **Same-tab hand-off (ruling 15).** Dropped `target="_blank"` and every
  "(opens in a new tab)" announcement from all four conversation links
  (the seat line's Begin/Bring, the closing door's Begin/Bring) and the
  seven — now four, see below — question links.
- **The `#q=` fragment, extended one page (storyboard §2.2).** A question
  held on the homepage now survives the click through: on arrival, the
  page reads `location.hash` (decode in `try/catch`, trim, cut to 280,
  `textContent` only — §5.1's rule, verbatim), shows a held block between
  the AI line and the seat line, and appends `#q=<encoded>` to *all four*
  conversation links (the storyboard's own instruction for this page,
  distinct from the homepage's own Ask-links-only rule) — not gated
  behind the app's own change order (ruling 34, still unauthorized),
  since this is the site's own on-page behavior either way. "Edit it"
  goes back to `../index.html#q=…`, the only place the actual input lives.
- **The AI line, added.** The hybrid's seat line had no equivalent of the
  homepage's 1.2g disclosure; the storyboard's fix-pass added one
  (§2.2a, "the review's R5") — a visitor arriving here directly, from a
  search result or a shared link, has passed no other disclosure. Added
  verbatim, in the same graphite-rule/sans/ink-text treatment as the
  homepage's own.
- **"On this page" nav, added (ruling 22, §2.3)** — five links, not in
  the hybrid at all: a twenty-screen phone page needs a way in without an
  accordion. With JavaScript the links scroll by script and leave the
  hash alone, so a held `#q=` survives a same-page jump and a share taken
  afterward doesn't lose the question; without it, a plain anchor jump —
  no question was ever held without JavaScript regardless.
- **Only four questions ship, not seven (⚠ real content gate, ruling 3 —
  storyboard §2.6c/d).** The hybrid showed all seven; the storyboard is
  explicit that the tradition's own three starter-draft questions "ship
  with four until cleared." Ruling 3 has not been cleared, so the three
  starters are cut here, not just visually deprioritized — verified by
  counting: 4 question `<li>`s, not 7. **Raising this to Mark now**: the
  three held-back questions are in the storyboard's own §2.6d if he wants
  to clear them and bring the page to seven.
- **The lexicon terms and breadcrumb links now carry a real 44px hit
  area (R-A4).** The reference measures the four lexicon terms at 29px
  tall and the breadcrumb links at 34px — named in the storyboard as "a
  build fix the verifier checks, not a property of the reference." Added
  a transparent `::before` on `.lex` sized `max(100%, 44px)` and centered
  over the button (extends the hit box without moving or resizing the
  visible dotted text), and gave the breadcrumb links `min-height:44px`.
  Verified by hit-testing actual coordinates 2–7px outside the visible
  text box (not just reading `getBoundingClientRect` on the visible
  glyphs, which would have missed the fix entirely) — dispatched clicks
  land on the button through 7px past its edge, and correctly stop
  landing on it at 8px, exactly matching the computed 44px box.
- **The Level-3 panel's "Full entry" control degrades correctly without
  JavaScript** (storyboard §2.10's no-JS row: "the card's Full entry
  control is not rendered — the build hides it without script rather
  than showing a dead control"). `<html class="no-js">` flips to `class="js"`
  via a one-line synchronous script at the top of `<head>`; `.no-js
  .lex-card .full{display:none}` hides the control until that flip
  happens. The rest of the lexicon grammar the hybrid already built
  (Level-2 shows on hover/focus by CSS alone, `aria-describedby` reaches
  assistive tech whether or not the card is painted, focus held open
  across the wrapper, Escape/× returns focus to the term) carries over
  unchanged — this was already reviewed and verified in D2/D3, not
  something this increment needed to redo.
- **`noindex` removed.** The hybrid mockup carried
  `<meta name="robots" content="noindex">`, correct for a sandbox file
  never meant to be found; the storyboard's own §2.2a explicitly plans
  for "seven indexed pages," so the real page should be indexable.
- **Real relative paths, corrected title/meta, no sandbox note, no
  visible draft tags** — the same fixes as Increment 1, applied here:
  paths now resolve from `traditions/` (one level up to `cic-website/`
  root); title "The House-Churches — Church in Conversation" and the
  description drafted for Chloe's instance, both from storyboard §S.6's
  pattern, replacing the hybrid's own differently-worded versions;
  `data-copy` attributes kept as invisible provenance, every visible
  `<mark class="draft">` removed; the palette matches the 2026-09-02
  change order (`#F6F6F2` / `#FFFFFF`) automatically, since the tokens
  were copied fresh rather than carried from the older hybrid file.

**Content otherwise carried verbatim from the record**, unchanged from
the hybrid where the hybrid was already quoting `records/pahc/*` and the
reviewer's brief: the five `honest_limit` silences (Chloe's is five, not
four — the guard-line silence makes a fifth, correctly counted against
the storyboard's own H-level outline), the two `doctrinal_witness` texts
and their four lexicon terms, the sources table, the seven gravities, the
contested list, the floor note, legacy and review-status sections, and
the four peer-review press questions. None of this is this session's
prose; it is the record's own words, arranged.

**Verified locally** (headless Chromium, no live preview): zero
horizontal overflow 320–1440px including the exact 1099/1100px
sidenote-float breakpoint; heading outline is one clean H1 → H2 → H2
(H3×5) → H2 → H2 → H2 (H3×8) → H2, no skipped levels; exactly 4 question
links, not 7; the lexicon grammar re-tested end to end — hover shows the
Level-2 card, click opens the Level-3 panel with focus moved to its close
button, Escape closes it and returns focus to the term, the 44px hit
extension verified by coordinate, not just by class name; the held-
question flow re-tested fresh (not on a same-document hash-only
navigation, which doesn't re-run the page's script — caught this test
artifact before trusting a false negative) — held block renders, all
four conversation links gain `#q=`, the edit link points back to the
homepage with the fragment; no-JS confirmed via `javaScriptEnabled: false`
— `no-js` class never flips, all four questions present, the "Full
entry" control absent, the panel stays `visibility:hidden`; zero
`target="_blank"` anywhere on the page.

**Open, unchanged by this increment:** ruling 3 (the three held-back
starter questions), ruling 34 (the app-side `#q=` change order), and the
six remaining tradition pages, each gated on ruling 4 until its own
record clears — none has a reviewer's brief on file except Desert Fathers
and Mothers, the Bethlehem Circle, and Syriac Christianity, per the
storyboard's own table; the other three (Alexandria, Cappadocia, Church
and Empire) would ship with §2.8's record section shortened, not
paraphrased, exactly as §2.10 specifies for that state.

---

## 2026-09-03 (later) — Change order: the Table becomes its own page

**What was raised.** Reviewing the built homepage and Chloe's tradition
page, Mark: "the mulit-voice should be stand alone with the table the
first place and a way to invite up to 3 worlds to the table, it should be
a chloe card and then find others, that gets confusing and sets chloe to
be the leader rather than joining the conversation (perseption) can we do
a cool graphic that opens the table and then gives you the worlds to
select." The individual-conversation path (Atlas, homepage chairs, each
tradition page's own "Begin" links) was affirmed as correct; the complaint
was specifically that the *multi-voice* entry point, as built, put one
tradition's card first and framed the rest as add-ons to it.

**Investigated before designing anything:**
- The app's actual Table contract (`cic-poc/frontend`, not assumed): a
  link of the shape `?worlds=id1,id2,id3&mode=table` pre-seats up to three
  traditions and lands on the Launch screen with "Convene the Table"
  enabled once ≥2 are filled — it never auto-starts a session (the app's
  own code comment: "the link chooses seats, the participant convenes").
  No app-side change needed; the website can build this link today.
- What "the open door graphic" referred to, when Mark pointed to it as the
  illustration to adapt: the existing "Arriving" brand mark
  (`Ministry/Communication/Brand-Assets/CiC_Logo_Arriving_Master.svg`), a
  ring with a doorway-gap and a dot "sitting down" at the threshold — not
  a separate, uncommissioned asset.

**Ruling, after Mark confirmed the shape** ("3 open seats and the
participant view as the fourth"): a new standalone page, `table.html`,
not in the original storyboard (§1's site map had "Set your own table" go
straight into the app). Four seats shown symmetrically: "You," already
seated at the mark's own threshold position, and three open doorways.
Picking a seat opens a chooser (all seven traditions, portrait + name +
tradition, already-seated ones shown disabled rather than hidden); two or
more filled seats enables a single "Open the conversation" link built
from the live selection. No tradition is ever cast as host — resolving
the perception problem directly, not just relabeling it.

**Built:** `cic-website/table.html`, and the storyboard now carries this
as new §2a (change order, full section — purpose, page order, the
chooser, hand-off behavior, states/screen-reader/keyboard/responsive,
open items). The site map (§ "Site map") updated to route "Set your own
table" through this page instead of straight into the app, and to show
each tradition page's "Bring {Name} to the Table" link doing the same.

**Two existing links rewired to point here instead of the app directly:**
the homepage's `.second-door` link (was
`https://cic-engine.onrender.com/?mode=table`, now `table.html`, `data-app`
removed since it no longer targets the app), and Chloe's page's two
"Bring Chloe to the Table" links (`#seat-bring`, `#door-bring`; now
`../table.html?worlds=post-apostolic-house-church`, same `data-app`/
`data-ask` removal). **Deliberate deviation from §2.2a's "all four
conversation links carry `#q=`" rule:** these two links no longer carry
the held question forward. A question held for one voice doesn't
cleanly address a table where that voice is no longer singled out;
forwarding it would re-seat the exact "one tradition speaks for the
room" framing this change order exists to remove. The other two links on
Chloe's page ("Begin a conversation with Chloe," `#seat-begin`/
`#door-begin`) are untouched and still carry `#q=`. Recorded in §2a
rather than left as a silent gap in §2.2a's rule.

**A bug caught in verification, not assumed fixed:** the chooser panel's
"← Leave this seat open" button used `hidden` to show/hide itself, but
`.panel .remove{display:flex}` had no `[hidden]` override — the same
class of bug as the homepage's `.era-nav` earlier this session. The first
functional-test pass read the `hidden` *attribute* and reported success;
only a screenshot of the chooser opened on an *empty* seat showed the
remove button rendered anyway. Fixed with `.panel .remove[hidden]{display:
none}`; re-verified with `getComputedStyle` on both the empty-seat case
(`display:none`) and the filled-seat case (`display:flex`), not the
attribute alone. Also caught and fixed separately: the arrival animation
screenshot was taken at 600ms, before the sequence (ring draws to 1400ms,
"You" seats in to 1800ms) had finished, making "You" appear to not exist
at all — a test-timing error, not a page bug; corrected by waiting 2000ms
before screenshotting.

**Mark's correction on seeing the first version:** "the circles need to
be centered on the 1/4 segment and sitting just outside the table (as if
at the table and make the table the same c that is the logo, not 4
segments, but three and an open 4th that the participant sits at, same
as the logo." The first build had drawn the ring as four separate dashed
arc-segments (one gap per seat, `stroke-dasharray` cycling four equal
dash/gap pairs) and placed the three open-seat circles at a radius that
put them mostly *inside* the ring's own band — reading as four notches
cut into the ring, each seat sitting in its own cut-out, rather than one
table with chairs around it. Corrected to match what was actually asked:
the ring redrawn as a single continuous arc (`<path>` with one `A` arc
command, not a dashed `<circle>`) — the logo's own unbroken "C," not a
segmented one — with exactly one gap, a quarter of the circle, centered
on the right where "You" sits (the mark's own threshold position, kept).
All four seats — "You" and the three open ones — recentered to sit just
outside the ring's outer edge (worked out by computing exact geometry
rather than eyeballing it: ring radius, stroke width, and seat-circle
size solved together so each seat clears the ring with a small margin and
still fits inside the graphic's own box with room to spare, at both the
280px desktop size and the 240px phone tier — verified the phone tier by
scaling every figure by the same 240/280 ratio rather than re-deriving it
independently, so the two tiers stay geometrically consistent). Seat
circles shrunk slightly (72px → 56px, 48px on phones) to make the outside
clearance work within the graphic's existing footprint rather than
enlarging the graphic itself, still well clear of the 44px hit-target
floor. Re-verified after the change: zero overflow at every breakpoint,
the full seat/chooser/convene functional suite unchanged and passing, and
reduced-motion's finished-state dasharray recomputed for the new (shorter)
arc length and confirmed by `getComputedStyle`, not assumed to still
match after the geometry changed.

**Verified locally** (headless Chromium): zero horizontal overflow
320–1440px on `table.html`; initial state (0 of 3, convene disabled);
seating a tradition updates the seat's portrait/tint, the live count, and
un-disables the tradition in other seats' choosers only once it's no
longer selected; a tradition already seated elsewhere shows disabled,
"Already seated," in a second seat's chooser; two seated traditions
correctly build `?worlds=id1,id2&mode=table` and enable "Open the
conversation"; removing a seated tradition empties the seat and
decrements the count; arriving at `table.html?worlds=id1,id2` pre-seats
both immediately with the convene link already live; reduced-motion shows
the finished ring and seated "You" with `animation:none` on every
animated rule, not just the resting-state values (the same fix this
session already had to make once, on the homepage's own mark — verified
this time rather than assumed carried over); dark mode legible; 390px
mobile lays out cleanly, graphic rescaled with seat positions
recalculated, not just shrunk; zero `target="_blank"` anywhere on the
page.

**Open:** ruling 35 (whether the Table ships free and prominent, as built
here, or behind a paid-tier gate — not yet ruled); whether to fold the
app's curated `pairings.ts` suggested-pairing shortcuts into this page as
a faster path than picking three individually (asked, not yet answered);
the SVG ring's gap centering is tuned by eye against the mark's own
geometry, not derived analytically — a fine first pass, revisit if Mark's
reaction calls for it.

---

## 2026-09-03 (later still) — The homepage's own table link plays the mark's motion

**Asked:** "now use the motion of the logo to draw attention to the
table, either when you first scroll down to it or click on it the first
time." Two trigger moments named; the click-triggered one already
existed — `table.html`'s own copy of the Arriving mark already plays on
arrival, so clicking through was already covered. What was missing was
the scroll-triggered one: the homepage's own "Set your own table" line
(`.second-door`, near the bottom of a long page) was plain text with no
visual weight, easy to scroll past without noticing it at all.

**Built:** a small copy of the header's own Arriving mark (same ring +
seat SVG, same `cic-buildC`/`cic-sitdown` keyframes) placed inside the
"Set your own table" link itself, id `table-cue`. An `IntersectionObserver`
(threshold 0.6) adds `.play` the first time it scrolls into view, then
disconnects — the same motion the header plays unconditionally on load,
now played once, on this link, at the moment a visitor actually reaches
it.

**A shared-component default had to flip, carefully.** The existing
`.arriving-ring`/`.arriving-seat` rules' un-animated default was the
*pre-draw* look (invisible ring, unsettled seat) — correct for the header
mark, which always carries `.play` from first paint and so never
renders that default (the animation's own `fill-mode:both` 0% keyframe
takes over from frame one regardless of what the base rule says). But
that same default would leave a *new*, not-yet-triggered instance
permanently invisible before its `IntersectionObserver` fires — worse,
permanently invisible with no JS at all, since this page has no
`no-js`/`js` class-flip to hook a fallback to (confirmed by checking:
unlike the tradition page and `table.html`, `index.html` never adopted
that pattern). Rather than bolt on a page-specific fallback, flipped the
shared component's own default to the resting/complete look, and added
`.arriving.pending` as the one opt-in exception — applied by JS only to
instances it's actually about to animate, immediately before observing
them. Verified the header mark's own animation timeline is byte-for-byte
unaffected by the flip (early frame still pre-draw via the keyframe's own
0%, late frame still fully drawn and seated) — the change was safe
specifically because the header's permanent `.play` class means the
default rule was never actually reaching the screen for it either way.

**Verified locally** (headless Chromium): before scrolling to it, the cue
carries `.pending` and its ring is invisible (`opacity:0`); scrolling it
into view swaps to `.play` and the same draw-and-settle motion runs,
ending at the same fully-drawn resting state computed by `getComputedStyle`
(not just checked by class name); with JavaScript disabled, the cue
renders its resting/complete state immediately — never the invisible
pre-draw look, so no dead icon without JS; under `prefers-reduced-motion:
reduce`, same immediate resting state, `animationName:"none"`, no
motion at all; zero horizontal overflow 320–1440px on the homepage with
the icon in place; zero page errors.

**Open, unchanged:** everything already open from the Table page's own
build above.
