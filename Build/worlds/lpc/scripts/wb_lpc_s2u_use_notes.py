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
B395 = (395, 430)
E251 = (248, 251)

QUOTES = {
"lpc.quote.a-dreadful-plague-broke-out": (
    "Pontius says in the plague Carthage shuddered, fled, cast out its own people and left the dead in the streets.",
    ["a claim about how many died or what the disease was",
     "a claim that Pontius is an outside witness, since he wrote in praise of his bishop",
     "a claim that 'their own friends' means companions rather than the household and kin the Latin names"], C),
"lpc.quote.a-hundred-thousand-sesterces": (
    "Cyprian says his church sent 100,000 sesterces to buy back captive believers.",
    ["a claim about what the sum was worth in modern money",
     "a claim that the ransom freed anyone",
     "a claim about what share of the church's wealth the sum was"], C),
"lpc.quote.a-standard-bearer-of-the-sect": (
    "Pontius reports a sentence calling Cyprian an enemy of the gods, with discipline to be made firm by his blood.",
    ["a claim that 'discipline' in the sentence means punishment rather than restored order",
     "a claim that Pontius and the Acta are independent witnesses to the wording of the sentence",
     "a claim about the details of the dream Pontius mentions earlier"], D258),
"lpc.quote.ancient-venom-against-my-episcopate": (
    "Cyprian calls his rivals' anger old venom aimed at his office, which he ties to the people's voice and God's judgment.",
    ["a claim that the quarrel was only personal or only rhetorical exaggeration",
     "a claim that the rivals' own account of the dispute is heard here",
     "a claim that the election was a modern vote with a ballot and a count"], C),
"lpc.quote.apart-in-heart-united-in-body": (
    "Augustine tells lay hearers to stay in the Church beside its bad members, apart in heart, and to correct those in their charge.",
    ["a claim that bishops disagreeing with bishops appears in this passage",
     "a claim that the threshing-floor image just before it is part of the quoted words",
     "a claim that it permits hearers to ignore wrongdoing"], A),
"lpc.quote.because-i-am-already-weary": (
    "Lucian ends his prison letter by greeting friends by name and excusing those he left out because he is weary.",
    ["a claim about the roles of Saturus, Bassianus or the others he greets",
     "a claim about what became of Lucian or his companions after the letter",
     "a claim that the letter is Cyprian's own"], C),
"lpc.quote.bind-him-justly": (
    "Augustine says to bind a wrongdoing brother only justly, and to count him loosed once he is corrected.",
    ["a claim that it describes formal public penance, excommunication or a bishop readmitting a penitent",
     "a claim that the passage stands without the Matthew 18 steps Augustine quotes just before it",
     "a claim that 'publican' means a keeper of a pub"], A),
"lpc.quote.bishop-of-bishops": (
    "At the council of 256, Cyprian says no bishop makes himself a bishop of bishops, and each has his own right of judgment.",
    ["a claim that it is an early anti-papal manifesto",
     "a claim that it states a modern principle of separated powers among equal branches",
     "a claim that Cyprian's words name Stephen as their target",
     "a claim that ordinary believers or most clergy were formed by this question"], D256),
"lpc.quote.boast-in-nothing-since-nothing-is-our-own": (
    "A heading in Cyprian's handbook of proof texts says we must boast in nothing, since nothing is our own.",
    ["a claim that the words in inner quotation marks are Cyprian's own",
     "a claim that it replies to Pelagius, whose controversy came long after Cyprian",
     "a claim that Cyprian taught the full doctrine of grace that Augustine later argued"], C),
"lpc.quote.chosen-while-still-a-neophyte": (
    "Pontius says God and the people's favour made Cyprian bishop, though he was new to the faith.",
    ["a claim about how the people made their favour known, such as a vote, a count or a ceremony",
     "a claim that Pontius judges Cyprian as an outside witness",
     "a claim that any second witness confirms that Cyprian was a neophyte"], E248),
"lpc.quote.christ-redeemed-in-our-captive-brethren": (
    "Cyprian says Christ is to be seen in captive believers, so ransoming them redeems the one who redeemed us.",
    ["a claim that the words in inner quotation marks are Cyprian's own",
     "a claim that 'redeemed' carries only its church sense here",
     "a claim that the ransom succeeded"], C),
"lpc.quote.clamour-and-tears": (
    "Possidius says a crowd at Hippo seized Augustine and loudly told their bishop to make him a priest, while he wept.",
    ["a claim that it was an orderly election",
     "a claim that it describes Augustine's later consecration as bishop",
     "a claim that Possidius, Augustine's friend, writes as an uninvolved witness"], D391),
"lpc.quote.consider-who-was-there": (
    "Augustine has a man tell a Donatist that the One he believed in was there, and is everywhere.",
    ["a claim that the 'I' is Augustine baptizing or being baptized",
     "a claim that the Donatist's quoted words are Augustine's own position",
     "a claim that the sermons show a formal ordination or a dispute between bishops"], A),
"lpc.quote.earlier-councils-corrected-by-later": (
    "Augustine says a later, wider council can correct an earlier one, and Scripture stands above them all.",
    ["a claim naming which later council corrected which earlier one",
     "a claim that 'Catholic' here means a modern denomination",
     "a claim that this theory of council authority organized much of the world"], A),
"lpc.quote.going-out-without-violating-unity": (
    "Augustine says going out from the wicked means warning them with discipline that keeps unity.",
    ["a claim that every hearer had the same power to discipline, since the passage ties it to rank",
     "a claim that it names the Donatists or can be told without its Isaiah context",
     "a claim that bishops disagreeing with bishops appears here"], A),
"lpc.quote.good-done-to-all-not-only-the-household": (
    "Pontius says plague relief in Carthage reached all, not only believers, and outdid what is told of Tobias.",
    ["a claim about who received help, how much, or whether persecutors were among them",
     "a claim that any source outside Pontius describes the relief",
     "a claim that Tobias is anyone other than Tobit of the Book of Tobit"], C),
"lpc.quote.good-works-the-comfort-of-our-dangers": (
    "Augustine tells his hearers that their good lives comfort him in the dangers of his office.",
    ["a claim about what the dangers of the office were",
     "a claim that the earlier sentences on standing in the Apostles' place are part of the quoted words",
     "a claim that 'good conversation' means pleasant talk"], B395),
"lpc.quote.grief-and-not-without-tears": (
    "In reply to eight Numidian bishops, Cyprian says he read of captives with great grief and tears.",
    ["a claim about who took the captives or where",
     "a claim that the opening is only a formal greeting",
     "a claim about what the passage says Cyprian then sent"], C),
"lpc.quote.grieve-with-me-for-my-sister": (
    "Celerinus asks Lucian to grieve for his sister, who made a sacrifice and is dead in spirit.",
    ["a claim that gives the sister a name",
     "a claim that she had physically died",
     "a claim that the letter is Cyprian's, or that the sister's own account survives"], C),
"lpc.quote.he-covered-his-eyes-with-his-own-hand": (
    "The Acta says Cyprian covered his own eyes, and two clergy both named Julianus tied the cloths for him.",
    ["a claim that Pontius and the Acta agree on who tied the cloths",
     "a claim that merges the two accounts or settles which is right",
     "a claim that the Acta is a court transcript"], D258),
"lpc.quote.he-slept-with-his-fathers": (
    "Possidius says Augustine died with clear sight and hearing while others prayed.",
    ["a claim about the day or the cause of his death",
     "a claim that the Scripture phrases are Augustine's own words",
     "a claim that any witness other than Possidius describes the sickroom"], D430),
"lpc.quote.it-becomes-us-to-answer-to-our-birth": (
    "In Pontius's report of Cyprian's plague sermon, God shows kindness even to strangers, so his children must not fall short.",
    ["a claim that these are words of a sermon Cyprian wrote down",
     "a claim that the persecutors themselves were helped",
     "a claim that 'aliens' means beings from elsewhere or that 'degenerate' means depraved",
     "a claim that the critical Latin text names strangers, which only older editions print"], C),
"lpc.quote.let-us-too-be-beheaded-with-him": (
    "The Acta records the brethren crying that they too should be beheaded with Cyprian, and a large crowd then followed him.",
    ["a claim that Pontius records this cry",
     "a claim that anyone besides Cyprian was executed",
     "a claim that the cry was a riot"], D258),
"lpc.quote.let-your-creed-be-a-mirror": (
    "Augustine tells candidates for baptism to treat the Creed as a mirror and as the daily wealth and clothing of the mind.",
    ["a claim that the sermon is about the Creed itself rather than the Lord's Prayer",
     "a claim about the words of the Creed or how often it is said",
     "a claim that 'mind' and 'soul' are the same word in the Latin and the English"], A),
"lpc.quote.longing-expectation-is-a-prayer-for-me": (
    "Augustine tells the people who came to hear him that their longing expectation is itself a prayer for him.",
    ["a claim that it is only flattery of an attentive crowd",
     "a claim about when or where the sermon was preached",
     "a claim about why or how often the congregation attended"], A),
"lpc.quote.no-one-has-the-love-of-god-from-himself": (
    "Augustine reads Paul to say God's love is poured into the heart by the Holy Spirit, so no one has it from himself.",
    ["a claim that the passage names Paul or the Pelagians",
     "a claim that it replies to the Pelagians",
     "a claim that it sets out a whole doctrine of grace"], A),
"lpc.quote.numidicus-remained-unwillingly": (
    "Cyprian says Numidicus, left for dead, stayed behind against his will and joins the presbyters.",
    ["a claim about where his daughter searched or found him",
     "a claim that gives the wife's or the daughter's name or words",
     "a claim that 'burned, preserved' is a cold word game rather than a naming of a martyr's completion",
     "a claim that the Latin certainly says 'unconquered' rather than 'unwillingly'"], C),
"lpc.quote.o-blessed-people-of-the-church": (
    "Pontius calls the people of Carthage blessed for suffering with their bishop, and says their wish to die counted as a letter to God.",
    ["a claim that anyone besides Cyprian died that day",
     "a claim that 'the priest' means a parish priest rather than the bishop",
     "a claim that the whole congregation suffered martyrdom"], D258),
"lpc.quote.one-good-shepherd-not-many": (
    "Augustine calls Peter, Paul, the bishops and Cyprian good shepherds, yet says the Lord named one Shepherd.",
    ["a claim that Augustine and Cyprian agreed or differed on rebaptism",
     "a claim that bishops disagreeing with bishops appears here",
     "a claim that the passage stands without John 10:14, which the next sentence quotes"], A),
"lpc.quote.pardon-through-a-wicked-clergyman": (
    "Augustine says one who comes to the Church in good faith is forgiven in the Spirit, even through a bad priest.",
    ["a claim that 'Catholic' means Roman Catholic",
     "a claim that the passage names the Donatists",
     "a claim about how a clergyman was ordained or removed",
     "a claim that it can be told without the argument on the sin against the Holy Spirit"], A),
"lpc.quote.peter-the-sick-man-and-the-physician": (
    "Augustine calls Peter the sick man and the Lord the physician, and says three confessions of love answer three denials.",
    ["a claim that Peter is restored to feed the flock in this passage",
     "a claim that it describes a penitential rite or a bishop restoring a penitent",
     "a claim that 'invalid' means a lasting disability"], A),
"lpc.quote.reprove-and-forgive-the-surgeons-knife": (
    "Augustine says to correct with words, or blows if need be, yet forgive in the heart, as a surgeon cuts from kindness.",
    ["a claim that the blows are a church penalty, when they belong to an illustration about unruly boys",
     "a claim that it describes formal public penance or excommunication",
     "a claim that the Latin asks for forgetting the fault"], A),
"lpc.quote.shepherd-wounded-in-the-flock": (
    "Cyprian tells his grieving people that the shepherd is most wounded in the wound of his flock, and weeps with them.",
    ["a claim that it is only pastoral sentiment and not a claim about the office",
     "a claim that it describes how readmission of the lapsed worked",
     "a claim that the lapsed give their own account of their fall"], C),
"lpc.quote.shut-up-in-two-cells": (
    "Lucian writes from prison that, by the emperor's command, the confessors were shut in two cells to die of hunger and thirst.",
    ["a claim about what 'the brightness' is, such as a vision or a death",
     "a claim that the Latin of the first sentence is clear",
     "a claim that the letter is Cyprian's"], C),
"lpc.quote.stewards-and-future-bishops": (
    "Augustine tells his people that many of them will one day dispense the Lord's food, and that he once stood where they stand.",
    ["a claim about when or how Augustine was ordained",
     "a claim that it describes an ordination rite",
     "a claim that 'dispensers' means machines or pharmacists"], B395),
"lpc.quote.such-a-one-with-his-friends": (
    "Cyprian objects to a certificate naming one person and his friends, a vague request no martyr meant.",
    ["a claim that gives a real person's name for 'such a one'",
     "a claim about the full wording of a certificate",
     "a claim that 'friends' means companions rather than household and kin"], C),
"lpc.quote.thanks-be-to-god": (
    "The Acta gives Cyprian's whole answer to his death sentence as Deo gratias, thanks be to God.",
    ["a claim that Pontius records this answer",
     "a claim that the Acta is a court transcript",
     "a claim that the words show relief or irony"], D258),
"lpc.quote.the-branch-cut-from-the-vine": (
    "Augustine says a branch cut from the vine keeps its form but not the root's life, as the sacraments do outside the Church's unity.",
    ["a claim that the rite outside is void, since the washing is not repeated for those baptized among schismatics",
     "a claim that Augustine used the word valid",
     "a claim that the sermon shows a formal ordination or a dispute between bishops"], A),
"lpc.quote.the-case-set-before-the-bishop": (
    "Lucian grants peace to fallen women in the martyrs' name, if each case goes to the bishop and the sin is confessed openly.",
    ["a claim that the grant stands without its condition that each case go before the bishop",
     "a claim about what the bishop decided for Numeria and Candida",
     "a claim that 'confession' means a private act before a priest"], C),
"lpc.quote.the-creed-first-then-the-prayer": (
    "Augustine tells those to be baptized they got the Creed first, to know what to believe, then the Lord's Prayer, to know whom to ask.",
    ["a claim that the sermon is about the Creed rather than the Lord's Prayer",
     "a claim that it describes a formal ceremony of handing over the Creed",
     "a claim that the passage names Paul, whose words the first sentence quotes"], A),
"lpc.quote.the-paper-itself": (
    "Cyprian checks a letter from the Roman clergy by its hand, its content and its paper, then sends it back.",
    ["a claim about what had been changed in the letter or by whom",
     "a claim that the letter was proved a forgery",
     "a claim that 'clerical' means office work"], C),
"lpc.quote.the-people-kept-watch-at-the-door": (
    "Pontius says Cyprian spent his last night in an officer's house while the whole people kept watch outside.",
    ["a claim about how many kept watch",
     "a claim that Cyprian spent the night in a prison cell"], D258),
"lpc.quote.the-psalms-hung-upon-the-wall": (
    "Possidius says Augustine had psalms of penance copied and wept over them as he lay dying.",
    ["a claim about which psalms they were",
     "a claim that the deathbed was calm",
     "a claim that a second witness confirms the sickroom"], D430),
"lpc.quote.the-sermon-and-the-readings-are-daily-bread": (
    "Augustine calls his own preaching, the readings in church and the hymns daily bread, needed while the people are far from home.",
    ["a claim that the Eucharist was not daily bread",
     "a claim about how often hymns were sung",
     "a claim that 'pilgrimage' means a trip to a shrine"], A),
"lpc.quote.the-trees-and-the-trembling-executioner": (
    "Pontius sets Cyprian's death among thick trees, and says the hand that struck him was steadied from above.",
    ["a claim that the strengthening of the hand is a fact and not Pontius's telling",
     "a claim that merges Pontius's account of the blindfold with the Acta's",
     "a claim that these details are independently attested, since the Acta tells none of them"], D258),
"lpc.quote.the-whole-people-of-the-brethren-came": (
    "The Acta says all the Christian people stood at the officer's house, and Cyprian had the young women guarded.",
    ["a claim about what the young women were guarded from",
     "a claim that the Acta is a court transcript",
     "a claim that Pontius gives this detail"], D258),
"lpc.quote.thirteen-letters-sent-to-rome": (
    "Cyprian tells Rome that thirteen letters from hiding show how he guided and rebuked.",
    ["a claim about which thirteen letters they were",
     "a claim that they were a published book of letters"], C),
"lpc.quote.thousands-of-certificates-daily": (
    "Cyprian says thousands of letters of peace were given each day with no test, against the Gospel.",
    ["a claim that 'thousands' is a count",
     "a claim that the 'wicked certificates' and the confessors' certificates are one document",
     "a claim that Cyprian said such letters should not exist"], C),
"lpc.quote.two-hear-one-scorns-one-rises": (
    "Augustine marvels that when Christ crucified is preached, two hear, one scorns and one rises, and the one who rises must not claim credit.",
    ["a claim that it replies to the Pelagians",
     "a claim that it explains why one hearer rises and the other scorns, such as a doctrine of election",
     "a claim that 'rises' means the resurrection"], A),
"lpc.quote.walled-in-by-a-mingled-multitude": (
    "Pontius says Cyprian went out from the officer's house walled in on all sides by a mingled multitude.",
    ["a claim about the size of the crowd",
     "a claim that everyone in the crowd was a Christian"], D258),
"lpc.quote.what-is-done-by-you-he-does-in-you": (
    "Augustine explains the petition 'Thy will be done in heaven and in earth' by saying that what is done by you, God does in you.",
    ["a claim that it teaches compulsion, when read without its lead-in on God's will done in everyone",
     "a claim that it replies to the Pelagians",
     "a claim that the opening question was an objection raised by a hearer"], A),
"lpc.quote.ye-belong-to-my-care": (
    "Augustine says his hearers are in his care so he can give account for them, and that he wept when not heard.",
    ["a claim about the date, place or occasion of the sermon",
     "a claim that the closing prayer is Scripture",
     "a claim that the sentence before it, calling the hearers a Catholic people not divided from unity, is part of the quoted words"], B395),
}

