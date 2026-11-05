# Test Strategy

Owner: QA and Automation Engineer | Status: Draft v0.1 | Date: 2026-11-05

Labels used: **[Fact]** Confirmed fact, **[Assumption]**, **[Recommendation]**, **[Decision required]**, **[Forecast]**.

## 1. Current State

- [Fact] AgentZ contains only `claude.md`, 12 agent definitions under `.claude/agents/`, and `docs/delivery/ROSTER.md`. No `/src`, `/tests`, `/pipelines`, build files or CI config exist in AgentZ.
- [Fact] All project fields in `claude.md` section 1 (project, customer, stack, timeline, budget, compliance, phase) are unfilled placeholders.
- [Fact] No tests have been written or executed. This document reports **no test results**, and no pass rates, coverage or defect metrics exist.
- [Fact] The git status shows `../mobile`, `../docs`, `../.github/workflows/ci.yml` and `../scripts/demo.py` as deleted in the parent repo. They are outside AgentZ and are not assessed here. [Decision required] Confirm whether they are in scope.

## 2. Assumptions (reversible; revise when project fields are filled)

1. [Assumption] The stack is a Microsoft full-stack (TypeScript/React front end, .NET or Node back end, REST APIs, Azure), following `claude.md` section 3.
2. [Assumption] There are four environments: dev, test, staging and prod. Testing is limited to local and non-production environments.
3. [Assumption] Accessibility target is WCAG 2.2 AA. Security baseline is OWASP Top 10 and ASVS.
4. [Assumption] If AI features are built, they follow the responsible-AI controls in `claude.md` section 11.

## 3. Objectives and Quality Goals

| Goal | Measure | Target | Status |
|---|---|---|---|
| Defects caught before release | Defect escape rate | [Decision required] set with Delivery Lead | No baseline |
| Requirements traceability | % of requirements with at least one linked test | 100% of must-have | No requirements exist yet |
| Automation | % of regression suite automated | [Recommendation] at least 80% | No baseline |
| Release gate | Open Sev1/Sev2 defects | 0 Sev1, 0 Sev2 at go-live | No baseline |

Targets are proposals. They are not measured values.

## 4. Test Levels and Automation Plan

| Level | Scope | Tooling [Recommendation] | Run when | Owner |
|---|---|---|---|---|
| Unit | Functions, components, domain logic | xUnit/NUnit or Jest/Vitest | Every commit/PR | Fullstack Engineer |
| Static and SCA | Lint, SAST, dependency, secret scan | CodeQL/Semgrep, Dependabot, gitleaks | Every PR | DevOps/Security |
| Integration | Service-to-database/queue, internal APIs | Testcontainers or equivalent | Every PR | Fullstack Engineer + QA |
| Contract | API consumer/provider, OpenAPI conformance | Pact or schema validation | Every PR | QA |
| UI/E2E | Critical user journeys | Playwright | Merge to main, nightly | QA |
| Accessibility | WCAG 2.2 AA | axe-core in Playwright plus manual screen-reader pass | Nightly, release | QA |
| Performance | Load, stress, soak against NFRs | k6 or Azure Load Testing | Pre-release, in non-prod only | QA + SRE |
| Security | DAST, authz tests, ASVS checks; pen test | OWASP ZAP; external pen test is a separate approval | Pre-release | Security Architect |
| Infrastructure | IaC validation, policy-as-code | `terraform validate`/`bicep build`, OPA/Azure Policy | Every PR touching IaC | Cloud/DevOps |
| Smoke | Post-deploy health check | Scripted Playwright/HTTP checks | Every deployment | QA + SRE |
| UAT | Business acceptance | Manual, scripted scenarios | Before release | Product Owner |
| AI evaluation (if applicable) | Grounding, hallucination, prompt injection, content safety, bias | Evaluation datasets with versioned prompts/models | Every prompt/model change | Data/AI Engineer + QA |

Test pyramid: most tests at unit level, fewer at integration, fewest at UI. [Recommendation]

## 5. Entry and Exit Criteria

**Entry (per test cycle):** build passes in CI; requirements and acceptance criteria are approved; the test environment is available and uses synthetic or authorised data only.

**Exit / release gate [Recommendation]:**
- All must-have acceptance criteria are executed, with results recorded.
- 0 open Sev1 or Sev2 defects. Sev3 items have an accepted waiver.
- 0 critical or high unresolved security findings. Any waiver needs the Security Architect and a business-owner risk acceptance.
- No P0 regression failures.
- Performance meets NFR thresholds, once the NFRs exist.
- UAT sign-off recorded by the Product Owner.

## 6. Test Data and Environments

- Use synthetic or anonymised data only. Never put PII, credentials or regulated data in fixtures, logs or prompts.
- Secrets come from a secrets store or CI variables, never from test code.
- Tests must not write to production. Load and security tests run only in approved non-production environments.
- Test data is reset or recreated per run, so tests stay repeatable.

## 7. Defect Management

| Severity | Definition | Target response [Assumption] |
|---|---|---|
| Sev1 | Outage, data loss, or security breach path | Same day |
| Sev2 | Major function broken, no workaround | Before release |
| Sev3 | Function impaired, workaround exists | Prioritised in backlog |
| Sev4 | Cosmetic | Backlog |

Each defect records the linked requirement, environment, build, reproduction steps and evidence. Metrics tracked: defect density, escape rate, mean time to fix, reopen rate.

## 8. Traceability

Requirement -> design -> test case -> execution result -> defect -> business outcome. Maintained in `docs/testing/TRACEABILITY.md` once `docs/requirements/REQUIREMENTS.md` exists. [Recommendation] Tag tests with requirement IDs.

## 9. CI/CD Integration (aligned to claude.md section 10)

Required status checks on PRs: build, unit, static analysis, SCA, secret scan, integration, contract. Merge/nightly: UI, accessibility, container scan. Pre-release: performance and DAST. Post-deploy: smoke, with automated rollback on failed health indicators. Test evidence (reports, logs) is stored as pipeline artifacts. No pipeline exists yet. [Decision required] CI platform: GitHub Actions or Azure DevOps.

## 10. Metrics and Reporting

| KPI | Baseline | Target | Current | Evidence |
|---|---|---|---|---|
| Tests executed / passed | None | n/a | **No tests executed** | None |
| Automated test coverage | None | [Decision required] | Not measured | None |
| Defect escape rate | None | [Decision required] | Not measured | None |
| Flaky test rate | None | under 2% [Recommendation] | Not measured | None |

Report only values produced by an executed run, with the command, build and date.

## 11. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Project context and requirements unfilled | Test scope and targets cannot be finalised | Fill `claude.md` section 1; obtain requirements |
| No source or pipeline yet | Automation cannot begin | Build the framework skeleton once the stack is chosen |
| No non-production environment defined | E2E, performance and security tests are blocked | Environment strategy from Cloud/DevOps |
| NFRs not defined | Performance and availability tests lack pass criteria | Business Analyst and Solution Architect to supply NFRs |

## 12. Decisions and Next Actions

1. [Decision required] Confirm the tech stack and CI platform (Delivery Lead, Solution Architect).
2. [Decision required] Confirm quality targets in section 3 (Delivery Lead, Product Owner).
3. [Recommendation] Create `/tests` and `/pipelines` skeletons after the stack decision. This is safe and reversible.
4. [Recommendation] Draft requirement-tagged acceptance tests once `REQUIREMENTS.md` exists.
5. Approval needed before: pen test or any external security tool spend, paid load-testing services, and any test run against shared or production environments. Each request must give the action, reason, benefit, cost, risk, rollback, validation and approver.
