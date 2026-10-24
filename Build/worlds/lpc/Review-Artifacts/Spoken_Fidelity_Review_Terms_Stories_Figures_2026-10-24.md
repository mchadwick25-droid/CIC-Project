# Source-fidelity review B: lpc spoken fields

Reviewer: Claude Opus 5.5 (claude-opus-5-5), independent pass, 2026-10-24.
Scope: the 57 fields listed in `spoken_B.txt`. Every sentence was read against the record's own `sources[].locus`. I read the cited lines myself in `cic/texts/`. No repo file was changed.

Abbreviations used for file paths:
- ANF5 = `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`
- POSS = `cic/texts/possidius_vita-augustini_weiskotten1919.txt`
- NPNF101 = `cic/texts/npnf101_augustine-confessions-letters.xml`
- NPNF103 = `cic/texts/npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml`
- NPNF104 = `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml`
- NPNF105 = `cic/texts/npnf105_augustine-anti-pelagian-writings.xml`
- NPNF107 = `cic/texts/npnf107_augustine-homilies-john-soliloquies.xml`
- HARTEL-EP = `cic/texts/cyprian_epistulae-lat_hartel1871-csel3-tei.txt`
- HARTEL-UN = `cic/texts/cyprian_de-unitate-ecclesiae-catholicae-lat_hartel1868-csel3-tei.txt`

Proposed texts make no new claims. Each one keeps only what the cited lines say.

---

## Figures

### lpc.figure.augustine — bridge_line — P2
- **Sentence:** "seized by our own acclaim for the office twice over his own reluctance"
- **Problem:** Loose paraphrase. Augustine was seized only once, to be made presbyter (Vita IV). The second time was the episcopate (Vita VIII). The people clamoured for it and he refused, because his own bishop was still alive. Then he was "convinced", not seized. These were two offices, not "the office" twice.
- **Evidence:** POSS:1808-1818 (Ch. IV: "laid hands on him… while he wept freely"); POSS:2131-2140 (Ch. VIII: "all who heard rejoiced and clamored… the presbyter refused to accept the episcopate contrary to the custom of the Church, since his bishop was still living. However, when they had convinced him").
- **Proposed:** "our bishop at Hippo, seized by the people and made a presbyter while he wept, then pressed into the bishop's office over his own refusal; who spent his last days weeping over psalms of penitence while an army lay outside the walls"

### lpc.figure.celerinus — bridge_line — P1
- **Sentence:** "a confessor who did not write about his own suffering, but about his sister's"
- **Problem:** Unsupported, and contradicted by the letter. Celerinus does write about himself. He mentions his own "purple" (bloodied) confession. He also describes his own tears, sackcloth and ashes. Calling the sister's fall "suffering" also shifts the meaning: the letter grieves her sacrifice, her "(spiritual) death".
- **Evidence:** ANF5:30556-30560 ("when I also was in such a purple… confession"); ANF5:30568-30580 ("weeping day and night, have spent the days in tears, in sackcloth, and ashes").
- **Proposed:** "a confessor who wrote to another confessor in prison, weeping for his sister who had sacrificed, and asked him to help restore her"

### lpc.figure.cyprian — bridge_line — P2
- **Sentence:** "who taught us to care for our enemies during a plague"
- **Problem:** Loose paraphrase. Pontius reports the teaching as "loved even his enemies… pray for the salvation of those that persecute him". The relief went "to all". The record's own linked story says Pontius does not say whether enemies were among those helped (`lpc.story.the-plague-and-the-enemies` absent_detail). "Care for" leans toward practical help that the source does not report.
- **Evidence:** ANF5:27960-27966 (Pontius §9).
- **Proposed:** "our bishop, chosen while still a neophyte over his own reluctance, who taught us during a plague to love even our enemies, and was executed under Valerian"

