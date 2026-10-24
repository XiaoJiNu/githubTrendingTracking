# GitHub Trending 每日追踪

每天自动抓取 [GitHub Trending](https://github.com/trending) Top 20，一句话速览 + 分类索引，帮你 1 分钟掌握当日流行仓库。

## 快速入口

- 📅 每日日报：[`daily/`](./daily) （按日期命名，如 `daily/2026-10-15.md`）
- 🗂 分类索引：[`categories.md`](./categories.md) （按用途归类，找工具直接查这里）

<!-- LATEST:START -->
### 最新一期 · 2026-10-24

- [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) — A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings
- [php/php-src](https://github.com/php/php-src) — The PHP Interpreter
- [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) — Open source repository of plugins primarily intended for knowledge workers to use in Claude Cowork
- [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) — OpenShell is the safe, private runtime for autonomous AI agents.
- [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) — 紫微斗数开源排盘引擎 — 基于倪海厦《天纪》体系，含完整排盘算法、四化系统、格局知识库、古籍原文数据
- [SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red) — claude-red is a curated library of offensive security skills designed for the Claude skills system. Each skill is a structured SKILL.md file that primes Claude with expert-level methodology for a specific attack surface — from SQLi to shellcode, EDR evasion to exploit development.
- [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) — VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-Life Cloning
- [nodejs/node](https://github.com/nodejs/node) — Node.js JavaScript runtime ✨🐢🚀✨

> 完整 Top 8 见 [当日日报](daily/2026-10-24.md)，分类索引见 [categories.md](categories.md)。
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
