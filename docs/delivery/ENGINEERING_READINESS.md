# Engineering Readiness

Owner: Full-Stack Engineer. Status: Draft for review. Source: AgentZ/claude.md sections 2, 3, 10, 12, 13, 14.

Labels used: **Confirmed fact**, **Assumption**, **Recommendation**, **Decision required**.

## 1. Current state

- **Confirmed fact:** No application repository is assigned. claude.md project fields (name, customer, stack, repo path, phase, budget) are unfilled placeholders.
- **Confirmed fact:** AgentZ contains only `claude.md`, `.claude/agents/`, and `docs/delivery/ROSTER.md`. There is no source, test, or pipeline code.
- **Assumption:** The stack is Microsoft-first (.NET/ASP.NET Core, TypeScript/React, Azure) per claude.md section 3. It is unconfirmed and applies only until the intake below says otherwise.
- **Decision required (Program Owner):** Provide the repository path or URL, the target cloud, and the current delivery phase.

## 2. Repository intake checklist

Run in order once a repo is assigned. Steps 1 to 7 are read-only. Record the result of each as Confirmed fact with evidence (file path or command output). Do not record "pass" without running the check.

| # | Check | Evidence to capture | Result |
|---|---|---|---|
| 1 | Access: read access is granted and the default branch is identified | Remote URL, default branch, last commit date | Not started |
| 2 | Structure: top-level layout, monorepo or single app | Directory tree to depth 2 | Not started |
| 3 | Docs: README, CONTRIBUTING, existing architecture and deployment docs | File list and gaps | Not started |
| 4 | Languages, frameworks, versions, build tools | Manifests (`*.csproj`, `package.json`, `global.json`, lockfiles) | Not started |
| 5 | Dependencies: outdated, vulnerable, unlicensed or unknown license | SCA output (`dotnet list package --vulnerable`, `npm audit`) | Not started |
| 6 | Secrets: hard-coded credentials, committed `.env`, keys | Secret scan output. Never paste found values into docs. | Not started |
| 7 | CI/CD and IaC: pipelines, Bicep/Terraform, environments, approvals | File list, required checks, branch protection | Not started |
| 8 | Build: clean build on a fresh clone with documented steps | Command and exit code | Not started |
| 9 | Tests: existing test projects run and pass locally | Command, pass/fail/skip counts, coverage if available | Not started |
| 10 | Static analysis and lint: configured and clean or baseline known | Tool output and warning count | Not started |
| 11 | Runtime config: how config and secrets are supplied (Key Vault, env vars) | Config files, redacted | Not started |
| 12 | Observability: logging, tracing, health endpoints | Code and config references | Not started |
| 13 | Data: database, migrations tooling, data classification | Schema or migration folder, classification notes | Not started |
| 14 | Accessibility and i18n: WCAG 2.2 AA tooling, localization approach | Tool config, resource files | Not started |
| 15 | Capability map: map the repo to the business outcome it serves | Short mapping note | Not started |

Intake output: a findings list (security, quality, performance, maintainability) with severity, then a delivery plan. No code changes happen before the plan and the pre-change statement (section 5.1) exist.

Run only in local or approved non-production environments. Ask for approval before any step that touches confidential data not already authorized.

## 3. Proposed layout

**Recommendation.** Adopt this layout, per claude.md section 14, unless the assigned repo already has a working convention. If it does, keep the repo's convention and do not restructure it.

```
/src
  /backend            # ASP.NET Core solution (Api, Application, Domain, Infrastructure)
  /frontend           # TypeScript/React app (or Next.js if SSR is justified)
  /shared             # API contracts (OpenAPI), generated clients
/tests
  /unit               # Fast, no I/O, per layer
  /integration        # Real DB/queue via containers, no shared state
  /contract           # API/consumer contract tests against OpenAPI
  /e2e                # UI flows with accessibility checks (axe)
  /performance        # Load/baseline scripts, run in non-prod only
/scripts              # Repeatable dev tasks (setup, seed, lint)
/pipelines            # CI/CD definitions (GitHub Actions or Azure DevOps)
/infrastructure       # IaC: /modules, /environments, /azure
/monitoring           # Dashboards, alerts as code
/runbooks             # Operational procedures
/docs                 # architecture, decisions, security, testing, delivery ...
```

Conventions:
- Backend follows clean architecture. Dependencies point inward: Domain has no framework references.
- Test projects mirror the source tree (`Orders.Application` maps to `Orders.Application.Tests`).
- Test names state behavior: `Method_Condition_ExpectedResult`.
- Test data is synthetic. No real personal or customer data in fixtures, logs, or samples.
- Each service exposes a health endpoint and emits structured logs with correlation IDs.
- Every major technology choice gets an ADR in `/docs/decisions` (rationale, alternatives, cost, operations, exit strategy).

