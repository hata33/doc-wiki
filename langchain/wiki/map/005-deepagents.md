---
name: 005-deepagents
title: DeepAgents 知识地图
sequence: 005
domain: deepagents
---

> Navigation: [[001-overview-architecture|001 总览]] | [[005-deepagents|当前]] | [[006-model-integrations|下一页]] | [[012-ecosystem-navigation|012 导航中心]]

## 概述

DeepAgents 是 LangChain 生态系统中的高级多智能体框架，专注于构建具备自主能力的 AI 系统。它提供了 Subagents、Skills、Streaming 等核心能力，支持命令行工具、前端集成、数据分析和生产部署。DeepAgents 强调上下文工程、权限管理和沙箱隔离，适用于构建企业级 AI 应用。

## 知识地图

```mermaid
mindmap
  root((DeepAgents))
    入门
      Overview
        框架介绍
        核心概念
        适用场景
      Comparison
        与其他框架对比
        优势分析
        选择指南
      Quickstart
        快速安装
        Hello World
        第一个 Agent
    核心能力
      Subagents
        子代理概念
        创建方法
        通信机制
      Async Subagents
        异步执行
        并发控制
        性能优化
      Skills
        技能定义
        技能注册
        技能调用
      Streaming
        实时输出
        事件流
        前端集成
      Context Engineering
        上下文管理
        提示工程
        系统提示
    命令行工具
      CLI Overview
        命令结构
        基本用法
        常见命令
      CLI Configuration
        配置文件
        环境变量
        配置选项
      CLI MCP Tools
        MCP 协议
        工具集成
        扩展开发
      CLI Providers
        模型提供商
        API 配置
        切换方法
    前端集成
      Frontend Overview
        集成方式
        组件库
        架构设计
      Frontend Sandbox
        沙箱环境
        安全隔离
        资源限制
      Frontend Subagent Streaming
        流式处理
        状态管理
        事件处理
      Frontend Todo List
        示例应用
        最佳实践
        代码参考
    数据能力
      Data Analysis
        数据读取
        分析工具
        可视化
      Data Locations
        数据源配置
        存储选项
        访问权限
      Deep Research
        深度搜索
        研究流程
        结果整合
      Content Builder
        内容生成
        模板系统
        输出格式
    生产部署
      Deploy
        部署方案
        环境配置
        CI/CD
      Going to Production
        性能优化
        监控告警
        故障排查
      Permissions
        权限模型
        访问控制
        安全策略
      Sandboxes
        沙箱类型
        隔离机制
        资源管理
    高级特性
      Backends
        后端架构
        存储选择
        扩展开发
      Customization
        自定义配置
        插件开发
        扩展点
      Harness
        编排框架
        工作流定义
        执行引擎
      Models
        模型集成
        提示管理
        参数调优
      Memory
        记忆系统
        存储机制
        检索策略
      Human-In-The-Loop
        人机协作
        审批流程
        中断恢复
    协议
      ACP
        Agent Communication Protocol
        消息格式
        通信规范
    Related Maps
      002 LangChain Core
      003 LangGraph Core
      010 Multi Agent Systems
      011 Cross Framework Data Flow
```

## 关键统计

| 类别 | 数量 | 代表项 |
|------|------|--------|
| 核心文档 | 32 篇 | Overview, Subagents, Skills |
| CLI 文档 | 4 篇 | Configuration, MCP Tools |
| 前端集成 | 4 篇 | Overview, Sandbox, Streaming |
| 协议规范 | 1 篇 | ACP |

## 关联地图

| 主题 | 关联地图 | 关联主题 |
|------|---------|---------|
| 多智能体系统 | 010-multi-agent-systems | Subagents, Skills, Handoffs |
| 跨框架数据流 | 011-cross-framework-data-flow | Context Engineering, Memory, Streaming |
| LangChain 核心 | 002-langchain-core | Tools, Agents, Context |
| LangGraph 核心 | 003-langgraph-core | Workflows, Subgraphs, Interrupts |

## 相关 Wiki 页面

- [[005-deepagents/overview]] DeepAgents 概览
- [[005-deepagents/subagents]] 子代理系统
- [[005-deepagents/skills]] 技能系统
- [[005-deepagents/streaming]] 流式处理
- [[005-deepagents/context-engineering]] 上下文工程
- [[005-deepagents/cli/overview]] 命令行工具
- [[005-deepagents/frontend/overview]] 前端集成
