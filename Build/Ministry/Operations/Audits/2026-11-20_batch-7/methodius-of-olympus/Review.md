# Review: Methodius of Olympus

Story: `methodius-of-olympus.brief.txt`, approved before the kit (Standard v1), reviewed under the change order of 2026-11-19: approved wording is kept wherever it passes, and a fix touches only what fails. There is no `Outline.md`; the story is traced to `Build/Ministry/Operations/Audits/2026-11-16_eight-standard-v1/` (`drafts/methodius-of-olympus.refs.md`, `reviews/`, `quotation-originals.json`) and to `cic/texts/`.

## The three lines, from one hearing

- **Who:** Methodius, a bishop in Lycia around the year 300, who wrote against Origen half a century after Origen's death.
- **What happened:** He argued in On the Resurrection that the body is no chain on the soul and that the same flesh will rise; two of Origen's admirers say he attacked Origen and then praised him; Jerome says he died a martyr at Chalcis.
- **Why the connection matters:** His answer outlasted him. Epiphanius copied it word for word against Origen, Jerome counted his reply to Porphyry among the good ones, and Theodoret kept his words among the martyrs who witness to the faith.

All three lines can be written. None is blank or wrong.

## The essence

My own, from the census entry and what he is known for: **a bishop in Lycia, martyred about 312, who wrote the Banquet of the Ten Virgins in praise of the chaste life, and argued against Origen that the body is no fetter and that the same body rises; later opponents of Origen leaned on his answer.** Also told: his reply to Porphyry, and Theodoret keeping him among the bishops and martyrs.

The census `why` names the Banquet first ("He wrote the Banquet of the Ten Virgins, a dialogue that praises virginity"), the teaser gives "a bishop who had ten women speak on chastity", and the card's `knownFor` ends "and who praised the life of chastity". The story never names the Banquet (finding B2).

The story's essence is complete at "His chief quarrel with Origen was over the body." (word 147 of 311). That is inside the first minute, at its edge. Pass.

## Scores

- **Voice: 3.** An adult, plain register with no AI tells. But the opening sentence stacks time, place and tradition, and the middle runs witness after witness ("says", "asked", "says", "reports", "writes", "counted", "kept"), so parts read as a report about the record. With a record this thin that is partly unavoidable.
- **Craft: 3.** The fig-tree image carries the idea well, as the Teacher shape asks. But the death is told in the third paragraph and the story then goes back to his writings, and it ends on Theodoret, a later writer, rather than on Methodius.
- **Rigor: 4.** Every sentence traces to a held source, the one quote is verbatim, and both partisan witnesses are flagged as such. It loses a point for leaving out his one surviving whole work, which the census puts first.
- **Accessibility: 4.** Grade 9.3 (names out 7.1), reading ease 73.5 (names out), 16.4 words a sentence, longest 27. Lycia and Porphyry get their plain sense in the sentence. Nothing talks down.

Score: `python -m engine.m1.profile_readability ...methodius-of-olympus.brief.txt`: 311 words, grade 9.3 (names out 7.1), reading ease names out 73.5, 16.4 words a sentence, 0.3 joining words per 100, 5% short sentences, longest sentence 27 words, pass.

## Verdict: REVISE

Two BLOCKING findings, both fixed by moving one clause and adding one sentence of wording that was already checked and approved in the Standard v1 rounds. All other approved wording stands.

## Findings

### B1. BLOCKING: the death is told, then the story goes back (jump back after the essence)

Paragraph 3 ends "and that he died a martyr at Chalcis." Paragraphs 4 and 5 then go back to what he wrote while alive: the quarrel over the body and the reply to Porphyry. Kit Part 1: "never the ending and then back"; the bar: "a jump back after the essence is a failure to understand on one hearing." This also leaves the story ending on Theodoret, a later writer (Kit Part 1: "end on the person ... their death").

**Change (smallest):**
- In paragraph 3, replace `Jerome says he was bishop of Olympus and later of Tyre, and that he died a martyr at Chalcis.` with `Jerome says he was bishop of Olympus and later of Tyre.` (the Banquet sentence from B2 follows it).
- After the last sentence (`He named him among the bishops and martyrs whose words witness to the church's faith in Christ.`), add: `Jerome says Methodius died a martyr at Chalcis.`

