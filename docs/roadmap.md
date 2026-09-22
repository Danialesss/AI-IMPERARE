# Roadmap

## v0.1 — Policy foundation

- Canonical `AGENTS.md`
- Lifecycle and risk model
- Provider-neutral design principles
- README onboarding

## v0.2 — Conformance

- Define a versioned policy schema
- Add scenario fixtures for planning, testing, failure reporting, and approval boundaries
- Build a runner that checks agent transcripts/evidence against the schema
- Add policy versioning and changelog rules

## v0.3 — Provider adapters

- Generate or maintain thin Claude Code, Codex, and Copilot instruction files
- Document installation and precedence rules
- Add adapter snapshots to detect accidental policy drift

## v0.4 — Developer workflow

- Add templates for plans, evidence reports, and risk assessments
- Add CI validation for policy files and examples
- Add a local command for repository conformance checks

## v1.0 — Operational maturity

- Integrate with pull request checks without replacing human review
- Support repository-specific profiles while preserving mandatory gates
- Add metrics for verification coverage, escaped defects, unsupported claims, and approval violations
- Publish a security model and threat assessment

## First implementation priorities

1. Keep the core policy short enough that agents reliably load it.
2. Build conformance scenarios before adding complex orchestration.
3. Make evidence structured and provider-independent.
4. Test failure behavior, not only happy-path compliance.
5. Treat adapters as generated or mechanically checked translations to prevent drift.
