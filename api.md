# Agent

Types:

```python
from tinyfish.types import AgentRunResponse, AgentRunAsyncResponse, AgentRunWithStreamingResponse
```

Methods:

- <code title="post /v1/automation/run">client.agent.<a href="./src/tinyfish/resources/agent.py">run</a>(\*\*<a href="src/tinyfish/types/agent_run_params.py">params</a>) -> <a href="./src/tinyfish/types/agent_run_response.py">AgentRunResponse</a></code>
- <code title="post /v1/automation/run-async">client.agent.<a href="./src/tinyfish/resources/agent.py">run_async</a>(\*\*<a href="src/tinyfish/types/agent_run_async_params.py">params</a>) -> <a href="./src/tinyfish/types/agent_run_async_response.py">AgentRunAsyncResponse</a></code>
- <code title="post /v1/automation/run-sse">client.agent.<a href="./src/tinyfish/resources/agent.py">run_with_streaming</a>(\*\*<a href="src/tinyfish/types/agent_run_with_streaming_params.py">params</a>) -> <a href="./src/tinyfish/types/agent_run_with_streaming_response.py">AgentRunWithStreamingResponse</a></code>

# Runs

Types:

```python
from tinyfish.types import RunRetrieveResponse, RunListResponse
```

Methods:

- <code title="get /v1/runs/{id}">client.runs.<a href="./src/tinyfish/resources/runs.py">retrieve</a>(id) -> <a href="./src/tinyfish/types/run_retrieve_response.py">RunRetrieveResponse</a></code>
- <code title="get /v1/runs">client.runs.<a href="./src/tinyfish/resources/runs.py">list</a>(\*\*<a href="src/tinyfish/types/run_list_params.py">params</a>) -> <a href="./src/tinyfish/types/run_list_response.py">RunListResponse</a></code>
