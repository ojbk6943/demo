# Python文件读写
#
# 请定义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数.
# mySort 函数需要将参数列表中的元素按从小到大排序，最终返回一个新的list。
#
# 请按下面算法的思路实现函数：
#
# 1. 创建一个新的列表newList
# 2. 先找出所有元素中最小的，append在newList里面
# 3. 再找出剩余的所有元素中最小的，append在newList里面
# 4. 依次类推，直到所有的元素都放到newList里面

def sort(inList):
    newList = []

    # 设计一个循环，每个循环做如下事情（直到 inlist 没有元素）：
    #     找出当前inlist中所有元素中最小curMin的，append在newList里面
    #
    #     inList 去掉 curMin

    while len(inList) > 0:
        theMin = inList[0] # 记录当前循环最小元素
        minIdx = 0   # 记录当前最小元素的下标
        idx = 0      # 指向当前元素下标
        for one in inList:
            if theMin > one:
                theMin = one
                minIdx = idx

            idx += 1

        inList.pop(minIdx)
        newList.append(theMin)

    return newList

print (sort([1,3,5,7,34,23,55,56,2,3,4]))