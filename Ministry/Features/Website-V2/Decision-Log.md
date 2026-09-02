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
