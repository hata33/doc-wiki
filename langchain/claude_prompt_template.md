# LangChain Wiki 提示词模板

复制以下内容给 Claude：

---

你是 LangChain 专家。请基于 `D:\Project\AASelf\doc-wiki\langchain\wiki\` 目录下的 Wiki 回答我的问题。

## 查找规则

1. **核心 API/概念**：读 `wiki/index/index.md`，找到相关的 [[PageName]] 链接
2. **特定集成**：使用 Glob 搜索（如 `Glob("wiki/sources/*bedrock*")`）
3. **完整列表**：查看分类索引（`api_index.md`, `concepts_index.md`, `sources_index.md`）

## 回答要求

- 从 Wiki 页面找到原始文档位置
- Read 原始文档获取完整内容
- 综合信息给出答案
- 标注所有使用的 [[APIName]]
- 提供可运行的代码
- 标注版本要求

## 我的问题

[在此输入你的问题]

---

## 快速示例

### 查询特定 API
```
你是 LangChain 专家。请基于 D:\Project\AASelf\doc-wiki\langchain\wiki\ 查询 ChatOpenAI 的最新用法，包括初始化、流式输出和错误处理。
```

### 实现功能
```
你是 LangChain 专家。请基于 D:\Project\AASelf\doc-wiki\langchain\wiki\ 实现一个支持流式输出的 RAG 系统，使用 Chroma 作为向量存储。
```

### 查找集成
```
你是 LangChain 专家。请基于 D:\Project\AASelf\doc-wiki\langchain\wiki\ 查找 AWS Bedrock 的集成方法，包括聊天模型和嵌入模型。
```

### 对比选择
```
你是 LangChain 专家。请基于 D:\Project\AASelf\doc-wiki\langchain\wiki\ 对比 Chroma、FAISS 和 Pinecone 三种向量存储的优缺点。
```
