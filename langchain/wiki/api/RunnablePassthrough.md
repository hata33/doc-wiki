---
name: RunnablePassthrough
module: langchain_core
source: langchain/overview.mdx
---

## 描述

RunnablePassthrough - 在链中传递数据而不修改，用于构建复杂的 LCEL 链。

## 原始文档

- **概念文档**: [`langchain/overview.mdx`](../../raw/langchain/overview.mdx)
- **快速开始**: [`langchain/quickstart.mdx`](../../raw/langchain/quickstart.mdx)

## 用途

- 在 RAG 链中传递用户查询
- 构建多步骤处理管道
- 数据路由和分发

## 示例

```python
from langchain_core.runnables import RunnablePassthrough
chain = {"query": RunnablePassthrough()} | llm
```

## 相关页面

- [[RAG]] - 常用于 RAG 链
- [[ChatOpenAI]] - 聊天模型
