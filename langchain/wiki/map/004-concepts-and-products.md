---
name: 004-concepts-and-products
title: 概念与产品关系图
sequence: 004
domain: concepts
---

> Navigation: [[003-langgraph-core|上一页]] | [[004-concepts-and-products|当前]] | [[005-deepagents|下一页]] | [[012-ecosystem-navigation|012 导航中心]]

## 概述

本图展示了 LangChain 生态中四个核心概念（Context、Memory、Products、Providers and Models）与各产品域之间的映射关系。通过这种可视化呈现，可以清晰理解每个概念在不同框架中的具体实现和集成方式，为开发者提供从概念学习到产品应用的知识导航。

## 知识地图

```mermaid
flowchart LR
    subgraph Concepts["核心概念"]
        direction TB
        CTX["Context 上下文工程"]
        MEM["Memory 记忆管理"]
        PRD["Products 产品体系"]
        PRV["Providers and Models 提供商与模型"]
    end

    subgraph Products["产品域"]
        LC["LangChain Core 蓝色"]
        LG["LangGraph Core 绿色"]
        DA["DeepAgents 红色"]
        PY["Python Integrations 琥珀色"]
    end

    %% Context connections
    CTX -->|"Context Engineering"| LC
    CTX -->|"Context Engineering"| DA

    %% Memory connections
    MEM -->|"Short-Term / Long-Term Memory"| LC
    MEM -->|"Persistence / Add-Memory"| LG
    MEM -->|"Memory"| DA

    %% Products connections
    PRD -->|"LangChain / LangGraph / DeepAgents / LangSmith"| LC
    PRD -->|"LangChain / LangGraph / DeepAgents / LangSmith"| LG
    PRD -->|"LangChain / LangGraph / DeepAgents / LangSmith"| DA

    %% Providers connections
    PRV -->|"Models"| LC
    PRV -->|"Models"| DA
    PRV -->|"Chat 102 / LLMs 97 / Embeddings 92"| PY

    %% Cross references
    XREF["跨域引用"]
    XREF -->|"架构总览"| NAV001["001 Overview Architecture"]
    XREF -->|"核心框架"| NAV002["002 LangChain Core"]
    XREF -->|"图框架"| NAV003["003 LangGraph Core"]
    XREF -->|"智能体"| NAV005["005 DeepAgents"]
    XREF -->|"RAG 流水线"| NAV007["007 RAG Pipeline"]

    %% Style classes
    classDef lc fill:#2563EB,color:#fff,stroke:#1D4ED8
    classDef lg fill:#059669,color:#fff,stroke:#047857
    classDef py fill:#D97706,color:#fff,stroke:#B45309
    classDef cp fill:#7C3AED,color:#fff,stroke:#6D28D9
    classDef da fill:#DC2626,color:#fff,stroke:#B91C1C
    classDef xref fill:#EC4899,color:#fff,stroke:#DB2777

    class LC lc
    class LG lg
    class PY py
    class DA da
    class CTX,MEM,PRD,PRV cp
    class XREF,NAV001,NAV002,NAV003,NAV005,NAV007 xref
```

## 关键统计

| 概念 | 关联产品数 | 主要实现 |
|------|----------|---------|
| Context（上下文） | 2 | Context Engineering (LC/DA) |
| Memory（记忆） | 3 | ST/LT Memory, Persistence, Memory |
| Products（产品） | 3 | 全产品栈支持 |
| Providers（提供商） | 3 | Models, Chat/LLMs/Embeddings |

## 关联地图

| 主题 | 关联地图 | 关联主题 |
|------|---------|---------|
| 生态架构 | 001-overview-architecture | LangChain 生态全景 |
| 核心框架 | 002-langchain-core | LangChain 详细知识 |
| 图框架 | 003-langgraph-core | LangGraph 详细知识 |
| 智能体 | 005-deepagents | DeepAgents 详细知识 |
| RAG 流水线 | 007-rag-pipeline | RAG 实现方案 |

## 概念说明

### Context（上下文工程）
- **LangChain Core**: 提供完整的上下文工程能力，包括 Prompt 设计、上下文优化、知识库集成
- **DeepAgents**: 在 Agent 系统中应用上下文工程，实现智能上下文管理

### Memory（记忆管理）
- **LangChain Core**: 短期记忆和长期记忆的完整实现
- **LangGraph Core**: 持久化和检查点机制，支持状态回溯
- **DeepAgents**: 记忆系统在多 Agent 环境中的应用

### Products（产品体系）
- **LangSmith**: 开发者平台和 observability 工具
- **LangChain/LangGraph**: 核心开发框架
- **DeepAgents**: 高级 Agent 编排平台

### Providers and Models（提供商与模型）
- **Chat Models**: 102+ 集成（如 OpenAI, Anthropic, 等）
- **LLMs**: 97+ 集成
- **Embeddings**: 92+ 集成
- 跨框架统一模型接口

## 相关 Wiki 页面

- [[004-concepts-and-products|概念与产品详情]]
- [[001-overview-architecture|生态架构总览]]
- [[002-langchain-core|LangChain Core]]
- [[003-langgraph-core|LangGraph Core]]
