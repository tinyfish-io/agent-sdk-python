# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RunListResponse", "Data", "DataBrowserConfig", "DataError", "Pagination"]


class DataBrowserConfig(BaseModel):
    """Browser configuration used for the run"""

    browser_type: Optional[str] = None
    """Type of browser used"""

    proxy_country_code: Optional[str] = None
    """Country code for proxy"""

    proxy_enabled: Optional[bool] = None
    """Whether proxy was enabled"""


class DataError(BaseModel):
    """Error details. Null if the run succeeded or is still running."""

    message: str
    """Error message describing why the run failed"""


class Data(BaseModel):
    """A single automation run"""

    browser_config: Optional[DataBrowserConfig] = None
    """Browser configuration used for the run"""

    created_at: str
    """ISO 8601 timestamp when run was created"""

    error: Optional[DataError] = None
    """Error details. Null if the run succeeded or is still running."""

    finished_at: Optional[str] = None
    """ISO 8601 timestamp when run finished"""

    goal: str
    """Natural language goal for this automation run"""

    result: Optional[Dict[str, Optional[object]]] = None
    """Extracted data from the automation run"""

    run_id: str
    """Unique identifier for the run"""

    started_at: Optional[str] = None
    """ISO 8601 timestamp when run started executing"""

    status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    """Current status of the run"""

    streaming_url: Optional[str] = None
    """URL to watch live browser session (available while running)"""


class Pagination(BaseModel):
    """Pagination information"""

    has_more: bool
    """Whether there are more results after this page"""

    next_cursor: Optional[str] = None
    """Cursor for fetching next page. Null if no more results."""


class RunListResponse(BaseModel):
    """Paginated list of runs"""

    data: List[Data]
    """Array of runs"""

    pagination: Pagination
    """Pagination information"""
