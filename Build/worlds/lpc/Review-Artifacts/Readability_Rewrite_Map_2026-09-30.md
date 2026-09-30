# Readability Rewrite Map

Date: 2026-09-30. World: lpc. Scope: one rewrite of every lpc field that failed FK grade 10 or FRE 60 in the readability gate (`gate_readability`), outside `records/lpc/quote/` and the `voice_craft`, `demonstration`, `world_front` and `facilitator_brief` records, which are handled elsewhere.

## Summary

- Fields rewritten: 43, in 39 records.
- Failing fields before: 43 (gate findings before: 60, counting FK and FRE separately). After: 0 (gate findings: 0).
- Every rewritten field now scores FK 10 or below and FRE 60 or above, measured with `engine.m1.gates.grade_text`.
- Method: sentences split, nominalizations and long words swapped for plain ones, every fact, date, name, number, quote, hedge and confidence marker kept. Nothing was added.
- Quoted words, ids, relations and all other fields are unchanged. Each edit was checked by parsing the record front matter before and after and confirming only the named field differs.
- Claims register: no claim id changed. `claims lpc` derives 110 claims and registers 110, as before. No row was re-registered.
- Silence scope: no sentence about what the record does or does not hold was reworded except by splitting. The Doc_02 section 7 scope text, and the class-level exception for rows 6 and 194, is not touched.

## Wording choices a reviewer may want to check

These swaps go beyond pure sentence splitting. Each keeps the meaning the field had.

- `figure.*.bridge_line`: the single long phrase became a lowercase lead phrase plus short sentences. The fleet already has multi-sentence bridge lines (a capitalised second sentence). How the line is displayed is unchanged.
- `contested.de-unitate-recensions`: 'alternative recension' became 'the other form'. 'Primacy Text' quotation marks kept.
- `contested.compel-coercion-development`: 'solicitation of legal protection' became 'request for legal protection'. 'Earlier in his own episcopate' became 'earlier in his own time as bishop'.
- `contested.grace-pelagius-characterization`: 'corpus' became 'writings'. 'Unaided' became 'with no help'. The Reformation-era and modern use is now attributed to 'later Catholics and Protestants'.
- `contested.cyprian-death-genre`: the quoted genus-clause fragments are verbatim and unchanged. 'Datable' outside the quotation became 'we can date'.
- Gravity and force descriptions: 'reinforces' became 'supports' in six gravity fields. 'Regulated process of penance' became 'process of penance run by rule'. 'Independent' became 'each on his own' in one place. 'Institution' became 'the church as a whole' in one place. 'Directly quoted' became 'quoted word for word'. 'Solidly attested' became 'firmly attested' in five places. 'Most populous' (Carthage) was kept.
- `core` horizon and formation_logic: 'ferociously' became 'fiercely'. 'Produces' became 'gives us'. 'Refuses to let' became 'will not let'. 'Sacramentally valid' became 'counted as a valid sacrament'. 'Orientation' became 'stance'. 'Experiences itself as' became 'knows itself as'. 'Convenient end' became 'tidy end'.
- The sentence 'No text from Augustine's phase is organized around a crisis like that of the lapsed...' in `gravity.penitential-discipline` is a registered claim and is kept word for word.

## Generators

- Updated so a regeneration keeps the new text: `Build/worlds/lpc/scripts/wb_lpc_s22.py` (two terms), `wb_lpc_s24.py` (two story lines, six figure bridge lines), `wb_lpc_s26.py` (four contested claims), `wb_lpc_s28.py` (ambient, witness and limit fields). Three of these generator strings were already behind the record (two-cities and communion-over-separation said 'a century and a third' where the record says 'a century and a half'; the 411 limit said 'other than our two anchor figures' where the record says 'beyond Cyprian and Augustine themselves'). They now carry the record's wording.
- Not changed, with the reason: the force, gravity and world_core generators (`wb_lpc_s25.py`, `wb_lpc_s21.py`) still emit the text from before the OG-14 re-voicing (layer headings, Doc_0N references). The current records were re-voiced by hand and the generators were never brought up to date, so a regeneration would already revert OG-14 independent of this task. No current sentence of those fields exists in them to update.
- No generator emits: `witness.baptism-traced-to-the-apostles`, `witness.constantine-did-not-corrupt`, `witness.marriage-a-threefold-good`, `witness.tradition-tested-by-apostolic-warrant`. They were edited in the records only.

## Old to new, field by field

### lpc.ambient.council-assembly-scale / detail

- Before: FK 10.4, FRE 62.4
- After: FK 5.3, FRE 79.1

Old:

> In September of 256, eighty-seven bishops gathered in one place to give their own sentence on the rebaptism question, one after another, each in his own words. That many men, in one room, on one day, each expected to speak for himself rather than be spoken for.

New:

> In September of 256, eighty-seven bishops met in one place. One after another, each gave his own sentence on the rebaptism question, in his own words. That was a great many men in one room on one day. Each was expected to speak for himself rather than be spoken for.

### lpc.ambient.two-cities-scale / detail

- Before: FK 10.0, FRE 60.6
- After: FK 6.0, FRE 72.2

Old:

> Our whole life is lived in two cities, a century and a half apart. The first is a great port city, the largest Latin Christian city outside the empire's own capital in the west. The second lies further along the same coast -- a smaller see, answerable within a different province than the first, though its own bishop sat in the same wider councils.

New:

> Our whole life is lived in two cities, a century and a half apart. The first is a great port city. It is the largest Latin Christian city outside the empire's own capital in the west. The second lies further along the same coast. It is a smaller see, answerable within a different province than the first. Even so, its own bishop sat in the same wider councils.

### lpc.contested.compel-coercion-development / claim

- Before: FK 36.6, FRE -34.0
- After: FK 7.5, FRE 62.1

Old:

> Augustine's three-phase development on coercion -- an early opinion against any compulsion (Letter XCIII §17), a narrow and unsuccessful solicitation of legal protection (Letter 185 §§25-26, earlier in his own episcopate), and finally a sustained defence of compulsion already in force -- records a genuine change of mind, reached through pastoral experience of the Donatist schism, rather than a retrospective self-presentation constructed after the fact to make an already-settled practice look like the outcome of principled reconsideration.

New:

> Augustine's views on coercion developed in three phases. First, he held an early opinion against any compulsion (Letter XCIII §17). Next, he made a narrow and unsuccessful request for legal protection (Letter 185 §§25-26, earlier in his own time as bishop). Last, he gave a sustained defence of compulsion that was already in force. All this records a genuine change of mind. It came from his pastoral experience of the Donatist schism. It was not a story he told about himself in hindsight. Such a story would make a settled practice look like the result of principled rethinking.

### lpc.contested.cyprian-death-genre / claim

- Before: FK 14.7, FRE 21.1
- After: FK 6.7, FRE 60.7

Old:

> Pontius's own account of Cyprian's death (Life §§15-19) is properly classified by Construction Framework V7.4's Tier 1 genus clause -- 'direct textual attestation... named author with identifiable social location... datable with reasonable confidence' -- since Pontius meets every element of that test as a named eyewitness deacon, and the Scriptural typology and providential framing are ornament on a real, datable public execution rather than evidence the account itself cannot be trusted as testimony.

New:

> Pontius's own account of Cyprian's death (Life §§15-19) rightly belongs in Tier 1 of Construction Framework V7.4. Its genus clause reads: 'direct textual attestation... named author with identifiable social location... datable with reasonable confidence'. Pontius meets every part of that test. He is a named deacon who saw it himself. The account also casts events as echoes of Scripture (typology). It sees God's plan in them (providential framing). Both are ornament. They sit on a real public execution that we can date. Neither is proof that we cannot trust the account as a witness's word.

### lpc.contested.de-unitate-recensions / claim

- Before: FK 26.0, FRE -9.1
- After: FK 6.8, FRE 62.9

Old:

> De Unitate 4-5 survives in a single authorial text, and the version of chapters 4-5 commonly called the 'Primacy Text' -- reading more favourably toward Roman primacy than the alternative recension -- is a later interpolation into Cyprian's own original wording, not evidence of anything Cyprian himself wrote or revised.

New:

> De Unitate 4-5 survives in a single authorial text. One form of chapters 4-5 is often called the 'Primacy Text'. It reads more kindly toward Roman primacy than the other form does. It is a later interpolation. A later hand added it to Cyprian's own original words. It is no proof of what Cyprian himself wrote or revised.

### lpc.contested.grace-pelagius-characterization / claim

- Before: FK 30.0, FRE -16.9
- After: FK 7.4, FRE 60.1

Old:

> Augustine's own anti-Pelagian corpus accurately represents the position Pelagius himself held -- that a believer's own moral effort, unaided, is sufficient to obey what God commands -- and the later Reformation-era and modern Catholic/Protestant use of this same controversy to stake out opposing positions on grace and merit continues an argument whose terms Augustine himself correctly set.

New:

> Augustine's own anti-Pelagian writings show what Pelagius himself held. They show it as it was. Pelagius held that a believer's own moral effort, with no help, is enough to obey what God commands. Later Catholics and Protestants used this same dispute to take opposing sides on grace and merit. They did so in the Reformation era and again today. Their use carries on an argument. Augustine himself set its terms correctly.

### lpc.witness.answerability-as-ground / positions[1]

- Before: FK 8.5, FRE 57.0
- After: FK 7.8, FRE 61.7

Old:

> This is why the same office teaches the newly arrived, washes them, corrects them when they fail, and receives them home again. A road back without answerability behind it would be a bureaucratic formality. A font without it would be a private transaction. A council without it would be an argument no one is actually responsible for. Held together, they are what we actually are.

New:

