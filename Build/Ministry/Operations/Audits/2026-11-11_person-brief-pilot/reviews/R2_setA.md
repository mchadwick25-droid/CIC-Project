# R2 targeted recheck — set A (Athanasius, Chrysostom)

Reviewer: independent Opus, round 2 (targeted: R1 findings, every new or changed brief claim, every card claim). Line numbers are file lines in /home/user/CIC-Project/cic/texts/. N2 = npnf202 (Socrates/Sozomen), N4 = npnf204 (Athanasius), G = npnf207 (Gregory), Cy = cyril-alexandria_three-epistles-grc-eng_pusey1872.txt, N9 = npnf109, N10 = npnf110, M = palladius_dialogue-life-of-chrysostom_moore1921.txt.

## Quote check
Exact-string compare after stripping tags and notes and collapsing line-wrap whitespace (script: scratchpad/r2/qc.py):
- "For He was made man that we might be made God": N4 18743-18744. MATCH.
- "begotten not made, One in essence with the Father": N4 19679. MATCH.
- "In praising Athanasius, I shall be praising virtue.": G 29460-29461. MATCH. This is the oration's opening sentence, so "began a sermon" is accurate.
- "our blessed and all-celebrated Father Athanasius": Cy 5392-5393. The file wraps it as "all-cele- / brated". A strict compare fails on the line-break hyphen alone. With the hyphen removed it is a MATCH. The unbroken spelling "all-celebrated" is confirmed in the same letter at Cy 5438.
- "Wouldest thou do honor to Christ’s body? Neglect Him not when naked": N10 29931 (curly apostrophe as printed). MATCH.

## score.py
- athanasius-of-alexandria.txt: 299 words, FK 9.2, FRE 62.0, in band.
- john-chrysostom.txt: 300 words, FK 8.6, FRE 62.3, in band.
- The replacement texts below were scored the same way. Athanasius: 300 words, FK 8.1, FRE 66.2. Chrysostom: 296 words, FK 8.6, FRE 62.5. Both are in band and at or under 300 words.

## Specific watch items
- **Eutropius in 399.** The year comes from the NPNF endnote at N2 17369 ("399 a.d."). That note is attached to Eutropius's beheading and to his consular year, the year Socrates names through his colleague Theodore (N2 17365-17368). Socrates places the flight during that consulship ("though bearing the consulate"). Moore's chronology (M 655-712) does not list it. This is an editor's date, but the file documents it plainly, so telling it directly is acceptable. The notes already say so. No finding.
- **Robertson and Schaff material.** The following are now told directly and documented plainly at the cited lines: 335 Tyre; 328 at about thirty (Robertson rejects the Theodoret-based 325/326 date in the N2 3992-3997 note, at N4 9242-9248); the search of towns, monasteries and tombs (N4 5918-5922); "more than half of his surviving works" (5916-5917); 366 (7104-7108); Peter (7262-7266); May 373 (7266-7268, 9614-9619); the Antioch riot, John's preaching and Flavian (N9 1244-1262). None of these sources is used as a story witness. OK.
- **Tyre opening.** Faithful. Socrates: "they publicly exposed it as the hand of Arsenius ... made use of by Athanasius in the performance of certain magic arts" (N2 5028-5033); "his traducers exhibited the hand" (5101-5102); the cloak and both hands (5104-5120); Sozomen's "as it is said" (30011-30016); deposed in absence (30049-30051). Nothing is embellished. The sentence has an ear problem, however (A2).
- **Eutropius opening.** Each detail is in Socrates (N2 17326-17363: the law against sanctuary, "fled for protection to the church", "trembling with fear lay under the table of the altar", "mounting the pulpit", "uttered an invective", "added insult to cruelty"). Nothing is invented. But the scene is one-sided against a source the Library holds (C1).
- **Cyril and 433.** The only support the notes give for 433 is Cy line 9. That is the project's own vendoring content note, not Pusey: Pusey's text gives no year (grep finds none). The year is independently documented at npnf203 4410-4413 ("In 433 formal peace was made ... by the acceptance by both John of Antioch and Cyril of the formula"). The notes should cite that. This is a fix to the notes only, not a finding.

---

## Athanasius of Alexandria — REVISE

### R1 findings
- R1-1 (Robertson as witness): RESOLVED. The point is told directly and the source stays in the notes.
- R1-2 (flat ending): PARTLY. The death is now told as a moment, with Peter named. But the brief now ends on "and sent out true copies of one of his letters", which is flatter than before (A3).

### Findings

