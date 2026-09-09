# CiC Prose Craft Analysis

**Source text:** `cic-website/atlas-v3.html`, movement `post-apostolic-house-church`
(fields: `entry.tile`, `longDescription`, `legacy`, `voices[0–4]`, `floorNote`,
`relationsSummary`, `why`).

**Corpus size:** 38 sentences, 746 words. Average sentence 19.6 words; median 18;
range 5–46.

**Reader's actual order** (from the panel renderer at atlas-v3.html:41549–41579):
`entry.tile` → *The Story* (`longDescription`) → *Documented stories* (collapsed) →
*Voices* → *Doctrinal floor note* → *Legacy* → *In its own record*
(`relationsSummary`) → *Where this tradition stands* (`why`). Term-introduction
claims below are checked against this order, not JSON field order.

Every principle in this document is derived from and cited to this text only. Where
the text breaks a pattern I would otherwise state, the break is reported as an
exception, not smoothed over.

---

## 1. Sentence length and rhythm

**Principle.** Write to a median of ~18 words with a working range of 5 to 46, and
never let two long sentences (30+) sit adjacent inside a paragraph in the narrative
fields. Build each paragraph around one sentence that is at least twice the length
of its neighbours — that long sentence is where the concrete inventory goes — and
buy the room for it by putting a very short sentence (5–12 words) directly before or
after it. In the story field, close each paragraph on a sentence shorter than the
paragraph's longest.

Measured distribution: 15 of 38 sentences (39%) are 15 words or fewer; 11 (29%) fall
in the 16–20 band; only 4 (11%) exceed 35 words. So the long sentence is rare enough
to register as an event.

Paragraph shapes, in words per sentence:

| Unit | Shape |
|---|---|
| `tile` | 17, 20, 15 |
| story P1 | 20, **5**, 25, 18, **29**, 12 |
| story P2 | **26**, 17, 8, 6, 17 |
| story P3 | 21, **45**, 18 |
| legacy P1 | **9**, **46** |
| legacy P2 | 40, 30 |
| legacy P3 | 11, **36**, 30 |
| `voices` | 20/20, 23/13, 26/15, 14/13, 13/11 |

Evidence:

- The purest instance of short-claim-then-long-unpacking is legacy P1, a 9-word
  thesis followed by a 46-word sentence — a 5:1 ratio in a two-sentence paragraph:
  "Almost every Christian tradition descends from these early gatherings." then "The
  basic rhythm of Christian worship—assembling on the first day of the week, reading
  aloud from the prophets and the apostles' memoirs, and sharing the bread and the
  cup, whether in a full communal meal or the bread and wine alone—shows up earliest
  in these spaces."
- The inverse move, long setup then a hammer, is story P1's second sentence: a
  20-word negative opener is followed by **"They had the Old Testament."** — five
  words, the shortest sentence in the corpus, placed immediately after the longest
  run of abstractions in the paragraph.
- Story P2 uses descending length as pacing rather than as emphasis: 26, then 17,
  then 8, then 6 — "How should conflict within the community be resolved?" (8) and
  "What did women's leadership look like?" (6) — then resets to 17 for the close.
- Story P3 is the textbook shape: 21-word source-locating opener, 45-word inventory,
  18-word close. The close is a semicolon pair: "Justin was executed for refusing to
  abandon his Lord; tradition has it that Ignatius met the same end."

**Exception, reported honestly.** The close-short rule holds in `longDescription`
(12 < 29; 17 < 26; 18 < 45) and in `voices` (four of five end on their shorter
sentence), but **fails in `legacy`**: P1 ends on its 46-word sentence and P2 ends
on a 30-word sentence after a 40. `legacy` is systematically heavier prose than
`longDescription` — 202 words across 7 sentences (28.9 avg) versus 267 across 14
(19.1 avg). If the pattern is generalised, it should be stated as belonging to the
narrative field, with the legacy field permitted to run long and end long.

---

## 2. Syntax patterns

**Principle.** Keep roughly six sentences in ten to a single main clause. Coordinate
with `and`/`but`/semicolon about a quarter of the time; stack two or more
subordinate clauses under one main clause less than one time in eight. Open with the
grammatical subject unless you have a *locator* to front — a place, a date, a source,
or a changed condition — and keep that fronted phrase to 3–8 words. Never front a
concessive or an argument.

