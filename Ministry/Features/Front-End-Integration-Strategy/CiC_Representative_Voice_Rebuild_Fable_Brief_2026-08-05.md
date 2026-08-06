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
  not in this entry** (its own line 57 says so directly) — they were
  rendered as a claude.ai Artifact, not a repository file this thread can
  read. Treat the entry's own quotes and findings as the evidentiary record,
  not an "actual transcripts" claim this brief can't back up. That entry's
  own findings list (its lines 12 and 15) predates this brief's finding (A)
  and (C) corrections below and now carries a superseding note pointing
  here — read this brief's §5 for the current diagnosis, not that list.
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
  content-mapping), and `drift_detection`'s ten signals are all content- or
  posture-based, not register-based. One exception worth empirical
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
- **Lexicon chunks (118 total):** 109 of 118 carry an explicit `Ecological
  Function` field (9 missing — 5 in Alexandria/Theon's own set, 2 each in
  Syriac and PAHC); all 118 carry `Distortion Risk` (Modern Hearing vs.
  World Hearing). `Tier` is present in each file's own front matter but is
  discarded by the lexicon parser before serialization — it survives only as
  `doc.metadata["tier"]` (`app/rag/indexer.py:227`), reachable for sorting
  (§4's retrieval-ordering note) but never as text the model actually reads.
- **Story chunks (60 total):** all 60 carry the same instinct, but under a
  different name — `## Formation Ecology Connection`, not `Ecological
  Function`. None carry a `Distortion Risk` equivalent; no such field exists
  in the story-chunk format at all. Story `Tier` is different again: it sits
  as a plain header line, not inside a stripped front-matter block, so —
  unlike lexicon `Tier` — it does reach the model as text on every
  retrieval.

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
complaint — that part holds; full transcripts and cost data are in the
Decision Log entry named in §3. But measured mean sentence length from those
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

1. Every Representative opens from where the participant actually stands —
   a recognizable want, fear, or doubt — before reaching for the world's own
   vocabulary or imagery. Period flavor arrives once the bridge is built, not
   as the price of admission.
2. A substantive answer draws on what's genuinely insightful (Ecological
   Function, Distortion Risk) rather than whatever's topically nearest, and,
   when the question calls for it, is built in a defensible order: most sure
   first, genuinely distinctive second, honestly unsettled last and lightest
   — as **one option among a real repertoire of answer shapes**, not a new
   template replacing the old one. (Mark's own words: "we need to have
   several patterns so it doesn't just repeat the same thin process.")
3. Sentences read as plain, real, everyday spoken English — not costume
   diction — while keeping each world's genuine imagery, vocabulary, and
   actual distinctiveness as seasoning, not performance. Albina's periodic
   rhythm is the one deliberate, formation-accurate exception, kept
   substantively.
4. No fabrication rule moves, anywhere, under any framing.
5. The Construction Framework itself changes so that world #7 doesn't
   reintroduce this exact gap — "self-sufficient... as we have done all
   along," Mark's own words. This is not optional scope; it's the actual
   point of doing this on a dedicated thread instead of hand-patching six
   files.

## 7. The shape of the output — two parts, both required

### Part A — rebuild the six Representative voices

- **Pilot first, isolated.** Rewrite the shared `_HOW_YOU_ENGAGE` block
  (`representative_prompts.py:5-76`) — bridge-first entry; explicit
  instruction to lead with Ecological Function material (and its
  story-chunk equivalent, `Formation Ecology Connection` — see finding B,
  these are not the same field and need naming separately); the shape
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
  - Full diction/rhythm audit of both files — the elevated register runs
    through more than the paragraph explicitly labeled "how you speak"
    (confirmed by direct reading: identity, era, and vocabulary paragraphs
    carry the same stylization). Content, fabrication-guard, and
    witness-not-recruitment blocks untouched.
  - Reconcile the new shape repertoire against that world's *own* existing
    reasoning-mode paragraph — Marius's precedent-first chancery mode,
    Yausep's stage-by-stage demonstration, Theon's surface-then-depth
    unfolding, etc. Each may host the repertoire cleanly or need explicit
    adjustment; check per file, don't assume uniformity.
  - Add worked `{{random_user}}`-style example dialogues to the five files
    that lack them, in the *same* pass as the register edit — not a separate
    polish layer. **The exact form these examples take (positive-only, or
    paired with a contrastive/negative demonstration) is a Design-stage
    decision, made only after the Research stage resolves the open question
    in finding (C) — not prescribed here.**
  - Albina keeps her periodic/hypotactic rhythm substantively — genuine
    formation-accurate craft — but gets the same plain-vs-performed
    naturalness audit on surrounding diction as the other five.
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
  for Objective 4, the one non-negotiable objective in this brief, which had
  no metric at all before this revision — see finding (C)'s note on the
  pilot's Albina firing for why this isn't hypothetical.
- **`over_settling_logging`'s confirmed rate** (`app/over_settling_
  logging.py`), reported separately from the raw `over_settling_
  adjudication` firing count §4 already names as expensive-but-expected.
  The raw count measures how often the screen ran; the confirmed rate
  measures how often it was actually right. Report both, as two different
  numbers.
- **A per-signal drift breakdown**, built if it doesn't already exist as
  usable data. `drift_detection` currently reaches usage logs as one
  undifferentiated label — which of the ten signals fired (including
  `FLATTENING`, §4's one open governance question) isn't captured today.
  Needs light instrumentation before it's a real metric.
- **A counted term-reclarification tally** — grep or classify transcript
  turns for the unprompted "when I said X a moment ago" pattern finding (C)
  is about, and report a rate. Nothing today produces this automatically.

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
  Ecological Function field (5 of 9 project-wide, finding B) — the world
  most exposed to §7 Part A's lead-with-insight instruction silently
  no-op'ing.
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

1. **Research** — extend and stress-test §5's diagnosis before treating any
   of it as ground to design on. At minimum: (a) check Mar Yausep against a
   FLAG-018-style probe first — he already carries a bridge-first
   instruction close to what this brief proposes project-wide and still
   shows the failure live, so he answers the prior question (does prose
   instruction work at all) more cheaply than Papnoute answers the narrower
   one (do worked examples specifically work); (b) only then run the
   Papnoute check; (c) confirm whether `readability_check` (§7 Part B) has
   ever actually been run against the six current builds — a fact this
   brief could not establish and must not be guessed at; (d) treat the
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
