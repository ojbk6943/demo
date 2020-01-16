try:
    jhjj
    print('helloword')
except ZeroDivisionError:
    print('handle ZeroDivisionError')
except NameError:
    print('handle NameError')
except :
    print('handle unkown exeption')
#else 指定没有异常的情况下，执行的一段代码，在finally前面
else:
    print('哈哈哈, no exception！！！')
finally:
    print('finally指定代码一定要执行')



