# Atlas final check: targeted recheck of the fixes (2026-10-17)

Reviewer: Opus 5.5, independent and read-only. Branch `audits/atlas-final-check`, fixes in the commits after 572ffc39.

**Scope.** A targeted recheck, not a fresh review. I checked only these four things:
- every BLOCKING and SHOULD-FIX finding in the three reviews (`fleet_atlas_final_check_{alx-cappadocian-hal-syr,don-gallic-pahc,ijc-witt-rzg}_2026-10-17.md`);
- whether the fix reached the live text and, where the review asked, the source record;
- whether any changed wording brought in a new fact or error, checked against the record and `cic/texts/`;
- the length limits and the "scholars" and jargon rules on the text that changed.

I applied Mark's three rulings: emic hedges in card voice; reported speech for the old-translation Wittenberg quotes; and the "we" voice throughout pahc. rzg's short card list is out of scope.

**Method.**
- Word diff of `Build/worlds/*/surface/world_front` and `records/` from 572ffc39 to HEAD.
- A script measured story, telling, teaser and note lengths, and sentences over 25 words, on the current files.
- I grepped `cic-website/` and `packages/` to confirm that the new wording is live and the old wording is gone.

---

## BLOCKING

### R-B1. syr `basil-legend` telling: the rewrite removed the doubt and settled a disputed identification
- **File:** `records/syr/story/syr.story.basil-legend.md` `telling` (live in `cic-website/data/worlds/syriac-edessa-nisibis.json`).
- **Now:** "Later tradition took that Syrian to be Ephrem. But the Syrian Basil praises was another man, Eusebius of Emesa, so the meeting is a later legend."
- **Was:** "Modern scholars judge the Syrian to be another man, Eusebius of Emesa, and so judge the meeting a legend."
- **Evidence:**
  - Ruling 1 says to rewrite the hedge emically and keep the doubt. The rewrite dropped the doubt and now states the identification as fact.
  - `syr.source.basil-hexaemeron` divergence_note: "Three candidates, no evidence in the text. This world … may not use it to identify him."
  - `syr.quote.basil-credits-a-syrian`: "The Syrian is unnamed and stays unnamed … No record may resolve this from the passage."
  - The vendored endnote shows the editors disagree. It reads: "Tillemont understands Eusebius of Samosata. The Ben. note prefers Ephrem Syrus" (`npnf208` l.16729-16731).
- **Proposed:** "Later tradition took that Syrian to be Ephrem. Basil never names him, and he may well be another man, Eusebius of Emesa. The meeting itself is a later legend."
- **Related (pre-existing, flagged for the same fix):**
  - The teaser says "The praise of a Syrian in Basil's writings is about another man." That is just as flat.
  - The record's own `text` says "is now known to be about another man entirely", which contradicts its two sibling records.

### R-B2. rzg main story [7]: a new pronoun now credits Zurich's council with the Consistory's fight
- **File:** `Build/worlds/rzg/surface/world_front/rzg.front.the-reformed-cities-zurich-and-geneva.md`, story unit beginning "In 1541 Geneva's church ordinances".
- **Now:** "Zurich's council ruled church and city as one. It fought to stay free of that control."
- **Was:** "Geneva's Consistory fought to stay free of that kind of control."
- **Evidence:**
  - The nearest subject for "It" is "Zurich's council", so the sentence now says Zurich's council fought to stay free of its own control.
  - This is the same kind of fault as rzg-B1, which the same edit fixed one sentence later.
  - `rzg.gravity.council-led-authority-vs-consistorial-independence` makes the Consistory the subject.
- **Proposed:** "Geneva's Consistory fought to stay free of that control."

### R-B3. syr `ephrem-famine-death` teaser: the trim makes Ephrem die within a month of starting the relief
- **File:** syr world_front, `syr.story.ephrem-famine-death` teaser.
- **Now:** "Palladius and Sozomen tell that in Edessa's famine, Ephrem takes money from the rich and sets up some three hundred beds. He nurses the starving, and he dies within a month."
- **Evidence:**
  - Palladius XL.4 (`palladius_lausiac-history_clarke1918.txt` l.471): "So when the year was completed and prosperity returned … he entered his own cell and died after a month."
  - The old teaser had "until the famine ends". Cutting it moved the month so that it now runs from the nursing, not from the end of the relief year.
- **Proposed:** "He nurses the starving until the famine ends, and he dies within a month." (14 words)

