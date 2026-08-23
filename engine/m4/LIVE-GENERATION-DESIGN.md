# M4 Live-Generation Design

**Status:** signed off (§9.5), implemented, amended 2026-08-23 (§9.7).
**Governs:** `engine/m2/builders.py` (prompt compilation), `engine/m4/`
(evidence, generation, grounding net, turn loop), `engine/m3/generation.py`
(`LiveModelAnswerer`), `records/_fleet/fleet_voice/`.

---

## §0. A note on this document

This file is **reconstructed**, on 2026-08-23, from the implementation it
governs and from the two dozen places in the codebase that cite it.

The original was written on `claude/cic-design-assignment-ecoxh2` against
the real `alx` package. Its *implementation* was merged; the document itself
never was. For roughly a day, every module in the live-generation path cited
"LIVE-GENERATION-DESIGN.md §5.2 / §6.3 / §9.5 Fork 2" as its ruling
authority, and the ruling authority was not in the repository. That is not a
filing error. It is how a documented-but-unimplemented compiler step
(`§5.3`, the citation-contract placeholder substitution) shipped a literal
placeholder into live model input for seven worlds and nobody could look up
what was supposed to happen — see §9.7.

What is written here is therefore of three kinds, and they are marked:

- **Recovered.** Phrases other files quote verbatim are preserved as quotes
  and attributed to the original. Where a file quotes the original saying
  something this document now contradicts, the contradiction is stated, not
  smoothed (§5.3 is the main one).
- **Read off the implementation.** The bulk of it. Where the code and a
  remembered intention differ, the code is described, and the difference is
  named.
- **Ruled 2026-08-23.** New decisions, in §9.7, made because the repair work
  forced them. These are marked RULED and dated, and are as binding as §9.5.

Section numbers are **fixed**: existing code comments cite them by number.
Do not renumber. Add.

---

## §1. What this is, and the occasion for it

A participant asks a formation-world's Representative a question. The
Representative answers in the strict we-voice, grounded only in that world's
own sourced records, and every claim it makes is traceable to the record it
came from.

The occasion for this design was a specific failure: a fabricated line about
a door — vivid, plausible, in register, and supported by nothing. The
question it forced is not "how do we detect fabrication after the fact" but
"what shape of generation makes fabrication structurally visible at the
moment it happens."

The answer this design gives: **the voice cites itself, inline, as it
speaks**, and a deterministic check reads those citations before any of the
turn reaches a participant.

The guard the whole design serves is the fleet's own:

> Honest thinness beats invented depth, absolutely.

With one corollary this document did not originally state and now must
(§9.7): **silently deleting true, sourced content is a violation of that
guard, not an application of it.** A system that drops a grounded sentence
without saying so has invented a thinness the record does not have.

---

## §2. The shape of a turn

```
participant message
   │
   ├─ safety call        (Haiku-class, engine/m5/live_calls)
   ├─ reader call        (Haiku-class — asks, register, ambiguity, scope)
   │
   ├─ gate + routing     (engine/m5/routing, engine/m5/failure)
   │
   ├─ EVIDENCE ASSEMBLY  (§3 — deterministic, no model call)
   │      └─ evidence block, rides in the per-turn USER message
   │
   ├─ ONE generation call (§4 — Sonnet-class, streaming)
   │      system = the world's whole compiled prompt (cached prefix)
   │      output = the answer, with inline [[record.id]] tags
   │
   ├─ GROUNDING NET      (§6 — deterministic, per sentence, no model call)
   │      └─ ok → streams │ withhold → never reaches the participant
   │
   └─ turn result        (text, per-sentence citations, withheld account)
```

**One generation call per ordinary turn.** Not two. See §9.1.

---

## §3. Evidence assembly

`engine/m4/evidence.py`. Deterministic, no model call, no network.

### §3.1 Retrieval as focus, not transport

