#定义函数，但是不会执行
def foo(a1,b1):
    print(a1,b1)
    global a
    a = 3
    global b
    b = 4
    print( a,b)
#定义两个变量a,b
a = 1
b = 2
foo(a,b)

print(a,b)