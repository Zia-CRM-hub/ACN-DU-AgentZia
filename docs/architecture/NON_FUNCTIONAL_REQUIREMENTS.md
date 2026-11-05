# Non-Functional Requirements (Initial)

Owner: Solution and Technical Architect | Status: Draft v0.1 | Date: 2026-11-05

**All targets are Assumptions or Recommendations.** claude.md has no project values, so no baselines or measurements exist. Each target must be confirmed by the business owner (Decision D1 in SOLUTION_ARCHITECTURE.md). The "Verification" column says how each target will be evidenced. Nothing has been tested.

| ID | Category | Requirement (provisional target) | Label | Verification | Design link |
|---|---|---|---|---|---|
| NFR-PERF-01 | Performance | p95 API latency under 500 ms for reads and under 1 s for writes at the expected load. | Assumption | Load test in staging | Cache, indexes |
| NFR-PERF-02 | Performance | p75 page load (LCP) under 2.5 s on a typical broadband connection. | Assumption | Synthetic and RUM monitoring | CDN, SPA budgets |
| NFR-SCAL-01 | Scalability | Horizontal autoscaling of stateless API and workers. Peak load of 5x the average is handled without manual action. | Assumption | Load test | Container autoscale |
| NFR-AVL-01 | Availability | 99.9% monthly for user-facing services (about 43 min downtime per month). | Assumption | SLO dashboard | Multi-instance, health probes |
| NFR-DR-01 | Resilience | RPO 15 min and RTO 4 h for production. | Assumption | DR drill in non-prod | Geo-backup, IaC rebuild |
| NFR-DR-02 | Resilience | Retries with backoff, circuit breakers, idempotent handlers and a dead-letter queue for all integrations. | Recommendation | Fault-injection tests | Outbox, Service Bus |
| NFR-SEC-01 | Security | Entra ID SSO with MFA. Role-based least-privilege access. No shared accounts. | Recommendation | Access review, tests | ADR-S04 |
| NFR-SEC-02 | Security | TLS 1.2+ in transit and encryption at rest. Secrets only in Key Vault. Managed identities are used. | Recommendation | Policy-as-code scan | Deployment view |
| NFR-SEC-03 | Security | OWASP ASVS L2 as the baseline. Zero open critical or high findings at release. Dependency, secret and container scans in CI. | Recommendation | CI reports, pen test | DevSecOps pipeline |
| NFR-PRIV-01 | Privacy | PII classified, minimised and excluded from logs and prompts. Retention and deletion rules defined. | Recommendation | Privacy impact assessment | Data model |
| NFR-AUD-01 | Auditability | Immutable audit trail of security and business events, with user, time and correlation id, retained 12 months (retention is an assumption). | Assumption | Audit query test | Audit module |
| NFR-OBS-01 | Observability | Structured logs, metrics, traces and a correlation id across all tiers. Alerts are tied to SLOs and each has a runbook. | Recommendation | Alert test | Azure Monitor |
| NFR-MNT-01 | Maintainability | Unit coverage of at least 80% on domain logic. Static analysis gate in CI. Modules are decoupled. | Assumption | CI reports | ADR-S02 |
| NFR-TST-01 | Testability | Automated unit, integration, contract, UI, security and performance tests run in the pipeline. | Recommendation | Pipeline evidence | Test strategy |
| NFR-DEP-01 | Deployability | Immutable, versioned artifacts. Automated smoke tests and rollback. Prod needs human approval. | Recommendation | Release records | CI/CD |
| NFR-PORT-01 | Portability | Containerised workloads, IaC and standards-based interfaces (OIDC, OpenAPI, SQL). | Recommendation | Review | ADR-S01 |
| NFR-ACC-01 | Accessibility | WCAG 2.2 AA. | Recommendation | Automated and manual audit | UI standards |
| NFR-I18N-01 | Localisation | Externalised strings, with locale and time zone support. Languages are TBD (D1). | Assumption | UI tests | UI design |
| NFR-CMP-01 | Compliance | Regime to be confirmed (GDPR, ISO 27001 and others). Controls are mapped once confirmed. | Decision required | Control mapping | Security architecture |
| NFR-COST-01 | Cost / FinOps | Monthly estimate before provisioning. All resources are tagged (owner, application, environment, cost center, lifecycle). Budget alerts are in place. Dev/test auto-shutdown is used where practical. | Recommendation | Cost reports | IaC tags |
| NFR-AI-01 | Responsible AI | Grounding with citations, content safety, prompt-injection defences, per-user data authorisation, human approval for consequential actions, an evaluation set, versioned prompts/models, a full action audit and a kill switch. | Recommendation | Eval runs, red-team tests | ADR-S05 |
| NFR-SUP-01 | Supportability | Runbooks, on-call and an incident process before go-live. Operational readiness checklist signed off. | Recommendation | Readiness review | Support model |
| NFR-DAT-01 | Data quality | Schema migrations are versioned and reversible. Backups are tested by restore. | Recommendation | Restore test | Data architecture |

## Open items

1. D1 and D2 fill in real targets and the compliance regime.
2. Load profile (users, transactions per second) is unknown. NFR-PERF and NFR-SCAL cannot be validated until it exists.
3. Conflicts to resolve: higher availability and shorter RTO raise cost (NFR-COST-01). Tier targets by service criticality once priorities are known.
