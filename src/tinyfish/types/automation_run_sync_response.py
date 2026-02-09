# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AutomationRunSyncResponse", "Error"]


class Error(BaseModel):
    """Error details. Null if the run succeeded."""

    message: str
    """Error message describing why the run failed"""


class AutomationRunSyncResponse(BaseModel):
    """Automation run response.

    Check status to determine success/failure. On success: result is populated, error is null. On failure: result is null, error contains message.
    """

    error: Optional[Error] = None
    """Error details. Null if the run succeeded."""

    finished_at: Optional[str] = None
    """ISO 8601 timestamp when the run finished"""

    num_of_steps: float
    """Number of steps taken during the automation"""

    result: Optional[Dict[str, Optional[object]]] = None
    """Structured JSON result extracted from the automation. Null if the run failed."""

    run_id: Optional[str] = None
    """Unique identifier for the automation run"""

    started_at: Optional[str] = None
    """ISO 8601 timestamp when the run started"""

    status: Literal["COMPLETED", "FAILED"]
    """Final status of the automation run"""
