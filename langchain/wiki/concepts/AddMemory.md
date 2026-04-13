---
name: AddMemory
category: concepts
source: langgraph/add-memory.mdx
---

## 描述

AddMemory - 基于原始文档的描述

## 原始文档

- **主文档**: [`langgraph/add-memory.mdx`](../../raw/langgraph/add-memory.mdx)

## 关键特性

- * [Trim messages](#trim-messages): Remove first or last N messages (before calling LLM)
- * [Summarize messages](#summarize-messages): Summarize earlier messages in the history and replace them with a summary

## 代码示例

```python
from langgraph.checkpoint.memory import InMemorySaver  # [!code highlight]
from langgraph.graph import StateGraph

checkpointer = InMemorySaver()  # [!code highlight]

builder = StateGraph(...)
graph = builder.compile(checkpointer=checkpointer)  # [!code highlight]

graph.invoke(
    {"messages": [{"role": "user", "content": "hi! i am Bob"}]},
    {"configurable": {"thread_id": "1"}},  # [!code highlight]
)
```

## 相关页面

- 查看原始文档获取更多详细信息
