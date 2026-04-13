---
name: HumanInTheLoop
category: 核心概念
source: langchain/human-in-the-loop.mdx
---

## 描述

Human-in-the-Loop (HITL) - 在 Agent 工具调用中添加人工监督和审批机制。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/human-in-the-loop.mdx`](..\..\raw\src\oss\langchain\human-in-the-loop.mdx)

## 决策类型

| 类型 | 描述 | 使用场景 |
|------|------|----------|
| ✅ `approve` | 按原样批准执行 | 发送邮件草稿 |
| ✏️ `edit` | 修改后执行 | 修改收件人后发送 |
| ❌ `reject` | 拒绝并提供反馈 | 拒绝草稿并说明修改建议 |

## 配置方式

```python
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model="gpt-4.1",
    tools=[write_file, execute_sql, read_data],
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                "write_file": True,      # 允许所有决策
                "execute_sql": {"allowed_decisions": ["approve", "reject"]},
                "read_data": False,      # 无需审批
            },
        ),
    ],
    checkpointer=InMemorySaver(),  # HITL 需要 checkpoint
)
```

## 相关页面

- [[Interrupts]] - 中断机制
- [[Middleware]] - 中间件概述
