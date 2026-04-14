---
name: 002-langchain-core
title: LangChain Core 知识地图
sequence: 002
domain: langchain-core
---

> Navigation: [[001-overview-architecture|001 总览]] | [[002-langchain-core|当前]] | [[003-langgraph-core|下一页]] | [[012-ecosystem-navigation|012 导航中心]]

## 概述

LangChain Core 是 LangChain 生态的核心框架，提供构建 LLM 应用的基础能力。本地图覆盖 Agent 系统、上下文工程、模型交互、记忆管理、执行运行时、前端集成、中间件、测试等核心概念模块。LangChain Core 采用模块化设计，支持从简单的单模型调用到复杂的多 Agent 协作系统。

## 知识地图

```mermaid
mindmap
  root((LangChain Core))
    入门
      Overview
        框架总览
        核心概念
        架构设计
      Philosophy
        设计理念
        可组合性原则
        开发哲学
      Quickstart
        快速开始
        第一个应用
        基础示例
      Install
        安装指南
        环境配置
        依赖管理
      Academy
        学习资源
        教程课程
        最佳实践
    Agent 系统
      Agents
        Agent 基础
        Agent 类型
        执行模式
      Multi-Agent
        Custom Workflow
          自定义工作流
          协作模式
          编排策略
        Handoffs
          交接机制
          状态传递
          控制转移
        Customer Support Example
          客服案例
          场景实现
          代码示例
        Router
          路由模式
          意图识别
          任务分发
        Knowledge Base Example
          知识库集成
          检索增强
          问答实现
        Skills
          技能定义
          能力封装
          工具注册
        SQL Assistant Example
          数据库助手
          SQL 生成
          查询执行
        Subagents
          子 Agent
          层级结构
          代理编排
        Personal Assistant Example
          个人助手
          场景应用
          实现方案
      Tools
        工具定义
        工具使用
        自定义工具
      SQL Agent
        SQL Agent
        数据库交互
        查询优化
      Voice Agent
        语音 Agent
        语音交互
        多模态支持
    上下文与记忆
      Context Engineering
        上下文构建
        Prompt 设计
        上下文优化
      Knowledge Base
        知识库管理
        文档组织
        知识检索
      Long-Term Memory
        长期记忆
        持久化存储
        回忆机制
      Short-Term Memory
        短期记忆
        会话状态
        上下文窗口
      Messages
        消息类型
        消息格式
        消息传递
    模型层
      Models
        模型接口
        模型配置
        模型调用
      Structured Output
        结构化输出
        输出解析
        格式验证
      RAG
        检索增强生成
        RAG 模式
        最佳实践
      Retrieval
        检索策略
        向量检索
        混合检索
    执行与通信
      Runtime
        运行时环境
        执行引擎
        生命周期管理
      Streaming
        流式输出
        实时响应
        增量处理
      MCP
        Model Context Protocol
        上下文协议
        互操作性
    中间件
      Overview
        中间件概述
        架构设计
        使用场景
      Built-In
        内置中间件
        预制组件
        开箱即用
      Custom
        自定义中间件
        扩展开发
        集成方式
    安全与质量
      Guardrails
        安全防护
        输出过滤
        内容审核
      Human-In-The-Loop
        人机协作
        审核机制
        干预流程
      Observability
        可观测性
        监控指标
        日志记录
    前端集成
      Frontend Overview
        前端概述
        集成方式
        架构设计
      Branching Chat
        分支对话
        对话树
        路径管理
      Generative UI
        生成式界面
        动态组件
        UI 生成
      Tool Calling
        工具调用
        函数执行
        结果处理
      Time Travel
        时间旅行
        状态回溯
        历史管理
    错误处理
      Invalid Prompt Input
        提示输入无效
        验证机制
        错误恢复
      Invalid Tool Results
        工具结果无效
        结果校验
        异常处理
      Message Coercion Failure
        消息转换失败
        类型转换
        兼容性处理
      Model Authentication
        模型认证
        凭证管理
        权限验证
      Model Not Found
        模型未找到
        模型发现
        降级策略
      Model Rate Limit
        模型速率限制
        限流处理
        重试策略
      Output Parsing Failure
        输出解析失败
        解析器设计
        容错机制
    测试
      Unit Testing
        单元测试
        测试策略
        Mock 方案
      Integration Testing
        集成测试
        端到端测试
        测试环境
      Evaluations
        评估框架
        指标体系
        评估方法
    其他
      Studio
        开发工具
        可视化界面
        调试支持
      UI
        用户界面
        交互设计
        体验优化
      Deploy
        部署指南
        生产环境
        运维管理
      Changelog
        更新日志
        版本历史
        变更记录
    Related Maps
      003 LangGraph Core
      006 Model Integrations
      007 RAG Pipeline
      008 Tools and Agents
      010 Multi-Agent Systems
```

## 关键统计

| 类别 | 数量 | 代表项 |
|------|------|--------|
| 入门指南 | 5 | Overview, Quickstart, Install |
| Agent 系统 | 12 | Agents, Multi-Agent, Tools |
| 上下文与记忆 | 5 | Context, Memory, Messages |
| 模型层 | 4 | Models, RAG, Retrieval |
| 执行与通信 | 3 | Runtime, Streaming, MCP |
| 中间件 | 3 | Overview, Built-In, Custom |
| 安全与质量 | 3 | Guardrails, HITL, Observability |
| 前端集成 | 5 | Overview, Branching, UI, Tool, Time |
| 错误处理 | 7 | 7 种错误类型处理 |
| 测试 | 3 | Unit, Integration, Eval |

## 关联地图

| 主题 | 关联地图 | 关联主题 |
|------|---------|---------|
| 图框架 | 003-langgraph-core | LangGraph 核心概念 |
| 模型集成 | 006-model-integrations | 模型提供商集成 |
| RAG 系统 | 007-rag-pipeline | 检索增强生成 |
| 工具系统 | 008-tools-and-agents | 工具与 Agent |
| 多 Agent | 010-multi-agent-systems | 多 Agent 协作 |

## 相关 Wiki 页面

- [[002-langchain-core|LangChain Core 详情]]
- [[003-langgraph-core|LangGraph Core 详情]]
- [[001-overview-architecture|生态架构总览]]
