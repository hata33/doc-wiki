---
name: RecursiveCharacterTextSplitter
category: 文本处理
source: integrations/splitters/recursive_text_splitter.mdx
---

## 描述

RecursiveCharacterTextSplitter - 通用文本分割器，按字符递归分割。

## 原始文档

- **主文档**: [`raw/src/oss/integrations/splitters/recursive_text_splitter.mdx`](..\..\raw\src\oss\integrations\splitters\recursive_text_splitter.mdx)

## 工作原理

- 按字符列表顺序分割：`["\n\n", "\n", " ", ""]`
- 尽可能保持段落、句子、词语完整
- 按字符数测量块大小

## 使用方法

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)

texts = text_splitter.create_documents([state_of_the_union])
```

## 安装

```bash
pip install -qU langchain-text-splitters
```

## 相关页面

- [[RAG]] - RAG 中的文本分割
- [[BM25Retriever]] - 文档检索
