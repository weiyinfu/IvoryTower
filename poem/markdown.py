"""
根据JSON生成markdown
"""

import json

a = json.load(open("poem.json", encoding='utf8'))
s = []
for poem in a:
    s.append(f"# {poem['title']}")
    for line in poem['content'].splitlines():
        s.append(f"{line}  ")
    s.append('\n')
open("poem.md", 'w').write('\n'.join(s))
