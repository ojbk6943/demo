#支持多个文件的打开
with open("file1.txt") as file1,open("file2.txt","w") as file2:
    fc = file1.read()
    file2.write(fc)