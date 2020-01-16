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

#把字符串1转换为列表1
list1 = str1.split("\n")
#print(list1)
one = ""
while one in list1:
    list1.remove("")
    #print(list1)
#print(list1)

#把列表1转换为集合1
set1 = set(list1)
#print(set1)

#把字符串2转换为列表2
list2 = str2.split("\n")
#print(list2)
while one in list2:
    list2.remove("")
    #print(list1)
#print(list2)

#把列表2转换为集合2
set2 = set(list2)
#print(set2)

#找出str1中所有str2中不存在的人名
a = set1 - set2
#print(f"str1中所有str2中不存在的人名为{a}")

#找出str2中所有str1中不存在的人名
b = set2 - set1
print(f"str2中所有str1中不存在的人名为{b}")