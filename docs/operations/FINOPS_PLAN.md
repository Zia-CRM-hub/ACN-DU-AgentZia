# FinOps Plan

Owner: Cloud, DevOps and SRE Engineer. Status: Draft. No cloud spend has been incurred or approved.

Labels: [Fact], [Calc], [Forecast], [Assumption], [Rec], [Decision].

## 1. Evidence base

- [Fact] Approved budget, cost threshold, commercial model, and cloud are unfilled in `claude.md`.
- [Fact] No billing data, subscriptions, or usage exist for this project. Actual cost is 0 and unmeasured.
- Estimates below are rough order-of-magnitude [Forecast] built on the reference architecture in CLOUD_ARCHITECTURE.md, using assumed list prices that are **not verified** against the current Azure price list. Re-price with the Azure Pricing Calculator before any approval request. They must not be quoted externally.

## 2. Indicative monthly cost model (USD, Forecast, assumptions A1 to A5)

| Component | Dev | Test | Staging | Prod | Basis (assumed) |
|---|---|---|---|---|---|
| Container Apps (API + worker) | 5 | 10 | 40 | 150 | Scale-to-zero non-prod, min 2 replicas prod |
| Database (small SKU, zone-redundant in prod) | 15 | 15 | 60 | 250 | Basic/General Purpose small |
| Front Door + WAF | 0 | 0 | 40 | 60 | Shared non-prod, standard tier |
| Key Vault, Storage, registry | 5 | 5 | 10 | 20 | Light usage |
| Monitoring (Log Analytics, App Insights) | 10 | 10 | 20 | 80 | Ingest-driven. Cap with daily quota |
| Backup / DR storage | 0 | 0 | 5 | 40 | GRS backup |
| Defender for Cloud (basic plans) | 0 | 0 | 15 | 40 | Per-resource plans |
| **Subtotal** | **35** | **40** | **190** | **640** | [Calc] column sums |
| Contingency 20% | 7 | 8 | 38 | 128 | [Assumption] |
| **Total per env** | **42** | **48** | **228** | **768** | [Calc] |

[Calc] Total monthly across all environments = 42 + 48 + 228 + 768 = **1,086 USD**, so about 13,000 USD per year. Range: -40% to +100% given the lack of a workload definition. Optional items excluded: API Management, Redis, Service Bus, firewall, Sentinel (each could add tens to hundreds of USD per month).

Payback and ROI cannot be calculated: no benefit baseline or business case exists (claude.md section 8 formulas apply once they do).

## 3. Governance and allocation

- Mandatory tags: `owner`, `application`, `environment`, `cost-center`, `lifecycle` (enforced by Policy). Untagged spend is reported weekly.
- One subscription (or resource group set) per environment group enables direct cost separation.
- Showback by `cost-center`. Chargeback is [Decision].
- Cloud cost is tracked as its own line in the Financial Tracker, split into dev/test and run costs, and flagged separately from licence and tooling cost.

## 4. Budgets, alerts, and thresholds

| Control | Proposal |
|---|---|
| Budget per environment | Equal to the table totals above, once approved [Decision] |
| Alert thresholds | 50%, 80%, 100% actual, and 100% forecast |
| Anomaly detection | Azure Cost Management anomaly alerts to the owner |
| Approval threshold | Spend above the approved threshold needs approval (value is **unknown**, [Decision]) |
| Hard stop | Non-prod auto-shutdown or scale-to-zero when budget is exceeded. Prod is never auto-stopped |

## 5. Optimization levers

| Lever | Expected effect | Confidence | Timing |
|---|---|---|---|
| Scale-to-zero and auto-shutdown for dev/test (off-hours, weekends: about 128 of 168 h off [Calc: 168 - 40 = 128, 76%]) | Up to about 70% off compute for non-prod [Forecast] | Medium | From day one |
| Right-sizing after 2 to 4 weeks of metrics | 10 to 30% on compute/DB [Forecast] | Low until data exists | After first load test |
| Reserved capacity / savings plan (1 year) for stable prod DB and compute | Roughly 20 to 40% on covered items [Forecast, unverified] | Medium | Only after 3 months of stable usage. Needs purchase approval |
| Log ingestion control (sampling, drop debug, daily cap, archive tier) | Prevents the most common surprise cost | High | Design time |
| Storage lifecycle rules, retention limits | Small | High | Design time |
| Delete orphaned disks, IPs, old images | Small | High | Monthly review |
| Dev/test pricing offers | Possible discount | Unknown | [Decision] check eligibility |

All stated savings are **estimated opportunities** and are not realized savings. They must not be reported as benefits until measured against a baseline.

## 6. Operating cadence

| Cadence | Activity | Owner |
|---|---|---|
| Daily | Anomaly alert review | SRE |
| Weekly | Cost vs budget, untagged resources, idle resources | Cloud Engineer, Finance |
| Monthly | Forecast refresh, optimisation backlog, commitment review | Cloud Engineer, Finance, Delivery Lead |
| Per release | Cost impact noted in the release evidence | DevOps |
| Quarterly | Architecture cost review (e.g. serverless vs reserved) | Architects |

## 7. KPIs

| KPI | Baseline | Target | Current | Evidence |
|---|---|---|---|---|
| Monthly cloud cost vs budget | None | Within 5% | Not measured | Cost Management export |
| Tagged spend % | None | At least 98% | Not measured | Policy compliance |
| Non-prod idle hours | None | Under 25% of hours running outside working hours | Not measured | Utilisation metrics |
| Unit cost (cost per active user or per 1,000 requests) | None | Defined after launch | Not measured | Cost + usage data |
| Forecast accuracy | None | Within 10% | Not measured | Monthly review |

## 8. Approval request (prepared, not submitted)

| Field | Content |
|---|---|
| Action | Approve non-prod cloud budget and subscription creation for dev and test |
| Reason | Needed to run the pipeline and validate IaC |
| Benefit | Enables first deployable increment and early cost data |
| Cost | About 90 USD per month incl. contingency (dev 42 + test 48) [Forecast, unverified pricing] |
| Risk | Cost overrun from unmonitored resources. Mitigated by budgets, alerts and auto-shutdown |
| Rollback | Delete the non-prod resource groups (deletion itself needs approval), and stop spend within 24 h |
| Validation | Budget alerts firing in test, cost visible by tag after 7 days |
| Approver | Customer sponsor / budget owner. Provider Finance Manager for the provider-funded portion |

Production cost approval is deferred until a workload, SLOs and a business case are agreed.

## 9. Decisions and inputs required

1. Approved budget and approval threshold.
2. Who funds cloud (customer pass-through vs included in the commercial model)? This affects provider margin.
3. Cloud and region (affects price).
4. Expected user and traffic volumes for sizing.
5. Existing enterprise agreement or discounts.
