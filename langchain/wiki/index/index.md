# LangChain Wiki 索引

欢迎来到 LangChain API Wiki！这是一个结构化的 LangChain API 知识库。

## 📦 当前版本

| 框架 | 版本 | 状态 | 支持期限 |
|------|------|------|----------|
| **LangChain** | `1.0.x` | 🟢 ACTIVE LTS | 至 2.0 发布后至少 1 年 |
| **LangGraph** | `1.0.x` | 🟢 ACTIVE LTS | 至 2.0 发布后至少 1 年 |

## 📊 Wiki 统计

- **最后更新**: 2026-04-13
- **总页面数**: 2,520
- **API 页面**: 406
- **概念页面**: 363
- **源文档页面**: 1,751
- **覆盖率**: 100%（所有原始文档已索引）
- **空文档**: 已清理

## 📚 快速导航

### 核心 API

#### Chat Models（聊天模型）
- [[ChatOpenAI]] - OpenAI 聊天模型
- [[ChatAnthropic]] - Anthropic Claude 聊天模型
- [[AzureChatOpenAI]] - Azure OpenAI 聊天模型
- [[ChatVertexAI]] - Google Vertex AI
- [[ChatCohere]] - Cohere 聊天模型
- [[ChatMistralAI]] - Mistral AI 聊天模型
- [[ChatGroq]] - Groq 聊天模型
- [[ChatOllama]] - Ollama 本地模型

#### Embeddings（嵌入模型）
- [[OpenAIEmbeddings]] - OpenAI 嵌入
- [[OpenAIEmbeddingsDetail]] - 嵌入详细说明

#### Vector Stores（向量存储）
- [[Chroma]] - Chroma 向量数据库
- [[FAISS]] - FAISS 向量存储
- [[Pinecone]] - Pinecone 向量数据库
- [[Qdrant]] - Qdrant 向量数据库
- [[Milvus]] - Milvus 向量存储
- [[Elasticsearch]] - Elasticsearch 向量存储
- [[PGVector]] - PostgreSQL 向量扩展

#### Retrievers（检索器）
- [[BM25Retriever]] - BM25 检索器

#### Text Splitters（文本分割）
- [[RecursiveCharacterTextSplitter]] - 递归文本分割
- [[CharacterTextSplitter]] - 字符文本分割

#### Runnables & Chains
- [[RunnablePassthrough]] - 数据传递
- [[StrOutputParser]] - 字符串输出解析
- [[LLMChain]] - LLM 链

#### Memory
- [[ConversationBufferMemory]] - 对话缓冲记忆

### 核心概念

#### 框架概述
- [[LangChain]] - LangChain 框架
- [[LangChainOverview]] - LangChain 概述
- [[LangGraph]] - LangGraph 框架
- [[LangGraphOverview]] - LangGraph 概述
- [[Products]] - 产品对比

#### 核心概念
- [[Context]] - 上下文工程
- [[Providers]] - 提供商和模型
- [[Models]] - 模型使用
- [[Messages]] - 消息类型
- [[StructuredOutput]] - 结构化输出

#### Agent 和工具
- [[Agent]] - AI 智能体
- [[Agents]] - Agent 系统
- [[AgentsDetail]] - Agent 详细说明
- [[ToolsDetail]] - 工具详细说明
- [[Tool]] - 工具调用
- [[Tools]] - 工具系统

#### 记忆和状态
- [[Memory]] - 记忆管理
- [[ShortTermMemory]] - 短期记忆
- [[LongTermMemory]] - 长期记忆
- [[Persistence]] - 持久化
- [[AddMemory]] - 添加记忆

#### RAG 和检索
- [[RAG]] - 检索增强生成
- [[RAGDetail]] - RAG 详细实现
- [[Retrieval]] - 检索系统

#### 流式和执行
- [[Streaming]] - 流式输出
- [[LangGraphStreaming]] - LangGraph 流式
- [[DurableExecution]] - 持久化执行

#### 中断和人机协作
- [[Interrupts]] - 中断机制
- [[HumanInTheLoop]] - 人机协作

#### 中间件
- [[Middleware]] - 中间件
- [[BuiltInMiddleware]] - 内置中间件

#### LangGraph API
- [[GraphAPI]] - 图 API
- [[FunctionalAPI]] - 函数式 API
- [[LangGraphCoreSyntax]] - Graph API 核心语法
- [[FunctionalAPIDetail]] - 函数式 API 详细语法

