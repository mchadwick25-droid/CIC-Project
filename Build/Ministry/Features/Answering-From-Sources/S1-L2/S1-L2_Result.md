# S1-L2: deterministic quoting on the replay bench

Free: no model call. Run 2026-10-29 by the engine thread.

## What was tried

The 308 saved drafts of fleet graded run 1 (eleven worlds; cappadocian saved no draft). For each draft, `bench.py` rebuilds the turn's evidence as the run did and checks that `apply_net` reproduces the shipped answer, then repairs each sentence the engine removed for a quotation reason and runs `apply_net` again on the repaired draft. The engine's own placement and net are unchanged, and the net re-verifies every placed quote against its record.

- V1: a quote marker the net refused for its lead-in is placed with a lead-in code writes from the record's speaker name ("Ephrem the Syrian puts it this way:").
- V2: V1, and a quotation the voice typed is replaced by the offered quote record it matches word for word.
- V3: V2, and a removed sentence that cites an offered quote record is replaced by that record, placed by code.

A reply carries one placed quote, so a draft whose quote was already placed takes no repair.

Reproduce: check out the saved runs from branch `claude/fleet-run-1-analysis` (`engine/m3/reports/fleet-graded-run-1/`), restore packages (`python -m engine.m2.cli restore`), then `python bench.py <dir of the world json files> <out dir>` and `python summarize.py <out dir>/results.json <out>.md`.

## Result

308 saved drafts; apply_net reproduced the shipped answer on 308.

| Step | Cuts | Probes with a placed quote | Placed quotes the net verified | Orphan flags | Repairs made |
|---|---|---|---|---|---|
| V0 today | 297 | 39 | 38 | 85 | 0 |
| V1 marker repair | 228 | 105 | 104 | 54 | 66 |
| V2 + typed quote selected | 228 | 105 | 104 | 54 | 66 |
| V3 + cited quote selected | 203 | 124 | 123 | 52 | 86 |

Cuts by reason:

| Reason | V0 today | V1 marker repair | V2 + typed quote selected | V3 + cited quote selected |
|---|---|---|---|---|
| gives a quote record's words without placing it | 20 | 18 | 18 | 18 |
| lead-in to a placed quote does not name its speaker | 81 | 4 | 4 | 4 |
| placed quote does not match its record | 23 | 5 | 5 | 5 |
| quotation typed by the voice | 42 | 42 | 42 | 42 |
| quote record not in this turn's evidence | 2 | 2 | 2 | 2 |
| second placed quote in one reply | 22 | 51 | 51 | 51 |
| second placed story in one reply | 1 | 1 | 1 | 1 |
| tagged to a quote record that has not been placed | 32 | 32 | 32 | 9 |
| tells an offered story without placing it | 28 | 28 | 28 | 28 |
| words after an attribution, not a placed quote | 22 | 21 | 21 | 20 |
| words attributed without a placed quote | 24 | 24 | 24 | 23 |

By world (V3 against V0):

| World | Drafts | Cuts V0 | Cuts V3 | Placed V0 | Placed V3 | Orphans V0 | Orphans V3 |
|---|---|---|---|---|---|---|---|
| alx | 28 | 24 | 12 | 9 | 19 | 10 | 4 |
| desert | 28 | 50 | 41 | 2 | 10 | 8 | 8 |
| don | 28 | 4 | 2 | 0 | 2 | 1 | 0 |
| gallic | 28 | 30 | 21 | 2 | 10 | 5 | 5 |
| hal | 28 | 26 | 16 | 6 | 16 | 11 | 6 |
| ijc | 28 | 34 | 24 | 5 | 13 | 5 | 3 |
| lpc | 28 | 45 | 39 | 4 | 10 | 13 | 11 |
| pahc | 28 | 25 | 10 | 2 | 17 | 16 | 6 |
| rzg | 28 | 7 | 4 | 5 | 8 | 2 | 0 |
| syr | 28 | 21 | 7 | 0 | 13 | 6 | 3 |
| witt | 28 | 31 | 27 | 4 | 6 | 8 | 6 |

Drafts changed by any repair: 86. By first repair step: {1: 66, 3: 20}.
Drafts where a repair was made but no quote ended up placed: 1.
Drafts with more cuts after repair than before: 0.
Words per changed draft: 251 shipped today, 340 after repair (mean change +89). All drafts: 265 today, 290 after repair.


## What the numbers do and do not show

- Every placed quote is the record's own rendering, verified by the net. No typed quote ships.
- The gain comes from V1 (66 drafts) and V3 (20 drafts). V2 found nothing: no typed quotation in the 308 drafts equals an offered quote record's words.
- Cuts fall by a third (297 to 203) and orphan flags by about 40% (85 to 52), but the replay cannot say whether the quote answers the question: that needs a human or judge read of the sample below. V3 selects a quote the voice cited, not one it asked to place.
- Answers grow by about 25 words on average (89 words on a changed draft): a placed quote is a whole rendering. Length is a measured cost.
- Cuts of other kinds are untouched (typed quotation 42, story 28, attribution 24). A second marker is now cut as "second placed quote" (22 to 51): the voice often marked more than one.
- The orphan count is the replay report's heuristic, applied the same way to every step.

## Sample of 30 changed drafts, before and after (for a human read)

### syr f2-t-probe-01 (F2-T); repairs: V1 -> syr.quote.on-a-certain-day-a-pearl

Before (shipped today):

> We would have found that question strange. Scripture was supreme and everywhere: sung, quoted, woven into every argument. But it always reached us through others. The church's worship. The harmony that gave the Gospel its shape. Our teachers. The covenant's practice. The book and the community that sang it were never rivals. The question assumes a separation we had not made.
> 
> We did not read Genesis the way moderns argue about it - as science. That was not because we doubted the text, but because we read for something else. Scripture's words were each a raza: a symbol bound to the truth - the shrara - it carries. So Eden was read toward the cross, Adam toward Christ, the ark toward the church.
> 
> A whole chapter's worth of meaning was found in a single pearl. And that reading happened inside the community. It was not a contest between the book and the church, with one claiming to trump the other. It was one life, sung and taught together.

After:

> We would have found that question strange. Scripture was supreme and everywhere: sung, quoted, woven into every argument. But it always reached us through others. The church's worship. The harmony that gave the Gospel its shape. Our teachers. The covenant's practice. The book and the community that sang it were never rivals. The question assumes a separation we had not made.
> 
> We did not read Genesis the way moderns argue about it - as science. That was not because we doubted the text, but because we read for something else. Scripture's words were each a raza: a symbol bound to the truth - the shrara - it carries. So Eden was read toward the cross, Adam toward Christ, the ark toward the church. Ephrem the Syrian puts it this way: “One day, my brothers, I picked up a pearl. In it I saw mysteries of the Kingdom, images and symbols of the Majesty; it became a fountain, and from it I drank mysteries of the Son. I set it, my brothers, on the palm of my hand so I could examine it. I went to look at it from one side, and it showed faces on every side. I discovered that the Son cannot be fully grasped, since he is wholly Light.”
> 
> A whole chapter's worth of meaning was found in a single pearl. And that reading happened inside the community. It was not a contest between the book and the church, with one claiming to trump the other. It was one life, sung and taught together.

### ijc c-t-probe-01 (C-T); repairs: V3 -> ijc.quote.nicene-creed

Before (shipped today):

> To us, Jesus is truly God, of one being with the Father - homoousios - sharing the very being that makes the Father God.
> 
> The Father is God, the Son is God, the Spirit is God - yet we confess one God, not three. Constantinople in 381 confessed the Spirit's full divinity alongside the Father and the Son. Leo's letter to Chalcedon states the binding truth of it: Christ is true God and true man together, each nature doing what belongs to it. So one Mediator could die in one nature and not die in the other. He wrote that it was equally perilous to believe Christ only God without man, or only man without God.
> 
> This was not settled while it was happening. For two imperial reigns our own establishment confessed differently: the Son is like the Father, homoios, as the scriptures say, and refused to go further. That was the empire's own faith, enforced by law, and men who confessed of one substance were the ones removed and exiled. The exactness we reached cost real blood and real exile. A century of councils spent itself making those words exact, because everything hung on them.
> 
> We did not write devotional memoirs about Jesus. We wrote definitions, the way people write what they are prepared to be exiled over.

After:

> To us, Jesus is truly God, of one being with the Father - homoousios - sharing the very being that makes the Father God. The Council of Nicaea puts it this way: “We believe in one God, the Father Almighty, maker of all things visible and invisible. And we believe in one Lord Jesus Christ, the Son of God, the only-begotten of his Father. He is of the substance of the Father: God from God, Light from Light, true God from true God. He was begotten...not made, being of one substance...with the Father. Through him all things were made, both those in heaven and those on earth. For us men and for our salvation he came down [from heaven], and took flesh, and was made man. He suffered, and on the third day he rose again, and went up into heaven. And he shall come again to judge both the living and the dead. And [we believe] in the Holy Spirit.”
> 
> That is who he was to us, confessed at every baptism, guarded by every council.
> 
> The Father is God, the Son is God, the Spirit is God - yet we confess one God, not three. Constantinople in 381 confessed the Spirit's full divinity alongside the Father and the Son. Leo's letter to Chalcedon states the binding truth of it: Christ is true God and true man together, each nature doing what belongs to it. So one Mediator could die in one nature and not die in the other. He wrote that it was equally perilous to believe Christ only God without man, or only man without God.
> 
> This was not settled while it was happening. For two imperial reigns our own establishment confessed differently: the Son is like the Father, homoios, as the scriptures say, and refused to go further. That was the empire's own faith, enforced by law, and men who confessed of one substance were the ones removed and exiled. The exactness we reached cost real blood and real exile. A century of councils spent itself making those words exact, because everything hung on them.
> 
> We did not write devotional memoirs about Jesus. We wrote definitions, the way people write what they are prepared to be exiled over.

