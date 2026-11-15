# Live-surfaces sweep, 2026-11-15 — changes for review round 1

Branch `claude/live-surfaces-sweep`. Mark's instruction, 15 Nov: "Make sure notes and comments are not in library or program, no comments, change orders or corruption in the program or working systems they go in outside files."

Every cut or rewritten passage is kept verbatim in `Moved_Notes.md` (this folder), with where its substance also lives.

## 1. The 16 lines the checker flagged on main

| Line | Judgment | Done |
|---|---|---|
| `engine/BASELINES.md:10, 14, 22` | Real content. The dates are part of a tag and a branch name; the baseline cannot be named without them. | Checker taught: a date inside a one-name code span or a fenced command is a name. Two hand labels in the precision/recall sample changed from REWRITE to KEEP for this reason. |
| `engine/BASELINES.md:17` | Redundant date in prose; the heading already names the baseline. | "the 2026-08-24 live routing run" → "this baseline's live routing run". |
| `engine/m2/validation.py:65` | Real content: "the freeze" names a touchpoint in a string the engine writes. | Checker taught: bare "the Freeze" is a stage name. "at the Freeze" and "fixed ... at the gate" still flag. |
| `records/ijc/force/ijc.force.leo-rejects-canon-28.md:29` (`name`) | Builder vocabulary ("Strand A/B") in a spoken field. | Not changed: it would change what a Representative says. Listed in section 5. |
| `records/pahc/world_core/pahc.core.house-church.md:69` (`cautions`) | Same ("Strand A"), spoken field. | Not changed. Listed in section 5. |
| `Build/reference/.../Doc_04_Gravity_Discovery_Template_V1.0.md:56` | Real content: a required section's name. | Checker taught: a heading in a Build/reference template is not an open item. |
| `Build/reference/.../Doc_04_Gravity_Discovery_Template_V1.0.md:72` | Process narration about the template's maturity, in a method document. | Not changed: a method document. Listed in section 5. |
| `Build/reference/L4-Templates/Voice_Configuration_Template.md:208` | Real content: an instruction inside a bracketed placeholder. | Checker taught: a bracketed placeholder in a template is not an open item. |
| `Build/worlds/_cross-world/discovery_helper.py:282-287` | Real content: TODO slots in a stub the program prints for its reader to fill. | Checker taught: an open-item cue on a Python code line (not a comment, not a docstring) is program output. Comments and docstrings still flag. |
| `Build/worlds/alx/Lexicon-Chunks/alexlex003_catechesis.md:34` | Real content: "has not yet been formed" is the lexicon's subject. | Checker taught: "has not yet been" is an open-item cue only with a process verb (tested, checked, located, acquired, ...). |
| `Build/worlds/ijc/Source_Registry.md:43` | Review history in a verification note. | Note rewritten in present tense; history appended to `Build/worlds/ijc/build/BUILD-LOG.md`; the Added cell keeps both dates in the registry's own date form. |

## 2. What was moved or cut

