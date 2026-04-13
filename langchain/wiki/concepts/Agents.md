---
name: Agents
category: concepts
source: langchain/agents.mdx
---

## 描述

Agents - 基于原始文档的描述

## 原始文档

- **主文档**: [`langchain/agents.mdx`](../../raw/langchain/agents.mdx)

## 关键特性

- * **Reasoning**: "Popularity is time-sensitive, I need to use the provided search tool."
- * **Acting**: Call `search_products("wireless headphones")`
- * **Reasoning**: "I need to confirm availability for the top-ranked item before answering."
- * **Acting**: Call `check_inventory("WH-1000XM5")`
- * **Reasoning**: "I have the most popular model and its stock status. I can now answer the user's question."

## 代码示例

```python
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse


basic_model = ChatOpenAI(model="gpt-4.1-mini")
advanced_model = ChatOpenAI(model="gpt-4.1")

@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model based on conversation complexity."""
    message_count = len(request.state["messages"])

    if message_count > 10:
        # Use an advanced model for longer conversations
```

## 相关页面

- 查看原始文档获取更多详细信息