### syr f4-p-probe-01 (F4-P); repairs: V1 -> syr.quote.aphrahat-medicine-penitence

Before (shipped today):

> Yes. Our teachers called it the medicine of penitence. They talked like field surgeons: everyone in this fight gets wounded, and the only fatal mistake is hiding the wound until it gets worse. Show the wound to someone who can help. The one who helps must not turn you away, or tell anyone what you showed him. When you heal, you go back into the line.
> 
> That was for what you had done. For what your own head will not stop doing to you - the racing thoughts, the silence you pray into - we had something else to say. We knew that silence at its harshest. Our teacher answered that God's faithfulness runs longer than one generation's rescue. We did not pretend the silence away. We endured inside it.
> 
> What we cannot give you is a technique for quieting the mind itself. That is not our idiom. What we had was people to stand in the silence with you, and the promise that showing the wound does not drive the physician away. Does your own mind race because of something you did, or for no reason you can name?

After:

> Yes. Our teachers called it the medicine of penitence. They talked like field surgeons: everyone in this fight gets wounded, and the only fatal mistake is hiding the wound until it gets worse. The Persian sage puts it this way: “For all diseases there are medicines, and there is healing when a skilled physician finds them. And for those who have been wounded in our conflict, there is the medicine of penitence; those who apply it to their wounds are healed.”
> 
> Show the wound to someone who can help. The one who helps must not turn you away, or tell anyone what you showed him. When you heal, you go back into the line.
> 
> That was for what you had done. For what your own head will not stop doing to you - the racing thoughts, the silence you pray into - we had something else to say. We knew that silence at its harshest. Our teacher answered that God's faithfulness runs longer than one generation's rescue. We did not pretend the silence away. We endured inside it.
> 
> What we cannot give you is a technique for quieting the mind itself. That is not our idiom. What we had was people to stand in the silence with you, and the promise that showing the wound does not drive the physician away. Does your own mind race because of something you did, or for no reason you can name?

### pahc f6-t-probe-01 (F6-T); repairs: V1 -> pahc.quote.justin-reasonable-livers

Before (shipped today):

> We will give you both of our own answers, because we actually held both. One of us, Justin, argued that anyone who lived reasonably - Socrates among the Greeks, others among peoples you might not expect him to name - was, in a real sense, already a Christian, born before Christ or not. And yet in at least one of our own communities, the way a new member was taught was stark: two roads, a way of life and a way of death, nothing in between named. We do not know how far that teaching reached beyond that one community. We are not going to pretend it fits neatly together with Justin's own wider reach. They are both truly ours.
> 
> Our writers also said two things about the faithful dead. Clement of Rome wrote that those whom God's grace has made perfect in love now have a place among the godly. Polycarp wrote that Ignatius, Paul and the other apostles are now in their due place with the Lord. Our writers also hope for a rising. Ignatius wrote that the Father will raise up those who believe in him through Christ Jesus. How the time between death and that day is spent, we cannot lay out. We cannot speak for any one person. We can tell you what our writers hoped.

After:

> We will give you both of our own answers, because we actually held both. One of us, Justin, argued that anyone who lived reasonably - Socrates among the Greeks, others among peoples you might not expect him to name - was, in a real sense, already a Christian, born before Christ or not. Justin puts it this way: “We have been taught that Christ is the first-born of God. We have said above that he is the Word, and every race of men shared in the Word. And those who lived by reason are Christians, even though people thought them atheists. Among the Greeks, there were Socrates and Heraclitus, and men like them. Among non-Greeks, there were Abraham, Ananias, Azarias, Mishael, Elijah, and many others...”
> 
> And yet in at least one of our own communities, the way a new member was taught was stark: two roads, a way of life and a way of death, nothing in between named. We do not know how far that teaching reached beyond that one community. We are not going to pretend it fits neatly together with Justin's own wider reach. They are both truly ours.
> 
> Our writers also said two things about the faithful dead. Clement of Rome wrote that those whom God's grace has made perfect in love now have a place among the godly. Polycarp wrote that Ignatius, Paul and the other apostles are now in their due place with the Lord. Our writers also hope for a rising. Ignatius wrote that the Father will raise up those who believe in him through Christ Jesus. How the time between death and that day is spent, we cannot lay out. We cannot speak for any one person. We can tell you what our writers hoped.

### don f3-i-probe-01 (F3-I); repairs: V1 -> don.quote.the-shores-are-covered

Before (shipped today):

> We cannot give you settled procedures, because we have none to show. What we can show you is the shape authority actually took among us, and where it broke down.
> 
> Bishops held authority, and councils held the bishops. That is the short answer, and the size of it is the part people get wrong. Three hundred and ten bishops of ours sat at Bagai and condemned a breakaway party. Later the same body took two of those condemned bishops back into office, without baptizing or ordaining either one again. That was not an advisory board. That was a church governing itself, and it did not govern consistently.
> 
> A bishop was made by people and bishops together, though the record shows it could go badly wrong. At Cirta, when Silvanus was being made bishop, the people shouted back — let it be another; hear us, God — and he was made bishop anyway, and a court heard about it years later from a man who said, I myself fought against his being made bishop. So a crowd could object, and still be overridden.
> 
> Now the hardest part. Authority among us failed its own test at the start. At Cirta, before the split hardened, our bishops were asked outright whether they had handed over the scriptures. Several said yes. Then someone turned the question back on the man presiding. The room could not finish. They reserved the matter to the Lord and sat down. The men who would make a bishop's purity the test of whether a sacrament exists at all found that test unusable on themselves.
> 
> And in 320 a charge came against one of our bishops, and another wrote urging him to settle it quietly, before the flame burst out — and said in the same letter that he knew the accusation was true. Several of those letters end the same way. Let no one learn of it. We are the church that said a man's purity decides whether a sacrament is real, and those are our founding bishops arranging for a true charge to go quiet.
> 
> Whether a woman could carry real authority among us we have to answer crookedly, because no woman among us left a line. The whole founding story, as our enemies tell it, turns on a wealthy laywoman of Carthage — her fortune, her household, her grievance. In their telling she made a bishop. That telling has a cost for the man making it: the accusation only works if her power was real. A hostile source that needs a woman's agency in order to blame her has recorded that agency, whatever it meant to do. What it cost her we do not know, except that it cost her this: she is the reason a whole church was said to exist, and she does not get to speak once in her own defence.
> 
> Authority among us was conciliar, real, and never consistent with the rule it enforced outward.

After:

> We cannot give you settled procedures, because we have none to show. What we can show you is the shape authority actually took among us, and where it broke down.
> 
> Bishops held authority, and councils held the bishops. That is the short answer, and the size of it is the part people get wrong. Three hundred and ten bishops of ours sat at Bagai and condemned a breakaway party. The council of Bagai puts it this way: “For the waves of truth have hurled the shipwrecked limbs of certain men against the sharp rocks. And, as happened to the Egyptians, the shores are covered with the bodies of the dying. Their punishment grows heavier in death itself. This is because, after the avenging waters have squeezed the life out of them, they do not even find burial.”
> 
> Later the same body took two of those condemned bishops back into office, without baptizing or ordaining either one again. That was not an advisory board. That was a church governing itself, and it did not govern consistently.
> 
> A bishop was made by people and bishops together, though the record shows it could go badly wrong. At Cirta, when Silvanus was being made bishop, the people shouted back — let it be another; hear us, God — and he was made bishop anyway, and a court heard about it years later from a man who said, I myself fought against his being made bishop. So a crowd could object, and still be overridden.
> 
> Now the hardest part. Authority among us failed its own test at the start. At Cirta, before the split hardened, our bishops were asked outright whether they had handed over the scriptures. Several said yes. Then someone turned the question back on the man presiding. The room could not finish. They reserved the matter to the Lord and sat down. The men who would make a bishop's purity the test of whether a sacrament exists at all found that test unusable on themselves.
> 
> And in 320 a charge came against one of our bishops, and another wrote urging him to settle it quietly, before the flame burst out — and said in the same letter that he knew the accusation was true. Several of those letters end the same way. Let no one learn of it. We are the church that said a man's purity decides whether a sacrament is real, and those are our founding bishops arranging for a true charge to go quiet.
> 
> Whether a woman could carry real authority among us we have to answer crookedly, because no woman among us left a line. The whole founding story, as our enemies tell it, turns on a wealthy laywoman of Carthage — her fortune, her household, her grievance. In their telling she made a bishop. That telling has a cost for the man making it: the accusation only works if her power was real. A hostile source that needs a woman's agency in order to blame her has recorded that agency, whatever it meant to do. What it cost her we do not know, except that it cost her this: she is the reason a whole church was said to exist, and she does not get to speak once in her own defence.
> 
> Authority among us was conciliar, real, and never consistent with the rule it enforced outward.

### syr c-i-probe-01 (C-I); repairs: V1 -> syr.quote.aphrahat-sure-thing

Before (shipped today):

> We sang him more than we defined him. He used Scripture's own names, one after another, not a philosopher's definition. The poet sang of the Only-Begotten who was with Deity and came to dwell among us. At our font we answered the question with praise. Our baptismal hymns sing the Father rejoicing with his Son and the Spirit over the one baptized. In baptism's second birth, our teachers said, the believer received the Holy Spirit.
> 
> Then we guarded what we confessed. Our teachers warned against prying scrutiny into the Godhead, because what God is, they held, is better sung than dissected. We stood with the great council's faith. Our tradition remembers that our own bishop of Nisibis sat at Nicaea. But our native tongue for that faith was not the council's Greek. It was praise.
> 
> We read him through raza, the symbol bound to the truth it carries. A raza is not a stand-in chosen at will. It is Scripture or creation itself showing what is hidden. Eden pointed to the cross, Adam to Christ, the ark to the church. That was how we read, and how we taught. Our native tongue for Jesus was hymn and symbol, not formula.

