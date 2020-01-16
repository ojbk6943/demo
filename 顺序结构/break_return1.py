nba_ages = [
    ('Mike Jordan', 19),
    ('Jason Kid', 18),
    ('Lebron James', 26),
    ('Korby Briant', 16),
]

idx = 0
flag = True
while flag:  # 这段代码为什么是个死循环
    current = nba_ages[idx]
    name = current[0]
    age = current[1]
    print(name, age)
    if name == 'Lebron James':
        print('!!!!!!!!!! 找到了, james年龄是 %d' % age)
        flag = False
    idx += 1