Counts across the 38 sentences:

- **Single main clause** (phrases and at most one embedded clause allowed): 25 (66%).
- **Coordinated / compound** (two or more main clauses via `and`, `but`, `;`, or
  dash): 10 (26%).
- **Genuinely complex** (two or more subordinate clauses under one main clause): 3
  clear (8%), 5 (13%) if two borderline cases are counted.
- **Verbless fragment:** 1 (`relationsSummary`).

Simple, subject-first:
- "New believers were taught the Two Ways on the road to baptism"
- "The apostolic texts themselves gained authority in much the same way."
- "Most of these communities' hosts and householders are never named in the record."

Compound:
- "The gatherings met in their homes, but no record says whose."
- "The roles of bishop, presbyter, and deacon were already named in the apostolic
  writings, but trying to live out those instructions under local pressures gave the
  offices more concrete form."

Genuinely complex (all three cited in full, since there are only three):
- "The gospels and letters of the apostles moved between communities as copies were
  made and passed along, though no fixed collection had been settled yet."
- "Justin, who told his imperial interrogator that he taught above a public
  bathhouse in Rome, wrote down the earliest record of what their Sunday actually
  looked like—the reading of the memoirs, the common loaf and cup, and the
  collection gathered for orphans, widows, and travelers."
- "What they confessed is part of the raw material the creed was later drawn from,
  not a departure from it."

**Openers.** 32 of 38 sentences (84%) open with the subject or a question word. Only
6 front an adverbial, and every one of them is a short locator, averaging 5.5 words:
"Once the apostles were gone," (5) · "In the generations following the apostles," (6)
· "Across long distances," (3) · "In his surviving letters," (4) · "With the apostles
no longer there to consult," (8) · "Carried by travelers from city to city," (7).

Verified absent as sentence openers, 0 occurrences each: *Although, Because,
Despite, However, Moreover, Furthermore, Indeed, In order to, There is/are/was/were,
It is important/worth/clear, Not only, Ultimately, In conclusion, Overall, In many
ways.* The two instances of `while` are both mid-sentence participials attached to a
named person — "while he was marched toward Rome under armed guard" — not fronted
concessives.

---

## 3. Concreteness ratio

**Principle.** Every abstract noun must be cashed out into a name, a number, a
physical object, or an action either inside its own sentence or in the next one. The
cheque is written in the abstract sentence and cashed in the following sentence —
write the pair together and never ship one without the other. Target: 85%+ of
sentences carrying at least one proper noun, physical object, or quantity.

Measured: **33 of 38 sentences (87%)** contain a proper noun, a physical object
noun, or a quantity. 46 proper-noun tokens across 753 tokens (6.1%) — Rome ×6,
Ignatius ×4, Antioch ×3, Smyrna ×2, plus Justin, Clement, Polycarp, Asia Minor,
Corinthians, Nicene Creed, Chloe. Eight quantities in 746 words (one per 93 words):
"seven letters", "c. 107-117", "the year 96", "around 155", "two centuries",
"ten-soldier guard", "the first day of the week", "Two Ways".

Cheque-and-cash pairs:

- Abstraction: **no institutions.** "the earliest Christian movement had no
  documented church buildings and no single leadership structure." Cashed one
  sentence later in five words: "They had the Old Testament." — and again two
  sentences later with three place names: "scattered across Antioch, Asia Minor, and
  Rome, meeting wherever they could."
- Abstraction: **persecution.** "Following Jesus routinely meant loss of social
  standing, suspicion from neighbors, and periodic waves of official violence."
  Cashed in the very next paragraph into a guard detail and two deaths: "while being
  marched toward Rome under a ten-soldier guard" … "Justin was executed for refusing
  to abandon his Lord."
- Abstraction: **worship.** "wrote down the earliest record of what their Sunday
  actually looked like" — cashed inside the same sentence, after the dash, into four
  objects and three classes of people: "the reading of the memoirs, the common loaf
  and cup, and the collection gathered for orphans, widows, and travelers."
