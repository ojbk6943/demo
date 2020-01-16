def loop(a):
    b=list(a)                         #将参数转为列表
    newlist=[]
    le=b.__len__()                    #计算列表长度
    for i in range(0,le-1):           #利用冒泡排序从小到大排序生成新列表
        for j in range(0,le-i-1):
            if int(b[j])>int(b[j+1]):
                temp=b[j]
                b[j]=b[j+1]
                b[j+1]=temp
    # print(b)
    for one in b:                      #每次找到最小的元素添加到newlist
        newlist.append(one)
    print(newlist)
loop([234,3425,3425,2,435,243,246,24362,643])



