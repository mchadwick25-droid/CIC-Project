# Source Readiness Dossier — Early Palestinian Ascetic Monasticism

See `worlds/_cross-world/SOURCE-READINESS.md` for what this is.

**Atlas ID:** I.34
**Corpus-map slug:** `palestinian-ascetic-monasticism-early`
**Time window:** c. 330–450
**Region(s):** Gaza, the Judean desert, Sinai road
**Dossier author / date:** source-research thread, 2026-09-15
**Corpus-map / `cic/texts/` state as of:** checked directly this pass, 2026-09-15

## 1. Already assigned

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Life of S. Hilarion | jerome | tradition | assigned | ~11,619 words | `npnf206_jerome-principal-works.xml` |
| The Life of Malchus, the Captive Monk | jerome | tradition | assigned | ~3,513 words | `npnf206_jerome-principal-works.xml` |

Both rows carry a disclosed doubt from the 2026-08-26 assignment pass: this movement had no census entry at the time either was first assigned, so both originally sat under `desert-monasticism` (Egypt, Nile Valley) as the nearest available bucket, then were re-pointed here once this entry was added on record. Matches the census's own `sourcing` note exactly: *"Jerome's Life of Hilarion and Life of Malchus are the main vendored witnesses... Nothing here is the movement's own teaching in its own voice."*

## 2. Cross-link opportunities

**Sozomen's Ecclesiastical History (`npnf202_socrates-sozomen-ecclesiastical-histories.xml`) — real, unassigned, directly host-verified this pass.** Currently carries zero assignment to this world in `cic/corpus-map/_staging/npnf202_socrates-sozomen-ecclesiastical-histories.yaml` (confirmed by direct grep, zero hits). Two loci checked directly against the vendored file, not from memory:

- **Book III, ch. 14** (div id `iii.viii.xiv`, chapter title "Of the Holy Men who flourished about this time in Egypt... [and] Hilarion, and a Register of many other Saints"): *"Hilarion was born in the village of Thabatha, which is about five miles [from Gaza]..."* — a direct biographical notice, independent of Jerome's own *Life*.
- **Book V, ch. 15** (div id `iii.x.xv`, chapter title "...Mention of the Ancestors of the Author"): Sozomen's own family history — his grandfather's household in Bethelia, near Gaza, converted to Christianity through Hilarion's healing of a neighbor, Alaphion, of demonic affliction. This is Sozomen writing as a Gaza-region native with a direct family connection to Hilarion's own circle, not a secondhand report.

CORPUS-USE.md tier: same time, same place (Palestine/Gaza, 4th–5th c.) — a near-contemporary independent witness corroborating Jerome's hagiography from outside it, exactly the kind of `context` role this project's corpus-map already uses for comparable cases. A third locus, Book VI.32 (naming four brother-monks of the region, "Salamines, Phuscon..."), was noted in the volume's own editorial introduction but not independently verified against the primary chapter text this pass — flagged for whoever assigns this, not asserted.

**Chrysostom's ascetic writings — checked, and the census's own note may be imprecise.** The census's `why` field states Chrysostom's ascetic treatises were "filed under `desert-monasticism`" for lack of a home entry. Directly checked: the Chrysostom ascetic works actually flagged this way in corpus-map (`npnf109_chrysostom-priesthood-ascetic-homilies-statutes.yaml` — *Exhortation to Theodore*, *Letter to a Young Widow*) are geographically **Antiochene** (Syria), already correctly pointed at `antiochene-exegetical-christianity-chrysostom-ce`, not at Gaza/the Judean desert. No Chrysostom work was found this pass with a genuine Palestinian-monastic subject. Recorded as an open question at §5 rather than resolved here.

## 3. Verified acquisition leads

None closed this pass. One real lead, checked and found currently inaccessible rather than confirmed or closed:

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| The Pilgrimage of Etheria (Peregrinatio Aetheriae / Egeria) | Egeria (Aetheria/Silvia) | M. L. McClure and C. L. Feltoe | 1919 | `archive.org/details/pilgrimageofethe00mccliala` | pd-us-by-date (per prior verification) | **re-checked 2026-09-15, currently returns empty metadata / 404 on both `/details/` and `/download/`, despite still appearing correctly in archive.org's own search index (title, creator, date all match).** Not re-confirmed as broken — may be a transient host-side issue — but not currently fetchable either. Do not re-cite the earlier 2026-09-13 "confirmed" status (recorded in the Jerusalem dossier, §3) without re-checking access first. |

This is the same edition already named as a verified lead in `jerusalem-liturgical-pilgrimage-christianity_Source_Readiness_Dossier.md` §3. Egeria's own route to Sinai plausibly passes through or near this world's own territory, but that content-level relevance to *this* world specifically was not checked this pass — the file isn't accessible right now to check, and it should not be assumed relevant here on title alone. Whoever vendors it (for Jerusalem's own sake, where it's load-bearing) should check its route description for monastic content before assigning it here too.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Palladius, *Lausiac History* (already vendored, `palladius_lausiac-history_clarke1918.txt`) | Census's own `sourcing` note names Palladius as one of the sources giving "glimpses" of this world | Directly checked: every "Palestine"/"Judaea" mention in the vendored file is incidental (money sent to Palestine, a cleric "of Caesarea in Palestine," "the consular of Palestine") — none of it is an account of Gaza, Chariton, the laura at Pharan, or any monk this world's own record names. Not a real source for this world despite the census's own general framing; closed, not merely unassigned. |
| Cyril of Scythopolis, *Lives of the Monks of Palestine* | The obvious classic source for Palestinian monasticism | **Out of window, not merely unvendored.** Covers Euthymius, Sabas, and the great Judean-desert monasteries — this world's own successor entry, `chalcedonian-monasticism-judean-desert-and-gaza` (post-450), not this one (330–450). Named here so a later pass doesn't mistake the omission for an oversight. |

## 5. Open cross-world questions

- **Chrysostom's ascetic works (§2 above).** The census's own `why` field names Chrysostom's ascetic treatises as material once filed under `desert-monasticism` for lack of a home — but the actual flagged works found in corpus-map are Antiochene, not Palestinian. Worth a ruling on whether the census note is imprecise, or whether a different Chrysostom work (not yet located this pass) is the one actually meant.
- **The Sozomen cross-link (§2 above), once assigned, should be checked against `antiochene-church-third-century` and any other world already drawing on `npnf202`** — non-exclusive assignment is fine, but whoever adds the row should confirm no duplicate-role conflict exists in the same bucket.
- **This world's own century-long relationship to its direct successor, `chalcedonian-monasticism-judean-desert-and-gaza` (c. 450 onward).** Not a sourcing question — flagged only because the Cyril-of-Scythopolis boundary (§4) is the same shape of question `GAPPED-FORMATION-WORLDS.md` was written up for elsewhere in this batch, and a future Step 0 for this candidate may want to check that precedent doc.
