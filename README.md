# AI Imperare

**A provider-neutral operating system for professional AI coding agents.**

AI Imperare defines how an AI coding tool should plan, implement, verify, test, and communicate changes across Claude Code, Codex, Copilot, and other agent runtimes. It is intentionally tool-agnostic: the engineering process is the source of truth, while adapters translate it into each provider's native rule or instruction format.

## Core promise

> Never change code without understanding the repository, stating the plan, defining verification, and reporting evidence.

The agent must optimize for **correctness, safety, maintainability, and traceability**—not merely producing a plausible patch.

## Repository layout

| Path | Purpose |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | Canonical rule set to place at the repository root or provide to an agent |
| [`docs/architecture.md`](docs/architecture.md) | Operating model, lifecycle, gates, and provider adapter strategy |
| [`docs/roadmap.md`](docs/roadmap.md) | Incremental plan for turning the rule into a reusable product |

## The lifecycle

1. **Discover** — inspect repository conventions, dependencies, history, constraints, and affected surfaces.
2. **Plan** — state the goal, assumptions, files, risks, acceptance criteria, and verification commands.
3. **Predict** — identify likely regressions, edge cases, security concerns, operational impact, and rollback strategy.
4. **Implement** — make the smallest complete change, following existing patterns and preserving unrelated work.
5. **Verify** — inspect the diff, run focused checks, then broaden validation according to risk.
6. **Test** — add or update tests for behavior and failure modes; do not rely on compilation alone.
7. **Report** — summarize changes, evidence, known limitations, and any follow-up required.

## Design principles

- **Evidence over confidence:** every success claim has a command, result, or explicit limitation.
- **Small reversible changes:** avoid speculative refactors and unrelated cleanup.
- **Human-controlled risk:** destructive, production, credential, migration, and publish actions require explicit approval.
- **Provider neutrality:** one canonical policy, many thin adapters.
- **Fail loudly:** never hide errors behind broad catches, silent fallbacks, or unverified success.
- **Operational thinking:** consider observability, deployment, rollback, performance, and supportability—not just source code.

## How to use it

Copy `AGENTS.md` into a project, or adapt its sections into:

- Claude Code: `CLAUDE.md`
- Codex: `AGENTS.md`
- GitHub Copilot: `.github/copilot-instructions.md`
- Other tools: their equivalent repository instruction file

Keep the canonical policy unchanged where possible. Provider-specific files should only describe invocation syntax, not weaken the engineering gates.

## Status

The repository currently contains the v0.1 operating policy and product roadmap. The next milestone is a conformance test suite and provider adapters that can validate whether an agent followed the lifecycle.

## License

MIT. See [`LICENSE`](LICENSE).