- Abstraction: **scriptural authority.** "The apostolic texts themselves gained
  authority in much the same way." Cashed in the next sentence into a physical
  repeated act and an excluded alternative: "Reading the apostles' letters aloud week
  after week became an enduring habit, and it was through this regular use in
  worship—not by an early decree—that these writings came to be heard alongside the
  ancient Jewish Scriptures."
- Abstraction: **unity across distance.** "these household communities were held
  together by carried letters." The anchor is the participle *carried* — an act, not
  a state — and it is repeated as a fronted participle in `legacy` P3: "Carried by
  travelers from city to city, these letters bound scattered households together."

**Exceptions — the five unanchored sentences, named exactly:**

1–3. The three questions in story P2: "How do we make room for genuine doubt?" /
"How should conflict within the community be resolved?" / "What did women's
leadership look like?" No name, object, or number appears in any of them, and none
is followed by an instance. This is the least-anchored passage in the entry. It is
defensible on the grounds that these are the community's open questions rather than
the narrator's claims — the paragraph's job is to say *these were unsettled*, and
supplying an example would imply a settlement — but if the pattern is applied
mechanically elsewhere, this passage is where it was suspended.

4. `floorNote`, second sentence: "What they confessed is part of the raw material the
creed was later drawn from, not a departure from it." **What** they confessed is
never stated, here or anywhere in these fields. This is a genuine floating
abstraction; its only anchors are the proper noun and the date-distance in the
sentence before it ("two centuries before the Nicene Creed was written").

5. `relationsSummary`: "Parent of nearly everything on the map" — a verbless label
whose only concrete referent, "the map", is the product rather than the history.

---

## 4. How technical, foreign, and ancient terms are introduced

**Principle.** Never define a term. Instead, put the plain-English word into service
first, and introduce the technical word later, attached to a person, a place, a date,
or a verb it is visibly performing — so the term arrives already doing its job and
the reader infers the sense from the work it does. Where a technical term has a
plain physical equivalent, use the objects and drop the term entirely. Where the
technical term is unavoidable, let its first appearance be inside a quotation from
the source.

Every unfamiliar term in the corpus, with its actual introduction:

| Term | First appearance in reading order | Mechanism |
|---|---|---|
| bishop | `tile`: "some were led by a single bishop and elders" | never defined; attached to the verb *led*, in contrast with *elders* |
| elders | `tile`, same sentence | plain-English word, used *instead of* presbyters |
| deacons | story P2: "a single bishop alongside elders and deacons" | introduced by company, inside an already-established triad shape |
| Two Ways | story P1: "New believers were taught the Two Ways on the road to baptism" | glossed by **role in a sequence** (who learns it, and when), not by content |
| presbyter | `voices[2]`, inside a quotation: "opening only as 'Polycarp, and the presbyters with him.'" | the technical word's debut is in the primary source's own words, ~400 words after *elders* has done the work |
| apostolic (adj.) | `legacy` P2: "already named in the apostolic writings" | the plain phrase "the gospels and letters of the apostles" appears first, in story P1; the compressed adjective comes only after |
| memoirs | `legacy` P1: "reading aloud from the prophets and the apostles' memoirs" | Justin's own term, made recoverable by the verb "reading aloud from" |
| Nicene Creed | `floorNote`: "two centuries before the Nicene Creed was written" | glossed by date-distance rather than by content |

**Two strong absences worth copying.**

First, "Eucharist" appears **zero times**, and so do *ecclesiology, episcopacy,
monepiscopacy, catechumen, agape, liturgy, christology, praxis, extant*. The rite is
carried entirely by objects and acts: "a shared table" (`tile`), "the weekly breaking
of bread and prayer" (story P1), "the common loaf and cup" (story P3), "sharing the
bread and the cup, whether in a full communal meal or the bread and wine alone"
(`legacy` P1).

Second, the jargon is quarantined in the labels. "Post-Apostolic Household-Church
Christianity" appears in `entry.subtitle` and nowhere in any sentence of prose. The
metadata absorbs the technical name so the prose never has to spend a clause on it.

**Bare-term audit.** Two terms do appear without their sense being supplied, and both
are handled the same way — by function rather than definition. "bishop" is never told
to the reader, only shown *leading* and *guiding* and being *addressed as* a title
someone else's letter declines to claim; "the Two Ways" is capitalised and never
explained, only located ("taught… on the road to baptism"). If a stricter rule is
wanted, "the Two Ways" is the one place a modern reader learns *when* a thing
happened without learning *what* it was.

