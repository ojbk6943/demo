height = float(input("请输入你的身高(单位米):"))
bodyWeight = float(input("请输入你的体重(单位公斤):"))
age = int(input("请输入你的年龄:"))
if age>=60:
    print("60岁以上老人不参与健康评估")
elif 60>age>=10:
    if bodyWeight/(height**2) > 24:
        print("您的体重超重")
    elif bodyWeight/(height**2) < 18:
        print("您的体重太轻")
    else:
        print("您的体重正常")
else:
    print("10岁以下儿童不参与健康评估")
