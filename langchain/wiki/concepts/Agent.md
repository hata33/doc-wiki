---
name: Agent
category: 架构概念
source: langchain/agents.mdx
---

## 描述

Agent - 结合 LLM 和工具，能够推理任务、选择工具并迭代解决问题。

## 原始文档

- **主文档**: [`raw/src/oss/langchain/agents.mdx`](..\..\raw\src\oss\langchain\agents.mdx)
- **教程**: https://docs.langchain.com/oss/langchain/agents

## 核心组件

- **Model** - 推理引擎 (LLM)
- **Tools** - 可调用工具
- **Runtime** - 执行循环

## 工作流程

```
用户输入 → LLM 决策 → 调用工具 → 观察结果 → 
LLM 再决策 → ... → 最终答案
```

## 初始化

```python
from langchain.agents import create_agent
agent = create_agent(model, tools)
```

## 相关页面

- [[ChatOpenAI]] - 作为 Model
- [[Streaming]] - Agent 流式输出
