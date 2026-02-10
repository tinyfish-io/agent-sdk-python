# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    cursor: str
    """Cursor for pagination (from previous response)"""

    limit: int
    """Maximum number of results to return (1-100)"""

    status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    """Filter by run status"""