**Decision required (Technical Architect):** Confirm the stack, or supply an alternative, before scaffolding. Scaffolding itself is out of scope here.

## 4. Coding standards

- Language and style: enforce through `.editorconfig`, analyzers (.NET), and ESLint plus Prettier with TypeScript `strict` on. Formatting is automated and not debated in review.
- Design: SOLID. Use DDD only where domain complexity justifies it. Prefer configuration and reuse over custom code. Add no framework or service without an ADR.
- APIs: API-first with OpenAPI. Use semantic versioning and keep changes backward compatible. A breaking change needs a new version and a deprecation note.
- Errors: fail explicitly and return typed or problem-details responses. Do not swallow exceptions.
- Logging: structured only. Never log secrets, tokens, or personal data.
- Security: validate all input. Parameterize queries. Apply authorization checks server-side. Use managed identities and Key Vault, with no secrets in code, config, or history. Align to OWASP ASVS and the Top 10.
- Accessibility: WCAG 2.2 AA for all UI. Automated axe checks run in CI, and manual keyboard and screen-reader checks are recorded for new flows.
- Dependencies: pin versions, commit lockfiles, review licenses, and keep updates small and separate from feature work.
- Feature flags: use them for risky or incomplete user-facing changes.
- AI features, if any: grounding and citations, content safety, prompt-injection defenses, human approval for consequential actions, versioned prompts and models, and an audit trail with a kill switch.

## 5. Pull request standards

### 5.1 Before changing code (record in the PR or the plan)
Requirement understanding, files likely to change, architecture impact, security impact, test approach, assumptions, risks.

### 5.2 PR rules
- Small and reversible: one logical change per PR. Aim for fewer than about 400 changed lines excluding generated files. Larger work is split.
- Branching: short-lived branches from the default branch, named `feat/`, `fix/`, `chore/`, `docs/` plus a work item ID.
- Commits: imperative mood, with the reason in the body when it is not obvious.
- Tests: new or changed behavior ships with tests in the same PR. A bug fix starts with a failing regression test.
- Docs: update the README, API spec, ADR, or runbook affected by the change.
- Review: at least one reviewer who is not the author. The author does not approve their own PR. Security-sensitive changes (auth, crypto, data access, infra) need a second reviewer.
- Required status checks (protected branch): build, unit tests, lint and static analysis, SCA, secret scan. Add integration, contract, UI/accessibility, container and IaC validation as the pipeline matures.
- No merge on red checks. Skipped or disabled tests need a linked issue.
- Rollback: each PR states how to revert. Schema changes use backward-compatible, expand-then-contract migrations.

### 5.3 PR description template

```
## Summary and business outcome
## Changes (files, behavior)
## Architecture / security impact
## Tests added and commands run (with actual results)
## Known limitations
## Rollback approach
## Linked work item / ADR
```

### 5.4 Change report after a code change (claude.md section 13)
Files changed, behavior implemented, tests added, commands executed, results, known limitations, security considerations, rollback approach, recommended next action. Report a test as passed only if it was run and succeeded.

## 6. Definition of Done

- Acceptance criteria met and traced to a requirement and a business outcome.
- Tests added and passing in CI, with evidence linked.
- Static analysis, SCA, and secret scan are clean, or each exception is recorded in the RAID log.
- Accessibility checked for UI changes.
- Logs, metrics, and health checks are present for new components.
- Documentation updated. Rollback verified in a non-production environment where applicable.
- No production deployment without human approval.

## 7. Approval gates

The engineer does not do the following without explicit human approval. Prepare an approval request with the action, reason, benefit, cost, risk, rollback, validation, and approver.

- Production deployment or production database migration.
- Deleting or replacing resources, or changing identity, access, or network security controls.
- Purchasing cloud services or licenses, or creating cost beyond the approved threshold.
- Accessing confidential data not already authorized.
- Any external communication or irreversible change.

## 8. Open items

| # | Item | Type | Owner |
|---|---|---|---|
| 1 | Assign the application repository (path or URL, access) | Decision required | Program Owner |
| 2 | Confirm stack, cloud, and CI platform (GitHub Actions or Azure DevOps) | Decision required | Technical Architect |
| 3 | Confirm compliance and data classification requirements | Decision required | Security Architect |
| 4 | Approved cost threshold for non-production cloud use | Decision required | Program Owner |
| 5 | Run the section 2 checklist and publish findings | Next action | Full-Stack Engineer |
