#定义一个列表。列表中每个元素用元组来存放
nba_ages = [
    ('Mike Jordan',19),
    ('Jason Kid',18),
    ('Korby Briant',16),
    ('Lebron James',26),
    ('Korby Briant4',16),
    ('Korby Briant5',16),
    ('Korby Briant6',16),
    ('Korby Briant7',16),
    ('Korby Briant7', 16),
    ('Korby Briant8',16),
    ('Korby Briant9',16),
    ('Korby Briantk',16)
]

for one in nba_ages:
    name = one[0]
    age = one[1]
    print (name)
    # if name == "Lebron James":
    #     # print("找到了%s,年龄%d" % (name,age))
    #     # print("找到了{},年龄{}".format(name,age))
    #     print(f"找到了{name},年龄{age}")
    #     break
    # print("********************")






# #循环取出列表的元素
# for one in nba_ages:
#     #分别取每个元素，每个元素为一个元组，可按索引操作
#     name = one[0]         #取出名字
#     age  = one[1]         #取年龄
#     print(name,age)
#     if name == 'Lebron James':
#         print('!!!!!!!!!! 找到了, james年龄是 %d' % age)