*(Secondary note, outside the nine fields: the same entry's source notes introduce
"deaconess" with a Latin-term-then-gloss dash — "two enslaved women called ministrae
— deaconesses." That mechanism does not appear in the prose fields, which prefer to
avoid the term rather than gloss it.)*

---

## 5. Holding tension without resolving it

**Principle.** State both possibilities in one sentence, in parallel grammar, with
the second limb elided down to its distinguishing detail — then either stop, or add a
short clause that refuses the verdict explicitly. Vary the machinery: use the full
"both were real, and neither was settled" formula **once only**, and carry the other
disagreements on lighter, shorter templates. Where the disagreement is between two
witnesses, quote the witness that dissents so the reader can weigh it.

There is no single reused template. Five distinct constructions appear:

**(a) `Some X, others Y` with the verb elided in the second limb — 2 instances,
deliberately unequal.** The `tile` states the split bare, with no comment:

> "Once the apostles were gone, some were led by a single bishop and elders, others
> by a council of elders."

The story field restates it and *then* closes it with the refusal — the only place in
the entry where the refusal is spelled out:

> "Some communities were guided by a single bishop alongside elders and deacons,
> others by a circle of elders alone—both forms were real, and neither was settled."

Note that "council of elders" becomes "circle of elders" on the second pass — the
institutional word is swapped out for a shape word.

**(b) `X, though Y` — the concession that names the counter-evidence. 3 instances.**

> "though no fixed collection had been settled yet."
> "Polycarp's own letter later speaks of him as already dead, though it admits not
> knowing the details of what happened."
> "Polycarp of Smyrna was addressed as bishop by Ignatius, though his own letter never
> claims the title, opening only as 'Polycarp, and the presbyters with him.'"

The last of these is the strongest instance in the entry: two sources disagree about a
title, both are reported, the dissenting evidence is quoted verbatim, and no verdict
is offered.

**(c) `Fact, but no record says…` — the fact plus the limit of the evidence. 2
instances.**

> "The gatherings met in their homes, but no record says whose."
> "The roles of bishop, presbyter, and deacon were already named in the apostolic
> writings, but trying to live out those instructions under local pressures gave the
> offices more concrete form."

The second holds continuity and development together in one sentence without deciding
which of them "invented" the offices.

**(d) Semicolon grading a documented fact against a traditional one. 1 instance.**

> "Justin was executed for refusing to abandon his Lord; tradition has it that
> Ignatius met the same end."

Two claims of unequal evidential weight, in one 18-word sentence, with the weighting
carried by four words on the far side of the semicolon.

**(e) `whether A or B`, left open inside a noun phrase. 1 instance.**

> "sharing the bread and the cup, whether in a full communal meal or the bread and
> wine alone"

**Where the text does resolve.** Two constructions of the shape `X, not Y` do
adjudicate, and both do it by exclusion rather than by argument: "it was through this
regular use in worship—not by an early decree—that these writings came to be heard…"
and, in `floorNote`, "part of the raw material the creed was later drawn from, not a
departure from it." The `X, not Y` shape is therefore *not* a tension-holding device
in this text — it is the verdict device. Do not confuse the two.

---

## 6. Verb choice

**Principle.** Choose verbs a camera could film. Reserve the passive for facts whose
agent the record genuinely does not supply — and when you use it, say so nearby.
Make documents the grammatical subjects of active verbs: let the letter speak, admit,
claim, or fail to say, rather than reporting that the historian is uncertain.

Sample of 20 main verbs, with the four abstract ones marked: *lived, meant, had,
moved, were taught, were held together, were guided, wrestled with, describes, wrote
down, was executed, descends, shows up, had to work out, gave (form)°, gained
(authority)°, became°, bound, were preserved and read, speaks, admits, claims, met,
says, was put to death, left, are never named, kept teaching, fell into.*
(° = abstract predicate)

