---
name: Context
category: 核心概念
source: concepts/context.mdx
---

## 描述

Context Engineering - 为 AI 应用提供正确信息和工具的动态系统构建实践。

## 原始文档

- **主文档**: [`raw/src/oss/concepts/context.mdx`](..\..\raw\src\oss\concepts\context.mdx)

## 上下文类型

| 类型 | 可变性 | 生命周期 | 访问方式 |
|------|--------|----------|----------|
| **Static Runtime** | 静态 | 单次运行 | `context` 参数 |
| **Dynamic Runtime (State)** | 动态 | 单次运行 | LangGraph State |
| **Cross-conversation (Store)** | 动态 | 跨会话 | LangGraph Store |

## 核心用途

- 依赖注入（数据库连接、API 客户端）
- 用户元数据传递
- 对话历史管理
- 长期记忆存储

## 相关页面

- [[Memory]] - 记忆管理
- [[Agent]] - Agent 中的上下文
