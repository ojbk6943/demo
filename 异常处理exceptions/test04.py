try:
    word
except NameError as a:       #捕获后得到详细的异常信息 ,a就是异常对象
    print(type(a))
    print('handle NameError:', a)

