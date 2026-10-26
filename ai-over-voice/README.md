# AI over voice

Original, compliance-first voice AI platform blueprint and local campaign operations prototype.

> **Scope:** This is an independent clean-room project. It is NOT OffHook software, not affiliated with OffHook, and does not include its brand assets, design, code, prompts, recordings, or proprietary documentation. The prototype **does not place calls**. Production integrations need separate credentials, licensed components, security review and legal approval.

## Try the prototype

Requires Python 3.11+ (stdlib only).

```bash
cd ai-over-voice
python3 -m unittest discover -s tests -v
python3 -m app.server
```

Open http://127.0.0.1:8080 for a locally hosted original dashboard. API endpoint GET /api/state. API stores data in process memory only and resets on restart. The dashboard is a non-production demonstrator.

## Included
- `docs/PRODUCT.md` — public-product analysis, differentiation, requirements and success metrics
- `docs/ARCHITECTURE.md` — target production architecture, stack choices, data model, call state machine and interfaces
- `docs/DELIVERY.md` — staffing, roadmap, release criteria, budget envelope and threat model
- `docs/COMPLIANCE.md` — consent, safety, privacy, telephony and IP checklist
- `app/server.py` — runnable dashboard/API mock with consent/suppression gate and audit trail
- `tests/test_policy.py` — policy tests
- `LICENSE` — original project code licensed under MIT

## How this relates to the reference
The reference website offhook.ai was analyzed only as public market research. Similar high-level functions (campaigns, agents, records and analytics) are generic product concepts and are implemented here from an original specification.

## Repository publication
Prepared inside a dedicated `ai-over-voice` branch of the owner's existing GitHub Pages repository because this connector cannot create a new repository. The owner's existing `main` website branch is untouched. To move this to a standalone repo later, copy the `ai-over-voice/` folder into a repository named `ai-over-voice`.

## Deployment status
**Not a production telephony system.** No dialer, SIP/WebRTC runtime, real transcription, identity service, billing processor or integration credentials are included. Do not use to initiate outbound calls.
