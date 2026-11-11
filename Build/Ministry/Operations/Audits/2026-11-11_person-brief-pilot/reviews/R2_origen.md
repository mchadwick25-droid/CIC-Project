# R2 targeted recheck — Origen (brief and card)

Reviewer: independent Opus, round 2 (targeted). Line numbers are lines of the files in /home/user/CIC-Project/cic/texts/. E = npnf201 (Eusebius), J = npnf203 (Jerome, Lives ch. 54), S = npnf202 (Socrates), A4 = anf04 (On First Principles), A9 = anf09 (Origen, Commentary on John), G = npnf207 (Gregory of Nazianzus), C = npnf214 (councils), P = npnf206 (Jerome, Against John).

## Verdict: REVISE

Two card claims misattribute or misstate their source. The audio needs one STANDARD fix: it no longer says what Origen did with Scripture. A second fix is also needed: the Demetrius sentence does not give cause and sequence by ear. Both audio fixes fit in one replacement of paragraphs 2 to 5, which runs to 339 words.

## Quote and score

- Quote: "Take heed not to change your mind on our account." Exact-string check against E 32562: MATCH (one occurrence; the curly quotes are in the file, and the brief uses straight quotes only).
- score.py on A/origen.txt: 330 words, FK 8.9, FRE 60.4, no fails. My replacement (below), scored from a scratch copy: 339 words, FK 9.0, FRE 60.9, no fails.

## Round-1 findings

