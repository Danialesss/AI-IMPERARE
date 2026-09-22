# Risk scoring and verification matrix

Score each dimension from 0 (negligible) to 2 (material), then sum:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| blast radius | one local file | one service or package | shared or production surface |
| data sensitivity | no sensitive data | internal data | credentials, personal, or regulated data |
| reversibility | trivial revert | recoverable migration | destructive or hard to restore |
| change uncertainty | isolated/documented | multiple callers | novel or poorly understood |
| concurrency/availability | offline | non-critical runtime | stateful or availability-critical |

Map totals to the policy levels: low 0–3, medium 4–6, high 7–10. High-risk
work requires an explicit approval gate and a rollback plan. The minimum
evidence for each level is machine-readable in `policy/v0.2.policy.json`.
Skipped evidence is a limitation, not a pass.