After:

> We sang him more than we defined him. The Persian sage puts it this way: “It is a sure thing with us that Jesus our Lord is God, the Son of God, the King, and the King's Son. He is Light of Light, Creator, and Counsellor. He is Guide, the Way, Redeemer, and Shepherd. He is Gatherer, the Door, the Pearl, and the Lamp.”
> 
> He used Scripture's own names, one after another, not a philosopher's definition. The poet sang of the Only-Begotten who was with Deity and came to dwell among us. At our font we answered the question with praise. Our baptismal hymns sing the Father rejoicing with his Son and the Spirit over the one baptized. In baptism's second birth, our teachers said, the believer received the Holy Spirit.
> 
> Then we guarded what we confessed. Our teachers warned against prying scrutiny into the Godhead, because what God is, they held, is better sung than dissected. We stood with the great council's faith. Our tradition remembers that our own bishop of Nisibis sat at Nicaea. But our native tongue for that faith was not the council's Greek. It was praise.
> 
> We read him through raza, the symbol bound to the truth it carries. A raza is not a stand-in chosen at will. It is Scripture or creation itself showing what is hidden. Eden pointed to the cross, Adam to Christ, the ark to the church. That was how we read, and how we taught. Our native tongue for Jesus was hymn and symbol, not formula.

### syr f1-i-probe-01 (F1-I); repairs: V3 -> syr.quote.aphrahat-persecuted-litany

Before (shipped today):

> We believed in one God, maker of all things, good and just in the same person. We said this out loud, against neighbors who taught otherwise. Against Marcion we held that the Maker of this world is the Father of Jesus, not a lesser or harsher god. Against Bardaisan we held that God made all things from nothing, not from eternal elements that drifted into order. Against Mani we refused a world split between two powers. And with Bardaisan, notably, we agreed on one great point: the stars do not rule us; free will is God's gift and cannot be compelled.
> 
> What this meant to us, lived out, was that God could be trusted with the hardest question: why he allows suffering at all. On the Persian side of our world, under a hostile crown, we asked that question with blood in our mouths. Taunted that our prayers had not stopped the killing, our sage did not claim they had. He answered with a roll-call instead. Abel was murdered, and his blood cried out. Jacob was persecuted, and fled. David was persecuted at the hands of Saul. Jesus was persecuted, and the martyrs came after him. The persecuted, he meant, were not abandoned. They stood in a long line that ran through Scripture. God did not spare that line from suffering. He was with it, and he promised it resurrection.
> 
> We also knew God as the Physician. A physician is not scandalized by wounds. He exists for them. And he does not reject the one who repents - the only thing that keeps a wound from healing is the shame that hides it. That was our experience of him: good, just, and present with the wounded.

After:

> We believed in one God, maker of all things, good and just in the same person. We said this out loud, against neighbors who taught otherwise. Against Marcion we held that the Maker of this world is the Father of Jesus, not a lesser or harsher god. Against Bardaisan we held that God made all things from nothing, not from eternal elements that drifted into order. Against Mani we refused a world split between two powers. And with Bardaisan, notably, we agreed on one great point: the stars do not rule us; free will is God's gift and cannot be compelled.
> 
> What this meant to us, lived out, was that God could be trusted with the hardest question: why he allows suffering at all. On the Persian side of our world, under a hostile crown, we asked that question with blood in our mouths. Taunted that our prayers had not stopped the killing, our sage did not claim they had. He answered with a roll-call instead. Abel was murdered, and his blood cried out. Jacob was persecuted, and fled. The Persian sage puts it this way: “Hear, my beloved, these names of martyrs, confessors, and the persecuted. Abel was murdered, and his blood cried out from the earth. Jacob was persecuted, and he fled and became an exile. Joseph was persecuted, and he was sold and thrown into the pit. Moses was persecuted, and he fled to Midian.”
> 
> Moses was persecuted, and fled to Midian. David was persecuted at the hands of Saul. Jesus was persecuted, and the martyrs came after him. The persecuted, he meant, were not abandoned. They stood in a long line that ran through Scripture. God did not spare that line from suffering. He was with it, and he promised it resurrection.
> 
> We also knew God as the Physician. A physician is not scandalized by wounds. He exists for them. And he does not reject the one who repents - the only thing that keeps a wound from healing is the shame that hides it. That was our experience of him: good, just, and present with the wounded.

### pahc f5-e-probe-01 (F5-E); repairs: V1 -> pahc.quote.two-female-slaves-who-were-called-deaconesses

Before (shipped today):

> You ask what a dig would find at the place we met. You ask how historians even know about ordinary days like ours. We cannot say. No building tied to us survives. No burial or inscription does either. The catacombs, the house-churches you can visit today - those belong to a later world. Ours had already closed. What we left behind is letters. Arguments about who should lead. Instructions for how to gather. Words passed between one household and another.
> 
> Once, a Roman governor went looking for us. He found two of our women and had them tortured to make them talk. What he wrote down afterward comes closer to an outside view of a meeting than anything we wrote ourselves. They were enslaved, and they served their church in some recognized way. Their own account of it was never kept.
> 
> Beyond that - an ordinary day, an ordinary meal, what our houses really looked like - none of that has come down to us. We would rather say plainly that it is missing than describe a house we cannot actually show you.

After:

> You ask what a dig would find at the place we met. You ask how historians even know about ordinary days like ours. We cannot say. No building tied to us survives. No burial or inscription does either. The catacombs, the house-churches you can visit today - those belong to a later world. Ours had already closed. What we left behind is letters. Arguments about who should lead. Instructions for how to gather. Words passed between one household and another.
> 
> Once, a Roman governor went looking for us. He found two of our women and had them tortured to make them talk. What he wrote down afterward comes closer to an outside view of a meeting than anything we wrote ourselves. Pliny the Younger puts it this way: “So I thought it all the more needed to question two female slaves. They were called deaconesses, ministrae. I did this even with torture, to find out the truth. But I found nothing but a depraved superstition that went too far. So I have put off further inquiry, and I have turned to you for advice.”
> 
> They were enslaved, and they served their church in some recognized way. Their own account of it was never kept.
> 
> Beyond that - an ordinary day, an ordinary meal, what our houses really looked like - none of that has come down to us. We would rather say plainly that it is missing than describe a house we cannot actually show you.

### pahc c-p-probe-01 (C-P); repairs: V1 -> pahc.quote.justin-flame-kindled

Before (shipped today):

> We cannot promise you a moment of sudden certainty. Justin, the one among us who wrote about his own path, says he went looking through other philosophies first. He turned the old man's words over in his mind and found this the one safe and worthwhile way. He said it was open to anyone who truly cared what became of them, who was genuinely looking for salvation, and who already believed there was a God.
> 
> We should say plainly, though: this is the account of a man with the time and learning to go looking for it. We do not have the same account from someone without what he had. What we can tell you is how it reached us at all. None of us saw him ourselves. What we have is what was handed to us. The apostles preached what they had received from the Lord, and appointed others to carry it forward when they themselves were gone. On the day we gathered, someone read aloud from the memoirs the apostles wrote or from the writings of the prophets, for as long as there was time. That is how it reached us: by receiving it and passing it on.
> 
> We cannot tell you what an ordinary believer among us made of the teaching as it was read aloud. Most of us could not read or write, so those who walked this road left no account in their own words. Everything we left behind came from the few among us who could write. Whether belief came slowly or all at once for someone without Justin's learning, our own words cannot show you.

After:

> We cannot promise you a moment of sudden certainty. Justin, the one among us who wrote about his own path, says he went looking through other philosophies first. Justin puts it this way: “He said these things, and many others there is no time to mention now. Then he went away, telling me to think them over, and I have not seen him since. But at once a flame was kindled in my soul. A love for the prophets, and for those who are friends of Christ, took hold of me. As I turned his words over in my mind, I found this philosophy alone to be safe and useful. This is why, and this is how, I am a philosopher.”
> 
> He turned the old man's words over in his mind and found this the one safe and worthwhile way. He said it was open to anyone who truly cared what became of them, who was genuinely looking for salvation, and who already believed there was a God.
> 
> We should say plainly, though: this is the account of a man with the time and learning to go looking for it. We do not have the same account from someone without what he had. What we can tell you is how it reached us at all. None of us saw him ourselves. What we have is what was handed to us. The apostles preached what they had received from the Lord, and appointed others to carry it forward when they themselves were gone. On the day we gathered, someone read aloud from the memoirs the apostles wrote or from the writings of the prophets, for as long as there was time. That is how it reached us: by receiving it and passing it on.
> 
> We cannot tell you what an ordinary believer among us made of the teaching as it was read aloud. Most of us could not read or write, so those who walked this road left no account in their own words. Everything we left behind came from the few among us who could write. Whether belief came slowly or all at once for someone without Justin's learning, our own words cannot show you.

### hal f1-i-probe-01 (F1-I); repairs: V1 -> hal.quote.house-destroyed

Before (shipped today):

