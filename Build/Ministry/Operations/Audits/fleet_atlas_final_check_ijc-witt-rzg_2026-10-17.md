# Atlas fleet consistency review C: ijc, witt, rzg (2026-10-17)

Reviewer: independent Opus 5.5, read-only. Inputs: `live_ijc.md`, `live_witt.md`, `live_rzg.md` and the matching compiled JSON in this folder; records at `.claude/worktrees/review-main/records/<code>/`; vendored text in `cic/texts/`; the renderer `cic-website/assets/orientation-render.mjs`; live Pleiades JSON fetched 2026-10-17.

I did not re-report these known open items:
- "this world" / "record" / "library" wording in `skim.tile`: ijc entry 40, witt OG-75, rzg entry 72.
- The `tome-that-would-not-bend` "no apostle had taught there" pivot: ijc entry 33(9).
- The Speratus hymn-count disagreement inside a figure record: witt OG-74.
- The rzg "five years apart" and "in advance" wording: rzg entries 71/73.

Severity key: **BLOCKING** means wrong, unsupported or misleading. **SHOULD-FIX** means craft, readability or a tell.

---

## 1. ijc (Imperial and Juridical Christianity)

### ijc-B1. BLOCKING: the Tome telling reverses the order of the session

- **Current text** (`ijc.story.tome-that-would-not-bend` telling, paragraph 2): "Before that cry, the Tome had been questioned in session and compared with the teaching of Cyril."
- **Evidence:**
  - In the vendored acts (`cic/texts/npnf214_seven-ecumenical-councils.xml`), the order runs as follows. The Tome was read, then the catena of Fathers (line 19985). Then "After the reading of the foregoing epistle, the most reverend bishops cried out ... Peter has spoken thus through Leo ... Leo and Cyril taught the same thing" (lines 19996-20006).
  - Only after that: "Some explanations were asked by the Illyrian bishops and the answers were found satisfactory" (lines 20007-20012).
  - So the questioning came after the cry, and the comparison with Cyril is inside the cry itself.
  - The record's `absent_detail` says "before the acclamation carried". That wording is vague, and the telling hardened it into "before that cry".
- **Proposed replacement:** "Not every bishop was satisfied. The Tome was questioned in session and compared with the teaching of Cyril."
  - This uses the `absent_detail`'s "was not unanimous" and "questioned in session and examined against Cyril", with no order claim.
  - Separately, the build thread should correct `absent_detail`'s "before the acclamation carried".

### ijc-B2. BLOCKING: the vision's army witnesses are told as fact

- **Current text** (story unit [2]): "About noon, he said, he saw a cross of light with the words "Conquer by this." His whole army saw it too."
- **Evidence:**
  - The army detail is part of what Constantine told Eusebius (`ijc.quote.vc-conquer-by-this`, VC I.28, npnf201 61203-61208: "He said that ... his whole army also ... witnessed the miracle").
  - As its own sentence, it loses the "he said" and reads as the narrator vouching for a miracle.
  - The round-1 review fixed the same fault for the vision itself ("Now 'he said'"). The army sentence was missed.
  - `ijc.story.vision-and-alliance` `use_note.not_for`: "a claim that Eusebius's account is a straightforward eyewitness report".
- **Proposed replacement:** "About noon, he said, he saw a cross of light with the words "Conquer by this." His whole army, he said, saw it too."

### ijc-B3. BLOCKING (minor): the tile has a claim no record carries

- **Current text** (tile): "Bishops who once met in secret now gathered in councils an emperor called and paid for."
- **Evidence:**
  - "Called and paid for" is supported by `ijc.force.constantine-alliance` (line 40: "Nicaea summoned at imperial initiative and expense") and `ijc.term.concilium` (line 49).
  - "Met in secret" is in no ijc record. A grep of `records/ijc` finds no such claim.
- **Proposed replacement:** "Bishops now gathered in councils an emperor summoned and paid for."
- **Note:** this is tile text, but it is not the jargon that entry 40 tracks.

### ijc-S1. SHOULD-FIX: two highlight notes are never shown