1. Philocalia told as settled: RESOLVED. The audio now tells it through Gregory's letter and hedges the compiling ("are thought to have gathered"). G 47440-47452 says "we send you the volume of the Philocalia of Origen". The date of about Easter 382 is at G 47441-47442.
2. "carried this into doctrine": RESOLVED. The phrase is gone. But the body, soul and spirit teaching went with it (see finding 3).
3. Theology read as a list, Celsus: RESOLVED.
4. Demetrius and Caesarea: PARTLY RESOLVED. The conflict is back, and the castration story is on the card as Eusebius's account (E 33190-33224, which checks). But the sentence that carries the conflict hides the cause (finding 4).
5. Ear anchors: RESOLVED. The brief now says "under the emperor Decius" (Decius took power in 249, E 37383-37388; 231 plus about twenty years fits). It also says "Three centuries after his death, a council at Constantinople" (553; Jerome's note gives his death as 253, J 40523).

New or changed audio claims, all checked. Around the year two hundred, the tenth year of Severus, dated 201–202 by the editor: E 32523, 32457-32458. Arrest, longing, mother, letter: E 32535-32562. Property taken: E 32613-32614. Eighteenth year, everyone else had fled: E 32670-32674, 32732. Ambrose and the seven secretaries: E 35887-35897. Eternal generation: A4 23139-23140. Souls before birth: A4 22108-22112, 28653-28655. End like the beginning: A4 24268-24272. Rufinus and Jerome: A4 22124-22130. Epiphanius: P 40528, 40816-40817. Jerome on the rage: J 40533-40538. 231: E 36331-36333. Decius, the stocks, the judge: E 37489-37508. Sixty-nine, Tyre: J 40589-40592. Socrates on Athanasius: S 18164-18172. Anathema XI: C 23853-23855. All supported.

## Findings

### 1. BLOCKING (card, legacy_traces[0]). Eusebius is credited with the editor's words, and the direction of the teaching is reversed.

The card says: "Eusebius tells that a young man named Gregory came to Caesarea with his brother Athenodorus, meaning to study law. They stayed five years with Origen, who led them from Greek philosophy into the study of divinity."

Eusebius does not mention law. The plan to study law at Berytus comes from the editor's note, which cites Gregory's own Panegyric (E 36587-36590). Eusebius says something different. Origen found them "deeply interested in Greek and Roman learning". He "infused into them a love of philosophy, and led them to exchange their old zeal for the study of divinity" (E 36678-36684). So Origen led them into philosophy, not away from it.

Replacement: "Eusebius tells of two brothers, Gregory and Athenodorus, who came to Origen at Caesarea full of zeal for Greek and Roman learning. He gave them a love of philosophy and turned them to the study of divinity. After five years with him, both became bishops in Pontus."

### 2. BLOCKING (card, legacy_remembered[1]). "First condemned" is not supported, and it gets Socrates's order wrong.

The card says: "Socrates also says Theophilus of Alexandria first condemned Origen's books as a cover for his move against John Chrysostom."

In Socrates, Theophilus first disowns Origen's works to calm the monks: "I myself also disapprove of Origen's works" (S 17605-17611). Only after that does he write to the bishops. In those letters he "concealing his real motive, ostensibly condemned therein the books of Origen merely" (S 17840-17842). The cover story comes second, not first.

Replacement: "Socrates also says Theophilus of Alexandria wrote to the bishops condemning Origen's books, to hide his real aim, which was to move against John Chrysostom."

Also fix the matching written_about entry. It should read "Church History, Book 6, chapters 7, 10 and 13", because the card draws on all three.

### 3. STANDARD (audio). What Origen developed is missing, though Mark asked for "what they developed". This is substantial.

The audio now gives his teaching only through the points later charged against him: pre-existence, the end like the beginning, the Rufinus caveat. The one exception is eternal generation. Nothing in the audio says what he built with the Bible. Yet the card's own role line is "Teacher and Bible scholar". His two lasting achievements are both well sourced, and both were cut:

- He learned Hebrew. Eusebius: "So earnest and assiduous was Origen's research into the divine words that he learned the Hebrew language" (E 34428-34430). Jerome adds "contrary to the spirit of his time, and of his people" (J 40556-40557).
- He set the texts side by side in the Hexapla: "placed them opposite each other, with the Hebrew text itself. He thus left us the copies of the so-called Hexapla" (E 34715-34717). Jerome describes the same work (J 40557-40566).
- He taught that Scripture has body, soul and spirit. The plain "body" is for "the more simple", the "soul" is for those who "have commenced to make considerable progress", and the spiritual law is for "those ... who are perfect". The basis is "For as man is said to consist of body, and soul, and spirit, so also does sacred Scripture" (A4 32390-32403).

The listener expects these things from a "Bible scholar", and they are what later readers took up: the Philocalia is a book of his passages on Scripture. Leaving them out flattens Origen into a list of the charges against him.

Fix: see the combined replacement under finding 4. To make room, it drops the Ambrose sentence, the judge clause and the Epiphanius sentence. The Epiphanius charge moves to the card (finding 5).

### 4. STANDARD (audio, for the ear, and the order of events). "...and Eusebius says the bishops of Caesarea and Jerusalem had ordained him" does not give cause and sequence correctly.

As heard, the listener gets the rage first and the ordination second, joined by "and" and handed to a second witness. It sounds like a separate fact. Nothing says the ordination is what enraged Demetrius, and "him" could mean Demetrius. Jerome gives a single, clear chain. On a journey through Palestine, "having been ordained presbyter by Theoctistus and Alexander, bishops of Cæsarea and Jerusalem, he offended Demetrius, who was so wildly enraged at him that he wrote everywhere to injure his reputation" (J 40531-40538).

Eusebius orders the events differently. Demetrius wrote against Origen first, out of jealousy over "this deed of his boyhood". The ordination came after, and then more accusations (E 33210-33234). Splicing Jerome's rage onto Eusebius's ordination suggests the two witnesses agree on the order, and they do not. Tell it in Jerome's order and name Jerome alone. The card already carries Eusebius's version.

Replacement for paragraphs 2 to 5 (paragraphs 1 and 6 unchanged):

"His father died a martyr, and the state took the family's property. Origen was not yet seventeen, with six younger brothers. In his eighteenth year he took charge of teaching the faith in Alexandria, because everyone else had fled.

Origen learned Hebrew, and he set the Hebrew text side by side with the Greek translations, in a work called the Hexapla. He taught that Scripture, like a person, has body, soul and spirit: a plain story for simple believers, and deeper senses for those who grow.

In On First Principles he taught that the Son's generation is as eternal as brightness from the sun. He also taught that souls existed before birth, and that the end will be like the beginning, when death, the last enemy, is destroyed. We read the book mostly in Rufinus's Latin, and Jerome said Rufinus changed it.

But on a journey through Palestine, the bishops of Caesarea and Jerusalem ordained Origen a priest. Jerome says this so enraged his own bishop, Demetrius, that he wrote everywhere to ruin Origen's name. In the year 231 Origen left Alexandria for Caesarea. About twenty years later, under the emperor Decius, he was chained and stretched in the stocks. Jerome says he lived on to sixty-nine and died at Tyre."

Scored with paragraphs 1 and 6 as they stand: 339 words, FK 9.0, FRE 60.9, no fails.

Optional, if the drafter wants Origen's own voice on why he left. In the preface to Book VI of his Commentary on John he writes: "We emerged from the storm, we were brought out of Egypt". He also writes that "the enemy assailed us with all bitterness by his new writings ... and stirred up against us all the winds of wickedness in Egypt" (A9 24726-24733). He names no one, so the brief must not name Demetrius as the enemy. One sentence after "for Caesarea" would do it: "Origen later wrote that he had come through a storm and been brought out of Egypt." It adds 15 words (about 354 in all). To keep near 330, drop the Socrates and Athanasius sentence in exchange. This would also answer the coordinator's request to give the break as the reason for the move, in the only words that say so, which are Origen's own. Without it, the brief rightly states only the sequence, as the round-1 notes say.

### 5. STANDARD (card, which follows from finding 4). The Epiphanius charge needs a home.

If the audio drops "Epiphanius charged that he even taught the devil would repent", add it to legacy_remembered. It is how one tradition remembers him. For example: "Epiphanius charged, and Jerome repeated, that Origen taught even the devil would one day repent" (P 40528, 40816-40817). Add Jerome, Against John of Jerusalem (npnf206_jerome-principal-works.xml), to written_about.

## Card: does it continue the story?

Yes, apart from the fixes above. legacy_traces moves on to his pupils, his letter to Gregory (Philocalia line 149, where the editor names the recipient as Gregory Thaumaturgus, E 51946-51947) and how Gregory of Nazianzus described the Philocalia. legacy_remembered moves on to his four critics, Theophilus and the special anathemas of 553 (C 23853-23855, 24015-24017). None of this restates the audio. The uncertain lines repeat the audio's wording, as REVISE.md asks. They also add the castration and Demetrius story as Eusebius's account, which checks: E 33190-33224, J 40535-40538. key_works and their "about" lines check: E 34715-34717, E 37104-37106. build_page.py's kw() renders the dict form.