WITNESSES = {
"lpc.witness.almsgiving-quenches-sin": (
    "Cyprian taught that almsgiving is the usual cure for sin after baptism.",
    ["a claim that the teaching sets a limit on how much a believer may keep",
     "a claim that it gives a full account of marriage, courtship or the wedding",
     "a claim that the quoted line about water and fire is Cyprian's own composition and not Scripture"], C),
"lpc.witness.answerability-as-ground": (
    "In our view, a bishop's duty to answer for his people is the root of the road back, the font, and disagreement without a break.",
    ["a claim that any source states this link, since it is our own reading",
     "a claim that answerability settles every hard case, such as the font answered twice in opposite ways",
     "a claim that the two bishops answered the font question alike"], W),
"lpc.witness.apostolic-succession-of-bishops": (
    "Augustine named Rome's bishops from Peter to show the line from the apostles, but Cyprian gave no list.",
    ["a claim that Cyprian drew up a name list of his own",
     "a claim that either bishop's account is all a modern listener means by apostolic succession"], W),
"lpc.witness.baptism-traced-to-the-apostles": (
    "Augustine held that infant baptism and no rebaptism came from the apostles, though none of them wrote it.",
    ["a claim that a written apostolic text gives either practice",
     "a claim that Augustine traces catechesis or the road back to the apostles by name",
     "a claim that Cyprian shared Augustine's test of apostolic origin"], A),
"lpc.witness.blamed-for-the-worlds-troubles": (
    "A Roman official blamed Christians for war, plague and famine, and Cyprian wrote a reply.",
    ["a claim that the neighbour's own words survive, since the charge is reported in Cyprian's reply",
     "a claim about whether Christians hid in catacombs",
     "a claim about what an outsider found strangest about them"], C),
"lpc.witness.communion-over-separation": (
    "In 256 Cyprian's council said it would cast out no one for a different view, and Augustine called it wrong but never cast Cyprian out.",
    ["a claim that the church never broke communion",
     "a claim that any source states a link between the early separations and the rule, since that link is our own reading",
     "a claim that Cyprian and Augustine reached the same ruling",
     "a claim that Carthage and Rome stayed in communion through the 256 dispute"], W),
"lpc.witness.confessor-claim-vs-regulated-peace": (
    "Confessors said they could ask peace for the lapsed, the church's rules answered them, and the two never became one rule.",
    ["a claim that the confessors' claim was a pretense or counted for nothing",
     "a claim that the church found a single rule saying which governs when the two conflict",
     "a claim that the confessors' own voice survives beyond a general letter to Cyprian"], C),
"lpc.witness.constantine-did-not-corrupt": (
    "Augustine called Constantine no foe of the Christian name, and said his power did not come from the old gods.",
    ["a claim that Augustine was a neutral witness, since Petilian's side had asked Constantine to judge and he ruled against them",
     "a claim that Augustine thought friendship with kings always safe",
     "a claim that Constantine's success proved a Christian's standing before God"], (400, 426)),
"lpc.witness.days-before-the-sun": (
    "Augustine said the days before the sun are past our senses, and that by Scripture's count less than 6,000 years had passed.",
    ["a claim that Augustine explained how those first days worked",
     "a claim that the histories he rejected as mendacious are described in their own words here",
     "a claim about Augustine's place in modern debates over the age of the earth or evolution",
     "a claim that Augustine held the first days were ordinary days"], (413, 430)),
"lpc.witness.grant-me-chastity-but-not-yet": (
    "In the Confessions Augustine recalls praying for chastity, but not yet, and says being convinced did not set him free.",
    ["a claim that everyone among them struggled in the same way",
     "a claim that delay always ended as his did",
     "a claim that the prayer was made at the moment he was persuaded"], (397, 401)),
"lpc.witness.heard-for-salvation-not-for-wish": (
    "From Paul's thorn Augustine taught that the saints are always heard for their salvation, even when not heard as they wished.",
    ["a claim that God removed Paul's thorn",
     "a claim that Augustine promised any wish would be answered"], A),
"lpc.witness.marriage-a-threefold-good": (
    "Augustine said marriage has three goods: children, faith to each other and sacrament.",
    ["a claim about courtship, weddings or attendance at them",
     "a claim that separation ended the marriage bond",
     "a claim that the translator's preface is Augustine's own words"], A),
"lpc.witness.restless-heart-and-the-unrepentant-enemy": (
    "Augustine said the heart is restless for God, and ranked love for an enemy who will not repent highest.",
    ["a claim that he thought everyone reaches the highest standard in full",
     "a claim that God forgives one who refuses from the heart to forgive someone who asks",
     "a claim that the two passages come from one work"], A),
"lpc.witness.scripture-above-councils": (
    "Cyprian said a custom with no truth is just old error, and Augustine put Scripture above all bishops and their meetings.",
    ["a claim that Scripture was the church's only authority",
     "a claim that bishops and councils had no binding authority",
     "a claim that the two bishops argued the same dispute"], W),
"lpc.witness.the-only-son-and-the-trinity": (
    "Augustine held Jesus to be God's only Son within one God in three, and an Arian bishop at Hippo fought that belief.",
    ["a claim that this doctrine is what sets this tradition apart",
     "a claim that the doctrine went unchallenged",
     "a claim about how the conference with Maximinus ended"], A),
"lpc.witness.the-pattern-we-are-modelled-on": (
    "Augustine taught that Christ's death, burial, rising and ascent were the pattern for the believer's life.",
    ["a claim that this exhausts who Jesus was to them or what he taught",
     "a claim that our sources keep a developed telling of his life as its own story",
     "a claim that the pattern is only mystical"], A),
"lpc.witness.tradition-tested-by-apostolic-warrant": (
    "Cyprian would call a rite the apostles' own only if it was written; Augustine would too if the whole Church kept it in all lands.",
    ["a claim that the two bishops agreed on one test",
     "a claim that the tradition settled which test is truer",
     "a claim that the two bishops argued the same dispute",
     "a claim that Cyprian's test covered every custom, since he aimed it at the tradition Stephen claimed"], W),
"lpc.witness.violence-commanded-not-cruel": (
    "Augustine told a Manichaean that Moses obeyed God and was not cruel, and that God punished justly.",
    ["a claim that this settles the question for a modern reader",
     "a claim that the answer lacked moral seriousness",
     "a claim that a command carried out is the same act as the same deed chosen on one's own account"], A),
}

