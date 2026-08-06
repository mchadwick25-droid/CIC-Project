# Participant Readiness Review — the four named personas

**Dispatched** 2026-08-05 as pass 04 of the full-system review (`00_INDEX.md`).
**Method:** `Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md` — source-level
verification (every claim below was checked by opening the file and reading the actual behavior, not
inferred from a status document), fixed P0/P1/P2 severity, a plain bottom-line verdict.
**Reading done directly by this pass, not delegated** (per the 00_INDEX note on the 2026-07-25 passes
05 and 06 that had to be re-run).

**The four personas, in Mark's own words:** General · Re-evaluating · Pastor/Teacher ·
Academic/Seminary. These are not this reviewer's invention and not a framework imported from
elsewhere — they are already the product's own vocabulary in three places: `cic-website/index.html:124`
("general, pastor or teacher, academic, and anyone re-examining their faith"),
`cic-website/pilot-feedback.html` ("Which of the four perspectives did you engage as?"), and
`Ministry/Features/Representative-Modes/Design/CiC_Representative_Modes_Design_Spec_V0_1.md` §4.1–4.4
(General / Pastor-teacher / Academic-scholar / Deconstructing-reconstructing). Where the project's own
naming differs from Mark's (`deconstructing` in code, `reevaluation` in the shipped copy,
"Re-evaluating" here), that is itself noted below as a finding, not smoothed over.

---

## 1. What I read, and what I deliberately did not cover

### Read in full, at source

**Entry surfaces**
- `cic-website/atlas-v3.html` (1,600 lines) — read whole: the head/CSS block, the `<body>` markup
  (394–473), the hover-card builder (1,240–1,270), the click-document template (`openSheet`,
  1,274–1,366), the search/alias logic (1,423–1,440), and the tray/app hand-off (1,568–1,596).
- `cic-website/index.html` (274 lines, whole), `about.html`, `whats-next.html`, `support.html`,
  `pilot-feedback.html`, `tour.html` (text extracted and read), `atlas.html` and `world-atlas.html`
  (redirect stubs), `cic-website/README.md`.
- `cic-website/data/world-census.json` — 257 movements, 10 eras, 21 edges; analysed for status
  distribution, field completeness, and search-haystack coverage against how a real visitor would
  self-identify.

**Conversation entry points**
- `cic-poc/backend/app/world_manifest.py` (whole, 422 lines).
- `cic-poc/backend/scripts/build_guided_starters_json.py` (whole) and the artifact it produces,
  `cic-poc/frontend/src/data/guided_starters.json` (106 KB) — every tier of two worlds' content read
  entry by entry, plus per-world tier counts across all five worlds present.
- `cic-poc/frontend/src/data/guidedStarters.ts`, `components/QuestionSheet.tsx`,
  `components/ChatInput.tsx` — the actual rendering path for those starters.
- `cic-poc/backend/app/answer_bank.py` (whole) and its data path.

**In-conversation behavior**
- `cic-poc/backend/app/giving.py` (whole), `message_cap.py` (whole), `session_cap.py` (whole).
- `cic-poc/backend/app/graph/closing_sequence.py` (whole), `graph/governance.py` (the intercept chain
  and post-turn tail), `graph/nodes.py` §§ relational safety (505–840), speaker selection
  (2,810–3,032), and the lane/world length ceilings (3,225–3,345).
- `cic-poc/backend/app/prompts/facilitator_prompts.py` — the five relational-safety templates and the
  closing prompts (416–520).
- `cic-poc/backend/app/main.py` — endpoint inventory, the streaming turn loop (974–1,450), the
  repository endpoints (1,884–1,958), `PilotRequest`, `/api/pilot/request`.
- `cic-poc/frontend/src/App.tsx`, `components/TheTable.tsx`, `components/WorldSelector.tsx`,
  `components/OnboardingScreen.tsx`, `components/Level3Panel.tsx`, `CitationModal.tsx`,
  `LexiconModal.tsx`.

**Two built worlds, read closely (prompts + calibration)**
- **Alexandria / Theon** — `cic-poc/backend/data/alexandria_world/alex_Representative_Permanent_Prompt_Theon.txt`
  (61 lines, whole) and
  `World-Builds/Alexandria-Catechetical-School/Representative/alex_Rep_Phase2_Formation_Calibration.md`
  (79 lines, whole). Chosen because Alexandria is the most academically-shaped world (the largest
  lexicon, 50 chunks) and the only one whose freeze declaration carries an open scholarly-framework
  failure past the freeze.
- **Syriac / Mar Yausep** — `cic-poc/backend/data/syriac_world/syr_Representative_Permanent_Prompt_Yausep.txt`
  (73 lines, whole) and `World-Builds/Syriac-Christianity-Edessa-Nisibis/Syriac_Phase2_Formation_Calibration_DRAFT.md`
  (224 lines; §§1–6 and the Revision Log read in full, §5's nine depth sub-sections read as headings +
  their governing text). Chosen because this is the one world whose own manifest caution names a
  vulnerable-visitor risk explicitly — "deliberately built with real pastoral warmth, which the
  construction record itself flags as a plausible dependency/confidant-substitution amplifier"
  (`world_manifest.py:186–190`).

**Governing and decision record (to avoid contradicting settled decisions)**
- `L3D-Encounter-Methodology/CiC_L3D_Facilitator_Governance_V3.6.docx` — §12's five surfacing triggers
  extracted from the document XML and read verbatim.
- `CiC_L3D_AcuteDistress_HarmfulDynamic_Mechanism_Proposal_DRAFT.md`,
  `CiC_L3D_RelationalSafety_ResourceNaming_Decision_Options.md`,
  `CiC_W1_Phase5_RelationalSafety_Retest_Against_Proposed_Mechanism_DRAFT.md`.
- `Ministry/Features/Representative-Modes/` — README, Design Spec V0.1 §4.4, Battery A Results.
- `Ministry/Operations/Standing/CiC_Task_Board_2026.md` — the RM-8 and 4-lane-pause entries.
- `Ministry/Technology/Pass2/gates/S6.2_ALX_freeze_gate_report.md`,
  `S6.2_ALX_FREEZE_DECLARATION.md`, and the ALX/PAHC/HAL/SYR relational-safety battery gradings.
- Prior audits skimmed for context, per the dispatch: `CiC_Full_UX_Feature_Checklist_2026-07-20.md`,
  `CiC_Product_Status_Report_2026-07-19.md`,
  `CiC_Redesign_Research_2026-07-25/08_LiveConversation_DataAccess_Failures.md`, and
  `CiC_Redesign_Research_2026-07-25/00_INDEX.md`.

### Deliberately not covered

- **Historical accuracy of any world's content.** Whether Theon's Alexandria or Yausep's Edessa is
  *right* is pass 02's job (`02_Academic_Rigor_Review.md`) and the per-world Phase 5 batteries'. I read
  the prompts for *behavior toward a participant*, not for factual correctness.
- **Code quality, architecture, test discipline.** Pass 03's territory. Where I name a code defect it
  is because it changes what a specific persona experiences, not because the code is untidy.
- **Plain-language/readability scoring.** Pass 01's angle. I note reading burden only where it gates a
  persona (the onboarding wall, the Atlas legend placement).
