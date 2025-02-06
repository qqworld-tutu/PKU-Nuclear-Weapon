import csv
from pypinyin import lazy_pinyin, Style


def process_csv_with_pypinyin(input_file, output_file):
    try:
        with open(input_file, newline='', mode='r') as infile, \
                open(output_file, newline='', mode='w') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            # 遍历每一行数据
            for row in reader:
                print(1)
                if row:  # 确保行不为空
                    name = row[0]  # 假设名字在第一列
                    print(name)
                    if name:  # 确保名字不为空
                        # 提取名字的拼音首字母并大写
                        initials = ''.join([word[0].lower() for word in lazy_pinyin(name, style=Style.NORMAL)])
                    else:
                        initials = ""  # 如果名字为空，则拼音首字母为空字符串
                    # 确保行数据长度至少为4列
                    while len(row) < 4:
                        row.append("")  # 如果不足4列，添加空列
                    row[3] = initials  # 将拼音首字母写入第四列
                    writer.writerow(row)  # 写入新的行
        print(f"处理完成，结果已保存到 {output_file}")
    except Exception as e:
        print(f"处理CSV文件时出错：{e}")


input_csv = 'test.csv'  # 输入文件名
output_csv = 'test_res.csv'  # 输出文件名
process_csv_with_pypinyin(input_csv, output_csv)

import chardet

# def detect_encoding(file_path):
#     with open(file_path, 'rb') as f:
#         raw_data = f.read()
#         result = chardet.detect(raw_data)
#         return result['encoding']
#
# # input_csv = 'input.csv'
# encoding = detect_encoding(input_csv)
# print(f"文件编码：{encoding}")