> We held God to be the Trinity: Father, Son, and Holy Spirit, one God in three persons. That is the faith we were born into after the great council, and we defended it against every heresy we fought. The Son is God the Word made flesh, of one being with the Father. His death is our redemption - the blood by which we were bought back.
> 
> But you ask about character, not just what we confessed. Here is what our lives show. We held God to be just - severely so. Rome fell in our own lifetime, and we read that fall as judgment: the head of the empire cut off, the light of all the world put out, judgment spoken in the prophets' words. A daughter died young after taking up the ascetic life, and at her funeral the crowd said fasting had killed her. We rebuked grief without limits as unbelief. That is justice as we held it.
> 
> And we held God to be merciful. Our comfort letters pardoned a mother's tears even while asking her to hold them back. Grief itself was allowed. Our holiest people are shown grieving too.
> 
> What we show you, then, is God both just and merciful, and we held the two together without resolving the tension between them. Our record shows those answers doing real work - and also failing to stop the weeping. We kept both the answers and the weeping, and that is the truth about what we held.

After:

> We held God to be the Trinity: Father, Son, and Holy Spirit, one God in three persons. That is the faith we were born into after the great council, and we defended it against every heresy we fought. The Son is God the Word made flesh, of one being with the Father. His death is our redemption - the blood by which we were bought back.
> 
> But you ask about character, not just what we confessed. Here is what our lives show. We held God to be just - severely so. Rome fell in our own lifetime, and we read that fall as judgment: the head of the empire cut off, the light of all the world put out, judgment spoken in the prophets' words. A daughter died young after taking up the ascetic life, and at her funeral the crowd said fasting had killed her. We rebuked grief without limits as unbelief. That is justice as we held it.
> 
> And we held God to be merciful. Our comfort letters pardoned a mother's tears even while asking her to hold them back. Jerome puts it this way: “As for our house, so far as its earthly wealth is concerned, it has been completely destroyed by the attacks of the heretics. But by the mercy of Christ it is still filled with spiritual riches. To live on bread is better than to lose the faith.”
> 
> Grief itself was allowed. Our holiest people are shown grieving too.
> 
> What we show you, then, is God both just and merciful, and we held the two together without resolving the tension between them. Our record shows those answers doing real work - and also failing to stop the weeping. We kept both the answers and the weeping, and that is the truth about what we held.

### lpc f1-p-probe-01 (F1-P); repairs: V1 -> lpc.quote.longing-expectation-is-a-prayer-for-me

Before (shipped today):

> There was, and we knew that struggle from the inside. One of our own bishops told it himself, years later, when he wrote the story of his life. Years later, close to his own conversion, the truth had become certain to him, yet the old burden had not lifted. We do not promise you that struggle resolves on any set schedule. We tell you it was real, in one of our own, and that it was not the end of his story.
> 
> He told them their longing expectation was itself a prayer for him. That restlessness was not something we judged out of existence. It was something we named, plainly, as part of being formed.

After:

> There was, and we knew that struggle from the inside. One of our own bishops told it himself, years later, when he wrote the story of his life. Years later, close to his own conversion, the truth had become certain to him, yet the old burden had not lifted. We do not promise you that struggle resolves on any set schedule. We tell you it was real, in one of our own, and that it was not the end of his story.
> 
> Augustine puts it this way: “But now I imagine that no one has come here except those who want to hear. So I am not speaking to deaf hearts, or to minds that will look down on the word. Instead, this longing expectation of yours is a prayer for me.”
> 
> He told them their longing expectation was itself a prayer for him. That restlessness was not something we judged out of existence. It was something we named, plainly, as part of being formed.

### ijc f4-e-probe-01 (F4-E); repairs: V1 -> ijc.quote.julius-custom

Before (shipped today):

> You ask for our own evidence that what we do was done by the first followers, and not made up later. Here is what we can say, and what we cannot.
> 
> The strongest currency we had was appeal to ancient custom. Nicaea itself legislates by it: 'let the ancient customs prevail'. That is Rome claiming a practice already old enough to count as inherited. But the record also lets us watch a custom being born, and admits it. Augustine, an eyewitness of the basilica siege at Milan in 386, dates a new practice at that city precisely. It was kept from then on, he says, and imitated by nearly all congregations afterward. He claims a real beginning at Milan and a wide later imitation, not the first Latin hymn ever written. Some of our practices genuinely came down from before anyone could remember otherwise. Some were new, and people knew they were new. The claim of apostolic age was also a tool, and it was used most where a practice was disputed.
> 
> What we inherited from before Constantine - a church already existing with settled convictions and a functioning structure of bishops - that much is solid. The office existed to shepherd a persecuted flock before any emperor asked it to settle imperial-scale disputes. What changed in 312 was what those convictions could now do in the world, not that they existed at all.
> 
> What we cannot give you is unbroken documentation from Jesus to us for every practice we held. The spine of our own record is documents: council acts with dates and signatures, church canons, imperial laws, and letters between named men about named disputes. That is the strong half. The honest other half is that nearly all of it was kept by the winners. Some founding stories are attested twice and disagree. The events and instruments are solid, the coverage is narrow, and the framing is interested.
> 
> So here is the honest answer. Some of what we did we received as already old, and our councils legislated by appeal to that inheritance. Some of what we did we began ourselves, and our own record says so. The claim that a practice went back to the apostles was strongest exactly where the practice was contested. We appealed to ancient custom because custom was our currency. Whether every appeal was true is a question our own record lets you ask.

After:

> You ask for our own evidence that what we do was done by the first followers, and not made up later. Here is what we can say, and what we cannot.
> 
> The strongest currency we had was appeal to ancient custom. Nicaea itself legislates by it: 'let the ancient customs prevail'. Julius puts it this way: “And why was nothing said to us about the Church of the Alexandrians in particular? Are you unaware that the custom has been to write to us first, and then for a just decision to be passed from this place?”
> 
> That is Rome claiming a practice already old enough to count as inherited. But the record also lets us watch a custom being born, and admits it. Augustine, an eyewitness of the basilica siege at Milan in 386, dates a new practice at that city precisely. It was kept from then on, he says, and imitated by nearly all congregations afterward. He claims a real beginning at Milan and a wide later imitation, not the first Latin hymn ever written. Some of our practices genuinely came down from before anyone could remember otherwise. Some were new, and people knew they were new. The claim of apostolic age was also a tool, and it was used most where a practice was disputed.
> 
> What we inherited from before Constantine - a church already existing with settled convictions and a functioning structure of bishops - that much is solid. The office existed to shepherd a persecuted flock before any emperor asked it to settle imperial-scale disputes. What changed in 312 was what those convictions could now do in the world, not that they existed at all.
> 
> What we cannot give you is unbroken documentation from Jesus to us for every practice we held. The spine of our own record is documents: council acts with dates and signatures, church canons, imperial laws, and letters between named men about named disputes. That is the strong half. The honest other half is that nearly all of it was kept by the winners. Some founding stories are attested twice and disagree. The events and instruments are solid, the coverage is narrow, and the framing is interested.
> 
> So here is the honest answer. Some of what we did we received as already old, and our councils legislated by appeal to that inheritance. Some of what we did we began ourselves, and our own record says so. The claim that a practice went back to the apostles was strongest exactly where the practice was contested. We appealed to ancient custom because custom was our currency. Whether every appeal was true is a question our own record lets you ask.

### desert f1-t-probe-01 (F1-T); repairs: V1 -> desert.quote.he-puts-into-us-the-beginnings

Before (shipped today):

> Were people born already guilty, carrying Adam's sin? We have no answer to give. No letter and no story of ours speaks to it in so many words. What we can tell you is that we argued grace and effort at length, and came down this way: a man may strive with all his might for a good result, yet he cannot become master of what is good unless he has it as a gift. Grace and free will look opposed to each other, but really are in harmony; we thought we ought to have both alike. The main share in our salvation belongs not to the merit of our own works but to heavenly grace. Sometimes he grants the carrying out of the work. And sometimes he saves people even against their will and without their knowledge, from a ruin close at hand. We took that from experience rather than from argument - led, as we put it, not by chattering words but by experience. One of us set that down at length, as a whole conference, though not in those words. He reported an abbot's teaching, and he wrote it far away, years later. That conclusion - grace holding the main share, and effort a real share - is what we have to give you. The question of guilt from birth does not reach us in our own words.

After:

> Were people born already guilty, carrying Adam's sin? We have no answer to give. No letter and no story of ours speaks to it in so many words. What we can tell you is that we argued grace and effort at length, and came down this way: a man may strive with all his might for a good result, yet he cannot become master of what is good unless he has it as a gift. Grace and free will look opposed to each other, but really are in harmony; we thought we ought to have both alike. The main share in our salvation belongs not to the merit of our own works but to heavenly grace. Abbot Chaeremon puts it this way: “... now he puts into us the very beginnings of salvation, and gives each person the zeal of their own free will. Now he grants the carrying out of the work, and the perfecting of goodness. Now he saves people, even against their own will and without their knowledge, from a ruin that is close at hand, and a headlong fall...”
> 
> Sometimes he grants the carrying out of the work. And sometimes he saves people even against their will and without their knowledge, from a ruin close at hand. We took that from experience rather than from argument - led, as we put it, not by chattering words but by experience. One of us set that down at length, as a whole conference, though not in those words. He reported an abbot's teaching, and he wrote it far away, years later. That conclusion - grace holding the main share, and effort a real share - is what we have to give you. The question of guilt from birth does not reach us in our own words.

### hal f4-p-probe-01 (F4-P); repairs: V1 -> hal.quote.a-follower-of-cicero-and-not-of-christ

Before (shipped today):

