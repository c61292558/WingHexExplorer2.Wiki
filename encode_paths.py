import glob
import os

# 定义 GitHub Raw 文件链接前缀
GITHUB_RAW_PREFIX = "https://raw.githubusercontent.com/c61292558/WingHexExplorer2.Wiki/refs/heads/master/"

# 获取所有 Markdown 文件
md_files = glob.glob("*.md")

for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 找到所有图片路径并加上 GitHub 的完整 URL 前缀
    import re
    content = re.sub(
        r'!\[(.*?)\]\((.*?)\)',
        lambda m: f'![{m.group(1)}]({GITHUB_RAW_PREFIX}{m.group(2)})',
        content
    )

    # 写回文件
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("图片链接已更新为完整的 GitHub Raw 链接！")
