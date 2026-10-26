# C1 "Jesus" — coverage map across the twelve worlds with records

Scope: records/<code>/ for alx, cappadocian, desert, don, gallic, hal, ijc, lpc, pahc, rzg, syr, witt (fix excluded as fixture). Method: eight `coverage_search.py` runs (S1–S8 json here), an inventory of every record carrying a C-* cell or a Jesus term in `retrieve_when`/`use_note.means` (records-inventory.json), greps of each world's mapped vendored texts for the thin topics (thin-topic-grep.json), and verbatim checks of every candidate quote (quote-verification*.json). Layers: **R** rendered (a record), **L** loaded (vendored and mapped, no record), **I** identified (registry/queue, not vendored), **O** open source outside the repo. Read with `use_note.means` and `retrieve_when`, not hit counts.

## Sub-questions

| | Sub-question | Items |
|---|---|---|
| S1 | Who Jesus was to them; the good news; what he taught | C1-01–04, 11, 20, 23, 28 |
| S2 | Was he God; Trinity; prophet/teacher/God as an outsider asks; virgin birth; "the Father is greater than I" | C1-13, 21, 22, 24, R-24 |
| S3 | His death: why killed, what it did, "in our place", "personal Lord and Savior" | C1-05, 14, 15, 27 |
| S4 | Resurrection: what happened, how they knew, "grew in the telling" | C1-06, 09, 18 |
| S5 | Did he exist; eyewitness chain; outside witnesses | C1-08, 16 |
| S6 | His humanity: what he looked like, Jewishness, what he was like | C1-17, 19, 20 |
| S7 | Which gospels / writings about Jesus they had | C1-07, 25 |
| S8 | Would Jesus want someone like me; I want to believe | C1-10, 12, 26 |

## Layer table (strongest layer; strength in brackets: h/m/l, or "hon" = honest limit rendered)

| world | S1 who | S2 God | S3 death | S4 risen | S5 exist | S6 looked | S7 gospels | S8 me |
|---|---|---|---|---|---|---|---|---|
| alx | R(h) | R(h) | R(m) | R(h) | L | L | R(l) | R(h) |
| cappadocian | R(h) | R(h) | R(m) | R(m) | R(hon) | L | R(l) | R(h) |
| desert | R(h) | R(m) | R(m) | R(m) | R(l) | L | R(m) | R(h) |
| don | R(m) | R(m) | R(hon) | R(hon) | R(hon) | L | R(hon) | R(h) |
| gallic | R(h) | R(m) | R(m) | R(hon) | R(hon) | L | R(m) | R(h) |
| hal | R(h) | R(m) | R(m) | R(l) | R(hon) | L | R(m+) | R(h) |
| ijc | R(h) | R(h) | R(l) | R(m) | R(hon) | L | L | R(h) |
| lpc | R(m) | R(m) | R(m) | R(m) | R(hon) | L | L | R(m) |
| pahc | R(h) | R(m) | R(m) | R(m) | R(h) | R(m)/L | R(m) | R(m) |
| rzg | R(l) | L | R(l) | L | R(hon) | L | L | R(m) |
| syr | R(h) | R(h) | R(m) | R(h) | R(hon) | R(m) | R(h) | R(h) |
| witt | R(m) | R(m+) | R(h) | R(m) | R(hon) | I | R(l) | R(m) |

Demonstration records against the four C cells: C-I in 7 worlds (missing don, gallic, lpc, rzg, witt); C-T in 3 (cappadocian, desert, pahc); C-E in 2 (desert, pahc); C-P in 9 (missing gallic, lpc, witt). `rzg.demo.why-we` is tagged `canon_question_id: c-t-03` but its exchange is "what are you" (C16), so rzg has no Jesus demo at all.

## World by world

