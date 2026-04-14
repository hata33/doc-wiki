#!/usr/bin/env python3
"""
测试层级索引查询
"""
import json

def load_index():
    with open('langchain/schema/scripts/docs_index.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def search_all_projects(index, keyword):
    """跨所有项目搜索"""
    results = []
    keyword = keyword.lower()

    for project, categories in index['projects'].items():
        for category, docs in categories.items():
            for doc_id, doc in docs.items():
                if (keyword in doc['title'].lower() or
                    keyword in doc.get('description', '').lower() or
                    any(keyword in kw.lower() for kw in doc['keywords'])):
                    results.append({
                        'project': project,
                        'category': category,
                        'doc_id': doc_id,
                        'doc': doc
                    })

    return results


def search_project(index, project_name, keyword):
    """在指定项目中搜索"""
    if project_name not in index['projects']:
        return []

    results = []
    keyword = keyword.lower()

    for category, docs in index['projects'][project_name].items():
        for doc_id, doc in docs.items():
            if (keyword in doc['title'].lower() or
                keyword in doc.get('description', '').lower() or
                any(keyword in kw.lower() for kw in doc['keywords'])):
                results.append({
                    'category': category,
                    'doc_id': doc_id,
                    'doc': doc
                })

    return results


def main():
    index = load_index()

    print("=" * 70)
    print("测试层级索引查询")
    print("=" * 70)

    # 场景1: 跨项目搜索 "stream"
    print("\n场景1: 跨项目搜索 'stream'")
    results = search_all_projects(index, 'stream')
    print(f"找到 {len(results)} 个相关文档:")
    for r in results[:5]:
        print(f"  [{r['project']}] {r['doc']['title']}")

    # 场景2: 在 langgraph 中搜索 "persist"
    print("\n场景2: 在 langgraph 中搜索 'persist'")
    results = search_project(index, 'langgraph', 'persist')
    print(f"找到 {len(results)} 个相关文档:")
    for r in results:
        print(f"  [{r['category']}] {r['doc']['title']}")

    # 场景3: 查找 langgraph 的错误文档
    print("\n场景3: 查找 langgraph 的错误文档")
    if 'errors' in index['projects']['langgraph']:
        errors = index['projects']['langgraph']['errors']
        print(f"找到 {len(errors)} 个错误文档:")
        for doc_id in list(errors.keys())[:5]:
            print(f"  - {doc_id}")

    # 场景4: 查找入门文档
    print("\n场景4: 查找所有项目的入门文档")
    for project, categories in index['projects'].items():
        if 'root' in categories:
            root_docs = categories['root']
            # 筛选可能的入门文档
            getting_started = [k for k in root_docs.keys() if 'overview' in k or 'install' in k or 'quickstart' in k]
            if getting_started:
                print(f"\n  {project}: {len(getting_started)} 个入门文档")
                for doc_id in getting_started[:3]:
                    print(f"    - {root_docs[doc_id]['title']}")

    print("\n" + "=" * 70)


if __name__ == '__main__':
    main()
