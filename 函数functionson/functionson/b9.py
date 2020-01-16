# def add():
#     sum = 0
#     for one in range(101):
#         sum += one
#     return sum
#
# a = add()
# print(a)


def add(i):
    if i == 0:
        return i
    return i+add(i-1)

a  = add(238823)
print(a)

