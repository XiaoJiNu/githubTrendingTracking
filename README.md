# GitHub Trending 每日追踪

每天自动抓取 [GitHub Trending](https://github.com/trending) Top 20，一句话速览 + 分类索引，帮你 1 分钟掌握当日流行仓库。

## 快速入口

- 📅 每日日报：[`daily/`](./daily) （按日期命名，如 `daily/2026-10-15.md`）
- 🗂 分类索引：[`categories.md`](./categories.md) （按用途归类，找工具直接查这里）

<!-- LATEST:START -->
### 最新一期 · 2026-11-19

- [cursor/plugins](https://github.com/cursor/plugins) — Cursor plugin specification and official plugins
- [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) — "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub:https://clianything.cc/
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) — AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary
- [getarcaneapp/arcane](https://github.com/getarcaneapp/arcane) — Modern Docker Management, Designed for Everyone
- [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) — Multi-tier framework for evaluating AI agent skills and plugins with quality gates, security scanning, harness compatibility checks, semantic overlap detection, synthetic evaluation dataset generation, and live agent evaluation that measures how skills affect agent behavior. Ships reusable CI templates that bring every check to any repository.
- [nvm-sh/nvm](https://github.com/nvm-sh/nvm) — Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions.
- [astral-sh/uv](https://github.com/astral-sh/uv) — An extremely fast Python package and project manager, written in Rust.
- [google-research/paper-orchestra](https://github.com/google-research/paper-orchestra) — PaperOrchestra is a multi-agent framework for automated AI research paper writing.
- [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) — A library of Agent Skills designed to work with the Stitch MCP server. Each skill follows the Agent Skills open standard, for compatibility with coding agents such as Antigravity, Gemini CLI, Claude Code, Cursor.
- [sveltejs/svelte](https://github.com/sveltejs/svelte) — web development for the rest of us

> 完整 Top 19 见 [当日日报](daily/2026-11-19.md)，分类索引见 [categories.md](categories.md)。
<!-- LATEST:END -->

## 内容设计（为什么这样组织）

| 设计 | 目的 |
| --- | --- |
| 每日只取 Top 20 | 控制信息量，避免阅读负担 |
| 每个仓库一句话简介 | 快速判断是否值得深入了解 |
| 按类别分组展示 | 同类项目可横向对比 |
| 分类索引去重（只保留最近上榜） | 索引不随时间膨胀，永远是「能用的清单」 |
| 原始数据存 `data/repos.json` | 便于后续做周报/趋势分析 |

## 分类说明

固定 9 个类别，规则自动归类：

🤖 AI / 机器学习 · 🛠 开发工具 · 🌐 Web 开发 · ⚙️ 系统 / 底层 · 📊 数据 / 爬虫 · 🔒 安全 · 📱 移动开发 · 📚 学习资源 · 📦 其他（兜底）

## 自动化

GitHub Actions 每天北京时间约 9:00（UTC 01:00）自动运行：

1. 抓取 GitHub Trending；
2. 生成当日日报 `daily/YYYY-MM-DD.md`；
3. 更新分类索引与本 README 的「最新一期」区块；
4. 有变化则自动提交，Watch 本仓库即可收到更新通知。

也可在 Actions 页面手动触发 **Daily Trending Update** 立即更新。
