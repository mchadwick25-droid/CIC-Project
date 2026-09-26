# Step 0 Review, Round 2 — Lollardy

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline. Targeted recheck, not a full re-review.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md` (Revision 2 as edited by the narration-stripping hygiene pass, commit `4b4ce830`).
**Checked against:** Round 1 findings (`Step0_Review_Round1.md`, commit `acd9a888`); the census at `8673befa` and at HEAD; `Build/Ministry/Features/Atlas-World-Map/Decision-Log.md`; `Build/Ministry/Features/Atlas-World-Map/Design/CiC_World_Atlas_PreStep0_Survey_V0_1.md`; the vendored files in `cic/texts/`; `cic/corpus-map/lollardy.yaml` and `the-hussite-and-bohemian-brethren-movement.yaml`; the sibling Hussite Step 0; a word-level diff of `a67b1b2e` against `4b4ce830`.

## Verdict

**Substantial revision needed.** Four Round 1 findings are properly fixed: S1, S2, S5 and S7. S4's "lateral" claim is properly withdrawn. But Revision 2 introduced two new defects. It cites the wrong Decision Log entry. Its new A1 floor quotes are not verbatim. S6 is only partly fixed: stale census `why` wording is still presented as the census's live text. The sourcing sections are also now out of date against the corpus. Foxe and *Fasciculi Zizaniorum* were vendored at 16:39 on 2026-09-25. The hygiene pass ran at 18:09. The document still calls both sources "untested leads" and says the trial-record leg "currently has no accessible source." Finally, the document never engages the Hussite sibling world, even though that world's own Step 0 names Lollardy as a batch-mate with direct textual dependence.

The narration-stripping pass itself changed no quote, date, or citation. It did introduce the tense and wording problems listed under Minor.

## Findings

### Substantial

**R2-S1. §0 and A3 cite a Decision Log entry that does not contain the cited item.** Both sections name the entry "2026-08-02 (Pass 3) — ERA 7 FROZEN by Mark." The item "Q4 — Lollardy person-defined check CLEARED (its floorNote ordered the run)" sits at line 4069, under a different entry: **"2026-08-02 (Pass 3) — ERA 6 FROZEN by Mark; census 202→212; four eras Frozen in one day"** (line 4049). The ERA 7 entry (line 3958) has no Lollardy item. Round 1 S6 had placed it correctly, "within the Era 6 Freeze." Revision 2 introduced this miscitation while fixing the S6 citation. The item's own wording is quoted correctly. Fix: cite the ERA 6 FROZEN entry in both places. If wanted, also cite the gate-package entry "A1.E6 CLEARED FOR GATE" (line 4090), which records the check as "drafted lean-clear and Mark-gated."

**R2-S2. A1's new floor quotes are not verbatim, and the attribution overstates the source.** Grepped exactly, neither quote string exists in `wyclif_select-english-works-v3_arnold1871.txt`. The file reads:
- line 6397: `Sij)J)e  alle  ]?e  holi  Trinite  is  fadir  of  us  alle` (document: "sij)J)e alle J?e holi Trinite is fadir of us alle")
- lines 21101–21104: `as  ]?es  ])ree  persones … werkes  of  ]pe  Trinite  mai  not  be  departid  from  o])ir.  For  as  al  ])at  ])e  Fadir  wole,  ])e  Sone  wole,  and  ])is  Goost  wole` (document: "as J?es J?ree persones … of J?e Trinite … from oJ?ir. For as al J?at J?e Fadir wole, J?e Sone wole, and J?is Goost wole")

The document has turned the OCR's varied thorn-garbage (`]?`, `])`, `]p`, `o])ir`) into a uniform "J?". That form is neither the file's text nor a scholarly normalisation (siþþe alle þe holi Trinite…). It is a transcription that exists nowhere, and it is presented inside quotation marks. Fix: either quote the file byte-for-byte with an OCR note, or give a clearly labelled normalised reading (þ) with the line references. Do not mix the two.

The attribution is also wrong. The quotes are introduced as "Wyclif's own vernacular writing." Line 6397 is in *The Pater Noster*. Arnold's own headnote (line 6331 ff.) ascribes it to Wyclif only as "probable," on Bale's catalogue. Line 21103 is in the tract on "þe chirche and hir membris." Arnold's headnote (line 20960 ff.) argues for Wyclif's authorship but does not establish it. The document's own B2 says modern scholarship treats much of this corpus as Wycliffite (collective). Calling these two texts "Wyclif's own" states a contested attribution as settled. That contradicts the document's own B2 and CLAUDE.md's rule against presenting disputed claims as settled. The fix is simple. For a movement-level floor test, "Wycliffite writing (Arnold ascribes to Wyclif)" is both more accurate and stronger evidence. The line locations and the Ascension/Pentecost reading ("Aftir þat Crist was stied in to hevene, aboute ten daies … he sente") are correct.

**R2-S3. Round 1 S6 is only partly fixed. The census `why` quotes in A5, B4 and §4.5 are still presented as the live record.** A5 says the census's "own `why` field states plainly that 'whether the line from Lollardy to the English Reformation is a real one is contested, and the entry carries the contest rather than the conclusion.'" That wording is not in the live `why` (checked at HEAD). It exists only at `8673befa` and earlier. Round 1 S6 named A5 and B4 explicitly. §0's statusWord problem was fixed; these were not. §4.5 repeats the stale phrase as "the census's own 'contest, not conclusion' framing." B4's "(the census's own `why` field states it plainly)" is half-supported: the live `why` still says trial records preserved ordinary believers' statements. The substance survives in the live `relationsSummary` ("Contested influence line to the English Reformation"), which is quoted correctly. Fix: anchor A5 and §4.5 to `relationsSummary`, or quote the `why` wording explicitly as "as of `8673befa`."

**R2-S4. The trial-record, Twelve Conclusions and acquisition claims are out of date. The Tier discussion rests on them.** `cic/corpus-map/lollardy.yaml` now has eleven works, not seven. Commit `79b68940` (2026-09-25 16:39) vendored four more, and it is an ancestor of the hygiene commit:
- `foxe_acts-and-monuments-v3_cattley-townsend1837.txt`. Its corpus-map note: Thorpe's 1407 Examination, Sautre, Badby, Brute, Oldcastle; "Fills this world's own Step0-flagged gap."
- `fasciculi-zizaniorum_shirley1858.txt`. Contains the Latin Twelve Conclusions and the Purvey and Sautre trial records.
- `wyclif_de-ecclesia-lat_loserth1886.txt` and `wyclif_de-veritate-sacrae-scripturae-lat_buddensieg1907.txt`.

The document still says the following:
- The Section B conclusion and B4 say the trial-record leg "currently has no accessible source at all."
- The Section B conclusion and §4.2 call Foxe and *Fasciculi* "untested leads."
- §4.3 lists "all seven works."
- §4.4 says the Twelve Conclusions' accessibility is unchecked. The Latin text is now vendored inside *Fasciculi*.

The hygiene pass rewrote these points in the present tense after the vendoring had landed. Two things are still genuinely open. Both new sources are hostile (`role: context`), and neither has been content-assessed. The document should say that, not that no source exists. The Tier question ("whether the trial-record gap is either filled or found unfillable") needs reframing to match.

**R2-S5. The document never engages its Hussite sibling, and it contradicts that sibling on batch membership and overlap.** `Build/World-Builds/Hussite-and-Bohemian-Brethren-Movement/Step0_Movement_Scope_Confirmation.md` describes itself as "a three-candidate Era 6 batch alongside Lollardy and Devotio Moderna." Its §3 B3 records direct textual dependence: Schaff's introduction to the vendored Hus *De Ecclesia* says "Huss appropriated paragraph after paragraph from his predecessor." That document flags the relationship "for whichever Doc_01 runs for either world."

This document names only its original 2026-09-15 batch (Wittenberg, Reformed cities, Jesuits, Anabaptists, Tridentine). That batch is accurate per `Build/worlds/_cross-world/README.md`. But the document never mentions Hus, Bohemia, or the Hussite world at all. As a result:
- B3's uniqueness test ("no figure or source overlap found") never tests against the one candidate with real source overlap.
- B5's "the only candidate in the batch confined to one region" sits beside the Hussite document's "narrower even than Lollardy's England-only claim." The two siblings contradict each other.

**Direct answers to the two cross-assignment questions:**
- **(a) Foxe, *Acts and Monuments* Vol. III.** Grepped: 712 lines match `hus`/`huss` as whole words (724 tokens). The file sits only on the Lollardy shelf. Its corpus-map note says it "was not checked for Hus/Bohemian content, so it is assigned only here." The scan contradicts that. This Step 0 does not mention Foxe as vendored and does not mention its Hus content. It does not acknowledge the overlap at all.
- **(b) Wyclif, *De Ecclesia* (Loserth 1886).** It sits only on the Lollardy shelf. This Step 0 does not mention it, because it was vendored after Revision 2 was drafted. The document does not address cross-assignment to the Hussite world. Note one distinction: the Middle English tract on "þe chirche and hir membris" quoted in A1 is a different work from the Latin *De Ecclesia*. Arnold's own headnote says so (line 20977 ff.).

Neither corpus-map issue was touched by this review. They are Library-thread items. The Step 0 should at least name the Hussite overlap in B3 and carry it forward in §4.

### Process (blocks disposition; not a content revision)

**R2-P1. The Round 1 finding record is missing from this branch.** The hygiene pass replaced §6's finding-by-finding recap with a bare pointer: "See `Step0_Review_Round1.md` for the full finding list." §0's header points there too. That file does not exist on `library-thread/step0-revision2-hygiene` or on `origin/main`. It exists only on `origin/source-research/step0-review-round1` (commit `acd9a888`, not an ancestor of HEAD). If this branch merges alone, the only record of Round 1's findings disappears from the tree. The same problem applies to all six sibling Step 0 folders. Fix: bring the six Round 1 files onto this branch, or merge that branch first.

### Minor, but actually wrong

- **Round 1 minors still unfixed:**
  - B1's "(archive.org, HathiTrust)" claim covers all four sources, but the dossier records a HathiTrust check only for Hudson's *Selections* (dossier line 62).
  - B1's "no figure here is word-extracted from vendored XML" boilerplate is still inapplicable. None of these files is XML.
  - §0 still says the census's citations were "verified for content accuracy only, never checked for actual public accessibility," framed as "a real correction." The census never claimed accessibility.
- **Tense drift from the hygiene pass (B1).** Revision 2 said only two sources "did" carry the tag. The hygiene pass changed this to "carry," "carries a `[S]` tag" and "includes." At HEAD the census carries no "Verified." or `[S]` tags at all. The opening clause "as it stood at drafting (`git show 8673befa`)" limits the damage. The verbs should still be past tense.
- **B5 rewrite (hygiene pass).** "Not simply the narrowest single-region claim … since Wittenberg's own listed region … is itself narrow" is garbled. "Not simply the narrowest" implies it *is* the narrowest and more besides, which is the overclaim Round 1 asked to drop. Say only: "the only candidate in its batch confined to one region throughout its window."
- **Process narration still present in the canonical text.** §4.1 says "corrected in scope." §4.2 says "new in this revision." §4.3 says "acquisition status current as of this revision." B1's heading says "disclosed in full." These are the same kind of narration the hygiene pass was meant to remove.
- **A1's opening quote has no source.** "No creedal question: Lollards disputed…" is the census `floorNote`, which matches HEAD verbatim. The next sentence attributes the *finding* to "an earlier Pre-Step0 Survey floor note" without citing it. That note is `Build/Ministry/Features/Atlas-World-Map/Design/CiC_World_Atlas_PreStep0_Survey_V0_1.md`, V.5 (line 627 ff.), and its wording is different: "no plain-reading creedal question (eucharistic and ecclesiological dissent, not trinitarian)." Name the census as the source of the quote and cite the Survey file.
- **Arnold's "spurious and doubtful writings."** The phrase is a verbatim substring of Vol. I, line 173 ("probably spurious and doubtful writings separately"). Two problems. Arnold is describing works in Shirley's catalogue, several of which he *excluded*. And the document's "meaning … modern-scholarship-attributed" merges Arnold's 1869 judgement with modern scholarship. Keep the two apart.
- **B1 calls the source of Hudson's *Two Wycliffite Texts* "an unrelated story note."** It is a Lollardy (Thorpe) story note in `Build/Ministry/Features/Atlas-World-Map/Design/river-prototype.html`. It is not a census source, but it is not unrelated to Lollardy.
- **The Tier record is not cited.** §0 says the Decision Log item records only the person-defined check. The Section B conclusion then says the Tier is "carried forward from the 2026-08-02 gate" but cites no durable record that assigns the Tier. Name the source, or say plainly that the Tier rests on the census record.

## Confirmed accurate

- **S1 fixed.** At `8673befa`, exactly two Lollardy sources carry the "Verified." tag: Hudson's *Selections* and Tanner's *Norwich*. *English Wycliffite Sermons* and the Lahey/Wyclif Society entry are `[S]`. The Cambridge chapter reads "Chapter verified this session," and the document handles it separately. *Two Wycliffite Texts* is not a census source. B1 and §4.1 agree with each other.
- **S2 fixed.** Two new leads, Arnold and Vaughan, matching dossier line 73. Buddensieg and Forshall & Madden are correctly treated as confirming census leads.
- **S7 fixed.** The selection rationale is withdrawn in substance, not reworded. A4 now says only what `Build/worlds/_cross-world/README.md` supports: prior Era 6 standing.
- **S4 at drafting.** The "lateral" claim is properly withdrawn. It is now stale for the separate reason given in R2-S4.
- **S5 fixed.** The contents of Arnold Vols. I–II are confirmed in the files: Sunday Gospels, Proprium Sanctorum, Commune Sanctorum, Ferial Gospels, Sunday Epistles.
- **Round 1 minors fixed:** the *lollaert* etymology, the ~930-year gap, the vendoring status (§4.3), and the Vaughan / 1840s Wycliffe Society distinction. Vaughan's `NOT_IN_COPYRIGHT` rights basis matches the file header.
- **Census quotes.** The `floorNote` quotes in A1 and A3 are verbatim against HEAD. The `relationsSummary` quote is verbatim. The Decision Log Q4 item text is verbatim, though under the wrong entry (R2-S1). The Pre-Step0 Survey exists and does contain a V.5 floor note.
- **Article 4 quotations** are unchanged from the Round 1-verified text.
- **Hygiene diff (`a67b1b2e`→`4b4ce830`), checked word by word.** No quote string, date, figure, or file citation was altered or dropped. Every changed passage is narration removal or tense change. The only problems are the minor items above and the staleness in R2-S4.

## Disposition

Per `cic-build-cycle`, R2-S1 through R2-S5 are each false, miscited, not verbatim, or contradicted by the record. That meets the bar for substantial revision. R2-S1, R2-S2 and R2-S3 are narrow, mechanical corrections. R2-S4 and R2-S5 need real reframing of B3, B4, the Section B conclusion and §4 against the current corpus and the Hussite sibling. R2-P1 must be resolved before any disposition, whatever the revision outcome.

This is **Round 2 of the three-round cap**. If Revision 3 does not clear a targeted Round 3 recheck, this becomes an unresolved tension for escalation, not a fourth round. The corpus-map cross-assignment questions (Foxe's Hus content; *De Ecclesia* on the Hussite shelf) belong to the Library thread and are a cross-world decision for Mark. The Step 0 needs only to name them honestly.
