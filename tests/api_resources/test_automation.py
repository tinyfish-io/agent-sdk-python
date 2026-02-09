# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tinyfish import Tinyfish, AsyncTinyfish
from tests.utils import assert_matches_type
from tinyfish.types import (
    AutomationRunSyncResponse,
    AutomationRunAsyncResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutomation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_async(self, client: Tinyfish) -> None:
        automation = client.automation.run_async(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        )
        assert_matches_type(AutomationRunAsyncResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_async_with_all_params(self, client: Tinyfish) -> None:
        automation = client.automation.run_async(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
            browser_profile="lite",
            proxy_config={
                "enabled": True,
                "country_code": "US",
            },
        )
        assert_matches_type(AutomationRunAsyncResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_async(self, client: Tinyfish) -> None:
        response = client.automation.with_raw_response.run_async(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(AutomationRunAsyncResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_async(self, client: Tinyfish) -> None:
        with client.automation.with_streaming_response.run_async(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(AutomationRunAsyncResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_sync(self, client: Tinyfish) -> None:
        automation = client.automation.run_sync(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        )
        assert_matches_type(AutomationRunSyncResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_sync_with_all_params(self, client: Tinyfish) -> None:
        automation = client.automation.run_sync(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
            browser_profile="lite",
            proxy_config={
                "enabled": True,
                "country_code": "US",
            },
        )
        assert_matches_type(AutomationRunSyncResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_sync(self, client: Tinyfish) -> None:
        response = client.automation.with_raw_response.run_sync(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(AutomationRunSyncResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_sync(self, client: Tinyfish) -> None:
        with client.automation.with_streaming_response.run_sync(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(AutomationRunSyncResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_method_run_with_sse(self, client: Tinyfish) -> None:
        automation_stream = client.automation.run_with_sse(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        )
        automation_stream.response.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_method_run_with_sse_with_all_params(self, client: Tinyfish) -> None:
        automation_stream = client.automation.run_with_sse(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
            browser_profile="lite",
            proxy_config={
                "enabled": True,
                "country_code": "US",
            },
        )
        automation_stream.response.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_raw_response_run_with_sse(self, client: Tinyfish) -> None:
        response = client.automation.with_raw_response.run_with_sse(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_streaming_response_run_with_sse(self, client: Tinyfish) -> None:
        with client.automation.with_streaming_response.run_with_sse(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncAutomation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_async(self, async_client: AsyncTinyfish) -> None:
        automation = await async_client.automation.run_async(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        )
        assert_matches_type(AutomationRunAsyncResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_async_with_all_params(self, async_client: AsyncTinyfish) -> None:
        automation = await async_client.automation.run_async(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
            browser_profile="lite",
            proxy_config={
                "enabled": True,
                "country_code": "US",
            },
        )
        assert_matches_type(AutomationRunAsyncResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_async(self, async_client: AsyncTinyfish) -> None:
        response = await async_client.automation.with_raw_response.run_async(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AutomationRunAsyncResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_async(self, async_client: AsyncTinyfish) -> None:
        async with async_client.automation.with_streaming_response.run_async(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AutomationRunAsyncResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_sync(self, async_client: AsyncTinyfish) -> None:
        automation = await async_client.automation.run_sync(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        )
        assert_matches_type(AutomationRunSyncResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_sync_with_all_params(self, async_client: AsyncTinyfish) -> None:
        automation = await async_client.automation.run_sync(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
            browser_profile="lite",
            proxy_config={
                "enabled": True,
                "country_code": "US",
            },
        )
        assert_matches_type(AutomationRunSyncResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_sync(self, async_client: AsyncTinyfish) -> None:
        response = await async_client.automation.with_raw_response.run_sync(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AutomationRunSyncResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_sync(self, async_client: AsyncTinyfish) -> None:
        async with async_client.automation.with_streaming_response.run_sync(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AutomationRunSyncResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_method_run_with_sse(self, async_client: AsyncTinyfish) -> None:
        automation_stream = await async_client.automation.run_with_sse(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        )
        await automation_stream.response.aclose()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_method_run_with_sse_with_all_params(self, async_client: AsyncTinyfish) -> None:
        automation_stream = await async_client.automation.run_with_sse(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
            browser_profile="lite",
            proxy_config={
                "enabled": True,
                "country_code": "US",
            },
        )
        await automation_stream.response.aclose()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_raw_response_run_with_sse(self, async_client: AsyncTinyfish) -> None:
        response = await async_client.automation.with_raw_response.run_with_sse(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_streaming_response_run_with_sse(self, async_client: AsyncTinyfish) -> None:
        async with async_client.automation.with_streaming_response.run_with_sse(
            goal="Find the pricing page and extract all plan details",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
