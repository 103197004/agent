### 代码实现

import pandas as pd
import os
import psycopg2
from sqlalchemy import create_engine

# 步骤1：读取并合并CSV文件
file_paths = ['file1.csv', 'file2.csv', 'file3.csv', 'file4.csv', 'file5.csv', 'file6.csv']
dfs = [pd.read_csv(file) for file in file_paths]

# 合并所有DataFrame，并保留所有列
merged_df = pd.concat(dfs, axis=0, ignore_index=True)

# 步骤2：去除重复列
# 通过转置DataFrame并去除重复列，然后再转置回来
merged_df = merged_df.T.drop_duplicates().T

# 步骤3：将列名从中文重命名为英文
# 示例映射，请替换为实际的列名
column_mapping = {
    '列1': 'column1',
    '列2': 'column2',
    # 在此添加所有列的映射
}
merged_df.rename(columns=column_mapping, inplace=True)

# 步骤4：将合并后的DataFrame拆分成较小的文件
chunk_size = 10000  # 根据需要调整
output_dir = 'output_chunks'
os.makedirs(output_dir, exist_ok=True)

for i, chunk in enumerate(range(0, merged_df.shape[0], chunk_size)):
    chunk_df = merged_df.iloc[chunk:chunk + chunk_size]
    chunk_df.to_csv(f'{output_dir}/chunk_{i}.csv', index=False)

# 步骤5：插入到PostgreSQL数据库
# 数据库连接详情
db_config = {
    'dbname': 'your_dbname',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432'
}

# 创建连接引擎
engine = create_engine(f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}")

# 将每个数据块插入到数据库
for i, chunk in enumerate(range(0, merged_df.shape[0], chunk_size)):
    chunk_df = merged_df.iloc[chunk:chunk + chunk_size]
    chunk_df.to_sql('your_table_name', engine, if_exists='append', index=False)

print("数据插入完成。")

