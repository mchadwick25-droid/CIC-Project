Simulated review — informational only, not an Article 31 substitute.

# Doc_06 targeted recheck of the CO-LPC-1 revision pass

- **Document:** `Build/worlds/lpc/Doc_06_Full_Lexicon_Development.md`, with `Lexicon-Chunks/`, `Lexicon_Deployment_Index.md` and `records/lpc/term/` (branch `claude/lpc-augustine-sermons-2026-10-23`, head `9a6d4d27`; diff checked: `git diff d6b449e6 9a6d4d27`)
- **Round:** 5
- **Reviewer:** Opus 5.5
- **Reviewer model:** Opus 5.5
- **Reviewer agent:** independent targeted-recheck subagent, fresh context (drafted none of the fixes)
- **Drafter:** Sonnet 5.5 (revision pass) and Opus 5.5 (renderings pass)
- **Drafter model:** Sonnet 5.5
- **Drafter agent:** the `lpc` build thread's revision-pass drafters
- **Date:** 2026-10-23
- **Scope:** targeted recheck of the revision pass. Only the Round 4 findings (`Review-Artifacts/Doc_06_ChangeOrder_Review_Round4.md`: P1-1 to P1-3, P2-1 to P2-10) are checked, each against the vendored source where factual, plus any new error the fixes introduced. This is not a re-review of the whole document.
- **Ordered by:** the project lead's Cap ruling of 2026-10-23 ("Cap ruling: lpc CO-LPC-1 revision pass", `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`)
- **Truncation check, method 1:** line and byte count with an end-of-file read. `wc` gives 164 lines and 29,526 bytes. The last line ends on the escalation assessment's closing sentence ("Doc_04 §7 items 6 and 8 are closed."), and all nine `## ` headings are present.
- **Truncation check, method 2:** hash comparison against the committed blob. `git hash-object` of the working file and `git rev-parse 9a6d4d27:<path>` both give `8404685fb2802b6cc0a39c5781ff055deeba6350`.
- **Method limits:** no web search and no model call. Nothing edited except this file. Counts re-run with Python over the vendored TEI. `python -m engine.m10.cli regate lpc` was run read-only and returned PASS.

---

## Prior findings

