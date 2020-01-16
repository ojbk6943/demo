try:
    hello
    b = 4396/0
except ZeroDivisionError:
    print('错误类型： ZeroDivisionError')
except NameError:
    print('handle NameError')

print('结尾处')