- **Current phrases:** "Bishop John" (label John Chrysostom) and "Altar of Victory".
- **Evidence:**
  - `orientation-render.mjs` lines 57-76 build a case-sensitive regex for each phrase. The regex runs only over the story units (`renderStory`, line 134) and each telling (`renderDocumentedStories`, line 179). Teasers and titles are never scanned.
  - "Bishop John" appears only in the Eutropius teaser. The telling says "The bishop, John, preached ...".
  - "Altar of Victory" (capital A) appears only in the title and teaser. The telling says "The altar of Victory stood ...".
  - My simulation of the renderer over the compiled JSON confirms that neither note is ever marked.
- **Proposed fix:**
  - Change the phrase "Bishop John" to "John", keeping the label "John Chrysostom". "John" first occurs in the Eutropius telling ("The bishop, John, preached"), and nowhere earlier in any ijc stretch.
  - Change the phrase "Altar of Victory" to "altar of Victory", or capitalize the telling's first sentence to "The Altar of Victory stood ...", which matches the title and teaser and needs no re-recording.
  - Also change the altar note. It currently repeats the telling's own first sentence nearly word for word, so the tooltip duplicates the line it sits on. Proposed: "An old altar in the Senate house at Rome. In 384 Symmachus asked the emperor to bring it back." (source: `ijc.story.altar-of-victory` text).
  - Bishop John note, trimmed to 24 words: "John Chrysostom, bishop of Constantinople from 398. He preached on Eutropius twice in 399, the first time with the man at the altar before him." (source: `ijc.source.chrysostom-eutropius` author field, and the story `text`).

### ijc-S2. SHOULD-FIX: the emperor's inward state is stated without attribution

- **Current text** (`ijc.story.emperor-penance` telling): "In his rage, Theodosius ordered a reprisal, and his soldiers massacred the crowd ..."
- **Evidence:**
  - "Rage" is Theodoret's word (npnf203 lines 16520-16526: "The emperor was fired with anger ... allowed his rage to be the minister of his vengeance").
  - The record's `absent_detail` says "Theodosius's own inward state is exactly what no source can give", and `use_note.not_for` excludes "a claim about Theodosius's inward state".
- **Proposed replacement:** "Theodoret writes that in his rage Theodosius ordered a reprisal. His soldiers massacred the crowd in the circus with no trial, cutting down innocent and guilty together. It is said, Theodoret adds, that seven thousand died."

### ijc-S3. SHOULD-FIX: Augustine's reason for the singing is changed

- **Current text** (`ijc.story.vigil-in-basilica` telling): "They sang so that the waiting need not be borne in silence."
- **Evidence:**
  - The sentence sits under "Augustine says". But Augustine gives the reason as "lest the people should pine away in the tediousness of sorrow" (`ijc.quote.augustine-vigil-hymns` text; npnf101 13765-13775).
  - The quote's `modern_rendering` reads "so that the people would not waste away in the weariness of sorrow".
  - "Silence" is not in the source.
- **Proposed replacement:** "They sang so that the people would not waste away in the weariness of sorrow."

### ijc-S4. SHOULD-FIX: a dating hedge was dropped, though the review says it is there

- **Current text:**
  - Telling: "The court was acting under an imperial law of January 386 ..."
  - Story [5]: "It acted under a law of January 386 ..."
- **Evidence:**
  - `ijc.story.vigil-in-basilica` `absent_detail` says the record follows "the now-dominant scholarly chronology", while "the vendored edition itself dates Ep. XX and the enabling law to Easter, 385".
  - `ijc_atlas_story_pass_review_round1` finding 3 says "the telling also carries that one edition dates it a year earlier". The live telling does not.
  - The tails ruling kept "hedges that qualify a specific claim". This hedge qualifies the date.
- **Proposed replacement** (telling): "The court was acting under an imperial law of January 386, which let that confession assemble for worship. The printed edition of Ambrose's letters dates the law a year earlier."

### ijc-S5. SHOULD-FIX: the letter telling ends on a jab and drops its hedge (91 words)

