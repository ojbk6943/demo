#traceback模块中的format_exc()方法用来获取详细错误信息，如果直接写except：要看详细信息必须使用traceback.format_exc()
import traceback

try:
    test
except :         #捕获所有异常的简写,但是不知道异常的信息
    print('handle unkown exeption\n' +
          traceback.format_exc())


