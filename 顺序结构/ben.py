# print("你爱我吗")
# a=(1,2,3,4,5)
# for i in a:
#     print(i)
# sum=float(input("请输入一个数字："))
# if 100>=sum>=90:
#     print ("优秀")
# elif 90>sum>=80:
#     print ("良好")
# elif 80>sum>=70:
#     print ("一般")
# elif 70>sum>=60:
#     print("及格")
# elif 0<sum<60:
#     print ("不及格")
# else:
# #     print ("输入错误")
# a=float(input("请输入第一个数字："))
# b=float(input("请输入第二个数字："))
# if a>b:
#     print("第一个数大")
# elif a==b:
#     print("两个数相等")
# else:
#     print("第二个数大")
here=1
end=100
sum=0
while here <=end:
    sum+=here
    here+=1
print("sum=%d"%(sum),here)