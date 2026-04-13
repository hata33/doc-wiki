---
name: StrOutputParser
module: langchain_core
source: langchain/structured-output.mdx
---

## 描述

StrOutputParser - 将 LLM 输出解析为字符串，是最常用的输出解析器。

## 原始文档

- **相关文档**: [`langchain/structured-output.mdx`](../../raw/langchain/structured-output.mdx)
- **概念文档**: [`langchain/overview.mdx`](../../raw/langchain/overview.mdx)

## 用途

- 提取 LLM 的文本输出
- 简化链的构建
- 与其他解析器组合使用

## 示例

```python
from langchain_core.output_parsers import StrOutputParser
chain = llm | StrOutputParser()
```

## 相关页面

- [[ChatOpenAI]] - 聊天模型
- [[Streaming]] - 流式输出
