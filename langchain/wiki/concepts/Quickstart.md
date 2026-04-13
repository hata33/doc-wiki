---
name: Quickstart
category: 入门指南
source: langchain/quickstart.mdx
---

## 描述

Quickstart - 从简单设置到功能完整的 AI Agent 的快速入门指南。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/quickstart.mdx`](..\..\raw\src\oss\langchain\quickstart.mdx)

## 基础 Agent

```python
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="claude-sonnet-4-6",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

agent.invoke({"messages": [{"role": "user", "content": "weather in sf"}]})
```

## 完整 Agent 特性

- **系统提示** - 定义 Agent 行为
- **工具集成** - 连接外部数据
- **模型配置** - temperature、timeout 等
- **结构化输出** - 可预测的响应格式
- **对话记忆** - 跨交互状态
- **运行时上下文** - 用户特定信息

## 相关页面

- [[LangChain]] - 框架概述
- [[Agent]] - Agent 开发
- [[Tool]] - 工具定义
- [[Memory]] - 记忆管理
