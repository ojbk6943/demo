fh=open('file1.txt')
list1=fh.readlines()                    #将文档转为列表
# print(list1)
list2=[]
list3=[]
for one in list1:
    list2.append(one.strip())           #去掉换行符
# print(list2)
for one in list2:
    k=one.split(" ")
    list3.append(k)
# print(list3)
list4=[]
for one in list3:
    s=[i for i in one if i !=""]
    list4.append(s)
# print(list4)
list5=[i for i in list4 if i !=[]]
# print(list5)
list5[0]=['name:', 'Jack', ';', 'salary:', '12000']
list5[1]=['name:', 'Mike', ';', 'salary:', '12300']
# print(list5)
list5[3]=['name:', 'Tim', ';', 'salary:', '9000']
print(list5)
for i in list5:
     fh=open('file2.txt','a')
     fh.write('{:>5s}{:>5s}{:>5s}{:>5s}{:>10s}{:>5s}{:>5s}{:>5.0f}'.format(i[0],i[1],i[2],i[3],i[4],";","tax:",int(i[4])*0.9)+'\n')
     fh.close()


