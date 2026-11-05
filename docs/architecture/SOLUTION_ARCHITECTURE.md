# Solution Architecture (Initial, Reference Baseline)

Owner: Solution and Technical Architect | Status: Draft v0.1 | Date: 2026-11-05

## 1. Evidence base and labels

Labels used: **Confirmed fact**, **Assumption**, **Recommendation**, **Decision required**.

- **Confirmed fact:** AgentZ/claude.md has every project field unfilled (name, customer, industry, problem, users, geography, outcomes, timeline, budget, commercial model, cloud, constraints, phase).
- **Confirmed fact:** AgentZ contains only agent definitions (.claude/agents), claude.md and docs/delivery/ROSTER.md. It has no application source, infrastructure code or tests.
- **Confirmed fact:** The surrounding git status shows untracked sibling folders (UniversalTravelEcosystem, measureMate, and others) and deleted travel-app files. Nothing in AgentZ links to them. They were not analysed and are out of scope.
- No progress, metrics, cost figures or test results exist, and none are claimed here.

## 2. Assumptions (all reversible)

| ID | Assumption | Impact if wrong |
|---|---|---|
| A1 | The target is a greenfield, web-first enterprise application with APIs, a relational store and an optional AI assistant capability. | Re-baseline the logical view. |
| A2 | Cloud is Azure-primary, with Microsoft Entra ID for identity. Chosen because claude.md lists Microsoft technologies first. No multi-cloud. | Swap the physical view. The logical view is unchanged. |
| A3 | Delivery phase is Discovery/Architecture. | Scope of this document. |
| A4 | Users are internal staff plus external customers, in one region initially. | Residency and DR design. |
| A5 | Data may include PII but no regulated (PCI/PHI) data until confirmed. | Raises the control baseline. |
| A6 | A modular monolith plus a few async workers, not microservices, until scale evidence justifies a split. | See ADR-S02. |

## 3. Decisions required from humans

| ID | Decision | Why it matters | Approver |
|---|---|---|---|
| D1 | Fill in the project fields in claude.md (problem, outcomes, users, geography, budget, cloud, compliance). | Every NFR target below is provisional until then. | Sponsor / Delivery Lead |
| D2 | Confirm the cloud and compliance regime (A2, A5). | Drives the physical design and the control set. | Sponsor, Security |
| D3 | Approve cloud spend before any provisioning. | claude.md section 12. | Finance / Sponsor |

## 4. Context (C4 level 1)

```mermaid
C4Context
  title System Context (assumed)
  Person(user, "End User", "Staff or customer using web/mobile")
  Person(admin, "Administrator", "Configures and supports the platform")
  System(sys, "Target Platform", "Web app, API and optional AI assistant")
  System_Ext(idp, "Microsoft Entra ID", "Identity and SSO")
  System_Ext(erp, "Existing systems", "Unknown. To be discovered (D1)")
  System_Ext(ai, "Azure OpenAI / AI Foundry", "LLM and content safety")
  System_Ext(notify, "Email / SMS provider", "Notifications")
  Rel(user, sys, "Uses", "HTTPS")
  Rel(admin, sys, "Administers", "HTTPS")
  Rel(sys, idp, "Authenticates", "OIDC")
  Rel(sys, erp, "Integrates", "REST / events")
  Rel(sys, ai, "Prompts", "HTTPS")
  Rel(sys, notify, "Sends", "HTTPS")
```

## 5. Containers (C4 level 2)

```mermaid
flowchart LR
  U[User browser/mobile] --> FD[Front Door + WAF]
  FD --> SPA[Web front end<br/>React/Next.js, TypeScript]
  SPA --> APIM[API gateway<br/>API Management]
  APIM --> API[Application API<br/>modular monolith, .NET or Node]
  API --> DB[(Relational DB<br/>Azure SQL/PostgreSQL)]
  API --> CACHE[(Redis cache)]
  API --> BUS[[Service Bus]]
  BUS --> WRK[Background workers]
  WRK --> DB
  WRK --> EXT[External/legacy systems]
  API --> AIG[AI gateway module<br/>grounding, safety, audit]
  AIG --> LLM[Azure OpenAI]
  AIG --> SRCH[(AI Search index)]
  API -. telemetry .-> OBS[Azure Monitor / App Insights]
  WRK -. telemetry .-> OBS
  API --> KV[Key Vault]
  SPA -. sign-in .-> IDP[Entra ID]
  API -. validates JWT .-> IDP
```

