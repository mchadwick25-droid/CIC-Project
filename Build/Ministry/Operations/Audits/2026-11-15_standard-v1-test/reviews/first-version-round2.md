# Who brief review, round 2 (targeted recheck): Gregory of Tours and Benedict of Nursia

This round checks two things: whether each round-1 blocking finding is resolved, and every new or changed sentence against the held files. It also applies Mark's rulings that came after round 1: several stances, the new length target, and four separate reports. It is not a fresh full review. No model or API calls were made, and no repo file was changed. No blind pair was supplied this round.

## Readability tool (check E)

| Draft | Words | Grade (full) | Reading ease, names out | Words a sentence | Joining words per 100 | Short sentences | Tool |
|---|---|---|---|---|---|---|---|
| Gregory, draft 2 | 439 | 9.5 | 72.7 | 20.9 | 1.1 | 10% | pass |
| Benedict, draft 2 | 413 | 8.8 | 77.9 | 19.7 | 0.2 | 10% | pass |

The length target is under 300 words, stretching to about 375 (2:30 at 150 words a minute), with no hard cap.

---

## GREGORY OF TOURS, draft 2

### Round-1 blocking findings

- **G-1, Hilary and Eusebius unidentified: RESOLVED.** The draft now says "meaning, his translator O. M. Dalton notes, Hilary of Poitiers and Eusebius of Vercelli". Dalton's note at l.26986-26987 supports it. (The way it is attached creates a new access problem: G2-1.)
- **G-2, Gregory's theological reason missing: RESOLVED.** The draft now reads: "Only the Son was made man and suffered, he answered, so that He might be offered for the world." Dalton l.10380-10386 has: "It was not the Father who suffered, nor the Holy Spirit, but the Son, that He who was incarnate in the world might Himself be offered for the world." The new Agilan paragraph adds a second theological idea, also sourced: "the Father was never without wisdom or light, and so never without the Son" (Dalton l.10215-10219).
- **G-3, the Clermont hanging sentence: RESOLVED.** The sentence is cut. Brehaut now appears once, in the close.

### New or changed sentences, checked against the held files

- **"Martin of Tours had been made bishop in that church two centuries before."** The church is supported (Dalton l.22657-22659). "About" has been dropped from "two centuries". Gregory's own counts give roughly 198 to 202 years, so the figure stands. NON-BLOCKING: "about two centuries" claims only what the count shows.
- **"...so he wrote ten books of History himself..."** Supported: the laments lead to "I have undertaken" (Brehaut l.850-856), and Dalton l.22705 gives the ten books.
- **"He opened them with his creed ... and before long a king put that faith to the test."** The creed is supported (Dalton l.339-340). No source supports "before long". The creed opens Book I, Chilperic's decree is in Book V, and nothing in the held lines says when Book I was written. NON-BLOCKING: drop "before long" and keep the link without the timing.
- **"Only the Son was made man and suffered, he answered, so that He might be offered for the world, and the king must hold to 'that which Hilary and Eusebius taught,' meaning, his translator O. M. Dalton notes, Hilary of Poitiers and Eusebius of Vercelli."** The content is supported (Dalton l.10372-10386 and the note at l.26986). For access, see G2-1.
- **"...who would have torn the paper up."** Dalton l.10401-10404 reads "if he could have reached the paper ... he would have torn it to pieces". Acceptable.
- **"He held the same ground against the Arians of Spain."** Supported. Agilan was Leuvigild's envoy (Dalton l.10197). Gregory calls Arius "your founder" (Dalton l.10316). Note one difference: Chilperic merged the Persons, while Agilan made the Son lesser. "The same ground" is the Trinity, so this is fair.
- **"When their king's envoy Agilan argued at Tours that the Son was lesser than the Father, Gregory answered that the Father was never without wisdom or light, and so never without the Son."** Supported by Dalton l.10200-10219.
- **"Agilan swore he would take no blessing from a priest of Gregory's faith, though later, Gregory reports, sickness in Spain drove him to that faith."** Supported. Agilan says: "The soul shall leave the bonds of this body, or ever I receive the benediction from a priest of thy religion" (Dalton l.10353-10354). "Swore" is a fair word for that vow. The conversion is at Dalton l.10357-10360: "when he was made weak by sickness, necessity constrained him, and he was converted to our faith."
- **"Gregory does not say his stand cost him anything. The charge he later faced before the bishops at Berny, of slandering the queen, came from a count of Tours removed from office, and he cleared himself by oath, by his own account."** Supported (Dalton l.10469-10490, l.10684-10727). For relevance, see G2-2.
- **"When Chilperic was murdered, Gregory called him 'the Nero and Herod of our time.'"** Supported (Dalton l.13278). Round 1's link, Chilperic's complaint that only the bishops ruled, has been cut, so the line is now bare. See G2-2.
- **"Two centuries later the historian Paul the Deacon sent readers to..."** Supported (Foulke l.5074-5075). The round-1 non-blocking note on Paul's missing context is addressed.
- **"His translator Ernest Brehaut calls the History often the sole authority for what it tells, the passing of Roman rule and the rise of the Frankish kingdom, and warns..."** Supported (Brehaut l.65-72). The scope now matches Brehaut, which addresses round 1's note on the close. NON-BLOCKING: "His" follows a sentence whose subject is Paul the Deacon, so a listener may hear "Paul's translator". "Gregory's translator" removes the doubt.

