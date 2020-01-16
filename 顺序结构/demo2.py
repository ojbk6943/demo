results = int(input("请输入你的成绩："))

if results >= 90:
    print("你的成绩很优秀")
elif  90 > results >= 70:
    print("你的成绩良好")
elif 70 > results >= 60:
    print("成绩合格")
else:
    print("很遗憾，成绩不合格，继续努力哦")