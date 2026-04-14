---
name: 003-langgraph-core
title: LangGraph Core 知识地图
sequence: 003
domain: langgraph-core
---

> Navigation: [[002-langchain-core|上一页]] | [[003-langgraph-core|当前]] | [[004-concepts-and-products|下一页]] | [[012-ecosystem-navigation|012 导航中心]]

## 概述

LangGraph 是 LangChain 生态中的状态图编排框架，专注于构建有状态的、多步骤的 AI 应用。本地图覆盖 Graph API、Functional API、记忆与状态管理、Agent 模式、生产部署、前端集成和错误处理等核心模块。LangGraph 通过图结构定义应用逻辑，支持持久化、时间旅行、子图等高级特性。

## 知识地图

```mermaid
mindmap
  root((LangGraph Core))
    入门
      Overview
        框架概述
        核心概念
        设计理念
      Quickstart
        快速开始
        第一个图
        基础示例
      Install
        安装指南
        环境配置
        依赖设置
      Thinking in LangGraph
        思维模式
        图式编程
        状态流转
      Choosing APIs
        API 选择
        Graph API
        Functional API
    API 体系
      Graph API
        图 API
        节点定义
        边定义
        状态管理
      Functional API
        函数式 API
        声明式定义
        类型安全
        简化语法
      Use Graph API
        使用图 API
        实践指南
        代码示例
      Use Functional API
        使用函数式 API
        实践指南
        代码示例
      Pregel
        Pregel API
        消息传递
        迭代计算
    记忆与状态
      Memory
        记忆系统
        状态持久化
        记忆类型
      Add Memory
        添加记忆
        记忆配置
        使用模式
      Persistence
        持久化机制
        检查点
        状态保存
      Use Subgraphs
        使用子图
        图组合
        嵌套结构
        模块化设计
      Use Time Travel
        时间旅行
        状态回溯
        历史查询
        调试支持
      Interrupts
        中断机制
        人工干预
        暂停恢复
        交互流程
    Agent 模式
      Workflows and Agents
        工作流与 Agent
        编排模式
        最佳实践
      Agentic RAG
        智能 RAG
        自主检索
        决策增强
      SQL Agent
        SQL Agent
        数据库操作
        查询生成
        结果处理
    生产部署
      Application Structure
        应用结构
        项目组织
        模块划分
      Durable Execution
        持久执行
        容错机制
        恢复策略
      Observability
        可观测性
        监控追踪
        性能分析
      Streaming
        流式输出
        实时响应
        增量更新
      Deploy
        部署方案
        生产环境
        扩展策略
      Studio
        开发工具
        可视化编辑
        调试界面
      Local Server
        本地服务器
        开发环境
        测试支持
    案例研究
      Case Studies
        真实案例
        最佳实践
        经验总结
    前端集成
      Frontend Graph Execution
        前端图执行
        客户端集成
        实时交互
    错误处理
      Graph Recursion Limit
        图递归限制
        循环检测
        深度控制
      Invalid Chat History
        聊天历史无效
        历史验证
        修复策略
      Invalid Concurrent Graph Update
        并发更新无效
        并发控制
        同步机制
      Invalid Graph Node Return Value
        节点返回值无效
        返回值验证
        类型检查
      Missing Checkpointer
        缺少检查点
        检查点配置
        持久化设置
      Multiple Subgraphs
        多子图问题
        子图管理
        嵌套限制
    Related Maps
      002 LangChain Core
      009 Infrastructure
      010 Multi-Agent Systems
      011 Cross-Framework Data Flow
```

## 关键统计

| 类别 | 数量 | 代表项 |
|------|------|--------|
| 入门指南 | 5 | Overview, Quickstart, Thinking |
| API 体系 | 5 | Graph API, Functional API, Pregel |
| 记忆与状态 | 6 | Memory, Persistence, Subgraphs |
| Agent 模式 | 3 | Workflows, Agentic RAG, SQL |
| 生产部署 | 7 | Structure, Durable, Observability |
| 案例研究 | 1 | Case Studies |
| 前端集成 | 1 | Frontend Execution |
| 错误处理 | 6 | 6 种错误类型 |

## 关联地图

| 主题 | 关联地图 | 关联主题 |
|------|---------|---------|
| 核心框架 | 002-langchain-core | LangChain 基础 |
| 基础设施 | 009-infrastructure | 部署与运维 |
| 多 Agent | 010-multi-agent-systems | 复杂编排 |
| 跨框架 | 011-cross-framework-data-flow | 数据流设计 |

## 相关 Wiki 页面

- [[003-langgraph-core|LangGraph Core 详情]]
- [[002-langchain-core|LangChain Core 详情]]
- [[004-concepts-and-products|概念与产品]]
