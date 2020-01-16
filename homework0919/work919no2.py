ageTable = '''
    诸葛亮, 28
    刘备, 48
    刘琦, 25
    赵云, 32
    张飞, 43
    关羽, 45
'''

#把字符串转换为列表
list1 = ageTable.split("\n")
#print(list1)
one = ""
while one in list1:
    list1.remove("")
    #print(list1)
#print(list1)

#定义两个空列表
list1a = []
list1b = []

#循环分支嵌套比较年龄
for i in list1:
    name,age = i.split(",")
    age = int(age.strip())
    name = name.strip()
    if age >= 30:
        list1a.append(name)
    else:
        list1b.append(name)
#print(list1a)
#print(list1b)

print("大于等于30岁的人有：")
for ia in list1a:
    print(ia)

print("小于30岁的人有：")
for ib in list1b:
    print(ib)