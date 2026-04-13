#!/usr/bin/env python3
"""
LangChain Wiki 验证和修复脚本

验证所有 Wiki 页面的原始文档链接是否有效，并修复常见问题。

使用方式:
    python verify_wiki.py              # 验证所有链接
    python verify_wiki.py --fix        # 验证并修复链接
    python verify_wiki.py --stats      # 只显示统计信息
"""

import sys
import re
from pathlib import Path

WIKI_DIR = Path("D:/Project/AASelf/doc-wiki/langchain/wiki")
RAW_DIR = Path("D:/Project/AASelf/doc-wiki/langchain/raw")


def verify_links():
    """验证所有 Wiki 页面的链接"""
    print("验证 Wiki 页面链接...\n")

    # 扫描所有 Wiki 文件
    wiki_files = []
    for category in ['api', 'concepts', 'sources']:
        category_dir = WIKI_DIR / category
        if category_dir.exists():
            wiki_files.extend(category_dir.glob("*.md"))

    print(f"找到 {len(wiki_files)} 个 Wiki 文件\n")

    valid = 0
    invalid = 0
    missing_source = []

    for wiki_file in wiki_files:
        try:
            content = wiki_file.read_text(encoding='utf-8')

            # 提取 source 路径
            source_match = re.search(r'^source:\s*(.+)', content, re.MULTILINE)
            if not source_match:
                missing_source.append(wiki_file.name)
                invalid += 1
                continue

            source_path = source_match.group(1).strip()

            # 验证原始文档是否存在
            raw_file = RAW_DIR / "src/oss" / source_path
            if raw_file.exists():
                valid += 1
            else:
                missing_source.append(f"{wiki_file.name} -> {source_path}")
                invalid += 1

        except Exception as e:
            print(f"[错误] {wiki_file.name}: {e}")
            invalid += 1

    print(f"验证完成！\n")
    print(f"有效链接: {valid}")
    print(f"无效链接: {invalid}")

    if missing_source:
        print(f"\n缺失的原始文档（{len(missing_source)} 个）:")
        for item in missing_source[:20]:
            print(f"  - {item}")
        if len(missing_source) > 20:
            print(f"  ... 还有 {len(missing_source) - 20} 个")

    return valid, invalid


def fix_source_links():
    """修复所有 Wiki 页面的 source 路径"""
    print("修复 Wiki 页面链接...\n")

    # 扫描所有 Wiki 文件
    wiki_files = []
    for category in ['api', 'concepts', 'sources']:
        category_dir = WIKI_DIR / category
        if category_dir.exists():
            wiki_files.extend(category_dir.glob("*.md"))

    print(f"找到 {len(wiki_files)} 个 Wiki 文件\n")

    fixed = 0
    errors = 0

    for wiki_file in wiki_files:
        try:
            content = wiki_file.read_text(encoding='utf-8')

            # 修复 1: 移除 source 中的 raw/ 前缀
            content_new = re.sub(
                r'^source:\s*raw/src/oss/',
                'source: ',
                content,
                flags=re.MULTILINE
            )

            # 修复 2: 移除 source 中的 src/oss/ 前缀
            content_new = re.sub(
                r'^source:\s*src/oss/',
                'source: ',
                content_new,
                flags=re.MULTILINE
            )

            # 修复 3: 修复原始文档链接中的路径
            content_new = re.sub(
                r'\[\`([^`]+)\`\]\(\.\.\/\.\.\/raw\/src\/oss\/',
                r'[`\1`](../../raw/',
                content_new
            )

            # 修复 4: 移除多余的 raw/ 前缀
            content_new = re.sub(
                r'\[\`([^`]+)\`\]\(\.\.\/\.\.\/raw\/raw\/',
                r'[`\1`](../../raw/',
                content_new
            )

            if content != content_new:
                wiki_file.write_text(content_new, encoding='utf-8')
                fixed += 1

        except Exception as e:
            print(f"[错误] {wiki_file.name}: {e}")
            errors += 1

    print(f"修复完成！\n")
    print(f"修复文件: {fixed} 个")
    print(f"错误: {errors} 个")


def show_stats():
    """显示统计信息"""
    print("\n各分类文件分布:\n")

    categories = {
        'api': 'API 文档',
        'concepts': '概念文档',
        'sources': '源文档索引'
    }

    total = 0
    for cat, name in categories.items():
        cat_dir = WIKI_DIR / cat
        if cat_dir.exists():
            files = list(cat_dir.glob("*.md"))
            print(f"{name} ({cat}): {len(files)} 个文件")
            total += len(files)

    print(f"\n总计: {total} 个文件")


if __name__ == "__main__":
    import argparse

    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    parser = argparse.ArgumentParser(description='验证和修复 LangChain Wiki')
    parser.add_argument('--fix', action='store_true', help='修复链接问题')
    parser.add_argument('--stats', action='store_true', help='只显示统计信息')

    args = parser.parse_args()

    if args.stats:
        show_stats()
    elif args.fix:
        fix_source_links()
        verify_links()
        show_stats()
    else:
        verify_links()
        show_stats()
