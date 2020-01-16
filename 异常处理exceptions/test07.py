try:
    badan
    b = 4/0
    print('hello')
except ZeroDivisionError:
    print('错误类型： ZeroDivisionError')
except NameError:
    print('错误类型： NameError')
except :
    print('handle unkown exeption')
#finally代码，指代，不管是否有异常，我们都执行要执行一段代码，必须放在最后
finally:
    print('finally指定一定要执行的代码')



