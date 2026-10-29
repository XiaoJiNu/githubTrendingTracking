# GitHub Trending 每日追踪

每天自动抓取 [GitHub Trending](https://github.com/trending) Top 20，一句话速览 + 分类索引，帮你 1 分钟掌握当日流行仓库。

## 快速入口

- 📅 每日日报：[`daily/`](./daily) （按日期命名，如 `daily/2026-10-15.md`）
- 🗂 分类索引：[`categories.md`](./categories.md) （按用途归类，找工具直接查这里）

<!-- LATEST:START -->
### 最新一期 · 2026-10-29

- [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail) — Vibe code with pi in a lightweight, real IDE that customises itself around the way you work — The Vibe You Need
- [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) — （无简介）
- [obra/superpowers](https://github.com/obra/superpowers) — An agentic skills framework & software development methodology that works.
- [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) — DeepTutor: Lifelong Personalized Tutoring.https://deeptutor.info/.
- [macro-inc/macro](https://github.com/macro-inc/macro) — Macro is a unified workspace for teams: email, chat, docs, tasks, agents, calls, and CRM — @-linked together with shared AI memory.
- [Nutlope/hallmark](https://github.com/Nutlope/hallmark) — Anti-AI-slop design skill for Claude Code, Cursor, and Codex.
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable) — The design vocabulary for your coding agent. Steer with polish and bolder, review with critique and audit, catch AI slop before it ships.
- [makecindy/cindy](https://github.com/makecindy/cindy) — Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。
- [nightly-labs/openbot](https://github.com/nightly-labs/openbot) — A local-first desktop workspace for persistent AI teammates. Run Codex, Claude, and Grok with dedicated workspaces, task queues, file sharing, browser control, and agent-to-agent collaboration.
- [togg53192-cmd/jailbreaks](https://github.com/togg53192-cmd/jailbreaks) — LIST OF ALL MY JAILBREAKS

> 完整 Top 14 见 [当日日报](daily/2026-10-29.md)，分类索引见 [categories.md](categories.md)。
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
