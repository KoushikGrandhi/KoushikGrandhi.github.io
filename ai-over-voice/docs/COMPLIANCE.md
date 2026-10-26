# Legal, compliance and intellectual-property safeguards

This is an engineering checklist, **not legal advice**. Counsel must validate the user journey, location of caller/recipient, call purpose, consent mechanism, AI disclosure, recording and retention before real dialing.

1. Artificial/prerecorded voice restrictions: the US FCC has stated AI-generated voices fall under TCPA artificial/prerecorded voice rules; consent requirements depend on call type and context. https://www.fcc.gov/document/fcc-makes-ai-generated-voices-robocalls-illegal
2. Telemarketing rules: apply national/state Do Not Call, company-specific DNC, permitted hours, identification, opt-outs, applicable recordkeeping, and changing FTC/FCC requirements. https://www.ftc.gov/business-guidance/resources/complying-telemarketing-sales-rule
3. Capture verifiable, purpose-specific consent provenance; never presume a purchased contact list provides permission.
4. Re-evaluate policy at dial time. Revocation, suppression and emergency stop trump prior campaign approval.
5. Track jurisdictions (including two-party recording consent states) before enabling recording, and play notices or require consent as determined by counsel.
6. Store only needed contact/call data; provide retention, export and deletion processes; encrypt all media.
7. Never copy third-party logos, site copy, layouts, source, nonpublic screenshots, cloned voices, customer data, music, audio samples or proprietary prompts.
8. Use original product copy, names, icons and demo data; review trademark clearance for 'AI over voice' before commercial launch.
9. Verify upstream open-source licenses, preserve attribution where applicable, scan transitive dependencies and avoid unlicensed assets.
10. This prototype includes NO call automation or third-party provider SDK, protecting against accidental dialing and vendor IP contamination.

Policy engine must default to DENY on missing facts. Test representative jurisdiction-specific requirements with counsel and automated regression tests.