TERMS = {
"lpc.term.bishop-of-bishops": (
    "The term names the rule, stated at the council of 256, that no bishop stands over another and each answers to Christ.",
    ["a claim that it is an early anti-papal manifesto or a modern separation of powers",
     "a claim that Cyprian's words name Stephen as their target",
     "a claim that ordinary believers or most clergy were formed by this question"], D256),
"lpc.term.catechesis": (
    "Catechesis was the teaching of the creed before baptism, and Augustine wrote a guide to it.",
    ["a claim that it was a children's catechism of memorized questions and answers",
     "a claim that it was an organizing force of its own and not the medium formation was taught through",
     "a claim that the creed was taught after the water"], W),
"lpc.term.certificates-letters-of-peace": (
    "A certificate was a confessor's letter of peace for the lapsed, and Cyprian wanted a name on it.",
    ["a claim that it is the same paper as the Decian sacrifice certificate",
     "a claim that Cyprian opposed such letters outright",
     "a claim that the confessors' side is heard beyond one general letter",
     "a claim that 'thousands' is a count rather than Cyprian's word in a dispute"], C),
"lpc.term.communion": (
    "For Cyprian, communion was a real standing that could be lost, given back, and kept through sharp disagreement.",
    ["a claim that it names only a rite or a general warmth of fellowship",
     "a claim that either bishop used this word for the pattern across both phases, since that pattern is our own reading"], W),
"lpc.term.compel-them-to-come-in": (
    "The phrase names Augustine's late claim that a Christian ruler may use force to bring a separated group back.",
    ["a claim that it is the church's settled endorsement of religious persecution throughout",
     "a claim that Augustine always held it, since his earlier opinion against coercion reaches us only through his own later account",
     "a claim that a Donatist answer to it survives",
     "a claim that an editor's verdict on Augustine's reading of the parable is part of the teaching"], A),
"lpc.term.confessor": (
    "In Cyprian's time a confessor, who kept faith when questioned and lived, could rival a bishop.",
    ["a claim that a confessor was a priest who hears confessions",
     "a claim that the word carries this sense in Augustine's phase",
     "a claim that confessors speak for themselves beyond a few letters"], C),
"lpc.term.grace": (
    "In Augustine's teaching, grace means that no effort of ours is enough alone, and any good we do was given to us first.",
    ["a claim that it means general benevolence or grace under pressure",
     "a claim that Pelagius himself held the position Augustine reports",
     "a claim that Cyprian taught it as an organizing concern",
     "a claim that it settles the Catholic and Protestant disagreements over grace"], A),
"lpc.term.heresy": (
    "The word asks if baptism outside the church counts: Cyprian's council said no, and Augustine said it was truly given but did no good there.",
    ["a claim that it names a settled malicious deviation from an agreed orthodoxy",
     "a claim that De Unitate bears on Cyprian's argument against Stephen",
     "a claim that the question was closed and not argued by both sides"], W),
"lpc.term.libellatici-sacrificati": (
    "Cyprian split the lapsed into those who bought a paper and those who sacrificed, both fallen but not alike.",
    ["a claim that it was a formal canonical taxonomy applied uniformly",
     "a claim that the two acts weighed the same",
     "a claim that the grading rests on an editor's endnote"], C),
"lpc.term.libelli": (
    "A libellus said you had made the pagan offering; some bought one without making it, and Cyprian still held them fallen.",
    ["a claim that it was a modern identity document or licence",
     "a claim that the Latin word appears in the English volume, which renders it certificates",
     "a claim that Latin libellus names only this paper"], C),
"lpc.term.plenary-council": (
    "Augustine held that small councils yield to wider ones, and the widest can still be corrected.",
    ["a claim that it is a plain claim of central institutional authority",
     "a claim that it restates Cyprian's formula",
     "a claim that the question reached ordinary formation in either phase"], A),
"lpc.term.preaching": (
    "Preaching was the regular talk to the whole church, and the main way its teaching reached plain believers.",
    ["a claim that it was a stern monologue or a polished performance among several parts of a service",
     "a claim that it was an organizing force of its own",
     "a claim that how often the word occurs measures its weight"], W),
"lpc.term.reconciliation-penitential-discipline": (
    "Reconciliation was the public road, in steps under the bishop, by which a failed member came back.",
    ["a claim that it was a private confession said alone",
     "a claim that it was complete once both parties felt differently",
     "a claim that the reconciled believer's own account survives"], C),
"lpc.term.schism": (
    "Schism is the tear that comes when arguing stops and a separate altar, bishop and people stand in the same town.",
    ["a claim that it was an ordinary feature of a plural religious landscape",
     "a claim that the line between heresy and schism was as stable as later usage implies",
     "a claim that this entry characterizes Donatism"], W),
"lpc.term.suffrage": (
    "Suffrage names the voice of the people that, with God's judgment, put a man into office, even against his wishes.",
    ["a claim that it was a vote with a ballot and a fixed procedure",
     "a claim that both phases share one word for it, when it is a pattern named from different figures and words",
     "a claim that Augustine's episcopate came by the people's choice alone"], W),
"lpc.term.the-flock": (
    "The flock is the particular people given to one bishop in one place, for whom he answers and who can hold him to it.",
    ["a claim that it is a sentimental name for churchgoers or the church in general",
     "a claim that Augustine used the image as often as Cyprian",
     "a claim that the bishop is a remote regional administrator"], W),
"lpc.term.the-lapsed": (
    "The lapsed were church members who gave way, by sacrifice or by a bought certificate, and then asked to return.",
    ["a claim that they drifted away gradually, as a modern believer might",
     "a claim that a lapsed believer's own account survives",
     "a claim that their standing was a private matter with no public consequence"], C),
"lpc.term.the-one-episcopate": (
    "Cyprian taught that the episcopate is one office, and each bishop holds his part for the whole.",
    ["a claim that it is a ranked hierarchy or a federation of independent officers",
     "a claim that De Unitate carries Cyprian's argument against Stephen",
     "a claim that either recension of De Unitate chapters 4 and 5 grounds the term"], C),
"lpc.term.the-people": (
    "The people names the congregation when it acts, as the flock names it when it is being cared for.",
    ["a claim that the Latin word plebs is a settled name for it",
     "a claim that the people held a formal ballot",
     "a claim that the people always prevailed"], W),
}

