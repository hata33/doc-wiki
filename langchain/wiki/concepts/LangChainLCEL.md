---
name: LangChainLCEL
category: 核心语法
source: langchain
---

## 描述

LangChain LCEL (LangChain Expression Language) - 使用管道操作符 (`|`) 组合 LangChain 组件的声明式语法。

## 核心语法

LCEL 使用管道操作符 `|` 从左到右组合组件，形成可执行的链。

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# LCEL 语法
chain = (
    ChatPromptTemplate.from_template("Tell me a joke about {topic}")
    | ChatOpenAI(model="gpt-4")
    | StrOutputParser()
)

# 执行
result = chain.invoke({"topic": "programming"})
```

## 核心组件

### 1. Runnable
所有 LCEL 组件的基础接口，实现 `invoke`、`stream`、`batch` 方法。

```python
from langchain_core.runnables import RunnableLambda

# 创建 Runnable
runnable = RunnableLambda(lambda x: x.upper())
```

### 2. 管道操作符 `|`
组合多个 Runnable，按顺序传递数据。

```python
chain = (
    component1
    | component2
    | component3
)
```

### 3. 并行执行
使用 `RunnableParallel` 并行执行多个分支。

```python
from langchain_core.runnables import RunnableParallel

chain = RunnableParallel(
    summary=component1 | output_parser1,
    analysis=component2 | output_parser2
)
```

### 4. 路由
使用 `RunnableLambda` 或 `RunnableBranch` 条件路由。

```python
from langchain_core.runnables import RunnableLambda

def route_func(x):
    return "branch_a" if x > 0 else "branch_b"

router = RunnableLambda(route_func)
chain = {
    "branch_a": chain_a,
    "branch_b": chain_b
} | router
```

## 常用模式

### 基础链

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "What is the capital of {country}?"
)
model = ChatOpenAI(model="gpt-4")

chain = prompt | model
```

### 带输出解析

```python
from langchain_core.output_parsers import StrOutputParser

chain = (
    ChatPromptTemplate.from_template("Tell me about {topic}")
    | ChatOpenAI(model="gpt-4")
    | StrOutputParser()
)
```

### 传递数据

```python
from langchain_core.runnables import RunnablePassthrough

chain = {
    "context": retriever | RunnableLambda(lambda x: "\n".join(x)),
    "question": RunnablePassthrough()
} | prompt | model
```

### 组合多个输出

```python
from langchain_core.runnables import RunnableMap

chain = {
    "summary": prompt | model | StrOutputParser(),
    "original": RunnablePassthrough()
}
```

## 执行方法

### invoke
同步执行一次。

```python
result = chain.invoke({"topic": "AI"})
```

### stream
流式输出。

```python
for chunk in chain.stream({"topic": "AI"}):
    print(chunk, end="")
```

### batch
批量执行。

```python
results = chain.batch([
    {"topic": "AI"},
    {"topic": "ML"}
])
```

### astream
异步流式输出。

```python
async for chunk in chain.astream({"topic": "AI"}):
    print(chunk, end="")
```

## 相关页面

- [[LangGraphCoreSyntax]] - LangGraph 图语法
- [[FunctionalAPI]] - 函数式 API
- [[StrOutputParser]] - 字符串输出解析
