# Roadmap

## v0.1 — Policy foundation

- Canonical `AGENTS.md`
- Lifecycle and risk model
- Provider-neutral design principles
- README onboarding

## v0.2 — Conformance (implemented)

- [x] Define a versioned JSON Schema and canonical policy document
- [x] Add valid/invalid evidence fixtures and a dependency-free validator
- [x] Specify lifecycle invariants and failure transitions
- [x] Document risk scoring, provider adapter capabilities, evidence, and threat boundaries

## v0.3 — Provider adapters

- Generate or maintain thin Claude Code, Codex, and Copilot instruction files
- Document installation and precedence rules
- Add adapter snapshots to detect accidental policy drift
- Validate provider event streams against the canonical lifecycle

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
2. Extend conformance scenarios from reports to provider event streams.
3. Make evidence structured and provider-independent.
4. Test failure behavior, not only happy-path compliance.
5. Treat adapters as generated or mechanically checked translations to prevent drift.
