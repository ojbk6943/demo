# f = open("file2.txt",'w+')
# f.write("I love zhongguo\n")
# f.write("12345678\n")
# f.write("abcdefg")
list1=['1','1','1']
f = open("file2.txt",'a+')
f.writelines(list1)
