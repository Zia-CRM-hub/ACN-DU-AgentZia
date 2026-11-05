# KPI DICTIONARY: Universal Travel Ecosystem (candidate scope)

Owner: Business Analyst, Product Owner and UX Designer. Version 0.1 (draft), 2026-11-05. Subject is assumption A0 in REQUIREMENTS.md (UTE is the program; unconfirmed, Q0).

## Status of every number

No KPI has a measured baseline or current value: no production usage or analytics is evidenced **[Fact]**. All targets are **[Assumption]** proposals for sponsor approval, not commitments. Owners are proposed roles, not named people. Baselines need Q13 and instrumentation (FR-13). Do not report anything here as a realized benefit until Evidence and Approval are filled.

## Conventions

- Period: calendar month unless stated; report per tenant and platform-wide.
- Exclude demo supplier/gateway bookings and test tenants (demo bookings are fake and take no money).
- Events carry no PII.
- Benefit type per claude.md s8: Validated realized / Validated forecast / Estimated opportunity / Qualitative.
- No double counting: a time saving is not also a cost saving unless capacity is actually removed or redeployed.

## Standard formulas (claude.md s8)

| Measure | Formula |
|---|---|
| Cost saving | Baseline operating cost - New operating cost |
| Efficiency improvement % | (Baseline effort - New effort) / Baseline effort x 100 |
| Productivity gain % | (New output per effort - Baseline output per effort) / Baseline output per effort x 100 |
| ROI % | (Realized benefit - Investment cost) / Investment cost x 100 |
| Payback (months) | Investment cost / Monthly net benefit |
| Gross margin % | (Revenue - Delivery cost) / Revenue x 100 |

## Business owner KPIs

| ID | KPI | Definition and formula | Data source | Baseline | Proposed target | Freq | Proposed owner | Benefit type |
|---|---|---|---|---|---|---|---|---|
| K01 | Search-to-booking conversion | Confirmed bookings / unique searching sessions | Analytics (FR-13), bookings | Not measured | TBD after 8 weeks of data | Weekly | Product Owner | Estimated opportunity |
| K02 | Gross booking value (GBV) | Sum of confirmed booking price per currency, excluding cancelled and demo | bookings, platform stats | None | TBD (Q4, Q6) | Monthly | Business owner | Estimated opportunity |
| K03 | Active users | Distinct users with a search or booking in period | Auth plus analytics | None | TBD | Monthly | Product Owner | Qualitative until measured |
| K04 | Channel mix | Share of bookings started from web, mobile, chat, WhatsApp | Analytics channel attribute | None | Informational | Monthly | Product Owner | Qualitative |
| K05 | Chat-to-book rate | Confirmed bookings following a chat Book link / chat sessions that returned results | Analytics | None | TBD | Weekly | Product Owner | Estimated opportunity |
| K06 | Checkout completion | Bookings confirmed / checkouts started | Checkout records | None | 85% (proposal) | Weekly | Product Owner | Estimated opportunity |
| K09 | Time to complete booking | Median seconds, first search to confirmation | Analytics timestamps | None | Median under 5 min (proposal) | Monthly | UX Designer | Validated forecast once measured |
| K10 | Margin per booking | Markup or commission less supplier and payment fees (Q6) | Finance, supplier invoices | None | TBD | Monthly | Finance | Estimated opportunity |
| K11 | Tenant onboarding time | Hours from tenant request to first member booking | Audit log, ops record | None | Under 1 day (proposal) | Per tenant | Support Lead | Validated forecast |
| K12 | Policy compliance (corporate) | Bookings within org travel policy / corporate bookings | bookings, org policy | None | TBD (Q9) | Monthly | Org admin | Estimated opportunity |

## Quality, reliability and risk KPIs

| ID | KPI | Definition and formula | Data source | Baseline | Proposed target | Freq | Proposed owner |
|---|---|---|---|---|---|---|---|
| K07 | Booking integrity | Checkouts ending consistent (all confirmed, or payment fully released/refunded) / all checkouts. Stuck = `pending`, `processing` or `needs_attention` older than `STALE_PENDING_MINUTES` | bookings, worker logs | None | 100% consistent; stuck count 0 | Daily | SRE |
| K08 | Availability and latency | `/health` uptime %; p95 search latency | Prometheus | None | 99.5%, p95 under 5 s (proposal, Q8) | Daily | SRE |
| K13 | Accessibility conformance | WCAG 2.2 AA criteria passed / applicable; open Sev1 a11y defects | Audit report | Not assessed | 100% AA on key journeys, 0 Sev1 | Per release | UX Designer |
| K14 | AI answer accuracy | Eval-set answers whose price/availability claims match server data / eval-set size; prompt-injection pass rate | Evaluation dataset (B11) | Not measured | 100% price consistency, 100% injection pass (proposal) | Per release | Data and AI Engineer |
| K15 | Defect escape rate | Production defects found after release / total defects in release | Defect tracker | None | TBD | Per release | QA |
| K16 | Security findings | Open Critical and High findings from scans and tests | Pipeline scans | Not measured | 0 Critical, 0 High at go-live | Per release | Security Architect |
| K17 | Test health | Passing / total automated tests; CI green rate | CI | README claims 72 backend tests pass; not verified by me | No regression; add web/mobile tests | Per commit | QA |
| K18 | Supplier health | Supplier error rate; circuit-breaker opens per supplier | Metrics | None | TBD | Daily | SRE |

## User experience KPIs

| ID | KPI | Definition | Source | Baseline | Proposed target | Owner |
|---|---|---|---|---|---|---|
| K19 | Task completion rate | Usability-test participants completing search-to-booking unaided / participants (5 per journey) | Moderated tests | None | 90% (proposal) | UX Designer |
| K20 | CSAT / customer effort | Post-booking 1 to 5 survey; average and % scoring 4 to 5 | In-app survey (approved channel) | None | TBD | UX Designer |
| K21 | Support contacts per 100 bookings | Tickets / bookings x 100 | Support desk | None | TBD | Support Lead |
| K22 | Form error rate | Validation/API errors per 100 sessions on search and checkout | Analytics | None | Downward trend | UX Designer |

## Service provider KPIs (need a commercial model, Q6)

| ID | KPI | Definition | Source | Status |
|---|---|---|---|---|
| K23 | Delivery gross margin % | (Revenue - delivery cost) / revenue x 100 | Finance tracker | No contract or cost data; cannot be calculated |
| K24 | Effort variance | (Actual - planned effort) / planned effort x 100 | Time tracking | No plan baseline yet |
| K25 | Cloud cost per 100 bookings | Monthly cloud cost / bookings x 100 | Cloud billing | Nothing provisioned; estimate before spend |
| K26 | SLA compliance | Incidents meeting response/resolve targets / incidents | ITSM | No SLAs defined (Q8) |

## Benefit record template (one row per claimed benefit)

| Benefit | Type | Baseline | Target | Realized | Financial value | Confidence | Evidence | Owner | Approval |
|---|---|---|---|---|---|---|---|---|---|
| Guest books in fewer steps | Qualitative | Not measured | K09 median under 5 min | None | None | Low | Commits c8371e5, bebdc55 show the change shipped; no usage data | Product Owner | Not approved |

## Open items

Baselines need Q13 and FR-13. Targets need sponsor approval (Q1, Q2, Q6). Reconcile IDs and benefit rows with `BENEFITS_REALIZATION.md` (Finance) once Q0 is answered. Dashboards should use the charter KPI table (KPI, Baseline, Target, Current, Variance, Trend, Evidence, Owner, Action) once data exists.