Physical or filmable: marched (×2), moved, carried (×2), wrote (×4), wrote down,
taught, brought into, held together, bound, met, gathered, assembling, reading aloud,
sharing, breaking, put to death, executed, preserved and read, left, fell into, shows
up, descends. Verified absent: *existed, functioned, represented, constituted,
embodied, reflected, served as* — 0 occurrences of any.

Only two genuinely abstract predicates appear, and both are anchored on the spot:
"gained authority in much the same way" (mechanism named in the next sentence) and
"gave the offices more concrete form" (immediately preceded by the concrete pressure,
"trying to live out those instructions under local pressures").

**Voice ratio across 46 main-clause verb slots: 25 active (54%), 14 passive (30%), 7
copula (15%).** The 30% passive rate is high by generic advice and is entirely
deliberate — every passive is evidence-shaped, used where the agent is the whole
community or is unrecorded:

> "New believers **were taught** the Two Ways… only then **were they brought** into
> the fellowship"
> "these household communities **were held together** by carried letters"
> "Most of these communities' hosts and householders **are never named** in the
> record."

**The distinctive move: documents as agents.** Five instances, and they replace what
would otherwise be narrator hedging:

> "Polycarp's own letter later **speaks** of him as already dead, though it
> **admits** not knowing the details"
> "his own letter never **claims** the title"
> "no record **says** whose"
> "**tradition has it** that Ignatius met the same end"

---

## 7. Hedging mechanics

**Principle.** Carry uncertainty on one word inside the noun phrase whenever
possible — an adjective, an adverb, a quantifier. Spend a whole clause on a hedge
only when the uncertainty belongs to a named source, and in that case make the source
the subject of the clause. Never hedge with the narrator's own doubt.

Word-level hedges (11 instances) versus clause-level (3) — roughly 4:1.

| Quote | Hedge carried by | Class |
|---|---|---|
| "no **documented** church buildings" | one adjective | word — and the honest one: absence of evidence, not absence of buildings |
| "**periodic** waves of official violence" | one adjective | word — replaces "constant"; sets frequency without a clause |
| "**Almost** every Christian tradition descends…" | one adverb | word |
| "**Most** of these communities' hosts and householders are never named" | one quantifier | word |
| "around the year 96" / "at Smyrna **around** 155" / "**c.** 107-117" | one word / one abbreviation + a range | word |
| "the earliest Christian writing outside the New Testament **to survive**" | two words folded into the superlative | word-level, and the highest-precision hedge in the entry — it limits the claim to the surviving record without adding a clause |
| "gained authority in **much** the same way" | one adverb | word |
| "**nearly** everything on the map" | one adverb | word |
| "though no fixed collection had been settled **yet**" | concessive clause + one adverb | **clause** |
| "**tradition has it that** Ignatius met the same end" | 4-word attribution phrase | **clause**, attributed |
| "though **it admits** not knowing the details of what happened" | concessive clause whose subject is the document | **clause**, attributed to the source, not the narrator |

Verified absent, 0 occurrences each: *perhaps, may have, might have, likely,
suggests, appears to, seems, would have, arguably, scholars debate, it is possible
that, some would say.* The entire academic hedging apparatus is replaced by (i) one
precise word and (ii) naming who is uncertain.

The most economical hedge in the text is a negation rather than a qualification: "no
record says whose" and "his own letter never claims the title" — statements about
what the evidence does, which cost nothing in confidence.

---

## 8. Paragraph and section openings

**Principle.** Open on an absence, a changed condition, or a named person — never on
a thesis. In a multi-paragraph field, hook each paragraph after the first to the
mechanism of the paragraph before it rather than announcing a new topic. Keep at most
one true topic sentence per field, make it the shortest sentence in its paragraph,
and hedge it with a single word.

Every opening sentence in the nine fields, in reading order:

1. `tile`: "An uncommon faith in scattered households lived as one body, connected by
   letters and a shared table." — characterisation plus two objects (letters, table).
2. story P1: "In the generations following the apostles, the earliest Christian
   movement had **no** documented church buildings and **no** single leadership
   structure." — **opens on absence.** The world is introduced by what it lacked.
3. story P2: "Some communities were guided by a single bishop alongside elders and
   deacons, others by a circle of elders alone—both forms were real, and **neither
   was settled**." — **opens on the unresolved disagreement**, with no preamble.