> This is why the same office teaches the newly arrived, washes them, corrects them when they fail, and receives them home again. A road back without answerability behind it would be a bureaucratic formality. A font without it would be a private transaction. A council without it would be an argument that no one answers for. Held together, they are what we actually are.

### lpc.witness.baptism-traced-to-the-apostles / positions[0]

- Before: FK 9.3, FRE 50.3
- After: FK 7.5, FRE 61.0

Old:

> Augustine names two of our practices as apostolic in origin, by name, not only by a general conviction. Not rebaptizing someone already baptized among heretics is one. No one could find that this custom was invented later. He held that it is rightly believed to come down from the apostles.

New:

> Augustine names two of our practices as apostolic in origin. He names each one, and he does not rest on a general conviction. One is not rebaptizing someone who was baptized among heretics. No one could find that this custom was invented later. He held that it is rightly believed to come down from the apostles.

### lpc.witness.communion-over-separation / positions[0]

- Before: FK 12.4, FRE 55.7
- After: FK 6.7, FRE 71.9

Old:

> We can argue that a colleague's own ruling was wrong, at real length, without ever placing him outside our own table for having been wrong. One of us said it plainly, opening the very council that would decide the sharpest question in the room: no bishop sets himself up as a bishop of bishops, and none compels a colleague by force, since each has his own proper right of judgment. A century and a half later, another of us argued at book length that the ruling reached that day was mistaken, and never once suggested the man who reached it stood outside communion for it. Disagreement, in our own life, is not a reason to separate. It is close to the opposite: separating over a disagreement is the one thing we have organized our whole life never to do again.

New:

> We can argue that a colleague's own ruling was wrong, at real length. We do not treat him as outside our table for having been wrong. One of us said it plainly, opening the very council that would decide the sharpest question in the room. No bishop sets himself up as a bishop of bishops. None compels a colleague by force, since each has his own proper right of judgment. A century and a half later, another of us argued at book length that the ruling reached that day was mistaken. He never once suggested that the man who reached it stood outside communion for it. Disagreement, in our own life, is not a reason to separate. It is close to the opposite. Separating over a disagreement is the one thing we have organized our whole life never to do again.

### lpc.witness.communion-over-separation / positions[1]

- Before: FK 12.6, FRE 44.9
- After: FK 7.5, FRE 63.2

Old:

> Underneath the disagreement sits a belief neither of us ever gave up: the one episcopate is undivided, held whole by each bishop rather than parceled out between colleagues. That is exactly why disagreeing with a piece of it never means stepping outside all of it.

New:

> Underneath the disagreement sits a belief that neither of us ever gave up. The one episcopate is undivided. Each bishop holds all of it, and it is not parceled out between colleagues. That is exactly why disagreeing with a piece of it never means stepping outside all of it.

### lpc.witness.communion-over-separation / text

- Before: FK 12.7, FRE 53.2
- After: FK 7.6, FRE 66.5

Old:

> We can argue that a colleague's own ruling was wrong, at real length, and never once treat him as outside our own table for having been wrong. One of our own voices said it plainly, opening the very council that would decide the sharpest question in the room: no bishop sets himself up as a bishop of bishops, and none compels a colleague by force, since every bishop has his own proper right of judgment. A century and a half later, another of our own voices argued at book length that the ruling reached that day was mistaken, and never once suggested the man who reached it stood outside our communion for having reached it. Disagreement is not, for us, a reason to separate. It is close to the opposite: separating over a disagreement is the one thing our own life has organized itself never to repeat, because we have already watched what that costs. In our own first years, a deacon's own faction opened a rival congregation while our bishop was kept away in hiding, and in that same span a rival bishop was set up at Rome over a disputed election. We do not pretend those separations never happened. We hold our rule against separation because we already know, from our own record, what it costs when it breaks.

New:

> We can argue that a colleague's own ruling was wrong, at real length. We never once treat him as outside our own table for having been wrong. One of our own voices said it plainly, opening the very council that would decide the sharpest question in the room. No bishop sets himself up as a bishop of bishops. None compels a colleague by force, since every bishop has his own proper right of judgment. A century and a half later, another of our own voices argued at book length that the ruling reached that day was mistaken. He never once suggested that the man who reached it stood outside our communion for having reached it. Disagreement is not, for us, a reason to separate. It is close to the opposite. Separating over a disagreement is the one thing our own life has organized itself never to repeat. We have already watched what that costs. In our own first years, a deacon's own faction opened a rival congregation while our bishop was kept away in hiding. In that same span a rival bishop was set up at Rome over a disputed election. We do not pretend those separations never happened. We hold our rule against separation because we already know, from our own record, what it costs when it breaks.

### lpc.witness.confessor-claim-vs-regulated-peace / positions[1]

- Before: FK 14.0, FRE 49.8
- After: FK 6.9, FRE 69.9

Old:

> And yet the road back is examined, weighed, and walked in the open, under one office's own care -- not handed out on anyone's own certificate, however real their own suffering was. We hold both convictions as genuine: the process that must govern the return, and the claim that pressed hard enough, from inside our own life, to require a process at all.

New:

> And yet the road back is examined, weighed, and walked in the open, under one office's own care. It is not handed out on anyone's own certificate, however real their own suffering was. We hold both convictions as genuine. One is the process that must govern the return. The other is the claim that pressed hard enough, from inside our own life, to require a process at all.

### lpc.witness.confessor-claim-vs-regulated-peace / text

- Before: FK 10.5, FRE 62.7
- After: FK 7.6, FRE 70.6

Old:

> In our earliest years, a survivor of interrogation carried a claim of his own: that his own suffering gave him standing to ask that a named person, one who had failed the test he himself had passed, be received back into the congregation at once. We took that claim in earnest. His suffering was real, and so was what it carried. And it still had to be answered by something steadier than one man's own word, however genuine his suffering had been -- a name set down, examined, weighed, and received at the end by the very people who watched the failure. We hold both as real: the claim that pressed hard enough to demand a hearing, and the process that had to govern what the hearing decided. We have never found the place where these become one settled rule, and we do not expect to.

New:

> In our earliest years, a survivor of interrogation carried a claim of his own. His claim was that his own suffering gave him standing to ask that a named person be received back into the congregation at once. That person had failed the test he himself had passed. We took that claim in earnest. His suffering was real, and so was what it carried. And it still had to be answered by something steadier than one man's own word, however genuine his suffering had been. That steadier thing was a name set down, examined, weighed, and received at the end by the very people who watched the failure. We hold both as real: the claim that pressed hard enough to demand a hearing, and the process that had to govern what the hearing decided. We have never found the place where these become one settled rule, and we do not expect to.

### lpc.witness.constantine-did-not-corrupt / text

- Before: FK 11.7, FRE 54.9
- After: FK 7.3, FRE 67.7

Old:

> Did Constantine corrupt what we were? Augustine does not answer that question directly anywhere in our own record. The nearest he comes is City of God's own argument about why God let Constantine, a worshipper of the true God, gain such earthly power -- not to reward Christian belief with worldly success, but to show that greatness on earth never depended on worshipping the old gods after all. Constantine reigned long, held the empire alone, founded a city bearing no temple to the old gods, and died of old age with his sons to succeed him. But our bishop did not make Constantine's own success the proof of a Christian's standing before God, either. He named other Christian emperors, Jovian and Gratian, whom God did not grant the same long or peaceful reign -- precisely so that no one would become a Christian only to court a Constantine's own fortune.

New:

> Did Constantine corrupt what we were? Augustine does not answer that question directly anywhere in our own record. The nearest he comes is City of God's own argument about why God let Constantine, a worshipper of the true God, gain such earthly power. It was not to reward Christian belief with worldly success. It was to show that greatness on earth never depended on worshipping the old gods after all. Constantine reigned long and held the empire alone. He founded a city bearing no temple to the old gods. He died of old age, with his sons to succeed him. But our bishop did not make Constantine's own success the proof of a Christian's standing before God, either. He named other Christian emperors, Jovian and Gratian, whom God did not grant the same long or peaceful reign. He did this precisely so that no one would become a Christian only to court a Constantine's own fortune.

### lpc.witness.marriage-a-threefold-good / positions[0]

- Before: FK 10.2, FRE 50.5
- After: FK 7.8, FRE 60.7

Old:

> Augustine wrote a whole treatise on marriage, answering those who thought praising virginity meant condemning it. He named three things marriage is good for -- offspring, faithfulness, and what he called its sacrament.

New:

> Augustine wrote a whole treatise on marriage. He wrote it against those who thought that praising virginity meant condemning marriage. He named three things marriage is good for: offspring, faithfulness, and what he called its sacrament.

### lpc.witness.tradition-tested-by-apostolic-warrant / text

- Before: FK 8.7, FRE 59.7
- After: FK 7.7, FRE 62.9

Old:

> How do we test whether a practice of ours truly goes back to the apostles? We do not agree among ourselves on one single test. Cyprian held that nothing counts as apostolic unless it is written in the Gospel or in the apostles' own letters. Custom alone, however old, is not enough. Custom without truth, he said, is only the old age of error. Augustine argued a related question a century and a half later. He held the opposite: a custom kept everywhere in the Church may fairly be presumed apostolic, even where no apostle's own writing says so. We give you both tests, because both are ours. In this dispute itself, neither test traces the road back or the teaching before the water to a named apostolic origin. Elsewhere, Augustine does trace two other practices of ours -- not rebaptizing, and baptizing infants -- to the apostles by name, using this same second test.

New:

> How do we test whether a practice of ours truly goes back to the apostles? We do not agree among ourselves on one single test. Cyprian held that nothing counts as apostolic unless it is written in the Gospel or in the apostles' own letters. Custom alone, however old, is not enough. Custom without truth, he said, is only the old age of error. Augustine argued a related question a century and a half later. He held the opposite: a custom kept everywhere in the Church may fairly be presumed apostolic, even where no apostle's own writing says so. We give you both tests, because both are ours. In this dispute itself, neither test traces the road back or the teaching before the water to a named apostolic origin. Elsewhere, Augustine does trace two other practices of ours to the apostles by name. They are not rebaptizing, and baptizing infants. He uses this same second test.

