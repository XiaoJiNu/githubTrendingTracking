# GitHub Trending 每日追踪

每天自动抓取 [GitHub Trending](https://github.com/trending) Top 20，一句话速览 + 分类索引，帮你 1 分钟掌握当日流行仓库。

## 快速入口

- 📅 每日日报：[`daily/`](./daily) （按日期命名，如 `daily/2026-10-15.md`）
- 🗂 分类索引：[`categories.md`](./categories.md) （按用途归类，找工具直接查这里）

<!-- LATEST:START -->
### 最新一期 · 2026-10-31

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) — Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
- [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) — Open-source Grok Bot alternative with a virtual machine that bots can use
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable) — The design vocabulary for your coding agent. Steer with polish and bolder, review with critique and audit, catch AI slop before it ships.
- [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) — Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.
- [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) — 紫微斗数开源排盘引擎 — 基于倪海厦《天纪》体系，含完整排盘算法、四化系统、格局知识库、古籍原文数据
- [expo/skills](https://github.com/expo/skills) — A collection of AI agent skills for working with Expo projects and Expo Application Services
- [macro-inc/macro](https://github.com/macro-inc/macro) — Macro is a unified workspace for teams: email, chat, docs, tasks, agents, calls, and CRM — @-linked together with shared AI memory.
- [mattpocock/skills](https://github.com/mattpocock/skills) — Skills for Real Engineers. Straight from my .agents directory.
- [pingdotgg/t3code](https://github.com/pingdotgg/t3code) — （无简介）
- [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) — DeepTutor: Lifelong Personalized Tutoring.https://deeptutor.info/.

> 完整 Top 15 见 [当日日报](daily/2026-10-31.md)，分类索引见 [categories.md](categories.md)。
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
