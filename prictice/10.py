ageTable = '''
    诸葛亮， 28
    刘备， 48
    刘琦， 25
    赵云， 32
    张飞， 43
    关羽， 45
'''
import re
p=re.compile(r'([\S]+)，(.+)', re.MULTILINE)
list1=p.findall(ageTable)
print(type(list1))
# for one in list1:
#     print (one)
print(list1)
source = '<html><head><title>Title</title>'

# import re
# # 注意多出的问号
# p = re.compile(r'<.*?>')
#
# print(p.findall(source))
# content = '''001-苹果价格-60
# 002-橙子价格-70
# 003-香蕉价格-80'''
#
# import re
# p = re.compile(r'价|格|蕉', re.M)
# # for one in  p.findall(content):
# #     print(one)
# print(p.findall(content))
# content = '''苹果，苹果是绿色的
# 橙子，橙子是橙色的
# 香蕉，香蕉是黄色的'''
#
# import re
# p = re.compile(r'^(.*)，', re.MULTILINE)
# # for one in  p.findall(content):
# #     print(one)
# # print(p.findall(content))
# content = '''张三，手机号码15945678901
# 李四，手机号码13945677701
# 王二，手机号码13845666901'''
#
# import re
# p = re.compile(r'^(.+)，(.+)(\d{11}$)', re.MULTILINE)
# # for one in  p.findall(content):
# #     print(one)
# print(p.findall(content))