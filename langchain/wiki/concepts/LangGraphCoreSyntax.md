---
name: LangGraphCoreSyntax
category: 核心语法
source: langgraph/graph-api.mdx
---

## 描述

LangGraph Graph API 核心语法 - 使用 StateGraph 定义图、节点和边。

## 原始文档

- **主文档**: [`raw/src/oss/langgraph/graph-api.mdx`](../../raw/langgraph/graph-api.mdx)
- **使用指南**: [`raw/src/oss/langgraph/use-graph-api.mdx`](../../raw/langgraph/use-graph-api.mdx)

## 核心概念

### 1. State（状态）
图的共享数据结构，定义输入和输出 schema。

```python
from typing_extensions import TypedDict
from langchain.messages import AnyMessage

class State(TypedDict):
    messages: list[AnyMessage]
    extra_field: int
```

### 2. Nodes（节点）
执行逻辑的函数，接收状态并返回更新。

```python
def my_node(state: State):
    messages = state["messages"]
    new_message = AIMessage("Hello!")
    return {"messages": messages + [new_message], "extra_field": 10}
```

### 3. Edges（边）
控制执行流程，定义节点间的连接。

```python
# 固定边
graph.add_edge("node_a", "node_b")

# 条件边
graph.add_conditional_edges("router", {
    "continue": "node_a",
    "end": END
})
```

## 基本语法

### 创建图

```python
from langgraph.graph import StateGraph, START, END

# 1. 定义状态
class State(TypedDict):
    messages: list[AnyMessage]

# 2. 创建图构建器
builder = StateGraph(State)

# 3. 添加节点
builder.add_node("node_a", node_a_function)
builder.add_node("node_b", node_b_function)

# 4. 添加边
builder.add_edge(START, "node_a")
builder.add_edge("node_a", "node_b")
builder.add_edge("node_b", END)

# 5. 编译
graph = builder.compile()
```

### 执行图

```python
# 调用
result = graph.invoke({"messages": [HumanMessage("Hi")]})

# 流式输出
for chunk in graph.stream({"messages": [HumanMessage("Hi")]}, stream_mode="values"):
    print(chunk)
```

## 高级特性

### 条件路由

```python
def route_function(state: State) -> str:
    if len(state["messages"]) > 5:
        return "continue"
    return "end"

builder.add_conditional_edges("node_a", route_function)
```

### 循环

```python
# 在条件边中返回当前节点名称创建循环
builder.add_conditional_edges("node_b", lambda s: "node_a" if s["count"] < 3 else END)
```

### 并行

```python
# 使用 Send API 并行执行
from langgraph.types import Send

def map_function(state: State) -> list[Send]:
    return [Send("process", {"item": item}) for item in state["items"]]

builder.add_node("map", map_function)
```

## 相关页面

- [[FunctionalAPI]] - 函数式 API
- [[StateSchema]] - 状态模式
- [[Persistence]] - 持久化
