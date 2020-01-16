# from random import randint  #或者使用 import random
import random

import time

class Tiger:      #(object)
    classname = 'tiger'

    def __init__(self,weight=200):
        self.weight = weight

    def roar(self):
        print('wow!!!')
        self.weight -= 5


    def feed(self,food):
        if food == 'meat':
            self.weight += 10
            print('正确，体重 + 10')
        else :
            self.weight -= 10
            print('太惨了，体重 - 10')


class Sheep:
    classname = 'sheep'
    def __init__(self,weight=100):
        self.weight = weight

    def roar(self):
        print('mie~~')
        self.weight -= 5

    def feed(self,food):
        if food == 'grass':
            self.weight += 10
            print('正确，体重 + 10')
        else :
            self.weight -= 10
            print('太惨了，体重 - 10')


class Room:
    def __init__(self,num,animal):
        self.num = num
        self.animal = animal


rooms = []
for no in range(10):
    if random.randint(0,1):      #随机产生0或者1
        ani = Tiger(200)
    else:
        ani = Sheep(100)

    room = Room(no,ani)

    rooms.append(room)
# print("****************")
# print(rooms)
# print("****************")
startTime = time.time()       #获取当前时间
while True:
    curTime = time.time()
    if (curTime - startTime) > 10:
        print('\n\n **********  游戏结束 ********** \n\n')
        for idx, room in enumerate(rooms):          #enumerate() 方法返回下标和元素
            print('房间 :%s' % (idx + 1), room.animal.classname, room.animal.weight)
        break

    roomno = random.randint(1, 10)
    room = rooms[roomno-1]  # why -1 ?
    ch = input('我们来到了房间# %s, 要敲门吗?[y/n]' % roomno)
    if ch == 'y':  #判断是否要动物叫
        room.animal.roar()

    food = input('请给房间里面的动物喂食:')
    room.animal.feed(food.strip())
