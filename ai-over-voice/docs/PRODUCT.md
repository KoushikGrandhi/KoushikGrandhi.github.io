# Product strategy and external reference evaluation

Research date: 2026-10-26. Public pages only, no authenticated trial, internal APIs, source code or benchmark access.

## Reference assessment
Publicly presented OffHook capabilities include AI phone agents, outbound campaigning, call administration, transcripts/recordings and agent setup. These are category-level observations, not reverse engineering. Claims about exact latency, implementation, reliability and conversion performance cannot be verified from public materials. Source: https://www.offhook.ai/

## Independent product thesis
**AI over voice** is a control plane for permission-based automated conversations, with full visibility into who may be contacted, why, and what happened. Target customers: appointment-heavy SMBs and B2B customer success teams with existing lawful customer relationships.

## Personas
- Operations manager: campaigns, schedules, contacts, opt-outs, results
- Agent designer: versioned conversation playbooks, tool permissions and escalation thresholds
- Compliance officer: consent provenance, suppression rules, retention and export
- Support supervisor: live monitoring and human handoff
- Administrator: tenant settings, access controls and spend limits

## MVP capabilities
1. Organization and RBAC boundary; SSO-ready tenant data model
2. Consent records with source, scope, timestamp and revocation
3. Contact import with field validation and DNC suppression
4. AI agent instructions/playbook versioning and simulations
5. Campaign approval, scheduling, per-tenant rate caps, time-zone controls
6. Call lifecycle, outcome tagging, callback tasks and human transfer
7. Transcript, recording controls, searchable metadata and deletion
8. Webhook and CRM outbound events, idempotent retries and observability

### Deliberately excluded from MVP
Voice cloning; scraped lead acquisition; unsolicited marketing dialer; unrestricted autonomous tool execution; covert or unconsented recordings; bulk overseas dialing; unverified number spoofing.

## Success criteria (targets, not measured claims)
- >= 99.9% campaign job execution availability after production hardening
- < 2 s median agent response latency measured end-to-end (stretch objective; benchmark by provider and region)
- 100% outbound calls blocked without an auditable valid consent/policy decision
- 0 secrets in the repository or logs
- >= 95% of calls have a normalized outcome
- Hard spending and concurrency limits enforced server-side

## Reference-to-product separation
Generic concepts: voice agent, call queue, playbooks, outcome analytics.
Original inventions: policy-decision receipts, preflight approval workflow, evidence-linked outcomes, provider abstraction, safe-mode simulator and incident stop switch.
Never copy website visual layouts, feature copy, prompts, logos, screenshots, customer quotes or hidden integrations.