### lpc.limit.411-gesta-unread / statement

- Before: FK 9.6, FRE 55.2
- After: FK 7.7, FRE 65.2

Old:

> A conference was held in 411, between our own bishops and the rival communion's own. It is the largest single gathering of inter-episcopal argument our own later years produced. We rest its date on the ordinary, undisputed record of when it happened. We do not draw on its own transcript of what was actually argued there, bishop by bishop. That transcript has not been validly read in building this record. What it would show about how our own bishops, beyond Cyprian and Augustine themselves, actually argued authority among themselves is not something we can tell you yet.

New:

> A conference was held in 411, between our own bishops and the rival communion's own. It is the largest single gathering of argument between bishops that our later years produced. We rest its date on the plain record of when it happened, which no one disputes. We do not draw on its own transcript of what was actually argued there, bishop by bishop. That transcript has not been validly read in building this record. We cannot yet tell you what it would show. It would show how our own bishops, beyond Cyprian and Augustine themselves, actually argued authority among themselves.

### lpc.story.election-of-cyprian / tellable_as

- Before: FK 9.8, FRE 58.4
- After: FK 8.5, FRE 66.4

Old:

> How we came to treat a recent convert's own election, over his reluctance, as God's own judgment made visible

New:

> How we came to read a recent convert's election, over his reluctance, as God's own judgment made plain

### lpc.story.the-death-of-cyprian / tellable_as

- Before: FK 9.9, FRE 50.6
- After: FK 6.3, FRE 66.1

Old:

> How our tradition remembered our first great bishop's death as a life fully given, completed

New:

> How our tradition remembered the death of our first great bishop. It was a life fully given, completed.

### lpc.term.grace / plain_meaning

- Before: FK 8.7, FRE 59.1
- After: FK 8.4, FRE 61.9

Old:

> For us, grace names the insistence that no one's own effort is ever sufficient on its own. Whatever good a person manages was given to them before they managed it.

New:

> For us, grace names the insistence that no one's own effort is ever enough on its own. Whatever good a person manages was given to them before they managed it.

### lpc.term.preaching / quick_meaning

- Before: FK 8.9, FRE 51.7
- After: FK 7.2, FRE 66.7

Old:

> For us, preaching is the weekly talk to those already baptized. It is how nearly everything else we hold reaches an ordinary believer.

New:

> For us, preaching is the weekly talk to those who are already baptized. It is how nearly all else we hold comes to an ordinary believer.

### lpc.figure.augustine / bridge_line

- Before: FK 14.7, FRE 50.4
- After: FK 8.0, FRE 67.7

Old:

> our bishop at Hippo, seized by our own acclaim for the office twice over his own reluctance, who spent his last days weeping over psalms of penitence while an army lay outside the walls

New:

> our bishop at Hippo, seized by our own acclaim for the office twice over his own reluctance. He spent his last days weeping over psalms of penitence while an army lay outside the walls.

### lpc.figure.celerinus / bridge_line

- Before: FK 12.5, FRE 48.5
- After: FK 7.8, FRE 60.7

Old:

> a confessor who did not write about his own suffering, but about his sister's, and asked another confessor in prison to help restore her

New:

> a confessor who did not write about his own suffering, but about his sister's. He asked another confessor in prison to help restore her.

### lpc.figure.cyprian / bridge_line

- Before: FK 13.7, FRE 44.7
- After: FK 6.7, FRE 63.0

Old:

> our bishop, chosen while still a neophyte over his own reluctance, who taught us to care for our enemies during a plague and was executed under Valerian

New:

> our bishop, chosen while still a neophyte over his own reluctance. He taught us to care for our enemies during a plague. He was executed under Valerian.

### lpc.figure.lucian / bridge_line

- Before: FK 11.5, FRE 60.4
- After: FK 6.3, FRE 74.8

Old:

> a confessor who answered from a cell where he expected to die of hunger and thirst, granting peace to three women he had never met in person

New:

> a confessor who answered from a cell where he expected to die of hunger and thirst. He granted peace to three women he had never met in person.

### lpc.figure.numidicus / bridge_line

- Before: FK 10.2, FRE 69.8
- After: FK 5.0, FRE 83.9

Old:

> a man who watched his own wife die with those he had exhorted to martyrdom, was himself left for dead, and did not want to have survived

New:

> a man who watched his own wife die with those he had exhorted to martyrdom. He was himself left for dead, and did not want to have survived.

### lpc.figure.pontius / bridge_line

- Before: FK 13.0, FRE 55.1
- After: FK 7.2, FRE 70.4

Old:

> our bishop's own deacon, who stayed with him through exile and wrote, after the execution, the account by which most of what we remember of Cyprian's own life reaches us

New:

> our bishop's own deacon, who stayed with him through exile. After the execution he wrote the account by which most of what we remember of Cyprian's own life reaches us.

### lpc.force.congregational-acclamation-overriding-preference / description

- Before: FK 8.7, FRE 55.0
- After: FK 7.6, FRE 60.4

Old:

> Cyprian was a trained rhetorician who converted in middle life. Within roughly two to three years of his conversion, the people of Carthage elected him bishop by acclamation. Five presbyters are recorded as opposing him. He called it "your suffrage and God's judgment," set against a faction's "ancient venom." A deacon who knew him described it from outside. By the judgment of God and the favour of the people, he wrote, Cyprian was chosen for the priesthood and the rank of bishop while still newly baptised.
>
> The pattern recurs in the second phase, at both of Augustine's offices. In 391 he was seized into the presbyterate at Hippo against his wishes. For the episcopate, Possidius's Vita, chapter VIII, records the scene. Valerius announced his intention to the bishops present, the whole Hippo clergy, and all the people. Those who heard rejoiced and clamoured eagerly for it. Augustine refused the episcopate while his own bishop lived. Then, persuaded by precedent from overseas and from Africa, he yielded under compulsion and constraint.
>
> The evidence is documented. It comes from Cyprian's Epistle XXXIX, from Pontius, and from Possidius's Vita, chapters IV and VIII.
>
> This force gives the pastoral office its two-way shape. A bishop answers to the people who placed him, as well as for them. One caution is kept rather than smoothed over. The pattern is attested through different people and in different words, not through one recurring term. But it appears at the same office in both phases.
>
> Two conditions shaped it. An office with no legal protection is one a sensible man declines, so the acclamation had to override reluctance. And a church organized enough to hold factions was organized enough to elect a bishop over a faction's opposition.

New:

> Cyprian was a trained rhetorician who converted in middle life. Within roughly two to three years of his conversion, the people of Carthage elected him bishop by acclamation. Five presbyters are recorded as opposing him. He called it "your suffrage and God's judgment," set against a faction's "ancient venom." A deacon who knew him described it from outside. The deacon wrote that, by the judgment of God and the favour of the people, Cyprian was chosen for the priesthood and the rank of bishop. He was still newly baptised.
>
> The pattern recurs in the second phase, at both of Augustine's offices. In 391 he was seized into the presbyterate at Hippo against his wishes. For the episcopate, Possidius's Vita, chapter VIII, records the scene. Valerius announced his intention to the bishops present, the whole Hippo clergy, and all the people. Those who heard were glad and clamoured eagerly for it. Augustine refused the office of bishop while his own bishop lived. He was persuaded by precedent from overseas and from Africa. Then he yielded, under compulsion and constraint.
>
> The evidence is documented. It comes from Cyprian's Epistle XXXIX, from Pontius, and from Possidius's Vita, chapters IV and VIII.
>
> This force gives the pastoral office its two-way shape. A bishop answers to the people who placed him, as well as for them. We keep one caution rather than smooth it over. Different people attest the pattern, in different words. No one recurring term carries it. But it appears at the same office in both phases.
>
> Two conditions shaped it. An office with no legal protection is one a sensible man declines. So the acclamation had to override reluctance. And a church with enough order to hold factions had enough order to elect a bishop over a faction's opposition.

### lpc.force.decian-persecution-libelli-system / description

- Before: FK 8.8, FRE 54.8
- After: FK 7.8, FRE 60.1

Old:

> The Decian persecution was the first empire-wide persecution to be systematically enforced. It worked through certificates recording that the holder had sacrificed. It did not mainly demand that Christians renounce their faith. It demanded a documented act of compliance. A person could obtain one by performing the sacrifice, or by paying to have it recorded. This is documented in Cyprian's crisis correspondence, which carries the higher citation grade (A), and in his De Lapsis, which carries the lower grade (B).
>
> It was felt not so much as an attack from outside as a table emptied one certificate at a time. The demand reached each person singly. It left the congregation sorted into those who had stood and those who had not. Both groups still belonged, still in the room. Cyprian said that when the flock is wounded, the shepherd is the one wounded most.
>
> This force created the category that the whole penitential system exists to process. There were no lapsed before there was a certificate to obtain. There were no confessors with a claim on anything before there was an interrogation to survive. So it produced two things at once. One was the ongoing contest over members who had failed, and the discipline for restoring them. The other was the confessors' rival claim to grant peace, which pushes against that discipline.
>
> It also sharpened the bishop's answerability, which becomes acute exactly when his people fail. And it produced this world's densest crisis vocabulary: the lapsed, reconciliation, confessor, and the certificates of both kinds.
>
> The later Valerianic persecution repeated this test. By then the community had built a discipline to meet it.

New:

