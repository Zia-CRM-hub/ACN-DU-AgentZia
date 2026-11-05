# AgentZ: Distribution and Engagement Guide

AgentZ is an AI delivery unit of 12 role agents (`.claude/agents/`) governed by `claude.md`.
This guide covers using it on a real engagement, publishing the status page, and adding it to Microsoft Teams.

## 1. Start an engagement
1. Copy this repo (or use it as a template) per engagement.
2. Fill every `[PLACEHOLDER]` in `claude.md` section 1. Without this, all outputs stay assumption-based.
3. Edit `docs/status/status.json`: project, customer, phase, overall RAG and reason.
4. Name human sponsor and approvers (DECISION_LOG D-02). Agents prepare approval requests; they do not send email, deploy or spend.
5. Run the agents with Claude Code (each file in `.claude/agents/` is a role). Each agent appends its line to `docs/delivery/ROSTER.md`.

Important: approval gates are currently written instructions, not technical enforcement (see `docs/security/SECURITY_ARCHITECTURE.md`). Add Claude Code permissions/hooks before using real data or credentials.

## 2. Hourly plain-HTML status
- Generate now: `python scripts/generate_status.py` produces `docs/status/index.html` (no JavaScript, auto-refreshes hourly).
- It shows who is working on what, RAG per role, artifacts with last-changed time, open decisions, open RAID items and overall status.
- RAG is evidence-based: Green is never assigned automatically. Role "Done" means a draft was written, not that outcomes were achieved.
- Hourly automation: `.github/workflows/hourly-status.yml` regenerates and commits every hour (GitHub Actions cron can lag a few minutes). Windows alternative:
  `schtasks /create /sc hourly /tn AgentZStatus /tr "python <path>\scripts\generate_status.py"`
- Note: the page reflects what agents wrote to the roster. Agents only work when run, so the page cannot show live work between runs.

## 3. Publish the page (needed for Teams)
Teams tabs need an https URL. Enable GitHub Pages (Settings > Pages > main branch, root). The manifest assumes
`https://zia-crm-hub.github.io/ACN-DU-AgentZia/docs/status/index.html`. Pages on a private repo needs a plan that supports it.
The page exposes project status to anyone with the URL on public Pages: do not publish confidential engagement data this way. For confidential work, host on an internal site (Azure Static Web Apps with Entra ID auth) and change `contentUrl` and `validDomains` in `teams/manifest.json`.

## 4. Add to Microsoft Teams
1. `python scripts/build_teams_package.py` builds `dist/AgentZ-Teams.zip` (manifest, color and outline icons).
2. Teams > Apps > Manage your apps > Upload an app > Upload a custom app. Sideloading must be allowed by your tenant admin.
3. For org-wide distribution, the Teams admin uploads it in the Teams admin center (Manage apps > Upload new app) and sets a permission policy.
4. Before org distribution: replace the app `id` GUID if you want a unique one, and set real privacy and terms URLs in the manifest. Bump `version` on each change.

The app is a read-only personal tab. It has no bot, so it cannot post messages to channels and sends nothing. A channel notification bot would be a separate build and needs approval.

## 5. Not yet verified
The Teams package was built and zip-tested locally but not uploaded to a tenant or validated in the Teams Developer Portal. The hourly workflow has not yet run on GitHub.
