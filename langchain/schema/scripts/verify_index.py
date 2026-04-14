#!/usr/bin/env python3
import json

with open('langchain/schema/scripts/docs_index.json', 'r', encoding='utf-8') as f:
    idx = json.load(f)

print('=== LangGraph 层级结构 ===')
lg = idx['projects']['langgraph']
print('一级分类:', list(lg.keys()))
print('\nroot 分类文档数:', len(lg['root']))
print('\nerrors 分类文档数:', len(lg['errors']))
print('\nerrors 下的文档:', list(lg['errors'].keys())[:5])

print('\n=== streaming 文档信息 ===')
streaming = lg['root']['streaming']
print(f"标题: {streaming['title']}")
print(f"描述: {streaming['description'][:100]}...")
print(f"关键词: {streaming['keywords']}")
