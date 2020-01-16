#捕获多种异常类型，加多个except
try:
    hello
    b = 4396/0
    print('谁知道4396这个梗请举手!!!')
except ZeroDivisionError:       #指定捕获错误的类型
    print('错误类型：ZeroDivisionError')
except NameError as a :
    print("错误类型：NameError")
    print(a)

print('代码执行结尾处')
