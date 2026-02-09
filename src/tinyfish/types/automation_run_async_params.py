# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AutomationRunAsyncParams", "ProxyConfig"]


class AutomationRunAsyncParams(TypedDict, total=False):
    goal: Required[str]
    """Natural language description of what to accomplish on the website"""

    url: Required[str]
    """Target website URL to automate"""

    browser_profile: Literal["lite", "stealth"]
    """Browser profile for execution.

    LITE uses standard browser, STEALTH uses anti-detection browser.
    """

    proxy_config: ProxyConfig
    """Proxy configuration"""


class ProxyConfig(TypedDict, total=False):
    """Proxy configuration"""

    enabled: Required[bool]
    """Enable proxy for this automation run"""

    country_code: Literal["US", "GB", "CA", "DE", "FR", "JP", "AU"]
    """ISO 3166-1 alpha-2 country code for proxy location"""
