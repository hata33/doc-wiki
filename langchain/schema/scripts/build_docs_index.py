#!/usr/bin/env python3
"""
通用文档索引生成器
递归扫描目录，自动从目录结构提取分类

使用方式:
    1. 修改下面的配置常量（SOURCE_DIR 和 OUTPUT_FILE）
    2. 直接运行脚本: python build_docs_index.py

配置说明:
    - SOURCE_DIR: 要扫描的源文档目录（绝对或相对路径）
    - OUTPUT_FILE: 输出的索引文件路径（绝对或相对路径）
"""
import json
import os
from pathlib import Path
import re

# ==================== 配置区域 ====================
# 修改这里的配置来适应你的需求

# 源文档目录（绝对路径或相对于项目根目录的相对路径）
SOURCE_DIR = "langchain/raw/src/oss"

# 输出索引文件（绝对路径或相对路径）
OUTPUT_FILE = "langchain/schema/scripts/docs_index.json"

# ==================================================


def extract_title(content, file_stem):
    """提取标题"""
    match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return file_stem.replace('-', ' ').title()


def extract_description(content):
    """提取描述（第一段话）"""
    content = re.sub(r'^---.+?---\n', '', content, flags=re.DOTALL)
    content = re.sub(r'^import .+?\n', '', content, flags=re.MULTILINE)
    match = re.search(r'^(.+?)(?:\n\n|\n#|\Z)', content, re.DOTALL)
    if match:
        desc = match.group(1).strip()
        desc = re.sub(r'\s+', ' ', desc)
        desc = re.sub(r'<[^>]+>', '', desc)
        desc = re.sub(r'\|', '', desc)
        desc = desc.strip()
        if len(desc) > 200:
            desc = desc[:197] + "..."
        return desc
    return ""


def extract_keywords(content, file_stem):
    """提取关键词"""
    keywords = []
    keywords.extend(file_stem.replace('-', ' ').split('_'))
    title_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).lower()
        keywords.extend(re.findall(r'\w+', title))
    return list(set(keywords))[:10]


def build_index(source_dir):
    """递归构建索引"""
    source_dir = Path(source_dir).resolve()
    project_root = Path(__file__).parent.parent.parent.parent.resolve()

    if not source_dir.exists():
        print(f"错误：目录不存在: {source_dir}")
        return None

    index = {
        '_meta': {
            'description': 'LangChain 生态文档索引',
            'source_dir': str(source_dir),
            'structure': '层级结构'
        },
        'projects': {}
    }

    total_docs = 0

    # 扫描一级子目录（项目）
    for project_dir in sorted(source_dir.iterdir()):
        if not project_dir.is_dir():
            continue

        project_name = project_dir.name
        index['projects'][project_name] = {}

        # 递归扫描该项目的所有 .mdx 文件
        for md_file in project_dir.rglob('*.mdx'):
            try:
                content = md_file.read_text(encoding='utf-8')
            except:
                continue

            file_stem = md_file.stem
            rel_path_from_project = md_file.relative_to(project_dir)

            # 从路径提取分类
            if len(rel_path_from_project.parts) == 1:
                # 文件在项目根目录
                category = "root"
            else:
                # 文件在子目录中
                category = rel_path_from_project.parts[0]

            # 提取信息
            title = extract_title(content, file_stem)
            description = extract_description(content)
            keywords = extract_keywords(content, file_stem)
            rel_path = md_file.relative_to(project_root)

            # 添加到索引
            doc_id = file_stem

            # 如果分类不存在，创建它
            if category not in index['projects'][project_name]:
                index['projects'][project_name][category] = {}

            index['projects'][project_name][category][doc_id] = {
                'file': str(rel_path).replace('\\', '/'),
                'title': title,
                'description': description,
                'keywords': keywords
            }

            total_docs += 1

    index['_meta']['total_docs'] = total_docs
    return index


def main():
    # 计算项目根目录（脚本向上4级到项目根目录）
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent.parent.parent

    # 解析源目录
    source_dir = Path(SOURCE_DIR)
    if not source_dir.is_absolute():
        source_dir = project_root / SOURCE_DIR

    # 解析输出文件
    output_path = Path(OUTPUT_FILE)
    if not output_path.is_absolute():
        output_path = project_root / OUTPUT_FILE

    print(f"项目根目录: {project_root}")
    print(f"扫描目录: {source_dir}")
    print(f"输出文件: {output_path}")

    index = build_index(str(source_dir))

    if index is None:
        print("错误：无法生成索引")
        return

    # 保存索引
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"\n索引已生成: {output_path}")
    print(f"总计: {index['_meta']['total_docs']} 个文档")

    # 显示项目统计
    print(f"\n项目统计:")
    for project, categories in index['projects'].items():
        doc_count = sum(len(docs) for docs in categories.values())
        category_count = len(categories)
        print(f"  {project}: {doc_count} 个文档, {category_count} 个分类")


if __name__ == '__main__':
    main()
