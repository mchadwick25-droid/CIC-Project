# Retrieval Architecture: CiC's Actual Stack Measured Against Current RAG Practice

**Method note.** Every external claim below was read on 2026-07-25/26 from the vendor engineering page, published paper, or framework documentation of record, and is confidence-rated. Items I could not verify are listed at the end under "Do not cite." CiC's own stack was read first, in full and directly, not through doc 08's summary of it: `cic-poc/backend/app/rag/{retriever.py, story_retriever.py, batch_evaluate.py, indexer.py, story_indexer.py, embeddings.py}`, `app/config.py`, the call sites in `app/graph/nodes.py`, and all 104 lexicon chunks plus 58 story chunks across six worlds. Where doc 08 already established a fact I re-measured it rather than restating it, and I flag where my numbers extend or refine its numbers.

**Two facts about the running stack that the earlier research did not record, and that change what the right fix is:**

- The generation model is `claude-sonnet-5` (`app/config.py:55`); every classifier and the retrieval filter are `claude-haiku-4-5-20251001`.
- The embedding model is `all-MiniLM-L6-v2`, loaded locally on CPU (`app/rag/embeddings.py:20`). **Its maximum sequence length is 256 word-pieces** — verified not from documentation but from the config file the running code actually loads: `~/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2/snapshots/.../sentence_bert_config.json` contains `{"max_seq_length": 256, "do_lower_case": false}`.

---

## Summary — the five findings that matter, ranked by how directly they fix a problem doc 08 already found

**1. The retrieval index is silently truncating roughly 85% of an Alexandria chunk, and the `Retrieve-When` text is not in the index at all. This is the mechanical cause of doc 08 §3's "retrieval for those three worlds is essentially pure vector similarity," and it is worse than that finding stated.**

`indexer.py:187-193` builds the embedded text as `Term:` + `Aliases:` + `Related:` + `entry.content`, where `entry.content` is `content.split("---", 2)[2]`. Two consequences, both verified against real files:

- **`Retrieve-When` and `Do-Not-Retrieve-When` are never embedded.** They live in `parts[0]` (inside the fenced front-matter block), which is discarded from `main_content`, and they survive only as FAISS *metadata* — read later by the LLM filter, never by the vector search. The single most retrieval-relevant field an author writes per chunk contributes nothing to whether the chunk is a candidate in the first place. `story_indexer.py:133-139` has the identical shape.
- **The embedding sees only the first ~256 word-pieces of what remains.** Alexandria's lexicon chunks average 1,249 words (I measured 56,198 words across 45 files); `alexlex001_logos.md` runs 1,767. After ~40 tokens of `Term/Aliases/Related`, roughly the first 150–170 words of `## World Meaning` are embedded and everything after — the rest of World Meaning, all of Ecological Function, Distortion Risk, Key Sources — is invisible to similarity search. So the vector for a 1,767-word chunk is a vector for its opening paragraph.

This means the "pure vector similarity" the three all-Tier-1 worlds fall back on is *pure opening-paragraph similarity*, computed by a 384-dimension 2021-era model, with the author's own trigger conditions excluded. **Verdict: REAL GAP, and the highest-severity item in this document.** **Confidence: High** on both mechanisms (read the code; read the model's own config file). **Medium** on the exact cutoff word count — 256 word-pieces is not 256 words, and the ratio differs for Greek and Syriac script; the confirmation step is one script, given in the recommendations.

**2. `Retrieve-When` conditions have a real, current name in the retrieval literature — instruction-following retrieval — and there is a published model class built to consume exactly this, which CiC's stack cannot use because its conditions never reach the retriever.** Promptriever (Weller et al., [arXiv:2409.11136](https://arxiv.org/abs/2409.11136)) is a retriever "able to be prompted like an LM," trained on ~500k instance-level instructions, that "adapt[s] its definition of relevance based on detailed natural language prompts." Two benchmarks exist specifically for this — **FollowIR** and **InstructIR** — and Promptriever reports +14.3 p-MRR on FollowIR and +12.9 Robustness@10 on InstructIR. CiC independently invented the *authoring* half of a real, named, benchmarked research direction and then routed it to an LLM post-filter instead of to the retriever. **Verdict: PARTIAL — WORTH ADOPTING (the pattern is real and validated; CiC's plumbing of it is not).** **Confidence: High** on the paper and benchmark names; **Medium** on the specific metric deltas (abstract-level, not reproduced).