> The Decian persecution was the first empire-wide persecution to be systematically enforced. It worked through certificates recording that the holder had sacrificed. It did not mainly demand that Christians renounce their faith. It asked for a documented act of compliance. A person could obtain one by making the sacrifice, or by paying to have it recorded. Cyprian's crisis correspondence documents this, at the higher citation grade (A). His De Lapsis documents it too, at the lower grade (B).
>
> It was felt not so much as an attack from outside as a table emptied one certificate at a time. The demand reached each person singly. It left the congregation sorted into those who had stood and those who had not. Both groups still belonged, still in the room. Cyprian said that when the flock is wounded, the shepherd is the one wounded most.
>
> This force created the class of people that the whole penitential system exists to handle. There were no lapsed before there was a certificate to obtain. There were no confessors with a claim on anything before there was an interrogation to survive. So it made two things at once. One was the ongoing contest over members who had failed, and the discipline for restoring them. The other was the confessors' rival claim to grant peace, which pushes against that discipline.
>
> It also made the bishop's answerability sharper. It grows acute just when his people fail. It also made this world's densest crisis vocabulary: the lapsed, reconciliation, confessor, and the certificates of both kinds.
>
> The later Valerianic persecution repeated this test. By then the community had built a discipline to meet it.

### lpc.force.donatist-schism / description

- Before: FK 8.8, FRE 58.1
- After: FK 7.9, FRE 61.0

Old:

> The Donatist church was dominant across large parts of North African Christian life for most of the century between the two phases. It remained a live pastoral problem throughout Augustine's time as bishop. This is documented.
>
> The Donatists were not strangers to this world, and not heretics of a foreign kind. They were a church in the same towns, with its own bishop in the same see, claiming to be the only true church. For their central practice, they appealed to a ruling by Cyprian, this world's own first bishop.
>
> In the second phase, no force had more far-reaching effects. It made the validity of sacraments across the church's boundary an urgent question for the institution, not only for individual converts. It tested, at its hardest edge, whether communion could hold despite disagreement, and communion held.
>
> It is also the whole reason Augustine argued about the authority of councils at all. The Donatists' appeal to Cyprian's conciliar acts obliged him to argue against a predecessor he could not disown. That prompt came from outside, but the reading and the argument were Augustine's own.
>
> Finally, it was the outside pressure behind Augustine's teaching on coercion. That teaching has to be held in its three phases, not compressed into one. A rival communion is what made the state's newly available power worth using.

New:

> The Donatist church was dominant across large parts of North African Christian life for most of the century between the two phases. It remained a live pastoral problem throughout Augustine's time as bishop. This is documented.
>
> The Donatists were not strangers to this world, and not heretics of a foreign kind. They were a church in the same towns. Their church had its own bishop in the same see, and it claimed to be the only true church. For their central practice, they appealed to a ruling by Cyprian, this world's own first bishop.
>
> In the second phase, no force had more far-reaching effects. It made the validity of sacraments across the church's boundary an urgent question for the institution, not only for individual converts. It tested, at its hardest edge, whether communion could hold despite disagreement. Communion held.
>
> It is also the whole reason Augustine argued about the authority of councils at all. The Donatists' appeal to Cyprian's conciliar acts obliged him to argue against a predecessor he could not disown. That prompt came from outside. But the reading and the argument were Augustine's own.
>
> Finally, it was the outside pressure behind Augustine's teaching on coercion. That teaching has to be held in its three phases, not compressed into one. A rival communion is what made the state's newly available power worth using.

### lpc.force.inherited-latin-theological-vocabulary / description

- Before: FK 8.8, FRE 59.5
- After: FK 7.3, FRE 63.6

Old:

> Before this world begins, North African Latin Christianity already had a vigorous local literary culture, along with a Latin theological vocabulary that Tertullian is credited with forging. This is widely accepted.
>
> The words were already to hand -- what had to be argued could be argued in the language the people in the assembly already spoke.
>
> This made preaching and catechesis possible as the main way of forming people, since that depends on a theological language in the people's own tongue, able to carry the content.
>
> The force is treated briefly, in proportion to its weight. It is real and enabling. But it is not contested and not tied to one phase. It does not shape what the world's central concerns say, only the medium they are said in. No link to any other force is named for it.

New:

> Before this world begins, North African Latin Christianity already had a vigorous local literary culture. It also had a Latin theological vocabulary that Tertullian is credited with forging. This is widely accepted.
>
> The words were already to hand. What had to be argued could be argued in the language the people in the assembly already spoke.
>
> This made preaching and catechesis possible as the main way of forming people. That way depends on a theological language in the people's own tongue, able to carry the content.
>
> The force is treated briefly, in proportion to its weight. It is real and enabling. But it is not contested and not tied to one phase. It does not shape what the world's central concerns say, only the medium they are said in. No link to any other force is named for it.

### lpc.force.organized-carthaginian-church / description

- Before: FK 10.5, FRE 46.8
- After: FK 7.6, FRE 61.1

Old:

> Cyprian inherited a church large and structured enough to hold real internal factions. It could also call councils of dozens of bishops at short notice. The evidence is documented: the councils themselves, and the Felicissimus material in Cyprian's letters.
>
> From the inside, this was not a gathering that had to be built. It was already standing, with its own men of weight, its own quarrels, and its own ability to meet and decide together.
>
> This organization made it possible to keep communion among colleagues who disagreed. That needs colleagues who can actually meet, and who already disagree. It also made a regulated process of penance possible, because an unorganized community could not have run one. And it supplied the council setting where both formulas of conciliar authority were eventually spoken.
>
> A church organized enough to hold factions was also organized enough to carry an election against a faction's opposition. And the councils that met and left written acts are what Augustine later read and argued with.

New:

> Cyprian inherited a church large enough, and structured enough, to hold real factions inside it. It could also call councils of dozens of bishops at short notice. The evidence is documented. It is the councils themselves, and the Felicissimus material in Cyprian's letters.
>
> From the inside, this was not a gathering that had to be built. It was already standing. It had its own men of weight, its own quarrels, and its own ability to meet and decide together.
>
> Because the church was organized, bishops who disagreed could still keep communion. That needs colleagues who can really meet, and who already disagree. It also made possible a process of penance run by rule. A community with no organization could not have run one. And it supplied the council setting. There, in time, both formulas of conciliar authority were spoken.
>
> A church with enough order to hold factions had enough order to carry an election against a faction's opposition. And the councils that met and left written acts are what Augustine later read and argued with.

### lpc.force.recurring-contest-failed-member / description

- Before: FK 8.6, FRE 57.3
- After: FK 7.7, FRE 61.5

Old:

> Under Cyprian, the contest was over the lapsed. Under Augustine, it was over ordinary sin after baptism, and over believers tempted by schism. The contest is documented in both periods.
>
> This was the question that would not go away, felt from inside: what do you owe someone who is yours and has failed? A church that takes everyone back the same afternoon has no door. One that takes no one back has no Master.
>
> In the first phase, this contest directly produced the church's penitential discipline. In that same phase, it also connects to the question of valid sacraments and ordination across the church's boundary. Both are questions of boundary and return, and Cyprian reasons about them consistently.
>
> It is only a qualified claim that the contest lasts into the second phase, not an assumed one. The concern does not continue under its own name. What survives is a family resemblance to two separately tested concerns: sacramental validity, and grace and human incapacity. The debate over grace reshapes the old concern; it does not continue it. So that later link is a resemblance only, not a direct connection. This force connects to penitential discipline and sacramental validity, both in the first phase. It does not connect to grace.
>
> The Decian edict created the category of the failed member that this contest is about. The confessors' own parallel system sharpened it. Because of that rival system, the contest had to be settled by a formal process, not by the bishop's word alone.

New:

> Under Cyprian, the contest was over the lapsed. Under Augustine, it was over everyday sin after baptism, and over believers tempted by schism. The contest is documented in both periods.
>
> This was the question that would not go away, felt from inside: what do you owe someone who is yours and has failed? A church that takes everyone back the same afternoon has no door. One that takes no one back has no Master.
>
> In the first phase, this contest directly produced the church's penitential discipline. In that same phase, it also connects to the question of valid sacraments and ordination across the church's boundary. Both are questions of boundary and return. Cyprian reasons about both in the same way.
>
> It is only a qualified claim that the contest lasts into the second phase, not an assumed one. The concern does not continue under its own name. What survives is a family resemblance to two concerns that were tested separately: sacramental validity, and grace and human incapacity. The debate over grace reshapes the old concern. It does not continue it. So that later link is a resemblance only, not a direct connection. This force connects to penitential discipline and sacramental validity, both in the first phase. It does not connect to grace.
>
> The Decian edict created the class of failed member that this contest is about. The confessors' own parallel system made it sharper. Because of that rival system, the contest had to be settled by a formal process, not by the bishop's word alone.

### lpc.force.standing-legal-condition-unlicensed-religion / description

- Before: FK 9.1, FRE 54.0
- After: FK 7.6, FRE 60.6

Old:

> Throughout this world's first phase, Christianity had no legal standing. It lived in a Romanized provincial society with real underlying Punic populations and, inland, Berber ones. Persecution came and went, but the exposure never stopped. This picture is widely accepted.
>
> It meant that a bishop could be taken, and was. The office carried no protection, and the community had no recourse. What it had was each other, and whatever a man would do for the people in his charge while he still could.
>
> This condition is why the pastoral office grew as personal answerability rather than as jurisdiction. An office with nothing outside to enforce it is held together by the bond between one man and one congregation.
>
> In the second phase, the condition was removed. We considered whether that shift was itself one of this world's own central concerns, but nothing in this world organizes around the shift itself. It is named here as a force precisely because it is not one of those central concerns. It shaped what the office could be without becoming something the world organizes around.
>
> An office with no legal protection is one a sensible man declines. That is why congregations had to override a chosen man's reluctance by acclamation. The same fact also appears at both ends of this world with opposite sign. The later shift from illegal to established religion removes exactly this condition.

