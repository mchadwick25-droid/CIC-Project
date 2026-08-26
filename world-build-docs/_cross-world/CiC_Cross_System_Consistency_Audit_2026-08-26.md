# Cross-System Consistency Audit — six formation worlds, end to end

**Date:** 2026-08-26 · **Branch:** `claude/cross-system-consistency-audit-ojl9h0` · **Tree:** `e80eb94`

Six formation worlds were built in parallel threads against one spec. This
audit maps the whole system a participant's session actually touches — world
records → compiler → compiled package → engine runtime → API → front ends —
and, at each stage, draws the line between **what must be identical across
all six by design** and **what is allowed to vary**, then checks every world
against that line.

It is a process audit, not a content audit. Six different historical records
are supposed to look different: alx holds 51 terms and syr holds 10, and
neither number is a defect. What is not supposed to differ is the shape the
pipeline moves that substance through, and every finding below is a place
where it did.

**Companion artifacts:**

- `pipeline-drift-map.svg` — the system/data-flow diagram: the two paths a
  participant's session depends on, and the three points where divergence
  enters.
- `CONSISTENCY-MATRIX.md` — the per-world matrix, every cell measured from
  the live tree by `gen_matrix.py`, nothing transcribed by hand.
- `CORPUS-USE.md` — the 46-file vendored corpus against what each world
  actually draws on, and how much of each world rests on text the pipeline
  can verify offline (`gen_corpus_table.py`).
- `engine/m1/cross_world.py` — the standing check this audit leaves behind.
  `python -m engine.m1.cross_world` exits non-zero on any drift not written
  up here.
- A published read-only version of all three, for reading rather than
  reviewing: <https://claude.ai/code/artifact/13a7db9b-25bc-4cf4-a1d8-deb65a4966de>

---

## 0. Scope, and one correction to it

**In scope.** `records/worlds.yaml`; the six worlds' record trees; `engine/m1`
(gates), `engine/m2` (compiler), `engine/m4`/`engine/m5` (runtime),
`engine/api`; `cic-website` (the Atlas and front page); and the participant
app the engine serves.

**Correction to the launch scope.** The launch brief put `cic-poc` out of
scope as "suspended, dead." That is true of `cic-poc/backend` — the old
LangGraph/Supabase POC — and false of `cic-poc/frontend`, which is the
**only** participant front end the new engine has. `engine/Dockerfile` builds
it, `engine/api/app.py` mounts it at `REPO_ROOT / "cic-poc" / "frontend" /
"dist"` and serves it same-origin, `render.yaml`'s `cic-engine` service ships
it, and its last four commits are from the past three days (`27242dc` richer
world cards from `GET /api/worlds`, `6c48fc5` the Facilitator's door turn,
`eebd08a` the transparency-display fixes). The launch brief also asks
explicitly for "the frontend's handling of each" world, which cannot be
answered without it.

So `cic-poc/frontend` is treated as in scope and `cic-poc/backend` is not.
Nothing in this audit reads or reasons about the old backend. The directory
name is itself a consistency hazard worth naming: the live front end lives
under a path whose name says it is dead, which is how it came to be excluded
from a scope that needed it.

**Explicitly out of scope**, per the brief: normalising content depth or
density across worlds. Where a number below differs because one world's
sources are richer than another's, that is recorded as measurement, never as
a finding.

**Method.** Every claim here is measured, not read off a comment. The gate
battery was run against all six worlds; all seven packages were recompiled in
memory and their structures diffed; the registry was cross-checked against
`cic-website/data/world-census.json` field by field; the real label resolvers
(`engine.m4.citation_cards._label`, `engine.m2.builders._quote_speaker`) and
the real frontend formatter (`FigureBridgeMark.formatDates`) were run over
every world's records to see what a participant actually reads. Where a
finding says "a participant sees X," X was produced by the code that produces
it in production.

---

## 1. The pipeline, stage by stage

Each stage below states its **invariant line** first — identical by design on
the left, allowed to vary on the right — and then what the check found.

### Stage 1 — The registry (`records/worlds.yaml`)

The ONE world registry (spec principle 4). Every downstream surface derives
its per-world identity from here, and no world identifier is supposed to
appear anywhere else in code or config.

| Identical by design | Allowed to vary |
|---|---|
| The key set on every formation entry | The values: name, place, window, representative |
| `kind`, and `state` for worlds at the same stage | `state` where worlds are genuinely at different stages |
| `census_id` present and resolving to a live census entry | Which census entry |
| The relationship between registry and census fields | The prose in `thinness_statement`, the comments |
| `package.location` + `package.manifest_hash` both pinned | The hash |

**Found.** The key set is uniform (11 keys, six worlds). `state` and `kind`
are uniform. Every package is pinned and its manifest is on disk. One world —
`desert` — carried `census_id: null` where the other five carried a real
value (**F-01**, fixed here). And the registry disagrees with the Atlas census
on four separate fields across five worlds (**F-06** through **F-09**).

### Stage 2 — The records tree (`records/<world>/`)

| Identical by design | Allowed to vary |
|---|---|
| The record-type vocabulary and directory layout | How many records of each type |
| The id shape **and its type-token vocabulary** | The slug |
| Envelope completeness (`confidence`, `world_id`, `schema_version`) | Confidence *values* |
| The key vocabulary of any field the UI renders verbatim | The values in those fields |
| Freedom from build-process language in participant-facing fields | Everything in commentary fields and bodies |
| Which canon cells are *covered* (all 28, either route) | Whether a cell is covered substantively or by honest limit |

**Found.** Directory layout is uniform (14 types, six worlds). All 15 M1 gates
are green on all six worlds — and that is the headline of this audit, not a
reassurance: **every inconsistency found lives in the space no gate looks
at.** The gate battery is world-uniform and correct; it simply cannot see two
worlds at once, so it cannot notice that five worlds answer a question one way
and the sixth answers it another.

Four drifts here: the id type-token vocabulary (**F-03**), `figure.dates` key
vocabulary (**F-04**), quote speaker labels (**F-05**), and build-process
language inside `figure.dates` (**F-10**). Plus a set of measured, uneven
adoptions of ungated optional fields (**F-11**, **F-14**).

### Stage 3 — The compiler and the package (`engine/m2` → `packages/`)

| Identical by design | Allowed to vary |
|---|---|
| The set of compiled file *classes* emitted | The number of files in each class |
| The set of `prompt.txt` section *kinds* | The number and content of sections |
| The `frame.json` field set, all fields non-null | The values |
| Determinism, and freshness against the pinned hash | The hash |

