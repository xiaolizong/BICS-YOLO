# 请你写出完成以下任务的代码，任务：给你一个txt文件，和一个储存图片的文件夹，请你根据txt文件找到与文件夹中图片名字第二个_之前一样的的所有图片，并将这些图片复制保存到一个新的文件夹中。
import os
import shutil

# 读取txt文件中的名称
txt_file = r'E:\lhb\465.txt'  # 替换为实际的txt文件路径
with open(txt_file, 'r') as file:
    names = [line.strip().split('_')[0:2] for line in file.readlines()]

# 设置原始图片文件夹和目标文件夹路径
source_folder = r'E:\lhb\114.465'  # 替换为实际的源文件夹路径
target_folder = r'E:\lhb\光谷三路pic'  # 替换为实际的目标文件夹路径

# 确保目标文件夹存在，如果不存在则创建
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 获取源文件夹中的所有图片文件名
image_files = [filename for filename in os.listdir(source_folder) if filename.endswith('.png')]

# 找到与txt文件中的名称相匹配的图片文件，并将其复制到目标文件夹中
for filename in image_files:
    for name_parts in names:
        if '_'.join(name_parts) in filename:
            source_path = os.path.join(source_folder, filename)
            target_path = os.path.join(target_folder, filename)
            shutil.copyfile(source_path, target_path)
            print(f"Copied {filename} to {target_folder}")
            break  # 找到匹配的名称就可以退出内循环