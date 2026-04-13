---
name: LangChain
category: 框架概述
source: langchain/overview.mdx
---

## 描述

LangChain - 开源 LLM 应用框架，提供预构建的 Agent 架构和模型集成。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/overview.mdx`](..\..\raw\src\oss\langchain\overview.mdx)

## 核心价值

- ✅ **快速开始** - 10 行代码构建 Agent
- ✅ **统一接口** - 标准化模型交互
- ✅ **预构建架构** - Agent 抽象
- ✅ **基于 LangGraph** - 持久化、流式、HITL

## 快速开始

```python
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    return f"It's sunny in {city}!"

agent = create_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

agent.invoke({"messages": [{"role": "user", "content": "weather in sf"}]})
```

## 相关页面

- [[LangGraph]] - 底层运行时
- [[Agent]] - Agent 开发
- [[Tool]] - 工具定义
