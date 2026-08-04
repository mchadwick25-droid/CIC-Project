# Launch prompt — Tours, redesigned from a token-free premise (Fable)

Paste this into a fresh thread, run on Claude Fable 5. This supersedes both prior
tour designs — `Tour-Experience-Module-Phase2/` (Strategy V0.3 + its L4 Manifest
Template + Build Spec + Eligibility Gate) and `Hosted-Tour/` (the Chloe Phase One
demo) — which were both built around a live-hosted-inside-an-encounter premise this
redesign deliberately does not carry forward. **This is a fresh design, not an
edit pass on either superseded folder.** Both are marked SUPERSEDED in their own
READMEs, kept in full as historical/research material, not deleted.

**Scope note, read this first:** this thread does **not** touch `cic-poc` code,
does **not** change anything about the current prototype or Phase One testing,
and does **not** integrate this feature into the live app. It produces strategy,
a per-scene evidentiary analysis, and an architecture design — planning artifacts
for a future build phase. Where this thread's work implies a build item, name it
plainly as a future handoff, the same discipline every other thread in this
project follows.

---

## Why this exists, and why it's a restart rather than a revision

Working through the Church in History Atlas content pass (2026-08-03) surfaced a
cost-model realization that applies project-wide: **live conversation is the
expensive, essential heart of this project — everything else should exist to
accompany a participant toward wanting it, not compete with it for API budget.**
The original Tour design failed that test by its own stated logic ("the
Representative's presence throughout is the product" — meaning: rendered live,
same cost class as ordinary conversation, every time, for every participant).

Mark's own words, on why this is a restart and not a patch: *"i am afraid that
there will be limitations that we don't see now. i want to start the process
over from a completely new perspective that reflects what we are describing, not
adjust what we did before and constantly fight a to rigid approach."* Retrofitting
the old design risks exactly that — fighting its hidden live-generation
assumptions one at a time (the manifest's "narration bounds," the Permanent-
Prompt overlay, retrieval scoping, drift monitoring as the primary guardrail)
instead of building cleanly from the new ones.

## The idea, stated exactly as decided (2026-08-03 Front-End Decision Log entries —
## read the original entry, the same-day correction, the three-voice
## refinement, the two-threshold refinement, the fill-density refinement, the
## visual-policy refinement, AND the Williamsburg correction below them, in
## that order, before starting; this is a compressed restatement of the
## fully refined version)

