# Wants-sort handoff: the unclassified wanted sources, by world

Written 2026-10-27 for whoever next builds one of these worlds. `Build/worlds/_cross-world/WANTS-REGISTER.md` is the live list and regenerates from the world records; this note carries the instructions and a dated snapshot.

As of 2026-10-27, 58 wanted sources have edition wording that `Build/worlds/_cross-world/gen_wants_register.py` cannot classify: Wittenberg 30, Cappadocian 18, Reformed 5, Donatism 4, Gallic 1.

## What the thread does

The generator reads each source record's own `edition` and `rights_status` wording and never guesses. A row leaves the unclassified list when the record says what the source needs. Rule each row into one of these, and say so in the record's wording:

- **Acquirable, public domain:** a public-domain edition exists and was never obtained.
- **Purchasable (in copyright):** in copyright and buyable; say "in-copyright".
- **No edition exists:** no usable English translation is known.
- **Resolved:** a vendored text already holds it; name that source.
- **Nothing to acquire:** a web page, a project file or a general pattern, with no text to hold rights over.

Rows with a nonzero **Records** count matter first: that many world records rest on the source.

## Wittenberg and the Lutheran reformation (`witt`): 30

Twelve rows are modern books or articles with a publisher and year in the edition field, and two more are an essay and a multi-author history. Ten are Reformation primary texts. Five are online or project pages with nothing to acquire: Wikipedia, Britannica, GAMEO, the Wittenberg museums and the census file. The Philadelphia Edition row (volumes IV to VI) is out of date: volumes IV and VI are now vendored and volume V follows on 1 January 2027.

