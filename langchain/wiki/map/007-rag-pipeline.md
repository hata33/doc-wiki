---
name: 007-rag-pipeline
title: RAG 数据管道
sequence: 007
domain: integrations
---

> Navigation: [[006-model-integrations|上一页]] | [[007-rag-pipeline|当前]] | [[008-tools-and-agents|下一页]] | [[012-ecosystem-navigation|012 导航中心]]

## 概述

RAG (Retrieval-Augmented Generation) 是 LangChain 的核心应用场景之一。完整的 RAG 管道包含数据加载、转换、分块、嵌入、向量存储和检索六个阶段。LangChain 提供了 170+ Document Loaders、19+ Document Transformers、多种 Text Splitters、86+ Embeddings 提供商、90+ Vector Stores 和 72+ Retrievers，构建了业界最完整的 RAG 生态系统。

## 知识地图

```mermaid
flowchart LR
    classDef lc fill:#2563EB,color:#fff,stroke:#1D4ED8
    classDef lg fill:#059669,color:#fff,stroke:#047857
    classDef py fill:#D97706,color:#fff,stroke:#B45309
    classDef cp fill:#7C3AED,color:#fff,stroke:#6D28D9
    classDef da fill:#DC2626,color:#fff,stroke:#B91C1C
    classDef xref fill:#EC4899,color:#fff,stroke:#DB2777
    classDef shared fill:#F59E0B,color:#000,stroke:#D97706

    Loaders["Document Loaders(170+)"]:::py
    Transformers["Document Transformers(19+)"]:::py
    Splitters["Text Splitters"]:::py
    Embeddings["Embeddings(86 providers)"]:::py
    VectorStores["Vector Stores(90+)"]:::py
    Retrievers["Retrievers(72)"]:::py

    Loaders -->|"原始数据"| Transformers
    Transformers -->|"处理文档"| Splitters
    Splitters -->|"文本块"| Embeddings
    Embeddings -->|"向量"| VectorStores
    VectorStores -->|"相似度搜索"| Retrievers

    Loaders --> WebLoaders["Web Loaders"]:::py
    Loaders --> FileLoaders["File Loaders"]:::py
    Loaders --> CloudLoaders["Cloud Loaders"]:::py
    Loaders --> APILoaders["API Loaders"]:::py

    WebLoaders --> WebBase["WebBaseLoader"]:::py
    WebLoaders --> Cheerio["Cheerio Web"]:::py
    WebLoaders --> AsyncHTML["Async HTML"]:::py
    WebLoaders --> Firecrawl["Firecrawl"]:::py

    FileLoaders --> PDF["PDF"]:::py
    FileLoaders --> CSVFile["CSV"]:::py
    FileLoaders --> JSONFile["JSON"]:::py
    FileLoaders --> TextFile["Text"]:::py
    FileLoaders --> Markdown["Markdown"]:::py

    CloudLoaders --> S3["AWS S3"]:::py
    CloudLoaders --> AzureBlob["Azure Blob"]:::py
    CloudLoaders --> GCS["GCS"]:::py
    CloudLoaders --> HuaweiOBS["Huawei OBS"]:::py

    APILoaders --> GitHubAPI["GitHub"]:::py
    APILoaders --> GoogleDrive["Google Drive"]:::py
    APILoaders --> Notion["Notion"]:::py
    APILoaders --> Confluence["Confluence"]:::py

    Transformers --> HTML["HTML Transformers"]:::py
    Transformers --> Rerankers["Rerankers"]:::py
    Transformers --> Translations["Translations"]:::py
    Transformers --> Extractors["Property Extractors"]:::py

    Splitters --> Recursive["RecursiveCharacter"]:::py
    Splitters --> Character["Character"]:::py
    Splitters --> Token["Token Splitters"]:::py
    Splitters --> Code["Code Splitters"]:::py

    Embeddings --> OpenAIEmb["OpenAI"]:::py
    Embeddings --> CohereEmb["Cohere"]:::py
    Embeddings --> HuggingFaceEmb["Hugging Face"]:::py
    Embeddings --> GoogleEmb["Google"]:::py
    Embeddings --> VoyageEmb["Voyage AI"]:::py

    VectorStores --> Chroma["Chroma"]:::py
    VectorStores --> FAISS["FAISS"]:::py
    VectorStores --> Pinecone["Pinecone"]:::py
    VectorStores --> Qdrant["Qdrant"]:::py
    VectorStores --> Milvus["Milvus"]:::py
    VectorStores --> PGVector["PGVector"]:::py
    VectorStores --> Elastic["Elasticsearch"]:::py
    VectorStores --> Weaviate["Weaviate"]:::py

    Retrievers --> BM25["BM25Retriever"]:::py
    Retrievers --> AzureAISearch["Azure AI Search"]:::py
    Retrievers --> CohereRetriever["Cohere"]:::py
    Retrievers --> Tavily["Tavily"]:::py
    Retrievers --> KNN["KNN"]:::py
    Retrievers --> Wikipedia["Wikipedia"]:::py
    Retrievers --> PubMed["PubMed"]:::py

    LCRAG["LangChain RAG"]:::lc
    LGRAG["LangGraph Agentic RAG"]:::lg

    Retrievers -.->|"语义检索"| LCRAG
    Retrievers -.->|"智能路由"| LGRAG

    CrossRef1["002 LangChain Core - RAG/Retrieval"]:::xref
    CrossRef2["003 LangGraph - Agentic RAG"]:::xref
    CrossRef3["006 Model Integrations - Embeddings"]:::xref

    Loaders -.-> CrossRef1
    LGRAG -.-> CrossRef2
    Embeddings -.-> CrossRef3
```