### R-B4. cappadocian C1/C2: the same errors remain in sibling record fields, and from there in the compiled package
The review said "Those records need the same correction". The named fields were fixed, but the same error is still in other fields that go into `packages/cappadocian/2026-10-17T20-13-24Z/compiled/repository.json`:
- `records/cappadocian/story/cappadocian.story.valens-caesarea.md` `narrative_tier_justification`: "delivered within living memory of eyewitnesses at Basil's funeral". This is in the same record the review named.
- `records/cappadocian/figure/cappadocian.figure.modestus.md` divergence_note: "Gregory's public telling at Basil's funeral".
- `records/cappadocian/figure/cappadocian.figure.forty-of-sebaste.md` `dates.display`: "c. 320, under one of the last empire-wide persecutions".
- **Proposed:**
  - "in his funeral speech for Basil, years later" (both funeral fields).
  - "c. 320, in one of the last persecutions" (forty-of-sebaste).
  - Then rebuild the package.

### R-B5. ijc-B2: the same "army saw it too" fault remains in the card telling and its record
- **File:** `records/ijc/story/ijc.story.vision-and-alliance.md`.
- **Now (`telling`):** "It carried the words "Conquer by this," and his whole army saw it too."
- **Now (`text`):** "His whole army saw it too."
- **Evidence:**
  - Story unit [2] was fixed ("His whole army, he said, saw it too"). The card on the same page still lets the narrator vouch for the army's sight.
  - `use_note.not_for` excludes "a straightforward eyewitness report". The review's own severity applies to identical text.
- **Proposed (telling):** "It carried the words "Conquer by this." His whole army, he said, saw it too."

### R-B6. The hal-H2 and witt-B4 claims are still on the public tradition pages, through the census copy
These two errors were fixed in the world_front tile. A second copy of each is live in `cic-website/data/world-census.json`. That file feeds `cic-website/traditions/*.html` and `atlas-v3.html`:
- **hal**, `cic-website/traditions/hieronymian-ascetic-literary.html` and the census `longDescription`: "Clergy still brought her their hardest scripture questions until her own death in 410." The flat, inflated claim from H2 is still there.
- **witt**, `cic-website/traditions/lutheran-wittenberg-and-its-congregations.html` (`<p class="tile">`) and the census `tile`: "He was an Augustinian friar and professor at the young university of Wittenberg." This is the B4 "young university" claim, which witt OG-73 already found unsupported.

The reviewers read the world_front tile, so these copies were outside the fix. They still put the same errors on the participant-facing page. Mark or the census owner needs to decide whether they are corrected in this pass.

---

## SHOULD-FIX

### Applied with new craft or accuracy problems
1. **gallic G-6, Julian note.**
   - **Now:** "Sulpitius calls him just Julian Caesar. That is all. A modern editor says he is Julian the Apostate. Sulpitius does not."
   - **Problems:**
     - "That is all." is a new tell.
     - It is also not true. Sulpitius calls him "Cæsar" and "the tyrant" in the same passage (`npnf211` l.829, l.841).
     - "Sulpitius does not." repeats the opening sentence, which is the tell the finding removed.
   - **Proposed:** "Sulpitius names him Julian Caesar. A modern editor identifies him as Julian the Apostate, a name Sulpitius never uses."
2. **gallic G-2, Trier telling is now 251 words**, one over the 250 ceiling.
   - **Now:** "Gallus says he lived sixteen more years and never went to a synod again."
   - **Proposed:** trim one word elsewhere, for example "Leaving the city, he sat alone in the woods near a village called Andethanna" → "…near the village of Andethanna".
3. **gallic G-7, Chaeremon note.**
   - **Now:** "Years later, in Gaul, Cassian set down his teaching in his own words."
   - **Problem:** "his own" can be read as Chaeremon's, which suggests a verbatim record. The record means Cassian's own composition.
   - **Proposed:** "…set down his teaching in Cassian's own words."
4. **syr S3, jacob-deliverance teaser.**
   - **Now:** "He says Jacob of Nisibis cursed the Persians, and only gnats and mosquitoes came. In his telling, they flee."
   - **Problems:**
     - "Only … came" reads as if the curse fell short of what he asked. Theodoret says the gnats were all he asked for: "he discharged no other curse than that mosquitoes and gnats might be sent" (`npnf203` l.11173-11175).
     - The tenses mix.
   - **Proposed:** "He says Jacob of Nisibis cursed the Persians with nothing worse than gnats and mosquitoes. In his telling, the Persians fled."
5. **syr F1/S1, abgar-addai teaser: the doubt is thinned.**
   - **Now:** "The church told it as the story of its own beginning, in a form written down later."
   - **Problem:** Ruling 1 keeps the doubt. The teaser no longer says the tale is legend, only that it was written down late. The record's `absent_detail` says "None of this is history", and its tellable_as says "never as history".
   - **Proposed (emic):** "We told it as the story of our own beginning. It was first written down centuries later, and nothing from Abgar's own day confirms it."
