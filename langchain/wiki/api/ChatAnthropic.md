---
name: ChatAnthropic
module: langchain_anthropic
source: python/integrations/chat/anthropic.mdx
---

## 描述

ChatAnthropic - Anthropic Claude 聊天模型集成，支持 Claude 系列。

## 原始文档

- **主文档**: [`raw/src/oss/python/integrations/chat/anthropic.mdx`](..\..\raw\src\oss\python\integrations\chat\anthropic.mdx)

## 关键特性

- ✅ 工具调用
- ✅ 结构化输出
- ✅ 图像输入
- ✅ Token 级流式输出
- ✅ 原生异步

## 初始化

```python
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    temperature=0.7,
    max_tokens=1024
)
```

## 安装

```bash
pip install -U langchain-anthropic
```

## 相关页面

- [[ChatOpenAI]] - OpenAI 集成
- [[Tool]] - 工具调用
