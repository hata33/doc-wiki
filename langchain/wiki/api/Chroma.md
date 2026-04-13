---
name: Chroma
module: langchain_community
source: python/integrations/vectorstores/chroma.mdx
---

## 描述

Chroma - 开源向量数据库，用于存储和检索文档嵌入。

## 原始文档

- **主文档**: [raw/src/oss/python/integrations/vectorstores/chroma.mdx](../../raw/src/oss/python/integrations/vectorstores/chroma.mdx)
- **官网**: https://www.trychroma.com

## 用途

- RAG 系统中的向量存储
- 语义搜索
- 文档索引

## 初始化

```python
from langchain_community.vectorstores import Chroma
vectorstore = Chroma.from_texts(docs, embedding=embeddings)
```

## 相关页面

- [[RAG]] - 检索增强生成
- [[OpenAIEmbeddings]] - 文本嵌入