6. **alx A5, origen-demetrius addition.**
   - **Now:** "The letters and rulings from the break are lost."
   - **Problem:** The record's `absent_detail` says only "The synodal documents are lost." "Letters" goes beyond the record.
   - **Proposed:** "The synods' rulings from the break are lost."
7. **don D-6, the persecution-of-303 note.**
   - **Now:** "They ordered clergy to hand over the scriptures. Church vessels were to be destroyed."
   - **Problem:** The split changes the meaning. `don.force.diocletianic-persecution-traditio-demand` l.31-32 says clergy had to hand over scripture and sacred vessels, both to be destroyed.
   - **Proposed:** "They ordered clergy to hand over the scriptures and church vessels to be destroyed." (14 words)
8. **don D-6, Vandal note.**
   - **Now:** "…the Roman power that had judged the Donatists and forced them."
   - **Problem:** "forced them" is incomplete.
   - **Proposed:** "…and coerced them."
9. **ijc S8, Thessalonica note.**
   - **Now:** "A city in north Greece, now Thessaloniki. After a massacre here in 390, Ambrose told the emperor to repent."
   - **Problem:** "north Greece" is not idiomatic. "Told the emperor to repent" is supported: Ambrose's letter says "Sin is not done away but by tears and penitence … does not forgive any but those who repent" (`npnf210` around l.44163-44166), and the record says "demanding repentance".
   - **Proposed:** "A city in northern Greece, now Thessaloniki. …"
10. **ijc S9, Constantine note.**
    - **Now:** "He called the Nicaea council in 325."
    - **Proposed:** "He called the council at Nicaea in 325."
11. **ijc S9, Eusebius note.**
    - **Now:** "He wrote a life of Constantine after his death."
    - **Problem:** "his" can be read as Eusebius's own death.
    - **Proposed:** "He wrote a life of Constantine after the emperor died."
12. **ijc S11, basilica telling order.**
    - **Now:** "He wrote to the bishops of Numidia about it … He left the Donatists where they were. The Catholic bishops asked for another site instead, and he granted it."
    - **Problem:** The rescript answers a petition the bishops had already sent (`optatus_against-the-donatists.txt` l.7222: "ask instead for another site … This petition of yours I gladly welcomed"). "Asked … and he granted" reads as if they asked after his letter.
    - **Proposed:** "The Catholic bishops had asked for another site instead, and he granted it." The other new facts check out against the rescript: the Custom House site, the building "at the Imperial expense", and the freeing of the lower clergy.
13. **witt S1, Kate telling.**
    - **Now:** "She asked him why, under the Pope, people prayed so often and so hard, while they were cold and careless in prayer."
    - **Problem:** In reported speech "they" now points back to the people under the Pope, so the sentence contradicts itself. Bell l.3147-3151 has "but we are very cold".
    - **Proposed:** "…while their own household was cold and careless in prayer."
14. **witt S1, eight-sermons telling.**
    - **Now:** ""God does not want hearers and repeaters of words, but doers and followers," he said, who practice the faith that works by love."
    - **Problem:** The relative clause dangles across the speech tag.
    - **Proposed:** "…doers and followers," he said. They were to practice the faith that works by love."
15. **witt S4, Speratus telling.**
    - **Now:** "Bacon, a later editor of Luther's hymns, notes something about that same book, the 1524 "Eight Songs." Luther's three versions of Psalms are all set to this hymn's tune."
    - **Problem:** "Notes something about" is filler. The split also leaves the fact without its attribution.
    - **Proposed:** "Bacon, a later editor of Luther's hymns, notes that in the same book, the 1524 "Eight Songs," Luther's three versions of Psalms are all set to this hymn's tune." (27 words; split if needed: "…notes a detail of the same book, the 1524 "Eight Songs." There, he says, Luther's three…")

### Applied, but incompletely or with an unjustified deviation
16. **pahc P-6 and ruling 3: "scholars" is still on five card `when` lines.** These lines show on every card head (`pahc.front…` l.112, 117, 127, 132, 137). Examples:
    - "scholars dispute whether a separate persecution tied to the fire took place in 64"
    - "scholars have argued for anywhere from 50 to 150"
    - "some scholars read it as two letters joined"

    They are not telling or teaser text, but ruling 3 says "throughout". **Proposed:** "we cannot be sure …" forms, matching the rewritten tellings.
