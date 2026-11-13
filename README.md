# GitHub Trending 每日追踪

每天自动抓取 [GitHub Trending](https://github.com/trending) Top 20，一句话速览 + 分类索引，帮你 1 分钟掌握当日流行仓库。

## 快速入口

- 📅 每日日报：[`daily/`](./daily) （按日期命名，如 `daily/2026-10-15.md`）
- 🗂 分类索引：[`categories.md`](./categories.md) （按用途归类，找工具直接查这里）

<!-- LATEST:START -->
### 最新一期 · 2026-11-13

- [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) — Keep your coding agent up to date with the latest web best practices
- [openai/codex-security](https://github.com/openai/codex-security) — OpenAI's Codex Security CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities. npm:https://www.npmjs.com/package/@openai/codex-security
- [nvm-sh/nvm](https://github.com/nvm-sh/nvm) — Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions.
- [pookjw/HermesEnabler](https://github.com/pookjw/HermesEnabler) — Enable Hermès Watch Faces on any Apple Watch devices
- [we-promise/sure](https://github.com/we-promise/sure) — The personal finance app for everyone (by everyone)
- [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) — An open-source AI coding agent that lives in your terminal.
- [ashhart/TensorFold](https://github.com/ashhart/TensorFold) — LLM Inference Engine for Metal, CUDA and Vulkan.
- [nodejs/node](https://github.com/nodejs/node) — Node.js JavaScript runtime ✨🐢🚀✨
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — Production-grade engineering skills for AI coding agents.
- [meta/astryx](https://github.com/meta/astryx) — An open source design system that's fully customizable and agent ready

> 完整 Top 13 见 [当日日报](daily/2026-11-13.md)，分类索引见 [categories.md](categories.md)。
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
