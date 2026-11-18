"""Records what the voice stream returned, without changing it.

CapturingClient wraps a client and keeps, for every streamed voice call, the
model's raw tagged text, the stop reason, the request settings and the
timings. Every other call passes through untouched. A caller slices the log
by position (mark() before a turn, since(mark) after it) to attach the calls
to the turn that made them.
"""
import time


class _CapturedStream:
    def __init__(self, inner, call):
        self._inner = inner
        self._call = call
        self.text_stream = self._timed(inner.text_stream)

    def _timed(self, chunks):
        for chunk in chunks:
            self._call.setdefault("seconds_to_first_text", round(time.monotonic() - self._call["_started"], 3))
            yield chunk

    def get_final_message(self):
        message = self._inner.get_final_message()
        self._call["raw_text"] = "".join(
            getattr(block, "text", "") for block in (getattr(message, "content", None) or []) if getattr(block, "type", None) == "text"
        )
        self._call["stop_reason"] = getattr(message, "stop_reason", None)
        return message


class _CapturedStreamContext:
    def __init__(self, inner_ctx, call):
        self._inner_ctx = inner_ctx
        self._call = call

    def __enter__(self):
        return _CapturedStream(self._inner_ctx.__enter__(), self._call)

    def __exit__(self, *exc):
        self._call["seconds_total"] = round(time.monotonic() - self._call.pop("_started"), 3)
        return self._inner_ctx.__exit__(*exc)


class _CapturingMessages:
    def __init__(self, inner, calls):
        self._inner = inner
        self._calls = calls

    def stream(self, **kwargs):
        call = {
            "request": {"model": kwargs.get("model"), "max_tokens": kwargs.get("max_tokens")},
            "_started": time.monotonic(),
        }
        self._calls.append(call)
        return _CapturedStreamContext(self._inner.stream(**kwargs), call)

    def create(self, **kwargs):
        return self._inner.create(**kwargs)


class CapturingClient:
    def __init__(self, inner):
        self.calls: list[dict] = []
        self.messages = _CapturingMessages(inner.messages, self.calls)

    def mark(self) -> int:
        return len(self.calls)

    def since(self, mark: int) -> list[dict]:
        return [{k: v for k, v in call.items() if not k.startswith("_")} for call in self.calls[mark:]]
