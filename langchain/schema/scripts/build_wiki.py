#!/usr/bin/env python3
"""
LangChain Wiki 构建脚本

为 langchain、langgraph、python 目录下的所有文件创建 Wiki 索引。
这是主要的数据导入脚本，运行后会生成完整的 Wiki 结构。

使用方式:
    python build_wiki.py              # 完整构建（索引 + 分类索引）
    python build_wiki.py --index-only # 只生成文档索引
    python build_wiki.py --category   # 只生成分类索引
"""

import sys
from pathlib import Path

# 目录路径
RAW_DIR = Path("D:/Project/AASelf/doc-wiki/langchain/raw/src/oss")
WIKI_DIR = Path("D:/Project/AASelf/doc-wiki/langchain/wiki")


def get_wiki_name(source_path):
    """基于源文件路径生成唯一的 Wiki 名称"""
    rel_path = source_path.relative_to(RAW_DIR)
    path_str = str(rel_path).replace('\\', '/')

    # 移除 .mdx 扩展名
    path_str = path_str[:-4] if path_str.endswith('.mdx') else path_str

    # 转换为有效的文件名
    name = path_str.replace('/', '_').replace('-', '_')

    # 确保名称不以数字开头
    if name[0].isdigit():
        name = 'file_' + name

    return name


def determine_category(source_path):
    """根据源文件路径确定 Wiki 分类"""
    path_str = str(source_path).replace('\\', '/')

    # python/integrations 目录
    if 'python/integrations/chat/' in path_str:
        return 'api'
    elif 'python/integrations/embeddings/' in path_str:
        return 'api'
    elif 'python/integrations/vectorstores/' in path_str:
        return 'api'
    elif 'python/integrations/retrievers/' in path_str:
        return 'api'
    elif 'python/integrations/' in path_str:
        return 'sources'
    # langchain 核心文档
    elif 'langchain/' in path_str:
        return 'concepts'
    # langgraph 核心文档
    elif 'langgraph/' in path_str:
        return 'concepts'
    else:
        return 'sources'


def extract_title(content, source_path):
    """从内容中提取标题"""
    import re

    # 尝试提取 title
    title_match = re.search(r'^title:\s*"(.+?)"', content, re.MULTILINE)
    if title_match:
        return title_match.group(1)

    # 如果没有 title，使用侧边栏标题
    sidebar_match = re.search(r'^sidebarTitle:\s*"(.+?)"', content, re.MULTILINE)
    if sidebar_match:
        return sidebar_match.group(1)

    # 使用文件名作为标题
    return source_path.stem.replace('_', ' ').replace('-', ' ').title()


def extract_description(content):
    """从内容中提取描述"""
    import re

    desc_match = re.search(r'^description:\s*"(.+?)"', content, re.MULTILINE)
    return desc_match.group(1) if desc_match else ""


def create_wiki_content(source_file):
    """创建 Wiki 内容"""
    try:
        content = source_file.read_text(encoding='utf-8')
    except (OSError, UnicodeDecodeError) as e:
        print(f"[警告] 无法读取文件 {source_file.name}: {e}")
        content = ""

    title = extract_title(content, source_file)
    description = extract_description(content)
    source_path = source_file.relative_to(RAW_DIR).as_posix()
    category = determine_category(source_file)
    name = get_wiki_name(source_file)

    # 构建 Wiki 内容
    wiki_content = f"""---
name: {name}
category: {category}
source: {source_path}
---

## 描述

{title} - {description if description else '原始文档索引'}

## 原始文档

- **主文档**: [`{source_path}`](../../raw/{source_path})

## 文档信息

"""

    # 添加元信息
    if title:
        wiki_content += f"- **标题**: {title}\n"
    if description:
        wiki_content += f"- **描述**: {description}\n"

    # 添加路径信息
    wiki_content += f"- **源路径**: `{source_path}`\n"

    wiki_content += "\n## 说明\n\n"
    wiki_content += "这是原始文档的索引页面。点击上方链接查看完整文档内容。\n\n"
    wiki_content += "## 相关页面\n\n"
    wiki_content += "- 查看原始文档获取完整信息、示例和配置选项\n"

    return wiki_content, category, name


def build_docs_index():
    """为所有文档创建索引"""
    import sys

    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("为所有文件创建 Wiki 索引...\n")

    # 扫描所有目标目录
    all_files = []

    # langchain 目录
    langchain_files = list((RAW_DIR / "langchain").rglob("*.mdx"))
    all_files.extend(langchain_files)

    # langgraph 目录
    langgraph_files = list((RAW_DIR / "langgraph").rglob("*.mdx"))
    all_files.extend(langgraph_files)

    # python 目录
    python_files = list((RAW_DIR / "python").rglob("*.mdx"))
    all_files.extend(python_files)

    print(f"找到 {len(all_files)} 个文件\n")

    created = 0
    errors = 0

    for i, source_file in enumerate(all_files):
        if i % 100 == 0:
            print(f"处理进度: {i}/{len(all_files)} ({i*100//len(all_files)}%)")

        try:
            # 创建 Wiki 内容
            wiki_content, category, name = create_wiki_content(source_file)

            # 确定 Wiki 文件路径
            if category == 'api':
                wiki_file = WIKI_DIR / "api" / f"{name}.md"
            elif category == 'concepts':
                wiki_file = WIKI_DIR / "concepts" / f"{name}.md"
            else:
                wiki_file = WIKI_DIR / "sources" / f"{name}.md"

            # 创建目录
            wiki_file.parent.mkdir(parents=True, exist_ok=True)

            # 写入文件
            wiki_file.write_text(wiki_content, encoding='utf-8')

            created += 1

        except Exception as e:
            errors += 1
            print(f"[错误] {source_file.relative_to(RAW_DIR)}: {e}")

    print(f"\n完成！")
    print(f"创建: {created} 个文件")
    print(f"错误: {errors} 个文件")

    # 统计
    total_api = len(list((WIKI_DIR / "api").glob("*.md"))) if (WIKI_DIR / "api").exists() else 0
    total_concepts = len(list((WIKI_DIR / "concepts").glob("*.md"))) if (WIKI_DIR / "concepts").exists() else 0
    total_sources = len(list((WIKI_DIR / "sources").glob("*.md"))) if (WIKI_DIR / "sources").exists() else 0

    print(f"\n当前 Wiki 统计:")
    print(f"  API: {total_api}")
    print(f"  Concepts: {total_concepts}")
    print(f"  Sources: {total_sources}")
    print(f"  总计: {total_api + total_concepts + total_sources}")


def build_category_indexes():
    """生成分类索引文件"""
    import subprocess
    import sys

    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("\n生成分类索引文件...\n")

    # 执行 generate_category_indexes.py 脚本
    script_path = Path(__file__).parent / "generate_category_indexes.py"
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(script_path.parent)
    )

    if result.returncode == 0:
        print("分类索引生成完成！")
    else:
        print(f"分类索引生成失败，返回码: {result.returncode}")


if __name__ == "__main__":
    import argparse

    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    parser = argparse.ArgumentParser(description='构建 LangChain Wiki')
    parser.add_argument('--index-only', action='store_true', help='只生成文档索引')
    parser.add_argument('--category', action='store_true', help='只生成分类索引')

    args = parser.parse_args()

    if args.category:
        # 只生成分类索引
        build_category_indexes()
    elif args.index_only:
        # 只生成文档索引
        build_docs_index()
    else:
        # 完整构建
        build_docs_index()
        build_category_indexes()
