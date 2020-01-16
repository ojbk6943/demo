import csv

#此csv文件是一个文本文件，并非二进制文件，使用rt
with open("h:/test.csv",'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)