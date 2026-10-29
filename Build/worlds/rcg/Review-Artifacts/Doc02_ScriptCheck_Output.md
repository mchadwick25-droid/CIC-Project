# Doc_02 and Source Registry script check: rcg

Script: `tools/verify_world_source_docs.py rcg --texts <repo>/cic/texts`. It reads `Build/worlds/rcg/Doc_02_Source_Ecology.md`, `Build/worlds/rcg/Source_Registry.md` and the vendored texts, and changes nothing. Date of runs: 2026-10-29.

Two runs of the same script:

1. Before the fixes, on the two documents as on `origin/main` at `d5d7eef44`: 4 of 8 checks fail, with 9 findings.
2. After the fixes, on the documents in the same pull request as this file: 8 of 8 checks pass.

The findings in run 1 map to the second cap-ruling review as follows. CR2-1: the two `absence-claims` findings on John the Faster and the `absence-claims` finding on the Donatist sentence. CR2-2: the `same-volume` finding on rows 15 and 19 and the two `universal-claims` findings. The three `quotes` findings are further slips the review did not list (an apparatus quotation that changed a semicolon to a full stop, and the Ostia quotation in Doc_02 and in Registry row 12 that dropped the file's footnote mark).

Quotation matching normalises whitespace, drops soft hyphens and makes curly quotation marks straight. Nothing else is normalised.

# Run 1: before the fixes

## Doc_02 and Source Registry checks: rcg

- Documents: `Build/worlds/rcg/Doc_02_Source_Ecology.md` (143 lines) and `Build/worlds/rcg/Source_Registry.md` (20 rows)
- Vendored texts: `cic/texts`
- Window used for dating checks: 560-604
- Checks run: 8; passed: 4; failed: 4

| Check | Result | Scope |
|---|---|---|
| `texts-exist` | PASS | 19 distinct file names |
| `registry-vocab` | PASS | 20 rows |
| `cross-refs` | PASS | 29 row references, 17 Registry file names |
| `same-volume` | FAIL | 5 multi-row groups |
| `absence-claims` | FAIL | 8 absence statements; 3 named entities searched in 32 in-window files |
| `universal-claims` | FAIL | 1 universal claims; dominant author 'Gregory I', 2 other Native primary authors |
| `doc-vs-registry` | PASS | 2 sentence/work pairs |
| `quotes` | FAIL | 37 quotations (40 pieces) with a cited line range or element id; tolerance 10 lines |

### texts-exist: PASS

Every vendored file named in Doc_02 or the Registry exists.

Checked: 19 distinct file names.

### registry-vocab: PASS

Each Registry row is well formed and uses the template's vocabulary.

Checked: 20 rows.

### cross-refs: PASS

Row references resolve, and each file a row names is also named in Doc_02.

Checked: 29 row references, 17 Registry file names.

### same-volume: FAIL

Rows for one work or one file share a Boundary Status unless a note says why.

Checked: 5 multi-row groups.
- FAIL Registry:26: work: liber pontificalis is classified differently without a stated reason (row 15 Excluded, row 19 Native)

### absence-claims: FAIL

Statements that a source is not vendored hold against the vendored directory.

Checked: 8 absence statements; 3 named entities searched in 32 in-window files.
- FAIL Doc_02:44: absence claim names 'John the Faster', which occurs in `john-ephesus_ecclesiastical-history-part3_paynesmith1860.txt` (dated 507-588, inside the window); the Registry does not classify that file
- FAIL Doc_02:44: absence claim names 'John the Faster', which occurs in `john-of-ephesus_ecclesiastical-history-part3_paynesmith1860.txt` (dated 507-588, inside the window); the Registry does not classify that file
- FAIL Doc_02:70: unscoped absence claim names 'Donatist', but vendored files carry it: `augustine_oeuvres-completes-tome13-donatistes-slice-fra_raulx1869.txt`, `augustine_oeuvres-completes-tome15-donatistes-slice-fra_raulx1870.txt`, `augustine_scripta-contra-donatistas-opera-omnia-t9-lat_migne-pl43.txt`; scope the claim to the window

### universal-claims: FAIL

'Every Native primary source is <author>'s own writing' names each exception.

Checked: 1 universal claims; dominant author 'Gregory I', 2 other Native primary authors.
- FAIL Doc_02:41: universal claim about Native primary sources does not name the Native primary row by 'Gregory of Tours' (dominant author 'Gregory I')
- FAIL Doc_02:41: universal claim about Native primary sources does not name the Native primary row by 'Liber Pontificalis' (dominant author 'Gregory I')

### doc-vs-registry: PASS

Doc_02 sentences that call a Registry work Native or Excluded agree with its rows.

Checked: 2 sentence/work pairs.

### quotes: FAIL

Quotations with a cited file and locus occur there (whitespace collapsed, soft hyphens dropped, curly quotes made straight).

Checked: 37 quotations (40 pieces) with a cited line range or element id; tolerance 10 lines.
- Note: 3 quotation pieces were found in a named file or reference document but not at the locus on their line (Doc_02:32, Doc_02:34, Registry:19); informational.
- Note: 6 quotations of four or more words name no file or element id on their line and were not checked (Doc_02:30, Doc_02:30, Doc_02:50, Doc_02:68, Doc_02:78, Registry:22).
- FAIL Doc_02:22: quotation not found in its cited locus or any named file: "He in vain endeavoured, either by remonstrance or by trying to enlist the emperor's aid..."
- FAIL Doc_02:55: quotation not found in its cited locus or any named file: "could not rest till he came back from Ostia to see with his own eyes how the consecrati..."
- FAIL Registry:23: quotation not found in its cited locus or any named file: "Our deacon could not rest till he came back from Ostia to see with his own eyes how the..."

Overall: FAIL
# Run 2: after the fixes

## Doc_02 and Source Registry checks: rcg

- Documents: `Build/worlds/rcg/Doc_02_Source_Ecology.md` (145 lines) and `Build/worlds/rcg/Source_Registry.md` (21 rows)
- Vendored texts: `cic/texts`
- Window used for dating checks: 560-604
- Checks run: 8; passed: 8; failed: 0

| Check | Result | Scope |
|---|---|---|
| `texts-exist` | PASS | 23 distinct file names |
| `registry-vocab` | PASS | 21 rows |
| `cross-refs` | PASS | 35 row references, 19 Registry file names |
| `same-volume` | PASS | 5 multi-row groups |
| `absence-claims` | PASS | 7 absence statements; 1 named entities searched in 32 in-window files |
| `universal-claims` | PASS | 1 universal claims; dominant author 'Gregory I', 1 other Native primary authors |
| `doc-vs-registry` | PASS | 3 sentence/work pairs |
| `quotes` | PASS | 49 quotations (52 pieces) with a cited line range or element id; tolerance 10 lines |

### texts-exist: PASS

Every vendored file named in Doc_02 or the Registry exists.

Checked: 23 distinct file names.

### registry-vocab: PASS

Each Registry row is well formed and uses the template's vocabulary.

Checked: 21 rows.

### cross-refs: PASS

Row references resolve, and each file a row names is also named in Doc_02.

Checked: 35 row references, 19 Registry file names.

### same-volume: PASS

Rows for one work or one file share a Boundary Status unless a note says why.

Checked: 5 multi-row groups.

### absence-claims: PASS

Statements that a source is not vendored hold against the vendored directory.

Checked: 7 absence statements; 1 named entities searched in 32 in-window files.

### universal-claims: PASS

'Every Native primary source is <author>'s own writing' names each exception.

Checked: 1 universal claims; dominant author 'Gregory I', 1 other Native primary authors.

### doc-vs-registry: PASS

Doc_02 sentences that call a Registry work Native or Excluded agree with its rows.

Checked: 3 sentence/work pairs.

### quotes: PASS

Quotations with a cited file and locus occur there (whitespace collapsed, soft hyphens dropped, curly quotes made straight).

Checked: 49 quotations (52 pieces) with a cited line range or element id; tolerance 10 lines.
- Note: 2 quotation pieces were found in a named file or reference document but not at the locus on their line (Doc_02:32, Registry:19); informational.
- Note: 4 quotations of four or more words name no file or element id on their line and were not checked (Doc_02:50, Doc_02:68, Doc_02:78, Registry:22).

Overall: PASS