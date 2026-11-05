# REQUIREMENTS: Universal Travel Ecosystem (UTE) candidate scope

Owner: Business Analyst, Product Owner and UX Designer. Version 0.1 (draft). Date: 2026-11-05.

Labels: **[Fact]** confirmed from repo evidence, **[Calc]** calculated, **[Forecast]**, **[Assumption]**, **[Rec]** recommendation, **[Decision]** decision required.

## 1. Evidence base and caveats

- `AgentZ/claude.md` project fields are all unfilled (name, customer, problem, users, budget, timeline). **[Fact]** AgentZ itself holds only the charter, agent definitions and delivery docs; no product code. **[Fact]**
- The only product evidence is the sibling application in the parent git repository (`../README.md`; docs as committed in HEAD: ARCHITECTURE, SAAS, API, CONFIGURATION, OPERATIONS). It is "Universal Travel Ecosystem". **Whether UTE is the program this delivery unit is meant to deliver is not confirmed (Q0).** I use it as the candidate subject so requirements are concrete; if wrong, discard section 4 and keep the method. **[Assumption A0]**
- Other AgentZ docs (e.g. OUTCOME_MAP.md) were written assuming an empty repo and a generic program. Reconcile after Q0. **[Decision]**
- Git status shows `docs/`, `mobile/`, `.github/workflows/ci.yml`, `scripts/demo.py` of the parent repo as deleted in the working tree but present in HEAD. I read them from HEAD. Confirm the deletion is intended (Q11). **[Decision]**
- README claims 72 passing backend tests; I did not run them. Adapters for Duffel, Amadeus, Razorpay and the Docker/Compose files are self-reported as never run against real services. **[Fact: self-reported, unverified]**

## 2. Understanding

| Item | Statement |
|---|---|
| Product | Multi-tenant SaaS to search, plan and book flights, trains, buses and hotels via web, mobile (Expo), AI chat concierge and WhatsApp on one FastAPI/PostgreSQL backend. **[Fact]** |
| Business problem | Unknown. Inferred: travel booking is fragmented across suppliers and channels. **[Assumption]** (Q1) |
| Built (claimed) | Flight adapters (Duffel/Amadeus, unverified live), synthetic train/bus/hotel, planner, multi-booking single-payment checkout, chat agent (search/plan only, cannot book), WhatsApp webhook, tenant/org/user admin API with audit. **[Fact]** |
| Not built | Real rail/bus/hotel inventory, cruises, homestays, business-travel approvals/invoicing, personalization, experiences, local mobility, admin console UI. **[Fact]** |
| Stakeholders | Platform operator (super admin), tenant admins, org admins, travellers, suppliers (Duffel, Amadeus), Razorpay, Meta (WhatsApp), delivery team. Names and sponsor unknown. **[Assumption]** |
| Geography | Likely India (Razorpay, INR-style policy currency). **[Assumption]** (Q5) |

## 3. Assumptions (reversible)

| ID | Assumption | Impact if wrong |
|---|---|---|
| A0 | UTE is the program subject. | Whole document. |
| A1 | Near-term goal is a pilot with one real tenant, not a broad launch. | Roadmap order. |
| A2 | Commercial model is a per-tenant SaaS fee; no contract exists. | Finance KPIs unusable. |
| A3 | Users: consumers (public tenant) and corporate travellers (private tenants). | Business travel scope. |
| A4 | Compliance: India DPDP Act; card data stays with Razorpay (not stored). WCAG 2.2 AA per charter. | Security backlog. |
| A5 | Demo supplier/gateway stay disabled in production (config already enforces it). | Fake-booking risk. |
| A6 | Cloud not chosen; Docker Compose on a Linux host is baseline. | Architecture, cost. |

## 4. Functional requirements

Priority: M = Must for pilot, S = Should, C = Could. Status is as claimed by repo docs; not verified by me.

