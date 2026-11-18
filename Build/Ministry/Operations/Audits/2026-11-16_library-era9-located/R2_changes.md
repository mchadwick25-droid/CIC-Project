# Round 2 changes, era 9, the located volumes (2026-11-16)

`R2_recheck.md` closed all 16 findings and found one new problem in the fix for R1-07. It was corrected in
`mkspec299.py` and the batch was vendored again from it. The review cycle ends here: one review and one
targeted recheck.

| finding | what changed |
|---|---|
| R1-07 American Church History | Hamilton's history starts at host line 17815, where its title stands, not 17816, which is blank; Dubbs's history runs to about 17814. The header, the shelf row's locus and the `authors_ruled` evidence range (file lines 17827-17841) follow. The spec's anchor for this line now allows no neighbor line, since a one-line allowance is what let the slip through. |

The spec's line-anchor checks, the map check and the registry checks pass after the change.