STORIES = {
"lpc.story.celerinus-writes-to-lucian": (
    "Celerinus asked Lucian in jail to give peace to three fallen women, and Lucian said yes if the bishop heard each case.",
    ["a claim that gives words to Celerinus's sister, Numeria or Candida, none of whom speaks in our sources",
     "a claim that Lucian's grant stood without his condition that each case be set before the bishop",
     "a claim that the confessors were either usurpers or heroes"], C),
"lpc.story.election-of-cyprian": (
    "Pontius says God's judgment and the people's favour made Cyprian bishop, and he later called it suffrage.",
    ["a claim that it was a vote with a candidacy and a count",
     "a claim that any witness besides Pontius confirms that Cyprian was a neophyte",
     "a claim that Pontius, writing in praise, is a neutral witness"], E251),
"lpc.story.hundred-thousand-sesterces": (
    "Cyprian told eight Numidian bishops that Christ is seen in captives, and sent them 100,000 sesterces.",
    ["a claim about what the sum was worth in modern money",
     "a claim that the ransom worked",
     "a claim about what share of anything the sum represented"], C),
"lpc.story.numidicus": (
    "Cyprian told Carthage that Numidicus, who watched his wife burn and was left for dead, joins the presbyters of Carthage.",
    ["a claim that gives words to Numidicus, his wife or his daughter",
     "a claim about where the daughter searched",
     "a claim that 'burned, preserved' is a cruel word game and not a martyr's death named as completion"], C),
"lpc.story.the-death-of-cyprian": (
    "Cyprian died on 14 September 258, and Pontius and the Acta agree on the core but differ on who tied the cloths.",
    ["a claim that the executioner's hand was strengthened from above, which is only how Pontius tells it",
     "a claim that the two texts agree on who tied the cloths",
     "a claim that the Acta is a court transcript",
     "a claim that any spectator's own account survives"], D258),
"lpc.story.the-plague-and-the-enemies": (
    "Pontius says that in the plague Cyprian preached love of enemies, and help reached beyond believers.",
    ["a claim that the persecutors themselves were helped",
     "a claim that any source outside Pontius describes the relief",
     "a claim that the sermon survives in Cyprian's own hand",
     "a claim that a pagan Carthaginian's account of being helped survives"], C),
"lpc.story.the-psalms-on-the-wall": (
    "Possidius says Augustine had psalms of penance copied and wept over them in his last illness.",
    ["a claim that the death was serene",
     "a claim that any witness besides Possidius describes the sickroom",
     "a claim about what leaving Hippo was like"], D430),
}

