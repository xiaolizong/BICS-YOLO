# 请你写出完成以下任务的代码，任务：给你一个储存图片的文件夹，请将名称中带有_90_0和_270_0的文件复制到一个新的文件夹中。
import os
import shutil

# 设置源文件夹和目标文件夹路径
source_folder = r'E:\lhb\光谷四路pic'  # 替换为实际的源文件夹路径
target_folder = r'E:\lhb\光谷四路pic2'  # 替换为实际的目标文件夹路径

# 确保目标文件夹存在，如果不存在则创建
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 获取源文件夹中的所有图片文件名
image_files = [filename for filename in os.listdir(source_folder) if filename.endswith('.png')]

# 找到需要复制的图片文件，并将其复制到目标文件夹中
for filename in image_files:
    if '_90_0' in filename or '_270_0' in filename:
        source_path = os.path.join(source_folder, filename)
        target_path = os.path.join(target_folder, filename)
        shutil.copyfile(source_path, target_path)
        print(f"Copied {filename} to {target_folder}")