- **Current text** (`ijc.story.letter-that-outranked-a-council` telling, last sentence): "Julius had not attended their council, yet he wrote as though his absence were their fault."
- **Evidence:**
  - This line is a characterization, not an event, so it is the kind of add-on tail the "tails" ruling removes.
  - The telling also leaves out the record's own qualification. `absent_detail` says "whether the 'custom' Julius appeals to was as ancient or as settled as he implies is exactly what his correspondents disputed". The `not_for` excludes a settled authority in 341.
  - Story unit [3] does carry that hedge, so the card is weaker than the story.
  - At 91 words, the telling is also the shortest on the page.
- **Proposed replacement** for the last sentence: "Julius had not attended their council. Those he wrote to disputed how old and settled that custom was."

### ijc-S6. SHOULD-FIX: the opening unit names three claimants, then explains three different ones

- **Current text** (story [1]): "... the church fought over one question. Who has the last word over it? The emperor, a council and the bishop of Rome each had a claim. Rome traced its standing to the apostle Peter. Constantinople based its rank on being near the emperor. Ambrose of Milan held ..."
- **Evidence:**
  - `ijc.core.imperial-juridical` `horizon` holds two separate triads. One is the claimants: "with the emperor, with an assembled council, or with the bishop of Rome". The other is the "three strands" that contest the *ground* of authority: Roman, Constantinopolitan and Ambrosian.
  - The unit runs them together, so the reader looks for the emperor and the council among Rome, Constantinople and Ambrose.
  - The rhetorical question setup is also assistant cadence.
- **Proposed replacement:** "From 312 to 451, in Rome, Constantinople and Milan, the church fought over who had the last word: the emperor, a council or the bishop of Rome. Three answers competed over what that authority rested on. Rome traced its standing to the apostle Peter. ..." (the rest is unchanged).

### ijc-S7. SHOULD-FIX: an unclear pronoun in the Callinicum unit

- **Current text** (story [6]): "Theodosius ordered the local bishop to pay for a new one. Ambrose would not offer the sacrament until the emperor promised to change it ..."
- **Evidence:** the nearest noun for "it" is "a new one", meaning the synagogue. The record says "to amend the order" (`ijc.story.callinicum-synagogue` text).
- **Proposed replacement:** "... until the emperor promised to change the order ..."

### ijc-S8. SHOULD-FIX: two notes flatten an attribution that the records corrected

- **Current notes:**
  - Theodoret: "... He tells the fullest story of the penance, but he wrote a generation later."
  - Thessalonica: "... A massacre here in 390 led to the penance."
- **Evidence:**
  - ijc entry 35 item 4 changed `emperor-penance` "within a generation" to "decades later". The story and telling now say "Decades later". Theodoret's history runs to 429 (`ijc.source.theodoret-he` work field), well past one generation after 390.
  - Entry 35 item 3 also credits the public penance to later historians. "Led to the penance" states the penance as fact.
- **Proposed replacements:**
  - Theodoret: "A bishop whose church history covers 325 to 429. He tells the fullest story of the penance, written decades later." (20 words)
  - Thessalonica: "A city in northern Greece, known today as Thessaloniki. After a massacre here in 390, Ambrose demanded the emperor's repentance."

### ijc-S9. SHOULD-FIX: seven highlight notes run over 25 words

Counts by word: Constantine 32, the apostle Peter 26, Bishop John 27 (see S1), Theodoret 26 (see S8), Eusebius 27, Ambrose 26, Homoian 27. Proposed versions, each drawn only from the records already cited:

- **Constantine** (25): "Emperor who won at the Milvian Bridge in 312. He called the council at Nicaea in 325. He was baptized as he lay dying, in 337." (`ijc.figure.constantine`)
- **the apostle Peter** (21): "Rome held that what was given to Peter passed to each later bishop in his seat. Its standing was an inheritance." (`ijc.term.primatus`)
- **Eusebius** (25): "Bishop of Caesarea and the emperor's historian. He wrote a life of Constantine after his death. It praises its hero and leaves some things out."
- **Ambrose** (23): "Bishop of Milan from 374 until his death in 397. A former provincial governor, he was chosen bishop by the people of Milan."
- **Homoian** (25): "From homoios, meaning like. The creed that the Son is like the Father, as the scriptures say. For years it was the empire's official faith."