**3. Anthropic's own published contextual-retrieval guidance says CiC's knowledge bases are small enough that five of six worlds do not need retrieval at all — and CiC's own discarded `Quick Meaning` field is the field that makes that affordable.** [Anthropic's contextual retrieval post](https://www.anthropic.com/engineering/contextual-retrieval) states plainly: "If your knowledge base is smaller than 200,000 tokens (about 500 pages of material), you can just include the entire knowledge base in the prompt." Measured per world (lexicon + story chunks, approximate at chars/4):

| world | lexicon chunks | story chunks | whole-world corpus ≈ tokens | complete Quick Meaning set ≈ tokens |
|---|---|---|---|---|
| desert | 9 | 8 | 13,000 | **0 — none authored** |
| hieronymian | 15 | 12 | 15,700 | 588 |
| imperial-juridical | 12 | 6 | 16,700 | 583 |
| syriac | 10 | 9 | 23,400 | 854 |
| pahc | 13 | 13 | 26,400 | 613 |
| **alexandria** | **45** | **10** | **101,600** | **4,000** |

Every world is under the 200K threshold; five are under 27K. And the layer the template designed for exactly this — `## Quick Meaning`, which the template says "Does not require the full entry to be surfaced" and which `indexer.py:117-118` silently drops — is **588 to 4,000 tokens for a world's *complete* term set**. Against a Sonnet 5 input rate of $3/MTok, Alexandria currently injects ~6,700 tokens of uncacheable retrieved context per turn (~$0.020); its entire 45-term Quick Meaning layer, riding inside the already-cached static prefix at the 0.1× cache-read rate, costs ~$0.0012 per turn. Cheaper by an order of magnitude, and **all 45 terms are present instead of 3**. **Verdict: REAL GAP — and the one place in this document where quality, cost, and the register-leak problem are one fix.** **Confidence: High** on the Anthropic guidance and my measured counts; **Medium** on the token figures (chars/4 approximation, and Greek/Syriac script tokenizes worse than English — re-measure with `count_tokens` before costing).

**4. Hybrid dense+sparse retrieval is a fair read of the Term-formatting problem, and Anthropic's own numbers quantify the gain — but the honest diagnosis is narrower than doc 08's framing.** Contextual embeddings alone cut retrieval failures 35% (5.7%→3.7%); adding contextual BM25 takes it to 49% (→2.9%); adding reranking to 67% (→1.9%). The cookbook implementation weights semantic 0.8 / BM25 0.2 and reports that in the hybrid configuration BM25 supplies 45.4% of surfaced results. **But** the specific failure doc 08 §3.2 documents — `label.lower() in context_lower` firing constantly for Alexandria (`Logos`, `Theosis`) and never for Syriac (`raza (ܐܪܙܐ) / shrara`) — is a *de-duplication guard*, not a retrieval matcher, and BM25 does not fix it. Hybrid retrieval fixes the adjacent problem (a participant who names `episkopos` or `qyama` verbatim currently has no lexical channel to surface it); the de-dup guard needs a different, also-standard fix. **Verdict: PARTIAL — WORTH ADOPTING, with the diagnosis corrected.** **Confidence: High** (read the engineering post and the cookbook implementation).

**5. `evaluate_batch` is a real, named pattern — the *retrieval evaluator* / relevance grader from Corrective RAG and Self-RAG — and its "uniform literal keyword-matching when Tier 2/3 dilutes the batch" failure is a known artifact of the batched-listwise prompt shape, not of the idea.** CRAG's retrieval evaluator grades each retrieved document and triggers corrective actions; Self-RAG trains reflection tokens (`[IsRel]`, `[IsSup]`) for the same job. So CiC's approach is legitimate and precedented. The failure mode is specific: CiC asks for *independent per-candidate binary labels* inside a *single shared listwise prompt*, and cross-candidate contamination in exactly that shape is why the code already had to split Tier 1 into its own call (`batch_evaluate.py:126-149`). The cheaper standard alternative is a cross-encoder: on production benchmarks "a calibrated pointwise cross-encoder matches or beats listwise LLM rerankers at 100×–1000× lower cost and latency," and a specialized reranker costs ~$0.025/1M tokens. CiC already has `sentence-transformers` loaded locally — a CPU cross-encoder is a zero-marginal-cost drop-in. **Verdict: ALREADY DOES THIS (the pattern), REAL GAP (the mechanism).** **Confidence: High** on CRAG/Self-RAG; **Medium** on the 100×–1000× figure (vendor blog, not a peer-reviewed benchmark).

---

## 1. Anthropic's contextual retrieval

**What it is.** Before embedding a chunk, prepend 50–100 tokens of LLM-generated context situating that chunk in its parent document, and index the contextualized text in *both* the embedding store and a BM25 store. The cookbook's exact generation prompt is:

> "Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk. Answer only with the succinct context and nothing else."

The document is passed with `cache_control: ephemeral` so the whole-document tokens are cached across all of its chunks; the cookbook runs this on `claude-haiku-4-5` at `temperature=0.0`, `max_tokens=1000`, and reports ~$1.02 per million document tokens with caching (measured: $2.85 vs $9.20 for a 737-chunk corpus — 69% saving).

**Published results** (248 queries, 737 chunks across 9 codebases, Pass@K):

| configuration | Pass@5 | Pass@10 | Pass@20 |
|---|---|---|---|
| baseline embeddings | 80.92% | 87.15% | 90.06% |
| + contextual embeddings | 88.12% | 92.34% | 94.29% |
| + contextual BM25 | 88.86% | 92.31% | 95.23% |
| + reranking (Cohere rerank-english-v3.0, retrieve 10k → keep k) | 92.15% | **95.26%** | 97.45% |

**Does CiC already do anything like this?** Partly, and by accident of a different design. Contextual retrieval exists because small chunks lose their document context. CiC's chunks are whole files with a `Term:` header — so they are *already* self-contained in the way contextual retrieval is trying to manufacture. **On that axis CiC does not need it.**

But CiC has the inverse problem, and it is the one finding #1 names: its chunks are so large that the embedding model truncates them. Contextual retrieval's real applicability to CiC is therefore **inverted** — the value is not in adding a generated context header, it is in the fact that the technique presupposes chunks small enough to embed whole. And CiC already possesses a hand-authored version of the summary contextual retrieval generates with an LLM: `## Quick Meaning`. A 60-word human-written `Quick Meaning`, plus the `Term`, `Aliases`, and `Retrieve-When` fields, is *exactly* a contextualized chunk header — and it is 250–350 word-pieces, i.e. right at the embedding budget, rather than 5× over it.

One honest gap in the data: **Desert has no `Quick Meaning` sections at all** (0 of 9 chunks; every other world has one per chunk — alexandria 45/45, hieronymian 15/15, imperial-juridical 12/12, pahc 13/13, syriac 10/10). Desert is also the world with the worst confirmed fabrication record. That is not a coincidence worth asserting causally, but it is a build-completeness gap that this recommendation depends on closing.

**Verdict: PARTIAL — WORTH ADOPTING, in a form CiC almost has.** Don't generate contextual headers with an LLM; index the human-authored `Quick Meaning` + `Term` + `Aliases` + `Retrieve-When` as the *embedded* text, and keep the full body as retrievable payload rather than as index input. **Confidence: High** (engineering post and cookbook read directly; CiC measurements are my own).

---

## 2. Hybrid retrieval (dense + sparse)

**The standard shape.** Two independent indexes — a dense embedding index and a sparse lexical index (BM25, or a learned sparse model like SPLADE) — over-retrieved separately and fused. **Reciprocal Rank Fusion** is the default fusion method because it "ignores the scores and focuses only on the rank of the document in each result list," which removes the need to calibrate two incomparable score scales. RRF computes `1/(rank + k)` per list and sums; `k = 60` is the conventional constant and is hardcoded in LangChain's `EnsembleRetriever`.

**Reported gains.** On the WANDS e-commerce benchmark a tuned hybrid reaches 0.7497 nDCG against 0.6983 (BM25 alone) and 0.6953 (vector alone) — a ~7.4% lift over either. Anthropic's own measurement (§1 above) is a 14-point-of-failure-rate improvement from adding contextual BM25 on top of contextual embeddings. Fusion-weight tuning is genuinely contested: Anthropic's cookbook uses weighted RRF at semantic 0.8 / BM25 0.2, while one 2026 text-and-table benchmark found a convex combination at α=0.5 beat RRF with k=10 (Recall@5 0.726 vs lower) — so treat the weights as something to sweep, not import.

**Is doc 08's read fair — is the Term-field-formatting problem the kind of thing hybrid retrieval smooths out?** Partly, and the distinction matters for what to build.

*Fair.* Six worlds format the `Term:` field incompatibly — `episkopos (ἐπίσκοπος)`, `Diakrisis (Discernment)`, `raza (ܐܪܙܐ) / shrara`, versus bare `Logos` / `Theosis`. Today the *only* channel by which a participant's exact word can surface a chunk is a 384-dimension MiniLM cosine over a truncated opening paragraph. A participant who writes "what does *qyama* mean" has no lexical path to `syrlex002_qyama.md`. BM25 over `Term` + `Aliases` + `Related-Terms` + body is precisely the missing channel, and CiC's `Aliases` field — already parsed with real care in `indexer.py:132-162`, extracting quoted glosses and transliterations separately — is an unusually good sparse-index field that nothing currently searches.

*Not fair.* The specific live failure doc 08 attributes to Term formatting — "Albina and Papnoute each reached for the same story twice" (commit `1252fd4`) — runs through `partition_tier1_short_circuit`'s `already_discussed = label.lower() in context_lower` (`batch_evaluate.py:78`). That is a *repetition guard*, and BM25 does not touch it. The standard fix for redundancy in a selected set is **Maximal Marginal Relevance** (Carbonell & Goldstein, 1998), which scores each candidate as a λ-weighted trade-off between query relevance and maximum similarity to already-selected items, and whose "clearest advantage is demonstrated in constructing non-redundant multi-document summaries." For turn-to-turn repetition rather than within-turn, the analogous mechanism is a session-level exclusion set keyed on stable chunk IDs — CiC already has stable, never-reused IDs (`desertstory002`, `alexlex001_logos.md`), so this is a set membership test, not a substring match against a title nobody says.

**Verdict: REAL GAP on the sparse index; the diagnosis needs splitting.** Add BM25 + RRF for the lexical-match gap; add MMR and an ID-keyed session exclusion set for the repetition gap. They are different problems that doc 08 read as one. **Confidence: High** on RRF and MMR as standard practice; **Medium** on the optimal fusion weights (genuinely contested in the 2026 literature).

---

## 3. Re-ranking

**The standard shape.** Over-retrieve cheaply (Anthropic's cookbook: 150 per source, or 10× the target `k`), then re-score the candidate set with a model that sees query and document *together* — a cross-encoder — and keep the top `k`. Anthropic's own numbers put reranking's marginal contribution at 88.86%→92.15% Pass@5 on top of contextual hybrid search, at "+100-200ms per query" and "~$0.002 per query."

**Is CiC's `evaluate_batch` a reasonable, real pattern, and what is it called?** Yes, and it has two names depending on which literature you're in:

- In the agentic-RAG literature it is a **retrieval evaluator** or **relevance grader**. CRAG (Corrective RAG) "adds a retrieval evaluator that grades retrieved documents and triggers corrective actions… grade each document as Correct/Ambiguous/Incorrect." Self-RAG trains the same judgment into the model as reflection tokens (`[Retrieve]`, `[IsRel]`, `[IsSup]`, `[IsUse]`). CiC's binary `RETRIEVE`/`SKIP` with a brief reason is a two-value version of CRAG's three-value grade.
- In the IR literature it is **LLM reranking**, subdivided into *pointwise* (score each document independently) and *listwise* (emit a permutation over a candidate list — RankGPT is the canonical instance). CiC's `_run_batch` is a hybrid that the literature does not have a clean name for: it asks for **independent pointwise labels delivered inside a single shared listwise prompt**.

That hybrid is where the failure comes from. The comment at `batch_evaluate.py:126-135` records it precisely — Tier 1 terms judged alone retrieve correctly on a foundational question without literal keyword overlap; "mixed into a 6-candidate batch dominated by peripheral Tier 2/3 terms, the model reverted to uniform literal keyword-matching across the whole batch and the exception was lost." A single prompt containing multiple candidates makes them mutually visible; the model regresses to a consistent policy across the visible set. The Tier-1 split is a workaround for the prompt shape, and doc 08 §3.1 shows it is inert for exactly the three worlds that need it most: with every chunk Tier 1, there is nothing to split from.

**Is there a more standard, cheaper approach that also fixes the dilution?** Yes, and it fits CiC's existing dependency tree with no new vendor. A cross-encoder scores each (query, document) pair in an **independent forward pass** — the candidates are structurally unable to contaminate each other, which is precisely the dilution failure, eliminated by construction rather than by a prompt split. The published trade-off: LLM listwise reranking can be "5-8% higher accuracy… but adds 4-6 seconds of latency" and costs far more, while "on most production RAG benchmarks, a calibrated pointwise cross-encoder matches or beats listwise LLM rerankers at 100×-1000× lower cost and latency"; a dedicated reranker runs ~$0.025/1M tokens against frontier-LLM rates. CiC already loads `sentence-transformers` on CPU for embeddings (`embeddings.py`), so a local cross-encoder is a zero-marginal-cost, zero-new-vendor addition, and it removes two Haiku calls per world per turn from the latency critical path.

There is also a real, published cheap-grader result: [*Lightweight Relevance Grader in RAG*](https://arxiv.org/pdf/2506.14084) (arXiv 2506.14084) is a paper about exactly this substitution — a small fine-tuned model matching a large LLM at grading retrieved-document relevance, evaluated on recall/precision/F1. I could not extract its numeric results (see "Do not cite"), so I cite it only as evidence that the substitution is an actively studied pattern, not for any figure.

**One thing to preserve.** A cross-encoder scores *semantic relevance*. It cannot read `Do-Not-Retrieve-When: participant is using "logos" in an unrelated modern/linguistic sense with no theological bearing`. That judgment genuinely needs a language model, or a structural replacement (§6). Do not delete the LLM grader; demote it to the cases where its judgment is the thing being bought.

**Verdict: ALREADY DOES THIS on the pattern (it is CRAG's retrieval evaluator, legitimately). REAL GAP on the mechanism — the batched-listwise prompt shape is the source of a failure the code has already fought three times and lost, and the standard alternative is cheaper, faster, and immune to it by construction.** **Confidence: High** on CRAG/Self-RAG/cross-encoder mechanics; **Medium** on the cost/latency multipliers (vendor blog sources).

---

## 4. GraphRAG / knowledge-graph-augmented retrieval

**What it is.** [Microsoft's GraphRAG](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/) extracts an entity-and-relation graph from a corpus with LLM calls, clusters it into a hierarchical community structure, generates an LLM summary per community ("community reports"), and then serves two query modes: **local search** (traverse from matched entities) and **global search** (answer from community summaries). Its claimed advantage is on questions "that require high-level knowledge of the entire dataset, especially with abstract and global questions" — where "baseline RAG responses were typically shorter, less complete, and contained more hallucinations."

**Is GraphRAG the real, named version of what CiC's own data is gesturing toward?** Half of it, and the half that matters is the cheap half.

Doc 08's and doc 07's observation stands up: `Related-Terms` "became the backbone of a real analytical finding" because it was structured and queryable, and `alexlex001_logos.md` carries not just the list (`Divine Pedagogy, Illumination, Knowledge/Gnosis, Participation, Theosis, Scripture`) but an explicit **reciprocity audit** — a `## Related-Terms Reciprocity Note` distinguishing mutual from one-directional edges and naming unbuilt targets. That is a hand-maintained, bidirectionality-checked edge list. It is an adjacency list. CiC has a knowledge graph and does not know it, and `indexer.py:204` already carries `related_terms` into FAISS metadata where **nothing traverses it**.

But the expensive, named parts of GraphRAG are the parts CiC does not need and should not buy:

- **The extraction stage is the cost, and CiC has no extraction problem.** GraphRAG's price is LLM entity-and-relation extraction plus deduplication plus community summarization: reported at "6–8× more to index and 3× more to operate," and one 5GB legal corpus cost $33,000 to index in early 2024. CiC's edges are *already authored by hand, reciprocity-checked, and free.* Buying GraphRAG would be paying an LLM to infer a graph CiC already has better than an LLM could produce.
- **Global search would fight CiC's own constraints.** "MS-GraphRAG(global) reaching prompt sizes of up to 40,000 tokens" is the opposite direction from the brief's §2 cost requirement, and community summaries are LLM-generated scholarly-register prose — a new, larger supply line for exactly the "documentation voice" register leak doc 08 §4.3 traced.
- **The published guidance says don't.** The 2026 survey [*When to use Graphs in RAG*](https://arxiv.org/pdf/2506.05690) frames it as a three-way choice — flat RAG, hybrid RAG, GraphRAG — and the practitioner consensus is direct: "If you can answer the user's question by reading a single chunk plus its neighbours, you don't need a graph." Graph structures earn their cost "specifically when the answer depends on relationships among entities… not merely on term matching." Microsoft's own LazyGraphRAG exists because of this — reported to cut indexing cost to 0.1% of full GraphRAG.

"A single chunk plus its neighbours" is a near-exact description of what CiC needs: retrieve `Logos`, then have `Illumination` and `Theosis` reachable as one-hop neighbours because the author said they are. That is **graph-expanded retrieval as a candidate-generation step**, not GraphRAG. It is roughly ten lines against the metadata already in the index.

**Verdict: PARTIAL — ADOPT THE TRAVERSAL, REJECT THE PLATFORM.** GraphRAG is the named version of *one* thing CiC's data gestures at (relationship-dependent retrieval) and the wrong purchase for the reason CiC's data is good (the graph is hand-authored, so the expensive extraction stage buys nothing). A proper implementation would add: one-hop `Related-Terms` expansion of the candidate set before ranking; and a genuine capability CiC has no equivalent for — the ability to answer "how do this world's terms hold together" by traversal rather than by hoping three similarity hits happen to cohere. **Confidence: High** on GraphRAG's architecture and Microsoft's framing; **Medium** on the cost multipliers (practitioner write-ups and one Microsoft Community Hub post, not a controlled study); **Medium-High** on LazyGraphRAG's 0.1% figure (search-result summary of a Microsoft Research post).

---

## 5. Retrieval evaluation methodology

Doc 08 §4.1 established the gap exactly: `git log -S "k: int = "` returns two commits, the scaffold and the short-circuit, and "there is no tuning record, no measurement, no live finding about chunk count anywhere in the repo," against a generation-length record that measured 45 live turns and iterated 500→700→900→1200. **This section is the one that makes every other recommendation in this document falsifiable rather than plausible.**

**The standard metrics.** Precision@k (are the top-k relevant), recall@k (how much of the relevant set was retrieved), MRR (was the right item ranked early), nDCG (graded relevance with positional discounting). Anthropic's own harness uses **Pass@K** — "whether the golden document was present in the first K documents retrieved" — which for CiC's single-turn, few-chunks-per-turn shape is the right primary metric: it answers "did the chunk that should have fired, fire," which is precisely doc 08's bucket (B).

**RAGAS**, the RAG-specific framework of record, defines two retrieval metrics with published formulas:

- **Context Precision@K** = Σ(Precision@k × v_k) / (total relevant items in top K) — "evaluates the retriever's ability to rank relevant chunks higher than irrelevant ones."
- **Context Recall** = (claims in reference supported by retrieved context) / (total claims in reference).

**The finding that makes this cheap for CiC.** Both RAGAS metrics have **non-LLM and ID-based variants**, which I verified directly against the RAGAS documentation:

| variant | inputs required | LLM needed |
|---|---|---|
| `LLMContextPrecisionWithReference` | `user_input`, `reference`, `retrieved_contexts` | yes |
| `NonLLMContextPrecisionWithReference` | `retrieved_contexts`, `reference_contexts` (Levenshtein) | **no** |
| **`IDBasedContextPrecision`** | `retrieved_context_ids`, `reference_context_ids` | **no** |
| **ID-Based Context Recall** | `retrieved_context_ids`, `reference_context_ids` | **no** |

CiC has stable, never-reused chunk filenames and already logs every candidate considered and why, retrieved or skipped, through `/api/session/{id}/audit`. **The ID-based variants are computable from data CiC already emits.** No judge model, no API cost, no LLM-grader-grading-an-LLM-grader circularity, fully deterministic and therefore usable as a regression gate. This is the single largest effort-to-value item in this document, and it is a script, not an architecture.

**Golden-set size.** The published range is wide and there is no authoritative floor: practical harnesses run from 15 query-answer pairs to 200+; Anthropic's own contextual-retrieval evaluation used 248 queries against 737 chunks. Recommended thresholds circulating for 2026 are context precision ≥ 0.7 and context recall ≥ 0.8 — treat those as orientation, not targets, since they are aggregated practitioner guidance rather than a standard. **Confidence: High** on the metric definitions and RAGAS variants (read the documentation pages); **Medium** on the size guidance; **Low** on the 0.7/0.8 thresholds (one 2026 blog aggregation — do not quote as a standard).

**What a real, minimal harness looks like for CiC specifically.** Not a framework install — a fixture file and one script.

```
retrieval_eval/
  golden/<world_id>.yaml        # 12–20 cases per world, ~90 total
  run_eval.py                   # loads each world's retriever, no LLM in the loop
  baseline.json                 # committed; every change diffs against it
```

Each case is four fields, all of which a builder can write while looking at the chunks they just authored:

```yaml
- id: syriac-qyama-direct
  query: "Were there monks in your community?"
  transcript: ""                       # or prior turns, for de-dup and reactive-turn cases
  must_retrieve: [syrlex002_qyama.md]  # gold IDs → recall@k, Pass@k, MRR
  must_not_retrieve: []                # the Do-Not-Retrieve-When assertion, currently untestable
```

Four metrics, all ID-based and deterministic: **Pass@k** (any gold chunk in top k — the headline), **recall@k**, **MRR** (is the gold chunk first or third — the thing `k=3` is actually trading away), and a **violation count** on `must_not_retrieve` (the first time in the project's history that a `Do-Not-Retrieve-When` condition becomes a checkable assertion rather than prose).

The case mix should be drawn from the failures already on record, so the harness is a regression suite for real bugs from day one:

1. **Verbatim-term cases** — the participant uses the world's own word. Currently the pure-lexical failure mode; the BM25 test.
2. **Thematic cases** — the participant asks a question a Representative would answer with a term they never named. This is Papnoute's Amma Sarah occasion and the Origenist-vs-Chalcedon horizon: doc 08's bucket (B), where the material existed and was not reached for.
3. **De-duplication cases** — non-empty `transcript` where a chunk already surfaced. Asserts `must_not_retrieve` on the chunk the broken substring guard cannot catch (commit `1252fd4`).
4. **Negative-condition cases** — "logos" in a linguistic sense; the Byzantine hesychast retrojection `desertlex003_hesychia.md` guards against. Asserts the guard fires.
5. **Reactive-turn cases** — `transcript` containing another world's full turn, mirroring `nodes.py:932-934`. Directly tests doc 08 §4.4's untested hypothesis that cross-world query construction contributes to vocabulary drift.
6. **Cross-world isolation cases** — the same query run against two worlds, asserting each surfaces its own chunks. Tests the unevaluable cross-world guards of doc 08 §3.3.

**Two sequencing notes.** First, run this against the current system *before* changing anything; a baseline measured after the fixes is not a baseline. Second, 12–20 cases per world is roughly a day of authoring per world and is enough to catch a regression, not enough to tune a fusion weight — so build the harness first and let it tell you which of the recommendations below actually pays, rather than adopting them on this document's authority.

**Verdict: REAL GAP, total, and the cheapest thing in this document to close.** **Confidence: High.**

---

## 6. Condition-based / rule-based retrieval filtering as its own pattern

CiC's `Retrieve-When` / `Do-Not-Retrieve-When` is unusual, and it has not one precedent but three, each covering a different piece of it.

**a. Metadata filtering / the business-rules layer (recommender systems and vector databases).** Pinecone frames it as ["The Missing WHERE Clause in Vector Search"](https://www.pinecone.io/learn/vector-search-filtering/): "in search and recommender systems there is almost always a need to apply filters," and "a shoe store doesn't just want 'similar shoes'; they want 'similar shoes in size 10 and under $100.'" The literature's central distinction is **pre-filter** (filter the index, then search — risks "islands or dead ends in the graph" when the filter is strict) versus **post-filter** (search, then discard non-matching — "can be inefficient if the initial ANN search returns many candidates that are later filtered out").

CiC is a post-filter, and it pays the documented post-filter cost visibly. `retriever.py:112` retrieves `k*2 = 6` candidates and `retriever.py:178` caps kept documents at `k = 3`. When the filter skips aggressively, CiC does not backfill — it simply returns fewer than 3, and the audit trail records `Skipped 'X'` where a pre-filtered index would have surfaced a fourth candidate. This is the named, expected failure of the architecture CiC chose without naming it.

**b. Instruction-following retrieval (the IR research literature).** Covered in Summary #2. This is the closest published analogue to what `Retrieve-When` actually *is* — a natural-language statement of relevance criteria consumed by the retrieval stage — and it comes with two benchmarks (FollowIR, InstructIR) and a trained model class (Promptriever).

**c. Query-side condition extraction (the framework literature).** The pattern where a model reads natural language and emits structured filters, rather than judging documents one at a time, is LangChain's **self-query retriever** and the general **query-understanding** layer. It matters here because it inverts the cost curve: one call per *turn* to derive a filter, instead of one call per *candidate batch* to grade documents.

### The unevaluable-condition failures, and whether the literature has fixes

Doc 08 §3.3 named three classes the runtime cannot evaluate. Each has a real, named fix — and two of the three are not retrieval problems at all.

**Class 1 — cross-world guards** (`Do-Not-Retrieve-When: discussion concerns a different world's own withdrawal-adjacent practice (do not cross-apply)`). This is asking an LLM to enforce something that is a *hard structural constraint*, not a judgment. Each world already has its own FAISS index (`settings.get_vector_store_path(world_id)`), so cross-world contamination is structurally impossible on the retrieval side; what the condition is actually guarding is the *generation* side (a Representative cross-applying a concept). The metadata-filtering literature's answer is unambiguous: a hard constraint belongs in the filter predicate, never in a soft relevance judgment. **These conditions should be deleted from the retrieval layer** — they are asserting an invariant the architecture already guarantees, and leaving them in dilutes the filter prompt with unevaluable text. The generation-side concern needs a different mechanism, which is a Facilitator-governance question, not a retrieval one.

**Class 2 — Capsule-Core state** (`the World Capsule Core has already surfaced this term's core distinction in the current turn`). This is the most consequential, because doc 08 established it "is prescribed by the project's own template… so it propagates by design." It is also the class with the most standard fix, from two directions:

- **It is a state-visibility bug, and the standard fix is to make the state visible.** The filter call receives `query` and `conversation_context` and nothing else. The conversational-RAG literature's answer to "the retriever cannot see what the conversation already established" is **query rewriting / decontextualization**: "an additional LLM call to decontextualize the incoming question before sending it to the retrieval pipeline," producing "a standalone query without additional information from previous dialogue history." One turn-level rewrite that resolves what has already been covered replaces N per-candidate judgments that cannot see it.
- **Better: it should not be an LLM judgment at all.** "Has this already surfaced" is a set-membership question, and the runtime *knows the answer* — it assembled the Capsule Core and it knows which chunks it injected last turn. The correct mechanism is a **session-level exclusion set of chunk IDs**, plus **MMR** for within-turn redundancy. That replaces the entire class with a deterministic check, and it simultaneously fixes the repetition bug from §2 that the substring guard cannot catch.

**Class 3 — Representative internal need** (`Representative needs a formation example for gravity 1 (withdrawal)`). The classifier runs before generation and has no view of what the Representative "needs." The named architecture that does exactly this is **agentic / self-RAG-style retrieval**: the generation step decides to retrieve, mid-turn, because it has discovered it needs something — Self-RAG's `[Retrieve]` reflection token is literally this decision. It is a real and reachable pattern, but it is a substantially larger architectural change (tool-use retrieval inside the generation call) and it cuts against CiC's prompt-caching economics, since a mid-turn retrieval invalidates nothing but does add a round trip. **Recommendation: do not build this now.** Rewrite these conditions as participant-observable triggers, and log them as a deliberate deferral rather than leaving them as text the runtime silently cannot honour.

**One data-quality finding I re-verified independently** (doc 08 §3.3): five of nine Desert lexicon chunks carry `Do-Not-Retrieve-When: —` — a literal em-dash at line 9 of `desertlex004_logismoi.md`, `desertlex005_diakrisis.md`, `desertlex006_geron-abba-amma.md`, `desertlex007_cheironaxia.md`, `desertlex008_apophthegma.md`. Non-empty, so it passes the `if not candidate.retrieve_when and not candidate.do_not_retrieve_when` check at `batch_evaluate.py:118` and is rendered into the prompt as `DO-NOT-RETRIEVE-WHEN: —`. Confirmed. A one-line sentinel check (`in {"", "—", "–", "-", "n/a", "none"}`) fixes it, and any schema redesign should make the empty case a typed null rather than a hand-typed dash.

**Verdict: ALREADY DOES THIS, and is genuinely ahead of the frameworks on the authoring side** — no surveyed system has anything like a per-chunk, human-authored, positive-and-negative natural-language retrieval condition set with tier weighting; `Retrieve-When` in `syrlex002_qyama.md` is more operationally specific than the metadata predicates the vector-DB literature contemplates. **REAL GAP on the runtime**, in three separate and separately-fixable ways: the conditions never reach the retriever (finding #1), one class asserts an invariant the architecture already guarantees, and one class asks an LLM for state the runtime already holds. **Confidence: High** on the pattern names and the pre/post-filter distinction; **High** on the CiC-side mechanics (read the code and the chunks).

---

## What CiC already does at or above real current standard

Stated plainly, with the practice each can be defended against. None of these should be rebuilt.

1. **A positive retrieval apparatus.** `/api/session/{id}/audit` preserves every candidate considered — retrieved or skipped — and why. Doc 12 already named this correctly as the apparatus-criticus *positive apparatus*, the more expensive and more trusted choice. Its retrieval-specific significance is different and larger: **it is the data source that makes the §5 evaluation harness a script rather than a build.** Most teams building a retrieval eval harness start by instrumenting; CiC's instrumentation predates the harness.
2. **A retrieval evaluator / relevance grader.** Precedented directly by CRAG and Self-RAG. The mechanism needs replacing; the *idea* that retrieval needs a relevance judgment beyond cosine similarity is current best practice, and CiC arrived at it independently.
3. **Human-authored, tier-weighted, positive-and-negative retrieval conditions.** No framework surveyed has this. It is the authoring half of instruction-following retrieval, and CiC's best instances (Syriac `qyama`, Desert `hesychia`'s Byzantine-retrojection guard) are more operationally precise than the published instruction datasets' typical instances.
4. **A hand-authored, reciprocity-audited relation graph.** `Related-Terms` plus the `## Related-Terms Reciprocity Note`'s mutual / one-directional / not-yet-built distinction is a bidirectionality-checked edge list. GraphRAG spends its entire indexing budget trying to produce a lower-quality version of this with LLM extraction.
5. **A designed lightweight-surfacing tier.** `## Quick Meaning`, with the template's own note that it "does not require the full entry to be surfaced," is the persona-framework "permanence/eviction ranking" concept doc 09 flagged CiC as lacking — except CiC *does* have it, in the data, and the runtime discards it. That is a plumbing defect on top of a correct design, which is a much better position than a missing design.
6. **Two-model cost discipline, correctly placed.** Retrieval filtering runs on Haiku 4.5 while generation runs on Sonnet 5. This is the right split and matches the standard guidance that relevance grading does not need the generation model.
7. **Batching a per-candidate LLM call down to one call per retriever per turn.** `batch_evaluate.py`'s own docstring records the reasoning (4-6 calls collapsed to 1). The shape has a quality cost (§3), but the instinct — do not spend a round trip per candidate — is correct, and the fix preserves it.
8. **Stable, never-reused chunk identifiers.** `alexlex001_logos.md`, `desertstory002`. This is why the ID-based evaluation variants and the session exclusion set are both trivially implementable.
9. **Empirically-derived failure documentation in the code itself.** `partition_tier1_short_circuit`'s docstring records that generous-Tier-1 weighting "was tried three ways… and still reverted to literal keyword-matching," with a date. Most codebases do not record what was tried and failed. It is what let this audit identify the prompt shape as the cause rather than re-running the same three experiments.

---

## Prioritized recommendations

Ordered by (measured problem it fixes) ÷ (effort). Each is specific enough to hand to an implementer.

### Tier 0 — do this first, because everything below is unfalsifiable without it

**R0. Build the ID-based retrieval evaluation harness and commit a baseline against the current system.**
Create `cic-poc/backend/retrieval_eval/` with `golden/<world_id>.yaml` (12–20 cases per world, mix per §5's six categories, ~90 cases total), `run_eval.py`, and a committed `baseline.json`. Report **Pass@k, recall@k, MRR, and `must_not_retrieve` violations**, all computed from gold chunk IDs against the IDs the retriever returns — no judge model, no API cost, deterministic. Load each world's real `LexiconRetriever` / `StoryRetriever` so the harness tests the shipped path. Run it before touching anything else. *Effort: ~1 day of code, ~1 day per world of case authoring. Closes doc 08 §4.1 entirely.*

### Tier 1 — the index is broken; fix the index

**R1. Change what gets embedded. Stop embedding the chunk body; start embedding the retrieval surface.**
In `indexer.py:create_documents`, replace `searchable_text` with a bounded composite that fits inside the 256-word-piece budget and includes the fields authors actually write for retrieval:

```
Term: {term}
Aliases: {aliases}
Related: {related_terms}
Retrieve-When: {retrieve_when}
{quick_meaning}
```

Keep the full body as `page_content` payload (or better, as a separate `body` metadata field) so nothing is lost at injection time. Mirror the change in `story_indexer.py`. **Verify before and after with the harness from R0** — this is the change most likely to move Pass@k, and the only one whose direction I would not want asserted without measurement. *Two prerequisites: parse `## Quick Meaning` in `indexer.py` (it currently falls in the discarded `parts[1]`), and author Quick Meaning for Desert's 9 chunks, which have none.*

**R2. Confirm and then remove the truncation ceiling.**
First confirm: for each of the 104 lexicon chunks, tokenize the current `searchable_text` with the loaded model's tokenizer and report how many exceed 256 word-pieces and by how much. I expect near-universal truncation for Alexandria, Syriac, and PAHC; publish the actual distribution. Then, if R1 does not bring every chunk under budget, replace `all-MiniLM-L6-v2`. Two paths:
- **Cheap and local:** a longer-context sentence-transformer, keeping the zero-marginal-cost CPU inference and the existing FAISS store. Requires a re-index, nothing more.
- **Better retrieval quality, adds a vendor:** Voyage AI is Anthropic's recommended embedding provider and `voyage-3-large` leads retrieval-focused MTEB metrics as of April 2026, with Voyage noted as strongest on technical material. Adds a per-index API cost and a network dependency at build time — but embeddings are computed once per re-index, not per turn, so the runtime cost is zero.
Decide with R0's numbers, not on this document's authority. *Note the operational constraint already in the code: `embeddings.py`'s docstring records that loading the model 12 times OOM-killed the Render build — any model swap must keep the shared-instance pattern, and a larger model tightens that budget.*

### Tier 2 — the two cheap, high-certainty mechanical fixes

**R3. Add a BM25 sparse index alongside the existing FAISS index and fuse with weighted reciprocal rank fusion.**
Concretely, in CiC's existing stack: build a `BM25Retriever` over the same documents (same text as R1, so the lexical channel sees `Term`, `Aliases`, and `Related-Terms`), and combine with the FAISS retriever via LangChain's `EnsembleRetriever`, which implements RRF at `k=60`. Start at Anthropic's cookbook weights (semantic 0.8 / BM25 0.2), over-retrieve more than today (`k*2 = 6` is too tight to fuse meaningfully — try 20 per source), then sweep the weights against R0. `langchain_community` is already a dependency; this is an import and roughly 15 lines. *Fixes: the participant who names a world's own term verbatim and gets no lexical channel to it.*

**R4. Replace the two broken de-duplication mechanisms with an ID-keyed session exclusion set plus MMR.**
Delete `already_discussed = label.lower() in context_lower` (`batch_evaluate.py:78`) — it is an accident of six worlds' Term-line formatting, and it is the retrieval-layer cause of commit `1252fd4`'s repeated-story bug that was patched with a prompt clause instead. Replace with: (a) a per-session set of already-injected chunk IDs, passed into `retrieve()` and used as a hard filter or a strong rank penalty; and (b) **MMR** over the fused candidate set for within-turn diversity, λ tuned against R0. CiC's chunk IDs are stable and never reused, so both are set operations. *Fixes: doc 08 §3.2 in full, including the Capsule-Core-already-surfaced condition class (§6, Class 2), which becomes a deterministic check instead of an unanswerable LLM question.*

**R5. Two one-line correctness fixes.**
(a) Treat `—`, `–`, `-`, `n/a`, `none`, and whitespace as empty in the `batch_evaluate.py:118` no-conditions check, so the 5 Desert chunks stop handing the model an em-dash as a condition. (b) `retriever.py:112` discards the similarity score (`for doc, _score in docs_with_scores`) — there is currently **no relevance floor at all**, so the 6th-closest chunk in a 9-chunk world is a candidate no matter how unrelated. Add a distance threshold, calibrated against R0 rather than guessed.

### Tier 3 — the ranking stage, and the biggest cost-and-quality win

**R6. Replace the batched LLM relevance vote with a local cross-encoder, and keep the LLM only for negative conditions.**
Add a CPU cross-encoder (the existing `sentence-transformers` dependency already supports this — no new vendor, no per-turn API cost) as the reranking stage over the fused candidate set from R3. Because a cross-encoder scores each (query, document) pair in an independent forward pass, the Tier-2/3 batch-dilution failure the code has fought three separate times becomes structurally impossible, and the Tier-1 split at `batch_evaluate.py:136-149` — currently inert for the three all-Tier-1 worlds — can be deleted. Keep one Haiku call, invoked **only** for candidates carrying a genuinely evaluable `Do-Not-Retrieve-When` (a term-disambiguation or anachronism guard), which after R4 and the Class-1 deletions below is a small minority of candidates. Removes ~2 Haiku calls per world per turn from the latency critical path — 6 at a three-world table.

**R7. Move the lightweight surfacing layer out of retrieval and into the cached prefix. This is the quality-and-cost-are-one-decision item.**
Put every term's `Quick Meaning` for the seated world into the static, prompt-cached system prefix, and reduce per-turn retrieval to fetching *deep bodies* only when the participant actually goes deep on a specific term. The measured case:

| | today (Alexandria) | proposed |
|---|---|---|
| terms reachable per turn | 3 of 45 | **45 of 45** |
| retrieved tokens per turn | ~6,700, uncacheable, varies every turn | ~4,000 in a stable cached prefix |
| includes `Ecological Function`, `Distortion Risk`/`Modern Hearing`, `Key Sources`, gravity codes | yes, verbatim | **no** |
| ≈ input cost per turn (Sonnet 5, $3/MTok; cache read 0.1×) | ~$0.020 | ~$0.0012 |

Three caveats I will not smooth over. **First, do not extend this to full corpora.** Alexandria's whole 101,600-token corpus at the 0.1× cache-read rate costs ~$0.031/turn — *more* than today. Full-context is cheaper only for the five small worlds, and it is the wrong shape regardless because it reintroduces the apparatus injection. The Quick-Meaning layer is the version that wins on both axes. **Second, prompt caching has a 5-minute default TTL and Sonnet 5 has a 1,024-token minimum cacheable prefix** — a participant pausing mid-session past the TTL loses the advantage entirely, which the brief §2 already flags as an unmodelled cost variable, and the small worlds' Quick Meaning sets (583–854 tokens) are below the minimum *on their own* and only cache by riding inside the existing static prefix. Verify with `usage.cache_read_input_tokens`; if it is zero across turns, something is invalidating the prefix. **Third, and most seriously: doc 09's highest-priority warning cuts directly against this.** With original verbatim personas, models "unwittingly repeat profile information either verbatim or with significant word overlap," and a world's distinctive vocabulary in the always-present slot is the highest-parroting configuration there is. Moving 45 terms from occasionally-retrieved to always-present raises parroting risk by construction. This recommendation is contingent on the redesign shipping a real anti-parroting guard, and R7 should not be adopted ahead of one.

**R8. Traverse `Related-Terms`; do not buy GraphRAG.**
`related_terms` is already in FAISS metadata (`indexer.py:204`) and nothing reads it. Add one-hop expansion: after initial candidate generation, pull in the `Related-Terms` neighbours of top-ranked hits as additional candidates at a rank penalty, then let R6's reranker decide. This costs ~10 lines and a dictionary lookup, and captures the one thing similarity search structurally cannot do — surfacing a term because the *author* said it is connected, not because its opening paragraph happens to embed nearby. Explicitly reject GraphRAG's extraction, community-detection, and global-search stages: CiC's graph is hand-authored and reciprocity-audited, so the expensive stage buys a worse graph, and global search's 40,000-token prompts and LLM-generated community summaries run against both the cost requirement and the register-leak finding.

### Tier 4 — the query, and two deliberate deferrals

**R9. Fix query construction, which no recommendation above touches.**
Three separate defects, all documented and none addressed by better indexing or ranking:
- **Reactive turns** (`nodes.py:932-934`) set the retrieval query to `"{question}\n\n{OtherRep} just said: {their full turn}"` — so another world's full turn, in another world's vocabulary, drives this world's vector search. Doc 08 §4.4 flags this as a plausible untested contributor to the cross-world vocabulary drift that `check_cross_world_vocabulary_drift` was built for. **The harness in R0 has a case category for exactly this — measure it before theorizing.**
- **Bridged turns** (doc 08 §5.2) replace the participant's actual words with a world-agnostic handback paraphrase before retrieval runs, so on a false positive the world's own Tier-1 chunks are matched against text written for no world in particular.
- Both are the same fix, and it is the standard one: **conversational query rewriting** — one Haiku call that decontextualizes the incoming turn into a standalone, world-appropriate retrieval query, replacing the current string concatenation. This is well-established practice ("query rewriting makes an additional LLM call to decontextualize the incoming question before sending it to the retrieval pipeline"), it fits the existing two-model split, and it costs one Haiku call per turn — which R6 has already freed up by removing two.

**R10. Retire the two condition classes the runtime cannot honour, deliberately and on the record.**
- **Delete cross-world guards from the retrieval layer.** Each world has its own FAISS index; cross-world retrieval contamination is structurally impossible, so these conditions assert an invariant the architecture already guarantees while diluting the filter prompt with unevaluable text. The generation-side concern they were reaching for is real and belongs in Facilitator governance, not here.
- **Rewrite `Representative needs...` conditions as participant-observable triggers.** The named architecture that would honour them as written is agentic / Self-RAG-style mid-generation retrieval, which is a genuine option and out of scope for this cycle. Log it as a deferral with the reason, rather than leaving conditions in the data that the classifier silently cannot evaluate.
- **Update `L4-Templates/Deployment_Lexicon_Chunk_Template.md`.** Doc 08 established that the Capsule-Core-state phrasing "is prescribed by the project's own template… so it propagates by design." R4 makes that class mechanically unnecessary; the template has to change or the next world built will reproduce it.

---

## Do not cite — items I could not verify

- **[*Lightweight Relevance Grader in RAG*](https://arxiv.org/pdf/2506.14084) numeric results.** The PDF's compressed content streams would not extract. The paper exists and its subject is confirmed (small fine-tuned model vs. large LLM for grading retrieved-document relevance, evaluated on recall/precision/F1), but **do not attribute any specific figure, model name, or delta to it** without reading the rendered PDF.
- **Cross-encoder-vs-LLM-reranker cost and accuracy multipliers** ("100×–1000× lower cost," "5-8% higher accuracy, 4-6 seconds added latency," "~$0.025/1M tokens," "95% of LLM accuracy at 3× faster"). All from a single vendor blog (ZeroEntropy) with a commercial interest in cross-encoders. **The direction is well-supported by the general IR literature; treat the magnitudes as marketing until reproduced on CiC's own harness.** The one cross-encoder-vs-LLM comparison I found in a peer-reviewed venue ([arXiv:2403.10407](https://arxiv.org/abs/2403.10407), "A Thorough Comparison of Cross-Encoders and LLMs for Reranking SPLADE") supports only the weaker claim that "traditional cross-encoders remain very competitive."
- **GraphRAG cost multipliers** ("6–8× more to index and 3× more to operate"; the $33,000 legal-corpus figure; LazyGraphRAG at "0.1% of full GraphRAG"). Practitioner write-ups, a Microsoft Community Hub post, and search-result summaries — not controlled studies, and the $33,000 figure is from early 2024 and explicitly described in its own source as having collapsed since. Cite as "reported" with the source named, never as a benchmark.
- **RAG evaluation thresholds** ("context precision 0.7, context recall 0.8"). One 2026 blog aggregation. There is no authoritative threshold for these metrics and CiC should set its own from its own baseline. Do not present these as a standard.
- **Promptriever's metric deltas** (+14.3 p-MRR on FollowIR, +12.9 Robustness@10 on InstructIR). From the paper's abstract via search results; I did not read the results tables. The paper, the model class, and both benchmark names are confirmed.
- **Embedding-model leaderboard positions** (voyage-3-large "leads retrieval-focused MTEB metrics as of April 2026"; Gemini Embedding at 68.32; Jina v5-text at 71.7; Harrier-OSS-v1 at 74.3). Aggregator blogs, not the MTEB leaderboard itself. **Verify against the live leaderboard before choosing a model on these numbers.** The one claim I would stand behind is the qualitative one that Voyage AI is Anthropic's recommended embedding provider.

**Three further honest limits.** (1) My per-world token counts are `characters ÷ 4` approximations. That systematically *under*counts Syriac and Greek script, which tokenizes worse than English — so Syriac's and Alexandria's real figures are higher than the tables above. Re-measure with `client.messages.count_tokens` before costing anything. (2) The claim that ~85% of an Alexandria chunk is excluded from its embedding is arithmetic from a verified 256-word-piece limit and a verified 1,249-word mean, not a direct tokenizer run; R2's first step exists to convert it from inference to measurement. (3) The cost figures use Sonnet 5's standard $3/MTok input rate. An introductory rate of $2/MTok runs through 2026-08-31, which would shift every dollar figure down by a third; the *ratios* between configurations hold either way, and the ratios are what the recommendations turn on.

---

## Sources

**Anthropic and first-party:** [Contextual Retrieval in AI Systems (Anthropic Engineering)](https://www.anthropic.com/engineering/contextual-retrieval) · [Enhancing RAG with contextual retrieval (Claude Cookbook)](https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide) · prompt-caching economics, model IDs, and per-model cache minimums via the bundled `claude-api` skill (`shared/prompt-caching.md`, `shared/models.md`)

**Hybrid retrieval and fusion:** [Hybrid Search for RAG: Combining BM25 and Dense Vector Search](https://denser.ai/blog/hybrid-search-for-rag/) · [Hybrid Search in RAG: Dense + Sparse (BM25/SPLADE), Reciprocal Rank Fusion](https://blog.gopenai.com/hybrid-search-in-rag-dense-sparse-bm25-splade-reciprocal-rank-fusion-and-when-to-use-which-fafe4fd6156e) · [From BM25 to Corrective RAG: Benchmarking Retrieval Strategies for Text-and-Table Documents](https://arxiv.org/html/2604.01733v1) · [LangChain EnsembleRetriever (TruLens cookbook)](https://www.trulens.org/cookbook/frameworks/langchain/langchain_ensemble_retriever/) · [What is going on under the hood of LangChain Ensemble Retriever](https://medium.com/@autorag/what-is-going-on-under-the-hood-of-langchain-ensemble-retriever-73c3de5377a3)

**Re-ranking and relevance grading:** [A Thorough Comparison of Cross-Encoders and LLMs for Reranking SPLADE (arXiv:2403.10407)](https://arxiv.org/abs/2403.10407) · [Listwise reranking: LLM permutation over a candidate list (ZeroEntropy)](https://zeroentropy.dev/concepts/listwise-reranking/) · [Ultimate Guide to Choosing the Best Reranking Model (ZeroEntropy)](https://zeroentropy.dev/articles/ultimate-guide-to-choosing-the-best-reranking-model-in-2025/) · [Lightweight Relevance Grader in RAG (arXiv:2506.14084)](https://arxiv.org/pdf/2506.14084) *(named only — numeric results unverified)* · [Corrective RAG (Learn Prompting)](https://learnprompting.org/docs/retrieval_augmented_generation/corrective-rag) · [Corrective RAG (CRAG): Workflow and implementation (Meilisearch)](https://www.meilisearch.com/blog/corrective-rag) · [Relevance Isn't All You Need: Multi-Criteria Reranking (arXiv:2504.07104)](https://arxiv.org/pdf/2504.07104)

**Instruction-following retrieval:** [Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models (arXiv:2409.11136)](https://arxiv.org/abs/2409.11136) · [Promptriever (Microsoft Research)](https://www.microsoft.com/en-us/research/publication/promptriever-instruction-trained-retrievers-can-be-prompted-like-language-models/) · [Towards Better Instruction Following Retrieval Models (arXiv:2505.21439)](https://arxiv.org/pdf/2505.21439)

**GraphRAG:** [GraphRAG: Unlocking LLM discovery on narrative private data (Microsoft Research)](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/) · [Project GraphRAG (Microsoft Research)](https://www.microsoft.com/en-us/research/project/graphrag/) · [microsoft/graphrag (GitHub)](https://github.com/microsoft/graphrag) · [When to use Graphs in RAG: A Comprehensive Analysis (arXiv:2506.05690)](https://arxiv.org/pdf/2506.05690) · [GraphRAG Costs Explained (Microsoft Community Hub)](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/graphrag-costs-explained-what-you-need-to-know/4207978) · [You probably don't need GraphRAG](https://medium.com/@amrwrites/you-probably-dont-need-graphrag-0bc9cf671db1) · [Is GraphRAG Really Worth It?](https://ml-digest.com/when-to-use-kg-rag/)

**Evaluation:** [Ragas — Context Precision](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/) · [Ragas — Context Recall](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall/) · [Building a Golden Dataset and Evaluating Retrieval Quality](https://www.codersarts.com/post/building-a-golden-dataset-and-evaluating-retrieval-quality) · [Evaluate a RAG application (LangSmith docs)](https://docs.langchain.com/langsmith/evaluate-rag-tutorial) · [Can LLMs Be Trusted for Evaluating RAG Systems? (arXiv:2504.20119)](https://arxiv.org/pdf/2504.20119) · [Understanding the Fundamental Design Decisions of RAG Systems (arXiv:2411.19463)](https://arxiv.org/pdf/2411.19463)

**Filtering, diversity, and query rewriting:** [The Missing WHERE Clause in Vector Search (Pinecone)](https://www.pinecone.io/learn/vector-search-filtering/) · [Metadata Filtering in Vector Search: A Guide for Engineering Leaders](https://www.saumilsrivastava.ai/blog/metadata-filtering-in-vector-search-a-comprehensive-guide-for-engineering-leaders) · [Metadata Filtering in Vector Databases (apxml)](https://apxml.com/courses/vector-databases-semantic-search/chapter-2-introducing-vector-databases/vector-db-metadata-filtering) · Carbonell & Goldstein, ["The Use of MMR, Diversity-Based Reranking" (SIGIR 1998)](https://aclanthology.org/X98-1025.pdf) · [Leveraging historical information to boost RAG in conversations (Information Processing & Management)](https://www.sciencedirect.com/science/article/pii/S0306457325003905) · [Multi-Turn Conversation Support (NVIDIA RAG Blueprint)](https://docs.nvidia.com/rag/2.4.0/multiturn.html) · [ChatQA: Surpassing GPT-4 on Conversational QA and RAG (arXiv:2401.10225)](https://arxiv.org/pdf/2401.10225)

**Embedding models:** [sentence-transformers/all-MiniLM-L6-v2 (Hugging Face)](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) · [Embedding Models 2026: Benchmark and Comparison](https://app.ailog.fr/en/blog/news/embedding-models-2026) · [Voyage 3.5 vs OpenAI vs Cohere Embedding Models 2026](https://www.buildmvpfast.com/blog/best-embedding-model-comparison-voyage-openai-cohere-2026)

**CiC internal sources read directly:** `cic-poc/backend/app/rag/{retriever.py, story_retriever.py, batch_evaluate.py, indexer.py, story_indexer.py, embeddings.py}` · `cic-poc/backend/app/config.py` · `cic-poc/backend/app/graph/nodes.py` (call sites) · all 104 files under `cic-poc/backend/data/*/lexicon_chunks/` and 58 under `*/story_chunks/` · `~/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2/.../sentence_bert_config.json` · `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/{02_Codebase_Mining.md §7, 08_LiveConversation_DataAccess_Failures.md, 12_Academic_Source_Organization_Standards.md}` · `Ministry/Technology/CiC_System_Redesign_Fable_Brief_2026-07-25.md`