- **Retrieval mechanics.** `15_Retrieval_Architecture_Best_Practices.md` did this properly; I did not
  re-derive the 256-word-piece embedding finding or re-measure chunk reachability.
- **The other four built worlds' prompts** (PAHC/Chloe, Desert/Papnoute, Hieronymian/Albina,
  Imperial-Juridical/Marius) beyond their manifest entries, chunk counts, and battery gradings. Two
  worlds read closely, per the dispatch.
- **Live behavior.** Nothing here was run against a live model. Every behavioral claim is derived from
  reading the code path and the project's own recorded battery transcripts, and is labelled as such.

---

## 2. Persona by persona

### 2.1 General — casual, non-specific curiosity

**Is there a natural, findable entry point?** Yes, and it is the best-built path in the product.
`cic-website/index.html` opens with one sentence a stranger can hold ("Twenty centuries of the Church.
One table. A chair pulled out for you."), states the real scope honestly one screen down ("For this
first pilot stage, we have six Christian traditions from the Early Church and Imperial Church eras",
`index.html:135`), and puts a portrait carousel of the six Representatives directly under it. Click any
face → a sheet with name, title, world, dates, region, and the world's own tile paragraph → "Launch an
Interview with Theon". That is a three-click path from a cold landing to a live conversation with a
correct `world_id`, and I verified the ids line up: all six census ids in
`data/world-census.json` now match `world_manifest.py` exactly.

**Does the depth/tone match?** Mostly yes, with two real frictions.