4. story P3: "In his surviving letters, Ignatius of Antioch describes writing to
   sister churches…" — opens on a **named person and the document that attests him**;
   the fronted locator is the source itself.
5. `voices[0]–[3]`: "Ignatius, bishop of Antioch, wrote…" / "Clement of Rome wrote…" /
   "Polycarp of Smyrna was addressed as bishop…" / "Justin Martyr was a philosopher
   who…" — **proper name in the subject slot, every time.**
6. `voices[4]`: "Most of these communities' hosts and householders are **never
   named** in the record." — the fifth voice fills the same grammatical slot with the
   *absence* of a name. A deliberate structural rhyme, and the strongest single
   design decision in the field.
7. `floorNote`: "These communities lived two centuries before the Nicene Creed was
   written." — opens on a date-distance.
8. `legacy` P1: "Almost every Christian tradition descends from these early
   gatherings." — the **only true topic sentence in the entry**: 9 words, the
   shortest in its paragraph, hedged on one adverb.
9. `legacy` P2: "With the apostles **no longer there** to consult, these communities
   had to work out how to live together…" — opens on an absence again.
10. `legacy` P3: "The apostolic texts themselves gained authority **in much the same
    way**." — opens by hooking to the previous paragraph's mechanism, not by
    announcing a topic.
11. `why`: "This Christian tradition is fully built, and you can have a conversation
    with Chloe, a household leader, right now." — product register, discussed in §9.