### Several stances, checked (Mark's ruling)

**Stance 1, Chilperic: sourced, and the consequence follows from it.** Gregory refuses, and Salvius refuses. Then comes Gregory's "So the king desisted from his purpose" (Dalton l.10404-10405), attributed with "In his telling". It is told first, which fits its weight: a king's decree on the faith turned back.

**Stance 2, Agilan: sourced, real, and not filler.** It carries the brief's clearest theological sentence (the Father never without the Son), which the bar asks for. Its "what came of it" is Agilan's conversion. The draft rightly does not claim Gregory caused it. It gives Gregory's own cause, sickness and necessity in Spain. That is honest, but it means the sequel is not a consequence of Gregory's stand. NON-BLOCKING: this is acceptable as told, because the sentence claims no more than Dalton l.10357-10360. The draft must not be revised to make the conversion Gregory's doing.

### Findings

**G2-1. BLOCKING. ACCESS: a long sentence with a clause nested inside it (checklist item 4, rhythm).**

- **Sentence:** the 44-word sentence quoted above, from "Only the Son" to "Eusebius of Vercelli".
- **Problem:** It carries two ideas: the Son's suffering, and the authorities to hold to. It also has an attribution, "meaning, his translator O. M. Dalton notes,", nested inside the second idea. Read aloud, the ear loses it. `CLAUDE.md` sets a guide of about 25 words with nothing nested.
- **Fix:** split it at the idea. For example: "Only the Son was made man and suffered, he answered, so that He might be offered for the world. The king must hold to 'that which Hilary and Eusebius taught,' meaning Hilary of Poitiers and Eusebius of Vercelli." Put the Dalton credit for the identification on the card, or keep it as a short separate clause.

**G2-2. BLOCKING. SHAPE+LENGTH and CRAFT test 5 (everything relevant): padding beyond the 2:30 stretch.**

- **Passage:** paragraph 4, sentences 2 and 3: the Berny charge, and "the Nero and Herod of our time". Together they run about 44 words.
- **Problem:** At 439 words the brief is about 64 words past the 375-word stretch. These two sentences serve neither stance nor the impact.
  - The Berny charge, by the draft's own words, did not come from his stand.
  - With the bishops-ruling complaint gone, the Nero line is colour: sourced, but standing as a bare beat.
  - The honest limit Mark asked for, "Gregory does not say his stand cost him anything", stands on its own without them.
