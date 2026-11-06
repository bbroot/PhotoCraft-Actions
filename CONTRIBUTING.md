# 贡献指南 / Contributing

## 中文
1. Fork 本仓库并创建分支（`git checkout -b add/your-action-set`）。
2. 在 `actions/` 下新建目录，目录名即动作集名称（建议英文或拼音）。
3. 放入以下文件：
   - `<名称>-actions.json`：PhotoCraft 原生动作集（批处理用）
   - `<名称>-PhotoCraft.atn`：可 GUI 加载的移植版本
   - `<名称>-PS原版.atn`：（可选）Photoshop 原版动作
   - `使用说明.md`：步骤、语义差异、使用方式
4. 在 `manifest.json` 的 `actionSets` 中登记该集合。
5. 确保所有说明保持中英双语，提交 PR。

## English
1. Fork and branch (`git checkout -b add/your-action-set`).
2. Create a folder under `actions/` named after the set.
3. Add these files:
   - `<name>-actions.json`: PhotoCraft-native action set (for batch)
   - `<name>-PhotoCraft.atn`: GUI-loadable ported version
   - `<name>-PS原版.atn`: (optional) original Photoshop action
   - `使用说明.md`: steps, semantic diffs, usage
4. Register the set in `manifest.json` under `actionSets`.
5. Keep docs bilingual (Chinese + English) and open a PR.