**A1. BLOCKING (card, `uncertain` line 2).** The line reads: "It comes only from Rufinus and Socrates, and the story is not told in the audio." This is wrong. Sozomen tells the story too, at length (N2 29385-29403), and Robertson notes it ("adds Sozomen (ii. 17)", N4 1580-1581). The detail "on the shore" comes from Sozomen (N2 29391), not from Socrates (N2 4002-4017). Separately, "not told in the audio" is process narration on a participant-facing surface.
Replacement:
> "Rufinus tells that Bishop Alexander once watched boys on the shore playing at church, and that the boy who played bishop was young Athanasius. Socrates, who names Rufinus as his source, thinks it not improbable, and Sozomen tells it too."

**A2. BLOCKING (minor, card, `uncertain` line 3).** The card says "Socrates says Athanasius lay four months in his father's tomb." Socrates's text says "concealed himself for four entire months in an ancestral tomb" (N2 13061-13062). The phrase "father's tomb" is Robertson's rendering, in a note (N4 7096-7097).
Replacement:
> "Socrates says Athanasius hid for four months in a family tomb. The Historia Acephala, a record of his life, says he went to a country house near the city."

**A3. STANDARD (brief, ear).** The opening sentence runs 31 words. "Whom Athanasius had murdered and used for magic" makes Arsenius, not the hand, the thing used for magic. It also sounds like the narrator asserting the murder, in the first five seconds.
Replace:
> "Athanasius's accusers held up a severed hand and said it belonged to a bishop named Arsenius, whom Athanasius had murdered and used for magic."

with:
> "Athanasius's accusers held up a severed hand. They said he had murdered a bishop named Arsenius and used the hand for magic."

Source: N2 5028-5033. To stay within the ceiling, also cut "for Athanasius" after "plain sympathy".

**A4. STANDARD (brief, ending; notes inaccurate).** The legacy beat ends on "and sent out true copies of one of his letters". The listener cannot place which letter or why it matters. It is a weak last image. The Round-1b note also says this clause was removed from the audio, but it is still there. Gregory's line also has no time anchor.
Replace the last paragraph with:
> "Years later, Gregory of Nazianzus began a sermon: "In praising Athanasius, I shall be praising virtue." Sixty years after his death, as Cyril of Alexandria made peace with the bishops of the East, he wrote that he followed, above all, "our blessed and all-celebrated Father Athanasius.""

Sources: G 29434-29461 (oration opening; the sermon was given at Constantinople about 379-380 per its introduction, so "Years later"); Cy 5100-5104 ("deep exultation at the return of peace to the Church ... envoy of the Orientals"), Cy 5392-5393 ("specially of"); 433 at npnf203 4410-4413. The true-copies detail stays on the card, where it already is. Correct the 1b note.

Full replacement brief (A3 and A4 applied; 300 words, FK 8.1, FRE 66.2): scratchpad/r2/ath3.txt.

**A5. STANDARD (card restates the brief).** Mark ruled that the card continues the brief's story and does not restate it, and that `uncertain` repeats the brief's caveat in its own words before adding detail. The card breaks both rules:
- `uncertain` line 1 copies the audio almost word for word and adds nothing.
- `legacy_traces` line 2 and `legacy_remembered` line 1 repeat the Gregory and Cyril quotes the audio already carries.
- `legacy_traces` line 1 also has an unclear "he": "so that he need not tell it himself".
- `legacy_remembered` line 2 adds "chiefly", which Socrates does not say.

Replacements:
- `uncertain[0]`:
  > "How Arsenius reached Tyre is not settled. Socrates credits God's providence: the governor's servants heard at an inn that he was hiding in a citizen's house, and the governor had him found. Sozomen gives two reasons, a divine prompting or, "as it is said", a plan of Athanasius, and says Arsenius slipped into Tyre by night the day before the trial."

  Sources: N2 5084-5096; N2 30011-30016.
- `legacy_traces[0]`:
  > "Socrates declines to tell Antony's story because Athanasius had already given a whole book to it. Evagrius, later bishop at Antioch, put that book into Latin with a short apology for how freely he rendered it."

  Sources: N2 4508-4512; N4 30510-30516.
- `legacy_traces[1]`:
  > "Gregory of Nazianzus gave him a whole sermon at Constantinople, and in it says that all who have lived according to God still live to God."

  Sources: G 29440-29442, 29464-29466.
- `legacy_remembered[0]`:
  > "Honored in the East within a lifetime: Cyril of Alexandria singles him out among the Fathers whose teaching he refuses to step outside of."

  Source: Cy 5392-5394.
- `legacy_remembered[1]`: change "chiefly for peace" to "for the sake of unity in the church" (N2 5368-5371).

---

## John Chrysostom — REVISE