**Visual policy — read this before assuming any tour needs, or can safely
use, imagery. Honesty here is Williamsburg-shaped: two different registers,
not one repeated disclaimer.** (1) **Narrated framing happens once, warmly,
at the Facilitator's threshold, and is never repeated inside a scene to
disclaim it.** Once a scene begins, nobody breaks character — the interpreter
doesn't stop mid-tour to say "this is a reenactment," and neither should this.
(2) **Visual honesty is carried the way a museum label carries it** — a
small, quiet tag on the image, using the same hover-for-short/click-for-full
sourcing grammar already used everywhere else in this project — present and
discoverable, never a banner or a repeated spoken caveat. Both registers
still have to be *true*: the exemplar-vs-claim distinction from the
fill-density rule applies to images exactly as it applies to text, it just
doesn't need to announce itself loudly or often to stay honest. Two hard
constraints, unchanged from the superseded design and not up for
reconsideration: **no generated or commissioned "reconstruction" imagery,
ever** — only real photographs or excavation records of real sites (a
generated "typical Roman house" is pictorial fabrication, worse than
borrowing an out-of-period real site, not better); and nothing depicted
should carry Christian iconography or markers if the honest point is that
nothing distinguished the room as a meeting place. **This is world-specific,
re-answer it per world, don't assume one
verdict everywhere:** PAHC's own record has no visual evidence at all (its
Source Ecology assessment already found the window "essentially
archaeologically invisible," and the one tempting candidate, Dura-Europos, is
explicitly excluded as evidence for this world — third-century Syria against
Justin's second-century Rome); the Desert world, by contrast, already has
real, registered archaeological material (the Kellia excavation findings) in
its own record, a stronger position than PAHC's "closest we have" exemplar
case. **A real, well-founded candidate for PAHC's exemplar image, as a
research lead to verify — not decided here:** the excavated houses at Pompeii
and Herculaneum — same-region Roman domestic architecture, close in time
(79 CE against Justin's c. 150s), better-founded than Dura-Europos because
nothing about them needs to be misread as Christian; they simply illustrate
the *kind* of ordinary home such a gathering would have used, with no claim
about a specific building.

**Fill-density rule — read this before scoping how thin or thick any tour's
beats should be.** Every element a source names becomes its own full beat,
not a summarizing line — Justin's account names a gathering, a reading, an
exhortation, standing prayer, bread and wine, thanksgiving, a collection; each
is a place to give the participant the thing itself, not a sentence reporting
that it happened. Where a source names something generic (Justin's "the
memoirs of the apostles or the writings of the prophets, as long as time
permits" doesn't say *which* text), fill it with a real, specifically-attested
exemplar rather than leave it abstract — **but keep the two claims visibly
distinct: "a reading happened, in this shape" (Justin's own attested account)
is a different, stronger claim than "here is a real letter these communities
are known to have read aloud, so you can hear what such a reading actually
sounded like" (an honest exemplar, not a claim this specific text was read at
this specific gathering).** Drawing that line is the Facilitator's job, the
same discipline as the outside-scholarship-insertion flag, applied to a
different kind of boundary. **Two real letter candidates for the PAHC
gathering's reading beat, as a starting research lead — verify and choose
through the normal construction-review process, don't assume either without
checking:** 1 Clement (Rome to Corinth, c. 96 CE, with documented evidence of
being read aloud in Corinth's own gatherings) and Ignatius's seven letters
(c. 107–117 CE, one addressed directly to Rome, congregational reading-aloud
itself an attested PAHC practice).

**Two thresholds, not one — read this before drafting any tour's opening
beats.** The Facilitator's threshold welcomes the participant to the *tour as
an experience* (what it is, what it's built from, what it won't claim, how to
leave). Where a scene's own content naturally calls for it, the Representative
then welcomes the participant *into the scene itself*, in her own bound voice
— a hostess greeting a guest at her own gathering is content, not the
Facilitator performing hospitality on her behalf. These are two distinct
beats and must not collapse into one merged "welcome" the way the superseded
Hosted-Tour demo's "Stop 0: The Door" did. Generalize this: any scene where
the Representative's own presence and speech is natural and sourced (a
welcome, a teaching, a blessing) belongs to her, in bound voice, as content —
distinct from the Facilitator's role as host of the tour-as-experience.

A tour is a **fully authored, reviewed, produced experience** — not a live mode
inside a conversation. Concretely:

1. **Narration is completely written, never generated at runtime — and the
   Facilitator is the constant host, with up to three distinct voices appearing
   inside that frame at key moments.** Reconsidered twice, same day: first,
   having a Representative narrate her own tour risked real participant
   confusion (strictly bound to her own record in conversation, drawing on a
   wider pool in her tour reads as inconsistency, not richness); second, a
   Facilitator-only tour still needed a way to make the boundary between "her
   own record" and "outside scholarship" *felt*, not just labeled. The
   resolved structure:
   - **The Facilitator narrates** — orients the scene, moves it along, and is
     the only voice permitted to say, out loud and in the moment, when a detail
     is an outside-scholarship insertion ("historians who've studied this
     closely believe... though that's not something Chloe's own writings tell
     us"). **The entire widened primary-plus-secondary-scholarship pool
     belongs to the Facilitator alone.**
   - **Chloe may be quoted or given a brief authored aside — under a hard
     rule: she is never allowed to speak beyond exactly the same evidentiary
     bound she has in live conversation.** This is what makes bringing her
     back into the tour safe: if she only ever speaks from what her own record
     already contains, no version of tour-Chloe can ever be contradicted by
     live-conversation-Chloe. This is a checkable constraint for review, not a
     style note — flag any beat where "Chloe says" content isn't traceable to
     her own existing Doc_09/capsule/permanent-prompt material.
   - **The primary historical source is quoted directly in its own name**
     (Justin Martyr's own words, dated and attributed) — distinct from Chloe's
     own voice; this is the attested text itself, not her relaying it.
   - **Presentation needs three distinct visual/textual treatments**, not
     three voices in one typeface — reuse the source-cartouche pattern from
     the superseded Hosted-Tour demo (citation + tier + confidence, hover-
     short/click-full). A participant should be able to tell who's speaking at
     a glance.
   Every beat's text is authored once and passes the same review-gated
   construction-document cycle every other artifact in this project goes
   through.
2. **Launched from the Atlas/map, standalone — never gated behind starting a
   conversation.** A movement's Atlas entry carries a "Tour available" affordance.
   Where no licensed tour exists for a world or scene, the Atlas says so plainly,
   reusing the exact honesty pattern the census already carries for "not yet
   built" — not a new refusal screen to invent.
3. **Q&A is a small, pre-written, reviewed set — never live retrieval-and-
   generation.** Reuse the Guided Questions discipline and pipeline (sets desk-
   checked per world, sourced, reviewed) rather than inventing a new content
   type, re-scoped to a tour's specific beats. Default UI: tappable pre-written
   questions, not a free-text box. A retrieval-only nearest-match against the
   written set (embeddings, zero generation) is a real later option, not the
   Alpha shape — name it as a future handoff if it comes up, don't design it now.
4. **The boundary door is a designed feature, not an apology, and it is now a
   Facilitator-to-Representative handoff.** When a participant's question falls
   outside the pre-written set, the Facilitator says so plainly and offers to
   introduce the participant to the Representative directly — "Now that you've
   seen this, would you like to go meet Chloe yourself?" — rather than a
   Representative handing a participant off to a paid version of herself. This
   is the intended edge of a free experience pointing toward the real one; write
   it with the same care as any other participant-facing copy in this project.
5. **Live drift monitoring is retired for this surface.** Nothing generates at
   runtime, so there is nothing for a live monitor to watch. The guardrail is the
   construction-review cycle itself — verify every claim before it ships, the
   same discipline (writer pass + independent adversarial review) just proven at
   scale on the Atlas content pass tonight.

### The sourcing rule — widened pool, unchanged integrity

Because Tour content is now fully authored and reviewed rather than live-
generated, **"traceable evidence" for a tour beat is no longer limited to what's
already packaged into a world's own approved Doc_09 story chunks.** It extends to:

- the world's primary sources directly, and
- trusted secondary/historical scholarship — real historians' credentialed
  reconstructions of what a primary source doesn't itself narrate.

**What does not change:** zero invention, ever. Every element still has to trace
to something real. If neither the world's own primary sources nor trusted
secondary scholarship covers a detail, the detail is absent — the same "no new
texture" rule the old design already had, just applied to a bigger pool.

**What's new and load-bearing: disclosure moves to the element level.** Not just
"this tour is a reconstruction" once at the threshold — each beat (or each claim
within a beat) discloses whether it rests on a primary source or on named
secondary/historical scholarship, reachable by a curious participant the same way
Level 3's citation-chip apparatus already works elsewhere in the system. This is
*more* transparency than the old design had, not less, even though the pool it's
disclosing is wider.

**Scope of the widened rule, stated plainly so it doesn't drift:** this applies to
the Tours surface only. The live conversational Representative's sourcing stays
exactly as strict as it is today (Doc_09-licensed chunks only) — it is a real-time
generative surface with no per-output human review, and that is precisely why it
still needs the narrower, pre-packaged pool. Do not let this widened rule bleed
into how the live Representative retrieves or generates.

## What already governs this, read in this order

1. **`Ministry/Communication/Vision, Mission, Convictions, and Foundational
   Commitments V1.1.docx`** — Conviction 4 (trustworthy transparency), Conviction
   5 (technology serves encounter, never replaces it — read this one with fresh
   eyes against the new design: a fully-authored tour is arguably *more*
   faithful to this conviction than a live-generated one, since it removes the
   model as a runtime actor entirely and leaves only a reviewed, human-
   accountable artifact), Historical Responsibility, Participant Agency.
2. **`L1-Foundation/CiC_L1_Constitution_V2_2.docx`** — Article 6 (Encounter-
   Success Standard), Article 17 (visible-confidence rule — now needs applying
   at the element level, not just the tour level), Article 19 (free invention
   prohibited at every stage — unchanged, the sourcing pool widened, the
   prohibition did not).
3. **`L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.3.docx`**
   — the four-tier story classification and No Tier 5 rule. Decide explicitly in
   this thread's own strategy output how (or whether) the tier vocabulary maps
   onto the new two-source-type disclosure (primary vs. trusted secondary) —
   this is a real design question the old Class A/Class B split doesn't cleanly
   answer under the widened pool, and it should be answered on purpose, not left
   implicit.
4. **The superseded folders, as research material, not as a design to inherit:**
   `Tour-Experience-Module-Phase2/CiC_Tour_Experience_Module_Strategy_V0_3.md`
   §3 (the per-world evidentiary analysis — every verdict there was computed
   under the *old*, narrower sourcing pool and needs re-deriving, not assuming;
   some PARTIAL/NO verdicts may change under the wider pool, some may not — real
   historians may be just as silent as the primary record on a given gap).
   `Hosted-Tour/Design/CiC_Hosted_Tour_Design_Note_V0_1.md` — the stop-by-stop
   source-cartouche pattern and the "what we cannot show you" honest-decline
   stop are strong, reusable presentation ideas; evaluate them fresh against the
   new no-live-encounter-gate premise rather than assuming the built demo's flow
   still applies.
5. **`Ministry/Features/Front-End-Integration-Strategy/Decision-Log.md`**,
   all eight 2026-08-03 entries (the restart; the Facilitator-narration
   correction; the three-voice refinement; the two-threshold refinement; the
   fill-density refinement; the visual-policy refinement; the Williamsburg
   correction; the shape-proof + observer-not-participant entry; the
   voice/audio cost clarification) — the full reasoning, in order, read in
   full before drafting anything.
5a. **`Tour-Experience-Module-Phase2/CiC_Tour_PAHC_Worship_Service_Shape_Proof_
   2026-08-03.md`** — a full worked draft applying every decision above to
   real content (Justin's *First Apology* 65–67). Read this before drafting a
   formal manifest — it's already tested the design against an actual scene
   and surfaced three open construction calls (the letter candidate, quote
   verification, pacing), plus the observer-not-participant rule and the
   Corinth/Rome meal-diversity aside, both now standing rules for every tour.
5b. **`Tour-Experience-Module-Phase2/CiC_Tour_Comparator_Research_2026-08-03.md`**
   — research on real comparable projects (the Virtual Paul's Cross Project,
   Rome Reborn, museum audio-tour practice, Drive Thru History) and two
   cautionary cases (Google's live-generated Talking Tours, *The Chosen*'s
   single-disclaimer approach) — read for what's independently validated
   versus what's a live open question (multiple observer positions for one
   event; whether ambient soundscape sits at a different risk tier than
   narrated dialogue).
6. **Whatever governs the Facilitator's own established voice/register today**
   (Facilitator Governance, the L3D Table Process, any existing threshold-
   welcome/close copy already in production or design) — read this before
   drafting a single line of tour narration. The correction entry names a real,
   unresolved risk: a Facilitator-led tour could read as more curatorial and
   less intimate than a Representative narrating her own world, and the direct-
   quotation design (item 1 above) is a mitigation, not a guarantee. Confirm the
   Facilitator's existing voice is warm enough to carry a whole hosted
   experience before assuming it is.

## What to produce

Work through these in order — do not skip to architecture before the evidentiary
analysis is redone, since the architecture's scope depends on which scenes
actually qualify under the new sourcing rule.

### 1. Strategy

Draft the product strategy for the redesigned module, grounded in the premises
above: the map-launch flow end to end (from an Atlas entry to threshold to beats
to boundary door to hand-off), the tier-vocabulary-vs-source-type-disclosure
question named in item 3 above, and an explicit statement of what changed from
each superseded document and why — a future reader should not have to diff this
thread's output against V0.3 to understand the delta.

**Also settle, on purpose, not by default:** exactly how a Representative's
primary-source words get quoted inside a Facilitator-narrated beat (attribution
framing — "Justin himself wrote..." — voice/typographic distinction between the
Facilitator's own narration and the quoted primary text, whether a Representative
can be quoted at all in a scene her own Doc_09 doesn't license for conversation);
and a real gut-check, not just a design assertion, on whether the Facilitator's
existing register can carry a whole hosted experience's warmth — read its
governing voice material first (item 6 above), and if it can't yet, name that as
a real gap rather than build past it.

### 2. Per-scene evidentiary analysis — re-run under the widened sourcing pool

For every live and in-progress world, re-derive (do not assume) whether a tourable
scene exists, now allowing primary sources plus trusted secondary/historical
scholarship, not just already-packaged Doc_09 chunks. Name, per scene: the primary-
source basis, any secondary/historical scholarship drawn on to fill a gap (named,
credentialed, disclosed as such), and anywhere the record — primary *and*
secondary — is still genuinely silent, which stays a tour-refusing absence exactly
as before. Produce this as a real table or per-world section, the same discipline
V0.3 §3 used, so a future builder can look up "is a tour possible for World X, on
what basis" without re-deriving the analysis.

### 3. The Tour Manifest, redesigned

A new L4 template (or a substantial revision of `CiC_L4_Tour_Manifest_Template_
V1_0.md` — thread's judgment which is cleaner) reflecting: fully-written beat
narration (no "bounds"); per-element source-type disclosure; an anticipated-
questions block per beat or per tour, authored and reviewed like a Guided
Questions set; the boundary-door text as a required, reviewed field, not an
afterthought; and the persistent register banner, now needing language that can
name *which* secondary sources a beat draws on, not just "reconstruction."

### 4. Architecture

Design how this launches from the Atlas/map with zero runtime generation: the
map-entry affordance and its honest-absence state; how a produced tour is served
(static content, same cost-model logic as the Repository's Level 2/3 — read the
2026-07-28 Front-End Decision Log entry for that architecture's existing shape);
where the boundary door hands off into the live conversational system (this is
the one place the design re-enters Level 1, and it should re-enter it cleanly,
not awkwardly); and a forward-looking technical note only (not a build task) on
`cic-poc` touch points if this were built.

## Coordination boundary, stated plainly

This thread produces strategy, evidentiary analysis, and architecture design
only. It does not:
- Touch `cic-poc` frontend or backend code, now or as part of this thread's own
  work.
- Integrate anything into the current prototype or Phase One testing.
- Invent sourced scenes for worlds or scenes that don't have them under the
  widened pool either — the pool got bigger, the "no invention" rule did not.

## Logging

Log real decisions and open questions in a decision log under this same feature
folder (a fresh one, or continuing `Tour-Experience-Module-Phase2/Decision-Log.md`
with a clear dated break marking the restart — thread's judgment) — same dated-
entry discipline every other thread in this project uses: what was decided, the
reasoning including the heart of it, the specific next action. Don't let a real
decision live only in this thread's own conversation history.
