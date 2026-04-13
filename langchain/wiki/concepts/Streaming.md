---
name: Streaming
category: 功能特性
source: langchain/streaming.mdx
---

## 描述

流式输出 - 实时显示 LLM 生成内容，提升用户体验。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/streaming.mdx`](..\..\raw\src\oss\langchain\streaming.mdx)
- **教程**: https://docs.langchain.com/oss/langchain/streaming

## 流式模式

| 模式 | 描述 |
|------|------|
| `updates` | Agent 步骤更新 |
| `messages` | LLM token 流 |
| `custom` | 自定义数据 |

## 使用方式

```python
# LLM 流式输出
for chunk in llm.stream("你的问题"):
    print(chunk.content, end="")

# Agent 流式输出
for chunk in agent.stream(..., stream_mode="updates"):
    print(chunk)
```

## 相关页面

- [[ChatOpenAI]] - 支持流式输出
- [[Agent]] - Agent 流式执行
