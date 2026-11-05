# Outcome Map

Owner: Enterprise Architect | Status: Draft v0.1 | Date: 2026-11-05

Labels used: **[Confirmed]** fact from repository, **[Assumption]**, **[Calculated]**, **[Forecast]**, **[Recommendation]**, **[Decision required]**.

## 1. Evidence base

- [Confirmed] The repository `AgentZ` contains only `claude.md` (delivery charter), `.claude/agents/*.md` (12 role definitions) and `docs/delivery/ROSTER.md` (empty table). There is no source code, infrastructure, pipeline or test asset.
- [Confirmed] Every project field in `claude.md` section 1 (name, customer, industry, problem, users, geography, outcomes, timeline, budget, commercial model, cloud, constraints, phase) is an unfilled placeholder.
- [Confirmed] No baseline measurements, benefit data or approvals exist. All values below are targets or placeholders, not results.

## 2. Assumptions (A-xx)

| ID | Assumption | Impact if wrong | Validate with |
|---|---|---|---|
| A-01 | The program is an enterprise digital delivery engagement run by an all-AI delivery unit with human approvers. | Operating model and governance change. | Sponsor |
| A-02 | Current phase is Discovery / Mobilization. | Roadmap timing shifts. | Delivery Lead |
| A-03 | Commercial model is unknown; benefits are tracked for both owner and provider views. | Margin and KPI set change. | Finance |
| A-04 | Preferred cloud is Azure, with Microsoft stack default (claude.md section 3). Multi-cloud is out unless justified. | Cloud ADRs change. | Customer architect |
| A-05 | Users are business users, delivery staff and operations/support staff. Geography is unspecified, so privacy is treated at the strictest plausible level (GDPR-class). | Compliance scope. | Security Architect |
| A-06 | No production system or customer data is in scope until approved. | Approval gates. | Sponsor |

## 3. Outcome hierarchy

Rule: every capability and deliverable must trace to at least one outcome. Targets are placeholders until baselines exist.

| ID | Outcome | Perspective | KPI | Baseline | Target | Data source | Benefit class (claude.md s.8) | Owner |
|---|---|---|---|---|---|---|---|---|
| O1 | Faster time to market | Owner | Lead time, idea to production | Not measured | [Decision required] | Delivery tooling | Estimated opportunity | Product Owner |
| O2 | Lower delivery cost | Owner, provider | Effort per delivered work item | Not measured | [Decision required] | Timesheets, ROSTER | Estimated opportunity | Finance |
| O3 | Higher delivery quality | Both | Defect escape rate; test pass rate | Not measured | [Decision required] | QA reports | Estimated opportunity | QA lead |
| O4 | Risk reduction (security, compliance, AI) | Both | Open Sev1/Sev2 findings; audit gaps | Not measured | 0 open Sev1 at release | Security reviews | Qualitative until measured | Security Architect |
| O5 | Reliability | Owner | SLO attainment; MTTR | Not measured | Set in NFRs | Monitoring | Estimated opportunity | SRE |
| O6 | Adoption and satisfaction | Owner | Active usage; CSAT; task completion | Not measured | [Decision required] | Analytics, surveys | Qualitative until measured | Product Owner |
| O7 | Provider profitability | Provider | Gross margin % | Not measured | [Decision required] | Financial tracker | Estimated opportunity | Finance |

Formulas (claude.md s.8): gross margin % = (Revenue - Delivery cost) / Revenue x 100; efficiency % = (Baseline effort - New effort) / Baseline effort x 100; ROI % = (Realized benefit - Investment) / Investment x 100. Savings must not be double counted across automation, productivity and cycle-time.

## 4. Business capability map

Maturity is [Assumption] "None" for all, since nothing is built yet. Priority uses claude.md s.16 dimensions qualitatively until scored.

| Capability group | Capability | Supports outcome | Primary role(s) | Initial priority |
|---|---|---|---|---|
| Strategy and governance | Outcome and benefits management | O1-O7 | Enterprise Architect, PMO | High |
| | Architecture and decision governance | O3, O4 | Enterprise Architect | High |
| | Program delivery and PMO control (RAID, plan, status) | O1, O7 | Delivery Lead, PMO | High |
| | Finance and workforce planning | O2, O7 | Finance and Workforce | Medium |
| Product delivery | Requirements and backlog | O1, O6 | Business Analyst / Product Owner | High |
| | Solution design | O1, O3 | Solution Architect | High |
| | Full-stack engineering | O1, O3 | Fullstack Engineer | High |
| | Data and AI engineering (incl. responsible AI) | O3, O4 | Data/AI Engineer | Medium |
| | Test automation and quality assurance | O3 | QA Automation | High |
| Platform and operations | Cloud, DevSecOps pipelines, IaC | O1, O5 | Cloud/DevOps/SRE | High |
| | Security and privacy engineering | O4 | Security Architect | High |
| | Observability, support, runbooks | O5, O6 | SRE, Change/Support | Medium |
| Adoption | Change management, training, user experience | O6 | Change Support Lead | Medium |

## 5. Traceability skeleton

Requirement -> capability -> design -> code -> test -> outcome. Rows are populated by the owning roles; none exist yet.

| Req ID | Capability | Design artifact | Code | Test | Outcome |
|---|---|---|---|---|---|
| (none yet) | | | | | |

## 6. Architecture states

- Current state [Confirmed]: no application or infrastructure. Only governance documents and agent role definitions.
- Transition state [Recommendation]: (1) governance baseline and docs; (2) walking skeleton with CI, IaC and observability in a non-production environment; (3) incremental capability releases behind feature flags.
- Target state [Assumption]: API-first, Azure-hosted, managed-identity, IaC-provisioned, observable, with human approval gates for consequential and AI actions. Detail is deferred to `SOLUTION_ARCHITECTURE.md`, which depends on the project fields being filled.

## 7. Open information needed (material only)

1. [Decision required] Project name, customer, business problem and the 3-5 outcomes with numeric targets (owner: Sponsor).
2. [Decision required] Approved budget, timeline and commercial model (owner: Sponsor, Finance).
3. [Decision required] Preferred cloud and compliance regime (owner: Customer architect, Security).
4. [Decision required] Existing systems and integration constraints.

Until answered, work stays limited to documents and reversible, non-production design.

## 8. Approvals

No approval is requested by this document. Any later production deployment, spend, external communication or contract change requires the approval request format in claude.md s.12.
