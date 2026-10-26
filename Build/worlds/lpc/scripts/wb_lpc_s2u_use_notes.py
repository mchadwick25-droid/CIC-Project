"""S2u: Latin Pastoral-Congregational Christianity (lpc) use notes.

Runs after s2y. Holds each voiced citable record's use_note (what it means,
what it must not be made to support, the years it speaks for) as data and
writes it into that record's front matter. Re-running replaces the block, so
the result is the same every time.
"""
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
RECORDS_ROOT = REPO_ROOT / "records" / "lpc"

# Years each phase of the world speaks for, and the whole window.
C = (246, 258)
A = (391, 430)
W = (246, 430)
E248 = (248, 249)
D256 = (256, 256)
D258 = (258, 258)
D391 = (391, 391)
D411 = (411, 411)
D430 = (430, 430)

QUOTES = {
"lpc.quote.a-dreadful-plague-broke-out": (
    "Pontius describes the plague at Carthage as a city shuddering and fleeing, putting out its own people, and leaving the dead lying in the streets.",
    ["a claim about how many died or what the disease was",
     "a claim that Pontius is an outside witness, since he wrote in praise of his bishop",
     "a claim that 'their own friends' means companions rather than the household and kin the Latin names"], C),
"lpc.quote.a-hundred-thousand-sesterces": (
    "Cyprian tells eight Numidian bishops that his church sent one hundred thousand sesterces, gathered from its clergy and people, to ransom captive believers.",
    ["a claim about what the sum was worth in modern money",
     "a claim that the ransom freed anyone",
     "a claim about what share of the church's wealth the sum was"], C),
"lpc.quote.a-standard-bearer-of-the-sect": (
    "Pontius reports the proconsul's sentence calling Cyprian a standard-bearer of the sect and an enemy of the gods, and saying discipline would begin to be made firm with his blood.",
    ["a claim that 'discipline' in the sentence means punishment rather than restored order",
     "a claim that Pontius and the Acta are independent witnesses to the wording of the sentence",
     "a claim about the details of the dream Pontius mentions earlier"], D258),
"lpc.quote.ancient-venom-against-my-episcopate": (
    "Cyprian calls the hostility of his rivals old venom aimed at his office as bishop, which he equates with the people's suffrage and God's judgment.",
    ["a claim that the quarrel was only personal or only rhetorical exaggeration",
     "a claim that the rivals' own account of the dispute is heard here",
     "a claim that the election was a modern vote with a ballot and a count"], C),
"lpc.quote.apart-in-heart-united-in-body": (
    "Augustine tells lay hearers to stay in the one Church beside its bad members, apart from them in heart and joined in body, while still correcting those in their charge.",
    ["a claim that bishops disagreeing with bishops appears in this passage",
     "a claim that the threshing-floor image just before it is part of the quoted words",
     "a claim that it permits hearers to ignore wrongdoing"], A),
"lpc.quote.because-i-am-already-weary": (
    "Lucian ends his letter from prison by greeting friends by name and excusing the names he left out because he is already weary.",
    ["a claim about the roles of Saturus, Bassianus or the others he greets",
     "a claim about what became of Lucian or his companions after the letter",
     "a claim that the letter is Cyprian's own"], C),
"lpc.quote.bind-him-justly": (
    "Augustine reads Matthew 18 as telling one believer to bind a wrongdoing brother only justly, and to count him loosed once he is corrected and at peace.",
    ["a claim that it describes formal public penance, excommunication or a bishop readmitting a penitent",
     "a claim that the passage stands without the Matthew 18 steps Augustine quotes just before it",
     "a claim that 'publican' means a keeper of a pub"], A),
"lpc.quote.bishop-of-bishops": (
    "Presiding at the council of 256, Cyprian says no bishop sets himself up as a bishop of bishops or forces a colleague to obey, since each has his own right of judgment.",
    ["a claim that it is an early anti-papal manifesto",
     "a claim that it states a modern principle of separated powers among equal branches",
     "a claim that it was aimed at Stephen of Rome",
     "a claim that ordinary believers or most clergy were formed by this question"], D256),
"lpc.quote.boast-in-nothing-since-nothing-is-our-own": (
    "A heading in Cyprian's handbook of proof texts says we must boast in nothing since nothing is our own, with John and First Corinthians set below it.",
    ["a claim that the words in inner quotation marks are Cyprian's own",
     "a claim that it replies to Pelagius, whose controversy came long after Cyprian",
     "a claim that Cyprian taught the full doctrine of grace that Augustine later argued"], C),
"lpc.quote.chosen-while-still-a-neophyte": (
    "Pontius says Cyprian was chosen bishop by the judgment of God and the favour of the people while still newly baptized and thought a beginner.",
    ["a claim about how the people made their favour known, such as a vote, a count or a ceremony",
     "a claim that Pontius judges Cyprian as an outside witness",
     "a claim that any second witness confirms that Cyprian was a neophyte"], E248),
"lpc.quote.christ-redeemed-in-our-captive-brethren": (
    "Cyprian argues that Christ is to be seen in captive believers, so that the one who redeemed us from death is now to be redeemed from captivity with money.",
    ["a claim that the words in inner quotation marks are Cyprian's own",
     "a claim that 'redeemed' carries only its church sense here",
     "a claim that the ransom succeeded"], C),
"lpc.quote.clamour-and-tears": (
    "Possidius says the Catholics of Hippo seized Augustine and brought him to the bishop to be ordained, demanding it with loud zeal while he wept.",
    ["a claim that it was an orderly election",
     "a claim that it describes Augustine's later consecration as bishop",
     "a claim that Possidius, Augustine's friend, writes as an uninvolved witness"], D391),
"lpc.quote.consider-who-was-there": (
    "Augustine voices a baptized believer answering a Donatist: the One in whose name he believed was there, and that One is everywhere.",
    ["a claim that the 'I' is Augustine baptizing or being baptized",
     "a claim that the Donatist's quoted words are Augustine's own position",
     "a claim that the sermons show a formal ordination or a dispute between bishops"], A),
"lpc.quote.earlier-councils-corrected-by-later": (
    "Augustine ranks Scripture above every later bishop's letter and allows a council to be corrected by a fuller one, so that Cyprian's council could be wrong without Cyprian being cut off.",
    ["a claim naming which later council corrected which earlier one",
     "a claim that 'Catholic' here means a modern denomination",
     "a claim that this theory of council authority organized much of the world"], A),
"lpc.quote.going-out-without-violating-unity": (
    "Augustine teaches that going out from the wicked means reproving and warning them with fitting discipline that does not break unity.",
    ["a claim that every hearer had the same power to discipline, since the passage ties it to rank",
     "a claim that it names the Donatists or can be told without its Isaiah context",
     "a claim that bishops disagreeing with bishops appears here"], A),
"lpc.quote.good-done-to-all-not-only-the-household": (
    "Pontius says the plague relief at Carthage reached everyone and not only believers, and claims more was done than is told of Tobias.",
    ["a claim about who received help, how much, or whether persecutors were among them",
     "a claim that any source outside Pontius describes the relief",
     "a claim that Tobias is anyone other than Tobit of the Book of Tobit"], C),
"lpc.quote.good-works-the-comfort-of-our-dangers": (
    "Augustine tells his hearers that their good lives are the comfort of the dangers of his office, and says that is why he speaks to them at all.",
    ["a claim about what the dangers of the office were",
     "a claim that the earlier sentences on standing in the Apostles' place are part of the quoted words",
     "a claim that 'good conversation' means pleasant talk"], A),
"lpc.quote.grief-and-not-without-tears": (
    "Cyprian opens his reply to eight Numidian bishops by saying he read their news of captured brothers and sisters in great grief and with tears.",
    ["a claim about who took the captives or where",
     "a claim that the opening is only a formal greeting",
     "a claim about what the passage says Cyprian then sent"], C),
"lpc.quote.grieve-with-me-for-my-sister": (
    "Celerinus asks the confessor Lucian to grieve with him over his sister, whom he counts dead in spirit because she offered sacrifice in the persecution.",
    ["a claim that gives the sister a name",
     "a claim that she had physically died",
     "a claim that the letter is Cyprian's, or that the sister's own account survives"], C),
"lpc.quote.he-covered-his-eyes-with-his-own-hand": (
    "The Acta says Cyprian covered his eyes with his own hand, and that two clergy both named Julianus tied the cloths for him.",
    ["a claim that Pontius and the Acta agree on who tied the cloths",
     "a claim that merges the two accounts or settles which is right",
     "a claim that the Acta is a court transcript"], D258),
"lpc.quote.he-slept-with-his-fathers": (
    "Possidius says Augustine died with sight and hearing unimpaired while he and others stood by praying, in Scripture's words that he slept with his fathers.",
    ["a claim about the day or the cause of his death",
     "a claim that the Scripture phrases are Augustine's own words",
     "a claim that any witness other than Possidius describes the sickroom"], D430),
"lpc.quote.it-becomes-us-to-answer-to-our-birth": (
    "In Pontius's report of Cyprian's plague sermon, God shows kindness to strangers as well as his own, so those who call themselves his children must not fall short of it.",
    ["a claim that these are words of a sermon Cyprian wrote down",
     "a claim that the persecutors themselves were helped",
     "a claim that 'aliens' means beings from elsewhere or that 'degenerate' means depraved"], C),
"lpc.quote.let-us-too-be-beheaded-with-him": (
    "The Acta records the crowd of brethren crying that they too should be beheaded with Cyprian, after which an uproar rose and a large crowd followed him.",
    ["a claim that Pontius records this cry",
     "a claim that anyone besides Cyprian was executed",
     "a claim that the cry was a riot"], D258),
"lpc.quote.let-your-creed-be-a-mirror": (
    "Augustine tells candidates for baptism to treat the Creed as a mirror, checking whether they believe all they declare, and as their daily wealth and clothing of the mind.",
    ["a claim that the sermon is about the Creed itself rather than the Lord's Prayer",
     "a claim about the words of the Creed or how often it is said",
     "a claim that 'mind' and 'soul' are the same word in the Latin and the English"], A),
"lpc.quote.longing-expectation-is-a-prayer-for-me": (
    "Augustine tells the people who came to hear him that their longing expectation is itself a prayer for him.",
    ["a claim that it is only flattery of an attentive crowd",
     "a claim about when or where the sermon was preached",
     "a claim about why or how often the congregation attended"], A),
"lpc.quote.no-one-has-the-love-of-god-from-himself": (
    "Augustine reads Paul to say that the love of God is poured into the heart by the Holy Spirit, so that no one can have it from himself.",
    ["a claim that the passage names Paul or the Pelagians",
     "a claim that it replies to the Pelagians",
     "a claim that it sets out a whole doctrine of grace"], A),
"lpc.quote.numidicus-remained-unwillingly": (
    "Cyprian tells Carthage that Numidicus, left half burned under stones after urging others to martyrdom, stayed behind unwillingly and is to join the clergy.",
    ["a claim about where his daughter searched or found him",
     "a claim that gives the wife's or the daughter's name or words",
     "a claim that 'burned, preserved' is a cold word game rather than a naming of a martyr's completion"], C),
"lpc.quote.o-blessed-people-of-the-church": (
    "Pontius calls the people of Carthage blessed for suffering with their bishop in sight, feeling and words, and says their eager wish to die counted as a letter sent to God.",
    ["a claim that anyone besides Cyprian died that day",
     "a claim that 'the priest' means a parish priest rather than the bishop",
     "a claim that the whole congregation suffered martyrdom"], D258),
"lpc.quote.one-good-shepherd-not-many": (
    "Augustine lists Peter, Paul, the other Apostles, holy bishops and blessed Cyprian as good shepherds, and says the Lord spoke of one Shepherd to teach them unity.",
    ["a claim that Augustine and Cyprian agreed or differed on rebaptism",
     "a claim that bishops disagreeing with bishops appears here",
     "a claim that the passage stands without John 10:14, which the next sentence quotes"], A),
"lpc.quote.pardon-through-a-wicked-clergyman": (
    "Augustine says a person who comes to the gathered Church without hypocrisy receives forgiveness of sins in the Holy Spirit, even through a bad cleric, so long as the minister is a Catholic one.",
    ["a claim that 'Catholic' means Roman Catholic",
     "a claim that the passage names the Donatists",
     "a claim about how a clergyman was ordained or removed",
     "a claim that it can be told without the argument on the sin against the Holy Spirit"], A),
"lpc.quote.peter-the-sick-man-and-the-physician": (
    "Augustine calls Peter the sick man and the Lord the physician who feels the pulse of his heart, and says a threefold confession of love answers the threefold denial.",
    ["a claim that Peter is restored to feed the flock in this passage",
     "a claim that it describes a penitential rite or a bishop restoring a penitent",
     "a claim that 'invalid' means a lasting disability"], A),
"lpc.quote.reprove-and-forgive-the-surgeons-knife": (
    "Augustine says correction may use words and, if need be, blows, while the fault is forgiven in the heart, as a surgeon cuts out of kindness.",
    ["a claim that the blows are a church penalty, when they belong to an illustration about unruly boys",
     "a claim that it describes formal public penance or excommunication",
     "a claim that the Latin asks for forgetting the fault"], A),
"lpc.quote.shepherd-wounded-in-the-flock": (
    "Cyprian tells his grieving people that the shepherd is chiefly wounded in the wound of his flock, and that he wails and weeps with them.",
    ["a claim that it is only pastoral sentiment and not a claim about the office",
     "a claim that it describes how readmission of the lapsed worked",
     "a claim that the lapsed give their own account of their fall"], C),
"lpc.quote.shut-up-in-two-cells": (
    "Lucian writes from prison that by the emperor's command the confessors were ordered to die of hunger and thirst, shut up in two cells.",
    ["a claim about what 'the brightness' is, such as a vision or a death",
     "a claim that the Latin of the first sentence is clear",
     "a claim that the letter is Cyprian's"], C),
"lpc.quote.stewards-and-future-bishops": (
    "Augustine tells his people that many of them will one day be dispensers of the Lord's food, and that he too once stood where they stand.",
    ["a claim about when or how Augustine was ordained",
     "a claim that it describes an ordination rite",
     "a claim that 'dispensers' means machines or pharmacists"], A),
"lpc.quote.such-a-one-with-his-friends": (
    "Cyprian objects that certificates are given in one name to admit a person along with his own people, a vague petition he says no martyr ever meant.",
    ["a claim that gives a real person's name for 'such a one'",
     "a claim about the full wording of a certificate",
     "a claim that 'friends' means companions rather than household and kin"], C),
"lpc.quote.thanks-be-to-god": (
    "The Acta gives Cyprian's whole answer to his death sentence as Deo gratias, thanks be to God.",
    ["a claim that Pontius records this answer",
     "a claim that the Acta is a court transcript",
     "a claim that the words show relief or irony"], D258),
"lpc.quote.the-branch-cut-from-the-vine": (
    "Augustine says a branch cut from the vine keeps its visible form but not the life of the root, so the bodily sacraments outside the Church's unity have form without that life.",
    ["a claim that the rite outside is void, since the washing is not repeated for those baptized among schismatics",
     "a claim that Augustine used the word valid",
     "a claim that the sermon shows a formal ordination or a dispute between bishops"], A),
"lpc.quote.the-case-set-before-the-bishop": (
    "Lucian grants peace in the martyrs' name to women who fell, on the condition that each case first goes before the bishop and the sin is openly confessed.",
    ["a claim that the grant stands without its condition that each case go before the bishop",
     "a claim about what the bishop decided for Numeria and Candida",
     "a claim that 'confession' means a private act before a priest"], C),
"lpc.quote.the-creed-first-then-the-prayer": (
    "Augustine tells candidates for baptism that they received the Creed first, to know what to believe, and the Lord's Prayer after it, to know whom to call on.",
    ["a claim that the sermon is about the Creed rather than the Lord's Prayer",
     "a claim that it describes a formal ceremony of handing over the Creed",
     "a claim that the passage names Paul, whose words the first sentence quotes"], A),
"lpc.quote.the-paper-itself": (
    "Cyprian checks a letter from the clergy at Rome by its handwriting, its content and its paper, and sends it back to be compared with what was sent.",
    ["a claim about what had been changed in the letter or by whom",
     "a claim that the letter was proved a forgery",
     "a claim that 'clerical' means office work"], C),
"lpc.quote.the-people-kept-watch-at-the-door": (
    "Pontius says Cyprian spent his last night in gentle custody in an officer's house while the whole people kept watch before the door.",
    ["a claim about how many kept watch",
     "a claim that Cyprian spent the night in a prison cell"], D258),
"lpc.quote.the-psalms-hung-upon-the-wall": (
    "Possidius says Augustine, who taught that even good Christians must repent before death, had penitential psalms copied and read them weeping in his last illness.",
    ["a claim about which psalms they were",
     "a claim that the deathbed was calm",
     "a claim that a second witness confirms the sickroom"], D430),
"lpc.quote.the-sermon-and-the-readings-are-daily-bread": (
    "Augustine names his own preaching, the readings in church and the hymns as daily bread, needed while the people are far from home.",
    ["a claim that the Eucharist was not daily bread",
     "a claim about how often hymns were sung",
     "a claim that 'pilgrimage' means a trip to a shrine"], A),
"lpc.quote.the-trees-and-the-trembling-executioner": (
    "Pontius sets Cyprian's execution among thickly planted trees, with supporters climbing the branches as Zacchaeus did, and says the executioner's trembling hand was strengthened from above.",
    ["a claim that the strengthening of the hand is a fact and not Pontius's telling",
     "a claim that merges Pontius's account of the blindfold with the Acta's",
     "a claim that these details are independently attested, since the Acta tells none of them"], D258),
"lpc.quote.the-whole-people-of-the-brethren-came": (
    "The Acta says the whole Christian people gathered in the street before the officer's lodging, and that Cyprian had the young women among them guarded.",
    ["a claim about what the young women were guarded from",
     "a claim that the Acta is a court transcript",
     "a claim that Pontius gives this detail"], D258),
"lpc.quote.thirteen-letters-sent-to-rome": (
    "Cyprian tells the clergy at Rome that thirteen letters he sent from hiding show his counsel, exhortation and rebuke to the clergy, the confessors and the exiles.",
    ["a claim about which thirteen letters they were",
     "a claim that they were a published book of letters"], C),
"lpc.quote.thousands-of-certificates-daily": (
    "Cyprian says that while the lapsed pressed the martyrs and confessors, thousands of certificates were being given daily without examination, against the law of the Gospel.",
    ["a claim that 'thousands' is a count",
     "a claim that the 'wicked certificates' and the confessors' certificates are one document",
     "a claim that Cyprian said such letters should not exist"], C),
"lpc.quote.two-hear-one-scorns-one-rises": (
    "Augustine marvels that when Christ crucified is preached two hear, one scorns and one rises, and the one who rises is not to claim it as his own.",
    ["a claim that it replies to the Pelagians",
     "a claim that it explains why one hearer rises and the other scorns, such as a doctrine of election",
     "a claim that 'rises' means the resurrection"], A),
"lpc.quote.walled-in-by-a-mingled-multitude": (
    "Pontius says Cyprian went out from the officer's house walled in on all sides by a mingled multitude.",
    ["a claim about the size of the crowd",
     "a claim that everyone in the crowd was a Christian"], D258),
"lpc.quote.what-is-done-by-you-he-does-in-you": (
    "Augustine explains the petition 'Thy will be done in heaven and in earth' by saying that what is done by you, God himself does in you.",
    ["a claim that it teaches compulsion, when read without its lead-in on God's will done in everyone",
     "a claim that it replies to the Pelagians",
     "a claim that the opening question was an objection raised by a hearer"], A),
"lpc.quote.ye-belong-to-my-care": (
    "Augustine tells his hearers they belong to his care so that he may give a good account of them, and that before God he has spoken and wept when not heard.",
    ["a claim about the date, place or occasion of the sermon",
     "a claim that the closing prayer is Scripture",
     "a claim that the sentence before it, calling the hearers a Catholic people not divided from unity, is part of the quoted words"], A),
}