17. **Highlight notes still over 25 words in total**, against the D-6, G-7, A9 and C9 targets. Every sentence is now 25 words or fewer, so the readability rule holds, but the per-note targets were not met. Nothing in the fix logs justifies the deviation.
    - alx Gregory: 26.
    - cappadocian Pontus: 29.
    - don Vandal, Petilian and Tyconius: 26 each. Optatus: 27.
    - gallic communion: 26.

---

## Checked OK

**alx**
- A1, tile: "Eusebius reports that a young Origen took a hard verse from Matthew literally and acted on it. His bishop first admired his daring, then later turned the act against him." The record backs "admired his daring".
- A2 and A3: tile wording fixed.
- A4: "Not yet seventeen" is now in both the telling and the record `text`, matching HE VI.2.12. The opening "His son Origen was sixteen" is now consistent with it.
- A5, didymus: "Jerome, who studied with him briefly, says, writing in 392 or 393, that he had already passed his eighty-third year." Each part checks:
  - `alx.figure.didymus` gives "studied under him briefly" (l.40-41) and "written in 392/3" (l.32).
  - `npnf203` l.41465 reads "has already passed his eighty-third year".
  - The telling is 122 words.
- A5, origen-demetrius: now 135 words. "The church kept both memories…" and "we cannot hear" come from the record's `text`. The one exception is item 6 above.
- A6: "faith was formed".
- A7: "Some have doubted that it happened at all … Others see no reason to doubt it."
- gregory-formation: "though who gave it, and when, is not settled".
- A8: "The capital here was probably Arsinoe. It stood at Medinet el-Fayum, in Egypt today."
- A9: notes trimmed with no new facts.
- Logged open in the fix log: plague-nursing at 119 words, which the review did not flag. Also out of scope: the voices entry still says "acted on a hard verse from Matthew far too literally" (OG-30 tracks voices).

**cappadocian**
- C1, the funeral wording in the tellings: "When he rose to praise his dead friend" (athens) and "in his funeral speech for Basil" (valens).
- C1, the records: the valens `absent_detail` now reads "given in his funeral speech for Basil, years later". The divergence_note and the athens record `text` and `modern_contrast` are corrected. "Years later" fits Oration 43, given after Gregory returned to Nazianzus in 381.
- C2: telling, `when` and record `text` all read "in one of the last persecutions".
- C3, tile: "When famine came, Basil, then a priest, preached against landowners who hoarded grain."
- C4 to C8: all applied. Nyssa: "Hostile bishops of the court's party, who held the Son merely like the Father, had arranged them" (19 words).
- C9, Pontus: the note keeps "Basil's family had a home at Annisa, in Pontus." The renaming for Helena is unchanged in substance.
- C9, the other notes: Nicaea, Council of Constantinople ("kept the Nicene faith … led them"), Gregory, Modestus and Hypostasis were trimmed only.

**hal**
- H1: "No one here held a bishop's office."
- H2: "Jerome says priests were sometimes among those who brought her hard questions about scripture."
- H3: "Nearly everything we know of them comes through Jerome's pen."
- H4 and H5: applied. "In 416, armed men burned the Bethlehem monasteries" matches `hal.story.attack-416`.
- H6: applied.

**syr**
- S1: teasers are 25 to 40 words.
- S2: "The Paradise says one of the holy fathers…", "Then, it says, …" and "The story says he healed the king…".
- S4, flood: "Whether the line is original, or was added later by another hand, is not settled." The teaser's "Where that line came from is not settled" is looser but carries the doubt.
- S5: the acrostic note.
- S6: notes trimmed.
- Simeon's "in chains" and the choirs' "founded" both match their tellings.

**don**
- D-1: the story is 696 words, and the edict sentence is kept.
- D-2: "They split over whether a bishop's conduct … could void what his hand later gave. One side said it could."
- D-3: the Passio teaser is 22 words.
- D-4: "rival primate at Cebarsussi in 393 … In 394, 310 bishops met at Bagai. They condemned him."
- D-5: "The town where Maximian was made rival primate in 393. Its site is unknown." Byzacena is removed.
- D-7: "Constantina, which was the new name for Cirta".
- Cirta and Novapetra: "probably" is kept, per Pleiades.

**gallic**
- G-1: all four teasers now attribute the event ("Sulpitius says", "Cassian reports", "His disciple Hilary says").
- G-3: "He never goes to a synod again."
- G-4: "by all" in story unit [5], matching `gallic.quote.believed-everywhere-always-by-all`.
- G-5: Honoratus teaser is 26 words.
- G-7: the other notes were trimmed only. The grace note's "Scholars still disagree" is in a highlight note, not in card voice.

