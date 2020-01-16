list2 = [45,67,34,23,12,56]
list1 = []
# for one in list2:
#     if one > 40 :
#         print(one)
#         list1.append(one)
#     else:
#         pass
# print(list1)


list1 = [i for i in list2 if i > 40]
print (list1)
