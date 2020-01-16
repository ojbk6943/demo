def calc(*numbers):    #*numbers是可变参数
    total = 0
    for n in numbers:
        total = total + n*n
    return total


td = calc(1,2,3)
print(td)