> We would not offer you calm. We would offer you company and a method. Our founding scholar said his own desert years were anything but peaceful. His body starved among the rocks while his mind burned with the pleasures of Rome and crowds of girls. The discipline he taught was to fill the mind: psalms, fixed hours of prayer, work for the hands, a text to wrestle with. The restless head is not silenced by force. It is given something to hold.
> 
> Here is what that looked like in practice. Jerome himself told this story against himself: he would fast, then open his beloved Cicero. He would weep for his sins, then pick his favorite authors back up. Then came a fever so bad they were preparing his funeral, and a dream. After that dream he swore off the old books and threw himself into scripture with more zeal than he had ever given to the books of men. His critics later pointed out, fairly, that his pages never stopped quoting the classics. The turn was real, and the old loves stayed with him.
> 
> The method was this: give the mind the psalms instead of the silence, give the hands work instead of idleness, give the hours a shape instead of letting them drift. We never promised it would be easy. One of our own young women died within months of taking up the ascetic life. That cost was real, and we will not hide it from you.
> 
> On prayer that meets only silence, our record is thinner and sadder. Our comfort letters were written after deaths, and they offer hope. They do not report that the silence broke.

After:

> We would not offer you calm. We would offer you company and a method. Our founding scholar said his own desert years were anything but peaceful. His body starved among the rocks while his mind burned with the pleasures of Rome and crowds of girls. The discipline he taught was to fill the mind: psalms, fixed hours of prayer, work for the hands, a text to wrestle with. The restless head is not silenced by force. It is given something to hold.
> 
> Here is what that looked like in practice. Jerome himself told this story against himself: he would fast, then open his beloved Cicero. He would weep for his sins, then pick his favorite authors back up. Then came a fever so bad they were preparing his funeral, and a dream. Jerome puts it this way: “Suddenly I was caught up in the spirit and dragged before the judgment seat of the Judge. Here the light was so bright, and those standing around so radiant, that I threw myself on the ground. I did not dare look up. I was asked who and what I was. I answered: 'I am a Christian.' But he who presided said: 'You lie. You follow Cicero, not Christ. For where your treasure is, there your heart will be also.' At once I was struck speechless. Amid the strokes of the lash - for he had ordered me to be scourged - I was tortured more severely still by the fire of conscience...”
> 
> After that dream he swore off the old books and threw himself into scripture with more zeal than he had ever given to the books of men. His critics later pointed out, fairly, that his pages never stopped quoting the classics. The turn was real, and the old loves stayed with him.
> 
> The method was this: give the mind the psalms instead of the silence, give the hands work instead of idleness, give the hours a shape instead of letting them drift. We never promised it would be easy. One of our own young women died within months of taking up the ascetic life. That cost was real, and we will not hide it from you.
> 
> On prayer that meets only silence, our record is thinner and sadder. Our comfort letters were written after deaths, and they offer hope. They do not report that the silence broke.

### lpc f1-e-probe-01 (F1-E); repairs: V1 -> lpc.quote.bishop-of-bishops

Before (shipped today):

> We never fully settled which one settles it, and that must be said plainly. Cyprian opened the council of 256 with a rule he would not break. A century and a half later, Augustine held a different view. A small council yields to a wider one, he wrote.
> 
> These are real differences, and we do not resolve them. What we can say is this. When disagreement came, it was argued in council, bishop by bishop, and the bishops in communion did not break communion over it. At the 256 council, Cyprian's own words were these: we judge no one, and reject no one from communion, for thinking differently from us. That same council decided the question he and Stephen had argued most sharply. Augustine later argued at book length that the ruling made that day was wrong. He never once put Cyprian outside our communion.
> 
> So the process we can point to is this: councils met, bishops argued, each gave his judgment, and the bond held through the disagreement. Which theory of authority governed that bond is the very thing the two bishops disagree about, and we keep both.

After:

> We never fully settled which one settles it, and that must be said plainly. Cyprian opened the council of 256 with a rule he would not break. Cyprian puts it this way: “None of us sets himself up as a bishop over other bishops, and none of us uses a tyrant's terror to force a colleague into obedience. Every bishop has his own right to judge, in keeping with the freedom and power allowed to him. He can no more be judged by another bishop than he himself can judge another. Instead, let us all wait for the judgment of our Lord Jesus Christ. He is the only one who has the power both to place us in the government of His Church and to judge how we conduct ourselves there.”
> 
> A century and a half later, Augustine held a different view. A small council yields to a wider one, he wrote.
> 
> These are real differences, and we do not resolve them. What we can say is this. When disagreement came, it was argued in council, bishop by bishop, and the bishops in communion did not break communion over it. At the 256 council, Cyprian's own words were these: we judge no one, and reject no one from communion, for thinking differently from us. That same council decided the question he and Stephen had argued most sharply. Augustine later argued at book length that the ruling made that day was wrong. He never once put Cyprian outside our communion.
> 
> So the process we can point to is this: councils met, bishops argued, each gave his judgment, and the bond held through the disagreement. Which theory of authority governed that bond is the very thing the two bishops disagree about, and we keep both.

### hal f3-i-probe-01 (F3-I); repairs: V1 -> hal.quote.recourse-to-marcella

Before (shipped today):

> Leadership and authority among us never came from one source, and we will not pretend otherwise. At Bethlehem, the double monastery had two resident threads of leadership: Paula, then her daughter Eustochium, led the women; Jerome led the men. That arrangement stood on patronage and recognition, not church office. Paula's fortune paid for the buildings, the books, the copying work, and the care of travelers. Jerome's scriptural learning was what people crossed the sea to study with. The two threads held together by free recognition - people stayed because they chose to.
> 
> In Rome it worked differently, and here we must be more careful. Marcella's household on the Aventine became a center of scriptural counsel after Jerome left the city. That is one man's memorial of her, and we name it as such. Her own letters were not kept. The claim is contested. What we can say without contest is that she argued Jerome's own answers for years before he left Rome, and that her household remained a recognized place for scriptural work. How much authority she carried, and whether the consultation he describes was as steady as his words suggest, rests on his witness alone.
> 
> Authority among us never came from ruling a territory or from episcopal office. It came from known learning in scripture and from the wealth that sustained the work. That is the honest answer: patronage and recognition together, differently weighted at the two poles, and in Marcella's case attested by a single, interested voice.

After:

> Leadership and authority among us never came from one source, and we will not pretend otherwise. At Bethlehem, the double monastery had two resident threads of leadership: Paula, then her daughter Eustochium, led the women; Jerome led the men. That arrangement stood on patronage and recognition, not church office. Paula's fortune paid for the buildings, the books, the copying work, and the care of travelers. Jerome's scriptural learning was what people crossed the sea to study with. The two threads held together by free recognition - people stayed because they chose to.
> 
> In Rome it worked differently, and here we must be more careful. Marcella's household on the Aventine became a center of scriptural counsel after Jerome left the city. Jerome puts it this way: “So after I left Rome, people turned to her whenever a dispute arose about what scripture said on any subject. They looked to her to settle it.”
> 
> That is one man's memorial of her, and we name it as such. Her own letters were not kept. The claim is contested. What we can say without contest is that she argued Jerome's own answers for years before he left Rome, and that her household remained a recognized place for scriptural work. How much authority she carried, and whether the consultation he describes was as steady as his words suggest, rests on his witness alone.
> 
> Authority among us never came from ruling a territory or from episcopal office. It came from known learning in scripture and from the wealth that sustained the work. That is the honest answer: patronage and recognition together, differently weighted at the two poles, and in Marcella's case attested by a single, interested voice.

### lpc f6-t-probe-01 (F6-T); repairs: V1 -> lpc.quote.no-salvation-out-of-the-church

Before (shipped today):

> We held it hard, and we do not soften it here. Cyprian wrote that there is no salvation outside the Church. He said it of heretics -- people who confessed Christ but stood outside. He gave the ark as his picture. If anyone could have escaped outside Noah's ark, then someone might escape outside the Church. But no one did.
> 
> He also wrote to a pagan who blamed and persecuted us, a man named Demetrianus. Yet in that same letter he pressed the man to turn while he lived.
> 
> Cyprian did not write of people who never heard of Christ at all. We cannot say what he would have held of them.

After:

> We held it hard, and we do not soften it here. Cyprian wrote that there is no salvation outside the Church. He said it of heretics -- people who confessed Christ but stood outside. Cyprian puts it this way: “Can the power of baptism be greater or worth more than confession and suffering? That is when someone confesses Christ before others and is baptized in his own blood. Yet even this baptism does not help a heretic, though he confessed Christ and was put to death outside the Church. Only the defenders and advocates of heretics say otherwise. They declare that heretics killed in a false confession of Christ are martyrs. They give them the glory and crown of martyrdom against the word of the apostle. He says it will profit them nothing, even if they were burned and killed. Not even the baptism of public confession and blood can help a heretic to salvation, because there is no salvation outside the Church. How much less will it help him in a hiding-place and a den of robbers, stained with the infection of adulterous water! There he has not only failed to put off his old sins. He has piled up still newer and greater ones.”
> 
> He gave the ark as his picture. If anyone could have escaped outside Noah's ark, then someone might escape outside the Church. But no one did.
> 
> He also wrote to a pagan who blamed and persecuted us, a man named Demetrianus. Yet in that same letter he pressed the man to turn while he lived.
> 
> Cyprian did not write of people who never heard of Christ at all. We cannot say what he would have held of them.

### syr f5-p-probe-01 (F5-P); repairs: V1 -> syr.quote.warned-before-baptism

Before (shipped today):

> What a person gave up depended on what kind of belonging they chose. We offered two paths, not one.
> 
> Everyone who came to the font gave up the old gods. Baptism was a public event, sung as a second birth, and the one who came up from the water received the sealing and the Holy Spirit. That much everyone gave: the old worship, and the willingness to be named publicly as one of us. On the Persian side of our world, where we lived under a hostile crown, being known as a Christian could cost you everything. When the persecution came, bishops died first, then the covenant's vowed members. So the first answer is: everyone gave up the old worship, and on the Persian side some gave their lives.
> 
> But there was a second path, and it cost far more. The sons and daughters of the covenant - the qyama - gave up marriage for good. That vow was taken for life. They stayed in town, among their own kin, and served the congregation through fasting, vigil, and prayer. Later accounts say the daughters' choirs sang our teaching hymns in the churches. The vow itself is solid; how their order was structured inside is thinly documented. What we can say plainly is this: they gave up marriage, children, and an ordinary household, and they did not leave for the desert. They lived the vow where everyone could see it.
> 
> Most of our people married and raised children. Their cost was being marked out in a city of many religions, with rival teachers at every door. What their households gave up day by day, beyond the old gods and the willingness to be known, our record does not say. The voices that survive are the vowed celibates, and they wrote mostly to each other. We will not invent an ordinary believer's account to fill that silence.

