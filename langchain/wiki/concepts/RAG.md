---
name: RAG
category: 架构概念
source: langchain/rag.mdx
---

## 描述

RAG (检索增强生成) - 结合信息检索和文本生成，让 LLM 访问外部知识库。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/rag.mdx`](..\..\raw\src\oss\langchain\rag.mdx)
- **教程**: https://docs.langchain.com/oss/langchain/rag

## 核心概念

1. **索引** (Indexing) - 处理数据源并建立索引
2. **检索** (Retrieval) - 查找相关文档
3. **生成** (Generation) - 基于检索内容生成答案

## 实现方式

- **RAG Agent** - 使用 Agent 框架
- **RAG Chain** - 使用 LCEL 链

## 相关组件

- [[ChatOpenAI]] - 聊天模型
- [[OpenAIEmbeddings]] - 文本嵌入
- [[BM25Retriever]] - BM25 检索器