The world's entire compiled prompt is already in the system prefix, cached,
whole, on every call. Evidence assembly ships **no new content into
context**. It selects and scopes which of the already-compiled records
ground *this* turn.

This is why the evidence block rides in the **per-turn user message** and
never in the system prefix: the prefix must stay byte-stable to remain
cache-eligible. A block that changed per turn inside the prefix would
invalidate the cache on every call and pay full input price for content the
model already had.

### §3.2 The stages

**Stage A — asks → canon cells.** The reader call's extracted asks are
scored against each canon cell's keyword corpus, derived from the fleet's
own `canon_question` records (`engine/m1/canon.cell_keywords`).

A cell match requires at least two shared content words. One shared word
("church", "world") is noise. A genuinely off-canon turn — small talk, a
question the canon has no cell for — must be free to resolve to **no cell**
rather than be forced onto the nearest one; the evidence block is then
empty and the turn proceeds on the prompt alone.

`compiled/indexes/canon-map.json` exists as a **compiler-side cache of
exactly this derivation**. Caching it changes nothing about what Stage A
computes, only where the per-cell word sets come from. Still unread as of
this writing — an optimisation, not a correctness gap.

**Stage B — cell → candidates → rank.** The cell's own `compiled/
coverage.json` entry seeds the candidate pool. Candidates are scored by
lexical overlap against their own compiled record JSON.

The original's recommendation, quoted by `engine/m4/evidence.py` and
`engine/m2/builders.py`, was to

> score them directly off their compiled record JSON rather than adding a
> chunk directory

for `gravity` / `force` / `contested_claim`. That is what is built, and it
was extended: *every* type is scored off its own record JSON. No chunk
directory is read here at all.

Per-type floors admit a minimum of each type — the original's phrase was
"at minimum, when the cell has them" — so a turn is not handed six terms
and no story. `honest_limit` is **unconditional and uncapped**, because
§6.3's fallback ladder depends on it being present whenever the ground runs
thin, not only when it happens to score well against this turn's wording.

*A named simplification, not a silent gap:* the original's text ("every
other chunk-served record… scored… and the top scorers join") reads as also
searching outside the cell-seeded set. That whole-world expansion is not
built. Stage C is the one form of beyond-the-seed expansion performed.

**Stage C — tension completion.** `grounding_net.scope_completion`, imported
by `evidence.py` rather than reimplemented — one tension-walk, owned once.

Never serve one pole of a recorded tension without the record that names the
tension. Any `gravity` / `contested_claim` standing in a `tension-with` or
`disputed-by` relation with a retrieved record is pulled in, walked in
**both** directions so one missing back-edge cannot silently drop the guard.

This is the door-line fabrication's *systemic* fix, not a patch for it.

**Stage D — thin-topic riders.** A world's `world_core.thin_topics` ride
along as an explicit "what we do not have" marker whenever this turn's
wording touches one.

**Stage E — session exclusion.** Story and quote ids the M4 event log
already shows this session as told are marked, so the voice does not retell
the same story three turns running. Caller-supplied: `engine/m4/turn.py`
makes no store reads of its own.

### §3.3 The block itself

```
## Ground for this turn (cite only these; anything beyond them is spoken
## as our honest limit, never asserted)
- [[alx.term.eucharistia]] term — The thanksgiving meal of bread and cup…
- [[alx.story.potamiaena]] story — the tradition of Potamiaena, a young woman…
- THIN GROUND (do not claim past it): women's own words — no female-authored…
```

Ids are the **exact strings** the §4.1 tag grammar uses. This block and the
model's own tags share one id vocabulary by construction. As of §9.7 the
compiled prompt's record headers do too.

### §3.4 When real embeddings become admittable

Fork 3 (§9.5) rules lexical-first retrieval as the live path. Real
embeddings are **not foreclosed** — they become admittable on evidence, and
the threshold is **measured recall on real transcripts**: a demonstration
that lexical retrieval is missing records a participant's question plainly
wanted. Until that evidence exists, nothing pays a provider.

`compiled/indexes/` currently carries deterministic hash-derived stand-in
vectors. They are placeholders and are documented as such where they are
built.

---

## §4. The citation contract

The compiled prompt teaches every world's voice to tag each claim-bearing
sentence with the record id(s) it draws on. The contract text itself is a
**record**, not code: `records/_fleet/fleet_voice/`, field
`citation_contract`, compiled into every world's preamble (§5.2).

### §4.1 Tag grammar

```
[[world.type.slug]]
```

- Dotted lowercase, **no spaces inside the brackets**, so a sentence-boundary
  split can never break inside a tag.
- **Before the terminal punctuation**, not after it:

  > … the same bread, the same cup [[alx.term.eucharistia]].

  This is not a stylistic preference. The net splits sentences on
  `(?<=[.!?])\s+`; a tag emitted *after* the stop is carried onto the
  **next** sentence, grounding a claim it never came from and leaving its
  own claim untagged and withheld. See §9.7, where exactly this happened.
- A connective or interpretive sentence carries **no tag**. Only a sentence
  naming a person, place, text, number, or attributed quote does.
- Quoted words are tagged with the record that holds them **verbatim**. A
  quote with no tag, or words found in no tagged record, is not spoken.
- Tags are stripped before display. A participant never sees one.

Multiple ids on one sentence are legal and sometimes required — the net
checks a quoted span against the **union** of the records the sentence
cites, so a sentence quoting two records is grounded by naming both.

---

## §5. The compiled prompt

Built by `engine/m2/builders.build_prompt`. Deterministic: same records in,
same bytes out. It is the cached system prefix (§3.1), so nothing per-turn
may enter it.

### §5.1 Order

Fleet preamble first (§5.2), then the world's own identity, horizon,
formation logic, thinness, cautions, guard, characteristic concerns and
flavour notes, then its records, then its demonstrations (§5.3).

The preamble goes first deliberately: it reads as the voice's own standing
instruction, ahead of any one world's particulars.

### §5.2 The fleet preamble

One fleet-owned record (`records/_fleet/fleet_voice/`) supplies the register
statements, the pronoun rule, the citation contract and the limit
discipline, compiled into every world's prompt. It replaced text that had
been duplicated across six worlds' individual `voice_craft` records.

Principle 3 holds throughout: **prompt content is records, never code.** The
compiler performs *substitutions* into record-authored prose — the world's
display name into the pronoun rule's `{world}`, real record ids into the
citation contract's placeholders — and authors none of it.

### §5.3 Demonstrations

Each world's demonstration records are rendered as worked participant/
representative exchanges, with the representative's turns carrying citation
tags. These are the highest-leverage teaching surface in the file: a live
model reproduces what the demonstrations show far more faithfully than what
the contract says.

**The original was wrong here, and the error mattered.** It specified demos
rendered

> with citation tags derived from the demonstration record's own `sources`
> field

A real-record check found `sources` points to bibliographic editions, never
to the repository records a demo actually draws on. The implemented
alternative scores each demo sentence against candidate records directly.

Three things follow, and all three are §9.7 rulings:

1. Demo tags are **asserted ground truth** on the surface a model imitates
   most. A tag in the wrong place teaches wrong placement. A placeholder id
   teaches a fabricated namespace.
2. The bar the compiler tags at **must be the net's own bar** (§6.1). Two
   independently conservative bars compose into deletion.
3. The invariant "a demo that would pass its own net if it were live output
   is exactly the demo that gets tagged here" must be **enforced**, not
   documented. `engine/m2/demo_net.py` enforces it, over the compiled bytes,
   inside `compile_world`.

---

## §6. The grounding net

`engine/m4/grounding_net.py`. Deterministic, string operations only, no
model call — cheap enough to run inside the streaming path per sentence.

### §6.1 What it checks

Per sentence, in this order:

| | condition | verdict |
|---|---|---|
| 1 | honesty scaffolding, or the one sanctioned self-naming | **ok**, exempt |
| 2 | a tag naming a record not in the package | **withhold** |
| 3 | carries a quoted span → every span verbatim in the union of its tagged records | **ok** / **withhold** |
| 4 | no checkable claim (no proper noun, number, enumeration, attested figure name) | **ok**, no tag needed |
| 5 | a checkable claim with no tag | **withhold** |
| 6 | a checkable claim, ratio of its own content words found in its tagged records ≥ floor | **ok** / **withhold** |

The grounding floor is **0.4**, shared with `engine/m1/gates_experimental`.

Why this is sharper than the record-level gate it descends from: that gate
checks a sentence against the union of everything its *record* cites, so a
sentence can free-ride on words contributed by a source it never drew on.
Here every sentence names its own ground.

The quote branch is deliberately the **lenient** path: framing words around
a real quote should never sink a real quote. It is also the **strict** one —
quoted words either live verbatim in a cited record or they do not stream.

### §6.2 Calibration

Calibrated against the real `alx` package. The run log:

- the fabricated door line, tagged with the two records it originally cited,
  comes back **28% grounded → withheld**;
- the corrected line clears the floor against its three real sources at
  **40%**;
- both licensed-quote sentences pass by **verbatim window-match** rather
  than ratio.

Three defects the first draft showed against real data, fixed and worth
keeping named:

1. A "marginal band" between floor/2 and floor let the one known real
   fabrication stream with only its badge withheld. **Removed** — below the
   floor is withheld, full stop, and the quote-verbatim check carries the
   legitimate cases that used to need the band.
2. The naive splitter broke inside quotations, orphaning a tag from the
   claim it grounded. The splitter now merges until quotes balance. *(Amended
   2026-08-23: it did this for single quotes only — §9.7.)*
3. A sentence-initial figure name ("Clement wrote a whole book…") escaped the
   capitalisation heuristic. A compiled figure-name lexicon, built from the
   package's own `figure` records, now catches attributions
   positionally-blind.

### §6.3 The fallback ladder

1. **Drop and continue.** A withheld sentence never joins the turn's text.
   No retry. No partial regeneration. No human edit.
2. **Escalate to the honest limit.** When *nothing* substantive survives, the
   turn degrades to the matched cell's own `honest_limit` record — real,
   reviewed, already-compiled content — or, if no cell matched, to the fleet
   floor line. **Appended by code, never recalled by a model**, the same
   precedent as `crisis_resources.py`.
3. **Report.** `net_result` is kept whole on the voice turn so a caller can
   audit every sentence's verdict, tags and reason. This is the M7 audit
   input.

Step 3 was under-specified in the original and is tightened by §9.7:
"kept whole" is not the same as "reported". A structure nobody reads is not
a signal. See §8.

---

## §7. Build map

| row | lands in | state |
|---|---|---|
| evidence assembly, Stages A–E | `engine/m4/evidence.py` | built |
| tension completion | `grounding_net.scope_completion` | built |
| citation-tag net | `engine/m4/grounding_net.py` | built |
| one-call generation | `engine/m4/generation.py` | built |
| turn loop | `engine/m4/turn.py` | built |
| fleet voice record | `records/_fleet/fleet_voice/` | built |
| "emit the fleet preamble segment first" | `engine/m2/builders.py` | built |
| "render demonstrations with tags from their `sources`" | `engine/m2/builders.py` | built, **by a different method** — §5.3 |
| citation-contract placeholder substitution | `engine/m2/builders.py` | **built 2026-08-23** — was open, and shipped a placeholder meanwhile (§9.7) |
| "LiveModelAnswerer = this same pipeline" | `engine/m3/generation.py` | built; no real call made through it yet |
| compile-time demo/net agreement check | `engine/m2/demo_net.py` | **built 2026-08-23** (§9.7) |
| `canon-map.json` read as Stage A's cache | — | open, optimisation only |
| whole-world Stage B expansion | — | open, named simplification (§3.2) |

---

## §8. Observability

*Added 2026-08-23. The original had no equivalent section, and its absence
is the reason §9.7's failure ran undetected across seven worlds.*

Every ordinary voice turn publishes:

| field | meaning |
|---|---|
| `citations` | surviving sentences and the record ids each named |
| `grounding` | the whole `net_result` — every sentence's verdict, tags, reason |
| `sentences_total` | how many sentences the model produced |
| `sentences_withheld` | how many the net refused |
| `withheld` | each withheld sentence, its tags, and why |
| `degraded_by_net` | **total** loss only — nothing grounded survived |

`degraded_by_net` is the ladder's step-2 signal and keeps exactly that
meaning. It is **not** a loss signal. Losing one sentence of six and losing
none reported identically until `sentences_withheld` existed.

The rule this section exists to state: **a signal that is absent on success
and present on failure is a signal nobody reads.** Zero is published,
always, and the count rides the transcript projection — the only view most
readers ever open.

At compile time, `validation/demonstration-net.json` ships inside every
package: the compiled prompt run through the live net, with every
unresolvable tag and every withheld demonstration sentence named.
`python -m engine.m2.cli demo-net-check` is its CI shape and exits non-zero
on any finding.

---

## §9. Decisions

### §9.1 One call, not two — RULED

The retired shape was: stream the free-text answer, then make a second,
forced-tool-use call asking the model which records it had drawn on.

That is post-hoc grading, and it is what this design exists to stop doing.
A model asked after the fact which sources it used will produce a plausible
list whether or not it used them. `generation.call_citations` is **deleted,
not merely unused**.

### §9.2 In-band tags, not a citation field — RULED

The tag is emitted in the same breath as the claim, by the same forward
pass, before the model knows whether the sentence will survive. That is the
whole evidential value: the citation is a *commitment made during* the
claim, not a *justification produced after* it.

### §9.3 Deterministic, not model-graded — RULED

The net makes no model call. String operations only. A grounding check that
itself hallucinates is not a check, and a check cheap enough to run per
sentence inside the streaming path can be run on **every** turn rather than
sampled.

### §9.4 Withheld means withheld — RULED

No retry, no regeneration, no human edit of a live turn. A sentence that
fails to ground does not get a second chance to ground differently; that is
just fabrication with more attempts.

*Amended by §9.7:* this rules out **regenerating**. It does not license
**hiding**. Drop-and-continue is the behaviour; silence about it was never
the design.

### §9.5 The four forks — RULED, FINAL (2026-08-22)

Checked against real, populated data across all five worlds built at the
time, not only `alx`'s original test case.

| | fork | ruling |
|---|---|---|
| **Fork 1** | sentence-gated streaming | Every sentence is verified before **any** of the turn's text is placed on the voice event. No per-token transport exists yet; when one is built, gating moves into that layer and the check itself does not change. |
| **Fork 2** | in-voice honest-limit degradation | The degradation line is the matched cell's own `honest_limit` record, or the fleet floor line. Appended by **code**. Never a system apology, never a model-recalled limit. |
| **Fork 3** | lexical-first retrieval | Lexical overlap is the live path. Embeddings admittable later on measured recall (§3.4), not foreclosed. |
| **Fork 4** | report-only ratio-floor promotion | The ratio floor promoted from the m1 experimental gate reports; it does not silently retune itself against live data. |

### §9.6 Model tiering — PROVISIONAL / TEST

Haiku-class for safety and reader calls; **Sonnet-class for voice
generation**, which now carries the citation tags.

The measured price of downgrading the voice model was **halved grounded
citations**. That is the reason the voice stays Sonnet-class, and it is a
measurement, not a preference.

This section is explicitly **provisional** — the project lead's empirical
call, pending real cost/quality measurement. It is **not** locked the way
§9.5 is.

*Note (2026-08-23):* `generation.stream_voice_turn` sets no `temperature`,
so voice generation runs at the API default of 1.0. This has never been a
ruled choice. It is a default nobody selected, on a call that must produce
exact structural output. Flagged; not changed.

### §9.7 The citation-contract repair — RULED (2026-08-23)

**What was found.** Across nine live turns on three worlds, the net was
withholding **36% of generated sentences** — consistently the vivid,
quoted, concrete ones. Nothing reported it. Run against the seven shipped
packages, the same net withheld **47 of 377 sentences from the fleet's own
hand-authored demonstrations**, including *both* quoted lines of
`alx.demo.c-i-who-was-jesus` — Clement's New Song, and Athanasius's "He was
made man that we might be made God." Register statement 6 says the two
memorable lines *are* quotes. Those were the two being deleted.

The model was not refusing the contract. **The compiled prompt taught it a
contract the parser does not accept, and handed it a placeholder id to
copy.**

Five defects, none visible from either side alone because nothing checked
both:

1. **Tag placement.** The compiler emitted tags *after* the terminal
   punctuation. Every tag landed one sentence late. 218 of 225 tags in the
   shipped prompts; 85% of live model tags, which imitated them.
2. **Placeholder ids.** The citation contract's worked example shipped
   `[[world.term.example]]` verbatim into live model input in all seven
   packages — the substitution §7 named as open compiler work, never built.
   The model read `world` as the namespace and emitted
   `world.story.pliny-interrogation`. 46% of live tags were unresolvable.
   One desert turn on prayer was annihilated whole and the participant told
   the world had no grounded material on prayer.
3. **Quote-blind ranking.** Quote sentences were tagged to whichever record
   scored highest lexically — routinely a *paraphrase* — while the record
   holding the quote verbatim sat unused in the same package.
4. **Compiler and net disagreed about the bar.** The compiler declined to
   tag below a narrower bar; the net refused to speak any claim sentence
   with no tag. Two careful rules, composing into deletion of 20 true,
   sourced sentences. Not a content gap: 24 of 27 had a correct record in
   the same package.
5. **Single-quote-only splitter.** §6.2's defect-2 fix handled `'` only.
   The corpus already held 249 paired double-quoted spans and a live model
   quotes with `"` far more readily. Such spans were invisible to both the
   sentence-merge and the verbatim check — a sentence split mid-quote and
   the orphan reached a participant with its attribution stripped.

