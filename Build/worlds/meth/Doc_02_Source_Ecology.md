# Doc_02 — Source Ecology: The Methodist Revival

**Status:** Not approved to proceed. No review round on record is an independent clearance of this document, the Source Registry or the Acquisition Manifest (see §10). Not Frozen.
**Companion documents:** `Source_Registry.md` and `Source_Acquisition_Manifest.md` (co-equal Step 2 outputs — this document is the narrative judgment; the Registry is the per-source ledger; the Manifest is the acquisition-priority list).
**Date drafted:** 2026-09-25.
**Governed by:** `Build/reference/method/CiC_Record_Native_World_Build_Process_V2.0.md`, the Library stage (Step 2); Constitution V2.3 Article 17 (five-level confidence vocabulary), Article 20 (Affirmative Duty/marginalized voices), Article 26 (Author Gravity); grounded in `Doc_01_World_Identification_Boundaries_Orientation.md` (not approved to proceed; its §9 escalates the Whitefield allocation question to the project lead), which this document does not reopen except where Doc_01's §8 open items bind this document to act.

## 1. Primary Sources

Twelve corpus-map rows across seven vendored files (`cic/corpus-map/the-methodist-revival.yaml`), organized here by figure/genre.

**Corpus figures, counted two ways.** The seven files hold 1,005,750 words by `wc -w` under the `POSIX` locale and 1,013,823 under `C.UTF-8`; a Python 3 whitespace split gives the `C.UTF-8` figure. Asbury's three Journal volumes hold 569,170 words (`POSIX`) and 573,872 (`C.UTF-8`). Wesley's own material is the Journal (208,889 `POSIX`, 210,210 `C.UTF-8`) plus the Sermons volume (89,972 and 90,210) less Sermon III (4,936 and 4,937): 293,925 words (`POSIX`) and 295,483 (`C.UTF-8`). The counts include Gutenberg and Internet Archive header text and Curnock's editorial apparatus.

**John Wesley's own voice:**
- *The Journal of the Rev. John Wesley, A.M.* (Curnock ed., Vol. I) — this world's own doorway event (Aldersgate, 24 May 1738) in Wesley's own words, plus his early life. **Volume I of eight; the remaining seven volumes, covering essentially the entire working span of the revival, are not vendored** (Manifest item G1, a host-verified queue entry for a future pass, in `Build/worlds/_cross-world/download-queue-seed.yaml`).
- *Sermons on Several Occasions*, Vol. I (Bristol, 1771) — fifteen of the sixteen sermons in this volume are his own. The volume holds Sermons I–XVI of the Forty-Four Standard Sermons. Sermon III, "Awake, Thou That Sleepest," is a separate row, below: it is Charles's own composition, not John's, per its own footnote. The volume includes "Salvation by Faith" and "The Almost Christian," his doctrine preached directly.
- The Preface to *A Collection of Hymns* (1780) — Wesley's own stated theory of what the hymnody is for.

**Institutional (Conference) voice, not Wesley's own first-person voice, though it inherits and speaks about him:**
- The Large Minutes (1850 reprint). This is not Wesley's own voice: the vendored Advertisement says the Conference "carefully revised the Rules drawn up and left us by our late venerable Father in the Gospel" (`cic:wesley-j_large-minutes_1850.txt:line100`), and the Q&A text itself refers to Wesley in the third person past tense throughout, as in "the late Mr. Wesley". It is the post-Wesley Conference's own institutional self-account of the connexion's origin and design, compiled from material Wesley himself originated but not voiced by him directly.

**Charles Wesley's own voice:**
- Sermon III, "Awake, Thou That Sleepest" (in the same vendored *Sermons* volume) — Charles's own preached prose, the one place in this corpus his own words survive outside the hymns.
- The 525 hymns of the 1780 Collection itself — present in this specific edition (not assumed from later, better-known Methodist hymnals); the movement's theology in sung, memorized form. **Not purely his own original composition throughout, and not purely an English-original witness:** the Collection includes John Wesley's own English translations of German (Moravian/Lutheran) hymns alongside Charles's own compositions (§7 below).

