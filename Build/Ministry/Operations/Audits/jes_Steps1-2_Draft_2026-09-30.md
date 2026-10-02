# jes, drafting of Doc_01, Doc_02, Source_Registry and Open_Gaps_Tracking (2026-09-30)

Drafter: Sonnet 5.5, session `session_019FXuEebrCDmzYe987sNAxL`. Inputs: `Build/worlds/jes/Step0_Movement_Scope_Confirmation.md` (Approved to proceed; Round 4 spot-check clear); `Build/worlds/hus/Review-Artifacts/*.md` as the checklist of failure patterns; the finished `hus` files as the model; Construction Framework V7.4, Forces Framework V1.1 and Constitution V2.3, read from their `.docx` files. No independent review has run on any of the drafts.

## What was done

- The folder `Build/World-Builds/Society-of-Jesus` was moved to `Build/worlds/jes` with `git mv`. The Step 0 header now carries the code `jes`. Its Status line and Next-step line were brought into line with its own Disposition, which already said "Approved to proceed". The root `README.md` map line and `CiC_Repo_Structure_Tracking.md` were updated in the way the `hus` move did it.
- `build/jes_Build_State.yaml` was created.
- Doc_01 (Step 1), Doc_02 with `Source_Registry.md` (Step 2), and new entries in `Open_Gaps_Tracking.md` were drafted. The entry recording that the earlier header gap is resolved is in the ledger.
- Nothing was edited in `cic/texts/`, `cic/corpus-map/`, `records/` or `packages/`. `jes` is not registered in `records/worlds/`.

## How each hus failure pattern was handled

| hus finding pattern | What was done here |
|---|---|
| Article 4 check not verbatim, result too strong | The five commitments are quoted from the Constitution's text in Doc_01 §8, and each is answered clause by clause with "shown" and "not shown". The result names what cannot be checked (the later mission voice, 1585–1650). |
| Loci, quotes and figures not verified | Every quotation in the four live files was matched by script against the vendored files with the project's own quote gate (`engine/m1/quote_verbatim.py`, `verify_quote_text`). The last run matched all 74 quotations in Doc_01, all 16 in Doc_02 and all 157 in the Registry. The ledger holds three further quoted strings that come from Step 0 or from another world's file header, and were checked by eye. Line numbers were read from the files. Corpus figures were counted two ways: the sum of decoded file lengths, and `cat` piped to `wc -m`. Both give 23,171,710 characters. |
| Registry letters, cross-world rows | Every row carries one letter. A is used only where the Licensed-For passages were read. Rows 29, 31, 36 and 37 are B. No row is entered for a work the corpus map assigns to another world. Candidates on other worlds' shelves are in Open_Gaps section E. |
| Confidence tags too strong | A claim resting on one editors' preface is tagged "Documented as the editors' statement". Contested is used for the founding motive and for the two counts of residences in 1555. Attribution of the "Explanation of the Creed" to Xavier is Inferential/Thin. The rites dates carry no tag, because no source is on the shelf. |
| Forces lens missing | Doc_02 §6 has the forces lens: which sources speak to external forces, what the silences show, and survivorship. |
| Sources named without a row | Every source named in Doc_01, Doc_02 or the Registry has a row. Sources found in the apparatus (Sommervogel, Alcázar, Astrain, Orlandini, Sacchini, Menchaca, Poussines, Philippucci, Codretto) have rows at C. |
| Jesuit voice gap | Doc_02 §6 states it in six numbered points, with the years. The gap after 1585 is 65 of the window's 110 years. |
| Readability | The engine's grader (`engine.m7.turn_readability.score_turn`, markdown symbols and row citations stripped) gives Doc_01 FK 7.6, FRE about 59 and Doc_02 FK 7.5, FRE about 56. Both are below the floor of 60 for the whole document. Sections 4, 5, 6 and 7 of Doc_01 and section 7 of Doc_02 are above 60. The Confidence Map and the header lines pull the totals down. |
| Process narration in live files | None was written into the live files. The tool `tools/check_live_commentary.py --surface worlds` reports for the four live files only iso-date hits in schema fields (the Registry's Added and Discovery cells and the search-record date), and two PROTECTED heading hits. |
| Things left open | The Article 29 tradition and confirmation, the Representative, and the registration of `jes` are open in Doc_01 §9 and in the ledger. |

## Findings that differ from Step 0 or from the dossier

- Ignatius's own vendored letters run to March 1548 in the Latin volume, and not to 1547 (Registry row 16).
- The Generals are on the shelf as senders of register copies to Salmeron, under their names, in Salmeron's two volumes (Registry rows 67 and 69). Step 0 says nothing vendored gives their voice. Nothing in Step 0 or in the earlier ledger entry was edited. The difference is recorded as a change-order question for the project lead.
- Boero's Part the Second is an English rendering of Faber's whole diary, condensed in places (Registry rows 19 and 20). The corpus-map note leaves this open.
- The census's Xavier story quotes wording that is not in the vendored translation (Registry rows 23 and 43).
- The bull of 1540 has two days in Coleridge's volume (17 and 27 September). The Lainez editors give 27 September.
- A study of Japan is bound into a file assigned to Donatism (Open_Gaps section E).

## Tool runs

- `python -m engine.m10.cli gaps jes`: `gaps: PASS`.
- `python tools/check_live_commentary.py --surface worlds`: exit 0. It is report-only.
- The quote gate, run by script over the four live files: 0 unverified in Doc_01, Doc_02 and the Registry.

## Not verified

- Every Latin quotation is checked against the scan text only. No page image was available.
- The rites controversy dates (1623, 1627–28, 1645) come from Step 0 and were not tested against any source.
- The counts of letters headed Lainez, Borgia, Mercurian and Aquaviva were made from the scan's headings and are approximate.
- Most letters in the Latin volumes were not read. Sample letters were read for rows 11 to 13, 67 to 69.
- Nadal's letters were not read beyond the Preface. Canisius's catechism and the 1606 Constitutions were read only in parts, and are used by paraphrase or by structure.
