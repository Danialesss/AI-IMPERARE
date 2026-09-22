# Lifecycle and state machine

The v0.2 lifecycle is a finite state machine. `policy/v0.2.policy.json` is the
machine-readable source; this document explains how providers should implement it.

## States and transitions

Normal work moves `requested -> discovered -> planned -> risk_assessed ->
implementing -> verifying -> tested -> reported`. A provider may move to
`blocked` from any active state when the corresponding failure or approval event
occurs. It may return to an earlier active state only when new evidence
invalidates an assumption; the evidence record must explain the rewind.

The validator enforces that states and transition endpoints exist, the initial
state is present, terminal states are declared, and no transition leaves a
terminal state. Implementations must also enforce these invariants:

* implementation requires both a plan and a risk assessment;
* required check failures cannot be reported as success;
* every report claim points to evidence or is marked unverified;
* blocked work includes a reason, recovery attempt, and safe next action.

Providers may expose richer internal states, but their exported event stream
must map to these canonical states without skipping a required gate.
