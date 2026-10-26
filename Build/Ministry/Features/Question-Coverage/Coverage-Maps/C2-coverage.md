# C2 coverage map: God, the Trinity, the Spirit

Read-only pass, 26 October 2026; nothing in the repo was edited. Cells were judged from record front matter (retrieve_when, use_note, canon cells) and vendored lines read in context. Paths, lines and verification results are in `search/C2/C2-coverage.json`.

## The sub-questions

| id | sub-question | question ids |
|---|---|---|
| S1 | Is God real; who made God | R-01, R-02 |
| S2 | What God is like: father or judge, angry, same God as Jews and Muslims; anger at God | C2-01, 09, 11, 19 |
| S3 | The Trinity in plain words; the one-and-three objection | C2-06, 10, 12, 14 |
| S4 | The Spirit: person or force; tongues; prophecy; still speaks | C2-02, 08, 13, 21; R-25 |
| S5 | Councils, Arius, homoousios, filioque: "a council voted Jesus God" | C2-03, 04, 07, 15 |
| S6 | Can God be known, felt, found in nature, heal | C2-05, 16, 18; R-35, R-36 |
| S7 | Where evil comes from; did God create it | C2-20 |
| S8 | Pictures and images of God | C2-17 |

## Layer table

R = a record speaks to it; R* = partial (a guard, a not_for, or one facet only); L = vendored and mapped, read in context, no record; "-" = nothing. No cell reached I or O alone (those are listed below). Of 96 cells: 24 R, 44 R*, 15 L, 13 nothing.

| world | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 |
|---|---|---|---|---|---|---|---|---|
| alx | R* | R* | R* | R* | R | R | R* | R* |
| cappadocian | R* | R* | R | R | R | R | L | R* |
| desert | R* | L | R* | R | R | R | R* | R |
| don | - | - | R* | L | R | R | - | - |
| gallic | L | R* | R | R* | R* | R | R* | R* |
| hal | - | - | R* | L | R* | R* | - | L |
| ijc | - | - | R* | L | R | - | - | - |
| lpc | L | R* | R* | L | R* | R* | R* | - |
| pahc | R* | R* | R* | R | R | R* | R* | L |
| rzg | L | L | L | L | L | R* | R* | R |
| syr | R* | R* | R | R* | R | R | R | R* |
| witt | R* | R* | R* | R* | R | R* | R* | R |

lpc is still building and all its records are drafts. Time windows matter: ten worlds close by 451, so Islam and the filioque lie outside them.

## World by world

**alx.** Can say: the Word and Spirit are God's own; Nicaea fenced worship already in use and did not vote Jesus God (`alx.dw.councils`); God's severity is a physician's fire (verified). Thin: no plain Trinity answer, no "is God real", nothing on pictures, tongues or healing. Add: quote for Athanasius's Tome to the Antiochenes (`npnf204` L60054-60066, Spirit not a creature, hypostases not to be pressed); quote for De Incarnatione 3 (L16165); honest_limit for tongues. Several alx witnesses have empty retrieve_when.

**cappadocian.** Best fleet coverage on S3 to S6: ousia and hypostasis, Basil's reserve about calling the Spirit God, "a confession, not a vote", the filioque guarded in `cappadocian.core.cappadocian`. Thin: the "three gods" objection, evil, pictures, healing. Add: quote for Nazianzen Or. 31.26 (`npnf207` L34656-34673: the Spirit's Godhead revealed by stages, Pentecost tongues); quote for Nyssa On Not Three Gods (`npnf205` L29315 ff.); quote for Nyssa Cat. Or. V-VI (L43116-43124, "no evil other than wickedness"); honest_limit that Basil's "honour to the image" concerns the Son.

**desert.** Can say: God seen through stilled passions or felt (two currents, kept apart); Antony refused the Arians; the monk who wept for his human-shaped God (verified). Thin: God's character (Cassian X.4, `npnf211` L22581, anger ascribed to God is figurative), origin of evil. Add: quote for Vita Antonii 22 (`npnf204` L31789-31792, "God made nothing evil"); quote for Cassian X.4. Antony's Letters are unvendored.

**don.** Can say: same Trinitarian faith as the rivals; no creed survives; councils governed discipline; God felt in martyr visions. Thin: S1, S2, S7, S8 empty. Add: quote for Parmenian's "third Endowment, the Spirit, in the water" (`optatus_against-the-donatists.txt` L1397, read in editor's context); honest_limit on God's nature and evil.

**gallic.** Can say: one substance, three Persons (Vincent, verified); God judges now (Salvian); healing and prophecy as lost-and-repaired grace. Thin: no Spirit-as-person, no Arius. Add: quote for Salvian L5236 ("deny his very existence"); register Cassian's Incarnation as vendored (`npnf211` L48467); quote for Cassian X.4.

**hal.** Trinity "never negotiable" and the "wrong witness for the council hall" are rendered, but `hal.dw.authority` retrieves only on "who appointed bishops". Add: retrieve_when for the council-vote question; quote for Ep. XV to Damasus on three hypostases (`npnf206` L5002 ff.; written c.376, before the 382 window); honest_limit on evil and God's character; Ep. XLI on Montanism (L8270); Epiphanius and the painted curtain (L11100).

