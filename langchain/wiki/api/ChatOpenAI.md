---
name: ChatOpenAI
module: langchain_openai
source: python/integrations/chat/openai.mdx
---

## 描述

OpenAI 聊天模型集成，支持 GPT-4、GPT-3.5 等模型。

## 原始文档

- **主文档**: [`raw/src/oss/python/integrations/chat/openai.mdx`](..\..\raw\src\oss\python\integrations\chat\openai.mdx)
- **API 参考**: https://platform.openai.com/docs

## 关键特性

- ✅ 工具调用 (Tool calling)
- ✅ 结构化输出 (Structured output)
- ✅ 流式输出 (Streaming)
- ✅ 图像/音频输入
- ✅ 原生异步支持

## 初始化

```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4", temperature=0.7)
```

## 核心方法

- `invoke(messages)` - 同步调用
- `stream(messages)` - 流式输出
- `batch(messages)` - 批量调用

## 相关页面

- [[AzureChatOpenAI]] - Azure 版本
- [[OpenAIEmbeddings]] - 嵌入模型
