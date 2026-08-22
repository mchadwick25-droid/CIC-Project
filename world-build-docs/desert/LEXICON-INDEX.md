# Desert Monasticism — Lexicon Master Index (step 3a)

**Derived from:** the 18 term records in `records/desert/term/` (this index is generated against those files and re-checked against them; the records are the source of truth). Re-derivation base: the prior build's cleared Doc_06 (`World-Builds/Desert-Monasticism/CiC_W3_Doc06_Full_Lexicon.md`, three review rounds, 24-edge reciprocity graph verified there) — carried into the new record schema with senses rewritten to the four-register shape and FK-gated plain fields.

**Tier mapping:** Doc_06 lexicon tiers → `retrieval.tier`, with two recorded divergences: *apotagē* (Doc_06 Tier 1 → retrieval tier 2; supporting rather than core retrieval weight, noted in its record body) and *synaxis* (Doc_06 Tier 2 → retrieval tier 1; the F3-I gathering question retrieves it directly, noted in its record body).

**Tags** carried from Doc_06: AS = Signature Vocabulary · SC = Shared Vocabulary · DR = High Distortion Risk · TC = Technical Concept · RT = Likely Runtime Term · PV = Plural Voices · CT = Contested Tradition.

## Master table

| # | Term (record slug) | Tier | AS | SC | DR | TC | RT | PV | CT | canon_cells | False friends (aliases) | Related terms | Key sources (registry ids) | Author-gravity risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | anachoresis | 1 | y | – | y | y | y | – | – | F4-I, F5-P | retreat-as-escape; vacation | apotage, xeniteia, kellion, hesychia, cheironaxia, geron-abba-amma | vita-antonii; apophthegmata; palladius; kellia; nepheros; goehring | no (multi-stream; Nepheros stream caveated, Goehring consult-only with open verification bound) |
| 2 | apotage | 2 | – | y | – | y | y | – | – | F4-I, F5-T | one-time vow | anachoresis, koinonia | vita-antonii; pachomian-corpus; rousseau-pachomius | single corpus (Pachomian, consult-only scholarship channel) — flagged |
| 3 | hesychia | 1 | – | y | y | – | y | – | – | F4-P | mindfulness; hesychast method | anachoresis, nepsis, diakrisis | vita-antonii; apophthegmata | no |
| 4 | logismoi | 1 | y | – | y | y | y | y | – | F4-P | clinical symptom; distractions | diakrisis, apatheia, antirrhesis, theoria, nepsis | vita-antonii; evagrius; apophthegmata | taxonomy: single-author (Evagrius) — flagged |
| 5 | diakrisis | 1 | – | y | – | y | y | – | – | F4-I | trusting your gut; intuition | geron-abba-amma, logismoi, hesychia, nepsis, penthos, apophthegma | apophthegmata; cassian-conferences | no (cross-elder) |
| 6 | geron-abba-amma | 1 | – | y | – | – | y | y | – | F3-I, F6-P | life coach; formal office | diakrisis, koinonia, apophthegma, anachoresis | apophthegmata; palladius | amma material thin — flagged |
| 7 | cheironaxia | 1 | y | – | – | y | y | – | – | F5-I, F5-T | menial day-job | anachoresis | vita-antonii; palladius; nepheros; kellia; goehring | no (3 evidence types; Nepheros stream caveated - Melitian, intermediary organization, distant; Goehring consult-only with open verification bound) |
| 8 | apophthegma | 1 | y | – | – | y | y | – | – | F2-E | quotable aphorism; soundbite | geron-abba-amma, diakrisis | apophthegmata; burton-christie | compiler layer — flagged |
| 9 | koinonia | 1 | – | y | – | y | y | y | – | F3-I | loose fellowship; any monastery | apotage, geron-abba-amma | pachomian-corpus; palladius; sozomen; rousseau-pachomius | single corpus (Pachomian) — flagged |
| 10 | xeniteia | 2 | y | – | y | – | – | y | – | F5-P | travel; tourism | anachoresis | apophthegmata | no |
| 11 | apatheia | 2 | y | – | y | y | – | y | **y** | F4-P | apathy | logismoi, theoria, antirrhesis, puritas-cordis | evagrius; rubenson; gould | single-author (Evagrius) — flagged |
| 12 | theoria | 2 | y | – | y | y | – | y | – | F4-I | theory | apatheia, logismoi | evagrius | single-author — flagged |
| 13 | penthos | 2 | – | y | y | – | – | – | – | (none — deliberate) | depression; bereavement | diakrisis | apophthegmata | no |
| 14 | nepsis | 2 | y | – | y | y | – | y | – | F4-P | mindfulness | diakrisis, logismoi, hesychia | apophthegmata; evagrius | systematized register single-author — flagged |
| 15 | synaxis | 1 | – | y | – | – | y | y | – | F3-I, F4-I | generic church service | kellion | palladius; apophthegmata | no |
| 16 | kellion | 2 | y | – | – | – | y | – | – | F5-I, F5-E | prison cell; just a room | synaxis, anachoresis | kellia; palladius | no |
| 17 | antirrhesis | 3 | y | – | – | y | – | y | – | F2-I | affirmation technique; arguing with yourself | logismoi, apatheia | evagrius; socrates | single-author, single-text — flagged |
| 18 | puritas-cordis | 3 | – | y | – | y | – | y | – | F4-I | vague devotional phrase | apatheia | cassian-conferences; cassian-institutes | single-author (Cassian, export screen) — flagged |

