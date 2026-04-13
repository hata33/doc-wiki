---
name: ToolsDetail
category: 核心概念
source: langchain/tools.mdx
---

## 描述

Tools - 扩展 Agent 能力的可调用函数，支持数据获取、代码执行、数据库查询等。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/tools.mdx`](..\..\raw\src\oss\langchain\tools.mdx)

## 基础定义

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

## 自定义属性

```python
@tool("web_search")  # 自定义名称
def search(query: str) -> str:
    """Search the web for information."""
    return f"Results for: {query}"
```

## 工具命名规范

- ✅ 使用 `snake_case` (如 `web_search`)
- ❌ 避免空格和特殊字符
- ✅ 保持描述简洁清晰

## 相关页面

- [[Tool]] - 工具概念
- [[Agent]] - Agent 使用工具
