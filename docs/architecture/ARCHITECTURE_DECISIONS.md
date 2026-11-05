# Architecture Decisions

Owner: Enterprise Architect | Date: 2026-11-05 | Links: [OUTCOME_MAP.md](OUTCOME_MAP.md)

Basis: the repository holds no code and the project fields in `claude.md` are unfilled. These ADRs therefore rest on the assumptions A-01 to A-06 in OUTCOME_MAP.md. All are **Proposed** and none are approved. Approver for each is the customer architecture authority or sponsor [Decision required].

Status values: Proposed, Accepted, Superseded, Rejected. Cost figures are not given because no pricing or budget input exists. Each ADR states the cost direction only.

## ADR index

| ID | Title | Status |
|---|---|---|
| ADR-000 | ADR template | Template |
| ADR-001 | Record architecture decisions as versioned Markdown | Proposed |
| ADR-002 | Azure as the default cloud, no multi-cloud at start | Proposed |
| ADR-003 | Infrastructure as Code for all environments | Proposed |
| ADR-004 | API-first, modular service design | Proposed |
| ADR-005 | Managed identity and Entra ID; no stored secrets | Proposed |
| ADR-006 | Human approval gates for production and AI-initiated consequential actions | Proposed |
| ADR-007 | Observability and FinOps from the first environment | Proposed |

---

## ADR-000: Template

- Status: Proposed | Accepted | Superseded by ADR-xxx | Rejected
- Date / Deciders / Approver:
- Related outcomes (O-ids) and requirements:
- **Problem**:
- **Context** (facts vs assumptions, constraints):
- **Options** (at least two, including "do nothing"):
- **Selected option**:
- **Rationale**:
- **Benefits**:
- **Costs** (build, run, licence, effort):
- **Risks**:
- **Security impact**:
- **Operational impact**:
- **Business impact**:
- **Exit or reversal approach**:
- **Validation** (how we will know it worked; review date):

---

## ADR-001: Record architecture decisions as versioned Markdown

- Status: Proposed | Date: 2026-11-05 | Approver: Delivery Lead
- Outcomes: O3, O4
- **Problem**: Decisions made by multiple agents and humans get lost or contradicted without a durable record.
- **Context**: [Confirmed] docs live in the repo under `docs/`; claude.md s.5 requires ADRs with fixed fields.
- **Options**: (a) Markdown ADRs in repo; (b) wiki or Confluence page; (c) no formal record.
- **Selected option**: (a), one consolidated file now, split into `docs/decisions/ADR-nnn.md` once there are more than about 15.
- **Rationale**: Reviewable in pull requests, versioned with code, no extra tool.
- **Benefits**: Traceability, review history, zero licence cost.
- **Costs**: Small authoring effort per decision.
- **Risks**: ADRs go stale. Mitigation: review at each phase gate.
- **Security impact**: None. Do not place secrets or customer data in ADRs.
- **Operational impact**: None.
- **Business impact**: Faster onboarding, auditability.
- **Exit or reversal**: Export to any wiki; plain text.
- **Validation**: Each significant technology choice has an ADR before implementation.

## ADR-002: Azure as the default cloud, no multi-cloud at start

- Status: Proposed | Date: 2026-11-05 | Approver: Sponsor / customer architect [Decision required]
- Outcomes: O1, O2, O5
- **Problem**: A cloud target must be chosen before infrastructure design.
- **Context**: [Assumption A-04] Microsoft-centric stack; the customer's actual preference is unknown. claude.md s.4 says avoid multi-cloud without a clear regulatory, resilience, customer or capability reason. No such reason is evidenced.
- **Options**: (a) Azure only; (b) AWS or GCP only; (c) multi-cloud from day one.
- **Selected option**: (a) Azure only, using portable building blocks (containers, PostgreSQL or SQL, OpenAPI, Terraform or Bicep) to keep exit cost bounded.
- **Rationale**: Fits Microsoft technology expectations, lowest operational complexity, fewest skills required.
- **Benefits**: Single operating model, integrated identity, monitoring and policy.
- **Costs**: Azure consumption (not estimated; needs workload sizing). Some lock-in to managed services.
- **Risks**: The customer may mandate another cloud. Mitigation: confirm before any provisioning; keep application code cloud-neutral.
- **Security impact**: Uses Entra ID, Key Vault, Defender for Cloud and Azure Policy natively.
- **Operational impact**: One set of runbooks, one cost tool.
- **Business impact**: Faster mobilization.
- **Exit or reversal**: Containerized workloads and IaC modules can be re-targeted; data export via standard formats. Revisit if a stated regulatory or resilience driver appears.
- **Validation**: Customer confirmation recorded; a landing-zone review before the first provision.

