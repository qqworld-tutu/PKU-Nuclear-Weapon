# 本程序用于获取北大所有的单位

import re

# 读取整个文件内容
with open('results.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 使用正则表达式查找所有匹配的文本
pattern = r'class="ng-scope ng-binding">\s*(.*?)\s*</li>'
matches = re.findall(pattern, content, re.DOTALL)

# 将提取的文本写入新文件
with open('extracted_results.txt', 'w', encoding='utf-8') as file:
    for match in matches:
        file.write(match + '\n')