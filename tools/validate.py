"""Dependency-free conformance checks for the AI Imperare v0.2 contracts."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def validate_policy(policy):
    errors = []
    lifecycle = policy.get("lifecycle", {})
    states = set(lifecycle.get("states", []))
    if policy.get("version") != "0.2":
        errors.append("policy version must be 0.2")
    if lifecycle.get("initialState") not in states:
        errors.append("initial state must be declared in states")
    if not set(lifecycle.get("terminalStates", [])) <= states:
        errors.append("terminal states must be declared in states")
    for transition in lifecycle.get("transitions", []):
        if transition.get("from") not in states or transition.get("to") not in states:
            errors.append("transition references an unknown state")
        if transition.get("from") in set(lifecycle.get("terminalStates", [])):
            errors.append("terminal states cannot have outgoing transitions")
    required = {"task", "policyVersion", "finalState", "acceptance", "checks", "risks", "limitations"}
    if set(policy.get("evidenceContract", {}).get("requiredFields", [])) != required:
        errors.append("evidence requiredFields do not match the report contract")
    if not policy.get("adapters") or not policy.get("securityBoundaries", {}).get("approvalGates"):
        errors.append("adapters and approval gates are required")
    return errors


def validate_report(report):
    errors = []
    required = {"task", "policyVersion", "finalState", "acceptance", "checks", "risks", "limitations"}
    missing = required - report.keys()
    if missing:
        errors.append("missing report fields: " + ", ".join(sorted(missing)))
    if report.get("policyVersion") != "0.2":
        errors.append("report policyVersion must be 0.2")
    checks = report.get("checks", [])
    for check in checks:
        if check.get("status") in {"failed", "skipped", "not_run"} and not check.get("reason"):
            errors.append("non-passing checks require a reason")
    if report.get("finalState") == "reported" and any(c.get("status") != "passed" for c in checks):
        errors.append("reported state requires every check to pass")
    references = {ref for item in report.get("acceptance", []) for ref in item.get("evidenceRefs", [])}
    check_ids = {check.get("id") for check in checks}
    for item in report.get("acceptance", []):
        if item.get("status") == "met" and not references & check_ids:
            errors.append("met acceptance items require evidence references")
            break
    return errors


def main():
    policy = load(ROOT / "policy" / "v0.2.policy.json")
    errors = validate_policy(policy)
    for path, expected in [
        (ROOT / "conformance" / "fixtures" / "valid-report.json", False),
        (ROOT / "conformance" / "fixtures" / "invalid-report.json", True),
    ]:
        report_errors = validate_report(load(path))
        if bool(report_errors) != expected:
            errors.append(f"unexpected fixture result for {path.name}: {report_errors}")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("AI Imperare v0.2 policy and fixtures are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