LIMITS = {
"lpc.limit.411-gesta-unread": (
    "We know when the 411 meeting took place, but its record has not been properly read, so we cannot say how the other bishops argued.",
    ["a claim that the transcript shows how widely conciliar theory spread",
     "a claim about what was argued bishop by bishop",
     "a claim that the acts have been read in full"], D411),
"lpc.limit.apostolic-origin-undefended": (
    "Augustine ties infant baptism and the bishops to the apostles, but not teaching or the road back.",
    ["a claim that catechesis, the road back or teaching before the water is traced to the apostles",
     "a claim that the oneness of the episcopate is a traced lineage"], W),
"lpc.limit.no-chain-of-witnesses": (
    "The record names no one who saw the risen Jesus, and Augustine argues from what the apostles wrote.",
    ["a claim that anyone among them knew someone who saw Jesus",
     "a claim that the argument rests on a chain of living memory"], W),
"lpc.limit.ordinary-interior-life": (
    "We show what bishops ruled but almost never what plain people felt, save the tears Augustine shed at his baptism, told long after.",
    ["a claim that Augustine's account of his baptism shows ordinary believers' experience",
     "a claim that an ordinary believer's own account survives",
     "a claim about what believers felt at the font or in the congregation"], W),
"lpc.limit.rural-punic-berber-life": (
    "The record comes from two cities and says little of country churches or of Punic and Berber speakers.",
    ["a claim that rural congregations lived as the cities did",
     "a claim about Punic or Berber Christian practice"], W),
"lpc.limit.the-lapsed-own-account": (
    "The lapsed left nothing in their own words, so every account of them is a bishop's, written to decide what should be done.",
    ["a claim about why a particular person gave way",
     "a claim that a lapsed believer judged the terms of return just",
     "a claim that a first-person text from a lapsed believer survives"], C),
"lpc.limit.the-outsiders-own-view": (
    "The record cannot say if Christians hid in catacombs or what outsiders thought odd.",
    ["a claim that Christians hid in catacombs",
     "a claim that an outsider's own words survive",
     "a claim that Augustine asked whether Constantine corrupted the church in those words"], W),
"lpc.limit.the-silent-century": (
    "From 258 to 391 our own ordinary pastoral voice falls silent, as far as we have weighed it.",
    ["a claim that nothing happened in those years",
     "a claim that the silence is settled, since a handful of old sermons have not been weighed yet",
     "a claim that fills the silence from a neighbouring communion's sources",
     "a claim that no Catholic African writing survives from these years, since Optatus wrote against the Donatists c. 366 to 384"], (258, 391)),
"lpc.limit.womens-own-voice": (
    "Women like Numeria and Candida come to us in men's words, and no writing by a woman of our own survives.",
    ["a claim that a woman's own writing survives",
     "a claim that a woman's spoken words set down by a man are her own writing"], W),
}

