# PhotoCraft 插件 / 动作大全

> 收录可在 PhotoCraft 中直接使用的插件与动作集（含 Photoshop 原版）。
> A curated collection of plugins and action sets for PhotoCraft (Photoshop originals included).

---

## 简介 / Introduction

**中文**
本仓库收集能在 PhotoCraft 中直接加载、批处理的**动作集（Action Sets）**。每个动作集放在 `actions/<名称>/` 目录下，通常包含：PhotoCraft 原生 JSON、可 GUI 直接加载的 `.atn`、原始 Photoshop 动作（`.atn`），以及使用说明。

**English**
This repo collects **action sets** that run directly in PhotoCraft (load in the GUI or batch via CLI). Each set lives under `actions/<name>/` and usually ships a PhotoCraft-native JSON, a GUI-loadable `.atn`, the original Photoshop action (`.atn`), and a usage note.

---

## 已收录 / Included

### 人像精修（Portrait Retouching）
| 文件 | 说明 / Description |
|---|---|
| `人像精修-actions.json` | PhotoCraft 原生动作集（批处理用）/ native JSON for batch |
| `人像精修-PhotoCraft.atn` | 已移植、GUI 直接加载的版本 / ported, GUI-ready |
| `人像精修-PS原版.atn` | Photoshop 原版动作集 / original Photoshop action |
| `人像精修-批处理.pcdroplet` | 拖拽 / 命令行批处理 / droplet for batch |
| `使用说明.md` | 详细说明与语义差异 / detailed notes |

动作「完美磨皮@无忌视觉」包含 3 处需要人工介入的停止提示（模糊保留纹理、模糊中等瑕疵、画笔修复），GUI 播放时需手动完成；命令行批处理会自动跳过。

---

## 快速开始 / Quick Start

### GUI（PhotoCraft 窗口）
1. 打开 PhotoCraft → **Actions（动作）** 面板 → 菜单 **Load Actions…**
2. 选择 `actions/人像精修/人像精修-PhotoCraft.atn`
3. 打开照片 → 双击动作 **「完美磨皮@无忌视觉」**

### 命令行批处理 / CLI batch
```bat
photocraft-cli batch ^
  --actions "actions/人像精修/人像精修-actions.json" ^
  --action "完美磨皮@无忌视觉" ^
  --in "<图片目录>" --out "<输出目录>" --format psd
```

```bat
photocraft-cli droplet ^
  "actions/人像精修/人像精修-批处理.pcdroplet" "<图片目录>" --out "<输出目录>"
```

---

## 目录结构 / Structure

```
PhotoCraft-Actions/
├── actions/
│   └── 人像精修/
│       ├── 人像精修-actions.json
│       ├── 人像精修-PhotoCraft.atn
│       ├── 人像精修-PS原版.atn
│       ├── 人像精修-批处理.pcdroplet
│       └── 使用说明.md
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

---

## 贡献 / Contributing
欢迎提交新的动作集！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)（中英双语）。
Contributions of new action sets are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) (bilingual).

---

## 许可证 / License
[MIT](LICENSE)
