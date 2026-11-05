# Support Model (DRAFT v0.1)

Owner: Change, Training and Support Lead. Date: 2026-11-05. Status: Draft, not approved.
Labels: [Fact] confirmed, [Calc] calculated, [Assume] assumption, [Rec] recommendation, [Dec] decision required.

## 1. Evidence base
- [Fact] claude.md section 1 project fields (customer, users, geography, timeline, budget, commercial model, cloud, phase) are unfilled placeholders.
- [Fact] DELIVERY_PLAN.md (draft) assumes phase is Discovery/Mobilization, nothing built, nothing deployed, no go-live date.
- [Fact] No SLA, runbook, incident, ticket or usage data exists. No metrics are claimed here.
- Consequence: all targets below are placeholders for approval, not commitments.

## 2. Assumptions (reversible)
| ID | Assumption | Impact if wrong |
|---|---|---|
| S1 | Solution goes live in one or more waves, then hypercare, then BAU support | Tier and coverage change |
| S2 | Customer has an existing service desk/ITSM tool usable for L1 | Tool purchase (needs approval) |
| S3 | BAU is business hours in one time zone; extended in hypercare | Cost and staffing change |
| S4 | Commercial model unknown; support priced separately from build | SLA enforceability |
| S5 | Engineering and SRE roles from this unit provide L3 | Handover gaps |

## 3. Support tiers
| Tier | Scope | Owner | Escalate when |
|---|---|---|---|
| L0 Self-service | Quick guides, FAQ, in-product help | Change/Training | User cannot resolve, raises ticket |
| L1 Service desk | Log, categorize, how-to, access, known-error fixes | Customer service desk [S2] | Unresolved after 15 min or unknown issue |
| L2 Application support | Functional diagnosis, config, data fixes, workarounds | Application support (named owner [Dec]) | Defect or infrastructure cause |
| L3 Engineering/SRE | Code defects, infra, performance, security | Delivery engineering, SRE | Vendor or cloud provider case |
| Champions | Local first help, feedback, UAT support | Business-nominated | Raise to L1 |

## 4. Severity and response targets (placeholder, [Dec] approval needed)
| Sev | Definition | Response | Updates | Resolution |
|---|---|---|---|---|
| 1 | Service down, or data/security breach, no workaround | 15 min | 30 min | 4 h |
| 2 | Major function degraded, workaround exists | 1 h | 2 h | 1 business day |
| 3 | Minor issue | 4 business h | Daily | 5 business days |
| 4 | Question, request, cosmetic | 1 business day | On change | Backlog |
[Rec] Tighten Sev 1-2 during hypercare. Targets are not SLAs until contractually agreed.

## 5. Coverage
- [Assume] Hypercare 4 weeks per go-live wave: extended hours, daily triage stand-up, named on-call L3.
- [Assume] BAU: business hours; Sev 1 on-call rota.
- [Dec] Hours, time zones, languages (geography unknown).

## 6. Processes
1. Incident: log, classify, resolve or escalate, communicate, confirm with user, close. Sev 1-2 get a blameless review within 5 business days.
2. Problem: 3 or more incidents with the same cause raise a problem record and known-error entry.
3. Requests and changes: standard catalogue; production changes follow claude.md section 12 approvals.
4. Knowledge: every resolved Sev 2+ ticket creates or updates a knowledge article.
5. Major incident: incident commander, scribe, comms owner. Stakeholder updates are drafted by the Change lead and sent only after approval.
6. AI-agent aspects [Assume]: if AI agents handle any triage, they act in draft/recommend mode, humans own closure, and agent actions are logged (see SECURITY_ARCHITECTURE.md).

## 7. RACI (R responsible, A accountable, C consulted, I informed)
| Activity | L1 | L2 | L3/SRE | Change lead | Service owner |
|---|---|---|---|---|---|
| Ticket triage | R | C | I | I | A |
| Functional fix | I | R | C | I | A |
| Defect/infra fix | I | C | R | I | A |
| User communications | I | C | C | R | A |
| Training and KB | C | C | C | R | A |
| Handover acceptance | C | R | R | R | A |
Named individuals: [Dec] none assigned.

## 8. Hypercare exit criteria ([Rec], thresholds TBC)
- No open Sev 1; no open Sev 2 without an agreed plan.
- Ticket volume trending down for an agreed number of weeks.
- L1/L2 resolve at agreed rate without L3 help.
- Runbooks, KB and alerts reviewed and accepted by support.
- Training completion at agreed threshold; support signs handover acceptance.

## 9. Operational readiness checklist
All items Not started; no evidence exists yet.
| # | Item | Owner | Status | Evidence |
|---|---|---|---|---|
| 1 | Tiers, hours, severity targets approved | Service owner | Not started | None |
| 2 | ITSM queues, categories, routing configured | Service desk | Not started | None |
| 3 | Named L1/L2/L3 staff and on-call rota | Support manager | Not started | None |
| 4 | Runbook and known-error list handed over | Engineering/SRE | Not started | None |
| 5 | Monitoring and alert routing to support | SRE | Not started | None |
| 6 | KB and quick guides published | Change lead | Not started | None |
| 7 | Support staff trained, shadowing done | Change lead | Not started | None |
| 8 | Champions nominated and trained | Business | Not started | None |
| 9 | Escalation and vendor contacts verified | Support manager | Not started | None |
| 10 | Support staff access approved | Security | Not started | None |
| 11 | Rollback and comms rehearsed | Delivery lead | Not started | None |
| 12 | Go/no-go readiness sign-off | Service owner | Not started | None |

## 10. Support KPIs (definitions only, no baselines)
First response time, resolution vs target, first-contact resolution, reopen rate, tickets per 100 users, escalation rate, CSAT, KB usage, repeat-incident rate. [Dec] Baselines measured in hypercare; report no values until data exists.

## 11. Risks
| Risk | Rating | Mitigation |
|---|---|---|
| Support owner and funding undefined | High | Decide before any go-live |
| Service desk untrained at launch | High | Training plan and readiness gate |
| Expectations exceed agreed scope | Med | Targets non-binding until contract |
| Knowledge base stale after releases | Med | KB update in release checklist |

## 12. Approval request (prepared, not submitted)
- Action: approve support tiers, severity targets, hypercare length, and named support owner.
- Reason: no support model is agreed, so readiness cannot be assessed.
- Benefit: clear accountability, predictable response, smoother adoption.
- Cost: [Dec] unknown; depends on staffing and ITSM tooling (purchases need separate approval).
- Risk: targets too tight or loose; review after hypercare.
- Rollback: revert to draft values.
- Validation: Sev 1 tabletop exercise and readiness checklist review.
- Approver: customer service owner and delivery lead (names TBC).
