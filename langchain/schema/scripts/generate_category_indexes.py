#!/usr/bin/env python3
"""
LangChain Wiki 分类索引生成脚本

为 api/concepts/sources 目录生成分类索引文件。

使用方式:
    python generate_category_indexes.py
"""

import sys
import re
from pathlib import Path
from collections import defaultdict

WIKI_DIR = Path("D:/Project/AASelf/doc-wiki/langchain/wiki")
INDEX_DIR = WIKI_DIR / "index"


def extract_wiki_name_from_file(file_path):
    """从文件内容中提取 Wiki 名称"""
    try:
        content = file_path.read_text(encoding='utf-8')
        match = re.search(r'^name:\s*(.+)', content, re.MULTILINE)
        return match.group(1).strip() if match else file_path.stem
    except:
        return file_path.stem


def get_category_from_file(file_path):
    """从文件内容中提取分类"""
    try:
        content = file_path.read_text(encoding='utf-8')
        match = re.search(r'^category:\s*(.+)', content, re.MULTILINE)
        return match.group(1).strip() if match else 'sources'
    except:
        return 'sources'


def group_api_files():
    """将 API 文件按类型分组"""
    api_dir = WIKI_DIR / "api"
    if not api_dir.exists():
        return {}

    groups = defaultdict(list)

    for file in sorted(api_dir.glob("*.md")):
        name = extract_wiki_name_from_file(file)

        # 根据文件名前缀分组
        if name.startswith('python_integrations_chat_'):
            groups['聊天模型'].append(name)
        elif name.startswith('python_integrations_embeddings_'):
            groups['嵌入模型'].append(name)
        elif name.startswith('python_integrations_vectorstores_'):
            groups['向量存储'].append(name)
        elif name.startswith('python_integrations_retrievers_'):
            groups['检索器'].append(name)
        elif 'text_splitter' in name.lower():
            groups['文本分割'].append(name)
        elif name.startswith('python_integrations_'):
            groups['其他'].append(name)
        else:
            groups['其他'].append(name)

    return groups


def group_concept_files():
    """将概念文件按类型分组"""
    concepts_dir = WIKI_DIR / "concepts"
    if not concepts_dir.exists():
        return {}

    groups = defaultdict(list)

    for file in sorted(concepts_dir.glob("*.md")):
        name = extract_wiki_name_from_file(file)

        # 根据文件名前缀分组
        if name.startswith('langchain_'):
            groups['LangChain 核心'].append(name)
        elif name.startswith('langgraph_'):
            groups['LangGraph 核心'].append(name)
        elif 'agent' in name.lower():
            groups['Agent'].append(name)
        elif 'memory' in name.lower() or 'mem0' in name.lower():
            groups['记忆'].append(name)
        elif 'rag' in name.lower() or 'retrieval' in name.lower():
            groups['RAG'].append(name)
        elif 'stream' in name.lower():
            groups['流式'].append(name)
        else:
            groups['其他'].append(name)

    return groups


def group_source_files():
    """将源文件按类型分组"""
    sources_dir = WIKI_DIR / "sources"
    if not sources_dir.exists():
        return {}

    groups = defaultdict(list)

    for file in sorted(sources_dir.glob("*.md")):
        name = extract_wiki_name_from_file(file)

        # 根据文件名前缀分组
        if name.startswith('python_integrations_'):
            groups['Python 集成'].append(name)
        elif name.startswith('langchain_'):
            groups['LangChain'].append(name)
        elif name.startswith('langgraph_'):
            groups['LangGraph'].append(name)
        else:
            groups['其他'].append(name)

    return groups


def create_api_index():
    """创建 API 索引文件"""
    groups = group_api_files()
    total = sum(len(files) for files in groups.values())

    content = f"""# API 索引

本目录包含 {total} 个 API 相关页面。

## 📊 统计

"""

    # 添加统计信息
    for group_name, files in sorted(groups.items(), key=lambda x: len(x[1]), reverse=True):
        content += f"- {group_name}: {len(files)} 个\n"

    content += "\n"

    # 添加各组文件
    for group_name, files in sorted(groups.items()):
        if files:
            emoji = {
                '聊天模型': '💬',
                '嵌入模型': '🔢',
                '向量存储': '🗃️',
                '检索器': '🔍',
                '文本分割': '✂️',
                '链和解析': '⛓️',
                '记忆': '🧠',
            }.get(group_name, '📦')

            content += f"## {emoji} {group_name} ({len(files)})\n\n"
            for name in files:
                content += f"- [[{name}]]\n"
            content += "\n"

    # 写入文件
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    (INDEX_DIR / "api_index.md").write_text(content, encoding='utf-8')
    print(f"已生成 API 索引，共 {total} 个文件")