**Found. Clean, on every axis, for all six worlds.** Each package emits the
same 14 compiled file classes, the same 3 `validation/` files, the same 19
`prompt.txt` section kinds, and a `frame.json` with all 9 fields present and
non-null. The full staleness sweep passes for all seven worlds including the
fixture. This stage is the strongest part of the system: `compile_world()` is
a pure function of records + registry entry, so it *cannot* treat two worlds
differently, and it does not.

That is worth stating plainly, because it locates every finding in this
report on one side or the other of the compiler: drift enters upstream of it
(in records and registry) or downstream of it (in the front ends), never
inside it.

### Stage 4 — The engine runtime (`engine/m4`, `engine/m5`)

| Identical by design | Allowed to vary |
|---|---|
| Every code path — no per-world branching whatsoever | Nothing in code |
| Evidence type floors, caps, budgets, thresholds | Which records those constants select |
| Facilitator and crisis text (a fixed table) | The representative name/role substituted into it |
| Anachronism *mechanism* | Which terms it flags, from each world's own `time_window` |

**Found. Clean.** A search for per-world branching across `engine/m4`,
`engine/m5` and `engine/api` returns nothing outside comments and two
measurement scripts that name `fix` deliberately. `_TYPE_FLOORS`,
`_MIN_ASK_MATCH_WORDS`, the character budget and the session turn cap are
fleet constants. Facilitator and crisis turns are a fixed table with
`{representative_name}`/`{role_label}`/`{display_name}` slots filled from
`frame.json`. Anachronism is computed from the world's own `time_window`
against fleet `modern_term` records — correctly world-parametric, which is
why `pahc` (window ends 200) flags "Trinity" and the five later worlds do
not. That difference is justified by history and is not a finding; the size
of the dictionary behind it is (**F-22**).

The doorway's three starter questions resolve to the same three canon cells
(`C-I`, `C-P`, `C-E`) for all six worlds, drawn from fleet-owned
`canon_question` records — so the doorway offers the same *kind* of opening
everywhere, with each world's own answers behind it. That is the design
working.

### Stage 5 — The API (`engine/api`)

| Identical by design | Allowed to vary |
|---|---|
| The `WorldSummary` field set returned per world | The values |
| That every formation world (and no fixture) is listed | — |
| That each world's frame is read through the same hash-verified load path | — |

**Found. Clean.** `list_worlds()` filters on `kind == "formation"`, loads each
world's real `frame.json` through the same `LazyWorldLoader` a session load
uses, and selects the same ten fields for every world. There is no second,
hand-copied description of a world anywhere in the API layer — the endpoint
exists precisely to retire one, and it did.

### Stage 6 — The front ends (`cic-poc/frontend`, `cic-website`)

This is where the second-largest cluster of findings sits, and structurally
it is the weakest stage, because it is the only one that still holds
**hand-maintained per-world tables**.

| Identical by design | Allowed to vary |
|---|---|
| Every formation world has an entry in every per-world table | The values in them (portrait, colour) |
| The rendering path — one component, one format, every world | What that path renders |
| The name a participant is given for a world, across surfaces | — |
| The name and title a participant is given for a Representative | — |

**Found.** Three separate hand-maintained per-world tables exist downstream of
the registry: `WORLD_ASSETS` + `WORLD_ORDER` in the app
(`cic-poc/frontend/src/data/worlds.ts`), `PORTRAIT_FILES` in the site
(`cic-website/index.html`), and the `entry` object on every census movement
(`cic-website/data/world-census.json`). All six worlds are currently present
in all three. But the app's table **fails silently** when one is not
(**F-15**), the census `entry` object is a fourth description of each world
that disagrees with the registry on four fields (**F-06**–**F-09**), and a
fourth, dead table (`worldIcons.tsx`) is keyed inconsistently (**F-18**).

---

## 2. Findings

Severity is about what it does, not how hard it is to fix:

- **Live** — a participant meets this today.
- **Latent** — no live effect yet; it bites the moment a field is wired, or a
  seventh world is built.
- **Fleet** — systemic, affects all six equally; not per-world drift, but it
  is what makes per-world drift invisible.
- **Hygiene** — no behavioural effect; a comment or a table that has gone
  false.

---

### F-01 — `desert` could not be reached by its own deep link · Live · **FIXED**

`records/worlds.yaml`'s `desert` entry carried `census_id: null` where the
other five formation worlds carried a real value. The Atlas sends the census
entry's own id — `cic-website/index.html` as `?worlds=${w.id}`,
`atlas-v3.html` as `data-aid="${m.id}"` — and `App.tsx` matches it with
`findWorldByCensusId(worlds, censusId)` against the registry's `census_id`.
With `null` there, `desert`'s match could never succeed, and every "Launch an
Interview with Papnoute" click fell through to the world list while the other
five went straight to the doorway.

The census entry existed all along: `desert-monasticism`, era 2, atlasId
`I.3`, status `Built & Live`. The registry comment said the value was "not
yet verified against the running Atlas frontend this session — carried as an
open item." It stayed open, and `null` is not a neutral placeholder: every
consumer reads it as "this world has no Atlas entry."

**Root cause, stated as process:** the value was optional to write, nothing
compared the two files, and the one world whose thread did not get to it was
indistinguishable from a world that genuinely had no entry.

**Disposition:** fixed in this thread — `census_id: "desert-monasticism"`,
verified against the census file directly. No recompile needed: `census_id`
is not compiled into any package (`build_frame_json` does not carry it);
`wiring.list_worlds` reads it straight from the registry. The staleness sweep
still passes for all seven worlds.

Confirmed independently, and not re-derived here: `mode=interview` /
`mode=table` in those deep-link URLs is read nowhere in the front end.
`App.tsx` honours only the first `worlds=` id and says so in its own comment.

---

### F-02 — the Atlas census contradicted itself on `hal`'s start year · Live · **FIXED**

`hieronymian-ascetic-literary` carried `"dates": "c. 382–420 CE"` beside
`"start": 380`. Its own display string, the registry's `time_window`
(382–420) and the world's records all say 382. `start` is what the front
page's Representative carousel sorts on, and what any surface reading the
census numerically gets.

**Disposition:** fixed in this thread — `start: 382`. No ordering change
results (the carousel order is unaffected between `ijc` 312 and `hal` 380/382),
which is exactly why it survived: nothing visible moved.

---

### F-03 — one world addresses two record types its own way · Latent

Five worlds address doctrinal witnesses as `<world>.dw.<slug>` and voice
craft as `<world>.voice.craft`. `pahc` uses `pahc.witness.<slug>` (17
records) and `pahc.craft.chloe-voice`.

`gate_id_convention` holds every id to `<world>.<type>.<slug>` and bans a
canon-cell code in the slug — and passes both of these, because it never
compares the middle segment *between* worlds. Its own docstring names the
cost this leaves on the table: *"Before this gate, five worlds cell-coded
their witnesses and pahc did not... At the hundred the spec plans for, it is
a corpus nobody can write a tool against."* The gate closed the cell-coding
half of that and left the type-token half open.

