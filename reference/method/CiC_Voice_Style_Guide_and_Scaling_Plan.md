# CiC Atlas Prose — Voice & Style Guide, Review Process, and Scaling Plan

**Written 2026-09-08, from the Chloe / Scattered Households editorial pass
(commits `2b00a20d`..`35ab377a` on `claude/website-v2-sandbox`).**

Read this before touching any world's visitor-facing prose in
`cic-website/`. Everything below is derived from what was actually caught
and fixed in that pass, not from general advice about AI writing. Every
anti-pattern carries the real before → after from the diff that fixed it.

**Two companion documents this file draws on and points back to:**
`CiC_Prose_Craft_Analysis.md` (a sentence-by-sentence measurement of the
shipped Chloe text — sentence length, concreteness, term introduction,
hedging, verb choice) and `CiC_Marks_Voice_Analysis.md` (Mark's own actual
words extracted from the raw session transcript, not the polished output —
his correction patterns, and a direct check of what survives from his
input to shipped text). §1.1 below is this document's synthesis of both;
read the originals for the full evidence.

---

## What this document governs, and what it does not

This governs **visitor-facing Atlas prose**: the `tile`, `longDescription`
("The Story"), `legacy`, `voices`, `floorNote`, `why`, `sourcing`,
`sources`/`storySources`/`legacySources`, `experienceToday`,
`documentedStories`, and the matching copy on each `traditions/*.html`
page. This is third-person editorial prose *about* a movement, read by a
visitor deciding whether to sit down.

It does **not** govern the Representative's spoken voice. That has its own
anchor — `CiC_Register_Bar_2026-08-29.md` and the approved sample
`records/syr/demonstration/syr.demo.room-for-doubt.md` — which is first
person ("we/our/us"), 100–150 words a turn, and gated by
`gate_voice_perspective` in `engine/m1/gates.py`. Do not import rules from
one surface into the other. They meet at exactly one point, and it matters:
**an in-window voice has no standing to comment on anything after its own
window** (see anti-pattern 8).

### The governing constraint on this document itself

Mark's ruling of 2026-08-30, recorded in the Register Bar: *"i don't want a
series of rules for words... i want the base conditions to generate what we
are looking for in each world and throughout the system."* That document
holds a **no rules ledger** clause on purpose.

So this document is **not** a banned-word list, and it must never grow into
one. It holds two things:

1. **One exemplar** — the shipped `post-apostolic-house-church` entry in
   `cic-website/atlas-v3.html` (lines ~1119–1860). That entry *is* the bar.
   When something reads wrong, diff it against that entry, not against a
   rule in this file.
2. **The diagnosed failures behind that exemplar** — the specific things
   that were wrong before, so a future session recognises the same shape
   without rediscovering it. These are diagnostic aids for reading. They are
   not a checklist to apply mechanically to prose that does not have the
   problem.

---

## The baseline gap you are closing (measured, 2026-09-08)

Audited across all 292 entries in `atlas-v3.html`:

| Pattern | Entries affected | Notes |
|---|---|---|
| `voices` written as "Name — dash fragment" | **266 / 292** | The single most widespread pattern. Fixed only in pahc. |
| Sentence-initial "And" used as a dramatic beat in Story/Legacy | **123** | The `And both were killed for it` shape. |
| Verbless `Whether…`/`Who…`/`What…` fragment sentences in Story | **74** | The question-fragment list shape. |
| Absolutes (`routinely`, `constant`, `always`, `never`, `only`) in Story/Legacy | **112** | Needs case-by-case evidence scoping, not blanket softening. |
| `tile` on the "Place, dates — abstract descriptor" template | **6 of the 7 Built & Live** | Every Built & Live world except pahc. |
| Triple-negation absolutes (`no X, no Y, and no Z`) | 6 | The opener shape that was fixed first. |
| Stale `(disclosed on its tile)` pointer in `sourcing` | 2 (`syriac-edessa-nisibis`, `desert-monasticism`) | Same stale pointer removed from pahc in `35ab377a`. |
| `experienceToday` items possibly outside the world's own window | 9 | Same class as the Dura-Europos removal (`0373f37f`). |
| Multi-paragraph `longDescription` | **1** (pahc) | Render support exists and is backward compatible. |
| Per-section `storySources` / `legacySources` | **1** (pahc) | Helper `sectionSources()` exists and is generic. |

Two structural facts that shape everything in the Scaling section:

- **Only 7 of 292 worlds have a canonical record set.** `records/` holds
  `pahc`, `alx`, `syr`, `desert`, `cappadocian`, `ijc`, `hal` (plus `fix`
  fixture and `_fleet`). The other **285 entries have no `world_core`, no
  `cautions`, no `honest_limit`, no `contested_claim` to fact-check
  against.** For those, the strongest existing grounding is the `sources`
  array (present on 179) and `documentedStories` (545 stories across 278
  entries — and all 545 already carry `tier`, `verification`, `caveat` and
  `sources`, which is a real, usable floor).
- The `why` field template rollout in `68f67d2b` already covered all 7
  Built & Live worlds. That one is done.

---

# 1. Voice & Style Guide

## 1.1 The generative target: Mark's review instinct, not an external standard

Sections 1.2 onward are a diagnosed list of what got caught and fixed. This
section is what you're actually generating toward — derived from two
things, not from any outside comparison: a sentence-by-sentence
measurement of the shipped Chloe text (`CiC_Prose_Craft_Analysis.md`), and
a direct extraction of Mark's own words from this session's raw transcript,
separate from anything polished (`CiC_Marks_Voice_Analysis.md`). Read both
in full before drafting for a new world; what follows is their
distillation, not a replacement for them.

### The reframe that matters most

The instinct is to ask "how do I make this sound like Mark." That's the
wrong question. There is no clean evidence in this project's own
transcript of Mark drafting long-form prose himself — his unmediated
writing stays in short, typo-intact fragments throughout (4-24 words). The
two paragraph-length "drafts" that looked at first like his own long-form
writing turned out, on his own direct correction, to be **Gemini's**
output, pasted in as a second AI's take. What they still prove, once
correctly attributed, is more useful than what they seemed to prove at
first: Mark caught and removed the exact same class of flourish from
Gemini's draft that he catches from this assistant's — the same unhedged
certainty, the same em-dash fragment habit, the same performing sentence
(the Didache aside, cut with `yes the didache own story isn't about legacy
of influence`) — using the same vocabulary (`clunky`, `ai tells`, `dramatic
crap`) either time.

**His drafting voice isn't the thing to replicate, because there's no
clean sample of it at length. His review instinct is — and it's
model-agnostic: it catches the same defects regardless of which AI
produced the draft.**

What actually survived from his raw input to shipped text at high
fidelity, every time: his short sentences (one shipped with a single typo
fix and nothing else), and his own typed corrections applied on top of
someone else's draft — his or this assistant's. What got added and then
removed, every time, was material that appeared during *expansion* —
turning a 4-24 word instruction, or an AI's fluent paragraph, into a
shipped field. That is where every AI-tell in this session actually
originated.

So the actual target is: **write the short, plain, true version of the
idea first — expand it once, against the sources — then run the review
pass below before it ships.** Every word beyond what the sources establish
is a candidate for the exact defect this whole session existed to cut.

### The five-question review pass, built from how Mark actually caught things

The transcript shows a consistent shape to every correction he made
(`CiC_Marks_Voice_Analysis.md` §3). Before shipping anything, run these
five questions against it — they are not abstractions, they are literally
the axis of his corrections, on Claude's drafts and Gemini's alike:

1. **Is there a quantifier or modality word doing more work than the
   sources support?** *Only, no, always, never, occasional, both were
   executed.* This is the one class of problem he was always precise about
   naming, because it's a truth error wearing a style problem's clothes.
   ("held together *only* by" — the word is the whole defect. "*no* church
   buildings" → "no *documented* church buildings.")
2. **Did anything get added during expansion that isn't in the shortest
   true version of this idea?** If you can't point to the source sentence
   that put a given clause there, cut it. This is where "weary travelers,"
   "was not so fortunate," and an unrequested "right now" in the `why`
   field all came from. Highest-yield check available.
3. **Is the closing sentence of this paragraph doing more than stating the
   last fact?** The last sentence of a unit is the highest-risk position in
   the whole text — it's where a drafting pass, from any source, reaches
   for a beat, a flourish, a "gut-punch." Check it last, and check it
   hardest.
4. **Would this sentence survive being read back as a bare quotation?**
   Mark's entire correction vocabulary for prose problems (as opposed to
   truth problems) is one flat word applied to the quoted-back offending
   text — *clunky, to wordy, doesn't flow, feels to formal, ai cliche*. He
   never explains the mechanism for these; he reacts to the sentence in
   isolation. Read every sentence alone, out of its paragraph, the way he
   does, and ask if it survives.