After:

> What a person gave up depended on what kind of belonging they chose. We offered two paths, not one.
> 
> Everyone who came to the font gave up the old gods. Aphrahat puts it this way: “For this reason it is right for the preachers of the Church, who sound the trumpet, to warn everyone in God's covenant before baptism. They are also to warn those who choose for themselves virginity and holiness: the young men, the virgins, and those wishing to become holy. The preachers are to warn them and say this. If your heart is set on marriage, then marry before your baptism. Otherwise you may fall in the fight and be killed. And if you are afraid of this part of the fight, turn back now, so that you do not break your brothers' hearts along with your own. And if you love your possessions, turn back from the army too. Otherwise, when the battle goes against you, you may remember your possessions and turn back to them. For there is disgrace for the one who turns back from the fight.”
> 
> Baptism was a public event, sung as a second birth, and the one who came up from the water received the sealing and the Holy Spirit. That much everyone gave: the old worship, and the willingness to be named publicly as one of us. On the Persian side of our world, where we lived under a hostile crown, being known as a Christian could cost you everything. When the persecution came, bishops died first, then the covenant's vowed members. So the first answer is: everyone gave up the old worship, and on the Persian side some gave their lives.
> 
> But there was a second path, and it cost far more. The sons and daughters of the covenant - the qyama - gave up marriage for good. That vow was taken for life. They stayed in town, among their own kin, and served the congregation through fasting, vigil, and prayer. Later accounts say the daughters' choirs sang our teaching hymns in the churches. The vow itself is solid; how their order was structured inside is thinly documented. What we can say plainly is this: they gave up marriage, children, and an ordinary household, and they did not leave for the desert. They lived the vow where everyone could see it.
> 
> Most of our people married and raised children. Their cost was being marked out in a city of many religions, with rival teachers at every door. What their households gave up day by day, beyond the old gods and the willingness to be known, our record does not say. The voices that survive are the vowed celibates, and they wrote mostly to each other. We will not invent an ordinary believer's account to fill that silence.

### pahc f4-i-probe-01 (F4-I); repairs: V1 -> pahc.quote.two-ways-one-of-life-and-one-of-death

Before (shipped today):

> Someone asked to join. We taught them. They fasted. Then came the water.
> 
> The teaching was called the Two Ways. The teaching went all the way down to sharing what you had instead of calling it your own. That is what was put before the one who asked.
> 
> Then came fasting - a day or two for the one being baptized, and the one baptizing fasted too. Then the baptisma: the washing in water. Running water where it could be found, other water if not, or water poured three times over the head, in the name of the Father, the Son, and the Holy Spirit. Only after it could a person come to the table.
> 
> That is the path as one of our own communities set it down. We cannot tell you how far this exact shape reached beyond that community. We can tell you what it looked like where it was practiced. The teaching, the fast, the water, the table.

After:

> Someone asked to join. We taught them. They fasted. Then came the water.
> 
> The teaching was called the Two Ways. The manual known as the Didache puts it this way: “There are two ways: one of life and one of death, and there is a great difference between the two ways. The way of life is this. First, you shall love God, who made you; second, your neighbor as yourself. And all the things you would not want to happen to you, you also must not do to another.”
> 
> The teaching went all the way down to sharing what you had instead of calling it your own. That is what was put before the one who asked.
> 
> Then came fasting - a day or two for the one being baptized, and the one baptizing fasted too. Then the baptisma: the washing in water. Running water where it could be found, other water if not, or water poured three times over the head, in the name of the Father, the Son, and the Holy Spirit. Only after it could a person come to the table.
> 
> That is the path as one of our own communities set it down. We cannot tell you how far this exact shape reached beyond that community. We can tell you what it looked like where it was practiced. The teaching, the fast, the water, the table.

### ijc f1-p-probe-01 (F1-P); repairs: V3 -> ijc.quote.augustine-vigil-hymns

Before (shipped today):

> We hear the question, and we will tell you what we have. Our record comes from men who wrote law and doctrine, and it does not tell us how any of them prayed alone. It does not give us one believer's own struggle to trust, or what a congregation said to someone who brought their doubt into the open. What the record shows is what happened in public: the creed confessed together, the hymns and psalms sung when soldiers surrounded our basilica. That is worship under siege, not a conversation about doubt. We also know what our bishop did when the emperor who had ordered a massacre was not yet sorry. Ambrose barred him from the altar and waited. Forgiveness came after repentance, not before it. That is about a massacre, not about belief. We cannot promise it answers your question. It is what we have.

After:

> We hear the question, and we will tell you what we have. Our record comes from men who wrote law and doctrine, and it does not tell us how any of them prayed alone. It does not give us one believer's own struggle to trust, or what a congregation said to someone who brought their doubt into the open. What the record shows is what happened in public: the creed confessed together, the hymns and psalms sung when soldiers surrounded our basilica. Augustine of Hippo puts it this way: “The pious people kept guard in the church, ready to die with their bishop, your servant. There my mother, your handmaid, lived in prayer. She carried a chief part of those worries and that watching. ... At this time it was established that hymns and psalms should be sung, following the practice of the Eastern Church. This was so that the people would not waste away in the weariness of sorrow. That custom has been kept from then till now. It is copied by many, indeed by almost all of your congregations throughout the rest of the world.”
> 
> That is worship under siege, not a conversation about doubt. We also know what our bishop did when the emperor who had ordered a massacre was not yet sorry. Ambrose barred him from the altar and waited. Forgiveness came after repentance, not before it. That is about a massacre, not about belief. We cannot promise it answers your question. It is what we have.

### rzg f1-i-probe-01 (F1-I); repairs: V1 -> rzg.quote.taught-better-from-scripture

Before (shipped today):

> God, to us, is not first a word to be analyzed before it can be trusted. He is what Scripture shows him to be: sovereign, faithful, and utterly free. His own free choice, made before the world began, settles who is saved - not anything foreseen or earned in the one chosen. We hold that as the ground of a settled life, not a threat. Whoever is joined to Christ by true faith already has, in that faith itself, the only evidence of election anyone is given.
> 
> He is not a distant first cause who set the world going and walked away. He keeps caring for everything he made. That continuous, active rule is what we meant by his providence. And he is utterly consistent with himself: what he promises, he does. His word stands because he stands behind it. We tested everything we inherited against that word, and what it did not warrant, we let go.
> 
> The sharpest place this conviction pressed was at the Supper. To us, the bread and cup were not a sacrifice repeated, and not Christ's own body, confined to what you can chew.. What we affirmed is that Christ is truly given, by the Spirit, to whoever receives him believing. The reality is not shut out; it is also not confined to bread.
> 
> We did not hold this as one option among many. Rome's repeated sacrifice and its images: refused. Wittenberg's claim that Christ's body sits in the bread: refused. A third claim, from inside our own circle, that only a believer's own chosen profession makes a true church: refused as well. Each time, the same test: does this reading hold against Scripture? We do not pretend the refusing cost nothing, or that it was always argument alone. It was not.

After:

> God, to us, is not first a word to be analyzed before it can be trusted. He is what Scripture shows him to be: sovereign, faithful, and utterly free. His own free choice, made before the world began, settles who is saved - not anything foreseen or earned in the one chosen. We hold that as the ground of a settled life, not a threat. Whoever is joined to Christ by true faith already has, in that faith itself, the only evidence of election anyone is given.
> 
> He is not a distant first cause who set the world going and walked away. He keeps caring for everything he made. That continuous, active rule is what we meant by his providence. And he is utterly consistent with himself: what he promises, he does. His word stands because he stands behind it. We tested everything we inherited against that word, and what it did not warrant, we let go. Huldrych Zwingli puts it this way: “I, Ulrich Zwingli, declare that I have preached the articles and opinions below in the good city of Zurich. I preached them as based on the Scriptures that are called inspired by God... Where my present understanding of these Scriptures is not correct, I will let myself be taught better. But I will be taught only from these same Scriptures.”
> 
> The sharpest place this conviction pressed was at the Supper. To us, the bread and cup were not a sacrifice repeated, and not Christ's own body, confined to what you can chew.. What we affirmed is that Christ is truly given, by the Spirit, to whoever receives him believing. The reality is not shut out; it is also not confined to bread.
> 
> We did not hold this as one option among many. Rome's repeated sacrifice and its images: refused. Wittenberg's claim that Christ's body sits in the bread: refused. A third claim, from inside our own circle, that only a believer's own chosen profession makes a true church: refused as well. Each time, the same test: does this reading hold against Scripture? We do not pretend the refusing cost nothing, or that it was always argument alone. It was not.

### pahc f1-e-probe-01 (F1-E); repairs: V1 -> pahc.quote.asia-rejected-new-prophecy

Before (shipped today):

> We never settled doctrine the way you are asking about. No council met, in our own time, to decide what God is or what Christ must be believed to be. That kind of deciding belongs to a world that came after us. What we actually argued about, letter after letter, was who should lead: one bishop, or a council of elders. The other real fight was whether Christ truly suffered in the flesh.
> 
> Near the very end of our own years, churches in Asia did meet - often, and in many places - over a new prophetic movement spreading among them. But that gathering was about whether to receive a movement. It was not about settling what God is.
> 
> When disagreement came, what we have is letters. Rome wrote a long one to Corinth when Corinth removed some of its own presbyters. Rome argued those men had served blamelessly and should not have been removed. We do not have Corinth's reply. We do not know whether Corinth accepted Rome's correction, or what happened to anyone who still disagreed after the letter arrived. The letter is what survives, not the outcome.

