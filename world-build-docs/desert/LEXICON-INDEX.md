# Desert Monasticism — Lexicon Master Index (step 3a)

**Derived from:** the 18 term records in `records/desert/term/` (this index is generated against those files and re-checked against them; the records are the source of truth). Re-derivation base: the prior build's cleared Doc_06 (`World-Builds/Desert-Monasticism/CiC_W3_Doc06_Full_Lexicon.md`, three review rounds, 24-edge reciprocity graph verified there) — carried into the new record schema with senses rewritten to the four-register shape and FK-gated plain fields.

**Tier mapping:** Doc_06 lexicon tiers → `retrieval.tier`, with two recorded divergences: *apotagē* (Doc_06 Tier 1 → retrieval tier 2; supporting rather than core retrieval weight, noted in its record body) and *synaxis* (Doc_06 Tier 2 → retrieval tier 1; the F3-I gathering question retrieves it directly, noted in its record body).

**Tags** carried from Doc_06: AS = Signature Vocabulary · SC = Shared Vocabulary · DR = High Distortion Risk · TC = Technical Concept · RT = Likely Runtime Term · PV = Plural Voices · CT = Contested Tradition.

## Master table

| # | Term (record slug) | Tier | AS | SC | DR | TC | RT | PV | CT | canon_cells | False friends (aliases) | Related terms | Key sources (registry ids) | Author-gravity risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | anachoresis | 1 | y | – | y | y | y | – | – | F4-I, F5-P | retreat-as-escape; vacation | apotage, xeniteia, kellion, hesychia, cheironaxia, geron-abba-amma | vita-antonii; apophthegmata; kellia | no (multi-stream) |
| 2 | apotage | 2 | – | y | – | y | y | – | – | F4-I, F5-T | one-time vow | anachoresis, koinonia | vita-antonii; pachomian-corpus | no |
| 3 | hesychia | 1 | – | y | y | – | y | – | – | F4-P | mindfulness; hesychast method | anachoresis, nepsis, diakrisis | vita-antonii; apophthegmata | no |
| 4 | logismoi | 1 | y | – | y | y | y | y | – | F4-P | clinical symptom; distractions | diakrisis, apatheia, antirrhesis, theoria, nepsis | vita-antonii; evagrius; apophthegmata | taxonomy: single-author (Evagrius) — flagged |
| 5 | diakrisis | 1 | – | y | – | y | y | – | – | F4-I | trusting your gut; intuition | geron-abba-amma, logismoi, hesychia, nepsis, penthos, apophthegma | apophthegmata; cassian-conferences | no (cross-elder) |
| 6 | geron-abba-amma | 1 | – | y | – | – | y | y | – | F3-I, F6-P | life coach; formal office | diakrisis, koinonia, apophthegma, anachoresis | apophthegmata; palladius | amma material thin — flagged |
| 7 | cheironaxia | 1 | y | – | – | y | y | – | – | F5-I, F5-T | menial day-job | anachoresis | vita-antonii; palladius; nepheros; kellia | no (3 evidence types) |
| 8 | apophthegma | 1 | y | – | – | y | y | – | – | F2-E | quotable aphorism; soundbite | geron-abba-amma, diakrisis | apophthegmata; burton-christie | compiler layer — flagged |
| 9 | koinonia | 1 | – | y | – | y | y | y | – | F3-I | loose fellowship; any monastery | apotage, geron-abba-amma | pachomian-corpus; palladius; sozomen | single corpus (Pachomian) — flagged |
| 10 | xeniteia | 2 | y | – | y | – | – | y | – | F5-P | travel; tourism | anachoresis | apophthegmata | no |
| 11 | apatheia | 2 | y | – | y | y | – | y | **y** | F4-P | apathy | logismoi, theoria, antirrhesis, puritas-cordis | evagrius; rubenson | single-author (Evagrius) — flagged |
| 12 | theoria | 2 | y | – | y | y | – | y | – | F4-I | theory | apatheia, logismoi | evagrius | single-author — flagged |
| 13 | penthos | 2 | – | y | y | – | – | – | – | (none — deliberate) | depression; bereavement | diakrisis | apophthegmata | no |
| 14 | nepsis | 2 | y | – | y | y | – | y | – | F4-P | mindfulness | diakrisis, logismoi, hesychia | apophthegmata; evagrius | systematized register single-author — flagged |
| 15 | synaxis | 1 | – | y | – | – | y | y | – | F3-I, F4-I | generic church service | kellion | palladius; apophthegmata | no |
| 16 | kellion | 2 | y | – | – | – | y | – | – | F5-I, F5-E | prison cell; just a room | synaxis, anachoresis | kellia; palladius | no |
| 17 | antirrhesis | 3 | y | – | – | y | – | y | – | F2-I | affirmation technique | logismoi, apatheia | evagrius; socrates | single-author, single-text — flagged |
| 18 | puritas-cordis | 3 | – | y | – | y | – | y | – | F4-I | vague devotional phrase | apatheia | cassian-conferences; cassian-institutes | single-author (Cassian, export edge) — flagged |

