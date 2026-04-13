---
name: ShortTermMemory
category: 核心概念
source: langchain/short-term-memory.mdx
---

## 描述

Short-term Memory - 单个对话线程内的记忆系统，记住之前的交互。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/short-term-memory.mdx`](..\..\raw\src\oss\langchain\short-term-memory.mdx)

## 核心概念

- **Thread**: 组织单个会话中的多个交互
- **对话历史**: 最常见的短期记忆形式
- **状态持久化**: 使用 checkpointer 保存到数据库

## 使用方法

```python
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    "gpt-5",
    tools=[get_user_info],
    checkpointer=InMemorySaver(),
)

agent.invoke(
    {"messages": [{"role": "user", "content": "Hi! My name is Bob."}]},
    {"configurable": {"thread_id": "1"}},
)
```

## 生产环境

使用数据库支持的 checkpointer：
- PostgreSQL
- Redis
- SQLite

## 相关页面

- [[Memory]] - 记忆概述
- [[ConversationBufferMemory]] - 缓冲记忆