### lpc.figure.lucian — bridge_line — P1
- **Sentence:** "granting peace to three women he had never met in person"
- **Problem:** Invented, and contradicted by the source. Celerinus tells Lucian that Numeria and Candida are "our sisters whom you also knew well". Lucian's reply names and grants peace only to Numeria and Candida. It does not name Celerinus's sister. So "three" goes beyond the reply. "Never met" is the opposite of what the letter says.
- **Evidence:** ANF5:30588-30590 (Ep. XX: "our sisters whom you also knew well—that is, Numeria and Candida"); ANF5:30711-30716 (Ep. XXI: "greet Numeria and Candida, who (shall have peace)"); ANF5:30704-30708 ("ordered to be put to death by hunger and thirst, and were shut up in two cells").
- **Proposed:** "a confessor who answered from a cell where he and others had been sentenced to die of hunger and thirst, and granted peace to Numeria and Candida, women he knew well"

### lpc.figure.pontius — bridge_line — P1
- **Sentence:** "the account by which most of what we remember of Cyprian's own life reaches us"
- **Problem:** The claim is wider than its source. Most of what survives about Cyprian's life as bishop comes from his own letters and treatises, not from Pontius. The record's own body says only that his early life beyond the conversion date reaches us through Pontius (`lpc.figure.cyprian` body). A smaller point: "stayed with him through exile" stretches Pontius's own words. He says he was chosen "to a voluntary exile" with Cyprian. He does not say for how long he stayed.
- **Evidence:** ANF5:28055-28058 (Pontius §12: "chosen me among his household companions to a voluntary exile"); the whole Epistles corpus in ANF5 (div3 iv.iv.*).
- **Proposed:** "our bishop's own deacon, who went with him into exile and, after the execution, wrote the account of his life and death"

### lpc.figure.possidius — bridge_line — P2
- **Sentence:** "who had been Augustine's friend for forty years"
- **Problem:** Loose. Possidius says "almost forty years".
- **Evidence:** POSS:5058-5060 ("for almost forty years").
- **Proposed:** "the bishop of Calama who had been Augustine's friend for almost forty years, and who stood by him and prayed as he died"

