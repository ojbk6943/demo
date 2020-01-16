var1 = [ 33, ('我的名字', 'Augus'), 'hello world!']
#请接下来写一行代码， 修改var1这个列表变量里面的 人名字 Augus 为 酒剑仙

#把元组转换为列表
list1 = list(var1)

#修改列表中第二个元素
a = list1[1]
b = list(a)
b[1] = "酒剑仙"
#print(b)

#把修改后的元素加入列表
list1.remove(a)      #移除
list1.insert(1, b)   #添加
print(list1)