# Delivery plan, ownership and release gates

## Sequencing (indicative, dependent on vendor provisioning and legal review)
| Phase | Time | Work | Exit |
|---|---|---|---|
| 0 Discovery | weeks 1-2 | customer journeys, counsel signoff, data processing impact, vendor license checks, telephony sandbox | approved requirements/threat model |
| 1 Foundation | weeks 3-5 | tenant/RBAC, CI, DB, consent policies, suppression, audit, demo UI | integration/unit tests, security scan |
| 2 Voice beta | weeks 6-9 | SIP, live agent, STT/LLM/TTS adapters, recording notices, handoff, call outcomes | supervised test calls with opted-in testers |
| 3 Pilot | weeks 10-12 | campaign approvals, scheduling, analytics, CRM webhooks, quotas, operations runbooks | incident drill and legal signoff |
| 4 GA hardening | weeks 13-16+ | load test, DR, accessibility, privacy deletion, SOC2 readiness, failover | executive go/no-go |

## Proposed team
1 tech lead/architect, 2 backend engineers, 1 real-time voice engineer, 1 frontend engineer, shared DevOps/SRE, QA automation, fractional product, design, security and counsel. Staffing can be reduced by shipping appointment reminders first.

## Production estimates (planning assumptions, not quotes)
Early build labor: roughly 12-20 engineer-months plus QA/product/legal. Ongoing variable spend includes PSTN per minute, media platform, STT, LLM tokens, TTS, recordings, storage, compute and support. Model unit economics as `cost_per_completed_call = pstn_minutes_rate + stt_seconds_rate + tts_chars_rate + llm_tokens_rate + infra_allocation + retry_overhead`. Obtain dated provider quotes and test real calls before publishing price.

## CI and release rules
- lint, type checks, unit tests, contract tests, integration tests in sandbox
- secret scanning, dependency/SBOM and license scanning
- container image scanning and infrastructure policy checks
- automated call-policy tests for revoked consent, quiet hours, DNC, timezone ambiguity, retries and tenant leakage
- manually supervised production canary; automatic circuit-breaker on error/cost/complaints
- regional deployments, tested restore, encrypted backups and bounded retention

## Risks / mitigations
- TCPA, state, international and industry rules -> counsel-reviewed policy engine + kill switch
- ASR/TTS errors and hallucination -> scoped actions, explicit confirmation, escalation, eval set
- Voice latency -> streaming, VAD tuning, region locality, provider fallback, load testing
- Fraud/abuse -> verified tenants, rate/budget caps, abnormal-volume detection
- Privacy -> data minimization, encryption, access audit, vendor DPAs, retention automation
- Vendor lock-in -> adapters, contract tests and exportable event schema

## Gate for production use
Do not launch without written legal review, provider contracts, consent evidence, tenant isolation tests, abuse controls, incident response drills, accessibility verification, evaluation metrics and call recording notice rules.
