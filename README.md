# GitHub Trending 每日追踪

每天自动抓取 [GitHub Trending](https://github.com/trending) Top 20，一句话速览 + 分类索引，帮你 1 分钟掌握当日流行仓库。

## 快速入口

- 📅 每日日报：[`daily/`](./daily) （按日期命名，如 `daily/2026-10-15.md`）
- 🗂 分类索引：[`categories.md`](./categories.md) （按用途归类，找工具直接查这里）

<!-- LATEST:START -->
### 最新一期 · 2026-10-25

- [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) — A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings
- [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) — OpenShell is the safe, private runtime for autonomous AI agents.
- [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) — Official, AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS
- [Nutlope/hallmark](https://github.com/Nutlope/hallmark) — Anti-AI-slop design skill for Claude Code, Cursor, and Codex.
- [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) — A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value.
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable) — The design language that makes your AI harness better at design.
- [pollen-robotics/microduck](https://github.com/pollen-robotics/microduck) — A Tiny biped duck robot 🦆
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) — An open-source AI agent that brings the power of Gemini directly into your terminal.
- [jbiaojerry/ebook-treasure-chest](https://github.com/jbiaojerry/ebook-treasure-chest) — 欢迎来到电子书下载宝库，一个汇聚了各类电子书下载链接的地方。无论你是喜欢阅读经典文学、经管励志、终身学习、职场创业、技术手册还是其他类型的书籍，这里都能满足你的需求。 该库涵盖了帆书app(原樊登读书)、微信读书、京东读书、喜马拉雅等读书app的大部分电子书。
- [makecindy/cindy](https://github.com/makecindy/cindy) — Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI Agent。

> 完整 Top 10 见 [当日日报](daily/2026-10-25.md)，分类索引见 [categories.md](categories.md)。
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