No live effect: only one world is resident per session, so the voice never
meets two vocabularies at once. The cost is fleet tooling — every future
script that wants "all doctrinal witnesses" needs a special case, and the
special case is one world deep.

**Disposition:** open. Renaming 17 records re-hashes `pahc`'s package and
needs a `pahc` build thread with a recompile and a registry hash update. Held
in `ACCEPTED_OPEN` as `id-type-token/doctrinal_witness` and
`id-type-token/voice_craft`.

---

### F-04 — `pahc` participants read the words "display:" and "note:" · Live

`figure.dates` is `{"type": "object"}` in the schema — no key vocabulary at
all — and `FigureBridgeMark.formatDates` renders it as
`` `${key}: ${value}` `` joined by `·`, straight into the Level-3 panel.

Five worlds key it `born` / `died` / `floruit`. `pahc` keys it `display` /
`note` / `died`. So a participant who taps a figure's name in a `pahc`
conversation reads:

> **display:** the letter is traditionally dated c. 96; the plausible range is
> broadened by current scholarship to 80-140

and, on Hermas:

> **note:** these bound the WORK, not the man - his own dates are not attested

The *content* of `pahc`'s choice is good and historically motivated — several
of its figures are churches and texts rather than men, and `born`/`died`
genuinely cannot express "these bound the work, not the man." The defect is
that the field had no vocabulary, so a legitimate semantic need turned into a
raw key on a participant's screen.

**Disposition:** open, and it needs a decision rather than a patch. Two clean
repairs: (a) give `dates` a key enum in the schema plus a label map in
`FigureBridgeMark`, so `display` renders as something like *"Dated"* and
`note` as an unlabelled line; or (b) re-key `pahc`'s figures and accept the
loss of the distinction. (a) is better — it keeps the historical honesty and
removes the leak — but it is a schema change plus a frontend change, not a
trivial fix. Held as `figure-dates-keys/pahc`.

---

### F-05 — four `syr` quotes show a database key where the speaker should be · Live

The 2026-08-26 transparency audit (`0a3ca51`, `eebd08a`) fixed exactly this
class of defect: `speaker_or_author` is authored two ways across the corpus —
a figure record id, or already-readable prose — and
`citation_cards._quote_speaker_label` now resolves a figure id through the
same label lookup a figure's own card uses.

It resolves a **figure** id. Four `syr` quotes name a **source** record:

| record | what a participant reads |
|---|---|
| `syr.quote.chronicle-flood-line` | `syr.source.chronicle-of-edessa (the anonymous chronicler, from the city archives)` |
| `syr.quote.palladius-hospitaller` | `syr.source.palladius-lausiac-history (Ephrem as remembered in Palladius's account)` |
| `syr.quote.sozomen-melodies` | `syr.source.sozomen-historia-ecclesiastica (Sozomen on the rival hymnody Ephrem answered)` |
| `syr.quote.theodoret-gnats` | `syr.source.theodoret-historia-ecclesiastica (Theodoret's telling of Jacob's prayer)` |

Both resolvers miss them for the same reason and in the same way: the string
is not a bare id (it carries a trailing gloss), so `repository_records.get()`
returns nothing, and both fall through to printing the raw string. It reaches
the Level-3 General References card *and* the compiled prompt's own quote
index, so the model reads it too. Verified by running both resolvers over
every quote in all six worlds: `syr` 4, every other world 0.

**Disposition:** open. The better repair is in code, not records — teach both
resolvers to unwrap a leading record id of *any* citable type (a `source`
resolves to its `author` / `work`, which is precisely the readable
attribution wanted). That fixes all four without authoring new
participant-facing prose, and prevents the next world from reintroducing it.
It touches `engine/m2/builders.py`, which re-hashes every package, so it
belongs to a thread that can run the full recompile. Held as
`quote-speaker-label/syr`.

---

### F-06 — the Atlas and the app disagree about which worlds are living traditions · Live

| world | census `living` | registry `living_tradition_flag` |
|---|---|---|
| `alx` | `false` | `true` |
| `pahc` | `false` | `true` |
| `hal` | `false` | `true` |
| `ijc` | `false` | `true` |
| `desert` | `true` | `true` |
| `syr` | `true` | `true` |

The registry flag drives the doorway's disclosure sentence — *"This is a
bounded historical reconstruction, not today's church of the same name."* The
census `living` flag drives the Atlas. Four of six worlds carry opposite
answers on the two surfaces a participant meets in sequence.

The registry's own comments explain how: the flag is *"PENDING Mark's own
confirmation"* on `ijc`, *"PROVISIONAL, set toward disclosure"* on `hal`,
and carried-forward-with-re-confirmation-pending on `alx` and `pahc`. Each
world set it `true` toward disclosure, correctly and independently — the
spec's fail-toward-disclosure principle. Nobody told the census, which was
generated earlier from `world_manifest.py` and still reflects the old
determinations.

**Disposition:** open, and it is Mark's, not a build thread's. The
Living Tradition determination is a named per-world touchpoint (Constitution
Art. 29; Doc_01 §1). Once ruled, the fix is one field in each file and the
standing check enforces agreement thereafter. Held as `census-living-flag/*`.

---

### F-07 — the same Representative has two titles, one per surface · Live

| world | Atlas `representativeTitle` | registry `role_label` |
|---|---|---|
| `pahc` | Host of the Assembly | Household Leader |
| `syr` | Teacher of the Covenant Order | Mar |
| `desert` | Elder of the Desert | Abba (Elder) |
| `ijc` | Apocrisiarius — Deacon of the Letters | Deacon of the Letters |
| `alx` | Catechetical Teacher | Catechetical Teacher |
| `hal` | Widow of the Household | Widow of the Household |

Four of six. A participant reads "Chloe, Host of the Assembly" on the Atlas
card, clicks through, and meets "Chloe, Household Leader" at the doorway.

Two of these have a documented reason and two do not. `ijc`'s pair is a
prefix difference from Mark's own 2026-07-22 ruling ("Apocrisiarius — Deacon
of the Letters"), where the registry carries the second half only. `desert`'s
is a gloss difference on the same word. `pahc`'s and `syr`'s are simply
different titles.

**Disposition:** open, Mark's call — this is participant-facing copy, and
picking one of two good phrasings is not a build thread's decision. Held as
`census-role-label/*`.

---

### F-08 — `syr`'s Representative has two names · Live

