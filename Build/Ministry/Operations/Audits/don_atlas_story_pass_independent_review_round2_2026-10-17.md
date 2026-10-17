# Round 2 recheck: Donatist Atlas story pass

Scope: worktree `agent-a7199f86b9cdac231`, branch `site/atlas-story-don-fixes`, commits 8afababd9 and bcdd55fbb against `origin/main`. I read every changed field in `Build/worlds/don/surface/world_front/don.front.donatism.md` and the nine `telling:` lines. I checked them against the cited records (`text`, `absent_detail`, `not_for`, `divergence_note`, bridge lines, term senses) and the old text. I re-fetched Pleiades for Novapetra (334604) and Vegesela (334661). Both match the notes.

## 1. Round 1 BLOCKING findings

| # | Status | Note |
|---|---|---|
| B1 Nicene | Fixed | "same Latin words" is in `don.dw.the-creed-we-shared`. |
| B2 until 439 | Fixed | |
| B3 name | Partly fixed | The contradiction is gone. The Optatus attribution is lost. See SF-1. |
| B4 or die | Fixed | The tile's "to be burned" is supported by `don.term.traditor-traditio`. |
| B5 Marculus | Fixed in the story | Fixed in the voice and teaser too. |
| B6 second time | Fixed | The partial rejection is right. No record states "worst" or "most of the martyrs". |
| B7 own texts | Fixed | |
| B8 411 verdict | Fixed | Leaving out 412 is right. |
| B9 Marcellinus | Fixed | Redundant wording is noted in N5. |
| B10 Donatus | Fixed | |
| B11 Vandal | Fixed | |
| B12 voice inventory | **Not fixed** | See BL-1. |
| B13 traitors | Fixed | |
| B14 Bagai title | Fixed | |

**Rejected or partly accepted SHOULD-FIX items**
- **S26.** The fixer is right. `don.dw.two-churches-in-one-town` says "we were simply the church of the village".
- **S27.** The fixer is right. The Gesta record says Augustine "was drawing on the Acts of this same inquiry ... It is not a second, independent source."
- **S28.** The fixer's rejection holds. No `don` record defines a proconsul, so neither gloss comes from the records. The current note is narrow, but it is not false.

**Deleted commentary: FINDING 3 is moot.** `cic-website/atlas-v3.html` now gives `donatism` as `"status": "Built & Live"`, the same as `world-census.json`. It needs no gaps entry.

---

## BLOCKING

### BL-1. The voice inventory still leaves out the largest body of Donatist words (B12 only half fixed)
- **Where:** `orientation.story` unit 9; `skim.tile`, last sentence
- **Quote:**
  - Unit 9: "Their own voice survives in four short texts and in their bishops' words at the hearing of 411. It survives too in two words cut into pillars near Bagai, Deo laudes, praise to God."
  - Tile: "Its own voice survives in four short texts, in its bishops' words at the hearing of 411, and in two words cut into stone."
- **Evidence:**
  - Round 1 B12 named Petilian's quoted letters explicitly. The fixer's report does not mention that part or reject it.
  - `don.core.donatism` `thinness`: "Donatist literature survives almost entirely as quotation embedded inside its own refutations."
  - `don.figure.augustine`: "He preserves more of our own words than anyone else."
  - The same file contradicts the inventory. `read_first[1]` says the *Answer to Petilian* holds "the fullest Donatist voice that survives". `who_speaks` calls Petilian "its fullest surviving voice". The Petilian voice entry says "More of his words survive than of any other Donatist".
  - So the inventory reads as complete, but it leaves out the largest category the file names elsewhere.
- **Fix:**
  - Unit 9: "Almost everything known about the Donatists was written by two men arguing against them. Most of their own words survive only as quotations in those men's books. Four short texts speak for them directly, and so do their bishops at the hearing of 411. So do two words cut into pillars near Bagai, Deo laudes, praise to God."
  - Tile: "Nearly everything known of it comes from two bishops who wrote against it, and most of its own words survive as quotations in their books. Beyond those, it speaks in four short texts, in its bishops' words at the hearing of 411, and in two words cut into stone."

---

## SHOULD-FIX

### SF-1. "Party of Donatus" loses its attribution (B3 residue)
- **Where:** story unit 1
- **Quote:** "In court, its bishops called themselves 'the party of Donatus'."
- **Evidence:**
  - `don.term.pars-donati`: "Optatus says they used the phrase whenever they were questioned in court ... The only voice that kept the phrase kept it as an accusation."
  - The documented act is one signed petition to Constantine.
  - `not_for`: "a claim that it was the settled self-description".
  - The etic narrator now states Optatus's report as plain fact. The qualifier "cannot say among themselves" is cut, and that qualifier applied to this specific claim, so the ruling did not cover it.
- **Fix:** "History calls its members Donatists, after an early bishop. Optatus says its bishops used 'the party of Donatus' when questioned in court. What they called themselves among themselves is not known."

