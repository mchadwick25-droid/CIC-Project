# lpc handoff check 8: quote triage (2026-09-30)

Report only. Nothing in the world's documents, `engine/` or `cic/` was edited. Scope: every `quotes-unverified` and `quotes-unbalanced` finding that `python -m engine.m10.cli handoff lpc` raises on `Step0_Movement_Scope_Confirmation.md`, `Doc_01_World_Identification_Boundaries_Orientation.md`, `Doc_02_Source_Ecology.md` and `Source_Registry.md`.

## Basis and counts

- Checked against HEAD `1cc67e911` (2026-09-30, working tree clean). A fresh run of `check_quotes` gives **212 `quotes-unverified` + 2 `quotes-unbalanced` = 214 findings**, not 215 + 2: commits `377070249` and `2627d1d36` edited Step 0 and Doc_01 after the earlier output, so 6 findings went away and 3 new ones appeared in Step 0 (rows 212-214 below). The table lists the 214.
- Line numbers: the line of the document where the quotation starts, at that HEAD. For a `.docx` the number is the paragraph in the text of `word/document.xml` (one line per `w:p`, empty paragraphs kept), so paragraph N is the Nth `<w:p>`.
- Method: each quotation was re-derived with `engine.m10.quotes.extract_quotations`, then searched, with case, punctuation, markup and ellipses set aside, in `cic/texts/`, in every `.md`, `.yaml`, `.json` and `.docx` in the repo, and in the installed `cic-build-cycle` skill. The attributed source named in the paragraph was then opened and compared word by word. Where the quotation has ellipses or brackets, each fragment was located in the named source.

### Count per class

| Class | Meaning | Count |
|---|---|---|
| A | verbatim in a vendored text, checker cannot match | 3 |
| B | from a vendored or project source but not verbatim | 7 |
| C | verbatim from a project document (or corpus-map note, record, installed skill) | 131 |
| D | superseded or unverifiable source | 4 |
| E | not a quotation | 67 |
| U | quotes-unbalanced (not a quotation, a paragraph parity fault) | 2 |
| total | | 214 |

Class C by kind of source:

| Sub-class | Source | Count |
|---|---|---|
| C1 | `Build/reference` Word documents: Constitution V2.2, Construction Framework V7.4, Step 0 Methodology V1.0, Step 0 Conclusion FINAL v2 | 50 |
| C2 | `Build/reference` Markdown (inside the checker pool): `Source_Registry_Template.md` | 2 |
| C3 | installed `cic-build-cycle` skill, outside the repo (repo copy has since been reworded) | 5 |
| C4 | `cic/corpus-map/*.yaml` notes | 30 |
| C5 | other worlds' documents and review files (`Build/worlds/don`, `ijc`, `hal`) | 24 |
| C6 | `records/ijc/source/` built record and `cic/texts/README.md` | 5 |
| C7 | this world's own documents and review files | 15 |

### Count per document

| Document | A | B | C | D | E | U | Total |
|---|---|---|---|---|---|---|---|
| Step0_Movement_Scope_Confirmation.md | 0 | 0 | 59 | 2 | 2 | 0 | 63 |
| Doc_01_World_Identification_Boundaries_Orientation.md | 0 | 3 | 41 | 0 | 7 | 0 | 51 |
| Doc_02_Source_Ecology.md | 1 | 1 | 12 | 0 | 0 | 1 | 15 |
| Source_Registry.md | 2 | 3 | 19 | 2 | 58 | 1 | 85 |
| all | 3 | 7 | 131 | 4 | 67 | 2 | 214 |

Status of the four documents: all four carry "Approved to proceed" (Doc_01 and Step 0 self-disposed 2026-09-01; Doc_02 and Registry 2026-09-12). The Registry note says it was edited after its last review.

## What each class needs in `engine/m10/quotes.py`

How the checker decides (read first):

- A quotation is text between straight `"…"` (only if the paragraph holds an even number of straight marks) or curly `“…”`, at least 5 words, with `*`, backticks and edge punctuation stripped. A paragraph is a run of non-blank lines, so a whole Markdown table is one paragraph.
- Source tiers, in order: `cic/texts/` files named in the paragraph (path, bare filename, or a corpus prefix token such as `npnf104`), files named anywhere in the document, then the files in the world's corpus-map bucket. The first file that matches word for word wins. Only `.txt` and `.xml` are read.
- `cic:<file>:<locus>` is consulted only after a file has already matched, and its regex accepts only `.txt` and `.xml` files. It narrows where the quotation must sit; it never rescues a quotation that failed to match, and it does nothing for a project document.
- Project-document exemption (`_project_texts`): the quotation must be a substring of a `.md` file under `Build/worlds/_cross-world/` or `Build/reference/` (file names containing review, spotcheck, round, verification or history, and `Review-Artifacts/`, are excluded), or of `CLAUDE.md` or `cic-website/data/world-census.json`; this world's own directory and its own dossier are excluded. The test is `_norm(span) in _norm(file)`: lowercase, curly to straight, whitespace collapsed, but punctuation, emphasis marks and brackets kept. Whether the paragraph cites the document does not matter: the pool is global.

| Class | Rule it would need to pass | What that means in practice |
|---|---|---|
| A (rows 64, 81, 88) | Exact match in a `cic/texts` file. | Rows 64 and 88 are editorial endnotes. `TextStore.may_contain` screens on the apparatus-stripped text, so the file is ruled out before `verify_quote_against_notes` runs; an endnote-only quotation can never pass. That is an engine defect, not a document defect. Row 81 needs the quotation reshaped: the speaker label and the source's curly inner quotes sit inside the author's marks. Quote each contiguous run on its own, without the label. |
| B | Exact match after the wording is corrected. | Restore the true wording (given in each row), or mark the omission with an ellipsis or an editorial bracket. Each is an edit to an approved document, so it is a post-disposition correction that must be disclosed in the document and logged in `lpc_Decision_Log.md`. |
| C1 | A `.md` source in the pool. | None of the Word documents is in the pool (`rglob("*.md")`). Without an engine change or Markdown renderings of these five documents under `Build/reference/`, these quotations cannot pass however they are cited. Even with renderings, punctuation and emphasis would have to match character for character. Changing which files count as project documents is a methodology change; ask first. |
| C2 (rows 83, 84) | `_norm` substring of the pool file. | Both fail on formatting only: the template has `speaks *for* —` (emphasis asterisks; the span has them stripped, the file does not) and nested straight quotes where the Registry uses single quotes. Quote the runs around the emphasis separately, or restore the template's double quotes. Row 4 (Constitution Article 29, C1) is also in the pool through `CiC_Pipeline_Decision_Log.md:122` but fails on the editorial bracket `[t]he`. |
| C3 | Same pool rule; the skill is not in the repo. | The installed skill and the repo copy (`Build/reference/method/skills/cic-build-cycle/SKILL.md`) have diverged. The quoted wording is the installed one. The repo copy is in the pool, so a quotation that matched the repo copy would pass. Either quote the repo copy or bring the two copies back into line. |
| C4 | Not in the pool. | Corpus-map notes are only read for their `source_file` assignments (`_bucket_rows`), never for the note text. Cited or not, these never pass. The notes also change: commit `181eb76c6` (2026-09-24) stripped commentary from them (see row 73). |
| C5 | Not in the pool. | Other worlds' documents are outside `_cross-world` and `Build/reference`. Quoting a sibling build at second hand is a fidelity risk in itself; the Registry and Step 0 already cite them at source. |
| C6 | Not in the pool. | `records/` and `cic/texts/README.md` (a `.md`, and `TextStore` reads only `.txt` and `.xml`). |
| C7 | Excluded by design. | This world's own Step 0, Doc_01, Doc_02, Registry, Claims Register, Decision Log and review files are excluded so that one invented quotation repeated across them cannot exempt itself. A self-quotation cannot pass as written. Point to the section without quotation marks, or keep the marks and accept the finding. |
| D | No rule can pass them. | Replace with wording that exists in a live source, or remove the marks and say what is being reported and from where. |
| E | The paragraph must stop looking like a quotation. | Take the quotation marks off titles, labels, hypothetical slogans and scare quotes (italics are not quotation marks, so `*Title*` is safe). No engine change needed. The 55 article and chapter titles in the Registry's bibliography rows are the bulk of this. |
| U (rows 65 and 149: Doc_02 line 120, Registry table) | An even number of straight `"` per paragraph. | Doc_02: the stray mark is the closing `"` of a German `„Vita Pontii"` inside a code span. Registry: stray marks sit in code spans (line 291 lists `"` among punctuation marks) and in German `„…"` quotes; while the table's count is odd, every straight-quote quotation in it is skipped as unchecked, so fixing it will surface more findings. |

