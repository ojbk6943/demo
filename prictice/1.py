ageTable = '''
    诸葛亮, 28
    刘备, 48
    刘琦, 25
    赵云, 32
    张飞, 43
    关羽, 45
'''
list1=[]
list11=[]
list111=[]
list1111=[]
lista=[]
listb=[]
list1=ageTable.split("\n")  #以换行符切割字符串生成列表
#print(list1)
for one in list1:           #删除每个字符串中头尾的空格
    a=one.strip()
    list11.append(a)
#print(list11)
list111=list11[1:7]         #去除首尾的空格
#print(list111)
for one in list111:
    name,age=one.split(",")
    age=int(age.strip())
    name=name.strip()
    if age>=30:
        lista.append(name)
    else:
        listb.append(name)
print("大于30岁的人有:")
for one in lista:
    print (one)

print("小于30岁的人有:")
for one in listb:
    print (one)