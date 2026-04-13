# LangChain Wiki 脚本

这个目录包含用于构建和维护 LangChain Wiki 的脚本。

## 📁 核心脚本（2 个）

### build_wiki.py
**主构建脚本** - 为所有文档创建 Wiki 索引

```bash
# 完整构建（索引 + 分类索引）
python build_wiki.py

# 只生成文档索引
python build_wiki.py --index-only

# 只生成分类索引
python build_wiki.py --category
```

功能：
- 扫描 langchain、langgraph、python 目录下的所有 .mdx 文件
- 为每个文件创建 Wiki 索引页面
- 自动分类到 api/concepts/sources
- 生成分类索引文件

### verify_wiki.py
**验证和修复脚本** - 检查和修复链接问题

```bash
# 验证所有链接
python verify_wiki.py

# 验证并修复链接
python verify_wiki.py --fix

# 显示统计信息
python verify_wiki.py --stats
```

功能：
- 验证所有 Wiki 页面的原始文档链接
- 修复路径格式问题
- 显示统计信息（替代独立的 stats.py）

## 🔄 典型工作流程

### 初次构建
```bash
python build_wiki.py
```

### 更新 Wiki
```bash
# 1. 拉取最新文档
cd ../../raw && git pull

# 2. 重新构建
python build_wiki.py

# 3. 验证链接
python verify_wiki.py --fix
```

### 检查状态
```bash
python stats.py
python verify_wiki.py --stats
```

## 📊 Wiki 结构

```
wiki/
├── index/
│   ├── index.md          # 主索引
│   ├── api_index.md      # API 完整索引
│   ├── concepts_index.md # 概念完整索引
│   └── sources_index.md  # 源文档完整索引
├── api/                  # API 页面（406 个）
├── concepts/             # 概念页面（363 个）
└── sources/              # 源文档索引（1,751 个）
```

## ⚠️ 注意事项

1. **路径格式**：Windows 路径使用正斜杠 `/`
2. **编码**：所有文件使用 UTF-8 编码
3. **备份**：运行 build_wiki.py 前建议备份现有 Wiki