WITNESSES = {
"lpc.witness.almsgiving-quenches-sin": (
    "Cyprian taught that almsgiving is the ordinary remedy for sin committed after baptism, and spoke directly to rich believers about what their wealth was for.",
    ["a claim that the teaching sets a limit on how much a believer may keep",
     "a claim that it gives a full account of marriage, courtship or the wedding",
     "a claim that the quoted line about water and fire is Cyprian's own composition and not Scripture"], C),
"lpc.witness.answerability-as-ground": (
    "In the world's own reading, a bishop's answerability for a particular people is the one root from which the road back, the weight of the font and disagreement without separation all grow.",
    ["a claim that any source states this unity of the concerns in these terms, since it is this build's own synthesis",
     "a claim that answerability settles every hard case, such as the font answered twice in opposite ways",
     "a claim that the two bishops answered the font question alike"], W),
"lpc.witness.apostolic-succession-of-bishops": (
    "Augustine traced the bishops' office to the apostles by naming the line of Roman bishops from Peter, while Cyprian stated the principle and the practice but gave no list.",
    ["a claim that Cyprian drew up a name list of his own",
     "a claim that either bishop's account is all a modern listener means by apostolic succession"], W),
"lpc.witness.baptism-traced-to-the-apostles": (
    "Augustine said the refusal to rebaptize those baptized among heretics and the baptism of infants are rightly believed to come from the apostles, though no apostle's writing says so.",
    ["a claim that a written apostolic text gives either practice",
     "a claim that Augustine traces catechesis or the road back to the apostles by name",
     "a claim that Cyprian shared Augustine's test of apostolic origin"], A),
"lpc.witness.blamed-for-the-worlds-troubles": (
    "A Roman official named Demetrianus charged Christians with causing wars, plague and famine by refusing the old gods, and Cyprian wrote a whole reply.",
    ["a claim that the neighbour's own words survive, since the charge is reported in Cyprian's reply",
     "a claim about whether Christians hid in catacombs",
     "a claim about what an outsider found strangest about them"], C),
"lpc.witness.communion-over-separation": (
    "Cyprian's council of 256 kept colleagues in communion despite disagreement, and Augustine later argued its ruling wrong without putting Cyprian outside, after early separations had shown what a break costs.",
    ["a claim that the church never broke communion",
     "a claim that a source states the link between those early separations and the rule, which is a synthesis",
     "a claim that Cyprian and Augustine reached the same ruling"], W),
"lpc.witness.confessor-claim-vs-regulated-peace": (
    "Confessors who had suffered claimed standing to ask peace for the lapsed, and the regulated process of examination before the congregation had to answer that claim, with the two never joined in one settled rule.",
    ["a claim that the confessors' claim was a pretense or counted for nothing",
     "a claim that the church found a single rule saying which governs when the two conflict",
     "a claim that the confessors' own voice survives beyond a general letter to Cyprian"], C),
"lpc.witness.constantine-did-not-corrupt": (
    "Answering Petilian, Augustine called Constantine no foe to the Christian name, and in City of God he said God let Constantine gain great power to show that earthly greatness never depended on the old gods.",
    ["a claim that Augustine was a neutral witness, since Petilian's side had asked Constantine to judge and he ruled against them",
     "a claim that Augustine thought friendship with kings always safe",
     "a claim that Constantine's success proved a Christian's standing before God"], (400, 413)),
"lpc.witness.days-before-the-sun": (
    "Augustine admitted that Genesis reports three days before the sun and that what light made them lies beyond human senses, while holding that by Scripture's reckoning under 6,000 years had passed.",
    ["a claim that Augustine explained how those first days worked",
     "a claim that the histories he rejected as mendacious are described in their own words here"], (413, 430)),
"lpc.witness.grant-me-chastity-but-not-yet": (
    "As a young man Augustine prayed for chastity but not yet, and he later wrote that being persuaded of the truth did not by itself set him free.",
    ["a claim that everyone among them struggled in the same way",
     "a claim that delay always ended as his did",
     "a claim that the prayer was made at the moment he was persuaded"], A),
"lpc.witness.heard-for-salvation-not-for-wish": (
    "Augustine taught from Paul's thorn that the saints are always heard in what concerns their salvation, even when they are not heard as they wished.",
    ["a claim that God removed Paul's thorn",
     "a claim that Augustine promised any wish would be answered"], A),
"lpc.witness.marriage-a-threefold-good": (
    "Augustine defended marriage against those who thought praising virginity condemned it, naming offspring, faithfulness and sacrament as its goods.",
    ["a claim about courtship, weddings or attendance at them",
     "a claim that separation ended the marriage bond",
     "a claim that the translator's preface is Augustine's own words"], A),
"lpc.witness.restless-heart-and-the-unrepentant-enemy": (
    "Augustine said the heart is restless because it was made for God, and elsewhere ranked loving an unrepentant enemy as the highest standard, with forgiving one who asks as an ordinary standard.",
    ["a claim that he thought everyone reaches the highest standard in full",
     "a claim that God forgives one who refuses from the heart to forgive someone who asks",
     "a claim that the two passages come from one work"], A),
"lpc.witness.scripture-above-councils": (
    "Augustine placed the canon of Scripture above every later bishop's letter and council, and Cyprian held that custom without truth is only the old age of error.",
    ["a claim that Scripture was the church's only authority",
     "a claim that bishops and councils had no binding authority",
     "a claim that the two bishops argued the same dispute"], W),
"lpc.witness.the-only-son-and-the-trinity": (
    "Augustine's confession of Jesus as God's only Son and of the Holy Spirit as completing the Trinity was disputed by the Arian bishop Maximinus at a public conference in Hippo.",
    ["a claim that this doctrine is where this world's own material is most distinctive",
     "a claim that the doctrine went unchallenged",
     "a claim about how the conference with Maximinus ended"], A),
"lpc.witness.the-pattern-we-are-modelled-on": (
    "Augustine taught that Christ's cross, burial, rising and ascension were ordered as the pattern for the believer's life, worked out in ordinary life.",
    ["a claim that this exhausts who Jesus was to them or what he taught",
     "a claim that the record preserves a developed telling of his life as its own story",
     "a claim that the pattern is only mystical"], A),
"lpc.witness.tradition-tested-by-apostolic-warrant": (
    "Cyprian refused any practice not found in the Gospel or the apostles' letters, while Augustine counted a custom kept everywhere as apostolic even without apostolic writing.",
    ["a claim that the two bishops agreed on one test",
     "a claim that this world settled which test is truer",
     "a claim that the two bishops argued the same dispute"], W),
"lpc.witness.violence-commanded-not-cruel": (
    "Augustine, once disturbed by the violence of the Old Testament, answered a Manichaean that Moses showed obedience and not ferocity, and that God acted in righteous retribution.",
    ["a claim that this settles the question for a modern reader",
     "a claim that the answer lacked moral seriousness",
     "a claim that a command carried out is the same act as the same deed chosen on one's own account"], A),
}

