import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('相交2.xlsx', header=None)

# 对第四列（索引为3）进行分组合并，第三列（索引为2）进行求和
grouped = df.groupby(df.iloc[:, 3]).agg({2: 'sum'}).reset_index()

# 合并其他列的数据（保持不变）
for col in range(len(df.columns)):
    if col not in [2, 3]:  # 排除第三列和第四列
        grouped[col] = df.groupby(df.iloc[:, 3]).nth(0).iloc[:, col].tolist()

# 保存结果
grouped.to_excel('相交result.xlsx', index=False)
# import pandas as pd
#
# # 读取 Excel 文件
# df = pd.read_excel('相交end.xlsx', header=None)
#
# # 对第一列进行分组合并，同时计算每组相同项的个数
# grouped = df.groupby(df.iloc[:, 0]).size().reset_index(name='num')
#
# # 合并其他列的数据（保持不变）
# for col in range(1, len(df.columns)):
#     grouped[col] = df.groupby(df.iloc[:, 0]).nth(0).iloc[:, col].tolist()
#
# # 保存结果
# grouped.to_excel('result.xlsx', index=False)


