# Round 3 recheck (targeted, last allowed round): Donatist Atlas story pass

Scope: worktree `agent-a7199f86b9cdac231`, branch `site/atlas-story-don-fixes`, `git diff bcdd55fbb 80f9007e2`. I read every changed sentence in `Build/worlds/don/surface/world_front/don.front.donatism.md`, the eight changed `telling:` lines and the new OG-41 entry. I checked them against the records in `records/don/` myself. I re-read line numbers in `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`, and the deleted bodies at 8afababd9.

## 1. Round 2 findings

| # | Status | Note |
|---|---|---|
| BL-1 voice inventory | **Fixed** | Unit 9 and the tile now say most Donatist words survive as quotations in the opponents' books. This matches `don.core.donatism` `thinness` ("almost entirely as quotation embedded inside its own refutations"). The "four short texts" are core caution 2's four, which include the Liber Regularum. It now agrees with `read_first[1]`, `who_speaks` and the Petilian voice entry. |
| SF-1 party of Donatus | Attribution fixed. **The new closing sentence causes a contradiction.** | See R3-1. |
| SF-2 rebaptism as root | Fixed | It now agrees with `don.gravity.rebaptism-boundary-marking`. The rewrite leaves a referent clash. See R3-4. |
| SF-3 referents | Fixed in unit 3, unit 4 and the tile's "the church" | The tile still uses "rival church" for both sides. See R3-4. |
| SF-4 Emeritus "each time" | **Half fixed** | See R3-2. |
| SF-5 Macrobius attribution | Fixed | |
| SF-6 Marculus hedge | Fixed | |
| SF-7 legacy "beaten" | Fixed | |
| SF-8 provenance template | Fixed | The Acta and Gesta sentences now differ. A small repetition is left (N-c). |
| SF-9 Acta letter | Fixed | It matches the story `text` ("closing lines ... Caecilianus said he had never dictated them"). |
| SF-10 sourcing tells and tail | Fixed | |
| SF-11 Latin trail | Fixed through OG-41 | One line number is off by one. See N-a. |
| N1 to N12 | Fixed | Two side issues: N6's "it" has no antecedent (N-b), and N10's merge blurred unit 5 (N-d). N11 went to OG-41 rather than `Build/Ministry`. That is acceptable, because the gaps log is a permanent audit trail. |

Gesta check: "because its findings tell against us" is the story `divergence_note` almost word for word ("it is preserved because its findings tell against us"). Bagai check: "These two had baptized while in schism" is supported by the story `text` ("the baptisms these bishops had given in schism"). Augustine's conditional is kept.

---

## SHOULD-FIX

### R3-1. Unit 1 contradicts itself about the Donatists' own name
- **Where:** `orientation.story` unit 1, last sentence (new in 80f9007e2)
- **Quote:** "It called itself the Church of the Martyrs, the one pure, persecuted and true church. ... Optatus, an opponent, says its bishops called themselves 'the party of Donatus' when questioned in court. What they called themselves among themselves is not known."
- **Evidence:**
  - The same unit says, three sentences earlier, what they called themselves. The last sentence then says this is not known. Read together, the two statements cancel each other out.
  - The record's hedge is narrower. `don.term.pars-donati` `plain_meaning` reads "Whether we named ourselves that way among ourselves, the record cannot say." Its `translational` sense reads "Whether they named themselves so among themselves". Both are about the phrase *pars Donati* only.
  - Round 2 proposed this wording. The fixer adopted it, but it is still wrong against the record.
- **Fix:** Replace the last sentence with "Whether they used that name among themselves is not known." That is +1 word; see the word-cap note at the end.

### R3-2. Emeritus: the appeal reservation still reads as his usual practice (SF-4 half fixed)
- **Where:** `voices` Emeritus `text`, last sentence; `don.story.conference-of-carthage-411` telling, paragraph 4
- **Quote:** "He signed the notary's record of most of what he said, and added that he kept his right to appeal."
- **Evidence:**
  - The sentence ties the appeal clause to "most of what he said", so it says he reserved his appeal on most signatures.
  - `don.figure.emeritus` `bridge_line`: "He signed the notaries' record of his words, at times with his appeal reserved."
  - The same record, read directly: "He most often signs the bare formula ... but repeatedly signs instead in the qualified form, with his appeal reserved. ... That variation is real and must not be flattened into one uniform phrase; this world's own Doc_02 review round caught exactly that flattening once already."
  - The story `text` ("as he signed most of what he said there - I, Emeritus the bishop, have reviewed this, my appeal reserved") can be read either way. So the two records do not agree on this point. Log that gap (see the end of this review).
- **Fix (both places):** "He signed the notary's record of most of what he said. At times he added that he kept his right to appeal."

### R3-3. Unit 7: "their spokesman Petilian" makes him the only spokesman
- **Where:** `orientation.story` unit 7 (changed in 80f9007e2 to hold the word cap)
- **Quote:** "Christ had stood before his governor, said their spokesman Petilian, and so would they."
- **Evidence:**
  - Story `text`: "Seven were then chosen from each side to plead for all."
  - `don.figure.petilian`: "one of the seven Donatist pleaders at the 411 Conference of Carthage".
  - The 411 telling and the Emeritus voice entry both say Emeritus "carried" the case. Round 1 S5 had fixed this with "one of their spokesmen". The word-cap trim brought the error back.
- **Fix:** "Christ had stood before his governor, said Petilian, one of their speakers, and so would they." That is +2 words.