**pahc**
- P-1, the Quintus teaser: "The letter from Smyrna that honors Polycarp also names Quintus." The record's `tellable_as` still has the old order, which is tracked as OG-33.
- P-11: the cards are swapped.
- P-2 to P-5 and P-9: applied. The story is 631 words.
- P-6: Nero and Pliny now hedge with "We cannot be sure…" and "What that meal was, we cannot say for certain."
- Ruling 3: Ignatius, Polycarp and 1 Clement are in the "we" voice.
- P-7: "Ignatius writes to him as one, and Smyrna's letter on his death calls him its bishop." This matches the Ignatius salutation and Mart. Pol. XVI.
- P-8: "denarii … acres", matching `npnf201` l.16899-16906.
- P-10 and P-12: applied.

**ijc**
- B1, telling: "Not every bishop was satisfied. The Tome was questioned in session…".
- B1, record: `absent_detail` now reads "with explanations asked by the Illyrian bishops after the acclamation", which matches `npnf214` l.19996-20012.
- B2: story unit [2] reads "His whole army, he said, saw it too." The card is still open (R-B5).
- B3: "Bishops now gathered in councils an emperor summoned and paid for."
- S1: the "John" phrase first occurs only in the Eutropius telling. The renderer is case-sensitive, so "altar of Victory" now matches the telling. The altar note's "In 384 Symmachus asked the emperor to bring it back" matches the record.
- S2: "Theodoret writes that in his rage…" and "It is said, Theodoret adds…".
- S3: matches the quote's `modern_rendering`.
- S4: the telling and story [5] both read "The printed edition of Ambrose's letters dates the law a year earlier."
- S5: the letter telling is 93 words, under the ruling. The hedge "Those he wrote to disputed how old and settled that custom was" matches `absent_detail`.
- S6, S7 and S10: applied.
- S11: the facts match the rescript (see item 12 for word order only).

**witt**
- B1: story [9], the teaser and the voice now make it Luther's own report, matching Bell l.3141-3151.
- B2: "Elector was the title of Saxony's ruling prince… Frederick held it in 1518. By 1530 John held it."
- B3: "Baptism means the old self is drowned by daily sorrow and repentance".
- B4, world_front tile: "who taught theology at the university of Wittenberg". The census copy is still open (R-B6).
- S1: Cajetan ("Where, Cajetan asked, would he be safe then?") and Worms ("He said they were his"; "God's Word, he told them, was not his word, so he did not know how to give it away") are both reported speech now. No new `modern_rendering`s were added, per ruling 2.
- S2: Walter's story and telling are split, and "wrote out the notes for some of the Gospels and Epistles" matches Bacon l.766-768.
- S3: "or your own thoughts", matching `luther_small-catechism_smith1994.txt` l.557-558.
- S5 and S6: applied.
- S7: logged open with its reason (no witt record gives a modern location).

**rzg**
- B1: "By 1555 the fight was mostly settled in Calvin's favor." The sentence just before it now has the new fault described in R-B2.
- S1: "Zwingli's case", "ruled for the reform" and "both churches, Zurich's and Geneva's".
- S2: Strasbourg note.
- S3: Savoy is now a term.
- S4: the Myconius telling is joined.
- S5: "On his knees, he was reported to have said" and "after he fell", matching the Myconius source as the review cites it.
- S6: the Disputation teaser is 29 words.

**Fleet measurements on the current files**
- Main stories:

  | World | Words |
  |---|---|
  | alx | 623 |
  | cappadocian | 695 |
  | hal | 690 |
  | syr | 640 |
  | don | 696 |
  | gallic | 699 |
  | pahc | 631 |
  | ijc | 642 |
  | witt | 640 |
  | rzg | 637 |

  All are inside 600-700.
- Tellings outside 120-250:
  - gallic Trier at 251 (item 2);
  - alx plague at 119 (logged open, not touched);
  - ijc letter at 93 (ruled OK);
  - ijc dream at 99 and altar at 116 (not touched; the review said not to pad them);
  - witt Speratus at 98 (ruled not padded).
- Sentences over 25 words: none in touched story, telling, teaser, tile or note text.
- "Scholars" in card tellings or teasers: none left. The pahc `when` lines are item 16.
- "This world"-style jargon: none in any added participant text. It remains only in record fields that are not displayed (for example the valens divergence_note's "this world's independently documented policy arc"). Those fields were already tracked as open.
- Propagation: every fixed string checked is present in `cic-website/data/worlds/*.json` and the new packages, and the old wording is gone from both. The exceptions are R-B4, R-B5 and R-B6.