## View: by tier

- **Retrieval tier 1 (core):** anachoresis, hesychia, logismoi, diakrisis, geron-abba-amma, cheironaxia, apophthegma, koinonia, synaxis (9)
- **Retrieval tier 2 (supporting):** apotage, xeniteia, apatheia, theoria, penthos, nepsis, kellion (7)
- **Retrieval tier 3 (reference):** antirrhesis, puritas-cordis (2)

## View: by tag (the filterable sets)

- **DR (high distortion risk):** anachoresis, hesychia, logismoi, xeniteia, apatheia, theoria, penthos, nepsis — every one carries a false_friend list and a translational sense doing the bridge work.
- **CT (contested tradition):** **apatheia only.** CT-check: its contest type IS specified, not templated — contested as to *historical scope* (whether Antony himself possessed the philosophical literacy this register presupposes: Rubenson vs. Gould), NOT as to whether the vocabulary belongs to this world; `formation_confidence: Contested` carries it, and the full contest becomes `desert.contested.antony-literacy` at step 3c. (This is Doc_06 §2.2's twice-corrected formulation, preserved.)
- **PV (plural voices):** logismoi (general vs. Evagrian-systematized), geron-abba-amma (abba vs. amma attestation asymmetry), koinonia (Strand B only), xeniteia, apatheia, theoria, nepsis (Strand C systematization), synaxis (Strand C name), antirrhesis, puritas-cordis (export screen).
- **RT (likely runtime):** anachoresis, apotage, hesychia, logismoi, diakrisis, geron-abba-amma, cheironaxia, apophthegma, koinonia, synaxis, kellion.

## Reciprocity check

The Related-Terms graph is 24 symmetric edges (matching Doc_06's independently re-derived 24-edge graph): anachoresis–{apotage, xeniteia, kellion, hesychia, cheironaxia, geron-abba-amma}; apotage–koinonia; hesychia–{nepsis, diakrisis}; logismoi–{diakrisis, apatheia, antirrhesis, theoria, nepsis}; diakrisis–{geron-abba-amma, nepsis, penthos, apophthegma}; geron-abba-amma–{koinonia, apophthegma}; apatheia–{theoria, antirrhesis, puritas-cordis}; synaxis–kellion. **Mechanically verified**: the M1 reciprocity gate passes over these records (every `associated-with` declared on both ends), so this index cannot silently drift from the records without the gate failing.

## Deliberate empty cells

*penthos* carries no canon_cells: no canon question maps to it tightly, and a loose thematic stretch would be forcing (its record body says so). It remains retrievable by its own retrieve_when.

## Review rounds note (applied)

Step3a Review Round 1 (`world-build-docs/desert/reviews/Step3a_Review_Round1.md`)
found the reciprocity graph, canon-cell mappings, and Doc_06 fidelity
(including the twice-corrected apatheia [CT] form) all genuinely clean
on independent re-derivation. Two substantial patterns were fixed: build-
infrastructure vocabulary ("vendored," "consult-only," "this corpus")
inside eight records' evidential senses, reworded to in-world evidence
talk; and two paraphrased sayings (kellion, apophthegma) that had been
rendered inside quotation marks despite their own bodies saying they were
not quotations — un-quoted. Cosmetic fixes: puritas-cordis's Conference I
locus corrected (~26147 -> ~26109); this index's antirrhesis row restored
its second false_friend; cheironaxia's world_word restored the Doc_06
"Ergocheiron" alternate form; antirrhesis's translational sense softened
an uncited claim; apatheia gained the Gould source registration matching
its own evidential-sense citation.

Step3a Review Round 2 (`world-build-docs/desert/reviews/Step3a_Review_Round2.md`)
independently re-verified those fixes and found the build-jargon sweep
had swept for the previously-named strings rather than the pattern:
apatheia's own Round 1 fix had traded "vendored/consult-only" for
"this corpus," the same family, and two more pre-existing instances
(koinonia's "in this lexicon," kellion's "no record here") had never
been caught. It also found the Round-1 theoria rewrite had swapped a
jargon problem for a factual overclaim, a scripture quote in nepsis
matching no vendored wording, and smaller punctuation/word-collision
items.

Step3a Review Round 3 (`world-build-docs/desert/reviews/Step3a_Review_Round3.md`)
was convened specifically because the same pattern had now survived
two "exhaustive" sweeps, and it repeated once more: xeniteia's and
penthos's evidential senses used this build's own "compiler screen"
label (not carried from Doc_06), nepsis's evidential sense used
"flag" (this build's own risk-marker word), and theoria's Round-2 fix
had itself introduced a fresh review-process phrase plus a *new*
factual overclaim about what English exists for Evagrius's
contemplative teaching. Round 3 also found the Institutes IV.43 ladder
had been mischaracterized in puritas-cordis (its true final rung is
"the perfection of apostolic love," not purity of heart) under the
lexicon's only citation_specificity A / verified-verbatim label - a
locus checked for its words at three prior passes, none of which
checked the words against the claim. What this means for a future
pass: do not sweep for named strings again - reread every sense field
fresh, and check every locus claim against what its passage actually
says, not only against where the quoted words sit.

Step3a Review Round 4 (`world-build-docs/desert/reviews/Step3a_Review_Round4.md`)
did exactly that - read all 72 sense fields fresh, detached from their
records, before running any sweep at all - and found two whole jargon
families no prior round had examined: lettered strand labels
("Strand B"/"Strand C", this build's own analytic taxonomy, unintelligible
with no legend in a standalone chunk) in six fields across five records,
and "the window" (this build's periodization parameter, no antecedent in
its own field) in two more. It also found two real sourcing/factual
defects unrelated to jargon: apotage mischaracterized Vita SS2-3 (the
land was given, not sold; the record reported a reserve "kept" for
Antony's sister as the passage's upshot when SS3, inside the cited span,
has him give that reserve away too), and cheironaxia built its strongest
corroboration claim on the Nepheros archive without either of the two
standing cautions that source's own record requires on every use
(the community is Melitian; its representativeness is an unverified
working assumption). All fixed, checked against the vendored files and
the step-2 source records directly, not against prior commit messages.

Step3a Review Round 5 (`world-build-docs/desert/reviews/Step3a_Review_Round5.md`)
found two more jargon survivors outside any prior sweep's named
strings (puritas-cordis's "export edge," sibling of "compiler screen";
antirrhesis's "checked," the verb Rounds 3-4 excised from its two
sibling clauses but left standing here) and confirmed the 15 vendored
loci then on record accurate in full context, as of that round's own
count (new sources registered in later rounds add further vendored
loci, checked at the round that adds them - this count is not
re-asserted as a running total going forward).
Four substantial findings, two of them Round 4's own illusory-fix
recurrences: cheironaxia's Round-4 fix had invented "a nearby
community" for Nepheros, when the archive's community actually sat
~200-250km away in Middle Egypt, re-strengthening on a distance axis
the corroboration overclaim the fix meant to soften (corrected to
state no proximity); and the same record's Round-4 fix restored only
one of Nepheros's two standing cautions, leaving the "intermediary"
organizational-type complication off the record entirely, including
its informational sense (both cautions now carried in both senses and
the source row). A wholly new class - citation-completeness, distinct
from locus-accuracy - surfaced in anachoresis: its embeddedness claim
paraphrased Goehring without registering him against the standing
"cite Kellia + Nepheros + Goehring jointly" rule, and its martyrdom-
successor claim carried no locus at all, though a search record exists
specifically to anchor one (Vita SS46-47); both fixed by registering
the missing sources rather than rewording claims they already
supported. And puritas-cordis's Round-4 fix had installed "in his own
words" - the exact phrase Round 4's own fix had just removed from
antirrhesis in the same commit - a fifth consecutive illusory-fix
recurrence, corrected per the Conferences source record's own standing
attribution rule. Two invented/substituted details also fixed: apotage's
"days later" (the Life gives no interval) and synaxis's "resident
elders" (Palladius's own text names eight priests, an office - the
lexicon's office-vs-elder distinction is now consistent across
geron-abba-amma, koinonia, and synaxis alike).

Step3a Review Round 6 (`world-build-docs/desert/reviews/Step3a_Review_Round6.md`)
read all 72 sense fields cold, a third time, and found the jargon
pattern genuinely clear for the first time in six rounds - all five
prior families absent, and Round 5's own two jargon fixes held with no
new instance written in. What remained was a different, narrower
recurring signature: a citation-completeness fix applied to the record
where a finding was written and not swept to the sibling carrying the
identical claim. cheironaxia's translational and informational senses
state the same embeddedness claim Round 5 fixed on anachoresis, but
cheironaxia's own Nepheros row - edited in that same Round 5 commit -
still lacked Goehring; anachoresis's own evidential sense separately
named Palladius as an attesting stream without Palladius ever being
registered. Round 5's own cheironaxia fix also compressed the Nepheros
record's second caution into "organizationally distinct," inverting
Doc_02's actual working assumption (which holds the opposite);
reworded to match the correct caution already stated in the same
record's evidential sense. And apotage's evidence for the Pachomian
property-renunciation claim named the wrong channel: Palladius ch.
XXXII and Sozomen III.14, read in full, give the tablet-rule and a
three-year probation, not property renunciation - the claim's actual
channel is the Latin Rule tradition, per the Pachomian source record's
own standing rule to name it. Cosmetic: the master table's delimiter
row had 14 cells to the header's 15 and did not render as a table at
all, present since the draft and missed by five rounds - fixed; two
index cells (anachoresis's key-sources and author-gravity) updated to
match its now six-source record; puritas-cordis's index cells matched
to "export screen," the label the apparatus itself actually uses,
since the record's own "export edge" was excised in Round 5.

Step3a Review Round 7 (`world-build-docs/desert/reviews/Step3a_Review_Round7.md`)
independently re-confirmed the jargon pattern clear on a second cold
read of all 72 sense fields plus 108 other compiled-facing fields, and
re-verified Round 6's four fixes against the underlying sources rather
than the diff (Palladius XXXII/Sozomen III.14 read in full again;
Doc_02 SS5.2 re-opened for the wording-inversion fix). What it found
was the same "fix where written, not swept to the sibling" signature
one layer deeper, plus two standing-rule sweeps no prior round had
run to completion: anachoresis's own new Nepheros row (added in the
commit that fixed cheironaxia's missing second caution) carried only
the first of that source's two mandatory cautions - added; the
Round-6 apotage fix moved its claim onto "modern scholarship" without
registering any scholarship source, though desert.source.rousseau-
pachomius names itself as exactly that authority - registered on
apotage and, for the identical pre-existing gap, on koinonia; Goehring's
own source record says his verification bound "travels with every
citation," and neither citing record (anachoresis, cheironaxia) carried
it - added to both, alongside the almsgiving claim cheironaxia's own
Goehring locus had over-attributed to him (corrected to his source
record's actual wording). Two directions swept for the first time:
the Apophthegmata's own "compiler screen" standing rule, honored by
only 3 of the 10 records citing that source - added to the two records
where the gap sat on a live claim (diakrisis's cross-settlement
recurrence, geron-abba-amma's structure-as-evidence); and a "three
removes from the Coptic" count that had attached to the wrong link in
the Pachomian transmission chain, corrected against Doc_02 SS1.2's own
stated chain. Cosmetic: anachoresis's and apotage's index cells
updated for their newly-registered sources; the Round-5 paragraph's
"locus-verification is now complete" line reworded, since a later
round's own new registrations had already made the count stale by the
time it was written.

Step3a Review Round 8 (`world-build-docs/desert/reviews/Step3a_Review_Round8.md`)
changed method: rather than another spot-check, it read all 24 source
records end to end, extracted every standing rule they state (30 in
total), and checked each against every term record citing that source
at claim level - a durable matrix (the review's section C) rather than
another round of incremental discovery. Result: the standing-rule
application problem is closed, with no unswept sibling left. It found
two residual items instead. The Round 7 fix correcting apotage's
translation-chain count had itself written "this build" into the
evidential sense - the corpus/build self-reference family excised in
Rounds 1-3, reintroduced after two consecutive rounds had confirmed it
clear; a sixth illusory-fix recurrence, fixed by deleting the two
words. And a genuine inconsistency in where standing-rule caveats had
been landing - Round 4/5 required sense-level carriage (what a hearer
or compiled output actually gets), Round 7 had instead written new
caveats into `locus` fields (never compiled) - resolved by ruling for
sense-level carriage as this lexicon's standard (recorded in
DECISION-LOG.md) and bringing anachoresis, cheironaxia, and diakrisis
up to it. One cosmetic nit: koinonia's Rousseau locus named a narrower
claim-type than the claim it was actually covering.

## Author-gravity column basis

"Flagged" entries reproduce each record's own stated risk (single-author concentration for the Evagrian cluster and Cassian; the compiler layer for the sayings; the amma thinness bound) — the column is read off the records' sources/bodies, not asserted independently.
