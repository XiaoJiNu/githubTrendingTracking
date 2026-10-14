#!/usr/bin/env python3
"""抓取 GitHub Trending，生成每日日报、分类索引，并更新 README 最新区块。"""

import json
import os
import re
from datetime import datetime, timedelta, timezone

import requests
from bs4 import BeautifulSoup

TOP_N = 20
CST = timezone(timedelta(hours=8))
TODAY = datetime.now(CST).strftime("%Y-%m-%d")

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}

# 固定分类：按关键词规则归类，保证长期稳定可比
CATEGORIES = [
    ("AI / 机器学习", ["ai", "llm", "gpt", "agent", "rag", "model", "diffusion",
                    "transformer", "neural", "machine learning", "deep learning",
                    "inference", "embedding", "prompt", "mcp", "finetune", "训练"]),
    ("开发工具", ["cli", "git", "editor", "ide", "linter", "formatter", "debug",
                "docker", "kubernetes", "devops", "ci/cd", "build tool", "terminal",
                "package manager", "code review", "编译", "命令行"]),
    ("Web 开发", ["react", "vue", "svelte", "next", "nuxt", "css", "html", "web",
                "frontend", "javascript", "typescript", "node", "ui component",
                "tailwind", "前端", "组件"]),
    ("系统 / 底层", ["kernel", "os", "rust", "database", "storage", "network",
                  "proxy", "engine", "compiler", "runtime", "embed", "驱动", "内核"]),
    ("数据 / 爬虫", ["scrap", "crawl", "etl", "sql", "dataframe", "pipeline",
                  "analytics", "dataset", "数据", "爬虫"]),
    ("安全", ["security", "vulnerab", "pentest", "ctf", "malware", "exploit",
            "fuzz", "encrypt", "安全", "漏洞"]),
    ("移动开发", ["android", "ios", "flutter", "swift", "kotlin", "react native"]),
    ("学习资源", ["awesome", "tutorial", "course", "interview", "book", "roadmap",
                "cheatsheet", "教程", "学习", "面试", "指南"]),
]
DEFAULT_CATEGORY = "其他"

EMOJI = {"AI / 机器学习": "🤖", "开发工具": "🛠", "Web 开发": "🌐",
         "系统 / 底层": "⚙️", "数据 / 爬虫": "📊", "安全": "🔒",
         "移动开发": "📱", "学习资源": "📚", "其他": "📦"}


def classify(text: str) -> str:
    t = text.lower()
    for name, keywords in CATEGORIES:
        if any(k in t for k in keywords):
            return name
    return DEFAULT_CATEGORY


def fetch_trending():
    resp = requests.get("https://github.com/trending", headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    repos = []
    for row in soup.select("article.Box-row")[:TOP_N]:
        a = row.select_one("h2 a")
        full_name = "/".join(a.get_text(strip=True).split())
        url = "https://github.com" + a["href"]
        desc_tag = row.select_one("p")
        desc = desc_tag.get_text(strip=True) if desc_tag else "（无简介）"
        lang_tag = row.select_one('[itemprop="programmingLanguage"]')
        lang = lang_tag.get_text(strip=True) if lang_tag else ""
        stars_tag = row.select_one('a[href$="/stargazers"]')
        stars = stars_tag.get_text(strip=True) if stars_tag else ""
        today_tag = row.select_one("span.d-inline-block.float-sm-right")
        today_stars = today_tag.get_text(strip=True) if today_tag else ""
        text = f"{full_name} {desc} {lang}"
        repos.append({
            "name": full_name, "url": url, "desc": desc, "lang": lang,
            "stars": stars, "today_stars": today_stars, "category": classify(text),
            "date": TODAY,
        })
    return repos


def render_daily(repos):
    lines = [f"# GitHub Trending 日报 · {TODAY}", "",
             f"> Top {len(repos)} 一句话速览。分类总索引见 [categories.md](../categories.md)", ""]
    grouped = {}
    for r in repos:
        grouped.setdefault(r["category"], []).append(r)
    order = [c for c, _ in CATEGORIES] + [DEFAULT_CATEGORY]
    for cat in order:
        if cat not in grouped:
            continue
        lines.append(f"## {EMOJI[cat]} {cat}")
        lines.append("")
        for i, r in enumerate(grouped[cat], 1):
            meta = " · ".join(x for x in [r["stars"] and f"⭐ {r['stars']}",
                                          r["today_stars"], r["lang"]] if x)
            lines.append(f"{i}. [{r['name']}]({r['url']})　{meta}")
            lines.append(f"   {r['desc']}")
        lines.append("")
    return "\n".join(lines)


def load_store():
    if os.path.exists("data/repos.json"):
        with open("data/repos.json", encoding="utf-8") as f:
            return json.load(f)
    return {}


def update_store(store, repos):
    for r in repos:  # 同名仓库覆盖旧记录：索引只保留最近一次上榜
        store[r["name"]] = r
    return store


def render_categories(store):
    lines = ["# 分类索引", "",
             "> 按用途归类，同一仓库只保留最近一次上榜记录，点击日期可回到当日日报。", ""]
    order = [c for c, _ in CATEGORIES] + [DEFAULT_CATEGORY]
    for cat in order:
        items = [r for r in store.values() if r["category"] == cat]
        if not items:
            continue
        items.sort(key=lambda r: r["date"], reverse=True)
        lines.append(f"## {EMOJI[cat]} {cat}（{len(items)}）")
        lines.append("")
        lines.append("| 仓库 | 一句话简介 | 上榜日期 |")
        lines.append("| --- | --- | --- |")
        for r in items:
            desc = r["desc"].replace("|", "\\|")
            if len(desc) > 60:
                desc = desc[:60] + "…"
            lines.append(f"| [{r['name']}]({r['url']}) | {desc} | [{r['date']}](daily/{r['date']}.md) |")
        lines.append("")
    return "\n".join(lines)


def render_readme_section(repos):
    lines = [f"### 最新一期 · {TODAY}", ""]
    for r in repos[:10]:
        lines.append(f"- [{r['name']}]({r['url']}) — {r['desc']}")
    lines += ["", f"> 完整 Top {len(repos)} 见 [当日日报](daily/{TODAY}.md)，分类索引见 [categories.md](categories.md)。"]
    return "\n".join(lines)


def update_readme(section):
    with open("README.md", encoding="utf-8") as f:
        content = f.read()
    pattern = r"<!-- LATEST:START -->.*?<!-- LATEST:END -->"
    replacement = f"<!-- LATEST:START -->\n{section}\n<!-- LATEST:END -->"
    new_content, n = re.subn(pattern, replacement, content, flags=re.S)
    if n == 0:
        new_content = content + "\n" + replacement + "\n"
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    repos = fetch_trending()
    if not repos:
        raise SystemExit("未抓取到任何仓库，跳过本次更新")

    os.makedirs("daily", exist_ok=True)
    os.makedirs("data", exist_ok=True)

    with open(f"daily/{TODAY}.md", "w", encoding="utf-8") as f:
        f.write(render_daily(repos))

    store = update_store(load_store(), repos)
    with open("data/repos.json", "w", encoding="utf-8") as f:
        json.dump(store, f, ensure_ascii=False, indent=2)

    with open("categories.md", "w", encoding="utf-8") as f:
        f.write(render_categories(store))

    update_readme(render_readme_section(repos))
    print(f"已生成 {TODAY} 日报，共 {len(repos)} 个仓库")


if __name__ == "__main__":
    main()