TERMS = {
"lpc.term.bishop-of-bishops": (
    "The term names the rule stated at the council of 256 that no bishop stands over another, each judging for himself and answering to Christ.",
    ["a claim that it is an early anti-papal manifesto or a modern separation of powers",
     "a claim that it was aimed at Stephen of Rome",
     "a claim that ordinary believers or most clergy were formed by this question"], D256),
"lpc.term.catechesis": (
    "Catechesis was the teaching of the creed and the basics of belief to people before baptism, and Augustine wrote a manual for those who do it.",
    ["a claim that it was a children's catechism of memorized questions and answers",
     "a claim that it was an organizing force of its own and not the medium formation was taught through",
     "a claim that the creed was taught after the water"], W),
"lpc.term.certificates-letters-of-peace": (
    "A certificate was a confessor's letter for a lapsed person, asking for or granting peace, which Cyprian wanted to name the person and come from someone who knew him.",
    ["a claim that it is the same paper as the Decian sacrifice certificate",
     "a claim that Cyprian opposed such letters outright",
     "a claim that the confessors' side is heard beyond one general letter",
     "a claim that thousands were given, a wording that comes from an editor and not from Cyprian"], C),
"lpc.term.communion": (
    "Communion is a real standing inside the one body, which can be lost and given back, and which Cyprian held should survive sharp disagreement.",
    ["a claim that it names only a rite or a general warmth of fellowship",
     "a claim that either bishop used this word for the cross-phase pattern, which is this build's own synthesis"], W),
"lpc.term.compel-them-to-come-in": (
    "The phrase 'compel them to come in' names Augustine's late argument from the parable of the feast that a Christian ruler may use force to bring a separated group back into one communion.",
    ["a claim that it is the church's settled endorsement of religious persecution throughout",
     "a claim that Augustine always held it, since his earlier opinion against coercion reaches us only through his own later account",
     "a claim that a Donatist answer to it survives",
     "a claim that an editor's verdict on Augustine's exegesis belongs to this record"], A),
"lpc.term.confessor": (
    "A confessor was one who was questioned for the Name, did not deny it, and lived, and in Cyprian's time that standing could rival a bishop's authority.",
    ["a claim that a confessor was a priest who hears confessions",
     "a claim that the word carries this sense in Augustine's phase",
     "a claim that confessors speak for themselves beyond a few letters"], C),
"lpc.term.grace": (
    "Grace is the insistence that no effort of ours is enough on its own, and that any good a person does was given first.",
    ["a claim that it means general benevolence or grace under pressure",
     "a claim that Pelagius himself held the position Augustine reports",
     "a claim that Cyprian taught it as an organizing concern",
     "a claim that it settles the Catholic and Protestant disagreements over grace"], A),
"lpc.term.heresy": (
    "The word raises the question whether a baptism given outside the church counts, which Cyprian's council answered no and Augustine, a century and a half later, answered by saying it was truly given.",
    ["a claim that it names a settled malicious deviation from an agreed orthodoxy",
     "a claim that De Unitate bears on Cyprian's argument against Stephen",
     "a claim that the question was closed and not argued by both sides"], W),
"lpc.term.libellatici-sacrificati": (
    "Cyprian divided the lapsed into those who bought a certificate and those who sacrificed, and treated both as fallen but not alike.",
    ["a claim that it was a formal canonical taxonomy applied uniformly",
     "a claim that the two acts weighed the same",
     "a claim that the grading rests on an editor's endnote"], C),
"lpc.term.libelli": (
    "A libellus was a paper saying a person had sacrificed, which some bought without sacrificing, and Cyprian counted its holders among the lapsed.",
    ["a claim that it was a modern identity document or licence",
     "a claim that the Latin word appears in the English volume, which renders it certificates",
     "a claim that Latin libellus names only this paper"], C),
"lpc.term.plenary-council": (
    "The term names Augustine's rule that narrower councils yield to wider ones while even the widest can later be corrected when experience reveals what was hidden.",
    ["a claim that it is a plain claim of central institutional authority",
     "a claim that it restates Cyprian's formula",
     "a claim that the question reached ordinary formation in either phase"], A),
"lpc.term.preaching": (
    "Preaching was the regular address to the whole church, baptized or still learning, and the main way what the church held reached an ordinary believer.",
    ["a claim that it was a stern monologue or a polished performance among several parts of a service",
     "a claim that it was an organizing force of its own",
     "a claim that how often the word occurs measures its weight"], W),
"lpc.term.reconciliation-penitential-discipline": (
    "Reconciliation was a public road, walked in stages and held by the bishop, by which a failed member returned to the community.",
    ["a claim that it was a private confession said alone",
     "a claim that it was complete once both parties felt differently",
     "a claim that the reconciled believer's own account survives"], C),
"lpc.term.schism": (
    "Schism is the tear that comes when arguing stops and a separate altar, bishop and people appear in the same town.",
    ["a claim that it was an ordinary feature of a plural religious landscape",
     "a claim that the line between heresy and schism was as stable as later usage implies",
     "a claim that this entry characterizes Donatism"], W),
"lpc.term.suffrage": (
    "Suffrage names the voice of the people that, joined to God's judgment, put a man into office, even against his own wishes.",
    ["a claim that it was a vote with a ballot and a fixed procedure",
     "a claim that both phases share one word for it, when it is a pattern named from different figures and words",
     "a claim that Augustine's episcopate came by the people's choice alone"], W),
"lpc.term.the-flock": (
    "The flock is the particular people one bishop is given in one place, for whom he answers and who can hold him to it.",
    ["a claim that it is a sentimental name for churchgoers or the church in general",
     "a claim that Augustine used the image as often as Cyprian",
     "a claim that the bishop is a remote regional administrator"], W),
"lpc.term.the-lapsed": (
    "The lapsed were the church's own people who gave in to the order to sacrifice, by sacrificing or by buying a certificate, and who then asked to come back.",
    ["a claim that they drifted away gradually, as a modern believer might",
     "a claim that a lapsed believer's own account survives",
     "a claim that their standing was a private matter with no public consequence"], C),
"lpc.term.the-one-episcopate": (
    "The episcopate is one undivided office, each bishop holding his part of it for the whole.",
    ["a claim that it is a ranked hierarchy or a federation of independent officers",
     "a claim that De Unitate carries Cyprian's argument against Stephen",
     "a claim that either recension of De Unitate chapters 4 and 5 grounds the term"], W),
"lpc.term.the-people": (
    "The people names the congregation when it acts, consenting, demanding and electing, unlike the flock, which is the congregation being cared for.",
    ["a claim that the Latin plebs is settled as the world's word for it",
     "a claim that the people held a formal ballot",
     "a claim that the people always prevailed"], W),
}

