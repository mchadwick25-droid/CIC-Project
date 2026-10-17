# Round 2 targeted recheck: Gallic Atlas story pass

Reviewer: Opus 5.5, independent, read-only.
Scope: worktree `agent-a792408e07913bea8`, branch `site/atlas-story-gallic-fixes`, commits c1d79d3c2 and 4a890e172, diffed against `origin/site/atlas-story-gallic`.
Checked against: the ten story records (`text`, `tellable_as`, `absent_detail`, `use_note`, `divergence_note`, `claim_guards`), `gallic.core.gallic` (horizon, cautions), figures for Martin, Cassian, Honoratus and Sulpitius, the cited quote, term and force records, `gallic.limit.only-on-paper`, `gallic.dw.one-person-two-substances`, the vendored `npnf211` file (Vita II-III, VI-VII; Dial. III.11-13; Inst. Pref., IV.2; Conf. XIII.13, XIII.18, XV.3-4) and `npnf203` (Gennadius LXX), and Pleiades JSON for Condate, Lerina and Andethanna (fetched 2026-10-17).

---

## 1. Round 1 findings: status

| Finding | Status |
|---|---|
| B1 Faustus/Riez | Fixed. The sentence and the highlight are gone. `legacy` now names Faustus as bishop only in the post-450 field, which is acceptable there. |
| B2 "went alone" | Fixed in the story, the voice and the telling. |
| B3 Honoratus's offices / Arles | Fixed. The story, teaser, telling and voice now all name the priesthood on the island. "In time he became a bishop" rests on Conf. Pref. III. |
| B4 Tier 3 wonders flat | Fixed ("Sulpitius tells how..."). |
| B5 Nesteros misattributed | Fixed. But the new opening sentence of the unit adds a new error (R3). |
| B6 Egypt's teaching as Gaul's | Fixed. |
| B7 "only the colder climate" | Fixed in the story, tile and `read_first`. |
| B8 grace origin / Rome | Fixed. |
| B9 unit 7 not_for breaches | Fixed. |
| B10 pronoun | Fixed. |
| B11 Sulpitius portrait | Fixed. |
| B12, B13 dates | Fixed. |
| B14, B15 teasers | Fixed. |
| B16, B17 angel coda | Fixed by the cut. |
| B18 Honoratus source limit | **Not fixed. It regressed.** "Rough copy" is gone, but every trace of the wording limit is gone with it (R1). The voice hedge and `sourcing` now turn the build's unread portion into a claim that the source says nothing (R2). |
| B19 Germanus | Fixed. "Elsewhere" now separates XIII.13 from XIII.18, and the quote records still carry the not-joined guard. |
| S1-S3, S5, S8-S11 | Fixed. |
| S4 "Tricked Into the Bishop's Chair" | Fixed in the title, but the same overstatement came back in the Martin voice (S-3 below). |
| S6 Trier teaser | Reworded, but the new wording is factually wrong (S-1 below). |
| S7 Honoratus teaser hedge | **Not fixed.** The teaser still drops "as far as his sermon can be read" (part of R1). |
| C1-C8 | Fixed. No meta "record" or "this world" remains in the page fields, and the template is broken up. C8 brought in one new ambiguity (S-4 below). |
| N1-N9 | Fixed, except N8, which is correctly deferred to the log. |

**Deleted bodies.** None of the eleven deleted bodies held a fact that is now missing. The guard keeping XIII.13 and XIII.18 apart survives in `gallic.quote.chaeremon-grace-requires-our-effort` and `-three-stages-of-grace`. The Germanus of Auxerre guard survives in `gallic.figure.cassian` and `gallic.story.bishop-archebius`. The rule that the two households never mention each other is the core caution. The Brictio succession guard is in `claim_guards`. The front body was stale process commentary, and deleting it was correct.

**Mark's ruling on tails.** Every telling now ends on its last real event: the two years in uniform, no battle, the reputation, "our bishop", sixteen years, the Judas saying, the funeral, the two readings, Chaeremon's paradox, and the humility in the priesthood. No main-story unit ends on an empty summary. One hedge that rigor needed was removed with the tails: the Honoratus wording limit (R1).

