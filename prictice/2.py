var1 = [ 33, ('我的名字', 'Augus'), 'hello world!']
#请接下来写一行代码， 修改var1这个列表变量里面的 人名字 Augus 为 酒剑仙

list1=list(var1[1])
#print(list1)
list1[1]="酒剑仙"
#print(list1)
tuple=tuple(list1)
#print(tuple)
var1.remove(('我的名字', 'Augus'))
#print(var1)
var1.insert(1,tuple)
print(var1)
list7=dict()
print(type(list7))