New:

> Throughout this world's first phase, Christianity had no legal standing. It lived in a Romanized provincial society. Beneath that society were real Punic populations and, inland, Berber ones. Persecution came and went, but the exposure never stopped. This picture is widely accepted.
>
> It meant that a bishop could be taken, and was. The office carried no protection, and the community had no recourse. What it had was each other. It also had whatever a man would do for the people in his charge while he still could.
>
> This condition is why the pastoral office grew as personal answerability rather than as jurisdiction. An office with nothing outside to enforce it is held together by the bond between one man and one congregation.
>
> In the second phase, the condition was removed. We considered whether that shift was itself one of this world's own central concerns. But nothing in this world is built around the shift itself. It is named here as a force precisely because it is not one of those central concerns. It shaped what the office could be. It did not become something the world is built around.
>
> An office with no legal protection is one a sensible man declines. That is why congregations had to override a chosen man's reluctance by acclamation. The same fact also appears at both ends of this world with opposite sign. The later shift from illegal to established religion removes this very condition.

### lpc.force.valerianic-persecution / description

- Before: FK 8.3, FRE 57.2
- After: FK 6.8, FRE 63.1

Old:

> Imperial persecution returned under Valerian. Cyprian was exiled and then martyred in 258. This is documented, including in the Acta Proconsularia.
>
> The thing had not finished with them. The man who had spent seven years deciding what to do with those who failed the first test was taken by the second. He did not fail it.
>
> This persecution confirms two of the world's concerns rather than reshaping them: the pastoral office, and the tension between confessors and bishops. It closes the first phase by showing what the confessors' credential had been about. It shows this in the person of the bishop who had regulated the lapsed. It also ends the first phase's written record. That is why penitential discipline and the confessor tension are attested only within that phase.
>
> The Valerianic persecution repeats the Decian test on a community that has now built a discipline for it.

New:

> Imperial persecution returned under Valerian. Cyprian was exiled and then martyred in 258. This is documented, including in the Acta Proconsularia.
>
> The thing had not finished with them. The man had spent seven years deciding what to do with those who failed the first test. The second test took him. He did not fail it.
>
> This persecution confirms two of the world's concerns. It does not reshape them. They are the pastoral office, and the tension between confessors and bishops. It closes the first phase by showing what the confessors' credential had been about. It shows this in the person of the bishop who had regulated the lapsed. It also ends the first phase's written record. That is why penitential discipline and the confessor tension are attested only within that phase.
>
> The Valerianic persecution repeats the Decian test. It falls on a community that has now built a discipline for it.

### lpc.gravity.collegial-communion-preserved / description

- Before: FK 8.7, FRE 53.7
- After: FK 7.4, FRE 60.8

Old:

> Few things mattered more to this world than staying in communion despite real disagreement. Bishops in this world disagree, sometimes sharply. But they work to keep communion rather than break it and build a rival hierarchy.
>
> The pattern recurs across both phases. Cyprian's preface to the Council of 256 states it directly. None of them sets himself up as a bishop of bishops, and every bishop has his own right to judge. Augustine's On Baptism argues at length against Cyprian's own ruling on rebaptism. Yet it never treats him as outside communion. Letter 185 addresses the Donatist schism in the same pastoral, corrective tone.
>
> Our own case for this world's coherence across the century between its two bishops rests on this concern. A bishop who disagrees has two paths. He can work to keep communion, or he can break it and set up a parallel hierarchy. Both bishops take the first path. Neither breaks fellowship over the sharpest doctrinal disputes in the record. Neither bishop's writings hold a single counter-example.
>
> This explains why Augustine's long, respectful argument with a bishop he disputes reads as a son arguing with a father, not a rejection. It also directly explains the world's boundary against Donatism. The pattern shows in both phases, in how both bishops act, not just in a shared word. It reinforces pastoral office, penitential discipline, conciliar authority, and sacramental validity. Sacramental validity is the doctrinal question where it is tested hardest.
>
> The confidence split is disclosed, not resolved. The underlying facts are solidly attested. The 256 preface's own words and On Baptism's long argument are directly quoted and checked. But reading them as one concern across both phases, rather than two separate historical facts, is an interpretation. That interpretation stands at Widely Accepted, and the record carries this more cautious rating instead of hiding the split.
>
> Every force linked to this concern tested it rather than created it. The organized Carthaginian church gave colleagues who could meet and already disagreed. The Donatist schism tested it at its hardest edge. Augustine's engagement with Cyprian's conciliar acts tested it across the century gap. It held each time. It is this world's own way of adapting, tested three times from three directions.

New:

> Few things mattered more to this world than staying in communion despite real disagreement. Bishops in this world disagree, sometimes sharply. But they work to keep communion rather than break it and build a rival hierarchy.
>
> The pattern recurs across both phases. Cyprian's preface to the Council of 256 states it directly. None of them sets himself up as a bishop of bishops. Every bishop has his own right to judge. On Baptism by Augustine argues at length against Cyprian's own ruling on rebaptism. Yet it never treats him as outside communion. Letter 185 addresses the Donatist schism in the same pastoral, corrective tone.
>
> Our own case that this world holds together across the century between its two bishops rests on this concern. A bishop who disagrees has two paths. He can work to keep communion, or he can break it and set up a parallel hierarchy. Both bishops take the first path. Neither breaks fellowship over the sharpest doctrinal disputes in the record. Neither bishop's writings hold a single counter-example.
>
> This explains why the long, respectful argument of Augustine with a bishop he disputes reads as a son arguing with a father. It does not read as a rejection. It also directly explains the world's boundary against Donatism. The pattern shows in both phases. It shows in how both bishops act, not just in a shared word. It supports pastoral office, penitential discipline, conciliar authority, and sacramental validity. Sacramental validity is the doctrinal question where it is tested hardest.
>
> We disclose the confidence split and do not resolve it. The facts beneath it are firmly attested. The 256 preface's own words and On Baptism's long argument are quoted word for word and checked. But reading them as one concern across both phases is an interpretation. The alternative is to read them as two separate facts of history. That interpretation stands at Widely Accepted. The record carries this more cautious rating instead of hiding the split.
>
> Every force linked to this concern tested it rather than created it. The organized Carthaginian church gave colleagues who could meet and already disagreed. The Donatist schism tested it at its hardest edge. Augustine dealt with Cyprian's conciliar acts. That tested it across the century gap. It held each time. It is this world's own way of adapting, tested three times from three directions.

### lpc.gravity.confessor-authority-vs-episcopal-peace / description

- Before: FK 8.7, FRE 54.9
- After: FK 7.4, FRE 60.2

Old:

> This is an unresolved tension in this world, not a settled concern: two real, opposed pressures held against each other rather than settled. One limit should be said up front: the evidence rests mainly on one source, Cyprian's Epistles, read through a single term in this world's lexicon.
>
> The first pole belongs to the confessors. These were Christians who survived interrogation under persecution. On the strength of their confession, they wrote requests that named lapsed persons be received back. This was an informal claim to grant peace. The second pole is Cyprian's own penitential process, regulated and controlled by the bishop. He built it specifically to answer that rival claim.
>
> The tension recurs rather than resolves. Epistles XX-XXI show the confessors using this claimed authority themselves, in the first person. De Lapsis and Cyprian's letters on penance show the regulated answer. Penitential discipline has the shape it does because a rival claim to grant peace already existed. That claim had to be brought under order; the discipline was not invented from nothing.
>
> The tension shapes Cyprian's own conduct. Throughout his crisis letters he must keep reasserting the bishop's authority over reconciliation, instead of settling it once. It explains why De Lapsis and the letters on the lapsed insist so strongly on the bishop's control over readmission. Penitential discipline alone does not fully explain that insistence.
>
> The tension lasts only through Cyprian's crisis years. There it is a persistent, unresolved counter-pressure, not a force that organizes the world as a whole. That is what makes it a tension. It is not a failure. It competes with penitential discipline and reinforces the pastoral office.
>
> Both poles are solidly attested. The confessors' own letters in Epistles XX-XXI and the regulating argument of De Lapsis show them in their own words. The Epistles carry the higher citation grade (A) and De Lapsis the lower (B). Neither side lacks for evidence -- the tension itself is the finding.
>
> The forces around it hold the tension in place rather than resolve it. The Decian persecution created confessors as a class with any claim to authority at all. The Valerianic persecution confirmed the tension rather than reshaping it, and it ended the phase in which the tension appears. The confessors' claim is itself a force. All three forces belong to the first phase. A positive check found no confessor-authority material from Augustine's phase anywhere in this world's sources. That confirms the tension belongs to the first phase alone.

New:

> This is an unresolved tension in this world, not a settled concern. It is two real, opposed pressures held against each other rather than settled. One limit should be said up front. The evidence rests mainly on one source, Cyprian's Epistles, read through a single term in this world's lexicon.
>
> The first pole belongs to the confessors. These were Christians who lived through interrogation under persecution. On the strength of their confession, they wrote requests that named lapsed people be received back. This was an informal claim to grant peace. The second pole is Cyprian's own penitential process, run by rule and held under the bishop's control. He built it expressly to answer that rival claim.
>
> The tension recurs rather than resolves. Epistles XX-XXI show the confessors using this claimed authority themselves, in the first person. De Lapsis and Cyprian's letters on penance show the regulated answer. Penitential discipline has the shape it does because a rival claim to grant peace already existed. That claim had to be brought under order. The discipline was not invented from nothing.
>
> The tension shapes Cyprian's own conduct. Throughout his crisis letters he must keep restating the bishop's authority over reconciliation. He cannot settle it once. It explains why De Lapsis and the letters on the lapsed insist so strongly on the bishop's control over readmission. Penitential discipline alone does not fully explain that insistence.
>
> The tension lasts only through Cyprian's crisis years. There it is a lasting, unresolved counter-pressure, not a force that organizes the world as a whole. That is what makes it a tension. It is not a failure. It competes with penitential discipline and supports the pastoral office.
>
> Both poles are firmly attested. The confessors' own letters in Epistles XX-XXI show their side in their own words. The regulating argument of De Lapsis shows the other. The Epistles carry the higher citation grade (A) and De Lapsis the lower (B). Neither side lacks for evidence. The tension itself is the finding.
>
> The forces around it hold the tension in place rather than resolve it. The Decian persecution created confessors as a class with any claim to authority at all. The Valerianic persecution confirmed the tension. It did not reshape it. It ended the phase in which the tension appears. The confessors' claim is itself a force. All three forces belong to the first phase. A positive check found no confessor-authority material from Augustine's phase anywhere in this world's sources. That confirms the tension belongs to the first phase alone.

