import os

# 创建一个新文件来保存整合后的数据
output_file = open('武汉腾讯combine.txt', 'w', encoding='utf-8')

# 遍历labels文件夹中的所有txt文件
for filename in os.listdir('武汉腾讯'):
    if filename.endswith('.txt'):
        # 写入文件名到新文件中
        output_file.write(f'{filename} ')

        # 打开当前txt文件，并将其内容写入新文件中
        with open(os.path.join('武汉腾讯', filename), 'r', encoding='utf-8') as file:
            content = file.read()
            output_file.write(content.strip())
            output_file.write('\n')  # 在每个文件的内容之间添加空行

# 关闭新文件
output_file.close()

print('Combined data saved to combined_data.txt')
