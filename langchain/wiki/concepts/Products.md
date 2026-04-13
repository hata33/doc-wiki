---
name: Products
category: 架构概念
source: concepts/products.mdx
---

## 描述

LangChain 产品对比 - LangChain（框架）、LangGraph（运行时）、Deep Agents（Harness）的区别和使用场景。

## 原始文档

- **主文档**: [`raw/src/oss/concepts/products.mdx`](..\..\raw\src\oss\concepts\products.mdx)

## 三层架构

| 层级 | 产品 | 价值 | 使用场景 |
|------|------|------|----------|
| **Framework** | [[LangChain]] | 抽象、集成 | 快速开始、团队标准化 |
| **Runtime** | [[LangGraph]] | 持久化、流式、HITL | 长运行、有状态工作流 |
| **Harness** | [[DeepAgents]] | 预定义工具、提示 | 复杂、自主任务 |

## 选择指南

- **简单 Agent**: 使用 [[LangChain]]
- **复杂工作流**: 使用 [[LangGraph]]
- **长期自主任务**: 使用 [[DeepAgents]]

## 相关页面

- [[LangChain]] - Agent 框架
- [[LangGraph]] - 运行时框架
- [[Agent]] - Agent 开发
