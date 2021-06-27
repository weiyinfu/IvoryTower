import json
import os

#pip install python-docx
import docx

"""
解析若干个heading之间的内容作为诗歌内容
第一个Heading之前的内容是目录和序
"""


def show(paragraph):
    # 展示一个变量的非私有属性
    for i in dir(paragraph):
        if i.startswith("_") or i.startswith("add"):
            continue
        try:
            value = getattr(paragraph, i)
            print(i, value)
        except:
            pass


doc_path = os.path.join("..", "象牙塔集.docx")
doc = docx.Document(doc_path)
poem_list = []
now_poem = {}
for p in doc.paragraphs:
    print("=", p.text, p.style.name, p.style)
    if p.style.name == "Heading 1":
        if now_poem:
            poem_list.append(now_poem)
            now_poem['content'] = '\n'.join(now_poem['content'])
            now_poem = {}
        now_poem['title'] = p.text.strip()
        now_poem['content'] = []
    elif p.style.name == "Normal" and now_poem:
        now_poem['content'].append(p.text)
if now_poem.keys():
    now_poem['content'] = '\n'.join(now_poem['content'])
    poem_list.append(now_poem)
print(poem_list)
json.dump(poem_list, open("poem.json", "w", encoding='utf8'), ensure_ascii=0, indent=2)
