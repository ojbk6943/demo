class Tiger:
    classname = 'tiger'    #静态属性

    #实例方法
    def __init__(self, weight=200):       #weight实例属性
        self.weight = weight

    def tellWeight(self):
        print(f'my weight is {self.weight}')

    @staticmethod             #静态方法
    def roar():
        print('wow!!!')

    @staticmethod          #静态方法
    def roar2():
        print(Tiger.classname)


t1 = Tiger(300)     #将tiger这个类实例化，返回给T1
t2 = Tiger(100)

t1.roar()
t1.roar2()
t1.tellWeight()

t2.roar()
t2.roar2()
t2.tellWeight()



# Tiger.tellWeight()
# Tiger.tellWeight(t1)