---

## 2. New findings

### R1. The Honoratus wording hedge is gone from every field
- **Severity:** BLOCKING
- **Where:**
  - `honoratus-and-the-island` telling, paragraphs 2-3
  - teaser
  - `orientation.story` unit 3
  - `voices` (Honoratus)
  - `who_speaks`
- **Quote:**
  - Telling: "And there the priesthood caught up with the man who had run from it. He was made a presbyter, a priest..."
  - Unit 3: "Honoratus had run from church office, but on the island the priesthood caught up with him."
  - Teaser: "Then, his disciple says, the priesthood he had run from catches up with him there."
- **Evidence:**
  - This is the only story in the repository whose wording itself is Inferential-Thin. Its divergence_note says: "the English rests on the Doc_09 builder's own rendering of rough OCR of the Latin ... its sense not verified". It adds: "The Representative must not quote the English here as Hilary's words - only as a rendering."
  - `use_note.means` hedges this exact claim: "and that, **as far as the sermon can be read**, he was made a presbyter there".
  - `tellable_as` keeps "as far as his sermon can be read".
  - The not_for bars "an exact reading of Hilary's Latin".
  - The round 1 fix for B18 kept a wording hedge. The fixer cut it as a "tail", but it qualifies one specific claim, the presbyterate, so Mark's ruling keeps it.
  - In unit 3, the priesthood sentence also sits outside the "Hilary preached that" clause, so the narrator states an unverified rendering as fact.
- **Fix:**
  - Telling, paragraph 3: "There Honoratus set up a camp of God. And there, as far as Hilary's Latin can be read, the priesthood caught up with the man who had run from it."
  - Teaser: "Then, as far as his disciple's sermon can be read, the priesthood he had run from catches up with him there."
  - Unit 3: "Honoratus had run from church office. As far as Hilary's sermon can be read, the priesthood caught up with him on the island."
  - Voice text: "...but on the island, as far as the sermon can be read, the priesthood caught up with him."

### R2. Unread text is presented as silence in the source (the B18 error, reintroduced)
- **Severity:** BLOCKING
- **Where:** `voices` Honoratus `hedge`; `orientation.sourcing`
- **Quote:**
  - Hedge: "All we can tell of our founder comes from the funeral sermon his disciple Hilary preached. It tells how he came to the island and was made a priest there. Of our days on the island in between, it says nothing."
  - Sourcing: "Nothing survives of the island's daily life"
- **Evidence:**
  - The story's absent_detail says: "Hilary's sermon **exists in full, unread here beyond these lines**; Eucherius's In Praise of the Desert is in the same condition". It adds: "we can tell how the founder came to Lerins ... and not what he or anyone did there in between."
  - The gap is in what this build has read. It is not a silence in the sermon, and it is not a loss of sources. "It says nothing" and "Nothing survives" both turn it into a claim about the source.
  - "All we can tell ... comes from the funeral sermon" also contradicts the voice's own text two lines up: "In time he became a bishop" rests on Cassian, Conf. Pref. III (`gallic.figure.honoratus`).
- **Fix:**
  - Hedge: "Almost all we can tell of our founder comes from the part of Hilary's funeral sermon we can read, and its Latin is hard to read. It tells how he came to the island and was made a priest there. What he or anyone did on the island in between, we cannot tell you."
  - Sourcing: "No one among us has told the island's daily life, and the books from Tours do not say what the brothers sang or when."

### R3. "Cassian refused to tell stories of wonders" is contradicted by the source and by the angel card on this page
- **Severity:** BLOCKING
- **Where:**
  - `orientation.story` unit 6, sentence 1
  - `voices` Cassian
  - `who_speaks`
- **Quote:**
  - Unit 6: "Cassian refused to tell stories of wonders."
  - Voice: "on principle he told no stories of wonders"
  - who_speaks: "though he refused to write of wonders"
