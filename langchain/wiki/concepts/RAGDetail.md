---
name: RAGDetail
category: 核心概念
source: langchain/rag.mdx
---

## 描述

RAG (Retrieval Augmented Generation) - 检索增强生成，结合外部数据源的问答系统。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/rag.mdx`](..\..\raw\src\oss\langchain\rag.mdx)

## 核心概念

| 步骤 | 描述 |
|------|------|
| **索引** | 从源数据摄取并建立索引 |
| **检索** | 查询相关文档 |
| **生成** | 基于检索内容生成答案 |

## RAG 实现

```python
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def retrieve_context(query: str) -> str:
    """Retrieve information to help answer a query."""
    docs = vector_store.similarity_search(query, k=2)
    return "\n\n".join(doc.page_content for doc in docs)

agent = create_agent(
    model="openai:gpt-4",
    tools=[retrieve_context]
)
```

## 相关页面

- [[RAG]] - RAG 概念
- [[BM25Retriever]] - BM25 检索
- [[OpenAIEmbeddings]] - 嵌入模型
