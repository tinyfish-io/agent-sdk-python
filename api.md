# Automation

Types:

```python
from tinyfish.types import (
    AutomationRunAsyncResponse,
    AutomationRunSyncResponse,
    AutomationRunWithSseResponse,
)
```

Methods:

- <code title="post /v1/automation/run-async">client.automation.<a href="./src/tinyfish/resources/automation.py">run_async</a>(\*\*<a href="src/tinyfish/types/automation_run_async_params.py">params</a>) -> <a href="./src/tinyfish/types/automation_run_async_response.py">AutomationRunAsyncResponse</a></code>
- <code title="post /v1/automation/run">client.automation.<a href="./src/tinyfish/resources/automation.py">run_sync</a>(\*\*<a href="src/tinyfish/types/automation_run_sync_params.py">params</a>) -> <a href="./src/tinyfish/types/automation_run_sync_response.py">AutomationRunSyncResponse</a></code>
- <code title="post /v1/automation/run-sse">client.automation.<a href="./src/tinyfish/resources/automation.py">run_with_sse</a>(\*\*<a href="src/tinyfish/types/automation_run_with_sse_params.py">params</a>) -> <a href="./src/tinyfish/types/automation_run_with_sse_response.py">AutomationRunWithSseResponse</a></code>

# Runs

Types:

```python
from tinyfish.types import RunRetrieveResponse, RunListResponse
```

Methods:

- <code title="get /v1/runs/{id}">client.runs.<a href="./src/tinyfish/resources/runs.py">retrieve</a>(id) -> <a href="./src/tinyfish/types/run_retrieve_response.py">RunRetrieveResponse</a></code>
- <code title="get /v1/runs">client.runs.<a href="./src/tinyfish/resources/runs.py">list</a>(\*\*<a href="src/tinyfish/types/run_list_params.py">params</a>) -> <a href="./src/tinyfish/types/run_list_response.py">RunListResponse</a></code>
