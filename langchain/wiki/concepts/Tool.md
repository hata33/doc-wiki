---
name: Tool
category: 架构概念
source: langchain/tools.mdx
---

## 描述

Tool - Agent 可调用的函数或服务，如搜索、数据库查询、API 调用等。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/tools.mdx`](..\..\raw\src\oss\langchain\tools.mdx)
- **教程**: https://docs.langchain.com/oss/langchain/tools

## 类型

- **内置工具** - 搜索、计算等
- **自定义工具** - 用 `@tool` 装饰器创建
- **工具包** - 第三方集成

## 示例

```python
from langchain_core.tools import tool

@tool
def search(query: str) -> str:
    """搜索网络"""
    return f"搜索结果：{query}"
```

## 相关页面

- [[Agent]] - Agent 使用工具
- [[RAG]] - 检索工具
