---
name: Persistence
category: concepts
source: langgraph/persistence.mdx
---

## 描述

Persistence - 基于原始文档的描述

## 原始文档

- **主文档**: [`langgraph/persistence.mdx`](../../raw/langgraph/persistence.mdx)

## 关键特性

- - **Human-in-the-loop**: Checkpointers facilitate [human-in-the-loop workflows](/oss/langgraph/interrupts) by allowing humans to inspect, interrupt, and approve graph steps. Checkpointers are needed for these workflows as the person has to be able to view the state of a graph at any point in time, and the graph has to be able to resume execution after the person has made any updates to the state. See [Interrupts](/oss/langgraph/interrupts) for examples.
- - **Memory**: Checkpointers allow for ["memory"](/oss/concepts/memory) between interactions. In the case of repeated human interactions (like conversations) any follow up messages can be sent to that thread, which will retain its memory of previous ones. See [Add memory](/oss/langgraph/add-memory) for information on how to add and manage conversation memory using checkpointers.
- - **Time travel**: Checkpointers allow for ["time travel"](/oss/langgraph/use-time-travel), allowing users to replay prior graph executions to review and / or debug specific graph steps. In addition, checkpointers make it possible to fork the graph state at arbitrary checkpoints to explore alternative trajectories.
- - **Fault-tolerance**: Checkpointing provides fault-tolerance and error recovery: if one or more nodes fail at a given superstep, you can restart your graph from the last successful step.
- - **Pending writes**: When a graph node fails mid-execution at a given [super-step](#super-steps), LangGraph stores pending checkpoint writes from any other nodes that completed successfully at that super-step. When you resume graph execution from that super-step you don't re-run the successful nodes.

## 代码示例

```python
{"configurable": {"thread_id": "1"}}
```

## 相关页面

- 查看原始文档获取更多详细信息
