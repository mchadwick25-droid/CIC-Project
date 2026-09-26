# Source Readiness Dossier — The Roman Church in the Age of Gregory the Great

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** II.18
**Corpus-map slug:** `roman-church-gregorian`
**Time window:** c. 560–604 CE
**Region(s):** Rome and its Sicilian/Italian estates; the mission field
beyond (Anglo-Saxon England, Merovingian Gaul, Visigothic Spain reached
through Gregory's own correspondence)
**Dossier author / date:** source-research thread, 2026-09-21
**Corpus-map / `cic/texts/` state as of:** commit `009caaf0`, 2026-09-21

**A note on this candidate's own status.** Added to the census on record in
2026, not via a Step 0 survey verdict — the census's own `why` field names
the open questions a survey would settle as "whether these decades are a
world or the opening of the medieval papacy that later entries carry, and
whether an entry can properly be built around a single person at all." No
build has started (no `worlds/rcg/` or equivalent folder exists); this is
the first dossier written for it, from a cold search, not a write-up of
prior work.

## 1. Already assigned

`cic/corpus-map/roman-church-gregorian.yaml` holds three works, all Gregory
the Great's own voice, all re-pointed here on 2026-08-27 when this entry
was minted (previously scattered across the four worlds his letters merely
describe):

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Register of the Epistles, Books I–VIII (selection) | gregory | tradition | assigned | part of ~160k words total across both Register rows | `npnf212_leo-great-gregory-great.xml` |
| Register of the Epistles, Books IX–XIV (selection) | gregory | tradition | assigned | (see above) | `npnf213_gregory-great-ephraim-syrus-aphrahat.xml` |
| The Book of Pastoral Rule | gregory | tradition | assigned | ~70k words | `npnf212_leo-great-gregory-great.xml` |

This matches the census's own sourcing note exactly: "very good, and by a
long way the largest body among the five entries added at this ruling" —
about a quarter-million words, all one man, all administrative/pastoral
prose (the Register is "a working archive rather than a literary work:
grain shipments, episcopal discipline, the ransom of captives"). The
census's own gap disclosure is independently confirmed against `cic/texts/`:
**neither the *Dialogues* (Gregory's own hagiographical/theological
dialogues, Book II of which is the only surviving *Life of St. Benedict*)
nor the *Moralia in Job* (Gregory's own massive allegorical commentary) is
vendored anywhere in this corpus** — checked directly against the full
`cic/texts/` file list, not assumed from the census note alone.

Four already-existing cross-world context links, done correctly and needing
no action: `anglo-saxon-christianity`, `merovingian-gallic-christianity`,
`byzantine-imperial-church-justinianic`, and `early-benedictine-italian-monasticism`
each carry the Register's two rows as `context` (evidence about them, not
their own voice) — confirmed directly in `early-benedictine-italian-monasticism.yaml`,
whose own note states the reasoning explicitly: "leaving them as `tradition`
would have made Gregory a voice of four traditions he was not."

## 2. Cross-link opportunities

**A live, unresolved item, found on this pass: Gregory's own primary Latin
correspondence sits assigned only as `context` to a world it describes, with
no parallel `tradition` link back to his own home entry — the identical
structural gap the corpus-map's own Register rows exist specifically to
close, just not yet applied to this one.** `cic/corpus-map/donatism.yaml`
carries `Epistolae Selectae (selected letters concerning the African
Donatist remnant)`, author `gregory-great`, `role: context`,
`confidence: provisional`, sourced from `gregory-great_epistolae-selectae_turchi1907.txt`
— a 1907 Latin edition (Turchi, from the *Bibliotheca Sanctorum Patrum*
series, public domain, vendored 2026-09-07) of Gregory's own letters to and
about the surviving Donatist communities in Africa, roughly 150 years after
Augustine. Donatism's own note is explicit that this is "Gregory the
Great's own correspondence... late, outside, administrative description,"
correctly held as `context` there — but by the same reasoning the
roman-church-gregorian entry's own Register rows already use ("the
TRADITION row: fourteen years of a bishop administering a city, which is
this entry's own voice and nobody else's"), **this is also Gregory's own
voice and belongs here too, as a second `tradition` row, the same
double-placement pattern the corpus-map already uses elsewhere** (e.g.
lpc's Council of Carthage, Augustine–Jerome letters). Two things worth
checking before that link is made, named rather than resolved here: whether
Turchi's selection duplicates letters already covered by the NPNF Register
selection (in which case this would be a Latin-original pairing, like the
pattern documented in the companion `latin-pastoral-congregational-christianity`
dossier) or adds letters the NPNF selection omits (in which case it is new
primary content, not just a second witness) — donatism.yaml's own note
states this is "provisional pending confirmation of exactly which letters
in this selection touch Donatism specifically, and how many," so the
overlap question is genuinely open on both sides, not just this one.

No other cross-link candidates were found this pass. A targeted search
across the corpus for other 6th-century Italian/Roman material (Cassiodorus,
the *Liber Pontificalis*, Marius of Avenches, Paul the Deacon's later
*Historia Langobardorum*) turned up nothing currently vendored — this
world's own contemporaries are not otherwise represented in `cic/texts/`.

## 3. Verified acquisition leads

Both directly confirmed against archive.org this session — neither taken on
a title match.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Dialogues of Saint Gregory, surnamed the Great (complete, all four Books) | Gregory I | "P.W.", ed. Edmund G. Gardner | 1911 | `archive.org/details/dialoguesofsaint00greg` | Explicit `NOT_IN_COPYRIGHT` on the item page | Direct WebFetch of the item page, 2026-09-21 |
| Morals on the Book of Job (*Moralia in Job*), complete in 4 parts (Parts I–V, Books I–XXXV) | Gregory I | James Bliss, Library of the Fathers series | 1844–1850 | `archive.org/details/moralsonbookjob00igoog` (and `01`/`02`/`03igoog` for the other parts) | Explicit `NOT_IN_COPYRIGHT` confirmed on the Part V/Books XXX–XXXV item; the four parts are one Google-digitized set | Direct WebFetch of one part's item page, 2026-09-21; the other three identifiers located by the same search but not each individually opened this session |

**Why these matter beyond general completeness.** The Dialogues, Book II,
is *the only surviving Life of St. Benedict* — acquiring it would give
`roman-church-gregorian` and `early-benedictine-italian-monasticism` (whose
census entry names Gregory as the author of "the only life of Benedict
there is") a direct, shared primary-source link neither world currently
has, since Gregory's own Dialogues are vendored nowhere in the corpus. The
Moralia is the largest single work Gregory wrote and closes the "one man, a
quarter of a million words" framing's most obvious remaining gap.

**Not yet done, and worth naming plainly:** the four Moralia identifiers'
exact volume/book boundaries were not individually verified this session —
only one part (Books XXX–XXXV) was opened and read. Before either work is
vendored, each of the three unopened Moralia identifiers should be opened
and its own book range confirmed, the same discipline `SOURCE-READINESS.md`
asks for generally.

## 4. Checked and closed

None this pass — both leads run down (the Dialogues and the Moralia)
confirmed on the first search rather than dead-ending, so there is nothing
yet to record as closed. Worth naming as an open question rather than a
closed one: the modern critical edition of the Register (Norberg's CCSL
140/140A Latin text, 1982) almost certainly remains in copyright on its
imprint date alone, but this was not independently checked this session and
should not be assumed rather than verified before a future pass treats it
as settled.

## 5. Open cross-world questions

- **The Turchi *Epistolae Selectae* double-placement**, named at §2 above —
  whether it duplicates or extends the NPNF Register's own selection, and
  whether to add it here as `tradition` (mirroring the Register's own
  reasoning) is a call for whichever thread first drafts this world's
  Doc_02, not decided here.
- **Whether this candidate is a world at all**, per the census's own
  standing question — "whether these decades are a world or the opening of
  the medieval papacy that later entries carry, and whether an entry can
  properly be built around a single person at all." A sourcing dossier
  doesn't resolve a Step-0-level eligibility question; named here only so a
  build thread doesn't mistake this document's existence for that question
  already being settled.
- **Overlap with `early-benedictine-italian-monasticism`**, whose own
  window closes at Gregory's death — the census's own relations summary
  already states this is "in person rather than in kind" (Gregory was a
  monk and wrote the Benedict biography, but the Pastoral Rule and Register
  are episcopal/governmental, not monastic). Acquiring the Dialogues (§3)
  would sharpen this boundary question rather than remove it, since Book II
  specifically is monastic-biographical material from an otherwise
  non-monastic corpus.
