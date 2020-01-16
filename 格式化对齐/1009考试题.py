# # 有一个数据文件 qi.txt， 内容格式如下（12分）:
#     qi.txt='''薛蟠     4560 42
#     薛蝌     4460 25
#     薛宝钗   5776 43
#     薛宝琴   4346 42
#     王夫人   3360 25
#     王熙凤   4460 35
#     王子腾   5660 45
#     王仁     5034 65
#     尤二姐   5324 25
#     贾芹   5663 25
#     贾蓉     3446 15
#     贾兰     3443 35
#     贾芸     4522 25
#     尤三姐   5905 45
#     贾珍     4603 25'''
# # 这里面有3列数据，分别 保存了 游戏系统的用户名， 用户积分 ， 年龄要求大家写一个程序，读取内容并计算出同一姓氏的人的积分总和。输出结果格式如下：
# '''
# 薛 : 19142
# 王 : 18514
# 尤 : 11229
# 贾 : 21677
# '''
with open('qi_1.txt',encoding='utf8') as f:
    infoList = f.read().splitlines()
coinTable = {}         #创建积分的字典
for info in infoList:
    # 先去除左右空白字符
    info = info.strip()
   if not info:     #如果元素是空，则跳过不处理，继续遍历下一个元素
        continue
    parts = info.split(' ')
    name = parts[0]
   coin = int(parts[-2])
    # 如果姓氏还没有在统计表中
    # 创建新元素
    if name[0] not in coinTable:
       coinTable[name[0]] = coin
   # 如果姓氏已经在统计表中
   # 累加积分
    else:
     coinTable[name[0]] += coin
for name1,coins in coinTable.items():     #.items函数以列表的形式返回可遍历的（键，值）元组数组
   print(f'{name1} : {coins}')