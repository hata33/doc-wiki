---
name: FunctionalAPI
category: 核心语法
source: langgraph/functional-api.mdx
---

## 描述

LangGraph Functional API - 使用装饰器构建工作流，支持持久化、记忆和人机协作。

## 原始文档

- **主文档**: [`raw/src/oss/langgraph/functional-api.mdx`](../../raw/langgraph/functional-api.mdx)
- **使用指南**: [`raw/src/oss/langgraph/use-functional-api.mdx`](../../raw/langgraph/use-functional-api.mdx)

## 核心装饰器

### @task
定义工作单元，支持异步执行和结果缓存。

```python
from langgraph.func import task

@task
def process_data(data: str) -> str:
    """处理数据的任务"""
    return data.upper()

# 使用
result = process_data("hello").result()
```

### @entrypoint
定义工作流入口点，管理执行流程和中断。

```python
from langgraph.func import entrypoint
from langgraph.checkpoint.memory import InMemorySaver

@entrypoint(checkpointer=InMemorySaver())
def my_workflow(inputs: dict) -> str:
    """工作流函数"""
    result = process_data(inputs["value"]).result()
    return result
```

## 基本语法

### 简单工作流

```python
from langgraph.func import entrypoint, task
from langgraph.checkpoint.memory import InMemorySaver

@task
def is_even(number: int) -> bool:
    return number % 2 == 0

@task
def format_message(is_even: bool) -> str:
    return "偶数" if is_even else "奇数"

@entrypoint(checkpointer=InMemorySaver())
def workflow(inputs: dict) -> str:
    even = is_even(inputs["number"]).result()
    return format_message(even).result()

# 执行
config = {"configurable": {"thread_id": "1"}}
result = workflow.invoke({"number": 7}, config=config)
```

## 高级特性

### 并行执行

```python
import asyncio

@task
def task_a(value: int) -> int:
    return value + 1

@task
def task_b(value: int) -> int:
    return value * 2

@entrypoint(checkpointer=InMemorySaver())
def parallel_workflow(value: int) -> dict:
    # 并行执行
    results = asyncio.gather(
        task_a.run(value),
        task_b.run(value)
    )
    return {"results": [r.result() for r in results]}
```

### 人机协作

```python
from langgraph.types import interrupt

@entrypoint(checkpointer=InMemorySaver())
def workflow_with_approval(data: str) -> dict:
    # 执行任务
    result = process_data(data).result()
    
    # 请求审批
    approved = interrupt({
        "result": result,
        "action": "请审批此结果"
    })
    
    return {"result": result, "approved": approved}
```

### 与 LLM 集成

```python
from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4")

@task
def generate_text(topic: str) -> str:
    response = model.invoke(f"写一篇关于 {topic} 的文章")
    return response.content

@entrypoint(checkpointer=InMemorySaver())
def writing_workflow(topic: str) -> str:
    return generate_text(topic).result()
```

## 相关页面

- [[LangGraphCoreSyntax]] - Graph API 语法
- [[DurableExecution]] - 持久化执行
- [[Interrupts]] - 中断机制
