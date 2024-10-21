import os

def calculate_bear(angle, x1, y1, x2, y2):
    if (x1 + x2) / 2 < 240:
        bear = float(angle) - (480 - (x1 + x2) / 2) * (90 / 480)
        if bear < 0:
            return bear + 360
        else:
            return bear
    else:
        bear = float(angle) + ((x1 + x2) / 2 - 240) * (90 / 480)
        if bear > 360:
            return bear - 360
        else:
            return bear

def process_folder(folder_path, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # 遍历文件夹中的所有文件
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and filename.endswith('.txt'):
                # 获取文件名中第三个 '_' 前的数值作为角度值
                angle = filename.split('_')[2]
                # 读取文件内容并处理每一行
                with open(file_path, 'r', encoding='utf-8') as input_file:
                    lines = input_file.readlines()
                    if len(lines) == 0:
                        output_file.write(f"{filename}\n")
                    else:
                        for line in lines:
                            parts = line.strip().split()
                            if len(parts) >= 6:
                                category = parts[0]
                                confidence = parts[1]
                                x1 = parts[2]
                                y1 = parts[3]
                                x2 = parts[4]
                                y2 = parts[5]
                                bear = calculate_bear(angle, float(x1), float(y1), float(x2), float(y2))
                                output_file.write(f"{filename} {category} {confidence} {x1} {y1} {x2} {y2} {bear}\n")
            elif os.path.isfile(file_path) and filename.endswith('.txt'):
                output_file.write(f"{filename}\n")

# 调用函数处理文件夹中的所有文件，并将结果写入输出文件
process_folder(r'D:\Experiennces\ultralytics-main\angel\xyxy\labels', '光谷3路bear.txt')
print("Processing complete. Results saved to bear.txt")
