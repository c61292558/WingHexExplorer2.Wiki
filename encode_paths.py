import os
import glob
from urllib.parse import unquote

# 获取所有 Markdown 文件
md_files = glob.glob("*.md")

for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 使用 unquote 函数将 URL 编码还原为正常文本（如中文）
    import re
    content = re.sub(
        r'!\[(.*?)\]\((.*?)\)',
        lambda m: f'![{m.group(1)}]({unquote(m.group(2))})',
        content
    )

    # 写回文件
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("路径解码完成！")
