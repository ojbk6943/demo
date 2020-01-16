#CSV是一种以逗号分隔数值的文件类型，在数据库或电子表格中，常见的导入导出文件格式就是CSV格式，CSV格式存储数据通常以纯文本的方式存数数据表。

import csv
with open("h:\\test.csv") as f:
    rews= csv.reader(f)
    for rew in rews:
        print(rew)