Census `representativeName` is `Mar Yausep`; the registry is `name: Yausep`,
`role_label: Mar`. Everything downstream of the registry composes the two,
so the app says "Yausep" as a name and "Mar" as a role, while the Atlas says
the name is "Mar Yausep." The registry's own comment records the role being
revised Malpana → Deacon → Mar by Mark's rulings; the census kept the earlier
composite.

**Disposition:** open, Mark's call. Held as `census-representative-name/syr`.

---

### F-09 — one world's `display_name` follows a different convention · Live

Five worlds set the registry `display_name` to the census's formal `name`
(`Post-Apostolic House-Church Christianity`, `Desert Monasticism`, …). `alx`
sets it to the Atlas's *friendly* name, `Alexandrian Christianity`, where the
census's formal name is `Alexandrian Catechetical / Christian-Platonist
Tradition`.

`display_name` is compiled into `frame.json`, served by `/api/worlds`, shown
on the world card and the doorway, and substituted into the Facilitator's
door line. So five worlds greet a participant with a formal academic name and
one greets them with a friendly one — a difference in register with no
documented reason, on the world a participant is most likely to meet first
(it sorts second on the site and first in the app).

This one is arguably the *better* convention and the other five should follow
it. Either way it should be a decision, not an accident.

**Disposition:** open, Mark's call — one convention, applied to all six. Held
as `census-display-name/alx`.

---

### F-10 — `desert`'s figure dates carry build-process language onto a participant's screen · Live

Three fields across two `desert` figures carry text that was written for a
reviewer and is rendered verbatim in the Level-3 panel:

- `desert.figure.evagrius.dates.born` and `.died` — the literal record id
  `desert.source.evagrius-praktikos`, plus a reference to the build document
  `Doc_01 SS2.3`, in both fields
- `desert.figure.pachomius.dates.floruit` — *"its incident-level reliability
  is not independently adjudicated by this build"*

**Corrected 2026-08-26, same day.** This finding was first written up as
*six* fields, adding `desert.figure.antony.dates.born/died/floruit` on the
strength of the strings `Vita SS89`, `Vita SS92-93` and `Vita SS2`. Those are
not leaks. This project writes the section sign as `SS`, so they read *Vita
§89* — real primary-source loci in the Life of Antony, exactly the checkable
reference a participant is supposed to be shown. Desert uses that convention
in 44 of its 192 source loci, more than any other world, which is why the
false positives landed here and nowhere else. The pattern in
`check_participant_field_leaks` was matching a bare `SS<n>` and has been
narrowed to require a named build artifact (`Doc_`, `Artifact-`, `BUILD-LOG`)
or build prose. Antony's three dates are clean and were always clean.

`gate_no_build_attribution` exists for precisely this defect class and would
have caught the phrasing — but its `_ATTRIBUTION_FIELDS` map is scoped to the
fields `build_prompt()` compiles, and `figure.dates` is not one of them. That
scoping decision was correct when it was made (see F-20); `figure.dates`
became participant-facing later, when the name/figure bridge was built, and
nothing extended the map.

`desert` is the only world with hits, but that is not because the other five
were more careful in this field — it is because their `dates` values are
shorter. The exposure is fleet-wide; `desert` is where it landed.

**Disposition:** open. The repair is two-part: extend the gate's field map to
the fields the UI actually renders (F-20), then clean the six values. Held as
`ui-field-leak/desert`.

---

### F-11 — retrieval reach differs by build effort, and reads like a thinner world · Live · systemic

`retrieval.retrieve_when` is the one retrieval field the live turn loop
actually reads. `engine.m1.canon.retrieval_hint_keywords` credits each
record's hint text to the cells it serves, and `evidence.match_asks_to_cells`
uses it to fill Stage A slots the fleet canon vocabulary left empty. Its own
docstring gives the worked case: *"What was it like when the plague came?"*
reached no cell at all until `alx.story.plague-nursing`'s own
`retrieve_when: "sickness, death, plague, care for the dying"` was allowed to
widen it.

Adoption across the fleet, over records that carry a retrieval block at all:

| world | with `retrieve_when` | distinct hint phrases |
|---|---|---|
| `pahc` | 43/43 (100%) | 90 |
| `desert` | 40/40 (100%) | 87 |
| `alx` | 59/72 (82%) | 121 |
| `hal` | 35/51 (69%) | 67 |
| `ijc` | 21/33 (64%) | 57 |
| `syr` | 19/41 (46%) | 40 |

This is not a content difference. It is a difference in how much retrieval
tuning each build thread did, and it produces a *behavioural* difference at
turn time: a `syr` participant asking a question phrased outside the fleet
canon vocabulary is materially less likely to reach ground than a `pahc`
participant asking the equivalent question. The system then reports that as
the world's honest limit — which is the one failure mode this project most
needs to avoid, because it makes a build gap indistinguishable from a
historical silence.

Nothing gates it: `gate_distribution_health` only fires if *every*
chunk-feeding record shares one tier, and `retrieve_when` is a typed-empty
array whose empty state is legitimately "no hints."

**Disposition:** open, and this is the finding with the largest live effect
on conversation quality. It is not fixable by a rule (a floor would invite
padding); it wants a per-world hint-writing pass on the four worlds under
100%, prioritised by `syr`. The standing check reports the ratio every run so
the gap stays visible. Held as observation `retrieval-hint-coverage/*`.

---

### F-12 — every world authors `do_not_retrieve_when`; nothing enforces it · Fleet

125 records across the six worlds carry `do_not_retrieve_when` (`alx` 40,
`pahc` 29, `syr` 19, `ijc` 16, `desert` 11, `hal` 10). No runtime path reads
it as an exclusion. Its only appearance in `engine/m4` is in
`evidence._FALLBACK_EXCLUDED_KEYS`, which stops the fallback text search from
*matching on* it — the sharp reason given in that comment, *"matching on it
would retrieve a record's own list of reasons NOT to retrieve it"* — which is
the opposite job from enforcing it.

So a builder who wrote "do not retrieve this when the question is about
marriage" has recorded an instruction that is never followed, and the worlds
that invested most in it (`alx`, `pahc`) got nothing for the effort.

**Disposition:** open, fleet-level. Either wire it or retire it from the
schema; leaving it half-present teaches every future world builder to write a
field that does nothing. Reported every run as
`unread-retrieval-config/*`.

---

### F-13 — `retrieval.tier` is authored by every world and read by no runtime path · Latent · Fleet

Tier is read in exactly two places: `gate_distribution_health` (a degeneracy
check — it fires only if every chunk-feeding record shares one tier) and
`m1/mutate.py` (fixture defect seeding). Evidence assembly ranks by overlap
coefficient and per-type floors; tier plays no part.

Meanwhile the six worlds have drifted far apart on what tier *means*:

| world | tier 1 / 2 / 3 |
|---|---|
| `alx` | 59 / 13 / 0 |
| `pahc` | 16 / 22 / 5 |
| `desert` | 20 / 16 / 4 |
| `hal` | 26 / 21 / 4 |
| `syr` | 27 / 12 / 2 |
| `ijc` | 22 / 8 / 3 |

`alx` marks 82% of its retrievable records tier 1 and uses tier 3 not at all;
`pahc` marks 37% tier 1. If tier is ever wired to influence ranking, `alx`
will behave as though everything is equally central and `pahc` will have a
real priority ordering — a difference in *retrieval behaviour* produced
entirely by six threads reading the same one-line field description
differently.

**Disposition:** open, latent. Before tier is wired, one fleet-wide
definition of what each tier means, then a re-tiering pass. Reported every
run alongside F-12.

---

### F-14 — `desert` fills `sources[].license` on 42% of its source references · Latent

| world | `sources[]` entries carrying a `license` |
|---|---|
| `alx` | 254/254 |
| `syr` | 246/246 |
| `hal` | 215/215 |
| `ijc` | 201/201 |
| `pahc` | 189/189 |
| `desert` | **80/192** |

`gate_rights` checks that every `source` *record* has a `rights_status`, and
that passes everywhere. The per-reference `license` on the envelope's
`sources[]` array is separate, ungated, and read by nothing today — but it is
a rights field, and five worlds treat it as required while one treats it as
optional.

**Disposition:** open. Low urgency (nothing reads it) but it is the kind of
field that becomes load-bearing exactly when someone needs to answer a rights
question quickly. Reported every run as `source-ref-license/*`.

---

### F-15 — a world missing from the frontend's asset table disappears without an error · Latent

`useWorlds.toEntry()` returns `null` when `WORLD_ASSETS[summary.world_key]`
is absent, and the caller filters nulls out. A world that is built, gate-
green, compiled, pinned, admitted, and correctly returned by `GET /api/worlds`
simply does not appear on the world list, with no error in the console, no
degraded card, and nothing in the API response to indicate a problem.
Separately, a world absent from `WORLD_ORDER` gets `indexOf === -1` and sorts
*ahead* of every listed world.

All six are present today, so this is latent — but it is the failure mode a
seventh world build will meet, and it fails silent, which is the worst
available behaviour for a project whose whole discipline is failing toward
disclosure.

**Disposition:** open, and cheap. The right fix is a visible fallback (a
neutral portrait and colour) plus a console error, so a missing asset degrades
loudly. The standing check covers it in the meantime
(`check_app_world_assets`), which is the difference between "nobody notices
for a week" and "CI says so on the commit."

---

### F-16 — one world carries three participant-facing names, and two surfaces order the worlds differently · Live · systemic

Every world has three distinct names before the registry is even consulted —
census `name`, census `shortName`, census `entry.worldName` — plus the
registry's `display_name`. For `alx`: *Alexandrian Catechetical /
Christian-Platonist Tradition*, *Alexandria*, *Alexandrian Christianity*.

That the Atlas uses a formal name in one view and a friendly name in another
is a legitimate design. That the *fourth* name (the registry's, which is what
the app shows) sometimes matches one of them and sometimes matches none is
not — see F-09.

Ordering diverges too: the site's carousel sorts chronologically by census
`start` (pahc, alx, syr, ijc, desert, hal); the app's `WORLD_ORDER` is a
fixed Stage-7.5 list (alx, pahc, desert, hal, syr, ijc) that is neither
chronological nor the registry's own file order (alx, desert, pahc, hal, syr,
ijc). Three orderings of six worlds across three files.

**Disposition:** open, presentation-level, Mark's call. Named here because it
is the same root as F-07/F-08/F-09 — participant-facing identity is described
in more than one place and nothing compares the descriptions.

---

### F-17 — one census `dates` string breaks the house style · Hygiene

Five worlds render as `c. 320–430 CE` (en dash, `CE` suffix). `ijc` renders
as `c. 312-451` — ASCII hyphen, no era suffix. Displayed on the Atlas card.

**Disposition:** open, deliberately not fixed here despite being one
character. Typography of participant-facing copy is a house-style call, and
"five of six do it this way" is evidence, not authority. One line to change
whenever Mark says so.

---

### F-18 — a dead per-world table, keyed inconsistently · Hygiene

`cic-poc/frontend/src/data/worldIcons.tsx` exports `WORLD_ICONS`, documented
as *"Keyed by world_id (world_manifest.py)"*. It is imported nowhere — its
only consumer, `LivingTableScene`, does not exist in the tree. Five of its
keys are world_ids; the sixth is `imperial-juridical-christianity`, which is
`ijc`'s **census** id — its `world_id` is `imperial-juridical`.

Harmless today (dead code), and a precise illustration of the underlying
hazard: `ijc` is the one world whose `world_id` and `census_id` differ, and
the one place that difference was ever consumed got it wrong.

**Disposition:** open. Delete the file, or revive it with registry-derived
keys. Not fixed here — deleting a 190-line asset file is a frontend thread's
call, not an audit's.

---

### F-19 — a schema comment describes a fleet uniformity that does not exist · Hygiene

`engine/m1/schemas.py`'s `fleet_voice` comment states that *"the per-world
`voice_craft.flavor_notes` 'self-reference' entry duplicates the pronoun rule
across all six worlds today."* Five worlds carry a `self-reference` segment;
`pahc` does not (its four segments are `term-introduction`,
`correspondence`, `leadership`, `table`).

The flavor-note segment vocabulary is 13 distinct labels across six worlds,
only `term-introduction` universal. Much of that is legitimate — `ijc`'s
`three-strands` and `homoian-recentering` are that world's real voice
problems, and inventing a shared vocabulary would flatten them. But
`openers`, `place` and `honest-limits` are generic craft segments present in
some worlds and absent from others for no recorded reason, and the comment
above shows the cost: a maintainer reasoned about a fleet-wide invariant that
was never true.

**Disposition:** open. Correct the comment; separately, decide whether the
generic segments are a required floor.

---

### F-20 — the attribution gate guards the model's input, not the participant's screen · Latent · structural

`gate_no_build_attribution` scans exactly the fields `build_prompt()`
compiles, and its comment defends that scoping carefully and correctly
against a real 2026-08-21 audit: widening it to every string on those record
types produced false positives on legitimate commentary, so *"scanning them
would drown real findings in noise."*

That reasoning was sound for the surface that existed then — the model's
system prompt. Since then a second participant-facing surface was built (the
three-level transparency system: `citation_cards`, `name_bridge`,
`term_glosses`, `SourceList`), and it renders fields the gate does not
watch: `figure.dates`, `figure.bridge_line`, `figure.names[].name`,
`quote.speaker_or_author`. F-05 and F-10 are both consequences.

**Disposition:** open, and this is the structural repair that prevents the
recurrence of two findings rather than fixing their instances. Add a second
field map covering the UI render path, scoped the same disciplined way. The
standing check implements a first version of exactly this
(`check_participant_field_leaks`), deliberately narrow, as a stopgap until it
lands in the gate battery where it belongs.

---

### F-21 — a dead id-remap and a comment asserting a discrepancy that no longer exists · Hygiene

`cic-website/index.html` carries:

```js
const CENSUS_ID_FIX = { 'imperial-and-juridical-christianity': 'imperial-juridical-christianity' };
```

with a comment describing it as a *"Known discrepancy, not silently patched…
corrected here so the interview link actually works, not fixed at the source
in this pass."* No census entry has the id `imperial-and-juridical-christianity`
— the census already says `imperial-juridical-christianity`, so the map is a
no-op and the comment describes a state of the world that has since been
repaired at the source.

**Disposition:** open, hygiene. Not fixed here (it is website code, and the
audit's fix mandate was registry and config values), but the comment is
actively misleading: it tells the next reader a live inconsistency exists
where none does.

---

### F-22 — the anachronism dictionary has one entry, so five of six worlds get no anachronism coverage · Fleet

`records/_fleet/modern_term/` holds a single record: `_fleet.modern.trinity`,
`origin_year: 325`. `engine.m5.anachronism` flags a term when its origin year
postdates the world's window, so:

| world | window ends | flagged |
|---|---|---|
| `pahc` | 200 | `trinity` |
| `alx` | 400 | none |
| `syr` | 410 | none |
| `hal` | 420 | none |
| `desert` | 430 | none |
| `ijc` | 451 | none |

The mechanism is correct and correctly world-parametric. But with one entry
in the dictionary, the M5 anachronism route is exercised on `pahc` alone and
is untested in practice on the other five — a per-world difference in
*safety-relevant coverage* produced by fleet-level thinness rather than by
any world's own history.

**Disposition:** open, fleet-level. Not per-world drift, recorded here
because it looks exactly like per-world drift from the outside and would be
misdiagnosed as such.

---

### F-23 — every witness record explains its own limits, and the voice is never shown that explanation · Live · Fleet

Found by tracing a real complaint: asked *"who is Jesus"*, `desert` answered
with Antony's conversion and the inward struggle — a faithful, near
sentence-for-sentence rendering of `desert.dw.jesus`, the single record
covering cell C-I ("Who was Jesus, to you and your people?"). The pipeline
did its job. The participant's objection was that it told a founding story
instead of saying what the world held about Christ.

That record anticipated the objection exactly. Its `tensions` field reads:

> a lived, imitative Christology against a stated, defended one — this world
> left little in its own voice arguing who Christ was, compared to how much
> it left showing what following him cost

and its body says the oblique answer is deliberate, *"honestly named rather
than filled with invented doctrine."*

None of that reaches the model. `build_prompt` emits a witness as
`emit(f"Witness ({cells})", witness.get("text"), witness["id"])` — the `text`
field and nothing else. `positions` and `tensions` are both in
`COMPLETION_REQUIRED`, both authored on **94 of 94** doctrinal_witness
records across the fleet, and compiled into **zero** prompts. Verified
directly against the compiled bytes: `desert.dw.jesus`'s text is in
`compiled/prompt.txt`; its tensions sentence is not.

This is the same shape as F-12 (`do_not_retrieve_when`) and F-13
(`retrieval.tier`) — a field the gates require and nothing reads — but it is
the costliest instance, because what goes unread here is precisely the
world's own account of where its witness runs thin. The voice is given the
oblique answer and withheld the sentence that says it is oblique, which is
the whole difference between an answer that reads as evasive and one that
reads as honest. It is the project's central commitment, authored six times
over, never delivered.

Two aggravating facts, both measured:

- **`desert` is thinnest here by some way.** C-I holdings: `alx` 6
  substantive records, `ijc` 4, `hal` 3, `syr` 3, `pahc` 2, `desert` 1. Every
  other world holds at least one *quote* in that cell — someone's actual
  words about Jesus. `desert` holds none, so there was nothing for the voice
  to quote even if it had reached for it. That is content density, which this
  audit does not treat as a defect; it is recorded because it sets how much
  the uncompiled caveat was carrying.
- **The question is fragile to phrasing.** `"who is Jesus"` reduces to one
  content word, and `_MIN_ASK_MATCH_WORDS = 2`, so Stage A matches no cell at
  all and the Stage A2 fallback returns nothing for `desert`. The doorway's
  own starter — *"Who was Jesus, to you and your people?"* — matches `C-E`
  and `C-I` cleanly. A live turn survives this only because the reader's
  extracted `asks` widen the query; the bare message does not.

**Disposition:** open, fleet-level, and the highest-value repair in this
report. Compiling `tensions` beside `text` (and deciding whether `positions`
belongs too) is a `build_prompt` change, so it re-hashes all seven packages
and belongs to a thread that can run the full recompile and re-check voice
quality against the pilot baseline. It should be measured, not assumed: the
prompt grows, and `engine/BASELINES.md` names the state to compare against.

---

### F-24 — `desert` reports an acquisition gap to participants as a historical silence · Live

The direct follow-on from F-23, and the more serious half. Mark's objection to
desert's "who is Jesus" answer was not that the voice misread its ground — it
was that the world *does* have Christological material and said it did not.
Checked against desert's own source ecology, he is right, and the cause is
locatable:

| source Mark named | in desert's registry? | vendored text? | cells it feeds |
|---|---|---|---|
| Antony, *Letters* | yes (`antony-letters` + Rubenson) | **no** — none vendorable | F2-E, F4-I, F4-P — never C-I/C-T |
| Evagrius, *Praktikos* etc. | yes (`evagrius-praktikos`) | **no** — none vendorable | 7 cells — never C-I/C-T |
| *Apophthegmata Patrum* | yes (`apophthegmata-patrum`) | **no** — never landed | 16 cells — never C-I/C-T |
| Cassian | yes (Conferences + Institutes) | **yes**, `npnf211` | F4-I only |
| Pseudo-Macarius | **absent** | — | — |

**Every record in C-I and C-T rests on one source: `athanasius-vita-antonii`.**
Nothing else reaches either cell.

**Corrected 2026-08-26, on Mark's challenge.** A first draft of this finding
filed all three unvendored sources under "rights-blocked." That conflates two
different constraints, and the difference decides who can fix them.

`cic/engine/texts_registry.py` — the registry `cic/texts/README.md` is
generated from — records that **45 of the 46 vendored files were supplied by
Mark** (the 46th, a public-domain Bible, by Claude at his direction), and why
they had to be: *"the
sandbox this project's agents run in blocks every patristic text host
(ccel.org, newadvent.org, wikisource, archive.org, gutenberg,
tertullian.org)."* No build thread has ever fetched a text. The corpus is
entirely Mark's downloads, overwhelmingly the CCEL ANF/NPNF sets. So
"unvendored" never means "unavailable" — it means *nobody asked Mark, or
asked and it was not actioned*. The two constraints:

- **No public-domain English exists.** Antony's *Letters* and Evagrius. The
  surviving-version originals are public domain; the usable English
  translations (Rubenson 1995, Bamberger 1970) are in copyright, and both
  carry a `not_found` search record. No download fixes this. Earned.
- **Public-domain English exists and was never obtained.** The
  *Apophthegmata*. Budge 1907 is out of copyright and downloadable — by Mark,
  from the same kind of source as everything else in `cic/texts/`. The
  manifest's own stated blocker is the sandbox, not copyright. This is a
  request that sat open, not a limit of the record.

Two of the four are therefore not earned at all:

- **The Apophthegmata was never vendored, and it is the world's central
  teaching corpus.** `SOURCE-REQUEST-MANIFEST.md` item G1 identifies Budge's
  1907 *Paradise of the Holy Fathers* vol. 2 as "the only public-domain
  English Apophthegmata corpus in existence", rates it **P1**, and records
  why it is still open: *"This session could not fetch it: network policy
  blocks archive.org file downloads."* The manifest states the consequence
  itself — *"until this file lands, every saying in the record set is license
  `paraphrase-only` and no verbatim saying can be voiced."* That is why
  desert is the only world in the fleet with paraphrase-only quotes. The
  Apophthegmata is cited by 42 records across 16 cells from consult knowledge,
  and routed to Christology in none of them.
- **Cassian's own Christological treatise is vendored and unused.**
  `cic/texts/npnf211_...xml` is in the tree and contains *On the Incarnation
  of the Lord against Nestorius* (19 matches). The build used that file for
  Conferences/Institutes ascetic vocabulary in a single cell and never
  touched the one direct Christological treatise inside its own corpus.

And the corpus is under-drawn more broadly than desert alone. Of the 46
vendored files, **20 are reached by no world at all** — including Basil
(`npnf208`, 43 matches for "Ascetic", 50 for "monk"), Gregory Nazianzen
(`npnf207`), Gregory of Nyssa (`npnf205`) and Chrysostom's ascetic homilies
(`npnf109`), all of them directly adjacent to desert's own subject. Desert
draws on 6 of the 46, and only **76% of its sourced records rest on a
vendored text** — the lowest in the fleet, against pahc's 99% and alx's 96%
(see `CORPUS-USE.md`). Jerome's desert *Lives* (Paul the Hermit, Hilarion,
Malchus) sit in `npnf206`, a file desert already uses for other purposes.
The gap between what was supplied and what was reached for is larger than
the gap between what was supplied and what exists.

**The overclaim.** `desert.limit.doubt-and-doctrine` is careful and well
argued — but it is scoped to `C-T` and `F1-P`, and its claim is about *how
his death saves*, a genre argument about sayings-literature. It never covers
`C-I`, the cell "who is Jesus" actually lands in. What covers C-I is
`desert.dw.jesus`, whose `tensions` field generalises much further: *"this
world left little in its own voice arguing who Christ was."* That sentence
describes the Vita Antonii, applied to the whole world — and by F-23 it never
reaches the model anyway, so the participant gets the generalisation's
*effect* without its reasoning or its bounds.

This is F-11's failure mode arriving in full: a build gap rendered
indistinguishable from a historical silence, in the one place where the
project's credibility most depends on the difference.

**Disposition:** open. The highest-leverage single action is not a records
rewrite and not an agent task: it is **Mark supplying one public-domain
file** — Budge vol. 2, `archive.org` identifier `ParadiseOfTheHolyFathersV2`
— the same way he supplied the other 36. That unlocks verbatim sayings across
the whole desert corpus and puts the Christ-in-the-neighbour, kenosis and
Christ-invoked-in-warfare material within reach of C-I and C-T. Mining
Cassian's *On the Incarnation* needs no acquisition at all. Neither is this
audit's to perform: both are content work for a desert build thread, and both
change the package.

**Scope note.** Content depth is out of this audit's scope by the launch
brief, and this finding does not ask for depth to be normalised across
worlds. It reports a *process* fact: a world states a silence its own source
ecology does not support, and the statement reaches a participant as history.

---

### F-25 — three vendored volumes of in-window primary text are read by no world · Live

The fleet-wide form of F-24, and separable from it: F-24 is about a text
`desert` could not get. This is about text every world already has.

Mark's ruling on scope, 2026-08-26: **Basil and the Gregories are in.** With
that settled, three of the twenty unread volumes are a real gap, and the
figures inside them are demonstrably live in the builds already:

| figure | vendored in | named in records | cited from his own works |
|---|---|---|---|
| Basil (d. 379) | `npnf208` | `alx` 2, `syr` 2, `desert` 1, `ijc` 1 | **none** |
| Gregory Nazianzen (d. 390) | `npnf207` | `alx` 2, `ijc` 1 | **none** |
| Gregory of Nyssa (d. 395) | `npnf205` | **none anywhere** | none |
| Cyril of Jerusalem (d. 386) | `npnf207` | **none anywhere** | none |

All four sit inside five of the six worlds' time windows; `pahc` (70–200) is
correctly out of range for every one of them, which is the control that says
this measure is not just flagging noise.

Two of these are sharper than the rest:

- **`desert` reaches Basil only through Palladius.**
  `desert.figure.evagrius` records that Evagrius was "ordained reader by
  Basil of Caesarea, then deacon by Gregory Nazianzen," sourced to *Lausiac
  History* ch. XXXVIII. Both men's own works are vendored and neither is
  opened. Given F-24 — desert's Christology resting entirely on one
  hagiography written from outside the world — the unread ascetic corpus of
  the man who ordained its most systematic author is not a small omission.
- **`alx` is the catechetical world and has never opened the century's
  catechetical text.** Cyril of Jerusalem's *Catechetical Lectures* are in
  `npnf207`, vendored, in-window, and named in no `alx` record.

**Also settled by the same ruling, in the other direction:** the World
English Bible (`webbe`) is cited by nothing, and that is **correct by
design**. Mark: scripture is in this corpus only as the authors themselves
used it; the project does not interpret the Bible directly. `CORPUS-USE.md`
now records that verdict against the file, so no future audit re-raises it as
a gap. The same holds for `anf10`, a bibliographic index with nothing to
cite.

**Disposition:** open, per-world content work, and explicitly *not* a
normalisation demand — whether a given world should draw on Basil is that
world's own source-ecology judgment, not this audit's. What the audit
establishes is narrower and checkable: the text is in hand, the figures are
already named in the records, and nothing has read them. The remaining 15
unread volumes are reported as **not yet reviewed** rather than assumed
correct; most are plainly out of every window, but this audit has no standing
to rule on them.

---

## 3. What was checked and found clean

An audit that lists only defects misrepresents the system. These were checked
across all six worlds and are genuinely uniform:

- **The M1 gate battery.** 15/15 green on all six worlds and the fixture.
- **The compiler.** Same 14 compiled file classes, same 3 validation files,
  same 19 prompt section kinds, `frame.json` with all 9 fields non-null, for
  every world. `compile_world()` is a pure function and treats no world
  specially.
- **Package freshness.** The full staleness sweep passes for all seven
  worlds: every pinned manifest hash still matches a fresh recompile.
- **Runtime code.** No per-world branching anywhere in `engine/m4`,
  `engine/m5` or `engine/api`. Every threshold, floor, cap and budget is a
  fleet constant.
- **Record envelopes.** `world_id` and id prefix agree with the registry on
  every one of the 897 records; `schema_version: 2` throughout; the full
  four-field `confidence` block present on every record in every world.
- **Record-type layout.** The same 14 directories in every world.
- **The doorway's starters.** The same three canon cells for all six worlds,
  from fleet-owned canon questions.
- **The API contract.** The same ten `WorldSummary` fields per world, read
  through the same hash-verified load path, fixture correctly excluded.
- **Frontend table membership.** All six worlds present in `WORLD_ASSETS`,
  `WORLD_ORDER` and `PORTRAIT_FILES` (the *mechanism* is fragile — F-15 — but
  the current data is complete).

---

## 4. What this thread changed

Per Mark's ruling at thread start — *fix trivial and unambiguous, document the
rest* — exactly two data values were changed, both contradictions rather than
judgment calls:

| change | file | finding |
|---|---|---|
| `census_id: null` → `"desert-monasticism"` | `records/worlds.yaml` | F-01 |
| `"start": 380` → `382` on `hieronymian-ascetic-literary` | `cic-website/data/world-census.json` | F-02 |

Everything else is documented and handed off. Nothing was recompiled; no
package hash changed; the staleness sweep and the full collectible engine
test suite pass.

Deliberately **not** fixed despite being small: F-17 (one character, but
participant-facing typography is a house-style call) and F-21 (website code,
outside the registry-and-config fix mandate). Both are one-line changes
whenever their owner says so.

---

## 5. What this thread left behind

`engine/m1/cross_world.py` — the standing check, and the second half of
Mark's ruling.

It is the fleet-level counterpart to `gates.py`. Every gate in that battery
runs against one world in isolation, which is why all fifteen are green while
the fleet holds the findings above. This module is the missing view: twelve
`check_*` functions asserting fixed cross-world contracts, and four
`observe_*` functions that measure and never threshold.

```
python -m engine.m1.cross_world          # report; exit 1 on new drift
python -m engine.m1.cross_world --all    # also print the accepted-open detail
```

The mechanism that makes it useful rather than noisy is `ACCEPTED_OPEN`:
every defect this audit found and did not fix is listed there with the
finding that owns it and why it is somebody else's next step. **A defect with
no entry is new drift, and new drift fails the run.** Removing an entry is
what "fixed" means. `engine/m1/tests/test_cross_world.py` pins both
directions — the fleet carries no undocumented drift, *and* no
`ACCEPTED_OPEN` entry has gone stale, so a repair that lands without its
waiver being removed is caught too.

Current state: **0 new defects, 16 accepted-open, 24 observations.**

What it enforces, in one line each: the registry entry key set and no null
fields; package pinning; that every `census_id` resolves to a live census
entry and no live entry is orphaned; registry-vs-census agreement on window,
living flag, representative name, title and display name; the record-type
directory set; the id type-token vocabulary across worlds; record `world_id`
and id prefix; the `figure.dates` key vocabulary; that no participant-facing
field carries a record id or build reference; that every quote's speaker
resolves to a readable label through the real resolvers; that every world has
frontend assets and an order position; and that every world has a site
portrait. It measures, without judging: retrieval-hint coverage, tier spread,
`do_not_retrieve_when` adoption, source-reference licensing, and optional
field adoption.

**A seventh world build should run it before it asks to be admitted.** Every
finding above is something a build thread could have caught in seconds if
anything had been comparing worlds; nothing was, until now.

---

## 6. Open items

For Mark — decisions, not work:

1. **Living Tradition determinations** (F-06) — four worlds carry a pending
   or provisional flag, and the Atlas disagrees with all four. This is a
   named per-world touchpoint.
2. **One title per Representative** (F-07, F-08) — five titles and one name
   differ between the Atlas and the app.
3. **One `display_name` convention** (F-09) — formal name or friendly name;
   five worlds do one thing and `alx` the other.
4. **`do_not_retrieve_when`: wire it or retire it** (F-12) — 125 records
   carry an instruction nothing follows.

For build threads — work, scoped:

5. **`syr`** — the four source-attributed quote speakers (F-05), best fixed
   in the resolvers rather than the records.
6. **`pahc`** — the `figure.dates` key vocabulary (F-04) and the id
   type-token rename (F-03), both requiring a recompile.
7. **`desert`** — the six build-provenance leaks in `figure.dates` (F-10) and
   the `sources[].license` gap (F-14).
8. **Retrieval tuning** (F-11) — a `retrieve_when` pass on `syr` (46%),
   `ijc` (64%) and `hal` (69%). Largest live effect on conversation quality
   of anything in this report.
9. **Engine** — extend `gate_no_build_attribution` to the UI render path
   (F-20); give a missing frontend asset a loud failure instead of a silent
   drop (F-15).
10. **Basil, the Gregories, Cyril** (F-25) — three vendored volumes of
   in-window primary text, read by no world, with the figures already named
   in the records. No acquisition needed. Per-world judgment, not a
   normalisation.
11. **Vendor Budge vol. 2** (F-24). One public-domain file, rated P1 by
   desert's own source manifest, blocked only by a build session's network
   policy. Unlocks verbatim sayings fleet-wide for desert and puts real
   Christological material within reach of C-I/C-T. Mining Cassian's *On
   the Incarnation*, already vendored, needs no acquisition at all.
12. **Compile `doctrinal_witness.tensions`** (F-23). 94 of 94 witness records
   carry a gate-required sentence naming where that witness runs thin, and
   the voice has never once been shown one. Highest-value repair here;
   needs a full recompile and a voice-quality check against
   `baseline/pilot-2026-08-24`.