After:

> We never settled doctrine the way you are asking about. No council met, in our own time, to decide what God is or what Christ must be believed to be. That kind of deciding belongs to a world that came after us. What we actually argued about, letter after letter, was who should lead: one bishop, or a council of elders. The other real fight was whether Christ truly suffered in the flesh.
> 
> Near the very end of our own years, churches in Asia did meet - often, and in many places - over a new prophetic movement spreading among them. The Anonymous anti-Montanist writer puts it this way: “The faithful all over Asia met many times, in many places in Asia, to talk this over. They looked closely at these new teachings. They declared them false and rejected them as heresy. Because of that, they were thrown out of the Church and shut out of communion.”
> 
> But that gathering was about whether to receive a movement. It was not about settling what God is.
> 
> When disagreement came, what we have is letters. Rome wrote a long one to Corinth when Corinth removed some of its own presbyters. Rome argued those men had served blamelessly and should not have been removed. We do not have Corinth's reply. We do not know whether Corinth accepted Rome's correction, or what happened to anyone who still disagreed after the letter arrived. The letter is what survives, not the outcome.

### desert f2-p-probe-01 (F2-P); repairs: V3 -> desert.quote.three-renunciations-solomon

Before (shipped today):

> We do not know, in the way you are asking. We did not write about scripture's own hard parts, or its dull stretches, as their own subject. We used the parts that spoke to one struggle at a time - a verse taken up as counsel for whatever a person was actually facing that day - and we did not dwell on the rest. Nothing we kept says what we made of the passages that confused us, or the ones that bored us. We would rather tell you plainly that this is missing from what we left behind than invent an answer we do not actually have.
> 
> What we can tell you is how we did use it. That is scripture for us: not a book to be mastered whole, but a few verses heard as an order to be obeyed, or a weapon ready to hand. We lived inside a small number of passages, returned to again and again, until they had shaped how we saw everything else. That may not be what you are asking for. It is what we actually have to give you.

After:

> We do not know, in the way you are asking. We did not write about scripture's own hard parts, or its dull stretches, as their own subject. We used the parts that spoke to one struggle at a time - a verse taken up as counsel for whatever a person was actually facing that day - and we did not dwell on the rest. Nothing we kept says what we made of the passages that confused us, or the ones that bored us. We would rather tell you plainly that this is missing from what we left behind than invent an answer we do not actually have.
> 
> What we can tell you is how we did use it. That is scripture for us: not a book to be mastered whole, but a few verses heard as an order to be obeyed, or a weapon ready to hand. Abbot Paphnutius of Scetis puts it this way: “The three books of Solomon fit these three kinds of renunciation well. Proverbs answers to the first. In it, desires for fleshly things and earthly sins are held in check. Ecclesiastes fits the second, for there everything done under the sun is called vanity. The Song of Songs fits the third. In it the soul soars above all visible things. It is truly joined to the Word of God by gazing on heavenly things.”
> 
> We lived inside a small number of passages, returned to again and again, until they had shaped how we saw everything else. That may not be what you are asking for. It is what we actually have to give you.

### pahc c-t-probe-01 (C-T); repairs: V1 -> pahc.quote.those-who-lived-reasonably-are-christians

Before (shipped today):

> We believed in one God, maker of everything. Ignatius called Jesus Christ our God again and again, in how he opened his letters and in how he closed them. It was not one passing phrase; he reached for it often. But it was worship, not an argument worked out. No one whose writing survives explained how calling Jesus God fits together with calling the Father God, with there being one God. We can tell you plainly that we called him God. We cannot tell you we had worked out how he could be God when the Father is God, and God is one.
> 
> Justin went further and said God's own Word was present in some measure in every people, so that even a reasonable person born before Christ could in that sense already be called a Christian. That was his own argument about the Word's reach across all peoples. But it was not a worked-out teaching about how the Word relates to the Father or to the Spirit in the way later councils would take up.
> 
> If you are asking what we argued about among ourselves, the honest answer is not God's nature as later councils took it up. No gathering of ours ever met to settle a question like that about God. That kind of deciding belongs to a later world. What we actually argued about, letter after letter, was two things. One was who should lead us: one bishop, or a council of elders. The other was whether Christ truly suffered in the flesh. Those were our real fights.

After:

> We believed in one God, maker of everything. Ignatius called Jesus Christ our God again and again, in how he opened his letters and in how he closed them. It was not one passing phrase; he reached for it often. But it was worship, not an argument worked out. No one whose writing survives explained how calling Jesus God fits together with calling the Father God, with there being one God. We can tell you plainly that we called him God. We cannot tell you we had worked out how he could be God when the Father is God, and God is one.
> 
> Justin went further and said God's own Word was present in some measure in every people, so that even a reasonable person born before Christ could in that sense already be called a Christian. Justin Martyr puts it this way: “...and those who lived by reason are Christians, even though they were thought to be atheists. Among the Greeks there were Socrates and Heraclitus and men like them. Among the non-Greeks there were Abraham, Ananias, Azarias, Mishael, Elijah, and many more...”
> 
> That was his own argument about the Word's reach across all peoples. But it was not a worked-out teaching about how the Word relates to the Father or to the Spirit in the way later councils would take up.
> 
> If you are asking what we argued about among ourselves, the honest answer is not God's nature as later councils took it up. No gathering of ours ever met to settle a question like that about God. That kind of deciding belongs to a later world. What we actually argued about, letter after letter, was two things. One was who should lead us: one bishop, or a council of elders. The other was whether Christ truly suffered in the flesh. Those were our real fights.

### hal c-t-probe-01 (C-T); repairs: V1 -> hal.quote.ever-let-the-bridegroom-sport-with-you

Before (shipped today):

> Jesus is God the Son, of one being with the Father, and the Trinity - Father, Son, and Holy Spirit, one God - is simply the faith of the church. We defended it against every heresy we fought, and we were born after the great council had settled it. We never treated it as negotiable. To us it would be strange to hear it asked as an open question.
> 
> We spoke of his death as redemption: the blood by which we were bought back. That is near to the later language of punishment in our place without being identical to it; the precise formula belongs to a later age. Personal Lord and Savior was not our phrase. A widow greeted his birthplace by name. The devotion those words carry is close kin to what the modern phrase means.
> 
> The conviction that drove our whole translation labor - later called the Vulgata - was that the Hebrew text of scripture was the truest. It stood closer to what God said than the Greek version the church had long used. That conviction, the Hebraica veritas, was Jerome's own, and not every Christian of our age shared it.

After:

> Jesus is God the Son, of one being with the Father, and the Trinity - Father, Son, and Holy Spirit, one God - is simply the faith of the church. We defended it against every heresy we fought, and we were born after the great council had settled it. We never treated it as negotiable. To us it would be strange to hear it asked as an open question.
> 
> We spoke of his death as redemption: the blood by which we were bought back. That is near to the later language of punishment in our place without being identical to it; the precise formula belongs to a later age. Personal Lord and Savior was not our phrase. Jerome puts it this way: “Always let the privacy of your room guard you. Always let the Bridegroom take his delight with you there within. Do you pray? You speak to the Bridegroom. Do you read? He speaks to you. When sleep overtakes you, he will come behind and put his hand through the opening of the door. Your heart will be moved for him. You will wake and rise up and say: 'I am sick with love.'...”
> 
> A widow greeted his birthplace by name. The devotion those words carry is close kin to what the modern phrase means.
> 
> The conviction that drove our whole translation labor - later called the Vulgata - was that the Hebrew text of scripture was the truest. It stood closer to what God said than the Greek version the church had long used. That conviction, the Hebraica veritas, was Jerome's own, and not every Christian of our age shared it.

### syr f1-t-probe-01 (F1-T); repairs: V1 -> syr.quote.aphrahat-stone-foundation

Before (shipped today):

> We held that everyone enters the world under death's rule, and wounded by sin - but we did not say it that way, as guilt already carried. Our teacher put it plainly: from Adam's transgression, death has ruled over everyone, even over those who had not sinned the way Adam did. What people inherit from Adam, we described as death's rule and sin's wounding, a sickness in the human race. That is different from saying a newborn child is guilty for Adam's choice. We said the wound was there, the sickness was there, and death's kingdom held everyone alike until One Man broke into it.
> 
> Our sage taught it with a picture. On faith the whole house is raised: fasting, prayer, love, almsgiving, meekness. A house is built for someone. The believer becomes a dwelling-place for Christ, and a king's dwelling is not left bare. That is how we spoke of what grace does - not as erasing inherited guilt, but as ending death's rule and healing the wound.
> 
> The later frame that calls it original guilt belongs to arguments made after our years ended. We will not pretend we spoke that language. What we said was: death ruled, Christ nailed sin to his cross, and the one who believes is healed.

After:

> We held that everyone enters the world under death's rule, and wounded by sin - but we did not say it that way, as guilt already carried. Our teacher put it plainly: from Adam's transgression, death has ruled over everyone, even over those who had not sinned the way Adam did. What people inherit from Adam, we described as death's rule and sin's wounding, a sickness in the human race. That is different from saying a newborn child is guilty for Adam's choice. We said the wound was there, the sickness was there, and death's kingdom held everyone alike until One Man broke into it.
> 
> Our sage taught it with a picture. The Persian sage puts it this way: “In the same way the true Stone, our Lord Jesus Christ, is the foundation of all our faith. On him, on this Stone, faith is laid; and resting on faith, the whole structure rises until it is complete.”
> 
> On faith the whole house is raised: fasting, prayer, love, almsgiving, meekness. A house is built for someone. The believer becomes a dwelling-place for Christ, and a king's dwelling is not left bare. That is how we spoke of what grace does - not as erasing inherited guilt, but as ending death's rule and healing the wound.
> 
> The later frame that calls it original guilt belongs to arguments made after our years ended. We will not pretend we spoke that language. What we said was: death ruled, Christ nailed sin to his cross, and the one who believes is healed.

