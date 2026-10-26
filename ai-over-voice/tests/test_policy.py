import unittest
from datetime import datetime, timezone
from app.policy import Contact, can_schedule

DAY = datetime(2026, 10, 26, 16, 0, tzinfo=timezone.utc)  # Monday 11am Chicago
def contact(**overrides):
    values = dict(id="ct1", name="Test", phone="+12145550123", timezone="America/Chicago", consent=True)
    values.update(overrides)
    return Contact(**values)

class PolicyTests(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(can_schedule(contact(), DAY, True).allowed)
    def test_no_consent(self):
        self.assertIn("consent_missing_or_revoked", can_schedule(contact(consent=False), DAY, True).reasons)
    def test_suppression(self):
        self.assertIn("contact_suppressed", can_schedule(contact(suppressed=True), DAY, True).reasons)
    def test_approval(self):
        self.assertIn("campaign_not_approved", can_schedule(contact(), DAY, False).reasons)
    def test_invalid_phone(self):
        self.assertFalse(can_schedule(contact(phone="123"), DAY, True).allowed)
    def test_unknown_zone(self):
        self.assertIn("timezone_unknown", can_schedule(contact(timezone="Nowhere/City"), DAY, True).reasons)
    def test_weekend(self):
        sat = datetime(2026, 10, 24, 16, 0, tzinfo=timezone.utc)
        self.assertIn("demo_quiet_hours", can_schedule(contact(), sat, True).reasons)
    def test_unknown_purpose(self):
        self.assertFalse(can_schedule(contact(), DAY, True, "marketing").allowed)

if __name__ == "__main__":
    unittest.main()
