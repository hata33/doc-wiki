---
name: ConversationBufferMemory
module: langchain_core
source: concepts/memory.mdx
---

## 描述

ConversationBufferMemory - 缓冲所有对话历史的记忆组件。

## 原始文档

- **主文档**: [`raw/src/oss/concepts/memory.mdx`](..\..\raw\src\oss\concepts\memory.mdx)
- **教程**: https://docs.langchain.com/oss/langchain/memory

## 初始化

```python
from langchain_core.memory import ConversationBufferMemory
memory = ConversationBufferMemory()
```

## 用途

- 多轮对话
- 保持上下文
- Agent 记忆

## 相关页面

- [[Memory]] - 记忆概念
- [[Agent]] - Agent 使用
