<<<<<<< HEAD
# Fully Optimized Engineering Project Management

基于 Odoo 17 的智能工程项目管理系统  
涵盖功能包括：

- 项目基础信息管理  
- 任务计划与分解  
- 施工质量与安全追踪  
- AI 智能分析与日志记录  
- 多级项目字典与标准化编码系统

> 当前为开发版，持续完善中...
=======

# 🌐 Fully Optimized Engineering Project Management

[![License: LGPL v3](https://img.shields.io/badge/License-LGPLv3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0.html)
[![Odoo Version](https://img.shields.io/badge/Odoo-17.0-brightgreen.svg)](https://www.odoo.com)
[![GitHub stars](https://img.shields.io/github/stars/Leedefend/Fully_Optimized_Engineering_Project_Management?style=social)](https://github.com/Leedefend/Fully_Optimized_Engineering_Project_Management)
[![Issues](https://img.shields.io/github/issues/Leedefend/Fully_Optimized_Engineering_Project_Management)](https://github.com/Leedefend/Fully_Optimized_Engineering_Project_Management/issues)

一个基于 Odoo 17 的智能工程项目管理系统模块。通过全周期结构化设计、任务模板复用、AI 辅助分析、数据字典管理等功能，助力工程类企业实现数字化转型。

---

## 📋 功能概览

| 功能类别 | 描述 |
|----------|------|
| 📁 项目主数据 | 项目编号、状态、类型、单位、建设内容等基础字段 |
| 🗂 项目阶段 | 可配置的阶段列表（如策划、设计、施工、验收） |
| 🧾 数据字典 | 支持项目状态、结构类型、任务优先级等集中维护 |
| 📊 任务结构 | 模板化任务结构、支持任务依赖、进度跟踪 |
| 🤖 AI 接口 | 预留 DeepSeek 接口进行任务结构生成与分析 |
| 📈 项目计划 | 计划开始/结束时间、目标年份、关键节点 |
| 📦 模块划分 | 成本、质量、安全、计划、任务五大子模块 |
| 🔐 权限机制 | 采用 Odoo 权限体系进行用户行为控制 |
| 📄 报告支持 | 可扩展 PDF/Word 输出（项目立项书、汇报书等） |

---

## 🧱 系统结构

```plaintext
Fully_Optimized_Engineering_Project_Management/
├── models/
├── views/
├── report/
├── static/
├── security/
├── data/
└── __manifest__.py
```

---

## 🖼 截图预览

> 示例截图

- 📌 项目基础表单视图
- 🧭 项目阶段设置表单
- 📚 数据字典管理界面
- 📊 项目计划甘特图（规划中）

---

## 🚀 安装与使用

```bash
git clone https://github.com/Leedefend/Fully_Optimized_Engineering_Project_Management.git
# 放入你的 odoo17/addons/ 目录下
# 重启 Odoo 并在应用中安装模块
```

模块依赖：`project`, `base`, `mail`, `web`, `board`（推荐）

---

## 🧠 项目愿景

本模块不仅是一个工程项目管理工具，更是集成 AI 与智能分析的实验平台，目标构建：

- 通用化工程项目管理体系
- 模块化工程实施结构
- 智能化辅助决策引擎

---

## 🧑‍💻 贡献

欢迎提交 Issue 或 PR，如需深入合作或商业部署支持，请联系作者 [@Leedefend](https://github.com/Leedefend)。

---

## 📜 License

Licensed under the [LGPL-3.0](https://www.gnu.org/licenses/lgpl-3.0.html).

> Made with ❤️ for engineering project evolution.
>>>>>>> 784ad2f (添加增强版模块说明文档)
