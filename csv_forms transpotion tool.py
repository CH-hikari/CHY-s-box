import csv

def transpose_csv(input_file, output_file):
    # 读取CSV文件
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    
    # 转置数据
    transposed_data = list(zip(*data))
    
    # 写入转置后的数据到新的CSV文件
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(transposed_data)

# 使用示例
input_file = 'NAME.csv'  # 输入的CSV文件名
output_file = 'NEW_NAME.csv'  # 输出的转置后的CSV文件名
transpose_csv(input_file, output_file)
