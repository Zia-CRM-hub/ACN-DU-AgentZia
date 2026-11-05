# Communications and Training Plan (DRAFT v0.1)

Owner: Change, Training and Support Lead. Date: 2026-11-05. Status: Draft.
**Nothing in this file has been sent. Every send needs approval (claude.md section 12, customer communications).**
Labels: [Fact], [Assume], [Rec], [Dec].

## 1. Evidence base
- [Fact] Project name, customer, user groups, geography, timeline and go-live are unfilled in claude.md. No stakeholder, adoption or approval data exists.
- [Fact] DELIVERY_PLAN.md (draft) puts the programme in Discovery/Mobilization; no go-live date exists.
- [Assume] Bracketed placeholders are filled before any send. Timing is relative to go-live (T).
- No metrics, progress or approvals are claimed.

## 2. Stakeholder map (roles assumed, names TBC)
| Group | Interest | Influence | Likely concern | Engagement | Owner |
|---|---|---|---|---|---|
| Executive sponsor | Business outcomes | High | Value, cost, risk | Monthly brief, decision asks | Delivery lead |
| Business/process owners | Process fit | High | Workflow disruption | Fortnightly workshop | Change lead |
| End users (groups TBC) | Daily work | Med | Effort to learn, role impact | Demos, training, champions | Change lead |
| Champions | Local help | Med | Workload | Early access, briefings | Change lead |
| Service desk/support | Ticket load | Med | Unprepared for questions | Support training, KB | Support lead |
| IT, Security, Compliance | Control | High | Access, data risk | Review gates | Architect/Security |
| HR/labor representatives [Assume] | Role impact | Unknown | Consultation duties | [Dec] confirm need | Sponsor |
| Delivery team | Execution | Med | Scope change | Stand-ups | Delivery lead |

## 3. Change impact assessment (to complete)
Process changes by group, role impact, tool/access changes and a readiness-survey baseline are all Unknown; they need requirements and a named user population. Survey use needs approval.

## 4. Communications calendar (all draft, none sent)
| # | When | Audience | Channel | Message | Sender | Approver | Status |
|---|---|---|---|---|---|---|---|
| C1 | T-8 wks | Sponsor, process owners | Meeting + note | Vision, scope, roles | Sponsor | Sponsor | Draft |
| C2 | T-6 wks | All affected users | Email/intranet | Why, what, when | Sponsor | Sponsor + Comms | Text below |
| C3 | T-4 wks | Champions | Briefing | Role, early access | Change lead | Delivery lead | Draft |
| C4 | T-3 wks | Users | Email | Training schedule, enrolment | Change lead | Delivery lead | Text below |
| C5 | T-1 wk | Users, support | Email + Teams | Go-live details, help routes | Change lead | Service owner | Text below |
| C6 | T-1 day | Users | Reminder | Cutover window, downtime | Change lead | Service owner | Draft |
| C7 | T | Users | Email/banner | Live, help routes | Service owner | Service owner | Draft |
| C8 | T+1 wk | Users | Pulse survey | Feedback | Change lead | Delivery lead | Draft |
| C9 | T+4 wks | Sponsor | Report | Adoption and issues (actual data only) | Delivery lead | Sponsor | Draft |
| C10 | Ad hoc | Affected users | Email/status | Incident updates | Incident comms | Service owner | Text below |

## 5. Draft message texts (unsent)
**C2 Announcement.** Subject: [PROJECT NAME]: what is changing and when
> Hello [GROUP], from [DATE] we will introduce [PROJECT NAME] to [PURPOSE]. This will [BENEFIT TO THEM]. What it means for you: [CHANGE TO THEIR WORK]. What to do now: [ACTION, IF ANY]. Training will be offered before go-live and support will be available from day one. Questions: [CONTACT]. [SPONSOR NAME]

**C4 Training invitation.** Subject: Book your [PROJECT NAME] training
> Training for [GROUP] runs [DATES]. Choose a session: [LINK]. Each takes about [DURATION]. You will need [PREREQUISITES]. If you cannot attend, a recording and quick guide will be at [LINK]. [CHANGE LEAD]

**C5 Go-live notice.** Subject: [PROJECT NAME] goes live on [DATE]
> From [DATE, TIME] you will use [PROJECT NAME] for [TASKS]. [SYSTEM] will be unavailable from [START] to [END]. For help: quick guides [LINK]; service desk [CONTACT, HOURS]; your champion [NAME]. [SERVICE OWNER]

**C10 Incident update.** Subject: [PROJECT NAME] service issue, update [N]
> We are aware of [IMPACT], started [TIME]. Workaround: [IF ANY]. Next update by [TIME]. [CONTACT]

Rules: no unconfirmed dates, figures or promises; plain language; one clear action per message.

## 6. Training plan ([Assume] groups and roles to be confirmed; no tooling purchase)
| Audience | Content | Format | Duration | Timing | Trainer | Success check |
|---|---|---|---|---|---|---|
| End users | Core tasks, new workflow, help routes | Live demo + hands-on sandbox, recorded | [TBC] | T-3 to T-1 wks | Change lead/champions | Task exercise passed |
| Champions | Deep dive, troubleshooting, feedback loop | Workshop | [TBC] | T-4 wks | Delivery team | Scenario run unassisted |
| Service desk L1 | Triage, known errors, KB, escalation | Workshop + shadowing | [TBC] | T-3 wks | Support lead | Scenario quiz, shadow sign-off |
| L2/L3 support | Runbook, monitoring, deploy, rollback | Handover sessions | [TBC] | T-4 to T-2 wks | Engineering/SRE | Runbook walkthrough accepted |
| Managers | Reporting, coaching, adoption KPIs | Briefing | [TBC] | T-2 wks | Change lead | Attendance |
| Admins | Config, access, user management | Technical session | [TBC] | T-3 wks | Engineering | Tasks done in non-prod |

Materials (produce once solution is defined): role-based quick guides, FAQ, short videos, sandbox with synthetic data (no confidential data), attendance tracker, KB articles.
Dependencies: stable training environment, user access, finalized workflow from build and test.

## 7. Adoption measures (definitions only, no data yet)
Training completion %, assessment pass rate, active use vs target population, task completion via new process, tickets per 100 users, pulse/CSAT score, champion coverage. Targets [Dec]; actuals none.

## 8. Risks
| Risk | Rating | Mitigation |
|---|---|---|
| Unclear scope delays content | High | Content freeze window, update guides per release |
| Low attendance | Med | Manager nudges, flexible sessions, recordings |
| Messages sent before approval or decisions | High | Approval gate; nothing sent from this plan |
| Consultation duties missed | Med | Confirm with HR/Legal early |
| Champions overloaded | Med | Time allowance agreed with managers |

## 9. Decisions and approvals required
| Item | Approver |
|---|---|
| Fill project fields: customer, user groups, geography, go-live | Sponsor, Delivery lead |
| Approve sender identity and each outbound communication | Sponsor, Service owner |
| Approve training effort and user time off-task | Sponsor |
| Approve any survey/data collection (privacy review) | Security/Privacy |
| Confirm HR/labor consultation need | HR |

Send-approval template: action (send C#), reason, benefit, cost (usually nil), risk (wrong or early info), rollback (correction follow-up; cannot unsend), validation (proofread and fact-check against plan), approver.

## 10. Next actions
1. Obtain project fields and user groups. 2. Confirm stakeholder names. 3. Get support model approved (SUPPORT_MODEL.md in docs/operations). 4. Draft role-based materials once workflow is defined. 5. Agree training environment with engineering.
