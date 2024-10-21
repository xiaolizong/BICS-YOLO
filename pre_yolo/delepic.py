import os
import shutil

def remove_duplicate_files(folder_a, folder_b, folder_c):
    # 创建文件夹C
    if not os.path.exists(folder_c):
        os.makedirs(folder_c)

    # 复制文件夹B中的内容到文件夹C
    for root, dirs, files in os.walk(folder_b):
        for file in files:
            source_file = os.path.join(root, file)
            destination_file = os.path.join(folder_c, os.path.relpath(source_file, folder_b))
            if not os.path.exists(os.path.dirname(destination_file)):
                os.makedirs(os.path.dirname(destination_file))
            shutil.copy(source_file, destination_file)

    # 删除文件夹C中与文件夹A重复的文件
    for root, dirs, files in os.walk(folder_a):
        for file in files:
            source_file = os.path.join(root, file)
            relative_path = os.path.relpath(source_file, folder_a)
            duplicate_file = os.path.join(folder_c, relative_path)
            if os.path.exists(duplicate_file):
                os.remove(duplicate_file)

# 文件夹A和B的路径
folder_a = r"E:\lhb\代码\ultralytics-main\ultralytics-main\ultralytics-main\runs\detect\第五次"
folder_b = r"E:\街景\lhb\第五次"
# 文件夹C的路径
folder_c = r"E:\街景\lhb\第六2次"

remove_duplicate_files(folder_a, folder_b, folder_c)
