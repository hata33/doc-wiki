---
name: BuiltInMiddleware
category: concepts
source: langchain/middleware/built-in.mdx
---

## 描述

BuiltInMiddleware - 基于原始文档的描述

## 原始文档

- **主文档**: [`langchain/middleware/built-in.mdx`](../../raw/langchain/middleware/built-in.mdx)

## 关键特性

- - `fraction` (float): Fraction of model's context size (0-1)
- - `tokens` (int): Absolute token count
- - `messages` (int): Message count
- - `fraction` (float): Fraction of model's context size to keep (0-1)
- - `tokens` (int): Absolute token count to keep

## 代码示例

```python
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware

agent = create_agent(
    model="gpt-4.1",
    tools=[your_weather_tool, your_calculator_tool],
    middleware=[
        SummarizationMiddleware(
            model="gpt-4.1-mini",
            trigger=("tokens", 4000),
            keep=("messages", 20),
        ),
    ],
)
```

## 相关页面

- 查看原始文档获取更多详细信息
