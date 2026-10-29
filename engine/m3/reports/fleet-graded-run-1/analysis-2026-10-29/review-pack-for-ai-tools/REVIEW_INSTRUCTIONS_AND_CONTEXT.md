# Independent review pack: "Church in Conversation" fleet test, run 1

You are being asked to act as an outside specialist reviewer. This pack is self-contained. You do not need access to any other system.

## 1. What this is

"Church in Conversation" is a project that lets a person talk with a **representative** of a historical Christian community, for example the Donatist church of North Africa or the Reformed city of Geneva. The representative is an AI voice. It is supposed to speak from inside the community, in the first person, using only a curated set of that community's own records and sources, and to stay inside the community's time window. It must not invent, must say plainly what it does not know, and must be clear and readable to a general adult reader.

In this test, **12 worlds** each answered the **same 28 questions** (file 02). The answers are in the `worlds/` folder, one file per world. The worlds and their time windows are in file 01.

These answers were produced by a test harness, not by the finished product. Some sentences may have been removed by an automatic step, which can leave a dangling "he", "so" or "that" with nothing before it. Some raw system tags such as `[[thin:liturgy]]` or build words such as "this turn" or "the records I am holding" may also appear. Report these as defects (section 5) but keep them apart from your judgment of historical accuracy.

## 2. What we want from you

For every answer, judge two things.