### lpc.gravity.pastoral-office-flock-keeping / description

- Before: FK 10.2, FRE 46.1
- After: FK 7.9, FRE 60.5

Old:

> This is the concern everything else in this world turns on. A bishop is personally answerable for a bounded flock, and much of the rest of the world flows from that.
>
> It recurs without a break across every primary source for both bishops and both phases. It appears in both bishops' stories of coming to office, in the crisis letters of both phases, and in both collections of sermons.
>
> Other concerns in this world depend on it. Penitential discipline is carried out by a bishop who holds this office. Preaching and catechesis are the office's main activity. Conciliar authority is a theory about who legitimately holds the office. Sacramental validity asks the same question. This world's own formation is pastoral and sacramental before it is juridical. The whole apparatus of teaching and penance exists because a bishop answers personally for his flock.
>
> It explains why Cyprian's crisis letters exist at all and why Augustine's sermon collection is so large. It also explains why both bishops' accounts of coming to office are independently attested and treated as formative. It is visible in both Carthage and Hippo, across both phases, in both bishops' own words. It reinforces penitential discipline, collegial communion, preaching and catechesis, sacramental validity, and the confessor tension. Conciliar authority reinforces it weakly. No relationship with grace and human incapacity has been shown.
>
> The evidence is solidly attested. Accounts of holding and exercising this office are directly quoted and checked: the preface to the Council of 256, Augustine's own Letters XXXI and CCXIII, and Pontius's narrative. Possidius's Life of Augustine is not counted; that account has not independently been checked beyond identifying the Megalius consecration. So the rating rests on Pontius, the two letters, and the 256 preface alone.
>
> It is the concern most densely connected to the forces acting on the world. Christianity's standing legal condition as an unlicensed religion means the office has no outside enforcement. Personal bond holds it together. Congregational acclamation shows how a man comes to hold the office. The Decian and Valerianic persecutions make his answerability acute, through the flock's own failure and the bishop's own test. The plague is a pressure the bishop shares rather than judges. The Vandal invasion and siege of Hippo mark where the bond ends: it ends when the bishop does.

New:

> This is the concern all else in this world turns on. A bishop is answerable in person for a bounded flock, and much of the rest of the world flows from that.
>
> It recurs without a break across every primary source for both bishops and both phases. It appears in both bishops' stories of coming to office, in the crisis letters of both phases, and in both collections of sermons.
>
> Other concerns in this world depend on it. A bishop who holds this office runs penitential discipline. Preaching and catechesis are the main work of the office. Conciliar authority is a theory about who has the right to hold the office. Sacramental validity asks the same question. This world's own formation is pastoral and sacramental before it is a matter of law. The whole structure of teaching and penance exists because a bishop answers in person for his flock.
>
> It explains why Cyprian's crisis letters exist at all and why the sermon collection of Augustine is so large. It also explains why both bishops' accounts of coming to office are attested apart from one another and treated as formative. It shows in both Carthage and Hippo, across both phases, in both bishops' own words. It supports penitential discipline and collegial communion. It supports preaching and catechesis, sacramental validity, and the confessor tension. Conciliar authority supports it weakly. No link with grace and human incapacity has been shown.
>
> The evidence is firmly attested. Accounts of holding and using this office are quoted word for word and checked. They are the preface to the Council of 256, Letters XXXI and CCXIII by Augustine himself, and the narrative by Pontius. We do not count the Life of Augustine by Possidius. That account has had no separate check beyond identifying the Megalius consecration. So the rating rests on Pontius, the two letters, and the 256 preface alone.
>
> It is the concern with the most ties to the forces acting on the world. Christianity's standing legal condition as an unlicensed religion means that nothing outside enforces the office. Personal bond holds it together. Acclamation by the congregation shows how a man comes to the office. The Decian and Valerianic persecutions make his answerability acute. They work through the flock's own failure and the bishop's own test. The plague is a pressure the bishop shares rather than judges. The Vandal invasion and siege of Hippo mark where the bond ends. It ends when the bishop does.

### lpc.gravity.penitential-discipline / description

- Before: FK 8.4, FRE 55.3
- After: FK 7.5, FRE 60.4

Old:

> How the church received back its own failed members sat close to the center of this world's own life. This concern asks what happens to someone who gave way under persecution. Its answer is readmission, not permanent exclusion.
>
> It recurs strongly: in De Lapsis, in the letters about the lapsed, in Pontius's narrative, and in the world's liturgical evidence. One more limit belongs here. The evidence from Cyprian's phase comes from several independent sources that support each other. But the claim that this concern spans both phases rests on Cyprian's phase alone.
>
> Other concerns in this world depend on it. The confessor tension exists only because this one does. Its answer for the single believer is to readmit rather than exclude for ever. That mirrors, at a smaller scale, the logic of collegial communion. It is the model practice for shaping believers in this world's record. It explains two schisms. The Novatianists refused to readmit the lapsed at all. The Felicissimus schism offered a laxer rival route back. It also explains the confessor tension.
>
> Whether it continues into Augustine's phase was checked directly, not assumed. It holds directly for Cyprian's phase. For Augustine's phase, the case for continuity does not fully survive as this same concern under its own name. No text from Augustine's phase is organized around a crisis like that of the lapsed, at the same acute, empire-wide scale.
>
> The closest parallels are real: the pull toward the Donatist schism, and the ordinary sin of catechized believers. But those were tested and found to be concerns of their own, sacramental validity and grace and human incapacity. They are not its direct continuation. What crosses the boundary between the phases is a family resemblance, not the same concern restated.
>
> It reinforces pastoral office, collegial communion, preaching and catechesis, and sacramental validity. Grace and human incapacity reshapes it without continuing it. It competes with the confessor tension.
>
> The evidence is solidly attested for Cyprian's own conduct and letters, which are directly quoted and checked. The De Lapsis passage carries the lower citation grade (B). The Epistles and Pontius passages carry the higher grade (A). None of it runs short of evidence for Cyprian's phase.
>
> It is itself this world's ongoing internal pressure. Four forces connect to it. The Decian persecution created its subject matter. The organized Carthaginian church made a regulated process possible at all. It answers the recurring contest over the failed member. It was built against a rival claim, the confessors' claim to grant peace. Its life in the second phase is qualified, not assumed: the concern does not continue under its own name. So its ties to the forces stay rooted in the first phase.

New:

> How the church received back its own failed members sat close to the center of this world's own life. This concern asks what happens to someone who gave way under persecution. Its answer is readmission. It does not shut the person out for good.
>
> It recurs strongly: in De Lapsis, in the letters about the lapsed, in Pontius's narrative, and in the world's liturgical evidence. One more limit belongs here. The evidence from Cyprian's phase comes from several independent sources that support each other. But the claim that this concern spans both phases rests on Cyprian's phase alone.
>
> Other concerns in this world depend on it. The confessor tension exists only because this one does. Its answer for the single believer is to readmit rather than exclude for ever. That mirrors, at a smaller scale, the logic of collegial communion. It is the model practice for shaping believers in this world's record. It explains two schisms. The Novatianists refused to readmit the lapsed at all. The Felicissimus schism offered a laxer rival route back. It also explains the confessor tension.
>
> We checked directly whether it continues into Augustine's phase. We did not assume it. It holds in Cyprian's phase itself. For Augustine's phase, the case that it continues does not fully survive as this same concern under its own name. No text from Augustine's phase is organized around a crisis like that of the lapsed, at the same acute, empire-wide scale.
>
> The closest parallels are real: the pull toward the Donatist schism, and the ordinary sin of catechized believers. But those were tested and found to be concerns of their own, sacramental validity and grace and human incapacity. They do not carry it on directly. What crosses the boundary between the phases is a family resemblance. It is not the same concern restated.
>
> It supports pastoral office, collegial communion, preaching and catechesis, and sacramental validity. Grace and human incapacity reshapes it without continuing it. It competes with the confessor tension.
>
> The evidence is firmly attested for Cyprian's own conduct and letters, which are quoted word for word and checked. The De Lapsis passage carries the lower citation grade (B). The Epistles and Pontius passages carry the higher grade (A). None of it runs short of evidence for Cyprian's phase.
>
> It is itself this world's ongoing internal pressure. Four forces connect to it. The Decian persecution created its subject matter. The organized Carthaginian church made a process run by rule possible at all. It answers the recurring contest over the failed member. It was built against a rival claim, the confessors' claim to grant peace. Its life in the second phase is qualified, not assumed. The concern does not continue under its own name. So its ties to the forces stay rooted in the first phase.

### lpc.gravity.preaching-and-catechesis / description

- Before: FK 9.9, FRE 48.6
- After: FK 7.8, FRE 60.2

Old:

> This concern is real too, though its reach is narrower than the others'. It is the medium through which this world's other central concerns are taught, rather than a force that organizes the world by itself. It clearly recurs, shapes believers, and lasts across both phases. But its links to other concerns, and what it explains, are narrower.
>
> It recurs in Augustine's Sermons and Tractates on John, in the catechetical works, and in Cyprian's De Dominica Oratione. Pastoral office depends on it as its main activity. But nothing else depends on it the way pastoral office, penitential discipline, and collegial communion do. It is the channel through which those concerns are taught and enforced.
>
> Its power to shape believers is strong and direct. That is the explicit subject of the catechetical works and the stated purpose of both bishops' preaching. It explains how formation happens more than why any particular crisis occurred. It is attested in both phases, in both bishops' own words. It reinforces pastoral office, penitential discipline, and grace and human incapacity. No relationship has been shown with collegial communion, conciliar authority, sacramental validity, or the confessor tension.
>
> The evidence is solidly attested for the existence and basic content of these texts. The specific passages carry the lower citation grade (B), but that is not a thin spot in the evidence.
>
> It depends on a shared vernacular to teach in: the inherited Latin theological vocabulary. It also connects to every ongoing outside pressure on the world. These are the Valerianic persecution, the plague, the Donatist schism, and the rival systems of Manichaeism and Pelagianism. This concern is the channel through which outside pressure reaches an ordinary believer. That is this world's characteristic response: crisis turned into teaching. The plague is the clearest case. It produced no new concern and no new practice, only a treatise, and that treatise came entirely through preaching and teaching.

New:

> This concern is real too, though its reach is smaller than the others'. It is the means by which this world's other central concerns are taught. It is not a force that organizes the world alone. It plainly recurs, shapes believers, and lasts through both phases. But its links to other concerns, and what it explains, are narrower.
>
> It recurs in the Sermons and Tractates on John by Augustine, in the works on catechesis, and in Cyprian's De Dominica Oratione. Pastoral office rests on it as its main work. But nothing else depends on it the way pastoral office, penitential discipline, and collegial communion do. It is the channel through which those concerns are taught and enforced.
>
> Its power to shape believers is strong and direct. That is the plain subject of the works on catechesis and the stated purpose of both bishops' preaching. It explains how formation happens more than why any one crisis came about. Both phases attest it, in both bishops' own words. It supports pastoral office, penitential discipline, and grace and human incapacity. No link has been shown with collegial communion, conciliar authority, sacramental validity, or the confessor tension.
>
> The evidence is firmly attested for the existence and basic content of these texts. The passages cited carry the lower citation grade (B). That is not a thin spot in the evidence.
>
> It depends on a shared spoken language to teach in. That is the inherited Latin theological vocabulary. It also ties to every ongoing outside pressure on the world. These are the Valerianic persecution, the plague, the Donatist schism, and the rival systems of Manichaeism and Pelagianism. This concern is the channel through which outside pressure reaches an ordinary believer. That is this world's way of answering a crisis: it turns it into teaching. The plague is the clearest case. It produced no new concern and no new practice, only a treatise. That treatise came wholly through preaching and teaching.

### lpc.gravity.sacramental-ordination-validity / description

- Before: FK 10.2, FRE 45.3
- After: FK 7.3, FRE 60.2

Old:

> Few questions mattered more to this world than whether baptism and ordination given outside the church's boundary were valid. The two bishops answer it in opposite ways.
>
> It recurs strongly: in Cyprian's letters on rebaptism, in the ruling of the Council of 256, and throughout Augustine's On Baptism, which argues it at book length. Unlike conciliar authority, it is not confined to one source. Two independent bishops treat it at length, decades apart.
>
> Other concerns in this world lean on it. Collegial communion is tested hardest here, because the two bishops reach opposite conclusions and communion still holds. The confessor tension is a closely related question about who may grant standing within the community.
>
> It shapes practice directly. Cyprian's requirement of rebaptism is a working pastoral policy. Augustine's contrary ruling decides whether Donatist clergy are received back in their own orders or ordained again. It explains the whole rupture between Stephen and Cyprian. It is the central subject of an entire treatise by Augustine. It also explains why the Donatists could appeal to Cyprian's own authority for their rebaptism doctrine.
>
> The question persists across both phases even as the answer changes. That persistence is itself evidence of how central the question is. It reinforces pastoral office, penitential discipline, collegial communion, and conciliar authority.
>
> Both positions are solidly attested, directly quoted and checked: On Baptism I.1.2, the 256 preface, and Book III, chapter 2. Neither side of this dispute runs short of evidence.
>
> The Donatist schism, an ongoing outside pressure, makes the question urgent for the institution, not just a matter of individual converts. Augustine's engagement with Cyprian's conciliar acts reopens it across the century gap. It also connects to the recurring contest over the failed member, because Cyprian reasons about both questions consistently.
>
> That last link runs one way only. Penitential discipline reinforces this concern in the first phase, since both are questions about the boundary and about return. But penitential discipline relates to grace and human incapacity differently: it is reshaped by that concern, not continued in it. So this record's own tie to the recurring contest over the failed member is its own, and it belongs to the first phase. It does not depend on the second-phase family resemblance, which runs toward grace and human incapacity instead.

New:

> Few questions mattered more to this world than whether baptism and ordination given outside the church's boundary were valid. The two bishops answer it in opposite ways.
>
> It recurs strongly. It appears in Cyprian's letters on rebaptism and in the ruling of the Council of 256. It runs through all of On Baptism by Augustine, which argues it at book length. Unlike conciliar authority, it does not rest on one source. Two bishops, each on his own, treat it at length, decades apart.
>
> Other concerns in this world lean on it. Collegial communion is tested hardest here. The two bishops reach opposite answers, and communion still holds. The confessor tension asks a close question. Who may grant standing within the community?
>
> It shapes practice directly. Cyprian's rule of rebaptism is a working pastoral policy. Augustine's opposite ruling settles whether Donatist clergy are taken back in their own orders or ordained again. It explains the whole rupture between Stephen and Cyprian. It is the central subject of an entire treatise by Augustine. It also explains why the Donatists could appeal to Cyprian's own authority for their teaching on rebaptism.
>
> The question persists across both phases even as the answer changes. That the question stays is itself evidence of how central it is. It supports pastoral office, penitential discipline, collegial communion, and conciliar authority.
>
> Both positions are solidly attested. They are quoted word for word and checked: On Baptism I.1.2, the 256 preface, and Book III, chapter 2. Neither side of this dispute is short of evidence.
>
> The Donatist schism is an ongoing outside pressure. It makes the question urgent for the church as a whole, not just for single converts. Augustine dealt with Cyprian's conciliar acts. That reopens it across the century gap. It also connects to the recurring contest over the failed member. Cyprian reasons about both questions in the same way.
>
> That last link runs one way only. Penitential discipline supports this concern in the first phase. Both are questions about the boundary and about return. But penitential discipline ties to grace and human incapacity in another way. That concern reshapes it, and does not continue in it. So this record has its own tie to the recurring contest over the failed member. That tie belongs to the first phase. It does not depend on the second-phase family resemblance. That resemblance runs the other way, toward grace and human incapacity.

### lpc.core.latin-pastoral-congregational-christianity / formation_logic

- Before: FK 8.7, FRE 56.1
- After: FK 8.0, FRE 60.1

Old:

> What a person is actually formed into here is a member of a body that can hold them through their own failure.
>
> Every way of looking at this world arrives at the same shape. There is a rite that ends in restoration, and a pastor who will not stand apart from those who failed. There is a refusal of any single decisive test, and a graded road back rather than a verdict. There is one named man answerable for these particular people. And there is a boundary that disagreement does not breach.
>
> Here the rite generates the doctrine, not the other way round. This world's two defining crises are not doctrinal disputes with consequences for worship. They are disputes about rites, argued in doctrinal terms. The rebaptism controversy is a dispute over how baptism is validly given. The lapsed controversy is a dispute over the rite that reconciles penitents.
>
> Eight recurring concerns give this world its shape. This is an early reading of them, not a final one. Four carry the most weight, and three of those four are disputes about rites. The fourth is the office that performs the rites.
>
> The first of the four is the pastoral office, understood as keeping a flock in one territory. The second is penitential discipline. The third is communion among bishops, kept whole despite disagreement. The fourth is whether sacraments and ordinations stay valid across the boundary with a rival church.
>
> Three more concerns support these. They are preaching and teaching those preparing for baptism; theories of what councils can decide; and God's grace set against human inability. One last concern pulls against the others. It is the authority the confessors claimed, set against the peace the bishop regulated.
>
> Underneath positions that otherwise have nothing in common, one move keeps recurring. This world refuses to let any single factor be decisive. Cyprian refuses to let one act under persecution settle a person's membership for good. Augustine refuses to let a minister's purity decide whether a sacrament is valid. He also refuses to let a believer's unaided will decide where they stand before God.
>
> This world's most characteristic structure is an internal rule that keeps disagreement from becoming separation. Cyprian states it while presiding over the council that will decide the sharpest question in the room. He said each bishop should give his view, judging no one and shutting no one out of communion for thinking differently. A century and a third later, Augustine argues at book length that Cyprian's ruling was wrong. He never places him outside.
>
> Penitential discipline here is a working legal system, not a devotional practice. It has an examined entry, graded severity, a defined duration, a competent authority, and a formal act of restoration. And this law exists to bring failed members back. It does not exist to order relations between sees and the state, the way the legal life of an imperial church does.
>
> Two pressures produced two new kinds of person in a single year. The Decian edict created the lapsed, and in the same administrative stroke it created the confessors' own claim to grant reconciliation. The community had to hold both kinds of person in the room at once. Penitential discipline is its response, and so is the pull between the confessors' authority and the bishop's regulated peace.
>
> The system turns crisis into teaching. Persecution produces De Lapsis and an order of penance. Plague produces De Mortalitate. The rival communion produces a book-length argument about baptism. Pelagian teaching about human nature produces thirteen works. Every outside pressure on record reaches the ordinary believer transformed. It arrives as a sermon, as teaching, or as a decision about who comes to the table.
>
> To be formed here was to be somebody's, and to discover that this was a stronger fact about you than your own failure. A named man is answerable for you. The community is answerable for what it does with you when you fail. The road back is walked where the people who watched you fall are the ones who have to receive you.
>
> This world argues ferociously: about water, about councils, about grace. But it argues inside a bond it will not break, because the bond is the thing it actually believes in.