- **Fix:** cut the two sentences, or fold one clause onto the honest limit. That brings the brief to about 395 words. The rest is earned. Two stances, each with its reason and outcome, plus the recorder's impact, justify the stretch, and nothing else can go without losing sourced substance.

**NON-BLOCKING:**

- "before long" has no source (above).
- "two centuries" has lost its "about" (above).
- "His translator" has an unclear antecedent (above).
- A missed opportunity, which is not a defect: Gregory defends the Trinity against an error that merges the Persons (Chilperic) and one that ranks them (Agilan). The bar's Gregory of Nazianzus names the two errors in one sentence. One clause here would make the two stances read as one position.

### Reports

- **CRAFT: FAIL, on G2-2.**
  - Test 1, storytelling: pass. A recorder whose History records him turning back a king and arguing down an Arian envoy.
  - Test 2, flow: pass. Joining words have risen from 0.4 to 1.1 per 100, and acts carry their results ("so he wrote", "So the king desisted", "so never without the Son").
  - Test 3, no AI tells: pass. "a king put that faith to the test" is the nearest thing to a device, and it is mild.
  - Test 4, no hanging sentences: the Nero line is now weakly tied (G2-2). The close finishes on the record's authority and its limits, which is a sound close for a recorder. Model: Methodius, which weighs a thin record and moves on.
  - Test 5, everything relevant: fail (G2-2).
- **RIGOR: PASS.** Every new quote and claim is supported. Mark's source ruling is met: the brief rests on Gregory's own History, Paul the Deacon, and a modern translator named.
- **ACCESS: FAIL, on G2-1.** The tool passes: grade 9.5, reading ease 72.7. The close read fails the one 44-word nested sentence.
- **SHAPE+LENGTH: FAIL, on G2-2.** The shape is right: personal first, then stance 1 with its consequence, stance 2, the honest limit, and the impact. The length runs past the stretch with removable material.

**VERDICT, GREGORY OF TOURS: DOES NOT CLEAR.** Two small blocking fixes remain: split one sentence and cut two. Neither needs a new source. This is round 2 of the cap of 3.

---

## BENEDICT OF NURSIA, draft 2

### Round-1 blocking findings

- **B-1, the false "does not say why": RESOLVED.** The adoption now carries its stated reason, in the Franks' own words.
  - Boniface's letter is at pertz1881 l.2201-2205.
  - The Estinnes capitulary, "ad restaurandam normam regularis vitae", is at l.2449-2451.
  - The 802 Lorsch annals record both the reading and the order to correct by the Rule (l.7790-7796, l.7814-7815).
  - The Gasquet close is gone.
- **B-2, "did not claim to begin anything new": RESOLVED.** The sentence is cut. Paragraph 3 now says only what the Rule says.
- **B-3, Carloman unidentified: RESOLVED.** The draft now says "Carloman, duke of the Franks", which matches "Carlomannus dux Francorum" at l.2201-2202.
- **B-4, the wonders as a list: RESOLVED.** The links are now in the sentences:
  - "when he held them to a strict life they poisoned his wine" (Gardner l.3662-3672);
  - "then moved on to Cassino, where...";
  - "by his preaching brought the people to the faith";
  - Totila's rebuke, then "From then on ... the king was less cruel."
  The weakest join left is "Italy was at war, and when..." It is NON-BLOCKING.

### New or changed sentences, checked against the held files