### SF-2. The tile makes rebaptism the root of the rival church
- **Where:** `skim.tile`
- **Quote:** "So a whole rival church grew up around one demand, to be washed again by a hand that had never failed."
- **Evidence:** `don.gravity.rebaptism-boundary-marking` is cited in the tile's own `grounded_in`. It says: "The accusation against Felix of Aptungi is not its root. That accusation grounds the rival church's institutional form, not the rite itself."
- **Fix:** "So a rival church grew up with its own bishops, and anyone who came over to it was washed again by a hand that had never failed."

### SF-3. Unclear referents: "the church" and "their"
- **Where and quote:**
  - Tile: "Persecution came again, at the rival church's urging. The church kept the names of its dead"
  - Unit 4: "...at the rival church's urging, through the emperor's commissioners. The church's own account says ..." and "Every year, at the grave, the church read such accounts aloud again."
  - Unit 3: "So their font gave a convert the first real baptism of their life."
- **Evidence:**
  - In the tile and unit 4, the nearest antecedent of "the church" is the rival church. That reverses the meaning.
  - In unit 3, the first "their" means the Donatists and the second means the convert.
- **Fix:**
  - Tile: "The Donatists kept the names of their dead..."
  - Unit 4: "The Donatists' own account says..." and "Every year, at the grave, they read such accounts aloud again."
  - Unit 3: "So the Donatist font gave a convert his first real baptism."

### SF-4. Emeritus "each time" overstates the record
- **Where:** `voices` Emeritus; `conference-of-carthage-411` telling, paragraph 4
- **Quote:** "Each time, he signed the notary's record of his words and added that he kept his right to appeal."
- **Evidence:**
  - Story `text`: "as he signed most of what he said there".
  - `don.figure.emeritus` bridge: "at times with his appeal reserved".
  - In the telling, "each time" also follows "verse for verse", so it reads as "after each verse".
- **Fix:** "He signed the notary's record of most of what he said, and added that he kept his right to appeal." (in both places)

### SF-5. Macrobius telling: the sea's return lost its attribution
- **Where:** `macrobius-letter` telling, paragraph 4
- **Quote:** "The sea would not keep them. For six days the bodies were driven back toward the shore, until they came up whole to the people waiting."
- **Evidence:**
  - Story `text`: "Macrobius's letter says the bodies rose and were driven back".
  - `absent_detail`: "no independent notice of the deaths".
  - The old telling had "Macrobius says". The tail cut also removed this attribution, which qualified a specific miraculous claim.
  - The Passio telling keeps "we hold" and "we say" for its miracles, so the two tellings are now inconsistent.
- **Fix:** "The sea would not keep them. For six days, Macrobius says, the bodies were driven back toward the shore, until they came up whole to the people waiting."

### SF-6. Marculus hedge: the dangling clause misleads
- **Where:** `voices` Marculus `hedge`
- **Quote:** "Even hostile writers confirm that he was killed, though for two different reasons."
- **Evidence:**
  - Read aloud, it says he was killed for two reasons.
  - The record says two writers confirm the killing and each disputes a different thing (`don.story.passio-marculi` `divergence_note`).
- **Fix:** "Two hostile writers confirm his death, and each disputes its meaning in a different way."

### SF-7. Legacy: "the side that had beaten the Donatists"
- **Where:** `legacy[0]`
- **Quote:** "It passed to the side that had beaten the Donatists, and it shaped how Augustine read Scripture."
- **Evidence:**
  - `don.term.liber-regularum`: "His book went on to shape the rival church's own way of reading."
  - No record dates the transmission after a defeat.
  - "Had beaten" is an unsupported claim of victory.
- **Fix:** "It passed to the rival church, and it shaped how Augustine read Scripture."

### SF-8. A new template: Acta and Gesta share one provenance sentence
- **Where:** `acta-purgationis-felicis` paragraph 2; `gesta-apud-zenophilum` paragraph 1; `council-of-cirta` paragraph 1
- **Quote:**
  - Acta: "Optatus, our opponent, kept them among his documents."
  - Gesta: "Optatus, our opponent, kept the court record among his documents."
  - Cirta: "Optatus, our opponent, tells the story..."
- **Evidence:**
  - S24 asked for variation. "Who wrote against us" has been swapped for a new repeated appositive.
  - The Acta and Gesta sentences are near-identical, and the two cards are paired in retrieval.
- **Fix:**
  - Acta: "Their words survive in the dossier Optatus attached to his books against us."
  - Gesta: keep as is.
  - Cirta: "Optatus tells the story of that meeting, in his books against us."

### SF-9. Acta telling casts doubt on the whole letter
- **Where:** `acta-purgationis-felicis` telling, paragraph 2
- **Quote:** "The letter was said to come from a magistrate, Caecilianus. He told the court he had never dictated those lines."
- **Evidence:**
  - Story `text`: "a letter from the magistrate Caecilianus to Felix ... Caecilianus said he had never dictated them" (the closing lines only).
  - The gaps log has already corrected a similar drift ("supposedly written by Felix").
- **Fix:** "The letter came from a magistrate, Caecilianus. He told the court he had never dictated its closing lines."

