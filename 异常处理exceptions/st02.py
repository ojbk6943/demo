def f3():
    try:
        print('in f3 - start')
        b = 4/0
        print('in f3 - end')
    except:
        print("!!!")
        raise
def f2():
    try:
        print('in f2 - start')
        f3()
        print('in f2 - end')
    except:
        print("***")
        raise
def f1():
    try:
        print('in f1 - start')
        f2()
        print('in f1 - end')
    except:
        print('@@@@')
# def f1():
#     print('in f1 - begin')
#     f2()
#     print('in f1 - end')

f1()
print('底部')



    

    
    
    
        

    