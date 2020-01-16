ageTable = '''
    诸葛亮, 28
    刘备, 48
    刘琦, 25
    赵云, 32
    张飞, 43
    关羽, 45
'''
#处理结果，将其取出空内容和空格，然后保存在tlist列表中
tmp = ageTable.splitlines()
agelist = []
for one in tmp:
    if one == "":
        continue
    else:
        tit = one.strip()
        agelist.append(tit)
#使用for循环，对于agelist中每个元素的值进行处理，保存在两个列表中g30代表年龄大于30，l30代表年龄小于30
g30 = []
l30 = []

#
for ageone in agelist:
    name,age = ageone.split(",")
    ageint = int(age.strip())
    if ageint >= 30:
        g30.append(ageone)
    else:
        l30.append(ageone)

print(g30)
print(l30)