- **"Nearly all we know of his life comes from Gregory's Dialogues, written in Rome about fifty years after Benedict died, from what four of his disciples told him."** Supported, as in round 1. NON-BLOCKING: round 1's notes still apply. The fifty years rests on modern dates, and "Gregory the Great" is never called pope. The Subiaco cave scene is cut, and the opening moment is now his leaving Rome (Gardner l.3411-3420). That is a sourced moment and acceptable.
- **"In Gregory's telling, the monks of a nearby house made Benedict their abbot ... The glass broke as he blessed it, and he left them."** Supported (Gardner l.3648-3700).
- **"Near Subiaco he built twelve monasteries..."** Supported. Gardner l.3843-3847 says "in the same place ... he built there twelve Abbeys". The place is the wilderness he went back to after leaving the monks. "Near Subiaco" is fair.
- **"There, Gregory says, he broke the idol, built a chapel to Martin of Tours in its temple, and by his preaching brought the people to the faith."** Supported. Gardner l.4177-4182: "by his continual preaching, he brought the people dwelling in those parts to embrace the faith of Christ."
- **"...when the Gothic king Totila came to test him, Benedict told him, 'Much wickedness do you daily commit.' From then on, Gregory says, the king was less cruel."** The quote is verbatim from the first clause of Gardner l.4472-4473. The result is Gardner l.4486-4487: "from that time forward he was nothing so cruel as before he had been". NON-BLOCKING: in Gregory, the test was the disguised guardsman Riggo, and the rebuke came when Totila arrived in person afterwards. The sentence merges the two. It stays inside Gregory's telling.
- **"In it he founds 'a school for the service of God...'"** Supported. The quote is verbatim (Gasquet l.768-770). "Founds" is a fair word for "about to institute".
- **"For more, the last chapter points to the Lives of the Fathers, the Rule of Basil of Caesarea, and the Collations, which its editor Francis Gasquet takes to be John Cassian's."** Supported (Gasquet l.4283-4286, l.283).
- **"Gregory praised the Rule as 'excellent for discretion and also eloquent for the style.'"** The quote is verbatim (Gardner l.5565-5566).
- **"By the time he wrote, the Lombards had sacked Monte Cassino, but the Rule went on."** The sack is supported (Gardner l.4657-4659). "The Rule went on" still has no named witness, as in round 1's note. NON-BLOCKING.
- **"Two centuries later Boniface wrote that Carloman, duke of the Franks, wanted to repair a church trampled for sixty or seventy years."** The content is supported (l.2201-2205): "se de aecclesiastica religione, quae iam longo tempore id est non minus quam per sexaginta vel septuaginta annos calcata et dissipata fuit, aliquid corrigere et emendare velle". Two errors are new in this draft: the time span (B2-1) and the unidentified name (B2-2).
- **"At Carloman's councils of 742 and the year after, the abbots and monks took up Benedict's Rule, the council says, to restore the norm of the regular life."** The content is supported (l.2324-2325, l.2449-2451). The editor names Carloman as the author of the Estinnes capitulary (l.2361-2364). NON-BLOCKING, two points:
  - The editor dates Estinnes "743 vel paullo post" and says the date must stay uncertain ("in incerto relinquenda", l.2375-2379). "The year after" tells his likely date flat; "soon after" claims only what he holds.
  - "the councils ... the council says" pairs a plural with a singular. It should be "the second council says".
- **"In 802, the annals of Lorsch say, Charlemagne had the monks at Aachen read it together, and ordered that whatever in the monasteries went against it be put right by it."** Supported (l.7790-7796, l.7814-7815). This close finishes the story and names its witness.

### The added consequences, checked (Mark's ruling)

- **Cassino:** the act (idol broken, chapel built) leads to the preaching, and the preaching to the people coming to the faith. Sourced in Gregory, attributed, and the result follows from the act.
- **Totila:** the rebuke leads to "less cruel". Sourced in Gregory and attributed.
- **The Rule's stance:** the Rule leads to the Frankish adoption "to restore the norm of the regular life", which leads to correction by the Rule in 802. This is sourced in period witnesses, and the causal claim is theirs.

None of these is a weak link added for space. Each states a result its witness gives. Ordered by weight, the Rule and its consequence carry most of the brief and close it, which is right.

### Findings

**B2-1. BLOCKING. RIGOR: a wrong time span.**