Four of the seven paragraph openings state an absence or an unsettled state ("had
no…", "neither was settled", "are never named", "no longer there to consult"). One
hooks to the previous mechanism. One names a person. Exactly one is a thesis.

---

## 9. What is absent

**Principle.** No similes, no scene-painting, no rhetorical questions aimed at the
reader, no second person outside operational copy, and no adjective that adds warmth
without adding information. Metaphor is permitted only where a single word carries a
distinction a literal phrase would lose — and it must not be extended past its own
clause.

Verified counts across the corpus:

- **Similes: 0.** Zero occurrences of "like a", "as if", "a kind of", "seemed to".
  The single "like" is comparative-listing, not figurative: "writings like those of
  Clement, Ignatius, and Polycarp".
- **Parentheses: 0.** Punctuation is 6 em-dashes, 3 semicolons, 2 colons — and each
  mark has exactly one job. All 6 dashes either unpack into a concrete inventory ("what
  their Sunday actually looked like—the reading of the memoirs, the common loaf and
  cup…") or insert an excluded alternative ("in worship—not by an early decree—that…")
  or pivot to the refusal of a verdict ("a circle of elders alone—both forms were
  real…"). None is used for drama or emphasis. All 3 semicolons attach an evidential
  or sequential status to a fact ("around 155; his own congregation recorded his
  death"). Both colons introduce a list of the community's open tasks or questions.
- **Rhetorical questions aimed at the reader: 0.** Three questions exist, all in one
  cluster after a colon in story P2, and all are framed as content — the questions
  *they* wrestled with. The single "we" in the corpus is inside one of them ("How do
  we make room for genuine doubt?") and belongs to the historical community, not the
  reader. **Reported honestly as the nearest thing to a device:** these three do read
  as a rhetorical run, and they are the only unanchored sentences in the story field
  (§3). The framing sentence — "The questions they wrestled with had no easy answers:"
  — is what keeps them content rather than device.
- **Reader address:** exactly one "you", in `why`: "you can have a conversation with
  Chloe, a household leader, right now." This is an affordance statement about the
  product, not a rhetorical invitation. Zero instances of "you can imagine", "picture
  this", "consider", "think about". If a rule is stated, it should be: the historical
  prose never addresses the reader; the interface copy may, and only to name what the
  reader can do.
- **Feeling-only adjectives: one clear instance.** Of the 32 distinct adjectives,
  nearly all are classificatory (weekly, communal, imperial, apostolic) or
  evidentiary (documented, surviving, fixed, detailed). Two are candidates:
  - **"faithful households"** (story P1) — *faithful* supplies no information the
    sentence does not already carry and is the one adjective in the corpus whose job
    is warmth. This is the genuine exception.
  - "An **uncommon** faith" (`tile`) — borderline, but defensible as a demographic
    claim (the faith was statistically rare) rather than a compliment.
  Note that even the intensifiers earn their place by drawing a distinction: "even
  **outright** persecution" separates legal violence from social suspicion, and
  "**genuine** doubt" separates real doubt from performed doubt.
- **Metaphor: not zero — four single-word instances, each doing precision work.**
  Stating a flat prohibition would be inaccurate. What is actually true is that every
  metaphor is one word inside an otherwise literal sentence, none is extended, and
  each buys a distinction:
  - "periodic **waves** of official violence" — *waves* encodes cresting and receding,
    which "episodes" would flatten.
  - "the **raw material** the creed was later drawn from" — encodes pre-formal
    continuity, which "source" would over-formalise.
  - "**Parent** of nearly everything on the map" — encodes descent, in a label field.
  - "on the **road** to baptism" — and this one is licensed by the source's own
    imagery: the Two Ways is itself a roads text.
- **AI-tell vocabulary: 0.** Zero occurrences of *tapestry, crucible, beacon,
  lifeblood, bedrock, delve, underscore, pivotal, robust, navigate, landscape,
  journey, embrace, resonate, profound, vibrant, multifaceted, holistic, it is
  important to note.*
- **Repetition instead of synonym-hunting.** "earliest" is used 5 times and never
  varied into *primordial*, *primitive*, or *inaugural*. "letters" appears 7 times,
  "apostles" 6, "bishop" 5. The tile's phrases are reused nearly verbatim in the body
  rather than paraphrased — "loss of status, suspicion from neighbors, and even
  outright persecution at times" (tile) becomes "loss of social standing, suspicion
  from neighbors, and periodic waves of official violence" (story P2): the same
  tricolon skeleton, with limbs two and three upgraded in specificity. Likewise "what
  their Sunday actually looked like" appears verbatim in both story P3 and
  `voices[3]`. The repetition is the structure, not a lapse.

---

## Generative checklist

- **Median 18 words. One long sentence per paragraph (35–46) and buy it with a short
  one (5–12) adjacent.** In narrative fields, end the paragraph shorter than its
  longest sentence.
- **Open on an absence, a changed condition, or a name — never a thesis.** One topic
  sentence per field, maximum; make it the shortest sentence in its paragraph and
  hedge it on one word ("*Almost* every Christian tradition descends…").
- **Every abstraction gets cashed in the same sentence or the next one** — into a
  name, a number, an object, or an act. Aim for 85%+ of sentences carrying at least
  one. Write the abstract sentence and its concrete pair together.
- **Subject first, 8 sentences in 10.** Front only a 3–8 word locator: place, date,
  source, or changed condition. Never front a concession.
- **Never define a technical term.** Use the plain word first, bring the technical
  word in later attached to a person, place, date, or verb it is visibly performing —
  and let its first appearance be inside a quotation if possible. Where objects will
  do the work, drop the term (loaf and cup, not Eucharist). Keep the jargon in the
  labels and metadata, out of the sentences.
- **Hedge on one word — *documented, periodic, almost, most, around, c., to
  survive*.** Spend a clause only when a named source owns the uncertainty ("tradition
  has it that…", "though it admits not knowing…"). No *perhaps*, *may have*,
  *suggests*, *arguably*.
- **Let documents be the subjects of active verbs** — the letter *speaks*, *admits*,
  *never claims*; *no record says whose*. Reserve the passive for facts whose agent
  the record does not supply (~30% is fine if every one is evidence-shaped).
- **State both possibilities in parallel grammar with the second limb elided, then
  stop.** Spell out the refusal ("both forms were real, and neither was settled")
  once per entry only; carry the rest on lighter machinery — *X, though Y*; *X, but
  no record says whose*; a semicolon grading documented against traditional. Reserve
  *X, not Y* for verdicts, never for tensions.
- **Repeat your own key phrases rather than reaching for synonyms**, and let the
  summary's tricolon reappear in the body with its limbs upgraded in specificity.
- **Zero similes, zero parentheses, zero questions to the reader, zero "you" outside
  interface copy, zero adjective whose only job is warmth.** One-word metaphor is
  allowed only when it carries a distinction the literal phrase loses — and never
  extended past its clause.
