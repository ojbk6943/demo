var = 'Hello world！'
a=var.count("l")
b=var.capitalize()
c=var.center(50, 'x')
d=var.find('j')
e=var.replace('l','k',1)
f=var.istitle()
print(f)
print(e)
print(d)
print(c)
print(b)
print(len(var))
print(var[2::2])
print(var[::-1])
list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2
list1.extend(list2)
print(list1)
del list3[0]
print(list3)
list2.insert(1,7)
print(list2)
list1.reverse()
print(list1)
list1.sort()
print(list1)
tup1 = ('哈哈',2,'safe',['1',2,4])
# tup1[2] = 3
# tup[3][1] = 'a'
print(tup1[1])
dict1=dict()
print(type(dict1))

dict4=dict1.fromkeys(list1,2)
print(dict4)
ll=dict4.keys()
print(ll)
dict5=dict4.copy()
print(dict5)