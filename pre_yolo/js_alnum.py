# 请你写出完成以下任务的代码，任务：给你一个txt文件，要求从第一行开始将每一行空格前内容相同的行合并，并将需要合并的行中最后一个数字相加，生成一个新的txt文件。
def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    merged_lines = {}

    for line in lines:
        # 获取每一行空格前的内容和最后一个数字
        parts = line.strip().split()
        content = ' '.join(parts[:-1])
        last_number = int(parts[-1])

        # 如果内容已经在字典中，则累加最后一个数字
        if content in merged_lines:
            merged_lines[content] += last_number
        else:
            merged_lines[content] = last_number

    # 将合并后的内容写入输出文件
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for content, total_number in merged_lines.items():
            output_file.write(f"{content} {total_number}\n")


# 调用函数处理输入文件，并将结果写入输出文件
process_file('combined_data.txt', 'output.txt')
print("Processing complete. Results saved to output.txt")