### lpc.figure.numidicus — bridge_line — clean (advisory note only)
Every clause is supported by ANF5:32100-32111. One advisory note, not counted as a finding: "did not want to have survived" rests on *remansit inuitus*. Hartel prints that reading (HARTEL-EP:5676). The ANF footnote at ANF5:32108 records the variant "unconquered" (*inuictus*, Hartel's apparatus "inaictus Bv"). The reading follows the critical text, so no change is needed. The variant could be disclosed in the record body.

---

## Quotes (modern_rendering: meaning only, not style)

### lpc.quote.ancient-venom-against-my-episcopate — modern_rendering — P2
- **Sentence:** "which means against your vote and against God's judgment"
- **Problem:** The rendering adds a meaning. "Vote" brings in a ballot. This world's own records name that as a distortion: `lpc.term.suffrage` gives distortion_risk high ("hears as a modern franchise"), and `lpc.story.election-of-cyprian` modern_contrast says "A modern listener may hear… a vote… We had none of that." The source word is "suffrage".
- **Evidence:** ANF5:32372-32374.
- **Proposed (minimal, meaning only):** replace "against your vote" with "against your suffrage". The Opus rendering is left otherwise as it is.

### Clean
- lpc.quote.bishop-of-bishops — modern_rendering: matches ANF5:56871-56880 in meaning.
- lpc.quote.clamour-and-tears — modern_rendering: matches POSS:1808-1818 in meaning ("laid hands on" → "seized" keeps the sense).
- lpc.quote.longing-expectation-is-a-prayer-for-me — modern_rendering: matches `cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml`:9398.
- lpc.quote.shepherd-wounded-in-the-flock — modern_rendering: matches ANF5:43725-43729, and the ellipsis is kept.

---

## Stories (tellable_as, checked against text, tier and claim_guards)

### lpc.story.celerinus-writes-to-lucian — tellable_as — P1
- **Sentence:** "How two confessors, not our bishop, decided who could come back to us"
- **Problem 1:** A contested point is stated as settled. Whether the confessors' peace actually decided anything is the confessor-authority tension itself. The record's own claim_guard says "we must not resolve the confessor-authority tension by presenting the confessors as either usurpers or heroes." "Decided" resolves it in the confessors' favour.
- **Problem 2:** The detail is wrong. The women were at Rome, not in Carthage, so "come back to us" is not true to the source. At Rome the clergy had ordered them "to remain as they are, until a bishop should be appointed."
- **Evidence:** ANF5:30533 (ANF Argument: "His Lapsed Sisters at Rome"). The letter body places them at Rome: ANF5:30620-30626 (Candida at the Tria Fata, on the way up to the Capitol) and ANF5:30648-30650 (the sisters "went down to the harbour… and took them up into the city"). ANF5:30632-30634 gives the clergy's order to wait for a bishop.
- **Proposed:** "How one confessor asked another, not a bishop, to grant peace to women who had fallen"

### lpc.story.hundred-thousand-sesterces — tellable_as — P1
- **Sentence:** "to ransom people most of us had never met"
- **Problem:** Invented detail. Ep. LIX never says whether Carthage knew the captives. Cyprian calls them "our brethren and sisters" and asks each reader to imagine "his sons are there."
- **Evidence:** ANF5:36011-36015; ANF5:36046-36050; ANF5:36082-36086.
- **Proposed:** "How we sent a hundred thousand sesterces to ransom our captive brethren"

### lpc.story.numidicus — tellable_as — P1
- **Sentence:** "How we ordained a man on the strength of what he had endured"
- **Problem:** The claim is wider than the letter's own body. Cyprian writes that "Numidicus the presbyter should be appointed in the number of Carthaginian presbyters". In Hartel's Latin this is *Numidicus presbyter adscribatur presbyterorum Carthaginensium numero*. The letter calls him a presbyter already and enrols him in the Carthaginian presbyterate. "Ordained" comes from the ANF Argument and the manuscript incipits, not from Cyprian's text. The record's sibling (`lpc.story.hundred-thousand-sesterces`) explicitly bars resting on the ANF Argument. "We" also widens the act: Cyprian says he himself was "admonished and instructed by divine condescension." The "had not wanted to survive" clause follows Hartel's *inuitus*; see the advisory note under the Numidicus figure.
- **Evidence:** ANF5:32088-32091 (ANF Argument "Ordained by Him Presbyter"); ANF5:32095-32098 (body); HARTEL-EP:5644-5646; HARTEL-EP:5658 (incipit variants).
- **Proposed:** "How our bishop added to our presbyters a confessor who had not wanted to survive"

### lpc.story.the-plague-and-the-enemies — tellable_as — P1
- **Sentence:** "teaching us to care for the very people persecuting us"
- **Problem:** Unsupported, and it contradicts the record's own absent_detail ("Whether the persecutors themselves were among those helped is not something Pontius says"). Pontius reports a teaching to love enemies and *pray for* persecutors, and relief given "to all men". Neither Pontius nor the story says anyone was persecuting the church during the plague.
- **Evidence:** ANF5:27960-27966; ANF5:27980-27985 (§10).
- **Proposed:** "How our bishop met a plague by teaching us to love even our enemies, and to help everyone, not only our own"

### lpc.story.the-psalms-on-the-wall — tellable_as — P1
- **Sentence:** "the one who spent his life adjudicating others' penitence"
- **Problem:** Unsupported, and wider than the source. Possidius never shows Augustine administering or judging other people's penance. What Possidius records is Augustine's *teaching*: even exemplary Christians and priests should not die without fitting repentance. "His life" is also too wide, since his clerical life was "almost forty" of seventy-six years.
- **Evidence:** POSS:4919-4925.
- **Proposed:** "How the man who taught that even good Christians must repent before death did it himself"

### lpc.story.the-death-of-cyprian — tellable_as — P2
- **Sentence:** "our first great bishop's death"
- **Problem:** Loose. "First" can be heard as Carthage's first bishop, which Cyprian was not (his predecessor Donatus is named in the corpus). Tier 1 and the claim_guards are otherwise respected: the cloth discrepancy is flagged as a difference.
- **Evidence:** the record's own sources; ANF5 Epistles corpus (Cyprian is not the first bishop of Carthage).
- **Proposed:** "How two early texts tell the death of our great bishop Cyprian, and where they differ"

### lpc.story.election-of-cyprian — tellable_as — clean
Supported by ANF5:27816-27830 (Pontius §5: "judgment of God and the favour of the people… a neophyte… he humbly withdrew… thinking himself unworthy").

---

## Terms

### lpc.term.bishop-of-bishops
- **plain_meaning — P2.** Sentence: "Each bishop judges for himself, and answers for it elsewhere." Problem: "elsewhere" is vague, and a listener could hear another bishop or see. The source names Christ. Evidence: ANF5:56878-56882 ("let us all wait for the judgment of our Lord Jesus Christ, who is the only one that has the power… of judging us"). Proposed: "For us, this is a simple rule, said at the start of a council: no bishop stands over another. Each bishop judges for himself. Only Christ judges him."
- **quick_meaning — P2.** Same sentence and problem. Proposed: "For us, no bishop stands over the others. Each one judges for himself, and answers to Christ."

### lpc.term.certificates-letters-of-peace
- **plain_meaning — P1.** Sentence: "He names one lapsed person and asks that they be let back in." Problem: this states Cyprian's demanded form as if it were the practice. Cyprian says that was often *not* the practice: certificates read "Let such a one be received to communion along with his friends." He also says certificates were given to the lapsed person, who held them ("the man who receives the certificate"). The only surviving certificate does not ask; it says "we have granted peace" to all. "Asks" takes Cyprian's side in the confessor-authority tension, which is a contested point stated as settled. Evidence: ANF5:29936-29948 (Ep. X.4); ANF5:30383-30390 (Ep. XVI). Proposed: "A certificate is a letter from a confessor, given to a lapsed person. It asks for peace, or says peace is granted. Cyprian wanted each one to name the person. Many named one person 'with his friends.'"
- **quick_meaning — P1.** Sentence: "a letter a confessor sends the bishop. It asks that one named lapsed person be let back into communion." The problem and evidence are the same. Proposed: "For us, a certificate is a confessor's letter for a lapsed person. It asks for peace, or grants it. Who decides is what we argued over."

### lpc.term.communion
- **plain_meaning — P1.** Sentence: "Its hardest test is that it survives sharp disagreement between the people who hold it." Problem: a contested point is stated as settled. The 256 preface states Cyprian's *principle*: no one is rejected from communion for differing. The vendored corpus also holds Firmilian's charge that Stephen denied "peace and communion" to the African envoys over this very dispute. The record's own rating is Widely Accepted synthesis, not a fact. Evidence: ANF5:56869-56871; ANF5:40046-40054 (Ep. LXXIV). Proposed: "For us, communion is a formal standing within the one body. You can lose it, and be given it back. At the council of 256, Cyprian said no one would be put out of it for thinking differently."
- **quick_meaning — P2.** Sentence: "It can survive sharp disagreement between the people who hold it." "Can" softens the claim, but it is still unattributed. Proposed: "For us, communion is a real standing inside the one body. You can lose it, and be given it back. Cyprian held that it should survive sharp disagreement."

### lpc.term.compel-them-to-come-in
- **plain_meaning — P2.** Sentence: "A Christian ruler may rightly use force…" Problem: this is Augustine's argument, given in the world's "for us" voice with "rightly". The record's own guard says the entry "does not endorse or condemn the position", and nothing in Cyprian's phase corresponds to it. Evidence: NPNF101:38247 (Letter XCIII: "originally my opinion was, that no one should be coerced"); NPNF104:19609 (Letter 185, the parable). Proposed: "This is a late argument of Augustine's, against his own earlier view. He argued that a Christian ruler may use force to bring a separated group back into the one communion."
- **quick_meaning — P2.** The same attribution is missing. Proposed: "For us, this is Augustine's late argument. A Christian ruler may use force to bring a separated group back into the one communion."

### lpc.term.confessor
- **plain_meaning — P2.** Sentence: "That standing… is the strongest rival we have to a bishop's own authority." Problem: "strongest" is a superlative from the build's analysis, not from the source. The record's own divergence_note also limits the term to Cyprian's phase, but "we have" is present tense for the whole world. Evidence: ANF5:30383-30390 (Ep. XVI, confessors granting peace); ANF5:29900-29905 (Ep. X, Cyprian asking them to reserve petitions for the bishops). Proposed: "For us, a confessor is one who was interrogated for the Name, did not deny it, and lived. In Cyprian's time, that standing could rival a bishop's own authority."
- **quick_meaning — P2.** Same problem. Proposed: "For us, a confessor is someone who was asked to deny the faith, did not, and lived. In Cyprian's time, that standing could rival a bishop."

### lpc.term.grace
- **plain_meaning — P2.** Problem: the locus is missing. The source is cited only as "the anti-Pelagian corpus", with no passage. The content is supportable. Evidence and proposed locus: NPNF105:10082 (*On the Proceedings of Pelagius* 34: "we certainly do not deserve by any faith that we should have faith itself… 'His mercy has prevented us'"). The text stays as it is; add the locus.
- **quick_meaning — P2.** Same missing locus. Text stays as it is.

### lpc.term.heresy
- **plain_meaning — P1.** Sentence: "this word does not ask which belief is wrong. It asks one question: does a baptism given outside our one church count at all?" Problem: this is contradicted by the record's own cited source, the rebaptism correspondence. There Cyprian's case against heretical baptism rests on wrong belief: "Does Marcion then maintain the Trinity?… Widely different is the faith with Marcion." Evidence: ANF5:38529-38548 (Ep. LXXII.5, to Jubaianus). Proposed: "For us, this word raises one sharp question: does a baptism given outside our one church count at all? We answer it twice, in two different ways, a century apart."
- **quick_meaning — P1.** Sentence: "this word does not ask which belief is wrong." The problem and evidence are the same. Proposed: "For us, the sharpest question this word raises is whether a baptism given outside our one church counts at all."

### lpc.term.libellatici-sacrificati
- **plain_meaning — P2.** Sentence: "Both are outside now, and both ask to come back." Problem: this flattens the source. Cyprian's council decided that certificate-holders "should in the meantime be admitted", while those who sacrificed were to be helped at death. Evidence: ANF5:33780-33783 (Ep. LI.17); HARTEL-EP:7979. Proposed: "Not everyone who failed, failed the same way, and we knew it. One person paid money and got a paper. Another stood at the altar and did the deed. Both fell. Cyprian did not treat them the same."
- **quick_meaning — clean** (ANF5:33700-33710, Ep. LI.14: "I pay a price for this purpose").

### lpc.term.libelli
- **plain_meaning — P1.** Sentence: "Rome did not ask anyone to renounce Christ in writing." Problem: no cited locus supports this, and Cyprian's own text frames it the other way. He calls the certificate "that profession of one who denies… the testimony of a Christian disowning what he had been." The other two sentences are supported: "He says that he has done what another has actually committed," and Ep. LI.14 has "I pay a price". Evidence: ANF5:44357-44363 (De Lapsis 27); ANF5:33700-33710. Proposed: "Rome ordered a sacrifice. Some people paid for a paper saying they had made it, without sacrificing at all. Cyprian called that paper a denial: their hands were clean, but their conscience was not."
- **quick_meaning — P1.** Sentence: "papers given to people who obeyed the order to sacrifice." Problem: this conflicts with the record's own plain_meaning and with Cyprian. In the cited loci, libelli are the papers obtained *without* sacrificing. Evidence: as above. Proposed: "The libelli were papers saying a person had sacrificed. Some people bought one without sacrificing. Holding that paper made a person one of the lapsed."

### lpc.term.plenary-council
- **plain_meaning — P2.** Sentence: "even the widest council can later be corrected, because the church learns." Problem: loose. Augustine gives the reason as experience bringing hidden things to light. Evidence: NPNF104:11303-11304 (On Baptism II.3: "when, by some actual experiment, things are brought to light which were before concealed"). Proposed: "Two ideas sit in one sentence here. A small council yields to a wider one -- that is a hierarchy. But even the widest council can later be corrected, when experience brings to light what was hidden."
- **quick_meaning — clean.**

### lpc.term.preaching
- **plain_meaning — P1.** Sentence: "You are baptized, so you are in the room. Week by week…" Problem: this is contradicted by the record's own cited source. Augustine's Tractates on John speak directly to catechumens in the congregation. Nothing cited says "week by week". Evidence: NPNF107:2280-2281 (Tractate X: "we exhort you to prepare yourselves, such of you as are catechumens"); NPNF107:2319-2320 and 2350 (Tractate XI). Proposed: "You are in the room, baptized or still learning. Again and again, the same voice works on you. It is not a lecture and not a show. It is the man in charge of you, telling you to your face what he thinks you need."
- **quick_meaning — P1.** Sentence: "preaching is the weekly talk to those already baptized. It is how nearly all we hold reaches an ordinary believer." The problem and evidence are the same. "Nearly all" is also the build's own synthesis. Proposed: "For us, preaching is the regular talk to the gathered church, baptized and catechumens alike. It is the main way what we hold reaches an ordinary believer."

### lpc.term.reconciliation-penitential-discipline
- **plain_meaning — P2.** Problem: the locus is missing ("the Epistles carry the process in operation"). The content is supported. Proposed locus: ANF5:29768-29773 (Ep. IX.2: "do penance for a set time, and according to the rules of discipline come to public confession, and by imposition of the hand of the bishop and clergy receive the right of communion"). The text stays as it is.
- **quick_meaning — P2.** Same missing locus. Text stays as it is.

### lpc.term.schism
- **plain_meaning — P2.** Problem: the locus is missing ("the general treatise"). The content is supported. Proposed locus: ANF5:42694-42701 (De Unitate 17: "separates himself from the company of His clergy and people… he dares to set up another altar"). The text stays as it is.
- **quick_meaning — P2.** Sentence: "a real split inside the one body of bishops, over belief or over practice." Problem: loose. In the cited De Unitate, schism separates a person from "His clergy and people", not just from the bishops. "Over belief" also blurs the heresy/schism line, which the record itself flags as contested. Proposed: "For us, schism means a split in the one church: someone leaves its clergy and people and sets up another altar. It is a tear, not a mere argument."

### lpc.term.suffrage
- **plain_meaning — P2.** Sentence: "Cyprian's own word for what put him in office was suffrage." Problem: loose. Cyprian pairs the two: "your suffrage and God's judgment". Dropping the second half loses meaning that the world itself holds onto. Evidence: ANF5:32372-32374. Proposed: "Cyprian named two things that put him in office: our suffrage, and God's judgment. A rival group opposed him, but the people chose him anyway."
- **quick_meaning — P2.** Sentence: "It often goes against his own wishes." Problem: "often" is wider than the sources, which show three cases. Pontius reports Cyprian withdrawing (ANF5:27826-27829), and Possidius reports Augustine twice (POSS:1808-1818, 2131-2140). Proposed: "For us, suffrage is the voice of the people that puts a man into office. It can go against his own wishes."

### lpc.term.the-flock
- **plain_meaning — P1.** Sentence: "He preaches to them, baptizes them, and buries them." Problem: invented detail. No cited locus has the bishop burying his people. The only burial passage in Cyprian's volume is a letter from the Roman clergy about whose duty burial is (ANF5:28877). A second, P2 problem: "his flock can stand in front of his seat and refuse to leave" is supported only by Augustine's Letter CXXVI (NPNF101:44495-44506, "the crowd having gathered in front of the steps, and persisting… with terrible and incessant clamour"), which this record does not cite. Proposed: "A bishop, for us, is not an officer of some wider institution, dropped into a posting. He is given a people. He preaches to them and baptizes them, and when they fail it is not a problem he manages but a wound he carries. The charge runs both ways: he answers for his flock, and his flock can stand in front of his seat and refuse to leave until he hears them." Also add Letter CXXVI to sources.
- **quick_meaning — P2.** Sentence: "by name, week after week, in one place." Problem: "by name" and "week after week" are not in the cited loci. Ep. LIV.14 gives "a portion of the flock" assigned to each pastor, who answers to the Lord (ANF5:35009). Proposed: "For us, the flock is not the church in general. It is the particular people one bishop is given, in one place. He answers for them, and they can hold him to it."

### lpc.term.the-one-episcopate
- **plain_meaning — P1.** Sentence: "Each bishop holds the whole of it in his own place, not a share of it." Problem: this contradicts the cited text. Cyprian says "each *part* of which is held by each one for the whole" (*cuius a singulis in solidum pars tenetur*). "Not a share" denies the *pars*. How to read *in solidum* is an interpretive question; the entry should not settle it against the wording. The locus is also missing (no chapter given). Evidence: ANF5:42290-42291 (De Unitate 5); HARTEL-UN:339. Proposed: "For us, the episcopate is one undivided office. Each bishop holds his part of it, and holds it for the whole." Add locus "De Unitate 5".
- **quick_meaning — P1.** Sentence: "Each bishop holds the whole of it, not just a part." The problem and evidence are the same. Proposed: "For us, the episcopate is one office, shared by every bishop. Each one holds his part on behalf of the whole."

### Clean terms
- lpc.term.catechesis — plain_meaning, quick_meaning. Supported by NPNF103:30470-30476 (*On the Creed: A Sermon to the Catechumens*: "that are about to give back with your tongue").
- lpc.term.the-lapsed — plain_meaning, quick_meaning. Supported by ANF5:44357-44365 (De Lapsis 27: "He says that he has done what another has actually committed… he has obeyed his edict") and ANF5:33700-33710.
- lpc.term.the-people — plain_meaning, quick_meaning. Supported by ANF5:32372-32374 and NPNF101:44495-44506 (Letter CXXVI).
- lpc.term.libellatici-sacrificati — quick_meaning.
- lpc.term.plenary-council — quick_meaning.

---

## Outside scope, seen in passing (not counted)
These are in non-scoped fields of the same records. They are of the same kind as the findings above and worth a follow-up.
1. **lpc.story.celerinus-writes-to-lucian `text`:** "She was alive, in Carthage". This is contradicted by the source, which places the women at Rome (ANF5:30533 Argument; ANF5:30620-30626, 30648-30650). It is the same class of invented detail as today's earlier finding.
2. **lpc.figure.lucian `dates.display`:** says he granted peace "to Celerinus's own sister". The reply names only Numeria and Candida (ANF5:30711-30716).
3. **lpc.figure.numidicus `dates.display`:** "ordained presbyter by Cyprian". This has the same issue as the Numidicus tellable_as (ANF5:32095-32098; HARTEL-EP:5644-5646).
4. **lpc.story.hundred-thousand-sesterces `text`:** "Numidian towns". Numidia appears only in the ANF Argument (ANF5:36000-36003), which this record's own tier note says not to rely on. The letter body does not name the region.

---

## Fields checked clean (14)
1. lpc.figure.numidicus — bridge_line (advisory note on *inuitus* only)
2. lpc.quote.bishop-of-bishops — modern_rendering
3. lpc.quote.clamour-and-tears — modern_rendering
4. lpc.quote.longing-expectation-is-a-prayer-for-me — modern_rendering
5. lpc.quote.shepherd-wounded-in-the-flock — modern_rendering
6. lpc.story.election-of-cyprian — tellable_as
7. lpc.term.catechesis — plain_meaning
8. lpc.term.catechesis — quick_meaning
9. lpc.term.libellatici-sacrificati — quick_meaning
10. lpc.term.plenary-council — quick_meaning
11. lpc.term.the-lapsed — plain_meaning
12. lpc.term.the-lapsed — quick_meaning
13. lpc.term.the-people — plain_meaning
14. lpc.term.the-people — quick_meaning

## Counts
- Fields in scope: 57
- **P1: 20** — figures 3 (celerinus, lucian, pontius); stories 5 (celerinus-writes-to-lucian, hundred-thousand-sesterces, numidicus, the-plague-and-the-enemies, the-psalms-on-the-wall); terms 12 (certificates ×2, communion plain, heresy ×2, libelli ×2, preaching ×2, the-flock plain, the-one-episcopate ×2)
- **P2: 23** — figures 3 (augustine, cyprian, possidius); quote 1 (ancient-venom); story 1 (the-death-of-cyprian); terms 18
- **Clean: 14**
- 20 + 23 + 14 = 57
