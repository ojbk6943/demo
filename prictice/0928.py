# for i in range(10):
#     print(i+1)
room=["张","李","王","罗"]
# a=enumerate(room)
# print(a)
# # for b in enumerate(room):
# #     print(b)
# class Tiger:
#     def __init__(self):
#         self.name="王多余"
#         self.weight = 5
#
#     def ford(self):
#         self.name="王多余+1"
#         self.weight-=1
# print(Tiger().weight)

# class Sheep:
#     classname = 'sheep'
#     def __init__(self):
#         self.weight = 5
#
#     def roar(self):
#         print('mie~~')
#         self.weight -= 1
#         # print(self.weight)
# print(Sheep().weight)
# Sheep().roar()
# # print(Sheep.classname)
# # # print(Sheep().weight)
# class Sheep:
#     classname = 'sheep'
#     def __init__(self,weight=100):
#         self.weight = weight
#
#     def roar(self):
#         print('mie~~')
#         self.weight -= 5
#
#     def feed(self,food):
#         if food == 'grass':
#             self.weight += 10
#             print('正确，体重 + 10')
#         else :
#             self.weight -= 10
#             print('太惨了，体重 - 10')
# s=Sheep()
# s.roar()
# s.feed("grass")
# print(s.weight)
# # Sheep().roar()
# # print(Sheep().weight)
import re

names = '关羽; 张飞, 赵云,   马超, 黄忠  诸葛亮'

namelist = re.split(r'[;,\s]\s*', names)
print(namelist)
# '关羽; 张飞, 赵云,   马超, 黄忠  诸葛亮'