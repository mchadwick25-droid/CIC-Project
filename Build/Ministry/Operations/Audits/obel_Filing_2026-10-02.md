# obel filing and gate resync, 2026-10-02

Scope: bring PR #623 (The Old Believers, code `obel`, Steps 0 to 2 written 2026-09-25 under the V1.8 process) up to the current Library-stage gates of `main`. No change to scholarship, confidence tags or any review outcome. The package carries "Approved to proceed" as the project lead's ruling of 2026-09-26 gave it (the commit `bcbae1a15`, recorded in `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md` under "Escalation does not park the document: a named escalated item waits, the document proceeds"); this filing adds no disposition beyond that ruling. Not Frozen. Session: https://claude.ai/code/session_019FXuEebrCDmzYe987sNAxL

## Merge of origin/main

| Conflict | Resolution |
|---|---|
| `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md` (both sides appended at the end) | Main's entries kept in main's order; the branch's one entry (2026-09-26, "Escalation does not park the document") appended after them. Paths in that entry repointed to `Build/...`. |
| `Build/worlds/_cross-world/NEEDS-RULING.md` (both sides appended after item 4) | Main's text kept; the branch's hand-maintained item 5 appended after it. Paths in item 5 repointed. |
| `Build/worlds/_cross-world/dossiers/the-old-believers_Source_Readiness_Dossier.md` (the branch added it at the retired `worlds/_cross-world/dossiers/`) | Lands at `Build/worlds/_cross-world/dossiers/`. |
| `cic/texts/README.md` (generated) | Main's version taken, regenerated with `python cic/engine/texts_registry.py --write-readme` (433 files listed). `REGISTRY.yaml` merged without conflict; the branch's two rows are appended and no existing row is changed. |
| `cic/corpus-map/the-old-believers.yaml` (generated) and its two staging files | `python cic/engine/corpus_map_merge.py --assign-ids` gave both staging rows a `row_id`, then a full merge; `--check` is valid. |
| `worlds/obel/` (the branch added seven files under the retired top-level `worlds/`) | Moved to `Build/worlds/obel/`. The empty `worlds/` directory is removed. |

## Filing

