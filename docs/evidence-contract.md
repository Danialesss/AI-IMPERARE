# Evidence and report contract

Providers export one JSON report per task. It must contain:

```json
{
  "task": "short description",
  "policyVersion": "0.2",
  "finalState": "reported",
  "acceptance": [{"id": "AC-1", "statement": "...", "status": "met", "evidenceRefs": ["check-1"]}],
  "checks": [{"id": "check-1", "command": "python -m unittest", "status": "passed", "result": "6 tests passed"}],
  "risks": [{"statement": "...", "score": 4, "level": "medium", "mitigation": "..."}],
  "limitations": []
}
```

`finalState` is `reported` only when required checks passed. A check with
`skipped`, `not_run`, or `failed` status requires a non-empty reason. Reports
must not contain secrets or raw credentials. Claims in a human summary should
refer to check IDs, acceptance IDs, or explicit limitations.
