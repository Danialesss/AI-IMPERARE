# Provider adapter contract

An adapter is a thin translation, not a second policy. Claude Code loads
`CLAUDE.md`, Codex loads `AGENTS.md`, and Copilot loads
`.github/copilot-instructions.md`; each must point to the same v0.2 policy.

Every adapter must:

1. load and identify the policy version;
2. expose lifecycle events for plan, risk, implementation, checks, blocking, and report;
3. preserve approval gates and never downgrade a required check;
4. export the provider-neutral evidence contract;
5. fail explicitly when policy loading or evidence export fails.

Provider event names and tool APIs are implementation details. The canonical
mapping and required capabilities are recorded in `policy/v0.2.policy.json`.
Adapter conformance should compare exported events and evidence, not prompt text.