### SF-10. Sourcing still has AI tells and one empty tail
- **Where:** `sourcing`
- **Quote:**
  - "That is the central problem with the sources, not a side note."
  - "The clearest exception was never a text at all. It is two words..."
  - "That question is left open."
- **Evidence:**
  - The first is a "not X" tag line, and the second is a set-up and reveal.
  - The question just before the third sentence already leaves the matter open, so the third adds nothing. The project lead's tail ruling covers it.
- **Fix:**
  - "That is the central problem with the sources."
  - "The clearest exception is two words, Deo laudes, cut into stone."
  - Delete "That question is left open."

### SF-11. The deleted 411 body held a quote-verification trail that the gaps log still points to
- **Where:** `don.story.conference-of-carthage-411` body (deleted); `Build/worlds/don/Open_Gaps_Tracking.md` near line 1530
- **Evidence:**
  - The gaps entry reads "The vendored Collatio scan is too damaged to string-search the Latin phrases listed in the body note". That body note no longer exists.
  - The deleted list was the Latin behind each English rendering ("salva appellatione recognovi", "A personis incipit omnis causa", "Mandavi et subscripsi", and others). CLAUDE.md requires verbatim re-checks of quotes, and this was the trail for them.
  - The commentary had to leave the canonical file. It should have been routed somewhere, not dropped.
- **Fix:** In the same PR, append a gaps entry (subject and date) that carries the nine Latin phrases and their line ranges from 8afababd9. Reword the stale pointer through a new entry, since entries are append-only.

---

## NIT

- **N1.** Tyconius telling, last sentence: "He was never received back..."
  - This is grounded in `text`. But it assumes a formal exclusion that the `divergence_note` leaves open.
  - Log it with the fixer's defect 2. Possible change: end on "...then condemned him. He never went over to the other side."
- **N2.** Novapetra highlight: "Where Marculus was held four days at a cliff and thrown from it."
  - These details come only from the Passio, and its portrait is rated Contested. Augustine disputes whether such men threw themselves down.
  - Possible change: "Where, by his church's account, Marculus was held four days at a cliff and thrown from it."
- **N3.** Lucilla telling:
  - "who wrote against us fifty years later". The record says "roughly". Use "about fifty years later".
  - "Then persecution broke over Carthage". The record says "Around the same time". Use "Around then, persecution broke over Carthage".
- **N4.** Acta telling: "denied that he had ever been to Numidia". The record says "denied that he had been to Numidia". Drop "ever".
- **N5.** Marcellinus highlight: "The imperial officer ... He was the emperor's officer, not a cleric of either church." The point is made twice. Use "He was not a cleric of either church."
- **N6.** Wording:
  - The 411 teaser repeats "a judge ... a judge". Use "...they argue before a court bound by an order...".
  - Bagai telling: "the harshest terms the council had". Use "in the harshest terms it had".
- **N7.** Aphoristic closers. Each line is accurate, but each is a stock summary line. Cut or plain them:
  - Gesta: "He kept it because it hurts us."
  - 411 telling: "So he put his name to his words while refusing the court that recorded them."
  - `who_speaks`: "its fullest surviving voice and its most filtered"
  - Emeritus hedge: "Even this voice has limits."
- **N8.** Two narrator statements about the window: unit 1 "This account follows them to 439" and unit 8 "This story ends in 439". Keep one.
- **N9.** `floor_note`:
  - "From about 400 Augustine called them heretics, and only for their separation, and the emperor's law of 405 placed them beside the Manichaeans" runs to 28 words. Split it.
  - "Father, Son and Holy Spirit were one God" is narrator assertion. Use "They confessed Father, Son and Holy Spirit as one God."
- **N10.** Unit 5 uses "its rival" twice in a row. Use "In Numidia it far outnumbered the other church."
- **N11.** The deleted front body held judgment call (e): why `don.quote.the-shores-are-covered` is kept out of `pull_quotes` (it is violent imagery that a reader may take literally). Route the reason to `Build/Ministry` so a later pass does not add the quote back unknowingly.
- **N12.** Bagai telling: "Neither was baptized again or ordained again" matches the records. But the next line, "If baptisms given in schism could stand", has no link back to it. Possible change: "...and the baptisms they had given in schism were allowed to stand."

## Tails (the project lead's ruling)

Every telling now ends on its last real event or on a hedge attached to a claim. The one remaining empty tail is "That question is left open." (SF-10). Two cuts removed hedges that rigor required: the Macrobius attribution (SF-5) and the pars Donati attribution (SF-1).

## Readability

Most units score below FK 8, as the fixer reports. CLAUDE.md treats grade 8 as a floor worth staying above, but says the risk it guards against is flattening, not over-simplicity. The substance has not been flattened. Not a finding.

## Verdict

**NOT APPROVED.**

Counts: BLOCKING 1 · SHOULD-FIX 11 · NIT 12.

Thirteen of the fourteen round 1 blocking findings are truly fixed. B12 is half fixed. The remaining defects are mostly lost attributions, unclear referents and a few new overstatements. All have exact fixes above. This is round 2 of 3. A targeted round 3 that checks only BL-1 and SF-1 to SF-11 should be enough.
