#'A girl come in, the name is Jack, level 955;'

# def getName(srcStr):
#     a = srcStr
#     n = a.split(",")[1]
#     b = n.split("is")[1]
#     return b
# print(getName('A girl come in, the name is Jack, level 955;'))

def getName(srcStr):
    a = srcStr
    n = a.split(",")[1]
    b = n.split("is")[1]
    print (b)
    return b
getName('A girl come in, the name is 爷爷, level 955;')