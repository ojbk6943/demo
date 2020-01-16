#使用a模式打来，追加模式，文件指针最后位置。直接添加写入内容
fh = open("tmp1","a")
names = ["\ntom\n","root"]
fh.writelines(names)
print(fh)
fh.close()