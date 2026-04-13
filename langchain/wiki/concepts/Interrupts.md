---
name: Interrupts
category: 核心概念
source: langgraph/interrupts.mdx
---

## 描述

Interrupts - 在特定点暂停图执行，等待外部输入后继续，支持人机协作模式。

## 原始文档

- **主文档**: [`raw/src/oss/langgraph/interrupts.mdx`](..\..\raw\src\oss\langgraph\interrupts.mdx)

## 核心特性

- **动态暂停** - 可在代码任意位置设置条件中断
- **状态保存** - 使用持久化层保存图状态
- **无限等待** - 直到恢复执行才继续

## 使用中断

```python
from langgraph.types import interrupt

def approval_node(state: State):
    # 暂停并请求审批
    approved = interrupt("是否批准此操作？")

    # 恢复时 Command(resume=...) 返回该值
    return {"approved": approved}
```

## 恢复执行

```python
from langgraph.types import Command

# 首次运行 - 遇到中断暂停
config = {"configurable": {"thread_id": "thread-1"}}
response = graph.invoke(state, config)

# 恢复执行 - 传入响应值
response = graph.invoke(
    Command(resume="approved"),  # 传递给 interrupt() 的返回值
    config
)
```

## 相关页面

- [[HumanInTheLoop]] - 人机协作
- [[DurableExecution]] - 持久化执行
