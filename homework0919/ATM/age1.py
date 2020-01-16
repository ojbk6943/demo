ageTable = '''
    诸葛亮, 28
    刘备, 48
    刘琦, 25
    赵云, 32
    张飞, 43
    关羽, 45
'''
agelist = []
for line in ageTable.splitlines():
    nameage = line.replace('', '')
    if nameage != "":
        agelist.append(nameage)
g30 = []
l30 = []
for nameage in agelist:
    name, age = nameage.split(',')
    age = int(age)
    if age >= 30:
        g30.append(name)
    else:
        l30.append(name)
print("30以上")
print(g30)
print("30一下")
print(l30)
