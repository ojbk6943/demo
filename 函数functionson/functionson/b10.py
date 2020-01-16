# 1什么是递归：在一个函数里在调用这个函数本身
# 2.最大递归层数做了一个限制：997，但是也可以自己限制
# 3.递归效率不高，递归层次过多会导致栈溢出
def foo(n):
    print(n)
    n+=1
    foo(n)
foo(1)

# import sys
# sys.setrecursionlimit(997)  #修改递归层数
# n=0
# def f():
#     global n
#     n+=1
#     print(n)
#     f()
# f()