## ADR-003: Infrastructure as Code for all environments

- Status: Proposed | Date: 2026-11-05 | Approver: Cloud/DevOps lead, then customer
- Outcomes: O1, O3, O5
- **Problem**: Manual provisioning is unrepeatable and unauditable.
- **Context**: claude.md s.4 requires IaC, separate dev/test/staging/prod, tagging and cost estimates before provisioning.
- **Options**: (a) Bicep; (b) Terraform; (c) portal/manual.
- **Selected option**: Terraform with versioned modules under `/infrastructure/modules` [Recommendation], because it also covers non-Azure resources if ADR-002 is reversed. Bicep remains acceptable if the customer standardizes on it.
- **Rationale**: Repeatability, peer review, policy-as-code checks in CI.
- **Benefits**: Faster environment creation, drift detection, evidence for audit.
- **Costs**: Skill and state-management setup; tooling is free at base tier.
- **Risks**: State file exposure or a bad apply. Mitigation: remote encrypted state, plan-only in CI, apply to production only after human approval.
- **Security impact**: Policy scans on plans; no secrets in code.
- **Operational impact**: Changes only through pull requests.
- **Business impact**: Lower rework cost, safer releases.
- **Exit or reversal**: Resources can be imported into another IaC tool.
- **Validation**: A non-production environment is rebuilt from code with no manual steps.

## ADR-004: API-first, modular service design

- Status: Proposed | Date: 2026-11-05 | Approver: Solution Architect, then customer architect
- Outcomes: O1, O3, O6
- **Problem**: Need an integration-ready structure without premature complexity.
- **Context**: Existing systems unknown [Assumption]. claude.md prohibits unnecessary frameworks and requires API-first design.
- **Options**: (a) Modular monolith with versioned REST/OpenAPI contracts; (b) microservices from the start; (c) low-code only.
- **Selected option**: (a), with module boundaries aligned to the capability map, splitting out services only when scaling or team-autonomy evidence justifies it.
- **Rationale**: Lowest delivery and operations cost for an unproven scope; contracts keep later extraction cheap.
- **Benefits**: Fast start, simple deployment and testing, contract tests possible.
- **Costs**: Discipline needed to keep module boundaries.
- **Risks**: Boundary erosion. Mitigation: architecture fitness tests in CI.
- **Security impact**: A smaller attack surface than many services; one authN/authZ enforcement point.
- **Operational impact**: One deployable unit to monitor.
- **Business impact**: Earlier first release.
- **Exit or reversal**: Extract modules into services behind the same contracts.
- **Validation**: OpenAPI specs published and contract-tested before the first consumer integrates.

## ADR-005: Managed identity and Entra ID; no stored secrets