## Class B: corrections that touch approved documents

Seven quotations are not verbatim. All sit in documents marked "Approved to proceed"; each correction is an edit to an approved document.

| Row | Document | Claim changed? | What the true wording changes |
|---|---|---|---|
| 12 | Doc_01 line 96 | Nearest to a change | The Step 0 Conclusion says the Constitutional ambiguity was "Checked directly against the Constitution's actual text and found genuinely undefined". Doc_01 cuts that sentence out without an ellipsis, so the quotation no longer shows that the finding was verified. Restoring it strengthens Doc_01's use of the Conclusion; no conclusion in Doc_01 changes. |
| 47 | Doc_01 line 200 | No | "own" dropped from Round 6's "the document's own account of its own authority". |
| 51 | Doc_01 line 202 | No | Word order changed and "between them" dropped from the Conclusion's sentence. |
| 60 | Doc_02 line 38 | No | Doc_01 says "argues", Doc_02 quotes "arguing". |
| 74 | Registry line 38 | No | The corpus map says "Held in Augustine's own entry for want of a better home"; the Registry quotes "held for want of a better home". |
| 87 | Registry line 58 (Letter 185 §25) | No | NPNF has "if they would take the law"; the Registry quotes "to take the law". The only class B item against a vendored text. |
| 103 | Registry line 168 (the Augustine–Cyprian study row) | No | "not fully settled" condenses "does not consider fully settled" (Doc_01 line 180). |

No class B correction changes a claim's substance. The class D items below are closer to it, and row 30 (class C) has a wrong attribution.

## The five most serious class B or D findings

1. **Row 211, Step 0 line 177 (D).** Step 0 §6 quotes the project lead as saying "the old thread that did this is retired". No record of those words exists. The nearest is a paraphrase in `Build/worlds/ijc/Open_Gaps_Tracking.md:123`; `Doc01_Round6_Review.md:184` only re-quotes Step 0. The quotation is what authorises the repair of IJC's boundary breach, and the installed `cic-build-cycle` skill forbids attributing a quotation to the project lead without a checkable record.
2. **Row 73, Registry line 38 (D).** The Registry says the `Soliloquies` corpus-map note is "quoted to its own actual end". It is not: the live note ends at "…for want of a better home." (`latin-pastoral-congregational-christianity.yaml:1356-1358`). The tail exists only in the pre-cleanup file (`git show 181eb76c6^:…yaml`, lines 663-667), and `NEEDS-RULING.md:180` words it differently. A claim of completeness about a source the reader can no longer check.
3. **Row 12, Doc_01 line 96 (B).** Silent removal of the verification clause from a Step 0 Conclusion quotation, quoted in support of a CO-022 escalation label. See the class B table.
4. **Row 91, Registry line 139 (D).** The Registry quotes an earlier ground of exclusion for row 103 (Clark, *Monica*). The row was rewritten; the wording survives only in `Doc02_Round12_Review.md:69`. The Registry is quoting history as if it were the row's current text.
5. **Row 87, Registry line 58 (B).** A changed word inside a quotation from Augustine, Letter 185 §25 ("to take" for "would take"), in a passage built on exactly which legal step the council proposed. Meaning holds; fidelity bar does not.

Also worth acting on, though class C by wording:

- **Row 31, Doc_01 line 162.** "this world's own corpus-map records that Letter 185 … is '[D]irect evidence for the ijc world's core question …'". The note is in IJC's bucket (`imperial-juridical-christianity.yaml:146`), not lpc's. Verbatim, wrongly attributed.
- **Rows 1, 43, 44, 206, 209 (C3).** Five quotations of `cic-build-cycle` are verbatim from the installed skill but not from the repo copy, which was reworded on 2026-09-29. Two sources, one rule, different words.

## Table

Class keys: A, B, C (C1 to C7 as above), D, E, U. Row number is the order of the table, not a line number. The second column is the document; the third is the line of the quotation in it.

