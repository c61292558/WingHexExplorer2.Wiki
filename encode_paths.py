import os
import glob

# 获取所有 Markdown 文件
md_files = glob.glob("*.md")

for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 在这里进行路径的编码
    # 假设您只需要编码 markdown 文件中的图片路径
    # 这里您可以使用 urllib.parse.quote 对路径进行编码
    from urllib.parse import quote

    # 处理每个路径
    # 这个正则表达式会查找 markdown 中的路径
    import re
    content = re.sub(r'!\[(.*?)\]\((.*?)\)', lambda m: f'![{m.group(1)}]({quote(m.group(2))})', content)

    # 写回文件
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("路径编码完成！")
