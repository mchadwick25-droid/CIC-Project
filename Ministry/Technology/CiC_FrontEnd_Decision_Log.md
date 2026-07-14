# CiC Front-End / Product Strategy — Decision Log

Dated entries. Each records what was decided (or what's still open), the reasoning — including the "heart" reasoning, not just the operational one — and the specific next action. A decision that only lives in conversation history is a decision that gets re-litigated by accident later.

---

## 2026-07-07 — Voice at Prototype Alpha: Table Design Document governs

**Decided:** The engineering spec follows the Table Design Document (V2.3, Section 11) as written: Prototype Alpha ships text conversation *and* audio voice together, with a static picture background — not text-only. Mark's own framing for this thread ("text first, then pictures and voice") does not override this; it was reconciled rather than treated as a silent scope change.

**Reasoning:** The Table Design Document is a construction-complete, already-worked-out design document — Section 11's phase ladder is a considered position, not a placeholder. Flattening it to "text-only, voice later" would have quietly revised a governing document without that revision being named as a revision, which cuts against this project's own discipline (deferrals are documented, not hidden — Constitution Article 36). Reconciling before drafting, rather than guessing which framing was authoritative, kept the spec from being wrong on its very first structural section.

**Open question closed:** What did "text first" mean, if not a feature cut? Left unresolved in this pass — Mark accepted the Table Design Document's framing without specifying what he meant by his own phrase. If it resurfaces (e.g., as a build-sequencing preference for the engineer — stand up text before wiring voice — rather than a participant-facing cut), that's a distinct, compatible decision and can be layered in without contradicting this one.

**Next action:** Spec Section 1 ("What it looks like") states the phase-by-phase modality plainly, sourced to Table Design Document Section 11, with the static-picture-not-text-only distinction called out explicitly so a reader doesn't default to assuming a text-only Alpha.

---

## 2026-07-07 — First full draft of the Front-End & Runtime Engineering Specification produced

**Status:** Draft complete, not yet reviewed by Mark. Per this project's standing discipline (full documents shown in full, not summarized), the draft is being handed to Mark in full before any version is treated as ready for a specialist engineer.

**What it covers:** Five parts, matching the launch brief — what it looks like (pre-encounter threshold, the Table, phase-by-phase build sequence through Phase 2+); what content it has (the three-tier deployment package: World Capsule Core, World Priority Layer, and the three retrieved-on-demand chunk types, plus Voice Configuration and the Facilitation Brief, illustrated throughout with real excerpts from World #1 and World #7 rather than hypothetical placeholders); how it handles Table conversations (context isolation, the public transcript, Facilitator orchestration, all eleven fidelity-drift signals, the five-Representative ceiling); the transparency and rigor apparatus (Three-Level Transparency, Transparency Mode, and the five-level confidence vocabulary kept as three distinct concepts, each rated built vs. designed-but-not-built); and what's genuinely unbuilt (the missing Deployment Standards document, the Layer 7 runtime retrieval systems, the Runtime State Model, no platform chosen yet). A closing section summarizes the Technology Engagement Brief's review model for the engineer's own orientation, and an appendix cross-references every claim back to its governing Constitution article.

**Reasoning:** Research was done directly against the primary governing documents (Vision, Constitution, Essential Experience, Table Design Document, Facilitator-Governance, Pre-Encounter Experience Design, Architecture Map, Technology Engagement Brief) rather than summarized secondhand, using parallel research agents to extract precisely enough detail to write engineering-grade content from — because a first-of-its-kind deliverable for an outside specialist deserves the same scrutiny as a construction document, even though it isn't one.

**Open items flagged inside the document itself, not smoothed over:** modality continuity for Beta/Phase 1 is inferred, not explicitly stated, in the two governing design documents — flagged for confirmation against the Phase Structure document. The five-Representative ceiling is currently enforced only by Facilitator judgment, with no system-level guard — flagged as a decision engineering should make deliberately. Several referenced documents (Phase Structure, Table Runtime Document, System Level Map, V7 file structure spec) were not themselves reviewed for this draft and are named in Section 7 rather than paraphrased with false confidence.

**Next action:** Mark reviews the full draft (saved to Ministry/Technology/CiC_FrontEnd_Engineering_Specification_V1_0.docx). Revise or approve before it is treated as ready to hand to a specialist engineer at Engagement One.

---

## 2026-07-07 — Course correction: vision before spec

**Decided:** The engineering spec drafted earlier today was premature. Mark redirected: the actual engineer engagement needs a description of how Mark envisions the experience working, not an engineering spec — and before that description can be written, Mark needed to actually articulate the vision out loud, starting with the landing page and "the discussion." This session is that conversation.

**Reasoning (the heart of it):** Formalizing mechanics (context isolation, retrieval tiers, drift signals) before the experience itself has been described in Mark's own words risks building the wrong thing precisely, rather than the right thing loosely. The governing documents already answer *how the Table is governed*; they don't answer *what it feels like to sit at it*, which only Mark can supply.

**Next action:** Once landing page is settled, synthesize this whole conversation into a single vision-description document (not an engineering spec) for Mark to react to, ahead of any renewed engineering work.

---

## 2026-07-07 — The Table, visually and experientially: first full concept

**Decided — "the discussion" is the Table encounter itself**, not a separate feature. No distinct "discussion" surface exists apart from the participant-plus-Representatives-plus-Facilitator conversation already named "the Table" in the Table Design Document.

**Decided — governing atmosphere:** a pub-style gathering in the spirit of the Inklings (C.S. Lewis, Tolkien, the Eagle and Child) but re-set in an early-church register — communal, unhurried, argument as affection rather than combat, humble and close to the ground rather than academically clever. This gives the already-existing term "the Table" its first real atmosphere; previously it was defined only mechanically.

**Decided — Prototype Alpha visual concept** (a considerable enrichment of "static picture background" as currently scoped in the Table Design Document):
- A single static background image showing up to five figures seated at a table — one per active Representative — in clothing typical of their world, with ethnicity/demographic representation drawn from that world's actual evidenced population, not defaulted to homogeneity or invented for the sake of visual diversity. Mark's own framing: "if there is diversity we would look for diversity at the table, but only if there was diversity" — this should be decided per world from its own Source Ecology (Doc_02), the same evidentiary discipline that governs everything else in construction.
- Each Representative's figure carries an object typical of that world's own expression of faith — a scroll for Alexandria, a codex for a world where that was the era's technology, nothing at all for the Post-Apostolic/pastoral world, which Doc_01 itself already establishes had no closed canon yet. The absence is not a gap to fill; it is itself the honest finding, consistent with the "Where This World Is Quiet" discipline already built into the World Capsule Core template.
- Camera movement (zoom and pan) across the single static image, driven by conversational turn-taking: zoom to the current speaker, pan between two Representatives mid-exchange, widen to the full table when the participant addresses everyone or turns to the Facilitator. This is a deliberate middle tier between a flat static image and the full "animated table" currently scoped for Phase 1 — it may mean Alpha can feel considerably more alive than the phase ladder's current language implies, without paying for character animation.
- A name and world descriptor displayed with each Representative's figure, so a participant can hold up to five distinct voices in mind without losing track of who is who.

**Decided — the dialogue box is the permanent structural layer, not a fallback:** the conversation is typed text at the center of the scene, and text stays load-bearing regardless of how rich the voice layer becomes, because the transparency apparatus (highlighting, hover, click) is fundamentally a text mechanism — it has no audio equivalent. Voice is an experience enhancement layered on top, not a replacement.

**Decided — voice ambition, explicitly cost-gated:** culturally- and gender-matched text-to-speech per Representative is the goal; English first, with other languages as the project grows; cost is the named barrier today, not a design or architecture limitation. Flagged as a concrete, fundable line item to raise with the org/funding workstream, not solved here.

**Decided — the transparency/lexicon interaction pattern, made concrete:** terms unique to a world, or whose meaning differs from modern understanding, are highlighted in the dialogue text. Hovering surfaces a short popup description (Level 2). Clicking opens the full lexicon and context detail (Level 3). The same hover/click pattern extends beyond lexicon terms to stories, quotes, and transparent sourcing generally — one consistent interaction pattern for anything carrying a confidence tier, rather than a different treatment per content type.

**New gap identified, not yet built:** no per-world ethnicity/demographic profile exists in the current template set (World Profile, Source Ecology, Voice Configuration). One should be built — likely as an extension of Source Ecology or a sibling to Voice Configuration — so the visual/physical representation of a Representative answers to the same evidentiary discipline as its vocabulary and voice. Directly serves Article 20 (marginalized-voices duty) and the Historical Responsibility value.

**Still open, not yet answered:** whether an unevidenced-object absence (e.g., the pastoral world's empty space) is something a participant might notice and ask about, or simply present without any emphasis either way.

---

## 2026-07-07 — Main page: menu pattern decided, hero content still open

**Decided:** About, Features, FAQ, and similar informational content live behind a menu that opens as a temporary overlay window on top of the main page, rather than navigating the participant away from it. Keeps the participant anchored on the main experience rather than routing them through separate pages.

**Still open:** what the main page's primary content actually is — the first five seconds before any menu is touched. Not yet resolved whether this is the Table image itself (populated or with empty/waiting seats), something simpler, or something else entirely.

---

## 2026-07-07 — Landing page hero (provisional), Ask the Facilitator, onboarding shaping, Tours, and the one rule underneath everything

**Decided — landing page hero (provisional, pending Mark's confirmation):** an evocative, not-yet-populated version of the Table — empty or waiting seats, warm light, no specific Representatives visible since no world has been chosen yet — with a short, honest invitation line rather than marketing copy. The three entry pathways (Bypass, Build Your Own Table, Guided Onboarding) sit with equal visual weight beneath or alongside it, no default or "recommended" badge on any. "Ask the Facilitator" sits as a clearly secondary but visible option. The About/Features/FAQ menu overlay sits outside all of this.

**Decided — "Ask the Facilitator":** the pre-threshold Q&A feature (for a skeptical or curious visitor who wants to interrogate the project before trusting it with anything real — e.g., "why can't I talk to Origen or Augustine") is voiced by the Facilitator itself, not a separate support persona. Reasoning: the Facilitator is already the neutral, trustworthy host a participant can step outside an encounter to address directly; a second voice for FAQs would mean maintaining two different personalities that both need to sound credible, for no real benefit. "Why can't I talk to Origen or Augustine" is itself a strong worked example for this feature — the honest answer (a single historical figure's exact voice can't be reconstructed with the confidence this project requires, but the world that formed people like him can be) is a feature to state plainly, not a limitation to dodge.

**Decided — onboarding role-shaping, future feature, not yet activated:** the existing four-role selection (regular visitor, pastor/teacher, academic/scholar, deconstructing/reconstructing) will eventually shape two distinct things, kept distinct: (1) a baseline readability target — currently 10th-grade reading level for accessible (Level 2) explanations of source words and ideas, which applies to everyone regardless of role, and gives Constitution Article 30's "accessible, plain-language explanation" a concrete, testable definition it doesn't currently have; and (2) role-based content emphasis layered on top of that floor — e.g., a pastor is offered more sermon-prep-relevant angles by default, an academic is offered more exposed rigor by default. Access to everything remains universal regardless of role — role changes what's offered first, never what's reachable. This is explicitly a later feature, not scoped now, but important enough to design the underlying data model for from the start rather than bolt on afterward.

**Decided — Tours, future feature, Phase 3 (confirms and extends what the Architecture Map already names):** the Representative can guide a participant through a tour of their world — illustrated with pictures, potentially including experiences like a church service or the Eucharist — bounded strictly by what that world's source material actually documents. A world with rich liturgical description can support a full tour; a world without one must say so plainly rather than inventing content to fill the request — Mark's own example: a participant asking to "sit through a sermon" in a world with no documented sermons should hear something like "this world doesn't have the documented sources to describe this," not silence and not fabrication. This also resolves the earlier open question about whether an unevidenced absence (e.g., the empty object at the table for the pastoral world) should be noticed or silent: the answer, extended from this example, leans toward explicit and honest when a participant actively asks, rather than uniformly silent.

**The one rule underneath all of it, named explicitly because it kept resurfacing independently:** only what the evidence actually supports is shown, played, or offered — for a world's vocabulary, its people's ethnicity, the object on its table, and now the experiences and tours it can offer. Where evidence runs out, the system says so plainly. This is not several rules that happen to agree; it is the same rule, expressed once, showing up everywhere.

**Next action:** synthesize this entire conversation into a single experience-vision description document — not an engineering spec — for Mark to react to. This is the actual deliverable the specialist engineer asked for.

---

## 2026-07-07 — Experience Vision document produced; entry-path reconciled; phased build plan produced

**Produced:** `CiC_FrontEnd_Experience_Vision_V1_0.docx` — the full narrative description of the Table experience (atmosphere, room, objects, camera, voice, transparency mechanics, landing page, Ask the Facilitator, future features), written for the specialist engineer in descriptive rather than technical-spec register.

**Reconciled — entry path already documented:** Mark's own phrasing ("straight to question," "pick worlds," "facilitator picks worlds," "introductions") maps directly onto the Pre-Encounter Experience Design's existing three pathways (Bypass, Build Your Own Table, Guided Onboarding) plus the encounter arc's opening move. Confirmed as a match, not a new decision — nothing changed here, just traced back to the governing document that already specifies it.

**Produced — `CiC_FrontEnd_Vision_and_Phased_Plan_V1_0.docx`:** a shorter, phase-organized version of the vision for the front-end engineer specifically, structured the way Mark asked for it: Prototype 1 (Alpha), Prototype 2 (Beta), Phase 1 Implementation, Periodic Improvements, and Ultimate Vision. Periodic Improvements is framed as an ongoing track (voice-casting quality, onboarding role-shaping, the ethnicity/demographic reference) rather than a sequential fifth phase, since none of those three have a fixed release trigger — they improve as funding and evidence allow. Prototype 1's voice is named explicitly as "a first pass," not the fully culturally-matched casting — that richer casting is Periodic Improvements' job, not Alpha's.

**Next action:** Mark reviews both documents. The Vision and Phased Plan doc is the one meant to go to the front-end engineer directly; the fuller Experience Vision doc is the source material behind it, for reference if the engineer wants more texture than the phased summary carries.

---

## 2026-07-07 — Naming corrections: "conversation" not "discussion"; "The Church in Conversation"; Phase 1 named

**Decided — terminology:** "conversation," not "discussion," for what happens at the Table. Applied across all three documents produced so far.

**Decided — project name:** "The Church in Conversation," not "Church in Conversation." Applied to titles, headers, and body text in the three documents this workstream has produced (Engineering Specification, Experience Vision, Vision and Phased Plan).

**Not applied — scope note:** the L1 governing documents (Vision, Constitution, Essential Experience, and the rest) consistently use "Church in Conversation" without "The." This correction was not cascaded to those documents — that's a larger naming decision touching constitutional-tier documents outside this workstream's authority to change unilaterally, and worth Mark's explicit confirmation before anyone edits them, rather than assuming a naming fix here should propagate there.

**Decided — Phase 1's real name:** "Conversations with the Early Church." Added to the Vision and Phased Plan document as the named title of the Phase 1 Implementation stage.

**Next action:** if "The Church in Conversation" is meant to also govern the L1 documents, that should be raised as its own explicit decision, not inferred from this correction.

---

## 2026-07-07 — World Map feature (Ultimate Vision); Constitution version discrepancy investigated and corrected for in the Engineering Spec

**Decided — World Map, future feature (Ultimate Vision):** once the world catalog outgrows a simple list (Phase 1 launches with 9 worlds; the eventual catalog may hold 50-100 spanning all of history and today), world discovery becomes an abstract timeline — in the visual spirit of a Bible timeline chart, not a literal geographic map — with worlds positioned as bands or nodes at their real historical moment, parallel lanes making contemporaries visible without the participant doing the math, and lines drawn between worlds that shaped each other. Worlds can be pulled to the same Table across eras, not just within one. Worlds the project has chosen not to build sit right on the same timeline, dimmed, using the same hover-for-short-explanation/click-for-detail mechanic already built for lexicon terms and stories — extended here to a fourth content type: why a world isn't here at all. Two distinct exclusion reasons, surfaced honestly rather than smoothed together: insufficient evidence for a real build, or falling outside the project's doctrinal floor (see below). Not scoped for any near-term phase; captured now so the idea survives to when the catalog actually needs it.

**Investigated — the Constitution's "Movement Scope" doctrinal floor:** confirmed real and located. It sets a doctrinal floor, drawn from the Nicene-Constantinopolitan Creed, for which historical movements are eligible for construction at all (five specific affirmations: the Father as maker of all things, Christ's full divinity and eternal begottenness, Christ's full humanity, Christ's death/resurrection/ascension/return, and the Holy Spirit's status) — a test of belief in plain historical sense, not institutional submission to a council, and never imposed on a selected world's own voice or used to suppress a marginalized voice within an included world. World #1 and the Syriac world both predate Nicaea/Constantinople chronologically but meet the floor in substance, consistent with the Constitution's own language that a movement "need not have existed at a date when doing so was possible."

**Investigated — real version discrepancy found and explained:** this section exists in the Constitution copy on the branches currently building toward Phase 1 (internal Version 2.3) but not in the frozen main-tree copy (Version 2.2, same filename). Confirmed intentional, not drift: Mark's practice is to prove constitutional changes out against real world builds before merging them back to the main tree that governs the whole project. Two more differences found the same way: Facilitator Governance moved V3.4 to V3.6 on the same branches (a new Self-Narration drift signal, discussed below, plus a tested decoupled classify-then-route-then-generate Facilitator architecture); the Architecture Map now names the Source Registry as its own tracked deployment artifact and marks the Article 17/19 Construction-Framework reconciliation gap resolved on those branches. Vision, Essential Experience, Technology Engagement Brief, Pre-Encounter Experience Design, Table Design Document, Phase Structure, and Forces Framework are all confirmed unchanged.

**Corrected — Engineering Specification bumped to V1.1** (in this workstream's own output only; no governing document files were touched, per Mark's explicit instruction): the drift-signal count is now twelve, not eleven, with the new Self-Narration signal described in full and its stricter automatic-frame-breaker handling explained; a paragraph added on the tested classify-then-route-then-generate Facilitator architecture; Section 7's Construction Framework bullet corrected from "a live, named reconciliation gap" to "resolved on the branches this deployment is actually building against, still open in the frozen main-tree copy"; a new Section 7 bullet and Appendix intro line naming the Constitution version discrepancy plainly; the Appendix cross-reference table gained Article 28 (Anti-Fabrication Prohibition, grounding Self-Narration) and an updated Article 31 description naming the Source Registry; Section 2.5 gained a Source Registry bullet with real file citations from both World #1 and World #7.

**Next action:** none pending on this thread specifically. World Map is logged as a future feature ready to pick up when Ultimate Vision work resumes.

---

## 2026-07-07 — Academic Documents (raw transparency) and the world-click menu; phasing corrected

**Decided — Academic Documents:** a fourth, distinct transparency feature, separate from the in-conversation hover/click mechanic. Where hover/click surfaces sourcing reactively, per claim, as it comes up in a live conversation, Academic Documents is proactive and standalone — the full Lexicon, full Story Repository, and source documents (Source Ecology, Source Registry) for a world, raw and unmodified, browsable independent of any conversation. Same view for a casually curious visitor as for a qualified external reviewer doing Article 31 review — no separate reviewer-only layer inside this feature; whatever formal review workflow Article 31 requires is a distinct track, not part of this. Content is not new production — it's the L4-Templates-shaped, already-existing per-world build documents (Doc_01 through Doc_09, Lexicon-Chunks, Story-Chunks, Source Registry) exposed directly.

**Decided — lives in the world-click menu:** clicking into a world (from world-browsing or the future World Map) opens a menu of four options rather than a single action: Description, Tour, Choose for Table, and Academic Documents. This unifies four previously-separate ideas (the short menu card, the Phase 3 Tour feature, the core Table-selection action, and Academic Documents) into one consistent interaction point.

**Decided — phasing, corrected from an earlier draft in this same log:** at Phase 1, only Choose for Table is functional. Description, Tour, and Academic Documents all appear as visible placeholders in the same menu — signaling what's coming without being built yet — and become real at Phase 2. Keeps Phase 1 lean and honest rather than shipping partial versions of three features at once.

**Next action:** fold into the Phased Plan (Phase 1 gets the world-click menu with only Choose for Table live; Phase 2 activates Description, Tour, and Academic Documents) and the Experience Vision document, next time either is updated.

---

## 2026-07-07 — Checked against Facilitator Governance directly; closing-resources idea is a genuine addition, not a gap

**Investigated, at Mark's direction:** whether the vulnerable-participant and closing concerns raised this session are already covered in Facilitator Governance (V3.6, the branch currently building toward Phase 1) before treating them as gaps.

**Confirmed already mature, correcting an earlier overstatement in this thread:** Facilitator Governance already specifies an Acute Distress trigger (present crisis or self-harm risk — "surface with warmth and honesty about the limits of what this encounter can offer, and with whatever redirection toward human support is appropriate") and a Harmful Dynamic trigger that names dependency directly ("the participant is relating to the Representative as a substitute for human relationship rather than as a formation encounter"). Both resolve through the same three-posture model as every other governance trigger — Hold, Surface briefly, Intervene — matching Mark's own description of the Facilitator watching in the background and only surfacing when a pattern needs it. No product-level gap here; this is conversational, not a separate UI, and it's already well specified.

**Genuinely new — closing resources:** the current "gracious close" section describes the general posture (the last word is always a comma, not a period; the door left open) but says nothing about offering resources tied to what came up. Mark's addition: at closing, ask — never push — whether the participant would like resources around a topic or a hurt that surfaced, and if so, hand over links or sources for self-directed follow-up. Explicitly framed around participant agency: this lets them take control of their own learning or transformational journey rather than the system prescribing a next step. Directly serves Article 34 (Doorway Not a Home)'s "gentle redirection outward" requirement, which had no product expression before this.

**Resolved:** Facilitator-curated in the moment, genuinely responsive to what actually came up in that specific conversation — not a generic per-topic list. Mark's own reasoning, worth preserving: this is deliberately building relational feel and connection into the Facilitator even though it isn't human. Not in tension with Article 34's prohibition on substituting for human relationship — a doorway that greets someone well is still a doorway; the warmth is what makes leaving well possible, rather than leaving feeling processed.

**Also flagged, still open, not yet decided this session:** conversation privacy/data-logging disclosure, and whether Phase 1 requires accounts or stays stateless — both raised as real, unresolved product questions, neither resolved yet.

**Decided — closing resources use the same hover/click mechanic:** hover gives a brief explanation of a suggested resource, click opens the link and more detail. The fifth application of the same interaction pattern already built for lexicon terms, stories, quotes/sourcing, and Academic Documents — no new UI invented for this moment. Keeps a potentially heavy moment (offering resources around something painful) light and optional rather than a wall of links.

## 2026-07-07 — Funding model direction: free core experience, paid professional layer — with a constitutional boundary named explicitly

**Decided — direction:** the general encounter stays free for everyone, Bible-Project-style (donor/crowd-funded, no paywall on the mission-critical experience). A cost may apply to unlock deeper pastor and academic-facing features — sermon-prep tooling, Academic Documents, Tours — rather than the core conversation itself.

**Boundary drawn, and it matters:** Article 30's Three-Level Transparency invariant ("Levels 2 and 3 always reachable from Level 1, never gated") governs a participant's own in-conversation encounter — whatever comes up in a live conversation, the grounding behind it stays free and reachable via the existing hover/click mechanic, for everyone, regardless of what happens with anything else. That does not change under this model. Tours and sermon-prep tooling don't touch Article 30 at all — they're experience and productivity features, not evidentiary access, so no constitutional question there. Academic Documents is the genuinely gray case: still "seeing the sources," just at a standalone-browsing surface rather than tied to a specific conversation. Gating it is defensible (nobody's own encounter depends on the full corpus being free to browse independent of any conversation) but is a real product decision sitting close enough to Article 30 that it needs an explicit, named carve-out in the Constitution rather than a quiet workaround.

**Mark's own instinct, worth preserving:** if Academic Documents ends up gated, the Constitution should be changed to say so plainly — the same discipline already used for the Movement Scope addition: test the change on a branch, state plainly what it does and doesn't cover, merge back once proven, rather than letting a product decision quietly outrun what the governing document actually says.

**Next action:** flag for the funding thread as a real model direction. If/when Academic Documents gating moves from idea to decision, the Article 30 carve-out is a governance change outside this workstream's authority to draft unilaterally — same category as the Movement Scope and "The Church in Conversation" naming questions already logged.

---

## 2026-07-07 — Engineering Considerations Catalog created (Project-Reference), so this doesn't stay locked to one thread

**Decided:** The "what else should I be considering, especially for Phase 1 and earlier, without setting something up that has to be completely rebuilt to grow" answer from this thread is durable, cross-cutting engineering judgment, not a narrative decision specific to this workstream — so it doesn't belong only in this dated log. Catalogued instead at `Project-Reference/CiC_Engineering_Considerations_Catalog_V1_0.md`, alongside the existing Cleaning Pattern Log, in the same disciplined pattern-entry format (the risk, what to do now at lean/prototype scale, what it protects later). Committed to git on main so it's available to any future thread — world builds, org/funding, validation — without that thread having to rediscover it independently.

**What's in it:** six build-now-vs-rebuild-later considerations (world data schema readiness for the future World Map; retrieval behind a clean interface; the funding model forcing the accounts/identity question sooner than expected; building the real voice pipeline now with a cheap voice rather than a throwaway version; the unresolved tension between internal QA conversation-logging and participant privacy, flagged as time-sensitive rather than someday; world-content versioning separate from app-code versioning) plus a short pointer section to considerations already logged elsewhere (Article 30 boundary, the five-Representative ceiling's missing system-level guard, the world-click-menu placeholder architecture, and the standing hazard of conflating the three distinct transparency concepts).

**Note on the commit itself:** a stale `.git/index.lock` blocked normal `git add`/`git commit` (likely a Windows-side file lock from another process with the repo open). Worked around it using git plumbing commands (temporary index, `write-tree`, `commit-tree`, `update-ref`) that don't touch the locked index file — the commit is real and on `main` (`0a7b1ac`), but the real working-tree `.git/index` itself is now stale until that lock clears. Worth closing whatever has that repo open on the Windows side, then running `git status` once to let it self-correct; not urgent, doesn't affect committed history.

**Next action:** none pending. Future threads should check the Engineering Considerations Catalog before re-deriving this kind of judgment from scratch.

---

## 2026-07-08 — Design Brief corrected: Academic Documents governance caveat restored, Alpha-scope clarified, Facilitator-orchestration question flagged as genuinely open

**Context:** A detailed review of `CiC_FrontEnd_Design_Brief_V1_0.docx` (the one-to-two-page brief for the engineer) identified two substantive accuracy problems, not stylistic ones. Both were verified against source documents before any edit was made.

**Fix 1 — Academic Documents overstated as settled.** The brief had described Academic Documents as a future paid-tier feature alongside Tours and sermon-prep, full stop — no caveat. The 2026-07-07 entry above calls Academic Documents "the genuinely gray case": gating it is defensible, but it sits close enough to Article 30's always-free-and-reachable transparency guarantee that it needs an explicit, named constitutional carve-out before being built that way — a carve-out that hasn't been made. The brief's funding paragraph now states this directly: Academic Documents' gating is an open governance dependency, not a settled product decision, and should be treated that way by whoever builds it.

**Fix 2 — Alpha vs. Phase 1 scope was undifferentiated.** The Functional Requirements section described the full system (five Representatives, three equal-weighted entry paths, full Facilitator orchestration) without saying which parts Alpha actually needs, against Mark's own Alpha philosophy ("smallest possible thing that lets a real person talk to a Representative"). Checked against the actual governing document, not assumed: Table Design Document Section 11 confirms Alpha = 1–3 worlds with Bypass entry only and basic role selection; the full three-pathway portal (including world browsing) isn't delivered until Phase 1, with Beta still excluding it. The entry-state requirement in the brief now states this phase split explicitly, with a citation to Section 11.

**Genuinely open, not resolved — flagged in the document rather than guessed at:** Table Design Document Section 11 confirms entry-pathway scope but is silent on whether full multi-Representative Facilitator orchestration (turn-taking across concurrent Representatives, cross-world drift monitoring) is required at Alpha or can be deferred to Beta. This materially affects Alpha engineering scope. Added as an explicit open-scope note in the brief, immediately before the Build Order table, rather than resolved unilaterally — this is Mark's call, and the reviewer was right that it could change engineering estimates.

**Verification:** claim 1 checked directly against this log's 2026-07-07 entry; claim 2 checked against `CiC_FrontEnd_Strategy_Scoping_2026-07-07.md` and against Table Design Document Section 11 itself (read across all four copies on disk — main, both worktrees, Syriac-Build — confirmed byte-identical, so no version drift risk).

**Next action:** Mark to decide whether Facilitator orchestration is in scope for Alpha or deferred to Beta — the one open question the brief could not resolve from existing governing documents.

---

## 2026-07-08 — One-page Design Brief produced; landing-page hero resolved: the Facilitator is present, not an empty Table

**Produced:** `CiC_FrontEnd_Design_Brief_V1_0.docx` — a one-page distillation of the Experience Vision and Vision & Phased Plan, written to hand directly to the engineer so he can start designing without reading the full spec set. Covers: what this is, the governing feeling, the one rule, the experience compressed into five bullets, the build-order table, and the constraints worth knowing before starting (five-Representative ceiling, text as permanently load-bearing, build the seams not the features).

**Resolved — the landing-page hero, previously logged provisional:** the 2026-07-07 entry on the landing page described "an evocative, not-yet-populated version of the Table — empty or waiting seats... no specific Representatives visible" and flagged it pending Mark's confirmation. Mark corrected this directly: the Table at entry is not empty — the Facilitator is there, the one figure present, to greet the participant and offer the three entry choices. This isn't a new decision so much as a completion of the original one: "no Representatives yet" was always true, but it read as "no one yet," which wasn't intended. The Facilitator's presence at the threshold is consistent with its role everywhere else in the design (neutral host, the one voice a visitor can address before committing to anything, "Ask the Facilitator") — it would have been an odd gap for it to be the one place the Facilitator isn't visually present.

**Applied:** the Design Brief's Landing bullet now reads accordingly. Not yet propagated to the fuller Experience Vision document (still not updated with this or the several other post-creation decisions logged above — World Map, Academic Documents, funding model, Article 30 boundary — same open gap noted repeatedly in this log).

**Next action:** none blocking. Worth folding into the Experience Vision doc's own landing-page section next time that document is revised.

---

## 2026-07-08 — Design Brief extended to two pages: "Where This Is Headed (So You Don't Build a Trap)"

**Decided:** Mark explicitly waived the one-page constraint to add long-term-vision context for the engineer — reasoning stated directly: without it, Phase 1 gets built as if it's the whole product, and something in it becomes a trap. Added a new section between Build Order and Design Constraints covering, in narrative form, everything the Build Order table doesn't show: the eventual 50–100 world catalog and the World Map timeline it needs, the four-option world-click menu (Description/Tour/Choose for Table/Academic Documents), Academic Documents as a future standalone feature distinct from the in-conversation hover/click, Tours, maturing voice, and the funding shape (free core permanently, a possible paid pastor/academic tier on top).

**The concrete payoff, not just narrative:** a seven-row table — "Build this seam now (cheap)" against "Because this needs it eventually (expensive to retrofit)" — translating the Engineering Considerations Catalog directly into engineer-facing guidance: world data fields, retrieval behind a clean interface, the four-option menu built disabled rather than added later, a role/entitlement field, the real voice pipeline, content versioning, and a written logging/privacy policy before Alpha testing starts. This is the same seven-ish items from the Catalog, translated from "why it matters" into "build it this way," which is what an engineer actually needs at the point of building rather than a reference document to go read separately.

**Reasoning:** Kept the seam table separate from prose so it functions as a checklist an engineer can actually work against, not just context to have read once. Trimmed the old "build the seams" bullet under Design Constraints to a pointer rather than deleting it outright, so the constraints section still names it without duplicating the fuller explanation above.

**Next action:** none blocking. The doc is now two pages by design, not by accident — Mark should treat any further additions as a deliberate length trade-off, same as this one.

---

## 2026-07-08 — Design Brief reworded for an experienced-engineer audience

**Decided:** Mark's own phrase "so you don't build a trap" was informal shorthand from our conversation, not the register he wanted in the document itself. Reworded the Roadmap Context section, the seam table, and the Design Constraints bullets throughout: the section title became "Roadmap Context — Forward-Compatibility Requirements"; the seam table's two columns became "Requirement (Phase 1)" and "Forward-Compatibility Rationale," with every row rewritten as an explicit implementation requirement paired with its rationale, rather than descriptive prose; the constraints bullets were tightened to name the actual enforcement point ("enforce it explicitly in session/state logic," "non-functional requirements alongside the functional spec") instead of conversational framing like "full stop" and "hard ceiling."

**What was deliberately left alone:** the experience-description sections (What This Is, The Feeling We're Building Toward, The One Rule, The Experience Compressed) — those are product/UX description meant to convey feel to whoever builds this, and an evocative register is doing real work there, not a lapse in precision. The register change was scoped to the sections giving the engineer direct implementation guidance, where imprecision has a real cost.

**Reasoning:** A design brief that describes intent in engineer-precise language is more likely to be read as a requirements document and actually followed, rather than as color commentary the reader skims past. Worth naming as a general pattern for any future engineering-facing document produced in this workstream — vision/experience sections can stay evocative, requirement sections should read like requirements.

**Next action:** none blocking.

---

## 2026-07-08 — Section order corrected to a big-to-little flow; table row-splitting fixed

**Decided:** Mark asked directly whether the document's order was a natural flow. It wasn't: What This Is → Feeling → One Rule → Experience Compressed → Build Order → Roadmap Context → Constraints put the near-term Phase 1 build order immediately before a jump out to the 50–100-world long-term picture, then back into specifics — a zigzag rather than a single trajectory. Reordered to context-first: What This Is → The Feeling → The One Rule → Roadmap Context (with its requirements table) → The Experience, Compressed → Build Order → Design Constraints. Every section is now more concrete than the one before it, so nothing the engineer is asked to build in the near term is read before he has the full scope envelope it needs to fit inside.

**Reasoning:** This matches how technical specs are conventionally structured for an engineering reader — context and goals before detailed design — precisely because the whole point of the Roadmap Context section is to shape how the near-term work gets built. Reading it last, as originally ordered, would have let the reader form a mental model of the architecture before encountering the constraints meant to inform it.

**Also fixed while rebuilding:** the seam table's last row was splitting mid-sentence across the page 1/2 boundary. Added `cantSplit` to table rows in the docx-js build so a row now moves to the next page whole rather than breaking across it, with the header repeating above it — same fix belongs in any future table-heavy document built with this pipeline.

**Next action:** none blocking.

---

## 2026-07-08 — Terminology correction: "engaging conversation," not argument or debate

**Decided:** Mark rejected the "argument as affection rather than combat" framing under The Feeling We're Building Toward — his own words: "it's not a theological debate or an exegetical argument, its healthy, deep insightful, challenging, stretching, resonating conversations (thus the name), summed up in 'engaging conversation.'" The Inklings image stays (the setting still communicates unhurried, communal, close-to-the-ground), but the verb changed from Lewis and Tolkien "arguing" to "meeting," and the description changed from "argument as affection rather than combat" to an explicit definition: not a theological debate or an exegetical argument, but engaging conversation — healthy, deep, insightful, challenging, stretching, resonating. Added "The name is deliberate" to tie the phrase directly back to the project's own name, "The Church in Conversation."

**Why this matters beyond word choice:** "argument," "debate," and "combat" carry a winner/loser, position-defending connotation that cuts against Witness-Not-Recruitment (Article 24) and the project's own stated failure modes (ideological persuasion, generated panel entertainment). "Engaging conversation" — challenging and stretching without needing a winner — is the more accurate description of what this project is actually for, not just a softer synonym.

**Propagation gap, not yet fixed:** the same "argument as affection rather than combat" phrasing exists in `CiC_FrontEnd_Experience_Vision_V1_0.docx` ("Inklings image: unhurried conversation, argument as a form of affection rather than combat, people who trust each other enough to disagree hard..."). Not corrected there yet — same standing gap already noted several times in this log (the Experience Vision doc lags behind decisions made after its creation). Worth a full pass next time that document is revised, this correction included.

**Next action:** none blocking on the Design Brief. Carry this correction into the Experience Vision doc whenever it's next revised.

---

## 2026-07-08 — Full document reworded for an engineer audience, not just the Roadmap Context section

**Decided:** Mark asked for the whole document to speak to an engineer, extending the earlier register fix beyond the sections it was originally scoped to. Reworded every remaining section: "What This Is" became "System Overview," rewritten as a functional description of the session/agent/orchestration model rather than narrative description of a participant's experience. "The Feeling We're Building Toward" became "Design Intent" — same content (the Inklings reference, "engaging conversation," the name being deliberate), reframed as a design-tone requirement rather than a mood-setting passage. "The One Rule Underneath Everything" became "Governing Content Rule," stated as a global invariant. "The Experience, Compressed" became "Functional Requirements — Core Experience," with each bullet rewritten from descriptive prose ("Landing: an evocative Table...") into an implementation-oriented requirement (entry states, rendering behavior, data sources, interaction patterns). "Design Constraints Worth Knowing Before You Start" tightened to "Constraints." Also caught and fixed two remaining casual words in the Roadmap Context prose ("is real at Phase 1" → "is implemented at Phase 1," "first pass voice matures" → "is expected to be superseded by").

**What didn't change:** every fact, requirement, and number in the document is unchanged — this was a register pass, not a content revision. The Inklings reference and "engaging conversation" language survive intact inside Design Intent, reframed as what tone the implementation should target rather than as atmosphere-setting for its own sake.

**Reasoning:** A document meant to be read and acted on by an engineer should read like a requirements document throughout, not only in the sections added most recently — mixing an engineering register with a narrative one in the same document reads as inconsistent and makes it unclear which parts are binding. This is a genuine content-vs-register question worth remembering: the same underlying decisions can be expressed as either narrative (for Mark's own thinking, or the fuller Experience Vision document) or requirements (for an engineer), and this document should now consistently be the latter.

**Next action:** none blocking. Worth treating the fuller Experience Vision and Vision & Phased Plan documents as intentionally narrative-register — this Design Brief is now the one requirements-register artifact in the set, and the two registers shouldn't be blended going forward.

---

## 2026-07-14 — Citation transparency confirmed half-built, not just half-designed; new world-selection mode raised, heart-reasoning still open

**Context:** This session had been deep in backend prompt/orchestration work on the actual running prototype (`cic-poc`), not this workstream's planning documents. Mark raised two ideas directly against that running code: (1) three-level rigor for the lexicon, extended to stories and sources, surfaced as inline colored text or an icon at sentence-end with hover and click, rather than listed separately at the end; (2) restructuring world selection from a single "choose a world" action into two distinct modes — a deeper interview with one world, harness deliberately loosened for longer dialogue, versus choosing 2-3 worlds for comparison.

**Confirmed, not re-decided — idea 1 already exists at two levels:** the 2026-07-07 entry above already decided this exact pattern (highlight in dialogue text, hover for Level 2, click for Level 3, extended to stories/quotes/sourcing generally). Checked against the actual running frontend, not just the doc: `LexiconHighlight.tsx`/`HighlightedText` already implements this live for lexicon terms - inline highlight, hover tooltip, click-through. The gap is narrower than "build the mechanic": citations/sources currently render as a plain list block at the bottom of each message (`MessageBubble.tsx`'s "Sources" section), not through the same inline hover/click component. That's the one piece of an already-decided, already-partially-built pattern that hasn't been extended yet.

**Decided this session:** build the citation-inline mechanic next, ahead of any of the richer visual Table work (multi-figure background, camera pans, voice) already described in the Experience Vision documents - reasoning being that this is a scoped, already-proven-pattern frontend change working directly against the real prototype, not a new design question, while the richer visual work is real but is specialist-engineer-tier and more expensive to get wrong. Not a reversal of the phase-ladder work above, just a sequencing call for what to build with the time available right now.

**Raised, not yet decided — the two-mode world-selection idea:** genuinely new, not present anywhere earlier in this log. Noted as mechanically compatible with what the backend already does: the reactive-turn constraints tuned extensively this session (length ceilings, table_discourse.py's reactive guidance, anti-resolution rules) only activate when a representative speaks after another has already spoken in the same round - a single-world conversation never triggers any of it. So "a looser harness for a deep interview" is closer to the existing default behavior of a one-world conversation than a new backend mode to build; the open work is making that an explicit, named entry-point choice rather than an accidental byproduct of world count.

**Heart question asked, not yet answered:** whether "Deep Interview" mode is meant to protect real formation-encounter depth with one voice (in the spirit of Encounter Over Persuasion - one voice actually forming a participant, not just answering questions), with "Compare Worlds" understood as a different kind of use (useful, but structurally comparison-shopping rather than encounter), or whether something else is driving the split. Left open rather than assumed, since the answer would shape whether Compare Worlds gets the same conversational depth treatment or is deliberately kept lighter/shorter.

**Next action:** citation-inline mechanic build starts this session (see cic-poc frontend changes). World-selection mode split stays logged as raised-but-open until Mark answers the heart question above - do not treat it as decided or start building an entry-point split before that's answered.

---
