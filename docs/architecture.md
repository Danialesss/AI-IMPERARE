# Operating Model

## 1. Product shape

AI Imperare should remain a small core policy plus provider adapters:

```text
                 +----------------------+
                 |  Canonical policy    |
                 |  AGENTS.md + schema  |
                 +----------+-----------+
                            |
        +-------------------+-------------------+
        |                   |                   |
  Claude adapter      Codex adapter      Copilot adapter
  CLAUDE.md           AGENTS.md          copilot instructions
        |                   |                   |
        +-------------------+-------------------+
                            |
                 Conformance checker/runner
```

The policy defines engineering behavior. Adapters define only where the policy is loaded and how lifecycle events are represented. No adapter may remove a safety gate.

## 2. State machine

```text
request
  -> discovered
  -> planned
  -> risk-predicted
  -> implementing
  -> verifying
  -> tested
  -> reported
```

An agent may return to an earlier state when evidence invalidates an assumption. It must not skip directly from request to implementation for non-trivial work.

## 3. Risk-based verification

| Risk | Examples | Minimum evidence |
| --- | --- | --- |
| Low | docs, isolated formatting, local wording | diff inspection and relevant lint/docs check |
| Medium | business logic, API behavior, persistence | focused tests, type/build check, caller review |
| High | auth, payments, migrations, concurrency, deployment | focused and integration tests, security review, rollback plan, explicit human approval where applicable |

The agent should select checks based on affected behavior, not a fixed ritual. A skipped check is a reported limitation, never an implicit pass.

## 4. Control surfaces

- **Repository policy:** instruction files and contribution docs.
- **Execution policy:** allowlists, approval boundaries, and command safety.
- **Evidence ledger:** commands run, outputs, changed files, assumptions, and unresolved risks.
- **Conformance tests:** scenarios that detect skipped planning, missing tests, unsafe claims, and ignored failures.
- **Provider adapters:** thin translations for Claude Code, Codex, Copilot, and future tools.

## 5. Evidence record

The eventual machine-readable evidence format should capture:

```yaml
task: "short description"
acceptance:
  - id: AC-1
    statement: "..."
    status: met
checks:
  - command: "npm test -- --runInBand"
    status: passed
    notes: "42 tests"
risks:
  - statement: "..."
    mitigation: "..."
limitations:
  - "..."
```

This record makes reports auditable without requiring a specific model or provider.

## 6. Non-goals

AI Imperare is not a replacement for CI, code ownership, security review, production change management, or human accountability. It improves agent behavior; it does not grant an agent authority it did not already have.
