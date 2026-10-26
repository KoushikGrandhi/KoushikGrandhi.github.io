"""Local-only demonstration. No telephony integration and no durable storage."""
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
from .policy import Contact, can_schedule

HOST = "127.0.0.1"
PORT = 8080
CONTACTS = [
    Contact("ct_001", "Sample Customer A", "+12145550101", "America/Chicago", True),
    Contact("ct_002", "Sample Customer B", "+12145550102", "America/Chicago", False),
    Contact("ct_003", "Sample Customer C", "+12145550103", "America/New_York", True, True),
]
AUDIT = []
APPROVED = False

def snapshot():
    now = datetime.now(timezone.utc)
    return {
        "project": "AI over voice",
        "mode": "local simulation only — outbound calling disabled",
        "approved": APPROVED,
        "contacts": [
            {"id": c.id, "name": c.name, "phone": c.phone[-4:].rjust(len(c.phone), "*"),
             "consent": c.consent, "suppressed": c.suppressed,
             "decision": can_schedule(c, now, APPROVED).__dict__}
            for c in CONTACTS
        ],
        "audit": AUDIT[-25:],
    }

class Handler(BaseHTTPRequestHandler):
    def _respond(self, status, data):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/state":
            self._respond(200, snapshot())
        elif self.path in ("/", "/index.html"):
            body = (Path(__file__).parent / "static" / "index.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self._respond(404, {"error": "not_found"})

    def do_POST(self):
        # Deliberately exposes no dialing/approval actions; safe demo is read-only.
        self._respond(405, {"error": "read_only_demo"})

def main():
    print(f"AI over voice demo: http://{HOST}:{PORT} (no calls placed)")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()

if __name__ == "__main__":
    main()
