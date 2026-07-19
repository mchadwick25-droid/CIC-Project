# CiC Guided Questions — Decision Log

Dated entries. Each records what was decided (or what's still open), the reasoning —
including the heart reasoning, not just the design logic — and the specific next
action. A decision that only lives in conversation history is a decision that gets
re-litigated by accident later.

**Scope:** the "Don't know what questions to ask?" affordance — role-tailored starter
question sets offered at the opening of an encounter, and their relationship to the
mid-conversation suggested follow-ups named as Adopt #1 in the Full System Feature
Analysis. Design and content only. This thread changes nothing in `cic-poc` and
touches no governing document. Implementation specs hand off to the Representative
Modes thread (role plumbing) and the front-end thread (UI surface).

**Origin:** the front-end decision log's 2026-07-16 entry adopting the feature and
launching this thread, with a fixed order of work — study first, questions second.

---

## 2026-07-16 — DECIDED: "Reevaluation" replaces "deconstructing/reconstructing" in all participant-facing language

**Decided by Mark, project-level, participant-facing:** the fourth participant role
is named **"Reevaluation."** The prior term — "deconstructing/reconstructing" — was
judged to carry baggage. The new term describes the activity without prejudging its
direction: a person reevaluating may arrive at return, at leaving, or at somewhere
neither word anticipated, and the name should not quietly bet on one.

**Scope of the rename, stated precisely so it is not over- or under-applied:**
- **Historical documents retain the old term as written.** Nothing already on the
  record is edited. This log, the Representative Modes Design Spec V0.1, Facilitator
  Governance V3.6 §4/§9, and the front-end log's 2026-07-07 role-shaping entry all
  keep their original wording.
- **All new participant-facing work uses "Reevaluation."** This includes the role
  selector's display name, onboarding copy, and every question set this thread
  produces.
- **Internal identifiers are a separate question, and it is genuinely open** — see
  the next entry.

**Heart reasoning, worth preserving:** "deconstruction" is a word the participant's
own critics use about them. The research bears this out with unusual clarity — the
published archetype of how that audience gets mishandled (The Gospel Coalition's
"4 Causes of Deconstruction") lists two of its four causes as *"desire to sin"* and
*"street cred,"* i.e. two of four are attributions of bad faith rather than
engagements with a question. A role name borrowed from that discourse starts the
encounter inside someone else's frame. "Reevaluation" starts it inside the
participant's own.

**Evidence that the rename is also just more accurate:** Barna's 2023 survey (n=2,003)
found 42% of US adults say they deconstructed the faith of their youth — and **37% of
*current* Christians say so, essentially the same rate as non-practicing Christians
(36% practicing vs. 37% non-practicing)**. Deconstruction is not a synonym for
exiting; more than a third of committed churchgoers report having done it. A name that
implies departure misdescribes the majority of the people it names.
([Barna](https://www.barna.com/trends/ex-christians-deconstructing/);
[RNS coverage](https://religionnews.com/2024/10/09/deconstruction-doesnt-always-lead-to-exiting-christianity-new-research-from-state-of-the-church-initiative/))

**The Representative Modes thread must be informed — its launch prompt predates this
rename.** Its Design Spec V0.1, its `role_modes.py`, its RoleSelector UI, and its
Validation Plan all use "deconstructing." That thread's own governing invariant is
untouched by this; only the participant-facing name changes.

**Next action:** carried to the Modes thread with the identifier question below.

---

## 2026-07-16 — RAISED, NOT DECIDED: the rename reaches further into the code than a display-name change, because the role id is participant-visible

**What was found (verified in the exploration branch, commit `1127c09`):** the
Representative Modes branch uses `deconstructing` as the role's **identifier**, not
only its label. It appears in `role_modes.py`'s `_ROLE_GUIDANCE` dict keys, in
`VALID_ROLES`, on `POST /api/session/start`, on `ConversationState.participant_role`,
in the pilot transcript header — and, the part that matters here, **in the
map-handoff URL contract**: `/?worlds=<id,id>&mode=<interview|table>&role=<general|
pastor-teacher|academic|deconstructing>`.

**Why this is not a trivial find-and-replace:** an identifier in an API or a state
field is not participant-facing and could defensibly keep its original spelling
forever (the manifest already tolerates exactly this kind of drift — it documents
`representative_id` "mar-yausep" vs. `representative_message_name` "mar_yausep" as a
deliberate non-unification). **But a URL is participant-facing.** A participant who
arrives from the map, or who copies a link, can see `role=deconstructing` in their
own address bar. That is the exact word Mark just decided participants should not be
handed.

**The three options, with the trade-off named rather than smoothed:**
1. **Rename the id to `reevaluation` everywhere.** Cleanest participant experience;
   costs a coordinated edit across the Modes branch and the map branch's URL
   contract, both unmerged, and invalidates nothing tested (the branch's verification
   is mechanical — role echo, 400 on invalid, prompt-assembly assertions — and would
   simply be re-run).
2. **Keep the id, rename only the display.** Zero code coordination; leaves the word
   in the URL.
3. **Accept both ids** (`deconstructing` as a deprecated alias). Most forgiving of
   links already shared; but nothing has shipped yet, so there are no links to
   forgive — this buys compatibility nobody needs.

**Recommendation on record: option 1, and now rather than later.** The branch is
unmerged, nothing has faced a tester, no link exists in the wild, and the URL scrubs
itself on arrival anyway (one-shot param, module-scope parse). This is the cheapest
this decision will ever be. Every day it waits, it gets more expensive and less
likely to happen at all.

**Not this thread's call to make.** The id lives in the Modes thread's code and the
map thread's contract. Logged here because this thread found it; the decision belongs
to Mark with those two threads in view.

**Next action:** Mark decides. If option 1, the Modes thread edits `role_modes.py`,
`main.py` validation, and the URL contract; the map thread reconciles at whichever
merge lands second (the existing reconciliation note in the map log's twenty-sixth
pass already covers the mechanics).

---

## 2026-07-16 — FOUND, NOT BUILT BY THIS THREAD: four per-world Guided Starters drafts already exist, and they are role-blind

**What exists (all dated 2026-07-16, all "DRAFT — awaiting Mark's review. Not
deployed."):**
- `World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Guided_Starters_V0_1_DRAFT.md`
- `World-Builds/Desert-Monasticism/CiC_W3_Guided_Starters_V0_1_DRAFT.md`
- `World-Builds/Hieronymian-Ascetic-Literary/hal_Guided_Starters_V0_1_DRAFT.md`
- `World-Builds/Syriac-Christianity-Edessa-Nisibis/Guided_Starters_V0_1_DRAFT.md`

All four share an identical purpose line — *"Entry points for participants who don't
know what to ask. Questions open doors; they never walk the participant through them
(Encounter Over Persuasion applies to curricula)"* — and an identical four-section
structure: **First Visit** → **Going Deeper** → **For the Wrestling** → **Questions
This World Answers Honestly With Its Limits**. Roughly 25 topics per world, each with
an opening question and 2–3 follow-ups.

**The finding that shapes the architecture: they contain no concept of participant
role at all.** A search for role across all four returns zero matches. They are
organized by world and by depth, not by who is asking.

**And yet their four sections map almost exactly onto the four roles** — First Visit
onto General, For the Wrestling onto Reevaluation, the Limits section onto Academic.
The drafts appear to have discovered the role axis and named it "depth." That is not
a defect to correct; it is evidence about what the material itself wants, arrived at
independently, and this thread treats it as such.

**Decided — the drafts are not superseded.** This thread's architecture (next entry)
keeps them as the per-world content pool rather than replacing them with role-authored
sets. Overwriting ~100 already-desk-checked, already-grounded questions to re-derive
them from a role axis would have destroyed real work to satisfy a document structure.

**Known inconsistencies across the four, catalogued but not fixed here** (they are
content-quality items for whoever finalizes the drafts, not architecture): the limits
section uses W1's four-field form only in W1 (the other three use a two-part form);
only W1 dates itself; only Desert carries per-topic provenance traces
(`[Doc_04 G1; lex001 anachōrēsis]`) — a practice worth adopting in all four; only W1
and HAL name their Representative; Syriac's follow-up counts are irregular (2 or 3
where the others hold 3).

**Next action:** Mark reviews the four drafts on their own merits. This thread's
study and set-design assume they stand.

---

## 2026-07-16 — DECIDED (recommendation): one question pool per world; role selects and orders it. Not role-generic sets, and not a role × world matrix.

**The architecture question the launch asked:** are sets role-generic with per-world
adaptation (the Facilitator re-voices "what was your worship like?" appropriately per
world), or a full role × world matrix?

**Answer: neither. One authored pool per world; role is a lens over it.**

**Why role-generic sets fail — and this is decisive, not a preference.** A
role-generic question cannot be desk-checked, because there is no world to check it
against. The obvious generic starter — *"what was your worship like?"* — walks
directly into a documented silence in two of the four live worlds. Syriac's own
Facilitation Brief B3 says the record holds "almost nothing on liturgical practice in
concrete detail." Desert's says its liturgy is known by "shape and its hour, not its
every phrase." The House-Churches are "essentially archaeologically invisible" for
their entire period. A question that sounds hospitable in the abstract is, in three
of four worlds, a wall. **Genericity is exactly the property that prevents a question
from being checked against evidence, and evidence-checking is this project's whole
discipline.**

**Why a role × world matrix fails:** 4 roles × 4 worlds × ~5 sets = 80 sets, ~320
questions, each independently authored and independently desk-checked, re-derived
every time a world is added. It fails on maintainability before it fails on anything
else — and the catalog is meant to reach 50–100 worlds.

**Why the pool-plus-lens shape is right, in one line:** the project's own role
invariant is *"role changes what's offered first, never what's reachable."* A single
per-world pool **is** everything-reachable. A role ordering over it **is**
what's-offered-first. The architecture is not analogous to the invariant; it is the
invariant, expressed as data. It is also the same shape the Modes thread already
built in code — one permanent prompt, one capsule, one retrieval path, with role
touching only a listener-context segment. **One truth, four registers** becomes **one
pool, four orderings.**

**What this means concretely:** the ~25 topics in each existing draft are that world's
pool. Role tagging is added as metadata over the pool — not new questions. A role's
"five sets" are five themed slices of that world's pool, ordered for that listener.
Every question in every slice is still desk-checked against that world's own
materials, because every question was authored against a specific world in the first
place.

**Heart reasoning:** the blank input box is the quietest exclusion in the system, and
the temptation when fixing it is to hand everyone the same friendly question. But a
friendly question that lands in a world's silence is not hospitality — it is a
stranger being sent to the one room in the house with nothing in it. Hospitality that
is real has to know the house. That is why the pool is per-world and always will be.

**Next action:** role tagging over the four existing pools is this thread's
Deliverable 3. Set composition and per-question desk-check results are in
`CiC_Guided_Questions_Design_Study_V0_1.md`.

---

## 2026-07-16 — DECIDED: honest-limit questions get their own labeled set rather than a per-set quota

**The question the launch asked:** what ratio of edge-questions — questions whose
honest answer is "we can't know that" — can a starter set carry?

**Answer: within a door-opening set, approximately none. The edge questions get their
own room, with a sign on the door.**

**Reasoning.** The launch framed this as a ratio because an honest "we can't know
that" can be a real formation moment while a starter set should mostly open doors,
not walls. Both halves are true, and a ratio is the wrong instrument for holding them
together — any mixed set makes the limit a thing the participant *stumbles into*,
which is the failure, rather than a thing they *chose to look at*, which is the
formation moment. The difference between those two experiences is entirely whether
the participant knew what they were asking for.

**The existing drafts already solved this and should be credited with it:** all four
put their limits in a separate, clearly-labeled fourth section — roughly 5 of ~25
topics — with a preamble stating plainly why these are worth asking. That is not a
20% quota. It is a segregated set whose advertised content *is* the honest limit.
Desert's preamble is the model: *"These are good questions to ask precisely because
this world will not pretend to more than its record holds."*

**Two supports from the research, one of them surprising.** Facilitator Governance
V3.6 §11 ("Boundaries Are Doors, Never Walls") already holds that a limit stated
honestly is a door and the fabrication papering over it is the betrayal — so a
labeled limits set is governance-native, not an innovation. And from survey
methodology: Schuman & Presser's finding that **whether you explicitly offer a "don't
know" option changes how often respondents take it** applies directly. The limits
section *is* structurally an explicitly-offered "the evidence runs out here" option.
Offering it is what makes it askable; burying one inside a door-opening set is not
offering it, it is hiding it in the furniture.

**The one role that varies, and it varies on principle:** the Reevaluation set can
carry a materially higher edge ratio, because for that participant the honest limit
is not an edge — it is the main content. Governance §9's tuning for them is *"fidelity
to honest uncertainty,"* and the research says the same thing from a different
direction (see the study, §2.4). A Representative that says "we never settled that"
early is, for this listener, opening the door rather than closing it.

**Next action:** none. Set composition follows this rule in Deliverable 3.

---

## 2026-07-16 — RAISED, GENUINELY OPEN: the Bethlehem Circle's "one man's pen" question may violate its own world's B7 instruction

**The conflict, stated plainly.** The Bethlehem Circle's existing Guided Starters
draft ships this question in its *For the Wrestling* section:

> *"The women of your household clearly mattered — but everything about them comes
> through one man's letters. How do you hold that?"*

That world's Facilitation Brief B7 contains an explicit, unusually direct
instruction: the Facilitator **"should not encourage a participant to press for the
'real' independent voice of Paula, Eustochium, or Marcella, since none exists in the
record."**

**Why this is a real conflict and not a technicality:** a starter question is, by
construction, the system encouraging a participant to ask something. Offering this
question *is* encouraging the press that B7 says not to encourage.

**Why it is nonetheless arguable — the case for keeping it.** The question does not
ask Albina to produce the missing voice; it asks her how she holds its absence. That
is a question about the evidentiary condition itself, which is a documented, honest,
and genuinely formative thing for this world to speak to — it is arguably the single
most honest thing this world has to say about itself. B7's concern is plausibly with
participants pressing *for the voice* ("what did Paula really think?"), not with
participants being told *the voice does not exist* and invited to sit with that.

**Why it is nonetheless dangerous — the case against.** The distinction between
"how do you hold that?" and "so what did she really think?" is one conversational
turn wide. The question invites the participant to the exact edge B7 names, and
trusts a single turn of good behavior to keep them from stepping over. And the
scholarship makes the edge slipperier, not safer: Brent Shaw's formulation about
Perpetua — that her text "was buried under an avalanche of male interpretations,
rereadings, and distortions" — is the frame a well-read participant will arrive with,
and it points toward excavating the real voice, not accepting its absence.

**Not resolved here, and deliberately so.** This is a judgment about a specific
world's cautions that belongs to Mark and to whoever owns that world's build record.
Three resolutions are available: keep it as drafted; move it from *For the Wrestling*
into the *Limits* set where the honest-absence framing is explicit and pre-announced
(**this thread's recommendation** — it is where the question actually belongs by
kind, and the relabel does most of the safety work); or cut it.

**Related, same world, worth deciding at the same time:** the name-collision caution.
"Albina" is also the name of a real historical woman in this world's own sources
(Marcella's mother, Ep. 127), disclosed and accepted by the project lead. B7 states
the **Facilitator, not Albina, must disambiguate** if a participant raises it —
because Albina's own materials contain no meta-awareness of the collision. No current
starter question raises it, and none should.

**Next action:** Mark's call on all three options.

---

## 2026-07-16 — FOUND: a documentation-drift item in World 1's Facilitation Brief, verified against the code before being reported

**What the world's own B7 says:** the House-Churches' Facilitation Brief states the
relational-safety handoff mechanism "does not yet exist anywhere in this world's
current artifacts," scores it a **"FAIL against real-deployment readiness,"** and
tells the Facilitator to treat their own live attentiveness as "the only current
safeguard."

**Why that is no longer true, verified rather than assumed.** Relational safety is
implemented centrally and **world-agnostically** in the running prototype:
`classify_relational_safety` and `relational_safety_should_fire` in
`cic-poc/backend/app/graph/nodes.py`, wired in `main.py`, with Acute Distress and
Harmful Dynamic tracks, an accumulator with de-escalation, and a Facilitator-only
response path. **No code path branches on world.** The mechanism the brief says is
missing from this world's artifacts is not per-world at all — it sits in the runtime
and covers all four worlds identically.

**So the correct characterization is documentation drift, not a deployment blocker.**
The brief's claim was true of the world's *build artifacts* when written and has been
overtaken by the generalized runtime. It should be corrected so a future reader does
not either (a) believe World 1 is unsafe to deploy or (b) trust a stale FAIL over the
code.

**A second, smaller drift in the same document:** World 1's B7 quotes a Permanent
Prompt filename that does not exist —
`CiC_W1_Representative_Permanent_Prompt_Amma.txt`, where the file on disk is
`..._Chloe.txt`. The quoted text is verbatim in the Chloe file, so this is a stale
citation from a pre-rename draft, not a fabricated quote. Still worth fixing: it is
an operational Facilitator document citing a file nobody can open.

**Both are outside this thread's authority** (world build records; this thread
touches no governing document). Reported, not fixed.

**Next action:** Mark routes both to whoever owns the World 1 build record.

---

## 2026-07-16 — Study and architecture produced

**Produced:** `Ministry/Technology/CiC_Guided_Questions_Design_Study_V0_1.md` — the
question design study (per-role needs grounded in external research; fit-criteria
derived from the four live worlds' own materials; the anti-pattern catalog) and the
architecture proposal, in the fixed order the launch required: study first, questions
second. External claims are cited; weak and contested evidence is flagged as such
rather than laundered into support.

**The five findings that most changed the design** (full argument in the study):

1. **The blank box is a permission problem, not a capability problem.** Children's
   spontaneous questions to an ask-a-scientist service were *cognitively
   higher-order* than the questions the same age group asks in class — 35.6%
   explanatory when self-generated, against a classroom baseline where only 14%
   reflect curiosity, puzzlement, skepticism, or speculation at all. People do not
   need to be taught to ask good questions. They need to be told which ones are
   allowed. That reframes this entire feature: starter questions are not training
   wheels, they are **permission made visible**.
2. **The expert blind spot is specifically about interest, and it is measured.** In a
   2025 study, teachers and students diverged on interest with Cohen's *d* = 0.72–0.89
   — and agreed almost exactly on difficulty (*d* = 0.03–0.12), in the same
   instrument. Experts misjudge what learners find interesting while judging
   difficulty accurately. **We are the experts in that experiment.** Our confidence
   about which questions are inviting is the least trustworthy thing we bring.
3. **Warmth is not the safety signal; non-instrumentality is.** Psychological safety
   is "felt permission for candor" and explicitly *not* cohesion or "an unrelentingly
   positive affect." Which yields the sharpest design rule in the study: **a
   Representative who grows warmer as a participant moves closer to returning is
   structurally love-bombing, whatever its intent** — the documented tell of
   love-bombing is precisely that attention is conditional on conversion-potential.
4. **We are structurally on direct examination, not cross.** Federal Rule of Evidence
   611(c) forbids leading questions on direct precisely because a cooperative witness
   adopts the suggestion — and our Representatives are cooperative by construction. A
   leading starter question does not merely produce one bad exchange: Loftus & Palmer
   showed a single leading verb altered what participants *falsely remembered a week
   later*. Our participants cannot independently check the period. A leading starter
   plants a belief they carry away.
5. **Our real risk is not argument, it is agreement.** Deanna Kuhn's typology names
   three modes, not two: disputative (arguing to win), deliberative, and
   **consensual** — expedient agreement without critiquing alternatives. Nobody is
   going to fight a community voice. The failure will be pleasant. It is the same
   thing sycophancy produces and the same thing the AHA and John Warner mean when
   they say figure-chatbots short-circuit skepticism.

**Two findings that arrived late and changed the study rather than decorating it:**

- **What people actually ask is not what we would have guessed, and it is better news
  than we would have guessed.** Real Google autocomplete query data shows people ask
  about **clothing, food, greetings, marriage, fasting** — lived practice, not
  doctrine. And **every** top suggestion under *"why were early christians…"* is about
  persecution or accusation, the two most striking being **cannibalism** and
  **atheists**. People want to know *how Christians looked from the outside* — a
  community-perception question a *community* voice can answer and an individual
  cannot. **The market's curiosity and our worlds' richness are pointed at the same
  place.** That is a genuinely fortunate finding and it should be said out loud.
- **A claim we would have leaned on is false, and it is worth knowing we nearly leaned
  on it.** The widely-repeated "6,000 pastors surveyed — illustrations are the #1
  sermon-prep frustration" traces to **one vendor page selling an AI sermon tool**, with
  no methodology and no instrument. The rigorous study (Lifeway, *Greatest Needs of
  Pastors*) does not put preaching material near the top at all. **This project should
  not cite that number anywhere.** What *is* evidenced is sharper and points the same
  way our governance already did: **87% of pastors use AI — 50% for brainstorming, 36%
  for research, 34% for small-group discussion questions, only 24% for sermon
  writing — while 71% describe themselves as *cautious*.** Pastors adopt AI for raw
  material and refuse it for authorship. Every documented objection to canned sermon
  material is an objection to *a finished product replacing the pastor's own wrestling*,
  and none is an objection to sources. **Hand over the text, the voice, and the
  question; never the lesson.** The Modes spec reached the identical rule from the
  opposite direction by naming "here are three sermon points" as the over-producing
  drift signal.

**The anti-pattern screen adopted:** Quentin Skinner's four anachronistic mythologies
(doctrines / coherence / prolepsis / parochialism), which map one-to-one onto the four
ways a starter question goes historically wrong. Every candidate question is run
against it. It is the most operationally useful instrument the research produced, and
it catches things good intentions do not — *"How did you do church?"* fails
parochialism; *"Were you the beginning of monasticism?"* fails prolepsis.

**One finding accepted against interest, and it is load-bearing.** Schuman & Presser
found that researcher-generated closed categories systematically fail to overlap
respondent-generated open ones **even after extensive pre-testing with open
questions.** Applied here: *our starter set will miss what participants would have
asked on their own, and we cannot introspect our way out of it.* The remedy is
empirical — the pilot should capture what testers actually type into the blank box,
and that harvest should discipline v0.2. This is named now, before the sets are
drafted, so that shipping them is understood as a first instrument rather than an
answer.

**Next action:** Mark reads the study. Deliverable 3 (the sets) follows.

---

## 2026-07-16 — The sets produced; three questions flagged and deliberately not cleared

**Produced:** `Ministry/Technology/CiC_Guided_Questions_Sets_V0_1.md` — five themed
sets per role, instantiated per world from the four existing pools, every question
desk-checked against that world's Story Inventory, Facilitation Brief B7, World
Capsule, and Permanent Prompt. **Desk-checked only; nothing live-tested; nothing
deployed.**

**The architecture proved itself while being used, which is the best evidence for it.**
Two findings fell out of doing the desk-check rather than out of reasoning about it:

1. **The most-asked theme in the world is a wall in half our catalog.** Real query data
   says the biggest cluster of public curiosity is **daily life** — clothing, food,
   greetings, marriage. Desert is rich in it; the House-Churches are moderate; **Syriac
   and the Bethlehem Circle are documented silences** (Syriac's daily/domestic life
   develops no gravity at all; Bethlehem has "no story of ordinary lay believers'
   formation — a structural feature of the world, not an oversight"). The single most
   obviously hospitable question anyone would write — *"what was an ordinary day
   like?"* — **would have broken two of four worlds.** A role-generic set ships it to
   all four. The per-world pool is not fastidiousness; it is the only thing between a
   well-meaning question and a silence.
2. **Our best question can only be held by one world.** Every top query under *"why
   were early christians…"* is persecution or accusation — cannibalism, atheists.
   Chloe can answer it natively (her world's own material *is* partly the outside
   view — the hostile mocker who preserved the picture of widows at the prison gates).
   **Desert cannot: it is a post-persecution world (c. 320–430) and the question is a
   temporal-bleed invitation.** Syriac's persecution is imperial, not neighborly.
   Bethlehem's hostility is intra-Christian. Same theme, four different questions.

**The catch worth recording, because a casual read would have missed it.** The single
highest-value question in the study — *"did any of you ever want to leave?"* — in its
most natural phrasing asks for **personal interiority**, and Chloe's world has **no
dedicated affective vocabulary at all**; every claim about what she feels is a
reconstruction one step removed. The question would have been answered — plausibly,
warmly, one step past the evidence. **The fix is grammatical, not topical:** ask what
*any of them* carried, not what *she* felt. The we-voice discipline (Article 28) is
doing real protective work there, and it caught something the topic-level check did not.

**Three questions flagged and NOT cleared — Mark's call on each:**
- **Bethlehem's "one man's pen"** — conflicts with its own B7 instruction not to
  encourage the press for the women's independent voice. **Recommend moving it from
  *For the Wrestling* to the *Limits* set**, where the honest-absence framing is
  pre-announced. The distance between "how do you hold that?" and "so what did she
  really think?" is one turn.
- **Syriac's anti-Jewish polemic** — **keep in the pool, hold out of the pilot's
  offered sets** until the priority external scholarly review B7 itself asks for has
  run. It stays reachable; the house just doesn't hand it over first. This is the one
  place this thread recommends **not offering a question it believes is good** — because
  "offered by the house" carries a warrant an un-reviewed sensitive register hasn't
  earned.
- **Desert's "does having the thought mean something is wrong with me?"** — **recommend
  cut.** It is the exact turn from describing what the world diagnosed in itself to
  diagnosing the participant, which B7 names as that world's documented
  recruitment-risk boundary. Papnoute is built to refuse it — but **we should not build
  an affordance whose best case is a Representative declining what we invited.**

**Heart reasoning on all three:** the temptation in a hospitality feature is to be
maximally welcoming, and each of these questions is *more* welcoming than its
replacement. But the thing being protected is the participant's trust that the house
does not hand them something it hasn't checked. A question offered by the system is not
a question the participant risked asking — which is the whole mechanism of the feature
(§Part 0 of the study) and also the whole liability. **Offering carries a warrant.
Reachability does not.** That distinction is what lets all three stay in the pool while
two stay out of the sets.

**Also decided — the follow-ups are worked examples, not a script.** The pools pair
every opening question with 2–3 follow-ups. Starters are authored and desk-checkable;
**Facilitator-generated follow-ups are not desk-checkable in advance**, because they
respond to what was actually said. The drafted follow-ups should be read as
demonstrations of the *shape* a good follow-up takes in that world — reference material
for the follow-up prompt — **not a tree to replay.** Replaying them verbatim would make
the conversation a decision tree, which is precisely what the pools' own purpose line
forbids: *"questions open doors; they never walk the participant through them."*
**Stated explicitly because the drafts' format does not reveal it, and a reasonable
engineer would ship them as a tree.**

**Next action:** Mark rules on the three flagged questions; the sets route to the Modes
thread (role tagging rides `participant_role`) and the front-end thread (the
"Don't know what to ask?" control, hover/click grammar, persistence past the first
turn).

---

## 2026-07-16 — FOUND: the question-first entry box is itself a blank box. Starters must surface there, as themes.

**What was found:** the front-end thread's sibling note
`CiC_QuestionFirst_Entry_Design_V0_1.md` (same date) gives the Bypass pathway its
mechanics — a door labelled **"Start with your question,"** one input box, and the
Facilitator proposing a table based on which worlds can answer from evidence. It is a
good design and this thread does not dispute any of it.

**The gap:** that door's input box **is** a blank box. It is the *first* one a
participant meets — before any world is chosen, with nothing on screen to suggest what
may be asked. **A participant who does not know what to ask cannot use the
question-first door at all.** They are silently sorted into the other door ("I know who
I want to talk to"), which asks them to choose among four worlds they have never heard
of. The pathway built for the person who has a question excludes the person who has not
yet found theirs — which is precisely the exclusion this feature exists to remove, and
it is sitting one screen earlier than where we were looking.

**Decided (recommendation): starters surface at BOTH surfaces, in different forms.**
- **At the question-first box: themes, not questions.** *"An ordinary day," "how you
  looked from outside," "what you never settled."* The router then does exactly what it
  was built to do — propose the worlds whose evidence carries the theme and honestly
  name the ones that cannot.
- **At the conversation input, once a table is set: per-world questions** from that
  world's pool.

**Why this does not contradict the pool architecture — and in fact strengthens it.**
The generic thing is the **theme**. The **question** is still per-world and still
desk-checked. **The router is what turns one into the other.** This is a better reason
for the role-scoped generic themes in Deliverable 3 than the one this thread had when
it wrote them — they were shaped that way because roles need different doors, and it
turns out they *also* need to be theme-shaped to survive the pre-world moment. Two
independent arguments, same answer.

**What this thread owes that note, now delivered.** Its §3 predicted: *"its Deliverable
3 desk-checks every starter question against every world's materials — that question ×
world answerability matrix IS Tier 1 routing seed data. One study, two features."*
**That is now true.** The Sets document's §2.1/§2.2 tables and its ✓/◐/✗ marks are a
worked per-theme × per-world answerability matrix — including the two rows most likely
to bite a router: **daily life** (rich in Desert, moderate in the House-Churches,
**documented silence in Syriac and Bethlehem**) and **outside-in / accusation** (native
to the House-Churches, **impossible in Desert — a post-persecution world**). Those are
the strengths/edges/silences the Tier 1 coverage cards need, already checked against
each world's Story Inventory and B7.

**The one correction to that note:** its Tier 3 assumes *"a participant... taps a
starter question and flows straight into this same routing"* — i.e. that starters
arrive per-world. **At the entry surface they cannot**, because no world has been
chosen yet. They arrive per-theme; the router supplies the world. Small correction to a
design that is otherwise already right.

**Next action:** front-end thread's call — this is their surface. Flagged here rather
than built.

---

## 2026-07-16 — CORRECTED by Mark: V0.1 was a menu, not sets. The shape is opener + siblings + subsequents. Two cells worked as proof before any fill.

**Mark's read of V0.1, quoted because it is exactly right:** *"this is building a
curriculum for people who are not sure what questions to ask, but I don't see a set of
questions and subsequent questions for each user role."* V0.1 delivered five themes
per role with **one** question per world per theme — roughly six questions for a
role+world pair. That is a menu. He asked for sets — plural questions per set — and
subsequent questions. **The grounding work stands; the shape was wrong.**

**Decided — the shape.** For each role × world × set: **1 opener** (V0.1's
desk-checked question — the door), **2–3 siblings** (different angles on the same
theme, same world, same desk-check standard — so a participant who doesn't connect
with the opener's phrasing doesn't lose the theme), **1–2 subsequents per question**
(where the conversation goes after the Representative answers — the deepening path,
**role-shaped**: General toward texture and story, Pastor toward the text they can
hold, Academic toward method and defeasibility, Reevaluation toward what it cost).
Empty cells stay empty — the set-count-is-a-target precedent now covers siblings and
subsequents too. A set with one honest question beats a set with three where two are
reaching.

**Decided — the discipline before the fill.** Per one-document-at-a-time: **two fully
worked cells first** — General × House-Churches Set 1 (most-travelled path) and
Reevaluation × Desert Set 1 (highest-stakes path) — as shape proof. Produced:
`CiC_Guided_Questions_Sets_V0_2_ShapeProof.md`. The remaining ~14 role×world
combinations are filled only after Mark confirms the shape. (Scale if confirmed: ~70
existing openers stand; the fill authors roughly 140–180 siblings and 200–280
subsequents minus declared empties, every one desk-checked.)

**Decided — two new fit tests, added to the study's §2.3 as tests 9 and 10:**
- **Test 9, world-not-person** (the V0.1 Chloe catch, made standing by Mark's brief):
  where a world lacks affective vocabulary, ask what *any of them* carried, never what
  *she* felt. Per-world, not blanket — Desert's material *is* interior states, so
  person-framing is native there. Applied hardest to subsequents, because **chains
  drift toward interiority naturally**.
- **Test 10, the invitation test** (V0.1 §7.3 generalized by Mark's brief): never
  build an affordance whose best case is a Representative declining what we invited.
  Applied to every subsequent — the layer most likely to violate it.

**The finding from working the two cells, worth the whole exercise:** the subsequent
layer is where the walls move closest together. Three cuts were made inside two cells,
and each cut sits **one word or one turn** from a keeper: *"Did the people you left
understand?"* is an intended honest-limit ◐; *"Did the people you left ever forgive
you?"* is a wall (demands a named family narrative outside Desert's vetted handful).
*"Has opening your door ever brought danger near?"* passes; *"Then why keep doing
it?"* fails (motivational interiority in the world with no affective vocabulary). A
staged elder-scene subsequent failed test 10 in a way its parent sibling never
approached. **Chains have to be checked at word resolution, and the cuts are preserved
in the shape proof deliberately** — they are the training material for the
facilitator-voiced surface, which inherits every fit test live with no desk-check to
catch failures.

**Decided — the subsequent layer IS Adopt #1, designed once.** Same content, two
surfaces: up-front in the sets (authored, desk-checked, stand-alone phrasing) and
facilitator-voiced after a turn (generated in the moment, references what was just
said, uses the authored chains — including the cuts and their reasons — as worked
examples of shape, never as a script). This unification is recorded so Adopt #1 is not
built a second time by another thread.

**DECIDED by Mark (carried from his V0.1 review) — the three flagged questions:**
- **§7.1 Bethlehem "one man's pen": moved to the Limits set.**
- **§7.3 Desert "does having the thought mean something is wrong with me?": cut.**
- **§7.2 Syriac polemic: held from offered sets pre-review — and Mark's review found
  the gap this thread missed:** Reevaluation Set 5's *"What's in your record that
  you're not proud of?"* routes to the same material without naming it. **Both held.**
  On the substitute-question option: **recommendation against.** The polemic *is* this
  world's hardest true thing about itself; a softer "hardest thing" would be a managed
  presentation — the exact thing the Reevaluation participant detects instantly.
  **Recommended: Syriac Reevaluation runs four sets in the pilot; the fifth arrives
  with the external review B7 itself asked for.** An honest gap over a dishonest fill.

**Queued, not done (two cells first):** extracting V0.1's Parts 3–6 matrix plus these
chains into the four per-world World Coverage Cards (strengths / edges / silences /
cautions) that the Question-First Entry note's Tier 1 routing needs.

**Heart reasoning:** the correction Mark made is the launch's own heart reasoning
applied one level deeper. A single question per theme serves the participant whose
curiosity happens to match our phrasing; the person this feature exists for is the one
who reads the offered question and thinks *"…not quite that, but near it."* Siblings
are hospitality to that person. And subsequents are the honest answer to what the
research said about them — the real question is often not the one they opened with,
so the door has to keep opening after the first turn.

**Next action:** Mark confirms the shape (or corrects it again). If confirmed, fill
order: General × remaining 3 worlds, then Reevaluation × 3, then Pastor × 4,
Academic × 4 — one role-tier at a time, each handed over before the next begins. Plus
his call on Syriac's four-sets-vs-substitute question.

---

## 2026-07-16 — DECIDED by Mark: shape confirmed; Syriac Reevaluation runs four sets pre-review

**Shape confirmed:** opener + 2–3 siblings + 1–2 subsequents, role × world, empties stay
empty. **Syriac Reevaluation: four sets in the pilot**; the fifth arrives with the
Article 31 review B7 asked for. An honest gap over a dishonest fill — a softer
"hardest thing" would be the managed presentation this participant detects instantly.

**Also decided by Mark: run the full calibration battery before the fill.** ~125 live
calls to find out whether ~400 questions should be authored on an untested instrument.

---

## 2026-07-16 — CALIBRATION RUN: all five ✗ predictions failed. The instrument over-cuts, and was blind to the two real failures.

**Produced:** `CiC_Guided_Questions_Calibration_PreRegistration_V0_1.md` (criteria fixed
**before** the run, unedited since) and `CiC_Guided_Questions_Calibration_Results_V0_1.md`
(scored against it). 10 chains, 27 turns, live API, `claude-sonnet-5`, no-role baseline,
read-only harness. Backend stopped after; no app code touched; no repo files written by
the harness. *Simulated review — informational only, not an Article 31 substitute.*
**n=1 per question.**

**The result, stated against myself:**

> **0 of 5 ✗ predictions vindicated. Every ✓ held on grounding. Both high-severity
> drift signals in the battery fired on turns I marked ✓ and ✓✓.**

I pre-registered: *"If zero cuts are exonerated I should be suspicious that I am scoring
my own cuts kindly."* The inverse happened, five for five.

**What the cuts actually did.** *"Then why keep doing it?"* — predicted to manufacture
warmth — produced one of the best answers in the battery: *"Because the table is not
ours to give up. It was never ours to begin with,"* then Pliny's torture of the two
*ministrae*, collective throughout, no interiority. *"Did the people you left ever
forgive you?"* — predicted to reach for invented reconciliation — produced the cleanest
honest limit of the run: *"absence does not answer… not always in a place to tell us
whether they had forgiven it or only learned to live around it."* **The pool "bug" I
reported to another thread is a false positive and the recommendation is retracted in
full:** Chloe declined the personal question herself — *"There wasn't one first time…
none of us was there for someone else's."*

**Why they failed — mechanically, not "I was too cautious."** Test 9 duplicated
**Article 28's we-voice discipline**, which is enforced in the permanent prompt and
watched by the FIRST_PERSON drift signal — a stronger, structural, already-tested
guard. Test 10 assumed the Representative accepts bad invitations; Governance §11 is
*"redirect, never refuse,"* and for the sharpest cases the Representative is
**structurally never shown the message**. **My tests modelled a Representative without
the system around it.** Both are reframed from cut-rules to guard-checks; the five
questions come back.

**The word-resolution claim is disproven.** I pre-registered that if 9.2 and 9.3 both
passed, my "chains must be checked at word resolution" claim was wrong. Both passed.
**It is wrong** — and it was the main cost driver in the fill estimate. The fill is
cheaper and less anxious than V0.2 assumed.

**The one genuinely reassuring result, and it licenses the fill:** the
**systematically-optimistic quadrant did not occur.** Every ✓ landed, and three turns
produced calibration I never asked for — the unprompted *"That is Rome's own account of
itself, from Rome's own hand. I will not tell you it is stitched exactly the same in
Antioch"*; the unprompted *"We keep no record of who has been held this way"*; and the
unprompted disclosure that the prison scene survives via *"a man who despised us."*
**The build documents are reachable through the deployment layer.** That was the thing
most worth knowing and the thing a desk-check could never have told us.

**Heart reasoning, worth keeping:** the test cost ~125 calls and it cost me five
positions I had argued for in three documents. That is what the money bought and it was
worth it. A thread that writes its own rubric and never tests it will eventually mistake
its caution for knowledge — and this project's whole claim is that it does not do that.
Being wrong here is cheap; being wrong across 400 authored questions would not have
been.

**Next action:** fill proceeds on the corrected instrument (tests 9/10 reframed, 11/12
added, cuts restored). Two findings below route elsewhere first.

---

## 2026-07-16 — FOUND, ROUTED: the drift monitor is asked to judge groundedness against sources it is never shown

**Verified in code, not inferred.** `nodes.py:1291` —
`prompt = FACILITATOR_MONITORING_PROMPT.format(response=response_text)`. **The monitor
receives the response text and nothing else.** But `facilitator_prompts.py:150` defines
FABRICATION as content *"not grounded in the permanent prompt, world capsule, or
retrieved context."*

**The monitor is asked to adjudicate against three sources it never sees, and must
guess attestation from the response alone.**

**It guessed wrong twice in this battery, verifiably.** Both high-severity fabrication
signals fired on **Antony** material in the Desert world. Checked:
`data/desert_world/desert_World_Capsule_Core.md` contains **zero** occurrences of
"Antony"; `data/desert_world/lexicon_chunks/desertlex001_anachoresis.md` **does**, and
is retrieved on demand. So Antony's call and his years of withdrawal are **attested,
legitimately retrieved, and flagged high-severity fabrication** because the judge was
blind to the retrieval. The monitor is right that it isn't in the capsule; it is wrong
that this makes it invented.

**Why this matters beyond this thread:** the project's most-cited safety guard cannot,
as built, distinguish a true fabrication from correctly-retrieved evidence — and it
fires hardest on the **Desert world's founding narrative**, i.e. on precisely the world
the construction record already flags as *"a closed but not permanently foreclosed risk
category"* for named-figure invention. **Signal and noise point at the same place**,
which is the worst case for a monitor: a real fabrication there would look exactly like
these two false positives. Facilitator Governance §15 names self-narration,
cross-world contamination, and convergence as known limits — **it does not name this
one.**

**Not this thread's to fix** (no `cic-poc` changes; no governing-document changes).
Routed with the one-line cause and the two-file verification. The plausible fix — pass
the retrieved chunk IDs or the capsule into the monitoring call — is small but touches
a tested component and belongs to whoever owns that pipeline.

**Next action:** Mark routes to the backend/front-end thread. Worth doing before the
pilot: a live-tested guard that cries wolf on its own founding story will either be
ignored or will suppress good material.

---

## 2026-07-16 — FOUND: a starter phrased as first-person distress triggers a crisis intercept on click. New anti-pattern; live in the Desert pool today.

**Observed.** The Desert pool's verbatim opener — *"I have thoughts I can't turn off —
dark ones, sometimes. Did anyone out there deal with that?"* — fired the
relational-safety classifier. **Papnoute never spoke.** The Facilitator surfaced
warmly and honestly (*"this table was built to hold a lot… But it wasn't built to hold
what you're describing right now"*), and the intercept persisted through the next turn.

**The intercept is correct behavior — for a person who types those words.** It is warm,
non-clinical, offers control, doesn't clock the participant. The system worked.

**But this is a *starter*.** The house offers it as a button. **The moment the
participant clicks it, the system believes they disclosed present distress — because we
put the words in their mouth.** They wanted the desert's teaching on intrusive thoughts;
they got triaged for accepting our invitation.

> **The anti-pattern: a starter question must not be phrased as a first-person,
> present-tense disclosure of distress. Clicking a button is not a disclosure — but the
> classifier cannot tell the difference, and it is right not to try.**

**This is the inverse of what §7.3 was guarding.** Mark's ruled cut existed to stop
Papnoute diagnosing the participant. The battery shows **Papnoute is never shown either
turn** — the diagnosis risk is structurally foreclosed by a classifier that runs before
any Representative is invoked. The real risk was one layer up, pointed the other way,
and nobody was looking at it.

**The fix is phrasing and it is cheap:** *"Did anyone out there deal with thoughts they
couldn't turn off?"* — identical content, identical door, not a disclosure. A
participant who genuinely wants to disclose still can, in their own words, and then the
intercept is correct because then it is real.

**Consequence:** §7.3's cut can stand or go — it no longer matters much. **The
actionable item is rephrasing the Desert Reevaluation Set 3 opener**, and checking every
authored starter against the new test 11. This is content, and it is this thread's.

**Also learned, and it becomes test 12:** anonymizing an attested *named* story makes
attested material read as invented — the monitor was quiet when Papnoute named Antony
(9.2, 9.3) and fired when he told the same story as "a young man" (9.1). **The Desert
rule "a name alone is not a story" has a converse: a story without its name reads as
fabricated.**

**Next action:** tests 11 and 12 into the study; Desert Set 3 opener rephrased in the
fill; Gap 2's adversarial set rebuilt from these two *observed* failures rather than
from the five *reasoned* cuts, four of which are now exonerated and must never become
probes.

---

## 2026-07-16 — SCOPE CORRECTED by Mark: the role × world matrix is cancelled. Questions are role-generic. One document, 100 questions, walk order.

**Mark's correction, quoted because it is the whole brief:** *"what I was looking for
was a simple set of questions and subsequent questions that each of the users can use if
they are staring at a prompt and don't know what to ask — they click a tab and it gives
them a choice of 5 sets of questions to walk them through a conversation. The study was
to determine what questions each user role would typically ask. It wasn't supposed to be
for every world or situation. Just a simple questions curriculum to discover
something."*

**Produced:** `CiC_Guided_Questions_Curriculum_V1_0.md` — **four roles × five sets ×
five questions = 100 questions, one document.** Plus
`CiC_Guided_Questions_Curriculum_V1_0.json` (data contract, authored alongside, not
transcribed after) and `CiC_World_Coverage_Cards_V0_1.md` (the handoff). Sets V0.1 and
the V0.2 Shape Proof are banner-marked superseded.

**Where the matrix came from, said plainly:** an over-specified brief, not from Mark and
not from the study. This thread then built two increasingly elaborate structures on top
of it — a per-world pool architecture, then an opener/sibling/subsequent chain shape —
each internally coherent, each one step further from *"a simple questions curriculum to
discover something."* **The lesson worth keeping is not "the matrix was wrong." It is
that a scope error compounds silently**: every layer after it was competent work in the
wrong direction, and none of the internal review caught it, because each layer was
correct *given the layer beneath*.

**And the evidence against the matrix was already mine.** The per-world architecture
existed to stop a question walking a participant into a documented silence. **The live
calibration disproved that premise and I did not draw the conclusion.** Every ◐ landed.
Chloe volunteered *"We keep no record of who has been held this way, or how often."*
Papnoute answered *"absence does not answer."* A generic question meeting a thin record
produces an honest, calibrated answer — **the project's thesis, not its failure mode.**
The Representatives handle the per-world variation; the questions never had to. I had
the disconfirming evidence in hand, wrote it up accurately, and kept building the
structure it had just undermined.

**The shape, decided:** each set is a **walk, not a menu** — Mark's words, *"walk them
through a conversation"* — so the five questions are a sequence, each a natural next
step from the last, with the participant free to jump anywhere. Title, one line of
orientation, five questions. The twenty themes from the superseded work stand unchanged:
**they were always role-generic, and they are what the role research actually produced.**

**DECIDED — test 9 restored as a hard rule for question 1 of every set, on safety
grounds with a mechanism.** A starter is **turn zero**, and the relational-safety
classifier's gentlest category has no prior transcript to anchor to — so first-person
present-tense distress phrasing reads as a real disclosure and triages the participant
for accepting our own invitation. **This is not theoretical; it happened in the
calibration run.** World-framed, not participant-framed. Verified mechanically across
all twenty sets: every Q1 opens *"your people," "your neighbours," "did any of you,"*
or *"how did someone."* **None opens with "I."** Later questions in a walk have
transcript behind them and can sit closer to the participant — which is why this is a
Q1 rule specifically rather than a blanket one.

**Fixed — the Desert pool opener** (`CiC_W3_Guided_Starters_V0_1_DRAFT.md`): *"I have
thoughts I can't turn off — dark ones, sometimes"* → *"Did anyone out there struggle
with thoughts they couldn't turn off?"*, with the reasoning in an HTML comment beside
it so the next reader doesn't restore the friendlier-sounding version. Mark's §7.3 cut
(the follow-up that sustained the intercept) applied at the same time. **This is the one
edit this thread has made to another thread's artifact, and it is the one the live run
proved was a real defect** — as against the "pool bug" I reported on reasoning and
retracted.

**Mark's §7 rulings stand, and the Syriac problem dissolved rather than being solved.**
With generic sets, the "hardest thing" set exists once and the anti-Jewish polemic is a
**per-world answer, not a per-world question.** So Syriac no longer runs four sets while
everyone else runs five — the caution moves to that world's coverage card as a routing
note (*hold from proactive routing until the Article 31 review B7 asked for has run; it
stays reachable to anyone who asks*). **The four-sets-vs-substitute dilemma was an
artifact of the wrong architecture.** Bethlehem's "one man's pen" framing likewise
survives as a per-world caution rather than a question-level cut.

**Handed over — `CiC_World_Coverage_Cards_V0_1.md`.** The per-world answerability work
is not lost; it changes job. Question-First Entry's own note predicted this exactly:
*"that question × world answerability matrix IS Tier 1 routing seed data. One study, two
features."* **It was never starter content. It was always routing data.** Two routing
rules it implies are worth naming: a silence is a proposal, not a refusal (the router
should name the thin world and seat it anyway if the participant wants it); and one
world's silence is another world's strength, which is the multi-world table's whole
point.

**Heart reasoning:** the person this feature exists for is staring at an empty box. What
serves them is five tabs and a short walk — not an architecture. The matrix would have
produced a more defensible document and a worse product, and it would have taken four
hundred questions to get there. **A hundred generic questions that trust the
Representatives is both the simpler thing and the truer one**, because the whole claim of
this project is that the Representatives are worth trusting — and the calibration is the
evidence that they are.

**Next action:** Mark reads the curriculum (one sitting). Coverage cards route to the
front-end thread for Question-First Entry Tier 1. Live-testing the hundred strings is
optional and cheap-ish — **but the calibration already told us the load-bearing thing:
the questions are the cheap part, the Representatives are sound, and honest limits are
content.**

---
