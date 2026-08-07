# Church in Conversation: Representative Voice Rebuild — Design & Build Brief

## 1. Mission — read this first, it governs everything below

A Representative exists to let a real person encounter a real historical
Christian tradition — genuinely, not as a lecture in period costume. Per
Article 6 — the Constitution's own participant-facing evaluative measure
(`L1-Foundation/CiC_L1_Constitution_V2_2.docx`), which the Vision document
references directly, not authors itself — a real encounter keeps the Representative
itself, protects the participant's authorship, presents the world honestly
with its tensions held, and leaves interpretation to the participant. Mark's
own framing of this rebuild, verbatim: the Representative "has to be rebuilt
(not the name and role) but who they are to have a conversation that engages,
is natural and not distracting and gives truely insightful and accurate
answers." A voice a participant has to work to get into is quietly failing
"protect the participant's authorship" — it's making *them* cross into the
world, when a Representative's whole premise is that it crosses toward them.

**The plain-language test, alongside Article 6's formal one: would a modern
person actually enter into this the way they already do with other
programs, trust that what it says is true, and come away impressed rather
than lectured?** That means real adaptation, not translation-as-dilution —
the Representative is speaking *to* a person who lives now, not to someone
from its own world, so the delivery has to move toward them (plain
sentences, an entry point they already recognize, a reading level that
doesn't gate who gets in) while the actual content — imagery, vocabulary,
distinctiveness, the world's real positions — stays genuinely that world's
own. Diluting the content to ease the delivery fails Article 6's honesty
condition; refusing to adapt the delivery fails this test before the
content ever gets heard. Both failures are real, and this rebuild has to
solve for both at once, not trade one for the other.

## 2. What this rebuild is for

Mark named the actual architectural inversion needed: this system was built
**sources → voice → conversation** — the vetted record dictates the register,
and a participant has to enter through that register to be understood. It
needs to run **participant → bridge → world**, circularly: start from what a
person standing there actually needs to feel oriented and drawn in, reach into
the real record to answer them, and let the world's own flavor arrive as the
conversation deepens rather than as the price of entry.

**One thing does not move, stated by Mark twice, in these exact terms: no
fabrication. This is "our world grounding."** Register, structure, and
entry-point can all change. What a Representative is licensed to claim never
does.

## 3. What governs this — read directly, verify against it, don't design in a vacuum

- `Ministry/Communication/Vision, Mission, Convictions, and Foundational
  Commitments V1.1.docx` — every product decision below answers to it. Two
  of its Foundational Values govern most directly — **Participant Agency**
  and **Encounter Over Persuasion** — alongside two of its Five
  Convictions — **Authentic Encounter Requires Trustworthy Transparency**
  (#4) and **Technology Should Serve Encounter, Never Replace It** (#5). The
  other two Foundational Values, **Historical Responsibility** and
  **Intellectual Humility**, govern this brief too and weren't previously
  named here — Objective 4's no-fabrication line and finding (C)'s
  Marcella-story caution both answer to Historical Responsibility directly.
- `Ministry/Features/Front-End-Integration-Strategy/Decision-Log.md`, entry
  dated **2026-08-05 — "Live conversation test run"** — real per-call cost
  data, the exact defects and quotes found, and the two adjacent defects
  (§4) this brief carves out of scope. **The full transcripts themselves are
  not in this entry** (its own line 59 says so directly) — they were
  rendered as a claude.ai Artifact, not a repository file this thread can
  read. Treat the entry's own quotes and findings as the evidentiary record,
  not an "actual transcripts" claim this brief can't back up. **Treat that
  entry's entire findings list as superseded, not just the two lines its own
  note marks:** bullet 1 (the "100%" register claim), bullet 2 (finding B's
  "every retrieved chunk" claim — actually 107 of 118 lexicon chunks, and
  story chunks under a different field name entirely), bullet 4 (the
  original worked-examples conclusion), and bullet 6 ("the three plainest
  worlds," contradicted by Yausep's own measured sentence length) are all
  superseded by this brief's §5, marked or not — read §5 for the current
  diagnosis in every case.
- `L3C-Representative-Methodology/
  CiC_L3C_Representative_Construction_Framework_V3.2.docx` — the current
  Construction Framework, Part Five (Voice Construction) and Part Eight (the
  validation probe battery). Read Part Five closely before writing anything:
  it already states the destination — "This does not mean archaic English or
  artificial formality... language should feel natural rather than
  performed" — and this rebuild is as much about closing the gap between that
  stated principle and what six actual builds produced as it is about the
  Representative prompts themselves.
- `Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md`
  — the discipline this project holds every design claim to. Before treating
  any finding in §5 below as settled, verify it against the file/line it
  cites — this brief was assembled by directly reading the code and prompt
  files named, not by summarizing a summary, but check it anyway.
- **The existing research base this project has already paid for and
  verified — read before treating "what makes a good conversation" as an
  open question to answer from scratch. This is not optional background;
  §9's Research stage starts here, not with §5.**
  - `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/
    10_Fable_Conversational_Realness_Study_2026-07-24.md` — 105-agent deep
    research, adversarially verified (22 of 25 claims confirmed, 3 refuted
    and dropped, not just asserted). Its standout finding for this brief
    specifically: models state a persona but fail to *enact* it, especially
    by refusing to sustain disagreement — "a Representative that stops
    pushing back theologically stops feeling real *and* stops being
    faithful to its own world." Nothing in this brief's diagnosis or
    objectives addressed that before this revision (now Objective 6). Also
    names response-length growth, declining initiative, and agreement-rate
    drift as three specific, measurable naturalness-collapse signals — see
    §7 Part B and §8.
  - `.../09_External_AIPersona_Framework_Survey.md` — verified field
    inventories from shipping persona systems (Character Card V1-V3,
    SillyTavern). Its own verdict on worked examples is **mixed, not
    industry-wide either direction — "it is not unanimous," the document's
    own words** — but two prior drafts of this citation each got the
    specifics wrong in a different way, so read the actual tally directly:
    five sources treat demonstration dialogue as required/first-class
    (Google Conversation Design, Amazon Alexa, Salesforce, and, separately,
    two facts about the character-card ecosystem itself — Character.AI's
    own field limits, 32,000 characters for its Definition field against
    500 for description, and the `mes_example` field's normative status,
    Ali:Chat's whole authoring school built on it); two treat it as
    secondary (Microsoft: "relegated to a scratch pad"; IBM: absent
    entirely). **One genuine internal complication, not a simplification to
    smooth over: the Character Card *spec itself*, as distinct from
    Character.AI's own field limits, states `mes_example` "SHOULD... be
    pruned to make room for actual conversation history"** — i.e., the
    written spec calls it ephemeral even though Character.AI's actual
    production numbers and the Ali:Chat community both treat it as
    load-bearing in practice. Spec and practice disagree with each other on
    this one point; cite them as two separate facts, not one. What's
    actually unanimous across every source, for or against: description or
    trait-adjectives come first, as the rubric, and dialogue — where used —
    gets written and judged against them, never the reverse. And one clean,
    single-direction, directly relevant data point: Anthropic's own
    prompting guidance recommends 3-5 examples for steering output format,
    tone, and structure. Read all of this as genuine, unresolved evidence
    for §7 Part A's worked-example plan, not as a reason to lean either way
    in advance — Fable's Research stage still has to answer this for CiC's
    own case. Separately,
    `post_history_instructions` exists because instructions placed after
    conversation history carry measurably stronger weight than instructions
    before it — this one *is* a clean, single-direction finding, and
    independent, external confirmation of the exact principle behind
    FLAG-018 layer 3 (finding C), that the constraint most needing to
    survive attention decay rides closest to generation.
  - `.../07_RepresentativeVoice_Lenses_Audit.md` — already investigated
    whether pre-written insight material (Ecological Function and its kin)
    actually reaches a Representative, and found the failure pattern is
    usually placement or form, not absence: Papnoute's Abba Moses
    misattribution traced to correct information already sitting in the
    World Capsule as an unnamed allusion, fixed by promoting it into the
    Permanent Prompt as an explicit ownership rule — "same information,
    different placement and form." Worth checking finding (B)'s own
    diagnosis against this precedent directly.
  - `.../16_MultiParty_Dialogue_Architecture.md` — Facilitator/table-scoped.
    **Deliberately out of scope here, by explicit sequencing decision
    (2026-08-07), not because it matters less.** Table-mode conversation
    quality — engaging the participant as a real party at the table
    alongside the Representatives, celebrating genuine consistency across
    traditions, clearly surfacing genuine difference, reading whether a
    participant wants the exchange more personal or more theological — is
    named as equally critical to this rebuild's own single-voice work, and
    is planned as a deliberate second phase once this one ships, using the
    same research → design → blueprint → build discipline, not a lesser
    follow-up. Still worth reading now for anything that bears on the
    six-voice work itself (per finding on `table_discourse.py` in §4), just
    not the ground for a Table-mode redesign in this thread.

## 4. What NOT to rebuild — this is a voice rebuild, not a restart

- **The world/source layer's content** — lexicon chunks, story chunks,
  source registries. Confirmed good by Mark directly. Prose *style* inside
  the World Capsule Core files is explicitly in scope (§7); their
  *content/sourcing* is not.
- **The no-fabrication apparatus** — the near-verbatim shared "museum guide"
  fabrication-guard block, literally present (verified by direct string
  match) in **Yausep's and Marius's** permanent prompts only. Theon carries
  the same mechanism fully reworded, not near-verbatim — a different figure
  ("one who keeps the reading of a school long since scattered"), same
  three-failure-mode structure — closer in kind to Papnoute's own
  differently-worded version than to Yausep's/Marius's near-copies. Do not
  edit, shorten, or soften any of the four under any framing.
- **The near-verbatim "witness not recruitment" block** — present, reworded
  per world, in **all six** files, not five: Chloe's, Albina's, Yausep's,
  Theon's, Marius's (which names it "SECTION 6 — WITNESS-NOT-RECRUITMENT"),
  **and Papnoute's own version** ("you do not argue as an advocate arguing a
  case... whoever is speaking with you is free to leave this conversation
  exactly as they arrived" — missed in an earlier pass of this brief because
  it isn't set off as its own labeled section). Not fabrication-related, but
  a separate, deliberate, already-shared module — leave its content alone;
  it's fine if register work touches its sentence rhythm the same way it
  touches surrounding prose.
- **Historical identity, era, and vocabulary content** in every permanent
  prompt — who each Representative is, what span they speak from, their
  world's real terms. This rebuild changes how something is said and what
  gets reached for, never the facts being spoken.
- **The governance/monitoring layer.** Confirmed directly, this session, by
  reading the actual prompts: `over_settling` (`app/prompts/
  facilitator_prompts.py:241`, its own screen prompt states "tone is not a
  limit... the question is whether the specific qualification this claim
  needs is present, not whether the voice sounds modest"), `citation_grounding`
  (`app/graph/nodes.py`, explicitly tolerant of paraphrase, purely
  content-mapping), and `drift_detection`'s signals — **twenty declared
  types** (`app/graph/state.py`'s `DriftSignal.signal_type`, confirmed by
  count; `wrs/parameters.yaml:116-121` records the same number and its own
  history — an earlier "ten" or "seventeen" count is stale, flagged FLAG-016
  in that file) — are all content- or posture-based, not register-based.
  Two of the twenty are worth naming here specifically since §7 Part B
  cites them: `agreeing` (signal 3) and `over_producing` (signal 4) already
  exist as declared types, covering agreement-drift and response-length
  growth by name — see §7 Part B for what that changes about the "new
  telemetry" framing. One exception worth empirical
  attention, not redesign: `FLATTENING` ("sounds like educated generic
  Christian voice with historical accent") is a holistic LLM judgment that
  could plausibly read "plainer" as "more generic" — watch it in verification
  (§8), don't design around a hypothetical.
- **Confirmed inline glosses** (`app/prompts/confirmed_glosses.py`) — a
  small per-world whitelist requiring an exact fixed string for specific
  terms, checked deterministically. Explicitly out of scope by its own
  docstring: "the only place... an exact form is asked... everything else
  about how you speak is unchanged."
- **Retrieval ordering.** Tier-based sorting of retrieved documents before
  they reach the model is a real, confirmed-cheap follow-up
  (`doc.metadata["tier"]` already exists per chunk in `app/rag/
  indexer.py:227`; the hook point is a sort key before the per-document loop
  in `app/rag/retriever.py:192`, `get_context_for_response`) — Mark's own
  framing was "we could still add some more codes to prioritize things," a
  minor addendum. Note it, don't build it, unless the blueprint stage finds
  a compelling reason it has to move together with the voice work.
- **The `wrs/` record layer must move in lockstep with `data/`, not be
  treated as separate scope.** Every world has a `voice_profile/` record
  under `wrs/records/<world>/`, and `wrs/views/probe_parity.py` compares
  deployed prompts against generated ones. The running app reads `data/`
  directly (`main.py:156`), so `data/`'s six permanent-prompt and capsule
  files remain the real rebuild target — but a hand-edit to `data/` that
  isn't mirrored into the matching `wrs/records/` entry desyncs the record
  layer the gates (including the readability gate in §7 Part B) read. §7's
  per-world passes must update both files in the same pass.
- **The existing interview-vs-table pacing distinction — real, but not where
  an earlier draft of this note placed it.** `REACTIVE_TURN_GUIDANCE`
  (`app/prompts/table_discourse.py:75`) carries no length ceiling and
  explicitly refuses one: *"does not need to be brief for its own sake if
  there is a real view to add... do not match your length to the turns
  around you... speak at your own formation's measure even when it is
  conspicuously shorter or longer."* `table_discourse.py` has no per-world
  reasoning either — only `CROSS_WORLD_VOCABULARY_GUIDANCE`, about
  terminology, not pacing. **The actual, only turn-length ceiling in the
  system is `_HOW_YOU_ENGAGE`'s "A Turn Has a Measure"**
  (`representative_prompts.py:59-60`: "default short: most turns are one to
  two short paragraphs, and a turn should almost never exceed three") —
  which is inside the exact block §7 Part A rewrites, not a separate file
  to preserve alongside it. And the real asymmetry runs opposite to how
  this note first described it: a solo Deep Interview turn gets *less*
  injected guidance, not more restrictive pacing —
  `reactive_turn_guidance = ""` for that path (`nodes.py:1140`), its own
  comment recording that turn-shape guidance was deliberately folded into
  `_HOW_YOU_ENGAGE` instead of kept as a separate block. **What this means
  for scope:** there is no separate interview-vs-table mechanism sitting
  outside `_HOW_YOU_ENGAGE` for the register rewrite to accidentally
  collide with — the one real length instruction *is* inside the block
  being rewritten, so §7 Part A's edit has to preserve "A Turn Has a
  Measure" deliberately, and every new instruction §7 Part A adds pushes
  length upward against exactly this ceiling — worth Design treating as a
  real tension, not background noise.
- **Two adjacent, already-diagnosed defects, deliberately not bundled here** —
  log them for Mark's own separate triage rather than fixing them as part of
  this thread:
  1. `CitationModal.tsx` renders a citation's `key_sources` field in full,
     unfiltered, to participants — and some `key_sources` values carry
     build-process language straight from source chunk files (a real example
     surfaced this session: "...is itself the term's own live contest. See
     CT Contest Type below" — a dangling reference to an internal document
     no participant can see).
  2. `over_settling_adjudication` fired on 10 of 12 turns in this session's
     live test — not a rare safety net in practice. Worth watching (§8)
     since a "begin with substance, avoid generic hedging" voice
     instruction pushes toward more unhedged claims, which is exactly what
     this check screens for — but fixing the check itself is out of scope
     here.

## 5. The diagnosis — what's actually broken, and where

Four converging findings, verified directly against the code and prompt
files, not inferred:

**A. Five of six worlds already explicitly instruct short, plain, paratactic
sentences — the "100 percent sourced from the six files" framing this
finding originally used was itself imprecise, and this brief should not
carry that imprecision to Fable.** `app/prompts/representative_prompts.py`'s
`_HOW_YOU_ENGAGE` block (lines 5-76) does defer register to each world's own
file: "Your own permanent formation... specifies how your world
characteristically builds an answer... That is your register." But the six
files aren't a blank canvas the archaic register simply fills — five of the
six already state close to the opposite instruction, explicitly, in
comparable language, and it isn't being followed:
- **Papnoute** (desert-monasticism, `:7`) — "Your sentences stand next to
  each other; they do not lean on each other... Say the thing. Stop. Say
  the next thing." The only file with worked example dialogues.
- **Chloe** (PAHC, `:23`) — "build it as a line of short, separate
  sentences, not one sentence carrying several ideas stitched together with
  dashes. Land one part. Stop." No worked examples.
- **Mar Yausep** (Syriac, `:41`) — "Each stage is its own short sentence...
  Land one thought. Stop. Begin the next stage fresh." No worked examples —
  and he already carries a bridge-first instruction close to what §7 Part A
  proposes adding project-wide; see finding (C) for why that matters more
  than it first appears to.
- **Theon** (Alexandria, `:37`) — "You keep each thought in its own short
  sentence. You land one thing, and stop." No worked examples.
- **Marius** (Imperial-Juridical, `:117`) — "one short sentence for the
  first fact. A full stop... Each one short enough to stand alone." The most
  detailed of the five plain-sentence files — his SECTION 3 register block
  is longer than Papnoute's, so "Papnoute has the richest register
  instruction" was a size impression, not a measured one.
- **Albina** (Hieronymian, `:29`) — the one genuine, deliberate exception:
  prescribes periodic/hypotactic Latin-scholar sentence rhythm ("one clause
  answering to another") as her own formation-accurate voice, explicitly the
  opposite of the other five, argued with comparable craft, with her own
  built-in anti-stacking limiter. No worked examples.

Five files instructing short sentences and mostly not getting them, plus
§7's own separately-confirmed finding that the elevated register runs
through the identity/era/vocabulary paragraphs and the World Capsule Core
files too, not only the paragraph labeled "how you speak" — together, these
say the register gap isn't a missing instruction. It's an unenforced one,
running through more surface than any single paragraph fix reaches. That
reframes what §7 Part A is actually for: not writing the plain-sentence rule
for the first time, but making an already-written rule (in five of six
files) actually hold, plus getting right the one file (Albina's) where the
existing instruction is the genuinely correct one and shouldn't be touched.

**B. Most, not all, of the raw material for insight and bridging already
reaches the model — and lexicon and story chunks carry it under different
field names, which matters for how §7 has to word the instruction to use
it.** Measured directly against every chunk file, not sampled:
- **Lexicon chunks (118 total):** 107 of 118 carry an actual `Ecological
  Function` field — not 109; the two remaining string matches
  (`ijclex011_basilica.md`, `ijclex012_martyrium.md`, both Marius/IJC) are
  chunks that mention "Ecological Function" only to record it was
  **omitted** per their own Tier-3 template instruction, not chunks that
  have the field. All 118 carry `Distortion Risk` (Modern Hearing vs. World
  Hearing). `Tier` is present in each file's own front matter but is
  discarded by the lexicon parser before serialization — it survives only as
  `doc.metadata["tier"]` (`app/rag/indexer.py:227`), reachable for sorting
  (§4's retrieval-ordering note) but never as text the model actually reads.

  **Two distinct leaks, not one, and the second is worse than the first —
  found by executing the actual serialization path, not by grepping for a
  field name.** First: at least a quarter of the 107 Ecological-Function
  chunks carry internal build-process language, not participant-safe
  insight — `hal_lex11_exegesis-practiced-authority.md`'s field reads,
  verbatim, *"The evidentiary core of this world's one Tensional gravity...
  this candidate was tested directly and found insufficient to establish a
  difference in kind."* "Tensional gravity" and "candidate... tested" are
  this project's own internal gravity-analysis vocabulary (Doc_04/Doc_08
  apparatus). Same pattern, different fields, in other worlds: `Related-
  Terms Reciprocity Note` in Yausep's `syrlex005`/`syrlex008`, `Confidence:
  Inferential-Thin` in Chloe's `pahclex012`/`pahclex013`.

  Second, and structurally worse: `truncate_at` (`app/rag/sections.py:159-
  160`) returns a chunk's body **completely unchanged** when it finds no
  `Key Sources` marker to cut at — a fail-open, not a fail-safe. **Six
  chunks have no marker at all**, so their entire body, including trailing
  internal notes, reaches the model verbatim. `ijclex011_basilica.md` — one
  of Marius's, an acceptance world — ends, unfiltered, with: *"## Final
  Assembly Instruction — Completed per `L4-Templates/Deployment_Lexicon_
  Chunk_Template.md` V1.0 (Tier 3: World Meaning brief, Ecological Function
  and Key Sources omitted per Template instruction). No brackets or builder
  notes remain. CT tag not applied."* This is a real gap in what the
  project could otherwise treat as settled about how Key Sources stripping
  works — it only strips when it finds something to strip at. §7 Part A's
  leak filter (below) needs to cover both patterns, not just the
  Ecological-Function field specifically — a filter scoped to one field
  name misses the worse of the two.
- **Story chunks (60 total):** all 60 carry the same instinct, but under a
  different name — `## Formation Ecology Connection`, not `Ecological
  Function`. None carry a `Distortion Risk` equivalent; no such field exists
  in the story-chunk format at all. Story `Tier` reaches the model, but not
  for the reason an earlier draft of this finding claimed (**a real
  correction, not a restatement**): it is not that story front matter
  escapes the stripping lexicon front matter gets — 35 of the 60 story
  files carry the identical `## Retrieval Front-Matter` block lexicon files
  do. Tier reaches the model because `app/rag/story_retriever.py:148`
  explicitly synthesizes it into every retrieved story's own context header
  (`f"### {title} (Tier {tier})\n"`, pulled from `doc.metadata["tier"]`),
  independent of whatever happens to the body — a deliberate code behavior,
  not an accident of file layout. Lexicon's own retriever
  (`app/rag/retriever.py`) has no equivalent line, which is the actual,
  narrow reason lexicon `Tier` doesn't reach the model and story `Tier`
  does.

Confirmed directly via `app/rag/retriever.py:get_context_for_response`:
`Key Sources` is stripped (`truncate_at(body, KEY_SOURCES_MARKERS)`), and,
for all six migrated worlds, `Quick Meaning` is also stripped
(`retriever.py:224`) — not previously noted here. (`app/rag/sections.py`
defines the marker constants both strip on; it doesn't itself confirm what
reaches generation context — `retriever.py` does, and is the file to cite
for that claim.) Nothing in `_HOW_YOU_ENGAGE` or any permanent prompt
instructs the model to lead with any of this, which is a real gap and most
of why answers currently "pick random things." But §7 Part A's instruction
to "lead with Ecological Function/Distortion Risk material" needs its own
wording to survive contact with the data above: as written it silently
no-ops on all 60 story chunks (wrong field name) and Distortion Risk simply
doesn't exist for stories. The instruction needs to name `Formation Ecology
Connection` explicitly as story material's own version of the same
instinct, not assume one field name covers both chunk types.

**C. Four layers of guard already exist against unprompted term-reclarification,
not two — and the same-day pilot that seemed to test them was a
non-discriminating null result, not a weak negative one. This finding needed
a real correction, not a restatement, and got one on 2026-08-06.**

The guard commonly labeled FLAG-018 is **not inside `_HOW_YOU_ENGAGE`**
(`representative_prompts.py:5-76`) — an earlier draft of this brief cited it
there, and that citation was wrong. It's composed at four separate points:
1. `representative_prompts.py:168-181` — inside `build_representative_
   prompt`'s dynamic per-turn content, and only present at all `if
   retrieved_context:` — absent entirely on a turn where retrieval surfaces
   nothing.
2. Chloe's own permanent prompt, an independent per-world copy (`:29`).
3. `app/graph/nodes.py:1155-1167` — a second copy, composed at the wiring
   site and appended closest to generation, live on every migrated world's
   turn. Its own comment carries a measured baseline never previously cited
   here: *"the no-unprompted-sense-clarification constraint survived only
   partially when placed before the retrieved context (one false 'I meant X
   earlier' opener remained in 16 turns)."* This guard already wasn't fully
   holding, measured, before today's pilot.
4. `app/graph/nodes.py:~3871` and `app/graph/modern_term_bridge.py:237` — a
   mechanism, not prose: a citation only proves a chunk was *retrieved* for
   the turn, not that the voice *spoke* the term, so an earlier version of
   a related offer could fire on a retrieved-but-unspoken term and produce
   exactly this false-referent opener. Already partly fixed at the code
   level.

Marius also carries a fifth, per-world instance (`:119`) not previously
named here, plus a unique IJC-scoped extension of layer 3
(`nodes.py:1174-1180`) — he is not exempt from this failure mode, and he is
one of the two named acceptance worlds (finding D).

**What the same-day ad hoc pilot (`cic-poc/backend/scripts/
mark_voice_simulation.py`, results not committed to the repo) actually
showed, read honestly:** it tested a bridge-first instruction plus positive
worked-example dialogues against Chloe, live through the real backend,
current prompt vs. prototype. The guarded behavior — an unprompted "when I
said X a moment ago" opener — surfaced in **both arms**, not only the
prototype. That makes this pilot a non-discriminating matched pair, not a
weak negative result about worked examples specifically: it shows the
pre-existing guards weren't holding either, which layer 3's own 1-in-16
baseline above already established. It does not, by itself, tell Fable
anything new about whether worked examples help.

There's also an unnamed confound worth stating plainly: the prototype's own
added shared-file text (`PROTOTYPE_ADDITIONS` in the pilot script) instructs
the model that *"where a retrieved note names the gap between a modern
assumption and your own world's actual view, that gap is often exactly the
bridge worth opening with"* — language close enough to the guarded-against
move that the pilot may have partly cued the very behavior it was probing.
Two further things this pilot surfaced that hadn't been reported before this
revision: the prototype's Chloe turn 1 opens with a false claim about the
participant's own conversational history ("you asked this before, or
someone standing where you stand asked it") — a new defect, not a repeat of
an old one — and the prototype's turn 3 is measurably *more* honest than the
current arm on an unrelated factual point. This pilot is genuinely mixed
evidence, not a clean negative.

**A second, more consequential pilot result belongs in this finding and
hadn't made it into the brief before this revision.** On Albina's prototype
run, the same pilot produced a `fabrication_adjudication` signal — the one
governance check this brief names as completely out of scope and
non-negotiable (§4, Objective 4) — on the exact turn where the prototype
told the Marcella story concretely, elsewhere in this thread's own process
notes cited as a clear win for bridge-first storytelling. Checked directly:
not a fabrication — it traces to a real source chunk
(`hal_story05_marcella-death.md`) — but that chunk's own Usage Guidance says
the detail follows "the epitaph genre's conventions of dramatic irony...
real, but shaped by a commemorative genre, not a transcript," and the
prototype delivered it flatly, as record. This is exactly the risk a
bridge-first, lead-with-the-concrete-story instruction creates if it isn't
paired with an equally explicit instruction to carry a source's own genre
caveats into the telling — Fable's Research stage should treat this as a
real, not hypothetical, interaction between Objective 2 (draw on stories
more) and Objective 4 (no fabrication, ever), not a coincidence to note and
move past.

**What was already correctly left open stays open, and today's correction
if anything weakens the case for a specific fix:** whether worked examples
are the right tool for any of this is still Fable's Research-stage
question — the pilot that seemed to bear on it turns out not to
discriminate at all. The Papnoute check (does his existing worked-example
pattern hold up against this exact probe) is still worth running. But
there's a cheaper, sharper check that should run first: **Mar Yausep's
permanent prompt already contains a bridge-first instruction close in
spirit to what §7 Part A proposes adding project-wide** — `syr_
Representative_Permanent_Prompt_Yausep.txt:45`: *"Before you reach for
raza, qyama, or Iḥidaya as your first word, ask whether your own record
gives you a face, a name, or a scene for this question instead... Let the
word follow the story, not stand in front of it."* This instruction already
exists, in a world that still showed the guarded-against behavior live
(this finding's original evidence, before today's pilot). Papnoute's check
tells Research whether *worked examples* work. Yausep's tells Research
whether *prose instruction of any kind* is the right lever at all — the
prior question, and the cheaper one to answer since the instruction to test
is already written. **Run Yausep's check first**, not as a substitute for
Papnoute's but as the one that should come before it. Do not carry a
specific fix (e.g., a contrastive/negative example paired with the positive
one) into the Design stage as a foregone conclusion from either check —
treat both as Research-stage evidence, not a decided approach.

**D. The three baseline transcripts this session captured do NOT actually
reproduce "over formal / distracting" — but "the three plainest worlds
already" overstates it, and shouldn't be repeated as written.** Read cold,
all three (Papnoute, Chloe, Mar Yausep) handled real pushback substantively
and didn't read as generic or archaic in a way that visibly matches the
complaint — that part holds; the Decision Log entry named in §3 carries the
real quotes and cost data this finding rests on, not the full transcripts
themselves (§3's own correction — those live only in a claude.ai Artifact).
But measured mean sentence length from those
same baseline transcripts complicates "plainest": Papnoute 14.6 words/
sentence, Chloe 16.6 — genuinely short — but **Yausep 23.0**, statistically
indistinguishable from **Albina's 23.6**, the world this brief treats
throughout as the elaborate, register-heavy exception. Yausep reads as
substantively engaged in these transcripts; he does not read as short. This
matters concretely for how this thread verifies its own work (§8):
re-testing only these three worlds and finding they "still read fine" proves
even less than originally stated, since one of the three was never
demonstrably plain to begin with. **The real acceptance evidence has to come
from Albina and Marius** — the two worlds never live-tested this session,
and, per the comparative read in (A), the two with the most to lose from a
careless rewrite (Albina's deliberate periodic rhythm; Marius's entangled
register-and-reasoning-mode) — **with Yausep added as a third world worth
deliberate live-testing**, not assumed safe as a "plain" baseline.

## 6. The concrete objectives

**Priority, not just a list — two parallel things this rebuild fails at its
peril, one mechanism that makes the first of them possible, a second tier,
and one thing held apart because it isn't a property of any single
conversation at all.**

- **Two parallel, non-negotiable priorities — neither one waits on the
  other, and either one failing fails the whole program:** Objective 3
  (conversation quality — clear, easy to understand, engaging, genuinely
  that world's own flavor) and Objective 4 (honest, rigorous
  representation — from the real source record, no fabrication,
  transparently sourced). These are not sequential; they're the two axes
  the Mission's plain-language test (§1) actually measures.
- **Objective 1, bridge-first entry, is the mechanism that makes Objective 3
  achievable — not a third priority sitting beside it.** If a participant
  has to work to orient themselves before a conversation starts making
  sense, "clear, easy to understand, engaging" has already failed,
  regardless of how good the content underneath is. It has to run
  circularly (participant → bridge → world → back to the participant, an
  actual loop, not a one-way handoff), which is a real design task on its
  own — see the note at the end of Objective 1 below.
- **Tier 2, real but not immediately program-ending:** Objective 2
  (insightful, well-ordered answers) and Objective 6 (consistent — holds
  under pressure, doesn't drift, doesn't compromise).
- **Held apart, not ranked among the others at all:** Objective 5. A
  replicable build process is a property of the system that produces
  conversations, not a property of any one conversation, and doesn't belong
  ranked against qualities a participant actually experiences.

1. Every Representative opens from where the participant actually stands —
   a recognizable want, fear, or doubt — before reaching for the world's own
   vocabulary or imagery. Period flavor arrives once the bridge is built, not
   as the price of admission. **The circular half of this, not yet a
   concrete mechanism:** a real callback to something the participant
   already said is what actually closes the loop back to them, rather than
   the conversation only ever launching forward from an opening bridge. The
   Realness Study's "proactive memory surfacing" finding (§3) is the
   closest existing lever — worth Fable's Research stage treating as a real
   design task, not an assumption that circularity falls out of bridge-first
   for free.
2. A substantive answer draws on what's genuinely insightful (Ecological
   Function, Distortion Risk) rather than whatever's topically nearest, and,
   when the question calls for it, is built in a defensible order: most sure
   first, genuinely distinctive second, honestly unsettled last and lightest
   — as **one option among a real repertoire of answer shapes**, not a new
   template replacing the old one. (Mark's own words: "we need to have
   several patterns so it doesn't just repeat the same thin process.")
3. Sentences read as plain, real, everyday spoken English — not costume
   diction — while keeping each world's genuine imagery, vocabulary, and
   actual distinctiveness as seasoning, not performance. **This is
   adaptation, not dilution: the Representative is speaking to a person who
   lives now, not to someone from its own world, so the delivery moves
   toward them while the content stays genuinely that world's own** (§1).
   Concretely, that means holding to Part Five's own reading-level floor
   (Flesch-Kincaid grade 8-10, Flesch Reading Ease 60+) as an access
   requirement, not a style suggestion — a reader who isn't already fluent
   in this register has to be able to get in at all. Part Five's own text
   draws a real line here: register elaborateness and accessibility are
   separate axes, and "a world whose own sources are rhetorically trained
   and elaborate should still keep its sentences within the accessibility
   band — elaboration belongs in vocabulary, imagery, and clause content,
   not in unbroken sentence length." That reading of Part Five is right and
   holds.

   **What does NOT hold, and this brief should not assert a resolution it
   doesn't actually have: "achieve her periodic quality through vocabulary
   and clause richness instead of sentence length" is not a working fix,
   it's arithmetically impossible at her measured length.**
   `readability_check` computes Flesch-Kincaid from exactly two variables —
   words per sentence and syllables per word. At Albina's measured 23.6
   words/sentence, passing the grade-10 ceiling requires roughly 1.39 or
   fewer syllables per word on average — *simpler* vocabulary than any of
   the other five prompts currently run (they measure 1.34-1.47), not
   richer. Richer vocabulary makes the score worse, not better; clause
   *structure* (subordination, held qualifications) is invisible to the
   formula entirely. The only lever that actually moves her score is
   shortening her sentences — which is precisely the "kept substantively"
   protection this objective states in its opening sentence, for a rhythm
   this brief has argued elsewhere is genuine, formation-accurate craft,
   not incidental archaism.

   **This is a real, unresolved tension, not a solved problem — Fable's
   Design stage has to actually decide it, with the tradeoff stated
   plainly rather than assumed away:** either Albina's sentence length
   comes down to pass the same floor the other five hold to (a real cost to
   what makes her voice distinct), or this project decides her periodic
   rhythm is a deliberate, named exception to the accessibility floor
   specifically (a real cost to Objective 3's own access argument, and one
   this brief cannot make unilaterally — it's a values call, not a prompt-
   engineering one). §9's Research stage should confirm whether
   `readability_check` has ever actually been run against her current
   prompt and what it returned, and Design should make this decision
   explicitly and name it, rather than the gate silently failing her (or
   silently never being run on her) while this objective still reads as
   settled.
4. No fabrication rule moves, anywhere, under any framing. **Paired with
   transparent sourcing, not separable from it** — the existing three-level
   transparency mechanism (Article 30: inline in the text, hover for a
   summary, click for full detail — already built, `CitationMarker`/
   `LexiconHighlight`) has to keep working honestly through this rebuild,
   including its one known real defect (the `key_sources` leak, §4) and its
   one open placement question (per-turn marker vs. something closer to
   per-story) — neither is this thread's job to fix, but both are this
   thread's job not to make worse by changing what citations actually carry.
5. The Construction Framework itself changes so that world #7 doesn't
   reintroduce this exact gap — "self-sufficient... as we have done all
   along," Mark's own words. This is not optional scope; it's the actual
   point of doing this on a dedicated thread instead of hand-patching six
   files.
6. A Representative holds its world's actual position under real, sustained
   pushback across a conversation — the Realness Study's own standout
   finding (§3), and CiC's naturalness goal and fidelity conviction
   converging on the same fix: a voice that drifts toward agreement to stay
   comfortable is failing Objective 3's naturalness the same turn it fails
   to actually witness its world. Explicitly licensed, not just permitted by
   omission, and validation-probed (§8) across multiple turns of real
   disagreement, not read off a single turn's tone.

## 7. The shape of the output — two parts, both required

### Part A — rebuild the six Representative voices

**This is a clean rebuild, not an edit pass — read this before writing
anything, it governs every bullet below.** Design does not start from the
current permanent prompts and work forward by auditing and adjusting them.
It starts from the world's actual sources — lexicon chunks, story chunks,
the World Capsule Core's own content, the Source Registry (all confirmed
good and frozen, §4) — and from this brief's own principles (§1, §2, §6),
and writes fresh. The current permanent prompt is one input signal among
several, no more privileged than the raw source material, not the document
being edited. **No comparative diffing against the current prompt is part
of the design process itself** — that's a §8 verification activity (the
continuity-regression pass), a different purpose (checking the rebuilt
voice against the deployed one for returning-participant continuity), not
how the new voice gets built.

This matters concretely, not just procedurally: Mark's own stated
concern is that six builds have accumulated assumption rules that were
never actually necessary — inherited because an earlier file already said
them, not because the sources support them. **The test for keeping
anything from a current prompt is never "it's already there" — it's "the
source material actually supports it."** Albina's periodic rhythm, Marius's
precedent-first reasoning, Yausep's stage-by-stage demonstration structure —
if these are genuinely attested in the world's own real character, a clean
build grounded in sources should re-derive them on its own, for the right
reason, not inherit them by default. If something only survives in the
current prompt because nobody ever questioned it, a clean rebuild is
supposed to let it drop. Finding (A)'s own comparative read already argues
Albina's rhythm is genuine, formation-accurate craft, not incidental
archaism — that's evidence worth weighing during the rebuild, not a reason
to skip re-deriving it from her actual sources.

**The same license applies to cost and complexity, not just voice — say so
explicitly rather than let it default to "add more."** This brief's own
three adversarial-review rounds added real apparatus this week: readability
enforcement, fabrication-rate tracking, per-signal drift telemetry,
three-level-sourcing checks, sustained-disagreement probes,
continuity-regression testing. None of it is fixed by default just because
this document names it — Design has explicit license to question, simplify,
or drop any of it if it doesn't earn its cost and complexity, the same
scrutiny applied to what six builds inherited. This does **not** extend to
the no-fabrication apparatus, the witness-not-recruitment block (§4,
untouchable under any framing), or the existing governance layer
(`over_settling`, `citation_grounding`, `drift_detection` — §4, already
justified as content-based, not up for reconsideration here). One real,
already-measured tension worth naming rather than silently resolving either
way: `over_settling_adjudication`'s second-stage check is the single
largest invisible cost line item after the main response itself (§4,
10-of-12-turns finding), and §4 currently treats fixing the check itself as
out of scope. Now that lowering cost and complexity is an explicit goal of
this rebuild, Design should raise this tension with Mark directly rather
than assume either "still out of scope" or "now in scope."

- **Pilot first, isolated.** Rewrite the shared `_HOW_YOU_ENGAGE` block
  (`representative_prompts.py:5-76`) — bridge-first entry; explicit
  instruction to lead with Ecological Function material (and its
  story-chunk equivalent, `Formation Ecology Connection` — see finding B,
  these are not the same field and need naming separately) **filtered for
  the two real risks finding B names — roughly a quarter of Ecological
  Function fields carrying internal build-process vocabulary ("Tensional
  gravity," "candidate... tested"), and a handful of chunks with no Key
  Sources marker at all whose entire body, internal notes included, passes
  through unfiltered — neither is topical material safe to lead with**; the
  shape
  repertoire from objective 2 folded into the existing "Let the Question Set
  the Shape, Not a Habit" section as one option among several — story-first,
  question-behind-the-question, plain-and-short, consensus-then-contrast.
  **The FLAG-018 guard itself is not inside this block** (see finding C —
  it's composed at four separate points, none of them `_HOW_YOU_ENGAGE`);
  don't word anything here as an "extension" of a guard that lives
  elsewhere. If Design concludes the guard needs strengthening, that's a
  change to `nodes.py`'s layer 3 (closest to generation, already carries a
  measured 1-in-16 baseline) or one of the per-world copies, not to this
  block — keep the two changes distinct so a failure in one isn't misread as
  a failure of the other. Pilot it against Chloe alone, verify in isolation
  (§8) before touching any other file.
- **Per-world passes, risk-ordered — Albina → Marius → Theon → Papnoute →
  Chloe → Yausep.** Not build order, not alphabetical: highest-register-shift
  and least-validated worlds first. Each pass covers **both** that world's
  permanent prompt **and** its World Capsule Core file (Mark confirmed:
  capsule content/sourcing frozen, prose style in scope — the capsule sits
  in the cached prefix at equal weight to the permanent prompt on every
  turn, in the same elevated register, so a register fix that stops at the
  permanent prompt is capped by its own neighbor).
  - Write each world's identity, era, vocabulary, register, and
    reasoning-mode content fresh from its actual sources — not an audit of
    the existing paragraph labeled "how you speak," since the elevated
    register this brief diagnoses runs through more surface than that one
    paragraph (confirmed by direct reading: identity, era, and vocabulary
    paragraphs currently carry the same stylization, and a clean rebuild
    starting from sources rather than editing that paragraph is what
    actually reaches all of it). Content, fabrication-guard, and
    witness-not-recruitment blocks untouched — these are re-included as
    given, not rebuilt.
  - A reasoning-mode structure — Marius's precedent-first chancery mode,
    Yausep's stage-by-stage demonstration, Theon's surface-then-depth
    unfolding, etc. — earns its place only if the world's actual sources
    support it, tested fresh, not carried forward because the current file
    already has it. Where it re-derives genuinely, host the shape
    repertoire (§6 Objective 2) inside it; where it doesn't, it's not a
    "reconciliation" problem to solve, it's evidence the structure wasn't
    load-bearing to begin with.
  - Write worked `{{random_user}}`-style example dialogues for all six
    worlds as part of this same fresh build (five currently lack them,
    Papnoute doesn't — write his fresh too rather than treating him as
    already done, so all six are built to the same standard). **The exact
    form these examples take (positive-only, or paired with a
    contrastive/negative demonstration) is a Design-stage decision, made
    only after the Research stage resolves the open question in finding
    (C) — not prescribed here.**
  - Albina's periodic/hypotactic rhythm is kept substantively if it
    re-derives from her actual sources during the fresh build — finding
    (A)'s comparative read already argues it should (genuine,
    formation-accurate craft, not incidental archaism) — but that's a
    prediction to confirm against her sources during the rebuild, not a
    standing exemption from writing her fresh like the other five.
  - Update the matching `wrs/records/<world>/voice_profile/` entry in the
    same pass, not as separate cleanup (see §4) — the running app reads
    `data/`, but `wrs/views/probe_parity.py` and the readability gate (§7
    Part B) compare against the record layer, and a `data/`-only edit
    desyncs the two.
- **Facilitator's three "distinct from period diction" occurrences**
  (`app/prompts/facilitator_prompts.py`, Acute Distress/Harmful Dynamic
  prompts, roughly lines 429/449/485) — fixed last, once all six permanent
  prompts are settled, so the replacement contrast phrase is accurate to
  the actual new voice rather than guessed early. This is a real safety-UX
  cue (helps a participant register mid-conversation that the Facilitator,
  not the Representative, has broken in) — don't just delete it, replace it
  with something still true.

### Part B — revise the Construction Framework itself

Update `L3C-Representative-Methodology/
CiC_L3C_Representative_Construction_Framework_V3.2.docx`:
- **Part Five (Voice Construction) already has real operational teeth, not
  just principle — the gap is narrower than this brief originally framed,
  and Fable should know that before proposing to build what's already
  built.** Part Five states a numeric floor: "a Flesch-Kincaid grade band of
  roughly 8 to 10 and a Flesch Reading Ease of 60 or above... this standard
  is independent of vocabulary" — and, immediately after it, the exact
  guidance §6/§7 believed they were inventing for Albina: "A world whose own
  sources are rhetorically trained and elaborate should still keep its
  sentences within the accessibility band — elaboration belongs in
  vocabulary, imagery, and clause content, not in unbroken sentence length."
  Both ends are real and wired: `wrs/parameters.yaml:101-114` (the canonical
  numbers, sourced to this exact Part Five passage) and
  `wrs/gates/core.py:211` (`readability_check`), which hard-fails rather
  than silently passing when it can't check. **The open question this brief
  cannot answer and must not guess at: has this gate actually been run
  against the six current builds.** If it has and they pass, the register
  problem isn't a missing standard at all — FK/FRE measures
  vocabulary-independent grade level, not archaic *diction* or performed
  formality, and text can score inside the band while still sounding like
  costume. If it hasn't been run, that's the cheapest, most concrete first
  Research-stage task in this brief. Either way, Part Five's real gap is
  narrower than "no operational teeth": add the pattern-repertoire concept,
  the bridge-first instinct, the Ecological Function/`Formation Ecology
  Connection` instruction (see finding B), and the worked-example
  requirement — still real, needed additions — but as an extension of an
  existing, working mechanism, not as if enforcement is being invented from
  nothing.
- **Part Eight (the validation probe battery)** — add a naturalness/register
  probe category. Confirmed directly: Part Eight has no such category
  today — that part of this finding was correct. But "naturalness" needs to
  be more than a probe category name; §8 below names the actual instruments
  this needs to run (readability_check, a term-reclarification count, the
  fabrication rate, a per-signal drift breakdown) — Part Eight's new
  category should point at those, not describe naturalness only in prose the
  way Part Five's own destination-statement already does without
  enforcement. This is still the actual "self-sufficient" fix — without it,
  the framework can restate its own good philosophy indefinitely while
  builds keep drifting from it unnoticed until someone runs a live
  conversation test months later.
- **Drift telemetry, made visible, not invented from nothing.** The Realness
  Study (§3) names three specific, measurable signals that degrade over a
  long conversation — response-length growth, declining initiative, and
  agreement-rate drift. **A real correction to how this was first framed:**
  two of the three already exist as declared signal types — `agreeing`
  (signal 3) and `over_producing` (signal 4, response length by name) —
  among `drift_detection`'s twenty (§4), not ten. Declining initiative has
  no existing equivalent and is the one genuinely new signal to add. The
  actual gap isn't missing signal types, it's visibility: nothing today
  captures *which* of the twenty signals fired in a form the verification
  harness can report (§8's per-signal breakdown) — that's the real
  instrumentation task, plus adding the one missing initiative signal.
- **New: a continuity-regression-testing step, required before any future
  voice-affecting prompt change reaches a built world — including this
  rebuild's own output before it ships.** The Realness Study's clearest
  governance lesson: personality is a versioned artifact, and a voice change
  that reads as objectively better can still break a returning participant's
  sense of who they were talking to. Same probes, old prompt vs. new prompt,
  diff the actual voice — before merge, not after a complaint. This is the
  concrete mechanism Objective 5's "self-sufficient" standard needs for
  voice specifically, the same way Part Eight's validation battery already
  exists for content.
- **New: adapt the Realness Study's 16-trait human-likeness rubric as a
  named validation instrument**, keeping the study's own caveat intact —
  some traits (informal grammar, typos) are excluded as incompatible with
  CiC's historical-fidelity and brand commitments. Fable's Research stage
  does the actual trait-by-trait adaptation; this brief only requires that
  it happen.

## 8. Verification — a real checkpoint, not a self-report

(This verifies the rebuilt voices themselves, once built — distinct from
§9's adversarial-review gates below, which verify the thread's own
research/design/blueprint documents at each stage, before the next stage
builds on them.)

**Every prediction this brief or its Research stage makes needs to be
falsifiable by an instrument actually named here.** A round-1 Opus
adversarial review of the draft that preceded this one
(`Ministry/Operations/Audits/CiC_VoiceRebuild_Brief_Opus_Adversarial_
Review_Round1_2026-08-06.md`) produced six per-world conversation-improvement
predictions as part of its own pass and found that none of them were
measurable by that draft's verification plan — two of them, in fact, would
have been actively mis-scored as improvements when they weren't. The fix is
naming real instruments, not more prose:
- **`readability_check` (`wrs/gates/core.py:211`)** — already built, already
  wired to Part Five's own numbers (`wrs/parameters.yaml:101-114`). Run it
  against baseline and rebuilt output for all six worlds; this is the
  instrument that actually tests Objective 3, which no metric named here
  tested before this revision.
- **The `fabrication_adjudication` rate**, counted, not eyeballed — already
  logged per-call (`log_llm_usage("fabrication_adjudication", ...)`,
  `nodes.py:2101`) and captured under that exact label by
  `mark_conversation_test.py`'s usage records. This is the actual instrument
  for Objective 4, one of the two parallel non-negotiable priorities named
  in §6, which had no metric at all before this revision — see finding
  (C)'s note on the pilot's Albina firing for why this isn't hypothetical.
- **`over_settling_logging`'s confirmed rate** (`app/over_settling_
  logging.py`), reported separately from the raw `over_settling_
  adjudication` firing count §4 already names as expensive-but-expected.
  The raw count measures how often the screen ran; the confirmed rate
  measures how often it was actually right. Report both, as two different
  numbers.
- **A per-signal drift breakdown**, built if it doesn't already exist as
  usable data. `drift_detection` currently reaches usage logs as one
  undifferentiated label — which of the twenty signals fired (including
  `FLATTENING` and `agreeing`/`over_producing`, §4's governance note and §7
  Part B) isn't captured today. Needs light instrumentation before it's a
  real metric — surfacing signals that already exist, not building new
  ones, except for the one genuinely missing initiative signal §7 Part B
  names.
- **A counted term-reclarification tally** — grep or classify transcript
  turns for the unprompted "when I said X a moment ago" pattern finding (C)
  is about, and report a rate. Nothing today produces this automatically.
- **A continuity-regression pass on all six voices**, per §7 Part B's new
  requirement — same probes run against the current, unrebuilt prompt and
  the rebuilt one, diffed directly, before this thread's output is treated
  as ready to ship, not only "does the rebuilt voice pass its own probes in
  isolation." **This is a verification activity, not a design one — it
  doesn't contradict §7 Part A's "no comparatives" principle.** The rebuild
  itself is built fresh from sources, never by editing the current prompt;
  this pass exists afterward, to catch whether the fresh build broke
  something a returning participant would notice, which is a different
  question from how the build was produced.

- Reuse `cic-poc/backend/scripts/mark_conversation_test.py` as the
  conversation-driving harness (real FastAPI backend, real Anthropic
  billing, full transcript + per-call usage capture) — already built and
  proven. **Its `SCENARIOS` list is currently hardcoded to the three
  baseline worlds only; extend it to cover Albina, Marius, and Theon before
  relying on it, not after.** This environment's network policy blocks
  huggingface.co, so the script's embeddings/cross-encoder are network-free
  lexical stand-ins — documented in the script itself; BM25 and every
  citation shown are real. If this thread runs somewhere with real network
  access, prefer the real embeddings model.
- **Live-test Albina, Marius, and Yausep as the primary acceptance
  evidence** — Yausep added per finding (D)'s correction: his baseline
  transcripts read substantively engaged but were never actually shown to
  be short, so he shouldn't be assumed safe as a "plain" regression world.
- Regression-check Papnoute and Chloe (transcripts referenced in the
  Decision Log entry in §3, **not currently committed to this repository** —
  only a session-scratchpad copy exists; commit a durable copy before this
  thread starts so Fable has real baseline data to diff against, not a
  description of it) — confirm nothing about them got worse, not that they
  "still read fine."
- **Theon gets live-tested too — not silently skipped.** He was in neither
  the original three baselines nor this brief's acceptance pair, and
  Alexandria carries the single largest share of lexicon chunks missing an
  Ecological Function field (5 of 11 project-wide, finding B) — the world
  most exposed to §7 Part A's lead-with-insight instruction silently
  no-op'ing.
- **A sustained-disagreement probe, run across multiple turns per world, not
  a single-turn tone check** — the actual instrument Objective 6 needs and
  didn't have before this revision: pressure a Representative toward
  agreement repeatedly across a conversation and confirm it holds its
  world's real position rather than softening by the third or fourth push.
- Run at minimum the confidence-under-thinness and **Sustained Engagement
  Testing** (Part Eight's actual name for the multi-turn-coherence
  category — corrected here) probe categories from the Framework's existing
  Part Eight methodology (`cic-validation-suite`) against the rebuilt
  worlds — a stronger, more auditable bar than a transcript read by eye
  alone.
- Before treating any finding in this brief as settled, verify it against
  the file/line cited, per §3's standing discipline — this brief's own
  round-1 Opus adversarial review found and corrected eight send-blocking
  errors in the draft that preceded this one; read it directly
  (`Ministry/Operations/Audits/CiC_VoiceRebuild_Brief_Opus_Adversarial_
  Review_Round1_2026-08-06.md`) for the full account of what changed and
  why, not just this revised text.

## 9. One thread, staged — research, design, blueprint, build, each gated by adversarial review

Unlike the prior system redesign (which deliberately split design and
blueprint across two separate weekly Fable passes), this brief's scope —
six voice files plus one framework document — is likely small enough to
carry through **research → design → blueprint → build in one thread**,
staged rather than split. Four stages, not three: this brief's own §5
diagnosis was shown mid-session to be incomplete in at least one place (the
worked-examples question in finding C), so Fable needs real room to extend
and verify the diagnosis before designing against it — not to "confirm" a
diagnosis this brief hands over as settled fact.

**What Fable is building, at every stage below: two tracks, not one.**
(1) A standardized mechanism — the shared `_HOW_YOU_ENGAGE` changes, and
whatever the Research stage concludes about worked-example form — applying
to all six worlds alike. (2) Individual adaptation — each world's own
per-file pass, keeping and sharpening what already makes it distinct
(Albina's periodic rhythm, Marius's entangled reasoning-mode, etc.) rather
than flattening toward a template. This brief tells Fable what to research,
design, blueprint, and build toward — never the specific per-world answer;
that's what the individual-adaptation track is for, and deciding it per
world, informed by the standardized track's findings, is Fable's call.

1. **Research — starting with the actual question, not just this brief's
   bug list, and not limited to what this brief already thought to ask.**
   Before any per-world work: what makes a conversation with a
   Representative genuinely good — engaging, clear, insightful, accurate and
   trustworthy not only in fact but in voice and feel, without becoming
   distracting? Ground this in the four studies named in §3, not from
   scratch — especially the Realness Study's persona-enactment and
   sustained-disagreement findings (now Objective 6) and the Persona
   Framework Survey's genuinely mixed evidence on worked examples (bearing
   directly on §7 Part A's worked-example plan). §5 below is real,
   verified, bug-level evidence about these six specific builds — treat it
   as supporting evidence for that larger question, not as the question
   itself. **Research owns identifying what else it needs, specific to
   Interview-mode conversation quality — this brief's own reading list and
   §5's diagnosis are the floor, not the ceiling.** If Research concludes
   there's a real, specific gap this brief hasn't named, say so plainly and
   go find it before Design starts, the same discipline that produced the
   four studies already cited. Then, specifically, extend and stress-test
   §5's diagnosis before
   treating any of it as ground to design on. At minimum: (a) check Mar Yausep against a
   FLAG-018-style probe first — he already carries a bridge-first
   instruction close to what this brief proposes project-wide and still
   shows the failure live, so he answers the prior question (does prose
   instruction work at all) more cheaply than Papnoute answers the narrower
   one (do worked examples specifically work); (b) only then run the
   Papnoute check; (c) confirm whether `readability_check` (§7 Part B) has
   ever actually been run against the six current builds — a fact this
   brief could not establish and must not be guessed at — and specifically
   against Albina's, given Objective 3's own unresolved tension: if she
   fails it, Design must explicitly decide (and record) whether her
   sentence length comes down or she's named a deliberate exception, not
   let the gate fail silently or go unrun; (d) treat the
   pilot's Albina `fabrication_adjudication` firing (finding C) as a real
   open interaction between Objectives 2 and 4, not a one-off. Live-test
   whatever the Research stage still finds underdetermined — don't inherit
   this brief's diagnosis uncritically, per §3's standing discipline.
2. **Design** — confirm or revise the shared-file approach and each
   per-world pattern against the (now Fable-verified, not just
   this-thread-verified) diagnosis and this brief's objectives (§6). Produce
   both tracks explicitly: the standardized mechanism, and a stated
   per-world adaptation approach for each of the six.
3. **Blueprint** — sequence the risk-ordered per-world passes (§7) with a
   real verification checkpoint after the pilot and after each subsequent
   world — not just a final pass at the end.
4. **Build** — execute in order, checkpointing as sequenced.

**Adversarial review gates every transition, per
`Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md`
— Opus tier, not Fable, per the model-tier policy that document itself
cites.** Research's findings get an adversarial pass before Design is
allowed to build on them; Design's output gets one before Blueprint
sequences it; Blueprint gets one before Build spends the expensive pass
executing it. Each pass uses the Standard Practice's actual discipline —
source-level verification against the cited file/line, not
plausibility-checking; P0/P1/P2 severity; cross-reference and completeness
checks counted, not eyeballed; read the prior gate's findings first; a
genuine "ready" or "not ready" verdict, not softened toward approval because
a deadline is close. Name the failure mode explicitly in each dispatch, per
the Standard Practice's point 5 — for this thread specifically: **this
brief itself already contained one claim (finding C's original "worked
examples are the fix") that sounded right and didn't survive being tested
live; assume the same risk is present in Research's and Design's own
findings until checked.**

**Mark's own review and approval gates every transition too, after the
adversarial pass, not instead of it.** Order matters: adversarial review
first, so factual and logical errors are caught before Mark spends time on
it; then Mark reviews the (already-cleaned) stage output directly and
approves before the next stage begins. Research doesn't hand off to Design,
Design doesn't hand off to Blueprint, and Blueprint doesn't hand off to
Build without both — an adversarial pass finding "ready" is a necessary
condition for moving on, not a sufficient one. This is the single most
important process fact in this brief, given Mark's own framing: "this is
the most critical rebuild we have done."

**Round 1 of this brief's own required Opus adversarial pass ran on
2026-08-06** (`Ministry/Operations/Audits/CiC_VoiceRebuild_Brief_Opus_
Adversarial_Review_Round1_2026-08-06.md`) — verdict: not ready, eight
send-blocking defects, all applied directly to this document (§1, §3, §4,
§5, §7, §8, and this section). Per the same project precedent that caught
new errors in the System Redesign brief's own round-3 fix pass (that
brief's docs 18→19), **a round 2 pass checking this fix itself is still
warranted before Friday** — a rewrite this size is exactly the kind of pass
most likely to introduce a new citation error while correcting the old
ones, and round 2 exists to catch that, not to re-litigate what round 1
already settled.

If partway through this genuinely doesn't fit in the available Fable budget,
say so plainly and stop at a clean boundary (e.g., after the pilot, or after
the two highest-risk worlds) rather than compressing quality to finish —
matching this project's own standing discipline of honest partial completion
over a rushed full one.
