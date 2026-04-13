---
name: Memory
category: 架构概念
source: concepts/memory.mdx
---

## 描述

Memory - 为 LLM 对话提供记忆功能，使模型能够记住之前的对话内容。

## 原始文档

- **主文档**: [`raw/src/oss/concepts/memory.mdx`](..\..\raw\src\oss\concepts\memory.mdx)
- **教程**: https://docs.langchain.com/oss/langchain/memory

## 类型

- **ConversationBufferMemory** - 缓冲所有对话
- **ConversationBufferWindowMemory** - 只保留最近 N 轮
- **ConversationSummaryMemory** - 总结历史对话

## 用途

- 多轮对话
- 上下文保持
- 长对话管理

## 相关页面

- [[Agent]] - Agent 中的记忆
- [[ChatOpenAI]] - 聊天模型
