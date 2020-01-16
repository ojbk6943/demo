# *args 和 **kw
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 以及调用函数时如何传入可变参数和关键字参数的语法：
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。


#在python中定义函数，可以用必填参数、缺省参数、可变参数和关键字参数，这4中参数可以一起使用，或者只用其中某些，但是请注意，
# 参数定义的顺序应该是：必填参数、缺省参数、可变参数和关键字可变参数

def register_student(name,age,**kargs):
    # print('name:',name,'age:',age,'other:',kargs)
    print(kargs)

#方式一：
register_student('augus',14,**{"area":'beijing',"emial":"11200287@qq.com"})

#方式二
# register_student('lrin',18,gender='m',job='Engineer')


# #可变参数
# def reg(username,password,*args):
#     print(args)
#
# reg("wangduoyu","3843848",[121,"sdfsdf","sdfs"])
