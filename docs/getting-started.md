# Getting started

AI Imperare is a policy and documentation kit, not a package installed into
an agent runtime. Installation means vendoring the canonical policy into the
repository where an agent will work and placing a provider-specific instruction
file where that provider automatically loads it. The v0.2 validator uses only
the Python standard library; no `pip install` step is required.

## Requirements

* Git, if installing from the repository.
* Python 3.9 or newer for validation (`python --version`).
* One supported agent runtime: Claude Code, Codex, or GitHub Copilot.

## Install from a checkout

Clone AI Imperare once:

```bash
git clone https://github.com/Danialesss/ai-imperare.git
cd ai-imperare
python tools/validate.py
python -m unittest discover -s tests -v
```

The expected validator output is:

```text
AI Imperare v0.2 policy and fixtures are valid.
```

To install the policy into another project, copy the policy, documentation,
and validator into that project's repository. Run these commands from the
target project (replace `AI_IMPERARE` with the checkout path):

```bash
mkdir -p policy docs tools
cp "$AI_IMPERARE/policy/v0.2.policy.json" policy/
cp "$AI_IMPERARE/policy/v0.2.schema.json" policy/
cp "$AI_IMPERARE/docs/"*.md docs/
cp "$AI_IMPERARE/tools/validate.py" tools/
```

On Windows PowerShell, the equivalent is:

```powershell
New-Item -ItemType Directory -Force policy, docs, tools | Out-Null
Copy-Item "$env:AI_IMPERARE\policy\v0.2.policy.json" policy\
Copy-Item "$env:AI_IMPERARE\policy\v0.2.schema.json" policy\
Copy-Item "$env:AI_IMPERARE\docs\*.md" docs\
Copy-Item "$env:AI_IMPERARE\tools\validate.py" tools\
```

Set `AI_IMPERARE` to the absolute path of the checkout first. Do not blindly
overwrite an existing `AGENTS.md`, `CLAUDE.md`, or Copilot instruction file:
merge the provider section below into the existing file so local repository
rules remain intact.

## Connect a provider

The policy is the same for every provider. Only the instruction-file location
changes:

| Provider | Instruction file | Installation action |
| --- | --- | --- |
| Codex | `AGENTS.md` | Add the v0.2 policy references and lifecycle rules to the repository's existing `AGENTS.md`. |
| Claude Code | `CLAUDE.md` | Create or update `CLAUDE.md` with the same rules and links to `policy/v0.2.policy.json` and `docs/`. |
| GitHub Copilot | `.github/copilot-instructions.md` | Create the `.github` directory if needed and add the same rules and policy links. |

At minimum, the provider file must tell the agent to:

1. read `policy/v0.2.policy.json` before non-trivial work;
2. complete `requested -> discovered -> planned -> risk_assessed` before implementation;
3. use `blocked` when approval, context, or a required check prevents progress;
4. run `python tools/validate.py` when policy or conformance files change; and
5. report the v0.2 evidence fields: `task`, `policyVersion`, `finalState`,
   `acceptance`, `checks`, `risks`, and `limitations`.

## Use it on a coding task

For each task, ask the agent to follow the lifecycle and include explicit
acceptance criteria. A provider-neutral prompt can be pasted into any runtime:

```text
Read policy/v0.2.policy.json and docs/lifecycle.md.
Before editing, report:
- the requested outcome and affected files;
- acceptance criteria with IDs;
- the risk score and level using docs/risk-matrix.md;
- planned verification commands; and
- approval gates or assumptions.
Then implement the smallest complete change. Run the planned checks.
Finish with a v0.2 evidence report containing task, policyVersion, finalState,
acceptance, checks, risks, and limitations. Never claim a skipped or unrun
check passed.
```

For a documentation-only change, a typical local verification is:

```bash
python tools/validate.py
python -m unittest discover -s tests -v
git diff --check
```

For code changes, add the project's formatter, type checker, focused tests,
integration tests, and security checks to the `checks` array. A high-risk task
must also record a rollback plan and obtain approval for the gates listed in
`policy/v0.2.policy.json`.

## Produce and validate an evidence report

Save a report such as `evidence/task-001.json` (the location is a repository
choice) using the contract in [`evidence-contract.md`](evidence-contract.md):

```json
{
  "task": "Add request validation",
  "policyVersion": "0.2",
  "finalState": "reported",
  "acceptance": [
    {
      "id": "AC-1",
      "statement": "Invalid requests return a documented error",
      "status": "met",
      "evidenceRefs": ["check-1"]
    }
  ],
  "checks": [
    {
      "id": "check-1",
      "command": "python -m unittest discover -s tests -v",
      "status": "passed",
      "result": "12 tests passed"
    }
  ],
  "risks": [
    {
      "statement": "Input parsing affects the public API",
      "score": 5,
      "level": "medium",
      "mitigation": "Focused API tests and caller review"
    }
  ],
  "limitations": []
}
```

The included `tools/validate.py` validates the policy and its representative
fixtures. It does not yet validate arbitrary report files; use the documented
shape and keep provider-specific report ingestion in the adapter layer.

## Updating the policy

Treat `policy/v0.2.policy.json` and `policy/v0.2.schema.json` as a versioned
pair. When changing required fields or lifecycle semantics, create a new
versioned pair (for example `v0.3`) rather than silently changing v0.2. Update
the linked docs, fixtures, tests, and provider instruction files together.
