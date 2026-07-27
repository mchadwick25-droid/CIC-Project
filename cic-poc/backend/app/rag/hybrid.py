"""S3.2 - hybrid lexical+dense candidate search (Pass 1 R3 + R8).

R3: BM25 over the same retrieval surface the dense index embeds, fused
with the dense results by weighted reciprocal-rank fusion. The
participant who says a native term verbatim (qyama, anachoresis) finally
has a lexical path to its chunk - MiniLM embeddings alone rank rare
transliterated terms poorly, and body-text phrasings lost by S3.1's
surface change get their lexical route back.

R8: one-hop related-terms expansion (~the "10 lines against metadata
already in the index" Pass 1 describes): any candidate's related_terms /
aliases naming another doc's term pulls that doc into the candidate set
at expansion rank. GraphRAG explicitly rejected (Pass 1 SS5.4) - the
graph is hand-authored and reciprocity-audited; this is a metadata walk,
not an extraction platform.

Deterministic, no API calls, CPU-only - same properties as the harness.
"""
from __future__ import annotations

import re
import unicodedata

from langchain_core.documents import Document
from rank_bm25 import BM25Okapi

# RRF constant per the standard formulation; dense weighted above lexical
# (dense carries the thematic load; BM25 is the verbatim-term path)
RRF_K = 60
W_DENSE = 1.0
W_LEXICAL = 0.7
# expansion hits enter as if ranked just past the fused list - present,
# never displacing a direct hit
EXPANSION_RANK = 30
# S3.3 (Pass 1 R5): relevance floor on the dense leg - normalized-embedding
# L2 distance beyond which a dense-only candidate is noise, not a match
# (observed good hits sit ~0.65-1.1; the floor drops the far tail). A
# candidate with genuine lexical overlap is never floored - BM25 presence
# is itself relevance evidence. The floor is ADAPTIVE: max(absolute cap,
# best distance + margin) - long reactive-style queries (another world's
# turn text embedded, the pre-S3.5 shape) shift the whole distance
# distribution upward, and an absolute 1.4 cut a must-doc sitting 0.2
# behind the best hit (HAL-RT-01's vulgata at 1.41). Constants here until
# S4.4 makes parameters.yaml the runtime parameter home (F9).
DENSE_RELEVANCE_FLOOR = 1.4
DENSE_FLOOR_MARGIN = 0.35
# S3.3 (Pass 1 R5): MMR balance - relevance vs. redundancy among the
# selected candidates (standard maximal-marginal-relevance formulation).
# 0.85, not the textbook 0.7: at 0.7 MMR demoted a world's genuinely
# distinct sibling doc (vulgata vs hebraica-veritas, both must-retrieve
# for one translation question) as if it were a duplicate - measured on
# HAL-RT-01. The within-turn target is near-identical redundancy only.
MMR_LAMBDA = 0.85


def _tokenize(text: str) -> list[str]:
    """Lowercase, diacritic-folded word tokens. Folding is load-bearing:
    the corpus writes transliterated terms with macrons (anachōrēsis,
    qyāmā) while participants type plain ASCII (anachoresis, qyama) - an
    ASCII-only tokenizer shattered the macron forms into fragments and
    broke the exact lexical path this searcher exists to provide."""
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.findall(r"[a-z0-9]+", text)


