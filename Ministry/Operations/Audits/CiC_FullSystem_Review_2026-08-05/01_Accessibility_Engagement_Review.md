# 01 — Accessibility & Engagement Review

**Dispatched:** 2026-08-05, as pass 1 of the four-angle full-system review (`00_INDEX.md`).
**Method:** `Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md` — source-level
verification (every claim below was checked by opening the actual file and reading the actual line,
not summarized from a similar-sounding artifact), fixed P0/P1/P2 severity, counted structural checks
rather than impressions, and a plain bottom-line verdict.
**Reading done directly by this reviewer.** No sub-agents were dispatched, per the note at the bottom
of `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/00_INDEX.md` (passes 05 and 06 had to
be re-run for exactly that reason).

**The question this pass asks:** would a curious, intelligent adult with no religious-studies or
church-history background find this clear, welcoming, and genuinely interesting — or would it read as
homework written for someone else?

---

## 1. What I read, and what I deliberately skipped

### Read in full, at source

**Entry point / participant-facing web**
- `cic-website/atlas-v3.html` — all 1,600 lines, read as source: every visible copy string, the
  search placeholder, the era-header assembly (§ lines 735–746), the hover-card builder (lines
  1229–1256), the click-document builder (`openSheet`, lines 1272–1360), the "Reading the marks"
  footer (lines 446–464), the generated Categories & Regions glossary (lines 1166–1183), the tray/
  hand-off (lines 1568–1592), and the mobile-vs-desktop layout gating in `<style>` (lines 255–395).
- `cic-website/data/world-census.json` — the live data the atlas reads. All 257 movement entries and
  10 era records inspected programmatically for the fields that actually reach a participant
  (`teaser`, `longDescription`, `voices`, `legacy`, `floorNote`, `statusWord`, `sources`,
  `statusMeta`, era `title`/`academicName`/`keyEvents`/`tag`/`rec`).
- `cic-website/index.html` — full body copy extracted and read (the actual front door).

**The three worlds I went deep on**
- **Post-Apostolic House-Church (W1):** `CiC_W1_Representative_Permanent_Prompt_Chloe.txt` (all 45
  paragraphs), `CiC_W1_World_Profile.md`, `CiC_W1_Doc09_Story_Inventory.md`, and 5 story chunks —
  `pahcstory001` (Ignatius), `pahcstory004` (Pliny), `pahcstory008` (Polycarp), `pahcstory009`
  (Two Ways), `pahcstory013` (mutual aid).
- **Desert Monasticism (W3):** `CiC_W3_Representative_Permanent_Prompt_Papnoute.txt` (all 37
  paragraphs), `CiC_W3_Doc09b_World_Profile.md` (full), `CiC_W3_Doc09a_Story_Inventory.md`, story
  chunks `desertstory004` (leaking jug) and `desertstory008` (day in a Kellia cell), plus
  `desert_World_Capsule_Core.md` (the live prompt-side capsule).
- **Syriac Christianity, Edessa/Nisibis (W7):** `syr_Representative_Permanent_Prompt_Yausep.txt` (all
  71 paragraphs — the longest of the three), `syr_World_Profile.md` (opening + structure),
  `Doc_09_Story_Inventory.md` including its Absent Stories section, story chunk `syrstory005`
  (Simeon bar Sabbae), and `syr_World_Capsule_Core.md`.

**App copy and the plain-language machinery**
- `cic-poc/frontend/src/components/` — `OnboardingScreen.tsx`, `WorldSelector.tsx`, `ChatInput.tsx`,
  `QuestionSheet.tsx`, `Level3Panel.tsx`, `GlossHighlight.tsx`, `TheTable.tsx` (copy paths),
  `LexiconModal.tsx`, `CitationModal.tsx`, `SignInScreen.tsx`.
- `cic-poc/frontend/src/data/guided_starters.json` — all 385 starter questions across 5 worlds.
- `cic-poc/backend/wrs/views/plain_explanation.py` and `wrs/views/level3.py` — the Level-2 / Level-3
  render contracts, read end to end.
- `cic-poc/backend/wrs/gates/core.py` (`readability_check`, `gate_readability`),
  `wrs/parameters.yaml` (`reading_floor`), `cic-poc/backend/app/main.py` route table,
  `data/desert_world/repository.json`, and the term records under `wrs/records/*/term/`.

**The project's own stated bar**
- `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/01_DesignDoc_Mining.md` §3
  (Reading Level / Plain Language), then **re-verified at its own cited source** rather than trusted:
  `L3B-World-Build-Methodology/Representative_Permanent_Prompt_Template.txt`, Final Assembly
  Instruction 5c (lines 642–660) and 5d (lines 663–681), and `cic-poc/backend/wrs/parameters.yaml`
  lines 102–110. All three claims in 01_DesignDoc_Mining §3 check out verbatim.

### Deliberately skipped, and why

- **Alexandria, Hieronymian, and Imperial-Juridical world builds.** The dispatch named three worlds
  to go deep on; covering six at this depth would have produced a thinner pass on each. I did pull
  their *counts* where a count was load-bearing (term records, story chunks, `plain_explanation`
  coverage) so that no cross-world claim below rests on a three-world sample when a six-world number
  was cheaply available.
- **Doc_01–Doc_08 in all three worlds.** These are construction documents. Nothing in them is served
  to a participant (verified: `grep -rn "World_Profile\|world_profile"` across `cic-poc/backend`
  returns nothing, and the FastAPI route table in `app/main.py` exposes no world-build document
  path). Judging their reading level would be judging the wrong artifact. I read the World Profiles
  because the dispatch named them, and report their register below **only** as context, not as a
  defect.
- **Review-round artifacts** (`Doc_0N_Review_RoundN.md`, LiveTest transcripts). Build-process
  evidence, not participant surface. Out of scope for this angle; they are pass 03's and pass 04's
  ground.
