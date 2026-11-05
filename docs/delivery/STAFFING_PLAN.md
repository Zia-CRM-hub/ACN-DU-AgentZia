# Staffing Plan: AI Agent Team and Human Oversight

Owner: Finance and Workforce Planner. Status: DRAFT. Labels: Fact / Assump / Rec / Decision.

## 1. Team model
[Fact] The delivery unit is 12 AI agent roles defined in `.claude/agents/` (11 delivery roles plus this planner). [Assump] No dedicated human delivery staff are assigned; humans act as sponsor, approvers and reviewers. Human headcount and names: [TO BE CONFIRMED].

## 2. AI agent roles
| Agent | Responsibility | Primary artifacts | claude.md s7 roles covered |
|---|---|---|---|
| delivery-lead | Program Director; orchestrates team, plan, roadmap, RAG, exec status | DELIVERY_PLAN, EXECUTIVE_STATUS | Program/Project Manager |
| pmo-analyst | RAID, decisions, changes, governance, roster, status drafts | RAID_LOG, DECISION_LOG, CHANGE_LOG, ROSTER | PMO Analyst |
| enterprise-architect | Capability map, target state, ADRs | ARCHITECTURE_DECISIONS | Enterprise Architect |
| solution-architect | Solution, integration, NFRs | SOLUTION/INTEGRATION_ARCHITECTURE, NFR | Solution, Technical Architect |
| cloud-devops-sre | IaC, CI/CD, observability, DR, FinOps | CLOUD_ARCHITECTURE, RUNBOOK, FINOPS_PLAN | Cloud Architect, DevOps, SRE |
| security-architect | Threat model, Zero Trust, responsible AI | SECURITY_ARCHITECTURE | Security Architect |
| data-ai-engineer | Data architecture, AI design | DATA_ARCHITECTURE | Data Architect, Data/AI Engineer |
| fullstack-engineer | Implementation with tests | Code, change reports | Frontend, Backend Engineer |
| qa-automation | Test strategy and automation | TEST_STRATEGY | QA, Automation Engineer |
| business-analyst-product-owner | Requirements, backlog, KPIs, UX | REQUIREMENTS, KPI_DICTIONARY | BA, Product Owner, UX |
| change-support-lead | Comms drafts, training, support model | SUPPORT_MODEL | Change Manager, Trainer, Support Lead |
| finance-workforce | Cost model, benefits, staffing, capacity | COST_MODEL, BENEFITS_REALIZATION, STAFFING_PLAN | Workforce planner, Financial manager |

## 3. Coverage gaps and single points of failure
- [Fact] No agent for Dynamics 365 or Power Platform engineering. [Assump] Needed only if [MICROSOFT TECHNOLOGIES] includes them; fullstack-engineer is the fallback.
- Each role is a single agent, so each artifact area is a single point of failure. [Rec] Peer review by another agent plus human sign-off for key artifacts.
- Agents carry no continuity between sessions beyond repository files. [Rec] Keep ROSTER.md and docs current as the knowledge-transfer mechanism.

## 4. Where human oversight sits (claude.md s12)
| Decision point | Human role | Agent role |
|---|---|---|
| Production deployment, DB migration, resource deletion | Release/Change approver [NAME] | cloud-devops-sre prepares plan and rollback |
| Identity, access, network security changes | Security approver [NAME] | security-architect recommends |
| Cloud/licence purchase, spend above threshold | Budget owner [NAME] | finance-workforce prepares approval request |
| Customer communications, external financial figures | Sponsor/Account lead [NAME] | change-support-lead, finance-workforce draft only |
| Contract scope changes | Commercial owner [NAME] | pmo-analyst logs change request |
| Hiring, termination, replacement | HR/Delivery owner [NAME] | Recommendation only |
| Risk acceptance, confidential data access | Business owner [NAME] | Escalate only |
| Benefit sign-off | Benefit owners / approver [NAME] | finance-workforce calculates |
| Acceptance of AI outputs (code, tests, security) | Named reviewer per area [NAME] | Agents propose; humans accept |

Approval request fields: action, reason, benefit, cost, risk, rollback, validation, approver.

## 5. 12-week capacity plan (rolling)
| Week | Phase | Active agent roles | Human oversight hours | Constraint |
|---|---|---|---|---|
| 1-12 | [PHASE per week] | [ROLES] | [HOURS] | [X] |

[Assump] Agent capacity is bounded by session/token budget ([LIMIT]) and human review throughput, not working hours. No utilization data exists, so none is reported.

## 6. Milestone staffing forecast
| Milestone | Date | Roles needed | Human approvers needed |
|---|---|---|---|
| [MILESTONE] | [DATE] | [ROLES] | [NAMES] |

## 7. Decisions required
- Name human approvers/reviewers and review turnaround targets.
- Confirm whether human engineers are added (compare permanent, contractor, partner, managed service) once scope is known.
- Confirm AI usage budget limits (see docs/financials/COST_MODEL.md).