### ijc-S10. SHOULD-FIX: the tile's tells are separate from the known jargon item

- **Current text** (tile): "For roughly two decades, the empire's own church confessed the Son as merely like the Father, not equal to him - the official faith, not a fringe belief, and bishops who refused it went into exile."
- **Evidence:** this is a 36-word sentence with a dash aside and a double "not X" framing. The tile then ends on an aphorism: "It settled who Christ is. It did not settle where authority itself belonged."
- **Proposed replacement:** "For roughly two decades, the empire's own church confessed that the Son is like the Father. That was the official faith, and bishops who refused it went into exile." (source: `ijc.term.homoios` quick_meaning, and story [4]).
- The ending can close on the fact: "This story closes at the Council of Chalcedon in 451, which settled who Christ is."

### ijc-S11. SHOULD-FIX: the record-level text hides who asked for the new church

- **Current text** (`emperor-builds-another-basilica` telling): "He wrote to the bishops of Numidia about it, but he did not order the buildings seized ... Instead he paid for another church to be built for the Catholics ..."
- **Evidence:**
  - In the rescript itself (`cic/texts/optatus_against-the-donatists.txt` line ~7222), the Catholic bishops "ask instead for another site for yourselves in exchange, namely the Custom House". Constantine "gladly welcomed" the petition.
  - The rescript also says the Donatists had been "often warned, both by us and by our judges at our command, to give up what was not theirs".
  - The telling follows the record `text`, which leaves both out. The result makes the exchange the emperor's own idea.
- **Proposed fix:** a build-thread record correction first. Then: "The Catholic bishops asked for another site instead, and he granted it. He paid for a new church to be built there for the Catholics, once again at his own expense." This is not a card-only edit, because the record must carry it.

### ijc rigor spot-check (5 claims)

| Claim | Verified against | Result |
|---|---|---|
| Julius's quote, 341 | `ijc.quote.julius-custom` modern_rendering; npnf204 23549-23552 | Exact |
| "I dare not offer the sacrifice if you intend to be present" | `ijc.quote.ambrose-dare-not-offer`; npnf210 44180-44186 | Exact |
| "seven thousand", "no trial", "innocent and guilty together" | Theodoret V.17, npnf203 16520-16530 | Supported. See S2 for "rage" |
| Leo: "things secular stand on a different basis..."; "royal city... never an apostolic see" | npnf212 9077-9090 (chapter heading and text) | Supported |
| Tome reception order | npnf214 19985-20012 | **Wrong. See B1** |

Eutropius (npnf109 17593-17741) and the Lactantius and Milan quotes also check out.

---

## 2. witt (Lutheran Wittenberg)

### witt-B1. BLOCKING: the story credits a student with remembering Katharina's question, but it was Luther's own account

- **Current text:**
  - Story [9]: "At Luther's own table, a student remembered his wife, Katharina von Bora, asking why the old church prayed with such fervor and their own household so coldly."
  - Teaser: "A student also remembered a question from his wife, Katharina von Bora."
- **Evidence:**
  - The Table Talk text, "Of the Power of Prayer" (`cic/texts/luther_table-talk_bell1886.txt` 3141-3151), reads: "When my wife, said Luther, was sick ... At that time my wife said unto me, Sir! how is it ...".
  - Luther is the one recalling the question. The student only wrote down Luther's telling.
  - The record says "Katharina herself is remembered asking him" and "Luther's answer, as his students recorded it" (`witt.story.household-and-kate-on-prayer` text). The telling gets this right. The story and the teaser do not.
- **Proposed replacements:**
  - Story [9]: "At his table, Luther told his students that his wife, Katharina von Bora, had asked him a question. Why did the old church pray so hard, and their own household so coldly?" (this also fixes the 27-word sentence).
  - Teaser: "At table, Luther said his whole life was patience. He also told of a question from his wife, Katharina von Bora. Why did the old church pray so hard, and their own house so coldly?"

### witt-B2. BLOCKING: the "Elector" note names Frederick wherever the word appears, including 1530

