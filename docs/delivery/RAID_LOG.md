# RAID Log

Owner: PMO Analyst (AI). Created 2026-11-05. Status of log: initial baseline, not reviewed by a human.
Labels: Confirmed fact / Assumption / Recommendation / Decision required.

## Risks

| ID | Risk | Label | Likelihood | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|
| R-01 | Project fields in claude.md section 1 are all unfilled placeholders, so scope, outcomes, budget and timeline cannot be baselined. | Confirmed fact | High | High | Obtain sponsor inputs (see D-01). Work limited to safe, reversible planning meanwhile. | Delivery Lead (proposed) | Open |
| R-02 | No approved budget or commercial model, so cost and margin cannot be tracked or forecast. | Confirmed fact | High | High | Request budget and commercial model from sponsor. | Finance (proposed) | Open |
| R-03 | No named human sponsor or approver, so approval gates in claude.md section 12 have no addressee. | Confirmed fact | High | High | Nominate approver(s) (see D-02). | Sponsor (TBC) | Open |
| R-04 | Team is all-AI. Outputs may contain unverified content. No human review has occurred. | Assumption | Medium | High | Human review of all artifacts before use or external release. | PMO Analyst | Open |
| R-05 | Git status shows many tracked files deleted in the working tree (.github, docs, mobile, scripts) in the parent repo, plus untracked folders. Possible unintended data loss or reorganisation. | Confirmed fact (git status snapshot); cause unknown | Medium | Medium | Human to confirm intent before any commit. PMO has not modified or restored them. | Repo owner (TBC) | Open |
| R-06 | AgentZ folder content is untracked, so planning artifacts are not version-controlled. | Confirmed fact | Medium | Medium | Commit after human approval. | Repo owner (TBC) | Open |

## Assumptions

| ID | Assumption | Label | Validation needed |
|---|---|---|---|
| A-01 | AgentZ is a new delivery workspace with no existing product code, and no delivery has started. Only claude.md, agent definitions and an empty ROSTER.md were found in AgentZ. | Assumption (based on file inspection) | Sponsor confirms scope and repo path. |
| A-02 | Current phase is Discovery / Mobilization (pre-baseline). | Assumption | Sponsor confirms. |
| A-03 | No production systems, customer data or spend are involved yet. | Assumption | Sponsor confirms. |

## Issues

| ID | Issue | Label | Impact | Action | Owner | Status |
|---|---|---|---|---|---|---|
| I-01 | Charter inputs missing (project name, customer, outcomes, timeline, budget, team size, cloud). | Confirmed fact | Blocks baselining, RAG, finance tracking. | Sponsor to supply; see D-01. | Sponsor (TBC) | Open |
| I-02 | Only ROSTER.md existed in docs/delivery. No charter, plan, WBS or milestones exist to report against. | Confirmed fact | Status reporting has no baseline. | Create charter and plan once inputs arrive. | Delivery Lead (proposed) | Open |

## Dependencies

| ID | Dependency | Needed from | Needed by | Status |
|---|---|---|---|---|
| DEP-01 | Completed project fields (claude.md section 1) | Sponsor | Before baselining | Not received |
| DEP-02 | Named human approver(s) | Sponsor | Before any approval-gated action | Not received |
| DEP-03 | Budget and commercial model | Sponsor / Finance | Before cost tracking | Not received |
