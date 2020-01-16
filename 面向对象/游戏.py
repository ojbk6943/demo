# coding=utf8
import random
number=random.randint(1,8)
print(number)
class Tiger:
    classname = 'tiger'
    def __init__(self,weight=200):
        self.weight = weight
    def roar(self):
        print('wow!!!')
        self.weight -= 5
    def feed(self,food):
        if food == 'meat':
            self.weight += 10
            print('good, weight + 10')
        else :
            self.weight -= 10
            print('bad, weight - 10')
class Sheep:
    classname = 'sheep'
    def __init__(self,weight=100):
        self.weight = weight
    def roar(self):
        print('mie!!!')
        self.weight -= 5
    def feed(self,food):
        if food == 'gress':
            self.weight += 10
            print('good, weight + 10')
        else :
            self.weight -= 10
            print('bad, weight - 10')

class Room:
    def __init__(self,num=number):
        self.num =
        self.animal = Tiger(300)

# action1=input('请输入你想要执行的操作,喂羊请输入"meet",喂羊请输入"gress",您的选择是：')
Animal().feed(action1)