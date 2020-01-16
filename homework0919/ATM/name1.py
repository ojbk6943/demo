str1 = '''
熊宁
杰益

王伟伟

青芳

玉琴
焦候涛
莫福
杨高旺
唐欢欢
韩旭
'''
str2 = '''
焦候涛 
熊宁 
玉琴 

骆龙 

韩旭 
杨高旺

杰益  

莫福  

伟伟

李福  
'''


# 从Str1 和Str2中取出每个人的名字
def nameyang(nameStr):
    names = []
    # 从字符串中去除空行
    lineList = nameStr.splitlines()
    for line in lineList:
        name = line.strip()
        if name != "":
            names.append(name)
    return names


names1 = nameyang(str1)
names2 = nameyang(str2)
# 从names1中取每一个人名
print("2中不存在")
for name in names1:
    if name not in names2:
        print(name)
print("1中不存在")
for name in names2:
    if name not in names1:
        print(name)



