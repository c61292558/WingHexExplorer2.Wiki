import os
import urllib.parse

# 指定要处理的目录和文件类型
base_path = 'markdown-pic'  # 替换为您的文件夹路径
markdown_files = [f for f in os.listdir(base_path) if f.endswith('.md')]

for md_file in markdown_files:
    file_path = os.path.join(base_path, md_file)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 找到所有的图片路径并进行解码
    # 这里假设图片的路径在markdown中都是类似的格式
    updated_content = content
    for line in content.splitlines():
        if '![' in line:
            start = line.find('(') + 1
            end = line.find(')', start)
            img_path = line[start:end]

            # 解码路径
            decoded_path = urllib.parse.unquote(img_path)
            # 重新编码为中文路径
            updated_path = os.path.join(base_path, decoded_path)

            # 替换内容中的路径
            updated_content = updated_content.replace(img_path, updated_path)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
