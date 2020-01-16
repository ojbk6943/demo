# #如下是一些打开文件的例子
# # fp = open('C:\Users\EDZ\Desktop\软件测试学习资料\11.text')       #以只读方式打开文件
# fp = open('D:\11.text','r+')       #以写文件方式打开
# # fp = open('data','r+')     #r+读取 并且写入文件
# fh = open(r'D:\11.txt')
# st1 = fh.read()
# print(st1)
# fh.close()
# fp = open(r'D:\11.txt',"br")
# fp.seek(400,1)
# print(fp.tell())
# print(fp.read())

# a=fp.read()
# print(a)

# st1 = fp.readlines()
# print(st1)
# st2 = fp.readline()
# print(st2)
# st3 = fp.readline()
# print(st3)
# st4 = fp.readline()
# print(st4)
# st5 = fp.readline()
# print(st5)
# st6 = fp.readline()
# print(st6)
# st7 = fp.readline()
# print(st7)
# st8= fp.readline()
# print(st8)
# fp.close()
# dict1 = {'Google': 'www.google.com', 'baidu': 'www.baidu.com', 'biying': 'cn.bing.com/','sougou':'www.sogou.com'}
# for i in dict1:
#     # print(f"NAME:{i},URL:{dict1[i]}")
#     print('Name:%s,URL:%s' % (i, dict1[i]))
    # print(i)
# print(dict1)
# for name,url in dict1.items():
#     print('Name:%s,URL:%s'% (name,url))
# a=["jfdslka\n","2222222\n"]
# # list1=[]
# list2=[]
# for i in a:
#
#     list2.append(i.strip())
# print(list2)
    # print(b)
    # print(type(b))
# print(list2)
# list2=[ i for i in a ]
# print(list2)