| # | Document | Line | First 60 characters | Class | Evidence |
|---|---|---|---|---|---|
| 1 | Doc_01 | 3 | if no escalation category applies, the build thread applies  | C3 | installed cic-build-cycle SKILL.md (outside repo: ~/.claude/skills/synced/…/cic-build-cycle/SKILL.md) line 72 — repo copy Build/reference/method/skills/cic-build-cycle/SKILL.md:123 now reads "applies it without waiting for Mark"; the quoted wording survives in the installed skill, witt_Doc_08_Forces_Document.md:712 and witt_Doc08_Review_Round3.md:112 |
| 2 | Doc_01 | 18 | plausibly the richest ordinary-believer, ordinary-worship, o | C7 | Build/worlds/lpc/Step0_Movement_Scope_Confirmation.md line 97 — own Step 0 §3 B2 |
| 3 | Doc_01 | 20 | Project lead's Article 29 confirmation | E | title of a decision-log entry (Build/worlds/lpc/lpc_Decision_Log.md line 1897) |
| 4 | Doc_01 | 20 | [t]he method of confirmation is governed by the build docume | C1 | Constitution V2.2 docx para 592 — Article 29; same words at Build/reference/L2C-System-Status/CiC_Pipeline_Decision_Log.md:122 (a .md in the checker pool) but the span carries the editorial bracket "[t]he", so the substring test fails |
| 5 | Doc_01 | 26 | Project lead's ruling: Possidius Vita ch. VIII corrects Doc_ | E | title of a decision-log entry (Build/worlds/lpc/lpc_Decision_Log.md line 667) |
| 6 | Doc_01 | 32 | ~97 sermons preached to his own congregations at Hippo and C | C7 | Build/worlds/lpc/Step0_Movement_Scope_Confirmation.md line 87 — own Step 0 §3 B1 |
| 7 | Doc_01 | 86 | a finding, never a presupposed universal schema | C1 | Constitution V2.2 docx para 515 — Article 21 |
| 8 | Doc_01 | 88 | historically developing ecclesial realities shaped, to the d | C1 | Constitution V2.2 docx para 339 — Article 15 |
| 9 | Doc_01 | 90 | once made, governs all subsequent strand attribution | C1 | Constitution V2.2 docx para 516 — Article 21 |
| 10 | Doc_01 | 90 | is made at Step 1 and governs all subsequent work | C1 | Construction Framework V7.4 docx para 117 — Strand Determination entry |
| 11 | Doc_01 | 96 | Constitutional ambiguity flagged, not resolved | C1 | Step 0 Conclusion FINAL v2 docx para 56 — label phrase of the Conclusion's constitutional-ambiguity item |
| 12 | Doc_01 | 96 | Article 3 (Formation-World Principle) requires 'sufficient h | B | Step 0 Conclusion (docx para 56) reads "…or whether it requires continuous, unbroken community existence. Checked directly against the Constitution's actual text and found genuinely undefined. Logged as a standing interpretive question, likely to recur." Doc_01 cuts out the sentence "Checked directly against the Constitution's actual text and found genuinely undefined" with no ellipsis and runs "existence" into "logged as a standing interpretive question" inside one pair of quotation marks. The dropped sentence is the verification basis of the ambiguity finding. |
| 13 | Doc_01 | 96 | Constitutional ambiguity on gapped/diachronic formation-type | C1 | Step 0 Conclusion FINAL v2 docx para 64 — Conclusion item text |
| 14 | Doc_01 | 102 | the Donatists revived Cyprian's own third-century position a | C5 | Build/worlds/don/Step0_Movement_Scope_Confirmation.md line 40 — Donatism Step 0 §2 A2 |
| 15 | Doc_01 | 102 | which mode of pastoral life recurs: ordinary, territorial, s | E | a constructed formulation of "the obvious way to resolve it", put in quotation marks and answered ("does not hold"); no source has these words (only Doc_01 itself) |
| 16 | Doc_01 | 104 | Augustine argues with Cyprian, disputing his ruling while cl | C7 | Build/worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md line 100 — own Doc_01 §5 sentence, quoted by Doc_01 itself; line cited is the original sentence |
| 17 | Doc_01 | 104 | #8's Cyprian is defined by crisis pastoral management within | C5 | Build/worlds/don/Doc_01_World_Identification_Boundaries_Orientation.md line 97 — Donatism Doc_01; also the Coach3 critique at Archive/Syriac-Build-2026-07/CiC_Coach3_Step0_Critique_2026-07-06.md:25 |
| 18 | Doc_01 | 112 | Cyprian as working pastor navigating the Decian persecution  | C1 | Step 0 Conclusion FINAL v2 docx para 20 — World #8 entry |
| 19 | Doc_01 | 114 | In the source it is a parenthesis attached specifically to C | C5 | Build/worlds/don/Review-Artifacts/Step0_Round2_Review.md line 56 — Donatism Step 0 Round 2 review file |
| 20 | Doc_01 | 152 | is not yet built and cannot itself hold the line from its si | C5 | Build/worlds/ijc/Step0_Movement_Scope_Confirmation.md line 118 — IJC Step 0 §4 item 3 |
| 21 | Doc_01 | 152 | the corpus embeds letters by others... under Cyprian's name | C4 | cic/corpus-map/novatianism.yaml line 67 — corpus-map note (the Cyprian *Epistles* entry); same sentence also in cic/corpus-map/cappadocian-nicene-pastoral-monastic-tradition.yaml:137 |
| 22 | Doc_01 | 154 | exercised through office, decretal, and canon law, independe | C5 | Build/worlds/ijc/Doc_01_World_Identification_Boundaries_Orientation.md line 61 — IJC Doc_01 §4 Strand A |
| 23 | Doc_01 | 154 | grounded in a see's political proximity to imperial power, n | C5 | Build/worlds/ijc/Doc_01_World_Identification_Boundaries_Orientation.md line 62 — IJC Doc_01 §4 Strand B |
| 24 | Doc_01 | 154 | a claim about the church's independence from imperial comman | C5 | Build/worlds/ijc/Doc_01_World_Identification_Boundaries_Orientation.md line 63 — IJC Doc_01 §4 Strand C |
| 25 | Doc_01 | 156 | The authority-structure/state-power boundary named in [IJC's | C5 | Build/worlds/ijc/Step0_Movement_Scope_Confirmation.md line 118 — IJC Step 0 §4 item 3; editorial bracket "[IJC's own Step 0]" replaces "§3" context |
| 26 | Doc_01 | 156 | confirmed distinct from world #6 (non-overlapping authority  | C1 | Step 0 Conclusion FINAL v2 docx para 20 — World #8 entry |
| 27 | Doc_01 | 158 | genuine distinctiveness... (formation-logic, authority struc | C1 | Step 0 Conclusion FINAL v2 docx para 10 — two fragments of one sentence joined by an ellipsis |
| 28 | Doc_01 | 158 | independent, temporally-overlapping formations with differen | C1 | Step 0 Conclusion FINAL v2 docx para 10 — Conclusion selection rule |
| 29 | Doc_01 | 162 | this world always solicited state power | E | a slogan the paragraph rejects, in quotation marks (one of three hypothetical one-line characterisations) |
| 30 | Doc_01 | 162 | this world solicited it only once, late | E | a slogan the paragraph rejects, in quotation marks (one of three hypothetical one-line characterisations) |
| 31 | Doc_01 | 162 | [D]irect evidence for the ijc world's core question — the ch | C4 | cic/corpus-map/imperial-juridical-christianity.yaml line 146 — ATTRIBUTION DEFECT: Doc_01 says "this world's own corpus-map records …" but the note is in IJC's bucket (imperial-juridical-christianity.yaml); lpc's bucket has no such note; editorial bracket "[D]irect" |
| 32 | Doc_01 | 162 | Church-State Alliance and Its Limits | E | name of a gravity in IJC Doc_04 (Build/worlds/ijc/Doc_04_Gravity_Discovery.md line 37) |
| 33 | Doc_01 | 162 | the single most load-bearing explanatory claim in [IJC's] en | C5 | Build/worlds/ijc/Doc_04_Gravity_Discovery.md line 44 — IJC Doc_04; "[IJC's]" replaces "this world's" |
| 34 | Doc_01 | 162 | historically developing ecclesial realities shaped, to the d | C1 | Constitution V2.2 docx para 339 — Article 15 |
| 35 | Doc_01 | 162 | never displaced by an assumption that instability must be pr | C1 | Constitution V2.2 docx para 340 — Article 15 |
| 36 | Doc_01 | 163 | charismatic-scholarly and voluntary-aristocratic-patronage-b | C5 | Build/worlds/hal/hal_Doc_01_World_Identification_Boundaries_Orientation.md line 172 — Hieronymian Doc_01 §8.1 |
| 37 | Doc_01 | 163 | drove him from Rome within months with no institutional reco | C5 | Build/worlds/hal/hal_Doc_01_World_Identification_Boundaries_Orientation.md line 172 — Hieronymian Doc_01 §8.1 |
| 38 | Doc_01 | 165 | the largest single thing in this volume after the Confession | C4 | cic/corpus-map/hieronymian-ascetic-literary.yaml line 31 — corpus-map note |
| 39 | Doc_01 | 165 | deliberately - the exchange contains Jerome's own letters, w | C4 | cic/corpus-map/hieronymian-ascetic-literary.yaml line 28 — corpus-map note |
| 40 | Doc_01 | 165 | adjacent worlds may share material | C1 | Construction Framework V7.4 docx para 131 — World Continuity & Distinction |
| 41 | Doc_01 | 167 | pending a validated primary-gravity contrast against world # | C1 | Step 0 Conclusion FINAL v2 docx para 67 — Conclusion, Antiochene hold-out |
| 42 | Doc_01 | 178 | Project lead's Article 29 confirmation | E | title of a decision-log entry (Build/worlds/lpc/lpc_Decision_Log.md line 1897) |
| 43 | Doc_01 | 190 | has cleared an independent review without that review callin | C3 | installed cic-build-cycle SKILL.md (outside repo: ~/.claude/skills/synced/…/cic-build-cycle/SKILL.md) line 67 — repo copy SKILL.md now reads "eligible only after an independent review that calls for no substantial revision" (around line 118); quoted wording survives in the installed skill and in Step0_Round5_Review.md:21 |
| 44 | Doc_01 | 190 | If no escalation category applies, the build thread applies  | C3 | installed cic-build-cycle SKILL.md (outside repo: ~/.claude/skills/synced/…/cic-build-cycle/SKILL.md) line 72 — repo copy reworded ("applies it without waiting for Mark") |
| 45 | Doc_01 | 194 | confirmed distinct from world #6 (non-overlapping authority  | C1 | Step 0 Conclusion FINAL v2 docx para 20 — World #8 entry |
| 46 | Doc_01 | 194 | Constitutional ambiguity flagged, not resolved | C1 | Step 0 Conclusion FINAL v2 docx para 56 — label phrase |
| 47 | Doc_01 | 200 | on the document's account of its own authority, an escalatio | B | Round 6 review reads "on the document's own account of its own authority, an escalation category applies and self-disposition is unavailable" (Review-Artifacts/Doc01_Round6_Review.md:73); Doc_01 drops the word "own" inside quotation marks. Meaning unchanged. |
| 48 | Doc_01 | 200 | the honest course, since I can find no reason to withdraw it | C7 | Build/worlds/lpc/Review-Artifacts/Doc01_Round6_Review.md line 218 — own Round 6 review (review file, not a primary document) |
| 49 | Doc_01 | 200 | in Round 7's favour more directly than either round argued | C7 | Build/worlds/lpc/Review-Artifacts/Doc01_Round8_Review.md line 98 — own Round 8 review |
| 50 | Doc_01 | 200 | a ground neither round gave | C7 | Build/worlds/lpc/Review-Artifacts/Doc01_Round8_Review.md line 98 — own Round 8 review |
| 51 | Doc_01 | 202 | confirmed [Cyprian and Augustine] to hold together despite t | B | Step 0 Conclusion reads "Cyprian and Augustine confirmed to hold together despite the roughly century-long gap between them (with Donatism occupying and contesting the interval)". Doc_01 moves "confirmed" in front, substitutes a bracket, and drops "between them" without an ellipsis. Meaning unchanged. |
| 52 | Doc_02 | 23 | is the census's home for that tradition | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 2241 — corpus-map note |
| 53 | Doc_02 | 23 | because the entry choice is inferred from region and date —  | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 2242 — corpus-map note |
| 54 | Doc_02 | 23 | Assigned twice with different roles, deliberately (worker br | C4 | cic/corpus-map/donatism.yaml line 713 — corpus-map note (Donatism bucket, Optatus entry) |
| 55 | Doc_02 | 25 | Donatism is included as shared ancestry rather than heresiol | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 1519 — corpus-map note (Council-of-Carthage entry), two fragments joined by an ellipsis |
| 56 | Doc_02 | 25 | what remains open is the Optatus placement question... and t | C7 | Build/worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md line 166 — own Doc_01 §7 (World #4 bullet), three fragments joined by ellipses |
| 57 | Doc_02 | 27 | the direct root of the Carthaginian congregational tradition | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 2320 — corpus-map note |
| 58 | Doc_02 | 27 | without Tertullian himself being this world's own voice | C7 | Build/worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md line 146 — own Doc_01 §8 item 5 (line cited is the original sentence) |
| 59 | Doc_02 | 37 | let it pass silently a second time | C7 | Build/worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md line 175 — own Doc_01 §8 item 5 |
| 60 | Doc_02 | 38 | arguing with Cyprian, disputing his ruling while claiming hi | B | Doc_02 says Doc_01 §5 records Augustine "arguing with Cyprian, …". Doc_01 line 100 reads "Augustine argues *with* Cyprian, disputing his ruling while claiming his communion" (repeated at line 104). "arguing" appears only in Doc_04_Gravity_Discovery.md:56, which itself quotes it as Doc_02 §2. One word form changed inside quotation marks; meaning unchanged. |
| 61 | Doc_02 | 45 | what the ordinary Latin pastoral bishop of this period was l | C7 | Build/worlds/lpc/lpc_Claims_Register.md line 62 — own Claims Register |
| 62 | Doc_02 | 54 | often counted the earliest Christian biography | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 2382 — corpus-map note |
| 63 | Doc_02 | 95 | how deeply that substrate culture shaped ordinary congregati | C7 | Build/worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md line 35 — own Doc_01 §2; ellipsis legitimately drops a parenthetical (as against the literate, Latin-trained episcopal voice …) |
| 64 | Doc_02 | 107 | of historical value, as embodying the rules of nunneries bel | A | npnf101_augustine-confessions-letters.xml lines 54746-54747: the editorial endnote n. 2922 to Letter 211 ("This letter is of historical value, as embodying the rules of nunneries belonging to the Augustinian orders."). Verbatim. The checker cannot reach it: TextStore.may_contain() screens on the apparatus-stripped text, so the endnote-only wording fails the screen and verify_quote_against_notes() is never run. |
| 65 | Doc_02 | 120 | (unbalanced quotation marks) | U | Doc_02 line 120: seven straight quotation marks in the paragraph (odd). The stray one is the closing mark of a German quote, `„Vita Pontii"` (line 120, column 2342), inside a code span. |
| 66 | Doc_02 | 133 | Not currently licensed for a specific claim | C7 | Build/worlds/lpc/Source_Registry.md line 38 — own Source Registry row 38 "Licensed For" (line 51) |
| 67 | Registry | 6 | row N sits physically after rows X–Y | E | an example of the wording of a claim ("Any claim of the form …"), not a quotation |
| 68 | Registry | 18 | dependent on Tertullian's De Oratione | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 1933 — corpus-map note |
| 69 | Registry | 23 | the exchange contains Jerome's own letters... and Augustine' | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 718 — corpus-map note (Augustine–Jerome entry; also hieronymian yaml); two fragments joined by an ellipsis |
| 70 | Registry | 25 | also assigned to imperial-juridical-christianity below | C4 | cic/corpus-map/donatism.yaml line 380 — corpus-map note; same note also in the lpc bucket |
| 71 | Registry | 28 | written for the Carthaginian deacon Deogratias... as near th | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 992 — corpus-map note; two fragments joined by an ellipsis |
| 72 | Registry | 36 | Not addressed to Pelagians... Victor was no Pelagian. The do | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 1186 — corpus-map note (On the Soul and its Origin); two fragments joined by an ellipsis |
| 73 | Registry | 38 | a philosophical dialogue, not pastoral work from Hippo. Held | D | Registry says "quoted to its own actual end". The live note (cic/corpus-map/latin-pastoral-congregational-christianity.yaml:1356-1358) ends at "…for want of a better home." The tail ("the doubt worth a reviewer's eye is whether the Cassiciacum period should also touch ambrosian-milan-standalone, which is Ambrose's entry, not Augustine's — not asserted here") is verbatim only in the pre-cleanup file (git show 181eb76c6^:cic/corpus-map/latin-pastoral-congregational-christianity.yaml, lines 663-667; commentary stripped 2026-09-24 by commits 181eb76c6 / a9b11a4f0). NEEDS-RULING.md:180 (in the checker pool) has a differently worded tail. |
| 74 | Registry | 38 | held for want of a better home | B | Corpus-map note (latin-pastoral-congregational-christianity.yaml:1356-1358, Soliloquies) reads "Held in Augustine's own entry for want of a better home." The Registry quotes "held for want of a better home", dropping "in Augustine's own entry" with no ellipsis. Meaning unchanged. |
| 75 | Registry | 40 | Mark may prefer another Latin home for a Numidian polemicist | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 2243 — corpus-map note |
| 76 | Registry | 40 | Assigned twice with different roles, deliberately (worker br | C4 | cic/corpus-map/donatism.yaml line 713 — corpus-map note |
| 77 | Registry | 41 | predates the entry's c. 240s start | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 2322 — corpus-map note |
| 78 | Registry | 41 | the direct root of the Carthaginian congregational tradition | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 2320 — corpus-map note |
| 79 | Registry | 42 | without Tertullian himself being this world's own voice | C7 | Build/worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md line 146 — own Doc_01 §8 item 5 |
| 80 | Registry | 56 | Donatism is included as shared ancestry rather than heresiol | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 1519 — corpus-map note, two fragments joined by an ellipsis |
| 81 | Registry | 56 | Zonaras remarks: '...In it moreover above eighty-four bishop | A | npnf214_seven-ecumenical-councils.xml lines 37650-37658, Introductory Note (div3 xv.vi.ii): Zonaras remarks: “This is the most ancient of all the synods … In it moreover above eighty-four bishops were gathered together”. Verbatim, with the Registry's ellipses. The checker stops at the segment "Zonaras remarks: '" (straight apostrophe against the source's curly opening quote; the speaker label is inside the marks). |
| 82 | Registry | 56 | the sententiae of the 87 bishops | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 1518 — corpus-map note |
| 83 | Registry | 57 | assessed by what the source speaks for — its own subject, tr | C2 | Build/reference/L3B-World-Build-Methodology/Source_Registry_Template.md line 50 — IN the checker pool (Build/reference .md). Fails only on formatting: the template has "speaks *for* —" with emphasis asterisks (extract_quotations strips * from the span, not from the file) |
| 84 | Registry | 57 | the question this check asks is never 'does another world al | C2 | Build/reference/L3B-World-Build-Methodology/Source_Registry_Template.md line 52 — IN the checker pool. Fails only on formatting: the template has nested straight double quotes ("does another world already have this") where the Registry has single quotes |
| 85 | Registry | 57 | this step governs a single world's own Registry only. Checki | C1 | Construction Framework V7.4 docx para 626 — Step 2 scope note, two fragments joined by an ellipsis |
| 86 | Registry | 58 | all resolved to the same wrong volume … or were rejected on  | C5 | Build/worlds/don/Source_Registry.md line 27 — Donatism Registry row 16; two fragments joined by an ellipsis |
| 87 | Registry | 58 | to take the law which Theodosius, of pious memory, enacted g | B | Augustine, Letter 185 §25 (npnf104_augustine-anti-manichaean-anti-donatist.xml line 19625; the page break <pb n="643"/> falls just before): "…if they would take the law which Theodosius, of pious memory, enacted generally against heretics of all kinds, to the effect that any heretical bishop or clergyman, being found in any place, should be fined ten pounds of gold, and confirm it in more express terms against the Donatists, who denied that they were heretics…". The Registry opens its quotation with "to take", the source has "would take". One word changed inside quotation marks; meaning unchanged. |
| 88 | Registry | 58 | held June 26 (more correctly, probably June 15th or 16th), 4 | A | npnf104_augustine-anti-manichaean-anti-donatist.xml line 19631: NPNF endnote n. 2521 "That of Carthage, held June 26 (more correctly, probably June 15th or 16th), 401." Verbatim. Same checker path failure as row 63 (endnote text removed before the may_contain screen). |
| 89 | Registry | 65 | every named work is dispositioned — rowed, or excluded with  | C1 | Construction Framework V7.4 docx para 628 — Doc_02 review requirement |
| 90 | Registry | 135 | written by a deacon with every personal and institutional re | C7 | Build/worlds/lpc/Doc_02_Source_Ecology.md line 81 — own Doc_02 §2 / §4 Author Gravity assessment (line cited is the original) |
| 91 | Registry | 139 | outside this world's own Carthage/Hippo congregational-life  | D | Quotes an earlier wording of Registry row 103 (Clark, Monica; line 139): "Monica's own formation and most of her life lie outside this world's own Carthage/Hippo congregational-life focus". The row has since been rewritten (now "Native, unlicensed"). The earlier wording survives only in Review-Artifacts/Doc02_Round12_Review.md:69 (quoting row 103 as it then stood). |
| 92 | Registry | 150 | A Note on the Interpretation of the Parable of the Threshing | E | bibliographic title of a modern article or chapter in a Registry row |
| 93 | Registry | 151 | Heresy and Schism according to Cyprian of Carthage | E | bibliographic title of a modern article or chapter in a Registry row |
| 94 | Registry | 152 | Episcopal Elections in Cyprian: Clerical and Lay Participati | E | bibliographic title of a modern article or chapter in a Registry row |
| 95 | Registry | 156 | The Metamorphosis of Sodom: The Ps.-Cyprian De Sodoma as an  | E | bibliographic title of a modern article or chapter in a Registry row |
| 96 | Registry | 157 | Peregrinatio and Peregrini in Augustine's City of God | E | bibliographic title of a modern article or chapter in a Registry row |
| 97 | Registry | 161 | Ad Quirinum Book Three and Cyprian's Catechumenate | E | bibliographic title of a modern article or chapter in a Registry row |
| 98 | Registry | 162 | Situating and Studying Augustine's Sermons | E | bibliographic title of a modern article or chapter in a Registry row |
| 99 | Registry | 163 | Valerius of Hippo: A Profile | E | bibliographic title of a modern article or chapter in a Registry row |
| 100 | Registry | 164 | Augustine and the Significance of Perpetua's Words: 'And I W | E | bibliographic title of a modern article or chapter in a Registry row |
| 101 | Registry | 165 | Les manuscrits des sermons de saint Augustin utilisés par le | E | bibliographic title of a modern article or chapter in a Registry row |
| 102 | Registry | 166 | Les interpolations dans le traité de S. Cyprien sur l'Unité  | E | bibliographic title of a modern article or chapter in a Registry row |
| 103 | Registry | 168 | real, substantial differences… not fully settled | B | Doc_01 §8 item 10 (Doc_01 line 180) says the differences are "real, substantial differences this document argues do not clearly touch this world's own formation-relevant ground, but does not consider fully settled". "not fully settled" is a condensation of "does not consider fully settled", not a verbatim run. |
| 104 | Registry | 174 | Les églises doubles et les familles d'églises | E | bibliographic title of a modern article or chapter in a Registry row |
| 105 | Registry | 175 | Navigating the Vast Tradition of St. Augustine's Sermons: Ol | E | bibliographic title of a modern article or chapter in a Registry row |
| 106 | Registry | 176 | Was There 'Augustinian' Concupiscence in Pre-Augustinian Nor | E | bibliographic title of a modern article or chapter in a Registry row |
| 107 | Registry | 177 | Legimus supra magistrum non esse discipulum: Pope Celestine  | E | bibliographic title of a modern article or chapter in a Registry row |
| 108 | Registry | 178 | La notion de prochain d'Augustin au début de son épiscopat:  | E | bibliographic title of a modern article or chapter in a Registry row |
| 109 | Registry | 180 | Christianity and Paganism, IV: North Africa | E | bibliographic title of a modern article or chapter in a Registry row |
| 110 | Registry | 180 | Surrounding cultural and religious environment | E | label of a Doc_02 §5 bullet ("Surrounding cultural and religious environment"), Doc_02 line 93 (Build/worlds/lpc/Doc_02_Source_Ecology.md line 96) |
| 111 | Registry | 182 | Augustine's Eucharistic Spirituality in his Easter Sermons | E | bibliographic title of a modern article or chapter in a Registry row |
| 112 | Registry | 187 | Augustine's Appropriation of Cyprian's Unitive Tropes from D | E | bibliographic title of a modern article or chapter in a Registry row |
| 113 | Registry | 188 | Orthodoxy, Heresy and Episcopal Authority in the Third-Centu | E | bibliographic title of a modern article or chapter in a Registry row |
| 114 | Registry | 189 | Penance and Ecclesial Purity: The Divine Urgency Behind Cypr | E | bibliographic title of a modern article or chapter in a Registry row |
| 115 | Registry | 190 | A Late Antique Preacher in Action: Augustine, Ep. 29 | E | bibliographic title of a modern article or chapter in a Registry row |
| 116 | Registry | 191 | Augustine and Men of Imperial Power | E | bibliographic title of a modern article or chapter in a Registry row |
| 117 | Registry | 192 | Das Bischofsmartyrium als Stellvertretung bei Cyprian von Ka | E | bibliographic title of a modern article or chapter in a Registry row |
| 118 | Registry | 193 | The education and (self-)affirmation of (recent or potential | E | bibliographic title of a modern article or chapter in a Registry row |
| 119 | Registry | 195 | A Note on the Vandal Occupation of Hippo Regius | E | bibliographic title of a modern article or chapter in a Registry row |
| 120 | Registry | 196 | Local Cultures in the Roman Empire: Libyan, Punic and Latin  | E | bibliographic title of a modern article or chapter in a Registry row |
| 121 | Registry | 197 | Pastoral lessons from Augustine's theological correspondence | E | bibliographic title of a modern article or chapter in a Registry row |
| 122 | Registry | 198 | St. Cyprian and the Reconciliation of Apostates | E | bibliographic title of a modern article or chapter in a Registry row |
| 123 | Registry | 199 | Cyprianic Ecclesiology: Redefining the Office of the Christi | E | bibliographic title of a modern article or chapter in a Registry row |
| 124 | Registry | 203 | L'Humanité vue d'en haut (Cyprien, Ad Donatum, 6–13) | E | bibliographic title of a modern article or chapter in a Registry row |
| 125 | Registry | 204 | 'As far as my poor memory suggested': Cyprian's compilation  | E | bibliographic title of a modern article or chapter in a Registry row |
| 126 | Registry | 205 | The Procedure of St. Cyprian's Synods | E | bibliographic title of a modern article or chapter in a Registry row |
| 127 | Registry | 206 | The young Augustine's knowledge of Manichaeism: An analysis  | E | bibliographic title of a modern article or chapter in a Registry row |
| 128 | Registry | 207 | Cyprian's Early Career in the Church of Carthage | E | bibliographic title of a modern article or chapter in a Registry row |
| 129 | Registry | 208 | The White Crown of Works: Cyprian's Early Pastoral Ministry  | E | bibliographic title of a modern article or chapter in a Registry row |
| 130 | Registry | 209 | The Secular Profession of St Cyprian of Carthage | E | bibliographic title of a modern article or chapter in a Registry row |
| 131 | Registry | 210 | Cyprien d'Antioche et Cyprien de Carthage | E | bibliographic title of a modern article or chapter in a Registry row |
| 132 | Registry | 211 | Reading Psalm 4 to the Manichaeans | E | bibliographic title of a modern article or chapter in a Registry row |
| 133 | Registry | 212 | Preaching Adam in John Chrysostom and Augustine of Hippo | E | bibliographic title of a modern article or chapter in a Registry row |
| 134 | Registry | 219 | Original Sin in Tertullian and Cyprian: Conceptual Presence  | E | bibliographic title of a modern article or chapter in a Registry row |
| 135 | Registry | 220 | Possidius et les 'Confessions' de saint Augustin | E | bibliographic title of a modern article or chapter in a Registry row |
| 136 | Registry | 221 | Notables et chrétiens: les enseignements des Lettres de Cypr | E | bibliographic title of a modern article or chapter in a Registry row |
| 137 | Registry | 222 | 'The very deceitfulness of devils': Firmilian and the doubtf | E | bibliographic title of a modern article or chapter in a Registry row |
| 138 | Registry | 223 | L'ontologie de l'Église selon saint Cyprien | E | bibliographic title of a modern article or chapter in a Registry row |
| 139 | Registry | 224 | Sur une page de saint Cyprien chez saint Ambroise. Hexameron | E | bibliographic title of a modern article or chapter in a Registry row |
| 140 | Registry | 225 | Agostino celebra i martiri Scillitani: il sermo 299/D | E | bibliographic title of a modern article or chapter in a Registry row |
| 141 | Registry | 226 | Πρῶτος τῶν τότε Κυπριανός. Cipriano di Cartagine in Oriente | E | bibliographic title of a modern article or chapter in a Registry row |
| 142 | Registry | 227 | Cyprian of Carthage and the Episcopal Synod of Late 254 | E | bibliographic title of a modern article or chapter in a Registry row |
| 143 | Registry | 228 | Women in Late Antique North Africa (in the Writings of Augus | E | bibliographic title of a modern article or chapter in a Registry row |
| 144 | Registry | 235 | La double édition du De unitate de S. Cyprien | E | bibliographic title of a modern article or chapter in a Registry row |
| 145 | Registry | 236 | The 'Plague of Cyprian': A revised view of the origin and sp | E | bibliographic title of a modern article or chapter in a Registry row |
| 146 | Registry | 242 | From Rigor to Reconciliation: Cyprian of Carthage on Changin | E | bibliographic title of a modern article or chapter in a Registry row |
| 147 | Registry | 245 | Hippone: à la recherche de la (vraie) basilique de saint Aug | E | bibliographic title of a modern article or chapter in a Registry row |
| 148 | Registry | 247 | It Happened One Saturday Night: Ritual and Conversion in Aug | E | bibliographic title of a modern article or chapter in a Registry row |
| 149 | Registry | 258 | (unbalanced quotation marks) | U | Source_Registry.md: the table paragraph has an odd number of straight quotation marks (279 in lines 258-391, where a blank line ends the paragraph). Stray marks sit in code spans: `. , ; : ( ) - ' " ? !` (line 291), German „Vita Pontii" (line 279-282 and others), and lines 290-307 and 331-337 each carry one unpaired mark. Every straight-quote quotation in that paragraph is skipped as unchecked. |
| 150 | Registry | 395 | Flag entries resting at Confidence C or below that are inten | C1 | Construction Framework V7.4 docx para 621 — Step 2 text |
| 151 | Registry | 419 | What the sweep did not reach | E | name of a Registry section ("What the sweep did not reach", bold run-in label at Source_Registry.md:410) (Build/worlds/lpc/Source_Registry.md line 419) |
| 152 | Step0 | 12 | a phase-level process, run once when the project opens a new | C1 | Step 0 Methodology V1.0 docx para 28 — scope paragraph |
| 153 | Step0 | 12 | phase-level, run once per new release phase | C1 | Step 0 Methodology V1.0 docx para 44 — Procedure heading |
| 154 | Step0 | 20 | 8. Latin Pastoral-Congregational Christianity. c. 240s–430 C | C1 | Step 0 Conclusion FINAL v2 docx para 20 — World #8 block quotation |
| 155 | Step0 | 24 | Tertullian's own voice, distinct from Cyprian. With Cyprian  | C1 | Step 0 Conclusion FINAL v2 docx para 79 — disclosure paragraph |
| 156 | Step0 | 28 | This section is the procedural home for the Constitutional M | C1 | Step 0 Methodology V1.0 docx para 5 — Section A preamble |
| 157 | Step0 | 32 | This is the authoritative statement of the floor's content;  | C1 | Constitution V2.2 docx para 168 — Article 4 |
| 158 | Step0 | 32 | One God, the Father, the Almighty, maker of heaven and earth | C1 | Constitution V2.2 docx para 162 — Article 4 five commitments |
| 159 | Step0 | 32 | Jesus Christ as the only Son of God, eternally begotten of t | C1 | Constitution V2.2 docx para 163 — Article 4 five commitments |
| 160 | Step0 | 32 | Jesus Christ as truly human — incarnate of the Holy Spirit a | C1 | Constitution V2.2 docx para 164 — Article 4 five commitments |
| 161 | Step0 | 32 | Christ's death under Pontius Pilate, burial, bodily resurrec | C1 | Constitution V2.2 docx para 165 — Article 4 five commitments |
| 162 | Step0 | 32 | The Holy Spirit as Lord and giver of life, worshiped and glo | C1 | Constitution V2.2 docx para 166 — Article 4 five commitments |
| 163 | Step0 | 40 | dependent on Tertullian's De Oratione | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 1933 — corpus-map note |
| 164 | Step0 | 46 | Constitutional ambiguity flagged, not resolved. Article 3 (F | C1 | Step 0 Conclusion FINAL v2 docx para 56 — label + text |
| 165 | Step0 | 48 | eligibility... assessed at the world level against its estab | C1 | Step 0 Methodology V1.0 docx para 25 — A5; two fragments |
| 166 | Step0 | 48 | Test each candidate against A1 (and A2 or A3 as applicable) | C1 | Step 0 Methodology V1.0 docx para 46 — Procedure |
| 167 | Step0 | 50 | Strand is a finding, never a presupposed schema... This dete | C1 | Construction Framework V7.4 docx para 117 — Strand Determination; two fragments |
| 168 | Step0 | 64 | now applies a second, separate test alongside the doctrinal  | C1 | Step 0 Conclusion FINAL v2 docx para 8 — Conclusion sentence |
| 169 | Step0 | 64 | a broader communal interpretive tradition | C1 | Step 0 Conclusion FINAL v2 docx para 8 — Conclusion sentence |
| 170 | Step0 | 70 | appear, where relevant, as an included world's own opponents | C1 | Step 0 Methodology V1.0 docx para 23 — A5 |
| 171 | Step0 | 72 | working pastor navigating the Decian persecution and its aft | C1 | Step 0 Conclusion FINAL v2 docx para 20 — World #8 entry |
| 172 | Step0 | 72 | preaching, catechesis, and ordinary sacramental administrati | C1 | Step 0 Conclusion FINAL v2 docx para 20 — World #8 entry |
| 173 | Step0 | 72 | not the schism-crisis angle, which belongs to world #4 | C1 | Step 0 Conclusion FINAL v2 docx para 20 — World #8 entry |
| 174 | Step0 | 86 | the corpus embeds letters by others (Cornelius, the Roman cl | C4 | cic/corpus-map/novatianism.yaml line 67 — corpus-map note |
| 175 | Step0 | 105 | non-overlapping authority structure, orthogonality to state  | C1 | Step 0 Conclusion FINAL v2 docx para 20 — World #8 entry |
| 176 | Step0 | 106 | World #8 (Latin Pastoral-Congregational Christianity, not ye | C5 | Build/worlds/ijc/Doc_01_World_Identification_Boundaries_Orientation.md line 98 — IJC Doc_01 boundary bullet |
| 177 | Step0 | 107 | evidence for ijc's themes rather than a work from inside it | C4 | cic/corpus-map/imperial-juridical-christianity.yaml line 114 — corpus-map note (Augustine, City of God entry) |
| 178 | Step0 | 107 | Augustine is a North African pastor, not a participant in th | C4 | cic/corpus-map/imperial-juridical-christianity.yaml line 113 — corpus-map note (same entry) |
| 179 | Step0 | 108 | Confessions, Book 9 ch. 7 ONLY | C6 | records/ijc/source/ijc.source.augustine-confessions.md line 17 — IJC built source record |
| 180 | Step0 | 108 | Augustine's formation, theology, and the rest of the Confess | C6 | records/ijc/source/ijc.source.augustine-confessions.md line 36 — IJC built source record, BOUNDARY note |
| 181 | Step0 | 109 | the largest single thing in this volume after the Confession | C4 | cic/corpus-map/hieronymian-ascetic-literary.yaml line 31 — corpus-map note |
| 182 | Step0 | 109 | deliberately - the exchange contains Jerome's own letters, w | C4 | cic/corpus-map/hieronymian-ascetic-literary.yaml line 28 — corpus-map note |
| 183 | Step0 | 109 | the other side of this entry's central argument | C4 | cic/corpus-map/hieronymian-ascetic-literary.yaml line 39 — corpus-map note |
| 184 | Step0 | 109 | this world's own evidence, not World #8's content | C5 | Build/worlds/hal/hal_Doc_01_World_Identification_Boundaries_Orientation.md line 168 — Hieronymian Doc_01 §8.1 |
| 185 | Step0 | 109 | World #8 has not been built and its documents have not been  | C5 | Build/worlds/hal/hal_Doc_01_World_Identification_Boundaries_Orientation.md line 168 — Hieronymian Doc_01 §8.1 |
| 186 | Step0 | 109 | leav[ing] the comparison's other half to World #8's own, ind | C5 | Build/worlds/hal/hal_Doc_01_World_Identification_Boundaries_Orientation.md line 172 — Hieronymian Doc_01 §8.1; "leav[ing]" is a bracketed form of "leaves" |
| 187 | Step0 | 110 | Donatism is included as shared ancestry rather than heresiol | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 1519 — corpus-map note, two fragments joined by an ellipsis |
| 188 | Step0 | 110 | Mark may prefer another Latin home for a Numidian polemicist | C4 | cic/corpus-map/latin-pastoral-congregational-christianity.yaml line 2243 — corpus-map note |
| 189 | Step0 | 110 | not the schism-crisis angle, which belongs to world #4 | C1 | Step 0 Conclusion FINAL v2 docx para 20 — World #8 entry |
| 190 | Step0 | 110 | THE primary source for Donatism | C6 | cic/texts/README.md line 616 — Library README, not a vendored text (TextStore reads only .txt/.xml) |
| 191 | Step0 | 110 | the earliest substantial Catholic polemical treatise against | C5 | Build/worlds/don/Step0_Movement_Scope_Confirmation.md line 86 — Donatism Step 0 §3 B1 |
| 192 | Step0 | 110 | by far the largest body of surviving evidence | C5 | Build/worlds/don/Doc_02_Source_Ecology.md line 18 — Donatism Doc_02 |
| 193 | Step0 | 103 | judged relative to what is already selected or built for the | C1 | Step 0 Methodology V1.0 docx para 37 — B3 test |
| 194 | Step0 | 112 | held out of Phase One... pending a validated primary-gravity | C1 | Step 0 Conclusion FINAL v2 docx para 67 — Antiochene hold-out, two fragments |
| 195 | Step0 | 112 | its distinctiveness from world #8 is not yet demonstrated on | C1 | Step 0 Conclusion FINAL v2 docx para 73 — Antiochene hold-out |
| 196 | Step0 | 120 | a church that failed under pressure | E | a scare-quoted characterisation the document rejects ("not generically …"); Review-Artifacts/Step0_Round5_Review.md:175 files it as "scare-quoted characterizations the document is explicitly rejecting (e.g. B4's …)" |
| 197 | Step0 | 140 | The authority-structure/state-power boundary... must be stat | C5 | Build/worlds/ijc/Step0_Movement_Scope_Confirmation.md line 118 — IJC Step 0 §4 item 3, two fragments |
| 198 | Step0 | 141 | credited with forging much of the Latin theological vocabula | C1 | Step 0 Conclusion FINAL v2 docx para 79 — Tertullian disclosure |
| 199 | Step0 | 142 | pending a validated primary-gravity contrast against world # | C1 | Step 0 Conclusion FINAL v2 docx para 67 — Antiochene hold-out |
| 200 | Step0 | 143 | though partly mitigated there, since Cyprian's ecclesiology  | C1 | Step 0 Conclusion FINAL v2 docx para 55 — World #8 entry |
| 201 | Step0 | 148 | No explicit Step 0 per-world output template exists... Recom | C5 | Build/worlds/ijc/Step0_Movement_Scope_Confirmation.md line 131 — IJC Step 0 §5 Finding 3, two fragments |
| 202 | Step0 | 151 | must not restate it independently | C1 | Constitution V2.2 docx para 168 — Article 4 |
| 203 | Step0 | 159 | Cyprian appears nowhere in IJC's Doc_01 or Doc_02 | C7 | Build/worlds/lpc/Review-Artifacts/Step0_Round2_Review.md line 17 — own Round 2 review quoting the Round 1 claim that Step 0 had certified |
| 204 | Step0 | 159 | without adding a new test, waiving a stated requirement | C5 | Build/worlds/ijc/Step0_Movement_Scope_Confirmation.md line 143 — IJC Step 0 §6 |
| 205 | Step0 | 159 | direct application rather than a novel methodology interpret | C5 | Build/worlds/ijc/Step0_Movement_Scope_Confirmation.md line 137 — IJC Step 0 §6 |
| 206 | Step0 | 163 | two reviews disagreeing with each other, a contradiction bet | C3 | installed cic-build-cycle SKILL.md (outside repo: ~/.claude/skills/synced/…/cic-build-cycle/SKILL.md) line 59 — CO-022 limbs as worded in the installed skill; the repo CO-022 text (Build/reference/Project-Reference/CiC_OneDocAtATime_Build_Protocol_2026-07-06.md:39) says "a contradiction discovered between two already-cleared master documents … a decision made earlier in the build", and the repo skill copy (SKILL.md:109) has four limbs |
| 207 | Step0 | 163 | Confessions, Book 9 ch. 7 ONLY | C6 | records/ijc/source/ijc.source.augustine-confessions.md line 17 — IJC built source record |
| 208 | Step0 | 163 | Augustine's formation, theology, and the rest of the Confess | C6 | records/ijc/source/ijc.source.augustine-confessions.md line 36 — IJC built source record, BOUNDARY note |
| 209 | Step0 | 165 | Before disposing of any document, check it against these fou | C3 | installed cic-build-cycle SKILL.md (outside repo: ~/.claude/skills/synced/…/cic-build-cycle/SKILL.md) line 54 — repo copy SKILL.md now reads "Check these before any disposition. If one applies, stop and escalate to Mark, however clean the review." |
| 210 | Step0 | 167 | the ordinary pastor navigating persecution | D | Quotes a phrase of an earlier draft of Step 0 §2 A5, "a construction not actually present in the Step 0 Conclusion" (Step 0 says so itself). Survives only in Review-Artifacts/Step0_Round4_Review.md:9 and Round 3 review; not in the live Conclusion. |
| 211 | Step0 | 177 | the old thread that did this is retired | D | Quotes Mark as saying "the old thread that did this is retired". No verbatim record exists: nearest is a paraphrase in Build/worlds/ijc/Open_Gaps_Tracking.md:123 ("once the original build thread was confirmed retired"); Doc01_Round6_Review.md:184 only re-quotes Step 0 itself. The installed cic-build-cycle skill forbids attributing a quote to the project lead without a verifiable record. |
| 212 | Step0 | 16 | Project lead's Article 29 confirmation | E | title of a decision-log entry (Build/worlds/lpc/lpc_Decision_Log.md line 1897) |
| 213 | Step0 | 70 | as Donatism's own opponents, reconstructed from inside Donat | C5 | Build/worlds/don/Step0_Movement_Scope_Confirmation.md line 65 — Donatism Step 0 §0/A5 |
| 214 | Step0 | 72 | the source's own parenthetical attached specifically to that | C5 | Build/worlds/don/Step0_Movement_Scope_Confirmation.md line 116 — Donatism Step 0 §3 B3 |
