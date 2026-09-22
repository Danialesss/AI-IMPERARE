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
requested -> discovered -> planned -> risk_assessed
    -> implementing -> verifying -> tested -> reported
                         \-> blocked
```

The normative transitions and failure events are in [`lifecycle.md`](lifecycle.md)
and `policy/v0.2.policy.json`. An agent may return to an earlier state when
evidence invalidates an assumption, but must record the rewind. It must not
skip directly from requested to implementation.

## 3. Risk-based verification

| Risk | Examples | Minimum evidence |
| --- | --- | --- |
| Low (0–3) | docs, isolated formatting, local wording | diff inspection and relevant lint/docs check |
| Medium (4–6) | business logic, API behavior, persistence | focused tests, type/build check, caller review |
| High (7–10) | auth, payments, migrations, concurrency, deployment | focused and integration tests, security review, rollback plan, explicit human approval where applicable |

The scoring dimensions and machine-readable minimum evidence are in
[`risk-matrix.md`](risk-matrix.md). A skipped check is a reported limitation,
never an implicit pass.

## 4. Control surfaces

- **Repository policy:** instruction files and contribution docs.
- **Execution policy:** allowlists, approval boundaries, and command safety.
- **Evidence ledger:** commands run, outputs, changed files, assumptions, and unresolved risks.
- **Conformance tests:** scenarios that detect skipped planning, missing tests, unsafe claims, and ignored failures.
- **Provider adapters:** thin translations for Claude Code, Codex, Copilot, and future tools.

## 5. Evidence record

The v0.2 JSON report contract is defined in [`evidence-contract.md`](evidence-contract.md).
It makes reports auditable without requiring a specific model or provider.

## 6. Non-goals

AI Imperare is not a replacement for CI, code ownership, security review, production change management, or human accountability. It improves agent behavior; it does not grant an agent authority it did not already have.
