# syr — Forces index (Doc_08 six-cell matrix, record-native)

Derived from `records/syr/force/` (13 records re-expressing the approved Doc_08, 2026-07-08). One row per force; connections are declared as typed record relations, so the reciprocity gate keeps this index from drifting.

| force record | cell | kind | confidence (L1) | connected gravities | cross-cell connections | transmission |
|---|---|---|---|---|---|---|
| `frontier-plural-milieu` | 1A | initiating/ext | Widely Accepted (DMR for the periphery characterization) | C1 raza-shrara-method · C3 heresiological (assoc) | → 2A-2 rival-movements | — |
| `two-empires-frontier` | 1A | initiating/ext | Widely Accepted | C3 · C6 (assoc) | → 3A-1 yazdegerd-toleration | — |
| `raza-inheritance` | 1B | initiating/int | Documented (Ephrem) / DMR (inherited-disposition synthesis) | C1 (precondition-for) | → 2A-2 (intensification path) | — |
| `qyama-commitment` | 1B | initiating/int | Widely Accepted (Inferential-Thin on pre-337 depth) | C2 (precondition-for) | none (C2 held; none manufactured) | — |
| `diatessaron-adoption` | 1B | initiating/int | Documented | C5 (precondition-for) | → 3B-2 transmission-ending | — |
| `shapur-persecution` | 2A | ongoing/ext | Widely Accepted–Documented (dates Contested) | C6 (precondition-for) · C4 (assoc: fractures) | → 2B-1 | — |
| `rival-movements` | 2A | ongoing/ext | Documented | C1 (assoc: intensifies) · C3 (precondition-for) | → 1A-1 | — |
| `authority-ambiguity-condition` | 2B | ongoing/int | WA–Documented facts / Contested-Thin lived reality | C4 (assoc: coextensive — Doc_08's named exception) | → 2A-1 | — |
| `transmission-ongoing` | 2B | ongoing/int | Documented (witnesses) / WA (selection reading) | — (shapes what survives, not a gravity) | → 3B-2 | **yes (required 2B entry)** |
| `yazdegerd-toleration` | 3A | ending/ext | Widely Accepted (succession dates Contested-Thin) | — (hinge) | → 3A-2 (precondition-for) | — |
| `synod-410` | 3A | ending/ext | WA–Documented (Bar Hebraeus template claim DMR) | C4 (assoc: external resolution) | ← 3A-1 · → 3B-1 | — |
| `institutional-consolidation` | 3B | ending/int | DMR (this build's own flagged synthesis) | C4 (assoc) | ← 3A-2 | — |
| `transmission-ending` | 3B | ending/int | WA (timeline) / Contested (Rabbula's role) / Documented (legend layer's 6th-c. dating) | C5 (assoc: explains its non-survival) | ← 1B-3 · ↔ 2B-2 | **yes (required 3B entry)** |

**By connected gravity (completion check — every Doc_04 gravity traces to ≥1 force):**
- C1 raza-shrara-method ← raza-inheritance (enabled-by), rival-movements, frontier-plural-milieu
- C2 covenant-life ← qyama-commitment (enabled-by) — Doc_04's own finding: C2 *held*; no other force-dynamic evidenced or manufactured
- C3 heresiological-self-definition ← rival-movements (enabled-by), frontier-plural-milieu, two-empires-frontier
- C4 authority-ambiguity ← authority-ambiguity-condition, shapur-persecution (fracture), synod-410, institutional-consolidation
- C5 diatessaron-normative ← diatessaron-adoption (enabled-by), transmission-ending
- C6 persecution-endurance ← shapur-persecution (enabled-by), two-empires-frontier

**Transmission check:** dedicated entries exist in both 2B (`transmission-ongoing`) and 3B (`transmission-ending`), never folded into another force.

**Confidence roll-up:** Contested/Inferential-Thin material is quarantined where Doc_08 put it — the chronicle-derived succession dates (2A-1, 3A-1), the lived interior of the authority ambiguity (2B-1), Rabbula's personal causal role (3B-2 → `syr.contested.rabbula-peshitta`), and the two flagged own-syntheses (1B-1's inherited-disposition claim; 3B-1 entire, at DMR).

**Contested-claim register (built this step):** bardaisan-nicene-floor (F1-I) · aphrahat-episcopacy (F3-I) · papa-primacy (F3-I) · qyama-structure (F4-I) · edessa-origins (F2-E) · rabbula-peshitta (no cell — post-horizon, deliberate) · diatessaron-name (no cell — build-vocabulary contest, deliberate) · jacob-death-year (no cell — dating conflict, deliberate). The three empty-cell records state their emptiness rationale in their own bodies, per the canon-cells discipline.
