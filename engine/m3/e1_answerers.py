"""Answerers for the E1 experiment arms. Both match LiveModelAnswerer's
interface: answer(cell, probe_text) -> AnswerResult.

The cells that pick a dossier come from the question text alone, through
engine.m4.evidence.match_asks_to_cells (top two); the probe's own cell is
never an input.

DossierAnswerer (arm C) sends the dossier layout as the system prompt and
runs LiveModelAnswerer's own evidence, generation and net path.

NativeCitationAnswerer (arm C-native) attaches the dossier records as API
documents with citations enabled and reads the sources from the response.
The net does not run: its input is inline [[id]] tags, which this arm does
not ask for.

Construction makes no call; only .answer() does.
"""
import inspect
from dataclasses import replace

from anthropic import APIError

from engine.m3 import e1_layout
from engine.m3.generation import AnswerResult, LiveModelAnswerer
from engine.m4 import evidence as m4_evidence
from engine.m4.generation import stream_voice_turn
from engine.m4.voice_request import build_voice_request
from engine.m4.world_loader import LoadedWorld

_MAX_TOKENS = inspect.signature(stream_voice_turn).parameters["max_tokens"].default
_TIMEOUT = inspect.signature(stream_voice_turn).parameters["timeout"].default


def _field(obj, name, default=None):
    return obj.get(name, default) if isinstance(obj, dict) else getattr(obj, name, default)


class _Base:
    arm = ""

    def __init__(self, *, world: LoadedWorld, canon_questions: dict[str, dict], client, model_id: str):
        self.world = world
        self.canon_questions = canon_questions
        self.client = client
        self.model_id = model_id
        self.live = LiveModelAnswerer(world=world, canon_questions=canon_questions, client=client, model_id=model_id)
        self.repository_records = self.live.repository_records
        self.thin_topics = self.live.thin_topics
        self.manifests: list[dict] = []

    @property
    def last_manifest(self) -> dict | None:
        return self.manifests[-1] if self.manifests else None

    def choose_cells(self, probe_text: str) -> list[str]:
        matches = m4_evidence.match_asks_to_cells(
            message=probe_text, asks=None, canon_questions=self.canon_questions,
            repository_records=self.repository_records, top_n=2,
        )
        return [m["cell"] for m in matches]

    def user_message(self, probe_text: str) -> str:
        turn_evidence = m4_evidence.assemble_evidence(
            message=probe_text,
            asks=None,
            canon_questions=self.canon_questions,
            coverage=self.world.coverage,
            repository_records=self.repository_records,
            thin_topics=self.thin_topics,
        )
        block = m4_evidence.render_evidence_block(turn_evidence)
        return f"{block}\n{probe_text}" if turn_evidence["candidates"] else probe_text


class DossierAnswerer(_Base):
    arm = "c"

    def answer(self, cell: str, probe_text: str) -> AnswerResult:
        cells = self.choose_cells(probe_text)
        system = e1_layout.assemble_c(self.world.prompt_text, self.repository_records, cells)
        _, blocks, _ = e1_layout.split_prompt(self.world.prompt_text)
        ids = e1_layout.dossier_ids(self.repository_records, cells, blocks)
        self.manifests.append(e1_layout.manifest(self.arm, cells, ids, len(system)))
        inner = LiveModelAnswerer(
            world=replace(self.world, prompt_text=system), canon_questions=self.canon_questions,
            client=self.client, model_id=self.model_id,
        )
        return inner.answer(cell, probe_text)


class NativeCitationAnswerer(_Base):
    arm = "native"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.raw_response_texts: list[str] = []

    @property
    def last_raw_response_text(self) -> str | None:
        return self.raw_response_texts[-1] if self.raw_response_texts else None

    def answer(self, cell: str, probe_text: str) -> AnswerResult:
        cells = self.choose_cells(probe_text)
        system, documents = e1_layout.assemble_native(self.world.prompt_text, self.repository_records, cells)
        ids = [d["title"] for d in documents]
        chars = len(system) + sum(len(d["source"]["data"]) for d in documents)
        self.manifests.append(e1_layout.manifest(self.arm, cells, ids, chars))

        system_blocks, _ = build_voice_request(system_prompt=system, message="")
        messages = [{"role": "user", "content": [*documents, {"type": "text", "text": self.user_message(probe_text)}]}]
        try:
            response = self.client.messages.create(
                model=self.model_id, max_tokens=_MAX_TOKENS, system=system_blocks, messages=messages, timeout=_TIMEOUT,
            )
        except APIError as e:
            raise RuntimeError(f"NativeCitationAnswerer: voice generation call failed: {e}") from e

        text, entries, raw = read_response(response, ids)
        self.raw_response_texts.append(raw)
        citations = sorted({rid for entry in entries for rid in entry["record_ids"]})
        primary = self.repository_records.get(citations[0]) if citations else None
        return AnswerResult(
            text=text,
            citations=citations,
            source_record_id=citations[0] if citations else None,
            source_record_type=primary.get("record_type") if primary else None,
            citation_entries=entries,
        )


class WholeWorldNativeAnswerer(NativeCitationAnswerer):
    """Today's whole-world prompt with every record attached as a citable
    document. No cell is chosen and no index is added, so the citation
    mechanism is the only difference from the baseline."""

    arm = "native-whole"

    def answer(self, cell: str, probe_text: str) -> AnswerResult:
        system, documents = e1_layout.assemble_native_whole(self.world.prompt_text)
        ids = [d["title"] for d in documents]
        chars = len(system) + sum(len(d["source"]["data"]) for d in documents)
        self.manifests.append(e1_layout.manifest(self.arm, [], ids, chars))

        system_blocks, _ = build_voice_request(system_prompt=system, message="")
        messages = [{"role": "user", "content": [*documents, {"type": "text", "text": self.user_message(probe_text)}]}]
        try:
            response = self.client.messages.create(
                model=self.model_id, max_tokens=_MAX_TOKENS, system=system_blocks, messages=messages, timeout=_TIMEOUT,
            )
        except APIError as e:
            raise RuntimeError(f"WholeWorldNativeAnswerer: voice generation call failed: {e}") from e

        text, entries, raw = read_response(response, ids)
        self.raw_response_texts.append(raw)
        citations = sorted({rid for entry in entries for rid in entry["record_ids"]})
        primary = self.repository_records.get(citations[0]) if citations else None
        return AnswerResult(
            text=text,
            citations=citations,
            source_record_id=citations[0] if citations else None,
            source_record_type=primary.get("record_type") if primary else None,
            citation_entries=entries,
        )


def read_response(response, document_ids: list[str]) -> tuple[str, list[dict], str]:
    """(answer text, per-text-block citation entries, raw text with each
    cited block followed by its [[id]] tags). A citation resolves through
    document_index into the documents order; one that does not resolve is
    dropped."""
    parts, entries, raw = [], [], []
    for block in _field(response, "content") or []:
        if _field(block, "type") != "text":
            continue
        text = _field(block, "text") or ""
        ids = set()
        for citation in _field(block, "citations") or []:
            index = _field(citation, "document_index")
            if isinstance(index, int) and 0 <= index < len(document_ids):
                ids.add(document_ids[index])
        parts.append(text)
        if text.strip():
            entries.append({"sentence": text.strip(), "record_ids": sorted(ids)})
        raw.append(text + "".join(f" [[{rid}]]" for rid in sorted(ids)))
    return "".join(parts).strip(), entries, "".join(raw)
