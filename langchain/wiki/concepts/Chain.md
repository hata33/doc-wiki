---
name: Chain
category: 架构概念
source: langchain/overview.mdx
---

## 描述

Chain - LangChain 中的链式调用机制，用于构建多步骤的 LLM 应用。

## 原始文档

- **概念文档**: [`langchain/overview.mdx`](../../raw/langchain/overview.mdx)
- **快速开始**: [`langchain/quickstart.mdx`](../../raw/langchain/quickstart.mdx)

## 类型

- **LLMChain** - 基本 LLM 链
- **SequentialChain** - 顺序链
- **RouterChain** - 路由链

## 构建

```python
from langchain_core.chains import LCEL
chain = prompt | llm | parser
```

## 相关页面

- [[ChatOpenAI]] - 聊天模型
- [[ChatPromptTemplate]] - 提示模板
