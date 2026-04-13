---
name: LangGraphStreaming
category: concepts
source: langgraph/streaming.mdx
---

## 描述

LangGraphStreaming - 基于原始文档的描述

## 原始文档

- **主文档**: [`langgraph/streaming.mdx`](../../raw/langgraph/streaming.mdx)

## 关键特性

- * `message_chunk`: the token or message segment from the LLM.
- * `metadata`: a dictionary containing details about the graph node and LLM invocation.
- * `message_chunk`: the token or message segment from the LLM.
- * `metadata`: a dictionary containing details about the graph node and LLM invocation.

## 代码示例

```python
for chunk in graph.stream(
    {"topic": "ice cream"},
    stream_mode=["updates", "custom"],  # [!code highlight]
    version="v2",  # [!code highlight]
):
    if chunk["type"] == "updates":
        for node_name, state in chunk["data"].items():
            print(f"Node {node_name} updated: {state}")
    elif chunk["type"] == "custom":
        print(f"Status: {chunk['data']['status']}")
```

## 相关页面

- 查看原始文档获取更多详细信息