**alx.** The voice can say: Jesus is the Logos come in flesh (dw.jesus, demo who-was-jesus, Clement's New Song, Athanasius "made man that we might be made God"); why Nicaea's word mattered (dw.was-jesus-god, terms homoousios, son-of-god, incarnation); and it holds the fleet's best resurrection argument, Origen against Celsus II.56 (quote verified, anf04). Thin: no C-T demo; nothing on penal substitution or "personal Lord" (C-T-02/03); nothing on existence or appearance, though the two best ancient texts on appearance are mapped to this world and unread: Clement, *Paedagogus* III.1 "the Lord Himself was uncomely in aspect" (anf02:24488) and *Contra Celsum* VI.75 "little, and ill-favoured" (anf04:57478). Celsus's "mere man" and the Panthera charge (C. Cels. I.28–39) are loaded for the outsider's "prophet or God" and the virgin birth. S7 has only the Origen "firstfruits" quote (what they looked for in a gospel); Eusebius HE VI.25 (Origen's canon) and Athanasius Festal 39 are loaded. Add: quote records from C. Cels. VI.75, I.47 (Josephus on James), II.55 ("story grew"), and a C-T witness on the cross.

**cappadocian.** Strong on S1–S2 (demos who-was-jesus, taught-most, was-jesus-god; ousia/hypostasis quote verified). dw.was-jesus-god already distinguishes ransom-and-physician from "in our place". dw.how-it-reached-us states plainly that no one knew an eyewitness and that "lists still differed at the edge" (S7, but names no gospel). Thin: no quote on the cross; nothing on appearance; outsider framing and John 14:28 unrendered though Nazianzen Or. 29–30 (npnf207) answer both. Add: a quote from Or. 30.7 (Father greater), Cat. Or. 22–26 (ransom) and Amphilochius's canon list (held only as an editor's epitome).

**desert.** Everything rests on Athanasius's *Vita Antonii* and is tagged Contested, honestly. Antony to the philosophers gives S1, S2 and S4 real quotes (verified npnf204). limit.doubt-and-doctrine already says there is no penal account. Thin: S5 is silence, not an honest limit (no record says no one knew a witness); S6 nothing, though C. Cels. VI.75 is mapped here too. Add: an honest_limit for S5; consider whether anything on appearance belongs in this world (probably not).

**don.** The Donatist voice answers S3–S7 mainly by honest limits, and does it well: "no creed of ours survives", "we will not manufacture an answer" on the resurrection, "a chain of hands" not eyewitnesses, "we cannot give you a list of the books". But C-I is served by a single doctrinal_witness with no demo and no quote (Program Spec: never only propositional records). Cyprian's *Testimonia* II.13 (Christ without comeliness, anf05) is the world's own father and is loaded. Add: a C-I demo and at least one quote (Petilian or Emeritus at Carthage 411 from pl11); a quote from Testimonia II.13 for S6.

**gallic.** Good S1 (Martin and the wounded Christ, verified), S8, and a well-written C-E honest_limit that also carries the only "four men tell the Gospel, but the Gospel is one body" line in the fleet (S7). dw.one-person-two-substances says they never spoke of punishment in our place. Finding: `gallic.source.cassian-de-incarnatione` is marked unvendored and sits on WANTS-REGISTER, yet the whole work is in the vendored npnf211 (heading at line 48467). Add: fix the source record; a C-I demo; a quote from De Incarnatione for S2/S6.