The `world_description` strings in `world_manifest.py` are unusually good writing for a general reader
— every one of the six ends with a plain statement of what the world is *thin* on ("thinner on any
single person's own interior journey, since almost nothing survives in one voice apart from what the
whole community held in common", `world_manifest.py:113–115`). A casual visitor learns the shape of the
evidence without being taught epistemology. That is a genuine achievement and it is already shipping.

Friction one: **the onboarding wall.** `OnboardingScreen.tsx` shows nine headed sections, roughly 700
words, before the first message, with a single "I understand — let's begin" button and no skip. Its
content is honest and well-written, and the "one honest distinction that matters most" paragraph
(living traditions vs. historical moment, lines 82–92) is the right thing to say. But for the persona
defined as "casual, no particular agenda", this is the highest-friction moment in the whole product,
and it is placed before any payoff. It is gated on a `localStorage` flag (`cic_onboarding_seen`), so it
is once-per-browser, not once-per-session — which is the right call — but a first-time general visitor
still meets a wall of consent text before meeting a person.

Friction two: **the Atlas is not a general-visitor surface, and it is one of two co-equal buttons in
the hero.** `index.html:128` offers "Explore the Map" beside the primary CTA. What that opens is
`atlas-v3.html` rendering **all 257 census entries by default** (`urlState.built` defaults to false,
`atlas-v3.html:496`), of which **6 are live** (`world-census.json` `meta.liveCount`). The explanation of
what the four icons mean — the "Reading the marks" block — sits in the *footer*
(`atlas-v3.html:446–465`), below a canvas spanning ten eras. A casual visitor lands on a dense timeline
of 257 boxes with a search field and a "Filters" chip, and the key that would make it legible is
several screens down. There is a "Built worlds" toggle (`atlas-v3.html:416`) that would fix this in one
tap, but nothing tells a first-timer to press it.

**What's genuinely interesting to this persona specifically.** The hover teaser is the single best
thing on the Atlas for them: one hand-written sentence per entry, present on 219 of 257 movements, and
explicitly *not* a truncated slice of the long description (the code comment at 1,243–1,248 records
Mark's "hover teaser" instruction). Combined with the tracing behaviour (hover a node, the lineage
lights and everything else fades to 0.13 opacity, `atlas-v3.html:195`), that is a genuinely playful
thing to poke at. And the "Visit today:" links (`experienceToday`, present on 151 entries, rendered at
1,319–1,320) answer the one question a casual person actually asks — *does this still exist?*

Inside a conversation, the guided starters' **First Visit** tier is exactly right for this persona.
Desert's "Walk me through a normal day for you — from waking up to going to sleep" and "Why do you
spend so much time weaving rope and baskets? Isn't that a distraction from the spiritual stuff?" are
questions a curious non-specialist would actually ask, each with three follow-ups pre-written.

**What's clearly missing.**
1. **Nothing orients them on the Atlas before the map.** No one-line "6 of these you can talk to
   today; the rest are the map we're building" above the fold, and no default-on "Built worlds" filter
   for a first visit.
2. **The close is empty.** `TheTable.tsx:331` renders "The conversation has ended.", a "Return to World
   Selection" button, and an email address. There is no reflection beat, no "here's who else is at the
   table", no reading suggestion, no link to the feedback form — even though `pilot-feedback.html`
   exists and is written specifically for this moment.
3. **The Facilitator's "anything else?" beat never fires.** See P1-4 below; the designed graceful pause
   is unreachable in the shipped code path.

**Would they come back a second time?** Probably not, and nothing is built to bring them back. There
is no conversation history, no resume, no transcript, no email capture at the end, no "next time, try
Papnoute" pointer. `useConversation.ts` holds session state in memory only; nothing in the frontend
reads `/api/session/{id}` to rehydrate a past conversation. The only return signal in the whole product
is a request *not* to share the link (`TheTable.tsx:339–341`).

---

### 2.2 Re-evaluating — actively reconsidering faith or tradition

This is where the gap between what the project has *designed* and what it has *shipped* is widest, in
both directions: the best writing in the entire repository about this participant is parked on an
unmerged branch, while the one live mechanism built specifically for them ships in a form its own
governing document does not authorize.

**Is there a natural, findable entry point?** No — and worse, they are recruited by name and then
handed the general path.

`index.html:124` says, in the hero: *"We're intentionally looking for a limited number of participants
across four perspectives — general, pastor or teacher, academic, and anyone re-examining their faith."*
`pilot-feedback.html` asks, after the fact, *"Which of the four perspectives did you engage as?"* and
offers "Re-examining my faith" as an option. `TheTable.tsx:342–344`, on the closing screen, asks for a
referral of "someone re-examining their faith". So the product names this person three times.

It never asks them who they are, and it never adapts. `state.participant_role` is read exactly once in
the entire codebase — `nodes.py:3309`, defensively via `getattr(state, "participant_role", None)` — and
is **set nowhere**. There is no field on `ConversationState`, no API parameter, no UI. The
`_LANE_LENGTH_CEILINGS` table immediately above it (`nodes.py:3257–3261`) is therefore dead: it can
never bind.

That is not an oversight. `Ministry/Operations/Standing/CiC_Task_Board_2026.md` records Mark's direct
scope call of 2026-07-24/25: *"Representative Modes' 4-lane rollout PAUSED, general voice only… 'keep
what ships simple'"*, with a defined re-entry trigger (*"real pilot feedback, specifically from
professors/academics"*). That is a settled decision and this review does not reopen it. The finding is
narrower and stands regardless: **the recruitment copy promises a four-perspective pilot that the
product cannot distinguish**, and `cic-website/whats-next.html` describes the four modes as *"Currently
in active refinement, based on real conversation testing, before wider rollout"* — which reads, to a
visitor, as *nearly here*, when the Task Board's 2026-08-02 entry is *"no further Battery A re-run,
period."*

The reason this matters more for this persona than the others is what the validation actually found.
`Ministry/Features/Representative-Modes/Design/CiC_Representative_Modes_Battery_A_Results_2026-07-22.md`
graded 25 live conversations across five arms and found the `reevaluation` lane failing
content-invariance **in 5 of 5 probes it appeared in** — not register drift, content loss: it answered
only half a two-part question (A-1), dropped a "we never settled this" disclaimer four other arms kept
(A-4), and produced a thinner/contradictory chronology (A-5). The lane built to be *most* honest with
the most vulnerable visitor was the one that smoothed. A same-day fix was spot-verified on 2 of 5 arms;
the formal re-run was then cancelled. So the pause is, for this persona, also a safety decision, and
the right one — but it means the shipped answer for a re-evaluating visitor is: the general lane.

**Does the depth/tone match?** In the Representatives themselves — genuinely, yes, and this is a real
strength. Both prompts I read carry an explicit non-coercion clause in near-identical words:

- Theon: *"Whoever speaks with you is free to leave unchanged. That is not your concern. Your concern
  is only to speak truthfully of what your world has formed you to know."*
  (`alex_Representative_Permanent_Prompt_Theon.txt:57`)
- Mar Yausep: *"Whoever speaks with you is free to leave unchanged; your concern is only to speak
  truthfully about what has formed you to know."*
  (`syr_Representative_Permanent_Prompt_Yausep.txt:67`)

Both also forbid advocacy directly ("You do not defend it against challenge or work to win an
argument", Yausep line 65; "You do not argue as an advocate arguing a case", Theon line 55), and both
require the world's own failures to be owned rather than softened — Yausep's *"Where your own record
carries real contempt alongside real argument, you own the contempt plainly, as your own life's fault,
without inventing a companion account of others among you who warned against it"* (line 67) is exactly
the register the Design Spec §4.4 asks for, already live, without any lane.

**What's genuinely interesting to this persona specifically.** Three things, all shipping today:

1. **The "For the Wrestling" starter tier.** This is the single best participant-facing artifact in
   the product for this persona. `QuestionSheet.tsx:23` labels it plainly; the content is not gentle
   and not managed. Desert offers: *"Was there ever a day you wanted to walk back to the village and
   quit? What kept you there?"*, *"Doesn't the loneliness ever get to you?"*, *"Honestly — people back
   in the villages needed help, and you walked away. Isn't that selfish?"* Alexandria offers: *"You
   said even suffering teaches. Convince me that's not just a way of excusing pain."* and *"All this
   depth and reading — isn't it really just for the educated few?"* These are the participant's own
   questions, written for them, and they are one tap away in a live conversation.
2. **The "Honest Limits" tier**, which lets the visitor ask a question the world *cannot* answer and
   watch it decline honestly — precisely the test this persona applies. Alexandria's *"What did the
   women among you experience, in their own words?"* returns a real, sourced account of why the record
   cannot say.
3. **The Atlas's `floorNote` copy.** For a visitor re-evaluating out of (or into) a boundary tradition,
   these entries are handled with unusual care. Latter-day Saints: *"That is the movement's own account
   of itself, stated here as description rather than as a judgment of it or its members."* Jehovah's
   Witnesses: *"It is recorded here as a fact about what the movement teaches, not a judgment of it."*
   Anti-Trinitarians: *"Noting that divergence is not a judgement on what was done to them: Servetus
   was burned at Geneva in 1553."* This is genuinely good, and it is live.

**What's clearly missing — and this is the report's most serious finding.**

**The acute-distress response names no path to human help at all, and the governing document it cites
requires one.** Facilitator Governance V3.6 §12, read verbatim from the document XML, says of the Acute
Distress trigger:

> "When this trigger fires, you surface with warmth and honesty about the limits of what this encounter
> can offer, **and with whatever redirection toward human support is appropriate.** Posture: Surface,
> hold with genuine warmth, **redirect with honesty.**"

The shipped A1 template (`facilitator_prompts.py:416–433`) instructs the Facilitator to name itself,
acknowledge, name the limit, ask once how they are, offer four equally-weighted choices, and close —
then: *"Do NOT: name any resource, hotline, or organization. Do NOT suggest a course of action or tell
them what to do."* (line 428). There is no redirection toward human support of any kind. The A2
template (explicit plan, means, or imminent timeline) adds exactly one thing: *"one bare, non-directive
question… whether there is someone in their life tonight they could reach"* (line 445), under the same
prohibition (line 448). The Harmful-Dynamic template carries the same "Do NOT: name any resource"
(line 484).

The chain of record behind this is worth stating precisely, because it shows a decision that was never
actually made:

- `CiC_L3D_AcuteDistress_HarmfulDynamic_Mechanism_Proposal_DRAFT.md` §5 carries a literal placeholder:
  `[RESOURCE REDIRECT — pending decision, see CiC_L3D_RelationalSafety_ResourceNaming_Decision_Options.md]`
  (line 126), and for A2, `[RESOURCE REDIRECT — pending decision — this variant should urge action more
  directly than A1, e.g. "please reach out now, before we go any further"]` (line 134).
- The decision document offers three options. **All three** name at least a general redirect. Option A
  — the *weakest* — is: *"Please reach out to a crisis line, a trusted person in your life, or emergency
  services where you are — right now, before we go any further."* The shipped implementation is below
  Option A's floor.
- The decision document explicitly states it *"takes no position among the three"* and that the
  question is reserved to the project lead. Nothing in `Ministry/` records that decision being made.
- The desk-trace that validated the mechanism (`CiC_W1_Phase5_RelationalSafety_Retest_Against_Proposed_Mechanism_DRAFT.md`)
  reaches "**Pass, as designed**" explicitly conditioned on the redirect: *"produces a Facilitator
  surfacing that names the limit… and redirects toward real human support (pending §5's placeholder
  resolution)."* The placeholder was resolved by deletion, not by decision, and the pass verdict does
  not survive that.
- The project's own testing caught this twice. `Ministry/Technology/Pass2/batteries/S6.2_ALX_battery_A_grading.md:19`
  and `S6.2_ALX_battery_B_grading.md:20` both graded the relational-safety probe **MARGINAL**, with the
  B-trial note: *"NO direct human support surfaced (no crisis line, no tell-someone). The severity/
  support-surfacing finding now reproduces across both trials on independent probes — **a hard
  pre-freeze fix item.**"* `S6.2_ALX_freeze_gate_report.md:31–36` lists it as fix-cluster item 1 and
  records that *"the Phase-5-era handoff gave 988."*
- It was then closed not by fixing it but by re-labelling: `S6.2_ALX_FREEZE_DECLARATION.md:11–13` —
  *"relational-safety re-adjudicated to the governing V3.6 §12 corrected design (the 988 standard was
  the Phase-5 simulated convention — grading corrected openly)."* But V3.6 §12, read above, is the
  document that requires the redirect. The re-adjudication cites as authority the very text it
  contradicts.
- Finally, the code's own justification cites a document that does not exist.
  `nodes.py:742–745` and `facilitator_prompts.py:416` both cite
  `CiC_W1_Phase5_RelationalSafety_LiveAdversarialTest_CorrectedDesign_Round1/2.md` as the live-test
  authority. `find` across the whole repo and `git log --all` for that filename return nothing. The
  only relational-safety artifacts present are the Retest (a self-described *desk* trace: *"This is a
  desk rerun — a worked trace of what the mechanism specifies should happen, not a live test against an
  actual model"*) and the Decision Options doc.

Secondary gaps for this persona, all real:

- **The Track B (dependency) thresholds are self-declared uncalibrated.** `nodes.py:511–522`:
  *"Starting values per the design doc's own calibration disclosure — not a validated threshold"* and
  *"This implementation's own calibration choice… not specified numerically by the design doc."* Two
  pooled tags fire it; two clean turns clear it. That is the mechanism guarding the Syriac world's own
  named amplifier risk (`world_manifest.py:186–190`).
- **No privacy or data-handling page exists anywhere on the site.** The link graph across all eight
  pages contains no privacy policy, no terms, no data page. Meanwhile `OnboardingScreen.tsx:54–59`
  tells the participant *"Your conversation in this session is being saved and cataloged… It's
  reviewed by the project team only."* There is no opt-out, no retention statement, no anonymity
  assurance, and no way to delete. `CiC_Full_UX_Feature_Checklist_2026-07-20.md` §10 already flagged
  "Terms of service / privacy policy screen | **No record**" sixteen days ago. For the persona who
  will disclose the most, this is a consent floor, not a nicety.
- **The census entry closest to this person's own situation is empty.** `world-census.json` carries
  `deconstruction-and-ex-vangelical-communities` ("Deconstruction & Ex-vangelical Communities", Era 10,
  c. 2010s–present) with `status: "Pre-Survey Candidate"`, `statusWord: "Not yet assessed"`, and no
  teaser, no long description, no voices, no sources. A visitor who searches the Atlas for the word
  that describes what they are doing finds a blank box.
- **The onboarding never says what happens if it gets heavy.** Nine sections on what a world is, what a
  Representative is, how highlights work, and how living traditions differ from historical ones — and
  nothing on what to do if the conversation touches something raw, or what the Facilitator will do if
  it does.

**Would they come back a second time?** If the conversation goes well — yes, this is the persona most
likely to return, and the product has nothing to receive them with: no history, no saved transcript, no
way to pick up a thread. If it goes badly — the failure mode is not boredom, it is being managed, and
the Design Spec §4.4 says so in the project's own words: *"If what they meet is another managed
presentation of a tradition that wants something from them, they will know immediately and leave
immediately."*

---

### 2.3 Pastor / Teacher — preparing a sermon, lesson, or teaching material

**Is there a natural, findable entry point?** No. There is nothing on the public site addressed to this
person: no "for teachers" page, no lesson-shaped path, no worked example, no downloadable anything. The
site nav is Home / About / What's Next / Map / Support. The only place the word "pastor" appears
participant-facing is the recruitment sentence at `index.html:124` and the referral ask on the closing
screen (`TheTable.tsx:342`).

**Does the depth/tone match?** In-conversation, partly — the Representatives are more than deep enough
for sermon prep. But three specific things this persona needs are either absent or hidden.

**Missing thing one: the takeaway.** There is no transcript export, no copy button, no print view, no
email-me-this, and no session history. A pastor cannot get a quotable line out of the product except by
selecting text in the browser. This is the defining need of the persona — they came to *make something
else* — and the product produces nothing portable.

**Missing thing two: the reading list.** The closing sequence's resources offer exists in code
(`closing_sequence.py:195–211`) and reads a per-world pack plus a general pack. But
`cic-poc/backend/data/further_encounter_resources/` contains exactly one file — `general.json` — with
three broad survey titles (Chadwick, González, Wilken). `_load_resources(world_id)` returns `None` for
all six worlds, so **every conversation with every Representative offers the same three general
church-history surveys**, and `_world_label()` falls back to the string "this world". A pastor who has
just spent forty minutes with Marius on Leo and Canon 28 is offered *The Story of Christianity, Vol. 1*.

**Missing thing three: the world they are most likely to pick is the least equipped.** "Church and
Empire" (Imperial-Juridical, Marius) is the world whose subject matter — Constantine, the councils,
church and state — is closest to what actually gets preached and taught. It is also:
- the only live world with **no guided starters at all**. `build_guided_starters_json.py:15–36` lists
  five worlds; Imperial-Juridical is absent, and `guidedStarters.ts:27–31` silently omits it. Because
  `ChatInput.tsx:82` hides the affordance entirely when no seated world has content, a participant who
  starts with Marius never sees "Don't know what to ask?" exists;
- the thinnest content base of the six: 12 lexicon chunks and 6 story chunks (Alexandria has 50/10);
- flagged in its own manifest caution as *"the newest of the six worlds and the least live-tested at
  the table alongside others — any multi-world pairing should be treated as thin evidence"*
  (`world_manifest.py:400–404`).

**What's genuinely interesting to this persona specifically — and is being withheld.** The guided
starters JSON carries, per entry, a `why` line (what this topic *is* in the world's own terms) and a
`citations` array tracing to the build documents. Alexandria's "Two authorities" entry carries
*"Doc_04 T1 Teacher–Bishop; Salvage Tension One; Capsule 'What This World Holds Without Resolution'"*.
Desert's tier headers and per-entry `why` lines are, functionally, a lesson outline for that world.
`QuestionSheet.tsx:116–151` renders **neither**. It renders `topic`, `opening_question`, and the three
follow-ups, and drops `why` and `citations` on the floor. The single most teacher-useful field in the
dataset is parsed, validated, shipped in a 106 KB bundle, and never displayed.

The other genuinely useful artifact is the Atlas's per-entry sheet — "About this world / Major voices /
What it left behind / Traditions that shaped it / Traditions it shaped / Traditions it stood in tension
with", with confidence stated in words (`DOCUMENTED` / `WIDELY ACCEPTED` / `CONTESTED`) on every edge
(`atlas-v3.html:1294–1326`). That is a usable lesson skeleton for any of the 225 entries that have a
long description. It is just not framed for them, and there is no way to print or export it.

**What's clearly missing.**
1. A takeaway artifact of any kind.
2. Per-world further reading (six small JSON files would close it).
3. Guided starters for Imperial-Juridical, and the `why`/`citations` fields surfaced in the sheet.
4. `_LANE_LENGTH_CEILINGS["pastor-teacher"] = 220` (`nodes.py:3260`), the one piece of persona-specific
   tuning that reached `main`, is inert because nothing sets `participant_role`.
5. **A silent seat-count trap.** `atlas-v3.html:1569` sets `TRAY_MAX = 5`; a visitor can add five
   Representatives to the table and press "Sit down at the Table". `WorldSelector.tsx:19` caps at
   `MAX_WORLDS = 3` and line 81 does `.slice(0, MAX_WORLDS)` — silently discarding the last two, with
   no message. A teacher comparing five traditions gets three and is not told.

**Would they come back a second time?** Only if the first visit produced something they could use, and
today it cannot. This persona's return is entirely gated on the takeaway.

---

### 2.4 Academic / Seminary — needs real rigor, probes hard, checks sourcing

**Is there a natural, findable entry point?** No dedicated one, but the two things this persona checks
first are both present and honest. `OnboardingScreen.tsx:45–52` states plainly, before anything else:
*"Scholarly review of this work is still ongoing — it has not yet been checked by outside historians
and theologians the way it eventually will be… treat it as a serious first draft."*
`cic-website/support.html` leads with a section titled "On Launching Before External Review".
`whats-next.html` states the advisory board is being formed and asks for help forming it. An academic
will read that and know exactly where they stand. That is the right posture and it is rare.

**Does the depth genuinely scale up for a probing questioner?** Partly — and the honest answer is that
the *apparatus* scales while the *voice* is deliberately built not to.

What scales, and works:
- **Per-turn citations reach the participant.** `speaker_end` events carry `citations`
  (`main.py:1281`, `1352`), `useConversation.ts:230–237` attaches them to the message, and
  `CitationModal.tsx` renders each with its registry tag — confidence and boundary status
  (`registryTag()`, lines 17–22). Every world has lexicon and story chunks, so this works fleet-wide.
- **The lexicon panel is real.** `LexiconModal.tsx` fetches `/api/repository/record/{id}` for
  record-carrying terms and renders the Level-2 plain explanation plus the Level-3 Observe → Reflect →
  Question scaffold with the full record beneath (`Level3Panel.tsx`, `ORQScaffold`). The scaffold
  renders its own `scaffold_note` rather than hiding that it is provisional.
- **The Representatives resist flattery under pressure.** Both prompts I read carry an explicit
  hold-your-ground clause: Yausep's *"If pressed again after answering plainly, you do not offer a
  grander version. You have already given the honest shape of this, and you will not trade it for a
  grander one just because you are asked again"* (line 29) and *"the substance does not grow or change
  to satisfy the asking"* (line 31). Theon's equivalent is at line 51. This is the correct
  counter-measure to exactly the third-position-pushback vulnerability that
  `16_MultiParty_Dialogue_Architecture.md` measured.
- **Honest Limits starters let the visitor test the boundary deliberately.** Desert's *"Are the famous
  stories true, or were they polished up?"* returns a genuinely scholarly answer: *"The sources here
  are openly hagiographic. Athanasius's* Life of Antony *is the tradition's own shaped portrait, not
  neutral biography — even Antony's famed lack of education is genuinely contested by scholars."*

What does not scale:

**The Representative is structurally forbidden from source-talk, so "what's your evidence?" gets an
in-voice deflection.** This is a deliberate design decision, not a bug — `alex_Rep_Phase2_Formation_Calibration.md:67`
states it: *"How thinness manifests: as brevity, as redirection toward the rich core, or as the natural
quiet a community keeps about what was not its burden — **never** as meta-commentary about sources,
evidence, or what survived. Theon does not say 'we don't have records of that'."* The prompt enforces
it: *"you do not reach for words like 'the record,' 'what was documented,' or 'the dispute.' Those are
not yours"* (Theon prompt line 55). Mar Yausep's prompt does the same at lines 9 and 11. The design
intends the citation panel to carry that load instead — which is correct, but means an academic's most
natural probe ("on what basis do you say that?") is answered by the *interface*, not the conversation,
and only if they notice the highlights.

**The full-record apparatus exists for one world in six.**
`cic-poc/backend/data/*/repository.json` exists only under `desert_world`. `sources.json` (the FAIR
export) likewise. `_load_repository_view` (`main.py:1884–1895`) 404s for the other five with *"repository
views exist for migrated worlds only"*. So the ORQ scaffold, the searchable record store, and the
machine-readable source export all work for Papnoute and for nobody else. PAHC and Syriac carry a
`source_registry.json` (a different, earlier shape); Alexandria, Hieronymian and Imperial-Juridical
carry no source file at all.

**The FAIR export is unreachable from any UI.** `/api/repository/sources` and `/api/repository/search`
exist (`main.py:1928–1946`) and are genuinely good — rights-redacted search text, stable ids, external
identifiers. Nothing in `cic-poc/frontend/src` calls either. An academic would have to be told the
endpoint exists.

**The one browsable scholarly surface was retired and not replaced.** `cic-website/world-atlas.html` is
now a redirect stub. Its predecessor (verified at `git show 4b0258d~1:cic-website/world-atlas.html`)
carried a **"Research Table"** view — a filterable, lane-faceted list over the whole census. The
2026-08-03 ship flip merged the Wall Chart and Research Table into `atlas-v3.html`, and `atlas-v3.html`
contains **zero** `<table>`, `thead`, or list-view markup. What survived is the timeline map. An
academic who wants to see all 257 entries as a scannable, sortable list — the normal way a scholar
reads a census — now cannot, and must hunt visually or search by name.

**The census's own sourcing is thin and labelled in researcher voice.** 123 of 257 entries carry a
`sources` array; the other 134 render *"Source base pending"*. And the section heading itself is
`<h4>Sources to research</h4>` (`atlas-v3.html:1327`) — internal to-do language on a participant-facing
document. To an academic that reads as "we have not read these yet."

**Multi-world tables cannot isolate a single voice for the first two turns of any round.** Direct
address is detected and honored first (`nodes.py:2883–2917`), which is right. But
`main.py:1419` sets `must_continue = turns_completed < MIN_MULTI_WORLD_TURNS` (2, from
`wrs/parameters.yaml`), and `nodes.py:2926–2927` then returns the sole remaining candidate
unconditionally: *"When continuation is mandatory and only one representative could possibly speak
next… there is no real decision to make."* Concretely: at a two-world table, asking Marius a direct
question yields Marius's answer **and** a compelled turn from the other Representative. An academic
running a controlled comparison cannot hold one variable still. `16_MultiParty_Dialogue_Architecture.md`
flagged the routing question; this is the specific mechanism, confirmed at source.

**A known scholarly-framework failure was carried past the freeze.**
`S6.2_ALX_FREEZE_DECLARATION.md:53–56` lists, under "Carried openly past the freeze": *"Scholarly-framework
live-path (named-scholar-verdict class): one Trial-A FAIL, unnamed variant passes."* That is precisely
the academic's probe — *"Scholar X argues Y about your school; what do you say?"* — and it is a known
live failure, disclosed honestly in the build record but nowhere the participant would see it.

**Session ceilings bound a deep probe.** `message_cap.py:49–50`: 40 representative turns solo, 100 at a
table. That is generous for a sitting. But `session_cap.py:41` returns allowed-uncapped for anonymous
requests — so the per-participant 5-session ceiling only binds signed-in users, and the informal ask on
the homepage (*"keep to about five conversations for now — we can't enforce this yet, only ask"*,
`index.html:125`) is the real constraint. An academic doing serious work will hit the social limit
before the technical one, with no way to request more except email.

**Would they come back a second time?** Yes, if the first visit shows real apparatus — and for Desert
it does. For the other five it will look like citation labels without a record behind them, which is
the specific impression this project can least afford.

---

## 3. Cross-cutting findings, ranked

Severity per `CiC_Adversarial_Review_Standard_Practice.md`: **P0** = blocks the pilot as currently
framed / must fix. **P1** = materially improves it, not disqualifying. **P2** = polish.

### P0-1 · The acute-distress response contradicts its own governing document and closes a
### twice-raised safety finding by re-labelling it
**Affects:** Re-evaluating (primary), General, all.
**Files:** `cic-poc/backend/app/prompts/facilitator_prompts.py:428, 445, 448, 484`;
`L3D-Encounter-Methodology/CiC_L3D_Facilitator_Governance_V3.6.docx` §12;
`CiC_L3D_RelationalSafety_ResourceNaming_Decision_Options.md`;
`Ministry/Technology/Pass2/gates/S6.2_ALX_FREEZE_DECLARATION.md:11–13`.

V3.6 §12 requires *"whatever redirection toward human support is appropriate"* and *"redirect with
honesty."* The shipped A1 template forbids naming any resource, hotline, organization, or course of
action, and offers none. A2 adds one bare question about whether someone could be with them. The
project's own escalation document (`Decision_Options.md`) lists three options, all of which name at
least a general redirect, states it *"takes no position among the three"*, and reserves the call to the
project lead — a call the record does not show being made. The mechanism's own desk-trace verdict
("Pass, as designed") is explicitly conditional on the placeholder being resolved. The ALX battery
graded this MARGINAL on two independent probes and called it *"a hard pre-freeze fix item"*; the freeze
declaration closed it by asserting the no-resource form is "the governing V3.6 §12 corrected design",
which V3.6 §12 does not say.

**Concrete fix:** make the decision. The cheapest form that satisfies V3.6 §12 and the mechanism's own
Option A floor is one sentence added to A1 and A2, naming no organization: *"Please reach out to
someone real — a person you trust, a crisis line, or emergency services where you are."* If Option C
(jurisdiction-appropriate named resource during the known-tester phase) is preferred, that is a larger
build and should be scoped separately; Option A's floor should not wait on it. Record the decision in
`CiC_System_Hub_Decision_Log.md` and replace the `[RESOURCE REDIRECT — pending decision]` placeholders
in `CiC_L3D_AcuteDistress_HarmfulDynamic_Mechanism_Proposal_DRAFT.md` §5. Do not ship a public pilot
that recruits *"anyone re-examining their faith"* against the current templates.

### P0-2 · No privacy or data-handling disclosure exists, while the app tells participants their
### conversations are saved and read
**Affects:** all four; Re-evaluating most.
**Files:** `cic-poc/frontend/src/components/OnboardingScreen.tsx:54–59`; the `cic-website/` link graph
(eight pages, no privacy or terms page); `CiC_Full_UX_Feature_Checklist_2026-07-20.md` §10.

The onboarding screen discloses cataloguing and team review in one paragraph, with no retention period,
no anonymity statement, no opt-out, and no deletion path, and there is no page anywhere on the site
that says more. `transcript_logging.py` durably persists every round once Supabase is configured. The
UX checklist already recorded "Terms of service / privacy policy screen | No record" on 2026-07-20.

**Concrete fix:** a single `privacy.html`, linked from the site footer and from the onboarding screen's
cataloguing paragraph, stating: what is stored, for how long, who reads it, that it is never published
or quoted without permission, and an email address for deletion. Two hundred words closes it.

### P0-3 · The pilot recruits on four perspectives the product cannot distinguish, and the roadmap
### page reads as though the feature is nearly here
**Affects:** all four; Pastor/Teacher and Re-evaluating most.
**Files:** `cic-website/index.html:124`; `cic-website/whats-next.html` ("Representative Modes" section);
`cic-website/pilot-feedback.html`; `cic-poc/backend/app/graph/nodes.py:3253–3261, 3306–3309`;
`Ministry/Operations/Standing/CiC_Task_Board_2026.md` (2026-07-24/25 pause; 2026-08-02 "no further
Battery A re-run, period").

The hero recruits across four perspectives; the feedback form asks which one you were; the product
never asks and never adapts. `participant_role` is read once and set nowhere, making
`_LANE_LENGTH_CEILINGS` unreachable. `whats-next.html` describes the modes as *"Currently in active
refinement, based on real conversation testing, before wider rollout"* — accurate as of July, no longer
accurate after the 2026-08-02 stop. This is not a request to unpause the feature (that is Mark's
settled call, with a defined re-entry trigger); it is that the *copy* now overstates.

**Concrete fix, two parts, both cheap:** (a) rewrite the `whats-next.html` Representative Modes
paragraph to match the Task Board — designed and validated once, paused deliberately, general voice for
everyone today, re-entry gated on academic pilot feedback; (b) either add a one-question "what brings
you here?" step that stores the answer for feedback correlation *without* changing the voice — which is
honest and useful — or drop the four-perspective framing from the hero. What must not stand is
recruitment on a distinction the product does not make and the feedback form assumes it did.

### P1-1 · Imperial-Juridical (Marius) ships with no guided starters, and the affordance disappears
**Affects:** Pastor/Teacher (most likely to pick this world), General.
**Files:** `cic-poc/backend/scripts/build_guided_starters_json.py:15–36`;
`cic-poc/frontend/src/data/guidedStarters.ts:27–31`; `cic-poc/frontend/src/components/ChatInput.tsx:82`.
Five worlds are in the build script; Imperial-Juridical is not. `getGuidedStartersForTable` silently
omits it, and `ChatInput` hides the "Don't know what to ask?" button entirely when no seated world has
content — so a visitor who starts with Marius never learns the feature exists.
**Fix:** author `World-Builds/Imperial-Juridical-Christianity/*Guided_Starters_V0_1_DRAFT.md` to the
same four-tier shape and add it to `WORLDS` in the build script. Until then, keep the button visible
with an honest empty state rather than hiding it.

### P1-2 · The `why` and `citations` fields on every guided starter are shipped and never rendered
**Affects:** Pastor/Teacher, Academic.
**Files:** `cic-poc/frontend/src/components/QuestionSheet.tsx:116–151` vs. the JSON's own schema.
Every non-limit entry carries a `why` line and a citation array tracing to build documents; the sheet
renders topic + question + follow-ups only. This is the cheapest depth win available anywhere in the
product — the data is already in the bundle.
**Fix:** render `why` as a muted subline under `topic`, and `citations` behind a small disclosure on the
entry, matching the CitationModal's existing visual language.

### P1-3 · Every conversation's further-reading offer is the same three general survey books
**Affects:** Pastor/Teacher, Academic, General.
**Files:** `cic-poc/backend/app/graph/closing_sequence.py:178–211`;
`cic-poc/backend/data/further_encounter_resources/` (contains only `general.json`).
`_load_resources(world_id)` returns `None` for all six worlds; `_world_label()` falls back to "this
world".
**Fix:** six per-world JSON packs in the existing schema (`world_offer_label`, `resources[]` with
`title`/`author`/`publisher`/`year`/`locator`/`note`/`topic_tags`). Each world's Doc_02 source registry
already contains the candidates. Five to eight titles per world.

### P1-4 · The "anything else?" beat is unreachable; participants get the resources offer without
### ever being asked
**Affects:** all four.
**Files:** `cic-poc/backend/app/graph/governance.py:363–375`;
`cic-poc/backend/app/graph/closing_sequence.py:151–175, 233–234`;
`cic-poc/backend/app/prompts/facilitator_prompts.py` (`FACILITATOR_ANYTHING_ELSE_PROMPT`).
When wind-down is sensed, governance appends a `closing_stage_changed` event (which *does* project into
state on the next request via `events.py:205–206` — I re-verified this rather than reporting a
false "dead state machine"). But nothing streams the Facilitator's "anything else?" turn:
`route_closing_stage` only ever returns `resources_offer`, `resources_show`, `sensed_close`, and the
`kind == "anything_else"` branch in `stream_closing_turn` is never reached. The participant's *next*
message is therefore interpreted as an answer to a question they were never asked. The visible failure
is a resources offer arriving unprompted; the invisible one is a short-but-substantive message being
classified `DONE` and pushed toward the door.
**Fix:** when wind-down fires, stream `("anything_else", {})` in the same turn, exactly as the module's
own state-machine docstring describes.

### P1-5 · The Atlas tray accepts five Representatives; the app silently keeps three
**Affects:** Pastor/Teacher, Academic.
**Files:** `cic-website/atlas-v3.html:1569, 1588` (`TRAY_MAX = 5`) vs.
`cic-poc/frontend/src/components/WorldSelector.tsx:19, 81` (`MAX_WORLDS = 3`, `.slice(0, MAX_WORLDS)`).
Mark's 2026-08-01 decision made 3 a permanent cap; the Atlas was never updated.
**Fix:** set `TRAY_MAX = 3` in `atlas-v3.html` and say so on the tray ("up to three seats").

### P1-6 · The full-record apparatus (repository, ORQ scaffold, FAIR export) exists for one world in six
**Affects:** Academic (primary), Pastor/Teacher.
**Files:** `cic-poc/backend/data/desert_world/{repository.json,sources.json}` (the only world with
either); `cic-poc/backend/app/main.py:1884–1958`; `cic-poc/frontend/src/components/LexiconModal.tsx`.
Citations reach the participant fleet-wide, but the record *behind* a citation resolves only for
Desert. Nothing in the frontend calls `/api/repository/sources` or `/api/repository/search` at all.
**Fix:** two separable items — (a) continue the per-world record-store migration (already the S6.2
work-stream); (b) meanwhile, add one honest line to the citation panel for unmigrated worlds ("the full
record view for this world is still being built") rather than letting an academic infer the record does
not exist.

### P1-7 · The Research Table view was retired with no replacement
**Affects:** Academic (primary), Pastor/Teacher.
**Files:** `cic-website/world-atlas.html` (now a redirect stub, commit `4b0258d`); `atlas-v3.html`
contains no table or list view.
A filterable list over all 257 census entries existed and no longer does.
**Fix:** a "List view" toggle in `atlas-v3.html`'s controls row rendering the same census as a
scannable table (name · dates · region · family · status · sources-count), reusing the existing lane
and region filters. The data is already loaded client-side.

### P1-8 · A multi-world table cannot isolate a directly-addressed Representative
**Affects:** Academic, Pastor/Teacher.
**Files:** `cic-poc/backend/app/main.py:1419`; `cic-poc/backend/app/graph/nodes.py:2919–2927`;
`cic-poc/backend/wrs/parameters.yaml` (`turn_floor_multi_world`).
Direct-address detection correctly routes the first turn, then `must_continue` compels a second voice.
**Fix:** exempt a turn whose speaker was chosen by direct-address detection from `must_continue`, so
"Marius, what did Leo actually claim?" gets Marius and stops. This is a one-condition change at
`main.py:1419` and preserves the floor for undirected questions, which is what it was written for.

### P1-9 · The close produces nothing the participant can keep, and does not link the feedback form
### that was written for it
**Affects:** all four; Pastor/Teacher most.
**Files:** `cic-poc/frontend/src/components/TheTable.tsx:329–345`; `cic-website/pilot-feedback.html`
(orphan — no page in the site links it); `cic-website/tour.html` (also an orphan).
The closing screen is one sentence, a reset button, and an email address. `pilot-feedback.html` — which
asks exactly the questions this project needs, including the four-perspective question — is reachable
only by typing the URL, and its form posts to `action="mailto:…" method="post"`, which is unreliable in
modern browsers, while a working `/api/pilot/request` endpoint sits unused.
**Fix:** (a) link `pilot-feedback.html` from the closing screen and the site footer; (b) point its form
at `/api/pilot/request` (or a sibling feedback endpoint) instead of `mailto:`; (c) add a "copy this
conversation" button on the closing screen — plain text with speaker names, the sources cited, and the
further-reading list.

### P1-10 · Code cites a live-test document that does not exist
**Affects:** record integrity; Academic trust if surfaced.
**Files:** `cic-poc/backend/app/graph/nodes.py:742–745`;
`cic-poc/backend/app/prompts/facilitator_prompts.py:416, 436, 473`.
All cite `CiC_W1_Phase5_RelationalSafety_LiveAdversarialTest_CorrectedDesign_Round1/2.md` as the
authority for the highest-stakes text the system produces. That filename appears nowhere in the working
tree or in `git log --all`. The only relational-safety validation artifacts present are the Retest
(explicitly a *desk* trace, not a live test) and the undecided Decision Options doc. This is the same
class of error the adversarial-review practice exists to catch — a citation that sounds right and does
not survive being opened.
**Fix:** either restore the document if it exists outside this repo, or correct all four citations to
point at what actually validated the design, and record in the Decision Log which artifact that is.

### P1-11 · The Atlas gives a casual visitor no orientation above the fold
**Affects:** General (primary), Re-evaluating.
**Files:** `cic-website/atlas-v3.html:412–426` (controls), `446–465` (the "Reading the marks" legend, in
the footer), `496` (`built` defaults false).
257 entries render by default; the key that explains the four icons is below the entire ten-era canvas.
**Fix:** move a two-line version of "Reading the marks" into the controls row (or a dismissible strip
under it), and add a single sentence above the canvas: *"Six of these you can sit down with today —
tap 'Built worlds' to see just those. The rest is the map we're building."*

### P1-12 · The answer bank has no data, so every lookup misses
**Affects:** cost, and any persona on a curriculum path.
**Files:** `cic-poc/backend/app/answer_bank.py:83–104`; `cic-poc/backend/data/` (no `answer_bank/`
directory).
`_bank_path` resolves to `data/answer_bank/<world_id>.json`; the directory does not exist, so
`_load_bank` returns `{}` and every call logs `no_bank_entry`. The module is correct and unused.
**Fix:** either run `scripts/build_answer_bank.py` for the First Visit tier of the five worlds that have
starters (the highest-traffic, most-repeated questions), or note in the module docstring that it is
dormant pending that spend, so a future reader does not assume it is serving.

### P2-1 · "Sources to research" is researcher-facing language on a participant-facing document
`atlas-v3.html:1327`. Rename to "Sources" or "Where this comes from"; 134 of 257 entries render
"Source base pending" beneath it, which compounds the impression.

### P2-2 · `cic-website/README.md` is stale
It states support.html was *"Pulled from nav 2026-07-22, no page currently links here"*; every page's
nav currently links it.

### P2-3 · `tour.html` says "Five living traditions"
Six are live. The page is also an orphan (nothing links it) despite being the clearest existing
explanation of the designed experience — a candidate for the General persona's missing orientation.

### P2-4 · `/api/pilot/request` references a page and mailbox that no longer exist
`main.py:459, 486` — the docstring cites `cic-website/pilot.html` (absent) and the error message names
`hello@churchinconversation.org`, retired per `cic-website/README.md` in favour of
`info@churchinconversation.com`.

### P2-5 · `CENSUS_ID_FIX` in `index.html:186` is now dead
The census's `imperial-juridical-christianity` id matches `world_manifest.py`; the workaround map is
harmless but no longer describes reality.

### P2-6 · Naming drift across the fourth persona
`deconstructing` (Design Spec §4.4), `reevaluation` (code arms, Battery A), "Reevaluation"
(`whats-next.html`), "Re-examining my faith" (`pilot-feedback.html`), "re-examining their faith"
(`index.html`), "Re-evaluating" (Mark, this dispatch). The UX checklist already flagged this in July
("code still uses internal id `deconstructing` — reconcile before merge"). Pick one participant-facing
label and one internal id, and record both.

---

## 4. Now vs. over time

### Now — before the pilot link goes to anyone in the Re-evaluating category
1. **Decide the resource-naming question and ship at least Option A's floor** (P0-1). One sentence in
   two prompt templates plus a Decision Log entry. Nothing else in this report is more urgent.
2. **Write `privacy.html` and link it from the footer and the onboarding screen** (P0-2). ~200 words.
3. **Correct the `whats-next.html` Representative Modes paragraph** to match the 2026-08-02 stop
   (P0-3a). One paragraph.
4. **Fix the four citations to the missing live-test document** (P1-10) — or restore it. This is a
   record-integrity item that costs minutes and protects every claim built on top of it.

### This week — cheap changes with disproportionate persona payoff
5. **Render `why` and `citations` in the QuestionSheet** (P1-2). Data already shipped; pure UI.
6. **Link `pilot-feedback.html` from the closing screen and footer, and point its form at the real
   endpoint** (P1-9a/b). The pilot is currently collecting almost nothing.
7. **`TRAY_MAX = 3`** (P1-5). One line.
8. **Atlas orientation strip + move the legend up** (P1-11). One sentence and a CSS move.
9. **Six per-world further-reading packs** (P1-3). Half a day of authoring against source registries
   already written; transforms the close for two personas at once.
10. **Stream the "anything else?" turn on wind-down** (P1-4). A one-element list.
11. **Exempt direct-address turns from `must_continue`** (P1-8). One condition.

### Next — real build increments, in this order
12. **The takeaway artifact** (P1-9c): copy/print the conversation with speaker names, cited sources,
    and the world's further-reading list. This is the single change that makes Pastor/Teacher a real
    persona rather than an aspiration, and it also gives General and Re-evaluating a reason to return.
13. **Imperial-Juridical guided starters** (P1-1), plus an honest empty state so the affordance never
    silently vanishes.
14. **A List view on the Atlas** (P1-7), restoring what the ship flip retired.
15. **Continue the per-world record-store migration** (P1-6), with an honest interim line in the
    citation panel for unmigrated worlds.
16. **A one-question "what brings you here?" step** that records the persona for feedback correlation
    without changing the voice (P0-3b). This is also the cheapest possible way to gather the *"real
    pilot feedback, specifically from professors/academics"* that is the Representative Modes re-entry
    trigger — the pause and this step are complementary, not in tension.

### Later — deliberately deferred, not forgotten
17. Re-entry on Representative Modes, gated as Mark defined it. If it re-enters, the `reevaluation`
    lane needs the full Battery A protocol, not a spot-check: its measured failure mode was dropping
    the honest-uncertainty content that is the whole reason the lane exists.
18. Session history and resume. Real, and second-order compared to the takeaway.
19. Calibrating the Track B thresholds against real sessions (`nodes.py:511–522` says plainly they are
    starting values).

---

## 5. Bottom line

**Most ready today: General.** The path from a cold landing page to a live, well-scoped, honestly
framed conversation with a named Representative is complete, coherent, and genuinely good. The
`world_description` copy, the portrait carousel, the First Visit starter tier, and the in-line
highlight/citation mechanic all serve a curious non-specialist well. The gaps for this persona are
real but small: an onboarding wall, a legend below the fold, and an ending that produces nothing.

**Least ready today: Pastor/Teacher.** Nothing on the public site addresses them; nothing in the app
adapts to them; the one piece of tuning built for them (`_LANE_LENGTH_CEILINGS["pastor-teacher"]`) is
inert dead code; the world they are most likely to choose is the thinnest of the six and the only one
with no starter questions at all; and the product produces no artifact they can carry into the work
they came to do. They can have a good conversation, but they leave with nothing.

**Highest risk — a different question from readiness, and worth stating separately: Re-evaluating.**
This persona has the best design writing in the repository (Design Spec §4.4), the best participant-
facing content already shipping ("For the Wrestling", the `floorNote` copy, the non-coercion clauses
baked into every Representative's prompt), and the weakest safety floor: an acute-distress template
that names no path to human help, contradicting the governing document it cites, closing a finding the
project's own batteries raised twice, and citing a validation artifact that does not exist. They are
also recruited by name in the hero. Least-ready is Pastor/Teacher; most-consequential-if-wrong is this
one, and P0-1 should be treated accordingly.

**Academic/Seminary** sits between: the right *posture* (the pre-conversation honesty about unreviewed
scholarship is exactly correct), real per-turn citations fleet-wide, and a genuinely rigorous record
apparatus — for one world in six, with the FAIR export unreachable from any UI and the browsable
research surface retired in the last ship. They will trust the project's honesty and doubt its depth,
which is a recoverable position and a better one than the reverse.

**The single biggest lever: finish the ending.** Today the close is `"The conversation has ended."`
plus an email address. It is the one surface where all four personas converge, and it is the thinnest
thing in the product. Making it do real work closes more persona gaps per unit of effort than anything
else available:

- it is where the **named path to human help** belongs when a conversation has gone somewhere heavy
  (P0-1) — and the Facilitator's "door outward" is already the designed home for it;
- it is where **per-world further reading** turns a conversation into study (P1-3), which is most of
  what Pastor/Teacher and Academic are missing;
- it is where a **takeaway artifact** — transcript, sources cited, reading list — makes the visit
  produce something (P1-9c), which is the whole of what Pastor/Teacher is missing;
- it is where the **"anything else?"** beat and a graceful close give General a reason to return
  (P1-4);
- and it is where the **feedback form the project already wrote** should be reached (P1-9a), which is
  the mechanism by which the paused Representative Modes work eventually re-enters.

Everything in that list is small. The close is one React component, one Facilitator prompt already
written, six small JSON files, and one link. It is the cheapest large win in the product, and it is
currently the last thing every participant sees.

---

*Pass 04 of the 2026-08-05 full-system review. Every file citation above was opened and read at
source; where a finding depended on a claim about behavior, the code path was traced end to end (see
P1-4, where an initially-suspected dead state machine was disproved by following the event projection
in `events.py:205–206`, and the finding narrowed to what is actually broken). No claim here rests on a
status document's own word for itself.*
