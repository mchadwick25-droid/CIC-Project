# alx — Build Log

Per-session build history for the Alexandria (Catechetical-Formation) world's
compiled/participant-facing records — the counterpart to
`Build/worlds/alx/Open_Gaps_Tracking.md`, which tracks what is still open rather
than what has already been done and settled.

---

## world_front record build — 2026-09-19/20

**Record built:** `Build/worlds/alx/surface/world_front/alx.front.alexandria-catechetical.md`
(`skim`, `orientation`, and `narrative` only; `facilitator_brief` is a
separate, later record this pass did not build). The fourth world in the
fleet-wide `world_front` rollout, following the two-world pilot
(desert-monasticism, syriac-edessa-nisibis) and the third world
(cappadocian) — all merged under the Website V2 world_front design
(approved to proceed 2026-09-19).

### Worktree base-fix

At session start, this worktree's `HEAD` was found on commit `e2291dfb`
("Merge pull request #301: voice_craft readability + prompt-budget
gates"), a different, unrelated merge — not a descendant of
`claude/amazing-lovelace-coy644` — and the sibling desert world_front file
did not exist in that checkout. Per the session's own instruction, no
manual merge or re-implementation was attempted: `git fetch origin
claude/amazing-lovelace-coy644` followed by `git reset --hard
origin/claude/amazing-lovelace-coy644` moved `HEAD` to `ff679fcc` ("Merge
cappadocian world_front content"), confirmed by the presence of the
desert, syriac, and cappadocian world_front files and by `git log -1`
showing the correct merge commit.

### World key

`records/worlds/alx.yaml` (read via `engine.m1.registry.load_registry()`)
gives `world_id: alexandria-catechetical` and `census_id:
"alexandria-catechetical"` — the same string, matching both pilot worlds
(desert, syriac), not cappadocian's divergence (where `world_id` and
`census_id` differ). This confirmed the record's id/filename convention:
`alx.front.alexandria-catechetical`, matching
`<registry-code>.front.<world_id-slug>`.

### Sourcing method

Every unit's `grounded_in` names a record this session opened and read
directly: `alx.core.alexandria` for the world-level frame; the four
`figure` records for `orientation.voices`; `gravity`, `force`, and
`story` records for `orientation.story`; `alx.dw.was-jesus-god`,
`alx.term.homoousios`, and `alx.contested.origen-positions` for
`orientation.floor_note`; `alx.force.transmission-ending`,
`alx.source.origen-philocalia`, and `alx.contested.origen-positions` for
`legacy`; `alx.contested.desert-attribution` for `relations_summary`. No
unit restates a claim from `cic-website/data/world-census.json` or
`atlas-v3.html` without first checking it against the record(s) it cites.

### Site-prose reconciliation

Six claims found on the live site were checked directly against this
world's own records before deciding whether to carry them into the
compiled record:

1. **"Scholarship parent of the Bethlehem Circle"** (`world-census.json`
   `relationsSummary`) — no record anywhere in `records/alx/` registers a
   relationship between Alexandria and the Bethlehem/Hieronymian world
   (`hal`). Likely true as general church history, but not this world's
   own registered evidence. Dropped from `relations_summary`; only the
   desert-monasticism relationship (grounded in
   `alx.contested.desert-attribution`) was kept.
2. **"Shaping how the East and West alike read Scripture"** (site
   `legacy`) — the only registered force record on this point,
   `alx.force.transmission-ending`, names only "Eastern Christianity
   broadly." The "and West alike" clause was dropped as unsupported;
   `legacy` states only the Eastern transmission the record actually
   makes.
3. **"Ambrose and Jerome read him closely... even when careful about
   saying so"** (site `legacy`) — no alx figure record exists for
   Ambrose, and no source/force record registers his reception of
   Origen at all. Jerome's registered relationship to Origen is
   adversarial (`alx.contested.origen-positions`), not admiring. Both
   claims dropped; the grounded material (interested, adversarial
   transmission) was folded into `legacy` instead.
4. **"Fed directly into Egyptian monasticism, giving the desert its
   intellectual vocabulary"** (site `legacy`) — this is precisely the
   claim `alx.contested.desert-attribution` holds open rather than
   settles (it concedes real transmission but refuses "the desert's
   formation logic as Alexandria's own"). Not carried into `legacy`; the
   desert relationship is handled only in `relations_summary`, at the
   hedged strength the contested_claim record itself uses.
5. **"A church council formally condemned them three centuries after
   that [c. 399-400]"** (site `floorNote`) — checked against
   `alx.contested.origen-positions` and `alx.core.alexandria`'s caution
   4 (the 553 condemnation) and found consistent. Kept, restated from
   the registered records rather than copied from the site.
6. **`experienceToday`** — no such field exists on this world's site
   data at all, matching cappadocian's finding (not either pilot's).
   `orientation.experience_today` is correctly absent, not a scope
   decision this pass had to make.

### Name-disambiguation check

`alx.figure.gregory-thaumaturgus` (Gregory Thaumaturgus of Neocaesarea,
Origen's student at Caesarea) and cappadocian's own
`cappadocian.figure.gregory-thaumaturgus` are the same historical person,
appearing as a figure record in two different worlds. Not a same-world
naming collision and no conflation risk follows (each world's record
stands on its own evidence); this record voices him only briefly, by his
full disambiguating name, in one `orientation.story` paragraph, never in
`orientation.voices`. "Dionysius" and "Origen" were both checked and
found to collide with no other figure in this corpus.

### Cross-record consistency check

`alx.contested.desert-attribution` was read alongside its cross-build
counterpart, `desert.contested.alexandria-continuity`: both hold the same
question open, neither asserts what the other denies. No cross-record
contradiction found. `alx.gravity.teacher-bishop-tension`,
`alx.force.origen-demetrius-conflict`, and `alx.story.origen-demetrius`
were checked against the newly authored `alx.story.origen-daring-deed`
for overlap (the new record narrates the incident the older one
deliberately omits; no contradiction), and all three sibling records'
`relations` were updated with the required reciprocal
(`gate_reciprocity`). The `narrative.questions` C-I and F1-P pairings
were each checked for citation consistency between their
`doctrinal_witness`/`demonstration` pair — no drift found in either.

### `documented_stories` migration

`atlas-v3.html`'s alexandria-catechetical `documentedStories` array holds
three entries. Two matched an existing record directly ("Nursing the
Plague-Stricken While the City Fled" → `alx.story.plague-nursing`;
"Three Days of Argument at Arsinoe" → `alx.story.arsinoite-conference`).
The third, "Origen's Rash Act and the Bishop Who Turned on Him," covered
material — Origen's youthful act on Matthew 19:12 and Demetrius's later
use of it against him — that no existing alx story record narrated
(`alx.story.origen-demetrius` covers the same rupture but was built
structural-only, deliberately refusing this incident-level detail). A new
story record, `alx.story.origen-daring-deed`, was authored this session
and verified directly against the vendored Eusebius file (*HE* VI.8,
npnf201 lines 33140-33224) rather than against the site's own prose.
`title`/`teaser` for all three `documented_stories` entries were written
fresh against each record's own `text`/`tellable_as` fields, not copied
from the site.

### Judgment calls

- **`orientation.voices`** uses four of this world's eight `narratable:
  true` figures (Origen, Athanasius, Dionysius, Didymus), not the site's
  five-voice list and not all eight available. Clement is excluded
  because his figure record sets `narratable: false` by prior ruling.
  Pantaenus is excluded as the thinnest of the eight; the four chosen
  already anchor the world's full chronological span and its central
  Tensional gravity (teacher vs. bishop). Gregory Thaumaturgus is used
  briefly in `orientation.story` but excluded from `voices`, since his
  formation happened at Caesarea, after the Alexandrian rupture.
- **Antony is deliberately excluded** from `orientation.story`,
  `voices`, and `documented_stories` entirely, despite being
  `narratable: true`. His figure record carries a cross-build flag
  ("Antony belongs at least as much to the Desert world... as to
  Alexandria"), and `alx.core.alexandria`'s caution 5 forbids any
  Alexandrian claim resting constitutively on desert-formation texts.
  The one place he legitimately belongs — the open cross-build question
  — is handled in `relations_summary` instead.
- **`narrative.quiet`** names `alx.limit.f5-women-own-words` rather than
  this world's other two `honest_limit` records, because it is the
  silence `orientation.story`, `sourcing`, and `skim.tile` all make
  audible in advance. `alx.limit.marriage` is instead folded into
  `sourcing`, matching the site's own placement of that gap.
- **`narrative.questions`** pairs cell C-I with cell F1-P, not a C-T or
  C-E pairing as desert and cappadocian used: this world has no
  demonstration record at all for C-T or C-E. F1-P was chosen because it
  is the only remaining cell with both a demonstration and a matching
  doctrinal_witness record on the same cell, and because it reuses the
  Arsinoite conference material `orientation.story` and
  `documented_stories` already feature.
- **`legacy`** is deliberately kept to one entry, matching cappadocian's
  own restraint: `alx.core.alexandria`'s caution 4 (the out-of-horizon
  trap on c. 399-553 Origenist material) counsels against smoothing this
  world's genuinely unsettled afterlife into a longer, more confident
  list than the registered records support.

### `modern_rendering` coverage — found here, since resolved

This build's own verification pass found a severe pre-existing gap: only
1 of this world's 26 `quote` records (3.8%) carried a populated
`modern_rendering` field at the time — a clear outlier against desert's
24% and syriac's 53% coverage on the same check. `narrative.pull_quotes`
was deliberately left at a single entry rather than padded with quotes
whose `modern_rendering` would compile to `null`, and the finding was
flagged for a dedicated retrofit pass.

**That retrofit has since happened.** Commit `da3f1a77` ("R40: author
modern_rendering for alx's 25 quote records missing it", PR #442),
followed by `2c7b3fc7` and `d808787d`, authored and re-verified
`modern_rendering` for all remaining quote records. A direct recount at
the time of this build-log entry (`grep -L "^modern_rendering:"
records/alx/quote/*.md`) confirms 26 of 26 quote records now carry the
field. This is recorded here as settled build history, not filed as a
new `Open_Gaps_Tracking.md` entry, because the gap it would describe no
longer exists.

---

## Source-form fragment re-author — 2026-09-25

Two `modern_rendering` values re-authored after the report-only
sentence-completeness check (P3 Decision-Log Entry 29) flagged them as
fragments, under Mark's R44 ruling of 2026-09-24 ("Interjections and
answers stay; lists become one sentence; true ellipses get finished").
Only `modern_rendering` changed; every other field is byte-identical.
Authored by Opus. P3 Decision-Log Entry 37 carries the fleet-wide record
of this pass.

- `alx.quote.couches-and-trenchers-and-bowls`: the inventory had been
  rendered one item per sentence ("Silver couches." "Pans and
  vinegar-dishes." ...). A single list sentence scores FK 41.7 and fails
  the live readability gate. Mark ruled on 2026-09-24 for this record
  ("Option 1"): whole short sentences, each with its own subject and verb,
  carrying the source's own verb ("are all to be given up. So are ...").
  The source's closing reason ("as having nothing whatever worth our
  pains") stays tied to the verb with "because". FK 8.28.
- `alx.quote.to-believe-or-disbelieve`: "For example, to philosophize or
  not, to believe or to disbelieve." was a clause split away from its own
  sentence. Rejoining it scores FK 12.0, so it is split differently: the
  source's "as, say" becomes an imperative, "Take, for example, ...".
  FK 9.3.

Both read "translation" on two consecutive runs of each grader (Haiku 4.5
and Sonnet 4.6). `alx.quote.timothy-ordinary-questions` ("Answer: No."
twice) stays as the source speaks it.
