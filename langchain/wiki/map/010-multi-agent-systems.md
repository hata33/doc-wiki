---
name: 010-multi-agent-systems
title: 多智能体系统知识地图
sequence: 010
domain: multi-agent
---

> Navigation: [[001-overview-architecture|001 总览]] | [[009-infrastructure|上一页]] | [[010-multi-agent-systems|当前]] | [[011-cross-framework-data-flow|下一页]] | [[012-ecosystem-navigation|012 导航中心]]

## 概述

多智能体系统是 LangChain 生态系统的核心能力之一，涵盖 LangChain Multi-Agent、LangGraph Agents 和 DeepAgents 三个框架。本地图展示了各框架的多智能体实现方式、路由机制、技能系统和人机协作等共享概念，帮助开发者理解跨框架的一致性和差异。

## 知识地图

```mermaid
flowchart LR
    subgraph LC["LangChain Multi-Agent"]
        direction TB
        LC1["Custom Workflow"]
        LC2["Handoffs"]
        LC21["Customer Support Example"]
        LC3["Router"]
        LC31["Knowledge Base Example"]
        LC4["Skills"]
        LC41["SQL Assistant Example"]
        LC5["Subagents"]
        LC51["Personal Assistant Example"]

        LC1:::lc
        LC2:::lc
        LC21:::lc
        LC3:::lc
        LC31:::lc
        LC4:::lc
        LC41:::lc
        LC5:::lc
        LC51:::lc
    end

    subgraph LG["LangGraph Agents"]
        direction TB
        LG1["Workflows and Agents"]
        LG2["Use Subgraphs"]
        LG3["Agentic RAG"]
        LG4["Interrupts"]
        LG41["Human-in-the-Loop"]

        LG1:::lg
        LG2:::lg
        LG3:::lg
        LG4:::lg
        LG41:::lg
    end

    subgraph DA["DeepAgents"]
        direction TB
        DA1["Subagents"]
        DA2["Async Subagents"]
        DA3["Skills"]
        DA4["Harness"]
        DA5["Permissions"]

        DA1:::da
        DA2:::da
        DA3:::da
        DA4:::da
        DA5:::da
    end

    subgraph Shared["Shared Concepts"]
        SH1["Streaming"]
        SH2["Memory"]
        SH3["Human-In-The-Loop"]
        SH4["Context Engineering"]

        SH1:::shared
        SH2:::shared
        SH3:::shared
        SH4:::shared
    end

    subgraph XREF["Related Maps"]
        XR1["002 LangChain Core"]
        XR2["003 LangGraph Core"]
        XR3["005 DeepAgents"]
        XR4["011 Cross Framework Data Flow"]

        XR1:::xref
        XR2:::xref
        XR3:::xref
        XR4:::xref
    end

    LC1 -.-> SH4
    LC3 -.-> SH4
    LC5 -.-> SH1
    LG1 -.-> SH1
    LG2 -.-> SH2
    LG4 -.-> SH3
    DA1 -.-> SH1
    DA3 -.-> SH4
    DA2 -.-> SH1

    LC --- Shared
    LG --- Shared
    DA --- Shared

    Shared -.-> XREF

    classDef lc fill:#2563EB,color:#fff,stroke:#1D4ED8
    classDef lg fill:#059669,color:#fff,stroke:#047857
    classDef py fill:#D97706,color:#fff,stroke:#B45309
    classDef cp fill:#7C3AED,color:#fff,stroke:#6D28D9
    classDef da fill:#DC2626,color:#fff,stroke:#B91C1C
    classDef xref fill:#EC4899,color:#fff,stroke:#DB2777
    classDef shared fill:#F59E0B,color:#000,stroke:#D97706
```

## 关键统计

| 类别 | LangChain | LangGraph | DeepAgents |
|------|-----------|-----------|------------|
| 工作流模式 | 5 种 | 4 种 | 3 种 |
| 示例代码 | 4 个 | 3 个 | 内置 |
| 共享概念 | Streaming, Memory | Human-in-the-Loop | Context Engineering |

## 关联地图

| 主题 | 关联地图 | 关联主题 |
|------|---------|---------|
| LangChain 核心 | 002-langchain-core | Tools, Agents, Runnable |
| LangGraph 核心 | 003-langgraph-core | Graph API, Subgraphs, Persistence |
| DeepAgents | 005-deepagents | Subagents, Skills, Harness |
| 跨框架数据流 | 011-cross-framework-data-flow | 完整数据处理流程 |

## 框架对比

| 特性 | LangChain Multi-Agent | LangGraph Agents | DeepAgents |
|------|----------------------|------------------|------------|
| 工作流定义 | Runnable 链 | Graph 状态机 | Harness 编排 |
| 子代理 | Handoffs/Router | Subgraphs | Subagents |
| 技能系统 | Skills (LangChain) | 内置于 Graph | Skills (DA) |
| 人机协作 | 中断 + 审批 | Interrupts | Human-In-The-Loop |
| 流式输出 | Streaming | Streaming | Streaming |
| 适用场景 | 轻量级多代理 | 复杂状态流转 | 企业级应用 |

## 相关 Wiki 页面

### LangChain Multi-Agent
- [[010-multi-agent/custom-workflow]] 自定义工作流
- [[010-multi-agent/handoffs]] 代理切换
- [[010-multi-agent/router]] 路由机制
- [[010-multi-agent/skills]] 技能系统
- [[010-multi-agent/subagents]] 子代理

### LangGraph Agents
- [[010-multi-agent/workflows-agents]] 工作流与代理
- [[010-multi-agent/use-subgraphs]] 使用子图
- [[010-multi-agent/agentic-rag]] 智能检索
- [[010-multi-agent/interrupts]] 中断与人机协作

### DeepAgents
- [[010-multi-agent/subagents]] 子代理系统
- [[010-multi-agent/async-subagents]] 异步子代理
- [[010-multi-agent/skills]] 技能框架
- [[010-multi-agent/harness]] 编排系统
- [[010-multi-agent/permissions]] 权限管理