STORIES = {
"lpc.story.celerinus-writes-to-lucian": (
    "The confessor Celerinus asked Lucian, another confessor in prison, to grant peace to his sister and two other women who had fallen, and Lucian did so on condition that each case go before the bishop.",
    ["a claim that gives words to Celerinus's sister, Numeria or Candida, none of whom speaks in our record",
     "a claim that Lucian's grant stood without his condition that each case be set before the bishop",
     "a claim that the confessors were either usurpers or heroes"], C),
"lpc.story.election-of-cyprian": (
    "Pontius reports that Cyprian was chosen bishop by God's judgment and the people's favour while newly baptized, and Cyprian later called that acclamation his people's suffrage joined to God's judgment.",
    ["a claim that it was a vote with a candidacy and a count",
     "a claim that any witness besides Pontius confirms that Cyprian was a neophyte",
     "a claim that Pontius, writing in praise, is a neutral witness"], E248),
"lpc.story.hundred-thousand-sesterces": (
    "Cyprian told eight Numidian bishops that Christ is to be seen in captive believers, and sent one hundred thousand sesterces gathered from his church's clergy and people.",
    ["a claim about what the sum was worth in modern money",
     "a claim that the ransom worked",
     "a claim about what share of anything the sum represented"], C),
"lpc.story.numidicus": (
    "Cyprian told Carthage he was adding the presbyter Numidicus to the clergy, a man who watched his wife burned, was left for dead, was found alive by his daughter, and stayed behind unwillingly.",
    ["a claim that gives words to Numidicus, his wife or his daughter",
     "a claim about where the daughter searched",
     "a claim that 'burned, preserved' is a cruel word game and not a martyr's death named as completion"], C),
"lpc.story.the-death-of-cyprian": (
    "Pontius's Life and the Acta both tell Cyprian's death on 14 September 258 and agree on its core, but differ on who tied the cloths over his eyes.",
    ["a claim that the executioner's hand was strengthened from above, which is only how Pontius tells it",
     "a claim that the two texts agree on who tied the cloths",
     "a claim that the Acta is a court transcript",
     "a claim that any spectator's own account survives"], D258),
"lpc.story.the-plague-and-the-enemies": (
    "Pontius reports that in the plague at Carthage Cyprian preached love of enemies and help for everyone, and that relief followed which reached beyond believers.",
    ["a claim that the persecutors themselves were helped",
     "a claim that any source outside Pontius describes the relief",
     "a claim that the sermon survives in Cyprian's own hand",
     "a claim that a pagan Carthaginian's account of being helped survives"], C),
"lpc.story.the-psalms-on-the-wall": (
    "Possidius tells how Augustine, who taught that even good Christians must repent before death, had penitential psalms copied and wept over them in his last illness during the Vandal siege.",
    ["a claim that the death was serene",
     "a claim that any witness besides Possidius describes the sickroom",
     "a claim about what leaving Hippo was like"], D430),
}

