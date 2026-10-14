# GitHub Trending 每日追踪

每天自动抓取 [GitHub Trending](https://github.com/trending) Top 20，一句话速览 + 分类索引，帮你 1 分钟掌握当日流行仓库。

## 快速入口

- 📅 每日日报：[`daily/`](./daily) （按日期命名，如 `daily/2026-10-15.md`）
- 🗂 分类索引：[`categories.md`](./categories.md) （按用途归类，找工具直接查这里）

<!-- LATEST:START -->
### 最新一期 · 2026-10-15

- [morluto/rea](https://github.com/morluto/rea) — 用 Agent 逆向一切：从应用行为到原生二进制
- [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) — 开源、全本地的 ElevenLabs 替代品：声音克隆、配音、听写、转录，支持 646 种语言
- [mksglu/context-mode](https://github.com/mksglu/context-mode) — AI 编程 Agent 的上下文窗口优化：工具输出沙箱化（减少 98%）、会话记忆持久化，通过 MCP 覆盖 17 个平台
- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) — 把任意 AI Agent 变成 AI 科学家：177 个验证过的技能 + 100+ 科学数据库
- [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) — CLI-Anything：让所有软件都能被 Agent 原生操作
- [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) — 独立审计 AI Agent：120 秒内回答「Agent 是否在做该做的事」
- [nvm-sh/nvm](https://github.com/nvm-sh/nvm) — Node 版本管理器：POSIX 兼容的 bash 脚本，管理多个 Node.js 版本
- [rust-lang/rust](https://github.com/rust-lang/rust) — Rust 语言主仓库：让每个人都能构建可靠、高效的软件
- [ntdevlabs/tiny11builder](https://github.com/ntdevlabs/tiny11builder) — WinUI 应用，用于构建精简、定制化的 Windows 11 镜像
- [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) — 全自动 AI Agent 系统，可执行复杂的渗透测试任务

> 完整 Top 12 见 [当日日报](daily/2026-10-15.md)，分类索引见 [categories.md](categories.md)。
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