**hal.** Strong S1 (Bethlehem, Paula's eyes of faith; verified). dw.record is the best Latin answer to S7 (Gospels revised against the Greek; helmeted preface; term vulgata), and Jerome's Preface to the Four Gospels to Damasus is loaded (npnf206) and unquoted. Jerome's *De viris illustribus* 13 (Josephus on Christ) is loaded (npnf203) and unused for S5. Thin: no quote on divinity or the cross; S4 has no argument. Add: Damasus preface quote; De viris 13 quote; Against Helvidius for the virgin birth.

**ijc.** The conciliar world: Nicaea, Leo's Tome, Chalcedon all verified quotes; "council voted Jesus God" handled. Thin: no atonement witness (C-T-02/03 unanswered); S7 is only loaded, though Eusebius HE III.25 (recognised/disputed books) is mapped here and to three other worlds and rendered by none; Hilary De Trin IX (John 14:28) loaded. Add: a C-T demo; an HE III.25 quote; Leo's Passion sermons for S3.

**lpc.** Three demonstrations in the whole world, none for C cells. The witnesses are sound (the-pattern-we-are-modelled-on; the-only-son-and-the-trinity; limit.no-chain-of-witnesses already carries Augustine's City of God XXII.5 argument). The world sits on 112 mapped files: Augustine's *Harmony of the Gospels* (npnf106), *De doctrina* II.8 canon list, Tractate 78 on John 14:28, and *De Trinitate* VIII.4.7 "the countenance of our Lord Himself in the flesh is variously fancied" (npnf103:10455) — the one patristic text that answers "what did he look like" by saying nobody knows. Add: C-I, C-T, C-P demos; quotes from De Trin VIII.4.7, Harmony I, Enchiridion 33–41.

**pahc.** The one world where S5 is genuinely rendered: demo center-how-we-know, witness.how-we-know, Papias, the grandsons of Jude, Pliny, Tacitus (verified against tacitus_annals-15-44), Lucian. Yet no record's `retrieve_when` says "did he exist"; the Tacitus quote retrieves on persecution. Ignatius "truly born … truly crucified … truly raised" (verified anf01) carries S1, S3, S4, S6-humanity. Thin: appearance (Justin Dial. 14, 88; Clement Paed III.1; Tertullian De carne 9 all mapped, none rendered); the outsider's "prophet or God" (Justin–Trypho Dial. 48–49, mapped, unrendered — the fleet's only period-native version of R-24); Jewishness (Dialogue throughout). S7: `pahc.quote.appointed-to-be-read` is Athanasius 367 inside a 70–200 world; Justin 1 Apol 66–67 ("memoirs … called Gospels"), Irenaeus III.11.8 (anf01:41046) and Papias are the right texts. Mara bar Serapion's "Wise King" (anf08:69289) is mapped here and to syr. Add: retrieve_when lines for existence on the Tacitus/Pliny/Lucian records; Trypho quote; Justin 1 Apol 66 quote; replace or re-home the Athanasius quote.

**rzg.** Weakest C1 world. One witness for S1, no divinity record, one Zwingli quote for S3 (verified; "eter-nity" hyphenated at line 4565), no resurrection record. The irony: this is the world whose own idiom is "in our place", and Calvin *Institutes* II.16 (vendored) is unrendered, as are I.13 (Trinity), III.25 (resurrection) and Second Helvetic XI. Add: C-I/C-T demos, Institutes II.16 and Second Helvetic XI quotes, a C-I quote from the Sixty-Seven Articles 2–5.

**syr.** Best world for S7 (Diatessaron as the Gospel: dw.gospel-harmony, gravity, two contested_claims, anf09 cited) and strong on S1, S4, S8 (Ephrem and Aphrahat quotes verified npnf213). dw.gospel-harmony is also the best-phrased honest limit on eyewitnesses ("our story of an apostle sent to our king is our cherished legend, not our evidence"). Thin: Aphrahat Dem. XVII — written against the Jewish objection "you call a man God" — is the fleet's best period answer to R-24 and only its opening line is rendered; Mara bar Serapion loaded; no penal statement, no appearance. Add: Dem. XVII quote for the outsider; Mara bar Serapion quote for S5; an honest_limit on appearance.

**witt.** Catechism-shaped and good on S3 ("redeemed … with his holy precious blood"; "He is my Lord"; verified Small Catechism). Thin: no C-I or C-P demo; S7 does not say which gospels (Luther's 1522 Preface to the NT is the text; the 1522 German is PD, the Holman English only from 2028); S6 is the single IDENTIFIED cell in the table: *That Jesus Christ Was Born a Jew* (1523) is on WANTS-REGISTER and is the one text in the fleet whose title answers C1-19. Add: C-I demo; the 1523 treatise (German PD) and Augsburg Art. III quote.

## Where the whole fleet is thin

1. **"Did he really exist?"** No record in any world retrieves on it. Honest limits on the eyewitness chain exist in 9 worlds; the outside witnesses are vendored for pahc (Tacitus, Suetonius, Lucian, Pliny via npnf201, Mara bar Serapion) and the Josephus passages are loaded through Eusebius HE I.11 (alx, ijc, pahc, syr) and Jerome De viris 13 (seven worlds). Josephus is not vendored in his own right.
2. **"What did he look like?"** Nothing rendered anywhere. Loaded: Clement Paed III.1, Contra Celsum VI.75, Tertullian De carne 9, Justin Dial. 14/88, Cyprian Test. II.13, Augustine De Trin VIII.4.7. These answer the question historically (the second-century consensus: plain, from Isaiah 53) and are already in hand.
3. **"Prophet or teacher or God?" as an outsider asks.** Every world says "God"; none stages the objection. Period texts that do: Justin–Trypho (pahc), Aphrahat Dem. XVII (syr), Celsus in Origen (alx/desert/hal), Nazianzen Or. 30 (cappadocian), Calvin I.13 (rzg). All loaded.
4. **"Which gospels?"** Rendered well only in syr (Diatessaron) and hal (Vulgate); gallic names "four". Eusebius HE III.25, Irenaeus III.11.8, Justin 1 Apol 66–67, Athanasius Festal 39, Augustine De doctrina II.8 and Harmony are all vendored and mapped.
5. **Penal substitution (C-T-02).** Honest distinctions are rendered in cappadocian, desert, gallic, hal, don; absent in alx, ijc, lpc, pahc, syr; and unrendered in the two worlds that actually taught it (witt partly, rzg not at all).

## Other open sources (not downloaded)

- Josephus, *Antiquities* XVIII.3.3, XX.9.1, trans. William Whiston (1737): Project Gutenberg #2848, Perseus; public domain.
- Muratorian fragment: B.F. Westcott, *A General Survey of the History of the Canon of the New Testament* (Macmillan, 1875), appendix C; archive.org; PD.
- F.C. Burkitt, *Evangelion da-Mepharreshe: the Curetonian Version of the Four Gospels, with the readings of the Sinai palimpsest* (Cambridge 1904); archive.org; PD — Old Syriac for syr S7.
- J. Hamlyn Hill, *The Earliest Life of Christ … the Diatessaron of Tatian* (T&T Clark 1894); archive.org; PD.
- M.R. James, *The Apocryphal New Testament* (Oxford 1924); PD in the US since 2020 — Acts of John 88–93, Gospel of Peter, Oxyrhynchus sayings (Grenfell & Hunt, *Logia Iesou*, 1897, PD) for apocryphal-gospel questions.
- Calvin, *Harmony of the Evangelists*, trans. William Pringle (Calvin Translation Society 1845–46); CCEL; PD.
- Luther, *Commentary on Galatians* (1535), trans. Middleton 1575, rev. 1850; CCEL; PD — the penal locus (3:13).
- Luther, *Dass Jesus Christus ein geborener Jude sei* (1523), WA 11; German PD; the English LW 45 (1962) is in copyright.
- Luther, *Vorrede auf das Neue Testament* (1522), WA DB 6; German PD; Holman English (1932) US-PD from 2028.

## Not checked

The .docx Doc_02 files (cappadocian, pahc W1) were not opened; only the .md versions were grepped. `canon/sealed_probes/` was not read. Vendored texts were grepped, not read through, so a loaded text's exact wording at the cited line is confirmed only where a line number is given. Six verbatim mismatches outside C1's scope (desert Macarian x2, gallic Salvian x4) were not resolved. `fix` was excluded. Worlds without records (aec, hus, jes, meth, obel, rcg, wsyr) were not mapped. External-source licences are from knowledge, not re-verified online.
