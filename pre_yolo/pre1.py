# 请你写出完成以下任务的代码，任务：给你一个文件夹，里面有许多txt文件，要求将所有的txt文件只保留后四列数值并转成xlsx文件，文件名不变，保存在yolo文件夹中
import os
import pandas as pd

# 定义文件夹路径
folder_path = 'D://Experiennces//ultralytics-main//ultralytics-main//runs//detect//predict//labels'

# 创建一个yolo文件夹来存储结果
output_folder = 'yolo'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历文件夹中的每个txt文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        # 尝试读取txt文件
        try:
            # 读取txt文件
            data = pd.read_csv(file_path, sep='\t', header=None)
            # 检查数据是否为空
            if data.empty:
                # 如果数据为空，创建一个空白的DataFrame
                data = pd.DataFrame(columns=['Column 1', 'Column 2', 'Column 3', 'Column 4'])
        except pd.errors.EmptyDataError:
            # 如果出现EmptyDataError，则创建一个空白的DataFrame
            data = pd.DataFrame(columns=['Column 1', 'Column 2', 'Column 3', 'Column 4'])

        # 构造输出文件路径，保持文件名不变
        output_file_path = os.path.join(output_folder, file_name)
        # 将数据写入xlsx文件
        data.to_excel(output_file_path + '.xlsx', index=False)