# Lexicon Gloss & Phrase-Gap Audit — Proposal for Review

**Date:** 2026-07-23
**Status:** Proposal only. Nothing in this document has been implemented. No frontend or backend code was touched to produce it. Every gloss below is drafted from the term's own existing lexicon-entry content (Quick Meaning / World Meaning / Distortion Risk) or from the story chunk it appears in — nothing here introduces a historical claim that wasn't already present in the source material.

**Purpose:** This is source material for the project owner to review one decision at a time, not a finished spec. Each item below is a recommendation, not a settled choice — accept, reject, or edit any single line independently of the rest.

**What this document is for:** Two things, per the task that produced it.

- **Category A** — for every existing lexicon term in each world, a proposed short modern-language gloss (the kind that would lead the sentence in the new "modern gloss (original term)" rendering pattern — e.g. "we prepare for the baptism (water)"). Where no clean modern equivalent exists, that is flagged explicitly rather than forced.
- **Category B** — phrase-level expressions found in each world's Permanent Prompt, World Capsule Core, or story chunks that are **not currently tracked as lexicon terms at all**, but that a Representative would plausibly say in voice and a modern reader would not decode (the paradigm case: "the day of the sun" for Sunday). Day/date-naming was the confirmed starting category; other categories — time-of-day, units of measure, descriptive-not-formal titles — were checked in each world, and the finding (including "nothing found") is reported honestly rather than assumed.

**Confidence key used throughout:**
- **High** — the gloss is essentially just the term's own Aliases/Quick Meaning restated plainly; very low risk of distorting the entry.
- **Medium** — the gloss is a fair compression of the entry but involves a judgment call about which facet to lead with.
- **Flagged / no clean equivalent** — the entry itself documents that the obvious modern word is a false friend, or that nothing in English captures it cleanly.
- **Confirmed** — settled in a live, one-decision-at-a-time review with the project owner. This is no longer a recommendation; it's the final wording, and the Notes column records what was decided and why (including any alternatives that were considered and rejected along the way). Everything not marked Confirmed remains an open recommendation awaiting review.

**General rendering rule, decided during project owner review — applies document-wide, not just to the items marked Confirmed:**
- **Category A (vocabulary terms):** modern gloss leads, original term follows in brackets — e.g. "we prepare for the baptism (water)." This was the pattern already used throughout Category A in this document and stays unchanged.
- **Category B (phrase-level circumlocutions):** original phrase leads exactly as attested, modern reference follows in brackets — e.g. "the day named for the sun (Sunday)," **not** "Sunday (the day named for the sun)." This is the opposite order from an earlier draft of this document, which had written Category B glosses the same way as Category A. Reasoning: Category A terms are genuinely opaque vocabulary a reader can't parse without help; Category B phrases are readable and often evocative on their own, and only need their specific reference resolved, not translated. This rule has been applied to every Category B entry below, decided or not.

---

## 1. Syriac World (Yausep) — 10 lexicon terms

### Category A

