---
name: AgentsDetail
category: 核心概念
source: langchain/agents.mdx
---

## 描述

Agents - 结合语言模型和工具，创建能够推理、决策和迭代解决问题的系统。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/agents.mdx`](..\..\raw\src\oss\langchain\agents.mdx)

## Agent 循环

```
用户输入 → 模型推理 → 工具调用 → 观察结果 → 再次推理 → ... → 最终输出
```

## 核心组件

| 组件 | 描述 |
|------|------|
| **Model** | 推理引擎，决策何时使用工具 |
| **Tools** | 可调用的外部函数 |
| **Middleware** | 提示、记忆、上下文处理 |

## 创建 Agent

```python
from langchain.agents import create_agent

agent = create_agent(
    model="openai:gpt-5",
    tools=[search, calculator]
)
```

## 相关页面

- [[LangChain]] - 框架概述
- [[Tool]] - 工具定义
- [[Memory]] - 记忆管理