**ijc.** Richest on councils (Eusebius's hesitation, Homoian side, Chalcedon). Empty on God, Spirit, evil. Add: quote for the 381 creed (`npnf214` L13393) and Ambrose on the Spirit "from the Father and the Son" (`npnf210` L12068-12070); that is the only in-window filioque text.

**lpc.** Draft records on Trinity, councils, Manichaeans and "restless heart". Add (when the world is built): Confessions VII "Whence is evil?" (`npnf101` L10384); Augustine on Psalm 14 (`npnf108` L2608); the Maximinus debate.

**pahc.** Honest guard: no gathering decided God's nature; the only fights were leadership and Christ's flesh. Only world with prophecy testing and Montanism. Add: Tatian "He alone is without beginning" (`anf02` L5833-5836); Theophilus, "types of the Trinity" (L8992-8999); Justin Dial. 82 (`anf01` L22231) and Irenaeus V.6.1 "speak all kinds of languages" (L51060); Tertullian On Idolatry (`anf03` L4962).

**rzg.** Nothing on God, Trinity, Spirit, evil or councils, though the sources are vendored. Add: quote for SHC ch.3 (L458-472, Trinity, filioque, and a line condemning "the Jews and Mohammedans" that needs a not_for); SHC ch.4 on images (L479); Calvin Inst. I.13.5 (`calvin_...vol1` L11242); SHC ch.7 on evil (L534). Images are the one cell where the world is rendered (refusal), but no record states the doctrine.

**syr.** Strongest on evil: free will against Marcion, Bardaisan and Mani, and Ephrem's argument that evil has no existence of its own (verified). The Trinity is answered from the font. Thin: tongues, pictures, "is God real". Add: Tatian (`anf02` L5835); Ephrem on fire and the Spirit at baptism (`npnf213` L20580).

**witt.** Christ truly God, the devil, sin, images, Scripture over councils, "a confession, not a vote" are rendered. Missing though vendored: AC I (Nicaea's decree on the Three Persons, `melanchthon_augsburg...` L168-177); Small Catechism first and third articles (L171, L209-219); Large Catechism "how angry God is ... how good and gracious" (L584); AC XIX "Of the Cause of Sin" (L483-489).

## Fleet-wide thin spots

1. S1: no world answers "is God real"; only cappadocian answers "who made God" (no beginning). Tatian L5835 serves pahc and syr.
2. Muslims: no world before 451 can speak; no record says so. Only witt (`term.the-turk`) and rzg (SHC L472, a hazard) touch it.
3. S3 plain-words Trinity: only cappadocian, gallic, syr.
4. Tongues and prophecy: pahc only; healing by God: gallic, desert, syr in part.
5. S7 and S8: evil answered directly by syr alone; images by desert, rzg, witt.
6. Filioque: guarded only in cappadocian's core.

## Identified, not vendored

`cappadocian.source.basil-against-eunomius`, `...gregory-nyssa-on-the-deity-of-the-son-and-spirit`, `...eunomius-apology-for-the-apology`, `...epiphanius-on-eustathius-pneumatomachians` (WANTS-REGISTER L54, 98, 112-116); Nazianzen's Five Theological Orations (download-queue-seed, not downloaded); `desert.source.antony-letters` (L70); `witt.source.marburg-articles` (L189), Luther's Jews tracts; `ijc.source.auxentius-letter-ulfila`. Stale: `gallic.source.cassian-de-incarnatione` says unvendored but the text is vendored and mapped (L48467).

## Other sources (not fetched; from working knowledge)

Basil, Against Eunomius (PG 29, Greek PD); Antony's Letters (PG 40 Latin); Didymus, De Spiritu Sancto (PG 39) and Athanasius, Letters to Serapion (PG 26:529-676, not found in the vendored PG 26 by grep); Marburg Articles (WA 30/3); Luther 1523 on Christ born a Jew and Bibliander 1543; Zwingli, Exposition of the Faith (Latin Works vol. 2, Hinke 1922); Bullinger, Decades (Parker Society); Odes of Solomon (Harris and Mingana); Augustine, Collatio cum Maximino (PL 42). Editions and licences are in the JSON.

## Verification

51 quote records are cited as RENDERED; all 51 MATCH their vendored file (file and line in the JSON). Four needed hand checks because the tool failed them: Nyssa Cat. Or. 25 (an editorial footnote marker [2002] sits inside the sentence), Macarian Homily IV (the tool strips "<...>" spans from a .txt file), Ephrem's Freewill argument (an inline page marker), and the Second Helvetic Confession mirror line (OCR "onr" for "our"). None is a wording change.

## Not checked

- `canon/sealed_probes/` was not read.
- The tool scans whole mapped files, so shared volumes give hits for the wrong work (Cyril in npnf207, John of Damascus in npnf209, Lactantius On the Anger of God in anf07 is mapped to latin-apologists, not to any of the twelve).
- Non-English vendored files (Faustus of Riez, PG 26, Zwingli Latin) were counted, not read.
- Whether records with empty retrieve_when (many alx, syr, cappadocian witnesses) are reached by canon-cell routing.
- Readability of spoken fields; whether lpc drafts are in a compiled package; the seven record-less worlds (aec, hus, jes, meth, obel, rcg, wsyr).
- Optatus L1397 and the numbered chapter citations (Cassian X.4, Vita 22, De Incarnatione 3) were located by text, not cross-checked against a section index.
