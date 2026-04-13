---
name: ChatMistralAI
category: api
source: python/integrations/chat/mistralai.mdx
---

## 描述

ChatMistralAI integration - Integrate with the ChatMistralAI chat model using LangChain Python.

## 原始文档

- **主文档**: [`python/integrations/chat/mistralai.mdx`](../../raw/python/integrations/chat/mistralai.mdx)

## 代码示例

```python
import getpass
import os

if "MISTRAL_API_KEY" not in os.environ:
    os.environ["MISTRAL_API_KEY"] = getpass.getpass("Enter your Mistral API key: ")
```

## 相关页面

- 查看原始文档获取更多详细信息
