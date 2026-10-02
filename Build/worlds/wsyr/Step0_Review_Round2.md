# Adversarial Review, Round 2: wsyr library stage (Step 0, Doc_01, Doc_02), targeted recheck against the Round 1 fixes (commit e8d2c80a)

**Verdict: SUBSTANTIAL REVISION REQUIRED.** Most Round 1 findings were fixed
correctly. The fix pass itself introduced new errors while adding the
Tritheist material: it used the 1860 translator's own editorial excursus
(drawing explicitly on the 13th-century chronicler Bar-Hebraeus) as if it
were John of Ephesus's own contemporary narrative, in five places, and it
mischaracterized the Tritheist dispute as a rival reading of the
Christological "one nature" formula when it is actually a Trinitarian
dispute (Ascunages's own quoted creed affirms "one nature of Christ" and
diverges only on how many "Godheads" the Trinity contains). It also left
stale "formulaic" wording in Step 0 immediately next to the paragraph that
re-tags that same claim as Contested, added an unsupported specific
consecration date for Sergius of Tella (544/546), and a minor overreach
("Jacobite... was never its own chosen name"). The 586-616 Antioch-
Alexandria schism and Heraclius's reunion efforts, flagged as missing from
Doc_01's own internal-hinges list, were still missing.

Independently verified before fixing: the Payne Smith/Bar-Hebraeus
attribution directly, at `cic/texts/john-of-ephesus_ecclesiastical-
history-part3_paynesmith1860.txt` around line 4568 ("We may now, however,
return to our author, whose narrative will be found to confirm the above
statements of Bar-Hebraeus").

All findings fixed in a further revision (commit — see git log): the
misattribution corrected across the EH3 staging file, Doc_01 §1/§2/§6,
Doc_02 (Table A, author-gravity section, §8, verification loci), Step 0
§1, and Open_Gaps item 5; the Tritheist dispute recharacterized as
Trinitarian throughout; the "formulaic" wording in Step 0 rewritten to
match the claim-one/claim-two structure; the Sergius date replaced with
the vendored text's own vaguer "some years after" and flagged as
unconfirmed; the Jacobite overreach narrowed; the 586-616 schism/Heraclius
material added as a named (not yet researched) internal hinge in Doc_01 §2
and a new Open_Gaps item.

**This is the third round of substantial revision.** Per `cic-build-cycle`'s
own review-cycle rule, three rounds is the cap — if a further review still
finds substantial issues, this document must stop and escalate as an
unresolved tension rather than attempt a fourth round.
