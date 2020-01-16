import re

list2=[]
list3=[]
list4=[]
list5=[]
fh=open('file1.txt')
list1=fh.readlines() #将文档转为列表
print(list1)
for i in list1:
    list2.append(i.strip())
    # list4.append(i.replace('\n', ""))
# print(list4)
print(list2)
for one in list2:
    a=re.split(r'[:;,\s]\s*', one)  #a是列表
    list3.append(a)
print(list3)
list4=[one for one in list3 if one !=['']]
print(list4)
for one in list4:
    n=[i for i in one if i !='']
    list5.append(n)
print(list5)
fh=open('file2.txt','a')
for i in list5:

     fh.write('{:>5s}{:>5s}{:>5s}{:>10s}{:>5s}{:>5s}{:>5s}'.format(i[0],':',i[1],';',i[2],':',i[3]+'\n'))
fh.close()

