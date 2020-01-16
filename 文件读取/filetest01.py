fh = open("file1.txt","r")
fh.seek(2)
# print(fh.tell())
print(fh.read())
fh.seek(5)
# print(fh.tell())
print(fh.read())
fh.close()

# fh = open("file11.txt","a+")      #缺省只读方式打开
# fh.write("\nhelloword")
# fh.close()                  #关闭