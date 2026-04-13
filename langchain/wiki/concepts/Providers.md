---
name: Providers
category: 核心概念
source: concepts/providers-and-models.mdx
---

## 描述

Providers and Models - LangChain 提供统一 API 接入任何提供商的模型。

## 原始文档

- **主文档**: [`raw/src/oss/concepts/providers-and-models.mdx`](..\..\raw\src\oss\concepts\providers-and-models.mdx)

## 核心特性

- ✅ **统一接口** - 相同代码切换提供商
- ✅ **自动解析** - `provider:model` 格式
- ✅ **即时可用** - 新模型无需更新 LangChain

## 初始化方式

```python
from langchain.chat_models import init_chat_model

# 方式1: 前缀格式
model = init_chat_model("openai:gpt-4")

# 方式2: 直接实例化
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4")
```

## 常用提供商

| 提供商 | 包名 | 模型查找 |
|--------|------|----------|
| OpenAI | `langchain-openai` | platform.openai.com/docs/models |
| Anthropic | `langchain-anthropic` | docs.anthropic.com/en/docs/about-claude/models |
| Google | `langchain-google-genai` | ai.google.dev/gemini-api/docs/models |

## 相关页面

- [[ChatOpenAI]] - OpenAI 集成
- [[AzureChatOpenAI]] - Azure 集成
- [[Tool]] - 工具调用
