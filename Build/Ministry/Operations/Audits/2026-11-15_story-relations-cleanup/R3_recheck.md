# Round 3 targeted recheck (cap round): story cards, "How it connects" (2026-11-15)

Items checked: 22 (17 changed lines, the Scillitan `text`, 4 decisions not taken as worded). BLOCKING: 1. MINOR: 7.

Method: one fresh Opus reviewer at full effort, who had not seen the drafting or rounds 1 and 2. Only what changed in round 2 was checked. All 17 "After" lines in R2_changes.md match the `relationsSummary` now in `DATA.stories` (cft-website/index.html, commit b6992635), and no sentence runs past 25 words. Each fact was checked against the story's own `text`/`caveat` and against the census entries it names, one movement at a time.

### silesian-childrens-prayer-revival
PASS. The causal claim is gone. The story: the 1707 Convention of Altranstädt led to six "Churches of Grace — among them the Jesus Church at Teschen". The revival began in the winter of 1707-08, so "won in the same year" holds.

### perpetua-and-felicity
PASS. "The editor who put their story together" matches the story's "An anonymous editor combined Perpetua's diary with a vision ... and an eyewitness account". Census Latin Pastoral: c. 240s-430, Carthage.

### abercius-epitaph
- Round 2 finding resolved: 'the same faith everywhere' and "bishop's" are gone, and "the Prophecy" is spelled out.
- BLOCKING (quote fidelity): the line still puts 'the same faith' in quotation marks as the epitaph's words ("The epitaph says ... he found 'the same faith'"). No vendored text of the epitaph exists in cic/texts (searched: only Harnack's German discussion and ANF vol. 7 footnotes on Abercius Marcellus). The story's own source note says the stone was "consulted only through museum and reference summaries". The stone's Greek has "Πίστις πάντη δὲ προῆγε" ("Faith everywhere led the way"), with no "the same". So the quotation cannot be verified verbatim, and the standard rendering differs. Under CLAUDE.md a quote that cannot be re-verified does not pass. The paraphrase itself is fair, so the fix is to drop the quotation marks.
- Proposed (second sentence): "The epitaph says that everywhere he went, he found the same faith."
- Outside this job, for Open-Gaps: the story's `text` ("everywhere he found 'the same faith'") and `teaser` ("found 'the same faith everywhere'") carry the same unverified quotation. The teaser's form is the one round 2 found in no source.

### abitinian-martyrs
PASS. "Reportedly" matches the story ("had reportedly cut off communion") and the caveat (the break comes "through partisan editing"). The split reads cleanly.

### moses-the-ethiopian
- Round 2 finding resolved: "abba" is explained, and "widens the picture" is gone. The census Desert supports the gloss: "a younger monk asked an elder for 'a word,' and the elder answered in one sentence". The story supports "enslaved", "a robber" (leader of "a robber band") and "a disciple of Macarius".
- MINOR (writing): "an honored elder other monks came to for a word" stacks a relative clause without "whom" and ends on "for a word", an emic phrase a B2 reader may not catch.
- Proposed (last sentence): "Once enslaved and later a robber, he became an abba there: an honored elder whom younger monks asked for a word of guidance."

### olympias-the-deaconess
PASS. "An ordained deaconess" matches the story ("ordained deaconess by Archbishop Nectarius"). "Closest" comes from the old line and is supported by the seventeen letters, "the longest he wrote to anyone". Census Antioch is "Chrysostom-centered".

### severinus-of-noricum
PASS. Census Danube Provinces: Victorinus "wrote the first Latin biblical commentaries around the year 300". Its region includes Noricum and Poetovio.

### masona-of-merida
PASS. The story: "Reccared's conversion in 587–589 brought him back". Census Visigothic Iberia: Reccared "at the third council of Toledo in 589 brought his bishops with him into the Nicene church of his subjects". The order of events is now right.

### john-the-almsgiver
- Round 2 finding resolved: the 614 event is no longer placed inside a tradition that ends c. 450, and Heraclius is no longer made part of a window that opens after he appointed John.
- MINOR (writing): "after 614" leaves the reader to guess what happened in 614. "The emperor who opens the Byzantine imperial church of 622-843" reads as a map label with dates, and an emperor does not "open" a church. The census Byzantine Church II (622-843) starts its account with Heraclius, so the link holds.
- Proposed (last two sentences): "The Jerusalem he relieved after it fell to the Persians in 614 was the city of the Jerusalem pilgrimage tradition, two centuries on. He was appointed by Heraclius, the emperor whose reign opens the Byzantine imperial church's next era, from 622 to 843."