LIMITS = {
"lpc.limit.411-gesta-unread": (
    "The record dates the 411 conference but has not validly read its transcript, so it cannot say how bishops beyond Cyprian and Augustine argued authority.",
    ["a claim that the transcript shows how widely conciliar theory spread",
     "a claim about what was argued bishop by bishop",
     "a claim that the acts have been read in full"], D411),
"lpc.limit.apostolic-origin-undefended": (
    "Augustine traces infant baptism, the refusal to rebaptize and the office of bishop to the apostles, but catechesis, the road back and teaching before the water are not traced to the apostles by name.",
    ["a claim that catechesis, the road back or teaching before the water is traced to the apostles",
     "a claim that the oneness of the episcopate is a traced lineage"], W),
"lpc.limit.no-chain-of-witnesses": (
    "No one in the record names an eyewitness of the resurrection or claims a living memory passed back to one, and Augustine reasons from the apostles' written testimony instead.",
    ["a claim that anyone among them knew someone who saw Jesus",
     "a claim that the argument rests on a chain of living memory"], W),
"lpc.limit.ordinary-interior-life": (
    "The record gives what bishops decided about believers but almost never what an ordinary believer felt, apart from Augustine's weeping at his own baptism, written years afterward.",
    ["a claim that Augustine's account of his baptism shows ordinary believers' experience",
     "a claim that an ordinary believer's own account survives",
     "a claim about what believers felt at the font or in the congregation"], W),
"lpc.limit.rural-punic-berber-life": (
    "The record comes from two urban sees and says almost nothing about rural congregations or the Punic- and Berber-speaking life around them.",
    ["a claim that rural congregations lived as the cities did",
     "a claim about Punic or Berber Christian practice"], W),
"lpc.limit.the-lapsed-own-account": (
    "The lapsed left nothing in their own words, so every account of them is a bishop's account written to decide what should be done.",
    ["a claim about why a particular person gave way",
     "a claim that a lapsed believer judged the terms of return just",
     "a claim that a first-person text from a lapsed believer survives"], C),
"lpc.limit.the-outsiders-own-view": (
    "The record cannot say whether Christians hid in catacombs or what an outsider found strangest about them, though Demetrianus's charge and Augustine's answer on Constantine survive.",
    ["a claim that Christians hid in catacombs",
     "a claim that an outsider's own words survive",
     "a claim that Augustine asked whether Constantine corrupted the church in those words"], W),
"lpc.limit.the-silent-century": (
    "Between Cyprian's death in 258 and Augustine's ordination in 391 the world's own pastoral voice is absent, so far as this build has weighed it, with nine tractatus in Morin's 1917 edition still unassessed.",
    ["a claim that nothing happened in those years",
     "a claim that the silence is settled, since the Morin tractatus are not yet assessed",
     "a claim that fills the silence from the Donatist world's sources"], (258, 391)),
"lpc.limit.womens-own-voice": (
    "The women who appear in either phase, such as Numeria, Candida and Albina, are met through men's words, and the record holds nothing a woman wrote herself.",
    ["a claim that a woman's own writing survives",
     "a claim that a woman's spoken words set down by a man are her own writing"], W),
}