**Francis Asbury's own voice:**
- His complete three-volume Journal (1821 first American edition), covering his entire American ministry (1771–1815) — **the one figure in this world's corpus whose primary-text coverage is complete across his own active ministry, though not across this world's full window**: the window opens in 1738, thirty-three years before Asbury's coverage begins in 1771.

**What this list does not contain:** no Whitefield primary text at all (§6 below); no annual Conference Minutes distinct from the Large Minutes; no class/band record, class paper, or society/circuit record — the census's own named "lived organizational core" of this movement is entirely absent from what is vendored; no Bosanquet Fletcher, Hester Ann Rogers, *Arminian Magazine*, or Wesley–Crosby material — every one of the census's own named "ordinary voice" sources remains unacquired; and seven of eight Wesley Journal volumes and 28 of the Forty-Four Standard Sermons (44 total, minus the 16 held in this vendored Vol. I). This is a corpus of doctrine, connexional self-definition, hymnody, and one figure's complete pastoral journal — rich in the voices it holds, and thin in the ordinary-member and rival-movement voices it does not yet hold.

**Quotability flag per file.**

| File | Quotability |
|---|---|
| `wesley-j_journal-v1_curnock1909.txt` | Verbatim-ready (Wesley's own retrospective prose; Curnock's own editorial matter flagged separately, context role only) |
| `wesley-j_sermons-v1_1771.txt` | Verbatim-ready (own-voice throughout except Sermon III, flagged Charles's own voice) |
| `wesley-j_large-minutes_1850.txt` | Verbatim-ready, but institutional (Conference) voice, not Wesley's own first-person voice — flag on every quotation |
| `wesley-c_hymns-methodists_1780.txt` | Verbatim-ready for the Preface and the hymns; flag any specific hymn used as a translation-vs-original question before citing it as purely Charles's own composition |
| `asbury_journal-v1_1821.txt`, `-v2_1821.txt`, `-v3_1821.txt` | Verbatim-ready, with one caveat: Asbury's own Vol. II records that he spent time looking over his journals and that some things he corrected and some he expunged (lines 243–246, in 1786), so the text is his own edited retrospective, not a contemporaneous diary preserved unaltered |

**Table C — dossier section 2 cross-links.** The dossier's section 2 records no cross-link candidate for this world.

| Dossier item | Disposition |
|---|---|
| No cross-link candidate. The Reformed Cities' vendored corpus is doctrinally adjacent but not the same tradition or figures, and no Moravian-tradition text is assigned in the corpus-map | Out of scope; no row. No source is usable in both worlds' registries |

**Table D — holdings dispositions.** `python -m engine.m9.cli holdings meth` runs once `records/meth/` exists. It marks none of this world's files "not yet assessed" or "in scope, unread". It marks all seven "no coverage entry", because the tool reads a hand-typed coverage table in `engine/m1/cross_world.py` that has no entry for `the-methodist-revival`. Files marked "no coverage entry" are a Library gap, counted and left (`Open_Gaps_Tracking.md` items 15, 16 and 31).

| File | Holdings disposition | Registry row |
|---|---|---|
| `wesley-j_journal-v1_curnock1909.txt` | no coverage entry; counted and left | 1, 24 |
| `wesley-j_sermons-v1_1771.txt` | no coverage entry; counted and left | 2, 23 |
| `wesley-j_large-minutes_1850.txt` | no coverage entry; counted and left | 3 |
| `wesley-c_hymns-methodists_1780.txt` | no coverage entry; counted and left | 4, 5 |
| `asbury_journal-v1_1821.txt` | no coverage entry; counted and left | 6 |
| `asbury_journal-v2_1821.txt` | no coverage entry; counted and left | 7 |
| `asbury_journal-v3_1821.txt` | no coverage entry; counted and left | 8 |

## 2. Author Gravity Assessment

Per the Framework's own five dimensions (Visibility, Representativeness, Influence, Limitations, Transmission History).

**John Wesley.**
- *Visibility:* **Not the dominant figure in this corpus by raw volume.** The corpus totals 1,005,750 words (`POSIX`); Asbury's three Journal volumes alone are 569,170 words (56.6%), while Wesley's own material is **293,925 words (29.2%)** (the Journal at 208,889 words plus the Sermons volume at 89,972 words, minus Sermon III's own 4,936 words). Under `C.UTF-8` the figures are 573,872 of 1,013,823 (56.6%) and 295,483 (29.1%). A real share of even Wesley's total is Curnock's own editorial apparatus, not Wesley's own prose. Wesley remains the movement's central organizing figure on every other measure — first in the census's own source list, foundational to its doctrine and discipline — but that does not stand in for raw corpus dominance.
- *Representativeness:* Represents the movement's own opening year (1738, via the one vendored Journal volume) and its doctrinal core (the Sermons, the Large Minutes) in unusual depth; does **not** yet represent his working ministry across the following five decades (1738–1790) at all. Wesley in 1738 and in his own catechism is not Wesley across his own working life.
- *Influence:* Foundational, on all evidence — the connexion's own doctrine, discipline, and hymnody all derive directly from his own preaching and organizing.
- *Limitations:* A single opening-year Journal volume and a single sermon volume cannot evidence how Wesley's own preaching, or his own relationship to the connexion, changed across five subsequent decades — including his own documented later discomfort with developments (Asbury's own adoption of the title "Bishop," Doc_01 §5). This corpus cannot show that discomfort in his own words, since no letters collection is vendored.
- *Transmission History:* The Journal is the standard scholarly Curnock edition (1909–1916); the Sermons volume is Wesley's own 1771 first collected edition (Bristol: William Pine) — an earlier, more directly authorial text than a later collected-Works redaction would be.

**Charles Wesley.**
- *Visibility:* Represented by exactly one work-class (the hymns) but a substantial one — 525 hymns in a single volume of his own era's printing.
- *Representativeness:* Represents his own hymn-writing at a relatively mature point (1780, eight years before his 1788 death) but not his own Journal, letters, or any prose account of his own life or ministry — none of which is vendored.
- *Influence:* The census's own account says he set the movement's whole theology to thousands of singable hymns — a transmission mechanism distinct from his brother's preached and written prose, reaching members (particularly those who could not read) that no sermon or catechism reached the same way.
- *Limitations:* This corpus knows Charles Wesley only through his own hymn texts, not through any first-person prose account of his own life, his real and documented tensions with his brother over Methodism's relationship to the Church of England, or his role in the movement's governance.
- *Transmission History:* The 1780 Collection is a mature, standardized edition (Wesley's preface presents it as a considered arrangement, not a first printing of individual hymns written across the prior four decades). This document does not treat it as evidence of how any single hymn's text evolved across its publication history.

**Francis Asbury.**
- *Visibility:* The only figure in this corpus with complete primary-text coverage across his own active span — three full Journal volumes, 1771 through 1815, not this world's full 1738–1815 window (his American ministry begins thirty-three years after the doorway event).
- *Representativeness:* Represents the American strand's itinerant, frontier-facing ministry in exceptional depth and continuity — a strength this corpus holds that its Wesley coverage does not.
- *Influence:* The shaping figure of American Methodism, per the census's own account, and the direct authority-structure divergence point from British Methodism (Doc_01 §5).
- *Limitations:* A single figure's journal, however complete, cannot evidence the American connexion's collective decision-making (the annual Conferences, not vendored) or the experience of the ordinary circuit-riders and members under his oversight.
- *Transmission History:* The vendored edition is the original 1821 first American printing (N. Bangs and T. Mason) — not the modern 1958 critical edition, which remains in copyright (Registry rows 6–8). His text is not an unedited contemporaneous diary: Asbury records in Vol. II (lines 243–246, 1786) that he looked over the journals he had kept for fifteen years and that "some things I corrected, and some I expunged" (`cic:asbury_journal-v2_1821.txt:line169`), a layer of later self-editing.

**The corpus's overall shape.** By raw word count this corpus is dominated by Asbury and the American strand (56.6%), not by Wesley or the movement's British founding. Wesley's visibility is front-loaded to 1738, and the larger distortion is the Asbury weight: a portrait of the Methodist Revival built from this corpus alone would risk reading as a portrait of American frontier Methodism as seen by one itinerant bishop, with the British founding and its class-meeting ecology as a thin prologue, the reverse of how the census frames this world (Britain, then America). Charles Wesley is visible only as hymnodist (and in one sermon). Doc_04 and Doc_05 should guard against both risks.

## 3. Secondary Scholarship Assessment

No secondary scholarship is vendored for this world. Per the Framework: "Secondary scholarship is not a source within the world. It is the interpretive layer through which the world's primary sources are accessed." The census's own `sources` field names Henry Rack's *Reasonable Enthusiasm* (1989/2002) and David Hempton's *Methodism: Empire of the Spirit* (Yale, 2005) as the standard scholarly biographies and histories, and the Cambridge History of Christianity Vol. 7 (W. R. Ward) as a direct-fit reference chapter. None is checked against the actual books (Registry rows 20–22). This document draws directly on the primary vendored texts wherever possible and flags every place it instead relies on general historical knowledge not checked against a primary or secondary source, per the confidence discipline in §8 below.

## 4. Formation Narrative Sources

Thin in one specific sense, present in another; the two stay distinct. **Present:** Wesley's own Journal and Asbury's complete Journal are first-person, dated, narrative accounts of the movement's formation as it happened — a direct formation-narrative source class that this project's patristic worlds mostly lack (those worlds' formation narratives are more often later commemorative accounts, such as martyrdoms and saints' lives, not the founder's own contemporaneous journal). **Thin:** no *ordinary convert's* own formation narrative survives in what is vendored — no class paper, no *Arminian Magazine* testimony, no Bosanquet Fletcher or Hester Ann Rogers account. Doc_09's Story Inventory should expect strong founder-level formation narrative (especially from Asbury's complete Journal) and should not assume it can draw equally on ordinary-member narrative, which this corpus does not supply.

## 5. Material Culture and Daily Life Sources

The thinnest lens this corpus offers. The census's own selection rationale for this world names "class-meeting records" and "thousands of member narratives" as the movement's richest layer, and the vendored corpus holds none of it. What the corpus does hold that bears on daily and lived practice is indirect: Asbury's Journal narrates his own daily itinerant experience in detail (weather, distances ridden, congregations preached to, hospitality received) and is a genuine, if single-figure, daily-life source; the Large Minutes prescribe class-meeting practice in the abstract (what a class leader should ask, how often societies should meet) without evidencing how any named ordinary member lived it. This world's build cannot reconstruct an ordinary class member's weekly experience directly from primary text — only from a founder's prescription of what that experience should be, and from Asbury's clergy-level itinerant narrative. Per the Framework, this thinness is an evidentiary gap in the build's own corpus, not a claim that such material does not exist or was not richly produced (the opposite is true, and is why the census selected this world).

## 6. Source Asymmetries and Missing Voices

**The Wesley-1738/Wesley-working-ministry asymmetry (§2 above).** The Author Gravity Assessment names the gap plainly rather than letting the one vendored Journal volume's richness stand in for five decades it does not cover.

**The complete absence of Whitefield's own primary voice (Doc_01 §4, binding on this document).** This world's most important contemporary-movement figure has zero primary-text presence in this corpus. Every characterization of Whitefield in this world's documents — including Doc_01's account of the 1739–41 breach — is drawn from Wesley's own references to him, from the census's account, or from general historiography, **never from Whitefield's own words.** This is a load-bearing limitation, not a footnote: any future document quoting or characterizing Whitefield's own theology must either acquire his own text first (Manifest item G5) or flag every such characterization as second-hand. This document does not treat Whitefield as settled "context, never tradition" for this world: the census names him as one of this world's six voices and builds two of its three documented stories around him, and Doc_01 §9 escalates the allocation of his post-1741 institutional legacy to the project lead with four named options, none yet chosen. The Source Registry (row 13) states his Boundary Status neutrally as Pending. Row 13 and this paragraph hold equally under any of the four options.

**Missing voices, under Article 20's Affirmative Duty regarding the marginalized within the community.** Four named, real absences:
- **Mary Bosanquet Fletcher** — argued for women's right to preach in a 1771 letter to Wesley and won his qualified agreement (per the census's account). An Article 20 case: a documented woman's voice that the census names directly, entirely unvendored. This document cannot reconstruct her argument in her own words.
- **Hester Ann Rogers** — an ordinary female member's own spiritual narrative, unvendored.
- **The *Arminian Magazine*'s lay narrators** (1778– ) — a composite, plural Article 20 case: ordinary members' conversion accounts, in their own words, entirely absent from this corpus.
- **Richard Allen** — the census's `voices` entry states that his narrative was not published until 1833, past this world's 1815 close. This is not merely an acquisition gap that trying harder could close: even a fully successful acquisition would leave this world unable to quote Allen's account of his own 1770s conversion *as he himself later told it*, since that telling postdates the window. The era-edge tension is named rather than treating Allen as a straightforward missing-voice acquisition candidate like Bosanquet Fletcher or Rogers.

**Evidential visibility versus ecological visibility (the Framework's distinction).** What survives in the vendored corpus — a founder's doctrine and one opening year of his Journal, a connexional catechism, hymn texts, and one successor's complete pastoral record — reflects what the acquisition effort reached, not what the movement itself produced or preserved (the census is explicit that class records, member narratives, and Conference Minutes exist in abundance in real archives). The gap between corpus and ecology is named here rather than letting acquisition limits stand in for the movement's evidentiary richness.

## 7. Required Disclosure

**Cross-world relationships and overlaps.**
- **The Moravian Church at Herrnhut (VII.4).** A substantial formative-influence-then-rupture relationship (Doc_01 §7). No policy decision is made here for that world's eventual build, and the question stays open in `Open_Gaps_Tracking.md` item 2. **No corpus-map pair entry is claimed for this relationship.** The relationship is stated in prose (Doc_01 §7), since ruling on a fleet-level pair is outside this build thread's authority under that file's header (`Open_Gaps_Tracking.md` item 28).
- **The Evangelical Awakening in New England (VII.6).** Whitefield is a named `voice` of both this world and VII.6, per the census. This world's corpus-map carries no Whitefield row; the overlap is a census fact, not a corpus-map fact. It is load-bearing for the Whitefield-allocation escalation in Doc_01 §9. VII.6's 1734–c.1760 window means it cannot hold Whitefield's post-1741 legacy.
- **The Welsh Revival Tradition (VII.10).** "Sibling of Methodism" per the census's `relationsSummary`, but it does not name Whitefield among its own voices (Howell Harris, Daniel Rowland, Pantycelyn, Ann Griffiths, Thomas Charles). It remains central to the Doc_01 §9 escalation, though not as a cleanly separate home for Whitefield's line.
- **The Restoration and Georgian Church of England (VII.20).** The establishment Wesley was ordained into and never left; the source of the SPG, which sent him to Georgia (Doc_01 §2).
- **The Second Great Awakening & Camp-Meeting Tradition (VIII.2).** Asbury is a named `voice` of both this world and VIII.2 — a second direct figure-overlap, named for Doc_07 (Doc_01 §5).
- **The Holiness Movement (VIII.4).** The census's `edges` record a direct, `Documented`-confidence `formed` relationship from this world to VIII.4: the Holiness movement understood itself as recovering Wesley's doctrine of sanctification.
- **The Black Church in America (VIII.1) and Nineteenth-Century Methodism (VIII.34).** Named descendant lines (Doc_01 §1); this document reaches no claim about either tradition's eventual build. VIII.34 is this world's `continuesAs` target and the home of the in-window Primitive Methodist schism (Doc_01 §5).
- **German Pietism (VII.2).** An antecedent tradition named in the census's `relationsSummary` as feeding the Moravians; not checked against a vendored source.
- **The Reformed Cities (Zurich & Geneva, VI.2) and the Remonstrants and Dort (VI.26).** A doctrinal echo only: Whitefield's Calvinism restates the predestination question the Reformed tradition argues two centuries earlier, and the census's VI.26 entry says the label 'Arminian' became a permanent one in English-language theology and was taken up a century later by John Wesley and through him by the whole Methodist family, which is the source of this world's 'Arminian Methodism' label. Both are echoes, not institutional links, and this document cites no `Build/worlds/rzg/` material as evidence for any claim about this world.

**Edition and original-language notes.** Most vendored sources in this world's corpus are English-language originals or early English printings, but not all. The 1780 hymn Collection includes John Wesley's own English translations of German (Moravian/Lutheran) hymns alongside Charles Wesley's original compositions (§1 above), so a translation-fidelity question exists for that file. Specific translated hymns are not individually isolated (Doc_03+ scope). The other edition questions: which volume of a multi-volume work is vendored (Journal Vol. I of VIII; Sermons Vol. I of the full Standard Sermons run), and which historical printing a reprint represents (the Large Minutes' 1850 reprint states its underlying text as 1797, not Wesley's final 1789 edition; Registry row 3).

**OCR quality, gathered from the file-level disclosures in `cic/texts/REGISTRY.yaml` and the Registry.** The Aldersgate entry has no OCR defect in its date: "14." and "15." are Wesley's own paragraph numbers within a single continuous retrospective account of 24 May 1738 (Doc_01 §2). Two genuine OCR defects stand: the Large Minutes' founding year ("1/29" for "1729", Registry row 3), and a small number of stray thorn/eth-shaped glyphs in the 1780 hymnal, left untouched rather than guessed at (`cic/texts/REGISTRY.yaml`). A separate, non-OCR textual-layer note: the Journal's text embeds Curnock's own bracketed editorial insertions directly inside quoted passages (for example lines 6956 and 6981), so the bracketed words are Curnock's, not Wesley's, and any quotation drawn from a bracketed span must flag that.

## 8. Confidence Map

Per Constitution Article 17's five-level vocabulary, applied to specific claims:

- **Documented:** the existence and basic content of every primary text named in §1, confirmed against the files themselves; the Aldersgate date (24 May 1738) and quotation; the Large Minutes' catechism text on the movement's design and rise; the 1780 hymnal's preface and its stated compiler and date.
- **Widely Accepted:** the 1739–41 Wesley/Whitefield "Free Grace" breach and its doctrinal substance; the 1740 Fetter Lane/Moravian breach over "stillness"; the 1784 Christmas Conference's date, place, and episcopal-structure outcome; Wesley's later documented discomfort with the title "Bishop" as applied to Asbury; Asbury's choice to remain in America through the Revolutionary War.
- **Dominant Modern Reconstruction:** the reading of this corpus's shape (§2 above) as front-loaded toward 1738 and doctrine, thin on 1739–1790 — a reasoned inference from what is vendored, not a claim about the movement's historical balance.
- **Contested:** none identified at the level of a specific, named scholarly dispute (distinct from the unresolved acquisition gaps in §6, which are evidentiary absences, not live scholarly contests over an existing claim).
- **Inferential/Thin:** any claim about an ordinary class member's lived weekly experience beyond what the Large Minutes prescribe in the abstract (§5 above); any claim about Whitefield's theology stated in his own words (§6 above — this corpus has none); any claim about Charles Wesley's prose voice, governance role, or personal relationship to his brother beyond what his hymn texts alone can show.

## 9. Open items carried forward to later steps

1. **Holdings tool coverage.** `python -m engine.m9.cli holdings meth` reports "no coverage entry" for all seven of this world's files (Table D). The hand-typed coverage table in `engine/m1/cross_world.py` has no entry for `the-methodist-revival`; the gap is counted and left (`Open_Gaps_Tracking.md` items 15, 16 and 31).
2. **Seven of eight Wesley Journal volumes remain unacquired (Manifest item G1)** — a host-verified `download-queue-seed.yaml` entry, the highest-priority acquisition this world's build can point a future pass to.
3. **Whitefield's complete primary-text absence (Manifest item G5, Doc_01 §4)** — this world's most consequential remaining acquisition gap in figure terms. His Boundary Status is Pending (Registry row 13): not settled as "context, never tradition" and not settled as Native. Doc_01 §9 escalates the allocation of his post-1741 institutional legacy to the project lead, with four named options, pending a ruling.
4. **Four named Article 20 missing-voice items (Bosanquet Fletcher, Rogers, the *Arminian Magazine*, Manifest items G6–G8), plus the Richard Allen era-edge case (§6 above, not a straightforward acquisition item).**
5. **The class/band/circuit-record archival-access question (Manifest item G4)** — possibly requiring a different acquisition channel (a research-library request) than this project's public-domain-text sweep.
6. **The Twenty-Four Articles' own text (Manifest item G10)**, to move Doc_01 §1's Article 4 commitments (4)–(5) from general-knowledge confidence to text-verified.
7. **The individual German-hymn translations within the 1780 Collection are not isolated (§7 above)** — Doc_03+ scope.
8. **The Forces-lens step and the Article 4 check that the Library-stage rules assign to Doc_02 are not written in this document** (`Open_Gaps_Tracking.md` item 32).

## 10. Disposition

Disposition: Not approved to proceed.

Three review files are on record: `Review-Artifacts/Doc02_Round1_Review.md`, `Review-Artifacts/Doc02_Round2_Review.md` and `Review-Artifacts/Doc02_Round3_Review.md`. Round 1 was a same-thread pass by the thread that drafted this document. Rounds 2 and 3 describe themselves as independent cross-model reviews, but no reviewer record accompanies them and the pull request records every round as same-thread. Round 3 finds this document, the Source Registry and the Acquisition Manifest still substantial, on a narrower list than Round 2. No round is an independent clearance, and a self-certified clearance is not a clearance. Three review files are the cap, so a further review file needs the project lead's ruling.

**Escalation-category assessment:**
- **Portfolio-level or cross-world decision: does not apply to this document itself.** The Whitefield-allocation question is escalated at Doc_01 §9; this document's content (the corpus-map roles, the Registry, the Manifest) is written to be correct regardless of how that question is decided. The Moravian relationship (§7) is stated and carried forward as an open question for a future build thread, not decided as policy for VII.4.
- **Representative identity, title, or voice decision: does not apply.** This document's Author Gravity findings inform, but do not decide, the Step 10 Representative-structure question that Doc_01 §5 reserves for the project lead.
- **Governance or methodology decision: does not apply.** The holdings-tool gap (§9 item 1) is a Library gap, not a change to the build process.
- **Unresolved tension: applies.** Three review files are on record and none clears the document, so the three-round cap is reached without a clearance.

**Next step.** The project lead rules on review clearance and on the Doc_01 §9 escalation. Doc_03 (Lexicon Candidate List) and everything beyond it waits on that ruling.