- **Current note:** "Elector: Frederick of Saxony was Luther's prince, and Elector was his title. Luther said Frederick gave him a guard in 1518."
- **Evidence:**
  - The renderer marks the first "Elector" in each telling separately. My simulation marks it in three tellings:
    - `diet-of-augsburg-1530`: "It begins with John, Duke of Saxony and Elector." There the note tells the reader the Elector is Frederick. In 1530 it is John, as the record's own list says.
    - `first-german-mass-sung`: "the Elector of Saxony". Walter does not name him, and the record years are 1526.
    - `return-and-the-eight-sermons`: correct in 1522.
- **Proposed replacement:** "Elector was the title of Saxony's ruling prince, Luther's own prince. Frederick held it in 1518. By 1530 John held it." Sources: `witt.story.augsburg-before-cajetan` ("Frederick, the Elector of Saxony") and `witt.story.diet-of-augsburg-1530` ("John, Duke of Saxony and Elector").

### witt-B3. BLOCKING: "Baptism is daily" misleads

- **Current text** (story [2]): "Baptism is daily, and absolution is given as though from God himself."
- **Evidence:**
  - A plain reader hears that people were baptized every day.
  - The records mean the daily drowning of the old self. `witt.term.repentance` line 88: "baptism means 'the old Adam in us should be drowned by daily sorrow and repentance'". `witt.term.sin` line 21 says the same.
  - `witt.gravity.promise-and-sign`'s bare "Baptism is 'daily.'" cites v2 15694-15724. That passage (`luther_works-v2-selected_jacobs-spaeth1916.txt`) speaks of baptism as a comfort, not of anything daily.
- **Proposed replacement:** "Baptism means the old self is drowned by daily sorrow and repentance. Absolution is given as though from God himself."

### witt-B4. BLOCKING (minor): the tile carries a claim the pass already found unsupported

- **Current text** (tile): "... an Augustinian friar and professor at the young university of Wittenberg ..."
- **Evidence:** witt OG-73 states: "The old story's 'young' university has no record." The story dropped it, but the tile kept it. OG-75 tracks only the tile's "this world" wording.
- **Proposed replacement:** "... an Augustinian friar who taught theology at the university of Wittenberg ..." (`witt.story.letter-to-albrecht-and-theses-circulation` telling).

### witt-S1. SHOULD-FIX: archaic translation wording in tellings (decision 24)

- **No modern rendering exists for any of these.**
  - `records/witt/quote/` holds 7 quote records, none of them for these passages.
  - The wording sits only in story `text` fields, verbatim from Bell 1886, Jacobs-Spaeth and Bacon.
  - Decision 24 (System Hub Decision Log, 2026-10-02) and the pahc/syr atlas reviews hold that quotation marks carry only `modern_rendering` words.

| Telling | Current wording | Source |
|---|---|---|
| augsburg-before-cajetan | "Oh, no; where wilt thou remain in safety?" | Bell 3459 |
| worms-1521 | "Yea, they are mine"; "therefore I know not how to give it away" | Bell 3554, 3566 |
| household-and-kate-on-prayer | "Sir! how is it, that in Popedom they pray so often with great vehemence ..."; "but we, indeed, are ice cold therein, and negligent." | Bell 3147-3151 |
| return-and-the-eight-sermons | "... exercise themselves in the faith that worketh by love." | Jacobs-Spaeth v2 14687-14688 |
| first-german-mass-sung | He "kept me three weeks long at Wittenberg" | Bacon 766 |

- **Proposed fix:** either (a) Opus authors `modern_rendering`s in new quote records, per CLAUDE.md's rendering exception, and the tellings quote those; or (b) the tellings move to reported speech. Option (b) uses only wording the records support:
  - Cajetan: "Where, Cajetan asked, would he be safe then? 'Under Heaven,' Luther answered." The answer "Under Heaven" is already modern.
  - Worms: "He said they were his." Then: "God's Word, he told them, was not his word, so he did not know how to give it away."
  - Kate: "She asked him why, under the Pope, people prayed so often and so hard, while they were cold and careless in prayer." Then: "Luther answered that the devil drives his own servants on, while we are ice cold and negligent in prayer."
  - Eight sermons: end the quote at "doers and followers," then "who practice the faith that works by love."
  - Walter: see S2.