Source: Jerome, Lives 83, `npnf203_theodoret-jerome-gennadius-rufinus.xml` 41102-41105 ("he was crowned with martyrdom at Chalcis in Greece"). The story still gives no date, so Jerome's two dates (end of the recent persecution, or under Decius and Valerian) stay on the card, which already credits both.

### B2. BLOCKING: missing essential material, the Banquet of the Ten Virgins

The census `why`, teaser and card `knownFor` all set the Banquet and its praise of chastity at the centre of who he is, and William Clark's introduction calls it the only complete work of his that survives (`anf06_...methodius-arnobius.xml` 29774-29776). The Standard v1 text had it; the 2026-11-16 tightening cut it because it "carries no stance with a consequence" (`reviews/tightening-recheck.md`). Under the kit, the essence and what is also told are set from the census entry and what the person is known for, and what a writer made is told as substance. A listener now hears nothing of his surviving book.

**Change (smallest):** after `Jerome says he was bishop of Olympus and later of Tyre.` (B1), add the sentence the Standard v1 rounds already checked, with its subject made plain: `Methodius wrote a Banquet of the Ten Virgins, in which ten women in turn praise the chaste life.`

Sources: Jerome, Lives 83, J3 41097-41098 ("a *Banquet of the ten virgins*"); the work itself, AN 29720 (title "The Banquet of the Ten Virgins; or Concerning Chastity"), 29930-29933 ("ten in number"), and the Discourse headings from AN 29984 (Marcella to Domnina, ten speakers in turn). Claim nothing further for it: the held sources show no later use of it.

After B1 and B2 the story runs about 329 words, about 2:12.

### M1. MINOR: the opening sentence stacks time, place and tradition

`Around the year 300, Methodius was a bishop in Lycia, in the south of Asia Minor, in the Anatolian church of the third century.` Kit Part 1: time, place and tradition come "a clause at a time ... never stacked in one sentence." "Around the year 300" and "of the third century" also say the time twice. Optional split, since the text is re-recorded for B1 and B2 anyway: `Around the year 300, Methodius was a bishop in Lycia, in the south of Asia Minor. He belonged to the Anatolian church of the third century.`

### M2. MINOR, source finding for the card: Tyre or Patara

The story credits "later of Tyre" to Jerome by name (J3 41095-41097), so the story is sound. But the NPNF editor's note to Theodoret's Eranistes reads "Bishop first of Olympus and then of Patara at the beginning of the 4th c." (J3 20517-20520, note 1126). Under "Batch 6: where sources disagree" (2026-11-19), the card's `uncertain` should credit both: Jerome's Tyre and the editor's Patara. No change to the story.

### M3. MINOR, for the card: "Only Socrates" tells of his change of heart

The card's `uncertain` says "Only Socrates of Constantinople tells of his change of heart". The story also gives Eusebius's complaint, as Jerome quotes it (J3 51484-51490). The refs note rightly that Eusebius's words do not by themselves say Methodius praised Origen; Jerome reads them so. The card line should say that, so card and story agree. No change to the story.

## One-hearing checks

- **Hook to essence:** the story opens on its setting rather than a moment, and reaches the essence (he wrote against Origen; the quarrel was over the body) by word 147. Pass.
- **Held-back name reveal:** none. Pass.
- **Life told once, in order:** fails only at B1. The Socrates and Eusebius scene in paragraph 2 reaches ahead to his later change, which the kit allows the hook and essence to do.
- **Ending on the person:** fails now (ends on Theodoret); fixed by B1.
- **Names:** Methodius, Origen, Socrates of Constantinople, Eusebius of Caesarea, Jerome, Photius of Constantinople, Epiphanius of Salamis, Porphyry, Theodoret of Cyrrhus. Each one acts or is a tree link (all but Porphyry are census people; Porphyry acts, as the writer Methodius answered). Nine is past six, but each is needed: five are the witnesses the story credits beside their claims. Spellings match the census. No finding.
- **Where I got lost:** nowhere. **Children's book or talking down:** nowhere.
- **Words to explain:** there is no outline list. Lycia ("in the south of Asia Minor") and Porphyry ("who had written against the Christians") get their plain sense in the sentence. "Fetter" is told as "chain". No word a grown listener knows is glossed. No finding.

