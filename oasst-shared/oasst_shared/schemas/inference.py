import random

import pydantic

from . import protocol


class WorkerConfig(pydantic.BaseModel):
    model_name: str = "distilgpt2"


class WorkRequest(pydantic.BaseModel):
    conversation: protocol.Conversation = pydantic.Field(..., repr=False)
    model_name: str = "distilgpt2"
    max_new_tokens: int = 100
    seed: int = pydantic.Field(default_factory=lambda: random.randint(0, 2**31 - 1))
    do_sample: bool = True
    top_k: int = 50
    top_p: float = 0.9
    temperature: float = 1.0


class TokenResponse(pydantic.BaseModel):
    text: str
    log_prob: float
    token_id: int


class GeneratedTextResponse(pydantic.BaseModel):
    text: str


class WorkResponsePacket(pydantic.BaseModel):
    token: TokenResponse | None = None
    generated_text: GeneratedTextResponse | None = None
    is_end: bool = False