### alx c-p-probe-01 (C-P); repairs: V1 -> alx.quote.gregory-spark

Before (shipped today):

> That is where many of us began. Among us, wanting to believe and not yet believing was not failure. Our teachers said faith - pistis - was a foundation, not a finish line: something to stand on while the rest is still dark. And we did not ask anyone to force belief. We asked them to stay near - to listen, to ask questions, to walk with a teacher, sometimes for years, before ever coming to the water.
> 
> It was love for the Holy Word, and for the man who taught him. We cannot make it happen for you either, and we will not pretend we can. But we can tell you what we would have done with you: we would not have shut the door. We would have said: stay, and keep asking.
> 
> The assembly - the ekklesia - was not a members list you signed. It was the gathering around the one who calls. Walking toward that gathering, with your questions still open, was itself part of the path. And for us the path itself was formation: learning was not preparation for a life with God, it was that life beginning.

After:

> That is where many of us began. Among us, wanting to believe and not yet believing was not failure. Our teachers said faith - pistis - was a foundation, not a finish line: something to stand on while the rest is still dark. And we did not ask anyone to force belief. We asked them to stay near - to listen, to ask questions, to walk with a teacher, sometimes for years, before ever coming to the water.
> 
> Gregory puts it this way: “And so, like a spark falling on our innermost soul, love was kindled and burst into flame within us. It was love at once for the Holy Word, the most lovely object of all, who draws everyone irresistibly toward himself by his unutterable beauty. And it was love for this man, his friend and advocate.”
> 
> It was love for the Holy Word, and for the man who taught him. We cannot make it happen for you either, and we will not pretend we can. But we can tell you what we would have done with you: we would not have shut the door. We would have said: stay, and keep asking.
> 
> The assembly - the ekklesia - was not a members list you signed. It was the gathering around the one who calls. Walking toward that gathering, with your questions still open, was itself part of the path. And for us the path itself was formation: learning was not preparation for a life with God, it was that life beginning.

### syr f2-i-probe-01 (F2-I); repairs: V1 -> syr.quote.on-a-certain-day-a-pearl

Before (shipped today):

> We read to find what the words were bound to. Scripture was not only a record of events; it was full of signs - the raza, we called each one - and each raza carried a truth, the shrara, that it was made to show. The raza was not a stand-in someone picks at will. It was bound to the truth it disclosed. Eden pointed to the cross. Adam pointed to Christ. The Jordan pointed to the font. Type answered type across the whole of Scripture, and we read for those bindings.
> 
> Our own poet showed this in one of his hymns about a pearl. That turning of the pearl was how we read. The symbol itself held what it was meant to disclose, and reading meant turning it until the truth it carried showed itself. The mystery was guarded, not solved.
> 
> What we read was the one continuous Gospel story - not four separate books, but the harmony Tatian had woven from them. For two hundred years that one telling was what our churches heard in worship. Alongside it stood the Law and the Prophets, read as one long promise pointing to Christ. Every old word found its answer in him.
> 
> Our purpose in reading was formation, not information. Doctrine was taught by singing it. The madrashe - our teaching hymns - carried theological argument in verse, with melody and refrain so the congregation learned the faith by keeping the tune. Scripture reached us through worship, through the harmony's own shape, through our teachers' voices, and through the covenant's practice. The book and the community that sang it were never rivals. We would have found that separation strange.

After:

> We read to find what the words were bound to. Scripture was not only a record of events; it was full of signs - the raza, we called each one - and each raza carried a truth, the shrara, that it was made to show. The raza was not a stand-in someone picks at will. It was bound to the truth it disclosed. Eden pointed to the cross. Adam pointed to Christ. The Jordan pointed to the font. Type answered type across the whole of Scripture, and we read for those bindings.
> 
> Our own poet showed this in one of his hymns about a pearl. Ephrem the Syrian puts it this way: “One day, my brothers, I picked up a pearl. In it I saw mysteries of the Kingdom, images and symbols of the Majesty; it became a fountain, and from it I drank mysteries of the Son. I set it, my brothers, on the palm of my hand so I could examine it. I went to look at it from one side, and it showed faces on every side. I discovered that the Son cannot be fully grasped, since he is wholly Light.”
> 
> That turning of the pearl was how we read. The symbol itself held what it was meant to disclose, and reading meant turning it until the truth it carried showed itself. The mystery was guarded, not solved.
> 
> What we read was the one continuous Gospel story - not four separate books, but the harmony Tatian had woven from them. For two hundred years that one telling was what our churches heard in worship. Alongside it stood the Law and the Prophets, read as one long promise pointing to Christ. Every old word found its answer in him.
> 
> Our purpose in reading was formation, not information. Doctrine was taught by singing it. The madrashe - our teaching hymns - carried theological argument in verse, with melody and refrain so the congregation learned the faith by keeping the tune. Scripture reached us through worship, through the harmony's own shape, through our teachers' voices, and through the covenant's practice. The book and the community that sang it were never rivals. We would have found that separation strange.

### desert f3-i-probe-01 (F3-I); repairs: V3 -> desert.quote.sarah-man-among-you

Before (shipped today):

> We never settled who really carried authority. One view gave it to a man who had earned it through his own discipline and a lifetime of discernment. The other gave it to an office that came with the Rule, held by anyone appointed to it, regardless of who he was underneath. Both existed among us at once, in the same decades, and neither one gave way to the other.
> 
> The first kind we called geron - the elder, abba for a man, amma for a woman. Their word carried teaching weight, though they held no office. A person came to them and stayed, learning through shared work and close company, watching how they lived, hearing a short saying given for one struggle at a time. Authority came from recognized discernment, not from being appointed. We have at least one clear case of a woman holding that kind of weight.
> 
> The other kind belonged to the Koinonia - Pachomius's own name for his linked houses. They lived under one written rule and one leader. Offices such as housemaster and steward were appointed, not earned through a lifetime's discernment. The Rule itself carried the authority, and the office came with it.
> 
> Even Pachomius, who founded the office-based way, is remembered partly in the older, personal terms: a father whose own example, not just his Rule, formed his community. That tells you how deeply the two models ran through each other, never cleanly separated. We lived with both unresolved. No one among us ever solved it.

After:

> We never settled who really carried authority. One view gave it to a man who had earned it through his own discipline and a lifetime of discernment. The other gave it to an office that came with the Rule, held by anyone appointed to it, regardless of who he was underneath. Both existed among us at once, in the same decades, and neither one gave way to the other.
> 
> The first kind we called geron - the elder, abba for a man, amma for a woman. Their word carried teaching weight, though they held no office. A person came to them and stayed, learning through shared work and close company, watching how they lived, hearing a short saying given for one struggle at a time. Authority came from recognized discernment, not from being appointed. We have at least one clear case of a woman holding that kind of weight.
> 
> The other kind belonged to the Koinonia - Pachomius's own name for his linked houses. They lived under one written rule and one leader. Offices such as housemaster and steward were appointed, not earned through a lifetime's discernment. The Rule itself carried the authority, and the office came with it.
> 
> Even Pachomius, who founded the office-based way, is remembered partly in the older, personal terms: a father whose own example, not just his Rule, formed his community. That tells you how deeply the two models ran through each other, never cleanly separated. We lived with both unresolved. No one among us ever solved it.

### alx f1-i-probe-01 (F1-I); repairs: V3 -> alx.quote.origen-punishment-heals

Before (shipped today):

> We believed in one God, the maker of all things. He is good, and beyond every image and every clever description. And he is never alone: his Word and his Spirit are his own - not lesser gods, and not created things. Only after Nicaea was that last part said with full clarity.
> 
> God is known the way light is known. You do not stare at the sun; you see everything else by it.
> 
> Our deepest habit was to speak of God as a teacher. The whole creation is his school, and scripture is his main lesson. The slow healing of a soul is his patient method. When pain came - and it came to us - we said God's hand in it was a physician's. Suffering was the school's hardest classroom, not proof of abandonment.
> 
> God made every rational being - every soul that could know him - for his own Word, the Logos. That is what logikos meant: made for the Word, able to know God. We were made to share in his own life. Not by becoming God ourselves, but by becoming fully what a creature was made to be, because the Logos entered human nature.

After:

> We believed in one God, the maker of all things. He is good, and beyond every image and every clever description. And he is never alone: his Word and his Spirit are his own - not lesser gods, and not created things. Only after Nicaea was that last part said with full clarity.
> 
> God is known the way light is known. You do not stare at the sun; you see everything else by it.
> 
> Our deepest habit was to speak of God as a teacher. The whole creation is his school, and scripture is his main lesson. The slow healing of a soul is his patient method. When pain came - and it came to us - we said God's hand in it was a physician's. Origen puts it this way: “And so we think that every threat, pain and punishment that comes from God is never inflicted in order to injure the sufferers. Instead, it is always intended to do them good.”
> 
> Suffering was the school's hardest classroom, not proof of abandonment.
> 
> God made every rational being - every soul that could know him - for his own Word, the Logos. That is what logikos meant: made for the Word, able to know God. We were made to share in his own life. Not by becoming God ourselves, but by becoming fully what a creature was made to be, because the Logos entered human nature.

