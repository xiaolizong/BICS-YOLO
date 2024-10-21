import os

def process_folder(folder_path, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # 遍历文件夹中的所有文件
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and filename.endswith('.txt'):
                # 读取文件内容并处理每一行
                with open(file_path, 'r', encoding='utf-8') as input_file:
                    lines = input_file.readlines()
                    if len(lines) == 0:
                        # 如果文件没有数据，生成仅包括文件名的一行
                        output_file.write(f"{filename}\n")
                    else:
                        for line in lines:
                            parts = line.strip().split()
                            if len(parts) >= 4:
                                last_four_columns = ' '.join(parts[-4:])
                                output_file.write(f"{filename} {last_four_columns}\n")
                        # 如果文件有数据，生成每行数据的文件名和后四列数据的组合
                        # 如果文件没有数据，生成仅包括文件名的一行

# 调用函数处理文件夹中的所有文件，并将结果写入输出文件
process_folder(r'D:\Experiennces\ultralytics-main\angel\labels', 'output.txt')
print("Processing complete. Results saved to output.txt")
