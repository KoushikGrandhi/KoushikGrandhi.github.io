# Target architecture and stack (technical director decision record)

## Architecture
```text
Next.js 15+ console -> API Gateway/Auth -> Control Plane (FastAPI)
                                        |-- Tenant/RBAC & Audit
                                        |-- Agent/Prompt Versions
                                        |-- Consent/Policy Engine
                                        |-- Campaign Scheduler -> Temporal workflow queue
                                        |-- Call Metadata / Outcome Service
                                        |-- Webhooks & CRM Connector
                                        |
                                        +-> PostgreSQL + pgvector
                                        +-> Redis (rate limiter/cache)
                                        +-> Object Storage (encrypted media)
                                        +-> OpenTelemetry collector
Telecom/SIP provider -> Voice Session Gateway (LiveKit Agents)
                    -> STT -> conversation orchestration/LLM -> TTS
                    -> tool permission gateway -> scoped business services
                    -> event stream -> transcript/outcome aggregator
```

## Recommended stack
| Layer | Decision | Reason |
| --- | --- | --- |
| UI | TypeScript, Next.js, Tailwind, shadcn/ui (license verification at install) | typed console and rapid original UI |
| API | Python 3.12+, FastAPI + Pydantic | clear contracts and Python AI ecosystem |
| Realtime media | LiveKit Agents with SIP ingress / egress; alternate provider behind adapter | handles low-latency streaming primitives |
| Telephony | licensed Twilio Voice/SIP or compliant local carrier | phone numbers, PSTN origination, routing |
| AI | model-provider adapter, streaming STT and TTS | portability, budget and reliability controls |
| Workflow | Temporal | durable scheduling and call retries |
| Data | PostgreSQL (row-level isolation), pgvector only when retrieval is justified | transactional correctness |
| Cache / controls | Redis | quota and rate limiting |
| Object storage | S3-compatible storage + envelope encryption | recordings, retention |
| Identity | OIDC/SAML via managed identity provider | MFA and enterprise SSO |
| Infrastructure | Docker, managed Kubernetes/ECS, Terraform, GitHub Actions | reproducible delivery |
| Telemetry | OpenTelemetry + Prometheus/Grafana + error monitoring | SLO and per-call tracing |

Check the current licenses and API terms of every optional package/provider before inclusion. Do not commit vendor code or media.

## Core entities
tenants(id, name, region, retention_policy)
members(tenant_id, user_id, role)
contacts(id, tenant_id, phone_e164, timezone, preferred_language)
consents(id, contact_id, purpose, channel, obtained_at, expires_at, revoked_at, proof_ref, source)
suppression(id, tenant_id, phone_hash, reason, created_at)
agents(id, tenant_id, name, active_version_id)
agent_versions(id, agent_id, instructions, tool_allowlist, reviewed_by, published_at)
campaigns(id, tenant_id, purpose, status, approved_by, schedule, max_concurrency)
campaign_contacts(id, campaign_id, contact_id, state, attempts)
calls(id, tenant_id, campaign_id, contact_id, provider_call_id, status, policy_decision_id)
call_events(id, call_id, event_type, occurred_at, payload_json)
recordings(id, call_id, encrypted_object_ref, retention_until, notice_status)
outcomes(id, call_id, category, rationale, evidence_event_ids)
audit_events(id, actor_id, tenant_id, action, timestamp, immutable_payload_hash)
policy_decisions(id, contact_id, purpose, allowed, reasons, evaluated_at, policy_version)

Use tenant isolation at query layer AND Postgres row-level security, least-privilege credentials, and separate service principals.

## Required API contracts
POST /v1/consents
POST /v1/contacts:import (preflight validation)
POST /v1/campaigns (draft only)
POST /v1/campaigns/{id}:approve
POST /v1/campaigns/{id}:launch (idempotency key)
POST /v1/campaigns/{id}:stop
GET /v1/calls/{id}
GET /v1/calls/{id}/timeline
POST /v1/calls/{id}:handoff
POST /v1/webhooks/{provider} (verified signatures + replay protection)
POST /v1/privacy/requests
GET /v1/audit?resource_id=...

Generate OpenAPI and scoped SDK clients. Document error codes, retry semantics and pagination.

## Outbound state machine
DRAFT -> APPROVED -> QUEUED -> PREFLIGHT -> DIALING -> RINGING -> ACTIVE -> COMPLETED
                                      |-> BLOCKED
Other terminal states: NO_ANSWER, BUSY, FAILED, OPTED_OUT, CANCELLED.
Every transition must be idempotent and auditable. Before each dial, re-evaluate consent, local time, suppression, campaign approval, provider capacity and expense budget. Stop and suppress on opt-out; never retry opted-out calls.

## Safety-critical orchestration
- All agent tools execute through an allowlisted, permission-scoped gateway; no arbitrary URLs or shell execution.
- Prompt injection from caller speech/transcripts is untrusted; never override system policies.
- Provider webhooks require cryptographic signature verification and replay windows.
- Disclose AI and recording where legally required; route to human on request.
- Avoid storing raw card numbers, credentials or sensitive personal information in transcripts.
- Fail closed when consent or geography cannot be established.
- Outbound only for lawful consented uses; jurisdiction-specific legal validation required.