**A. Rigor (accuracy and context).** The standard is **scholarly acceptability, not perfection.** Would a competent historian of this period and tradition let this stand in a textbook or a museum panel?
- **SOUND**: accurate and in context; honest about uncertainty.
- **ACCEPTABLE**: a small imprecision, thin coverage, a loose generalisation, or an omission, but nothing misleading.
- **NOT ACCEPTABLE**: a specialist would object. Use only for: a factual error; an invention (a person, text, place, event or attribution that does not exist); an anachronism (knowledge from after the world's window); a quotation used against its context or given to the wrong person; a contested question stated as settled; a **false silence** (see below); or an answer to a different question than the one asked.

**B. Access and craft.** Grade each of these GOOD, FAIR or POOR.
- **Readable**: plain adult English; sentences mostly 12 to 20 words, none past about 30; no unexplained jargon.
- **Understandable**: a non-specialist could follow it unaided. POOR if there are dangling pronouns or connectives, announced points never made, raw tags, or the voice talks about its own records, evidence or "this turn".
- **Succinct**: the length fits the question. POOR if it is padded, repeats itself, lectures, or pastes in material the question did not ask for. Good answers are often 120 to 260 words, but judge against the question.

**Overall call per answer:** SHIP (rigor is SOUND or ACCEPTABLE and nothing is POOR), FIX (rigor is fine but something is POOR), or BLOCK (rigor is NOT ACCEPTABLE).

## 3. The most important thing to look for: false silence

The representative often says that no source, record or voice exists on a topic, or that "we never said" something, when the period's sources do say it. Examples from this test (all found by checking): saying no woman's own writing survives from Roman Africa (Perpetua's prison narrative does); saying the Cappadocian writings are silent on the fate of non-believers (Gregory of Nyssa, Gregory of Nazianzus and Basil all discuss it); saying the community did not speak of being "born again" (it did).

A representative is allowed to say "our records do not hold this" or "I cannot recall a saying on this". It is **not** allowed to say "no such source exists" unless that is true of the whole period. If an answer claims an absence, check it. Name the source that contradicts it, or say you could not find one.

## 4. How to work

1. Read file 01 (worlds and windows) and file 02 (questions). **Use the window given for each world.** Anything after the end year is outside what the community can know. Anything inside it is fair, even if later scholarship named it.
2. Review **one world at a time**, in a fresh session if your tool has limited memory. Give your tool this README plus that world's file from `worlds/`.
3. For each answer: check each factual claim and each quotation from your own knowledge. If your tool can search the web, use it for claims you doubt and say you did.
4. Be fair. Credit what is right. Do not mark an answer NOT ACCEPTABLE for style alone, and do not mark it down for being brief and honest.
5. **Do not guess.** If you are unsure, write "unverified" and grade ACCEPTABLE, not NOT ACCEPTABLE. Never invent a source, a page number or a quotation yourself. Name a primary text or standard scholarship for a correction only when you are confident of it.
6. Do not ask for, or look at, our own grades (file 99) until you have finished.

## 5. Defects to log separately from rigor

Count and quote these where you see them: (a) dangling pronoun or connective with nothing before it; (b) an announced teaching never given; (c) raw tags such as `[[thin:...]]`; (d) build or system talk such as "this turn", "the ground given", "the records I am holding", "vendored", "I am a representative of..."; (e) chatbot phrasing such as "The short answer first. Yes."; (f) whole paragraphs reused word for word across answers; (g) stray characters.

## 6. Output format

For each world, return a table, then a short summary.

| Answer | Rigor | Readable | Understandable | Succinct | Overall | Doubted claim, and what the sources say | Defects (section 5) |
|---|---|---|---|---|---|---|---|

Then:
- Counts of SHIP, FIX and BLOCK.
- The three most serious rigor problems, each with the exact words from the answer and the correction.
- The recurring access or craft problems.
- One paragraph: would you put your name to this world's answers if the problems you named were fixed? What is the single biggest change?
- A line saying whether you used web search and which claims you could not verify.

If your tool can return structured data, also give JSON: `{"world":"...","answers":[{"n":1,"rigor":"SOUND|ACCEPTABLE|NOT ACCEPTABLE","readable":"GOOD|FAIR|POOR","understandable":"GOOD|FAIR|POOR","succinct":"GOOD|FAIR|POOR","overall":"SHIP|FIX|BLOCK","doubted":[{"claim":"exact words","problem":"...","source":"..."}],"defects":["..."]}],"summary":"..."}`

## 7. Pack contents

- `00_READ_ME_FIRST.md` this file
- `01_WORLDS.md` the twelve worlds, with windows
- `02_QUESTIONS.md` the 28 questions
- `worlds/<code>.md` 28 answers per world (lpc, gallic, desert, ijc, alx, witt, rzg, pahc, hal, syr, cappadocian, don)
- `99_OUR_GRADES_key_do_not_share_first.md` our own verdicts, for comparison after your review

## 8. Known limits of this pack

- Time windows come from each world's own definition record. They are the project's choice, not a settled scholarly boundary. Flag a window you think is wrong, but grade against the stated one.
- The "community" is a reconstruction from a curated source set. An answer may be accurate to the sources and still miss the wider period; judge the wider period.
- The answers come from one test run and are not the final product.


---

# The twelve worlds

Each "world" is a historical Christian community in a fixed time window. A representative speaks from inside that community, using only that community's own records. The window below is taken from each world's own record and is the period the representative may speak from. Anything after the window is not the community's to know.

## lpc: Latin North African pastoral-congregational Christianity (Cyprian to Augustine)
**Window:** 246 to 430 CE

The formation of ordinary Latin North African Christianity, c. 246-430 CE. Here Christianity is lived as the life of a local congregation, in its own territory, under a bishop's care. Two bishops hold it together. Cyprian of Carthage led his church through the Decian persecution, plague, and schism as a working bishop (248/249-258). A century later, Augustine of Hippo preached, taught those preparing for baptism, and gave the sacraments to his own congregation (391/395-430).

## gallic: Gallic monastic and ascetic Christianity
**Window:** 360 to 450 CE

Our span opens with Martin, freed from Caesar's service, gathering his first brethren near the town where Hilary was bishop. It closes in the years after the council at Ephesus, when Vincent had written his remembrancer and the churches of Gaul still took their bishops from among us. All of that span is ours to speak from. We speak from all of it at once, not from one year inside it.

## desert: Egyptian desert monasticism
**Window:** 320 to 430 CE

Egypt (the Nile valley and the desert's edge), c. 320s-c. 430 CE: the desert monastic formation ecology anchored on withdrawal as the whole work of formation, not merely its precondition.

## ijc: Imperial-juridical Christianity (church and empire, councils and law)
**Window:** 312 to 451 CE

Rome, Constantinople, and Milan, c.

## alx: Alexandrian catechetical Christianity
**Window:** 150 to 400 CE

Alexandria and Egypt, c. 150-400 CE: the Alexandrian Christian formation ecology anchored on its catechetical-formation tradition - learned teaching, allegorical-spiritual reading of Scripture, the staged catechumenate, confident engagement with Greek thought (Clement, Origen, the teaching tradition through Didymus, the episcopal line through Athanasius).

## witt: Lutheran Wittenberg and its congregations
**Window:** 1517 to 1580 CE

Our span opens with the theses sent against the selling of indulgences in 1517, and closes with the fuller confessional book gathered and bound in 1580, drawing together the catechisms and the confession already given decades before. Nothing within that span is closed to us; we do not experience one moment in it as a single now, with the rest as past or future.

## rzg: The Reformed cities of Zurich and Geneva
**Window:** 1519 to 1650 CE

The Swiss branch of the magisterial Reformation, 1519-1650. Two cities began their reforms independently. The men who started them had no contact. The reforms were later formally bridged but never merged. Zurich's reform opens on 1 January 1519. Huldrych Zwingli had just been appointed Leutpriester at the Grossmunster. He began to preach straight through the Gospel of Matthew. He set aside the fixed cycle of readings. The reform goes on through the First and Second Zurich Disputations (1523).

## pahc: Post-apostolic house-church Christianity
**Window:** 70 to 200 CE

Antioch and Syria, the cities of western Asia Minor, and Rome, c. 70-200 CE: Greek-speaking Christian communities gathering in households, joined into one world by letters and travelers - a bishop's guarded journey from Antioch toward Rome, Smyrna forwarding his letters onward at another church's asking, Rome writing at length to correct Corinth. The generations after the apostles' deaths, before settled bishops everywhere, before a closed canon, before legal peace.

## hal: The Hieronymian ascetic-literary circle (Jerome and the Roman women around him)
**Window:** 382 to 420 CE

Bethlehem and Rome, c. 382-420 CE: the ascetic-literary formation ecology around Jerome's scriptural scholarship and the network of aristocratic Roman women who sustained and were formed by it - Marcella's Aventine household, Paula and Eustochium's Bethlehem monasteries, Fabiola's Roman charitable foundations.

## syr: Syriac Christianity of Edessa and Nisibis
**Window:** 200 to 410 CE

The Syriac-speaking Christian ecology across the Roman-Persian Mesopotamian frontier, c. 200-410 CE: Edessa, a Roman-administered but linguistically and culturally Aramaic city; Nisibis, Roman fortress-city from 298 until ceded to Persia in 363; and the Persian-side communities Aphrahat wrote from.

## cappadocian: Cappadocian Trinitarian Christianity
**Window:** 325 to 394 CE

The Nicene-confessing churches of Cappadocia and Pontus, c. 325 - c. 394: the formation ecology of the communities that held, defended, and -- after 381 -- inherited the imperial establishment of the Nicene confession in this region, whose surviving voice is Basil of Caesarea, Gregory of Nazianzus, Gregory of Nyssa, and the households and congregations around them.

## don: Donatist (rigorist) African Christianity
**Window:** 311 to 439 CE

The rigorist rival church of Roman North Africa, c. 311/312 to 439. It split from the Catholic party of North Africa over one question. In Diocletian's persecution, some clergy were suspected of handing over the scriptures. Were the sacraments and ordinations they gave valid at all? This church then lived as a full parallel church. It had its own bishops, basilicas and line of ordination, and it contested the rival church town for town. That contest ran across Africa Proconsularis, Numidia, Byzacena and Mauretania.


---

# The 28 questions

The same 28 questions were put to every world. Cell codes (such as C-I, F3-P) are internal labels for the question's slot. They carry no meaning you need.

1. **C-I** In your own words, describe who Jesus was for your community.
2. **C-E** What sources, if any, connected your community to Jesus, and by what path did they arrive?
3. **C-P** Someone tells you they cannot manage to believe in Jesus - what is your response to them?
4. **C-T** Explain your community's understanding of Jesus's divine status and its relation to God the Father and the Spirit.
5. **F1-I** Describe the character and nature of God as your community understood it.
6. **F1-E** When your people disagreed about doctrine, who settled it, and what evidence tells us that process actually worked that way?
7. **F1-P** Was there space in your community for someone who struggled to believe?
8. **F1-T** Did your community hold that a person enters the world already carrying guilt?
9. **F2-I** Describe your community's approach and purpose in reading sacred texts.
10. **F2-E** If a modern scholar examined your claims, how much would survive rigorous scrutiny?
11. **F2-P** A modern reader finds the scriptures confusing or dull - what would you say they are missing?
12. **F2-T** Was scripture your community's sole source of authority, or were there others?
13. **F3-I** Explain how leadership and authority were established within your community.
14. **F3-E** Is it accurate that believers regularly concealed themselves underground?
15. **F3-P** Every community has failed people at times - how did yours respond when it failed someone?
16. **F3-T** Does any present-day church continue your community's exact tradition?
17. **F4-I** Describe, step by step, the process by which someone joined your community.
18. **F4-E** What evidence connects your rituals to the earliest followers, rather than later invention?
19. **F4-P** For someone whose mind won't settle, does your community's practice offer anything?
20. **F4-T** Would your community describe conversion using language like being 'born again'?
21. **F5-I** Describe a typical day in the life of someone in your community.
22. **F5-E** What physical evidence would remain of your community's gathering place?
23. **F5-P** What, if anything, did people give up to belong to your community?
24. **F5-T** How did your community understand and mark marriage?
25. **F6-I** Was there a part of your own community's life that unsettled you?
26. **F6-E** Given that a key outside record of your worship was obtained under torture, how reliable is that source?
27. **F6-P** How would your community have regarded a person like the one asking you this?
28. **F6-T** What did your community hold about the eternal fate of those outside it?
