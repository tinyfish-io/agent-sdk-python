# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AgentRunWithStreamingResponse",
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember3",
    "UnionMember4",
]


class UnionMember0(BaseModel):
    run_id: str = FieldInfo(alias="runId")

    timestamp: str

    type: Literal["STARTED"]


class UnionMember1(BaseModel):
    run_id: str = FieldInfo(alias="runId")

    streaming_url: str = FieldInfo(alias="streamingUrl")

    timestamp: str

    type: Literal["STREAMING_URL"]


class UnionMember2(BaseModel):
    run_id: str = FieldInfo(alias="runId")

    status: Literal["COMPLETED", "FAILED", "CANCELLED"]

    timestamp: str

    type: Literal["COMPLETE"]

    error: Optional[str] = None

    result_json: Optional[Dict[str, Optional[object]]] = FieldInfo(alias="resultJson", default=None)


class UnionMember3(BaseModel):
    timestamp: str

    type: Literal["HEARTBEAT"]


class UnionMember4(BaseModel):
    purpose: str

    run_id: str = FieldInfo(alias="runId")

    timestamp: str

    type: Literal["PROGRESS"]


AgentRunWithStreamingResponse: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4]
