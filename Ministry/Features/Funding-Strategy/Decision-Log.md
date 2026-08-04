# Funding Strategy — Decision Log

Dated entries. What was decided (or what's still genuinely open), the reasoning, and the
next action. This thread was dispatched by System Hub specifically to be a live, ongoing
exploration with Mark — not a background research task converging to a locked memo on its
own — so expect this log to accumulate real decisions gradually across many sessions, not
resolve in one pass. See `Business-Plan-Idea-Box.md` in this same folder for ideas
explicitly parked for a future comprehensive business plan, not decided here.

**Operating model, set explicitly by Mark 2026-07-22:** this thread runs on Sam Kaner's
Divergent → Groan Zone → Convergent process, not a straight line to a recommendation. A
conversation that starts to *sound* convergent (options narrowing, ideas tested against each
other) is still Groan Zone struggle, not actual closure — real convergence is a distinct
state Mark signals explicitly, not something to infer from tone. Entries below marked
"working," "for now," or "not yet decided" should be read as Divergent/Groan-Zone
snapshots, not commitments, unless a later entry marks them otherwise.

---

## 2026-07-22 — Thread launched; three funding-model families presented; conversation redirected twice by Mark toward what's real

**Launch:** dispatched from System Hub (`Ministry/Operations/Standing/Launch-Prompts/CiC_Funding_Strategy_Thread_Launch_2026-07-22.md`) per Mark's own request for a coherent funding strategy — not a tipping model vs. membership vs. free-tier decision made in isolation, but "a coherent strategy that funds the organization, allows for growth, and gives transparent access at some level to everyone." Explicitly required to run as live back-and-forth, not a background thread converging to a recommendation and handing it back — Mark corrected this directly once already, before this thread existed, on an earlier pass at the same question.

**Three model families opened the conversation** (Guardian-shaped voluntary giving, Hallow/Calm-shaped free-tier+membership, Khan-Academy-shaped free-for-individuals/paid-for-institutions) — not to pick one, but as concrete starting scenarios. The conversation did not converge on picking one; it moved past the three-family frame entirely once real constraints surfaced.

**Real user-behavior input from Mark, not yet validated by live data:** individual users likely show a spike-then-bifurcate pattern — a strong initial "this scratches an itch" reaction, then either real depth of engagement or drop-off into novelty-only use. Named as evidence against a recurring-subscription model for individuals specifically (bad fit for a spike-then-churn pattern) and toward either a one-time ask at the moment of the spike, or not monetizing individuals for predictable revenue at all.

**A load-bearing principle, stated plainly by Mark, that should govern every funding idea from here forward:** rigor and sourcing are the truth-telling itself and must never be gated for money — doing so would corrupt the project's own model, not just look bad. A genuinely additional service that costs real money to build and deliver beyond that core truth-telling is fair to charge for. This resolved the real tension this thread had been circling (does "academic mode" or deeper sourcing become a paywall) — it does not; new, separately-built services do.

**A real correction from Mark, worth preserving so it doesn't get silently re-litigated:** the previously-drafted institutional-funding groundwork (World Sponsorship, Church-Designated Fund, Seminary Alignment/Wabash-grant path) was drafted under the old, more idealistic posture and depends on a third party's yes on a third party's timeline — a church board, a grant committee, a faculty champion. Mark named this directly as repeating the same idealism-over-sustainability mistake that already drove the nonprofit-to-PBC pivot. Old drafted work stays useful as a source of ideas, not as the near-term plan. The project's own Go-Live Cost Model already agreed with this without anyone noticing: its monetization ladder puts individual, self-controlled moves first and treats institutional licensing as a parallel track running "on its own relationship clock," not the load-bearing plan.

**Found and dispatched, not fixed in this thread:** two `.docx` drafts in `Ministry/Funding/` (`CiC_World_Sponsorship_OnePager_V0_1_DRAFT.docx`, `CiC_Church_Designated_Fund_OnePager_V0_1_DRAFT.docx`) still promise tax-deductibility through a bridge-to-501(c)(3) mechanism that no longer exists post-PBC-pivot — missed by the 2026-07-21 nonprofit-to-PBC cleanup because that sweep ran on a repo-wide grep, which cannot see text inside a zipped `.docx`. Confirmed by cross-checking that cleanup's own completion log: all 43 files it touched are `.md` or `.html`, zero `.docx`. Dispatch prompt written and saved:
`Ministry/Operations/Standing/Launch-Prompts/CiC_System_Hub_Funding_Docx_TaxStatus_Fix_2026-07-22.md`.
Not yet run as of this entry.

**Payment mechanism — working decision, held as "for now," not treated as final:** stay with a direct Stripe integration on churchinconversation.com itself, per the path already set in `CiC_Go_Live_Cost_Model_V0_1.md`. Evaluated and set aside: Patreon (confirmed current real cost ~13–15% all-in vs. Stripe's ~2.9%+$0.30, built around episodic-content-unlock mechanics that fit a D&D actual-play show and don't fit CiC's non-gating values, weak organic discovery for a product with no pre-existing audience to funnel in). Ko-fi was evaluated favorably (0% platform fee on one-time gifts, no account required to give one, "tip jar" cultural framing arguably a better match for the spike-then-bifurcate individual behavior pattern than committed patronage) but Mark chose to hold the existing direct-Stripe path rather than adopt a third-party platform at this time. Open Collective noted only as a values-echo (public-ledger transparency matches CiC's own disclosure commitments) — not treated as a real structural candidate, likely an awkward fit for a PBC.

**Terminology — genuinely open, not decided.** Mark flagged real, current cultural backlash against "tipping" language (tip creep, forced-tip fatigue) as a reason to avoid that register entirely, not just the word "tip" — consistent with his own original framing at this thread's launch ("not called tips"). The project's own already-finalized ask copy already leans this way without it being named as a rule ("keep the Table open," "steward, not hero"). Candidate directions offered, none chosen: "Keep the Table open" as the primary verb rather than a caption, "Hold a seat," "Steward"/"become a Steward of the Table."

**A five-stream portfolio frame, introduced by Mark, not yet resolved in detail:** rather than one funding mechanism, explore multiple concurrent streams — (1) time-bounded free access + a paid membership unlocking more usage headroom and a new community layer, with a separate keep-it-open gesture alongside both; (2) segment-tailored paid add-ons (pastor/teacher, academic, homeschool/educator) built around the existing four-mode framework, never gating the modes themselves; (3) creative, non-institutional-relationship-dependent ways to fund scholarly validation (individual-scale crowd-funding per world, a distributed review panel instead of one expensive reviewer, coursework-based review, matching gifts); (4) other revenue not yet on any list (print products, Mark's own paid speaking/training, small mission-aligned equity investors — newly possible specifically because of the PBC/share structure); (5) products built on the 100+-world database itself beyond one-to-one conversation (a licensed research database, a published reference work, per-class/semester course licensing). Each stream generated real ideas; none has been decided or sequenced yet.

**One concrete idea from stream (5)/(2), refined live and then explicitly parked rather than developed further** — see `Business-Plan-Idea-Box.md` §1: a paid cross-tradition comparative brief for pastors/teachers, built from parallel per-tradition answers (not synthesis, not system-drawn conclusions) — Mark corrected an earlier draft of this idea that leaned toward "synthesis," and the corrected version is architecturally simpler and lower-risk than what was first proposed. Two retrieval approaches floated (manual pick from the Atlas, or a comparative search ranked by how strongly a theme appears in each world's own source material) — also parked, not decided.

**Open, unresolved, likely the next real thread to pull:**
- Which of the five streams to actually develop first, if any — nothing sequenced yet.
- Final terminology for the keep-it-open ask.
- Whether the "time-bounded free + membership" idea (stream 1) needs a concrete usage-cap number, or is still conceptual.
- Whether the docx tax-status dispatch has been run, and whether the Church-Designated Fund document's entire premise (not just its wording) needs retiring under the PBC structure — flagged in that dispatch, not resolved here.

**Next action:** Mark's call — this thread stays open and live per its own launch brief; no forcing function to converge exists here, and shouldn't be manufactured.

---

## 2026-07-22 (same day, continued) — "And, not or": the rigor-vs-charging tension reframed as compatible, not opposed; a layered tier structure emerging as a Groan-Zone candidate, explicitly not yet decided

**A standing correction from Mark, not scoped to this thread alone:** stop framing things as false oppositions ("X vs Y" / "X or Y") when a real "X and Y" structure exists — applies to how strategy gets reasoned about generally, not just public copy (which already had this rule). Saved to project memory as its own entry, linked to the existing brand-kit no-contrast-framing rule.

**Applied immediately to the rigor-vs-charging tension this log already recorded above:** it was never really an opposition. Paying can buy *more of the same honest access* (time), not a different or better tier of truth — "pay for some services and more access of our base model," not "access or pay for service." That reframing is why the tension dissolved rather than needing a side picked.

**A layered model taking shape from that reframing — a Groan-Zone candidate per this log's own operating note above, explicitly not decided:**
- Free, base: full access to the conversational model and the Atlas, same rigor, bounded only by time.
- Paid subscription: more time, and explicitly framed as covering real cost broadly — operations and development, not narrowly API usage.
- A deeper, higher-priced tier: more time again, plus role/function-specific features (pastor, academic, homeschool, the parked comparative-brief idea) — several such features could coexist, each adding value and income independently.
- A top tier: unlimited, everything.
- An institutional track, parallel to the individual ladder: multi-seat access for an institution's people, with time and relevant features scaled to that use.
- A giving layer running alongside all of it, pointed outward: more paid revenue funds more free-tier generosity, not just operating costs — plus a specific, nameable "help sponsor a world's review" channel, folding in the parked crowd-funded-world idea rather than running it separately.

**A new, real risk named by Mark, genuinely open, not resolved:** institutional partnerships aren't ruled out, but leaning too hard on any one institutional relationship risks real or perceived influence over content, or CiC being perceived as a single tradition's mouthpiece rather than neutral across traditions. Connected to, not separate from, principles already committed elsewhere: the World Sponsorship draft's "sponsorship confers honor, never influence" and the Seminary Alignment Analysis's own multi-tradition-tolerance criterion. The open question is whether that same principle needs a structural form at the institutional-partnership scale (multiple partners by design, public disclosure of who's funding what, a cap on how much revenue any one partner represents, something else) — not answered here.

**Next action:** Mark's call whether to pressure-test the institutional-balance question next, or continue testing the tier structure itself. Neither the tier model nor the institutional-balance question is decided as of this entry — both are live Groan-Zone material.

---

## 2026-07-22 (same day, continued again) — Staggered rollout sequencing; sponsorship confirmed as an ongoing parallel stream despite no tax-deductibility

**Sequencing added to the tier-structure candidate above, same "prove it before adding complexity" logic the Go-Live Cost Model's own giving ladder already used, now applied to the fuller structure:** launch with only the keep-it-open gesture plus a capped free-time allowance; add the "more time" paid tier once real usage and more worlds provide signal (or design it early so it's ready, without necessarily shipping it yet); add deeper tiers/institutional track later still, each gated on real signal rather than a fixed calendar. Not yet decided what "capped" actually means in hours/conversations — a concrete number, not just the concept, is still open.

**Sponsorship confirmed as a real, ongoing, parallel short-term revenue stream** — world rigor/review, extending free-tier time, and launch costs are all namable sponsorship targets. Explicitly not blocked by the PBC structure; a sponsor gets recognition and real effect, never a tax deduction, same honesty already committed to on the fixed `support.html`. "Sponsor a world's review" (already logged above) and "sponsor more free time for others" both instantiate the same "more revenue → more given away" flywheel concretely rather than abstractly.

**Next action:** unchanged — still Mark's call which thread to pull next; the launch-phase shape (gesture + capped time, nothing else yet) may be approaching real settlement but per this thread's own operating rule, that's for Mark to confirm, not to infer.

---

## 2026-07-22 (same day, continued again) — Sponsorship family expanded; a real, warm/relational funding channel named; an existing asset found (`Letter to Friends`)

**Sponsorship stream (logged above) expanded into named, distinct asks**, not one vague "help fund review" line: academic-review sponsorship, "make the next world available" (full construction+review+testing, echoing the existing $3,500 World Sponsorship figure), and "help a world gain academic standing" — the last one relational and ongoing (introductions, endorsement-seeking) rather than a one-time transaction.

**A new, distinct stream named by Mark: a direct, warm, relational ask** — explicitly not the after-experience gesture, not a self-serve website mechanism at all. Individual or institutional, angel money or partnerships, moved through Mark's own relationships and introductions rather than a stranger's self-serve decision. Real and parallel to everything else logged, not a replacement for it.

**Found, not built:** `Ministry/Communication/Church_in_Conversation_Letter_to_Friends.docx` already exists and is close to exactly this — warm, personal, explicitly "not a grant pitch," and already includes an organic version of the academic-standing ask ("introducing me to a scholar or a pastor who ought to see it"). Read in full 2026-07-22. Honestly stale, but not dangerously — it names only one world (pre-dates the other four going live), predates the adversarial safety testing already completed, predates the PBC pivot and the Faithways Studio name, and every cost figure in it is still a literal unfilled blank. Unlike the two files already dispatched to System Hub, it makes no tax-deductibility claim, so it carries no urgent-fix risk — just needs a real content refresh (voice and structure hold up fine) before anyone could actually send it. Refresh timing not yet decided.

**Next action:** Mark's call whether refreshing the letter moves now (a lever fully in his own control, unlike the slower institutional paths already set aside) or stays parked with the rest of this thread's open material.

---

## 2026-07-22 (same day, continued again) — Standing status set for every old funding/communication draft: source material only, never finished or influencing until reworked

**Mark's direct instruction, applied as a general rule, not a one-off:** every pre-existing draft this thread has touched or named — `CiC_World_Sponsorship_OnePager_V0_1_DRAFT.docx`, `CiC_Church_Designated_Fund_OnePager_V0_1_DRAFT.docx`, `Church_in_Conversation_Letter_to_Friends.docx`, and the still-unread `CiC_Seminary_Alignment_Analysis_V0_1_DRAFT.docx`, `CiC_Growth_Plan_V0_1_DRAFT.docx`, `CiC_Ministry_Funding_Strategy_v1_0.docx`, `CiC_Ministry_Proposal_Packet_V0_1_DRAFT.docx`, `CiC_Org_Funding_Bridge_Memo_V0_1_DRAFT.docx`, `CiC_Wabash_Pilot_OnePager_V0_1_DRAFT.docx` — is **source material only**. None of them are finished, none are authoritative, none should be sent, cited, or quietly allowed to shape a decision as-is. Each one either gets genuinely reworked and confirmed by Mark before any real use, or gets explicitly set aside and not used at all. A factual patch (like the tax-status fix already dispatched to System Hub) corrects an error — it does not promote a document to "finished." That distinction matters and shouldn't get lost once that dispatch runs.

**Next action:** none of these documents move without Mark's own explicit rework-and-confirm pass. Nothing currently queued.

---

## 2026-07-22 (same day, continued again) — Real reactions to the broader-access/org-health batch; the academic advisory circle sharpened into a three-jobs-at-once idea; a genuine sequencing challenge named

**Affirmed from the last batch (Business-Plan-Idea-Box §2):** broader-access ideas generally, with **translation/multi-language access added** as its own item — real, not folded into the others. The volunteer/contributor layer confirmed.

**The academic advisory circle promoted from "worth exploring" to "I really want to build this"** — and sharpened past what was first proposed: Mark wants it to actively build strategy and connections toward the best possible reviews, *and* to bring cross-traditions together for a purpose, not just supply counsel generally. Worth recording why this matters: a circle deliberately composed across traditions does three jobs at once — it's the ongoing mechanism for the validation-bottleneck problem (ongoing relationship, not a one-off paid engagement each time), it's a structural safeguard against the institutional-balance/single-point-of-view risk named earlier (built into the org, not a policy promise about one partner), and it's real organizational health (counsel and accountability without full board weight). Not yet designed — who, how convened, how compensated if at all — genuinely open.

**Correction, not a new decision:** the world-building method is already standardized and documented internally — the `L3B` Formation World Construction Framework and Blueprint docs are real and current. What's actually valuable and undone is narrower: extracting a donor-facing piece from that existing rigor, not documenting the method itself. A translation/editing task, not a documentation task.

**A real, named challenge, not yet resolved: ask coherence across the accumulating list of funding mechanisms.** Mark's own concern: multiple distinct asks shouldn't stack onto the same people in a short window. Working observation offered, not yet confirmed as sufficient: most of the mechanisms already on the table naturally map to different audiences (anonymous website visitors for the gesture/subscription tiers; churches/major donors for sponsorship; scholars for the advisory circle, recruited for expertise not money; volunteers for time not cash) — the real risk concentrates specifically in Mark's own personal network (the Letter to Friends audience), which could plausibly receive several overlapping asks at once. Mark's own three-part filter for narrowing going forward: fit with culture, fit with convictions, fit with actual likely funders — not yet applied systematically to the full list.

**Next action:** Mark's call whether to start mapping which ask belongs to which audience now, or hold that for later once more of the individual pieces (the advisory circle, the donor-facing L3B extraction, the refreshed Letter to Friends) are less new themselves.

---

## 2026-07-22 (same day, continued again) — Everything organized into a working map, not a new decision

**What this is:** all of the above — foundation, access ladder, revenue streams, cross-cutting features, governing principles, and the still-open struggles — organized into one reference document and a companion visual, so the whole shape can be seen at once. Per this thread's own operating rule, organizing/clustering is itself Groan Zone work, not a declaration of closure — every item in the map carries its real status (Working / Affirmed / Parked) rather than being flattened into "decided."

**Documents:**
- `Ministry/Features/Funding-Strategy/CiC_Funding_Strategy_Map_V0_1.md` — full text version, the source of truth.
- Companion visual artifact (published 2026-07-22) — same content, laid out as a map: foundation at the base, the access ladder with phase tags and funded-by lines, revenue streams grouped by which audience is actually being asked, cross-cutting features, governing principles, and open struggles, each item's status shown as a pill (solid = Working, outlined = Affirmed, dashed = Parked).

**Next action:** unchanged from the entries above — nothing here is more decided than it was; the map just makes the existing state legible at a glance.

---

## 2026-07-22 (same day, continued again) — Deep research dispatched (Opus, background) on business-plan structure, real comparables, and how to reach potential contributors within three hard boundaries

**Dispatched, not yet returned.** A background research agent (Opus model, per Mark's explicit request) was launched to research, not draft: (1) what a good business plan actually contains for a venture with this shape — mission-driven, solo-founder, low/no-capital, not chasing venture scale, a modest ~5-year exit horizon, rather than generic VC-plan guidance; (2) real case studies, successes and cautionary tales both — The Bible Project (the founder's own named inspiration), Khan Academy, Hallow, Calm/Headspace, and any real examples of mission-driven ventures actually damaged by debt, founder over-commitment, or investor control, plus financing mechanisms compatible with the boundaries below (revenue-based financing, capped crowd-equity, PBC-specific mission-related investment); (3) how to structure a document meant for actual potential contributors (donors, mission-aligned small investors, institutional sponsors), not a VC pitch deck.

**Three absolute boundaries given to the research, stated by Mark and non-negotiable, not just preferences:**
1. No debt of any kind.
2. No large cash outlays from Mark personally.
3. No giving away influence to any partner or investor who wants it — governance control, content-approval rights, or veto power over editorial/theological integrity are all out of bounds.

Briefed with everything already worked out in this thread (the tier ladder, the named revenue streams, the Academic Advisory Circle, the unresolved institutional-balance tension, the funder-landscape finding that most grants are 501(c)(3)-gated) so the research builds on real prior work rather than generic startup advice. Instructed explicitly to flag, not quietly omit, anything it finds that would cross one of the three boundaries.

**Next action:** none until the agent returns. Its output is research and synthesis to react to, not a plan to adopt — same Groan-Zone discipline as everything else in this log.

---

## 2026-07-22 (same day, continued again) — Research returned: `CiC_Business_Plan_Research_V0_1.md`

**Status: material to react to, not decided.** Full report saved and published in full (per this
project's standing rule that documents Mark develops are shown whole, not summarized) —
`Ministry/Features/Funding-Strategy/CiC_Business_Plan_Research_V0_1.md`.

**Findings load-bearing enough to flag here, not just in the report:**
- **Gifts to the PBC are not tax-deductible, confirmed** — extends, not just repeats, the docx
  tax-status finding already dispatched to System Hub. Fiscal sponsorship (partnering with an
  existing 501(c)(3) to receive earmarked deductible gifts) surfaced as a real, not-yet-explored
  option specifically for the academic-review/world-building costs.
- **Revenue-based financing is flagged as likely violating the no-debt boundary** despite being
  marketed as "not debt" — a real trap worth knowing about before it looks attractive.
- **Etsy losing its B Corp status to activist shareholders after its IPO**, and **Family Christian
  Stores / Crystal Cathedral both filing bankruptcy under debt even after major debt forgiveness**,
  are concrete, well-documented precedent for boundaries 3 and 1 respectively — not hypothetical
  caution.
- **A genuinely new idea, not previously on the map:** Khan Academy's Khanmigo AI-cost problem was
  partly solved by a donated-compute partnership (Microsoft/Azure) — in-kind infrastructure
  sponsorship is a boundary-safe way to lower the AI-cost floor, worth adding as its own line
  alongside the sponsorship family already logged.
- **A perpetual purpose trust (the strongest mission-lock tool) directly conflicts with the
  ~5-year sale horizon already named** — it's built to make a company unsellable. A lighter
  golden-share/charter-provision approach was flagged as the better structural fit, with the
  Academic Advisory Circle named as already functioning as a soft version of the same protection.
- **BibleProject confirmed as a 501(c)(3), not equity-funded** — validates the warm/crowdfunded
  instinct already central to this thread, but runs on a tax status CiC doesn't have; the
  asymmetry is real, not just a technicality.
- **Recommended document genre: a "case for support," not a VC pitch deck or lender's business
  plan** — concrete structure given in the report (case summary → model/theory of change →
  proven history → vision → tiered ask).

**Next action:** Mark's reaction — nothing here is adopted; per this thread's own rule the
agent's closing synthesis is explicitly offered as a recommendation to react to, not a conclusion.

---

## 2026-07-22 (same day, continued again) — Correction: run by Mark and his wife, not a solo founder; Faithways Studio's parent/product structure clarified

**Real correction, not a new decision:** Church in Conversation is run by Mark **and his wife**,
not a solo founder — "solo founder" language used earlier in this thread, including in the brief
given to the research agent, is inaccurate and should not be repeated in future work without
this correction.

**Structural clarification, deliberate by design:** Faithways Studio, Inc. is the parent PBC;
Church in Conversation is a product/system inside it, not identical to the entity. Set up this
way on purpose for optionality — room to build other platforms under Faithways Studio later, or
to reposition Church in Conversation specifically as a nonprofit down the road if that better
serves the mission. Mission restated plainly by Mark: "provide safe places to explore faith and
the story of Jesus."

**Confirmed, not a course change:** no IPO, no major-tech-lane growth trajectory — already the
direction everything in this thread and the research pointed toward (the research's own
recommended genre, "case for support" not a VC pitch deck, already assumed this).

**One real addition to the value-stability picture:** the parent/product structure is itself a
mission-protection asset the research's golden-share suggestion didn't know about — if CiC ever
needed to move away from a for-profit shape to protect the mission, that's a pre-built option,
not an emergency restructure. Sits alongside, not in place of, the cultural and light-structural
layers already logged.

**Next action:** none required; correction on the record for any future work (research briefs,
documents, decision-log entries) to build from accurately.

---

## 2026-07-22 (same day, continued again) — Research rerun dispatched (Opus, background), corrections folded in, two new threads added

**Dispatched, not yet returned.** A second background research agent (Opus) was launched to
produce a complete, standalone V0.2 of the business-plan research — not a delta — correcting the
solo-founder framing and the Faithways Studio parent/product structure throughout, and adding two
new research threads V0.1 never had grounds to cover: (A) how family/couple-run mission-driven
ventures actually differ from solo-founder ones in credibility, succession, and exit framing; (B)
whether the flexible-parent/repositionable-product structure (Faithways Studio hosting Church in
Conversation, with a built-in option to convert CiC to a nonprofit later) is a recognized pattern,
what actually converting a for-profit product to an independent nonprofit involves in practice,
and how it should reshape the mission-protection question (golden share vs. this built-in
escape-hatch — different tools for different scenarios, not redundant).

Also instructed to revise, not just footnote, V0.1's founder-story guidance and any place it
assumed single-person governance, and to state "no IPO, no venture-scale growth trajectory" as
its own explicit boundary alongside the three financial/control ones.

Same three absolute boundaries carried forward unchanged: no debt, no large personal cash outlay
(now: from Mark and his wife), no influence given away.

**Next action:** none until the agent returns. Will be saved as `CiC_Business_Plan_Research_V0_2.md`.

---

## 2026-07-22 (same day, continued again) — V0.2 returned: `CiC_Business_Plan_Research_V0_2.md`

**Status: material to react to, not decided.** Full report saved and published in full —
`Ministry/Features/Funding-Strategy/CiC_Business_Plan_Research_V0_2.md`. V0.1 stays in the repo as
a dated record; V0.2 replaces it as the current report.

**Findings load-bearing enough to flag here, not just in the report:**
- **The couple structure reads as a credibility asset for this audience, not a liability** — the
  literature's cautions about married co-founders are specifically growth-equity investors'
  objections, i.e. the exact capital source the boundaries already exclude. For a contributor
  audience, two accountable principals answers the real fear ("will this outlive one person?")
  better than a solo founder can.
- **A real, clean precedent exists for converting CiC to a nonprofit later: the Salt Lake
  Tribune** — new charity formed, IRS 501(c)(3) approval, then the for-profit owner donated the
  operation into it. Real mechanics, not exotic; three genuine watch-items (asset/IP valuation,
  §337(d) tax on appreciated value — cheaper the earlier it's done, and private-inurement risk
  since Mark and his wife would stay involved, managed via an independent board and reasonable
  compensation).
- **Important clarification, not previously distinguished:** the modest continuity sale (~$2M,
  ~5 years) and converting CiC to a nonprofit are **mutually exclusive endings**, not both
  available at once — a charity's assets can't be distributed back to founders for personal gain
  once converted. The parent/product structure is what keeps both doors open **until a choice is
  made**, not a way to have both endings simultaneously.
- **The golden-share idea and the conversion option are complementary, not redundant** — one
  protects the mission while CiC stays a for-profit that might take outside equity; the other
  protects it by exiting the for-profit shape entirely. The conversion option does reduce the case
  for a heavier perpetual purpose trust, since it already serves as the ultimate backstop without
  freezing the exit.
- **BibleProject itself is a two-person partnership, not a solo founder** — an independent,
  unprompted validation of the couple-run frame.
- **A fourth boundary now scored explicitly:** no IPO / no venture-scale growth trajectory — added
  to the financing-mechanism table alongside the original three; mainly tightens the equity-
  adjacent rows (Reg CF, SAFE, mission-related investment) rather than excluding anything new.

**Next action:** Mark and his wife's reaction — nothing here is adopted; same Groan-Zone
discipline as the rest of this log.

---

## 2026-07-22 (same day, continued again) — Case-for-support drafting begun, one section confirmed, paused to return to strategy

**Real progress, held as in-progress, not final:** working one idea at a time per Mark's own
request, the document's first section — "Why Under a PBC Umbrella" — went through several live
edit rounds (dash removal and other AI-tell cleanup; personal ministry background from Mark and
Susan woven in without naming others negatively; an accountability paragraph added covering the
real annual-benefit-report requirement and the locked mission clause; explicit framing that the
PBC is the right structure "for now," not a permanent ideological choice). Saved to
`Ministry/Features/Funding-Strategy/CiC_Case_For_Support_DRAFT_V0_1.md`. Hope Over
Crisis/LDI-China specifics deliberately left out — on the Task Board for later, not urgent.

**Paused at Mark's request** to return to the broader strategy conversation. Document structure
follows the research's recommended genre (case summary → model → proven history → vision →
tiered ask) — only the PBC-umbrella section exists; the rest is unstarted.

**Next action:** none on the document until Mark returns to it.

---

## 2026-07-22 (same day, continued again) — Market-analysis research dispatched (Opus, background): conversion rates, contribution amounts, tier benchmarks

**Dispatched, not yet returned.** A third background research agent (Opus), narrower and more
data-focused than the two business-plan reports — Mark's own framing: what percentage of people
actually contribute, how much, and what additional services correlate with what price tiers,
across real comparable models. Briefed with everything already anchored in this thread (Wikimedia's
donor-behavior figures, BibleProject's ~$20/mo average patron, Hallow's tier pricing, Khan
Academy's AI-cost-driven $4/mo add-on, Ko-fi's fee structure) and asked to go deeper and verify
rather than re-derive — specifically told to check the Wikimedia "2% conversion" figure against a
primary source, since it's been load-bearing in this project's cost projections without a fresh
check. Also asked to research The Guardian's reader-revenue data and NPR/public-radio membership
conversion as close comparables to CiC's own free-stays-free, ask-after-value model.

**Next action:** none until the agent returns.

---

## 2026-07-22 (same day, continued again) — Market analysis returned: `CiC_Market_Analysis_Contribution_Rates_V0_1.md`

**Status: material to react to, not decided.** Full report saved and published in full —
`Ministry/Features/Funding-Strategy/CiC_Market_Analysis_Contribution_Rates_V0_1.md`.

**Findings load-bearing enough to flag here, not just in the report:**
- **The Wikimedia "2%" figure this project's own cost projections have been leaning on is banner
  marketing, not a measured rate** — verified against the actual 2022 banner copy. The real
  visitor-to-donor math (8M+ donors against 1B+ annual readers) implies a true rate well under
  1%. The one Wikimedia figure that *is* solid: 75%+ of donors give on their first or second ask,
  conversion collapses after ~10 exposures — timing matters more than the raw percentage.
- **A defensible planning range: 2–6% of the whole free base ever contributes anything, anchored
  conservatively at ~2%** — triangulated independently from freemium industry data, Wikipedia's
  own stated rate, and Calm's pre-2021 conversion rate, before Calm gutted its free tier. Against
  an *engaged* (returning, invested-time) subset specifically, real comparables (NPR loyal ~10%,
  a niche patron platform ~13%) suggest real upside — but only for that subset, never the whole
  base. Open question, not resolved: should projections run against the whole free base or a
  defined "engaged user"?
- **Real validation for the already-suggested giving amounts:** $10 one-time lands almost exactly
  on Wikimedia's actual average gift ($10.05). $8/month recurring sits in the dense middle of the
  real market band and matches NPR+'s own $8/month benefit threshold exactly — though NPR
  attaches real perks at that price and CiC's version is deliberately benefit-free by design, a
  distinction worth being conscious of, not treating as an oversight.
- **Calm's own history is a direct, real data point on the free-tier commitment:** they raised
  conversion from 2% to 7% specifically by gutting free content from ~90% of their library down to
  ~5%. This validates, with real numbers, that never degrading the free tier is genuinely in
  tension with a higher conversion rate — and that the resolution modeled by Guardian/Wikipedia/
  BibleProject is reach and right-skewed giving carrying the weight, not a higher conversion rate.
- **The "same content, higher tier = recognition, not more stuff" pattern is real and proven**
  across Substack, Patreon, Guardian, and BibleProject — direct validation that the keep-it-open
  gesture is a proven mechanic, not an untested hope.

**Next action:** Mark and Susan's reaction — same Groan-Zone discipline as the rest of this log.

---

## 2026-07-22 (same day, continued again) — Partial convergence: `CiC_Business_Roadmap_V0_1.md`, at Mark's own explicit signal

**Real convergence, not another divergent pass — Mark named this transition himself** ("it's time
to converge partially"), per this thread's own operating rule that only he can declare it.
Synthesized everything already established (the tier/revenue map, both business-plan research
passes, the market analysis) into one simple, five-phase roadmap for building the business, with
the program's own build-timing folded in as a dependency rather than the main subject.

**Saved and published:**
- `Ministry/Features/Funding-Strategy/CiC_Business_Roadmap_V0_1.md` — full text, source of truth.
- Companion visual artifact — five phases (Go Live → Learn → Build the Second Rung → Deepen → The
  Structural Choice), each showing program and business tracks side by side where both apply, with
  the still-genuinely-open items (final gesture wording, the exact capped-time number) flagged
  rather than smoothed over.

**Explicitly not everything converged — a few real items still open, named in the roadmap itself:**
final terminology for the keep-it-open gesture; the concrete number behind "capped" free time.
Phase 5 (the modest-sale vs. nonprofit-conversion fork) is deliberately left as a future trigger,
not a scheduled date — both doors stay open until Mark and Susan actually choose.

**Next action:** Mark and Susan's reaction to the roadmap as a whole — this is "partial"
convergence per Mark's own word, not a claim that every open thread in this log is now closed.

---

## 2026-07-22 (same day, continued again) — Real cost data ($1.25–1.50/hour) confirms prior estimates; free-tier time cap deliberately deferred to pilot data, not projection

**Real testing result, not an estimate:** actual measured cost is **$1.25–1.50 per hour of
conversation**. Cross-checked against this thread's own prior per-conversation estimates
($0.20–0.75 at a 15–25 min average conversation length) — consistent, not a surprise; the new
number just replaces a wide guess with a tested one, in a cleaner unit for tier design.

**Recalculated against budget levels already anchored in this thread:** the go-live ceiling
($100–150) buys ~67–120 hours of total conversation; the $243/month and $375/month variable-
budget scenarios buy ~162–194 and ~250–300 hours respectively; the $8/month subscription buys
~5.3–6.4 hours — a genuinely large step up over a modest free cap, not a marginal one.

**Decision: the free-tier time cap will be set from real pilot data, not a pre-launch
projection.** Mark and Susan's own call. The real cost rate gives the *method* (budget ÷ rate ÷
target audience) but the actual number waits for the pilot. What the pilot needs to surface to
make that call well: real average conversation length, the real usage distribution (whether the
"spike then bifurcate" pattern named early in this thread actually holds at real scale), and real
spend velocity. `CiC_Business_Roadmap_V0_1.md` and its companion artifact updated in place —
Phase 2 now states this explicitly as a deliberate deferral, not an unresolved gap; Phase 3 is
where the number actually gets set.

**Next action:** none until pilot data exists. The market-validated $10/$8 giving amounts and the
tier structure itself are unaffected by this — this only sharpens the free-tier cap and the
subscription tier's real value, both already flagged as open in the roadmap.

---

## 2026-07-27 — Faithways Studio, Inc. actually incorporated (real this time); a stale wrong ID found spread across 11 files, correction dispatched

**The entity is now genuinely real, confirmed two ways, not just an on-screen claim like the
earlier failed attempt:** Entity ID 20261918758, Status "Good Standing," Form "DPC-PBC" (confirms
the Public Benefit Corporation election itself was captured, not just a generic profit corp),
Formation Date 07/27/2026 — verified via an actual email receipt and a public-record search.
Everything this thread's own documents have said about "Faithways Studio, Inc., a Colorado Public
Benefit Corporation" is now literally true, not aspirational.

**What led here:** the prior registration attempt (Entity ID 20261874960) never actually
completed — an on-screen verification with no receipt ever issued, later traced by the Secretary
of State's office to a likely address mismatch. Mark refiled from scratch, working through it
live with real-time guidance on each step of the Colorado online form, including catching before
submission that the Article III/IV/V/VIII/IX content (the actual public-benefit purpose and the
4/5-of-shares mission-lock protection) had no home in the standard form fields and needed to be
uploaded as an "Additional Provisions" attachment — a real near-miss caught at the Filing Review
step, not after submission.

**A real, wider correction found and dispatched, not fixed inline:** the old, wrong ID had already
spread into 11 files across the project — decision logs, the Task Board, Dashboard, both Gantt
files, the website README, two launch-prompt files, and — the two that matter most — the PBC
Bylaws/Organizational Resolutions and the IP Assignment Agreement, both real operative legal
documents. Dispatch written and saved:
`Ministry/Operations/Standing/Launch-Prompts/CiC_System_Hub_Entity_ID_Correction_2026-07-27.md`,
reusing this project's established three-bucket convention (dated history gets an addendum, not a
rewrite; live trackers get corrected directly; the two legal documents get real individual review
for whether any operative date was set assuming the earlier, false incorporation actually
happened — a sequencing question, not just a number swap). Not yet run as of this entry.

**Next action:** none in this thread — the correction belongs to System Hub. Worth noting for
this thread's own record: the foundational assumption underneath every document built here
(the Business Roadmap, both research reports, the case-for-support draft) is now confirmed
accurate, not provisional.

---

## 2026-07-27 (same day, continued) — The two real legal documents corrected directly; a genuine sequencing problem, not just a stale ID

**Read both in full before touching anything, per the dispatch's own instruction not to blanket
find-and-replace.** Both `CiC_PBC_Bylaws_and_Organizational_Resolutions_V0_1.md` and
`CiC_PBC_IP_Assignment_Agreement_V0_1_DRAFT.md` turned out to have exactly the sequencing risk
flagged as a possibility: both explicitly dated the corporation's own existence to July 21, 2026 /
Entity ID 20261874960 — the filing that never completed. The Bylaws/Resolutions' Step 1 is Mark
acting *as incorporator*, and Step 2 (board action) is the specific paragraph authorizing bank and
Stripe account setup — both invalid if dated before the entity actually existed. The IP
Assignment's entire effective-date clause was explicitly conditioned on that same false date.

**Corrected in place, both with a dated correction note preserved (not silently erased) — Mark's
confirmed go-ahead.** Both now read July 27, 2026, Entity ID 20261918758. Dispatch note updated to
mark this bucket done, so System Hub doesn't duplicate the work when it runs the remaining 9-file
correction.

**Real next step, not a document-editing one:** confirm whether either document was already
physically signed with the old, wrong date — if so, both need to be re-signed with the corrected
date before being relied on for opening the bank/Stripe accounts, since that authorization lives
in the Organizational Resolutions' Step 2 specifically. Answers this thread's own opening
question this session: yes, fix and re-sign these two before bank setup — not all eleven files,
just these two.

**Next action:** Mark's own confirmation of signing status, then bank/Stripe setup can proceed.

---

## 2026-07-27 (same day, continued) — Both legal documents re-signed with the correct date and Entity ID; clear to open bank/Stripe accounts

**Confirmed by Mark: both re-signed.** Clean, corrected PDFs generated (reportlab, verified by
reading them back before sending) and signed fresh in Kdan PDF — Bylaws & Organizational
Resolutions (Step 1 alone; Step 2 both Mark and Susan as Directors) and the IP Assignment
Agreement (Mark, both as Assignor and as President for Faithways Studio, Inc.). Old signed copies
based on the false July 21 filing were deleted rather than archived — no external party had relied
on them yet, and the correction note already embedded in both documents' text is the record of
what happened and why.

**This fully answers the question that opened this whole detour:** yes to resigning these two
specific documents, no to the other nine (narrative/tracking only, corrected via the separate
System Hub dispatch, not signed instruments). Bank and Stripe account setup is now unblocked —
Step 2 of the Organizational Resolutions is the actual authorization for both accounts, and it's
now validly signed with a date the corporation actually existed.

**Two small items worth knowing about, both already named in the resolutions just signed, not
new:** the $40 total cash consideration for the shares ($20 each) still needs to actually change
hands to make the issuance fully paid — natural to handle right alongside opening the new
account. And the resolutions direct the President and Treasurer to send each shareholder a short
written notice of the uncertificated share issuance, including the PBC disclosure required by
C.R.S. § 7-101-505 — a real but small, self-serve step, not urgent.

**Next action:** Mark's own — open the bank/Stripe accounts.

---

## 2026-07-27 (same day, continued) — Relay bank application walked through; "Church in Conversation" trade name (DBA) filed and paid, receipt received

**Relay application:** walked through live, screen by screen, same pattern as the state filing —
industry set to "Subscription and Membership," business description used Faithways Studio's own
Article III purpose language ("to create safe spaces to explore faith and the story of Jesus,"
Mark's own correct call, not the narrower product-description first suggested), both Mark and
Susan set up as genuine co-owners (the reason Relay was picked over Novo in the first place, per
this project's own prior decision). Colorado's public business search independently checked and
confirmed showing Faithways Studio, Inc. in Good Standing before the application, clearing the
index-lag issue that stalled the attempt before. EIN's July 21 issuance date checked and confirmed
not a substantive problem — the application's actual content (name, address) matches reality; only
Bylaws/Resolutions, IP Assignment, and Shareholder Agreement had the deeper structural dependency
on the false date, already fixed.

**Trade name filed, not just reserved.** Caught before it cost time: Mark was initially on the
wrong CO SOS form (Statement of Transfer of Reserved Name, which only moves a name hold, not a
real DBA registration). Correct form — Statement of Trade Name of a Reporting Entity, filed
against Faithways Studio's own entity record — confirmed via live web search before proceeding,
filled out, submitted, paid ($25), and receipt received. "Church in Conversation" is now a
registered trade name of Faithways Studio, Inc.

**One connected step still open, not done automatically by the state filing:** add "Church in
Conversation" as a DBA on the Relay account itself, now that the trade name is real — the bank
needs this separately from the state to allow checks/payments under that name. Confirmed
structurally: a future second program could either operate directly under "Faithways Studio" with
no new filing at all, or get its own separate trade name the same way, any time — nothing about
today's filing limits that.

**Next action:** add the DBA to the Relay account; otherwise this thread's real-world execution
work (entity, EIN, three legal documents, bank, trade name) is now complete and consistent.

---

## 2026-07-27 (same day, continued) — Relay live; the $40 share purchase actually paid, shares now fully issued

**Confirmed by Mark:** Relay account open, and the two $20 stock-purchase transfers (Mark and
Susan) have cleared, $40 total. Per the Organizational Resolutions' own terms, receipt of this
amount is what makes the 7,000,000 shares validly issued, fully paid, and non-assessable — not
just documented, actually complete. Today's payment date is the real issuance date for IRC §1202
holding-period purposes going forward.

**One remaining connected step, already named in the signed resolutions, now live:** the
President and Treasurer are directed to send each shareholder a short written notice of the
uncertificated share issuance (C.R.S. § 7-106-207), including the PBC disclosure required by
C.R.S. § 7-101-505, "within a reasonable time" after issuance — that clock starts now that payment
has actually cleared. Offered to draft it.

**Next action:** draft and send the shareholder notice; add the DBA to Relay (still open from the
prior entry). Once both are done, the full real-world formation/funding execution chain this
thread has walked through live is complete.

---

## 2026-07-27 (same day, continued) — Correction: the $40 transfers are pending, not cleared; notices held until they actually clear

**Not yet final — flagged by Mark before anything got signed.** The two $20 transfers are the
first ones on the brand-new Relay account, and first transfers commonly take a few days to
process. The earlier entry's "the $40 has gone through" was premature. Same discipline as the
incorporation-date lesson earlier in this thread: don't date or sign a document against an event
that hasn't actually completed. Both notice drafts (and their PDFs) are held unsigned until the
transfers actually clear; Mark will confirm the real clear date, and the notices get finalized
with that date, not today's.

**Next action:** wait for transfer confirmation, then finalize and sign both notices with the
real date.

---

## 2026-07-27 (same day, continued) — Next: a Stripe integration on the website for three ask types

**Mark wants to move forward on:** (1) the keep-it-open/pay-it-forward gesture — already fully
designed in this thread (market-validated $10 one-time / $8 recurring, non-tipping terminology
direction); (2) academic-review sponsorship — already named as part of the sponsorship family;
(3) "resource material" — not yet defined in this thread, needs clarifying with Mark before
scoping.

**Real scope question, not yet resolved:** this thread's own launch brief set an explicit
boundary — "no code changes to `cic-poc/` or `cic-website/` from this thread... building follows
once a direction is actually confirmed, same gate every other major decision in this project has
gone through." A direction is now genuinely confirmed (amounts, terminology posture, and
principles are all real, decided work from this thread), which is exactly the trigger condition
that boundary named for handoff — but whether that means dispatching to System Hub/a build
thread, or building directly here, hasn't been decided. Flagged back to Mark rather than assumed.

**Next action:** clarify "resource material," then decide build location (dispatch vs. direct).

---

## 2026-07-27 (same day, continued) — Updated technical cost study dispatched (Opus, background), grounded in the real codebase, not web research

**Dispatched, not yet returned.** Mark wants the giving amounts re-examined against current real
costs before building the Stripe integration — a real, grounded technical analysis, not another
market-comparables pass. Scoped to four numbers: cost per transaction (one message turn, every
model call that fires per turn), cost per conversation broken out by Living Table size (1, 2, 3
Representatives), cost per hour, and current verified model pricing — all anchored against the
real tested $1.25–1.50/hour figure as ground truth, with any bottom-up deviation from that range
required to be explained, not smoothed over. Instructed to read the actual `cic-poc/backend/app/`
code (config.py, graph/nodes.py, table_discourse.py, message_cap.py, usage_logging.py) rather than
estimate generically, and to check for real logged usage data if `usage_logging.py` captures any.

**Next action:** none until the agent returns. Closes with a recommendation on whether $10/$8 and
the free-tier time-cap approach still hold against the real cost structure — a recommendation to
react to, same discipline as every other research pass in this thread.

---

## 2026-07-30 — Cost study returned: `CiC_Cost_Study_Per_Transaction_V0_1.md` — the $1.25-1.50/hr figure traced and corrected; table size, not time, is the real cost driver

**Status: material to react to, not decided.** Full report saved and published in full —
`Ministry/Features/Funding-Strategy/CiC_Cost_Study_Per_Transaction_V0_1.md`.

**A correction to this thread's own prior record, not a criticism of anyone:** the $1.25–1.50/hour
figure this thread treated as fresh real testing traces back to this same Decision-Log's own
2026-07-22 entry — itself an arithmetic back-derivation from an earlier per-conversation estimate,
not a direct measurement. A separate, later, more authoritative source (System Hub's own decision
log, 2026-07-24) already corrected this to **~$2/hour** based on real partial data, before this
thread's $1.25–1.50 figure was ever cited back to me. The codebase-grounded bottom-up math in the
new report reconciles with ~$2/hour for 1:1, not with $1.25–1.50.

**The real, load-bearing finding: cost does not scale mainly by time — it scales by Living Table
size.** A 3-Representative conversation costs roughly 2.5–3× a 1:1 conversation per turn, driven
by governance/classifier overhead as much as extra generation calls. The report's own
recommendation: keep the market-validated $10/$8 giving amounts as-is, and make **table size**,
not a time budget, the actual lever the free tier governs — it's the real cost driver, needs no
new metering (table size is already capped and chosen at session start), and avoids reopening the
already-validated giving amounts.

**Two time-sensitive items, independent of that recommendation:**
- **The Sonnet 5 introductory price expires 2026-09-01** — a ~37% blended cost increase arrives
  automatically, currently unbudgeted anywhere in this project's funding documents.
- **The cost baseline is stale and has one real gap** — no 2-Representative conversation has ever
  been measured; a full re-run (already scheduled elsewhere as pending) would close it cheaply.

**Also found, not this thread's to act on:** a real technical cost bug (Desert's response-length
ceiling triggers a full duplicate Sonnet generation on most turns) and a cheap, already-identified
fix (extend the prompt-cache TTL from 5 minutes to 1 hour, which would eliminate most of a
measured 61% cold-cache penalty at realistic human conversation pacing) — both worth passing to
whichever thread owns `cic-poc` engineering.

**Next action:** Mark and Susan's reaction — same Groan-Zone discipline as every other research
pass in this thread. The Stripe build conversation (paused above pending this study) can resume
once there's a reaction to react to.

---

## 2026-07-31 — Real Groan-Zone work on "$2 to $0.50": the Answer Bank's real limitation found, a genuine architectural idea surfaced live, cost-reduction feasibility study dispatched

**Mark named a hard viability threshold:** if blended cost can't come down from ~$2/hour to
roughly $0.50/hour, the project doesn't work at the already-validated giving amounts. Worked
through the real levers live rather than reassuring or despairing:

- **The Answer Bank's real limitation, found by reading the actual code and its own design
  doc:** it serves only ~5.2% of real interactions, not because the space of real questions is too
  varied, but because it matches by *position in a scripted question sequence* (role/set/order),
  not by meaning — only ~1/3 of participants choose that entry path, and any free-text deviation,
  even a near-exact paraphrase, falls through to a full-cost live call.
- **Mark's own correction, technically sound:** since this project's local embeddings are already
  free (zero API cost, confirmed in the prior cost study), the same infrastructure could plausibly
  match an incoming question's *meaning* against a curated answer bank regardless of wording or
  entry path — reframed correctly by Mark as predictive cost-preparedness, not a curriculum
  feature. Real quality risk named and taken seriously, not waved off: distinguishing a "canned"
  feeling from a genuine mismatch, with pre-generated (not live) response variations as a real,
  zero-marginal-cost mitigation worth testing.

**Cost-reduction feasibility study dispatched (Opus, background)** — five items, the
semantic/predictive answer-bank redesign as the lead item, plus the cache-TTL fix, Sonnet prompt
size and the Desert regeneration bug, Haiku call consolidation (flagged to protect safety-critical
checks specifically), and the September 1 pricing change as context for every estimate. Explicitly
scoped to say what needs real testing rather than guess at outcomes.

**Next action:** none until the agent returns. This directly gates the paused Stripe/website
build conversation — the giving amounts and free-tier design may need to wait on this answer.

---

## 2026-08-02 — Feasibility study returned: `CiC_Cost_Reduction_Feasibility_Study_V0_1.md` — $0.50/hour looks reachable for 1:1, structurally not for the Living Table

**Status: material to react to, not decided.** Full report saved and published in full —
`Ministry/Features/Funding-Strategy/CiC_Cost_Reduction_Feasibility_Study_V0_1.md`.

**The headline finding: the cache TTL fix alone, directly measured (not modeled), takes a
reflective-pace 1:1 conversation from $0.77/hour to $0.50/hour.** A one-line code change (5-minute
cache window → 1-hour), no behavioral risk, found via a real experiment already sitting in the
existing baseline data (one conversation had a genuine cache-lapse turn that cost nearly double,
$0.066 → $0.128). Stacked with a second real, already-diagnosed engineering fix (a response-length
regeneration bug affecting most or all worlds, not just Desert, root-caused to the prompt never
telling the model its actual word limit), the 1:1 target is reachable through low-risk engineering
alone, before touching anything uncertain.

**The Living Table remains structurally 2–3× the threshold regardless of optimization** — a
3-Representative table does 2–6 Sonnet generations and 45–60 Haiku calls per participant message,
by design, not by inefficiency. No caching or consolidation closes that gap. This independently
confirms, with real evidence this time, the standing recommendation: table size, not time, should
be what the free tier governs, with 1:1 as the free experience.

**Mark's semantic answer-bank idea is architecturally sound and cheap — and directly conflicts
with the project's own prior design decision.** The existing Answer Bank design doc explicitly
recommends against inference-based serving matching, on values grounds (never serve a paraphrase).
The study proposes a genuine "and": apply semantic matching at a tap-to-see suggestion layer, never
auto-serving, preserving the "explicit tap = signal" guarantee while still capturing free-text
traffic. Offered as a proposal, not a resolution — flagged back to Mark since it disagrees with
this project's own prior reasoning, not something to decide unilaterally. Also found: the Answer
Bank currently serves 0% of real traffic today (the bank file doesn't exist, no UI built) — the
5.2% figure was always the designed ceiling, never a current rate.

**Time-sensitive:** September 1 pricing (+35% blended) is real but the cache fix roughly cancels
it out for 1:1. Worth a quick check: if the "$2/hour" figure came from real billing, it was billed
at introductory rates, meaning real usage could hit ~$2.70/hour post-September — changing the gap
from 4× to ~5.4×, though the reachability conclusion for 1:1 doesn't change either way.

**Next action:** Mark and Susan's reaction — same Groan-Zone discipline as the rest of this log.
This also unblocks the paused Stripe/website build conversation, since the free-tier design
question (time-based vs. table-based) now has real evidence behind an answer.

---

## 2026-08-02 (same day, continued) — Mark rescinds the Answer Bank design doc's "do not build inference-based serving matching" recommendation

**Real correction, not a reading of tone.** The prior recommendation against inference-based
serving matching, recorded in `Ministry/Features/Guided-Questions/
CiC_Answer_Bank_Full_System_Design_V0_1.md` §3.4, was not Mark's own settled decision — he's
explicitly rescinding it now: *"that is exactly what we need."* Semantic/inference-based matching
is the live, endorsed direction for the Answer Bank going forward, not a ruled-out option.

**Not yet resolved: how far.** The feasibility study's own proposal — semantic matching surfaced
as a tap-to-confirm suggestion, never auto-serving, preserving the "explicit tap = signal"
guarantee — was built as a compromise around a rule that no longer applies. Whether Mark wants
that same tap-confirm shape anyway (as good design, independent of the now-lifted rule), or wants
to explore full auto-serving once the threshold-calibration testing the study proposed actually
happens, is open — asked directly, not assumed.

**Flagged, not yet done:** the design doc itself still states the old "do not build" recommendation
as its core conclusion. That document belongs to the Guided-Questions feature thread, not this one
— worth a correction note there (same "record what changed and why, don't silently rewrite"
convention as everywhere else in this project) whenever that thread is next active, or sooner if
Mark wants it done now.

**Next action:** Mark's call on auto-serve vs. tap-confirm (or explicitly "figure that out via the
testing already proposed"); the Guided-Questions doc correction can wait or happen now, his call.

**Decided, same day:** auto-serve, hidden — no participant-visible indication a match occurred or
that any answer might be prepared rather than live. Real consequence flagged, not a pushback on
the decision: with no tap-confirm step, there's no human check between a bad match and the
participant, which makes the study's proposed threshold-calibration test (near-zero false-positive
rate on the labeled paraphrase/near-miss set) and blind tone-comparison test load-bearing gates
before this ships, not optional validation. Guided-Questions doc correction still pending, timing
still Mark's call.

**Rollout philosophy decided, same day:** test in the real pilot rather than an offline
calibration study first — real usage over projection, consistent with how this thread has treated
every other open number. Two safety rails added, not as a delay but as what makes "test in pilot"
actually reviewable rather than just hopeful: launch with a conservative, high-confidence-only
match threshold (loosen later from real data), and log every match decision silently regardless of
UI state, so real mismatches can be reviewed directly rather than waiting only on participants to
say something.

---

## 2026-08-02 (same day, continued) — Build scope dispatched: cache fix, regeneration fix, and the Answer Bank redesign, bundled as one cost-reduction handoff

**Dispatched, not yet run.** `Ministry/Operations/Standing/Launch-Prompts/
CiC_Cost_Reduction_Build_Scope_2026-08-02.md` — the full, confirmed output of this thread's cost-
study arc, ready to hand to wherever `cic-poc` build work actually happens (this thread stays out
of that code per its own launch brief). Three items: the cache TTL fix (lowest risk, do first,
directly measured to take a reflective-pace 1:1 conversation to the $0.50/hour target on its own);
the response-length regeneration bug (root cause found, remedy already scoped, needs live testing
before shipping); and the Answer Bank redesign (hidden auto-serve, pre-generated variations with a
re-word-never-re-content guardrail, conservative launch threshold, full match logging, tested in
pilot per Mark's own call). The Guided-Questions design-doc correction is named explicitly as
still owed, not silently left inconsistent with the live decision.

**Next action:** none in this thread — implementation is the build thread's job now. Worth
watching for when it lands: real pilot data on match/mismatch rates, and whether the cache/
regeneration fixes actually close the gap to $0.50/hour the way the feasibility study predicted.

---

## 2026-08-02 (same day, continued) — Stripe setup: payment methods confirmed; "donate" wording still open

**Payment methods decided.** Individual giving flow (the keep-it-open gesture, and the future
$8/month tier): cards, Apple Pay, Google Pay, and Link — all free to enable in the same Stripe
integration, chosen for friction reduction over fee optimization at this scale. Explicitly not
enabled: ACH/bank debit (friction outweighs fee savings for a casual small gift), PayPal (skip
unless actually requested), Buy Now Pay Later (never — undercuts the steward-not-hero voice
entirely), crypto. USD only for now. **Institutional payments are a different, later fork** —
ACH/wire via Stripe Invoicing, built when the institutional-licensing tier (Phase 4) actually
opens, not part of the current setup.

**"Donate" wording — real answer given, not yet chosen between options.** Confirmed: "donate"
does not legally or inherently imply nonprofit status (political contributions, GoFundMe, Twitch,
Ko-fi all use it without deductibility) — the real risk is the same reasonable-expectation issue
already fixed once on `support.html`, not a legal one. If "donate" is used, it needs the same
plain non-deductibility disclosure already established elsewhere in this project, nearby. The
already-finalized "keep the Table open" language sidesteps the question entirely and doesn't need
a disclosure to feel complete. Neither chosen yet — flagged as open, not decided.

**Next action:** Mark's call on the wording; payment methods are ready to hand to whichever build
work actually wires up Stripe.

---

## 2026-08-02 (same day, continued) — Optional name field, anonymous by default

**Decided.** Givers can optionally share their name; nothing required beyond what Stripe itself
needs to process the payment (receipt email, etc.) — anonymous is the default, no friction added
for anyone who wants to stay private. One optional, warmly-framed field ("Your name (optional) —
let us know who to thank"), genuinely skippable, not a data-collection form. Distinguishes
Stripe's own unavoidable baseline transaction data from this deliberate, participant-initiated
field — only ever offered, never extracted.

**Next action:** none — ready to hand to the Stripe build work alongside the payment-methods
decision above.

---

## 2026-07-27 (same day, continued) — A third signed document found with the same false-date problem, missed in the original sweep

**Not caught in this thread's original 11-file scan — found via System Hub's own parallel work on
the dispatch, which this thread hadn't seen the results of yet.** `CiC_PBC_Shareholder_Buy-
Sell_Agreement_V0_1_DRAFT.md` (the Shareholder Agreement between Mark and Susan) was signed by
both, both dated 7/21/2026 — the same false predicate as the other two. Its own text doesn't cite
the wrong entity ID directly (nothing to correct in the wording, unlike the IP Assignment), but
the signatures themselves predate when the corporation and the shares it governs actually existed.

**Clean signable PDF generated and sent** — `Faithways_Studio_Shareholder_Agreement_SIGNABLE_
2026-07-27.pdf`, text unchanged, ready for both signatures with the correct date. Old signed copy
(dated 7/21/2026) to be deleted the same way as the other two, no external reliance yet.

**Next action:** Mark and Susan re-sign this third document, then all three (Bylaws/Resolutions,
IP Assignment, Shareholder Agreement) are consistently and correctly dated before bank/Stripe
setup proceeds.

**Confirmed signed, same day.** All three foundational documents — Bylaws & Organizational
Resolutions, IP Assignment Agreement, and now the Shareholder Agreement — are re-signed with the
correct July 27, 2026 date and Entity ID 20261918758. Nothing left blocking bank/Stripe setup.

**Next action:** Relay application (bank) — fund with $40 total ($20 each), watch for the CO
public business-search index to catch up before/during the application. Same live, screen-by-
screen walkthrough offered as with the Secretary of State filing, whenever Mark starts it.

---

## 2026-07-22 (cross-reference from System Hub, not a decision made in this thread)

Mark told System Hub directly: *"we can put a hold on the funding strategy and support gifts for
phase one of the launch, lets make that the first thing we do after we have feedback from several
participants."* Recorded here so this thread has the context whenever it resumes — not a new
strategy decision, and nothing above is undone by it. Concretely: `support.html` was pulled from
site navigation for Phase 1 (kept on disk, not deleted — see its own header comment). This
thread's own "Go Live" phase in `CiC_Business_Roadmap_V0_1.md` should be read against this
sequencing when work here picks back up. Full account: System Hub Decision Log, 2026-07-22.

---

## 2026-07-31 (cross-reference from System Hub, not a decision made in this thread)

**The 2026-07-22 hold above is lifted.** Mark confirmed directly to System Hub that Phase 1
feedback exists and gave the explicit go-ahead to build SH-9 (Stripe for contributions) live,
not just prep it dark. System Hub flagged the hold before proceeding rather than assuming it
no longer applied, since the original instruction was recorded here specifically so it
wouldn't be silently overridden — Mark's answer was direct: build it live.

**Built:** a real Stripe Checkout integration (one-time and recurring gifts, both, in one
pass — see Part B of the doc below on why not sequenced), `support.html` restored to site
navigation on every page, and the account-setup steps only Mark can do written up as a
checklist. Full account, including the two wording adaptations made and flagged (not silently
decided) and everything still genuinely open (final gesture terminology, unchanged from this
log's own earlier entries):
`Ministry/Features/Funding-Strategy/CiC_Stripe_Setup_Wording_Strategy_Logistics_V0_1.md`.

**Not yet live** — the code ships "off until configured" (same discipline as `app/auth.py`),
so nothing charges anyone until Mark completes the Stripe account/webhook/env-var checklist in
that doc's Part C. **Next action:** Mark's own Stripe dashboard work; nothing here needs this
thread's further input until that's done and real data exists to react to.