class HybridSearcher:
    """BM25 + dense RRF fusion over one world's vector store."""

    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.docs: list[Document] = list(vector_store.docstore._dict.values())
        corpus = [self._bm25_text(d) for d in self.docs]
        self._bm25 = BM25Okapi(corpus)
        # per-corpus document frequencies, for query-side stopwording:
        # rank_bm25 epsilon-floors negative idf, so near-universal tokens
        # ("what", "you", "of" - dense in every retrieve-when) still score
        # POSITIVELY and their sheer count swamps the one discriminating
        # token ("What do you mean when you speak of the Logos?" ranked
        # docs with none of 'logos' at the top). Query tokens present in
        # more than half the docs are dropped before scoring.
        self._df: dict[str, int] = {}
        for toks in corpus:
            for tok in set(toks):
                self._df[tok] = self._df.get(tok, 0) + 1
        self._df_cutoff = max(2, len(self.docs) // 2)
        # S3.3: per-doc embedding vectors for MMR, reconstructed from the
        # FAISS index already on disk (no re-embedding)
        self._vecs: dict[str, list[float]] = {}
        try:
            for i, ds_id in vector_store.index_to_docstore_id.items():
                d = vector_store.docstore._dict.get(ds_id)
                if d is not None:
                    self._vecs[self._doc_key(d)] = vector_store.index.reconstruct(int(i))
        except Exception:
            self._vecs = {}  # MMR degrades to pure fused order
        # term/alias lookup for R8 one-hop expansion (lexicon docs carry
        # term+aliases; story docs carry story_title)
        self._by_name: dict[str, int] = {}
        for i, d in enumerate(self.docs):
            names = [d.metadata.get("term", ""), d.metadata.get("story_title", "")]
            names += list(d.metadata.get("aliases", []) or [])
            for n in names:
                n = n.strip().lower()
                if n:
                    self._by_name.setdefault(n, i)

    @staticmethod
    def _bm25_text(d: Document) -> list[str]:
        """Field-boosted lexical corpus for one doc. Deliberately NOT the
        full embedded surface: the Related line is excluded (every term
        name appearing in many docs' Related lists flattens that name's
        idf to nothing - measured on 'What is theosis?', where the exact
        term's own doc lost the lexical race to docs merely *related* to
        it), and the identity fields (term/aliases; story title) are
        weighted 3x so a verbatim mention dominates the retrieve-when
        phrasing that many docs share ('what is...', which rank_bm25's
        epsilon flooring keeps positively scored despite near-universal
        document frequency)."""
        m = d.metadata
        identity = " ".join([m.get("term", ""), m.get("story_title", ""),
                             " ".join(m.get("aliases", []) or [])])
        toks = _tokenize(identity) * 3
        toks += _tokenize(m.get("retrieve_when", ""))
        toks += _tokenize(m.get("quick_meaning", ""))
        return toks

    def _doc_key(self, d: Document) -> str:
        return d.metadata.get("source_file", id(d))

    def search(self, query: str, k: int) -> list[tuple[Document, float]]:
        """Fused candidates: weighted RRF of dense + BM25, then one-hop
        related-terms expansion. Returns (doc, fused_score) sorted
        descending - same contract as similarity_search_with_score except
        the score is a fused rank score (higher = better)."""
        n = max(k * 2, 10)
        dense = self.vector_store.similarity_search_with_score(query, k=n)
        # S3.3 relevance floor (adaptive - see constants above):
        # dense-only candidates past the floor are noise; lexical evidence
        # below re-admits a doc on its own merits (fusion sums legs
        # independently)
        if dense:
            floor = max(DENSE_RELEVANCE_FLOOR,
                        float(dense[0][1]) + DENSE_FLOOR_MARGIN)
            dense = [(d, s) for d, s in dense if s <= floor]

        q_toks = [t for t in _tokenize(query)
                  if self._df.get(t, 0) <= self._df_cutoff]
        scores = (self._bm25.get_scores(q_toks) if q_toks
                  else [0.0] * len(self.docs))
        lex_ranked = sorted(range(len(self.docs)), key=lambda i: -scores[i])[:n]

        fused: dict[str, float] = {}
        docs_by_key: dict[str, Document] = {}
        for rank, (d, _s) in enumerate(dense):
            key = self._doc_key(d)
            docs_by_key[key] = d
            fused[key] = fused.get(key, 0.0) + W_DENSE / (RRF_K + rank + 1)
        for rank, i in enumerate(lex_ranked):
            if scores[i] <= 0:
                break  # BM25 zero means no lexical overlap at all
            d = self.docs[i]
            key = self._doc_key(d)
            docs_by_key[key] = d
            fused[key] = fused.get(key, 0.0) + W_LEXICAL / (RRF_K + rank + 1)

        # R8: one-hop expansion from the current top candidates
        top_keys = sorted(fused, key=fused.get, reverse=True)[:k]
        for key in list(top_keys):
            d = docs_by_key[key]
            for name in (d.metadata.get("related_terms", []) or []):
                j = self._by_name.get(str(name).strip().lower())
                if j is None:
                    continue
                nd = self.docs[j]
                nkey = self._doc_key(nd)
                if nkey not in fused:
                    docs_by_key[nkey] = nd
                    fused[nkey] = W_DENSE / (RRF_K + EXPANSION_RANK)

        ranked = sorted(fused.items(), key=lambda kv: -kv[1])
        # S3.3 (Pass 1 R5): MMR re-rank WITHIN the candidate window only -
        # it reorders the docs the retriever will consider (demoting
        # near-duplicates of already-selected ones) but never displaces a
        # relevant doc out of the window with a diverse-but-weaker one
        # (the first cut of this reordered globally and cost a reactive
        # case its second must-doc). Within-turn de-dup half; the
        # cross-turn half is the session exclusion set.
        window = ranked[: k * 2]
        ranked = self._mmr(window) + ranked[k * 2:]
        return [(docs_by_key[key], score) for key, score in ranked]

    def _mmr(self, ranked: list[tuple[str, float]]) -> list[tuple[str, float]]:
        if not self._vecs or len(ranked) <= 1:
            return ranked
        import math

        def cos(a, b):
            num = sum(x * y for x, y in zip(a, b))
            da = math.sqrt(sum(x * x for x in a)) or 1.0
            db = math.sqrt(sum(x * x for x in b)) or 1.0
            return num / (da * db)

        max_rel = ranked[0][1] or 1.0
        remaining = list(ranked)
        selected: list[tuple[str, float]] = []
        while remaining:
            best_i, best_v = 0, None
            for i, (key, score) in enumerate(remaining):
                rel = score / max_rel
                sim = 0.0
                v = self._vecs.get(key)
                if v is not None and selected:
                    sims = [cos(v, self._vecs[sk]) for sk, _ in selected
                            if sk in self._vecs]
                    sim = max(sims) if sims else 0.0
                mmr = MMR_LAMBDA * rel - (1 - MMR_LAMBDA) * sim
                if best_v is None or mmr > best_v:
                    best_i, best_v = i, mmr
            selected.append(remaining.pop(best_i))
        return selected