## 关键统计

| 类别 | 数量 | 代表项 |
|------|------|--------|
| Document Loaders | 170+ | Web, PDF, CSV, JSON, S3, Azure, GCS, GitHub, Notion |
| Document Transformers | 19+ | HTML, Rerankers, Translations, Extractors |
| Text Splitters | 多种 | Recursive, Character, Token, Code |
| Embeddings | 86 | OpenAI, Cohere, Hugging Face, Google, Voyage AI |
| Vector Stores | 90+ | Chroma, FAISS, Pinecone, Qdrant, Milvus, PGVector |
| Retrievers | 72 | BM25, Azure AI Search, Cohere, Tavily |

## 数据管道说明

1. **Document Loaders**: 从各种数据源加载原始文档
   - Web Loaders: 网页抓取和爬虫
   - File Loaders: 本地文件系统
   - Cloud Loaders: 云存储服务
   - API Loaders: 第三方 API 集成

2. **Document Transformers**: 清洗和预处理文档
   - HTML 转换: 提取纯净文本
   - Rerankers: 重新排序内容
   - Translations: 多语言翻译
   - Extractors: 结构化数据提取

3. **Text Splitters**: 智能分块策略
   - RecursiveCharacter: 递归字符分割
   - Character: 固定字符数分割
   - Token: Token 数量分割
   - Code: 代码专用分割

4. **Embeddings**: 文本向量化
   - 提供商: OpenAI, Cohere, Hugging Face 等
   - 作为文本到向量的桥梁

5. **Vector Stores**: 向量数据库
   - 存储: 高效向量索引
   - 检索: 相似度搜索

6. **Retrievers**: 高级检索策略
   - 稠密检索: 向量相似度
   - 稀疏检索: BM25/TF-IDF
   - 混合检索: 结合多种方法
   - 重排序: 优化结果质量

## 关联地图

| 主题 | 关联地图 | 关联主题 |
|------|---------|---------|
| LangChain RAG | 002 LangChain Core | LC RAG, Retrieval Chain |
| LangGraph RAG | 003 LangGraph Core | Agentic RAG, Agent RAG |
| 模型集成 | 006 Model Integrations | Embeddings 提供商 |

## 相关 Wiki 页面

- [[document_loaders/]] Document Loaders 完整列表
- [[document_transformers/]] Document Transformers 列表
- [[text_splitters/]] Text Splitters 指南
- [[embeddings/]] Embeddings 集成列表
- [[vectorstores/]] Vector Stores 集成列表
- [[retrievers/]] Retrievers 集成列表