## 6. Logical components

```mermaid
flowchart TB
  subgraph API[Application API]
    ID[Identity and access] --- CORE[Core domain modules]
    CORE --- INT[Integration adapters]
    CORE --- NOTI[Notifications]
    CORE --- AUD[Audit trail]
    CORE --- AIM[AI gateway module]
  end
  AIM -->|human approval for consequential actions| CORE
```

Design rules (Recommendation):
- API-first with OpenAPI contracts. Every integration sits behind an adapter and has an anti-corruption layer.
- Each module owns its tables. No cross-module table access.
- Every consequential AI action needs human approval and is audited. This follows claude.md section 11.

## 7. Key flows

```mermaid
sequenceDiagram
  actor U as User
  participant W as Web app
  participant G as API gateway
  participant A as API
  participant D as Database
  participant Q as Service Bus
  participant K as Worker
  U->>W: Action
  W->>G: HTTPS + JWT (Entra)
  G->>A: Rate-limited request
  A->>A: AuthZ check, validate input
  A->>D: Transaction (write + outbox)
  A-->>W: 202/200 with correlation id
  A->>Q: Publish event (from outbox)
  Q->>K: Deliver
  K->>K: Idempotent processing, retries, DLQ
```

## 8. Deployment view (physical, Azure, assumed)

```mermaid
flowchart TB
  subgraph Sub[Per environment: dev / test / staging / prod, separate subscriptions]
    FD[Front Door+WAF] --> CA[Container Apps or App Service]
    CA --> PE{{Private endpoints}}
    PE --> SQL[(SQL/PostgreSQL)]
    PE --> RED[(Redis)]
    PE --> SB[[Service Bus]]
    PE --> KV[Key Vault]
    CA --> MON[Log Analytics + App Insights]
  end
  GH[GitHub Actions CI/CD] -->|OIDC, no stored secrets| Sub
  IaC[Bicep/Terraform modules] --> GH
```

Prod deployment, identity changes and spend need explicit human approval (claude.md section 12).

## 9. Architecture decisions (summary)

| ID | Decision | Alternatives | Rationale | Exit / reversal |
|---|---|---|---|---|
| ADR-S01 | Azure-primary (A2) | AWS, GCP, multi-cloud | Microsoft stack alignment. Multi-cloud complexity is not justified without evidence. | Containers + IaC + OIDC/OpenAPI keep the app portable. |
| ADR-S02 | Modular monolith + workers (A6) | Microservices | Smaller team, lower ops cost, clear module seams for later extraction. | Extract a module behind its existing API and events. |
| ADR-S03 | Relational DB as system of record, with an outbox for events | Cosmos DB, event sourcing | Transactional integrity. | Outbox lets the broker be swapped. |
| ADR-S04 | Entra ID, OIDC, managed identities | Custom auth | Zero Trust and no secrets in code. | The IdP sits behind a standard OIDC interface. |
| ADR-S05 | AI via a controlled gateway module | Direct LLM calls from features | One place for grounding, content safety, PII filtering, audit and a kill switch. | Feature flag disables AI. Model is swappable. |

Each ADR needs the full record (costs, risks, security/ops/business impact) in docs/decisions once D1 and D2 are resolved.

## 10. Requirement traceability (skeleton)

| Outcome | Requirement | Design element | Test | Status |
|---|---|---|---|---|
| Unknown (D1) | Unknown | Sections 5-8 | Not yet defined | Not started |

Fill this in when REQUIREMENTS.md exists. See NON_FUNCTIONAL_REQUIREMENTS.md for the quality attributes.

## 11. Next steps (Recommendation)

1. Resolve D1 and D2.
2. Create INTEGRATION_ARCHITECTURE.md after the existing-systems inventory.
3. Hand the security view to the Security Architect and the data view to the Data/AI Engineer.
4. Produce a cost estimate before any provisioning (D3).