- **engine/** (25 files, comments and docstrings only; no code, no string the engine emits): pull-request and issue numbers as provenance (#403, #413, #419, #420, #440), a working-branch name, four pointers to a private plan file (`/root/.claude/plans/...`), "Mark's call", "Mark's standing quote ruling", "Mark-approved", "Mark's approved wording", "Mark runs/types" (now "the operator"), "the accounts change order" and "System Hub decision 34", "an earlier version of this ... got wrong" (rewritten as the rule itself), "this replaces" narrations, Open-Gaps pointers used as provenance (OG-9, OG-10, OG-45/48, the desert pilot's catch), the retired cic-poc Dockerfile's history, and the round-cap history in `live_table_battery.py` (the reason kept, in present tense).
- **cic/texts/** (the Library):
  - 44 vendored text headers rewritten in place, line counts unchanged: review-round wrappers ("Note (independent review, Round 18; extended, Round 19 ...)", "Corrected here (independent review, Round 17)", "corrected here, independent review Round 23's own M1, from an earlier draft ..."), "(Mark's OCR ruling, 2026-09-25)" on second-witness caveats (the caveat kept), a sibling session's id and branch, and Macrinae's "STILL NEEDED" to-do (now a scope note). The didymus header's six boxed lines were rewritten to six lines.
  - `REGISTRY.yaml` header comments: the move history and the R33 quotation (the principle kept in plain words), and a ruling attribution on the `letterform` kind.
  - `INTAKE.md`: the ruling dates, "Starting 2026-09-02", and the paragraph narrating the framing the 2026-09-25 rule replaced (recorded in LIBRARY-DECISION-LOG.md).
- **cic-website/README.md**: the funding-decision pointers, "the entity is now a for-profit PBC, and .org read as nonprofit-coded", "needs a content refresh", and the section "Known follow-ups, not yet done" (moved whole; carried in the Open-Gaps entry).
- **Build/worlds/ijc/Source_Registry.md** row 30, as above.

## 3. The checker (`tools/check_live_commentary.py`)

New surfaces:
- `cic-texts` (cic/texts/). A vendored edition (`.txt`) is source text and never scanned; only its intake header is, read from the first 256 KB. The header ends at its `---`, or at the closing rule of the older boxed form. In a header, a date and a thread naming itself as the fetcher are data (INTAKE.md section 4: "who supplied it and when"), and on the Source line so is the intake pull request. `REGISTRY.yaml`'s `notes`, `supplied_by`, `date_added` and apparatus `evidence` values are PROTECTED (reported, not blocking): the file's own declared policy keeps `notes` as "a historical record of what was known then", and the other three are schema data. Its header comments and other fields are scanned. README.md, AUTHORS.md and STRUCTURE.md are generated from REGISTRY.yaml, so they are PROTECTED and a find is reported once, at its source. `_intake/` and the 38 CCEL XML editions are not scanned.
- `sandbox` (Sandbox/).

New patterns, everywhere: `review-finding` (Critic/Review Finding N), `change-order`, `pr-ref` (PR #N, "#440's own", "(#419, #420)", "by #413"; a bare "#333" or "#6400" never matches), `session-branch` (claude/... branch names, /root/.claude/ paths), `mark-provenance` (Mark-approved, at Mark's direction, Mark's standing/approved/OCR/sign-off, confirmed/accepted/approved by Mark or the project lead, the project lead's own call; "supplied by Mark" is not here), `builder-thread`, `earlier-version`.

New on the two public sites only (cft-website/, cic-website/, stylesheets excluded):
- `builder-phrase`: whose record sits at, that record never names, the same province's church, consulted via, known to me, not consulted, census row/edge/relations line, per census, tension-sibling, Who scan.
- `record-slug`: a record id (`<world code>.<type>.<name>`, world codes read from records/) or a hyphenated census id (from cic-website/data/world-census.json) in reader text. A line is read with its HTML tags, id-like key/value pairs, keys starting `_`, bare one-token quoted strings (string literals read left to right), and paths and URLs taken out first, so ids in markup and data plumbing do not count.

False-positive repairs, each narrow (section 1): bare "the Freeze"; "has not yet been" needs a process verb; template headings and bracketed placeholders; open-item cues on Python code lines; dates inside one-name code spans and fenced commands; a dated file name in a Source Registry note no longer hides the Added column; "caught by the OCR/scan" is not change history; "Mark's own" before a gospel noun is the Evangelist; "prior turn" alone is a conversation turn.

Tests: `tools/tests/test_check_live_commentary_library_sites.py` (new), the old "vendored texts fully excluded" test removed (it encoded the rule this change replaces), and the two BASELINES hand labels. Whole suite: 351 passed.

Scope note for every other thread: the new patterns report existing text across the tree (counts in section 4). `--enforce` fails a change only on files it edits, so the existing text blocks nothing until a change touches its file.

## 4. Whole-tree counts after this change (REWRITE + ROUTE, then PROTECTED)

On main before this change the whole tree carried 16 REWRITE/ROUTE lines. With the wider check, and after this change's fixes:

| surface | REWRITE + ROUTE | PROTECTED (reported, never blocking) |
|---|---|---|
| cft-website | 104 (58 story `relationsSummary` lines and the story source notes under Release 45; the rest census text, section 5) | 0 |
| cic-website | 13 (census text mirrored from the map, and three real reader-text leaks: the syriac pull-quote cite in the page and its world JSON, and a desert story's date field, section 5) | 0 |
| cic-texts | 8 (section 5) | 5,406 |
| engine | 6 | 3,819 |
| records | 61 (mostly `mark-provenance` and `review-finding` in record bodies, section 5) | 443 |
| reference | 40 (method vocabulary such as "change order", and branch names in method documents) | 0 |
| worlds | 149 (construction documents: "this build thread", Mark provenance, change orders, review findings) | 21,909 |
| sandbox | 11 (the sample card's text and dated seeds, section 5) | 0 |
| cic-corpus-map | 9 | 0 |
| cic-poc-frontend | 1 | 0 |
| canon, fixtures, packages, cic-engine | 0 | 8 |

These are existing text that the new patterns now see. None blocks a change that does not edit its file.

## 5. Left for Mark or another thread (not changed)

- **Release 45 territory (session_01JMNsS9pAu8gHF18tfNX1Fs, branch claude/cft-story-relations-cleanup):** cft-website/index.html `DATA.stories`, the census `relationsSummary` and story fields. The checker now flags 58 relationsSummary lines and the story source notes in that region. Because Release 45 edits index.html, its `--enforce` run will see every flagged line left in that file, including the "consulted via" source notes that Mark is to word. Sequence this PR after Release 45, or have Mark rule on the source notes' wording first.
- **The 78 story source notes with "consulted via summaries only" and similar.** Real sourcing limits; Mark decides their wording.
- **Census text outside the stories (cft-website/index.html DATA and cic-website/data/world-census.json, and the generated tree pages):** "the census row ends here" (council-of-dvin-609, second-council-of-constantinople-553), "The Who scan lists him as not yet scored" (council-of-nicaea-325, council-of-sardica-343), "native genre per census" (the-stone-campbell-restoration-movement), "tension-sibling evidence (census relations line)" (latin-american-base-communities), "web-verified per the census row", a "Change order under G89-38 a" link reason; the census `meta.source`/`meta.notes` paths; `eras[].stepStatus`/`rec` ("Step 0 COMPLETE"); about 19 `statusWord` values in build jargon ("Floor divergence recorded ... register retained", "c2 CLEARED"); 166 `statusDescription` values opening "Tiered Strong (Tier 1)"; 22 `sourcing` values opening "RICH"/"THIN", which the map renders. Reader-facing census wording, and index.html is under Release 45: a decision for Mark and a slice after Release 45.
- **cic-website/traditions/syriac-edessa-nisibis.html:471**: a pull-quote's `<cite>` shows a record id, "syr.source.theodoret-historia-ecclesiastica (Theodoret's telling of Jacob's prayer)". Root cause: `records/syr/quote/syr.quote.theodoret-gnats.md`'s `speaker_or_author` holds a source id plus a note, and `cic-website/assets/orientation-render.mjs` prints the field raw. A record and renderer fix for the site-compiler thread.
- **A desert story's date field (cic-website/data/worlds/desert-monasticism.json):** "January 399, at Kellia ... per Palladius ch. XXXVIII (the year itself from desert.source.evagrius-praktikos and Doc_01 SS2.3)", from `records/desert/figure/desert.figure.evagrius.md`. A build note with a record id and a Doc_01 section in reader text, and probably in a spoken field. A record fix, then a package rebuild and site recompile, for the desert world's thread.
- **Spoken record fields:** `ijc.force.leo-rejects-canon-28` `name` ("the Strand A/B Fracture"), `pahc.core.house-church` `cautions` ("every Strand A use"), `rzg.force.synod-of-dort-international-dimension` `description` ("Confirmed by the project lead as part of this world's own transmission").
- **Record bodies.** The record schema (Artifact-1, line 7) defines a record's markdown body as "provenance and build notes — never read by any builder". About 25 body passages carry rulings, branch names, review findings and "the project lead's own call" (hal, desert, pahc voice_craft; ijc quotes; cappadocian stories, figures and demonstrations; gallic, hal and syr terms; syr, desert, hal world_core; lpc and don). By schema they are in their designed place. Whether that designed place conflicts with CLAUDE.md's rule is a governance question.
- **Source records' `discovery_channel`** values carrying review rounds and a change order (desert cassian ×2 "change order CO-P2-10(c)"; desert, ijc "added at Step2 Review Round 1, Finding 4", "located at review (Opus canon-structure pass)"). A schema-defined provenance field, PROTECTED by the checker.
- **REGISTRY.yaml `notes`.** About 35 notes narrate review rounds and corrections (for example didymus "corrected 2026-09-08, Round 2 Opus review", avvakum "CORRECTION ... CORRECTION-OF-A-CORRECTION"). The file's own policy says notes are append-only history, never silently corrected. A policy decision for Mark; the checker reports these as PROTECTED meanwhile.
- **Library headers:** hadewijch's Rights line ("Mark's ruling allows Hadewijch only in this 1875 edition", a rights decision); optatus's Rights basis ("confirmed by Mark 2026-08-15", a rights check by a named person); nestle1904's line 21, which still says an original-language text is "never primary evidence ... this project's evidence language is English", contrary to INTAKE.md's current rule (a content correction, not a comment); open-item pointers in calvin_letters-vol1 (l.28), luther_bondage-of-the-will (l.43), theodosianus-16 (l.69) and wyclif_de-civili-dominio (l.6); the tacitus and lucian "WHY THIS VOLUME / WHAT IT DOES NOT SETTLE" builder guidance; about 70 provenance notes naming "this world" or a world's manifest; aphrahat's "accepted ... by the project lead, 2026-08-18".
- **Method documents:** Doc_04 template "What this template deliberately leaves unsettled"; Build/reference hits on the new patterns (change order ×23, branch names ×8), which are mostly the method's own vocabulary.
- **Sandbox/answering-library:** `index/status.py`'s PENDING_OPTION and `index/card.py`'s card text ("The run waits for Mark to approve this sample by name and set the cap", "Embeddings are a separate metered class (proposal decision 2c) that Mark has not decided", "its own change order") are strings the program prints into a sample card for Mark. Whether that card belongs in Build/Ministry/Features/ is a decision for that feature's thread.
- **engine/, rest:** `engine/m1/rendering_fidelity.py:83` ("replaced by Sonnet 5 once the account can invoke it ... not this module's own call") is a design note about a future model change. The whole-tree scan's remaining engine hits are in section 4.

## 6. Fixes after review round 1 (`R1_review.md`, PASS WITH FIXES)

1. Cyprian Pars III: "three indices, the largest of them a scriptural index" → "three indices: a scriptural index"; the word index is again the one named largest.
2. ijc Source Registry row 30: "Title confirmed; publisher, series and year added at that check; not independently re-collated ..., so B, not A". Section 1's row is superseded by this wording.
3. `_library_header_end`: a boxed header now runs to its closing rule however long it is, and never falls back to the first blank line. The four boxed headers longer than 120 lines (pachomius, origen, gregory-great, pl11) are scanned; origen:125 and pl11 now report. Test added.
4. vonsoden_prosopographie's "NOT YET VENDORED, flagged for a future round" is rewritten in place as a pointer to the vendored `vonsoden_ketzertaufstreit-rom-karthago-deu_1909.txt`. The route cues now include "not yet vendored" and "flagged for a future round". The stale REGISTRY note for the same file (REGISTRY.yaml:1884) is PROTECTED and listed below.
5. The superseded "never primary evidence / evidence language is English" wording sits in thirteen headers, not one: csel57-pars4 (augustine_epistulae-critical_goldbacher), ausbund_lancaster1846, borromeo_acta-ecclesiae-mediolanensis, busch_chronicon-windeshemense, faber_memoriale, harnack_vita-cypriani-commentary, three kempis_opera-omnia files (sermones-de-compunctione, tractatus, vallis-liliorum-epistulae), nestle1904_greek-new-testament, piccolomini_historia-bohemica, pius-v_apostolicarum-epistolarum, ribadeneira_vita-ignatii-loiolae. One content correction for Mark; listed in Open-Gaps 280. (The csel57 and harnack headers were edited here for other lines; this wording was left as it stands, since changing a file's stated evidence status is a content decision.)
6. "support.html needs a content refresh before it is linked again" added to Open-Gaps 280.
7. Tests added for the "caught by the OCR" and "Mark's own" + gospel-noun exclusions, the Source-line data patterns, REGISTRY `evidence`/`date_added`/`supplied_by` protection, the `- date_added:` entry form, and the one-line change-history rule in REGISTRY.
8. Template placeholders: links, `[ ]`/`[x]` boxes, code spans and escaped `\[` are not placeholders, and a placeholder ends at a heading, a blank line or `---`. Test added.
9. `_registry_notes_lines`: for `- key:` the key's column is indent + 2, so an entry that opens with `- date_added:` no longer protects its other fields.
10. (a) A code span must hold more than a date to count as a name. (b) In a Library header, `builder-thread` is data on the Source line only; a new `dated-fix` pattern ("Fixed 2026-09-03", or "(Fixed" at a line end) flags dated repairs anywhere. evagrius_praktikos_dysinger:7 now reports.
11. "has not yet been" allows one adverb ("comprehensively assessed") and adds assessed and opened.
12. (a) quote_verbatim: "Two of the three patterns (the source-side ones)". (b) didymus: "No Greek characters survive in / this file's OCR." (c) Cyprian Pars III keeps the plain fact: "Closely related material from the same edition is vendored separately". Session ids in other headers' Source/Provenance lines are left: they say who fetched a file, which INTAKE.md section 4 asks for.

Library after these fixes: 9 REWRITE and 10 ROUTE lines, every one in a file this change does not edit (bell, cassian and eucherius "this build thread" outside a Source line; calvin, chronica-minora, gregory-great, luther, pl11 ×3, theodosianus, vonsoden_streit, wyclif open-item pointers; hadewijch, optatus, nestle1904 as listed; john-ephesus, origen and evagrius change history). Section 4's cic-texts row is superseded by this count.