- Status: Proposed | Date: 2026-11-05 | Approver: Security Architect
- Outcomes: O4
- **Problem**: Credentials in code or config are a primary breach cause.
- **Context**: claude.md s.11 mandates Zero Trust, least privilege, managed identities and secrets management. [Assumption A-04] Entra ID is available.
- **Options**: (a) Entra ID for users plus managed identities for workloads, Key Vault for unavoidable secrets; (b) app-local accounts and config secrets.
- **Selected option**: (a).
- **Rationale**: Removes long-lived secrets, central revocation, auditable.
- **Benefits**: Lower breach risk, SSO, conditional access.
- **Costs**: Entra licence tier may affect conditional access features (unverified). Setup effort.
- **Risks**: External or guest users may need Entra External ID [Decision required]. Misconfigured roles. Mitigation: role reviews and IAM-as-code.
- **Security impact**: Positive; secret scanning in CI as a backstop.
- **Operational impact**: Access reviews become a recurring task.
- **Business impact**: Supports compliance evidence.
- **Exit or reversal**: Standards-based OIDC/OAuth2 keeps the identity provider replaceable.
- **Validation**: Secret-scan reports zero findings; no password or key in repo or pipeline variables.

## ADR-006: Human approval gates for production and AI-initiated consequential actions

- Status: Proposed | Date: 2026-11-05 | Approver: Sponsor
- Outcomes: O4, O3
- **Problem**: Autonomous agents could cause irreversible, costly or non-compliant actions.
- **Context**: [Confirmed] claude.md s.10 and s.12 require explicit human approval for production deployment, migrations, deletions, access changes, spend and external communication.
- **Options**: (a) Mandatory approval gates with audit trail; (b) approvals only for production deployment; (c) full autonomy.
- **Selected option**: (a): protected environments and required reviewers in the pipeline; AI agents prepare approval requests using the s.12 format (action, reason, benefit, cost, risk, rollback, validation, approver) and never self-approve.
- **Rationale**: Matches the stated autonomy model and limits blast radius.
- **Benefits**: Segregation of duties, traceable accountability, kill-switch readiness.
- **Costs**: Added lead time per gated action.
- **Risks**: Approver bottleneck. Mitigation: name delegates and set an approval service time [Decision required].
- **Security impact**: Positive; agents run with least-privilege identities and no production write rights.
- **Operational impact**: Approver roster and on-call cover needed.
- **Business impact**: Reduced risk of costly incidents.
- **Exit or reversal**: Relax gates per action class only by a new ADR with approver sign-off.
- **Validation**: Pipeline refuses production deploy without a recorded approval; verified in a non-production dry run.

## ADR-007: Observability and FinOps from the first environment

- Status: Proposed | Date: 2026-11-05 | Approver: SRE lead / Finance
- Outcomes: O2, O5, O7
- **Problem**: Retrofitting monitoring and cost control is expensive; benefits cannot be proven without telemetry.
- **Context**: claude.md s.2 requires observability and FinOps by design; s.4 requires tagging and pre-provisioning cost estimates.
- **Options**: (a) Azure Monitor and Application Insights with OpenTelemetry instrumentation, mandatory tags and budgets; (b) add later; (c) third-party suite.
- **Selected option**: (a).
- **Rationale**: Native integration, OpenTelemetry keeps portability.
- **Benefits**: SLO tracking, faster diagnosis, cost accountability, KPI evidence for the outcome map.
- **Costs**: Log ingestion and retention charges (not estimated); mitigated by sampling and retention policy.
- **Risks**: Sensitive data in logs. Mitigation: structured logging with redaction rules and review.
- **Security impact**: Security events centralized; log access is restricted.
- **Operational impact**: Dashboards, alerts and runbooks are owned by SRE.
- **Business impact**: Enables measured, not claimed, outcomes.
- **Exit or reversal**: OpenTelemetry exporters can point to another backend.
- **Validation**: Every environment has tags, a budget alert, a health dashboard and a smoke-test signal before use.

---

## Decisions required (summary)

| # | Decision | Needed by | Owner |
|---|---|---|---|
| 1 | Confirm or replace Azure (ADR-002) | Before any provisioning | Sponsor / customer architect |
| 2 | Choose Terraform or Bicep (ADR-003) | Before IaC work | Customer architect |
| 3 | User population and identity model (ADR-005) | Before design of auth | Sponsor |
| 4 | Approver roster and service times (ADR-006) | Before first gated release | Sponsor |
| 5 | Fill project fields in claude.md | Immediately | Sponsor |
