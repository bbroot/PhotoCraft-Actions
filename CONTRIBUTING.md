# 贡献指南 / Contributing

## 中文
1. Fork 本仓库并创建你的分支 (`git checkout -b feature/your-feature`)。
2. 新增插件请继承 `photocraft.core.Plugin` 并用 `@register` 注册。
3. 新增动作请放在 `actions/` 目录，使用 JSON 声明式格式。
4. 确保所有说明保持中英双语。
5. 提交 PR，描述你的改动。

## English
1. Fork the repo and create your branch (`git checkout -b feature/your-feature`).
2. New plugins should subclass `photocraft.core.Plugin` and use the `@register` decorator.
3. New actions live in `actions/` as declarative JSON.
4. Keep all docs bilingual (Chinese + English).
5. Open a PR describing your changes.
