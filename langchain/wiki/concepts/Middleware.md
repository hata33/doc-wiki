---
name: Middleware
category: 核心概念
source: langchain/middleware/overview.mdx
---

## 描述

Middleware - 在 Agent 执行的每个步骤提供控制和自定义能力。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/middleware/overview.mdx`](..\..\raw\src\oss\langchain\middleware\overview.mdx)

## 用途

- 📊 **跟踪** - 日志、分析、调试
- 🔄 **转换** - 提示、工具选择、输出格式
- 🛡️ **保护** - 重试、回退、速率限制、PII 检测

## 使用方式

```python
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware, HumanInTheLoopMiddleware

agent = create_agent(
    model="gpt-4.1",
    tools=[...],
    middleware=[
        SummarizationMiddleware(...),
        HumanInTheLoopMiddleware(...)
    ],
)
```

## Agent 循环钩子

Middleware 在 Agent 循环的每个步骤前后暴露钩子：
- 模型调用前/后
- 工具选择前/后
- 工具执行前/后

## 相关页面

- [[HumanInTheLoop]] - 人机协作中间件
- [[ShortTermMemory]] - 记忆管理
