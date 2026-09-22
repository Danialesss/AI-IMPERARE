import json
import unittest
from pathlib import Path

from tools.validate import validate_policy, validate_report

ROOT = Path(__file__).resolve().parents[1]


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.policy = json.loads((ROOT / "policy/v0.2.policy.json").read_text(encoding="utf-8"))

    def test_policy_is_conformant(self):
        self.assertEqual(validate_policy(self.policy), [])

    def test_valid_report_is_accepted(self):
        report = json.loads((ROOT / "conformance/fixtures/valid-report.json").read_text(encoding="utf-8"))
        self.assertEqual(validate_report(report), [])

    def test_failed_check_cannot_be_reported(self):
        report = json.loads((ROOT / "conformance/fixtures/invalid-report.json").read_text(encoding="utf-8"))
        self.assertTrue(validate_report(report))

    def test_terminal_state_has_no_outgoing_transition(self):
        policy = json.loads(json.dumps(self.policy))
        policy["lifecycle"]["transitions"].append({"from": "reported", "to": "requested", "event": "bad"})
        self.assertIn("terminal states cannot have outgoing transitions", validate_policy(policy))


if __name__ == "__main__":
    unittest.main()