| ID | Requirement | Pri | Status (claimed) | Acceptance criteria (summary) |
|---|---|---|---|---|
| FR-01 | Search flights, trains, buses, hotels concurrently across allowed suppliers | M | Built; only flights have real adapters | Results from all enabled suppliers return within supplier timeout; one supplier failing does not fail the search. |
| FR-02 | One-action trip planner | S | Built (generic ideas) | Plan returns day-by-day outline with bookable legs. |
| FR-03 | Checkout: multiple items, single payment, all-or-nothing | M | Built (mock-tested) | If any booking fails the payment is released/refunded and the user told; nothing stays `pending` beyond `STALE_PENDING_MINUTES`. |
| FR-04 | Guest can plan and search; login/account creation deferred to booking | M | Built (recent commits) | Guest reaches payment on one page with no separate sign-up step. |
| FR-05 | View and cancel bookings (own; org admin for org; tenant admin for tenant) | M | Built | Scope enforced; foreign ids return 404. |
| FR-06 | AI concierge on web, mobile, WhatsApp: search, plan, hand off Book link; never books or takes payment | M | Built v1 | Chat cannot invoke checkout; every price shown comes from server data. |
| FR-07 | Tenants, orgs, roles, plan limits, suspension, audit | M | Built as API | Cross-tenant access impossible; suspension locks out at once; admin actions audited. |
| FR-08 | Organization travel policy (max trip amount) | S | Stored; enforcement at booking to confirm | Over-limit booking blocked, warned or routed for approval (Q9). |
| FR-09 | Admin console UI | S | Not built | All FR-07 capabilities usable without raw API calls. |
| FR-10 | Real inventory for trains, buses, hotels | S | Not built | At least one live supplier per mode, sandbox-verified. |
| FR-11 | Business travel: approvals, company invoicing, tax invoices | C | Not built | Defined after Q4, Q9. |
| FR-12 | Personalization | C | Not built | Needs privacy impact assessment first. |
| FR-13 | Product analytics events for KPI funnel | M | Not evidenced (Prometheus ops metrics exist) | Search, select, checkout start, payment success, cancel, chat-to-book captured, channel-tagged, no PII. |

## 5. Non-functional requirements (initial; full set belongs in architecture/NON_FUNCTIONAL_REQUIREMENTS.md)

| ID | Requirement | Label |
|---|---|---|
| NFR-01 | WCAG 2.2 AA on web and mobile | Charter mandate; not assessed |
| NFR-02 | Search p95 under 5 s with live suppliers; availability 99.5%; RPO/RTO TBD | Assumption (Q8) |
| NFR-03 | No hard-coded secrets, startup config validation, tenant-isolation tests, OWASP ASVS L2 | Partly claimed built; unverified |
| NFR-04 | PII minimised; none in logs or LLM prompts | Needs data inventory (Q7) |
| NFR-05 | Responsible AI: grounding, prompt-injection tests, eval set, audit trail, kill switch | Not evidenced |
| NFR-06 | JSON logs, Prometheus metrics, alert on stuck bookings | Built per docs |
| NFR-07 | More than one API replica requires Redis and a real load balancer | Per SCALING.md |

## 6. UX and accessibility measures

- Journeys to design and test: guest search to booking (one-page checkout), chat to Book link, WhatsApp to web Book handoff, tenant onboarding by an admin.
- Moderated usability test, 5 users per journey, before pilot: task completion, time on task, errors. **[Rec]**
- Accessibility checks: keyboard-only flow, screen-reader labels on From/To autocomplete, contrast, focus order, 24 px minimum target size (SC 2.5.8), no cognitive-test authentication (SC 3.3.8); automated (axe) plus manual audit. **[Rec]**
- Payment failure/release copy must state refund timing (5 to 7 working days per OPERATIONS.md). **[Fact: documented]**
- Currency, language and locale formats pending Q5.

## 7. Prioritised backlog (claude.md section 16 weighting)

Scale 1 to 5 per dimension (effort and dependency inverted: 5 = low effort / few dependencies). Weights: value 25, customer 15, risk 15, revenue/cost 15, strategy 10, regulatory 10, effort 5, dependency 5. Inputs are my judgement; scores are **[Calc]** from them and need sponsor validation.