- **Sentence:** "Two centuries later Boniface wrote..."
- **Checked:** The sentence before it sets the time as "By the time he wrote", meaning Gregory, about 593 by Gardner's date (l.1024-1025). Boniface's letter belongs to 742 (l.2199-2205). That is about a century and a half later. It is two centuries only if counted from Benedict's death, and the sentence does not anchor it there.
- **Fix:** "A century and a half later", or simply "In 742".

**B2-2. BLOCKING. RIGOR: a common name with no identifier (checklist item 8; the same rule as round-1 B-3).**

- **Sentence:** the same one. "Boniface" is a common name: several popes are called Boniface.
- **Checked:** the held line is "Bonifacius archiepiscopus in epistola ad Zachariam papam" (l.2200-2201).
- **Fix:** "Archbishop Boniface" at first mention. The pattern allows a role where the held source gives no place.

**NON-BLOCKING:**

- "The Rule went on" has no named witness. Paul the Deacon would carry it (Foulke l.12466-12479).
- "The year after" for the Estinnes council (above).
- "the council says" after a plural (above).
- Totila's two approaches are merged (above).
- "Gregory the Great" is never called pope.
- "Italy was at war" is a bare join.
- On length: "Italy was at war" (4 words) and "which its editor Francis Gasquet takes to be John Cassian's" could move to the card, but the second places Cassian, a census thread name. With those trims the brief is about 405 words.

### Reports

- **CRAFT: PASS.**
  - Test 1, storytelling: pass. A young man leaves Rome's schools, Gregory's wonder-book carries his life, and his Rule becomes the law the Franks laid on their monasteries to restore them.
  - Test 2, flow: pass. B-4's links are now in the sentences. The joining-word count is 0.2 per 100, but the joins are carried by "when", "then", "where", "by his preaching" and "From then on", which the counter does not count. Compare Constantine, which scores none and still joins its ideas.
  - Test 3, no AI tells: pass. "The Rule is Benedict's own words." is short, but it is the fact Mark asked to be stated.
  - Test 4, no hanging sentences: pass. The close finishes the story, with its witness named. Model: John Chrysostom's close.
  - Test 5, everything relevant: pass.
- **RIGOR: FAIL, on B2-1 and B2-2.**
- **ACCESS: PASS.** The tool gives grade 8.8 and reading ease 77.9. The longest sentences are about 30 words and read in one breath.
- **SHAPE+LENGTH: PASS.** Personal first (leaving Rome, then Gregory's wonders, each with its result), then the stance (the Rule), then the impact (Gregory's praise, and the Franks' adoption with its stated reason, closing on 802). At 413 words it is about 38 words past the stretch. Most of that is the sourced impact chain Mark asked for. Only about 10 words are non-load-bearing ("Italy was at war", plus the possible move of the Gasquet clause), so the length is earned.

**VERDICT, BENEDICT OF NURSIA: DOES NOT CLEAR.** One sentence needs two word-level fixes: "Two centuries later" and "Boniface". Everything else clears. This is round 2 of the cap of 3.

---

## Summary

| Brief | Round-1 blocking findings | New blocking findings | Craft | Rigor | Access | Shape+length | Verdict |
|---|---|---|---|---|---|---|---|
| Gregory of Tours | G-1, G-2 and G-3 all resolved | G2-1 the 44-word nested sentence; G2-2 the Berny and Nero sentences are padding past the 2:30 stretch | FAIL | PASS | FAIL | FAIL | DOES NOT CLEAR |
| Benedict of Nursia | B-1, B-2, B-3 and B-4 all resolved | B2-1 "Two centuries later" is wrong (about 150 years); B2-2 "Boniface" has no identifier | PASS | FAIL | PASS | PASS | DOES NOT CLEAR |

All four remaining blocking findings are small, mechanical fixes that need no new sources. A round-3 check limited to these four would be quick.