CONTESTED = {
"lpc.contested.compel-coercion-development": (
    "Whether Augustine truly changed his mind on force stays open, since we know his earlier view only from his own account.",
    ["a claim that the change of mind is settled as either genuine or a later construction",
     "a claim that Cyprian's corpus has anything corresponding to it",
     "a claim that a contemporaneous statement of the earlier view survives",
     "a claim that this position is or is not the ancestor of later inquisitorial practice"], A),
"lpc.contested.cyprian-death-genre": (
    "Whether Pontius gives testimony or a saint's life stays open, though Cyprian's death in 258 is sure.",
    ["a claim that the Scriptural patterning shows the account cannot be trusted",
     "a claim that the question is settled in either direction",
     "a claim that the strengthened hand of the executioner is a fact"], D258),
"lpc.contested.de-unitate-recensions": (
    "One form of two chapters of De Unitate may be a later hand's insertion or Cyprian's own rewrite, and that stays open.",
    ["a claim that the interpolation thesis is settled",
     "a claim that Cyprian wrote both recensions",
     "a claim that anything we say about the church rests on either recension's wording"], (251, 256)),
"lpc.contested.grace-pelagius-characterization": (
    "Whether Augustine was fair to Pelagius stays open, since we have only his side.",
    ["a claim that Augustine's report is the position Pelagius held",
     "a claim that later Reformation-era and modern uses of the controversy continue terms Augustine set correctly",
     "a claim that Pelagius's own words survive among our sources"], A),
}

