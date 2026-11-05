# Benefits Realization

Owner: Finance and Workforce Planner. Status: DRAFT framework. No benefits have been validated or realized.

Labels: Fact / Calc / Fcst / Assump / Rec / Decision.

## 1. Classification (claude.md s8)
Validated realized benefit | Validated forecast benefit | Estimated opportunity | Qualitative benefit.
Rule: estimated opportunities are never reported as realized savings. All rows below start as Estimated opportunity or Qualitative.

## 2. Benefits register
| Benefit | Type | Baseline | Target | Realized | Financial Value | Confidence | Evidence | Owner |
|---------|------|----------|--------|----------|-----------------|------------|----------|-------|
| Cost reduction | Estimated opportunity | [BASELINE] | [TARGET] | None | [X] | [Low/Med/High] | None yet | [OWNER] |
| Productivity improvement | Estimated opportunity | [BASELINE] | [TARGET] | None | [X] | [ ] | None yet | [OWNER] |
| Efficiency (effort reduction) | Estimated opportunity | [BASELINE] | [TARGET] | None | [X] | [ ] | None yet | [OWNER] |
| Faster time to market | Estimated opportunity | [BASELINE] | [TARGET] | None | [X] | [ ] | None yet | [OWNER] |
| User adoption / satisfaction | Qualitative | [BASELINE] | [TARGET] | None | n/a | [ ] | None yet | [OWNER] |

[Assump] Benefit categories come from the claude.md outcome list because [OUTCOMES] is unfilled. Replace once the sponsor supplies expected outcomes.

## 3. Per-benefit record (required fields)
Baseline, data source, measurement period, calculation method, benefit owner, expected value, realized value, confidence level, evidence, approval status. Approval status for all entries: Not approved.

## 4. Formulas (claude.md s8)
- Cost saving = Baseline operating cost - New operating cost
- Efficiency improvement % = (Baseline effort - New effort) / Baseline effort * 100
- Productivity gain % = (New output per unit of effort - Baseline output per unit of effort) / Baseline output per unit of effort * 100
- ROI % = (Realized benefit - Investment cost) / Investment cost * 100
- Payback period = Investment cost / Monthly net benefit

Investment cost links to delivery cost in docs/financials/COST_MODEL.md: [LINK AFTER ACTUALS].

## 5. Double-counting control
A single saving may be claimed under only one of: automation, productivity, headcount avoidance, cycle-time reduction. Each register row must state its category; a reviewer checks overlap before approval.

## 6. Measurement plan
| Step | Action | Status |
|---|---|---|
| 1 | Capture baselines before change | Not started |
| 2 | Agree data sources and measurement period | Not started |
| 3 | Owner validates calculation | Not started |
| 4 | Approver signs off realized value | Not started |

- [Decision] Sponsor to name benefit owners, baselines and approver.
- [Rec] Do not treat go-live as success; track adoption and stable operations.
