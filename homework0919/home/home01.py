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

#将str1中内容读取出来，splitlines()按照行('\r','\r\n',\n')分隔，返回一个包含各行作为元素的列表
def getNameList(nameStr):
    tmp = nameStr.splitlines()
    name_list = []
    for one in tmp:
        name = one.strip()         #使用strip方法去掉空格
        if name == "":
            continue          #做一个判断，如果中间没有值，则结束本次循环
        else:
            name_list.append(name)
    return name_list

#调用两次getNameList获取处理过的人名字列表
names1 = getNameList(str1)
names2 = getNameList(str2)

#新建一个列表，用来保存str1不再str2中的人名字
# str1_not_in_str2 = []
# for name in names1:
#     if name not in names2:
#         str1_not_in_str2.append(name)
# print(str1_not_in_str2)

#新建一个列表，用来保存str2 中所有 str1 中不存在的人名
str2_not_in_str1 = []
for name in names2:
    if name not in names1:
        str2_not_in_str1.append(name)

print(str2_not_in_str1)
