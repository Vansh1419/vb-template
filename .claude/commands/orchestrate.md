---
description: Split a big task across worker agents (orchestrator + workers)
---
Task: $ARGUMENTS

You are the orchestrator. Do not write code yourself.
1. Use the `planner` agent to split the task into independent steps. Show me and wait for approval.
2. Give each independent step to a separate `worker` agent, in parallel where steps don't touch the same files.
3. When workers finish, use the `tester` agent to run tests and the `reviewer` agent to review the full diff.
4. Send any issues back to a `worker`. Max 3 rounds, then ask me.
5. Give me a short final summary.
