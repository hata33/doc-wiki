---
name: LLMChain
module: langchain_chains
source: python/integrations/chat/openai.mdx
---

## 描述

LLMChain - LangChain 的基础链类，用于构建简单的 LLM 应用。

## 原始文档

- **相关文档**: [`python/integrations/chat/openai.mdx`](../../raw/python/integrations/chat/openai.mdx)
- **概念文档**: [`langchain/overview.mdx`](../../raw/langchain/overview.mdx)

## 初始化

```python
from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt)
```

## 用途

- 简单的问答应用
- 文本生成
- 提示工程

## 相关页面

- [[ChatOpenAI]] - 聊天模型
- [[ChatPromptTemplate]] - 提示模板