- The Albrecht, Brussels and Diet quotations read as modern enough and need no change.

### witt-S2. SHOULD-FIX: sentences over 25 words

1. Story [8], 26 words: "Johann Walter later remembered Luther keeping him three weeks at Wittenberg to set the Gospel and Epistle in German, until the first German Mass was sung."
   - It also drifts from the source. Walter was kept "to write out the notes over some of the Gospels and Epistles" (Bacon 766-768). Luther set the notes himself.
   - Proposed: "Johann Walter later remembered that Luther kept him at Wittenberg for three weeks. Walter wrote out the notes for some of the Gospels and Epistles, until the first German Mass was sung."
2. Story [9], 27 words: fixed by witt-B1.
3. Walter telling, 33 words: "He "kept me three weeks long at Wittenberg," Walter wrote, to write out the notes over some of the Gospels and Epistles, "until the first German Mass was sung in the parish church.""
   - Proposed: "Luther kept him at Wittenberg for three weeks, Walter wrote. Walter wrote out the notes for some of the Gospels and Epistles. He stayed until the first German Mass was sung in the parish church."

### witt-S3. SHOULD-FIX: a quotation cut changes its meaning

- **Current text** (household-catechism telling): 'Afterward one might "go about your work and perhaps sing a song inspired by the Ten Commandments."'
- **Evidence:** `luther_small-catechism_smith1994.txt` 557-558 reads "perhaps sing a song inspired by the Ten Commandments or your own thoughts." The cut narrows the choice.
- **Proposed replacement:** 'Afterward one might "go about your work and perhaps sing a song inspired by the Ten Commandments or your own thoughts."'

### witt-S4. SHOULD-FIX: "Bacon" appears twice without introduction

- **Current text** (Speratus telling): "Bacon notes that ..." and "Bacon's Introduction relates a tradition ..."
- **Evidence:** no participant knows who Bacon is. The Walter record calls him "a later editor, Bacon" (`witt.story.first-german-mass-sung` text).
- **Proposed replacement:** "Bacon, a later editor of Luther's hymns, notes that ..."

### witt-S5. SHOULD-FIX: the main story ends on a summary tail

- **Current text** (story [12], last two sentences): "A family of churches grew from these congregations. They still teach a catechism like this one and still sing in the language of the people."
- **Evidence:** this echoes the story's themes rather than telling an event, which is the kind of ending Mark's ruling ("remove all the add on tails that dont say anything") removes. ijc ends on Leo's letter.
- **Proposed replacement:** end on "... which drew together the catechisms and the confession given decades before."

### witt-S6. SHOULD-FIX: two highlight notes run over 25 words

- **absolution** (27 words). Proposed (23): "Forgiveness spoken to someone who has confessed sin, heard as though from God himself. Private confession was kept as a comfort, never forced." (`witt.term.confession-and-absolution`)
- **the Supper** (30 words). Proposed (25): "The meal of bread and wine. Christ's body and blood are truly present in and under them, this church taught, without explaining how."

### witt-S7. SHOULD-FIX (low): place notes lack a modern location

