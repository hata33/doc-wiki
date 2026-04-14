#!/usr/bin/env python3
import json

with open('langchain/schema/scripts/docs_index.json', 'r', encoding='utf-8') as f:
    idx = json.load(f)

print(f'索引文件存在，文档数: {idx["_meta"]["total_docs"]}')
print(f'项目数: {len(idx["projects"])}')