- Documents at `Build/worlds/obel/`: Step 0, Doc_01, Doc_02, `Source_Registry.md` (was `obel_Source_Registry.md`), `Open_Gaps_Tracking.md`. Build state and handoff manifest at `Build/worlds/obel/build/`. `records/obel/.gitkeep` added.
- The two combined review files are filed as `Step0_Review_Round<n>.md`, `Review-Artifacts/Doc01_Round<n>_Review.md` and `Review-Artifacts/Doc02_Round<n>_Review.md` for n = 1 (the Round 1 review) and n = 2 (the Round 2 targeted recheck), identical copies of each round's text. Only paths cited in the texts were repointed (`worlds/...` to `Build/worlds/...`, `Ministry/...` to `Build/Ministry/...`, `reference/...` to `Build/reference/...`; the retired process files V1.5 and V1.8 are cited by bare file name because they are not in the tree). One wrapped path fragment in the Round 1 review ("`cic/corpus-map/the-old-believers_Source_Readiness_ Dossier.md`") lost its directory prefix. The heading of Round 1 Finding 14 no longer contains the word "unresolved" (the gaps gate read it as an open-items heading): it read `Doc_01 §4 leaves as "unresolved" a question the evidence in hand settles, and states a false premise in doing so`. The Round 2 files end with the line `Disposition: Approved to proceed`, which restates section 11 of the Round 2 recheck (the project lead's ruling and its application). No header fields were added. No Round 3 review file exists.
- Registry entry `records/worlds/obel.yaml`: `state: candidate` added (the entry carried no state). `safety_adjacent` left unset (project lead's field).
- Source Registry rewritten to the 11-column layout with the `Discovery (channel / instrument / date)` column (12 pipes a row); one Confidence letter per row, unchanged from the branch (row 1 at A, row 2 at B, rows 3 to 12 at B or C); rows numbered 1 to 12 (the branch used R1 to R9, which earlier Open_Gaps entries and the review files still cite; rows 10 to 12 would otherwise trip the live-commentary "ruling-number" pattern); rows 10 (Tale of Boyarynya Morozova lead), 11 (census-named modern translations of the Zhitie) and 12 (*Vinograd rossiiskii*) added from the dossier and census; corpus figures counted two ways with the locale stated (also in Doc_02 section 5); R5's census quotation restored to the census's own hyphen.
- Doc_02 section 5 rewritten to the current holdings report (433 files, 2 + 145 + 286; the branch's text carried 224 files, 2 + 98 + 124).
- Doc_02 section 3: the statement that `row_id` and `voice_of` are not carried by any real bucket is replaced; the Library has issued `row_id` on both rows.
- Census wording: `cic-website/data/world-census.json` on `main` no longer carries the `statusWord` "Researched — strong candidate (Era 8 Step 0)" or the `statusDescription` that Step 0 section 1 quoted. Step 0 section 1 now quotes the current text and section 2 cites the current `statusDescription` for the phrase "a clean example that the floor is the Creed, not liturgical correctness". `floorNote` is unchanged. Step 0 section 5 and Doc_02 section 15 say `floorNote` where they said `floorNote`/`statusDescription`. `NEEDS-RULING.md` item 5, the Decision Log entry and Open_Gaps still name both fields; entry 21 of `Open_Gaps_Tracking.md` records this for the project lead.
- Open_Gaps_Tracking.md: bare-number cross-references (the gaps gate) now cite subject and date; entries 20 to 25 appended; no earlier entry's text is otherwise changed except path repointing.
- Corpus-map staging notes: the Russian file's note lost its CORRECTED and CORRECTION-OF-A-CORRECTION text; the English file's note no longer calls the OCR clean (it carries stray marks). The bucket is regenerated.
- Doc_01 section 3: the pointer "discussed at §9" after the Markovna passage removed (section 9 does not discuss it).

## Quotations changed to verify

The gate reads the vendored English file as printed, with its stray OCR marks and page-break running heads. Doc_01 section 9 now quotes pp. 34, 120 and 121 in segments joined by an ellipsis, or with the one bracketed repair of "zs", and says so; Doc_02 section 7 states that convention in place of the former "silent repair" convention. English renderings of Russian phrases and of the Russian authority list lost their quotation marks and are introduced as the document's own English. Quotations of `cic/texts/INTAKE.md`, the Atlas Decision Log and the Era 7 and Era 8 entries are plain prose.


## History moved out of the live documents

Each of the four documents ended in a Document Log; Step 0, Doc_01 and Doc_02 also carried status narration and dated citations in the body. Removed text, verbatim.

## Step 0 section 6, Document log

```text
## 6. Document log

- **Round 1 draft**, 2026-09-25, this build thread.
- **Round 1 self-review**, 2026-09-25, applied directly before
  independent review landed: corrected a misread Decision-Log citation
  for the Era 8 window, and withdrew a premature "Approved to proceed"
  self-disposition that had been applied before any review ran.
- **Round 1 independent review** (`obel_Step0_Doc01_Doc02_Review_
  Round1.md`, plus its own reconciliation addendum against the
  self-review commits): **substantial revision required.** Findings
  against this document: 1 (blocking — the floor claim, §2), 18 (a
  misreading of the Decision-Log's own "12 drafts" list as evidence this
  world was drafted at the Era 8 gate, §1), 19 (confirmed already fixed
  by the self-review pass), 21 (confirmed already fixed by the
  self-review pass), plus shared findings 2/3 (blocking — a fabricated
  INTAKE.md citation) and 20 (blocking — citing V1.8, a specification not
  present in this checkout).
- **Round 2 revision**, 2026-09-25, this build thread. §1 corrected to
  state precisely what the Decision-Log actually shows (this world
  pre-existed the Era 8 gate pass as a banked entry, rather than having
  been drafted at it). §2 restated in full around the p. 34 Creed-wording
  passage this world's own vendored source supplies, in place of the
  census's own overstated absolute floor claim. Process narration is
  removed from the body text above; this log entry is where that history
  now lives. This same revision also (at the time, apparently correctly)
  withdrew a citation to a 2026-09-25 INTAKE.md ruling as unfounded, and
  re-grounded this world's citations to the process specification on
  V1.5 rather than V1.8, on the finding that neither the ruling nor V1.8
  was present in this checkout — see the next entry.
- **Correction-of-a-correction, 2026-09-25, this build thread, following
  the coordinator's own direct check.** This worktree's checkout had
  branched from a stale local `main` (merge-base `41afa0f8`), roughly 150
  commits behind the real `origin/main` (`58fed0f6`). Both the
  2026-09-25 INTAKE.md ruling and `CiC_Record_Native_World_Build_Process_
  V1.8.md` were already merged to real `origin/main` — via PR #594 and
  commit `077b84fe` respectively — hours before this build thread
  started; this checkout simply predated them and could not see them.
  The citation was not fabricated — it was real and current, unreadable
  only from this stale checkout. After merging `origin/main` (merge
  commit `169dc5cb`) and independently re-reading the real, current
  `INTAKE.md` and `V1.8.md` directly (not taking the coordinator's word a
  second time), this document's escalation is narrowed at §5 above to
  the one item that was never a stale-checkout artifact: the census's
  own floor-claim overstatement. The corresponding restoration of the
  Russian source's own primary-evidence status, and the re-grounding of
  citations from V1.5 back onto V1.8, are made in `Doc_01` §4/§10/§13,
  `Doc_02` §0/§1.1/§7/§16/§17, the `obel_Source_Registry.md`,
  `cic/texts/REGISTRY.yaml`, `cic/corpus-map/`, and the Dossier — each
  disclosed there as its own dated correction-of-a-correction, and in
  `Open_Gaps_Tracking.md`. This entry, and the ones it points to, are
  left standing alongside the Round 2 entry above rather than replacing
  it, so the record shows both what was believed at the time and why it
  changed.
- **Round 2 targeted recheck** (`obel_Step0_Doc01_Doc02_Review_
  Round2_Recheck.md`): **substantial revision required, narrowly.** All
  six of Round 1's blocking findings confirmed closed; every quotation
  and locus re-verified independently and found correct. What remained
  against this document: the §1 aside naming this section's own
  jurisdiction (removed above, Finding 29); this section's own
  self-disposition sentence, read against the escalation categories it
  names in the same breath (N6 — put to Mark rather than resolved here,
  above).
- **Round 3 revision**, 2026-09-25, this build thread. §1's jurisdictional
  aside removed. §5 no longer self-dispositions; disposition of the
  whole package is deferred to Mark, and the tension between naming an
  escalation category and self-disposing under CO-022 is itself named as
  a second escalation item (N6) rather than resolved by this thread.
- **Approved to proceed.** The full disposition record — the review
  artifacts it rests on, the one item that waits, and who applied it —
  is at `Open_Gaps_Tracking.md` entry 18. Not Frozen; nothing here is
  closed.
```


## Step 0 section 1, census quotation and Era 7 / Era 8 account (replaced by present-tense text)

```text
- `status: "Pre-Survey Candidate"`, `chip/glyph: "psc"`
- `statusWord: "Researched — strong candidate (Era 8 Step 0)"`
- `statusDescription`: "Reviewed at the Era 8 Step 0 run and tiered Strong
  (Tier 1) on a rich inside voice: Avvakum's autobiography, verified in the
  source pass, is a first-person masterpiece. Its floorNote was cited
  approvingly at the gate as a clean example that the floor is the Creed
  and not liturgical correctness. Its end moved to 1815, with Edinoverie
  (1800) named so that a previously near-principled accident became a
  stated reason."


...
This world (VII.7) is a separate Atlas entry from the official Synodal
Russian church's own entry, already banked before the Era 8 gate pass
that drafted the Synodal church's entry alongside it: the 2026-08-02 Era
7 Frozen entry records "NOT written: VI.24→VII.4, VI.23→VII.7 (era 8's),"
and the same entry's own forward-reference note names "Old Believers at
era 8" among Era 8's banked flags (quoted again just below). This
world's Frozen status is separately confirmed ("ERA 8 FROZEN by Mark;
census 221→233... Mark's ruling, verbatim: 'yes to all, move forward.'").

**On the 1815 end date:** the same Decision-Log entry records that this
gate pass "replaced" a "round-1800 artifact cluster" across several Era 8
entries "with honest 1815 caps." Era 8 itself is explicitly scoped as
**1650-1815** in a forward-reference note at the close of the
immediately preceding Era 7 Frozen entry (2026-08-02): "Next: A1.E8
(1650–1815) with its banked forward flags... Old Believers at era 8..."
This means 1815 is **the fleet's own Era 8 portfolio boundary, not a
historical event specific to the Old Believer movement's own
trajectory**. The nearest genuinely Old-Believer-relevant event before
that boundary is Edinoverie's establishment in 1800 (the first formal
reconciliation channel between the Synodal church and old-rite worship),
which the census's own `statusDescription` names as giving the mechanical
1815 cap a substantive nearby anchor. The movement's next major
structural turn — the priestly Old Believers' restoration of their own
episcopate (Belokrinitsa hierarchy, 1846) — falls outside this window
and is noted in Doc_01 as a later development, not in scope.
```


## Doc_01 section 13, Document log

```text
## 13. Document log

- **Round 1 draft**, 2026-09-25, this build thread.
- **Round 1 self-review**, 2026-09-25, applied directly before
  independent review landed: corrected a silently-normalized name
  ("Meletina" printed as "Meletius"), split an over-broad confidence tag,
  and fixed an en-dash/citation-precision error in a Decision-Log quote.
- **Round 1 independent review** (`obel_Step0_Doc01_Doc02_
  Review_Round1.md`, plus its own reconciliation addendum against the
  self-review commits): **substantial revision required.** Findings
  against this document: 1 (blocking — the floor claim contradicted by
  this world's own vendored source at p. 34), 4, 5, 6, 7, 9, 10, 11, 14,
  16, 18, 19, 23, 26, 28, plus shared findings 2, 3 (blocking — a
  fabricated INTAKE.md citation), 20 (blocking — three canonical
  documents cited a specification, V1.8, not present in this checkout),
  and 29 (process narration embedded in canonical text).
- **Round 2 revision**, 2026-09-25, this build thread. Every finding
  fixed: the two/three-fingers authority list is re-quoted exactly
  against both vendored witnesses, correcting a misread that had wrongly
  called "Cyrene" a corruption and missed the real one ("Heart" for
  "Blest"); three of four quotable-passage loci are corrected from a
  page-numbering method that was backward (§9, Doc_02 §1.1); the
  Pomorian Answers' misattribution to Semyon Denisov alone is corrected
  to Andrei Denisov, with Semyon Denisov and Trifon Petrov as
  participants; a false claim that no Orthodox-lane world is built is
  corrected to name `cappadocian` and argue why it is still not a
  comparandum (§5, §8); a self-contradiction in §8 is resolved; the
  cultural-scope section (§4) is rebuilt in full around a genuine
  edition finding (the English translation omits Avvakum's own
  plain-speech apologia) in place of a withdrawn, rule-violating use of
  the Russian text as free-standing evidence; the floor claim (§9) is
  restated in full around the p. 34 Creed-wording passage the source
  itself supplies; census-only claims are re-tagged Widely Accepted
  rather than Documented throughout; and the V1.8 citations are
  re-grounded on V1.5, the specification actually present in this
  checkout. Process narration is removed from the body text; this log
  entry, together with `Open_Gaps_Tracking.md`, is where that history
  now lives.
- **Correction-of-a-correction, 2026-09-25, this build thread, following
  the coordinator's own direct check.** This worktree's checkout had
  branched from a stale local `main`, itself already well behind real
  `origin/main` before this session started. Both `reference/method/
  CiC_Record_Native_World_Build_Process_V1.8.md` and `cic/texts/
  INTAKE.md`'s real 2026-09-25 ruling ("a clean public-domain original
  can be primary evidence... language is not what decides whether a
  source is primary — credibility and truth are") were already merged to
  the real `origin/main` hours before this session began; this
  checkout's own copy of `INTAKE.md` simply predated the commit that
  added that ruling. The citation was not fabricated — it was real and
  current, unreadable only from this stale checkout. After merging
  `origin/main` and independently re-reading the real, current
  `INTAKE.md` directly (not taken on the coordinator's word a second
  time), the Russian text's status as this world's own primary evidence
  is restored at §4 above, in `Doc_02`, the Registry, `cic/texts/
  REGISTRY.yaml`, `cic/corpus-map/`, and the Dossier — each disclosed as
  a dated correction-of-a-correction in `Open_Gaps_Tracking.md`, not
  silently flipped back. The genuine, still-live quotability caveats
  (the unverified transcription chain; the bracketed editorial glosses
  elsewhere in the file) are unaffected by this correction and remain
  disclosed. V1.8 citations are likewise re-grounded back onto V1.8,
  which is now present in this checkout after the same merge.
- **Round 2 targeted recheck** (`obel_Step0_Doc01_Doc02_Review_
  Round2_Recheck.md`): **substantial revision required, narrowly.** All
  six of Round 1's blocking findings confirmed closed; every quotation
  and locus independently re-verified and found correct. Against this
  document specifically: the bracketed-gloss count ("roughly ninety")
  found to be a byte-versus-character measurement artifact, the real
  figure 116; §8's "same window" claim found over-broad against the
  three named `russian-church-*` candidates, only one of which
  (`russian-church-nikon-to-holy-synod`) actually overlaps this world's
  window; §5's same-lane enumeration found to omit
  `imperial-juridical-christianity`; and the filioque quotation at §9
  found to bridge a 577-character gap under a single ellipsis wider than
  a reader would assume.
- **Round 3 revision**, 2026-09-25, this build thread. The gloss count
  corrected to 116 throughout (§4, §11); §8 narrowed to name
  `russian-church-nikon-to-holy-synod` as the one genuinely overlapping
  candidate and the other two as adjacent, non-overlapping; §5 corrected
  to name `imperial-juridical-christianity` and set it aside by the same
  method as `cappadocian`; the filioque quotation at §9 split into its
  two actual fragments, each quoted and introduced on its own rather than
  joined by an ellipsis. A transcription convention (silent OCR repair
  and smart-quote normalization, disclosed once) is stated at Doc_02 §7
  rather than left undisclosed, closing a cosmetic item the recheck
  raised again after Round 1.
- **Escalated to Mark, not resolved by this document:** the census's own
  `floorNote`/`statusDescription`, which carry the overstated absolute
  floor phrasing this revision corrected (§9), were cited approvingly at
  a Frozen portfolio gate — correcting them is portfolio-level. A second,
  distinct governance/methodology question (whether naming an escalation
  category in a Disposition section bars self-disposition under CO-022)
  is escalated alongside it, per Step 0 §5. Nothing else from this
  world's own build remains escalated as a governance question: the
  INTAKE.md and V1.8 items above were a stale-checkout problem, now
  resolved by merging forward, not an open policy question.
- **Approved to proceed.** The full disposition record — the review
  artifacts it rests on, the one item that waits, and who applied it —
  is at `Open_Gaps_Tracking.md` entry 18. Not Frozen; nothing here is
  closed.
```


## Doc_01 section 9, text replaced by verifiable quotations

```text
> "It were better in the Creed not to pronounce the word Lord, which is
> an accidental name, than to cut out "True", for in that name is
> contained the essence of God. But we, the True Believers, confess both
> names, and we believe in the Holy Spirit, the True and Life-giving
> Lord, our Light, worshipped together..."


=====
first, on the Roman practice generally, "по-римски святую тройцу в
четверицу глаголют" ("in the Roman manner they make the Holy Trinity
into a foursome"); second, on the Spirit's procession specifically, "духу
и от сына исхождение являют" ("and they hold that the Spirit proceeds
from the Son also"). The same passage pronounces anathema on those who
sing the Alleluia fourfold: "Да будет проклят сице поюще" ("Cursed be
those who sing it so").


=====
> "Why," said they, "art thou stubborn? The folk of Palestine, Serbia,
> Albania, the Wallachians, they of Rome and Poland, all these do cross
> themselves with three fingers, only thou standest out in thine
> obstinacy and dost cross thyself with two fingers; it is not seemly."

And Avvakum's own reply, quoted verbatim from p. 121:

> "By the gift of God among us there is autocracy; till the time of
> Nikon, the apostate, in our Russia under our pious princes and tsars
> the orthodox faith was pure and undefiled, and in the Church was no
> sedition. Nikon, the wolf, together with the devil, ordained that men
> should cross themselves with three fingers, but our first shepherds
> made the sign of the cross and blessed men as of old with two fingers,
> according to the tradition of our holy fathers..."
```


## Doc_01, other passages reworded (old text only)

```text
**Built from:** `Step0_Movement_Scope_Confirmation.md`; `cic-website/
data/world-census.json`'s own `the-old-believers` entry (VII.7);
`Ministry/Features/Atlas-World-Map/Decision-Log.md`'s Era 7 and Era 8
gate entries; `reference/method/CiC_Record_Native_World_Build_
Process_V1.8.md`; `cic/texts/INTAKE.md`'s 2026-09-25 ruling on
original-language primary evidence; this world's own two vendored
=====
What makes this a distinct formation world, not merely "17th-century
Russian Orthodoxy in general":
=====
anathematized those who refused — **[Widely Accepted]**, on the
  census's own record and the Decision-Log's own Era 8 gate entry
  (§2.1).
=====
  - Russian (same locus): "Мелетия антиохийскаго и Феодора Блаженнаго,
    епископа киринейскаго, Петра Дамаскина и Максима Грека" — "Meletios
    of Antioch and Theodore the Blessed, bishop of Cyrene, Peter of
    Damascus and Maxim the Greek."
=====
From the
  official Synodal Russian church (Atlas entry unbuilt as of this
  writing), this world is the ritual-and-textual position the 1666
  council's own anathema was directed against, not the anathematizing
  body. This world (VII.7) is a separate Atlas entry from the Synodal
  church's own entry, already banked before the Era 8 gate pass that
  drafted the Synodal church's own entry alongside it: the 2026-08-02
  Era 7 Frozen entry records "NOT written: VI.24→VII.4, VI.23→VII.7
  (era 8's)," and the same entry's own forward-reference note names "Old
  Believers at era 8" among Era 8's banked flags (§2.2). 
=====
Era 8 is fleet-scoped as 1650-1815, per a forward-reference note at the
close of the immediately preceding Era 7 Frozen entry
(`Ministry/Features/Atlas-World-Map/Decision-Log.md`, 2026-08-02):
"Next: A1.E8 (1650–1815) with its banked forward flags... Old Believers
at era 8..." — this world is named directly, confirming it was already
in view when this boundary was set. The Era 8 gate's own Frozen entry
(2026-08-03, "ERA 8 FROZEN by Mark") separately records that this gate
pass "replaced" a "round-1800 artifact cluster" across several Era 8
entries "with honest 1815 caps" — i.e., 1815 is the fleet's own
portfolio-level closing year for the whole era, applied across multiple
movements at the same gate pass, not a date independently argued from
this movement's own history.


=====
census's own `statusDescription` names this as giving the
mechanical 1815 cap a substantive nearby anchor.
=====
lane that only half-overlaps this one ("Greek East / Latin West
bridge")
=====
under this project's own real, current rule
(INTAKE.md, Mark's ruling of 2026-09-25): language is not what decides
whether a source is primary; credibility and truth are.
=====
`reference/method/CiC_Record_Native_World_Build_Process_V1.8.md`
=====
(`worlds/_cross-world/dossiers/the-old-believers_Source_Readiness_
  Dossier.md`)
```


## Doc_02 section 16, Document log

```text
## 16. Document log

- **Round 1 draft**, 2026-09-25, this build thread, together with
  `obel_Source_Registry.md`.
- **Round 1 self-review**, 2026-09-25, applied directly before
  independent review landed.
- **Round 1 independent review** (`obel_Step0_Doc01_Doc02_Review_
  Round1.md`, plus its own reconciliation addendum): **substantial
  revision required.** Findings against this document: 6, 7, 8 (three of
  four quotable-passage loci wrong, from a page-numbering method that
  was backward), 9 (a false claim that no Orthodox-lane world is built),
  11 (a misattributed primary text, via the Registry), 12 (systematically
  misapplied Registry confidence tiers), 13 (an undisclosed quotation
  hazard — ~90 editorial glosses in the Russian file), 15 (an overstated
  edition-provenance claim and an undisclosed edition substitution), 16
  (an uncaught error in the vendored edition's own apparatus), 17 (a
  contradiction between the two vendored witnesses, read but not
  cross-checked), 20 (blocking — citing V1.8, a specification not
  present in this checkout), 24 (a docstring citation that said the
  opposite of what the actual module says), 25 (partial delivery against
  V1.8's own stated requirements), plus shared findings 1 (blocking — the
  floor claim), 2/3 (blocking — the fabricated INTAKE.md citation), and
  29 (process narration embedded in canonical text).
- **Round 2 revision**, 2026-09-25, this build thread. Every finding
  fixed: the p. 34 Creed-wording passage is added as a quotable, directly
  evidenced passage; all four loci are corrected against the file's own
  real pagination convention; the Pomorian Answers' authorship is
  corrected to Andrei Denisov; the Registry's confidence tiers are
  corrected per the Source Registry Template's own definitions; the
  bracket-gloss hazard and the loose `orv` tag are disclosed in full; the
  edition substitution against the census's own preferred modern
  translations is disclosed; the vendored edition's execution-date error
  and the two witnesses' authorship contradiction are both disclosed as
  open findings rather than silently resolved; the holdings-disposition
  section's docstring citation is corrected to what the module actually
  says, and the finding it was dismissing is left open rather than
  re-dismissed on a different unverifiable authority; the (at the time,
  apparently fabricated) INTAKE.md citation is removed from this document
  and from `cic/texts/REGISTRY.yaml` and `cic/corpus-map/`, outside this
  world's own folder; and citations are re-grounded on V1.5, the
  specification apparently present in this checkout at the time. Process
  narration and a full self-assessment section are removed from the body
  text; this log entry, together with `Open_Gaps_Tracking.md`, is where
  that history now lives.
- **Correction-of-a-correction, 2026-09-25, this build thread, following
  the coordinator's own direct check.** This worktree's checkout had
  branched from a stale local `main`, already well behind real
  `origin/main` before this session began. Both `V1.8` and `INTAKE.md`'s
  real 2026-09-25 ruling ("a clean public-domain original can be primary
  evidence... language is not what decides whether a source is primary —
  credibility and truth are") were already merged to the real
  `origin/main` hours earlier; this checkout's own copy simply predated
  that commit. The citation was real and current, not fabricated. After
  merging `origin/main` and independently re-reading the real, current
  `INTAKE.md` directly, the Russian text's status as this world's own
  primary evidence is restored throughout this document (§0, §1.1, §7),
  the Registry, `cic/texts/REGISTRY.yaml`, `cic/corpus-map/`, and the
  Dossier, and citations are re-grounded back onto V1.8, now present in
  this checkout. The still-live quotability caveats (the unverified
  transcription chain; the bracketed editorial glosses) are unaffected
  and remain disclosed.
- **Round 2 targeted recheck** (`obel_Step0_Doc01_Doc02_Review_
  Round2_Recheck.md`): **substantial revision required, narrowly.** All
  six of Round 1's blocking findings confirmed closed; every quotation
  and locus independently re-verified and found correct. Against this
  document specifically: the bracketed-gloss count corrected from
  "roughly ninety" (a byte-versus-character measurement artifact) to
  116; the former §15 and §16 (a pointer section, and the escalation
  check) found to still carry revision-bookkeeping framing; §0's "this
  session vendored two files" phrasing, and the holdings-disposition
  section's claim that `python -m engine.m9.cli holdings obel` "was run
  this session" (which, in this checkout, raises `FileNotFoundError`
  rather than producing a report) found to be inaccurate as printed,
  though the figures themselves were independently confirmed correct.
- **Round 3 revision**, 2026-09-25, this build thread. The gloss count
  corrected to 116 (§7); the former §15 merged into §14 and the remaining
  sections renumbered; §0's phrasing corrected to a plain statement of
  what is vendored; §5 corrected to state the actual, current holdings
  figures (224 vendored files fleet-wide after merging `origin/main`, 2 +
  98 + 124 = 224) and how they were obtained, rather than a claim this
  checkout cannot reproduce; the "Built from" block's `corpus_index.py`
  invocation corrected to the command actually run. A transcription
  convention (silent OCR repair and smart-quote normalization in
  quotations, disclosed once) is added at §7.
- **Approved to proceed.** The full disposition record — the review
  artifacts it rests on, the one item that waits, and who applied it —
  is at `Open_Gaps_Tracking.md` entry 18. Not Frozen; nothing here is
  closed.
```


## Doc_02, other passages reworded (old text only)

```text
**Built together with:** `obel_Source_Registry.md` (the Registry — the
same pass, per the Source Registry Template V1.0's own instruction not to
build these as two separate steps).

**Built from:** `Doc_01_World_Identification_Boundaries_Orientation.md`;
`worlds/_cross-world/dossiers/the-old-believers_Source_Readiness_
Dossier.md`; `cic/corpus-map/the-old-believers.yaml`; the fleet-wide
holdings figures at §5 below, derived as stated there since
`python -m engine.m9.cli holdings obel` itself cannot run until
`records/obel/` exists; `python cic/engine/corpus_index.py --build`
followed by `python cic/engine/corpus_index.py "<query>" --entry
the-old-believers` searches; `reference/method/CiC_Record_Native_World_
Build_Process_V1.8.md`; `cic/texts/INTAKE.md`'s 2026-09-25 ruling; and
this world's own two vendored files, read in full.


=====
Primary evidence in its own right, per INTAKE.md's own real rule; two
   real quotability caveats independent of language remain (§7).
=====
- The Russian witness, at the equivalent point, has Avvakum say the
  opposite about the same sentence: "По благословению отца моего старца
  Епифания **писано моею рукою грешною** протопопа Аввакума" — "by the
  blessing of my father the elder Epiphanius, **written by my own sinful
  hand**, [I,] the archpriest Avvakum."
=====
| The Creed-wording dispute: "It were better in the Creed not to pronounce the word Lord... for in that name is contained the essence of God" | p. 34 |
=====
not independently re-checked this session), and are not
=====
`cic/corpus-map/the-old-believers.yaml` (generated this session,
`corpus_map_merge.py --write-only avvakum`, `--check` clean) carries two
rows, both `role: tradition`, `confidence: assigned`, for the two
vendored files. Both rows carry `source_file`, `role`, and `confidence`
per the corpus-map schema as `corpus_map_merge.py` actually emits it
today (its own `_KEEP` tuple: `work, author, source_file, locus, role,
confidence, note`).

Own-voice/opponent-voice discipline is demonstrated directly in this
document's own prose (§1.1's table), not in the corpus-map YAML's own row
fields: `row_id` and `voice_of` are real, named, in-progress schema
fields (per `cic/corpus-map/fixture-synthetic.yaml`'s own header,
"CM-1/CM-2/CM-4/CM-8") that no real world's own bucket carries yet,
proven so far only against synthetic fixture data by a separate
corpus-map thread. This is a fleet-wide tooling state, not specific to
this world, logged at `Open_Gaps_Tracking.md` entry 9.


=====
independently verified against a primary source this pass.
=====
`python -m engine.m9.cli holdings obel` runs directly against this
world's own vendored files: 224 vendored files fleet-wide (186 `.txt` +
38 `.xml`), of which this world's own two files both show `no coverage
entry`: they are not yet in the hand-maintained COVERAGE table
`engine/m1/cross_world.py` reads from, a real, separate, pre-existing
table this world was never added to (it predates this world's own
corpus-map bucket). Whether that omission should be treated as a defect
to fix now or a gap to log and defer is a judgment call logged at
`Open_Gaps_Tracking.md` for the coach thread or whoever owns that table
to resolve, since the module's own disclosed practice elsewhere in the
fleet treats a missing COVERAGE key as a defect to be corrected rather
than an accepted gap.

For the record, the arithmetic is correct: 2 (`by design`) + 98 (`out of
window`) + 124 (`no coverage entry`) = 224.


=====
**Transcription convention, stated once for every quotation drawn from
either vendored witness in this world's documents:** the English
1924 printing's OCR carries stray hyphens at line-wraps, `zs` for `is`
in at least one place, and British punctuation printed outside the
closing quotation mark; a quotation presented here as verbatim silently
repairs OCR artifacts of that kind and normalizes typographic ("smart")
quotation marks to plain ones, while changing no word. The Russian
Wikisource transcription's own bracketed editorial variant readings
(distinct from the modern-editorial glosses below) are carried through
exactly as the file prints them wherever a quotation does not need to
cross one. This convention governs every quotation in this document,
Doc_01, Step 0 and the Source Registry; it is not restated at each one.


=====
**How this document uses the two witnesses:** per INTAKE.md's own real,
current rule (Mark's ruling, 2026-09-25) — language does not decide
whether a source is primary; credibility and truth do — both vendored

=====
(see `Open_Gaps_Tracking.md` for the disclosed naming
  exception — not renamed this pass, since a rename touches every
  reference to it).
=====
`cic/corpus-map/PAIRS.yaml` was not modified this
pass; no pairing candidate
=====
Not consulted this pass.
=====
but was not
  successfully downloaded this session (a Wikimedia Commons fetch
  returned HTTP 429, a rate-limit, not a rights or existence problem) —
  a live lead, not closed.
=====
The census's own `floorNote`/`statusDescription` state an absolute — "no
question of doctrine arises here at all" — that this world's own vendored
primary source contradicts at p. 34 (§1.1; Doc_01 §9). Correcting the
census is portfolio-level, not this world's. It is registered at
`Open_Gaps_Tracking.md` entry 11 and in
`worlds/_cross-world/NEEDS-RULING.md`.
```


## Source Registry, Document log

```text
## Document log

- **Round 1 draft**, 2026-09-25, this build thread, together with Doc_02.
- **Round 1 independent review** (`obel_Step0_Doc01_Doc02_Review_
  Round1.md`): confidence tiers systematically misapplied in five of nine
  rows (R2, R5-R9 — a tradition/genre-level tier, D, used where the
  Template's own definitions call for B or C on a named, specific work);
  R2's Confidence cell held prose rather than a plain letter; the header
  named a nonexistent companion filename; the Pomorian Answers (R7) were
  misattributed to Semyon Denisov alone, an attribution the census does
  not state; the bracketed editorial glosses in the Russian file (R2)
  were undisclosed; and this file's own footer asserted no other
  same-lane world exists, which is false.
- **Round 2 revision**, 2026-09-25, this build thread. All tiers
  corrected to the Template's own printed definitions (R2, R5 → C; R6-R9
  → B); the header's companion filename corrected; R7's authorship
  corrected to Andrei Denisov, with Trifon Petrov and Semyon Denisov as
  participants; the bracketed-glosses hazard disclosed at R2; the footer
  corrected to name `cappadocian-nicene-pastoral-monastic-tradition`
  directly and confirm no overlap. This same revision also (at the time,
  apparently correctly) withdrew R2's license for the plain-speech
  declaration and restricted the whole row to second-witness status, on
  the finding that the 2026-09-25 INTAKE.md ruling was not present in
  this checkout.
- **Correction-of-a-correction, 2026-09-25, this build thread, following
  the coordinator's own direct check.** This worktree's checkout had
  branched from a stale local `main`, roughly 150 commits behind real
  `origin/main`. The 2026-09-25 INTAKE.md ruling was already merged to
  real `origin/main` hours before this build thread started; the
  citation was not fabricated, only unreadable from this stale checkout.
  After merging `origin/main` (commit `169dc5cb`) and independently
  re-reading the real, current `INTAKE.md`, R2's license for the
  plain-speech declaration and its primary-evidence status are restored.
  The row's own genuine, disclosed quotability caveats (the unverified
  transcription chain; the bracketed editorial glosses) are unaffected by
  this reversal and remain in force. Full account at `Doc_01` §13,
  `Doc_02` §16, and `Open_Gaps_Tracking.md` entries 12 and 17.
- **Round 2 targeted recheck** (`obel_Step0_Doc01_Doc02_Review_
  Round2_Recheck.md`): every quotation and locus re-verified and found
  correct; the bracketed-gloss count corrected from "roughly ninety" to
  116 (a byte-versus-character measurement artifact in the original
  count); R1's Verification Note found to carry a dangling
  cross-reference ("see R-note below," naming nothing); and this file
  found, on its own account, to carry more revision-history narration in
  its header, status line, a self-justifying "Living-document protocol"
  paragraph, and eight of nine rows than the Round 1 review had found and
  asked removed — the opposite of the intended direction.
- **Round 3 revision**, 2026-09-25, this build thread. All
  "corrected Round N, Finding N — an earlier draft said X" narration
  removed from the header, status line, every row, and the footer; the
  "Living-document protocol" paragraph (which argued this file's own
  exemption from the Template's append-only rule to a reviewer) removed
  — its practical effect (in-place correction of a row's own prior
  misreading, disclosed via a Document Log rather than a new row) is
  simply what this Round 3 revision does, without the file arguing its
  own case. That revision history now lives entirely in this Document
  Log and in `Open_Gaps_Tracking.md`, per `CLAUDE.md`'s own rule for
  `worlds/`. R1's dangling "see R-note below" is removed.
- **Approved to proceed.** The full disposition record — the review
  artifacts it rests on, the one item that waits, and who applied it —
  is at `Open_Gaps_Tracking.md` entry 18. Not Frozen; nothing here is
  closed.
```


## Source Registry, former header and footer

```text
# Source Registry — The Old Believers (obel)

**Companion to Doc_02** (`Doc_02_Source_Ecology.md`), built together with
it in one pass per the Source Registry Template V1.0
(`reference/L3B-World-Build-Methodology/Source_Registry_Template.md`).
Boundary checked against this world's own Doc_01
(`Doc_01_World_Identification_Boundaries_Orientation.md`): 1666-1815;
central/northern Muscovite Russia and Siberia; Russian and Church
Slavonic; a ritual-and-textual (not doctrinal) schism (Doc_01 §9), strand
determination not yet decided (Doc_01 §6).

**Status: Approved to proceed.** One named item waits — Doc_02 §15.

---


...
**No Excluded entries this pass.** No cross-world comparandum risk was
identified against this world's own figures, texts, or controversy:
`cappadocian-nicene-pastoral-monastic-tradition` is a real, Built & Live
world whose lane string matches exactly ("Greek East & Orthodoxy"), and
`imperial-juridical-christianity` is Built & Live on a lane that
half-overlaps it — neither shares a figure, text, or controversy with
this world's own Registry rows (see Doc_02 §8).

**Checkpoint confirmed:** every claim in Doc_01 and Doc_02 that names a
specific source traces to a row above. No claim rests on an unregistered
source.

---
```


## Corpus-map staging note, Russian file (replaced by present-tense text)

```text
    note: >
      The same autobiography in its own original language. This world's own
      primary evidence in its own right, per INTAKE.md's real, current rule
      (Mark's ruling, 2026-09-25): language does not decide whether a source is
      primary, credibility and truth do. CORRECTED 2026-09-25 (independent review
      Findings 2/3/13): an earlier version of this note cited this same ruling but
      could not verify it in this build thread's checkout at that time, and was
      walked back to second-witness-only under INTAKE.md's older 2026-09-02
      framing. CORRECTION-OF-A-CORRECTION 2026-09-25 (following the coordinator's
      own direct check): that walk-back was itself wrong - the build thread's
      checkout was stale (merge-base 41afa0f8, ~150 commits behind real
      origin/main), and the 2026-09-25 ruling was real and already merged to real
      origin/main. After merging origin/main (commit 169dc5cb) and independently
      re-reading the real INTAKE.md, primary-evidence status is restored here.
      Two real quotability caveats remain, independent of that question: this file
      carries 116 bracketed modern-Russian editorial glosses
      interpolated into the running text - strip before quoting - and this
      transcription's own chain from manuscript to critical edition to az.lib.ru
      to Wikisource has not been independently verified hop by hop (az.lib.ru
      itself was unreachable from this session). Quotability flag: primary
      evidence in its own right; verbatim-ready where clean of the bracketed
      glosses, second-witness cross-check elsewhere. See this world's Doc_02 and
      Open_Gaps_Tracking.md.
```


## Source Readiness Dossier, header and section 5 before cleanup

```text
# Source Readiness Dossier — The Old Believers

See `worlds/_cross-world/SOURCE-READINESS.md` for what this is and why it
exists.

**Atlas ID:** VII.7
**Corpus-map slug:** the-old-believers (census id; matches
`cic-website/data/world-census.json`'s own `id` field)
**Time window:** 1666-1815
**Region(s):** Russian north, Siberia (North Europe, per the census's own
`regions`)
**Dossier author / date:** Claude, obel library-stage source-research pass,
2026-09-25
**Corpus-map / `cic/texts/` state as of:** 2026-09-25, this same pass (no
prior Old Believer/Avvakum material existed in either before this pass —
independently re-checked directly this pass, by title/author scan of
`cic/corpus-map/WORKS.yaml` and `AUTHOR-IDS.yaml`, §2 below.
**Corrected, Round 2 (independent review Finding 27): an earlier draft
of this line attributed this finding to `CLAUDE.md`'s "Scaling the
build" section, which does not in fact record anything about Old
Believer or Avvakum material** — that section discusses proactive
source acquisition in general terms, not this world specifically. The
finding itself is unaffected; only its citation was wrong, now removed.)


...
## 5. Open cross-world questions

- None specific to another sibling world's own territory. **Corrected,
  Round 2 (independent review Finding 9): an earlier draft of this line,
  and of §2 above, implied no other Greek East/Orthodoxy-lane world
  exists in this fleet.** One does:
  `cappadocian-nicene-pastoral-monastic-tradition` is Built & Live in the
  same lane. Checked directly against it this revision: fourth-century
  Cappadocia's own Trinitarian-doctrinal formation register, its
  different century, empire, and language, and the absence of any
  figure, text, or controversy shared with this world, together support
  no plausible overlap — the same conclusion an earlier draft reached
  without actually naming or checking against the one real comparandum
  that exists. If a later Greek-East or Balkan Orthodox world's own
  research turns up Nikon-era Greek-authority material (the Greek
  patriarchs whose approval Nikon cited), that would be the first
  genuine cross-link — flag it back here if found.
```


## Open_Gaps_Tracking.md wording changes

Bare cross-references were given a subject and a date on the same line, for example "see entry 7's own" became "see the 2026-09-25 V1.8 merge-state entry's own", "(PR #594)" became "(PR 594, 2026-09-25)" and "`#591`/`#594`/`#595`" became "PRs 591, 594 and 595 (2026-09-25)". No entry's meaning changed.
