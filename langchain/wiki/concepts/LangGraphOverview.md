---
name: LangGraph
category: 框架概述
source: langgraph/overview.mdx
---

## 描述

LangGraph - 低级编排框架和运行时，用于构建、管理和部署长运行、有状态的 Agent。

## 原始文档

- **主文档**: [`raw/src/oss/langgraph/overview.mdx`](..\..\raw\src\oss\langgraph\overview.mdx)

## 核心能力

- ✅ **持久化执行** - 故障恢复、长时间运行
- ✅ **人机协作** - 检查和修改 Agent 状态
- ✅ **全面记忆** - 短期和长期记忆
- ✅ **生产就绪** - 可扩展部署

## 安装

```bash
pip install langgraph
```

## Hello World

```python
from langgraph.graph import StateGraph, MessagesState, START, END

def mock_llm(state: MessagesState):
    return {"messages": [{"role": "ai", "content": "hello world"}]}

graph = StateGraph(MessagesState)
graph.add_node(mock_llm)
graph.add_edge(START, "mock_llm")
graph.add_edge("mock_llm", END)
graph = graph.compile()

graph.invoke({"messages": [{"role": "user", "content": "hi!"}]})
```

## 相关页面

- [[LangChain]] - 高层框架
- [[Memory]] - 记忆管理
- [[Streaming]] - 流式输出
