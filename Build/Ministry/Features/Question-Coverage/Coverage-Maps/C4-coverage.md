# C4 coverage map: Salvation, grace, works, and "am I saved"

Read-only survey, 2026-10-25. Twelve worlds with records (fixture excluded). Method: `coverage_search.py --regex --whole-words` once per sub-question (runs `S1`–`S8` in this folder), every surfaced record read in front matter (`fm-*.txt`), 30 quote records re-verified against the vendored files (`verify-fast-out.txt`). Machine-readable detail, with file paths and line numbers, is in `C4-coverage.json`.

## Sub-questions

| id | question | items |
|---|---|---|
| S1 | Faith and works, grace, "what must I do" | C4-01, 11, 13, 14, 16, 20, 23, 24 |
| S2 | Original sin, inherited guilt, infants | C4-02 (and C3-15/16) |
| S3 | Free will, predestination, election, Romans 9 | C4-03, 09, 10, 17, 21 |
| S4 | Assurance, losing salvation, falling and returning | C4-07, 15, 19 |
| S5 | Baptism as new birth, is it needed, once-only repentance | C4-04, 05, 06, 12, 26 |
| S6 | Those who never heard; good without God | C4-08, 22, R-05 |
| S7 | Indulgences, almsgiving, paying for sin | C4-18 |
| S8 | The sin that cannot be forgiven | C4-25 |

## Layer table

R-q = rendered quote, R-w = rendered witness/term/story/demo, R-l = honest_limit already says "we cannot answer", L = loaded (vendored and mapped, no record), L- = loaded but thin, hostile or an outsider's voice, – = nothing (honest_limit to build).

| world | S1 faith/works | S2 orig. sin | S3 free will | S4 assurance | S5 baptism/penance | S6 never heard | S7 paying | S8 unforgivable |
|---|---|---|---|---|---|---|---|---|
| alx | L | R-w | R-w | R-w | R-w | L | L- | L- |
| cappadocian | R-w | R-w | L | L- | R-q | L- | R-w (thin) | L |
| desert | R-q | R-l | R-q | R-w (thin) | R-w | R-l | L- | L- |
| don | R-l | R-l | – | R-w | R-w | – | – | L- (hostile) |
| gallic | R-q | L- (context) | R-q | R-w | R-q | L- | R-w | L- |
| hal | R-w | R-w | R-w (thin) | R-w | R-w | L- | L | L |
| ijc | R-l | R-w | – | L | R-w | – | R-w (thin) | L |
| lpc | R-q | R-w | R-q | L | R-q | L | R-w | R-q (mis-indexed) |
| pahc | L | – | L | R-w | R-w | R-q | L | R-w (thin) |
| rzg | L | R-w | R-q | R-l | L | L- | L | L |
| syr | R-q | R-w | L | L- | R-q | – | R-w (thin) | L- |
| witt | R-q | R-q | R-w | R-w | R-q | L- | R-w | L |

Canon check: F1-T demonstrations exist only in gallic, ijc (bread and cup) and witt; F4-T only in don and hal. The cells are not forced per world in `records/`.

## World by world

**alx (Alexandria).** The voice can say: a real inherited wound and death, no guilt at birth (`alx.dw.original-sin`); the soul's real self-determination (`alx.term.autexousia`); the lapsed restored even at the deathbed (`alx.dw.church-failure`, `alx.term.lapsi`, `alx.story.john-young-robber`). Thin: faith versus works (no record; the framing is later), the once-only repentance (no quote), the unevangelised. Add: an honest_limit on "faith alone"; quote records from Clement, *Who is the Rich Man* (anf02 L56126: the literal "what must I do to be saved", and 39–42 on the one repentance); Origen *De Principiis* III.1 on free will and the potter (anf04 L27830, L28834); Clement *Stromateis* I.5 and VI.6 (philosophy as covenant; gospel preached to righteous Gentiles, anf02 L46951). Alexandria holds the most distinctive patristic answer to "people who never heard", and none of it is rendered.

