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
#循环遍历一个列表，
for one in nba_ages:
    #分别取出姓名和年龄
    name = one[0]
    age  = one[1]
    print(name, age)
    if name == 'Lebron James':
        continue
        print('!!!!!!!!!! 找到了, james年龄是 %d' % age)
    p