| Finding | Status | Evidence |
|---|---|---|
| P1-1 *libelli* / *libellatici-sacrificati* deny Cyprian's own classification | Fixed | Doc_06:63-65 re-sources both entries to Cyprian. Each source statement checks out. *De Lapsis* §27 "libellis tamen conscientiam miscuerunt" (`cyprian_de-lapsis-lat_hartel1868-csel3-tei.txt:1028-1030`; ANF "yet have defiled their conscience with certificates", `anf05_hippolytus-cyprian-caius-novatian.xml:44357-44360`). §28 "nullo sacrificii aut libelli facinore constricti" (Latin :1070-1071; ANF "bound by no crime of sacrifice *to idols* or of certificate", anf05:44392-44394, where "to idols" is the translator's italic supply). Hartel letter 55 (line 7426) §13 (line 7811) "libellaticos cum sacrificatis aequari oportere" (:7838), and ANF Ep. LI (`div3 n="LI"`, anf05:33395) §13 "those who receive certificates are to be put on a par with those who have sacrificed" (:33676-33678), which Cyprian rejects ("Neither must you think… as some do"). §17 (Hartel :7952) "libellaticos interim admitti, sacrificatis in exitu subueniri" (:7979-7980), and ANF §17 "should in the meantime be admitted… assisted at death" (:33782-33783). ANF §14 "I pay a price for this purpose" (:33707). "condicio frequenter et causa diuersa sit" (Hartel :7839-7840). *Libellus* as a martyrs' petition: letter 15 §4 (:2467) and letter 27 §1 (:3629). Registry rows 1, 2, 8, 39, 191, 291 and 296 are the rows named (`Source_Registry.md:14, 15, 21, 52, 253, 356, 361`). The one English *libell-* hit is the American editor's Note to the Introductory Notice (anf05:64312). Both records now read `formation_confidence: Documented`, citation A, verified-direct (`records/lpc/term/lpc.term.libelli.md:19-29`; `lpc.term.libellatici-sacrificati.md:17-24`). That fits a term Cyprian names and grades himself. Build vocabulary is gone from `senses.evidential`. The register drops both entries and the count is five everywhere (Doc_06:125, :164; index §7, `Lexicon_Deployment_Index.md:134-144`). `lpclex002:61`, `lpclex017:57`, `lpclex018:57-59` and `lpclex019` agree. |
| P1-2 *plebs* absence claim and "English throughout" | Fixed | Doc_06:126 drops "English throughout" and cites Doc_02 §1. Doc_06:128, `lpclex010:57` and `lpc.term.the-people.md:26-31` scope the absence to the English volume. Hartel's examples verify: letter 4 §2 "et praepositis et plebi" (:498), letter 5 §2 "plebi prouidere debemus" (:769), and letter 43 headed "CVPRIANVS PLEBI VNIVERSAE S." (:5869), which is ANF Ep. XXXIX. "89 whole-word occurrences with notes excluded" reproduces: every *pleb-* word form, case-insensitive, with footnote and margin `<note>` elements removed, gives 89. Whether *plebs* becomes the world word is left to a change order, as the finding asked. |
| P1-3 stale "Open Item 6" tension | Fixed | Doc_06:164: "*Unresolved tensions:* **none open.** Doc_04 §7 items 6 and 8 are closed." This agrees with Doc_04:266. A re-sweep of `Build/worlds/lpc` for "Open Item 6" outside review artifacts, logs and gap tracking finds only an UNVERIFIED quotation row in `lpc_Claims_Register.md:96`. |
| P2-1 status and history lines | Partly fixed | The orphaned Round 2 paragraph and the "listed at §5" pointer are gone (Doc_06:20). Line :120 no longer narrates rounds. The Document Log still says "All applied" for the Round 3 fix pass (Doc_06:154). `lpc_Decision_Log.md:2497` still says CO-LPC-1 removed Doc_06's "nine rounds" line, which was in `lpclex012` and is now removed there. Not blocking. |
| P2-2 §5 item 3 cites a stale Doc_02 site | Fixed | Doc_06:122 cites the two liturgical reads and the 2026-10-23 ruling directly. |
| P2-3 OG-36 ruling not reflected | Fixed | Doc_06:124 and :126 cite the ruling. Doc_06:79 and :126 give 42 and 38, and :124 gives the rule and 102. |
| P2-4 Registry status stale | Fixed | Doc_06:16 and :123: Approved to proceed. |
| P2-5 *suffrage* lacks [DR] | Fixed | `lpclex011_suffrage.md:10`: "AS, DR". |
| P2-6 carried hygiene | Fixed in the parts checked | Round narration is removed from `lpclex012`, `lpclex016` and `lpclex019`, and no "Round N" text remains in any chunk or the index. The "bracketed block" sentence is gone from `lpclex019`. C-N1 is fixed: both quotations now open lower-case as in Epistle X. The zero-Tier-3 ground at Doc_06:67 and index :71 now rests on LDF Part III, not on Doc_03. |
| P2-7 CF / LDF attribution | Fixed | Doc_06:30 now splits the two quotations between CF V7.4 and LDF V2.1. |
| P2-8 preface phrase referent | Fixed | Doc_06:125, `lpclex016:63` and the index's §7 row attach "least satisfactory to Protestant readers" to the anti-Donatist works as a body, and "a false exegesis" to the coercion sentence. |
| P2-9 build vocabulary in world-voice fields | Fixed | `lpc.term.grace.md` and `lpc.term.schism.md` move the contest into third-person `divergence_note` and `informational` wording with no document names. `lpc.term.compel-them-to-come-in.md` has no "Doc_06" or "Reformation" in any field. |
| P2-10 two fields below FRE 60 | Fixed | `regate lpc` PASS. Neither `lpc.term.grace` `plain_meaning` nor `lpc.term.preaching` `quick_meaning` is flagged. |

---

## New findings

### P2-A. "Sets them beside" can be heard as the opposite of what Cyprian wrote

`records/lpc/term/lpc.term.libelli.md:67-68` (`senses.evidential`): "he writes of those who receive certificates and sets them beside those who sacrificed." Ep. LI §13 refuses to put the two "on a par". "Sets them beside" can be read as equating them. *Fix:* "…and refuses to rank them with those who sacrificed."

### P2-B. The *libelli* record's quick meaning disagrees with its own source and with its own plain meaning (not introduced by this pass)

`lpc.term.libelli.md:73-74`: "papers given to people who obeyed the order to sacrifice." The record's `plain_meaning` (:53-54) says some paid for the paper instead of sacrificing. The plea it now cites (Ep. LI §14, anf05:33704-33708) is a man who obtained the certificate without sacrificing. This text is older than the revision pass. It matters more now that the record is rated Documented. *Fix:* "papers saying a person had sacrificed, whether or not they had."

---

## Summary

All three P1s are fixed and verified at source. The Latin and English for *libelli*, *libellatici* and *sacrificati* match the quotations word for word. Documented is the right confidence for terms Cyprian names and grades. The *plebs* count reproduces. The two new findings are P2 wording faults in one record. No P0 or P1 remains.

VERDICT: Approved to proceed