CONTESTED = {
"lpc.contested.compel-coercion-development": (
    "Whether Augustine's three-phase path on coercion was a real change of mind or a later self-presentation stays open, since his earlier opinion reaches us only through his own retrospective account.",
    ["a claim that the change of mind is established as genuine",
     "a claim that it is shown to be a later construction",
     "a claim that Cyprian's corpus has anything corresponding to it",
     "a claim that a contemporaneous statement of the earlier view survives"], A),
"lpc.contested.cyprian-death-genre": (
    "Whether Pontius's account of Cyprian's death is direct testimony or a saint's life shaped by Scripture stays open, though the execution under Valerian in 258 is not in dispute.",
    ["a claim that the Scriptural patterning shows the account cannot be trusted",
     "a claim that the question of which Construction Framework clause governs is settled",
     "a claim that the strengthened hand of the executioner is a fact"], D258),
"lpc.contested.de-unitate-recensions": (
    "Whether the 'Primacy Text' of De Unitate chapters 4 and 5 is a later interpolation or Cyprian's own second recension stays unsettled, though the treatise's subject, schism and the one episcopate around 251, is not.",
    ["a claim that the interpolation thesis is settled",
     "a claim that Cyprian wrote both recensions",
     "a claim that any reasoning in this world rests on either recension's wording"], (251, 251)),
"lpc.contested.grace-pelagius-characterization": (
    "Whether Augustine's anti-Pelagian works describe Pelagius's own position fairly stays open, since what this record has to go on is Augustine's report of that position.",
    ["a claim that Augustine's report is the position Pelagius held",
     "a claim that later Reformation-era and modern uses of the controversy continue terms Augustine set correctly",
     "a claim that Pelagius's own words survive in this record"], A),
}