New:

> What a person is actually formed into here is a member of a body that can hold them through their own failure.
>
> Every way of looking at this world arrives at the same shape. There is a rite that ends in restoration, and a pastor who will not stand apart from those who failed. There is a refusal of any single decisive test, and a graded road back rather than a verdict. There is one named man answerable for these specific people. And there is a boundary that disagreement does not breach.
>
> Here the rite generates the doctrine, not the other way round. This world's two defining crises are not doctrinal disputes with consequences for worship. They are disputes about rites, argued in doctrinal terms. The rebaptism controversy is a dispute over how baptism is validly given. The lapsed controversy is a dispute over the rite that reconciles penitents.
>
> Eight recurring concerns give this world its shape. This is an early reading of them, not a final one. Four carry the most weight, and three of those four are disputes about rites. The fourth is the office that performs the rites.
>
> The first of the four is the pastoral office, understood as keeping a flock in one territory. The second is penitential discipline. The third is communion among bishops, kept whole despite disagreement. The fourth is whether sacraments and ordinations stay valid across the boundary with a rival church.
>
> Three more concerns support these. They are preaching and teaching those preparing for baptism; theories of what councils can decide; and God's grace set against human inability. One last concern pulls against the others. It is the authority the confessors claimed, set against the peace the bishop regulated.
>
> Underneath positions that otherwise have nothing in common, one move keeps coming back. This world will not let any single factor be decisive. Cyprian will not let one act under persecution settle a person's membership for good. Augustine will not let a minister's purity decide whether a sacrament is valid. He also will not let a believer's unaided will decide where they stand before God.
>
> This world's most distinctive structure is an internal rule. It keeps disagreement from becoming separation. Cyprian states it while presiding over the council that will decide the sharpest question in the room. He said each bishop should give his view, judging no one and shutting no one out of communion for thinking differently. A century and a third later, Augustine argues at book length that Cyprian's ruling was wrong. He never places him outside.
>
> Penitential discipline here is a working legal system, not a devotional practice. It has an examined entry and graded severity. It has a defined duration and a competent authority. It ends in a formal act of restoration. And this law exists to bring failed members back. It does not exist to order relations between sees and the state, the way the legal life of an imperial church does.
>
> Two pressures made two new kinds of person in a single year. The Decian edict created the lapsed, and in the same official stroke it created the confessors' own claim to grant reconciliation. The community had to hold both kinds of person in the room at once. Penitential discipline is its response. So is the pull between the confessors' authority and the bishop's regulated peace.
>
> The system turns crisis into teaching. Persecution gives us De Lapsis and an order of penance. Plague gives us De Mortalitate. The rival communion gives us a book-length argument about baptism. Pelagian teaching about human nature gives us thirteen works. Every outside pressure on record reaches the ordinary believer transformed. It arrives as a sermon, as teaching, or as a decision about who comes to the table.
>
> To be formed here was to be somebody's, and to discover that this was a stronger fact about you than your own failure. A named man is answerable for you. The community is answerable for what it does with you when you fail. The road back is walked where the people who watched you fall are the ones who have to receive you.
>
> This world argues fiercely: about water, about councils, about grace. But it argues inside a bond it will not break, because the bond is the thing it actually believes in.

### lpc.core.latin-pastoral-congregational-christianity / horizon

- Before: FK 8.8, FRE 55.1
- After: FK 7.8, FRE 60.2

Old:

> The formation of ordinary Latin North African Christianity, c. 246-430 CE. Here Christianity is lived as territorial, congregational, pastoral life under a bishop's office. Two bishops hold it together. Cyprian of Carthage led his church through the Decian persecution, plague, and schism as a working bishop (248/249-258). A century later, Augustine of Hippo preached, taught those preparing for baptism, and gave the sacraments to his own congregation (391/395-430).
>
> What bounds this world is two bishops' ordinary care of an entire local flock. It is not bounded by one continuous institutional story across the century between them.
>
> This is a world of ordinary pastors and their own congregations. It is not a world of courts, or of councils called to settle jurisdiction across the empire. Nor is it a world of ascetics who withdraw from congregational life. Its way of forming people is pastoral and sacramental before it is legal.
>
> Carthage was the metropolitan see of Africa Proconsularis. Through most of this world's span it was the most populous Latin Christian city outside Rome.
>
> Hippo Regius was a substantial port city. In civil terms it is usually placed in Africa Proconsularis, but in church terms it was Numidian. So Augustine was a provincial bishop, answerable within a different provincial structure from Carthage, the primate's see. Even so, he attended the wider African councils that Carthage led.
>
> The world begins with Cyprian's conversion and his rise to be bishop of Carthage (c. 246-249). The congregation acclaimed him, over the recorded opposition of five presbyters. The world closes with Augustine's death at Hippo on 28 August 430, during the Vandal siege of the city. That siege was a real break in this world's life, of the same kind as the one that opens it. It is not merely a convenient end to one man's lifespan.
>
> The century between the two bishops (258-391) is a genuine silence in this world's own record. It is not a general lack of evidence about the period. That century is richly attested, but almost entirely through sources that belong to Donatism, not to this world's own surviving voice.
>
> The two bishops' eras form one strand, not two. They share the same emphasis in formation, the same practice, and the same orientation to the world around them. Real and substantial differences in authority do separate them. One is how far a bishop could use coercion against a rival hierarchy. Another is whether a rival consecration was sacramentally valid. A third is their theory of what councils can decide, and that one is held open rather than fully settled.
>
> But none of these differences clearly touches a bishop's ordinary authority over his own flock. That ordinary authority is what this world's recurring concerns are actually about.
>
> What makes this one world is not a record that runs unbroken across the gap. It is a fact that this world's own surviving writings let anyone check. Augustine's church describes itself as the same catholic communion that Cyprian had led. Augustine argues with Cyprian, but never against Cyprian's standing.
>
> This tradition is still living, but it has no single named heir. Its core is an ordinary bishop's territorial, sacramental, congregational care of a local flock. That is close to how most historic Christian communions understand parish or diocesan ministry, wherever they kept the office of bishop or pastor at all. It is ancestral to the Western church before that church divided. It is not a claim that belongs to one see's own line of succession.
>
> This world is not a movement with a founding break to tell. It experiences itself as the ordinary church.

New:

> The formation of ordinary Latin North African Christianity, c. 246-430 CE. Here Christianity is lived as territorial, congregational, pastoral life under a bishop's office. Two bishops hold it together. Cyprian of Carthage was a working bishop (248/249-258). He led his church through the Decian persecution, plague, and schism. A century later, Augustine of Hippo preached, taught those preparing for baptism, and gave the sacraments to his own flock (391/395-430).
>
> What bounds this world is two bishops' ordinary care of an entire local flock. No one continuous institutional story across the century between them bounds it.
>
> This is a world of ordinary pastors and their own congregations. It is not a world of courts. It is not a world of councils called to settle jurisdiction across the empire. Nor is it a world of ascetics who withdraw from life in the congregation. Its way of forming people is pastoral and sacramental before it is legal.
>
> Carthage was the metropolitan see of Africa Proconsularis. Through most of this world's span it was the most populous Latin Christian city outside Rome.
>
> Hippo Regius was a large port city. In civil terms it is usually placed in Africa Proconsularis, but in church terms it was Numidian. So Augustine was a provincial bishop. He was answerable within a different provincial structure from Carthage, the primate's see. Even so, he attended the wider African councils that Carthage led.
>
> The world begins with Cyprian's conversion and his rise to be bishop of Carthage (c. 246-249). The congregation acclaimed him, over the recorded opposition of five presbyters. The world closes with the death of Augustine at Hippo on 28 August 430, during the Vandal siege of the city. That siege was a real break in this world's life, of the same kind as the one that opens it. It is not merely a tidy end to one man's lifespan.
>
> The century between the two bishops (258-391) is a real silence in this world's own record. It is not a general lack of evidence about the period. That century is richly attested. But it is attested almost entirely through sources that belong to Donatism, not to this world's own surviving voice.
>
> The two bishops' eras form one strand, not two. They share the same emphasis in formation, the same practice, and the same stance toward the world around them. Real and large differences in authority do separate them. One is how far a bishop could use coercion against a rival hierarchy. Another is whether a rival consecration counted as a valid sacrament. A third is their theory of what councils can decide. That one is held open rather than fully settled.
>
> But none of these differences clearly touches a bishop's ordinary authority over his own flock. That ordinary authority is what this world's recurring concerns are really about.
>
> What makes this one world is not a record that runs unbroken across the gap. It is a fact that this world's own surviving writings let anyone check. The church of Augustine describes itself as the same catholic communion that Cyprian had led. Augustine argues with Cyprian, but never against Cyprian's standing.
>
> This tradition is still living, but it has no single named heir. Its core is an ordinary bishop's territorial, sacramental, congregational care of a local flock. That is close to how most historic Christian communions understand parish or diocesan ministry, wherever they kept the office of bishop or pastor at all. It is ancestral to the Western church before that church split. It is not a claim that belongs to one see's own line of succession.
>
> This world is not a movement with a founding break to tell. It knows itself as the ordinary church.
