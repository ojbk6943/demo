class Tiger:
    classname = 'tiger'        #静态属性

    #__init__函数为实例方法
    def __init__(self, weight=200):         #weiht为实例属性
        print('haha, in __init__')
        self.weight = weight

    #实例方法
    def roar(self):
        print('self wow!!!')
        print(self.weight)

    @staticmethod
    def roar2():
        print('wow!!!')

    @staticmethod
    def roar3():
        print(Tiger.classname)

t1 = Tiger(3000)
# print(t1.weight)
# print(t1.classname)
print(t1.roar3())
# t1.roar()
# t1.roar2()
# t1.roar3()