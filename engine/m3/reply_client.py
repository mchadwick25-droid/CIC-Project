"""A model client that answers from reply files, so a turn can be run with no
model call. Whoever writes the replies stands in for the model.

Each call the engine makes is keyed by question id, kind and position:
`<question>.<kind>.<n>`. Kinds are `voice` (the streamed answer) and, for the
forced tool calls, the tool's name (`submit_safety_output`, `submit_reader_output`).
A call with no reply file yet writes its request to the pending directory and
raises PendingReply; the caller collects the pending requests, the replies are
written, and the turn is run again. Replies for a voice call are the raw tagged
text the model would have streamed; for a tool call, the JSON object the model
would have passed to the tool.
"""
import hashlib
import json
import re
from pathlib import Path

from engine.m3.gate_replay import _SavedDraftStream

_ZERO_USAGE = {"input_tokens": 0, "output_tokens": 0, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0}


class PendingReply(Exception):
    def __init__(self, key: str):
        super().__init__(key)
        self.key = key


def _blocks(system) -> list[str]:
    if isinstance(system, str):
        return [system]
    return [block.get("text", "") for block in system or []]


def _message_text(content) -> str:
    if isinstance(content, str):
        return content
    return "\n".join(block.get("text", "") for block in content)


class _ToolUseBlock:
    type = "tool_use"

    def __init__(self, name: str, tool_input: dict):
        self.name = name
        self.input = tool_input

    def model_dump(self) -> dict:
        return {"type": self.type, "name": self.name, "input": self.input}


class _ToolResponse:
    def __init__(self, name: str, tool_input: dict):
        self.content = [_ToolUseBlock(name, tool_input)]
        self.usage = type("Usage", (), _ZERO_USAGE)()
        self.stop_reason = "tool_use"


_OFFERED = re.compile(r"^- \[\[([^\]]+)\]\]", re.MULTILINE)


def offered_ids(request: dict) -> list[str]:
    """The record ids a voice request's ground block offers the voice: one
    list entry per `- [[id]]` line of its messages, in order, without repeats."""
    if request["kind"] != "voice":
        return []
    text = "\n".join(m["text"] for m in request["messages"])
    return list(dict.fromkeys(re.sub(r"^(?:quote|story):", "", found) for found in _OFFERED.findall(text)))


class ReplyFileClient:
    def __init__(self, *, question_id: str, reply_dir: Path, pending_dir: Path):
        self.question_id = question_id
        self.reply_dir = reply_dir
        self.pending_dir = pending_dir
        self.messages = self
        self._counts: dict[str, int] = {}
        self.requests: list[dict] = []

    def _key(self, kind: str) -> str:
        self._counts[kind] = self._counts.get(kind, 0) + 1
        return f"{self.question_id}.{kind}.{self._counts[kind]}"

    def _reply(self, key: str, extension: str, request: dict) -> str:
        self.requests.append({"key": key, "kind": request["kind"], "offered": offered_ids(request)})
        path = self.reply_dir / f"{key}.{extension}"
        if path.exists():
            return path.read_text(encoding="utf-8")
        self.pending_dir.mkdir(parents=True, exist_ok=True)
        shape = f"Reply with one JSON object only, matching this schema:\n{json.dumps(request['reply_schema'])}\n\n" if request["reply_schema"] else ""
        files = []
        for block in request["system_blocks"]:
            shared = self.pending_dir / f"system-{hashlib.sha256(block.encode()).hexdigest()[:12]}.txt"
            shared.write_text(block, encoding="utf-8")
            files.append(str(shared))
        request = {**{k: v for k, v in request.items() if k != "system_blocks"}, "system_files": files}
        (self.pending_dir / f"{key}.request.json").write_text(json.dumps(request, ensure_ascii=False, indent=1), encoding="utf-8")
        listing = "The system prompt for this call is in these files, read in order:\n" + "\n".join(files)
        messages = "\n\n".join(f"[{m['role']}]\n{m['text']}" for m in request["messages"])
        (self.pending_dir / f"{key}.prompt.txt").write_text(shape + listing + "\n\n--- messages ---\n\n" + messages, encoding="utf-8")
        raise PendingReply(key)

    @staticmethod
    def _request(kind: str, kwargs: dict) -> dict:
        tools = kwargs.get("tools") or []
        return {
            "kind": kind,
            "reply_schema": tools[0]["input_schema"] if tools else None,
            "system_blocks": _blocks(kwargs.get("system")),
            "messages": [{"role": m["role"], "text": _message_text(m["content"])} for m in kwargs.get("messages", [])],
        }

    def stream(self, **kwargs):
        request = self._request("voice", kwargs)
        key = self._key("voice")
        return _SavedDraftStream(self._reply(key, "txt", request))

    def create(self, **kwargs):
        tools = kwargs.get("tools") or []
        if not tools:
            raise NotImplementedError("a call with no tool and no stream has no reply file form")
        name = tools[0]["name"]
        request = self._request(name, kwargs)
        key = self._key(name)
        try:
            tool_input = json.loads(self._reply(key, "json", request))
        except json.JSONDecodeError as error:
            raise ValueError(f"{key}: the reply file is not one JSON object ({error})") from error
        return _ToolResponse(name, tool_input)
