class Tiger:
    classname = 'tiger'

    def __init__(self, weight=200):
        self.weight = weight


    @staticmethod       #静态方法
    def roar():
        print('wow!!!')

    @classmethod        #类方法
    def roar2(cls, para1):
        print(cls)
        print(cls.classname)


t1 = Tiger(200)

t1.roar2('hello')
# Tiger.roar2('hello')

