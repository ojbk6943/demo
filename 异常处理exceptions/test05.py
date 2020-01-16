try:
    4396/0
    hello
except Exception as e:     #指定捕获所有类型的异常
    print('异常原因：', e)

print('文件代码结尾执行输出')