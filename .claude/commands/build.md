---
description: Build the next step, then review it (plan → build → review loop)
---
Step: $ARGUMENTS (if empty, take the next unchecked step in `docs/PLAN.md`)

Loop:
1. Implement only this step. Follow CLAUDE.md rules.
2. Run the tests.
3. Ask the `reviewer` agent to review the diff.
4. If the reviewer finds issues, fix them and go back to 2. Max 3 rounds, then ask me.
5. Tick the step in `docs/PLAN.md` and give me a short summary.