### R3-4. Tile: "rival church" names both churches in consecutive sentences
- **Where:** `skim.tile` (the SF-2 rewrite)
- **Quote:** "So a rival church grew up with its own bishops. Anyone who came over to it was washed again by a hand that had never failed. It called itself the Church of the Martyrs. Persecution came again, at the rival church's urging."
- **Evidence:**
  - The first "rival church" is the Donatist church. The second is the Catholic church (`don.force.macarian-repression`: the repression came at the other side's request).
  - With "a rival church" introduced two sentences earlier, a reader takes "the rival church's urging" to mean the Donatists urged persecution of themselves. That reverses the meaning. It is the same kind of defect that SF-3 fixed in this tile.
- **Fix:** "So they built a church of their own, with its own bishops." Leave "at the rival church's urging" as it is. "They" refers back to "the Donatists held" in the sentence before.

---

## NIT

- **N-a. OG-41 item 1 has an off-by-one line number.**
  - Quote: "Line 73363 holds the editor's 279/286 count."
  - Evidence: In the current vendored file, the line "licis 286, et ex Donalislarum parte 279." is **73364**. I counted with `grep -n` and with a Python LF split. The file has no CR or form-feed characters. Line 73363 is blank. The range 124975-125010 is right: "ducenti [s]exaginti sex" is at 124991.
  - The same 73363 also appears in `don.contested.bishop-count-411-conference`, `Doc_02_Source_Ecology.md`, `don_Decision_Log.md` and `scripts/wb_don_s26.py`. So the error comes from older text, not from this fixer.
  - Fix: In OG-41 (not yet merged, so it can still be edited), write "Line 73364 (cited as 73363 elsewhere in the don records; off by one in the current file) holds the editor's 279/286 count." The fleet-wide citations are a separate gap and should not be edited in this PR.
- **N-b. Bagai telling: "it" has no antecedent.**
  - Quote: "Three hundred and ten of our bishops met there and condemned the followers of Maximian in the harshest terms it had."
  - The subject is plural bishops, so "it" points to nothing.
  - Fix: "...in the harshest terms they had."
- **N-c. "In his books against us" now appears in three cards.**
  - Quotes: Cirta ("Optatus tells the story of that meeting in his books against us."), Acta ("the dossier Optatus attached to his books against us") and Bagai ("Augustine quotes the decree word for word in his books against us"). Bagai's wording predates this round.
  - This is the template that SF-8 tried to break, in a new form.
  - Fix: Acta: "Their words survive in the dossier of documents Optatus kept." Cirta and Bagai stay as they are.
- **N-d. Unit 5: the N10 merge puts the councils "in the same towns".**
  - Quote: "a full parallel church, with its own bishops, basilicas and councils in the same towns as its rival."
  - Councils met at single places (Bagai, Carthage). They did not meet in each town. The earlier wording ("and it contested the same towns") did not claim this.
  - Fix: "a full parallel church, with its own bishops, basilicas and councils. It stood in the same towns as its rival." That is +2 words. Drop this NIT if the 700-word cap cannot carry it.

**Word cap (main story, 700).** R3-1 adds 1 word and R3-3 adds 2. To offset them:
- Unit 7: "and penal laws against them followed" becomes "and penal laws followed" (−2).
- Unit 4: "read such accounts aloud again" becomes "read such accounts aloud" (−1), since "Every year" already carries the repetition.

That is net 0. N-d would need two more words cut.

## 2. Every changed sentence in 80f9007e2

Apart from R3-1 to R3-4 and N-b to N-d, I found:
- no new unsupported claim;
- no lost hedge (the Macrobius, Novapetra and pars Donati hedges are all restored, and the Tyconius "it is reported" stays);
- no "this world" or meta "record" in participant text (the only "this world" is the envelope `confidence.divergence_note`, which is metadata);
- no dash asides;
- no AI-tell closers.

The tails Mark ruled on are gone: "That question is left open.", "Even this voice has limits.", "So he put his name...", "and its most filtered" and "He kept it because it hurts us." Every telling ends on an event or on a hedge attached to a claim. The new last sentence of unit 1 is a hedge attached to a claim, not an empty tail. It is defective only because it is too broad (R3-1).

## 3. OG-41

Accurate, except for N-a.
- **OG-33 pointer:** the quoted title and the phrase "the Latin phrases listed in the body note" match OG-33 (line 1530).
- **Latin phrases:** all nine match the deleted 411 body at 8afababd9, word for word.
- **Item 2:** it matches `don.quote.the-shores-are-covered` `modern_lens_note` and the deleted judgment call (e).
- **Item 3:** the deacon Felix in Mensurius's house and Alfius Caecilianus both match the deleted Lucilla and Acta bodies. Core caution 7 carries Maximian and the two Optatuses. The two Marcellini are in `don.figure.marcellinus`. The third Optatus (the Catholic bishop of 411) is still named in `don.contested.rigor-against-reception`, so nothing is lost.
- **OG-40 closure claim:** it holds. No participant section of the front still has "this world" or a dash aside.

**Gap to append in the same PR:** R3-2 shows that the `don.story.conference-of-carthage-411` `text` ("as he signed most of what he said there - ... my appeal reserved") and the `don.figure.emeritus` record ("most often signs the bare formula ... repeatedly ... with his appeal reserved") disagree. It is a record defect and is not fixed here. Append it as a new numbered entry (subject and date).

## Verdict

**NOT APPROVED.**

Counts: BLOCKING 0 · SHOULD-FIX 4 · NIT 4.

BL-1 and ten of the eleven round 2 SHOULD-FIX items are truly fixed. SF-4 is half fixed. The four SHOULD-FIX items are small: one contradiction the round 2 fix brought in, one record-flattening, one narrowing caused by the word-cap trim and one referent clash. Each has an exact one-sentence fix above.

This was the third and last review round. Under the cap rule, the next step is to escalate to Mark with these exact fixes, not to run a fourth review round. If he orders a check of the fixes, it counts toward the cap only if no "Cap ruling" entry names it.
