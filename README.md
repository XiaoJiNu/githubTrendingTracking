# GitHub Trending 每日追踪

每天自动抓取 [GitHub Trending](https://github.com/trending) Top 20，一句话速览 + 分类索引，帮你 1 分钟掌握当日流行仓库。

## 快速入口

- 📅 每日日报：[`daily/`](./daily) （按日期命名，如 `daily/2026-10-15.md`）
- 🗂 分类索引：[`categories.md`](./categories.md) （按用途归类，找工具直接查这里）

<!-- LATEST:START -->
### 最新一期 · 2026-11-05

- [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) — Auto Ontology is a Python framework for building semantic, graph-based reasoning layers over data. It enables deterministic query generation, better context retrieval, and more explainable AI for LLM and agent workflows.
- [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) — Worktrunk is a CLI for Git worktree management, designed for parallel AI agent workflows
- [mattpocock/skills](https://github.com/mattpocock/skills) — Skills for Real Engineers. Straight from my .agents directory.
- [floci-io/floci](https://github.com/floci-io/floci) — Light, fluffy, and always free - The AWS Local Emulator alternative
- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) — Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) — Computer use CLI for AI agents
- [github/spec-kit](https://github.com/github/spec-kit) — 💫 Toolkit to help you get started with SDD or any other process!
- [The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent) — 🚀 PR Agent: The Original Open-Source PR Reviewer. This project is not the Qodo free tier.
- [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) — 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow.
- [garrytan/gstack](https://github.com/garrytan/gstack) — Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

> 完整 Top 16 见 [当日日报](daily/2026-11-05.md)，分类索引见 [categories.md](categories.md)。
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
