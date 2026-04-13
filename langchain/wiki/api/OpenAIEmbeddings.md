---
name: OpenAIEmbeddings
module: langchain_openai
source: python/integrations/embeddings/openai.mdx
---

## 描述

OpenAI 文本嵌入模型，用于将文本转换为向量表示。

## 原始文档

- **主文档**: [`raw/src/oss/python/integrations/embeddings/openai.mdx`](..\..\raw\src\oss\python\integrations\embeddings\openai.mdx)
- **API 参考**: https://platform.openai.com/docs/guides/embeddings

## 初始化

```python
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
```

## 核心方法

- `embed_query(text)` - 嵌入单个文本
- `embed_documents(texts)` - 批量嵌入

## 使用场景

- RAG 系统中的文档索引
- 语义搜索
- 文本相似度计算

## 相关页面

- [[RAG]] - 检索增强生成
- [[ChatOpenAI]] - 聊天模型