| Rank | ID | Item | Score | Justification | Dependency | If skipped | Timing |
|---|---|---|---|---|---|---|---|
| 1 | B2 | Verify Razorpay in test mode (manual capture, refund) | 4.30 | Money path; endpoints noted "from memory" | Test keys | Charged without booking | Now |
| 2 | B1 | Verify Duffel in sandbox, fix adapter | 4.20 | No revenue without live flights | Test token | Cannot sell | Now |
| 3 | B5 | Security baseline: threat model, secret/dependency scans, tenant-isolation tests, DPDP privacy assessment | 3.90 | Multi-tenant, payments, PII | Q7 | Breach, regulatory | 30 days |
| 4 | B6 | KPI instrumentation (FR-13) | 3.75 | Benefits unprovable without it | Event schema | Unmeasurable outcomes | 30 days |
| 4 | B7 | One real train, bus, hotel supplier each | 3.75 | Core vision gap | Q3, contracts | Flights-only product | 60 to 90 days |
| 6 | B8 | First real Docker Compose deploy to non-prod | 3.45 | Never run per docs | Hosting approval | Go-live surprises | 30 days (approval) |
| 6 | B11 | Concierge eval set, prompt-injection and hallucination tests | 3.45 | Customer-facing LLM | Eval data, Q12 | Wrong prices or advice | 30 to 60 days |
| 8 | B9 | Business travel (approvals, invoices) | 3.35 | Likely revenue segment (A3) | Q4, Q9 | Corporates cannot adopt | 90+ days |
| 9 | B4 | WCAG 2.2 AA audit and fixes | 3.30 | Charter mandate | Stable UI | Exclusion, legal | 60 days |
| 10 | B3 | Admin console UI | 3.25 | Admins need API calls today | None | Slow onboarding | 60 to 90 days |
| 11 | B10 | Personalization | 2.55 | Not needed for pilot | B5, B6 | None short term | Later |

## 8. Discovery questions (only those that change scope, cost, security or timeline)

| # | Question | Why it matters | Who |
|---|---|---|---|
| Q0 | Is UTE (the parent-repo app) the program to deliver? If not, what is? | Validates this whole document. | Sponsor |
| Q1 | What business problem, which customer, who is the sponsor? | KPI targets are guesses without it. | Sponsor |
| Q2 | Pilot, commercial launch, or demo? Target date? | MVP scope, compliance depth. | Sponsor |
| Q3 | Which suppliers are contractually available (flights, rail, bus, hotels)? Is Amadeus Enterprise access held? | Drives revenue and effort. | Sponsor |
| Q4 | First tenants: consumers, corporates, agencies? Expected users and bookings per month? | Sizing, pricing, FR-11. | Sponsor |
| Q5 | Countries, currencies, languages at launch? | Tax, gateway, localization, data residency. | Sponsor |
| Q6 | Revenue model: SaaS fee, margin, commission, markup? | Unit economics, revenue KPIs. | Finance |
| Q7 | What personal data is collected (passport, ID, phone)? Retention rules? Which regulator (DPDP, GDPR)? | Privacy and security design. | Security/Legal |
| Q8 | Availability, latency, RPO/RTO, support hours? | NFRs, hosting cost. | Operations |
| Q9 | Travel policy exceeded: block, warn or require approval? | FR-08 behaviour. | Business owner |
| Q10 | Preferred cloud, hosting budget ceiling, spend approver? | Architecture, FinOps. | Sponsor |
| Q11 | Is the working-tree deletion of docs/mobile/ci.yml/demo.py intentional? | Risk of losing artifacts. | Repo owner |
| Q12 | Which LLM is approved for the concierge; may customer data be sent to it? | Responsible AI, privacy. | Security/Legal |
| Q13 | Is there a baseline for the current booking process (time, cost, conversion)? | Benefit baselines. | Business owner |

## 9. Approval requests to prepare (none executed)

| Action | Reason | Cost | Risk | Rollback | Validation | Approver |
|---|---|---|---|---|---|---|
| Create Duffel and Razorpay test accounts/tokens | B1, B2 | Free in test mode (Assumption) | Low | Revoke tokens | Sandbox bookings pass | Sponsor |
| Provision non-prod host for Compose deploy | B8 | Unknown (Q10) | Low to medium | Delete host | Health checks, smoke test | Sponsor |
| Production go-live, live supplier funds, customer comms | Launch | Unknown | High | Provider switch, feature flag | Release readiness review | Sponsor |

## 10. Traceability (starting point)

Conversion/revenue: FR-01, 03, 04 to K01, K02, K06, K10. Adoption: FR-04, 06 to K03, K04, K05. Reliability: FR-03, NFR-06 to K07, K08. Operations cost: FR-09 to K11. Trust and inclusion: NFR-01, 05 to K13, K14. KPI definitions: `docs/benefits/KPI_DICTIONARY.md`.
