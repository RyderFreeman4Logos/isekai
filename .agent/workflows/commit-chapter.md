---
description: 在完成新章节后更新世界观并提交
---

# Commit Chapter Workflow

此工作流用于在 `dev` 分支完成一章内容的撰写后，依据变更内容更新世界观数据库，并准备合并到 `main`。

## 1. 检查变更
运行以下命令查看当前工作区的变更（包括未提交和未跟踪的文件）：
```bash
git status chapters/
git diff chapters/
```
// turbo
请仔细阅读上述命令的输出，分析新章节的剧情、新登场人物、新设定或已有角色的状态变化。

## 2. 更新世界观数据库
基于 diff 分析结果，更新 `docs/` 下的相关文件：

### A. 全局剧情记录 (必须)
- **更新 `docs/timeline.md`**: 在文件末尾upsert新章节的记录。
    - 格式：
      ```markdown
      ## {章节编号}_{章节名}
      *   **地点**: ...
      *   **关键事件**: ...
      *   **伏笔/状态变更**: ...
      ```
    - *目的*: 确保剧情逻辑连贯，防止吃书。

### B. 设定词条 (按需)
- **更新经历**: 在 `docs/names/角色/*.md` 或 `docs/names/组织/*.md` 中添加最新的经历或状态变更。
- **新建词条**: 如果有新角色或新势力登场，创建新的 `.md` 文件。
- **消歧义**: 修正任何因剧情发展而产生的设定冲突。

## 3. 提交世界观更新
完成数据库修改后，进行提交：
```bash
git add docs/names/
git commit -m "docs: sync world settings for latest chapter"
```

## 4. (用户操作) 最终确认与合并
通知用户检查上述提交。用户满意后，将自行执行 `git branch -f main HEAD` 完成发布。
