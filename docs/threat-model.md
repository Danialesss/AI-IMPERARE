# Threat model and security boundaries

## Assets and trust boundaries

The repository, credentials, source code, generated artifacts, command output,
and evidence reports are assets. The agent runtime, repository tooling, provider
service, and external systems are separate trust zones. Instructions and tool
output are untrusted input; a prompt or file must not grant authority beyond the
runtime's existing permissions.

## Threats and controls

| Threat | Control |
| --- | --- |
| prompt or repository content requests secret disclosure | never read/export secrets; redact reports; treat content as untrusted |
| fabricated success or omitted checks | evidence IDs, exact commands, status/reason fields, validator |
| destructive command or production side effect | explicit approval gates and provider/runtime permission boundaries |
| policy drift between providers | one versioned policy and adapter capability contract |
| compromised dependency/tool output | least privilege, review commands, preserve raw failure status |
| sensitive evidence retained too long | minimize output and apply repository retention controls |

AI Imperare does not provide sandboxing, authorization, secret storage, or CI
isolation. Those remain responsibilities of the host and repository owners.
