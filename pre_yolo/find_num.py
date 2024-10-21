import os

# 获取脚本文件所在的目录
script_dir = os.path.dirname(__file__)

# 创建一个新文件夹用于存储结果
new_labels_dir = os.path.join(script_dir, r'D:\Experiennces\ultralytics-main\pre_yolo\武汉腾讯')
if not os.path.exists(new_labels_dir):
    os.makedirs(new_labels_dir)

# 遍历labels文件夹中的所有txt文件
labels_dir = os.path.join(script_dir, r'E:\lhb\代码\ultralytics-main\ultralytics-main\ultralytics-main\runs\detect\武汉腾讯\labels')
for filename in os.listdir(labels_dir):
    if filename.endswith('.txt'):
        # 统计每个txt文件中的行数
        with open(os.path.join(labels_dir, filename), 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)

        # 生成新的txt文件名
        new_filename = os.path.join(new_labels_dir, filename)

        # 将行数写入新的txt文件中
        with open(new_filename, 'w', encoding='utf-8') as new_file:
            new_file.write(f' {num_lines}')

        print(f'Processed {filename} and saved result to {new_filename}')
# import os
#
# # 创建一个新文件夹用于存储结果
# if not os.path.exists(r'E:\lhb\new_labels2'):
#     os.makedirs(r'E:\lhb\new_labels2')
#
# # 遍历labels文件夹中的所有txt文件
# for filename in os.listdir(r'D:\Experiennces\ultralytics-main\ultralytics-main\runs\detect\predict19\labels'):
#     if filename.endswith('.txt'):
#         # 获取文件名中第二个_之前的内容作为新文件名
#         parts = filename.split('_')
#         if len(parts) >= 2:
#             new_filename = '_'.join(parts[:2]) + '.txt'
#
#             # 统计每个txt文件中的行数
#             file_path = os.path.join(r'D:\Experiennces\ultralytics-main\ultralytics-main\runs\detect\predict19\labels', filename)
#             if os.path.exists(file_path):
#                 with open(file_path, 'r', encoding='utf-8') as file:
#                     lines = file.readlines()
#                     num_lines = len(lines)
#
#                 # 将行数写入新的txt文件中
#                 with open(os.path.join(r'E:\lhb\new_labels2', new_filename), 'w', encoding='utf-8') as new_file:
#                     new_file.write(f'The number of lines in {filename} is: {num_lines}\n')
#
#                 print(f'Processed {filename} and saved result to new file: {new_filename}')
#             else:
#                 print(f'File {filename} not found.')
#         else:
#             print(f'Invalid filename: {filename}')

