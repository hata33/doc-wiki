---
name: DurableExecution
category: 核心概念
source: langgraph/durable-execution.mdx
---

## 描述

Durable Execution - 持久化执行技术，保存进度以支持暂停和恢复。

## 原始文档

- **主文档**: [`raw/src/oss/langgraph/durable-execution.mdx`](..\..\raw\src\oss\langgraph\durable-execution.mdx)

## 核心特性

- 💾 **状态保存** - 在关键点保存执行进度
- ⏸️ **暂停恢复** - 支持人机协作暂停
- 🔄 **故障恢复** - 从中断点继续执行

## 要求

1. **持久化层** - 指定 checkpointer
2. **线程标识** - 使用 `thread_id` 跟踪
3. **幂等性** - 副作用操作应包装在 task 中

## 持久化模式

| 模式 | 描述 | 性能 | 持久性 |
|------|------|------|--------|
| `"exit"` | 仅在退出时保存 | 最高 | 最低 |
| `"async"` | 异步保存 | 高 | 中等 |
| `"sync"` | 同步保存 | 中等 | 最高 |

## 使用示例

```python
graph.stream(
    {"input": "test"},
    durability="sync"  # 同步持久化
)
```

## 相关页面

- [[Interrupts]] - 中断机制
- [[LangGraph]] - LangGraph 运行时