def create_concepts_index():
    """创建概念索引文件"""
    groups = group_concept_files()
    total = sum(len(files) for files in groups.values())

    content = f"""# 概念索引

本目录包含 {total} 个概念相关页面。

## 📊 统计

"""

    # 添加统计信息
    for group_name, files in sorted(groups.items(), key=lambda x: len(x[1]), reverse=True):
        content += f"- {group_name}: {len(files)} 个\n"

    content += "\n"

    # 添加各组文件
    group_order = ['LangChain 核心', 'LangGraph 核心', 'Agent', '记忆', 'RAG', '流式', '其他']
    for group_name in group_order:
        if group_name in groups and groups[group_name]:
            emoji = {
                'LangChain 核心': '🦜',
                'LangGraph 核心': '🔷',
                'Agent': '🤖',
                '记忆': '🧠',
                'RAG': '📚',
                '流式': '🌊',
            }.get(group_name, '📦')

            content += f"## {emoji} {group_name} ({len(groups[group_name])})\n\n"
            for name in groups[group_name]:
                content += f"- [[{name}]]\n"
            content += "\n"

    # 写入文件
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    (INDEX_DIR / "concepts_index.md").write_text(content, encoding='utf-8')
    print(f"已生成概念索引，共 {total} 个文件")


def create_sources_index():
    """创建源文档索引文件"""
    groups = group_source_files()
    total = sum(len(files) for files in groups.values())

    content = f"""# 源文档索引

本目录包含 {total} 个源文档索引页面。

## 📊 统计

"""

    # 添加统计信息
    for group_name, files in sorted(groups.items(), key=lambda x: len(x[1]), reverse=True):
        content += f"- {group_name}: {len(files)} 个\n"

    content += "\n"

    # 添加各组文件
    for group_name, files in sorted(groups.items()):
        if files:
            emoji = {
                'Python 集成': '🐍',
                'LangChain': '🦜',
                'LangGraph': '🔷',
            }.get(group_name, '📦')

            content += f"## {emoji} {group_name} ({len(files)})\n\n"
            for name in files[:50]:  # 限制显示数量
                content += f"- [[{name}]]\n"
            if len(files) > 50:
                content += f"- ... 还有 {len(files) - 50} 个\n"
            content += "\n"

    # 写入文件
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    (INDEX_DIR / "sources_index.md").write_text(content, encoding='utf-8')
    print(f"已生成源文档索引，共 {total} 个文件")


def create_main_index():
    """创建主索引文件"""
    categories = {
        'api': 'API 文档',
        'concepts': '概念文档',
        'sources': '源文档索引'
    }

    content = """# LangChain Wiki 主索引

欢迎使用 LangChain Wiki！这里包含了 LangChain、LangGraph 和 Python 集成的完整文档索引。

## 📚 文档分类

"""

    total = 0
    for cat, name in categories.items():
        cat_dir = WIKI_DIR / cat
        if cat_dir.exists():
            files = list(cat_dir.glob("*.md"))
            count = len(files)
            total += count

            emoji = {'api': '⚡', 'concepts': '💡', 'sources': '📄'}.get(cat, '📁')
            content += f"- {emoji} **[{name}](index/{cat}_index.md)**: {count} 个页面\n"

    content += f"\n**总计**: {total} 个页面\n\n"

    content += """## 🔍 快速导航

- [API 索引](index/api_index.md) - 查看所有 API 文档
- [概念索引](index/concepts_index.md) - 查看所有概念文档
- [源文档索引](index/sources_index.md) - 查看所有源文档

## 📖 使用说明

每个 Wiki 页面包含：
- 原始文档的链接
- 文档标题和描述
- 源文件路径信息

点击原始文档链接可查看完整内容。

---

*此索引由 `generate_category_indexes.py` 自动生成*
"""

    # 写入文件
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    (INDEX_DIR / "index.md").write_text(content, encoding='utf-8')
    print(f"已生成主索引")


if __name__ == "__main__":
    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("生成分类索引文件...\n")

    create_api_index()
    create_concepts_index()
    create_sources_index()
    create_main_index()

    print("\n所有索引文件生成完成！")
