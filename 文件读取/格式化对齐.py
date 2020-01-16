# print("学号\t姓名\t语文\t数学\t英语")
# print("2017001\t曹操\t99\t\t88\t\t0")
# print("2017002\t周瑜\t92\t\t45\t\t93")
# print("2017008\t黄盖\t77\t\t82\t\t100")
# print('{:^9}\t'.format("ii"),end = '')  # 采用居中对齐 左图
# # print('{:<9}\t'.format(ii),end = '')  # 采用左对齐 右图
#
# print('{:5s} and {:>15s}'.format('hello','world'))  # 取10位左对齐，取10位右对齐
#  4 hello      and      world
# print('{:^50s} and {:^50s}'.format('hello','world'))  # 取10位中间对齐
#  6   hello    and   world
# print('{} is {:.1f}'.format(1.123,1.123))  # 取2位小数
#  8 1.123 is 1.12
print('{0} is {0:>10.2f}'.format(1.123))  # 取2位小数，右对齐，取10位
# 10 1.123 is       1.12
