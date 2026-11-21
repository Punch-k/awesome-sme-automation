"""
Builds README.md from catalog.json + data/notes.json, with live GitHub data for every entry.

    python scripts/build.py            # refresh GitHub data and rewrite README.md
    GITHUB_TOKEN=... python scripts/build.py   (higher API rate limit; set automatically in Actions)

A tool stays in the main list only while it meets the "ready to use" bar: the repository exists,
is not archived and has had a commit in the last 180 days. Anything else moves to "Needs attention".
"""

import datetime as dt
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STALE_DAYS = 180


def gh(repo):
    headers = {"User-Agent": "awesome-sme-automation", "Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    try:
        with urllib.request.urlopen(urllib.request.Request(f"https://api.github.com/repos/{repo}", headers=headers), timeout=30) as r:
            d = json.load(r)
        return {"repo": d["full_name"], "stars": d["stargazers_count"], "license": (d.get("license") or {}).get("spdx_id"),
                "pushed": d["pushed_at"][:10], "archived": d["archived"], "homepage": d.get("homepage") or f"https://github.com/{repo}"}
    except Exception as e:  # noqa: BLE001
        return {"repo": repo, "error": str(e)}


def stars(n):
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


def lic(x):
    return "check terms" if x in (None, "NOASSERTION", "NONE") else x


def cell(t):
    return str(t).replace("|", "/").replace("\n", " ")


def main():
    cat = json.load(open(os.path.join(ROOT, "catalog.json"), encoding="utf-8"))
    notes = json.load(open(os.path.join(ROOT, "data", "notes.json"), encoding="utf-8"))
    today = dt.date.today()
    cache_path = os.path.join(ROOT, "data", "github.json")
    cache = json.load(open(cache_path, encoding="utf-8")) if os.path.exists(cache_path) else {}
    live, ok, attention = {}, [], []
    for t in cat["tools"] + cat["libraries"]:
        m = gh(t["repo"])
        if "error" in m and t["repo"] in cache:   # keep-last-good: a failed check (e.g. rate limit) reuses the last verified data
            m = dict(cache[t["repo"]], cached=True)
        live[t["repo"]] = m
        if "error" in m:
            attention.append((t, "could not be checked: " + m["error"][:60]))
            continue
        age = (today - dt.date.fromisoformat(m["pushed"])).days
        if m["archived"]:
            attention.append((t, "repository archived"))
        elif age > STALE_DAYS:
            attention.append((t, f"no commits for {age} days"))
        elif t in cat["tools"]:
            ok.append(t)
    json.dump(live, open(os.path.join(ROOT, "data", "github.json"), "w", encoding="utf-8"), indent=1)

    by_repo = {t["repo"]: t for t in cat["tools"]}
    name = lambda r: by_repo.get(r, {}).get("name", r.split("/")[-1])
    link = lambda t: f"[{t['name']}]({live[t['repo']].get('homepage') or 'https://github.com/' + t['repo']})"
    L = []
    L.append("""# Awesome SME Automation

**Open-source software a small or mid-size business can install and run today, organised by the business process it automates.**
Each entry is a complete product (not a code snippet or a one-off template) and is re-checked against GitHub every week.

**Who it is for:** owners, operations managers and consultants who want to replace manual work or per-seat SaaS fees with
software they control. **What you get per tool:** what it runs end to end, a concrete SME use case, advantages, watch-outs,
licence and live activity.

## Contents

""")
    for c in cat["categories"]:
        n = sum(1 for t in ok if t["cat"] == c["id"])
        L.append(f"- [{c['name']}](#{c['name'].lower().replace(',', '').replace(' ', '-')}) ({n})\n")
    L.append("- [Starter stacks](#starter-stacks)\n- [Workflow template libraries](#workflow-template-libraries)\n- [How tools are chosen](#how-tools-are-chosen)\n\n")

    L.append(f"""## What "ready to use" means here

Every tool listed:
1. is a **complete, self-hostable product** with documented installation (most also offer a hosted plan);
2. is **actively maintained**: a commit within the last {STALE_DAYS} days, and the repository is not archived;
3. has its **licence shown**. "check terms" means the project uses a source-available, fair-code or custom licence: free to use for
   your own business in most cases, with limits on reselling or hosting it for others. Read it before you build a product on top.

The **Status** column shows licence, GitHub stars, month of the last commit, and **AI** where the tool has built-in AI features. It is refreshed automatically every week by `scripts/build.py`.

""")
    for c in cat["categories"]:
        tools = [t for t in ok if t["cat"] == c["id"]]
        if not tools:
            continue
        L.append(f"## {c['name']}\n\n{c['why']}\n\n")
        L.append("| Tool | Use case | Advantages | Disadvantages | Replaces | Status |\n")
        L.append("|---|---|---|---|---|---|\n")
        for t in sorted(tools, key=lambda x: -live[x["repo"]]["stars"]):
            m, n = live[t["repo"]], notes.get(t["repo"], {})
            status = f"{lic(m['license'])}<br>★ {stars(m['stars'])}<br>{m['pushed'][:7]}" + ("<br>**AI**" if t["ai"] else "")
            L.append("| " + " | ".join([
                f"**{link(t)}**<br>{cell(t['runs'])}", cell(n.get("use", "")),
                "<br>".join("+ " + cell(p) for p in n.get("pros", [])),
                "<br>".join("− " + cell(p) for p in n.get("cons", [])),
                cell(t["replaces"]), status,
            ]) + " |\n")
        L.append("\n")

    L.append("## Starter stacks\n\nProven combinations of the tools above, by business need. Each runs on one small server.\n\n")
    L.append("| Stack | For | Tools | How it fits together |\n|---|---|---|---|\n")
    for s in cat["stacks"]:
        L.append(f"| **{s['name']}** | {cell(s['for'])} | {', '.join(name(r) for r in s['tools'])} | {cell(s['flow'])} |\n")
    L.append("\n")

    L.append("## Workflow template libraries\n\nReady-to-import n8n workflows. Useful starting points, but templates are not tested here and quality varies: "
             "check each one, and its licence and source, before using it with real data. n8n's official gallery is at [n8n.io/workflows](https://n8n.io/workflows).\n\n")
    L.append("| Library | What it is | Licence | Stars | Updated |\n|---|---|---|---|---|\n")
    for lb in cat["libraries"]:
        m = live[lb["repo"]]
        if "error" in m:
            continue
        L.append(f"| [{lb['name']}](https://github.com/{lb['repo']}) | {cell(lb['note'])} | {lic(m['license'])} | {stars(m['stars'])} | {m['pushed']} |\n")
    L.append("\n")

    if attention:
        L.append("## Needs attention\n\nThese no longer meet the ready-to-use bar and are excluded from the lists above until they do.\n\n| Project | Reason |\n|---|---|\n")
        for t, why in attention:
            L.append(f"| [{t['name']}](https://github.com/{t['repo']}) | {why} |\n")
        L.append("\n")

    L.append(f"""## How tools are chosen

- Complete products a business can run, not libraries or demos.
- Self-hostable, so you can keep your data, with a documented install.
- Maintained (see the bar above) and with a visible licence.
- Advantages and disadvantages are written for an SME decision-maker: cost, setup effort, lock-in and licence limits.
- Excluded on {today.isoformat()}: Flowise (repository archived), Automatisch (no recent commits).

**Contributing:** add an entry to `catalog.json` and `data/notes.json`, run `python scripts/build.py`, and open a pull request.
Include a real use case and at least one honest disadvantage.

**Disclaimer:** descriptions are a starting point, not a recommendation for your situation. Check licences, security and
compliance (for example payroll or e-signature rules in your country) before going live.

---
Last refreshed: {today.isoformat()} · {len(ok)} tools · Maintained by [Prapanch Kokkalemada](https://punch-k.github.io/Portfolio/)
""")
    open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8").write("".join(L))
    print(f"README.md: {len(ok)} tools listed, {len(attention)} need attention")


if __name__ == "__main__":
    sys.exit(main())
