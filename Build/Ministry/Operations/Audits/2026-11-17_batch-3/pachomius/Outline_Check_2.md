# Pachomius: outline check, round 2

## The heart of his life (checker's own account, written before opening Outline.md)

From the census (`role` "Monk and founder of communal monasticism"; `knownFor` "bound monks to a common rule in shared houses"), the source sheet (H1-H8, E8-E9, I1-I3) and what he is known for:

Pachomius took the monk's life, which in Egypt was lived each by his own way, alone or with one old teacher, and made it a shared life under one rule. In walled monasteries by the Nile he set brothers in houses under a head, with the same clothes and the same food for all, work and trading by turns, and a steward over the whole. The houses grew into a fellowship of about nine men's monasteries (and a house for women under his sister Mary) with one head and two great gatherings a year at Phbôou, at Easter and in Mesore. He began by serving his first brothers himself, kept his monks lay under the bishops, hid from ordination, and held to equality to his deathbed (the blanket). He did not invent monastic discipline (Palamon's older rule) and "founder" is later witnesses' word (Gennadius and others). What came of it: the fellowship outlived him under Petronius, Horsiesius and Theodore; Palladius counts about seven thousand monks under the rule; Jerome put the rule into Latin about 404 from a Greek version; Cassian drew on "the monks of Tabenna"; Benedict of Aniane set passages of it under the chapters of Benedict's Rule. The essence: a rule-bound common life of many, which later monasteries east and west copied.

## Comparison with the outline's heart

Same in substance. The outline's heart covers every major contribution in mine: the turn from the solitary life (H1, E4) to one shared life under a rule, the houses and their running, the federation of nine houses with one head and two gatherings, the women's house, older hermits and communities joining, and the rule's road through Greek and Latin to Benedict of Aniane. Its "what the sources hold" note keeps "founder" in later witnesses' voices and rules out "first monastery" and "invented monastic life", as the sheet requires (H8). Beats 1 and 2 carry the heart inside the first minute; the conscript story follows as beat 3. Lay monks under bishops and the deathbed equality sit in beat 2, beat 6, beat 7 and "What came of them" 3, so nothing major is left out.

## Verdict: FIX

One blocking finding, in the Connection field. Everything else holds or needs only minor changes.

## What was checked against the files

- Antony's words, Acta 86876-86896: checked. Context: Antony first says "omnes vos facti estis sicut Abbas Pachomius ... Apostolorum viam ingressus". Zacchaeus then praises Antony as the world's brightest light, "cujus ad ipsos usque Imperatores fama pervasit". Antony answers "Non ita, Zacchae, sentio" and goes on with the quoted passage. My rendering of 86887-86893: "For at the time when I first began to live as a monk, there was no community anywhere in which anyone had care or fear for the salvation of others. Each of the old monks, once the persecution was over, trained himself in the monastic life privately. Afterwards your father, with God's help, brought about so great a good." The outline's quote 1 matches. The fame that reached the emperors (Opening 1) is Zacchaeus's praise of Antony as the Life reports it. That is fine as "the Life says".
- Blanket, Acta 86619-86633: checked. My rendering of 86630-86633: "Take this piece of bedding away from here at once. It is not right that I should be better off in anything than the rest of the brothers." Quote 3 matches.
- Christians at the prison, Amélineau 5145-5146: checked. Quote 2 matches.
- Plague after Easter, "centum ac plures" across all the monasteries (86509-86512): checked. Theodore and three brothers move the body (86655-86658); the secrecy is "nemine conscio" in Theodore's reading of the instruction (86637-86639): checked.
- Athanasius and the ordination, Bohairic 6660-6674 and Greek 82504-82521: checked. The Greek Life puts the visit at Tabennesis by boat (82509-82510), so the Links line holds. The Bohairic Life has him hide "parmi la foule nombreuse", the Greek Life "inter Fratres". The Do not say entry is right.
- Palamon's rule, Bohairic 5424-5434: checked. The Bohairic says "méditant la parole du Seigneur". Beat 4's "with the Scriptures" is a fair plain rendering.
- Phbôou: walls, church, houses, heads and seconds (8175-8178), and Ebôneh's request (8180-8183): checked. The twice-yearly gatherings (9640-9644): checked.
- Jerome's preface, 4330-4397: checked. It names Silvanus, the books sent from Alexandria, the Latin speakers in the Thebaid and at Metanoia, and Vallarsi's note placing Metanoia as a suburb of Alexandria. It names Leontinus and the brothers sent to press him, the dictation from the Greek, and Eustochium and "nostri fratres". It also gives forty to a house and seniority by entry.
- Gennadius 42277-42286 (Theodore's letters, the dissension): checked. Palladius 405 (7000): checked. Cassian, Institutes IV.1 (npnf211 18521-18531): checked.
- Benedict of Aniane: Ardo 30903-30911, Ménard 58651-58655 and the heading at 66976: checked.
- Library sweep, spot-checked. The `desert-monasticism.yaml` rows match the sheet. A search of `cic/texts/` for pachom/pakhôme/tabenn turns up about 187 files, which is consistent with the sheet's 182. PL 67 (`facundus-ferrandus-caesarius-dionysius-pl67-lat_migne1865.txt`) names Dionysius Exiguus's Vita S. Pachomii, but at 32244-32250 it prints only a cross-reference ("Hanc Vitam ... in fine sexti saeculi dabimus"), with no text. So the sheet is right that Dionysius's Life is not held. The Basil volume (Clarke 1925) mentions Pachomius only in its editor's introduction, and Severus's History of the Patriarchs has passing mentions. I found no missing primary text or major later witness.

## Findings

**BLOCKING 1. The Connection field says more than Jerome's preface.** The outline says: "that it reached the West as books, more than fifty years after Pachomius died, because monks and nuns who wanted to live his way asked for them." The preface does not support this, on three points.
- Those who asked were Latin-speaking monks living in the Thebaid houses and at Metanoia, in Egypt. They asked through Silvanus, and Leontinus and his brothers pressed Jerome in person (4338-4344, 4349-4352).
- Eustochium's nuns did not ask. Jerome made the Latin so that Eustochium "haberet quod sororibus agendum tribueret" (4384-4386).
- The translation of about 404 did not carry the rule "to the West". It was made for Latin speakers in Egypt and for Jerome's own community, whose town the preface does not name (Source_Sheet I1). In the held texts, the West's use of the Latin is Benedict of Aniane's Concordia, four centuries later.

Correction: replace the sentence beginning "Second, that it reached the West as books ..." with: "Second, that it passed into Latin as books, more than fifty years after Pachomius died. Latin-speaking monks living in his own houses in Egypt could not read the Egyptian or Greek, and priests pressed Jerome to translate the rules. He made the Latin for them, and also for his own brothers and for the nuns under Eustochium. Through that Latin the rule later reached the monasteries of the West." Add to **Do not say**: "The nuns asked Jerome for the rule", or "Jerome's Latin took the rule to the West in 404" → "the Latin-speaking monks in Egypt asked, through Silvanus and Leontinus; Jerome also made it for his own brothers and Eustochium's nuns."

**MINOR 1. Beat 2: "Brothers serving at table changed every three weeks."** Bohairic 6477-6479 says "on changeait les frères qui faisaient le service", in a list that covers cooking for the sick, the gate and buying and selling. It does not say the service was at table. Correction: "the brothers on duty changed every three weeks".

**MINOR 2. Heart and beat 2: the house of about forty is Jerome's figure.** The forty to a house, the thirty or forty houses to a monastery and seniority by entry come from Jerome's preface of about 404, in the present tense, describing the houses of his own day (4390-4403). The Bohairic Life does not give these numbers for Pachomius's lifetime. Correction: in the heart and in beat 2, tie the figure to its witness: "Jerome, describing the houses some fifty years later, says about forty brothers lived in each". Add to Do not say: "forty to a house in Pachomius's day" as fact → "about forty, as Jerome describes the houses".

**MINOR 3. Heart: "Hermits and whole older communities asked to come under his rule."** H4 holds five hermits who came to live near him (6337-6341) and one older community, Ebôneh's at Schénésît (8180-8183). Correction: "Hermits came to live beside him, and the abbot of an older community asked to come under his rule."

**MINOR 4. Heart: "After his death the rule went into Greek and Latin."** Jerome dates the Latin to his own time (about 404). The held texts do not date the Greek version, so "after his death" says more than the sources for the Greek. Correction: "In time the rule went into Greek, and about 404 Jerome put it into Latin from the Greek; from that Latin it reached the West, where ..."

**MINOR 5. Beat 2 and the heart: the accounts.** The Bohairic Life says the brothers met at Phbôou at Easter "les uns avec les autres", and in Mesore "pour rendre leurs comptes" (9640-9644). The accounts belong to the August gathering only. Correction: "twice a year the brothers met at Phbôou: at Easter to keep the feast together, and in August to give their accounts".

**MINOR 6. Beat 7 and Do not say: the blanket.** At 86621-86628 Pachomius himself asks for a slightly lighter blanket, because the one he has is too heavy after forty days of illness. The brother brings one of the best and lightest, and Pachomius sends it back once he sees the difference. A writer could easily say the brothers pressed a better blanket on him. Add to Do not say: "The brothers gave him a better blanket and he refused it" → "he asked for a lighter one; when he saw it was finer than the brothers' own, he sent it back".

**MINOR 7. Setting: "Phbôou, which the Greek calls Pabau."** In the Acta file "Pabau" is the Bollandists' commentary (78921, 79348); Gennadius has "Bau". Correction: "Phbôou (Pabau or Bau in Greek and Latin sources)".

Nothing else needs changing. The setting, shape, length and openings are right. So are the impact ranking and its defended marks, the Links and Who tells it, and the confidence levels I checked. The tradition's spoken name, "the monks of Egypt", does not mislead.