GRAVITIES = {
"lpc.gravity.collegial-communion-preserved": (
    "Bishops here argued hard but worked to keep communion, not break it, from Cyprian to Augustine.",
    ["a claim that any source states this pattern across both phases, since it is our own reading",
     "a claim that bishops never broke communion"], W),
"lpc.gravity.conciliar-authority-theory": (
    "Cyprian and Augustine each had a theory of council power, but little shows it shaped much.",
    ["a claim that conciliar authority was a major organizing concern",
     "a claim that the two theories reconcile into one",
     "a claim that the question reached ordinary believers"], W),
"lpc.gravity.confessor-authority-vs-episcopal-peace": (
    "Confessors claimed a loose power to give peace to the lapsed, against the bishop's own penance, and neither won.",
    ["a claim that the tension was resolved",
     "a claim that evidence beyond Cyprian's letters supports it",
     "a claim that the confessors were either usurpers or heroes"], C),
"lpc.gravity.grace-and-human-incapacity": (
    "Grace and human weakness weigh heavily in Augustine's phase, but rest on one voice.",
    ["a claim that it spans both phases",
     "a claim that the volume of text shows breadth",
     "a claim that Pelagius's own view is known"], A),
"lpc.gravity.pastoral-office-flock-keeping": (
    "A bishop is personally answerable for a bounded flock, and much else they held flows from that office.",
    ["a claim that the bishop was a regional administrator"], W),
"lpc.gravity.penitential-discipline": (
    "Taking back the failed, not shutting them out, was central in Cyprian's time, and this concern is classified in his phase only.",
    ["a claim that it spans both phases under this name",
     "a claim that the rival routes of Novatianist rigor or Felicissimus laxity were the church's own",
     "a claim that the process was private confession",
     "a claim that Augustine's church had no penitential discipline"], C),
"lpc.gravity.preaching-and-catechesis": (
    "Preaching and teaching brought the main concerns to believers but shape little alone.",
    ["a claim that preaching and catechesis organize the world by themselves",
     "a claim that other concerns lean on it as they lean on the office, penance and communion"], W),
"lpc.gravity.sacramental-ordination-validity": (
    "The two bishops split on whether a baptism or ordination outside the church is real.",
    ["a claim that the two answered alike",
     "a claim that the disagreement broke communion",
     "a claim that the question is thinly evidenced"], W),
}

NOTES = {**QUOTES, **WITNESSES, **TERMS, **STORIES, **LIMITS, **CONTESTED, **GRAVITIES}

_TOP_KEY = re.compile(r"^[A-Za-z_]+:")


def note_block(means: str, not_for: list[str], years: tuple[int, int]) -> list[str]:
    lines = ["use_note:", f"  means: {json.dumps(means, ensure_ascii=False)}", "  not_for:"]
    lines.extend(f"    - {json.dumps(line, ensure_ascii=False)}" for line in not_for)
    lines.append(f"  years: {{from: {years[0]}, to: {years[1]}}}")
    lines.append("  status: provisional")
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
