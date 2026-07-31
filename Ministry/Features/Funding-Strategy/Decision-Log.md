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