| Source record | Records | What the edition field says |
| --- | --- | --- |
| `witt.source.erwin-theses-were-not-posted-luther-between` | 1 | (Boston: Beacon, 1968; German Luthers Thesenanschlag — Tatsache oder Legende?, 1962; first argued 1961) |
| `witt.source.gerald-luthers-house-of-learning-indoctrination` | 1 | (Baltimore: Johns Hopkins, 1978) |
| `witt.source.james-successes-and-failures-in-the-german` | 1 | Archiv für Reformationsgeschichte 73 (1982), pp. 153–175 — from prior knowledge |
| `witt.source.johannes-reception-of-luthers-writings` | 1 | Lutheran Quarterly n.s. 1, no. 1 (Spring 1987), pp. 72–97 |
| `witt.source.saxon-visitation-protocols` | 1 | (1527–28 ff.) and the church ordinances in Emil Sehling (ed.), Die evangelischen Kirchenordnungen des XVI.... |
| `witt.source.scribner-for-the-sake-of-simple-folk` | 1 | (Cambridge, 1981; Clarendon pbk.) |
| `witt.source.susan-reformation-of-ritual-an-interpretation` | 1 | (London: Routledge, 1997) |
| `witt.source.thomas-luthers-jews-a-journey-into-anti` | 1 | trans. Sharpe & Noakes (Oxford, 2017; German 2014) |
| `witt.source.wikipedia-on-the-jews-and-their-lies` | 1 | and "Against the Murderous, Thieving Hordes of Peasants" — tertiary, used only as G1 Part B itself suggested... |
| `witt.source.alejandro-andreas-bodenstein-von-karlstadt-1486-1541` | 0 | biographical essay for the Kritische Gesamtausgabe der Schriften und Briefe Andreas Bodensteins von Karlstadt... |
| `witt.source.cambridge-history-of-christianity` | 0 | vol. 6, ch. 1 "Martin Luther, reformer" (Hendrix), ch. 2 (Brady), ch. 4 (Lehmann) |
| `witt.source.church-cic-website-data-world-census-json` | 0 | entry VI.1 (lutheran-wittenberg-and-its-congregations) and the sibling entries VI.2, VI.3, VI.11, VI.22 |
| `witt.source.encyclopaedia-britannica` | 0 | (online), "Andreas Karlstadt" — tertiary |
| `witt.source.global-anabaptist-mennonite-encyclopedia-online` | 0 | (GAMEO), "Karlstadt, Andreas Rudolff-Bodenstein von (1486–1541)" — tertiary, from the Anabaptist tradition's... |
| `witt.source.heiko-luther-man-between-god` | 0 | (1989; German 1982) |
| `witt.source.johann-eyewitness-report-of-luthers-first-invocavit` | 0 | (9 March 1522) — as cited in Steimle's introduction to R15; not independently vendored, embedded within... |
| `witt.source.karsthans` | 0 | (anonymous popular dialogue, 1521; ed. Burckhardt in Clemen, Flugschriften, IV.1) — as quoted in Lambert's... |
| `witt.source.luther-admonition-to-peace` | 0 | (April 1525); Against the Murderous, Thieving Hordes of Peasants (May 1525); An Open Letter on the Harsh Book... |
| `witt.source.luther-das-newe-testament-deutzsch` | 0 | (September 1522) and the German Bible (1534) — NOT VENDORED |
| `witt.source.luther-de-votis-monasticis` | 0 | / Treatise on Monastic Vows (1521) — Philadelphia Ed. vol. IV — NOT VENDORED; embedded within... |
| `witt.source.luther-formula-missae` | 0 | (1523) and Deutsche Messe und Ordnung des Gottesdiensts (1526) as service orders — NOT VENDORED (only the... |
| `witt.source.luther-that-jesus-christ-was-born` | 0 | (1523) — Luther's Works vol. 45 (from prior knowledge) — NOT VENDORED |
| `witt.source.luther-von-den-juden-und-ihren-l` | 0 | (1543) — Luther's Works vol. 47 (Fortress, 1971; trans. Martin H. Bertram, in vol. 47 ed. Franklin Sherman —... |
| `witt.source.lutherstadt-wittenberg-luthers-house-and-melanchthons` | 0 | (Luther museums; UNESCO World Heritage), per the census experienceToday field |
| `witt.source.lyndal-martin-luther-renegade-and-prophet` | 0 | (2016) |
| `witt.source.martin-martin-luther` | 0 | 3 vols., trans. James L. Schaaf (Minneapolis: Fortress, 1985, 1990, 1993) |
| `witt.source.melanchthon-deuttung-der-zwo-grewlichen-figuren-bapstesels` | 0 | (1523; Wittenberg and reprints, e.g. Nuremberg: Stuchs), with Cranach-workshop woodcuts of the Papal Ass... |
| `witt.source.peter-revolution-of-1525-the-german-peasants` | 0 | trans. Brady & Midelfort (Baltimore: Johns Hopkins, 1981) |
| `witt.source.philadelphia-edition-vols-iv` | 0 | (1931), V (1931), VI (1932) — archive.org identifiers per G1 Part B — HELD BACK pending copyright-renewal... |
| `witt.source.scott-martin-luther-visionary-reformer` | 0 | (New Haven: Yale, 2015) |

## Cappadocian fathers (`cappadocian`): 18

Six Gregory of Nyssa texts are recorded as absent from the vendored NPNF 5. Four Gregory of Nazianzus rows are open; two of them, the Mamas homily and De vita sua, name the vendored NPNF 7 volume in the edition field while the rights field says the text is not yet acquired, so those records may be out of date.

| Source record | Records | What the edition field says |
| --- | --- | --- |
| `cappadocian.source.basil-moral-famine-homilies` | 8 | No open edition of the whole homilies acquired -- no open-license English translation of them is held in this... |
| `cappadocian.source.gregory-nyssa-forty-martyrs-theodore-recruit-homilies` | 5 | Confirmed absent from the vendored npnf205 per row 41's own note -- a named, currently unlocated acquisition... |
| `cappadocian.source.amphilochius-of-iconium-own-works` | 3 | No open English edition of his works as a corpus has been located. One short extract of his own argument --... |
| `cappadocian.source.gregory-nazianzus-oration-14-love-of-poor` | 3 | NOT within the vendored npnf207 edition -- only a single mention inside the Prolegomena's own catalogue of... |
| `cappadocian.source.gregory-nyssa-in-xl-martyres-ii` | 3 | Confirmed absent from the vendored npnf205 -- independently confirmed by a direct text search of the vendored... |
| `cappadocian.source.gregory-nyssa-life-of-gregory-thaumaturgus` | 3 | Not in the vendored npnf205, which only refers to it (lines 1246 and 21346). The seventeen-to-seventeen claim... |
| `cappadocian.source.epiphanius-on-eustathius-pneumatomachians` | 2 | Not independently located as a vendored text this session; a named author, no specific work title given |
| `cappadocian.source.gregory-nazianzus-on-the-mamas-festival` | 2 | Nicene and Post-Nicene Fathers, 2nd series, vol. 7 (Cyril of Jerusalem, Gregory Nazianzen), ed. Schaff (the... |
| `cappadocian.source.gregory-nyssa-song-of-songs-ecclesiastes-beatitudes-homilies` | 2 | Confirmed absent from the vendored npnf205 per row 41's own note (the G1 manifest audit specifically flagged... |
| `cappadocian.source.martyrium-shrine-panegyris-pattern` | 2 | Attested collectively via the homilies naming festival crowds (rows 16, 20, 53, and 115); no independent... |
| `cappadocian.source.nicaea-325-subscription-lists` | 2 | No open edition of the subscription lists themselves located; attested via secondary literature rather than... |
| `cappadocian.source.basil-small-asketikon` | 1 | Named witnesses only (Rufinus' 397 Latin translation; a dated Syriac manuscript tradition) -- no open English... |
| `cappadocian.source.eunomius-confession-of-383` | 1 | Not independently located as a vendored text this session; named for completeness per Doc_02 SS1.5/Doc_01... |
| `cappadocian.source.gregory-nazianzus-de-vita-sua` | 1 | Nicene and Post-Nicene Fathers, 2nd series, vol. 7 (Cyril of Jerusalem, Gregory Nazianzen), ed. Schaff... |
| `cappadocian.source.gregory-nazianzus-will-manumission` | 1 | Cited at work level per Doc_02 SS1.2/SS6.3; no specific vendored edition independently matched this session |
| `cappadocian.source.gregory-nyssa-on-the-deity-of-the-son-and-spirit` | 1 | Not in the Library. The Library's copy of Nicene and Post-Nicene Fathers, 2nd series, vol. 5 (npnf205) does... |
| `cappadocian.source.gregory-nyssa-ad-graecos` | 0 | Confirmed absent from the vendored npnf205 per row 41's own note; Doc_02 SS1.3's own correction states... |
| `cappadocian.source.liturgy-of-st-basil` | 0 | No vendored or independently locatable edition this session |

## Reformed Zurich and Geneva (`rzg`): 5

All five say "not yet acquired", and no record depends on any of them yet. The Consistory registers carry a 2000 Eerdmans imprint.

| Source record | Records | What the edition field says |
| --- | --- | --- |
| `rzg.source.beza-works` | 0 | No specific edition identified or searched this pass - NOT YET ACQUIRED |
| `rzg.source.dentiere-works` | 0 | No edition identified or searched this pass - NOT YET ACQUIRED |
| `rzg.source.ecclesiastical-ordinances-1541` | 0 | No verified public-domain English edition located this pass - NOT YET ACQUIRED |
| `rzg.source.geneva-consistory-registers` | 0 | Grand Rapids: Eerdmans, 2000 - NOT YET ACQUIRED |
| `rzg.source.genevan-psalter` | 0 | No edition searched or identified this pass - NOT YET ACQUIRED |

## Donatism (`don`): 4

The Lucilla row names two vendored files in its edition field. The Gregory the Great register is vendored only as a selection; the complete 1891 edition is not.

| Source record | Records | What the edition field says |
| --- | --- | --- |
| `don.source.acta-saturnini-abitinian-martyrs` | 4 | No edition is named. Not vendored; no specific printing, translation, or manuscript basis is identified... |
| `don.source.numidian-basilica-archaeology` | 3 | No edition. No specific site report, excavation record, or publication is named anywhere in... |
| `don.source.lucilla-and-second-woman-maximianist` | 2 | optatus_against-the-donatists.txt (row 1's file) and npnf101_augustine-confessions-letters.xml (row 6's file) |
| `don.source.gregory-great-register-of-letters` | 0 | the complete Ewald-Hartmann critical edition (Registrum Epistolarum, Berlin, 1891) remains unvendored; a... |

## Gallic monasticism (`gallic`): 1

The Cassian row says the edition is not confirmed.

| Source record | Records | What the edition field says |
| --- | --- | --- |
| `gallic.source.cassian-de-incarnatione` | 2 | Corpus-map assigned; specific vendored file/edition not independently confirmed by this authoring pass (see... |