| # | Term | Recommended gloss | Confidence | Notes |
|---|------|-------------------|------------|-------|
| 1 | raza | *(a sign tied to a hidden truth)* | **Confirmed** | Decided in project owner review — final gloss, not a recommendation. Grounds: the entry's own Distortion Risk section says the obvious modern word — "symbol" — is the wrong hearing (a modern symbol is arbitrary/agreed-upon, while raza is bound to the truth it signifies). This wording was settled on in place of the fuller two-part phrase this document originally proposed. Do not gloss as "(symbol)." |
| 2 | shrara | *(the truth itself)* | High | Paired term to raza; entry states this plainly. |
| 3 | qyama | **No clean modern equivalent** | Flagged | Confirmed by the coordinator as the paradigm no-equivalent case. It names a lifelong covenant vow of celibacy kept *inside* ordinary town life among one's own kin — not monastic withdrawal, not simply "vow," not "order" in the institutional sense. Recommend leaving qyama unglossed, or at most "(a kept lifelong vow)" with a note that this is a partial gloss, not a translation. |
| 4 | taḥwîṯâ | *(a demonstration / teaching-treatise)* | Medium | Aphrahat's own genre-term for his 23 doctrinal treatises, conventionally titled "Demonstrations" in English (corresponding to the Greek *apodeixis*). Several are built on the 22-letter Syriac acrostic, so the alphabet itself scaffolds the argument in memory — this is a paraphrase of the entry's own World Meaning, not a direct quote. Note: the entry itself also records that Aphrahat sometimes called these same works "Letters," so "(a demonstration)" is the better-attested lead gloss over anything narrower. |
| 5 | madrasha | *(teaching-hymn)* | High | Entry frames these as hymns that carry the teaching itself, not decoration. |
| 6 | memra | *(a verse composition)* | Medium | Entry itself flags an anachronism caveat on this term — hold loosely. |
| 7 | Ewangeliyon da-Mhallete | *(the harmonized Gospel)* | High | Paraphrased, not quoted, from the entry's own World Meaning: throughout this world's period "the Gospel" meant a single continuous harmonized narrative (Tatian's Diatessaron), not four separate books — the formation experience of hearing it is "the experience of a single unfolding story" (this closing phrase is an exact quote from the entry). |
| 8 | Iḥidaya | *(the undivided one)* | **Confirmed** | Decided in project owner review — final pick between the two options this document originally offered as a genuine judgment call (the entry holds two senses together: ascetic single-mindedness and the christological "Only-Begotten"). "(the undivided one)" was chosen over the other candidate, "(the Single One)," foregrounding the formation-ideal sense. |
| 9 | Mar | *(my lord / an honorific like "Saint")* | High | Corrected from an earlier draft of this document, which quoted a sentence — "a word for a teacher whose standing is real, without settling... what confers that standing" — that does not exist in `syrlex008_mar.md` and has been removed. The entry actually glosses Mar as "my lord," an honorific used across Syriac Christianity for bishops, saints, *and* revered teachers (not narrowed to teachers alone), "roughly parallel to 'Saint.'" The entry also flags that "Mar Ephrem" specifically is not confirmed as a form of address used during Ephrem's own lifetime — worth carrying as a caveat if the gloss is ever attached to that specific name. |
| 10 | Catholicos | *(not a term Yausep would use — out of scope)* | — | This entry exists in the lexicon as an anachronism-flag/gating entry, not a term the Representative affirmatively uses in voice. Recommend excluding it from the inline-gloss rendering entirely rather than forcing a gloss; flagging this as a scope question for whoever builds the rendering list, not a gloss question. |

*(The "Aphrahat's Anti-Jewish Demonstrations" entry, syrlex010, is a content-gating/topic entry rather than a vocabulary term — same recommendation as Catholicos: exclude from the inline-gloss list, not a Category A candidate.)*

### Category B — phrase-level gaps found

**Day/date naming (still an open recommendation — not decided in review):**
- `syrstory002_edessa-flood-201.md` uses **"the month of Tishrin"** paired with an in-text gloss ("November") and a Seleucid-era year reckoning ("513 by the reckoning of the Greeks"), which the story itself already glosses as "(201 CE)." Because the story chunk already parenthesizes both, this is **lower priority** — the existing text already does what Category B asks for. Recommend leaving this one alone unless the rendering mechanism specifically needs a lexicon-style entry to trigger (in which case a short entry — under the phrase-leads-gloss-follows rendering rule — reading **"Tishrin (roughly October–November)"** would be easy and low-risk to add).

**Other categories checked, nothing significant found:** time-of-day references, units of measure, and descriptive titles in the Syriac material are sparse and mostly already plain ("before dawn" in syrstory009 is already modern-legible). No hidden units-of-measure or title-circumlocution gap found in this world's material.

---

## 2. Desert World (Papnoute) — 9 lexicon terms

### Category A

**Correction note:** an earlier draft of this document listed Xeniteia, Apatheia, and Penthos as Desert lexicon terms. They are not — they appear only as passing Related-Terms cross-references inside other entries (`desertlex001`, `desertlex004`, `desertlex005` respectively) and have no lexicon file of their own. They've been dropped. The table below was rebuilt by reading all 9 actual files directly (`desertlex001` through `desertlex009` in `cic-poc/backend/data/desert_world/lexicon_chunks/`), including the 6 that were already listed correctly — none of those 6 were carried forward from memory without re-checking.

| # | Term | Recommended gloss | Confidence | Notes |
|---|------|-------------------|------------|-------|
| 1 | Anachōrēsis (Withdrawal) | *(withdrawal)* | High | Entry's own built-in parenthetical; Quick Meaning: "departing settled village or civic life... undertaken as the ascetic project itself, not a change of address." |
| 2 | Apotagē (Renunciation) | *(renunciation)* | High | Quick Meaning: "Formal renunciation of property, family ties, and worldly status marking entry into ascetic life." Entry's Distortion Risk warns against hearing this as a single dramatic one-time gesture — it's an ongoing, re-enacted discipline, not a one-time transaction. |
| 3 | Hēsychia (Stillness) | *(stillness)* | High | Quick Meaning: "Interior and exterior stillness, cultivated as both precondition and fruit of ascetic discipline." Entry cautions against reading this as modern "mindfulness" — it's pursued to expose, not soothe, interior disturbance. |
| 4 | Logismoi (The Thoughts) | *(the thoughts that trouble the mind)* | **Confirmed** | Decided in project owner review — final gloss, not a recommendation. Entry's own Aliases line lists "intrusive thoughts" as a recognized alias, but its Distortion Risk explicitly warns against the secular-clinical hearing (a symptom to manage or medicate). Do not gloss as "(intrusive thoughts)." |
| 5 | Diakrisis (Discernment) | *(discernment)* | High | Quick Meaning: "The capacity to judge rightly between competing courses of action, spirits, or thoughts — this world's own master virtue." Entry warns this is not a soft, individualized "trust your gut" — it's a relationally-developed skill specifically aimed against self-deception. |
| 6 | Gerōn / Abba / Amma (Elder / Father / Mother) | *(elder — "father"/"mother" as a title of spiritual authority)* | High | Quick Meaning: "Honorific address for a spiritually authoritative elder, male (abba) or female (amma), whose sayings and example carry teaching authority without formal ecclesiastical office." |
| 7 | Cheirōnaxia / Ergocheiron (Manual Labor) | *(manual labor)* | High | Quick Meaning: "Manual labor — chiefly rope- and basket-weaving — undertaken as both economic necessity and deliberate ascetic discipline." Entry stresses this was spiritually formative in itself, not incidental subsistence work. |
| 8 | Apophthegma (Saying) | *(a saying / teaching-saying)* | High | Quick Meaning: "The terse, memorable saying that is this world's primary vehicle of teaching." Entry notes the form's brevity is itself a formation technique, not just a container for content. |
| 9 | Koinōnia (Communal Rule) | *(Pachomius's monastic federation)* | **Confirmed** | Decided in project owner review — confirmed as already corrected in the prior independent-review pass (see Correction log below). The entry's own Quick Meaning: "The founder Pachomius's own name for his federated network of monasteries under a single Rule and spiritual authority." This is a proper name for a specific institutional innovation (multiple houses, common property, formal offices, a written Rule) — not a warm communal feeling, and the entry flags it as this world's most strand-bound term, with no equivalent among the more solitary ascetics. |

### Category B — phrase-level gaps found

**Day/date naming — resolved as a source fix, not a gloss. Nothing left to gloss here.**

An earlier draft of this document carried an open item about `desertstory008_day-in-a-kellia-cell.md`'s "on the sixth day" phrasing conflicting with the same story's own sourced "Saturday-to-Sunday" synaxis rhythm, and recommended either dropping it or flagging the inconsistency. That has since been resolved directly at the source, outside this document and outside this worktree: a separate deep-dive (not this document's own original pass) confirmed this was a genuine source-content error under the world's own period-authentic day-counting, not a gloss question. `desertstory008_day-in-a-kellia-cell.md` has been corrected on `main` — the Story Text now reads "on the Sabbath and the Lord's Day," and the front-matter Source line carries a visible, participant-facing correction note (confirmed to actually surface in the app's own citation modal, not just in the repo). See commits `0276b6b` and `64d65d8` on `main` for the full account. This item is now closed — removed from the open Category B gap list, with no gloss needed since the underlying phrase itself was fixed rather than translated.

**Other categories checked:** no clear units-of-measure or descriptive-title gaps found in the Desert material beyond the lexicon terms already covered above (Gerōn/Abba/Amma is itself a title-type term already captured in Category A).

---

## 3. Hieronymian World (Albina) — 15 lexicon terms

### Category A

| # | Term | Recommended gloss | Confidence | Notes |
|---|------|-------------------|------------|-------|
| 1 | Hebraica veritas | *(the Hebrew truth)* | High | Near-literal, entry supports directly. |
| 2 | Vulgata | *(the new Latin translation)* | **Confirmed** | Decided in project owner review — final gloss, chosen over the other candidate this document originally offered ("Jerome's Bible translation"). This remains a genuine trap worth flagging for anyone building the rendering list: the entry's own Distortion Risk explicitly warns that "the Vulgate" as a name/status is anachronistic for this world's period — Jerome's translation had not yet acquired that later official standing. Do not gloss as "(the Vulgate)." |
| 3 | Renuntiatio | *(renunciation)* | High | — |
| 4 | Virginitas | *(consecrated virginity)* | High | — |
| 5 | Vidua | *(ascetic widowhood)* | High | — |
| 6 | Patrocinium | *(patronage)* | High | — |
| 7 | Epistula | *(the letter)* | High | Already near-transparent; low priority but harmless to include. |
| 8 | Origenism | *(a theological position, later disputed)* | Medium | Already reads as an English word to most readers; recommend low priority for glossing, or skip. |
| 9 | Pelagianism | *(a theological position, later disputed)* | Medium | Same as above — low priority. |
| 10 | Matrona | *(a Roman noblewoman of standing)* | High | — |
| 11 | Exegesis (as practiced authority) | *(recognized teaching authority, held without office)* | Medium — corrected | Corrected from an earlier draft, which glossed this as plain "(interpretation)" — too general, and it flattens the entry's actual point. `hal_lex11` is specifically about one woman's (Marcella's) standing to be consulted on hard scriptural questions *without holding any clerical office* — the entry's own Distortion Risk explicitly rejects treating this as "merely social/informal and therefore unimportant," while also warning against overclaiming it as equivalent to ordination. Recommend leading with the authority-without-office framing above rather than the generic word "interpretation," which could describe anyone reading a text and loses what's actually distinctive about the entry. |
| 12 | Grammaticus | *(classical schooling)* | High | — |
| 13 | Praefatio | *(preface)* | High | — |
| 14 | Nosocomium | *(hospital)* | High | Entry itself notes this Greek word was left untranslated even by Jerome — i.e., historically it stayed foreign-sounding even in period. Still, "(hospital)" is the clean modern equivalent the entry supports. |
| 15 | Monachus | *(monk)* | **Highest confidence in this world** | The entry's own Distortion Risk section explicitly states this word is "likely unproblematic" and "maps reasonably well onto modern 'monk.'" |

### Category B — phrase-level gaps found

**Day/date naming:**
- `hal_story01_departure-from-rome.md` (Jerome, *Epistula* 108, describing his 385 CE departure — the story's own Retrieve-When line names "the 385 departure from Rome" directly) contains: *"he himself left Rome first, in the month named for the harvest."*
  - **Confirmed gloss, phrase-leads-gloss-follows order per the general rendering rule:** **"the month named for the harvest (August)"** — confidence upgraded from flagged-uncertain to confirmed. Jerome's own departure from Rome is independently documented as August 385 CE (per his letter to Asella, *Epistula* 45, written as he was leaving, and standard modern chronology of the episode) — this is corroboration from outside the story chunk itself, not just an inference from the chunk's own internal dating.
  - **One honest caveat worth keeping alongside the gloss, not smoothing over:** "the month named for the harvest" is not actually a literally accurate description of August in Roman naming — August is named for the emperor Augustus, not for the harvest. The month-*decode* (August) is solid; the story's own circumlocution, taken as a literal etymology, is loose. Worth flagging so nobody mistakes the phrase itself for a documented period name — it reads as the construction team's own stylistic circumlocution for the month, not a sourced ancient Roman name for it.
- No other day-of-week or hour-naming circumlocutions found in this world's material — Hieronymian content is centered on letters, scholarship, and Rome/Bethlehem rather than liturgical daily rhythm, which is consistent with what the World Capsule Core itself says about where this world's attention concentrated.

**Other categories checked:** units of measure and descriptive titles — no clear standalone gaps found beyond what Category A above already covers (Matrona, Grammaticus are themselves title/role terms already captured).

---

## 4. Imperial Juridical World (Marius) — 12 lexicon terms

### Category A

| # | Term | Recommended gloss | Confidence | Notes |
|---|------|-------------------|------------|-------|
| 1 | primatus (sedes apostolica) | *(primacy / Rome's authority)* | High | Entry's own alias list already gives "primacy," "apostolic see." |
| 2 | presbeia (tēs timēs) | *(rank of honor)* | High | Direct from the entry's own alias. |
| 3 | homoios | *(similar to the Father)* | **Confirmed** | Decided in project owner review — final gloss, simplified from this document's original recommendation of "(the 'like the Father' formula)." "Formula" itself was flagged during review as unclear jargon and dropped. This remains a genuine trap worth flagging for anyone building the rendering list: the entry's own Aliases line explicitly states "not 'Arian' (see Distortion Risk)" — do not gloss this term as "Arian." |
| 4 | communio | *(standing / being in fellowship)* | Medium | Modern "communion" already carries a private/devotional connotation the entry warns against; recommend leading with "(standing)" to signal the juridical sense, not "(communion)" bare. |
| 5 | Imperator intra Ecclesiam, non supra Ecclesiam | *(the emperor is within the Church, not above it)* | High | This is a formula, not a single word — the entry already gives this exact translation as its Quick Meaning. |
| 6 | homoousios | *(of one being with the Father)* | High | Direct from entry alias. |
| 7 | concilium (synodos) | *(council)* | High | Already a near-transparent English cognate. |
| 8 | haeresis | *(heresy)* | High | Already a transparent English cognate; low priority but harmless. |
| 9 | Tomus | *(a formal doctrinal letter)* | High | — |
| 10 | Nea Rhōmē | *(New Rome / Constantinople)* | High | — |
| 11 | basilica | *(church building)* | High | Already fairly transparent; low priority. |
| 12 | martyrium | *(martyr's shrine)* | High | — |

### Category B — phrase-level gaps found

**None found at meaningful confidence.** This world's material is unusual among the six in that it consistently anchors events to direct numeric calendar years (325, 341, 381, 386, 451) and named councils rather than period-style circumlocutions for dates, times, or measures. I checked all 6 story chunks and both the Permanent Prompt and World Capsule Core specifically for day-naming, time-of-day, and measure-circumlocution patterns and found none — this world's content is letters-and-councils-centered rather than liturgical-daily-life-centered, which is consistent with what its own World Capsule Core says about where this world's attention actually concentrated. Reporting "nothing found" here rather than forcing a finding.

---

## 5. PAHC World (Chloe) — 13 lexicon terms — likely origin of the "day of the sun" example

### Category A

All 13 terms in this world already carry clean English aliases, making this world's Category A the most uniformly high-confidence of the six.

| # | Term | Recommended gloss | Confidence | Notes |
|---|------|-------------------|------------|-------|
| 1 | episkopos | *(bishop / overseer)* | High | — |
| 2 | presbyteros | *(elder)* | High | — |
| 3 | ekklesia | *(assembly / church)* | High | — |
| 4 | eucharistia | *(the thanksgiving meal)* | High | — |
| 5 | diakonos | *(deacon / one who serves)* | High | — |
| 6 | presbyterion | *(council of elders)* | High | — |
| 7 | Two Ways | *(the teaching that lays the two paths of life and death before you)* | High | **Confirmed** — decided in project owner review 2026-07-25, wording edited from the original candidate above. |
| 8 | prophetes | *(prophet)* | High | Already transparent; low priority but harmless. |
| 9 | ministrae | *(servant-women, per Pliny's report)* | High | Entry itself is explicit that this is an outsider's word, not the community's own — worth preserving that framing in the gloss. |
| 10 | agape (as label) | *(the love-feast)* | High | — |
| 11 | baptisma | *(baptism)* | High | **Confirmed** — decided in project owner review 2026-07-25. This was always the coordinator's own tester example; the entry's Aliases list "the water," so the shipped form is "baptism (the water)," modern gloss leading, not the Greek "baptisma" in brackets. |
| 12 | hetaeria | *(a suspected illegal club, in Roman legal terms)* | Medium | — |
| 13 | pertinacia | *(stubbornness / refusal to recant)* | High | — |

### Category B — phrase-level gaps found (3 related items, one cluster)

This world supplied the clearest and best-sourced Category B material of any of the six — confirming the coordinator's expectation that this is likely where the "day of the sun" example itself originates. **All three items below are Confirmed — decided in project owner review, approved as one cluster (same referent, three attested phrasings), kept as three distinct entries for matching purposes rather than merged into one.** Gloss order follows the general rendering rule: phrase leads exactly as attested, modern reference follows in brackets.

1. **"the day named for the sun (Sunday)"** — `pahcstory006_justin-sunday-gathering.md`, directly quoting Justin Martyr's *First Apology* 67. The story chunk's own Usage Guidance already writes out the exact sentence: *"Justin tells the emperor that on the day of the sun, we gather..."* — this is almost certainly the coordinator's own source example.
   - **Confidence:** Confirmed — directly and explicitly sourced, with the Representative's own planned phrasing already written into the story chunk's Usage Guidance.

2. **"the Lord's own day (Sunday)"** — `pahcstory010_didache-eucharist.md`, from the Didache (14:1). A related but distinct circumlocution for the same day, from a different source-strand (Antioch/Syria rather than Rome).
   - **Confidence:** Confirmed — same referent as #1, different phrase, kept as its own entry since a Representative drawing on Didache material would use this phrasing rather than Justin's.

3. **"the first day of the week (Sunday)"** — used in the World Capsule Core itself ("a household that opens its door on the first day of the week"). A third variant, ordinal rather than named.
   - **Confidence:** Confirmed — already close to modern phrasing, but worth its own entry since it appears in Permanent-Prompt-adjacent material a Representative might echo directly.

**Other categories checked:** no significant units-of-measure gaps found. One soft candidate worth a brief mention rather than a full entry: `pahcstory008_martyrdom-of-polycarp.md` uses **"dies natalis, his birthday into true life"** for the community's annual death-anniversary commemoration — but the story chunk already glosses this inline ("his birthday into true life"), so it's lower priority; flagging it here for completeness rather than recommending a new entry.

---

## 6. Alexandria World (Theon) — 45 lexicon terms (largest world)

### Category A

This world's terms are different in character from the other five. Rather than opaque period vocabulary standing in for an everyday concept (like "water" for baptism or "the day of the sun" for Sunday), most Alexandria terms are Greek/Latin technical-theological words that are either (a) already common English religious vocabulary needing little gloss (sin, death, resurrection, faith, love, hope, prayer, virtue, church, salvation, incarnation), or (b) genuine Greek terms carrying real gloss value (Logos, gnosis, theosis, nous, autexousia, metanoia, oikonomia). Recommend prioritizing group (b) for the rendering mechanism; group (a) is included below for completeness but is low-priority.

**Higher-priority terms (genuine Greek/Latin vocabulary, real gloss value):**

| Term | Recommended gloss | Confidence |
|------|--------------------|------------|
| Logos | *(the Word)* | High — entry's own primary alias |
| Divine Pedagogy | *(God's ongoing teaching)* | High |
| Catechesis | *(formation before baptism)* | High |
| Illumination | *(the opening of sight / photismos)* | High |
| Knowledge / Gnosis | *(a transformative knowing of God)* | **Confirmed** — decided in project owner review. Final gloss avoids the bare word "gnostic," which the entry says risks being read as "very nearly the exact opposite" of what this world means (secret/elite/body-denying). |
| Wisdom / Sophia | *(wisdom)* | High — already transparent |
| Participation | *(a deep sharing in God's life)* | **Confirmed** — decided in project owner review. Revised from this document's original "(real sharing in God's life)" during the review conversation. |
| Theosis | *(being drawn into God's life)* | **Confirmed** — decided in project owner review, unchanged from this document's original recommendation. Must not be read as "becoming God" bare; entry stresses the Creator/creature distinction is presupposed, not erased. |
| Image of God | *(the image of God — eikon)* | High |
| Soul / Psyche | *(your whole self, body and heart together)* | **Confirmed** — decided in project owner review, after real back-and-forth. Two earlier candidates were tried and rejected: this document's original, "the whole person, not a separate spirit," was found too flat given the entry's own body-soul-nous depth framing — the entry states the nous is "the soul's own highest capacity, its depth rather than a separate resident," not three separate parts; a subsequent "living being" candidate was rejected as reading too physical/biological, missing the entry's explicit inclusion of desire and relationship as part of what the soul is. The final wording keeps unity (not a detachable ghost) while keeping the interior/emotional dimension the entry itself names. |
| Nous | *(the soul's deepest eye)* | **Confirmed** — decided in project owner review. Revised from this document's original "(the mind's eye / contemplative faculty)": "mind" was found during review to risk the exact modern-cognitive-reasoning misreading the entry's own Distortion Risk section warns against ("Intellect as abstract reasoning"). "The soul's deepest eye" avoids "mind" entirely and matches the entry's own repeated "soul's depth" framing. |
| Likeness of God | *(growing to reflect God more fully)* | **Confirmed** — decided in project owner review. Revised from this document's original "(the likeness — what the image grows toward)." |
| Freedom / Autexousia | *(the freedom to respond to God)* | **Confirmed** — decided in project owner review. An alternative considered during the review — "(the power to choose your own path)" — was explicitly rejected: the entry states freedom "is not the bare power to choose anything at all, balanced equally toward every option," and its own Distortion Risk section names exactly this autonomy/"choose your own path" reading as the modern misreading to avoid. "Freedom to respond to God" matches the entry's actual framing (freedom-for-response, not freedom-from-direction). |
| Christological Reading | *(reading Scripture toward Christ)* | High |
| Allegory | *(reading for the deeper meaning)* | **Confirmed** — decided in project owner review, unchanged from this document's original recommendation. |
| Rule of Faith | *(the received tradition)* | High |
| Repentance / Metanoia | *(a change of mind — turning back to God)* | High |
| Oikonomia | *(how God wisely arranges the whole plan of salvation)* | **Confirmed** — decided in project owner review. A shorter candidate, "(how God wisely arranges all things)," was considered and explicitly rejected as too generic/broad; the project owner asked to stay disciplined to the entry's true, narrower meaning (God's saving plan, centered on the Incarnation, not generic providence). |
| Mystery / Mysterion | *(a sacred reality known from within)* | **Confirmed** — decided in project owner review, unchanged from this document's original recommendation. Confirmed as the more accurate of two options considered: this is a near-direct echo of the entry's own Quick Meaning line, while the alternative ("grasped through participation") leaned too narrowly toward just the sacramental dimension. |

**Lower-priority terms (already close to plain English; gloss optional/low-value):** Wisdom, Faith, Love, Hope, Sin, Death, Resurrection, Restoration, Transformation, Christ, Son of God, Word of God, Baptism, Eucharist, Fasting, Prayer, Teacher, Bishop, Martyrdom/Witness, Household, Interpretation, Salvation, Virtue, Church/Ekklesia, Holy Spirit, Incarnation. These already read in English (or, like "Eucharist" and "Baptism," are terms most modern readers already have some working sense of, unlike "qyama" or "raza"). Recommend treating these as available-but-not-urgent for the rendering mechanism, rather than working through all 27 individually here — happy to draft any of them on request if the project owner wants full coverage rather than the prioritized subset.

**One genuine trap worth flagging specifically:** Logismoi-style false-friend risk does not really recur in Alexandria's vocabulary the way it did in Desert/Syriac/Hieronymian, with one partial exception — **"Gnosis"** carries real risk of being misread through the modern pop-culture association with "Gnosticism" (secret/elite/body-denying), which the entry says is "very nearly the exact opposite" of what this world means. Any gloss for this term should avoid the bare word "gnostic" and lead with "the knowing that changes the knower" instead.

### Category B — phrase-level gaps found

**None found at meaningful confidence.** I read the Permanent Prompt, World Capsule Core, and all 10 story chunks specifically checking for day-naming, time-of-day, and measure/title circumlocutions, following the same method used for the other five worlds. This world's material does not contain an equivalent to "the day of the sun" — its content centers on reading, teaching, and formation rather than a liturgical/calendar rhythm, and where it does reference the year's cycle it uses plain, already-modern-legible language ("the great fast," "the feast that follows it") rather than an opaque period term. Reporting "nothing found" honestly rather than manufacturing a finding to fill the category.

---

## Summary of totals

| World | Category A terms | Category B gaps found |
|---|---|---|
| Syriac | 10 (2 flagged: raza false-friend, qyama no-equivalent) | 1 (Tishrin/month-naming, low priority — already partly self-glossed in source) |
| Desert | 9, rebuilt from the actual files (2 flagged: logismoi false-friend, koinōnia false-friend with corrected gloss) | 1 candidate, unresolved — the "sixth day"/Friday reading contradicts the same story chunk's own sourced "Saturday-to-Sunday" gathering rhythm; recommend either dropping the item or flagging the source inconsistency rather than shipping a confident day-name (see write-up) |
| Hieronymian | 15 (1 flagged: Vulgata false-friend; Exegesis gloss corrected to preserve the authority-without-office point) | 1 confirmed (month circumlocution, "the month named for the harvest" = August, independently corroborated via Jerome's *Epistula* 45 and standard chronology — with the caveat that the phrase's own "harvest" etymology is loose even though the month-decode is solid) |
| Imperial Juridical | 12 (1 flagged: homoios/"not Arian") | 0 (world's material uses direct calendar years throughout) |
| PAHC | 13 (0 flagged — cleanest world) | 3, one cluster (day-of-week naming: "day of the sun" / "the Lord's own day" / "the first day of the week" — all = Sunday; this is almost certainly the coordinator's own source example) |
| Alexandria | 45 (18 prioritized as higher-value; 27 lower-priority/already-transparent; 1 soft false-friend note on "gnosis") | 0 (this world's material is not liturgical-calendar-centered) |

**Across all six worlds:** roughly 104 Category A terms addressed, with 6 flagged as false-friend traps (raza, homoios/"not Arian", Vulgata, logismoi, koinōnia, plus a soft caution on Alexandria's "gnosis") and one confirmed no-clean-equivalent case (qyama). Category B phrase-level gaps were found in 3 of the 6 worlds (Syriac, Hieronymian, PAHC) at safe-to-ship confidence, with Desert's single candidate held back pending a source-inconsistency fix rather than shipped as a confident gloss, and 2 of the 6 worlds (Imperial Juridical, Alexandria) genuinely showing no meaningful gap in that category once checked, because their source material isn't organized around liturgical daily/calendar rhythm the way the other four are.

---

## Correction log (this pass)

This document went through one round of independent review after its first draft, which found the following and required fixes — recorded here for the project owner's visibility into what changed and why, not just the final state:

1. **Desert Category A was rebuilt from the actual 9 files.** Three terms that were never their own lexicon entries (Xeniteia, Apatheia, Penthos — they only appear as Related-Terms cross-references inside other entries) were dropped, and three real entries that had been omitted (Apotagē, Cheirōnaxia/Ergocheiron, Apophthegma) were added, each drafted from its own actual file.
2. **Desert Koinōnia gloss was corrected** — it had reproduced the generic-fellowship misreading the entry itself warns against; now points at Pachomius's specific federated-monastery institution instead.
3. **Desert Category B's "sixth day = Friday" claim was pulled back** — it contradicted the same story chunk's own sourced "Saturday-to-Sunday" gathering rhythm, an internal inconsistency in the source data that isn't safe to paper over with a confident gloss.
4. **Syriac Mar had a fabricated supporting quotation removed** and its gloss rewritten from the entry's actual content ("my lord," an honorific like "Saint," for bishops/saints/teachers generally — not narrowed to "teacher of standing").
5. **Two Syriac rows (taḥwîṯâ, Ewangeliyon) had paraphrases presented as verbatim quotes** — fixed to either quote exactly or read plainly as paraphrase, and I re-checked the rest of the document for the same pattern (found and fixed one more instance in the original Desert Koinōnia row, addressed under item 2 above).
6. **Hieronymian Exegesis gloss was corrected** to preserve the entry's actual point (recognized teaching authority held without clerical office) rather than the flattened generic "(interpretation)."
7. **Hieronymian's "month named for the harvest" was upgraded** from a flagged, unverified guess to a confirmed reading of August, with independent corroboration cited and one honest caveat kept (the phrase's own "harvest" framing is a loose circumlocution, not a literal Roman etymology, even though the month it points to is right).

Everything not listed above — Syriac (aside from Mar and the two citation fixes), Hieronymian (aside from Exegesis and the August upgrade), Imperial Juridical, PAHC, and Alexandria — was independently re-verified and held up without changes.

---

## Decisions log (project owner review pass)

This document was then walked through live, one decision at a time, with the project owner. Everything below is settled — marked **Confirmed** at its own row/entry above — not a recommendation:

- **Syriac:** raza → "(a sign tied to a hidden truth)"; Iḥidaya → "(the undivided one)."
- **Desert:** logismoi → "(the thoughts that trouble the mind)"; Koinōnia → "(Pachomius's monastic federation)" (confirmed as already corrected); the "sixth day" Category B item is fully resolved as a source fix on `main` (commits `0276b6b`, `64d65d8`) and removed from this document's open gap list entirely.
- **Hieronymian:** Vulgata → "(the new Latin translation)"; the "month named for the harvest" Category B item confirmed = August, reformatted to "the month named for the harvest (August)" under the new rendering rule.
- **Imperial Juridical:** homoios → "(similar to the Father)" (simplified from the original "formula" wording, which was flagged as unclear jargon).
- **PAHC:** all three day-naming Category B entries confirmed as one cluster, kept as three distinct entries, reformatted to phrase-leads-gloss-follows order: "the day named for the sun (Sunday)," "the Lord's own day (Sunday)," "the first day of the week (Sunday)."
- **Alexandria:** Gnosis, Theosis, Participation, Nous, Soul/Psyche, Freedom/Autexousia, Likeness of God, Oikonomia, Mystery/Mysterion, and Allegory all confirmed — several went through real revision during the conversation (Nous, Soul/Psyche, and Freedom/Autexousia each had an earlier candidate wording explicitly rejected for reasons recorded at each row).
- **New general rendering rule** (applies document-wide, recorded at the top of this document): Category A glosses lead with the modern word, original term follows in brackets (unchanged from this document's original convention). Category B glosses lead with the original phrase exactly as attested, modern reference follows in brackets (a reversal from this document's original convention) — applied to every Category B entry in the document, not just the ones decided today.

**2026-07-25 addendum — a second review pass, prompted by live pilot testing:**
- **PAHC:** two Category A terms confirmed — baptisma → "baptism (the water)" (the entry's own tester example, alias "the water" used in the bracket rather than the Greek); Two Ways → "the teaching that lays the two paths of life and death before you (Two Ways)" (wording edited live from the original candidate).

**Still open, not decided in either pass:** Syriac's remaining terms beyond raza/Iḥidaya (including the Tishrin Category B item), Hieronymian's remaining terms beyond Vulgata, Imperial Juridical's remaining terms beyond homoios, PAHC's remaining 11 Category A terms beyond baptisma/Two Ways, and Alexandria's other 26+ lower-priority terms plus its Category A entries beyond the ten listed above. These remain recommendations awaiting review, exactly as before.
