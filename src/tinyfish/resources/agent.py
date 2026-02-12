# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..types import agent_run_params, agent_run_async_params, agent_run_with_streaming_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.agent_run_response import AgentRunResponse
from ..types.agent_run_async_response import AgentRunAsyncResponse
from ..types.agent_run_with_streaming_response import AgentRunWithStreamingResponse

__all__ = ["AgentResource", "AsyncAgentResource"]


class AgentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tinyfish-io/agent-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tinyfish-io/agent-sdk-python#with_streaming_response
        """
        return AgentResourceWithStreamingResponse(self)

    def run(
        self,
        *,
        goal: str,
        url: str,
        browser_profile: Literal["lite", "stealth"] | Omit = omit,
        proxy_config: agent_run_params.ProxyConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRunResponse:
        """Execute a browser automation task synchronously and wait for completion.

        Returns
        the final result once the automation finishes (success or failure). Use this
        endpoint when you need the complete result in a single response.

        Args:
          goal: Natural language description of what to accomplish on the website

          url: Target website URL to automate

          browser_profile: Browser profile for execution. LITE uses standard browser, STEALTH uses
              anti-detection browser.

          proxy_config: Proxy configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/automation/run",
            body=maybe_transform(
                {
                    "goal": goal,
                    "url": url,
                    "browser_profile": browser_profile,
                    "proxy_config": proxy_config,
                },
                agent_run_params.AgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunResponse,
        )

    def run_async(
        self,
        *,
        goal: str,
        url: str,
        browser_profile: Literal["lite", "stealth"] | Omit = omit,
        proxy_config: agent_run_async_params.ProxyConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRunAsyncResponse:
        """
        Creates and enqueues an automation run, returning the run_id immediately without
        waiting for completion. Use this for long-running automations where you want to
        poll for results separately.

        Args:
          goal: Natural language description of what to accomplish on the website

          url: Target website URL to automate

          browser_profile: Browser profile for execution. LITE uses standard browser, STEALTH uses
              anti-detection browser.

          proxy_config: Proxy configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/automation/run-async",
            body=maybe_transform(
                {
                    "goal": goal,
                    "url": url,
                    "browser_profile": browser_profile,
                    "proxy_config": proxy_config,
                },
                agent_run_async_params.AgentRunAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunAsyncResponse,
        )

    def run_with_streaming(
        self,
        *,
        goal: str,
        url: str,
        browser_profile: Literal["lite", "stealth"] | Omit = omit,
        proxy_config: agent_run_with_streaming_params.ProxyConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[AgentRunWithStreamingResponse]:
        """
        Execute a browser automation task with Server-Sent Events (SSE) streaming.
        Returns a real-time event stream with automation progress, browser streaming
        URL, and final results.

        Args:
          goal: Natural language description of what to accomplish on the website

          url: Target website URL to automate

          browser_profile: Browser profile for execution. LITE uses standard browser, STEALTH uses
              anti-detection browser.

          proxy_config: Proxy configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            "/v1/automation/run-sse",
            body=maybe_transform(
                {
                    "goal": goal,
                    "url": url,
                    "browser_profile": browser_profile,
                    "proxy_config": proxy_config,
                },
                agent_run_with_streaming_params.AgentRunWithStreamingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, AgentRunWithStreamingResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[AgentRunWithStreamingResponse],
        )


class AsyncAgentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tinyfish-io/agent-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tinyfish-io/agent-sdk-python#with_streaming_response
        """
        return AsyncAgentResourceWithStreamingResponse(self)

    async def run(
        self,
        *,
        goal: str,
        url: str,
        browser_profile: Literal["lite", "stealth"] | Omit = omit,
        proxy_config: agent_run_params.ProxyConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRunResponse:
        """Execute a browser automation task synchronously and wait for completion.

        Returns
        the final result once the automation finishes (success or failure). Use this
        endpoint when you need the complete result in a single response.

        Args:
          goal: Natural language description of what to accomplish on the website

          url: Target website URL to automate

          browser_profile: Browser profile for execution. LITE uses standard browser, STEALTH uses
              anti-detection browser.

          proxy_config: Proxy configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/automation/run",
            body=await async_maybe_transform(
                {
                    "goal": goal,
                    "url": url,
                    "browser_profile": browser_profile,
                    "proxy_config": proxy_config,
                },
                agent_run_params.AgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunResponse,
        )

    async def run_async(
        self,
        *,
        goal: str,
        url: str,
        browser_profile: Literal["lite", "stealth"] | Omit = omit,
        proxy_config: agent_run_async_params.ProxyConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRunAsyncResponse:
        """
        Creates and enqueues an automation run, returning the run_id immediately without
        waiting for completion. Use this for long-running automations where you want to
        poll for results separately.

        Args:
          goal: Natural language description of what to accomplish on the website

          url: Target website URL to automate

          browser_profile: Browser profile for execution. LITE uses standard browser, STEALTH uses
              anti-detection browser.

          proxy_config: Proxy configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/automation/run-async",
            body=await async_maybe_transform(
                {
                    "goal": goal,
                    "url": url,
                    "browser_profile": browser_profile,
                    "proxy_config": proxy_config,
                },
                agent_run_async_params.AgentRunAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRunAsyncResponse,
        )

    async def run_with_streaming(
        self,
        *,
        goal: str,
        url: str,
        browser_profile: Literal["lite", "stealth"] | Omit = omit,
        proxy_config: agent_run_with_streaming_params.ProxyConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[AgentRunWithStreamingResponse]:
        """
        Execute a browser automation task with Server-Sent Events (SSE) streaming.
        Returns a real-time event stream with automation progress, browser streaming
        URL, and final results.

        Args:
          goal: Natural language description of what to accomplish on the website

          url: Target website URL to automate

          browser_profile: Browser profile for execution. LITE uses standard browser, STEALTH uses
              anti-detection browser.

          proxy_config: Proxy configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            "/v1/automation/run-sse",
            body=await async_maybe_transform(
                {
                    "goal": goal,
                    "url": url,
                    "browser_profile": browser_profile,
                    "proxy_config": proxy_config,
                },
                agent_run_with_streaming_params.AgentRunWithStreamingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(
                Any, AgentRunWithStreamingResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[AgentRunWithStreamingResponse],
        )


class AgentResourceWithRawResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.run = to_raw_response_wrapper(
            agent.run,
        )
        self.run_async = to_raw_response_wrapper(
            agent.run_async,
        )
        self.run_with_streaming = to_raw_response_wrapper(
            agent.run_with_streaming,
        )


class AsyncAgentResourceWithRawResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.run = async_to_raw_response_wrapper(
            agent.run,
        )
        self.run_async = async_to_raw_response_wrapper(
            agent.run_async,
        )
        self.run_with_streaming = async_to_raw_response_wrapper(
            agent.run_with_streaming,
        )


class AgentResourceWithStreamingResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.run = to_streamed_response_wrapper(
            agent.run,
        )
        self.run_async = to_streamed_response_wrapper(
            agent.run_async,
        )
        self.run_with_streaming = to_streamed_response_wrapper(
            agent.run_with_streaming,
        )


class AsyncAgentResourceWithStreamingResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.run = async_to_streamed_response_wrapper(
            agent.run,
        )
        self.run_async = async_to_streamed_response_wrapper(
            agent.run_async,
        )
        self.run_with_streaming = async_to_streamed_response_wrapper(
            agent.run_with_streaming,
        )