GRAVITIES = {
"lpc.gravity.collegial-communion-preserved": (
    "Bishops in this world disagreed sharply yet worked to keep communion and not build a rival hierarchy, from Cyprian's preface to the council of 256 to Augustine arguing against Cyprian without casting him out.",
    ["a claim that the pattern across both phases is better than a synthesis rated Widely Accepted",
     "a claim that bishops never broke communion"], W),
"lpc.gravity.conciliar-authority-theory": (
    "Two competing theories of council authority are attested, Cyprian's egalitarian one and Augustine's appeal to plenary councils, but how far they organized the world is thinly evidenced.",
    ["a claim that conciliar authority was a major organizing concern",
     "a claim that the two theories reconcile into one",
     "a claim that the question reached ordinary believers"], W),
"lpc.gravity.confessor-authority-vs-episcopal-peace": (
    "The confessors' informal claim to grant peace to the lapsed and Cyprian's bishop-run penance pulled against each other, and neither won.",
    ["a claim that the tension was resolved",
     "a claim that evidence beyond Cyprian's letters, read through one term, supports it",
     "a claim that the confessors were either usurpers or heroes"], C),
"lpc.gravity.grace-and-human-incapacity": (
    "Augustine's thirteen anti-Pelagian works make grace and human incapacity a large concern in his phase, resting on one voice in one body of work.",
    ["a claim that it spans both phases",
     "a claim that the volume of text shows breadth",
     "a claim that Pelagius's own view is known"], A),
"lpc.gravity.pastoral-office-flock-keeping": (
    "A bishop is personally answerable for a bounded flock, and much else in this world flows from that office.",
    ["a claim that the bishop was a regional administrator",
     "a claim that Possidius's Vita counts as evidence in the cross-check"], W),
"lpc.gravity.penitential-discipline": (
    "Taking back the failed instead of shutting them out sat near the center of the world's life, and this concern is documented in Cyprian's phase alone.",
    ["a claim that it spans both phases under this name",
     "a claim that the rival routes of Novatianist rigor or Felicissimus laxity were the church's own",
     "a claim that the process was private confession"], C),
"lpc.gravity.preaching-and-catechesis": (
    "Preaching and catechesis were the channel through which the world's central concerns reached believers, a supporting concern that organizes little by itself.",
    ["a claim that preaching and catechesis organize the world by themselves",
     "a claim that other concerns lean on it as they lean on the office, penance and communion"], W),
"lpc.gravity.sacramental-ordination-validity": (
    "Cyprian and Augustine answered in opposite ways whether a baptism or ordination given outside the church is valid, and both argued it at length more than a century apart.",
    ["a claim that the two answered alike",
     "a claim that the disagreement broke communion",
     "a claim that the question is thin the way conciliar authority is"], W),
}