**cappadocian.** Already honest on the frame: `dw.not-later-formulas` says inherited guilt and faith alone were not its categories and salvation is theosis. Baptism as new birth, deliberate delay, graded penance: three verified Basil quotes. Thin: free will (no record, though Basil and Gregory's own *Philocalia* is vendored), assurance, the unforgivable sin. Unrendered gold: Gregory Nazianzen Or. 40.23, infants dying unbaptised "neither glorified nor punished" (npnf207 L38494), and Gregory of Nyssa *On Infants' Early Deaths*, whole (npnf205 L32849): these two are the best texts in the Library for C3-15/16. Basil's Shorter Rules: no sin is beyond forgiveness, "despair can never be justified" (basil_ascetic-works L3990).

**desert.** Faith and works is the one systematic thing the world says, and the records say plainly that it is Cassian's Latin written in Gaul and later condemned (all Contested, three verified quotes). Original sin, the Eucharist and outsiders' condemnation already carry honest_limits. "Born again" rests on one Galatian (`dw.born-again`, Contested). Add: Conference XX, Pinufius on the end of penitence (npnf211 L43946), the answer to "I keep falling into the same sin"; the Macarian homilies' felt assurance is the nearest patristic material to C4-19 and is flagged Messalian in the records.

**don.** The best-built refusal in the fleet: `don.limit.questions-we-never-argued` ("we wrote none on faith set against works"), with the rebaptism witness and the F4-T demo. Predestination, the unevangelised and indulgences have no record and no Donatist text: extend the limit to name them. The only "sin against the Holy Ghost" in the corpus is Optatus using it against the Donatist rite (optatus L3589): hostile, not the voice.

**gallic.** The richest C4 world: fourteen records on grace and effort, twelve quotes verified, both one-sided readings refused in Cassian's own words, "predestination" named as an outsider's word, perseverance "a gift that can still be lost". Thin: infants and inherited guilt (the brethren never argued them; Augustine's side is vendored as context), the unevangelised, Conference XX for C4-26. Identified, not vendored: Prosper *Contra Collatorem*, *Pro Augustino Responsiones*, *Carmen de ingratis*; Augustine Epp. 225–226 (omitted by NPNF). Two records carry the same Conf. XIII.7 sentence.

**hal.** `hal.dw.sin-grace` holds grace and works together and says the inherited-guilt machinery was unfinished in Jerome's lifetime: honest. Falling and returning is covered by Jerome's Cicero dream and Fabiola's public penance. Nothing is quoted from *Against the Pelagians* (npnf206 L42432) or Letter 133, both vendored. Letter 42 to Marcella (npnf206 L8389) is a whole vendored letter on the sin against the Holy Ghost: unrendered. Pelagius's *Letter to Demetrias* is vendored in Latin but mapped only to the unbuilt pelagianism world; hal, lpc and gallic build the controversy from the opponents' side only.

**ijc.** `ijc.limit.later-questions` refuses the faith-alone frame; Leo gives "transmission of original sin" in the world's own words. Nothing on free will or election (every "election" hit is a bishop's), nothing on the unevangelised. Unrendered and head-on: Ambrose, *Two Books Concerning Repentance* against the Novatians (npnf210 L33355), the direct answer to "only one chance after baptism?"; Nicaea canons 11–14 on the lapsed and the viaticum (npnf214); Ambrose on the sin against the Spirit (npnf210 L10428, L34155); Leo's sermons on the collections (npnf212 L13503).

**lpc.** Strong: grace (`term.grace`, three verified Augustine sermon quotes), the lapsed and the road back (seven records, three verified quotes), redemptive almsgiving (`witness.almsgiving-quenches-sin`). Already rendered but unreachable: `lpc.quote.pardon-through-a-wicked-clergyman` is Sermon 71 on Matt 12:32, indexed only for the wicked-minister question. Unrendered and vendored: *On Rebuke and Grace* 40, "No One is Certain and Secure of His Own Predestination and Salvation" (npnf105 L20590), the sharpest patristic answer to "did anyone know they were saved?"; *On the Merits and Forgiveness of Sins and Infant Baptism*; Letter 102 q. 2, why Christ came so late (npnf101 L41687); Enchiridion 69–70 and 83. *De fide et operibus* (James 2 head-on) is vendored in Latin only.

**pahc.** The STARTER question (C4-06) is this world's own, and `pahc.story.hermas-visions` carries it as a witness; the Hermas sentence "there is but one repentance to the servants of God" (anf02 L1933) and Tertullian *On Repentance* 7–9 (anf03 L55926) are vendored and unquoted. Justin's "those who lived reasonably are Christians" is rendered twice (two records, one sentence). Nothing on faith and works (1 Clement 32–34 would carry it), nothing on infants (the silence is the finding), free will only in the Library (Justin 1 Apol. 43, anf01 L17001).

**rzg.** The predestination and assurance cluster is the best-built in the fleet (gravity, term, verified quote, the SITE demo, and an honest_limit that the doctrine of comfort is attested and the feeling is not). The hole: no record at all on justification by faith, the world's own centre, with Institutes III.11 (calvin vol2 L13893), Second Helvetic XV–XVI and Heidelberg 60–64 vendored; no "born again" record although regeneration is a distinct Reformed doctrine; nothing on indulgences or the unforgivable sin though Institutes III.5 and Zwingli's section "The Sin Against the Holy Ghost" (zwingli vol3 L7958) are vendored. Calvin's *De aeterna praedestinatione* is vendored in Latin (calvin_opera vol8 L170).

**syr.** Faith as the foundation stone with the works as the house (verified quote, `dw.adam-grace`); death from Adam as wound not guilt; Demonstration VII on penitents as medicine (verified quote, two witnesses). Ephrem's defence of free will against fate (ephraim_prose-refutations L232–295) is vendored and unrendered. Nothing on the unevangelised or the unforgivable sin.

**witt.** The fullest C4 world by record count: justification, faith, works, merit, grace, assurance, indulgence, purgatory, satisfaction, two verified Augsburg quotes. Two sentences of AC XII are the unrendered answers to C4-06 and C4-07: remission "whenever they are converted... The Novatians also are condemned", and the condemnation of those "who deny that those once justified can lose the Holy Ghost" (melanchthon_augsburg-confession L339–355). Drift: `witt.term.free-will` says the library carries no developed predestination doctrine, but Formula of Concord XI is in the vendored and mapped Jacobs 1911 Book of Concord (L25390), while `witt.source.book-of-concord` is registered unvendored.

## Where a modern framing needs an honest_limit

"Faith alone, not works": every pre-Reformation world (built already in don, ijc, desert; implicit in cappadocian; missing in alx, pahc, syr, hal, lpc, gallic as a record, though gallic's demo answers it in substance). "Assurance" as a felt certainty: all patristic worlds (rzg and witt have it as doctrine; rzg's limit is the model). "Predestination, did it frighten you": don, ijc, syr, pahc, hal, cappadocian have nothing; alx and gallic can answer from their own free-will teaching. "Indulgences": every world but witt and rzg. "People who never heard": don, ijc, syr, witt, rzg (unless Zwingli's *Exposition* is vendored); desert's limit is the model.

## Identified, not vendored

Prosper's three anti-Cassian works and Augustine Epp. 225–226 (gallic registry); CSEL 42 anti-Pelagian Latin and Augustine Opera t. VI (lpc, DOWNLOAD-QUEUE, held); Erasmus *De libero arbitrio* and Melanchthon's *Instructions for the Visitors* (witt, WANTS-REGISTER); Beza's *Tabula praedestinationis* and the Geneva consistory registers (rzg); Gregory of Nyssa *De pauperibus amandis* and Amphilochius's canons (cappadocian).

## Other sources (public domain or open, not downloaded)

- Calvin, *Concerning the Eternal Predestination of God* (1552), trans. Henry Cole, *Calvin's Calvinism* (1856), PD, archive.org (rzg S3; the Latin is already vendored).
- Zwingli, *Sermon on the Providence of God* (1530) and *Exposition of the Faith* (1531, the saved pagans), in *Latin Works of Huldreich Zwingli* vol. 2, ed. Hinke (Heidelberg Press 1922), PD, archive.org; vols 1 and 3 are vendored, 2 is not (rzg S3, S6).
- Bullinger, *The Decades*, Parker Society, 4 vols (1849–52), PD, archive.org; Decade I sermons 4–6 on faith, justification, good works (rzg S1).
- Prosper, *Contra Collatorem*, Latin PL 51 (Migne 1861), PD; English ACW 32 (1963) in copyright (gallic S1/S3).
- Augustine Epp. 225–226, Latin CSEL 57 (Goldbacher 1911), PD; English FOTC 32 (1956) in copyright (gallic).
- Pelagius, *Commentary on Romans*, Latin ed. Souter, Texts and Studies IX (Cambridge 1922–31), PD in the US; English de Bruyn (OUP 1993) in copyright (hal, lpc, gallic: the opponent's own voice).
- Origen, *Homilies on Leviticus* 8.3 and *Commentary on Romans* 5.9 (infant baptism), Latin PG 12/14, PD; English FOTC 83 and 103–104 in copyright (alx S2).
- Council of Orange 529, English in Hefele, *History of the Councils* vol. 4 (1895), PD; outside every window, Facilitator context only.
- No public-domain English exists for Faustus *De gratia*, Augustine *De fide et operibus*, Athanasius *Letters to Serapion* IV, or Melanchthon's 1521 *Loci*; the Latin or Greek of each is vendored or PD.

## Verification

Thirty quote records cited above as RENDERED were matched clause by clause against the vendored file named in their own locus: 30 MATCH (file and line in `C4-coverage.json`). Four failed the whole-string match and passed at clause level because the vendored line carries an inline `<note>`, a `<pb>` page break splitting "pre|cedes" (Gennadius, npnf203 L43697), or a `~1~` footnote marker (Aphrahat, hallock L47).

## Not checked

`canon/sealed_probes/`; record bodies (front matter only); the contents of Latin, Greek, French and German files beyond headings; Zwingli Latin Works vol. 2 (asserted from its published contents); the exact Decades sermon on predestination; whether rzg's mapped 1735 *Ordonnances* printing is the 1541 text; worlds without records (aec, hus, jes, meth, obel, rcg, wsyr).