**And one more, found by fixing (4):** the compiled prompt carried 13
doctrinal witnesses, 13 terms and 18 forces (alx's counts) as content the
voice was told to cite, and showed the id of **none of them**. Only stories
named theirs. A claim drawn from that content *could only* carry an invented
id. Measured: 14 of 16 unresolvable tags had a real record in the package
that satisfies the net outright — the voice was reading the right record and
spelling its name wrong.

**Rulings.**

| | ruling |
|---|---|
| **7a** | Tags are emitted **before** the terminal punctuation, at compile time and in the contract alike. §4.1 is normative; the parser is not relaxed to accept drift. |
| **7b** | The citation contract's placeholder ids are **substituted from the world's own records** at compile time. A placeholder with no substitute is **dropped**, never shipped: an absent second tag still reads as a correct worked line; an unresolvable one teaches a fabrication. |
| **7c** | Quoted spans resolve **per span**, may name several records, and prefer an actual `quote` record over one that merely reproduces the words. |
| **7d** | The compiler tags at the **net's own bar**: ratio over a record's full text, over the floor, searched **package-wide**, with the demonstration's canon cell demoted to a tie-break. Whatever is too permissive to *assert* at compile time is already too permissive to *accept* at runtime — one bar, one place it can be wrong. |
| **7e** | Which sentences carry a tag is the **net's own question**. Interpretive framing is left bare, as §4.1 always said. Demo tags fell 222 → 107 as a result: the demonstrations had been contradicting the contract they teach. |
| **7f** | Citable types stay the content-bearing set. `source`, `search_record`, `figure`, `world_core` and `voice_craft` are never named as a sentence's ground. The net *would* accept them; the compiler is deliberately stricter, which can only change **which** record grounds a sentence, never **whether** one does. |
| **7g** | The quote-aware splitter recognises **double-quoted spans**, handled as families so a stray closer of one kind cannot cancel a genuine opener of another. Curly doubles included; curly singles deliberately excluded — U+2019 is overwhelmingly an apostrophe, and §6.2's own postmortem records what apostrophe ambiguity costs. |
| **7h** | Every citable record section in the compiled prompt **names its own id**, in `[[id]]` form — the literal string the voice must emit, beside the content it is emitting it for. Demonstration headers stay bare ids: a demonstration is never valid ground. Quote records stay **out** of the prompt entirely — they carry license fields gating do-not-voice material and reach a turn through the evidence block, which has always named candidates as `[[id]]`. |
| **7i** | Partial withholding is **published** (§8). |
| **7j** | The demo/net agreement invariant is **enforced at compile time** (`engine/m2/demo_net.py`), over the compiled bytes, and ships inside every package. A documented invariant that nothing asserts is not an invariant. |

**Measured effect**, nine live turns, three worlds, identical questions:

| | withheld | tags unresolvable | turns losing everything |
|---|---|---|---|
| before | 47/129 (36%) | 29/63 (46%) | 5/9 |
| after 7a–7c | 19/109 (17%) | 3/54 (6%) | 1/9 |
| after 7d–7g | 24/127 (19%) | 16/60 (27%) | 1/9 |
| after 7h | **11/109 (10%)** | **3/44 (7%)** | **1/9** |

Demonstration corpus: **47 → 0 withheld** on six of seven worlds.

The 7d–7g row going backwards is instructive and is left in the record:
adopting the net's bar shrank the demo-tag vocabulary from 222 to 107, and
for terms and witnesses that vocabulary was the *only* place their ids
appeared. Fixing one thing exposed the next. 7h paid it back.

---

## §10. Open

- **`syr` demonstration finding, 1.** Its heresiological sentence naming
  Bardaisan, Marcion and Mani has no single record clearing the floor; the
  topically correct one, `syr.gravity.heresiological-self-definition`,
  reaches 36% against a 40% floor. Left reported rather than tuned past. It
  is a real content question — does the world need a record here, or does
  the demonstration sentence need revising? — and surfacing it is what the
  check is for. `demo-net-check` exits non-zero on it.
- **Residual invented ids, 3 of 44 live.** Two are quote ids (quotes are
  license-gated out of the prompt by 7h); one names a record *type* that
  does not exist. Neither wants a header.
- **§9.6 temperature.** Voice generation runs at API default 1.0. Never
  ruled.
- **`canon-map.json` unread**; **whole-world Stage B expansion** not built
  (§3.2). Both optimisations, neither a correctness gap.
- **No real call has ever been made through `engine/m3`'s
  `LiveModelAnswerer`**, matching the same spend-authorisation discipline
  every other live path was run under.
- **The fleet floor line and the crisis-resources text** are honest and
  correct but **not yet project-lead-approved participant-facing copy**.
  Flag before any world that opens ships either literal string.
- **Two dangling cross-references in `engine/m4/evidence.py`**, found while
  checking this document's own numbering: it cites "spec §4.2:
  stories/quotes must stay reachable in conversation" and "spec §5.5"
  (the continuity rule). `Redesign-Spec/CiC-Program-Spec.md` §4.2 is *Step 0
  — the Question Canon*, and the spec has no §5.x headings at all. The
  reasoning in those comments is sound and matches the code; only the
  section numbers are wrong. Left as found — repointing a citation means
  knowing which section was meant, and guessing is how §0 happened. Same
  defect class as this document's own absence: a citation is not a source.
