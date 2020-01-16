import csv
list1 = ['1', '2','3','4','5']

outfile = 'h:/test.csv'
out = open(outfile, 'a')
csv_writer = csv.writer(out)       #指定写入的文件
csv_writer.writerow(dict1)          #写入文件的内容
#可能遇到的问题：直接使用这种写法会导致文件每一行后面会多一个空行。
# out = open(outfile, 'a', newline='')
# csv_writer = csv.writer(out)
# csv_writer.writerow(list1)