- **Evidence:**
  - The refusal is a statement about one book. `gallic.quote.cassian-refuses-to-weave-a-tale-of-miracles` sits at the Institutes Preface. Its own retrieve_when says "why Cassian's own writing has **so few** miracle stories".
  - The vendored Conferences narrate wonders. In Conf. XV.3 (npnf211 c. l. 39740-39780), Macarius raises "a most ancient corpse" before the people. In XV.4, Abbot Abraham works a miracle.
  - On this same page, the angel card has Cassian bringing "us" a story in which a singer vanishes and is taken for an angel.
  - The round 1 version did not make this claim. It was introduced with the B5 fix.
  - Root note, outside this pass: `gallic.gravity.virtus` means and `gallic.force.power-displayed-disowned` make the same overgeneralization. Log it.
- **Fix:**
  - Unit 6: "In the preface to his Institutes, Cassian said he would not write up the wonders he had seen, because they teach nothing about how to live."
  - Voice: "...and in his Institutes he chose not to write up the wonders he had seen."
  - who_speaks: "...carried their teaching to Marseilles, and wrote about how to live, not about wonders."

### R4. `sourcing` credits both households with writing on "the saint's power"
- **Severity:** BLOCKING
- **Where:** `orientation.sourcing`, sentence 3
- **Quote:** "Both households left much writing on virtue and on the saint's power, and little on daily life."
- **Evidence:**
  - The south left no writing on Martin's power. Its one wonder is Honoratus's snakes, a single episode. Unit 6 on the same page says the opposite of this sentence.
  - `gallic.gravity.virtus` describes the north's miracle literature against "Cassian refuses wonder-tales".
  - "Little on daily life" also contradicts `gallic.limit.only-on-paper`, where Cassian's Institutes I-IV (dress, hours, entrance) are the main daily-life source, as Egypt's customs.
  - Both claims are new in 4a890e172. The base text said "rich writing about ideas and virtues".
- **Fix:** "Both households wrote much about virtue. Tours also wrote of Martin's power, while Cassian set down Egypt's customs, not Gaul's own days."

### S-1. The Trier teaser says the tribunes were never sent
- **Severity:** SHOULD-FIX
- **Where:** `documented_stories` trier, `teaser`
- **Quote:** "He also stops officers from being sent to hunt heretics in Spain."
- **Evidence:**
  - Dial. III.13 (npnf211 l. 5186-5188): "only let the tribunes, **who had already been sent** to the Spains ... be recalled".
  - The telling says "the tribunes called back". The teaser contradicts it.
  - "He also" makes the recall sound like a second act. It was part of the same bargain.
- **Fix:** "To save lives, a bishop takes communion with men he had refused. In return, officers sent to hunt heretics in Spain are called back. He never fully forgives himself."

### S-2. The tile puts Martin's discharge in the Loire valley
- **Severity:** SHOULD-FIX
- **Where:** `skim.tile`, sentence 3
- **Quote:** "In the Loire valley, a soldier named Martin left the army to serve Christ."
- **Evidence:** The discharge took place before a battle, at "the city of the Vaugiones" on the frontier (`discharge-before-caesar` text). The Loire is where the household grew later.
- **Fix:** "In the Loire valley, the first household grew around Martin, a soldier who had left the army to serve Christ."

### S-3. The Martin voice brings back the S4 overstatement
- **Severity:** SHOULD-FIX
- **Where:** `voices` Martin, sentence 2
- **Quote:** "so the people of Tours made him their bishop by a trick."
- **Evidence:**
  - The trick only drew him out. The vote and the consecration made him bishop (`election-at-tours` text).
  - This is the reason the title was changed in round 1 (S4).
  - The tile and unit 2 already have the correct wording.
- **Fix:** "so the people of Tours drew him out by a trick and made him their bishop."

