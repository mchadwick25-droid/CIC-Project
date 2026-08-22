# Glossary / Story / Quote Template — the modern-vs-world contrast standard

This is the standard every world-build thread should retrofit its `term`,
`story`, and `quote` records against, once all six worlds have cleared
their own content canon. It exists so six independently-run threads
produce the same shape of answer to the same question — "how might a
modern reader mishear this, and what did this world actually mean by it"
— instead of six different interpretations of "upgrade your glossary."

**Status as of 2026-08-22: schema-ready, not yet enforced.** The fields
below are live in `engine/m1/schemas.py` (validate correctly wherever
populated) but deliberately NOT yet in `engine/m1/gates.py`'s
`COMPLETION_REQUIRED` — adding them there is the actual retrofit trigger,
and flipping it now would break every already-built world's currently
clean gate battery. Mark flips that switch when the retrofit task is
actually sent to all six threads; until then this is a template to build
toward, not a live requirement.

## SS1. Term (glossary) — already proven, formalize as-is

This one isn't new. `alx.term.eucharistia` (built, `world/alexandria`) is
the worked model:

```yaml
plain_meaning: 'The thanksgiving: the shared meal of bread and cup at the heart of the community''s worship.'
world_word: eucharistia
false_friend:
- transubstantiation (a term from a much later century)
- a mere symbol or memorial
senses:
  informational: "The community's central act..."
  evidential: "Eucharistic participation is attested across the corpus..."
  personal: "Whatever else a member could not read or argue, this was theirs..."
  translational: "'Is that what we call transubstantiation?' - this world had no such term and no such theory; it spoke of real participation and left the how in God's hands."
quick_meaning: The community's thanksgiving meal of bread and cup.
```

- `false_friend[]` — the explicit list of modern concepts/terms a reader
  might wrongly conflate this with. Empty array is the typed "none
  identified," never omitted (same sentinel rule as `retrieve_when`).
- `senses.translational` — the actual today-vs-world bridge sentence(s):
  names the modern question a reader is likely to bring, and states
  plainly that this world's own answer is different in kind, not just
  degree.

**What's changing when the retrofit lands:** `false_friend` and
`senses.translational` move from optional-in-practice to individually
required (not just the parent `senses` object) — every term record needs
both, not a `senses` object with only `informational` filled in.

Two more term fields, added 2026-08-22 after reviewing the prior
framework's own term design (`cic-poc/backend/wrs/` — pre-redesign
material, evidence not dependency per `Build-Blueprint.md`, but its
`desertlex001.md` worked example surfaced two genuinely useful ideas not
already covered):

- `distortion_risk: low | medium | high` — a quick-scan severity marker
  for `senses.translational`'s own gap. The old system buried this in
  free text ("Sharp then-vs-now gap: high grounding criterion"); making
  it a real enum lets a reviewer or future tooling triage the
  highest-risk terms without reading every paragraph.
- `prior_sense` (optional string) — the word's *own* older, ordinary
  sense before this world's community repurposed it. Different from
  `false_friend`: false_friend is a *modern* concept wrongly projected
  backward; `prior_sense` is the term's real pre-existing usage this
  world's own community redefined. Real example: *anachōrēsis* had an
  ordinary Greek sense (withdrawal, or a villager's flight from fiscal
  obligations) distinct from what the desert movement made of it. Leave
  blank for coinages with no meaningful prior secular sense — most
  `world_word`s will not need this field.

## SS2. Story — new field: `modern_contrast`

Stories don't currently have an equivalent field at all. Add one:

```yaml
modern_contrast: >
  A modern reader often hears [the story's surface action] as [the
  anachronistic modern category it superficially resembles]. This
  world's own record frames it differently: [what the story actually
  did/meant inside this world's own formation logic, in its own idiom,
  stated plainly].
```

Illustrative shape (not real content — pattern only): a story about a
public confession before a community isn't "medieval-style public
shaming" to a modern ear that reaches for that frame; state plainly what
the confession actually accomplished inside this world's own logic
(restoration to the table, not humiliation as an end).

- One field, not a four-part `senses` object like term — a story is a
  narrative unit, not a concept with four registers.
- Required only when a real modern-misreading risk exists for that
  specific story. When it doesn't, say so explicitly rather than
  omitting the field: `modern_contrast: "No significant modern-misreading risk identified for this story."`
  — same discipline as `false_friend: []` on a term with none.
- Draw this from material already established in the story's own
  `narrative_tier_justification` or the world's own gravities/forces
  where possible — this is compression of already-approved reasoning
  into a new, retrievable field, not new research.

## SS3. Quote — new field: `modern_lens_note`

Quotes are presented with direct attribution and license, so this is
lighter than term's four-part treatment, but the same principle:

```yaml
modern_lens_note: >
  [If the quote's vocabulary or imagery reads anachronistically to a
  modern ear — a word that changed meaning, an image that now carries
  different connotations — name it plainly here. Otherwise state
  explicitly that no significant modern-lens risk was identified.]
```

- Always present, never blank — same "explicit none" discipline as the
  other two fields.
- Do NOT use this field to soften, apologize for, or add balance to a
  quote's own content (see the anti-Jewish-material precedent already
  established on `syr` — one-sidedness is stated as such, never invented
  balance). This field is about vocabulary/imagery legibility, not about
  editorializing the quote's substance.

## SS4. What stays out of scope for the threads

Two things are follow-up engineering on `build/phase-1`, not part of any
world-build thread's retrofit task:

1. **Compiler wiring.** `engine/m2/builders.py` currently does not pass
   `false_friend`/`senses`/`modern_contrast`/`modern_lens_note` into any
   compiled artifact except the full `repository.json` dump (tier-3,
   whole-record view). There's no lightweight glossary-style index a
   hover UI could query cheaply the way `quotes.json`/`figures.json`
   already give quotes and figures their own compiled index. Fixing this
   is real work, separate from record content, and doesn't block the
   content retrofit.
2. **Frontend implementation.** No hover/click UI component consuming
   this data exists yet in this repo — M6 (Participant Surface) is a
   future build stage, not something to assume is already wired up.

The threads' job when this task is sent is content only: populate the
three fields above, consistently, across their own world's already-built
term/story/quote records. Compiling and rendering them is separate work
that happens once, centrally, not six times.
