fh = open("tmp","w")

#查看一下文件指针所在的位置
print(fh.tell())

# #文件写入
# fh.write("my name is tom")

#立刻写入磁盘
fh.flush()