- **`cic-website/tour.html`, `about.html`, `support.html`, `whats-next.html`.** Skimmed for the one
  cross-cutting question I needed them for (is "the Table" ever defined? — it isn't) and otherwise
  left to pass 04, which owns persona readiness across the marketing surface.

### One methodological caveat, stated up front

`textstat` — the library `wrs/gates/core.py` uses for every Flesch-Kincaid number in this project —
**is not installed and is not declared in `requirements.txt` or `pyproject.toml`** (finding P1-8
below). I therefore computed FK/FRE with my own standard-formula implementation. Syllable counting
differs slightly between implementations, so treat every grade number below as ±0.5, and every
*comparison* between two of my own numbers as reliable. Where a number is close to a threshold
(the onboarding screen's FRE 59.9) I say so rather than calling it a pass or a fail.

---

## 2. Genuine strengths

These are real and specific. I looked for reasons to withhold credit and did not find them.

**2.1 The census teasers and world descriptions are outstanding popular history.** This is the best
writing in the project and it is not close. From `cic-website/data/world-census.json`:

> "Rome and the wider Mediterranean, c. 390 to 430 — a movement built on the conviction that God
> never commands what a person cannot do, argued out of the church by Augustine and preserved mostly
> inside his rebuttals." (`teaser`, Pelagianism)

> "Ruthenia and Austrian Galicia, 1700 to 1815 — a church at its height that lost most of its people
> in two years, when the state that had protected it ceased to exist." (`teaser`, Ruthenian Uniate)

Every one of these is a *hook*, not a summary. They name stakes, not dates. 219 of 257 entries carry
one. The `voices` field does the same work for people — Ignatius is not "an early bishop" but "bishop
who wrote seven letters to congregations while being marched to his execution in Rome"; Didymus is
"blind from early childhood, taught in Alexandria for decades." And the House-Church `voices` array
closes with a line most projects would never write:

> "Most of these communities' hosts and householders are unnamed in the record — the gatherings met
> in the homes of people history did not bother to write down"

That is honesty deployed as narrative, and it is genuinely moving. This corpus is the project's
biggest accessibility asset.

**2.2 The Guided Starters are the single most newcomer-friendly artifact in the system.**
`cic-poc/frontend/src/data/guided_starters.json`, 385 questions across 5 worlds, measured at
**FK grade 4.8, Flesch Reading Ease 79.3** — comfortably the plainest prose anywhere in the project,
and it is precisely the prose a lost newcomer meets first. The questions sound like a real person:

> "Was it actually dangerous to be a Christian back then, day to day, or is that exaggerated?"
> "Who was actually in charge of your church — was there one leader, like a pastor, or something
> more like a board?"
> "Isn't 'we're still arguing about it' just a nicer way of saying you don't actually know?"

The fourth tier ("Honest Limits") invites the participant to interrogate the project's own
weaknesses. And the affordance is *persistently visible* above the input box, not buried in a menu
(`ChatInput.tsx` lines 85–91) — it is not disabled when unavailable, it is hidden entirely, so it
never teases content that isn't there. This is exactly right.

**2.3 The story chunks tell stories, not facts.** The dispatch asked whether the material reads as
human scenes or as a list of doctrines. Read at source, it is scenes. `pahcstory001`:

> "'ten leopards,' he calls his soldiers, 'who only get worse the better they are treated'"

`desertstory004`, the whole story in four sentences with a jug of water trailing behind a man walking
to a trial. `syrstory005`, where the eunuch Gushtazad "returned to the faith he had abandoned, and
was put to death before Simeon's own eyes — the first to die, going ahead of the bishop he had once
failed to imitate." `pahcstory013` reconstructs a community's care for a prisoner from *two hostile
outside witnesses* and says so. None of this reads as a list.

**2.4 The Permanent Prompts are genuinely voiced, and two of three hit the project's own reading
target.** Measured against the mandatory 5c band (FK 8–10, FRE ≥ 60):

| Prompt | Words | Sentences | Words/sentence | FK grade | FRE | 5c verdict |
|---|---|---|---|---|---|---|
| Chloe (`CiC_W1_Representative_Permanent_Prompt_Chloe.txt`) | 2,524 | 159 | 15.9 | **7.0** | 72.9 | passes (below band floor, which 5c reports rather than fails) |
| Papnoute (`CiC_W3_Representative_Permanent_Prompt_Papnoute.txt`) | 2,410 | 120 | 20.1 | **8.4** | 70.5 | **passes** |
| Mar Yausep (`syr_Representative_Permanent_Prompt_Yausep.txt`) | 3,304 | 140 | 23.6 | **10.3** | 62.9 | **fails the grade ceiling** (P1-6) |

Chloe at grade 7 is a real achievement for a text this dense with historical content, and it confirms
CO-015's own pilot claim (12.3 → 8.1) held after subsequent edits.

**2.5 Papnoute's prompt models the right way to teach a hard word.** `CiC_W3_Representative_Permanent_Prompt_Papnoute.txt`
¶11 is the pattern the whole project should copy:

> "The vocabulary through which we understand everything: the flight from settled life we call
> *anachoresis*. The thoughts we watch and weigh, we call the *logismoi*. The skill of telling one
> from another rightly, our master skill, we call *diakrisis*. The stillness we are always trying to
> reach and never quite finish reaching, we call *hesychia*."

Plain meaning **first**, term **second**, every time. Five Greek terms land without a single one
being an obstacle.

**2.6 Yausep's prompt carries an explicit gloss-as-you-go instruction — the only one that does.**
`syr_Representative_Permanent_Prompt_Yausep.txt` ¶43:

> "Before you reach for *raza*, *qyama*, or *Iḥidaya* as your first word, ask whether your own record
> gives you a face, a name, or a scene for this question instead... Let the word follow the story,
> not stand in front of it. And when your own vocabulary does carry the answer, bring it one term at
> a time. Ground each one, briefly, in what it means before reaching for the next, the way you would
> teach someone new to it rather than a fellow teacher who already carries the whole of it."

"Let the word follow the story, not stand in front of it" is the single best sentence of
accessibility design in the repository. It should be boilerplate in the template.

**2.7 The Desert world's Level-2 plain explanations are exactly what the constitutional promise
describes.** `cic-poc/backend/data/desert_world/repository.json`, record `desertlex001`:

> "Withdrawal was the heart of this world. A person left the village and moved to empty land. The
> leaving itself was the training, not a step before it... Today the word sounds like avoidance or
> escape. This world heard the opposite. Leaving forced a person to face what village life let them
> avoid."

Measured **FK 4.73, FRE 78.8** by the system's own render-time check, which stores the result in the
payload. It explains a Greek term without ever making the reader hold it. This proves the mechanism
works. It also makes P0-5 below far more visible: this exists for one world of six.

**2.8 The onboarding screen is honest and welcoming in a way most products are not.**
`OnboardingScreen.tsx` tells a first-time participant that the work "has not yet been checked by
outside historians and theologians," that their conversation is being catalogued, and — in a section
headed "The one honest distinction that matters most" — that a Representative "is not a spokesperson
for how that living community understands or practices its faith right now." That last paragraph is
the kind of thing a project usually gets forced into. Here it is volunteered, in plain words, before
anyone has typed anything.

**2.9 The "Absent Stories" discipline reaches the participant, not just the file.** The Story
Inventories' honesty about silence (`Doc_09_Story_Inventory.md` §3: "No *bnat qyama* woman's own
composed word survives, in her own voice") is not stranded in a build document — it is carried into
the live prompts. Chloe ¶37: "Of those in your own households who serve rather than lead, or who
never learned to write, you know mostly what others have said of them. You do not know what they
themselves would say. You hold that silence honestly, rather than inventing a voice for it."
Papnoute ¶31: "The women among us who lived this same life left us far less of their own words than
the men did." For a curious newcomer this is *more* interesting than confidence would be, not less.

---

## 3. Findings

### P0 — blocks; fix before a non-academic newcomer is put in front of this

---

#### P0-1 · The atlas has no orientation text a sighted visitor can see, and its only explanation is below the entire ten-era canvas

**File:** `cic-website/atlas-v3.html`, lines 394–446 (above the fold) vs. 446–466 (footer), with the
desktop layout gate at lines 305–312.

The page's only descriptive heading is screen-reader-only:

```html
<h1 class="sr-only">Church in History — an interactive map of Christian traditions across ten eras</h1>
```
(line 396; `.sr-only` is defined at line 380 as `position:absolute;width:1px;height:1px;...clip:rect(0,0,0,0)`)

Everything a sighted first-time visitor sees above the fold is: a search box, three chips ("Built
worlds", "Filters", "Copy link"), a theme toggle, and one small italic muted counter reading
`257 movements · ten eras` (line 1500). No sentence anywhere on that first screen says what the page
is, what the coloured bands mean, what the boxes mean, that time runs downward, or what to do.

The explanation exists — the "Reading the marks" block and the generated Categories & Regions
glossary are both good — but they are in `<footer>`, and the footer is below the canvas. On desktop
this is structural, and the code says so in its own comment (line 310):

> "Desktop gets no special sizing here at all -- `#wrap` keeps flowing in the page exactly as it
> always has, unscaled, un-transformed, un-contained."

With row pitch 60px, an era header allowance of 110px and 34px pad per band (line 585), even a
theoretical best case of one row per era puts the footer ~2,040px down; the realistic figure for 257
entries is several times that. A newcomer must scroll past the entire history of Christianity to be
told how to read the diagram they scrolled past. (Mobile is better — `#mapViewport` bounds the map to
one viewport-height pane, line 313 — so this is specifically a desktop defect.)

**Fix.** Put a two-to-three-sentence visible orientation line directly under `#controls`, above
`#mapViewport`, before first paint. It needs to say four things and nothing more: time runs downward;
each box is a movement at its birth and the tail is its lifetime; colour is a tradition family; a
house icon means you can talk to this one now. Move the "Reading the marks" block into a collapsed
`<details>` at the top (open on first visit, remembered in `localStorage` like `cic_onboarding_seen`
already does in `OnboardingScreen.tsx`), and leave the footer copy in place for anyone who scrolls.

---

#### P0-2 · The hover card — the first thing anyone reads on this map — shows internal build jargon on 182 of 257 entries, and so does the screen-reader label

**File:** `cic-website/atlas-v3.html` line 1254 (`<div class="s">${esc(m.statusWord)}</div>`) and
line 762 (`aria-label="... ${esc(m.statusWord)}"`), reading `statusWord` from
`cic-website/data/world-census.json`.

Counted directly against the census: **182 of 257 `statusWord` values (71%) contain internal process
vocabulary** — "Step 0", an era number as a decision-process reference, or a bare criterion code
(`A1`/`A3`/`c2`/`C1`). The most common single value, on 31 entries, is:

> `Researched — viable, secondary (Era 9 Step 0)`

The worst are worse than that. Verbatim from the census, rendered as-is into the hover card:

> `Floor divergence formally recorded — non-realist reinterpretation of creedal content by its own
> texts (the record-mandated Era 9 disposition; the register's first A3-led case); register retained`

> `Floor Question (register) — new-revelation and sonship claims at own-text strength [S];
> person-defined ground plain; shelf ruled REGISTER over Outside-A4 at the Era 9 Freeze; ended 1864`

This is not an oversight nobody spotted — the project has already diagnosed *this exact class of leak
one layer down*. The click-document's own code comment (lines 1336–1352) records that an 8-era
adversarial pass on 2026-08-03 found "~200 of 257 statusDescriptions still carry researcher-facing
text" and switched the click document to the clean `statusMeta[...].description` strings. **The hover
card and the `aria-label` were not included in that fix**, and they are the *earlier* surface — you
hover before you click. A blind user gets it worst: `statusWord` is read aloud as part of every node's
accessible name.

**Fix.** Route the hover card and the `aria-label` through the same `statusMeta[m.status].shortWord`
the census already carries in clean visitor language ("Open for conversation", "Not yet assessed",
"Chosen — not yet built"). One-line change at both sites; the clean strings already exist and are
currently used nowhere on the page.

---

#### P0-3 · The six worlds you can actually talk to are the only six that say "Source base pending"

**File:** `cic-website/atlas-v3.html` lines 1328–1333, against `cic-website/data/world-census.json`.

The click document renders:

```js
h+=`<h4>Sources to research</h4>
 ${m.sources&&m.sources.length? ...
   :`<p class="note">Source base pending — ${esc(eraState)}</p>`}`
```

Counted against the census: **123 of 257 entries carry a `sources` array. Zero of the six
`Built & Live` worlds do.** So a newcomer who reads about, say, thirteenth-century Bogomilism gets a
reading list, and a newcomer who reads about the House-Churches — one of the six traditions the site
is inviting them to sit down with — is told the source base is *pending*, followed (because era ≤ 2
takes the first `eraState` branch, line 1284) by:

> "the earliest research pass is still the deepest one on record here; a fuller pass hasn't reached
> this era yet."

Both halves of that sentence are false about these six worlds, and provably so from inside the same
repository: `cic-poc/backend/data/syriac_world/source_registry.json` is a **53-entry** registry
sitting in the app's own data directory, and each of the three worlds I read has a full Doc_02 Source
Ecology plus a Source Registry spreadsheet.

For engagement this is the worst possible placement of a dead end: it fires at the exact moment a
curious reader has decided to go deeper on the one thing they can go deeper *into*. For the project's
own honesty commitment it is an inverted claim — the map understates its best-evidenced work and
overstates its thinnest.

**Fix.** Backfill `sources` for the six built entries from each world's existing Source Registry (5–8
headline works each is plenty — this is a reading list, not the registry). Until that lands, branch
the empty-state copy on `status === "Built & Live"` so it says the true thing: that this world's full
source registry exists and is reachable inside the conversation, rather than that it is pending.

---

#### P0-4 · The largest body of participant-facing prose in the project breaches the project's own mandatory reading standard in 225 of 225 entries — by the exact mechanism CO-015 already diagnosed and fixed elsewhere

**Files:** `cic-website/data/world-census.json` (`longDescription`, `legacy`, `teaser`), against
`L3B-World-Build-Methodology/Representative_Permanent_Prompt_Template.txt` lines 642–660 and
`cic-poc/backend/wrs/parameters.yaml` lines 102–109.

I want to be precise about what is and is not wrong here, because the prose itself is excellent
(§2.1) and I am not going to pretend otherwise.

The standard, verified at source (5c, lines 656–658): *"Target: Flesch-Kincaid grade 8-10, Flesch
Reading Ease 60 or above"*, achieved by *"Break any sentence over roughly 25-30 words into two or
more shorter sentences at its natural clause boundaries"*, with vocabulary explicitly untouched.

Measured across the census:

| Field | Entries | Median FK | Median FRE | Median words/sentence | Median syllables/word | Over FK 10 |
|---|---|---|---|---|---|---|
| `longDescription` | 225 | **18.1** | 30.8 | **36.8** | 1.64 | **225 (100%)** |
| `legacy` | 225 | 16.1 | 31.8 | — | — | **225 (100%)** |
| `teaser` | 215 | 12.9 | 48.5 | 26.0 | 1.55 | 157 (73%) |

Syllables per word of 1.55–1.64 is *plain vocabulary*. The whole gap is sentence length — this is
CO-015's finding, on a new corpus, unmodified. The longest single sentence in any `longDescription`
runs **105 words** (Mission-Born Christianity):

> "Between the 1490s and the middle of the seventeenth century, Christian communities took root far
> outside Europe under very different conditions: the kingdom of Kongo, whose ruler Afonso I adopted
> the faith and whose letters survive in his own voice; Japan, where a Jesuit mission from 1549
> gathered a large Christian population before a savage prohibition drove the survivors underground;
> China, where Jesuits and Chinese converts argued out how the Christian God could be spoken of in a
> Confucian idiom; and Spanish America, where conquest and mission arrived together and Andean and
> Nahua Christians made something of their own out of what they were given."

That is four excellent paragraphs' worth of content in one breath. The median entry's longest
sentence is 54 words. This corpus — 34,167 words of `longDescription` plus 6,250 of `teaser` plus all
of `legacy` — is by a wide margin the biggest thing a participant reads on this project's own
website, and **5c does not cover it**: 5c is a Permanent Prompt assembly instruction, and no check
anywhere applies the reading floor to census prose (confirmed: `gate_readability` in
`wrs/gates/core.py` line 218 is called from no production path — see P1-8).

I am calling this P0 rather than P1 because it is (a) the project's own mandatory bar, (b) breached at
100% of entries, (c) on the highest-traffic prose surface, and (d) mechanically fixable without
touching a word of the content. It is not P0 because the writing is bad. The writing is the best in
the project.

**Fix.** Run 5c's own procedure over `longDescription`, `legacy`, and `teaser`: split at existing
semicolons, colons, and em-dashes only; change no vocabulary and cut no content. Then extend 5c (or
add a sibling check) to name the census as a covered surface, so the next 100 entries authored don't
reproduce it a third time.

---

#### P0-5 · The project's stated vocabulary contract — "the glossary tooling carries that load" — is unmet for five of six worlds

**Files:** `L3B-World-Build-Methodology/Representative_Permanent_Prompt_Template.txt` lines 653–656;
`cic-poc/backend/wrs/views/plain_explanation.py`; `cic-poc/backend/wrs/records/*/term/*.md`;
`cic-poc/backend/app/main.py` lines 1884–1945.

The reading-level standard makes an explicit trade, verified verbatim at source (5c, lines 653–656):

> "A world's own difficult or technical vocabulary is not the problem this check addresses and should
> not be simplified or removed on account of it; **participant-facing tooling elsewhere in this
> project (glossary lookups) carries that load.**"

That is a load-bearing promise: hard words are allowed to stay *because* something else explains them.
Checked at source, that something else is built for one world.

- **Authored plain explanations:** `plain_explanation.py`'s contract (CO-P2-12, lines 5–11) is that
  Level 2 renders the *authored* `plain_explanation` field verbatim. Counted across the term records:

  | World | Term records | With `plain_explanation` |
  |---|---|---|
  | desert_world | 18 | **18** |
  | alexandria_world | 50 | 0 |
  | hieronymian_world | 15 | 0 |
  | pahc_world | 13 | 0 |
  | imperial_juridical_world | 12 | 0 |
  | syriac_world | 10 | 0 |
  | **total** | **118** | **18 (15%)** |

- **The fallback is not plain language.** For the other 100 records, `plain_explanation.py` falls back
  to a "structure-only simplification of `period_sense`" whose own module contract states (lines
  32–33): *"On the fallback path vocabulary and claims pass through verbatim."* So what a participant
  gets is scholarly prose with some semicolons turned into full stops. Concretely, Syriac's
  `syrlex001` `period_sense` — the actual text that would render — reads:

  > "A raza is bound to the shrara (truth) it signifies and carries something of that truth's own
  > hidden power - reading Scripture and creation by raza is perceiving a real connection already
  > there for a formed eye, not decoding an arbitrary sign; richly developed as a whole theological
  > method in Ephrem, present at genuinely lesser depth in Aphrahat **(chunk Quick/World Meaning)**."

- **And the fallback leaks build-artifact references.** The apparatus stripper at line 82 matches only
  `Doc_\d|§|CO-|FLAG-`. `(chunk Quick/World Meaning)` matches none of those. Counted: **82 of 118 term
  records (69%)** have no authored `plain_explanation` *and* carry an unstripped `(chunk ...)`
  parenthetical in `period_sense` — so 82 of the project's "plain explanations" would end with an
  internal file-structure reference.

- **And the surface serving any of this exists for one world.** `_load_repository_view`
  (`app/main.py` lines 1884–1895) 404s for any world without a built `repository.json`; only
  `data/desert_world/repository.json` exists. Its 404 body is builder-facing too: *"repository views
  exist for migrated worlds only (generated by wrs/views/repository.py)"*.

- **And even in the one built world, only terms get a Level 2.** Of that repository's 99 records, 18
  carry `level2` — exactly the 18 terms. Stories, figures, gravities, forces, contested claims and
  quotes (81 records) have no plain-language face at all; a participant clicking one lands on the
  Level-3 scaffold and, under "Show the full record", a `JSON.stringify` dump (see P1-4).

**Fix.** Either author `plain_explanation` for the remaining 100 term records (the Desert set is a
proven template and averages ~90 words each), **or** amend 5c to stop claiming a backstop that does
not exist for five worlds. Do not leave the promise standing while the mechanism is one-sixth built.
Separately and immediately: widen `_APPARATUS_RE` to strip `chunk` parentheticals, and change the
404 detail string to visitor language.

---

### P1 — materially improves the result

---

#### P1-1 · "The Table" is the product's central metaphor and its primary call to action, and is never defined anywhere a participant will look

`cic-website/index.html` line 127: `Come and join us at the Table`. `atlas-v3.html` line 441:
`<button class="go" id="go">Sit down at the Table</button>`; line 1334: `Add to the Table`.
`TheTable.tsx` lines 227/254: `<h1>The Table</h1>` with the subtitle "A space for engaging
conversation".

`OnboardingScreen.tsx` has a section headed *"What a 'world' and a 'Representative' are"* and defines
both, well. It never mentions the Table. Searching the whole website for a definition returns only
further uses of the phrase (`tour.html` lines 22, 357, 386, 573).

So a first-time visitor's most prominent button asks them to do something they have not been told the
meaning of. Worse, it is *ambiguous in a load-bearing way*: from the atlas, "Sit down at the Table"
launches a **multi-Representative** conversation, while the same phrase on the homepage launches the
app generically and `WorldSelector` will start a **single** "Deep Interview" if only one world is
selected. Same words, two different products.

**Fix.** One sentence in `OnboardingScreen.tsx`, and one line of hover/aria text on the atlas
button — e.g. "The Table is a conversation with more than one tradition at once; they can hear and
answer each other." Then make the atlas button's label reflect seat count the way `WorldSelector`'s
`beginButtonText` already does (lines 153–158): "Interview Chloe" for one, "Sit down at the Table
with Chloe and Papnoute" for two or more. The good pattern already exists in the codebase.

---

#### P1-2 · "Nicene", "creedal", "the floor", "Criterion 2", "Step 0", "Article 4" all appear in participant copy with no gloss

`atlas-v3.html` uses "Nicene" four times in visible copy and never defines it:

- line 456 (footer): *"outside the Nicene base this project builds from"*
- line 897 (every excluded node's icon tooltip): *"outside the Nicene base — grounds stated in the entry"*
- line 1007 (Categories glossary): *"Traditions outside the Nicene consensus this project builds from —
  included on the map, marked plainly as outside the floor."*

"the floor" is CiC-internal metaphor with no external referent at all. And `statusMeta` — which *is*
the clean, visitor-language field the click document uses — still carries process vocabulary in three
of its descriptions (`world-census.json`):

> "Excluded because its authority rests on one person's revelation or standing **(Criterion 2)** — the
> theology was not the problem."
> "Named in the **Step 0** record as a live future candidate or a dropped voice, with reasoning..."
> "The survey for this era has not yet run."  ← this one is right; the other two are not

The era header displays `academicName` verbatim (line 741): a newcomer's first screen says
**"The Ante-Nicene Period"** and **"The Constantinian/Nicene Era"** with no explanation of either.

This matters more than ordinary jargon because these are the words carrying the project's *honesty*
commitment. If "outside the Nicene base" is opaque, an exclusion reads as an unexplained judgment —
the precise impression the design is trying to avoid.

**Fix.** Add "Nicene" and "the doctrinal floor" to the generated glossary block as two plain
definitions (one sentence each: the creed agreed at a council in 325 and completed in 381, and the
line this project draws using it), and link the first use in the footer to it. Strip "(Criterion 2)"
and "Step 0" out of `statusMeta` descriptions — those two strings exist specifically to be the
visitor-facing version.

---

#### P1-3 · The best line of copy per era is authored in the census and rendered nowhere

`world-census.json` gives every era a `tag`:

> `"tag": "The apostles' children, under an empire that could turn on them"`
> `"tag": "Reform, renewal, and the new orders"`
> `"tag": "The center of gravity moves south and east"`

These are excellent — they are the one place the map tells a newcomer what an era *felt* like.
`grep` across `cic-website/` for `.tag` returns no render site. The era header bar (lines 740–743)
renders `no`, `title`, `academicName`, `dates`, `keyEvents` — everything except the human line.

Related, in the same records: `rec` **is** stale and **would be wrong if rendered**. Eras III–IX carry
`"stepStatus": "Step 0 run complete — era FROZEN by Mark 2026-08-02"` alongside
`"rec": "The Step 0 assessment for this era has not yet run — entries below carry signals, not
verdicts."` The click document correctly reads `stepStatus` (line 1283), so this is latent, not live —
but it sits one field away from `tag`, so anyone wiring `tag` up will trip over it.

**Fix.** Render `tag` in `.erahead` in place of, or above, `academicName` — it is strictly better copy
for the target reader, and `academicName` can move to a secondary line or the tooltip. Delete or
correct `rec` in the same pass.

---

#### P1-4 · Level 3 hands a participant a raw JSON dump, and its section labels are schema vocabulary

`cic-poc/frontend/src/components/Level3Panel.tsx` lines 86–90:

```jsx
{showFullRecord && (
  <pre className="orq-scaffold__full-record">
    {JSON.stringify(face.full_record, null, 2)}
  </pre>
)}
```

The button offering this reads "Show the full record". This is the layer the constitution describes as
"full scholarly apparatus" — the promise that nothing is hidden. What arrives is a pretty-printed JSON
object with `field_relations`, `contested_claim_ids`, `cache_stability: static`, `register: emic`, and
`jobs: [1,2,4,6]` in it.

The scaffold above it leaks schema vocabulary too. `cic-poc/backend/wrs/views/level3.py` lines 183–188
label `world_core` fields as **"Time window"**, **"Horizon"**, **"Formation logic"**, and — untranslated —
**"Telos"**. Line 214 tells the participant *"This record's confidence level is 'Inferential-Thin'"*;
line 246 says *"This story is a marked composite reconstruction (Tier 4)"*. `CONFIDENCE_PLAIN` in
`plain_explanation.py` already contains beautiful plain renderings of every one of those confidence
levels ("this rests on thin evidence and inference. Hold it loosely.") — Level 3 does not use it.

**Fix.** Render `full_record` as a definition list of human-labelled fields with the internal keys
suppressed, not as JSON — or, cheaper and honest, relabel the button "Show the raw data record" so it
stops promising a readable thing. Reuse `CONFIDENCE_PLAIN` for the `_question`/`_reflect` confidence
lines. Gloss "Telos" as "What it was ultimately for."

---

#### P1-5 · Chloe never says the word "baptism", and leaves three Greek terms unglossed

`CiC_W1_Representative_Permanent_Prompt_Chloe.txt` glosses *ekklesia* well (¶1: "the assembly, the
church of God, called out and gathered under whatever roof will hold it") and *diakonoi* by
apposition (¶13). It does not gloss **eucharistia**, **episkopos**, or **presbyteroi** (all ¶13), and
**catechumen** appears four times (¶¶15, 33, 35, 37) never once explained.

More consequentially, baptism is referred to throughout as *"the water"* and never named:

> "You teach those preparing for the water, before they come to it." (¶1)
> "whether a member who has failed badly, **after the water**, can still be forgiven" (¶13)
> "a catechumen's question the night before the water" (¶15)

This is beautiful in-world writing and I would not want it removed. But a reader with no church
background may simply not connect "the water" to baptism, which means the whole second fear in ¶19 —
one of the two anxieties the entire voice is organized around — may not land at all.

Chloe's prompt also carries **no gloss-as-you-go instruction**. Papnoute has ¶11's plain-meaning-first
pattern; Yausep has ¶43's explicit "ground each one, briefly, in what it means." Chloe has neither.

**Fix.** Add Yausep ¶43's instruction (or a compressed version) to
`Representative_Permanent_Prompt_Template.txt` as standing boilerplate, so every world gets it rather
than two of six by chance. In Chloe specifically, name baptism once — "the water of baptism" on first
use in ¶1 — and gloss *catechumen* in the same apposition style ¶13 already uses for *diakonoi*.

---

#### P1-6 · Yausep breaches 5c's grade ceiling, and 5d's required boilerplate is why — but it is present in only one of the three prompts

Measured: Yausep **FK 10.3** against 5c's stated 8–10 band ceiling; **35 of 140 sentences (25%) exceed
30 words**, against 5c's *"Break any sentence over roughly 25-30 words"*; nine sentences exceed 50
words, the longest **86 words**:

> "Hold this operational test for every sentence you speak, not only an opening or closing one: if
> this sentence were deleted, would the listener lose something real about our history, our practice,
> or our God — something that could, in principle, be pointed to in our own record — or would they
> lose only a scene invented to satisfy the question, a description of how you are choosing to speak
> with them right now, or an explanation of why you are declining to answer as asked?"

The cause is structural and traceable: ¶¶7–15 are the **5d museum-guide backstop boilerplate**
(`Representative_Permanent_Prompt_Template.txt` lines 663–681), ~590 words of pure meta-instruction
about failure modes. 5d requires it "present in the completed prompt, unedited" — and it is present in
**Yausep only**. Chloe's and Papnoute's prompts contain no museum-guide passage at all.

So there are two findings tangled together and both matter for this angle:

1. Yausep is over the ceiling, and the overage is concentrated in template boilerplate that 5c's own
   sentence-splitting was never applied to.
2. Two of three prompts are missing a check 5d calls mandatory — which also means **~590 of Yausep's
   3,304 words (18%) are spent on anti-failure instruction that Chloe and Papnoute spend on world
   content**. For a participant, the practical effect is that Yausep has proportionally less room for
   the faces, names and scenes that make a tradition interesting.

**Fix.** Apply 5c's split to the 5d boilerplate once, in the template, so every world inherits the
shortened version. Then either bring Chloe and Papnoute into 5d compliance or record why they are
exempt — the current state is neither.

---

#### P1-7 · The onboarding screen sits just under the project's own Reading Ease floor, and is 503 words before anything can be done

`OnboardingScreen.tsx`: **FK 9.7 (inside the ≤10 ceiling), FRE 59.9 (the floor is 60)**. That is a
hair's breadth, and within my ±0.5 caveat — but it is the wrong side of the line on the project's own
number, and it is the screen that gates every single conversation.

Structurally it is eight `<h3>` sections and 503 words before the "I understand — let's begin" button.
The content is good (§2.8) and none of it is padding; the issue is that it all arrives at once, before
the participant has any reason to care about most of it. "Reading the highlights" in particular
explains an interaction the reader has not yet seen.

**Fix.** Split it: keep "What this is", "This is a prototype", and "We're cataloging this conversation"
on the gate screen (~220 words, and the FRE will rise on its own once the longest sentences go), and
move "Reading the highlights" to a one-time inline tooltip on the first highlighted term the
participant actually meets. Split the four sentences over 30 words to clear the floor.

---

#### P1-8 · The reading-floor check that is supposed to run "at render time, always" cannot run, and the general gate is dead code

`wrs/gates/core.py` line 207 does `import textstat` inside `readability_check`. **`textstat` appears in
neither `cic-poc/backend/requirements.txt` nor `pyproject.toml`** — verified by reading both files in
full. Running the module's own entry point reproduces it:

```
$ python3 wrs/views/plain_explanation.py
ModuleNotFoundError: No module named 'textstat'
```

`plain_explanation.py`'s docstring says the floor is *"computed at render time on every render,
always"* (lines 8–9), and `render_plain_explanation` calls it unguarded (line 175) — so in an
environment without the package this raises rather than degrading. Separately, `gate_readability`
(line 218), the function that would apply the floor to arbitrary texts, is called from **no production
path** — only from `run_gates.py`'s fixture self-test. That is the mechanical reason P0-4 was able to
happen: the project has a reading-floor instrument and points it at one surface.

**Fix.** Add `textstat` to both dependency files. Wrap the import so a missing library reports "floor
not checked" rather than 500-ing a participant request. Then point `gate_readability` at the surfaces
that actually need it — the census fields, the World Capsule Cores, and the Permanent Prompts — as a
CI check.

---

#### P1-9 · Guided Starters ship for five of six worlds, and the bundled data says it is not deployed

`guided_starters.json` covers `post-apostolic-house-church`, `alexandria-catechetical`,
`desert-monasticism`, `hieronymian-ascetic-literary`, `syriac-edessa-nisibis` — **not**
`imperial-juridical-christianity`. `guidedStarters.ts` line 27 handles this by silently omitting the
world, and `ChatInput.tsx` lines 15–16 hides the affordance entirely if no seated world has content.

That is graceful degradation, and it is the right engineering call. But given that the Guided Starters
are the single strongest newcomer aid in the system (§2.2), the practical result is that a newcomer
who picks Marius gets the *least* support of the six — with no signal that anything is missing.

Also: every world record in that bundled file carries
`"status": "DRAFT — awaiting Mark's review. Not deployed."` while being compiled into the shipping
bundle. The status string is not rendered, so no participant sees it, but the data is asserting
something about itself that is no longer true.

**Fix.** Draft the Imperial-Juridical set — it is the only gap, and the format is proven. Update the
`status` strings to match reality.

---

#### P1-10 · Papnoute's hard brevity cap has no newcomer-facing escape hatch inside the voice

`CiC_W3_Representative_Permanent_Prompt_Papnoute.txt` ¶21:

> "Hold to this as a hard measure, not a preference: four sentences is already long for you, and most
> of what you say should be one to three."

and ¶23:

> "You do not ask in order to keep a conversation going. Silence keeps it just as well."

Both are historically right and I would not soften either — the terseness *is* the tradition. But
consider the actual newcomer path: someone with no background types "so what was the desert thing
about?" and receives two sentences, with no return question. The prompt's own deepening rule (¶19,
"what opens later, once trust has grown") requires the participant to know what to ask next in order
to earn it.

The mitigation exists and is good — "Don't know what to ask?" is persistently visible above the input
(`ChatInput.tsx` lines 85–91) — which is why this is P1 and not P0. But it is a UI affordance
compensating for a voice constraint, and it only fires if the participant notices the button rather
than typing.

**Fix.** No change to the cap. Add one sentence to Papnoute's ¶19 authorising the *elder's own*
move — naming the next thing worth asking about, in one clause, without lengthening the answer. That
is period-faithful (an abba directing a visitor's attention is well attested) and costs nothing
against the four-sentence rule.

---

### P2 — polish

- **P2-1 · The "Reading the marks" footer is itself above the reading floor.** `atlas-v3.html` lines
  446–464 measures **FK 13.0, FRE 49.8** — the block explaining the map to newcomers is harder than
  the map. Six sentences carry 161 words. Split them.
- **P2-2 · 32 entries show a hover card with no description line at all.** `atlas-v3.html` line 1247
  falls back `m.teaser || m.entry.tile || ""` and renders nothing if both are absent; 32 of 257
  entries hit that. The card degrades to name/dates/family/status — and for most of those, "status" is
  a P0-2 jargon string. Authoring 32 teasers closes both.
- **P2-3 · "Built worlds" is team vocabulary on the map's most important control.** `atlas-v3.html`
  line 416. "Built" means "you can talk to this one now" — which is the only reason a newcomer is on
  the page. The footer glossary says it ("House — built and open: you can sit down with this tradition
  now"), but the footer is where P0-1 says nobody has been yet. Relabel: "Open for conversation (6)".
- **P2-4 · "A space for engaging conversation."** `TheTable.tsx` lines 228/255 — generic subtitle
  under the app's main heading, saying nothing the heading did not. Replace with the seat list, which
  the component already computes as `repNames`.
- **P2-5 · The `/api/repository` 404 shows an internal file path to the participant.**
  `app/main.py` lines 1892–1895: *"repository views exist for migrated worlds only (generated by
  wrs/views/repository.py)"*. Visitor language.
- **P2-6 · "For the Wrestling" as a tier label.** `QuestionSheet.tsx` line 23. The other three
  ("First Visit", "Going Deeper", "Honest Limits") are transparent; this one is in-house idiom. The
  questions behind it are the best in the set — they deserve a label that says so ("Push Back" /
  "The Hard Questions").
- **P2-7 · Search placeholder is doing two jobs.** `atlas-v3.html` line 415: *"Have a movement or
  period in mind? Search by name — e.g. Coptic, Reformation, Pentecostal"*. It is the only welcoming
  sentence above the fold and is therefore carrying orientation duty it was not designed for — which
  is a symptom of P0-1, and will read better once P0-1's orientation line exists above it.

---

## 4. Now vs. over time

### Now — before another newcomer opens the map (hours, not days)

1. **P0-2** — point the hover card and `aria-label` at `statusMeta[...].shortWord`. Two-line change;
   removes internal jargon from 182 of 257 entries and from every screen-reader label.
2. **P0-1** — add a visible three-sentence orientation line under `#controls`, and hoist "Reading the
   marks" into a `<details>` at the top of the map.
3. **P0-3, second half** — branch the "Sources to research" empty state on `Built & Live` so the six
   live worlds stop claiming their source base is pending.
4. **P1-2, second half** — delete "(Criterion 2)" and "Step 0" from the three `statusMeta`
   descriptions that carry them.
5. **P1-8** — add `textstat` to `requirements.txt`/`pyproject.toml` and guard the import.

### Next — the one pass that does most of the work (a week)

6. **A participant-copy pass over `world-census.json`.** One file, one sitting, and it closes P0-4
   (sentence splitting across `longDescription`/`legacy`/`teaser`), P0-3's first half (backfill six
   `sources` arrays), P1-3 (render `tag`, fix `rec`), P2-2 (32 missing teasers) and most of P2. This
   is the highest-leverage single action available.
7. **P1-1** — define "the Table" once in onboarding; make the atlas CTA reflect seat count.
8. **P1-5 / P1-6** — put Yausep ¶43's gloss-as-you-go instruction into the Permanent Prompt template
   as standing boilerplate; apply 5c's sentence split to the 5d museum-guide passage in the template;
   name baptism once in Chloe.
9. **P1-9** — draft Imperial-Juridical Guided Starters, closing the last coverage gap in the system's
   best newcomer aid.

### Over time — the structural work

10. **P0-5** — author `plain_explanation` for the remaining 100 term records, world by world, using
    the Desert set as the template; build `repository.json` for the other five worlds. Until then,
    amend 5c so it stops claiming a backstop that exists for one world in six. *Do not leave the
    promise standing while the mechanism is one-sixth built* — that is the finding, not the schedule.
11. **P1-4** — render Level 3's `full_record` as human-labelled fields rather than JSON; reuse
    `CONFIDENCE_PLAIN` in the Level-3 scaffold.
12. **P1-7** — split the onboarding screen; move "Reading the highlights" to the moment of first use.
13. **Extend the reading floor to every participant-facing surface** by pointing `gate_readability` at
    the census, the Capsule Cores (PAHC's measures FK 13.6 / FRE 54.0 against Desert's 9.8 and
    Syriac's 7.8), and the Permanent Prompts, as a CI check. P0-4 is CO-015's defect recurring on a
    surface the fix never covered; the durable fix is coverage, not another manual pass.

---

## 5. Bottom line

**Is this accessible and engaging to a non-academic today? No — not yet, and not because of the
history writing, which is excellent.**

I want to be precise about the shape of this verdict, because "not yet" could easily be heard as
harsher than I mean, and softening it would be worse than either.

The *content* passes this review comfortably. The census teasers, the `voices` entries, the story
chunks, and the three Permanent Prompts are genuinely good popular history — human, specific,
honest about silence, written by someone with an ear. The Guided Starters at FK 4.8 are better than
almost anything comparable I have read. Desert's Level-2 plain explanation of *anachōrēsis* at FK 4.73
is a small masterpiece of making a hard word easy without making it smaller. If a newcomer read the
Pelagianism teaser, then a Guided Starter question, then talked to Chloe, they would have a genuinely
interesting time and would want to keep going.

The problem is the **delivery layer between that material and the newcomer**, and it fails in ways
that are measurable, specific, and — this is the important part — mostly not hard to fix. A first-time
visitor lands on an unlabelled diagram with no sentence telling them what it is (P0-1). They hover a
box and read `Researched — viable, secondary (Era 9 Step 0)` (P0-2). They get curious about one of the
six traditions they can actually talk to, and the map tells them its source base is pending when a
53-row registry is sitting in the same repository (P0-3). They open an entry and meet a well-written
105-word sentence (P0-4). And behind all of it, the standard that permits hard vocabulary to stay does
so on the strength of a glossary backstop that is built for one world in six (P0-5).

None of these are content failures. Every one is a plumbing failure between good content and the
person it was written for — which is why the verdict is "not yet" rather than "no."

**The single biggest lever is a participant-copy pass over `cic-website/data/world-census.json`.**
That one file is simultaneously the atlas's entire content, the source of every string that reaches a
participant on the map — hover, click document, status, era headers — and the place where both the
best writing (teasers) and the worst leaks (`statusWord`, empty `sources` on the six live worlds,
`tag` authored and never rendered) live side by side. One disciplined pass over it closes one P0
outright, most of a second, one P1 and four P2s, and does not require touching a line of application
code. Everything else on the list is real, but nothing else buys that much for that little.

---

*Reviewer's note on process: findings P0-2, P0-3, P0-4, P0-5, P1-6 and P1-8 are counted, not
estimated — each number was produced by reading the actual file or dataset and counting, and the
counting method is stated inline so it can be re-run. The three claims I took from
`01_DesignDoc_Mining.md` §3 were re-verified against their own cited sources
(`Representative_Permanent_Prompt_Template.txt` 5c/5d and `wrs/parameters.yaml`) rather than trusted;
all three check out verbatim. FK/FRE figures are from my own implementation of the standard formulas
because `textstat` is not installed (P1-8) — treat individual grades as ±0.5 and comparisons between
my own numbers as sound.*
