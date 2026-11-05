# Cost Model (initial)

Owner: Finance and Workforce Planner. Status: DRAFT, template with placeholders. No figures have been supplied or approved.

Labels: **[Fact]** Confirmed fact, **[Calc]** Calculated, **[Fcst]** Forecast, **[Assump]** Assumption, **[Rec]** Recommendation, **[Decision]** Decision required.

## 1. Inputs status
| Input (claude.md s1) | Value | Label |
|---|---|---|
| Project name, customer, industry | [PROJECT NAME] / [CUSTOMER] / [INDUSTRY] | Unfilled |
| Approved budget | [BUDGET] | Unfilled |
| Commercial model | [FIXED PRICE / T&M / MANAGED SERVICE] | Unfilled |
| Timeline | [TIMELINE] | Unfilled |
| Preferred cloud | [CLOUD] | Unfilled |
| Team size | [TEAM SIZE] | Unfilled |

- [Assump] The delivery team is AI agents (see STAFFING_PLAN.md). Cost of AI agent usage is modelled as tooling/LLM consumption, not labour. Rate and pricing source: [TO BE CONFIRMED].
- [Assump] Human oversight roles (approvers/reviewers) are costed at [RATE] x [HOURS]; both unknown.
- [Decision] Approved budget, commercial model and approval threshold must be supplied by the sponsor.

## 2. Cost categories (claude.md s8)
| Category | Basis | Unit cost | Quantity | Planned | Actual | Forecast |
|---|---|---|---|---|---|---|
| AI agent usage (LLM tokens/compute) | tokens or sessions | [UNIT] | [QTY] | [X] | [X] | [X] |
| Human oversight effort | hours | [RATE] | [HOURS] | [X] | [X] | [X] |
| Subcontractor | per contract | [X] | [X] | [X] | [X] | [X] |
| Cloud | monthly estimate before provisioning | [X] | [MONTHS] | [X] | [X] | [X] |
| Licences | per seat/term | [X] | [X] | [X] | [X] | [X] |
| Tooling | per term | [X] | [X] | [X] | [X] | [X] |
| Cost of quality / rework | rework effort x rate | [X] | [X] | [X] | [X] | [X] |
| Support (post go-live) | monthly | [X] | [X] | [X] | [X] | [X] |
| Contingency | % of base | [X]% | | [X] | [X] | [X] |

[Assump] Onshore/nearshore/offshore mix is not applicable until human roles are defined; placeholder [MIX %].

## 3. Formulas
From claude.md s8:
- Gross margin = Revenue - Delivery cost
- Gross margin % = (Revenue - Delivery cost) / Revenue * 100
- Cost saving = Baseline operating cost - New operating cost
- ROI % = (Realized benefit - Investment cost) / Investment cost * 100
- Payback period = Investment cost / Monthly net benefit

Supporting definitions (not in claude.md s8; standard conventions, confirm):
- Delivery cost = sum of the category costs in section 2
- Estimate at completion = Actual cost to date + Estimate to complete
- Budget variance = Approved budget - Estimate at completion

Revenue and contract value apply only under a service-provider commercial model: [REVENUE] = unfilled.

## 4. Financial tracker (claude.md s15 format)
| Metric | Planned | Actual | Forecast | Variance | Corrective Action |
|--------|---------|--------|----------|----------|-------------------|
| Contract value | [X] | n/a | [X] | [X] | |
| Revenue | [X] | [X] | [X] | [X] | |
| Delivery cost | [X] | [X] | [X] | [X] | |
| Gross margin | [X] | [X] | [X] | [X] | |
| Gross margin % | [X] | [X] | [X] | [X] | |
| Cloud cost | [X] | [X] | [X] | [X] | |
| Contingency consumed | [X] | [X] | [X] | [X] | |
| Change request value | [X] | [X] | [X] | [X] | |

Actuals: none recorded. [Fact] No spend data exists in the repository.

## 5. FinOps and approvals
- [Rec] Estimate monthly cloud cost before any provisioning; tag resources (owner, application, environment, cost center, lifecycle).
- [Decision] Approval is required (claude.md s12) before purchasing cloud services or licences, exceeding the cost threshold, or committing figures externally. Approval request fields: action, reason, benefit, cost, risk, rollback, validation, approver. Cost threshold: [THRESHOLD]. Approver: [NAME].
