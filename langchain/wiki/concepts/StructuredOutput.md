---
name: StructuredOutput
category: 核心概念
source: langchain/structured-output.mdx
---

## 描述

Structured Output - Agent 返回特定、可预测格式的数据。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/structured-output.mdx`](..\..\raw\src\oss\langchain\structured-output.mdx)

## 响应格式

| 策略 | 描述 |
|------|------|
| `ToolStrategy` | 使用工具调用实现结构化输出 |
| `ProviderStrategy` | 使用提供商原生结构化输出 |
| `type[Schema]` | 自动选择最佳策略 |

## 使用示例

```python
from dataclasses import dataclass
from langchain.agents import create_agent

@dataclass
class ResponseFormat:
    summary: str
    sources: list[str]

agent = create_agent(
    model="openai:gpt-4",
    tools=[search],
    response_format=ResponseFormat
)

# 响应在 agent.state['structured_response'] 中
```

## 自动选择

- OpenAI/Anthropic/xAI: 使用 `ProviderStrategy`
- 其他模型: 使用 `ToolStrategy`

## 相关页面

- [[Models]] - 模型结构化输出
- [[Tool]] - 工具调用
