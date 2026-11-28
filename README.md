# GitHub Trending 每日追踪

每天自动抓取 [GitHub Trending](https://github.com/trending) Top 20，一句话速览 + 分类索引，帮你 1 分钟掌握当日流行仓库。

## 快速入口

- 📅 每日日报：[`daily/`](./daily) （按日期命名，如 `daily/2026-10-15.md`）
- 🗂 分类索引：[`categories.md`](./categories.md) （按用途归类，找工具直接查这里）

<!-- LATEST:START -->
### 最新一期 · 2026-11-28

- [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) — A Claude Code skill bundle for bug hunting and external red-team work - 85 skills, 16 slash commands, 681 disclosed-report patterns curated across 24 core vulnerability classes, plus enterprise identity + infrastructure attack matrices.
- [obra/superpowers](https://github.com/obra/superpowers) — An agentic skills framework & software development methodology that works.
- [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) — "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub:https://clianything.cc/
- [jingyaogong/minimind](https://github.com/jingyaogong/minimind) — 🧠 两小时从 0 训出你的 64M 大模型。Train your own 64M LLM from scratch in 2 hours.
- [cursor/plugins](https://github.com/cursor/plugins) — Cursor plugin specification and official plugins
- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) — Knowledge infrastructure to make your agents smarter. Search, scrape and access 550+ data providers through one API.
- [nginx/nginx](https://github.com/nginx/nginx) — The official NGINX Open Source repository.
- [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) — OpenVINO™ is an open source toolkit for optimizing and deploying AI inference
- [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) — Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, Qoder, and Pi. 52 diagram types. Self-contained HTML + SVG. No shadows. No Mermaid slop.
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) — AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

> 完整 Top 16 见 [当日日报](daily/2026-11-28.md)，分类索引见 [categories.md](categories.md)。
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