### R1 findings
- R1-1 (Isidore): RESOLVED (N2 17097, 17378-17381).
- R1-2 (February 398): RESOLVED (N2 17097, 17108-17110).
- R1-3 (Schaff as witness; John's action missing): RESOLVED. The riot, the preaching and Flavian are told directly (N9 1244-1262). Schaff is not named.
- R1-4 (witnesses as a pair): PARTLY. The pair is introduced in a sentence of its own that neither witness then uses (C2).
- R1-5 (33-word sentence): RESOLVED. But a new 38-word sentence now carries the riot (C2).

### Findings

**C1. BLOCKING (brief, misleading by omission in the opening scene).** The new opening gives only Socrates's hostile reading: John preached against the fallen man and "some thought John added insult to cruelty". The Library holds John's own sermon from that day, and it says the opposite about his intent.
- "I say these things not by way of reproaching him, or insulting his misfortune, but from a desire to soften your minds towards him, and to induce you to compassion" (N9 17699-17702).
- He was blamed "for having admitted him to the sanctuary" (17704).
- The church, "like an affectionate mother has concealed him under her cloak" (17722-17724).
- The editor's introduction to these homilies says John hid Eutropius and refused to give him up (N9 17534-17536). That is told directly, not as a witness.

Told as it stands, a disputed reading of John's character is the first thing the listener hears, and John's side of it, and his theology of the church's mercy, is missing. The trailing "Yet it was Eutropius who had made Theophilus of Alexandria ordain John" then reads as a further mark against him.
Replace paragraph 1 with:
> "In 399, the emperor's chief eunuch, Eutropius, fled into the cathedral of Constantinople, though he had just stripped refugees of the right to shelter there. As he lay trembling under the altar table, Bishop John climbed into the pulpit and preached against him. Socrates says some thought John added insult to cruelty. John himself said he spoke to soften the people's hearts toward him, for the church, like a mother, had hidden her enemy under her cloak."

Move the Eutropius-ordination fact into paragraph 3:
> "In February of 398 John had been made bishop, the court's own choice, and Eutropius had made Theophilus of Alexandria ordain him."

Source: N2 17097-17110.

**C2. STANDARD (brief, ear and shape).** Paragraph 2 has three problems.
- It opens with two sentences about the witnesses ("Palladius stood by John to the end. Socrates writes from a distance and judges him more coolly, calling him stern."). Neither witness is used in what follows. That is fact-giving about sources, not story.
- Socrates gives "stern" as hearsay ("It is said that ... he was stern and severe", N2 17243-17245), not as his own judgment.
- The riot has no time anchor after a 399 opening, and it sits in a 38-word sentence.

With C1, Socrates's distance is already shown in the scene. Palladius's loyalty goes where he is first used.
Replace paragraph 2 with:
> "Years before, a tax riot in Antioch tore down the emperor's statues. John, by then a priest, preached to the frightened crowds, comforting them and urging them to change their lives, until old Bishop Flavian won the emperor's pardon."

In paragraph 3, use:
> "Palladius, who stood by John to the end, says he found the bishop's expenses extravagant and moved that money to the hospital. John told the rich: ..."

This also drops "own" from "the bishop's own spending", which the ear hears as John's own (M 3745-3751). It drops the work title "in a homily on Matthew", which the card carries. Also cut "Socrates says" from the uncontested 438 sentence.

Full replacement brief (C1 and C2 applied; 296 words, FK 8.6, FRE 62.5): scratchpad/r2/chr5.txt.

**C3. STANDARD (card `uncertain`).** `uncertain[0]` copies the audio verbatim ("Palladius stood by John to the end. Socrates writes from a distance...") instead of restating the caveat in its own words before adding detail. After C1 and C2 the audio's caveat is the Eutropius sermon, so this line should carry it.
Replacement:
> "Socrates reports that the sermon over Eutropius struck some as cruel. In the sermon itself John says he was blamed for taking Eutropius into the sanctuary, and that he described the man's fall to move the people to mercy. Socrates also passes on that John was said to be stern and severe, and that a friend of his youth found him more prone to irritability than to modesty."

Sources: N2 17360-17363, 17243-17248; N9 17699-17706.

The rest of the card checks:
- shorthand (N2 17300-17308)
- Johannites and the baths (18489-18496)
- 27 January 438 and the Apostles (21455-21470)
- watch all night (18299-18301)
- Severian (18330-18337)
- Sisinnius and "Approach, although you may have repented a thousand times." (18617-18640)
- two hundred years / thirty-fifth year (21472-21478)
- meals (M 6623-6634; N2 17277-17300)
- Comana (N2 18609-18610; M 6436-6441)
- On the Priesthood as deacon (N2 17212-17215)
- Palladius's exile for John's cause, supporting "stood by" (M 788-801)

**Notes fix (not a finding).** The notes cite N2 17187-17190 for On the Priesthood. The passage is at 17212-17215.
