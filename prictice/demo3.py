class Dog:
    classname = 'dog!!!'

    @staticmethod
    def roar():
        print('wang!!!')

    @staticmethod
    def roar2():
        print(Dog.classname)

g1 = Dog()
print(g1.classname)
g1.roar2()