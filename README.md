# PhotoCraft

> 轻量、可扩展的图片处理插件与动作库。
> A lightweight, extensible photo-processing plugin & action library.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 简介 / Introduction

**中文**
PhotoCraft 是一套用于自动化图片处理的**插件（Plugin）**与**动作（Action）**集合。
你可以用声明式的动作文件（JSON）组合多个图像处理步骤，也可以通过编写插件轻松扩展新能力。
它基于 Python 与 [Pillow](https://python-pillow.org/) 构建，跨平台、零配置即可上手。

**English**
PhotoCraft is a collection of **plugins** and **actions** for automating image-processing tasks.
Compose multiple processing steps with declarative action files (JSON), or extend capabilities easily by writing your own plugins.
Built on Python and [Pillow](https://python-pillow.org/), it is cross-platform and works out of the box.

---

## 特性 / Features

- **声明式动作 / Declarative actions** — 用 JSON 描述处理流水线，无需写代码。
- **可扩展插件 / Extensible plugins** — 继承 `Plugin` 基类即可注册新算子。
- **内置算子 / Built-in operators** — 灰度、缩放、水印等常用动作开箱即用。
- **跨平台 / Cross-platform** — 纯 Python 实现，Windows / macOS / Linux 通用。
- **中英文档 / Bilingual docs** — 本仓库所有说明均提供中英双语。

---

## 快速开始 / Quick Start

### 安装 / Install

```bash
pip install photocraft
# 或本地开发 / or for local development:
git clone https://github.com/<your-username>/PhotoCraft.git
cd PhotoCraft
pip install -e .
```

### 使用 / Usage

```python
from PIL import Image
from photocraft.core import load_action, run_action

img = Image.open("input.jpg")
action = load_action("actions/grayscale.json")
result = run_action(img, action)
result.save("output.png")
```

通过命令行 / Via CLI:

```bash
python -m photocraft run actions/resize.json input.jpg output.png
```

---

## 动作示例 / Example Action

`actions/resize.json`

```json
{
  "name": "resize-to-512",
  "description": "Resize image to 512x512",
  "steps": [
    { "plugin": "resize", "params": { "width": 512, "height": 512 } }
  ]
}
```

---

## 目录结构 / Project Structure

```
PhotoCraft/
├── photocraft/          # 核心库 / core library
│   ├── core.py          # 动作运行器与插件基类 / runner & plugin base
│   └── plugins/         # 内置插件 / built-in plugins
├── actions/             # 示例动作（JSON）/ example actions
├── examples/            # 使用示例 / usage examples
├── README.md            # 中英双语介绍 / bilingual intro
├── LICENSE              # MIT
└── pyproject.toml
```

---

## 贡献 / Contributing

欢迎提交 Issue 与 PR！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)（中英双语）。
Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) (bilingual).

---

## 许可证 / License

[MIT](LICENSE) © PhotoCraft
