# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一部硬核科幻/伪奇幻异世界小说的创作仓库。核心设定：异世界是军方使用外星科技构建的超算模拟虚拟现实，魔法本质是算力配额。主角因其特殊的世界认知（理解世界是程序/虚拟现实），在"魔法表现形式取决于信仰/认知"的法则下能够利用漏洞执行指针操作，但他并非管理员。

## 常用命令

```bash
# 构建小说TXT并提交
just txt-gen

# 重命名设定中的术语/名称（自动更新所有文件引用）
just rename <old> <new>
```

## 目录结构

- `chapters/` - 正文章节，命名格式：`{n:08}_第{n}章 {章节名}.md`
- `docs/` - 世界观设定库
  - `docs/names/角色/` - 角色设定卡
  - `docs/names/组织/` - 组织/国家设定
  - `docs/names/物种/` - 种族设定
  - `docs/timeline.md` - 剧情时间线（核心文件，记录每章事件）
- `.agent/rules/` - AI Agent 永久生效规则
- `.agent/workflows/` - 工作流程指南
- `export/` - 导出的纯文本小说

## 核心工作流

### 新会话初始化

1. 读取 `.agent/rules/writing_style.md`（写作风格）
2. 读取 `docs/timeline.md`（剧情进度）
3. 读取 `docs/01-world-md-原始设定集.md`（底层设定）
4. 找到 `chapters/` 中编号最大的章节，确认断章位置

### 完成章节后

1. 运行 `git status chapters/` 和 `git diff chapters/` 检查变更
2. 更新 `docs/timeline.md`（必须）
3. 按需更新 `docs/names/` 下的角色/设定卡
4. 提交世界观更新：`git add docs/ && git commit -m "docs: sync world settings"`

## 写作规范

- **基调**: 理性的荒诞感，硬科幻逻辑审视奇幻世界
- **章节长度**: 2000-5000字
- **禁止**: 中二病喊招式名、谜语人、过度术语堆砌
- **正文格式**: 不使用 H1/H2 标题，段落间空一行
- **断章原则**: 勾引不恶心，每章有完整小事件闭环后再留悬念

## 重要规则

- 修改 `chapters/` 或 `docs/` 前必须先出 implementation plan（中文）
- 编辑文件时不使用 gemini-mcp
- 在 `dev` 分支工作，用户手动合并到 `main`
