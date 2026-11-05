#!/usr/bin/env python3
"""Generate plain-HTML delivery status (docs/status/index.html) from repo evidence.
Sources: docs/delivery/ROSTER.md, DECISION_LOG.md, RAID_LOG.md, docs/status/status.json, file/git timestamps.
Never invents progress: role status is what the roster says, checked against files that actually exist."""
import html, json, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

def table_rows(path):
    rows = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*-", line):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows[1:] if rows else rows  # drop header

def artifact_paths(cell):
    out = []
    for p in re.findall(r"(?:AgentZ/)?(docs/[\w./-]+\.md)", cell):
        if p not in out:
            out.append(p)
    return out

def last_changed(rel):
    f = ROOT / rel
    try:
        t = subprocess.run(["git", "log", "-1", "--format=%cI", "--", rel], cwd=ROOT,
                           capture_output=True, text=True, timeout=20).stdout.strip()
        if t:
            return t
    except Exception:
        pass
    return datetime.fromtimestamp(f.stat().st_mtime, timezone.utc).isoformat(timespec="seconds")

def count_open(path):
    return sum(1 for r in table_rows(path) if r and r[-1].strip().lower() == "open")

def role_rag(status, missing):
    s = status.lower()
    if missing or s.startswith("blocked"):
        return "Red"
    if s.startswith("not started") or not s:
        return "Grey"
    return "Amber"  # Done drafts are unreviewed and assumption-based; Green needs human acceptance

e = html.escape
REPO = "https://github.com/Zia-CRM-hub/ACN-DU-AgentZia/blob/main/"
cfg = json.loads((DOCS / "status" / "status.json").read_text(encoding="utf-8"))
roles = []
for r in table_rows(DOCS / "delivery" / "ROSTER.md"):
    if len(r) < 4:
        continue
    role, task, status, art = r[:4]
    paths = artifact_paths(art)
    missing = [p for p in paths if not (ROOT / p).exists()]
    present = [p for p in paths if (ROOT / p).exists()]
    updated = max((last_changed(p) for p in present), default="n/a")
    roles.append(dict(role=role, task=task, status=status, rag=role_rag(status, missing or not paths),
                      present=present, missing=missing, updated=updated))

overall = cfg.get("overall_rag", "Amber")
reason = cfg.get("overall_reason", "")
if any(x["rag"] == "Red" for x in roles) and overall != "Red":
    overall, reason = "Red", "Evidence check failed: a role has missing artifacts or is blocked. " + reason
done = sum(1 for x in roles if x["status"].lower().startswith("done"))
open_dec = count_open(DOCS / "delivery" / "DECISION_LOG.md")
open_raid = count_open(DOCS / "delivery" / "RAID_LOG.md")
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
COL = {"Green": "#1a7f37", "Amber": "#b7791f", "Red": "#c0392b", "Grey": "#6b7280"}

def badge(r):
    return f'<span style="background:{COL[r]};color:#fff;padding:2px 10px;border-radius:10px;font-weight:bold">{r}</span>'

rows = []
for x in roles:
    links = "<br>".join(f'<a href="../../{e(p)}">{e(p.split("/",1)[1])}</a>' for p in x["present"]) or "-"
    if x["missing"]:
        links += "<br><b style='color:#c0392b'>MISSING: " + e(", ".join(x["missing"])) + "</b>"
    rows.append(f"<tr><td><b>{e(x['role'])}</b></td><td>{e(x['task'])}</td><td>{e(x['status'])}</td>"
                f"<td>{badge(x['rag'])}</td><td>{links}</td><td>{e(x['updated'])}</td></tr>")

groups = {}
for f in sorted(DOCS.rglob("*.md")):
    rel = f.relative_to(ROOT).as_posix()
    groups.setdefault(rel.split("/")[1], []).append(rel)
rep = "".join(f"<h3>{e(g)}</h3><ul>" + "".join(
    f'<li><a href="{REPO}{e(p)}">{e(p.split("/")[-1])}</a> <span class="muted">({e(last_changed(p)[:16])})</span></li>' for p in ps)
    + "</ul>" for g, ps in groups.items())

page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta http-equiv="refresh" content="3600">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AgentZ Delivery Status</title>
<style>body{{font-family:Segoe UI,Arial,sans-serif;margin:24px;color:#1f2937}}
table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #d1d5db;padding:6px 8px;text-align:left;vertical-align:top;font-size:14px}}
th{{background:#f3f4f6}}.kpi{{display:inline-block;margin:0 24px 12px 0}}.kpi b{{font-size:22px}}.muted{{color:#6b7280;font-size:13px}}</style></head><body>
<h1>AgentZ Delivery Status</h1>
<p><b>Project:</b> {e(cfg.get('project',''))} &nbsp; <b>Customer:</b> {e(cfg.get('customer',''))} &nbsp; <b>Phase:</b> {e(cfg.get('phase',''))}</p>
<p>Overall status: {badge(overall)} &nbsp; {e(reason)}</p>
<div><span class="kpi">Roles reporting done<br><b>{done} / {len(roles)}</b></span>
<span class="kpi">Open decisions<br><b>{open_dec}</b></span>
<span class="kpi">Open RAID items<br><b>{open_raid}</b></span></div>
<h2>Who is working on what</h2>
<table><tr><th>Role (AI agent)</th><th>Task</th><th>Status (self-reported)</th><th>RAG</th><th>Artifacts</th><th>Last changed</th></tr>
{''.join(rows)}</table>
<h2>All project reports</h2>{rep}
<p class="muted">RAG rule: Red = artifact missing or blocked; Amber = delivered as a draft but not yet human-reviewed; Grey = not started. Green requires human acceptance and is never assigned automatically.
Role status is self-reported by each agent in ROSTER.md; artifact existence and timestamps are checked by this script. Status = Done means a draft was written, not that outcomes were achieved.</p>
<p class="muted">Generated {now}. Refreshes hourly. Status config: docs/status/status.json. Updated by: {e(cfg.get('updated_by',''))}.</p>
</body></html>"""
(DOCS / "status" / "index.html").write_text(page, encoding="utf-8")
print(f"Wrote docs/status/index.html ({len(roles)} roles, overall {overall})")