## Length

311 words, about 2:05, far under the 4:00 aim. I asked of each part whether the story needs it. Each one serves the heart, the record's force (the partisan witnesses), the connection (Epiphanius, Jerome on Porphyry, Theodoret) or what is uncertain ("Little else about Methodius is certain."). No cuts to list.

## Sentences

None past 30 words; the longest is 27. No finding.

## Source check

Each sentence traced to its held file and line (files under `cic/texts/`):

- Bishop in Lycia, of Olympus, later of Tyre: Socrates VI.13, `npnf202_socrates-sozomen-ecclesiastical-histories.xml` 18141-18142; Jerome, Lives 83, J3 41095-41097. "Around the year 300" is a reckoning (Eusebius's "now", J3 51488; Jerome's later date, J3 41102-41103), told as approximate. Origen dead some fifty years: J3 40589-40591.
- Socrates: attacked Origen "in various places", then "as if retracting all he had previously said, expresses his admiration of the man, in a dialogue": S 18151-18154. Socrates defends Origen against his "carping detractors": S 18135-18137.
- Eusebius, "in the sixth book of his Apology for Origen", as Jerome quotes him: "How could Methodius dare to write now against Origen, after having said this thing and that of his doctrines?": J3 51484-51490. Told without marks, fairly.
- Martyr at Chalcis: J3 41102-41105.
- Origen's teaching, as Photius's summary gives it: "the body was given to the soul as a fetter after the fall": AN 35875-35876. Methodius: "The body is not, then, a fetter ... at all" and man is "composed out of the union of soul and body": AN 35888-35894.
- The fig tree in the temple's stones, torn away so "the temple may be preserved": AN 35384-35398.
- Quote: "with the same parts, uninjured and immortal, while sin is utterly and entirely destroyed." Verified verbatim at AN 35400-35402 (the phrase breaks across lines at "same / parts"). It does a job the narrator's words cannot: Methodius's own claim that the same body rises. Card entry matches.
- Epiphanius, content "with what blessed Methodius said in his discourse on the resurrection against Origen", set out "κατὰ λέξιν" (word for word): `epiphanius_panarion-haer-34-64-gcs-bd2-grc_holl1922.txt` 32501-32506; Petavius's Latin "ad verbum omnia transcribam", `epiphanius_panarion-haer-48-69-corpus-haereseologicum-t2-pars-posterior-grc-lat_oehler1860.txt` 19234-19237. "Instead of arguing it himself" is fair to his "being of small ability, I thought it right to be content with".
- Porphyry "ably answered ... by Methodius, Eusebius, and Apollinaris": `npnf206_jerome-principal-works.xml` 16539-16540; the reply "perished": J6 9759-9760; Clark: lost "with the exception of some slight fragments", AN 29782-29784. The story's "lost" is sound for a hearing; the card carries the fragments.
- Theodoret, "Testimony of the Holy Methodius, bishop and martyr, from his discourse on the martyrs": J3 20517-20526; "Hippolytus and Methodius, bishops and martyrs", named on "the divine incarnation": J3 20250-20262.

No unsupported claim, no unsourced cause, no added feeling. The one disagreement the story could touch, Jerome's two death dates, stays out of the story because it gives no date, and the card credits both. Tyre or Patara: M2.

## Quotes and overlap

The only quoted words are the On the Resurrection line, verified above. Checked against every `*/*.brief.txt` in this batch: no other story quotes it or uses the fig tree in the temple (Peter of Alexandria's barren fig tree is the gospel's, a different image), and no other story quotes Socrates, Eusebius's complaint, Epiphanius or Theodoret on Methodius. Origen's story mentions him in one clause ("Methodius of Olympus wrote against him"), which agrees with this one.

## Do not say

No outline exists to add lines to. For any later revision of this story: do not give a date for the martyrdom (Jerome gives two); do not call the Banquet "the only complete work" without crediting Clark; do not claim any later use of the Banquet.
