# Agent

Types:

```python
from tinyfish.types import AgentRunAsyncResponse, AgentRunSyncResponse, AgentRunWithSseResponse
```

Methods:

- <code title="post /v1/automation/run-async">client.agent.<a href="./src/tinyfish/resources/agent.py">run_async</a>(\*\*<a href="src/tinyfish/types/agent_run_async_params.py">params</a>) -> <a href="./src/tinyfish/types/agent_run_async_response.py">AgentRunAsyncResponse</a></code>
- <code title="post /v1/automation/run">client.agent.<a href="./src/tinyfish/resources/agent.py">run_sync</a>(\*\*<a href="src/tinyfish/types/agent_run_sync_params.py">params</a>) -> <a href="./src/tinyfish/types/agent_run_sync_response.py">AgentRunSyncResponse</a></code>
- <code title="post /v1/automation/run-sse">client.agent.<a href="./src/tinyfish/resources/agent.py">run_with_sse</a>(\*\*<a href="src/tinyfish/types/agent_run_with_sse_params.py">params</a>) -> <a href="./src/tinyfish/types/agent_run_with_sse_response.py">AgentRunWithSseResponse</a></code>

# Runs

Types:

```python
from tinyfish.types import RunRetrieveResponse, RunListResponse
```

Methods:

- <code title="get /v1/runs/{id}">client.runs.<a href="./src/tinyfish/resources/runs.py">retrieve</a>(id) -> <a href="./src/tinyfish/types/run_retrieve_response.py">RunRetrieveResponse</a></code>
- <code title="get /v1/runs">client.runs.<a href="./src/tinyfish/resources/runs.py">list</a>(\*\*<a href="src/tinyfish/types/run_list_params.py">params</a>) -> <a href="./src/tinyfish/types/run_list_response.py">RunListResponse</a></code>
