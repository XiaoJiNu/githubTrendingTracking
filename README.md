# GitHub Trending 每日追踪

每天自动抓取 [GitHub Trending](https://github.com/trending) Top 20，一句话速览 + 分类索引，帮你 1 分钟掌握当日流行仓库。

## 快速入口

- 📅 每日日报：[`daily/`](./daily) （按日期命名，如 `daily/2026-10-15.md`）
- 🗂 分类索引：[`categories.md`](./categories.md) （按用途归类，找工具直接查这里）

<!-- LATEST:START -->
### 最新一期 · 2026-11-10

- [anthropics/skills](https://github.com/anthropics/skills) — Public repository for Agent Skills
- [meta/astryx](https://github.com/meta/astryx) — An open source design system that's fully customizable and agent ready
- [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) — Hunt down social media accounts by username across social networks
- [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) — Multi-Joint dynamics with Contact. A general purpose physics simulator.
- [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) — A collection of projects designed to help developers quickly get started with building deployable applications using the Claude API
- [garrytan/gbrain](https://github.com/garrytan/gbrain) — Garry's Opinionated OpenClaw/Hermes Agent Brain
- [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) — Browser automation CLI for AI agents
- [ruvnet/RuView](https://github.com/ruvnet/RuView) — π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection — all without a single pixel of video.
- [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) — LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs.
- [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) — Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants.

> 完整 Top 11 见 [当日日报](daily/2026-11-10.md)，分类索引见 [categories.md](categories.md)。
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
