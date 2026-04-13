---
name: Messages
category: 核心概念
source: langchain/messages.mdx
---

## 描述

Messages - LangChain 中模型的基本上下文单元，表示输入和输出。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/messages.mdx`](..\..\raw\src\oss\langchain\messages.mdx)

## 消息组成

| 组件 | 描述 |
|------|------|
| **Role** | 消息类型（system、user、assistant） |
| **Content** | 实际内容（文本、图像、音频等） |
| **Metadata** | 可选字段（响应信息、ID、token 使用） |

## 基本使用

```python
from langchain.messages import HumanMessage, AIMessage, SystemMessage

system_msg = SystemMessage("You are a helpful assistant.")
human_msg = HumanMessage("Hello, how are you?")

messages = [system_msg, human_msg]
response = model.invoke(messages)  # 返回 AIMessage
```

## 消息类型

- `SystemMessage` - 系统指令
- `HumanMessage` - 用户输入
- `AIMessage` - AI 响应

## 相关页面

- [[Models]] - 模型使用
- [[Agent]] - Agent 中的消息
