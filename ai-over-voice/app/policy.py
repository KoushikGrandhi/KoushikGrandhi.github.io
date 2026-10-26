"""Conservative demo outbound consent policy. Not jurisdiction-complete."""
from dataclasses import dataclass
from datetime import datetime, time
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

@dataclass(frozen=True)
class Contact:
    id: str
    name: str
    phone: str
    timezone: str
    consent: bool
    suppressed: bool = False

@dataclass(frozen=True)
class Decision:
    allowed: bool
    reasons: tuple[str, ...]

def can_schedule(contact: Contact, now: datetime, approved: bool, purpose: str = "appointment") -> Decision:
    reasons = []
    if not approved:
        reasons.append("campaign_not_approved")
    if not contact.consent:
        reasons.append("consent_missing_or_revoked")
    if contact.suppressed:
        reasons.append("contact_suppressed")
    if not contact.phone.startswith("+") or not contact.phone[1:].isdigit() or not (8 <= len(contact.phone[1:]) <= 15):
        reasons.append("invalid_e164_phone")
    if purpose not in ("appointment", "service"):
        reasons.append("purpose_not_allowed_in_demo")
    try:
        local = now.astimezone(ZoneInfo(contact.timezone))
        # The demo is intentionally more restrictive than many default calling-hour rules.
        if not (time(9, 0) <= local.time() < time(17, 0)) or local.weekday() >= 5:
            reasons.append("demo_quiet_hours")
    except (ZoneInfoNotFoundError, ValueError, TypeError):
        reasons.append("timezone_unknown")
    return Decision(not reasons, tuple(reasons))