NOTES = {**QUOTES, **WITNESSES, **TERMS, **STORIES, **LIMITS, **CONTESTED, **GRAVITIES}

_TOP_KEY = re.compile(r"^[A-Za-z_]+:")


def note_block(means: str, not_for: list[str], years: tuple[int, int]) -> list[str]:
    lines = ["use_note:", f"  means: {json.dumps(means, ensure_ascii=False)}", "  not_for:"]
    lines.extend(f"    - {json.dumps(line, ensure_ascii=False)}" for line in not_for)
    lines.append(f"  years: {{from: {years[0]}, to: {years[1]}}}")
    lines.append("  status: reviewed")
    return lines


def with_note(text: str, block: list[str]) -> str:
    """Put the block before the front matter's `confidence:` key, replacing
    any use_note already there."""
    head, sep, rest = text.partition("\n---\n")
    if not text.startswith("---\n") or not sep:
        raise ValueError("record has no front matter")
    lines = head.split("\n")
    out: list[str] = []
    skipping = False
    for line in lines:
        if line.startswith("use_note:"):
            skipping = True
            continue
        if skipping:
            if _TOP_KEY.match(line):
                skipping = False
            else:
                continue
        out.append(line)
    if out.count("confidence:") != 1:
        raise ValueError("expected exactly one top-level confidence: line")
    at = out.index("confidence:")
    out[at:at] = block
    return "\n".join(out) + sep + rest


def apply_notes() -> list[str]:
    touched = []
    for rid, (means, not_for, years) in NOTES.items():
        matches = list(RECORDS_ROOT.glob(f"*/{rid}.md"))
        if len(matches) != 1:
            raise FileNotFoundError(f"expected one record file for {rid}, found {len(matches)}")
        path = matches[0]
        text = path.read_text(encoding="utf-8")
        new_text = with_note(text, note_block(means, not_for, years))
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
        touched.append(str(path.relative_to(REPO_ROOT)))
    return touched


def main() -> None:
    touched = apply_notes()
    print(f"use_note set on {len(touched)} records")


if __name__ == "__main__":
    main()