## View: by tier

- **Retrieval tier 1 (core):** anachoresis, hesychia, logismoi, diakrisis, geron-abba-amma, cheironaxia, apophthegma, koinonia, synaxis (9)
- **Retrieval tier 2 (supporting):** apotage, xeniteia, apatheia, theoria, penthos, nepsis, kellion (7)
- **Retrieval tier 3 (reference):** antirrhesis, puritas-cordis (2)

## View: by tag (the filterable sets)

- **DR (high distortion risk):** anachoresis, hesychia, logismoi, xeniteia, apatheia, theoria, penthos, nepsis — every one carries a false_friend list and a translational sense doing the bridge work.
- **CT (contested tradition):** **apatheia only.** CT-check: its contest type IS specified, not templated — contested as to *historical scope* (whether Antony himself possessed the philosophical literacy this register presupposes: Rubenson vs. Gould), NOT as to whether the vocabulary belongs to this world; `formation_confidence: Contested` carries it, and the full contest becomes `desert.contested.antony-literacy` at step 3c. (This is Doc_06 §2.2's twice-corrected formulation, preserved.)
- **PV (plural voices):** logismoi (general vs. Evagrian-systematized), geron-abba-amma (abba vs. amma attestation asymmetry), koinonia (Strand B only), xeniteia, apatheia, theoria, nepsis (Strand C systematization), synaxis (Strand C name), antirrhesis, puritas-cordis (export edge).
- **RT (likely runtime):** anachoresis, apotage, hesychia, logismoi, diakrisis, geron-abba-amma, cheironaxia, apophthegma, koinonia, synaxis, kellion.

## Reciprocity check

The Related-Terms graph is 24 symmetric edges (matching Doc_06's independently re-derived 24-edge graph): anachoresis–{apotage, xeniteia, kellion, hesychia, cheironaxia, geron-abba-amma}; apotage–koinonia; hesychia–{nepsis, diakrisis}; logismoi–{diakrisis, apatheia, antirrhesis, theoria, nepsis}; diakrisis–{geron-abba-amma, nepsis, penthos, apophthegma}; geron-abba-amma–{koinonia, apophthegma}; apatheia–{theoria, antirrhesis, puritas-cordis}; synaxis–kellion. **Mechanically verified**: the M1 reciprocity gate passes over these records (every `associated-with` declared on both ends), so this index cannot silently drift from the records without the gate failing.

## Deliberate empty cells

*penthos* carries no canon_cells: no canon question maps to it tightly, and a loose thematic stretch would be forcing (its record body says so). It remains retrievable by its own retrieve_when.

## Author-gravity column basis

"Flagged" entries reproduce each record's own stated risk (single-author concentration for the Evagrian cluster and Cassian; the compiler layer for the sayings; the amma thinness bound) — the column is read off the records' sources/bodies, not asserted independently.
