# GitHub Trending 每日追踪

每天自动抓取 [GitHub Trending](https://github.com/trending) Top 20，一句话速览 + 分类索引，帮你 1 分钟掌握当日流行仓库。

## 快速入口

- 📅 每日日报：[`daily/`](./daily) （按日期命名，如 `daily/2026-10-15.md`）
- 🗂 分类索引：[`categories.md`](./categories.md) （按用途归类，找工具直接查这里）

<!-- LATEST:START -->
### 最新一期 · 2026-11-07

- [zed-industries/zed](https://github.com/zed-industries/zed) — Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.
- [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) — Auto Ontology is a Python framework for building semantic, graph-based reasoning layers over data. It enables deterministic query generation, better context retrieval, and more explainable AI for LLM and agent workflows.
- [rails/rails](https://github.com/rails/rails) — Ruby on Rails
- [mpv-player/mpv](https://github.com/mpv-player/mpv) — 🎥 Command line media player
- [rust-lang/rust](https://github.com/rust-lang/rust) — Empowering everyone to build reliable and efficient software.
- [react/react](https://github.com/react/react) — The library for web and native user interfaces.
- [angular/angular](https://github.com/angular/angular) — Deliver web apps with confidence 🚀
- [symfony/symfony](https://github.com/symfony/symfony) — The Symfony PHP framework
- [prometheus/prometheus](https://github.com/prometheus/prometheus) — The Prometheus monitoring system and time series database.
- [google/skills](https://github.com/google/skills) — Agent Skills for Google products and technologies

> 完整 Top 18 见 [当日日报](daily/2026-11-07.md)，分类索引见 [categories.md](categories.md)。
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