5. **Is this trying to be clever, cryptic, or quotable?** Not just imagery
   — any sentence built to be striking rather than to state a fact. Real
   vividness from an actual primary-source quotation stays (Ignatius's own
   "wheat of God" line). Invented vividness goes, full stop, however good
   it sounds. ("Chloe is seated. The chair beside her has been pulled out
   the whole time" — cut for exactly this, in Mark's own words: "the ai
   criptic speaking we are getting rid of.")

### The mechanical shape that passes this review

Once a draft would survive the five questions above, it tends to already
have the measurable shape `CiC_Prose_Craft_Analysis.md` found in the
shipped text — this is a description of what surviving the review looks
like, not a separate style to aim for on top of it:

- Median sentence length around 18 words; one long sentence per paragraph,
  bought by a short one next to it.
- Every abstraction cashed into a name, number, object, or action in the
  same or next sentence — no floating claims.
- Technical and ancient terms never defined, only put to work; the plain
  word arrives first, the term attaches later to a person or action
  already performing it. Where a plain object can carry the idea (a shared
  table, the common loaf and cup), use it and skip the term.
- Real disagreement stated in parallel grammar and left open — not
  resolved, not smoothed — and the "both were real, and neither was
  settled" formula spent once, not reused as a tic.
- Documents as the grammatical subjects of active verbs (the letter
  *admits*, *never claims*; *no record says whose*) instead of the
  narrator hedging.
- Hedges carried on one word wherever possible (*documented, periodic,
  almost*); a whole clause only when a named source owns the uncertainty,
  and then the source is the clause's subject.
- Paragraphs open on an absence, a changed condition, or a named person —
  never a thesis statement.
- Repeat your own established phrases across the entry rather than
  reaching for a synonym.

Full detail and the evidence behind each of these: `CiC_Prose_Craft_Analysis.md` §1-9.

### What the National Geographic / BBC / Bible Project comparison actually was, and wasn't

Those names came up once as a reach for a register (accessible, honest
about real complexity, modern language for old material), and they're not
wrong as a description of the *effect*. But they are not the generative
source, and citing them risks importing a house style that isn't Mark's.
The actual mechanism that produces that effect — plain word before
technical term, concreteness cashed immediately, tension held instead of
resolved — is derived above directly from Mark's own catches and the
shipped text's own measured shape. If the result reads like good
documentary narration, that's confirmation the mechanics are right, not
the goal itself.

### The mistake this section exists to prevent: reviewing only the text you already suspect

The first pass at Alexandria (`alexandria-catechetical` / Theon) applied
the five-question review to every sentence flagged as a dash fragment or
an obvious defect — and shipped several real tells anyway, because they
lived in sentences nobody had flagged: a pre-existing "staggering body of
commentary" (unearned intensifier, sitting in text that predated this
whole review and so was never scrutinized); a `floorNote` whose own first
sentence ("Nothing in this tradition's confession diverges...") flatly
contradicted its second ("...formally condemned by a church council");
a `legacy` claim ("became the dominant Christian approach for over a
millennium, in the East and West alike") that overstated the record
against a known counter-tradition; and — the most instructive failure —
a brand-new tile rewrite, written specifically to *fix* a dash fragment,
that introduced a stacked, overloaded metaphor ("the text's surface as a
door onto a deeper meaning underneath") in the process of fixing the
thing it was sent in to fix.

**The rule this establishes: run the five-question pass, the truth pass,
and the internal-consistency pass on every sentence in the entry — not
just the ones that already look wrong, and not just the ones you just
wrote.** A sentence that predates this review has never been checked
against this bar. A sentence you just wrote to fix one defect is a fresh
opportunity to introduce a different one, and needs the same scrutiny as
the sentence it replaced, not less. Two failure modes to add to the
watch list explicitly:

- **Self-contradiction between adjacent sentences.** Not the same as an
  unhedged absolute in one sentence (§1.6) — this is two true-sounding
  claims next to each other that can't both be true as written. Read
  every paragraph as a single claim, not as a sequence of independent
  sentences, and ask whether sentence two is quietly reversing what
  sentence one asserted.
- **Stacked or mixed metaphor introduced while fixing something else.**
  Cutting a dash fragment or rewriting a fact doesn't exempt the new
  sentence from the imagery discipline — check what you just wrote with
  the same suspicion you'd apply to someone else's draft.

### The depth gap: passing the sentence-level bar is not the same as matching Chloe's

A second full round on Alexandria (after the self-contradiction fixes
above) still left it short of Chloe's own bar, even with every sentence
individually clean. A direct side-by-side comparison — read both
entries' corresponding fields together, not one after the other from
memory — found three specific structural shortfalls, none of them a
sentence-level tell. **Run this comparison, field by field against
Chloe's shipped entry, as its own explicit step, separate from and after
the five-question pass.** A world can pass every sentence-level check
and still be a shallower first draft than Chloe's, because Chloe's own
fields were shaped by dozens of rounds of Mark's own direct correction
and a new world's have not been.

The three specific gaps found, each now fixed as the standing bar:

1. **Story and Legacy rendering as a single undivided block instead of
   multiple paragraphs.** The render code splits both fields on `\n\n`
   generically — Chloe's Story is 3 paragraphs and Legacy is 3
   paragraphs; Alexandria's were each one dense block. Check: does the
   field actually contain `\n\n`, and does the panel show visible
   paragraph breaks? If a field is more than ~120 words and has none,
   that's a miss, not a stylistic choice — find the natural thematic
   seams (a new named figure, a shift from practice to tension, a shift
   from one legacy-dimension to another) and split there. No content
   change required, just structure.

2. **The tile doing two jobs where Chloe's does three.** Chloe's tile
   always covers: (a) the practice/identity — what this community
   actually did, in concrete terms; (b) a structural tension held open,
   not resolved (the bishop/elders split, an institution-vs-informal
   question, a contested title); (c) the cost of it — persecution,
   suspicion, loss of status, whatever this world's own record actually
   attests. Alexandria's tile originally had (a) and a version of (b)
   folded into it (the interpretive method) but no (b)-as-tension and no
   (c) at all, despite both existing elsewhere in the very same entry
   (the institution question in Story, real persecution in the
   documented stories and figure records). **Before shipping a tile,
   check it covers a genuine tension and a genuine cost, sourced from
   material already in the entry — don't invent new claims to fill the
   slots, surface what's already there.**

3. **Voices with no hedge and no absence.** Two of Chloe's five voices
   demonstrate holding a tension without resolving it (Ignatius's
   contested death, Polycarp's disputed title), and her fifth voice
   plays a specific structural role: every other entry puts a name in
   the subject position, and the fifth puts an *absence* there ("Most of
   these communities' hosts and householders are never named"). Check
   every world's `voices` array for both: at least one entry that hedges
   a claim by naming what a later or dissenting source actually says
   (not just a flat biographical fact), and one entry — it can be an
   addition, `voices` isn't fixed at five — that states a structural
   absence the world's own `world_core` thin_topics or ABSENT STORIES
   section already names. Alexandria's fix added exactly this: Pantaenus's
   entry now notes that Clement's famous teacher-tribute never actually
   names its subject (the identification is Eusebius's, not Clement's),
   and a sixth voice states that no ordinary believer's own words
   survive — both drawn from material already in `records/alx/`, not
   invented.

**The general form of the check, for any new world:** read the shipped
Chloe entry and the draft entry's corresponding field side by side, not
sequentially, and ask what JOB each of Chloe's sentences is doing that
the draft's corresponding field has no equivalent for. A missing job is
a depth gap even when every sentence present is individually clean.

### There is no canonical record for style purposes — everything gets reviewed, including quotes and record-verbatim text

Alexandria's tradition page carried a "Where we are quiet" paragraph
lifted verbatim from its own canonical honest_limit record
(`alx.limit.material-remains.md`). It was waved through in every pass
so far for exactly that reason — it's sourced, so it was assumed to be
fine. It wasn't: "If you dug where we met, we could not tell you what
you would find... Our own writings describe souls and books far more
than rooms and walls... The city itself has kept little" is an indirect,
hypothetical-address construction with a rhyme-y parallel built for
effect ("souls and books... rooms and walls") — cryptic in exactly the
way this whole guide exists to catch, sitting untouched inside a
verbatim quotation. Compare Chloe's own equivalent section, which states
the same *kind* of fact plainly: "So we can tell you they were here...
What we cannot give you is a single word any of them chose to write."
Same content, same source-based honesty, but one reads as trying to
sound like something and the other just says the thing.

**Mark's ruling on this, verbatim: "there is no canonical record, all
text needs to be reviewed and updated to this standard not just problem
texts... everything is reviewable and upgradable."** This closes a gap
the process had been quietly leaving open: `records/<code>/*.md` files
are the source of truth for FACTS (truth-check every claim against
them, per §2.1) but they are not automatically the standard for STYLE —
they were authored by an AI during the world-build process and have
never been run through this review themselves. A quotation, a
paraphrase, or a "this is sourced so it's fine" pass-through is not
exempt from the five-question review (§1.1) or the depth-gap check
above just because the words came from a record rather than from your
own drafting. Read every quoted or record-derived sentence the same way
you'd read your own.

**Scope boundary, settled by Mark: website copy only.** "Everything is
reviewable and upgradable" applies to this website's use of a record —
a quote, a paraphrase, a "sourced so it's fine" pass-through — not to
the canonical record files themselves (`records/<code>/*.md`). Those
files are the direct source for the Representative's live spoken
conversation (a different register, governed by
`CiC_Register_Bar_2026-08-29.md` and gated by `engine/m1/gates.py`, not
by this document — see "What this document governs, and what it does
not" at the top), with its own established review process (Doc_08
gates, probe batteries, the validation suite). Mark's ruling, verbatim:
"website copy only, don't touch the record files." Never edit a
canonical record file under this document's authorization — truth-check
against it, quote it, rewrite the website's rendering of it, but leave
the file itself alone. If a record's own text is bad enough that fixing
the website copy isn't enough, that's an escalation (§3.2), not a quiet
edit.

### Checks a single-world pass misses that only a same-day, side-by-side comparison against Chloe/Alexandria catches

Running the review process well on one world in isolation is not the same
guarantee as comparing its shipped output field-by-field against the
exemplars on the same day. Two worlds shipped by a separate thread working
through the remaining timeline (Syriac Edessa/Nisibis and Desert
Monasticism) each individually passed the sentence-level vocabulary scan —
no AI-tell vocabulary, no dash-fragments, real hedges, real absence-voices —
and still carried four defects a side-by-side comparison caught immediately:

1. **A previously-deleted pattern came back, identically worded, in both
   worlds.** Chloe's tradition page originally had a door-section teaser
   line under the final "Come and join us" heading; Mark had it cut
   sitewide as "exactly the ai criptic speaking we are getting rid of."
   Both Syriac's and Desert's door sections shipped with the identical
   sentence template restored (only the Representative's name changed:
   "[Name] is seated. The chair beside him has been pulled out the whole
   time."). A single-world review has no fixed reference point to catch a
   regression like this — only a check against the current state of the
   shipped exemplar does. **The door section is a heading and two action
   buttons, nothing else, permanently — check this explicitly, every
   world, don't rely on remembering it from an earlier fix.**

2. **The hypothetical-address construction recurs as a distinct
   cryptic-speak variant.** Alexandria's original "If you dug where we
   met, we could not tell you what you would find" was flagged as cryptic
   for addressing a hypothetical questioner rather than stating the fact
   plainly. Syriac's "Where we are quiet" section opened with "You ask
   what the women among us said of their own lives" — a different
   sentence, the same underlying move (a "you ask / if you..." framing
   device standing in for a direct statement). Add this as its own check:
   does any "Where we are quiet" or similar reflective section open by
   addressing a hypothetical visitor instead of stating the fact? If so,
   cut the framing and lead with the fact, the way Chloe's own version
   does ("Enslaved people were among us...").

3. **Phrase-level reuse across different fields of the same entry.**
   Syriac's `voices` entry for Jacob repeated an entire clause from
   `longDescription` almost verbatim ("...the record itself never closes
   the question"), and its `relationsSummary` repeated a full clause from
   `legacy` almost verbatim ("the channel through which Greek philosophy
   and medicine... into Arabic... back to Europe"). Compare this against
   Chloe's own exemplar: her `voices` entry for Ignatius covers the same
   underlying facts as her `longDescription` (marched to Rome under
   guard, died) but in different words, and adds something the other
   field doesn't have. Every field should do its own job in its own
   words — restating the same fact is fine; copying the sentence that
   states it is not. Check every entry's fields against each other, not
   just against the exemplar, for exact or near-exact phrase reuse.

4. **A wrong character can hide inside otherwise-clean prose.** Both
   worlds' "Where we are quiet" sections used a plain hyphen (` - `) for
   a mid-sentence aside where the rest of each page — and every other
   field in the same entry — uses an em dash (` — `). A vocabulary or
   AI-tell scan won't catch this; only a direct check of the actual
   character used will. Grep the finished page for ` - ` (hyphen with
   spaces) as a mechanical step before shipping.

None of these four are things the six-step process or the five-question
review would catch if run only against the world being drafted, in
isolation, from memory of what "good" looks like. They are things a fresh
read of the *current* shipped exemplar — not a summary of it, not a
memory of an earlier fix — catches immediately. **Before shipping a
world, re-read Chloe's and Alexandria's current shipped pages in full,
same day, and diff your draft against them field by field**, the way this
comparison was done for these two worlds after the fact. Don't rely on a
guide section describing a past fix to carry the fix forward — the guide
can drift out of sync with what's actually still true of the shipped
exemplars if a later, unrelated change touches them.

---

## 1.2 The exemplar, and the one test that generates the rest

Read the shipped pahc `longDescription`, `legacy`, `voices` and `tile`
before editing anything. Its properties, as shipped:

- **Full sentences everywhere.** No dash fragments, no verbless
  constructions, no headline-style appositives. Even the `voices` list —
  the field most tempted toward fragments — is five complete sentences or
  sentence pairs.
- **Every dramatic-sounding claim is either sourced or scoped.** "Justin
  was executed for refusing to abandon his Lord" is stated flatly because
  the trial transcript survives. "Tradition has it that Ignatius met the
  same end" is hedged in the same sentence because the corpus sits under a
  three-way authenticity dispute.
- **Disagreement is left visible, not resolved.** "Some communities were
  guided by a single bishop alongside elders and deacons, others by a
  circle of elders alone—both forms were real, and neither was settled."
- **Terminology, once chosen, is reused.** "Gospels and letters" appears in
  Story; Legacy says "the apostolic writings" and "the apostles' letters"
  for the same referent and never reaches for a fresh synonym.
- **The prose never claims more than the evidence base allows**, and says so
  in plain words when it is claiming less: "no *documented* church
  buildings," "came to be heard alongside," "no record says whose."

**The one test that generates all of it:** for each sentence, name the
source that makes it true, and name what the source does *not* establish.
If you cannot name the source, the sentence is a candidate for cutting. If
the source establishes less than the sentence says, the sentence is
overstated. Most of the fixes below are that test applied once.

---

## 1.3 Dash-fragment constructions

A name or noun, an em dash, then a descriptor phrase with no finite verb.
It reads like a museum label written by someone who did not want to commit
to a sentence. It is the highest-volume defect in the Atlas (266 entries).

**Fixed in `ca3e04a2` ("Rewrite Chloe's Voices bios: full sentences, fixed accuracy").**

> **Before:** `"Clement of Rome — wrote from the Roman church to the Corinthians around 96 to settle a dispute over deposed leaders, the earliest Christian letter outside the New Testament"`
>
> **After:** `"Clement of Rome wrote on behalf of the Roman church to the Corinthians around the year 96, addressing a dispute over deposed leaders. The letter is the earliest Christian writing outside the New Testament to survive."`

> **Before:** `"Justin Martyr — a philosopher who kept teaching Christianity as a school in Rome and left the earliest detailed description of Christian Sunday worship"`
>
> **After:** `"Justin Martyr was a philosopher who kept teaching Christianity as a school in Rome. He left the earliest detailed description of what their Sunday actually looked like."`

Note what the rewrite is *not*: it is not just inserting "was." Breaking
the fragment into two sentences forces each claim to stand on its own, and
that is what exposed the accuracy problems in the same field (see 1.7).
The dash was doing work — it was letting two unrelated claims sit next to
each other without either being tested.

**Still open across the Atlas:** `alexandria-catechetical`,
`syriac-edessa-nisibis` and 264 others. Example of what is still shipped:
`"Bardaisan of Edessa — philosopher, astrologer and hymn-writer at the Edessan court, whose cosmological teaching the later Syriac tradition rejected while keeping his poetic form"`.

The same shape appears in `tile`. **Fixed in `dc1646a7`:**

> **Before:** `"The house-churches of Antioch, Asia Minor, and Rome, 70 to 200 CE — the scattered gatherings that held together after the apostles were gone, connected by letters, formed around the table, still discerning who should lead and what the body's suffering truly means."`
>
> **After (final, `e65a3ad3`):** `"An uncommon faith in scattered households lived as one body, connected by letters and a shared table. Once the apostles were gone, some were led by a single bishop and elders, others by a council of elders. Following Jesus meant loss of status, suspicion from neighbors, and even outright persecution at times."`

The commit message names three separate problems in that one before-string:
"a uniform templated shape shared across every chair bio, reaching for
profundity, and a theological overstatement." All six remaining Built &
Live tiles still use that template, e.g.
`"Alexandria, c. 150 to 400 CE — a community of readers who received seekers into a life of accompanied reading, convinced that Scripture's surface is a door onto the Logos's own inexhaustible depth."`

---

## 1.4 Rule-of-three and triadic padding

Three items because three sounds complete, not because three real things
exist. The tell is that the three items are not the same *kind* of thing,
or that one of them is doing no work.

**Fixed in `3f8445e9` ("Fix Story opening paragraph: accuracy on buildings, leadership, scripture").** The opener was a triple negation:

> **Before:** `"the earliest Christian movement had no church buildings, no uniform clergy, and no settled list of Scriptures."`
>
> **After:** `"the earliest Christian movement had no documented church buildings and no single leadership structure. They had the Old Testament. The gospels and letters of the apostles moved between communities as copies were made and passed along, though no fixed collection had been settled yet."`

The commit message dismantles all three legs separately, and this is the
model for how to read a triad:

- Leg 1 overstated the evidence — we know there is no *documented*
  building, not that none existed.
- Leg 2 was **redundant**: "leadership plurality is already explained in
  full in the next paragraph… this sentence now just flags there was no
  single structure, without duplicating."
- Leg 3 was **factually wrong as scoped**: "'no settled list of Scriptures'
  could be misread as the Old Testament itself being unsettled. It wasn't."

So the triad was not a style problem that happened to have accuracy
consequences. It was three unexamined claims that the rhythm of three had
protected from examination. That is what makes triadic padding worth
hunting: **the cadence is where unchecked claims hide.**

Related, in the same commit: the fix also *added* something the triple
negation had crowded out — what they actually did have. A list of absences
with no corresponding presence is a rhetorical shape, not a description.

**Real triads are fine.** The shipped tile ends "loss of status, suspicion
from neighbors, and even outright persecution at times" — three genuinely
different pressures, in ascending severity, each attested. Leave those
alone.

---

## 1.5 Unearned emotional and dramatic adjectives

Words that ask the reader to feel something the source never established.

**Fixed in `3f8445e9`:**

> **Before:** `"these homes were held together by courier letters and weary travelers."`
>
> **After:** `"these household communities were held together by carried letters."`

The commit message: *"Replaced 'courier letters and weary travelers'
(redundant, and 'weary' an unearned emotional adjective) with 'carried
letters,' which already implies both."* Two defects in four words — a
sentimental adjective, and a doublet where one term already contains the
other. Note the fix *shortened* the sentence. Cutting is usually the right
move; reaching for a different adjective usually is not.

The gut-punch closer is the same family. **Fixed in `1956cb6b`:**

> **Before:** `"…wrote down what a Sunday gathering actually looked like. And both were killed for it."`
>
> **After:** `"Justin was executed for refusing to abandon his Lord; tradition has it that Ignatius met the same end."`

The before-version is a five-word sentence engineered to land. It is also
factually sloppier than the version that replaced it, because it asserts
both deaths at equal confidence. The dramatic shape and the factual error
are the same defect. 123 entries still open a sentence with "And" in this
register.

**The theological version of an unearned claim** is the most serious form,
and it is why the very first tile rewrite happened. `dc1646a7`:

> **Before:** `"…held together only by letters and a shared table…"`

The commit: *"a theological overstatement… which denied the tradition's own
claim that Christ/the Spirit — not correspondence — is what holds the body
one."* The word doing the damage is **"only."** "Held together by letters"
is a description of a mechanism; "held together *only* by letters" is a
claim about what does and does not constitute the church, and it is a claim
this project does not hold. **See 3.2 — this class escalates. Do not fix
it yourself.**

---

## 1.6 Hedge calibration: absolutes, and the difference between "no X" and "no documented X"

This is the highest-risk category for a religious-education product, and
it cuts both ways. Under-hedging fabricates certainty; over-hedging turns
attested substance into mush and is its own kind of dishonesty.

**Persecution language, revised three times across the session.** The
canonical constraint is `pahc.core.house-church`'s caution 4: *"legal
exposure was real, local, sporadic, and improvised — never constant,
systematic, or empire-wide in this window."*

| Commit | Text | Verdict |
|---|---|---|
| `dc1646a7` | "suspicion more than outright persecution, though real persecution came too, local and sporadic, not constant" | Accurate, but hedge-stacked into unreadability |
| `fb1827f8` | "Following Jesus meant loss of status, suspicion from neighbors, and even outright persecution at times" | **Shipped.** Mark's own plainer wording; same finding, said simply |
| `1956cb6b` (Story) | "periodic waves of official violence" | Shipped — "periodic" carries the sporadic finding without a hedge clause |

The lesson is not "add hedges." `fb1827f8`'s commit message: *"same real,
local, non-constant persecution finding from the tradition's world_core
record, said simply."* **The correct hedge is usually a better noun or
adverb, not an added clause.** "Periodic waves" does the work that "real,
local, and sporadic — never constant" was doing in four times the words.

**Evidence-scope hedging: the "documented" move.** From `3f8445e9`:

> **Before:** `"had no church buildings"`
>
> **After:** `"had no documented church buildings"`

Commit: *"We only know there's no *documented* evidence of church buildings
in this window, not that none existed."* This is the single
highest-leverage one-word fix available across the Atlas. Any "no X"
absolute about a period with a thin material record should be tested
against it.

The same discipline appears in `ca3e04a2`, applied to a silence:

> **Before:** `"…are unnamed in the record — the gatherings met in the homes of people history did not bother to write down"`
>
> **After:** `"…are never named in the record. The gatherings met in their homes, but no record says whose."`

"History did not bother to write down" is a claim about the intentions of
the transmission process — unknowable, and faintly editorial. "No record
says whose" is a claim about the surviving record, which is exactly what we
can check. **Prefer statements about what the record does or does not say
over statements about what happened or did not happen.**

---

## 1.7 Anachronism

Two distinct failures, both fixed this session.

**(a) A term that names something that did not yet exist.** Fixed in
`110550cd`:

> **Before:** `"…along with the offices of bishop, presbyter and deacon…"` / `"…until they became Scripture by use rather than by ruling."`
>
> **After:** `"The roles of bishop, presbyter, and deacon were already named in the apostolic writings…"` / `"…it was through this regular use in worship—not by an early decree—that these writings came to be heard alongside the ancient Jewish Scriptures."`

The commit names it precisely: *"fixes an anachronism (the offices were
named in 'the gospels and letters,' not 'Scripture' — this window
explicitly had no settled canon, per the Story text's own claim)."* Note
the internal-consistency argument: the Story section had *already* said no
fixed collection was settled. Legacy contradicted its own entry. That is
the cheapest anachronism check available — **read the entry's other fields
before trusting a term in this one.**

Two other entries currently use "Scripture(s)" for a window ending at or
before 250 CE: `post-apostolic-house-church` (now correctly, of the Old
Testament and of the Jewish Scriptures) and `tertullian-s-voice` (unchecked).

**(b) A voice or a section reaching outside its own window.** Fixed in
`0373f37f` — the whole `experienceToday` block was deleted, not caveated:

> **Removed:** `"The Dura-Europos house-church, Syria — an ordinary home converted for worship between about 233 and 256, the earliest identified Christian church building…"` plus the Yale baptistery paintings.

The reasoning is worth quoting in full because it is the general rule:

> *"That site falls after this world's own c. 200 close, and the project's
> own canonical record for this world (`pahc.limit.material-remains.md`)…
> is explicit that no building, burial, or inscription survives from this
> world's actual 70-200 CE window anywhere… presenting it as something a
> participant can go see 'today' for this world implies it belongs to
> Chloe's own era, which it doesn't, and which this world's own voice can't
> legitimately comment on either way (an in-window voice has no standing to
> say what does or doesn't belong to a 'later world' it hasn't lived to
> see)."*

And the deletion form matters: *"Removed the field entirely rather than
leaving an empty array, matching how every other entry without this data
omits the key."*

9 entries currently have `experienceToday` items dating well after their
own window. **Not all are wrong** — `syriac-edessa-nisibis` pointing at Mor
Gabriel (founded 397, world closes 410) is fine; a still-living tradition
pointing at a modern building is fine. The test is whether the item is
offered as *this world's own* material. Check each one; do not batch-delete.

---

## 1.8 Contested and single-source claims stated as settled

The project's records already hold these as first-class objects —
`records/<code>/contested_claim/*.md`. When one exists, the prose must
carry it. Two were carried into shipped prose this session.

**Ignatius's execution.** `pahc.contested.ignatius-dating` records a
genuine three-way split (traditional c. 107–117 / redated 130s–140s /
pseudepigraphic c. 160–180), and `pahc.core.house-church` caution 1 calls
this "THE IGNATIUS CONCENTRATION… Never presented as settled if pressed."

In Story (`1956cb6b`), the two deaths are now weighted differently in one
sentence: *"Justin was executed for refusing to abandon his Lord; tradition
has it that Ignatius met the same end."*

In Voices (`ca3e04a2`), the same claim is hedged by naming the actual
evidentiary situation rather than by adding a hedge word:

> **Before:** `"Ignatius of Antioch — bishop who wrote seven letters to congregations while being marched to his execution in Rome, c. 107-117"`
>
> **After:** `"Ignatius, bishop of Antioch, wrote seven letters to congregations while he was marched toward Rome under armed guard, c. 107-117. Polycarp's own letter later speaks of him as already dead, though it admits not knowing the details of what happened."`

Note the technique: the before-version asserts the execution as a
subordinate clause, which is where unexamined claims live. The after-version
promotes the evidence itself into the text. **The best hedge is often to
say what the source says instead of what you concluded from it.**

**Polycarp's title, and a dropped unsourced claim.** Same commit:

> **Before:** `"Polycarp of Smyrna — bishop who had known the apostolic generation, put to death at Smyrna around 155, his death recorded by his own congregation"`
>
> **After:** `"Polycarp of Smyrna was addressed as bishop by Ignatius, though his own letter never claims the title, opening only as 'Polycarp, and the presbyters with him.' He was put to death at Smyrna around 155; his own congregation recorded his death."`

Commit: *"drops the unsourced 'knew the apostolic generation' claim and
states the real, documented tension instead."* The tension it states is
exactly the one `pahc.contested.two-strand-packaging` flags in its
`held_against`: *"Polycarp himself is addressed as bishop by Ignatius while
identifying himself, in his own letter, only alongside 'the presbyters.'"*
The prose is carrying the record's own contested-claim content. **That is
what "grounded" means operationally: the record's flagged tension appears in
the visitor-facing text.**

**Overstated origination.** `110550cd` names this as a recurring class:
*"corrects the same class of overstatement already fixed once in the Story
text (crediting bishop/presbyter/deacon as if invented here, when Scripture
already named the offices and this era's real contribution was the
practical, everyday struggle to live them out)."* The pattern to watch:
prose about an early movement drifting into *this is where X was invented*
when the honest claim is *this is where X was first worked out in practice*.

---

## 1.9 Terminology drift within a single entry

Once a phrase is established, reuse it. Do not introduce a synonym to avoid
repetition — in this genre, a fresh synonym reads as a fresh claim.

- `3f8445e9`: `"homes"` → `"household communities"`, explicitly *"to match
  the Scattered Households naming already used throughout."*
- `0250f13b`: a leftover `"house churches"` inside the Shepherd of Hermas
  source note → `"Scattered Households"`.
- `1956cb6b` / `110550cd`: "gospels and letters" (Story) is carried into
  Legacy as "the apostolic writings" / "the apostles' letters" — different
  words, but deliberately the same register and the same referent, never a
  new concept.
- `2b00a20d` records the boundary of a rename: every reference to *other*
  movements' house churches (Chinese house churches, the Lausanne
  Congress, a cited book title) was deliberately **not** changed, because
  those are accurate general usage, not this tradition's name. A rename is
  a scoped operation, not a find-and-replace.

## 1.10 Stale cross-references

`35ab377a` removed `"(disclosed on its tile)"` from pahc's `sourcing` field:
the tile had been rewritten four times and no longer disclosed anything
about thin interior voice, so the parenthetical pointed at content that had
stopped existing. The substantive claim was kept; only the false pointer
went.

**Two entries still carry the identical stale pointer**:
`syriac-edessa-nisibis` (`"Rich formal/doctrinal, thinner personal texture (disclosed on its tile)"` — its tile discloses no such thing) and
`desert-monasticism`. Whenever you rewrite a `tile`, grep the entry's other
fields for pointers into it.

## 1.11 Register: status announcements vs. someone talking

`68f67d2b` rewrote the `why` field template across all 7 Built & Live worlds:

> **Before:** `"This tradition has been fully built and is open for conversation now — Chloe is its voice at the table."`
>
> **After:** `"This Christian tradition is fully built, and you can have a conversation with Chloe, a household leader, right now."`

Commit: *"read like a status announcement rather than a person talking,
especially next to the plain, direct voice used in every other tradition's
own why field on this same map."* The diagnostic there is worth keeping:
the standard was found **in the Atlas's own neighbouring entries**, not
imported. It also swapped generic "talk" for the project's own
"conversation" language.

Related, `49129e64` cut a line from the tradition page:

> **Removed:** `"Chloe is seated. The chair beside her has been pulled out the whole time."`

Commit: *"too cryptic/writerly, matches the pattern of AI-sounding lines
being cut sitewide."* Atmospheric second-person-adjacent lines that gesture
at meaning without saying anything go.

## 1.12 Questions must match what the source is actually about

`49129e64`, on the tradition page's question list — this is the same
accuracy discipline applied to interrogatives:

> **Before:** `"How did your community handle wrongdoing among its own?"` (cited to *1 Clement* 1, 44, 47)
>
> **After:** `"How did you decide who should lead once the apostles were gone?"` (cited to Ignatius's letters; *1 Clement* 42, 44)

Commit: *"1 Clement is about a leadership dispute and succession, not
generic wrongdoing."*

> **Before:** `"What did a woman's life and role look like among your people?"`
>
> **After:** `"What did women's leadership look like among your people?"`

Commit: *"Pliny and Hermas attest functional roles — deaconesses, Grapte
instructing widows and orphans — not general 'life.'"* This tracks
`pahc.limit.womens-own-words` exactly, whose own note says the statement is
*"deliberately narrower than 'women are thin here': presence, office, and
memory are attested substance; the limit is authorship alone."* A question
must not be broader than its citation.

---

# 2. Review Process

The order below is not a suggestion. It is what the commit sequence
actually did, and several fixes were only findable in that order.

## 2.1 Truth pass before style pass — always

`3f8445e9` came *after* `1956cb6b` shipped the "finalized" Story. The
opening paragraph had been style-fixed and shipped, and only then did a
dedicated accuracy read find three overstatements in its first sentence.
Meanwhile `110550cd`'s commit message says the Legacy fix corrects *"the
same class of overstatement already fixed once in the Story text"* — the
same defect class had to be caught twice because the second field was
edited for flow before it was checked for truth.

**Run in this order, per world:**

1. **Truth pass.** Read the world's `records/<code>/` set first, in this
   order: `world_core` (`horizon`, `formation_logic`, `thinness`,
   `cautions`, `thin_topics`) → every `contested_claim` → every
   `honest_limit` → `voice_craft` → the `figure` records for anyone named
   in the prose. Then read the entry's existing prose and mark every claim
   against them. Where a claim rests on a primary text, open the text —
   `0250f13b` caught a real misattribution only by doing this (see 2.3).
2. **Internal-consistency pass.** Read all of the entry's own fields
   together. Story vs. Legacy contradicted each other on the canon
   (`110550cd`); `sourcing` pointed at a `tile` that no longer said it
   (`35ab377a`); Voices asserted an execution that Story hedged
   (`ca3e04a2`). None of these are findable field-by-field.
3. **Style pass.** Only now. Sections 1.2–1.4 and 1.8–1.11.
4. **Source-array reconciliation.** Every work the new prose names must
   have a row in `sources`. `110550cd` added Polycarp's *Epistle to the
   Philippians* precisely because *"the Legacy text credits his own writing
   by name."* `0250f13b` added Pliny 10.96 because it was cited on the
   tradition page but missing from the Atlas list.
5. **Sync pass** (2.4).
6. **Render verification** (2.5).

## 2.2 Never ship a fragment of a unit

Fifteen commits, but each one ships a **complete approved unit** — a whole
tile, a whole three-paragraph Story, a whole Voices array. The iteration
visible in `dc1646a7` → `fb1827f8` → `6dfc39c3` → `e65a3ad3` is four
complete versions of one tile, not four sentences appended to a growing
draft.

Two consequences worth copying:

- **A word swap gets its own commit** when it changes meaning.
  `6dfc39c3` is one word — "staying one body" → "living as one body" — and
  nothing else. Reviewability beats commit economy here.
- **Known-broken is recorded, not quietly carried.** `dc1646a7` shipped
  with an explicit *"Known display issue, not yet fixed"* section about the
  homepage card's 3-line clamp truncating the new text. `fb1827f8` then
  reported that the attempted fix *did not work* and re-stated the three
  remaining options. Nothing was claimed as fixed that was not fixed.

## 2.3 Verify against the primary text, not against your memory of it

`0250f13b` is the clearest single argument for this document existing.
The Atlas had attributed the vivid "rented room above a bathhouse" detail
to Justin's *First Apology*. It is not there. It is in *The Martyrdom of
Justin and Companions* — his trial transcript before the prefect Rusticus.
A plausible, well-known, frequently-repeated attribution, wrong, shipped,
and caught only by opening the text.

`1956cb6b` states the same discipline as policy: *"Every factual claim
re-verified against primary sources directly (Ignatius's 'ten leopards' in
his own Letter to the Romans; Justin's exchange with the prefect Rusticus
on living and teaching above a bath; the actual content of his First
Apology 65-67)."* The repo has vendored texts under `cic/texts/` and
`records/<code>/search_record/*.md` documents which volumes were swept —
use them.

## 2.4 Sync every location, and know the list before you start

Chloe's tile lives in **four** files: `atlas-v3.html`, `data/world-census.json`,
`index.html`, `traditions/post-apostolic-house-church.html` — and within
the tradition page, in **two** places (the tile and the figcaption).
`table.html` carries a separate short roster description. `e65a3ad3` names
"all five locations."

Rules that held all session:

- `atlas-v3.html` is the copy that renders. `data/world-census.json`'s
  duplicate is **not currently rendered anywhere** and was still updated
  every single time — *"kept in sync to avoid future drift."* Do not skip it.
- Both JSON payloads must still parse after every edit. Verified every commit.
- A rename is scoped deliberately. `2b00a20d` changed only visitor-facing
  surfaces and explicitly left the internal id (`post-apostolic-house-church`,
  `pahc`) alone because it is *"a live registry key in `records/worlds.yaml`
  used across 160+ engine/records files — renaming that is a
  conversation-engine migration, not a website wording change."*

## 2.5 Headless-browser verification before every commit

The standard that was actually met, from `110550cd`: *"3 paragraphs render
correctly under 'Legacy', both new per-section accordions render with the
right content, zero console errors and zero overflow at
320/390/1280/1440px in both themes, both JSON files remain valid, all local
links resolve."*

The checklist, generalised:

- The expected DOM actually appears (e.g. *"exactly 3 `<p>` elements render
  under 'The Story'"* — count, do not eyeball).
- Zero console errors.
- Zero horizontal overflow at **320 / 390 / 1280 / 1440** px.
- **Both themes.**
- Every interactive element clicked: `508e5bd2` verified the accordion
  toggles; `25213aa9` verified 1-, 2- and 3-story cards, hover tooltips,
  keyboard focus, multiple simultaneously open.
- All local links resolve; both JSON files valid.
- `fb1827f8` used a screenshot to *disprove* an assumed fix. Verification
  is allowed to return bad news; that is its job.

## 2.6 Render-code changes are content decisions

Three of the fifteen commits changed rendering to let honest content exist,
each generically and backward-compatibly:

- `1956cb6b`: `longDescription` split on `\n\n` into multiple `<p>` —
  *"collapsing it to one wall of text would undercut the whole point of
  this editing pass. Backward compatible — every other entry's
  single-paragraph text renders identically to before."*
- `110550cd`: a generic `sectionSources(list)` helper for per-section
  `Sources` disclosures, deliberately *flat* — *"a flat list of relevant
  works, not mapped to individual sentences"* — per Mark's explicit
  instruction, and reusing the existing `.docstories` CSS rather than
  inventing a visual pattern.
- `68f67d2b`: a second "Interview" button at the foot of the panel, plus a
  real bug fix (`querySelector` → `querySelectorAll`, so both buttons work).

`508e5bd2` shows the counter-discipline: a UI change that *"applies
site-wide across all 292 Atlas entries, since this is a UI consistency fix,
not content specific to any one tradition."* Know which kind you are making.

---

# 3. Escalation Criteria

The line, in one sentence:

> **If the world's own canonical records already decide it, fix it. If the
> fix decides something the records leave open — or changes what the
> project claims theologically or historically — escalate it.**

That line is not invented here. It is the repo's existing FLAG discipline:
*"Defects → `FLAGS.md`, never silently patched. Upstream wording problems
are referred, not rewritten (the FLAG-029 discipline)"*
(`CiC_Record_Native_World_Build_Process_V1.5.md`). And
`pahc.craft.chloe-voice.md` shows it in use inside a record: a Grapte
attribution was corrected against the vendored text, while the fact that
the *upstream approved decision document* is now wrong was **"FLAGGED, not
resolved here… the project lead's own call, not this build thread's —
carried forward to the closing summary rather than silently edited."**

## 3.1 Fix it yourself — no question to Mark

Each of these was done unilaterally this session, and each is verifiable
against something that already exists.

| Class | Real instance |
|---|---|
| **Source misattribution**, checkable against the text | Bathhouse detail moved from *First Apology* to *Martyrdom of Justin* (`0250f13b`) |
| **Missing source row** for a work the prose already names | Polycarp's *Epistle to the Philippians* added (`110550cd`); Pliny 10.96 added (`0250f13b`) |
| **Dash fragment → full sentence** (form only, meaning unchanged) | All five Voices bios (`ca3e04a2`) |
| **Cutting an unearned adjective or a redundant doublet** | "courier letters and weary travelers" → "carried letters" (`3f8445e9`) |
| **Cutting a cryptic/writerly atmospheric line** | The pulled-out-chair line (`49129e64`) |
| **`no X` → `no documented X`** where the record states the record is silent | "no documented church buildings" (`3f8445e9`) |
| **Removing a stale cross-reference** to content that no longer exists | "(disclosed on its tile)" (`35ab377a`) |
| **Terminology sync** to a name already established in the entry | "homes" → "household communities"; "house churches" → "Scattered Households" (`3f8445e9`, `0250f13b`) |
| **Deleting out-of-window material a canonical `honest_limit` already excludes by name** | Dura-Europos, named in `pahc.limit.material-remains` (`0373f37f`) |
| **Deduplicating a claim already made in full elsewhere in the entry** | Leadership plurality removed from the opener (`3f8445e9`) |
| **Narrowing a question to what its own citation supports** | "wrongdoing" → "who should lead" (`49129e64`) |
| **Render/CSS/wiring**, backward compatible | Paragraph support, `sectionSources()`, `querySelectorAll` fix |
| **Sync + verification** | All of 2.4 and 2.5 |

The unifying property: **a document in the repo already settles it.** The
Dura-Europos deletion looks like a big editorial call, and it is not — a
canonical record names that exact site as outside the window. That is what
made it mechanical.

## 3.2 Escalate — a real question, and do not guess

These are the ones that actually consumed Mark's attention this session.
They are distinct kinds of hard, and naming the kind helps him answer fast.

**(A) Theological characterisation — what is claimed to be doing the work.**
*"Held together **only** by letters and a shared table"* (`dc1646a7`).
Deleting "only" is trivial; deciding that the sentence as written *"denied
the tradition's own claim that Christ/the Spirit — not correspondence — is
what holds the body one"* is a doctrinal judgment. Any sentence that
implicitly answers *what makes the church the church*, *what saves*, *what
holds it together*, or *what the sacrament is* is in this class, however
casually it is phrased.

**(B) Compressing a flagged provisional interpretive frame into lay prose.**
The bishop/elders split. `pahc.core.house-church` caution 2 says *"both
authority patterns held, neither wrong, the disagreement visible — never
monepiscopacy-as-settled… the two-strand packaging itself is a provisional
interpretive frame, not a found fact."* And
`pahc.contested.two-strand-packaging` concedes the frame is *"this build's
own working interpretive packaging… No primary voice in this world's
evidentiary base uses 'Strand A'/'Strand B' language."* Rendering that as
one sentence a visitor reads in three seconds took four tile versions
(`dc1646a7` → `e65a3ad3`) plus a Story rewrite. **When a record says its
own frame is provisional, any compression of it is Mark's call.**

**(C) Evidentiary-weight calls across a live scholarly dispute.** Whether
Ignatius's execution is stated, hedged, or attributed — and whether Justin's
is treated differently in the same sentence. `pahc.contested.ignatius-dating`
records a three-way split and explicitly *"does not attempt to adjudicate
between them."* The record tells you a dispute exists; it does not tell you
how much hedge belongs in a 40-word visitor paragraph. That calibration is
the judgment.

**(D) The boundary of a silence — what an absence licenses saying.** The
women's-leadership wording. `pahc.limit.womens-own-words` insists presence
and office are *attested substance* and the limit is *authorship alone*.
Get that boundary wrong in either direction and you either erase attested
women or invent testimony. Same for enslaved members
(`pahc.limit.enslaved-voices`) and the ordinary majority
(`pahc.limit.ordinary-majority`).

**(E) Naming and identity.** The rename itself (`2b00a20d`) — explicitly
*"an editorial clarity choice, not a sourcing correction,"* and the commit
says so because that distinction is Mark's to make. Display names,
Representative names and role labels, and anything a visitor would read as
the movement's own name for itself.

**(F) Fleet-wide template and register decisions.** The `why` rewrite
(`68f67d2b`) changed 7 worlds at once. Any change to a shared template,
or any pattern applied across many entries, is a fleet decision even when
each instance looks small.

**(G) Upstream documents this pass proves wrong.** Not a prose question at
all, and the most easily lost. The `pahc.craft.chloe-voice` case: an
approved upstream decision document states a rationale the vendored text
does not support. **Never silently correct an approved upstream document
from a prose session. Flag it and carry it forward.**

**(H) Anything you cannot source and cannot cut.** If a claim is load-bearing
for the paragraph, you cannot verify it, and removing it would leave the
prose misleading — that is a question, not a judgment call. `ca3e04a2`
resolved one of these by cutting ("knew the apostolic generation" went) —
which is the right default. When cutting is not available, escalate.

## 3.3 The three tests that separate the two lists

1. **Can I point at the file and line that decides this?** Yes → fix it.
   No → candidate for escalation.
2. **Does my fix change what the project claims, or only how it reads?**
   Only how it reads → fix it. What it claims → escalate.
3. **Would this fix be wrong if a plausible alternative scholarly position
   is right?** If yes → escalate, and say which position.

---

# 4. Scaling Architecture Recommendation

## 4.0 The fact that determines the answer

**285 of the 292 entries have no canonical record set.** Only `pahc`, `alx`,
`syr`, `desert`, `cappadocian`, `ijc`, `hal` exist under `records/`. Every
verification step that actually caught something this session ran against
those files — the Dura-Europos deletion, the persecution calibration, the
two-strand wording, the women's-leadership scoping, the Ignatius hedge.

For 285 entries **that check cannot run at all.** Any architecture that
treats the Chloe pass as a template to fan out across 290 worlds is
proposing to do a truth pass with nothing to check against, which produces
confident, fluent, unverifiable prose — the precise failure mode this
product cannot absorb.

So the work is two different jobs and must be planned as two:

- **Job 1 — 7 record-backed worlds.** Edit existing prose against an
  existing canonical record set. Bounded, verifiable, no discovery. This is
  the Chloe pass, six more times.
- **Job 2 — 285 record-less worlds.** There is no source of truth. What
  exists is a `sources` array (179 entries) and `documentedStories` (545
  stories, **all** carrying `tier`, `verification`, `caveat` and `sources` —
  a real floor). Job 2's first move is not editing. It is establishing a
  per-world source floor, or else deliberately restricting the pass to
  **reduction only** — cutting AI-cliché form and unsupported claims,
  adding nothing.

## 4.1 Options compared

**Option A — Documented contract + checklist driving per-world Claude Code
sessions, batched escalation.** One world per session, this document plus
the shipped pahc entry as the contract, the 6-step sequence from §2, one
consolidated flag document per batch.
*For:* the session has filesystem and browser access, so the two checks
that actually caught errors — opening the primary text, and headless render
verification — are available. Escalations batch naturally. Reuses the
project's existing FLAG discipline. No new infrastructure.
*Against:* human-paced. ~292 sessions at Chloe's intensity is a lot of
sessions, though most worlds need far less than Chloe did.

**Option B — Scripted pipeline on the Claude API with a self-critique pass.**
Per-world script: load records + entry → generate revised fields →
self-critique → emit.
*For:* fastest, cheapest per world, uniform.
*Against:* fatal for the truth pass. A self-critique pass cannot open
`cic/texts/`, cannot check the `sources` array against the prose, cannot
run Playwright, and cannot notice that a beloved detail belongs to a
different document. The *First Apology* misattribution would have survived
this pipeline — self-critique confirms plausibility, and the wrong
attribution was highly plausible. It also concentrates risk: an
unsupervised generator produces **uniform** defects. The repo has this
measured — 250 voice-perspective violations across all 8 built worlds'
spoken fields, *"concentrated in the lexicon… authored as a Fable
subagent's Doc_03/Doc_06 pass — a systematic authoring pattern, not
scattered error"* — invisible until a mechanical gate was written for it
(`gate_voice_perspective`, 2026-09-04). Reviews had not caught it.

**Option C — Multi-agent fan-out: N drafting agents, separate fact-check
agent.**
*For:* right shape *within* one world, and it is already the project's
pinned policy (§4.3).
*Against:* wrong as the top-level structure, for exactly the §4.0 reason —
for 285 worlds the fact-check agent has no corpus to check against, so
fan-out multiplies unverifiable output. It also loses the cross-field
internal-consistency pass (2.2), which needs one reader holding the whole
entry: Story-vs-Legacy on the canon, `sourcing`-vs-`tile`, Voices-vs-Story
on Ignatius were each found by *one* reader seeing all fields at once.

## 4.2 Recommendation

**Option A as the top-level structure, with Option C's fan-out used inside
a single world session, and mechanical linters extracted from Option B's
one genuinely good idea.**

Concretely:

1. **Write the mechanical linter first, before any batch runs.** One script
   over `atlas-v3.html` + `world-census.json`, no model calls, reporting per
   entry: dash-fragment `voices`; sentence-initial "And" in Story/Legacy;
   verbless `Whether/Who/What` fragments; `no X, no Y, and no Z`; unhedged
   `no <noun>` absolutes; `(disclosed on its tile)` and other cross-field
   pointers whose target no longer contains the claim; works named in prose
   with no row in `sources`; `experienceToday` items dated beyond the
   world's `end`; drift between the four tile locations; both JSON payloads
   parse. This is the 250-instance lesson applied prospectively: **whatever
   model drafts, the check for each register property must exist before the
   batch, not after.** It also converts most of §1 into triage, so a session
   spends its attention on judgment rather than detection.

2. **Batch order by risk and by whether verification is even possible.**
   - **Batch 1 (6 worlds): the remaining Built & Live.** `alx`, `syr`,
     `desert`, `cappadocian`, `ijc`, `hal`. Full §2 pass. These are the only
     other worlds where the truth pass can run properly, and the only ones a
     visitor can actually converse with. Highest value per world by a wide
     margin. Two of them additionally carry the known stale-pointer defect.
   - **Batch 2 (19 + 28 entries): "Possible Future World (on record)" and
     "Floor Question (register)".** No `records/` set, but their `why` fields
     carry real written rationale (`greek-apologists-second-century`'s is a
     genuinely good, honest paragraph). Form pass + reduction pass. No new
     claims.
   - **Batch 3 (215): "Pre-Survey Candidate".** **Reduction only.** Strip
     dash fragments, cut the dramatic beats, hedge or delete absolutes, fix
     stale pointers. Explicitly forbid adding any new historical claim, and
     say so in the session contract. Enriching these needs a source floor
     first, which is a different project.

3. **One session per world, running §2's six steps in order**, ending in a
   commit whose message states what was checked against what — the commit
   messages in this session are the model and they are the durable record.

4. **Fan-out inside the session, not across worlds.** Per the project's
   pinned routing (§4.3): a discovery subagent for source/contested/absent
   material, an independent verification subagent that re-reads the drafted
   prose against the records and the primary texts without having seen the
   drafting reasoning. Both briefed as **pointers, not summaries** — the
   repo's own rule: *"An under-briefed subagent wastes the tier; a
   summarized brief launders the main thread's blind spots into the
   component that exists to avoid them."*

   **The verification subagent's brief should be §1.1's five-question
   review pass, run explicitly, not "check this for quality."** That pass
   is derived directly from what Mark's own corrections actually targeted
   across this session (quantifier/modality overclaims, material added
   during expansion, an over-performing closing sentence, a sentence that
   wouldn't survive being read back alone, invented cleverness) — proven
   to catch defects in both this assistant's drafts and a second model's
   (Gemini's), which is why it's a stronger brief than a generic
   quality check.

## 4.3 Which model drafts the prose — Fable, Sonnet, or Opus

**There is a written, adopted verdict on Fable in this repo, and it is
specific about where Fable does and does not pay.**

`reference/method/CiC_Record_Native_World_Build_Process_V1.5.md`
(§ "Model routing (Mark's policy, 2026-08-01 — pinned, not per-thread
discretion)"):

| Lane | Model | Scope (quoted) |
|---|---|---|
| Main thread | **Sonnet** | "Orchestration and ledger discipline; the mechanical Phase-B conversion scripts…; the remaining templated documents… the main thread's job is discipline, not depth." |
| Review + research | **Opus** | "Every adversarial review round (cross-model against BOTH other tiers — Opus reviews Sonnet's drafts and Fable's key components alike); blind battery grading; deep source research." |
| Key components | **Fable** (subagent calls) | "Lexicon discovery and development…; story inventory + quote discovery and vetting (Doc_09, incl. the Absent Stories question) — **these demand the deepest, most inclusive searching and building, and discovery misses are invisible to every gate**; gravity discovery; forces synthesis; voice construction; Phase-D battery-fail diagnosis loops." |

**Fable was adopted, not abandoned — but the branch evidence is thinner
than a first pass suggested.** Three substantial world-build attempts exist
on Fable branches — `origin/CiC-Fable-Cappadocian`, `origin/CiC-Fable-Desert`,
`origin/CiC-Fable-EarlyCommunal` (68-72 commits each, last activity
2026-07-03) — with real, substantial documents: Doc_01-06, Doc_09 (Desert's
Story Inventory has an actual "Absent Stories" section), a Forces Document,
a Voice Configuration / World Capsule Core, and a Representative Permanent
Prompt, under filenames that don't follow a clean Doc_01→Doc_10 numbering
(there is no Doc_07, Doc_08, or Doc_10 by that name on any of the three).
**None of the three branches is merged into `main`**, and neither
`worlds/Desert-Christianity/` nor `worlds/Early-Communal/`
exists on `main` at all — the `desert` and `cappadocian` world-record sets
that *are* live today under `records/` were not verified to have come from
these specific branches. Treat these as real, substantial Fable output to
learn from, not as shipped, adopted builds. `origin/CiC-Fable-Experiment`
carries a long validation-log sequence. That is a real track record on exactly this
project's material.

**But the repo also records the criterion for when Fable does *not* pay**,
and it applies squarely here. `CiC_FrontEnd_Decision_Log.md` (~line 185):
*"Fable 5 not recommended: its premium is for resolving ambiguity, and the
scope, framing, and interaction design here are already decided."*

**And it records Fable's one measured failure mode at scale**, which is
directly a prose-register failure: the 250 voice-perspective violations
across all 8 built worlds' spoken fields, *"concentrated in the lexicon…
authored as a Fable subagent's Doc_03/Doc_06 pass — a systematic authoring
pattern, not scattered error."* Fable did not miss content; it drifted
register **consistently**, invisibly, at fleet scale, and nothing caught it
until someone wrote a mechanical check. For a task whose entire purpose is
register discipline, that is the specific risk to design against.

**Recommendation, by role:**

- **Drafting/editing the Atlas prose — Sonnet.** For Job 1 and for all
  form-level work in Job 2, the scope, framing and standard are *already
  decided*: this document plus the shipped pahc entry. By the project's own
  criterion that is not an ambiguity-resolution task, so Fable's premium
  does not pay, and it is exactly the Sonnet lane ("discipline, not depth")
  — with the discipline supplied by the §2 sequence, the linter, and this
  document rather than by the model's own judgment. The Chloe pass itself
  was Sonnet-authored (`Co-Authored-By: Claude Sonnet 5` on all fifteen
  commits) with Mark supplying the judgment calls, and it cleared the bar.
- **Discovery on record-less worlds — Fable, and this is the strongest case
  for it.** The 285-world source-floor problem is *literally* the pinned
  Fable lane: "what sources exist, what is contested, what is absent" is
  Doc_02/Doc_09 discovery work, and "discovery misses are invisible to
  every gate" is precisely why an absent-source or absent-contest for one
  of these worlds would never be caught downstream. **Test it on one
  record-less world's source-floor pass before committing to it at scale**,
  and brief it as pointers-not-summaries.
- **Verification round per batch, and authoring the escalation document —
  Opus.** Its pinned lane ("every adversarial review round… cross-model
  against BOTH other tiers"). Keep the cross-model property: the reviewer
  must not be the drafter.
- **If Fable is used for drafting anyway** — a legitimate thing to try on
  Batch 1, where the material is richest and most contested — then the
  mechanical linter for every register property in §1 **must** exist and
  run over its output before the batch is accepted. That is the one lesson
  the 250-instance defect actually teaches, and it is cheap.
- **Not Haiku for drafting.** `origin/claude/fable-table-cost-analysis-ynunno`
  records per-world runtime failures on Haiku (*"Papnoute FAILS solo on
  Haiku — length/measure, his own documented failure class"*; *"Yausep
  FAILS solo on Haiku"*; Chloe passed). Different task, but it establishes
  that quality on this material varies world by world, and the cheapest
  tier is where that variance shows up first.

**Honest limit on this assessment:** I found no document that evaluates
Fable specifically as a *prose-drafting* model against a fixed style bar.
The evidence above is Fable as deep-research/discovery agent and as
world-build document author, plus one measured register defect. The
recommendation to prefer Sonnet for drafting rests on the project's own
"already decided scope" criterion and on the Chloe pass's own result, not
on a head-to-head prose comparison — which does not exist and would be
cheap to run on one world if Mark wants it.

## 4.4 The escalation mechanism

**One consolidated review document per batch. Never a live question per
sentence.** Mark's stated constraint is that he resolves genuinely hard
calls and does not re-read every sentence, so the mechanism has to make his
input *dense*.

Reuse what the repo already runs rather than inventing a format: the
`FLAGS.md` / FLAG-029 discipline (*"Defects → FLAGS.md, never silently
patched. Upstream wording problems are referred, not rewritten"*) and the
in-record precedent from `pahc.craft.chloe-voice.md` (*"FLAGGED, not
resolved here… carried forward to the closing summary rather than silently
edited"*).

Per batch, one file — e.g.
`Ministry/Technology/world-prose/BATCH_01_FLAGS.md`:

```markdown
# Batch 01 prose flags — 6 Built & Live worlds
Linter: clean except items below. Render verified on all 6 (320/390/1280/1440, both themes, 0 console errors).
Mechanically fixed without asking: 41 items — see commits, no action needed.

## Q1 · alexandria-catechetical · Story ¶3 · class (B) provisional frame
The entry states the Alexandrian school question as an open one ("Historians
still argue about how formal the whole thing was"), which is right. But
alx's own world_core caution <ref> calls the single-institution reading a
provisional frame. Current prose implies two clean alternatives.
  Option 1 (recommended): "…or a looser sequence of private Christian
    schools whose teachers were later remembered together."  [keeps two
    options, drops the implied completeness]
  Option 2: name the third possibility the record allows.
  Option 3: leave as shipped.
Sources: records/alx/world_core/<file> lines NN-NN; records/alx/contested_claim/<file>
If unanswered: ship Option 1 (weakest claim of the three).
```

Properties that make it work:

- **Every question carries its escalation class from §3.2 (A–H)**, so Mark
  sees at a glance whether he is being asked a doctrinal question or an
  evidentiary-weight one, and can answer the same kind in a row.
- **Drafted options, not open questions.** Mark's two most efficient
  contributions this session were supplying plain wording (`fb1827f8`) and a
  one-word swap (`6dfc39c3`). Give him something to swap.
- **A stated default if unanswered**, always the weakest-claim option. No
  question blocks the batch; unanswered ones ship at the humblest wording
  and stay in the file as open.
- **The mechanical fixes are counted, not enumerated.** He reads the
  questions, not the diff.
- **Answers are applied and the file is not rewritten** — it becomes the
  record of why the prose says what it says, the same role the commit
  messages played this session.

Target: **8–15 questions per 6-world batch.** If a batch generates 40, the
guide is underspecified for that material and the fix is to amend §3.1's
list, not to send 40 questions.

## 4.5 Illustrative session contract

```
PER-WORLD PROSE PASS — <world-id>   (one world, one session)

INPUTS
  reference/method/CiC_Voice_Style_Guide_and_Scaling_Plan.md   (this doc)
  cic-website/atlas-v3.html — the shipped post-apostolic-house-church entry  (THE BAR)
  records/<code>/**                          (if it exists; else Job 2 rules apply)
  cic/texts/**, records/<code>/search_record/*  (primary texts for verification)

1 TRUTH      Read world_core (horizon/formation_logic/thinness/cautions/thin_topics),
             every contested_claim, every honest_limit, voice_craft, figures named in
             the prose. Mark each existing claim: supported / overstated / unsourced /
             out-of-window. Open the primary text for any claim resting on one.
             JOB 2 (no records/): no truth pass is possible. REDUCTION ONLY —
             cut and hedge; add no historical claim.
2 CONSISTENT Read tile, Story, Legacy, voices, floorNote, sourcing, sources,
             experienceToday, documentedStories TOGETHER. Cross-field contradictions
             and stale pointers are found only here.
3 STYLE      §1.1's five-question review pass, then §1.3-1.5, §1.9-1.12 against the
             pahc exemplar. Full sentences. Cut, don't
             re-adjective. Reuse established terms.
             APPLY THIS TO EVERY SENTENCE IN EVERY FIELD, not just the ones
             you already flagged as defective. Pre-existing, previously-
             unedited text has never been checked against this bar and is
             exactly as likely to fail it as anything you're about to
             rewrite. AND: apply it again to every sentence you just wrote
             to fix something else - a rewrite that fixes one defect is a
             fresh chance to introduce a stacked metaphor, a redundant
             phrase, or a claim that contradicts the sentence next to it.
             Read each paragraph as one claim, not a sequence of
             sentences, and check whether any two of them quietly
             contradict each other (the Alexandria pass shipped a
             floorNote whose own first sentence said "nothing diverges"
             and second sentence said "formally condemned" - this class of
             error will not show up if you check sentences one at a time).
3.5 DEPTH GAP  Read §1.1's "depth gap" subsection, then put this world's
             tile, Story, Legacy, and voices side by side with Chloe's
             corresponding fields - not sequentially, side by side. Ask
             what job each of Chloe's sentences does that this world's
             field has no equivalent for. Specifically check: (a) does
             Story/Legacy actually contain \n\n and render as multiple
             paragraphs, not one block; (b) does the tile cover a
             practice, a held-open structural tension, AND a real cost
             (persecution/suspicion/loss of status), not just one or two
             of the three; (c) does at least one voices entry hedge a
             claim the way Ignatius's or Polycarp's does, and does one
             entry (voices isn't fixed at five - add one if needed) state
             a structural absence this world's own world_core/thin_topics
             already names. A world that passes every sentence-level
             check in step 3 can still fail this step - Alexandria did,
             twice, before this check existed as its own step.
4 SOURCES    Every work named in prose has a row in `sources`. Add storySources /
             legacySources. Note anything cited on the tradition page but not here.
5 SYNC       atlas-v3.html + data/world-census.json + index.html + table.html +
             traditions/<id>.html (tile AND figcaption). Both JSON files still parse.
6 VERIFY     Headless: expected element counts, 0 console errors, 0 overflow at
             320/390/1280/1440, BOTH themes, every control clicked, links resolve.

ESCALATE, DON'T DECIDE: §3.2 classes A-H. Append to BATCH_NN_FLAGS.md with class,
  location, the records citation, 2-3 drafted options, a recommendation, and the
  default-if-unanswered. Then continue — never block on an answer.

SHIP: one commit per approved unit, never a partial unit. Commit message states what
  was checked against what, and records anything known-broken and not fixed.
```

## 4.6 Sequencing note

Do not start Job 2's 215 Pre-Survey Candidates as an editorial project.
They are a **sourcing** project wearing editorial clothing. The reduction
pass in Batch 3 is genuinely worth running — it removes the specific
AI-cliché signals that undercut trust across the widest surface of the site,
and it is safe because it only ever subtracts. But enriching those entries
to the pahc bar requires each world to have a source floor, and that is the
`records/` build pipeline, not this document's scope. Say that out loud to
Mark rather than letting a prose pass quietly become the thing that invents
history for 215 movements.

---

## Appendix — the commits this document is derived from

Branch `claude/website-v2-sandbox`, all 2026-09-08.

| Commit | What it fixed |
|---|---|
| `2b00a20d` | Display rename, public surfaces only; scope boundary recorded |
| `dc1646a7` | Tile rewrite: templated shape, reaching for profundity, "held together only by" theological overstatement |
| `fb1827f8` | Plain phrasing over clunky abstraction (Mark's wording); disproved an assumed clamp fix |
| `6dfc39c3` | One-word meaning change: "staying" → "living as one body" |
| `e65a3ad3` | Final tile: three short sentences, leadership named as plural |
| `0250f13b` | Justin source misattribution; Pliny + Martyrdom of Justin added; sources CSS prep |
| `508e5bd2` | Sources accordion, site-wide UI consistency (all 292) |
| `1956cb6b` | Story: triplet opener, question fragments, gut-punch closer, two-strand leadership, Ignatius hedge; multi-paragraph render support |
| `110550cd` | Legacy: origination overstatement, "Scripture" anachronism, canon scoping; `sectionSources()`; Polycarp letter added |
| `ca3e04a2` | Voices: dash fragments → sentences; Ignatius death, Polycarp title, unnamed hosts |
| `3f8445e9` | Story opener: "no documented", canon scoping, dedup, "weary travelers" |
| `68f67d2b` | `why` template across 7 worlds; second Interview button; `querySelectorAll` fix |
| `0373f37f` | Dura-Europos `experienceToday` removed as out-of-window |
| `49129e64` | Tradition-page questions re-scoped to their citations; cryptic door line cut |
| `25213aa9` | Documented stories as per-story book-icon buttons |
| `35ab377a` | Stale "(disclosed on its tile)" pointer removed |