- **Current notes:** "Wittenberg" and "Wartburg" have no modern location. Pleiades has no entry for either.
- **Proposed fix:** if the build thread can cite one, add the modern location (Wittenberg, in today's Germany; the Wartburg, near Eisenach, Germany). Otherwise, say plainly that it is not given.

### witt rigor spot-check (5 claims)

| Claim | Verified against | Result |
|---|---|---|
| Albrecht letter quotes, 31 Oct 1517, "these my Disputations" | Jacobs-Spaeth v1 990-1096 | Exact |
| Cajetan: Revoco, three times bade rise, "Under Heaven" | Bell 3436-3460 | Supported. Archaic wording, see S1 |
| Worms: books of doctrine, "violent ... corrected", one day and one night | Bell 3540-3570 | Supported |
| Kate's question, and who remembered it | Bell 3141-3151 | **Wrong attribution in story and teaser. See B1** |
| Catechism: weekly examination, "neither food nor drink", "not to keep them in his house" | Large Catechism (Bente-Dau) 241-243, 330-337 | Supported. See S3 for the Small Catechism cut |

Also verified: Brussels ballad quotes (Bacon 1750-1795), the Walter letter (Bacon 755-768) and the eight sermons (v2 14510, 14676-14690).

---

## 3. rzg (Reformed Zurich and Geneva)

### rzg-B1. BLOCKING: the Perrinist sentence reads as if the Perrinists won

- **Current text** (story [7]): "The Perrinist party stood against the Consistory, but by 1555 it had mostly won."
- **Evidence:**
  - The nearest subject for "it" is "The Perrinist party". The natural reading therefore reverses the outcome.
  - `rzg.force.perrinist-crisis` description: "the fight was substantially resolved in Calvin's favor only by 1555". The tile says "until Geneva's Consistory won it".
- **Proposed replacement:** "The Perrinist party stood against the Consistory, but by 1555 the fight was settled mostly in Calvin's favor."

### rzg-S1. SHOULD-FIX: tellings speak as "our", unlike the story and the other worlds' cards

- **Current text:**
  - Disputation: "They met to test our founder's case against Scripture." and "the council found for our side."
  - Calvin's journey: "People who respected both our churches had begun to worry."
- **Evidence:**
  - The rzg main story and every ijc and witt telling use a third-person narrator. The ijc and witt records' own "our" was converted when their tellings were written.
  - In the Disputation telling, Zwingli is never named, so "our founder" points at no one the reader can identify. The record's `use_note.means` says "to test Zwingli's case against Scripture".
- **Proposed replacements:**
  - "They met to test Zwingli's case against Scripture."
  - "... the council ruled for the reform." (story [3]'s wording)
  - "People who respected both churches, Zurich's and Geneva's, had begun to worry."

### rzg-S2. SHOULD-FIX: a highlight note narrates the gazetteer

- **Current note** (Strasbourg): "Today's Strasbourg, in France. Pleiades lists it as the ancient Roman outpost of Argentorate. Calvin was exiled there from 1538 to 1541."
- **Evidence:** "Pleiades lists it" is process wording. The Zurich and Geneva notes use "In ancient times a town called ... stood there". Pleiades 108754 confirms "Argentorate (modern Strasbourg, France) ... a Roman outpost".
- **Proposed replacement:** "Today's Strasbourg, in France. In ancient times a Roman outpost called Argentorate stood there. Calvin was exiled there from 1538 to 1541."

### rzg-S3. SHOULD-FIX (low): Savoy is tagged as a place with no location

- **Current note:** "Savoy: Geneva broke politically from Savoy and the Prince-Bishop in 1536." It has kind `place` and no URL or modern location.
- **Proposed fix:** change the kind to `term`, since it names a ruling power rather than a site, and keep the record-supported sentence. Or add a sourced modern location.

### rzg-S4. SHOULD-FIX (low): the tellings are choppy

- **Evidence:**
  - The rzg tellings average 10.8 words a sentence, against 15.0 for ijc and 13.6 for witt. That is below the ~12-20 range in CLAUDE.md.
  - The Myconius telling is the clearest case: "The muster was disorganized. Five thousand had been summoned, and fewer than four thousand five hundred came. Myconius watched Zwingli ride out in the rear. He felt a sudden pain of heart."
- **Proposed replacement:** "The muster was disorganized: five thousand had been summoned, and fewer than four thousand five hundred came. As Myconius watched Zwingli ride out in the rear, he felt a sudden pain of heart." (Bracketed colon; all wording from the record.)

### rzg-S5. SHOULD-FIX (low): "as he fell"

- **Current text** (story [5] and telling): "said as he fell".
- **Evidence:** Myconius (`zwingli_latin-works-correspondence-vol1_jackson1912.txt` 1586-1593): "a fourth time he was struck ... and, fallen upon his knees, said". He spoke after he had fallen to his knees.
- **Proposed replacement:**
  - Telling: "On his knees, he was reported to have said, ..."
  - Story: "Zwingli was reported to have said, after he fell, ..."

### rzg-S6. SHOULD-FIX (low): the Disputation teaser runs 40 words

- **Current text:** the Disputation teaser has three sentences and repeats "day" three times. It is the longest teaser in the three pages; the others run 20-35 words.
- **Proposed replacement:** "Enemies of the new preaching mocked the gathering as a "tinker's day." A schoolmaster, Erhart Hegenwald, sat through it and wrote it down. The council ruled for the reform."

### Card count (item 6)

- `records/rzg/story/` holds exactly three story records: `first-zurich-disputation`, `myconius-account-of-zwinglis-death` and `calvins-journey-to-zurich`. All three are on the card, in date order.
- Under the pass's method (card stories chosen only from existing story records), **no more card stories are possible**. rzg entry 70 already lists the cut episodes and the records that hold them.
- Reaching 6-10 cards would need new story records, built under Doc_09 discipline by the build thread. That is a build decision, not an Atlas-pass fix.
- Likely candidates, each already held as force or witness records:
  - the 1522 Lenten fast;
  - the 1525 first Swiss Brethren baptisms (`rzg.force.anabaptist-schism`);
  - the 1529 Marburg Colloquy;
  - Calvin's 1538 exile and 1541 recall;
  - the Perrinist crisis.

### rzg rigor spot-check (5 claims)

| Claim | Verified against | Result |
|---|---|---|
| 29 Jan 1523, six hundred, "tinker's day", Hegenwald quote | `zwingli_selected-works_jackson1901.txt` 1547, 1612-1629, 1719 | Supported. The editor also gives 23 Jan once, and the record discloses that |
| Zwingli's last words | `rzg.quote.zwinglis-last-words` modern_rendering; Myconius 1590-1593 | Exact |
| Muster numbers, heart found whole (as reported) | Myconius 1566-1613 | Supported, and the hedge is kept |
| 21 Jan 1525, Grebel baptized Blaurock at Manz's house | `rzg.force.anabaptist-schism` line 29 | Supported |
| Calvin's 1549 journey with Farel, "indefatigable soldier of Christ", "faithful record", subscription | `calvin-zurich-pastors_consensus-tigurinus-...beveridge1844.txt` 84-146 | Supported. The letter also names Neuchâtel's colleagues; leaving them out does not mislead |

Bullinger's 44 years (`rzg.figure.bullinger`, 1531-1575) and Calvin's 1536/1538/1541 (`rzg.force.genevas-1526-...`) also check.

---

## 4. Consistency across the three pages

| Check | ijc | witt | rzg |
|---|---|---|---|
| Story length (600-700 words) | 623 | 645 | 639 |
| Card count (6-10) | 10 of 11 records | 10 of 12 records | 3 of 3 records (see item 6) |
| Cards in date order | Yes | Yes | Yes |
| Tellings of ~120-250 words | Three short: dream 99, letter 91, altar 116 | Speratus 92 (ruled not padded) | All in range |
| Narrator voice in tellings | Third person | Third person | **First-person "our" (rzg-S1)** |
| Miracles and visions as testimony | Army sentence slips (ijc-B2) | Speratus as tradition, ballad's own voice | Heart "as reported" |
| Quotes in modern rendering | All match `modern_rendering` | **Archaic, no renderings (witt-S1)** | Last words match. The Hegenwald and Calvin quotes are old translation but readable |
| Main story ending | Last event (Leo's letter) | Summary tail (witt-S5) | Descendant traditions (a concrete claim) |
| Highlight notes over 25 words | 7 | 2 | 0 |
| Highlights never shown | 2 (ijc-S1) | 0 | 0 |

ijc-S5's proposed fix raises the letter telling over 100 words with a real hedge. The dream telling is short because its record is short, and it should not be padded.

Readability:
- Story averages are ijc 12.0, witt 13.2 and rzg 12.8. Telling averages are ijc 15.0, witt 13.6 and rzg 10.8.
- Sentences over 25 words in participant text, outside the tile:
  - witt story [8] (26)
  - witt story [9] (27)
  - witt Walter telling (33)
  - The ijc tile has one more (36).
- No other sentence on the three pages, quotations included, runs over 25 words. The Julius question is exactly 25.
- No parentheses or dash asides were found in the story, tellings, teasers or notes. The only dash is in the ijc tile (ijc-S10).