### montesinos-advent-sermon
PASS. "First" is gone. "The long argument" makes no priority claim, and the story's Laws of Burgos and Las Casas show it ran on.

### little-gidding
PASS. The story: "George Herbert sent Ferrar the manuscript of The Temple from his deathbed in 1633" and "'The Arminian Nunnery'", capital T. "His poems" fairly names The Temple.

### hungarian-galley-pastors
PASS. "Were heirs of" no longer puts 1676 inside the census Dutch Reformation (c. 1570-1650). The story names the States General and de Ruyter.

### salzburg-emigrants
- Round 2 finding resolved: "one border east" is gone. Silesia (Sprottau, Teschen) does lie east of the Pongau.
- MINOR (misleading by implication): "farther east in the Habsburg lands" implies that Salzburg was a Habsburg land too. It was not. The Archbishopric of Salzburg was its own prince-archbishop's state; the story's "Catholic prince" is Archbishop Firmian. Silesia was Habsburg.
- Proposed (last sentence): "It too tells of a hidden Protestant people under a Catholic prince, twenty-five years earlier and farther east, in Habsburg Silesia."

### sam-sharpe-baptist-war
PASS. The ambiguous "which" is gone. Census Baptists: in 1792 Carey "persuaded a small association of ministers to found a missionary society".

### franz-jagerstatter
PASS. The nested sentence is split cleanly. Census Pius X to Council: "the record of Pius XII, which has a historiography of its own and was argued about for decades afterward". The story names Bishop Josef Fliesser.

### ludmila-javorova
PASS. "Belong to" fixes the equation. The census Persecuted Church covers Baptist ministers in the Soviet Union and Romania's Lord's Army, founded by a priest.

### nickel-mines-forgiveness
- Round 2 finding resolved: the ampersand is gone.
- MINOR (writing): with "Their" meaning the Amish, "Their later history belongs with the Mennonites and the Amish" now says the Amish story belongs with the Amish. The census Mennonites and the Amish: "After 1650 the heirs of the Anabaptists became settled churches."
- Proposed (last sentence): "Their later history is told with the Mennonites, among the heirs of the Anabaptists who became settled churches after 1650."

### Scillitan `text` (cic/texts/anf09_gospel-of-peter-diatessaron-origen-commentaries.xml, l.19787-19816)
PASS. Both quotations are verbatim against the vendored ANF once the markup and the double space after the colon are removed. "Donata said: Honour to Cæsar as Cæsar: but fear to God." (l.19801-19802) and "Speratus said: Books and epistles of Paul, a just man." (l.19815-19816). The paraphrase "he does not recognize the empire of this world" fairly renders "The empire of this world I know not". "Their chest" fits "the things in your chest". "Donata adds" is fair, though Cittinus speaks between Speratus and Donata. The audio gap is noted under the decisions below.

### Decisions on points not taken as worded
- walatta-petros: the outcome is acceptable, since the line is true. But the reason given (length, and "its worldwide mission") does not answer round 2's actual point, which was circular naming: "The Jesuits ... belong to the Society of Jesus" maps a short name onto a full one. MINOR. Proposed (last sentence), with nothing new added: "The Jesuit missionaries who won the emperor over are part of the story of the Society of Jesus."
- candida-xu: the reason is partly wrong. The detail is not new to the card: the story says she was "Educated by Jesuits in her grandfather's household". Leaving it out is still sound, because it is a fact and not a connection. The circular naming that round 2 raised is not answered. MINOR. Proposed (last sentence): "The Jesuits she supported are part of the story of the Society of Jesus."
- juliana-and-corpus-christi: sound. The corrected reason matches the census Beguines.
- `relatedIds` follow-up, and the Scillitan audio gap: sound as decisions. But neither is in Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md at HEAD (b6992635). R2_changes.md says both are "registered". MINOR (record): both entries must land in Open-Gaps.md in the release commit, together with the Abercius `text`/`teaser` quotation noted above.
