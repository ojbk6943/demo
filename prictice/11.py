# def loop(q,**args):
#
#     print(q,**args)
#     # print(a)
#
# # loop(3,6)
# for one in range(0,11,5):
#     print(one)
#     print("***************")
# print("kfds")+print("12434")

# def test(a,b,c=3,*args):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
# # test(11,22,33,44,55)
# def test(a,b,c=3,*args1,**args2):
#     print(a)
#     print(b)
#     print(c)
#     print(args1)
#     print(args2)
# test(11,22,33,dd=44,ee=55,ff=66)
# def loop(a,b=3):
#     c=a+b
#     print(c)
# loop(6)
# class Tiger:
#     'a tiger class,which is used in this game as tiger.'
#     classname = 'tiger'
#     def roar(self):
#         print('Wow!!')
# tiger1 = Tiger()
# tiger2 = Tiger()
# print(tiger1.classname)
# print(tiger2.classname)
# tiger1.roar()
# class Tiger:
#     classname = 'tiger'
#
#     def __init__(self, weight=200):
#         self.weighe = weight
#
# tiger1=Tiger()
# # print(tiger1.weighe)
# from random import randint
# # # print(randint(0,1))
# # # # print(randint(1,10))
# # info = [
# #     ['user1', 345.6, 12, '黄金'],
# #     ['user2', 2345.6, 8, '白银'],
# #     ['user3555', 55345.6, 22, '钻石'],
# # ]
# # for one in info:
# #     # dict1={'用户':one[0],'积分':one[1],'等级':one[2],'头衔':one[3]}
# #     print(f'"用户：{one[0]}","积分：{one[1]}","等级：{one[2]}","头衔：{one[3]}"')
# ageTable = '''
#     诸葛亮, 28
#     刘备, 48
#     刘琦, 25
#     赵云, 32
#     张飞, 43
#     关羽, 45
# '''
# # import re
# # # p=re.compile(r'([^\s]+),(.+)',re.M)
# # # a=p.findall(ageTable)
# # # print(a)
# # # b=[one for one in a if int(one[1])>=30]
# # # print(b)
# # a='1111'.isalpha()
# # print(a)
info = [
    ['user1', 345.6, 12, '黄金'],
    ['user2', 2345.6, 8, '白银'],
    ['user3555', 55345.6, 22, '钻石'],
]
i=dict()
print(type(i))
for one in info:
    i={'用户名':one[0],'积分':one[1],'等级':one[2],'头衔':one[3],}
    print(i)
# i=dict()
# i={'用户名':1,'积分':2,'等级':3,'头衔':4,}
#
# i={'用户名':2,'积分':2,'等级':2,'头衔':2,}
# print(i)
list1=tuple()
list1=(2,3,4,5,5,4,4,2)
list1=(2,3,4,5,5,4,4,9)

print(list1)
