with open("file1.txt","r") as a,open("file2.txt","r") as b:
    fc = a.read(2)
    print(fc)

#执行结束时，系统自动调用f.close()