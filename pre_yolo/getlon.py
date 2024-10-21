# 请你写出完成以下任务的代码，任务：给你一个文件夹，里面是1225个png图片，要求你提取他们的文件名称，并输出为1225个txt文件，并储存在txt文件夹内。
import os

# 设置文件夹路径
folder_path = r'E:\lhb\114.465'  # 替换为实际的文件夹路径

# 获取文件夹中的所有png图片文件名
png_files = [filename for filename in os.listdir(folder_path) if filename.endswith('.png')]

# 提取文件名的第二个_之前的部分作为名称
file_names = ['_'.join(filename.split('_')[:2]) for filename in png_files]

# 按名称排序
file_names.sort()

# 创建并写入txt文件
with open(r'E:\lhb\114.465.txt', 'w') as txt_file:
    for idx, name in enumerate(file_names, start=1):
        txt_file.write(f"{idx}: {name}\n")
