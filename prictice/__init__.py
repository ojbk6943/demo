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
list1=str1.split("\n" )                        #先把str1中的\n去掉
#print(list1)
list1a=[one for one in list1 if one != ""]     # 把list1列表中的空格去掉
#print (list1a)
s1=set(list1a)                                 #把list1a转换为集合
#print (s1)

list2aa=[]
list2=str2.split("\n" )                        #先把str2中的\n去掉
#print(list2)
list2a=[one for one in list2 if one != ""]     #把list2列表中的空格去掉
for one in list2a:                             #把list2a列表中每一个字符串前后的空格删掉
    n=one.strip()
    list2aa.append(n)
#print(list2aa)

s2=set(list2aa)                                 #把list2a转换为集合
#print (s2)
a=s1-s2                                        #求两个集合的差集，所得集合元素在s1中不在s2中
print ('存在于str1中，而不存在于str2中的元素有：{}'.format(a))
b=s2-s1                                        #求两个集合的差集，所得集合元素在s2中不在s1中
print('存在于str2中，而不存在于str1中的元素有：{}'.format(b))