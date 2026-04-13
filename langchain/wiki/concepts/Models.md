---
name: Models
category: 核心概念
source: langchain/models.mdx
---

## 描述

Models - LLM 是 Agent 的推理引擎，驱动决策过程。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/models.mdx`](..\..\raw\src\oss\langchain\models.mdx)

## 模型能力

- 🛠️ **工具调用** - 调用外部工具并使用结果
- 📐 **结构化输出** - 约束响应格式
- 🖼️ **多模态** - 处理图像、音频、视频
- 🧠 **推理** - 多步骤推理

## 初始化

```python
from langchain.chat_models import init_chat_model

model = init_chat_model("openai:gpt-4")
response = model.invoke("Why do parrots talk?")
```

## 关键方法

| 方法 | 描述 |
|------|------|
| `invoke` | 生成完整响应 |
| `stream` | 实时流式输出 |
| `batch` | 批量高效处理 |

## 相关页面

- [[ChatOpenAI]] - OpenAI 集成
- [[Tool]] - 工具调用
- [[Agent]] - Agent 开发