#### 高级功能
- [[Subgraphs]] - 子图
- [[TimeTravel]] - 时间旅行
- [[Chain]] - 链式调用

### 核心语法

#### LangChain 语法
- [[LangChainLCEL]] - LCEL 管道语法
- [[RunnablePassthrough]] - 数据传递
- [[StrOutputParser]] - 字符串输出解析

#### LangGraph 语法
- [[LangGraphCoreSyntax]] - Graph API 语法
- [[FunctionalAPIDetail]] - 函数式 API 语法

#### 入门指南
- [[Quickstart]] - 快速开始

### 源文档（精选）

- [[Install]] - 安装指南
- [[Academy]] - LangChain 学院

### 集成文档（部分示例）

#### 更多聊天模型
- [[Abso]] - ChatAbso 集成
- [[Agentql]] - AgentQL 集成
- [[Ai21]] - AI21 集成
- [[Aimlapi]] - AIMLAPI 集成

#### 更多向量存储
- [[Activeloop]] - Activeloop DeepLake
- [[Aerospike]] - Aerospike 向量存储
- [[ApifyActors]] - Apify Actors 集成

#### 所有集成文档

**📋 完整索引：**
- [[api_index]] - 406 个 API 完整索引（聊天模型、嵌入、向量存储等）
- [[concepts_index]] - 363 个概念完整索引（LangChain、LangGraph 核心概念）
- [[sources_index]] - 1,751 个源文档完整索引（所有集成）

**🔍 快速查找：**
- 查看上述分类索引获取完整文档列表
- 使用 `[[PageName]]` 格式直接访问页面
- 原始文档链接可直接点击跳转

## 🔧 如何使用

### 查找 API

使用 `[[APIName]]` 语法：
- `[[ChatOpenAI]]` - 查找 API
- `[[RAG]]` - 查找概念
- `[[module/path]]` - 查找模块

### 学习路径

1. **初学者**: 从 [[Install]] 和 [[Quickstart]] 开始
2. **RAG 开发**: 查看 [[RAG]] 和 [[BM25Retriever]]
3. **Agent 开发**: 查看 [[Agent]] 和 [[Tool]]
4. **高级用法**: 查看 [[Streaming]] 和 [[Memory]]

## 📂 目录结构

```
wiki/
├── index/index.md      # 主索引（当前页）
├── api/                # API 页面（406 个）
│   ├── 聊天模型集成
│   ├── 嵌入模型
│   ├── 向量存储
│   ├── 检索器
│   └── 其他 API 组件
├── concepts/           # 概念页面（363 个）
│   ├── LangChain 核心概念
│   ├── LangGraph 核心概念
│   ├── 核心语法（LCEL、Graph API、Functional API）
│   └── 高级功能
└── sources/            # 源文档索引（1,751 个）
    ├── 所有 Python 集成（integrations）
    ├── 错误文档
    ├── 指南和教程
    └── 其他文档
```

## 📝 维护信息

- **生成工具**: `schema/scripts/recreate_wikis.py`
- **源文档**: `raw/` 目录（LangChain 官方文档）
- **更新频率**: 建议每周更新一次

## 🔄 更新 Wiki

```bash
# 1. 拉取最新文档
cd raw && git pull

# 2. 重新生成 Wiki
python schema/scripts/recreate_wikis.py

# 3. 清理空文档
python schema/scripts/clean_empty_wikis.py
```

## ⚠️ 注意事项

1. **版本检查**: 使用 API 前检查版本要求
2. **废弃警告**: 避免使用标记为 `deprecated` 的 API
3. **原文优先**: Wiki 是索引，详细信息请查阅原始文档
4. **链接跳转**: 点击原始文档路径可直接跳转到源文件

## ✨ 核心特性

- ✅ **100% 基于原始文档** - 所有内容来自官方文档
- ✅ **中文描述** - 便于理解的中文说明
- ✅ **可点击链接** - 原始文档路径可点击跳转
- ✅ **结构化组织** - 按类别组织，易于查找
- ✅ **交叉引用** - 使用 `[[PageName]]` 格式关联相关页面
- ✅ **无空文档** - 已清理所有 TODO 和空文档
- ✅ **完整覆盖** - 所有 1,454 个原始文档均已索引

---

*最后更新: 2026-04-13 | Wiki 版本: 3.0.0 | 覆盖率: 全部文档 100%*
