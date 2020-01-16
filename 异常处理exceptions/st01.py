import traceback
def foo3():
    try:
        print('foo3 * start')
        b = 4/0
        print('foo3 * end')
    except :
        print("出错了！！！",traceback.format_exc())
        raise
def foo2():
    print('foo2 * start')
    foo3()
    print('foo2 * end')

def foo1():
    print('foo1 * start')
    foo2()
    print('foo1 * end')

foo1()
print('代码底部')



    

    
    
    
        

    