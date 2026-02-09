# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AutomationRunAsyncResponse", "Error"]


class Error(BaseModel):
    """Error details. Null if successful."""

    message: str
    """Error message if run creation failed"""


class AutomationRunAsyncResponse(BaseModel):
    """Async automation run response.

    Returns run_id immediately without waiting for completion.
    """

    error: Optional[Error] = None
    """Error details. Null if successful."""

    run_id: Optional[str] = None
    """Unique identifier for the created automation run"""
