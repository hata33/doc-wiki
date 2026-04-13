---
name: Tools
category: concepts
source: langchain/tools.mdx
---

## 描述

Tools - 基于原始文档的描述

## 原始文档

- **主文档**: [`langchain/tools.mdx`](../../raw/langchain/tools.mdx)

## 代码示例

```python
from langchain.tools import tool

@tool
def search_database(query: str, limit: int = 10) -> str:
    """Search the customer database for records matching the query.

    Args:
        query: Search terms to look for
        limit: Maximum number of results to return
    """
    return f"Found {limit} results for '{query}'"
```

## 相关页面

- 查看原始文档获取更多详细信息
