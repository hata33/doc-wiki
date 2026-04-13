---
name: OpenAIEmbeddingsDetail
module: langchain_openai
source: python/integrations/embeddings/openai.mdx
---

## 描述

OpenAIEmbeddings - OpenAI 嵌入模型，用于文本向量化。

## 原始文档

- **主文档**: [`raw/src/oss/python/integrations/embeddings/openai.mdx`](..\..\raw\src\oss\python\integrations\embeddings\openai.mdx)

## 初始化

```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    # dimensions=1024  # text-embedding-3 系列支持指定维度
)
```

## 安装

```bash
pip install -qU langchain-openai
```

## 用途

- RAG 索引和检索
- 语义搜索
- 文档相似度计算

## 相关页面

- [[RAG]] - 检索增强生成
- [[Chroma]] - 向量数据库
