import os
import glob
from urllib.parse import quote

# 获取所有 Markdown 文件
md_files = glob.glob("*.md")

for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 处理每个路径，确保只进行一次编码
    # 使用正则表达式查找图片路径
    import re
    content = re.sub(
        r'!\[(.*?)\]\((.*?)\)',
        lambda m: f'![{m.group(1)}]({quote(m.group(2), safe="/")})',
        content
    )

    # 写回文件
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("路径编码完成！")