### S-4. In the cloak telling, "His tribune" now reads as Martin's father
- **Severity:** SHOULD-FIX
- **Where:** `the-cloak-at-amiens` telling, last sentence
- **Quote:** "His tribune promised to leave the world with him when his service ended"
- **Evidence:**
  - The new opening (C8 fix) is "Martin's father was a tribune", so "His tribune" now points back to the father.
  - Vita III (l. 809-813): "his tribune, whom he admitted to be his familiar tent-companion ... promised that, after the period of **his office** had expired, he too would retire". The term that was ending is the tribune's, but "his service" reads as Martin's.
- **Fix:** "His commander, a tribune who shared his tent, promised to leave the world with him when his own term of office ended, so Martin stayed nearly two more years, a soldier in name only."

### S-5. The Postumianus highlight has an unclear "his"
- **Severity:** SHOULD-FIX
- **Where:** `highlights` "a traveler just back from Egypt"
- **Quote:** "Sulpitius wrote his praise of Martin."
- **Evidence:**
  - "His" can be read as Sulpitius's own praise. The base text was clear: "His praise of Martin was written by Sulpitius."
  - The quote's not_for bars "an independent traveller's judgment, when the speech belongs to Sulpitius's literary dialogue". The highlight is the only place on the page that carries that guard.
- **Fix:** "This is Postumianus, a speaker in Sulpitius's Dialogues. The praise of Martin given to him is Sulpitius's own writing."

### S-6. The Chaeremon highlight computes an interval the record says is not stated
- **Severity:** SHOULD-FIX
- **Where:** `highlights` "Chaeremon"
- **Quote:** "Cassian wrote down his words decades later in Gaul"
- **Evidence:**
  - `gallic.figure.cassian`: "The interval between his Egyptian journey and his writing in Gaul is not stated in this world's own documents and is not computed."
  - The Germanus telling on the same page says "years later".
- **Fix:** "Cassian wrote down his words years later in Gaul, setting out in his own composition what he had heard."

### S-7. Discretion is narrowed to excess only
- **Severity:** SHOULD-FIX
- **Where:** `orientation.story` unit 5
- **Quote:** "discretion, the judgment that tells when a practice goes too far."
- **Evidence:** `gallic.term.discretion` means: "the royal road between excess and slackness". The unit keeps only one of the two sides.
- **Fix:** "discretion, the judgment that keeps a monk between too much and too little."

### NITs
- **N-1.** Death telling: "The whole city poured out to meet his body". The city is never named, and the sentence follows directly on Condate, so a reader will take it as Condate. Fix: "The whole city his body was brought to poured out to meet it, with people from the villages and towns around."
- **N-2.** `read_first` Institutes: "changed only where its climate or habits made them too hard". "Its" points back to "a new house". Fix: "where Gaul's climate or habits".
- **N-3.** Unit 6: "Tours told its story through power instead." Tours (397-406) wrote before Cassian (420s), so "instead" makes Tours sound like it was answering him. Fix: "Tours told its story through power."

### Record-level, for the log only (no page defect)
- `gallic.figure.honoratus` says Honoratus's see at Arles is "the editorial apparatus's identification". But Gennadius ch. LXX, which is ancient text (npnf203 l. 43389-43401), reads "Hilary, bishop of the church at Arles ... his Life of Saint Honoratus, his predecessor". The card's `when`, "his successor at Arles", is therefore supported. The figure's divergence_note understates the evidence.
- `gallic.gravity.virtus` and `gallic.force.power-displayed-disowned` overgeneralize Cassian's refusal of wonders. This is the root of R3.

---

## Verdict

**NOT APPROVED.** Most of the round 1 work holds. 18 of 19 BLOCKING findings are closed, the tails are gone, the meta-language is gone, and the template is broken up. But B18 has regressed. The Honoratus material has lost the hedge on the one story whose very wording is unverified. And unread text is stated twice as the source's own silence. Two new claims also contradict the page and the vendored source: the blanket statement that Cassian told no wonder stories (while the angel card sits on the same page), and `sourcing`'s claim that both houses wrote on "the saint's power".

**Counts:** BLOCKING 4 · SHOULD-FIX 7 · NIT 3
