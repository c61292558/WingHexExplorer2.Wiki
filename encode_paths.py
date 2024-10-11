import os
import re
import urllib.parse

# 函数：对 .md 文件中的中文路径进行 URL 编码
def url_encode_chinese_paths(md_file):
    # 匹配中文字符的正则表达式
    chinese_char_pattern = re.compile(r'[\u4e00-\u9fff]+')

    # 读取 .md 文件内容
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # 查找 Markdown 中的图片路径并处理
    new_content = content
    for match in re.findall(r'!\[.*?\]\((.*?)\)', content):
        # 如果路径中含有中文字符
        if chinese_char_pattern.search(match):
            # 对路径进行 URL 编码
            encoded_path = urllib.parse.quote(match)
            # 替换原路径为编码后的路径
            new_content = new_content.replace(match, encoded_path)

    # 如果内容有变化，则写回文件
    if new_content != content:
        with open(md_file, 'w', encoding='utf-8') as file:
            file.write(new_content)

# 函数：遍历目录查找所有 .md 文件
def process_all_md_files(directory='.'):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_file_path = os.path.join(root, file)
                url_encode_chinese_paths(md_file_path)

# 脚本主入口
if __name__ == '__main__':
    process_all_md_files()
